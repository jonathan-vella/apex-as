"""Build an explicit, inspected source-only archive; never install a plugin."""

import argparse
import json
from pathlib import Path
import sys
import zipfile

from .delivery import ROOT, DeliveryError, canonical, checked_path, digest, fail, read_bytes


def package_plan(destination):
    destination = checked_path(destination)
    if destination.is_relative_to(ROOT) or destination.suffix.lower() != ".zip":
        fail("BLOCKED: choose an absolute .zip destination outside the product source")
    checked_path(destination.parent, directory=True)
    if destination.exists():
        fail("COLLISION: source archive already exists; choose a new destination")
    files = [ROOT / "plugin.json", ROOT / "README.md", ROOT / ".gitignore"]
    files += sorted((ROOT / "apex_as").glob("*.py"))
    files += [ROOT / "apex_as" / "guidance.json"]
    files += sorted((ROOT / "com.github.copilot" / "agents").glob("*.agent.md"))
    files += sorted((ROOT / "docs").glob("*.md"))
    files += sorted((ROOT / "tests").glob("test_*.py"))
    files += [ROOT / "fixtures" / "synthetic-evidence.json"]
    files += sorted((ROOT / "fixtures" / "delivery").glob("*.json"))
    records = [{"path": p.relative_to(ROOT).as_posix(), "sha256": digest(read_bytes(p))}
               for p in files]
    plan = {"contract": "apex-as.source-package/v1", "destination": str(destination),
            "files": records, "notice": "Experimental source kit, not a verified native authoring plugin release."}
    plan["approval"] = digest(canonical(plan))
    return plan


def create_package(destination, approval):
    plan = package_plan(destination)
    if approval != plan["approval"]:
        fail("NOT AUTHORIZED: package content/destination changed; preview again")
    payloads = [(item["path"], read_bytes(ROOT.joinpath(*item["path"].split("/"))))
                for item in plan["files"]]
    if any(digest(raw) != item["sha256"] for (_, raw), item in zip(payloads, plan["files"])):
        fail("CONFLICT: package source changed after preview")
    created = False
    try:
        with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED) as archive:
            created = True
            for name, raw in payloads:
                archive.writestr(name, raw)
            archive.writestr("APEX-AS-SOURCE-MANIFEST.json", canonical(plan))
    except (OSError, ValueError, zipfile.BadZipFile):
        if created:
            Path(destination).unlink()
        raise
    return {"outcome": "created", "destination": str(destination), "files": len(payloads),
            "sha256": digest(Path(destination).read_bytes())}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--approve")
    args = parser.parse_args(argv)
    try:
        result = create_package(args.output, args.approve) if args.approve else package_plan(args.output)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, DeliveryError, zipfile.BadZipFile) as error:
        print(json.dumps({"outcome": "blocked", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
