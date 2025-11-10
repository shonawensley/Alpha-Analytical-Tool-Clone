#!/usr/bin/env python3
"""
Validate the Stable Pattern extractor schema/feature contract.

Usage:
    python3 scripts/checks/validate_stable_schema.py
    python3 scripts/checks/validate_stable_schema.py --states Connecticut4 Delaware4

The script checks that each state's scores/families CSVs still export the
expected columns, that boolean/star fields stay within valid ranges, and
that section tags only include Midday/Evening/Combined. It exits with a
non-zero status if any required artifact is missing or a contract check fails.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import json
from typing import Iterable

import pandas as pd


REQUIRED_ROW_COLS = [
    "section",
    "Set",
    "Draw",
    "Column",
    "Canonical",
    "type",
    "score",
    "rows",
    "mirror",
    "straight2",
    "straight3",
    "single_left",
    "cons_full",
    "cons_3v",
    "cons_stub",
    "dom_last",
    "dom_pair",
    "hot",
    "perm_count_in_box",
    "repeat_extras_in_box",
    "horizontal_persistence_repeat",
    "orders_modal_value",
    "orders_modal_rows",
    "family_id",
    "hidden3v",
    "score_cov",
    "score_hpr",
    "score_perm",
    "score_repeat",
    "score_straight",
    "score_single",
    "score_cons",
    "score_hot",
    "score_mirror",
    "score_dom",
    "score_len",
    "score_hidden",
    "score_vtrac_straight",
    "score_persistence_set",
    "score_persistence_draw",
    "persistence_set_count",
    "persistence_draw_run",
    "score_double_mirror",
    "double_mirror",
    "why",
]

ROW_BOOL_COLS = [
    "single_left",
    "cons_full",
    "cons_3v",
    "dom_last",
    "dom_pair",
    "hidden3v",
    "double_mirror",
]

STAR_COL = "hot"

REQUIRED_FAMILY_COLS = [
    "section",
    "Set",
    "Draw",
    "Column",
    "family_id",
    "rows_cov",
    "perm_count_in_box",
    "repeat_extras_in_box",
    "horizontal_persistence_repeat",
    "hot_density",
    "any_straight2",
    "any_straight3",
    "any_consensus",
    "any_dom_last",
    "any_doubles_support",
    "any_vtrac_straight",
    "any_hidden3v",
    "max_persistence_set",
    "max_persistence_draw",
    "persistence_set_count",
    "persistence_draw_run",
    "hidden3v_hits",
    "hot1_count",
    "hot2_count",
    "consensus_hits",
    "top_canonicals",
    "top_modal_orders",
    "fam_cov",
    "fam_hpr",
    "fam_perm",
    "fam_repeat",
    "fam_cons",
    "fam_hot",
    "fam_straight2",
    "fam_straight3",
    "fam_doubles",
    "fam_vtrac",
    "fam_hidden",
    "fam_double_mirror",
    "fam_persistence",
    "fam_section_bonus",
    "fam_progression_bonus",
    "fam_last_remaining_bonus",
    "family_score",
    "best_compound_score",
    "section_count",
    "progression_flag",
    "last_remaining_3v",
]

FAMILY_BOOL_COLS = [
    "any_straight2",
    "any_straight3",
    "any_consensus",
    "any_dom_last",
    "any_doubles_support",
    "any_vtrac_straight",
    "any_hidden3v",
]

VALID_SECTIONS = {"Midday", "Evening", "Combined"}
VALID_BOOL_VALUES = {True, False, 1, 0}
VALID_STAR_VALUES = {0, 1, 2}
REQUIRED_COMPOUND_COLS = [
    "section",
    "Canonical",
    "family_id",
    "compound_score",
    "base_max_score",
    "set_chain_depth",
    "draw_chain_depth",
    "hot1_count",
    "hot2_count",
    "col1_hits",
    "consensus_hits",
    "hidden3v_hits",
    "vtrac_straight_hits",
    "double_mirror_hits",
    "rows_covered",
    "examples",
    "compound_why",
]
REQUIRED_METRIC_KEYS = [
    "winners",
    "winner_family_ids",
    "winner_family_best_rank",
    "best_compound_rank",
    "compound_schema_version",
    "signals",
]


def _bool_column_ok(series: pd.Series) -> bool:
    if series.empty:
        return True
    return series.dropna().map(lambda v: v in VALID_BOOL_VALUES).all()


def validate_scores(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path} is missing"]

    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_ROW_COLS if col not in df.columns]
    if missing:
        errors.append(f"{path.name}: missing columns {missing}")

    if STAR_COL in df.columns:
        star_values = set(df[STAR_COL].dropna().unique())
        if not star_values <= VALID_STAR_VALUES:
            errors.append(f"{path.name}: hot column has invalid values {sorted(star_values)}")

    for col in ROW_BOOL_COLS:
        if col in df.columns and not _bool_column_ok(df[col]):
            errors.append(f"{path.name}: column '{col}' is not boolean-like")

    if "section" in df.columns:
        invalid_sections = set(df["section"].dropna().unique()) - VALID_SECTIONS
        if invalid_sections:
            errors.append(f"{path.name}: unexpected sections {sorted(invalid_sections)}")

    return errors


def validate_families(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path} is missing"]

    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_FAMILY_COLS if col not in df.columns]
    if missing:
        errors.append(f"{path.name}: missing columns {missing}")

    if "section" in df.columns:
        invalid_sections = set(df["section"].dropna().unique()) - VALID_SECTIONS
        if invalid_sections:
            errors.append(f"{path.name}: unexpected sections {sorted(invalid_sections)}")

    for col in FAMILY_BOOL_COLS:
        if col in df.columns and not _bool_column_ok(df[col]):
            errors.append(f"{path.name}: column '{col}' is not boolean-like")

    return errors


def validate_compound(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path} is missing"]
    df = pd.read_csv(path)
    missing = [col for col in REQUIRED_COMPOUND_COLS if col not in df.columns]
    if missing:
        errors.append(f"{path.name}: missing columns {missing}")
    if "section" in df.columns:
        invalid_sections = set(df["section"].dropna().unique()) - VALID_SECTIONS
        if invalid_sections:
            errors.append(f"{path.name}: unexpected sections {sorted(invalid_sections)}")
    return errors


def validate_metrics(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path} is missing"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path.name}: unable to parse JSON ({exc})"]
    missing = [key for key in REQUIRED_METRIC_KEYS if key not in data]
    if missing:
        errors.append(f"{path.name}: missing keys {missing}")
    return errors


def iter_states(states: Iterable[str] | None) -> list[str]:
    patterns_root = Path("data/outputs/analysis/patterns")
    if states:
        return list(states)
    if not patterns_root.exists():
        return []
    return sorted([p.name for p in patterns_root.iterdir() if p.is_dir()])


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Stable Pattern schema/feature contract.")
    parser.add_argument(
        "--states",
        nargs="+",
        help="Specific states to validate (default: all directories under data/outputs/analysis/patterns)",
    )
    args = parser.parse_args()

    states = iter_states(args.states)
    if not states:
        print("No states found under data/outputs/analysis/patterns", file=sys.stderr)
        sys.exit(1)

    any_errors = False
    for state in states:
        base = Path("data/outputs/analysis/patterns") / state
        scores_path = base / f"{state}_stable_patterns_scores.csv"
        fam_path = base / f"{state}_stable_patterns_families.csv"
        compound_path = base / f"{state}_stable_patterns_compound.csv"
        metrics_path = base / f"{state}_metrics.json"

        state_errors = validate_scores(scores_path)
        state_errors += validate_families(fam_path)
        state_errors += validate_compound(compound_path)
        state_errors += validate_metrics(metrics_path)

        if state_errors:
            any_errors = True
            print(f"[FAIL] {state}")
            for msg in state_errors:
                print(f"  - {msg}")
        else:
            print(f"[PASS] {state}")

    if any_errors:
        sys.exit(2)


if __name__ == "__main__":
    main()
