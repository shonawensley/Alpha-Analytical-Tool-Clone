#!/usr/bin/env python3
"""
Print the headers for Stable CSV outputs (scores, families, compound) for a state.

Usage:
    python3 scripts/checks/print_stable_header.py data/outputs/analysis/patterns/Connecticut4
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


def print_header(csv_path: Path) -> None:
    if not csv_path.exists():
        print(f"{csv_path} (missing)")
        return
    df = pd.read_csv(csv_path, nrows=0)
    print(f"\n{csv_path.name} :: {len(df.columns)} columns")
    print(", ".join(df.columns))


def main(root: Path) -> None:
    if not root.exists():
        raise SystemExit(f"{root} not found")
    stems = [
        "_stable_patterns_scores.csv",
        "_stable_patterns_families.csv",
        "_stable_patterns_compound.csv",
    ]
    for stem in stems:
        for csv_path in root.glob(f"*{stem}"):
            print_header(csv_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python3 scripts/checks/print_stable_header.py data/outputs/analysis/patterns/<STATE>"
        )
    main(Path(sys.argv[1]))
