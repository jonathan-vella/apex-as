"""Static packaging checks only; these do not prove client installation."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PluginProofTests(unittest.TestCase):
    def test_manifest_has_only_documented_metadata(self):
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(
            set(manifest), {"$schema", "name", "version", "description"}
        )
        self.assertEqual(
            manifest["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        self.assertEqual(manifest["name"], "apex-as-proof")
        self.assertEqual(manifest["version"], "0.0.1")

    def test_one_agent_and_no_active_integrations(self):
        agents = list((ROOT / "com.github.copilot" / "agents").glob("*.agent.md"))
        self.assertEqual([path.name for path in agents], ["apex-as-fixture.agent.md"])
        header = agents[0].read_text(encoding="utf-8").split("---", 2)[1]
        self.assertIn("\ntools: ['read']\n", header)
        self.assertIn("\ndisable-model-invocation: true\n", header)
        for path in (
            "mcp.json",
            "hooks.json",
            "com.github.copilot/hooks",
            ".github/agents",
            ".vscode/settings.json",
            ".devcontainer",
            "Dockerfile",
        ):
            self.assertFalse((ROOT / path).exists(), path)

    def test_synthetic_fixture_and_expected_demonstration(self):
        fixture = json.loads(
            (ROOT / "fixtures" / "synthetic-evidence.json").read_text(encoding="utf-8")
        )
        self.assertEqual(fixture["fixtureContract"], "apex-as.synthetic-proof/v1")
        self.assertIs(fixture["synthetic"], True)
        self.assertEqual(
            [item["id"] for item in fixture["items"]],
            ["demo-design", "demo-acceptance", "demo-platform"],
        )
        self.assertEqual(
            [item["reference"] for item in fixture["items"]],
            ["synthetic:design-note-01", None, None],
        )

    def test_local_reference_directory_has_git_exclusion(self):
        rules = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn("/tmp/", rules)


if __name__ == "__main__":
    unittest.main()
