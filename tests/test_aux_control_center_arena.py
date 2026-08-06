from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.aux_control_center_arena import (
    build_aux_control_center_arena_payload,
    build_aux_control_center_markdown,
    build_aux_control_center_signals,
    write_aux_control_center_files,
)


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _build_aux_cc_fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks" / "_predictive"
    day_dir = sharepacks_root / "2026-03-15"
    state_key = "TestState"
    state_dir = day_dir / state_key
    aux_dir = state_dir / "aux" / state_key
    aux_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "positional": {
            "hard_due_by_variant": {
                "combined": [{"position": 0, "digit": 6, "draws_since": 42}],
                "evening": [{"position": 2, "digit": 8, "draws_since": 57}],
            },
            "shortlist_report": {
                "schema_version": "positional_shortlist_report_v2",
                "source_scope": "STATE",
                "variant_scope": ["combined", "midday", "evening"],
                "context_receipt": {
                    "due_doubles": {
                        "input_available": False,
                        "active": False,
                    },
                    "vtrac_hot_indices": {
                        "input_available": False,
                        "values": [],
                    },
                    "vtrac_hot_families": {
                        "input_available": False,
                        "values": {},
                    },
                    "any_optional_context_applied": False,
                },
                "variant_top_digits": {
                    "combined": [{"position": 0, "digit": 6, "gap": 42, "rank": 1}],
                    "midday": [{"position": 0, "digit": 0, "gap": 31, "rank": 1}],
                    "evening": [{"position": 2, "digit": 8, "gap": 57, "rank": 1}],
                },
                "variant_position_grid": {
                    "midday": {
                        "draws_used": 150,
                        "window": 150,
                        "positions": {
                            "0": {
                                "position": 0,
                                "population": 10,
                                "window": 150,
                                "top_digits": [
                                    {
                                        "digit": 0,
                                        "rank": 1,
                                        "gap": 31,
                                        "gap_percentile": 0.82,
                                        "lag_weight": 0.88,
                                        "occurrence_count": 15,
                                        "last_seen_index": 31,
                                        "score": 3.7,
                                        "score_components": {
                                            "lag": 2.5,
                                            "rank": 1.2,
                                        },
                                        "tags": ["R1"],
                                        "hard_due": False,
                                    },
                                    {
                                        "digit": 5,
                                        "rank": 2,
                                        "gap": 22,
                                        "gap_percentile": 0.61,
                                        "lag_weight": 0.63,
                                        "occurrence_count": 14,
                                        "last_seen_index": 22,
                                        "score": 2.1,
                                        "score_components": {"lag": 2.1},
                                        "tags": ["Mirror-Echo"],
                                        "hard_due": False,
                                    },
                                ],
                            }
                        },
                    }
                },
                "aggregated_position_ladders": {
                    "0": [
                        {
                            "rank": 1,
                            "digit": 0,
                            "score": 3.7,
                            "tags": ["R1"],
                            "occurrences": [
                                {
                                    "variant": "midday",
                                    "rank": 1,
                                }
                            ],
                        }
                    ]
                },
                "aggregated_digits": {
                    "0": [
                        {"digit": 0, "score": 3.7, "tags": ["R1"], "occurrences": [["midday", 1]]},
                        {"digit": 6, "score": 3.2, "tags": ["R1"], "occurrences": [["combined", 1]]},
                    ],
                    "2": [{"digit": 8, "score": 4.1, "tags": ["R2"], "occurrences": [["evening", 1]]}],
                },
                "candidates": [
                    {
                        "rank": 1,
                        "combo": "638",
                        "canonical": "368",
                        "score": 39.1,
                        "source": "cartesian",
                        "vtrac_index": 23,
                        "native_ranks": [1, 1, 2],
                        "digital_root": 8,
                        "tags": ["XVAR-Cons"],
                        "evidence": ["P1:6", "P2:3", "P3:8"],
                        "lineage": {
                            "source_family": "aux_positional",
                            "source_object": "state_shortlist",
                            "state_key": "TestState",
                            "native_rank": 1,
                            "construction_source": "cartesian",
                        },
                    },
                    {
                        "rank": 2,
                        "combo": "344",
                        "canonical": "344",
                        "score": 31.6,
                        "source": "cartesian",
                        "vtrac_index": 34,
                        "native_ranks": [2, 1, 1],
                        "digital_root": 2,
                        "tags": ["Double-Pressure"],
                        "evidence": ["P1:3", "P2:4", "P3:4"],
                        "lineage": {
                            "source_family": "aux_positional",
                            "source_object": "state_shortlist",
                            "state_key": "TestState",
                            "native_rank": 2,
                            "construction_source": "cartesian",
                        },
                    },
                ],
                "consensus_notes": ["P1 digit 6 aligns across Combined, Evening"],
                "double_pressure_notes": ["Digit 3 (mirror 8) pressuring two positions"],
            },
        },
        "pairs": {
            "top_by_variant": {
                "combined": {
                    "repeating": [{"pair": "11", "draws_since": 98, "severity": "blue"}],
                    "non_repeating": [{"pair": "16", "draws_since": 35, "severity": "purple"}],
                },
                "evening": {
                    "repeating": [{"pair": "77", "draws_since": 52, "severity": "purple"}],
                    "non_repeating": [{"pair": "23", "draws_since": 92, "severity": "red"}],
                },
            },
            "multi_variant_alerts": {
                "11": {"combined": {"severity": "blue", "draws_since": 98}, "evening": {"severity": "purple", "draws_since": 49}},
            },
        },
        "doubles": {
            "top_by_variant": {
                "combined": [{"combo": "445", "draws_since": 956, "severity": "B"}],
                "evening": [{"combo": "036", "draws_since": 796, "severity": "B"}],
            },
            "multi_variant_alerts": {
                "036": {"combined": {"draws_since": 935, "severity": "B"}, "evening": {"draws_since": 796, "severity": "B"}},
            },
        },
        "sums": {
            "top_by_variant": {
                "combined": [{"sum": 9, "draws_since": 41, "z": 1.7, "z_tail": 1.6, "flags": {"blue": True, "red": False, "purple": False}}],
            },
        },
        "repeat_watch": {
            "combined": {"current_index": 23, "current_streak": 2, "last_repeat_gap": 17, "last_repeat_index": 18, "max_streak": 4, "window": 250},
        },
        "vtrac": {
            "overlay_top": {"combined": [{"index": 23, "draws_since": 220}], "evening": [{"index": 34, "draws_since": 199}]},
            "heatboard_top": {"combined": [{"index": 23, "ds": 220, "hazard": 0.02, "trend": 3}]},
        },
        "blackapple": {
            "by_variant": {
                "combined": {
                    "score": 3,
                    "triggers": {"mirror": True, "root_due": [4], "pattern": {"extreme_due": False}, "floating": [1, 3, 6, 9], "pairs": {"remaining_count": 1}},
                    "candidates": [{"combo": "138", "score": 3, "tags": ["FLT", "RS"]}],
                }
            }
        },
    }
    (aux_dir / "summary.json").write_text(json.dumps(summary), encoding="utf-8")

    cc_dir = day_dir / "control_center"
    cc_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        cc_dir / "due_doubles.csv",
        [
            {
                "State": "Test",
                "StateKey": state_key,
                "Variant": "Evening",
                "Draws Since Double": "7",
                "Family 1": "3/8-4/9: 344(BC:724) 488(BM:685)",
                "Family 2": "1/6-3/8: 188(BM:903) 668(BE:812)",
            }
        ],
        ["State", "StateKey", "Variant", "Draws Since Double", "Family 1", "Family 2"],
    )
    _write_csv(
        cc_dir / "vtrac_repeat_watch.csv",
        [
            {
                "State": "Test",
                "StateKey": state_key,
                "Variant": "Evening",
                "Current Index": "34",
                "Current Streak": "1",
                "Heat Index": "23",
                "Heat Hazard": "0.059",
                "Last Repeat (draws)": "17",
                "Max Streak": "4",
            }
        ],
        ["State", "StateKey", "Variant", "Current Index", "Current Streak", "Heat Index", "Heat Hazard", "Last Repeat (draws)", "Max Streak"],
    )
    _write_csv(
        cc_dir / "blackapple_alerts.csv",
        [
            {
                "State": "Test",
                "StateKey": state_key,
                "Variant": "Evening",
                "BA-Score": "3",
                "Status": "ALERT",
                "Triggers": "Mirror, Root 2",
                "#Candidates": "12",
                "Examples": "138 344 368",
            }
        ],
        ["State", "StateKey", "Variant", "BA-Score", "Status", "Triggers", "#Candidates", "Examples"],
    )
    _write_csv(
        cc_dir / "profit_alerts.csv",
        [
            {
                "State": "Test",
                "StateKey": state_key,
                "Variant": "Evening",
                "AlertId": "A04",
                "Strength": "3",
                "Suggested": "BOX",
                "CapLines": "12",
                "DecayDraws": "3",
                "Badges": "PERSIST/BA",
                "Canonical": "138",
                "ImpliedSet": "[\"138\", \"183\", \"318\"]",
                "Evidence": json.dumps({"persistence_set_count": 3, "rowcov": 4, "ba_score": 2, "stable_family_id": "23.0", "stable_section": "Evening"}),
            }
        ],
        ["State", "StateKey", "Variant", "AlertId", "Strength", "Suggested", "CapLines", "DecayDraws", "Badges", "Canonical", "ImpliedSet", "Evidence"],
    )
    _write_csv(
        cc_dir / "profit_compound_events.csv",
        [
            {
                "results_date": "2026-03-15",
                "state_key": state_key,
                "variant": "Evening",
                "top_event": "STRAIGHT_GATE",
                "priority": "80",
                "watchlist_tags": "STRAIGHT_GATE",
                "candidate_alert_ids": "A04,A11",
                "promoter_alert_ids": "A08",
                "strength_max": "4",
                "merged_rows_total": "3",
            }
        ],
        ["results_date", "state_key", "variant", "top_event", "priority", "watchlist_tags", "candidate_alert_ids", "promoter_alert_ids", "strength_max", "merged_rows_total"],
    )
    (cc_dir / "meta.json").write_text(json.dumps({"history_excel_path": "data/history/Pick3StatsC4_2026-03-14.xlsm"}), encoding="utf-8")

    return repo_root, day_dir, state_dir


