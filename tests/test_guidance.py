import json
import re
import unittest
from pathlib import Path


GUIDANCE_PATH = Path(__file__).resolve().parents[1] / "apex_as" / "guidance.json"
ARTIFACT_IDS = [f"ART-{number:02d}" for number in range(1, 9)]
ARTIFACT_FIELDS = {
    "id",
    "title",
    "stage",
    "owner_role",
    "capture_point",
    "depends_on",
    "source_locator",
    "sections",
}
OWNER_ROLES = {
    "delivery_lead",
    "specialist",
    "architect",
    "migration_lead",
    "executor",
    "test_owner",
    "operations_owner",
}
DEPENDENCIES = [
    [],
    ["ART-01"],
    ["ART-02"],
    ["ART-03"],
    ["ART-04"],
    ["ART-04", "ART-05"],
    ["ART-03", "ART-05", "ART-06"],
    ARTIFACT_IDS[:7],
]


def reject_duplicate_fields(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate guidance field: {key}")
        result[key] = value
    return result


class GuidanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guidance = json.loads(
            GUIDANCE_PATH.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_fields,
        )

    def assert_nonempty_text(self, value):
        self.assertIsInstance(value, str)
        self.assertTrue(value.strip())

    def test_top_level_schema_and_source_record(self):
        self.assertEqual(set(self.guidance), {"version", "source", "artifacts"})
        self.assertEqual(self.guidance["version"], "delivery-guidance/v1")
        source = self.guidance["source"]
        self.assertIsInstance(source, dict)
        self.assertEqual(
            set(source), {"url", "observed_version", "window", "notice"}
        )
        self.assertEqual(
            source["url"],
            "https://assetsprod.microsoft.com/en-us/"
            "azure-infra-and-db-specialization-audit-checklist.pdf",
        )
        self.assertEqual(
            source["observed_version"],
            "V2.0 header / V1.9 Module B heading; unresolved",
        )
        self.assertEqual(
            source["window"], "2026-07-01 through 2026-12-31"
        )
        for field, value in source.items():
            with self.subTest(field=field):
                self.assert_nonempty_text(value)
        self.assertIn("PENDING", source["notice"])
        self.assertIn("supplied events", source["notice"])
        self.assertIn("not copied checklist", source["notice"])

    def test_exact_artifact_ids_and_stages(self):
        artifacts = self.guidance["artifacts"]
        self.assertIsInstance(artifacts, list)
        self.assertEqual(len(artifacts), 8)
        self.assertEqual([artifact["id"] for artifact in artifacts], ARTIFACT_IDS)
        self.assertEqual(
            [artifact["stage"] for artifact in artifacts],
            ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D6"],
        )

    def test_artifact_fields_and_owner_roles(self):
        for artifact in self.guidance["artifacts"]:
            with self.subTest(artifact=artifact["id"]):
                self.assertEqual(set(artifact), ARTIFACT_FIELDS)
                for field in ARTIFACT_FIELDS - {"depends_on", "sections"}:
                    with self.subTest(field=field):
                        self.assert_nonempty_text(artifact[field])
                self.assertIn(artifact["owner_role"], OWNER_ROLES)
                self.assertIn("Module B:", artifact["source_locator"])
        self.assertEqual(
            [artifact["owner_role"] for artifact in self.guidance["artifacts"]],
            [
                "delivery_lead",
                "specialist",
                "architect",
                "migration_lead",
                "executor",
                "test_owner",
                "operations_owner",
                "delivery_lead",
            ],
        )

    def test_dependency_lists_are_exact_unique_and_prior_only(self):
        prior_ids = set()
        for artifact, expected in zip(self.guidance["artifacts"], DEPENDENCIES):
            with self.subTest(artifact=artifact["id"]):
                dependencies = artifact["depends_on"]
                self.assertIsInstance(dependencies, list)
                self.assertEqual(dependencies, expected)
                self.assertEqual(len(dependencies), len(set(dependencies)))
                self.assertTrue(set(dependencies).issubset(prior_ids))
                prior_ids.add(artifact["id"])

    def test_sections_have_nonempty_renderer_fields_and_unique_input_keys(self):
        for artifact in self.guidance["artifacts"]:
            with self.subTest(artifact=artifact["id"]):
                sections = artifact["sections"]
                self.assertIsInstance(sections, list)
                self.assertGreaterEqual(len(sections), 4)
                self.assertLessEqual(len(sections), 6)
                input_keys = []
                for section in sections:
                    with self.subTest(section=section.get("heading")):
                        self.assertIsInstance(section, dict)
                        self.assertEqual(
                            set(section), {"heading", "prompt", "input_key"}
                        )
                        for value in section.values():
                            self.assert_nonempty_text(value)
                        self.assertIsNotNone(
                            re.fullmatch(r"[a-z][a-z0-9_]*", section["input_key"])
                        )
                        input_keys.append(section["input_key"])
                self.assertEqual(len(input_keys), len(set(input_keys)))


if __name__ == "__main__":
    unittest.main()
