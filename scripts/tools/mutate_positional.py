#!/usr/bin/env python
"""Helper wrapper around mutmut for the positional shortlist scorer.

Usage:
    python scripts/tools/mutate_positional.py --dry-run

If mutmut is not installed, the script prints installation instructions.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "modules" / "module_d_auxiliary_tools" / "refactored" / "positional_tool.py"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run mutmut against the positional shortlist scorer.")
    parser.add_argument("--dry-run", action="store_true", help="Only print the command that would be executed.")
    args = parser.parse_args()

    mutmut = shutil.which("mutmut")
    if mutmut is None:
        sys.stderr.write(
            "mutmut is not installed. Install with `pip install mutmut` and re-run this helper.\n"
        )
        return 1

    cmd = [mutmut, "run", "--paths", str(TARGET)]
    if args.dry_run:
        print("Dry run:", " ".join(cmd))
        return 0

    return subprocess.call(cmd, cwd=str(ROOT))


if __name__ == "__main__":
    sys.exit(main())
