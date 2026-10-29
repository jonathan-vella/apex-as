import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from apex_as import package
from apex_as.delivery import DeliveryError


class SourcePackageTests(unittest.TestCase):
    def test_explicit_source_archive_excludes_reference_and_caches(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "source.zip"
            plan = package.package_plan(target)
            self.assertFalse(target.exists())
            with self.assertRaisesRegex(DeliveryError, "NOT AUTHORIZED"):
                package.create_package(target, "wrong")
            package.create_package(target, plan["approval"])
            with zipfile.ZipFile(target) as archive:
                names = archive.namelist()
                self.assertIn("plugin.json", names)
                self.assertIn("apex_as/delivery.py", names)
                self.assertIn("fixtures/delivery/database.json", names)
                self.assertNotIn("tmp/as-infra-nov2026.md", names)
                self.assertFalse(any("tmp/" in name or "__pycache__" in name for name in names))
                manifest = json.loads(archive.read("APEX-AS-SOURCE-MANIFEST.json"))
                for item in manifest["files"]:
                    self.assertEqual(package.digest(archive.read(item["path"])), item["sha256"])
            with self.assertRaisesRegex(DeliveryError, "COLLISION"):
                package.package_plan(target)

    def test_source_destination_refused(self):
        with self.assertRaisesRegex(DeliveryError, "outside"):
            package.package_plan(package.ROOT / "source.zip")


if __name__ == "__main__":
    unittest.main()
