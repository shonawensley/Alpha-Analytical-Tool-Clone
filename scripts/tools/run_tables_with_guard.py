#!/usr/bin/env python3
"""
Helper to optionally activate a dated Pick3StatsC4 workbook and regenerate tables
only when necessary (using run_tables_with_guard).
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Any

from utils import path_handler as ph


def _activate_history_file(filename: str) -> None:
    history = Path("data/history") / filename
    if not history.exists():
        raise SystemExit(f"History file not found: {history}")
    dest = Path(ph.get_excel_path())
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(history, dest)
    print(f"Activated {history} -> {dest}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run tables pipeline with guard manifest.")
    parser.add_argument("--history-file", help="Optional filename under data/history/ to activate first.")
    parser.add_argument("--excel-path", default=ph.get_excel_path(), help="Explicit path to Pick3StatsC4 workbook.")
    args = parser.parse_args()

    if args.history_file:
        _activate_history_file(args.history_file)

    from core.pipeline_runner import run_tables_with_guard

    summary: dict[str, Any] = run_tables_with_guard(args.excel_path)
    if summary.get("skipped"):
        print("Tables already up to date.")
    else:
        print("Tables regenerated.")
    manifest = summary.get("manifest")
    if manifest:
        print("Manifest:")
        from pprint import pprint

        pprint(manifest)


if __name__ == "__main__":
    main()
