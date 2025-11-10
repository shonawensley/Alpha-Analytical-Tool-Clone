#!/usr/bin/env python3
"""
Print the Top-5 compound patterns per section for a Stable run.

Usage:
    python3 scripts/tools/compound_top5.py data/outputs/analysis/patterns/Connecticut4/Connecticut4_stable_patterns_compound.csv
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


def show_top5(compound_csv: Path) -> None:
    if not compound_csv.exists():
        raise SystemExit(f"{compound_csv} not found")

    df = pd.read_csv(compound_csv)
    if df.empty:
        print(f"{compound_csv.name}: no compound rows")
        return

    for section in ["Midday", "Evening", "Combined"]:
        section_df = df[df["section"] == section].copy()
        if section_df.empty:
            continue
        section_df = section_df.sort_values(
            ["compound_score", "base_max_score"],
            ascending=[False, False],
        ).head(5)
        print(f"\n== {section} Top-5 ==")
        cols = [
            "Canonical",
            "compound_score",
            "base_max_score",
            "set_chain_depth",
            "draw_chain_depth",
            "col1_hits",
            "hot1_count",
            "hot2_count",
            "consensus_hits",
            "hidden3v_hits",
            "vtrac_straight_hits",
            "double_mirror_hits",
            "compound_why",
        ]
        print(section_df[cols].to_string(index=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python3 scripts/tools/compound_top5.py "
            "data/outputs/analysis/patterns/<STATE>/<STATE>_stable_patterns_compound.csv"
        )
    show_top5(Path(sys.argv[1]))
