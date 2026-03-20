from __future__ import annotations

import pandas as pd

from scripts.tools.audit_aux_control_center_parity import (
    _diff_json,
    _infer_limit,
    _normalize_df_rows,
    _summary_signature,
)


def test_summary_signature_keeps_only_audit_relevant_sections() -> None:
    summary = {
        "draw_sources": {
            "snapshot_meta": {
                "mode": "generated_from_excel",
                "ok": True,
                "excel_path": "data/history/Pick3StatsC4_2025_12_30.xlsm",
                "state_key": "NewJersey4",
                "aux_state_label": "New Jersey",
                "ignored": "drop-me",
            },
            "live": {"combined": {"resolved_path": "/tmp/live.csv"}},
        },
        "config": {"max_n_used": 1000},
        "repeat_watch": {"combined": {"current_index": 18}},
        "positional": {"hard_due_by_variant": {"combined": []}},
        "doubles": {"top_by_variant": {"combined": [{"combo": "113"}]}},
        "pairs": {"top_by_variant": {"combined": {"repeating": [{"pair": "11"}], "non_repeating": []}}},
        "vtrac": {"overlay_top": {"combined": [{"index": 18}]}, "heatboard_top": {}},
        "sums": {"top_by_variant": {"combined": [{"sum": 9}]}},
        "blackapple": {"by_variant": {"combined": {"score": 3}}},
    }

    sig = _summary_signature(summary)

    assert sig["snapshot_meta"]["mode"] == "generated_from_excel"
    assert "ignored" not in sig["snapshot_meta"]
    assert "live" not in sig
    assert sig["repeat_watch"]["combined"]["current_index"] == 18


def test_infer_limit_uses_largest_top_list() -> None:
    summary = {
        "doubles": {"top_by_variant": {"combined": [{"combo": "113"}, {"combo": "224"}]}},
        "pairs": {"top_by_variant": {"combined": {"repeating": [{"pair": "11"}], "non_repeating": []}}},
        "vtrac": {"overlay_top": {"combined": [{"index": 18}, {"index": 23}, {"index": 31}]}, "heatboard_top": {}},
        "sums": {"top_by_variant": {"combined": [{"sum": 9}]}},
        "blackapple": {"top_by_variant": {"combined": [{"combo": "138"}, {"combo": "344"}]}},
    }
    assert _infer_limit(summary) == 3


def test_normalize_df_rows_filters_state_and_sorts() -> None:
    df = pd.DataFrame(
        [
            {"StateKey": "B", "Flag": False, "Score": 2.0},
            {"StateKey": "A", "Flag": True, "Score": 3.5},
            {"StateKey": "A", "Flag": False, "Score": 1.0},
        ]
    )

    rows = _normalize_df_rows(df, state_key="A")

    assert rows == [
        {"StateKey": "A", "Flag": "False", "Score": "1"},
        {"StateKey": "A", "Flag": "True", "Score": "3.5"},
    ]


def test_diff_json_reports_nested_mismatch_path() -> None:
    diffs = _diff_json({"a": {"b": [1, 2]}}, {"a": {"b": [1, 3]}})
    assert diffs == ["a.b[1]: 2 != 3"]
