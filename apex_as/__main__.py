"""Run with python -B -m apex_as; no installation required."""

import argparse
import json
import sys

from . import __version__
from .delivery import DeliveryError, apply, prepare, status


def main(argv=None):
    parser = argparse.ArgumentParser(description="APEX AS synthetic delivery drafts (local only)")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("preview", "apply", "status"):
        command = commands.add_parser(name)
        command.add_argument("--brief", required=True)
        command.add_argument("--inputs-root", required=True)
        command.add_argument("--documents", required=True)
        command.add_argument("--state", required=True)
        if name != "status":
            command.add_argument("--artifacts", nargs="+")
            command.add_argument("--events")
            command.add_argument("--carry-forward", nargs="*", default=[])
        if name == "apply":
            command.add_argument("--approve", required=True,
                                 help="exact approval digest from a reviewed current preview")
    args = parser.parse_args(argv)
    options = dict(brief_path=args.brief, inputs_root=args.inputs_root,
                   documents_root=args.documents, state_root=args.state)
    try:
        if args.command == "status":
            result = status(**options)
        else:
            preview = prepare(**options, artifacts=args.artifacts, events_path=args.events,
                              carry_forward=args.carry_forward)
            result = apply(preview, args.approve) if args.command == "apply" else preview
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return 0
    except (DeliveryError, OSError, UnicodeError) as error:
        print(json.dumps({"outcome": "blocked", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
