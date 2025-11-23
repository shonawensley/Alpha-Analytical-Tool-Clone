#!/usr/bin/env python3
"""
Regenerate JSON table mirrors for one or more states from the Combined CSV tables.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from utils import path_handler as ph
from utils.json_tables import build_json_tables_from_csv


def iter_states(tables_root: Path, selected: Iterable[str] | None) -> Iterable[str]:
    if selected:
        for state in selected:
            yield state
        return
    for entry in tables_root.iterdir():
        if entry.is_dir():
            yield entry.name


def main() -> None:
    parser = argparse.ArgumentParser(description="Build JSON mirrors from Combined tables.")
    parser.add_argument("--state", action="append", help="Specific state(s) to refresh.")
    parser.add_argument("--tables-root", default=ph.get_tables_output_dir())
    parser.add_argument("--out-root", default=ph.get_json_tables_dir())
    args = parser.parse_args()

    tables_root = Path(args.tables_root)
    out_root = Path(args.out_root)
    if not tables_root.exists():
        raise SystemExit(f"tables root missing: {tables_root}")

    for state in iter_states(tables_root, args.state):
        state_dir = tables_root / state
        if not state_dir.exists():
            print(f"[skip] tables not found for {state}")
            continue
        try:
            path = build_json_tables_from_csv(state, str(state_dir), str(out_root))
            print(f"[ok] {state}: {path}")
        except Exception as exc:
            print(f"[error] {state}: {exc}")


if __name__ == "__main__":
    main()
