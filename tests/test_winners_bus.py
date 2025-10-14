import pandas as pd
import pytest

from alpha_analytical import stable
from alpha_analytical.stable.post_pass_families import build_family_summary
from alpha_analytical.stable.winners_enrich import attach_stable_evidence


def _build_scores(pattern_map, section="Combined"):
    rows = []
    for row_type in ["R2", "R4", "R6", "R8"]:
        row = {"RowType": row_type, "Set": "Set1", "Draw": "Draw1"}
        for col in stable.COLS:
            row[col] = pattern_map.get(col, "")
        rows.append(row)
    df = pd.DataFrame(rows)
    _, results = stable.analyse(df, section)
    return pd.DataFrame(results)


def test_attach_stable_evidence(tmp_path):
    scores = _build_scores({"1": "227", "2": "277"})
    families = build_family_summary(scores, stable.CFG)

    scores_path = tmp_path / "scores.csv"
    scores.to_csv(scores_path, index=False)
    families_path = tmp_path / "families.csv"
    families.to_csv(families_path, index=False)

    winners = pd.DataFrame([{"Winner": "227"}])
    enriched = attach_stable_evidence(
        winners,
        families_path=families_path,
        scores_path=scores_path,
    )

    assert "family_id" in enriched.columns
    assert not enriched["family_id"].isna().all()
    assert "family_rank" in enriched.columns
    assert "row_score" in enriched.columns
    assert bool(enriched["any_doubles_support"].iloc[0]) is True
    assert enriched["stable_canonical"].iloc[0] == "227"
