import json

from scripts.tools.create_vtrac_corridor_summary import create_corridor_summary, render_markdown


def _write_json(path, payload):
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_corridor_summary_separates_ordered_lane_from_boxed_corridor(tmp_path):
    winner_json = tmp_path / "winner.json"
    enhanced_json = tmp_path / "enhanced.json"
    _write_json(
        winner_json,
        {
            "state": "Connecticut4",
            "winner_combo": "091",
            "index": 9,
            "legend": {},
            "patterns": {},
            "tables": {
                "Evening": [
                    {
                        "Set": "Set1",
                        "Draw": "Draw1",
                        "RowType": "R2",
                        "cells": {
                            "1": {"text": "591", "tags": []},
                            "2": {"text": "096", "tags": []},
                            "3": {"text": "901", "tags": ["hit-family"]},
                            "4": {"text": "019", "tags": ["hit-winner"]},
                            "5": {"text": "123", "tags": []},
                            "6": {"text": "N/A", "tags": []},
                            "7": {"text": "", "tags": []},
                        },
                    }
                ]
            },
        },
    )
    _write_json(
        enhanced_json,
        {
            "indices_ranked": [
                {
                    "index": 9,
                    "score": 27.0,
                    "evidence": {
                        "raw": {
                            "presence_score": 16.0,
                            "sections": ["Evening"],
                            "set_presence": ["Set1"],
                            "total_hits": 4,
                            "order_counts": {"901": 2.0, "019": 1.0},
                        }
                    },
                }
            ],
            "straights_ranked": [
                {"index": 9, "straight": "901", "score": 12.0},
                {"index": 9, "straight": "019", "score": 10.0},
            ],
        },
    )

    summary = create_corridor_summary(
        winner_json_path=winner_json,
        enhanced_json_path=enhanced_json,
        date="2026-03-09",
        state="Connecticut4",
        winner="091",
    )

    assert summary["case"]["ordered_vcode"] == "v152"
    assert summary["case"]["ordered_lane_8"] == ["041", "046", "091", "096", "541", "546", "591", "596"]
    assert summary["case"]["boxed_corridor_size"] == 48
    assert summary["winner_json_evidence"]["ordered_lane_exposure"]["strict_cell_hits"] == 2
    assert summary["winner_json_evidence"]["boxed_index_corridor_exposure"]["strict_cell_hits"] == 4
    assert summary["interpretation_flags"]["renderer_gap"] is True
    assert summary["interpretation_flags"]["analyzer_gap"] is True
    assert summary["enhanced_vtrac_comparison"]["top_corridor_straights"] == ["901", "019"]
    assert summary["enhanced_vtrac_comparison"]["top_ordered_lane_straights"] == []


def test_corridor_summary_markdown_marks_review_only(tmp_path):
    winner_json = tmp_path / "winner.json"
    _write_json(
        winner_json,
        {
            "state": "Demo4",
            "winner_combo": "246",
            "index": 23,
            "tables": {
                "Combined": [
                    {
                        "Set": "Set1",
                        "Draw": "Draw1",
                        "RowType": "R4",
                        "cells": {
                            "1": {"text": "246", "tags": []},
                            "2": {"text": "791", "tags": []},
                            "3": {"text": "741", "tags": []},
                            "4": {"text": "", "tags": []},
                            "5": {"text": "", "tags": []},
                            "6": {"text": "", "tags": []},
                            "7": {"text": "", "tags": []},
                        },
                    }
                ]
            },
        },
    )

    summary = create_corridor_summary(winner_json_path=winner_json, winner="246")
    md = render_markdown(summary)

    assert summary["case"]["ordered_vcode"] == "v352"
    assert "246" in summary["case"]["ordered_lane_8"]
    assert "791" in summary["case"]["ordered_lane_8"]
    assert "741" in summary["case"]["ordered_lane_8"]
    assert "Review-only diagnostic" in md
    assert "Ordered VSTRAIGHTS lane: `v352`" in md


def test_corridor_summary_splits_pattern_rows_from_draw_data(tmp_path):
    winner_json = tmp_path / "winner.json"
    _write_json(
        winner_json,
        {
            "state": "Demo4",
            "winner_combo": "091",
            "index": 9,
            "tables": {
                "Evening": [
                    {
                        "Set": "Set1",
                        "Draw": "Draw1",
                        "RowType": "R2",
                        "cells": {
                            "1": {"text": "096", "tags": []},
                            "2": {"text": "901", "tags": []},
                            "3": {"text": "", "tags": []},
                            "4": {"text": "", "tags": []},
                            "5": {"text": "", "tags": []},
                            "6": {"text": "", "tags": []},
                            "7": {"text": "", "tags": []},
                        },
                    },
                    {
                        "Set": "Set1",
                        "Draw": "Draw1",
                        "RowType": "draw_data",
                        "cells": {
                            "1": {"text": "591", "tags": []},
                            "2": {"text": "019", "tags": []},
                            "3": {"text": "", "tags": []},
                            "4": {"text": "", "tags": []},
                            "5": {"text": "", "tags": []},
                            "6": {"text": "", "tags": []},
                            "7": {"text": "", "tags": []},
                        },
                    },
                ]
            },
        },
    )

    summary = create_corridor_summary(winner_json_path=winner_json, winner="091")
    scopes = summary["winner_json_evidence"]["row_scope_breakout"]
    ordered = scopes["ordered_lane_exposure"]
    corridor = scopes["boxed_index_corridor_exposure"]

    assert ordered["pattern_rows_only"]["strict_cell_hits"] == 1
    assert ordered["draw_data_only"]["strict_cell_hits"] == 1
    assert ordered["all_rows_inclusive"]["strict_cell_hits"] == 2
    assert corridor["pattern_rows_only"]["strict_cell_hits"] == 2
    assert corridor["draw_data_only"]["strict_cell_hits"] == 2
    assert corridor["all_rows_inclusive"]["strict_cell_hits"] == 4
    assert summary["interpretation_flags"]["pattern_row_corridor_present"] is True
    assert summary["interpretation_flags"]["draw_data_corridor_support"] is True
    assert summary["interpretation_flags"]["draw_data_inflation_warning"] is True
