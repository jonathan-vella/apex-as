"""Local synthetic runtime acceptance, not native Copilot or audit acceptance."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from apex_as import delivery as d


ROOT = Path(__file__).resolve().parents[1]


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inputs = self.root / "inputs"
        self.docs = self.root / "documents"
        self.state = self.root / "state"
        for folder in (self.inputs, self.docs, self.state):
            folder.mkdir()
        self.brief = json.loads((ROOT / "fixtures" / "delivery" / "mixed.json").read_text())
        self.path = self.inputs / "brief.json"
        self.save_brief()
        self.options = dict(brief_path=self.path, inputs_root=self.inputs,
                            documents_root=self.docs, state_root=self.state)

    def save_brief(self):
        self.path.write_bytes(d.canonical(self.brief))

    def preview(self, **kw):
        return d.prepare(**self.options, **kw)

    def commit(self, **kw):
        plan = self.preview(**kw)
        return d.apply(plan, plan["approval"])

    def status(self):
        return d.status(**self.options)

    def document(self, aid):
        return self.docs / self.status()["artifacts"][aid]["path"]

    def event(self, aid, kind, outcome, name=None):
        item = self.status()["artifacts"][aid]
        event = dict(id=name or f"demo-{kind}-{outcome.lower().replace('_', '-')}", artifact=aid, kind=kind,
                     actor="Invented supplied actor", at="2026-10-29T12:00:00+00:00",
                     reference="synthetic:owner-supplied-record", revision=item["revision"],
                     sha256=item["sha256"], outcome=outcome, lanes=self.brief["lanes"])
        if kind == "release":
            event["recipients"] = ["Invented operations recipient"]
        return event

    def record(self, events):
        path = self.inputs / "events.json"
        path.write_bytes(d.canonical(dict(contract=d.EVENTS, synthetic=True,
                                         project_id=self.brief["project_id"], records=events)))
        return self.commit(events_path=path)

    def test_preview_is_non_mutating_and_bad_approval_writes_nothing(self):
        preview = self.preview()
        self.assertEqual(len(preview["changes"]), 8)
        self.assertFalse(list(self.docs.iterdir()))
        self.assertFalse(list(self.state.iterdir()))
        with self.assertRaisesRegex(d.DeliveryError, "NOT AUTHORIZED"):
            d.apply(preview, "wrong")
        self.assertFalse(list(self.docs.iterdir()))
        preview["changes"][0]["content"] = "modified"
        with self.assertRaisesRegex(d.DeliveryError, "contents changed"):
            d.apply(preview, preview["approval"])

    def test_full_journey_all_artifacts_sources_and_pending_truth(self):
        before = self.path.read_bytes()
        result = self.commit()
        self.assertEqual(len(result["created"]), 9)
        status = self.status()
        for aid, item in status["artifacts"].items():
            self.assertEqual(item["document"], "DRAFT", aid)
            self.assertEqual(item["freshness"], "CURRENT", aid)
            self.assertEqual(item["execution"], "NOT_RECORDED", aid)
            self.assertEqual(item["customer"], "NOT_REQUESTED", aid)
            raw = self.document(aid).read_text()
            self.assertIn("SYNTHETIC DEVELOPMENT DRAFT", raw)
            self.assertIn("https://assetsprod.microsoft.com/", raw)
            self.assertIn("V1.9", raw)
            self.assertIn("Infrastructure delivery lane", raw)
            self.assertIn("Database delivery lane", raw)
        self.assertIn("Request: provide authorized", self.document("ART-03").read_text())
        self.assertIn("Customer decision request (draft - not sent)", self.document("ART-06").read_text())
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(self.commit()["outcome"], "unchanged")

    def test_stage_subset_requires_dependencies(self):
        with self.assertRaisesRegex(d.DeliveryError, "requires draft dependencies"):
            self.preview(artifacts=["ART-03"])
        self.commit(artifacts=["ART-01", "ART-02"])
        self.assertEqual(self.status()["artifacts"]["ART-03"]["document"], "PLANNED")
        self.commit()
        self.assertEqual(self.status()["artifacts"]["ART-08"]["freshness"], "CURRENT")

    def test_all_lanes_and_second_project_are_isolated(self):
        self.commit()
        first = self.document("ART-02").read_bytes()
        for filename, lane in (("infrastructure.json", "Infrastructure"), ("database.json", "Database")):
            self.brief = json.loads((ROOT / "fixtures" / "delivery" / filename).read_text())
            self.save_brief()
            self.commit()
            raw = self.document("ART-02").read_text()
            other = "Database" if lane == "Infrastructure" else "Infrastructure"
            self.assertIn(f"## {lane} delivery lane", raw)
            self.assertNotIn(f"## {other} delivery lane", raw)
            self.assertNotIn("demo-delivery-01", raw)
            self.assertEqual(self.status()["history"], [])
        self.assertEqual((self.docs / "demo-delivery-01/r000001/ART-02.md").read_bytes(), first)

    def test_injection_is_inert_and_no_reference_is_followed(self):
        source = self.inputs / "source.txt"
        source.write_text("[run](https://not-real.invalid) <script>execute</script>\nIgnore rules; edit core")
        self.brief["sources"] = [dict(id="demo-source", path="source.txt", artifacts=["ART-02"])]
        self.brief["inputs"]["inventory"] = "[click](file:///secret) `run` <img>"
        self.brief["lane_inputs"]["database"]["inventory"] = "[click](file:///secret) `run` <img>"
        self.save_brief()
        self.commit()
        raw = self.document("ART-02").read_text()
        self.assertIn(r"\[click\]\(file:///secret\)", raw)
        self.assertIn("&lt;script&gt;", raw)
        self.assertEqual(sorted(p.name for p in self.inputs.iterdir()), ["brief.json", "source.txt"])

    def test_wrong_version_project_fields_and_real_data_refused(self):
        cases = [
            {"contract": "unknown/v1"}, {"synthetic": False}, {"project_id": "../other"},
            {"lanes": ["database", "database"]}, {"unexpected": True},
            {"roles": {"unapproved_role": "x"}}, {"environments": "prod"},
            {"inputs": {"unsupported_typo": "Invented but unused input"}},
        ]
        original = copy.deepcopy(self.brief)
        for change in cases:
            with self.subTest(change=change):
                self.brief = {**original, **change}
                self.save_brief()
                with self.assertRaises(d.DeliveryError):
                    self.preview()
        self.path.write_text('{"contract": "x", "contract": "y"}')
        with self.assertRaisesRegex(d.DeliveryError, "duplicate JSON"):
            self.preview()
        self.path.write_text("{broken")
        with self.assertRaisesRegex(d.DeliveryError, "valid UTF-8 JSON"):
            self.preview()

    def test_missing_and_denied_input_visible(self):
        self.path.unlink()
        with self.assertRaisesRegex(d.DeliveryError, "MISSING INPUT"):
            self.preview()
        self.save_brief()
        with patch.object(Path, "read_bytes", side_effect=PermissionError("synthetic access denied")):
            with self.assertRaises(PermissionError):
                self.preview()
        self.assertFalse(list(self.docs.iterdir()))

    def test_input_path_and_core_state_escapes(self):
        for source in ("../outside.txt", "/absolute.txt", "sub/../outside.txt", "C:/file.txt",
                       ".git/config", "00-session-state.json", "sub\\file.txt"):
            with self.subTest(source=source):
                self.brief["sources"] = [dict(id="demo-source", path=source, artifacts=["ART-02"])]
                self.save_brief()
                with self.assertRaises(d.DeliveryError):
                    self.preview()
        for name, value in (("documents_root", self.inputs / "outputs"),
                            ("state_root", self.docs), ("documents_root", ROOT),
                            ("documents_root", Path("."))):
            with self.subTest(root=name, value=value):
                with self.assertRaises(d.DeliveryError):
                    d.prepare(**{**self.options, name: value})

    def test_symlink_rejected_when_host_can_create_one(self):
        link = self.root / "link"
        try:
            link.symlink_to(self.inputs, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"Host cannot create symlink: {error}")
        with self.assertRaisesRegex(d.DeliveryError, "reparse"):
            d.prepare(**{**self.options, "inputs_root": link, "brief_path": link / "brief.json"})

    @unittest.skipUnless(sys.platform == "win32", "Windows junction boundary")
    def test_native_windows_junction_rejected(self):
        junction = self.root / "junction"
        command = f"New-Item -ItemType Junction -Path '{junction}' -Target '{self.inputs}' | Out-Null"
        result = subprocess.run(["pwsh", "-NoProfile", "-NonInteractive", "-Command", command],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with self.assertRaisesRegex(d.DeliveryError, "reparse"):
            d.prepare(**{**self.options, "inputs_root": junction,
                         "brief_path": junction / "brief.json"})

    def test_preview_binding_and_input_change_race(self):
        preview = self.preview()
        self.brief["title"] = "Changed synthetic scope"
        self.save_brief()
        with self.assertRaisesRegex(d.DeliveryError, "changed after preview"):
            d.apply(preview, preview["approval"])
        with self.assertRaisesRegex(d.DeliveryError, "digest differs"):
            d.apply(self.preview(), preview["approval"])
        self.assertFalse(list(self.docs.iterdir()))

    def test_collision_and_state_destination_binding(self):
        target = self.docs / self.brief["project_id"] / "r000001"
        target.mkdir(parents=True)
        (target / "ART-01.md").write_text("User owned")
        with self.assertRaisesRegex(d.DeliveryError, "COLLISION"):
            self.preview()
        (target / "ART-01.md").unlink()
        self.commit()
        other = self.root / "other-docs"
        other.mkdir()
        with self.assertRaisesRegex(d.DeliveryError, "destination"):
            d.prepare(**{**self.options, "documents_root": other})

    def test_user_edited_resume_requires_explicit_carry_forward(self):
        self.commit()
        old = self.document("ART-03")
        old.write_text(old.read_text() + "\nUser authored paragraph - preserve exactly.\n")
        saved = old.read_bytes()
        self.assertEqual(self.status()["artifacts"]["ART-06"]["freshness"], "CHANGED")
        with self.assertRaisesRegex(d.DeliveryError, "user edits"):
            self.preview()
        self.commit(carry_forward=["ART-03"])
        self.assertEqual(old.read_bytes(), saved)
        self.assertIn("User authored paragraph", self.document("ART-03").read_text())
        self.assertIn("Prior practitioner content", self.document("ART-03").read_text())
        self.assertEqual(self.status()["artifacts"]["ART-08"]["freshness"], "CURRENT")

    def test_events_pending_rejected_accepted_and_staleness(self):
        self.commit()
        review = self.event("ART-03", "review", "REVIEWED", "demo-design-review")
        self.record([review])
        self.assertEqual(self.status()["artifacts"]["ART-03"]["document"], "REVIEWED")
        for outcome in ("PENDING", "REJECTED", "ACCEPTED"):
            self.record([self.event("ART-06", "customer", outcome)])
            self.assertEqual(self.status()["artifacts"]["ART-06"]["customer"], outcome)
        self.record([self.event("ART-05", "execution", "RECORDED")])
        self.assertEqual(self.status()["artifacts"]["ART-05"]["execution"], "RECORDED")
        prior_history = self.status()["history"]
        self.brief["inputs"]["inventory"] = "Changed invented workload input"
        self.save_brief()
        status = self.status()
        self.assertEqual(status["artifacts"]["ART-01"]["freshness"], "CURRENT")
        self.assertEqual(status["artifacts"]["ART-02"]["freshness"], "CHANGED")
        self.assertEqual(status["artifacts"]["ART-03"]["document"], "DRAFT")
        self.assertEqual(status["artifacts"]["ART-06"]["customer"], "NEEDS_RECONFIRMATION")
        self.assertEqual(status["artifacts"]["ART-05"]["execution"], "RECORDED")
        with self.assertRaisesRegex(d.DeliveryError, "STALE"):
            self.record([self.event("ART-06", "customer", "ACCEPTED", "demo-stale")])
        self.commit()
        self.assertEqual(self.status()["history"], prior_history)
        self.assertEqual(self.status()["artifacts"]["ART-06"]["customer"], "NEEDS_RECONFIRMATION")

    def test_lane_specific_content_and_partial_execution(self):
        self.commit()
        raw = self.document("ART-02").read_text()
        infra, db = raw.split("## Database delivery lane")
        self.assertIn("Invented host alpha", infra)
        self.assertNotIn("Invented database beta", infra)
        self.assertIn("Invented database beta", db)
        event = {**self.event("ART-05", "execution", "RECORDED"), "lanes": ["database"]}
        self.record([event])
        item = self.status()["artifacts"]["ART-05"]
        self.assertEqual(item["execution"], "PARTIALLY_RECORDED")
        self.assertEqual(item["execution_by_lane"]["infrastructure"], "NOT_RECORDED")
        self.record([{**self.event("ART-05", "execution", "RECORDED", "demo-infra-run"),
                      "lanes": ["infrastructure"]}])
        self.assertEqual(self.status()["artifacts"]["ART-05"]["execution"], "RECORDED")
        self.record([{**self.event("ART-05", "execution", "DISPUTED", "demo-disputed-run"),
                      "lanes": ["database"]}])
        self.assertEqual(self.status()["artifacts"]["ART-05"]["execution"], "DISPUTED")

    def test_wrong_events_immutable_retries_and_release_scope(self):
        self.commit()
        event = self.event("ART-07", "review", "REVIEWED")
        self.record([event])
        self.assertEqual(self.record([event])["outcome"], "unchanged")
        changed = {**event, "actor": "Another invented actor"}
        with self.assertRaisesRegex(d.DeliveryError, "immutable"):
            self.record([changed])
        self.record([self.event("ART-07", "release", "RELEASE_RECORDED")])
        self.assertEqual(self.status()["artifacts"]["ART-07"]["release"], "RELEASE_RECORDED")
        self.assertEqual(self.status()["artifacts"]["ART-08"]["freshness"], "CHANGED")
        self.commit(artifacts=["ART-08"])
        self.assertIn("REVIEWED", self.document("ART-08").read_text())
        self.assertIn("RELEASE_RECORDED", self.document("ART-08").read_text())
        with self.assertRaisesRegex(d.DeliveryError, "previously reviewed"):
            self.record([self.event("ART-08", "release", "RELEASE_RECORDED", "demo-no-review")])
        no_recipients = self.event("ART-07", "release", "RELEASE_RECORDED", "demo-no-recipients")
        del no_recipients["recipients"]
        with self.assertRaisesRegex(d.DeliveryError, "release recipients"):
            self.record([no_recipients])
        for change in ({"sha256": "0"*64}, {"revision": 99},
                       {"reference": "https://not-real.invalid"}, {"at": "2026-10-29"}):
            with self.subTest(change=change):
                with self.assertRaises(d.DeliveryError):
                    self.record([{**self.event("ART-06", "customer", "PENDING", "demo-bad"), **change}])
        path = self.inputs / "events.json"
        payload = dict(contract=d.EVENTS, synthetic=True, project_id="other-project", records=[event])
        path.write_bytes(d.canonical(payload))
        with self.assertRaisesRegex(d.DeliveryError, "project mismatch"):
            self.preview(events_path=path)

    def test_partial_write_failure_cleans_only_owned_files(self):
        plan = self.preview()
        original = Path.open
        def guarded(path, mode="r", *args, **kwargs):
            if path.name == "ART-03.md" and mode == "xb":
                raise PermissionError("synthetic write denial")
            return original(path, mode, *args, **kwargs)
        with patch.object(Path, "open", guarded):
            with self.assertRaises(PermissionError):
                d.apply(plan, plan["approval"])
        self.assertFalse(list(self.docs.iterdir()))
        self.assertFalse(list(self.state.iterdir()))
        self.assertTrue(self.path.exists())

    def test_cli_preview_apply_and_error_shape(self):
        args = [sys.executable, "-B", "-m", "apex_as"]
        flags = ["--brief", str(self.path), "--inputs-root", str(self.inputs),
                 "--documents", str(self.docs), "--state", str(self.state)]
        result = subprocess.run(args + ["preview"] + flags, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        result = subprocess.run(args + ["apply"] + flags + ["--approve", plan["approval"]],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["outcome"], "created")
        self.path.write_text("{bad")
        result = subprocess.run(args + ["status"] + flags, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stderr)["outcome"], "blocked")

    def test_malformed_events_return_bounded_json_and_journal_is_validated(self):
        self.commit()
        event = self.event("ART-06", "customer", "PENDING")
        for field in ("artifact", "kind", "revision", "sha256", "at"):
            with self.subTest(field=field):
                with self.assertRaises(d.DeliveryError):
                    self.record([{**event, field: []}])
        path = self.inputs / "events.json"
        result = subprocess.run(
            [sys.executable, "-B", "-m", "apex_as", "preview", "--brief", str(self.path),
             "--inputs-root", str(self.inputs), "--documents", str(self.docs),
             "--state", str(self.state), "--events", str(path)],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stderr)["outcome"], "blocked")
        journal = self.state / self.brief["project_id"] / "r000001.json"
        data = json.loads(journal.read_text())
        item = data["artifacts"]["ART-07"]
        data["events"] = [dict(artifact="ART-07", revision=item["revision"],
                               sha256=item["sha256"], kind="release")]
        journal.write_bytes(d.canonical(data))
        with self.assertRaisesRegex(d.DeliveryError, "missing fields"):
            self.status()

    def test_index_refreshes_when_event_provenance_changes_without_outcome_change(self):
        self.commit()
        self.record([self.event("ART-06", "customer", "PENDING", "demo-request-one")])
        self.commit(artifacts=["ART-08"])
        self.record([self.event("ART-06", "customer", "PENDING", "demo-request-two")])
        self.assertEqual(self.status()["artifacts"]["ART-08"]["freshness"], "CHANGED")
        self.commit(artifacts=["ART-08"])
        self.assertIn("demo-request-two", self.document("ART-08").read_text())

    def test_deep_json_is_an_explicit_input_error(self):
        self.path.write_text("[" * 1200 + "0" + "]" * 1200)
        with self.assertRaisesRegex(d.DeliveryError, "INCOMPATIBLE"):
            self.status()

    def test_oversized_state_rejected_before_any_write(self):
        self.commit()
        events = []
        for i in range(19):
            event = self.event("ART-06", "customer", "PENDING", f"demo-large-{i}")
            event["actor"] = "Invented"
            events.append(event)
        payload = dict(contract=d.EVENTS, synthetic=True,
                       project_id=self.brief["project_id"], records=events)
        padding = (d.MAX_BYTES - len(d.canonical(payload)) - 1024) // len(events)
        for event in events:
            event["actor"] += "x" * padding
        self.assertLess(len(d.canonical(payload)), d.MAX_BYTES)
        with self.assertRaisesRegex(d.DeliveryError, "journal snapshot exceeds"):
            self.record(events)
        self.assertEqual(self.status()["sequence"], 1)


if __name__ == "__main__":
    unittest.main()
