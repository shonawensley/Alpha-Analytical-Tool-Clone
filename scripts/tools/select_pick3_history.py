#!/usr/bin/env python3
"""
Helper to swap the active Pick3StatsC4 workbook with any dated history file.

Usage examples:
  python scripts/tools/select_pick3_history.py --list
  python scripts/tools/select_pick3_history.py --file Pick3StatsC4_2025-06-24.xlsm
  python scripts/tools/select_pick3_history.py --latest
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


HISTORY_DIR = Path("data/history")
ORIGINAL_FILE = Path("data/original/Pick3StatsC4.xlsm")


def list_history_files() -> list[Path]:
    """Return sorted list of available history files."""
    if not HISTORY_DIR.exists():
        return []
    return sorted(HISTORY_DIR.glob("Pick3StatsC4_*.xlsm"))


def copy_file(src: Path) -> None:
    ORIGINAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, ORIGINAL_FILE)


def main() -> None:
    parser = argparse.ArgumentParser(description="Swap Pick3StatsC4 workbook with a dated history file.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", type=str, help="Specific filename under data/history to activate.")
    group.add_argument("--latest", action="store_true", help="Use the most recent history file.")
    parser.add_argument("--list", action="store_true", help="List available history files and exit.")

    args = parser.parse_args()
    files = list_history_files()

    if args.list:
        if not files:
            print("No history files found under data/history")
        else:
            print("Available history files:")
            for f in files:
                print(f"  {f.name}")
        return

    if not files:
        raise SystemExit("No files found under data/history")

    target: Path
    if args.file:
        target = HISTORY_DIR / args.file
        if not target.exists():
            raise SystemExit(f"{target} does not exist")
    elif args.latest:
        target = files[-1]
    else:
        # Default to newest file so casual runs stay simple.
        target = files[-1]

    copy_file(target)
    print(f"Copied {target.name} -> {ORIGINAL_FILE}")


if __name__ == "__main__":
    main()
