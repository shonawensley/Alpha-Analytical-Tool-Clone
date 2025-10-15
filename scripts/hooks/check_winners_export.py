#!/usr/bin/env python
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.dont_write_bytecode = True
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

REQUIRED_COLUMNS = {
    "stable_winner",
    "stable_canonical",
    "family_id",
    "family_score",
    "family_rank",
    "section_count",
    "progression_flag",
    "last_remaining_3v",
    "any_doubles_support",
    "row_score",
    "row_type",
    "row_rows",
    "row_why",
}

BOOLEAN_COLUMNS = {
    "progression_flag",
    "last_remaining_3v",
    "any_doubles_support",
    "mirror",
    "straight2",
    "straight3",
    "single_left",
    "cons_full",
    "cons_3v",
    "dom_last",
    "dom_pair",
    "hidden3v",
}


def _build_sample_frames() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    winners = pd.DataFrame(
        [
            {"Winner": "227", "state": "TestState"},
        ]
    )
    families = pd.DataFrame(
        [
            {
                "family_id": 12,
                "family_score": 42,
                "family_rank": 1,
                "section_count": 3,
                "progression_flag": True,
                "last_remaining_3v": False,
                "any_doubles_support": True,
                "hot_density": 0.42,
            }
        ]
    )
    scores = pd.DataFrame(
        [
            {
                "Canonical": "227",
                "score": 12.5,
                "type": "straight",
                "rows": "R2,R4,R6",
                "why": "consensus",
                "cons_full": True,
                "mirror": False,
                "straight2": True,
                "straight3": False,
                "single_left": False,
                "cons_3v": False,
                "dom_last": False,
                "dom_pair": False,
                "hidden3v": False,
            }
        ]
    )
    return winners, families, scores


def main() -> int:
    try:
        from alpha_analytical.stable.winners_enrich import attach_stable_evidence
    except Exception as exc:  # pragma: no cover - guard should fail loudly
        sys.stderr.write(f"[check_winners_export] Unable to import stable winners enrich module: {exc}\n")
        return 1

    winners, families, scores = _build_sample_frames()
    enriched = attach_stable_evidence(
        winners,
        families_df=families,
        scores_df=scores,
    )

    missing = REQUIRED_COLUMNS - set(enriched.columns)
    if missing:
        sys.stderr.write(f"[check_winners_export] Missing columns: {sorted(missing)}\n")
        return 1

    for column in BOOLEAN_COLUMNS & set(enriched.columns):
        if str(enriched[column].dtype) != "boolean":
            sys.stderr.write(f"[check_winners_export] Column '{column}' is not nullable boolean dtype.\n")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