def test_build_aux_control_center_arena_payload(tmp_path: Path) -> None:
    repo_root, day_dir, state_dir = _build_aux_cc_fixture(tmp_path)

    payload = build_aux_control_center_arena_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key="TestState",
        results_date="2026-03-15",
        history_date="2026-03-14",
        profile="tool_only",
        experiment_tag="stable10",
        sharepacks_root=repo_root / "sharepacks" / "_predictive",
        contains_winners_artifacts=False,
        repo_root=repo_root,
        badge_pressure={
            "available": True,
            "evidence_paths": [],
            "by_variant": {"evening": {"top_indices": [{"index": 23, "pressure_density": 2.0, "pressure_raw": 8}]}},
            "midday_evening_intersection": [23],
        },
        top_items=4,
    )

    assert payload["available"] is True
    assert payload["schema_version"] == "aux_control_center_arena_v1"
    assert "aux_positional_pressure" in payload["arena_objects"]
    positional = payload["arena_objects"]["aux_positional_pressure"]
    assert positional["source_contract"] == "positional_shortlist_report_v2"
    assert positional["shortlist_top"][0]["canonical"] == "368"
    assert positional["shortlist_full"][0]["rank"] == 1
    assert positional["shortlist_full"][0]["vtrac_index"] == 23
    assert positional["shortlist_full"][0]["native_ranks"] == [1, 1, 2]
    assert positional["shortlist_full"][0]["evidence"] == [
        "P1:6",
        "P2:3",
        "P3:8",
    ]
    assert (
        positional["shortlist_full"][0]["lineage"]["source_family"]
        == "aux_positional"
    )
    assert (
        positional["variant_position_grid"]["Midday"]["positions"]["0"][
            "top_digits"
        ][0]["digit"]
        == "0"
    )
    assert positional["aggregated_digits_top"]["0"][0]["digit"] == "0"
    assert positional["context_receipt"]["due_doubles"]["input_available"] is False
    assert payload["arena_objects"]["aux_badge_pressure"]["index_pressure"]["available"] is True
    assert payload["arena_objects"]["aux_due_doubles_family_pressure"]["by_variant"]["Evening"]["draws_since_double"] == 7
    assert payload["arena_objects"]["cc_profit_alert_context"]["alert_count"] == 1
    assert payload["arena_objects"]["cc_compound_event_context"]["top_events"][0]["top_event"] == "STRAIGHT_GATE"

    signal = build_aux_control_center_signals(payload)
    assert signal["available"] is True
    assert "arena_objects" in signal

    md = build_aux_control_center_markdown(payload)
    assert "Aux + Control Center Arena" in md
    assert "Profit Alerts + Compound Events" in md

    out_json = state_dir / "analysis" / "aux_control_center_arena.json"
    arena_json, arena_md = write_aux_control_center_files(out_json_path=out_json, payload=payload, write_md=True)
    assert arena_json.exists()
    assert arena_md is not None and arena_md.exists()
