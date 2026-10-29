"""Preview-bound, append-only delivery documents. No network or command execution."""

from __future__ import annotations

import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "apex-as.delivery-brief/v1"
STATE = "apex-as.delivery-state/v1"
EVENTS = "apex-as.delivery-events/v1"
STAGES = [f"D{i}" for i in range(7)]
IDS = [f"ART-{i:02}" for i in range(1, 9)]
MAX_BYTES = 256_000
ROLE_NAMES = {
    "delivery_lead", "specialist", "architect", "migration_lead",
    "executor", "test_owner", "operations_owner", "customer_owner", "platform_owner",
}


class DeliveryError(ValueError):
    """A bounded input, state or authorization failure."""


def fail(message):
    raise DeliveryError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n").encode()


def keys(value, required, optional=()):
    if not isinstance(value, dict):
        fail("INCOMPATIBLE: expected an object")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        fail(f"INCOMPATIBLE: missing fields {sorted(missing)}; unknown fields {sorted(extra)}")


def text(value, field):
    if not isinstance(value, str) or not value.strip() or len(value) > 16_000:
        fail(f"INCOMPATIBLE: {field} must be a nonempty string, at most 16000 characters")
    return value


def identifier(value, field):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z][a-z0-9-]{1,63}", value):
        fail(f"INCOMPATIBLE: {field} must be a lowercase opaque identifier")
    return value


def unique_strings(value, field, choices=None):
    if not isinstance(value, list) or not value or any(not isinstance(v, str) for v in value):
        fail(f"INCOMPATIBLE: {field} must be a nonempty string array")
    if len(set(value)) != len(value):
        fail(f"INCOMPATIBLE: duplicate {field}")
    for v in value:
        text(v, field)
    if choices is not None and not set(value) <= set(choices):
        fail(f"INCOMPATIBLE: unsupported {field}")
    return value


def checked_path(path, *, directory=False):
    path = Path(path)
    if not path.is_absolute():
        fail("BLOCKED: use an explicit absolute path")
    if ".." in path.parts or str(path).startswith(("\\\\", "//")):
        fail("BLOCKED: traversal and network/device paths are not supported")
    for part in [*reversed(path.parents), path]:
        if part.exists() or part.is_symlink():
            info = part.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                fail("BLOCKED: symlink/junction/reparse path is not permitted")
    if directory and not path.is_dir():
        fail("BLOCKED: explicitly selected root directory must already exist")
    return path


