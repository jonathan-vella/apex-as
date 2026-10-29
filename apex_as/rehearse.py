"""Replay the synthetic delivery using the real CLI, without a model or network."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from .delivery import DeliveryError, ROOT, canonical, checked_path, fail


def run_rehearsal(root):
    root = checked_path(root, directory=True)
    if any(root.iterdir()) or root.is_relative_to(ROOT) or ROOT.is_relative_to(root):
        fail("BLOCKED: rehearsal requires an empty directory outside product source")
    for folder in ("inputs", "documents", "state"):
        (root / folder).mkdir()
    brief_path = root / "inputs" / "brief.json"
    flags = ["--brief", str(brief_path), "--inputs-root", str(root / "inputs"),
             "--documents", str(root / "documents"), "--state", str(root / "state")]

    def command(name, *extra):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "apex_as", name, *flags, *extra],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        if result.returncode:
            raise DeliveryError(f"CLI rehearsal {name} failed: {result.stderr}")
        return json.loads(result.stdout)

    def author(*extra):
        preview = command("preview", *extra)
        return command("apply", *extra, "--approve", preview["approval"])

    def event(aid, kind, outcome, name):
        status = command("status")["artifacts"][aid]
        result = {
            "id": name, "artifact": aid, "kind": kind, "actor": "Invented supplied owner",
            "at": "2026-10-29T12:00:00+00:00", "reference": "synthetic:rehearsal-record",
            "revision": status["revision"], "sha256": status["sha256"],
            "outcome": outcome, "lanes": ["infrastructure", "database"],
        }
        if kind == "release":
            result["recipients"] = ["Invented operations recipient"]
        path = root / "inputs" / f"{name}.json"
        path.write_bytes(canonical({
            "contract": "apex-as.delivery-events/v1", "synthetic": True,
            "project_id": "demo-delivery-01", "records": [result],
        }))
        author("--events", str(path))

    brief = json.loads((ROOT / "fixtures" / "delivery" / "mixed.json").read_text())
    brief_path.write_bytes(canonical(brief))
    for aid in [f"ART-{i:02}" for i in range(1, 9)]:
        author("--artifacts", aid)
    event("ART-03", "review", "REVIEWED", "demo-design-review")
    event("ART-05", "execution", "RECORDED", "demo-migration-record")
    event("ART-06", "execution", "RECORDED", "demo-test-record")
    for outcome in ("PENDING", "REJECTED", "ACCEPTED"):
        event("ART-06", "customer", outcome, f"demo-customer-{outcome.lower()}")
    event("ART-07", "review", "REVIEWED", "demo-handover-review")
    event("ART-07", "release", "RELEASE_RECORDED", "demo-handover-release")
    author("--artifacts", "ART-08")
    delivered = command("status")
    if (delivered["artifacts"]["ART-05"]["execution"] != "RECORDED"
            or delivered["artifacts"]["ART-06"]["customer"] != "ACCEPTED"
            or delivered["artifacts"]["ART-07"]["release"] != "RELEASE_RECORDED"):
        fail("Rehearsal supplied-event assertions failed")
    index = root / "documents" / delivered["artifacts"]["ART-08"]["path"]
    if "RELEASE_RECORDED" not in index.read_text():
        fail("Rehearsal handover index omitted release state")
    edited = root / "documents" / delivered["artifacts"]["ART-03"]["path"]
    edited.write_text(edited.read_text() + "\nInvented practitioner edit to preserve.\n")
    preserved = edited.read_bytes()
    author("--carry-forward", "ART-03")
    if edited.read_bytes() != preserved:
        fail("Rehearsal overwrote practitioner content")
    revised = command("status")
    if revised["artifacts"]["ART-06"]["customer"] != "NEEDS_RECONFIRMATION":
        fail("Rehearsal improperly reused prior customer acceptance")
    results = [{"project": brief["project_id"], "artifacts": 8,
                "supplied_events": len(delivered["history"]), "reconfirmation": True}]
    for filename in ("infrastructure.json", "database.json"):
        next_brief = json.loads((ROOT / "fixtures" / "delivery" / filename).read_text())
        brief_path.write_bytes(canonical(next_brief))
        author()
        status = command("status")
        if status["history"] or any(item["customer"] != "NOT_REQUESTED"
                                     for item in status["artifacts"].values()):
            fail("Rehearsal carried prior project events into a new project")
        results.append({"project": next_brief["project_id"], "lanes": next_brief["lanes"],
                        "artifacts": len(status["artifacts"]), "history": 0})
    summary = {"outcome": "passed", "synthetic": True, "projects": results,
               "network_calls": 0, "native_plugin_test": False,
               "notice": "Local CLI replay only; invented records, not an actual migration or release."}
    (root / "rehearsal-result.json").write_bytes(canonical(summary))
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep", type=Path,
                        help="retain outputs in this explicitly selected existing empty directory")
    args = parser.parse_args(argv)
    try:
        if args.keep:
            result = run_rehearsal(args.keep)
        else:
            with tempfile.TemporaryDirectory(prefix="apex-as-rehearsal-") as directory:
                result = run_rehearsal(Path(directory))
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, DeliveryError) as error:
        print(json.dumps({"outcome": "blocked", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
