import pandas as pd
import pytest

from alpha_analytical import stable
from alpha_analytical.stable.metrics import build_metrics
from alpha_analytical.stable.post_pass_families import build_family_summary


def _build_table(pattern_map, set_label="Set1", draw_label="Draw1"):
    rows = []
    for row_type in ["R2", "R4", "R6", "R8"]:
        row = {"RowType": row_type, "Set": set_label, "Draw": draw_label}
        for col in stable.COLS:
            row[col] = pattern_map.get(col, "")
        rows.append(row)
    return pd.DataFrame(rows)


def _build_scores(pattern_map, section="Combined"):
    df = _build_table(pattern_map)
    _, results = stable.analyse(df, section)
    return pd.DataFrame(results)


def test_build_metrics_basic():
    scores = _build_scores({"1": "227", "2": "277"})
    families = build_family_summary(scores, stable.CFG)

    metrics = build_metrics(
        state="TestState",
        df_scores=scores,
        families_df=families,
        winners=["227"],
    )

    assert metrics["state"] == "TestState"
    assert metrics["total_patterns"] == len(scores)
    assert metrics["total_families"] == len(families)
    if len(scores):
        expected_ratio = round(len(families) / len(scores), 4)
        assert metrics["compression_ratio"] == pytest.approx(expected_ratio)
    assert metrics["spotlight_rate"] == pytest.approx(1.0)
    assert metrics["winner_family_ids"], "expected at least one winner family id"