def contained(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        fail("BLOCKED: use a plain relative source path")
    parts = relative.split("/")
    if any(p in ("", ".", "..") or p.startswith(".") for p in parts):
        fail("BLOCKED: source traversal/hidden paths are not permitted")
    if any(p.casefold() == "00-session-state.json" for p in parts):
        fail("BLOCKED: direct core session-state access is not supported")
    path = checked_path(root.joinpath(*parts))
    if not path.is_relative_to(root):
        fail("BLOCKED: source escaped its authorized root")
    return path


def read_bytes(path):
    path = checked_path(path)
    if not path.is_file():
        fail("MISSING INPUT: selected file does not exist")
    if path.stat().st_size > MAX_BYTES:
        fail("BLOCKED: input exceeds 256000 bytes")
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        fail("BLOCKED: input changed size during read")
    return data


def no_duplicate_keys(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            fail(f"INCOMPATIBLE: duplicate JSON key {key}")
        value[key] = item
    return value


def load_json(path):
    try:
        return json.loads(read_bytes(path).decode("utf-8"), object_pairs_hook=no_duplicate_keys)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise DeliveryError("INCOMPATIBLE: expected valid UTF-8 JSON") from error


def brief_at(path):
    brief = load_json(path)
    keys(brief, ("contract", "synthetic", "project_id", "title", "lanes",
                 "environments", "roles", "alz", "inputs", "sources"), ("lane_inputs",))
    if brief["contract"] != CONTRACT or brief["synthetic"] is not True:
        fail("INCOMPATIBLE: only delivery-brief/v1 synthetic examples are enabled")
    identifier(brief["project_id"], "project_id")
    text(brief["title"], "title")
    unique_strings(brief["lanes"], "lanes", ("infrastructure", "database"))
    unique_strings(brief["environments"], "environments")
    roles = brief["roles"]
    keys(roles, (), ROLE_NAMES)
    for role, value in roles.items():
        text(value, role)
    keys(brief["alz"], ("ownership", "owner", "status"))
    if brief["alz"]["ownership"] not in ("external", "partner", "unknown"):
        fail("INCOMPATIBLE: ALZ ownership")
    if brief["alz"]["status"] not in ("pending", "supplied", "unavailable"):
        fail("INCOMPATIBLE: ALZ input status")
    text(brief["alz"]["owner"], "ALZ owner")
    if not isinstance(brief["inputs"], dict):
        fail("INCOMPATIBLE: inputs must be an object of narrative strings")
    for key, value in brief["inputs"].items():
        identifier(key.replace("_", "-"), "input key")
        text(value, key)
    keys(brief.get("lane_inputs", {}), (), brief["lanes"])
    for lane, values in brief.get("lane_inputs", {}).items():
        if not isinstance(values, dict):
            fail("INCOMPATIBLE: lane inputs must be narrative objects")
        for key, value in values.items():
            identifier(key.replace("_", "-"), "lane input key")
            text(value, f"{lane} input")
    if not isinstance(brief["sources"], list):
        fail("INCOMPATIBLE: sources must be an array")
    seen = set()
    for source in brief["sources"]:
        keys(source, ("id", "path", "artifacts"))
        identifier(source["id"], "source ID")
        if source["id"] in seen:
            fail("INCOMPATIBLE: duplicate source ID")
        seen.add(source["id"])
        unique_strings(source["artifacts"], "source artifacts", IDS)
    return brief


def inert(value):
    """Render supplied text as literal quoted data, not Markdown links or HTML."""
    escaped = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for c in ("\\", "`", "*", "_", "[", "]", "(", ")", "#", "|", "!"):
        escaped = escaped.replace(c, "\\" + c)
    return "\n".join("> " + line for line in escaped.splitlines()) + "\n"


def guidance():
    return load_json(Path(__file__).with_name("guidance.json"))


def roots_for(inputs, documents, state):
    roots = [checked_path(p, directory=True) for p in (inputs, documents, state)]
    for i, first in enumerate(roots):
        for second in roots[i + 1:]:
            if first.is_relative_to(second) or second.is_relative_to(first):
                fail("BLOCKED: input, document and state roots must be disjoint")
    for output in roots[1:]:
        if output.is_relative_to(ROOT) or ROOT.is_relative_to(output):
            fail("BLOCKED: output/state roots must be outside the product source tree")
        if any(p.casefold() in ("agent-output", ".github", ".git") for p in output.parts):
            fail("BLOCKED: output/state root is a protected core/configuration location")
    return roots


def empty_state(project, documents):
    return {"contract": STATE, "project_id": project, "documents": str(documents),
            "sequence": 0, "artifacts": {}, "events": [], "previous": None}


def state_at(state_root, project, documents):
    folder = checked_path(state_root / project)
    if not folder.exists():
        return empty_state(project, documents), None
    if not folder.is_dir():
        fail("COLLISION: project state path is not a directory")
    children = list(folder.iterdir())
    if any(not re.fullmatch(r"r\d{6}\.json", p.name) for p in children):
        fail("BLOCKED: unknown state files or active/stale project lock; inspect manually")
    previous = None
    current = empty_state(project, documents)
    for sequence, path in enumerate(sorted(children), 1):
        if path.name != f"r{sequence:06}.json":
            fail("INCOMPATIBLE: noncontiguous state journal")
        record = load_json(path)
        keys(record, ("contract", "project_id", "documents", "sequence",
                      "artifacts", "events", "previous"))
        if (record["contract"] != STATE or record["project_id"] != project
                or type(record["sequence"]) is not int
                or record["documents"] != str(documents) or record["sequence"] != sequence
                or record["previous"] != previous):
            fail("INCOMPATIBLE: state identity, destination or journal chain mismatch")
        if not isinstance(record["artifacts"], dict) or not isinstance(record["events"], list):
            fail("INCOMPATIBLE: state collections")
        for artifact, item in record["artifacts"].items():
            if artifact not in IDS:
                fail("INCOMPATIBLE: unknown state artifact")
            keys(item, ("path", "revision", "sha256", "recipe", "dependencies", "project_id"))
            if (item["project_id"] != project or type(item["revision"]) is not int
                    or item["revision"] < 1 or not is_digest(item["sha256"])
                    or not is_digest(item["recipe"])
                    or not isinstance(item["dependencies"], dict)):
                fail("INCOMPATIBLE: artifact state metadata")
            if (not isinstance(item["path"], str)
                    or not re.fullmatch(rf"{project}/r\d{{6}}/{artifact}\.md", item["path"])):
                fail("BLOCKED: artifact state path is outside the revision layout")
            if (not set(item["dependencies"]) <= set(IDS)
                    or not all(is_digest(v) for v in item["dependencies"].values())):
                fail("INCOMPATIBLE: unknown artifact dependency")
            if any(IDS.index(dep) >= IDS.index(artifact) for dep in item["dependencies"]):
                fail("INCOMPATIBLE: journal has a forward/circular dependency")
        known_events = {}
        reviews = set()
        for event in record["events"]:
            validate_event(event)
            if event["artifact"] not in record["artifacts"]:
                fail("INCOMPATIBLE: journal event references an unknown artifact")
            if event["id"] in known_events:
                fail("INCOMPATIBLE: duplicate event ID in journal")
            known_events[event["id"]] = event
            binding = (event["artifact"], event["revision"], event["sha256"])
            if event["kind"] == "release" and binding not in reviews:
                fail("INCOMPATIBLE: journal release lacks an earlier exact-revision review")
            if event["kind"] == "review":
                reviews.add(binding)
        if record["events"][:len(current["events"])] != current["events"]:
            fail("INCOMPATIBLE: journal event history was rewritten")
        previous = digest(read_bytes(path))
        current = record
    return current, previous


def sources_at(brief, inputs):
    supported = {s["input_key"] for definition in guidance()["artifacts"]
                 for s in definition["sections"]}
    supplied = set(brief["inputs"])
    for values in brief.get("lane_inputs", {}).values():
        supplied.update(values)
    if supplied - supported:
        fail(f"INCOMPATIBLE: unsupported narrative keys {sorted(supplied - supported)}")
    result = []
    for source in brief["sources"]:
        path = contained(inputs, source["path"])
        if path.suffix.lower() not in (".md", ".txt", ".json"):
            fail("BLOCKED: only explicit narrative/JSON source files are supported")
        raw = read_bytes(path)
        try:
            content = raw.decode("utf-8")
        except UnicodeError as error:
            raise DeliveryError("INCOMPATIBLE: source is not UTF-8") from error
        result.append({**source, "sha256": digest(raw), "content": content})
    return result


def recipe_for(brief, definition, sources, guide):
    relevant = {section["input_key"] for section in definition["sections"]}
    base = {key: value for key, value in brief.items()
            if key not in ("inputs", "sources", "lane_inputs")}
    material = {
        "brief": base,
        "inputs": {k: v for k, v in brief["inputs"].items() if k in relevant},
        "lane_inputs": {lane: {k: v for k, v in values.items() if k in relevant}
                        for lane, values in brief.get("lane_inputs", {}).items()},
        "sources": [{k: v for k, v in s.items() if k != "content"}
                    for s in sources if definition["id"] in s["artifacts"]],
        "guidance": guide,
    }
    return digest(canonical(material))


def expected_recipe(brief, definition, sources, guide, statuses):
    recipe = recipe_for(brief, definition, sources, guide)
    if definition["id"] == "ART-08":
        fields = ("path", "revision", "sha256", "document", "freshness",
                  "execution", "customer", "release")
        index = {aid: {**{key: statuses[aid].get(key) for key in fields},
                       "records": statuses[aid].get("records", [])} for aid in IDS[:-1]}
        recipe = digest(canonical({"recipe": recipe, "index": index}))
    return recipe


def current_status(brief, guide, sources, state, documents):
    result = {}
    for definition in guide["artifacts"]:
        aid = definition["id"]
        item = state["artifacts"].get(aid)
        if item is None:
            result[aid] = {"document": "PLANNED", "freshness": "UNVERIFIED",
                           "execution": "NOT_RECORDED", "customer": "NOT_REQUESTED",
                           "release": "NOT_RELEASED", "actions": ["Create an authorized draft"]}
            continue
        raw = read_bytes(contained(documents, item["path"]))
        actual = digest(raw)
        reasons = []
        if actual != item["sha256"]:
            reasons.append("Document edited since last recorded revision")
        if expected_recipe(brief, definition, sources, guide, result) != item["recipe"]:
            reasons.append("Selected input or guidance changed")
        for dependency, snapshot in item["dependencies"].items():
            upstream = state["artifacts"].get(dependency)
            if (not upstream or digest(read_bytes(contained(documents, upstream["path"]))) != snapshot
                    or result[dependency]["freshness"] != "CURRENT"):
                reasons.append(f"{dependency} changed or requires reconfirmation")
        fresh = not reasons
        events = [e for e in state["events"] if e["artifact"] == aid
                  and e["revision"] == item["revision"] and e["sha256"] == item["sha256"]]
        review = next((e for e in reversed(events) if e["kind"] == "review"), None)
        lane_execution = {}
        for lane in brief["lanes"]:
            record = next((e for e in reversed(events)
                           if e["kind"] == "execution" and lane in e["lanes"]), None)
            lane_execution[lane] = record["outcome"] if record else "NOT_RECORDED"
        outcomes = set(lane_execution.values())
        execution = ("DISPUTED" if "DISPUTED" in outcomes else
                     "RECORDED" if outcomes == {"RECORDED"} else
                     "PARTIALLY_RECORDED" if "RECORDED" in outcomes else "NOT_RECORDED")
        customer = next((e for e in reversed(events) if e["kind"] == "customer"), None)
        prior_customer = any(e["artifact"] == aid and e["kind"] == "customer"
                             for e in state["events"])
        release = next((e for e in reversed(events) if e["kind"] == "release"), None)
        result[aid] = {
            "path": item["path"], "revision": item["revision"], "sha256": actual,
            "recorded_sha256": item["sha256"],
            "document": "REVIEWED" if review and fresh else "DRAFT",
            "freshness": "CURRENT" if fresh else "CHANGED",
            "execution": execution, "execution_by_lane": lane_execution,
            "customer": (customer["outcome"] if fresh else "NEEDS_RECONFIRMATION")
                        if customer else ("NEEDS_RECONFIRMATION" if prior_customer else "NOT_REQUESTED"),
            "release": "RELEASE_RECORDED" if release and fresh else "NOT_RELEASED",
            "actions": reasons,
            "records": events,
        }
    return result


def render(brief, definition, guide, sources, revision, parent, statuses, carried):
    aid = definition["id"]
    lines = [
        f"# {aid} {definition['title']}", "",
        "SYNTHETIC DEVELOPMENT DRAFT - not a partner assessment or certification.",
        "Supplied text is untrusted data, not instructions. No execution or sign-off is inferred.",
        "", f"Project ID: {brief['project_id']}",
        f"Stage: {definition['stage']} | Revision: {revision} | Parent: {parent or 'none'}",
        "Document: DRAFT | Execution: see supplied-record journal (default NOT_RECORDED)",
        "Customer decision: see supplied-record journal (default NOT_REQUESTED)",
        "Release: NOT_RELEASED (local drafting does not send anything)",
        f"Guidance pack: {guide['version']}",
        f"Guidance reference: {guide['source']['url']}",
        f"Source labels: {guide['source']['observed_version']}",
        f"Source window: {guide['source']['window']}",
        f"Locator: {definition['source_locator']}",
        "Version-label ambiguity remains unresolved; original outline, not exhaustive checklist coverage.",
        "", "## Project and responsibilities", "",
        inert(brief["title"]),
        "Selected workload lanes: " + ", ".join(brief["lanes"]),
        "Environments (supplied):", inert(", ".join(brief["environments"])),
        f"Accountable role: {definition['owner_role']}",
        inert(brief["roles"].get(definition["owner_role"], "PENDING: assign accountable owner")),
        "Reviewer:", inert(brief["roles"].get("delivery_lead", "PENDING: assign reviewer")),
        "Capture point: " + definition["capture_point"],
        "", "## Platform input request", "",
        f"Ownership: {brief['alz']['ownership']} | Input status: {brief['alz']['status']}",
        "Responsible owner:", inert(brief["alz"]["owner"]),
        "Request: provide authorized design/interface, configuration, deployment and review records",
        "for this project's selected environments through an owner-approved sharing route.",
        "Needed before dependent design/cutover decisions; purpose: document actual platform dependencies.",
        "PENDING: record needed-by date, sharing route, source revision and owner response.",
        "An external or unavailable platform source is an owner action, not an exemption or deployment command.",
        "No supplied platform metadata proves deployment or grants access.",
        "",
    ]
    if aid == "ART-01":
        lines += ["## Delivery artifact tasks", "",
                  "| ID | Stage | Artifact | Owner role | Capture point | Dependencies |",
                  "|---|---|---|---|---|---|"]
        for d in guide["artifacts"]:
            lines.append(f"| {d['id']} | {d['stage']} | {d['title']} | {d['owner_role']} | "
                         f"{d['capture_point']} | {', '.join(d['depends_on']) or 'none'} |")
        lines += ["", "Each task is OPEN until a practitioner records its actual work.",
                  "PENDING: agree task dates, reviewers and owner actions; no partner score.", ""]
    for lane in brief["lanes"]:
        lines += [f"## {lane.title()} delivery lane", "",
                  "Keep this lane's source baseline, target constraints, run results and decisions separate.", ""]
        for section in definition["sections"]:
            lane_value = brief.get("lane_inputs", {}).get(lane, {}).get(section["input_key"])
            supplied = lane_value if lane_value is not None else brief["inputs"].get(
                section["input_key"], f"PENDING: {definition['owner_role']} to supply {section['input_key']}")
            lines += [f"### {section['heading']}", "", section["prompt"], "",
                      "Supplied lane input:" if lane_value is not None else
                      "Shared project input (not lane-specific or verified by this tool):",
                      inert(supplied), ""]
    if aid in ("ART-05", "ART-06"):
        lines += ["## Actual event capture", "",
                  "| Lane | Run/test ID | Environment | Event time | Expected | Observed | Source | Owner |",
                  "|---|---|---|---|---|---|---|---|",
                  "| PENDING | PENDING | PENDING | PENDING | PENDING | NOT_RECORDED | PENDING | PENDING |",
                  "", "Only explicit synthetic event records populate the separate journal.",
                  "A plan, what-if, draft or successful file write is not a migration/test result.", ""]
    if aid in ("ART-06", "ART-07"):
        lines += ["## Customer decision request (draft - not sent)", "",
                  "Please review the identified project scope and current artifact revision, supplied",
                  "validation results and open actions. Record acceptance, rejection or requested changes",
                  "with the decision owner, date, exact revision and response reference.",
                  "Customer decision owner:",
                  inert(brief["roles"].get("customer_owner", "PENDING: identify decision owner")),
                  "No signature, response or customer decision has been generated.", ""]
    if aid == "ART-08":
        lines += ["## Current-revision delivery index (snapshot, not an audit submission)", "",
                  "| Artifact | Path | Revision | Document | Freshness | Execution | Customer | Release |",
                  "|---|---|---|---|---|---|---|---|"]
        for key in IDS[:-1]:
            value = statuses[key]
            lines.append(f"| {key} | {value.get('path', 'PENDING')} | {value.get('revision', '-')} | "
                         f"{value['document']} | {value['freshness']} | {value['execution']} | "
                         f"{value['customer']} | {value['release']} |")
            for record in value.get("records", []):
                lines += ["", f"Supplied synthetic {record['kind']} record for {key}:",
                          inert(json.dumps(record, sort_keys=True)), ""]
        lines += ["", "All unresolved actions remain open; recipient authorization is separate.",
                  "Sources are referenced, not copied into a handover package; nothing is sent.", ""]
    lines += ["## Selected source excerpts (literal supplied data)", ""]
    for source in sources:
        if aid in source["artifacts"]:
            lines += [f"Source ID: {source['id']} | SHA-256: {source['sha256']}",
                      inert(source["path"]), inert(source["content"]), ""]
    if carried:
        lines += ["## Prior practitioner content (literal carry-forward)", "",
                  "Preserved verbatim as quoted data; reconcile duplication before review.",
                  inert(carried), ""]
    lines += ["## Open owner actions", "",
              "- Resolve PENDING values and input access/ownership before dependent delivery work.",
              "- Independently review this original draft against actual project sources.",
              "- Capture real work and responses only at the actual event; no automatic sign-off.",
              "- Reconfirm affected review/acceptance after changes; preserve historical records.",
              "", "## Practitioner notes", "", "PENDING: add project-specific notes here.", ""]
    return "\n".join(lines).encode("utf-8")


def is_digest(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def validate_event(event):
    keys(event, ("id", "artifact", "kind", "actor", "at", "reference",
                 "revision", "sha256", "outcome", "lanes"), ("recipients",))
    identifier(event["id"], "event ID")
    if not isinstance(event["artifact"], str) or event["artifact"] not in IDS:
        fail("INCOMPATIBLE: invalid event artifact")
    if not isinstance(event["kind"], str) or event["kind"] not in (
            "execution", "review", "customer", "release"):
        fail("INCOMPATIBLE: unknown event kind")
    if type(event["revision"]) is not int or event["revision"] < 1 or not is_digest(event["sha256"]):
        fail("INCOMPATIBLE: invalid event revision/content digest")
    unique_strings(event["lanes"], "event lanes", ("infrastructure", "database"))
    text(event["actor"], "event actor")
    text(event["reference"], "event reference")
    if not event["reference"].startswith("synthetic:"):
        fail("BLOCKED: only synthetic event references are enabled")
    try:
        at = datetime.fromisoformat(event["at"])
    except (ValueError, TypeError) as error:
        raise DeliveryError("INCOMPATIBLE: event time must be ISO-8601 with timezone") from error
    if at.tzinfo is None:
        fail("INCOMPATIBLE: event time requires a timezone")
    allowed = {"execution": ("RECORDED", "DISPUTED"), "review": ("REVIEWED",),
               "customer": ("PENDING", "ACCEPTED", "REJECTED"),
               "release": ("RELEASE_RECORDED",)}
    if event["outcome"] not in allowed[event["kind"]]:
        fail("INCOMPATIBLE: event outcome does not match its kind")
    if event["kind"] == "execution" and event["artifact"] not in ("ART-05", "ART-06"):
        fail("INCOMPATIBLE: execution records belong to ART-05/06")
    if event["kind"] == "customer" and event["artifact"] not in ("ART-06", "ART-07", "ART-08"):
        fail("INCOMPATIBLE: customer decisions belong to ART-06/07/08")
    if event["kind"] == "release":
        if event["artifact"] not in ("ART-07", "ART-08"):
            fail("INCOMPATIBLE: release records belong to ART-07/08")
        unique_strings(event.get("recipients"), "release recipients")
    elif "recipients" in event:
        fail("INCOMPATIBLE: recipients apply only to release records")


def events_at(path, brief, state, statuses):
    batch = load_json(path)
    keys(batch, ("contract", "synthetic", "project_id", "records"))
    if (batch["contract"] != EVENTS or batch["synthetic"] is not True
            or batch["project_id"] != brief["project_id"]):
        fail("INCOMPATIBLE: event version, synthetic flag or project mismatch")
    if not isinstance(batch["records"], list) or not batch["records"]:
        fail("INCOMPATIBLE: supply a nonempty event record array")
    known = {e["id"]: e for e in state["events"]}
    accepted = []
    for event in batch["records"]:
        validate_event(event)
        if event["artifact"] not in state["artifacts"]:
            fail("INCOMPATIBLE: event references an uncreated artifact")
        if not set(event["lanes"]) <= set(brief["lanes"]):
            fail("INCOMPATIBLE: event lane is outside project scope")
        if event["kind"] != "execution" and set(event["lanes"]) != set(brief["lanes"]):
            fail("INCOMPATIBLE: document review/decision/release must cover selected document lanes")
        if event["id"] in known:
            if known[event["id"]] != event:
                fail("CONFLICT: event ID already has different immutable contents")
            continue
        item = statuses[event["artifact"]]
        if (type(event["revision"]) is not int or event["revision"] != item["revision"]
                or event["sha256"] != item["sha256"] or item["freshness"] != "CURRENT"):
            fail("STALE: event requires the exact current unedited artifact and dependencies")
        if event["kind"] == "release":
            if event["artifact"] not in ("ART-07", "ART-08") or item["document"] != "REVIEWED":
                fail("BLOCKED: release record requires previously reviewed ART-07/08")
        known[event["id"]] = event
        accepted.append(event)
    return accepted


def prepare(*, brief_path, inputs_root, documents_root, state_root,
            artifacts=None, events_path=None, carry_forward=()):
    inputs, documents, storage = roots_for(inputs_root, documents_root, state_root)
    brief_path = checked_path(brief_path)
    if not brief_path.is_relative_to(inputs):
        fail("BLOCKED: brief must be inside the explicit inputs root")
    brief = brief_at(brief_path)
    guide = guidance()
    sources = sources_at(brief, inputs)
    project = brief["project_id"]
    state, previous = state_at(storage, project, documents)
    old_state = json.loads(json.dumps(state))
    statuses = current_status(brief, guide, sources, state, documents)
    sequence = state["sequence"] + 1
    changes = []
    approved_events = []
    if events_path:
        if artifacts or carry_forward:
            fail("INCOMPATIBLE: event capture and document authoring are separate operations")
        events_path = checked_path(events_path)
        if not events_path.is_relative_to(inputs):
            fail("BLOCKED: event file must be inside the inputs root")
        approved_events = events_at(events_path, brief, state, statuses)
        state["events"].extend(approved_events)
    else:
        selected = artifacts if artifacts is not None else IDS
        unique_strings(list(selected), "selected artifacts", IDS)
        if not set(carry_forward) <= set(selected):
            fail("INCOMPATIBLE: carry-forward must refer to selected artifacts")
        for definition in guide["artifacts"]:
            aid = definition["id"]
            if aid not in selected:
                continue
            missing = set(definition["depends_on"]) - state["artifacts"].keys()
            if missing:
                fail(f"BLOCKED: {aid} requires draft dependencies {sorted(missing)}")
            dependencies = {}
            for key in definition["depends_on"]:
                if statuses[key]["freshness"] != "CURRENT":
                    fail(f"STALE: refresh {key} before {aid}")
                dependencies[key] = state["artifacts"][key]["sha256"]
            old = state["artifacts"].get(aid)
            recipe = expected_recipe(brief, definition, sources, guide, statuses)
            # ART-08 includes event-state in its snapshot, not only document bytes.
            if (old and old["recipe"] == recipe and old["dependencies"] == dependencies
                    and statuses[aid]["freshness"] == "CURRENT"):
                continue
            carried = ""
            old_raw = b""
            if old:
                old_raw = read_bytes(contained(documents, old["path"]))
                if digest(old_raw) != old["sha256"] and aid not in carry_forward:
                    fail(f"CONFLICT: {aid} has user edits; explicitly carry it forward")
                if aid in carry_forward:
                    carried = old_raw.decode("utf-8")
                elif "## Practitioner notes\n" in old_raw.decode("utf-8"):
                    carried = old_raw.decode("utf-8").split("## Practitioner notes\n", 1)[1]
            revision = old["revision"] + 1 if old else 1
            raw = render(brief, definition, guide, sources, revision,
                         old["path"] if old else None, statuses, carried)
            if len(raw) > MAX_BYTES:
                fail("BLOCKED: generated artifact exceeds 256000 bytes; reduce sources/carry-forward")
            relative = f"{project}/r{sequence:06}/{aid}.md"
            destination = contained(documents, relative)
            if destination.exists():
                fail("COLLISION: revision destination already exists")
            state["artifacts"][aid] = {
                "path": relative, "revision": revision, "sha256": digest(raw),
                "recipe": recipe, "dependencies": dependencies, "project_id": project,
            }
            had_customer = any(e["artifact"] == aid and e["kind"] == "customer"
                               for e in state["events"])
            statuses[aid] = {
                "path": relative, "revision": revision, "sha256": digest(raw),
                "document": "DRAFT", "freshness": "CURRENT", "execution": "NOT_RECORDED",
                "customer": "NEEDS_RECONFIRMATION" if had_customer else "NOT_REQUESTED",
                "release": "NOT_RELEASED", "actions": [],
            }
            changes.append({"path": relative, "content": raw.decode("utf-8"),
                            "diff": "".join(difflib.unified_diff(
                                old_raw.decode("utf-8").splitlines(True),
                                raw.decode("utf-8").splitlines(True),
                                fromfile=old["path"] if old else "/dev/null", tofile=relative))})
    changed = bool(changes or approved_events)
    if changed:
        state["sequence"] = sequence
        state["previous"] = previous
        if len(canonical(state)) > MAX_BYTES:
            fail("BLOCKED: journal snapshot exceeds 256000 bytes; reduce event/input volume")
    preview = {
        "contract": "apex-as.delivery-preview/v1", "project_id": project,
        "synthetic": True, "documents_root": str(documents), "state_root": str(storage),
        "brief_sha256": digest(read_bytes(brief_path)),
        "changes": changes, "new_events": approved_events,
        "state_path": f"{project}/r{sequence:06}.json" if changed else None,
        "state": state,
        "prior_state": digest(canonical(old_state)),
        "source_fingerprints": [{k: v for k, v in s.items() if k != "content"} for s in sources],
        "statuses_before": current_status(brief, guide, sources, old_state, documents),
    }
    if events_path:
        preview["events_sha256"] = digest(read_bytes(events_path))
    guard_paths = [brief_path, Path(__file__).with_name("guidance.json")]
    guard_paths += [contained(inputs, s["path"]) for s in sources]
    guard_paths += [contained(documents, a["path"]) for a in old_state["artifacts"].values()]
    guard_paths += sorted((storage / project).glob("r*.json"))
    if events_path:
        guard_paths.append(events_path)
    preview["guards"] = [{"path": str(p), "sha256": digest(read_bytes(p))}
                         for p in guard_paths]
    preview["approval"] = digest(canonical(preview))
    return preview


def apply(preview, approval):
    material = {key: value for key, value in preview.items() if key != "approval"}
    if digest(canonical(material)) != preview["approval"]:
        fail("NOT AUTHORIZED: preview contents changed")
    if approval != preview["approval"]:
        fail("NOT AUTHORIZED: digest differs from the current preview; preview again")
    for guard in preview["guards"]:
        if digest(read_bytes(Path(guard["path"]))) != guard["sha256"]:
            fail("CONFLICT: an input, document or state changed after preview")
    if not preview["state_path"]:
        return {"outcome": "unchanged", "project_id": preview["project_id"], "created": []}
    documents = checked_path(Path(preview["documents_root"]), directory=True)
    storage = checked_path(Path(preview["state_root"]), directory=True)
    project = preview["project_id"]
    state_folder = checked_path(storage / project)
    created_dirs = []
    created_files = []
    lock = state_folder / "writer.lock"
    acquired = False
    try:
        if not state_folder.exists():
            state_folder.mkdir()
            created_dirs.append(state_folder)
        with lock.open("xb") as handle:
            handle.write(b"APEX AS local writer; do not remove a live lock\n")
        acquired = True
        # A concurrent writer after prepare must not be overwritten.
        journal = [p for p in state_folder.iterdir() if p.name != "writer.lock"]
        if len(journal) != preview["state"]["sequence"] - 1:
            fail("CONFLICT: state changed after preview")
        target_state = contained(storage, preview["state_path"])
        if target_state.exists():
            fail("COLLISION: journal destination already exists")
        for change in preview["changes"]:
            destination = contained(documents, change["path"])
            for directory in (destination.parent.parent, destination.parent):
                if not directory.exists():
                    directory.mkdir()
                    created_dirs.append(directory)
                checked_path(directory, directory=True)
            with destination.open("xb") as handle:
                created_files.append(destination)
                handle.write(change["content"].encode("utf-8"))
                handle.flush()
                os.fsync(handle.fileno())
        with target_state.open("xb") as handle:
            created_files.append(target_state)
            handle.write(canonical(preview["state"]))
            handle.flush()
            os.fsync(handle.fileno())
    except (OSError, DeliveryError):
        for path in reversed(created_files):
            path.unlink()
        raise
    finally:
        if acquired:
            lock.unlink()
        for directory in reversed(created_dirs):
            if directory.exists() and not any(directory.iterdir()):
                directory.rmdir()
    return {"outcome": "created", "project_id": project,
            "created": [str(p) for p in created_files]}


def status(*, brief_path, inputs_root, documents_root, state_root):
    inputs, documents, storage = roots_for(inputs_root, documents_root, state_root)
    path = checked_path(brief_path)
    if not path.is_relative_to(inputs):
        fail("BLOCKED: brief must be inside the explicit inputs root")
    brief = brief_at(path)
    guide = guidance()
    sources = sources_at(brief, inputs)
    state, _ = state_at(storage, brief["project_id"], documents)
    return {"contract": "apex-as.delivery-status/v1", "project_id": brief["project_id"],
            "synthetic": True, "sequence": state["sequence"],
            "artifacts": current_status(brief, guide, sources, state, documents),
            "history": state["events"],
            "notice": "Supplied synthetic records only; no identity authentication or external release."}
