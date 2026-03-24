from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.build_aggregated_analysis_arena import (
    build_aggregated_analysis_arena_markdown,
    build_aggregated_analysis_arena_payload,
    write_aggregated_analysis_arena_files,
)


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _build_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks"
    day_dir = sharepacks_root / "2026-03-18"
    state_key = "TestState"
    state_dir = day_dir / state_key
    analysis_dir = state_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    control_meta = {
        "results_date": "2026-03-18",
        "history_date": "2026-03-17",
        "states": [{"state_key": state_key, "winners": {"Midday": "138", "Evening": "344"}}],
    }
    (day_dir / "control_center").mkdir(parents=True, exist_ok=True)
    (day_dir / "control_center" / "meta.json").write_text(json.dumps(control_meta), encoding="utf-8")

    stable_payload = {
        "schema": "stable_arena_v1",
        "metrics_summary": {"total_patterns": 10},
        "r_consensus_context": {
            "available": True,
            "event_count": 2,
            "single_digit_count": 0,
            "two_digit_count": 2,
            "col1_count": 1,
            "col2_count": 1,
            "cons_full_event_count": 1,
            "cons_3v_event_count": 1,
            "cons_stub_event_count": 1,
            "section_counts": {"Combined": 1, "Midday": 1},
            "cross_variant_tail_values": ["38"],
            "top_tail_values": ["38", "44"],
            "top_support_canonicals": ["138", "344"],
            "top_support_vtrac_indices": ["8", "13"],
            "signal_strength_class": "strong",
            "trial_eligible": True,
            "events_top": [
                {
                    "section": "Combined",
                    "set": "Set1",
                    "draw": "Draw1",
                    "column": 1,
                    "tail_value": "38",
                    "event_class": "two-digit",
                    "cons_full": True,
                    "cons_3v": True,
                    "cons_stub": True,
                    "top_support_canonicals": ["138"],
                    "top_support_vtrac_indices": ["8"],
                }
            ],
        },
        "sections": {
            "Combined": {
                "top_row_patterns": [{"canonical": "138", "score": 19.5}],
                "top_compound_patterns": [{"canonical": "344", "compound_score": 17.0}],
                "family_rollups_top": [{"family_id": 31, "family_score_total": 41.0}],
                "survivor_frontiers": [
                    {
                        "set": "Set1",
                        "draw": "Draw1",
                        "frontier_column": 5,
                        "progression_column_count": 3,
                        "is_single_family": True,
                        "frontier_family_count": 1,
                        "entries": [{"last_remaining_3v": True}],
                        "frontier_pattern_summary": {
                            "exact3digit_patterns_all": ["138"],
                            "exact3digit_patterns_top": [{"value": "138", "count": 2}],
                            "three_value_like_patterns_all": ["138"],
                            "vtrac_indices_all": ["8"],
                            "vtrac_indices_top": [{"value": "8", "count": 2}],
                            "hidden_terminal_patterns_all": ["1138"],
                            "hidden_terminal_patterns_top": [{"value": "1138", "count": 1}],
                            "top_patterns": [{"canonical": "1138"}],
                        },
                    }
                ],
                "survivor_progressions": [
                    {
                        "set": "Set1",
                        "draw": "Draw1",
                        "eligible_columns": [3, 4, 5],
                        "progression_column_count": 3,
                        "frontier_column": 5,
                        "has_last_remaining": True,
                    }
                ],
            },
            "Evening": {"top_row_patterns": [], "top_compound_patterns": [], "family_rollups_top": []},
            "Midday": {"top_row_patterns": [], "top_compound_patterns": [], "family_rollups_top": []},
        },
        "evidence_paths": [],
    }
    (analysis_dir / "stable_arena__tool_only__stable10.json").write_text(json.dumps(stable_payload), encoding="utf-8")

    dr_payload = {
        "schema_revision": "v1.1",
        "meta": {"cluster_scan": {"max_len": 12}},
        "sections": {
            "Combined": {
                "summary": {
                    "top_candidate_preview": [
                        {"best_pattern": "138", "family_id": "31", "score_v2": 13.2},
                        {"best_pattern": "344", "family_id": "44", "score_v2": 11.1},
                    ]
                }
            }
        },
        "paths": {},
    }
    (analysis_dir / "dr_arena__tool_only__stable10.json").write_text(json.dumps(dr_payload), encoding="utf-8")

    aux_payload = {
        "available": True,
        "schema_version": "aux_control_center_arena_v1",
        "arena_objects": {
            "aux_positional_pressure": {
                "shortlist_top": [
                    {"combo": "138", "canonical": "138", "score": 27.5, "vtrac_index": 8},
                    {"combo": "344", "canonical": "344", "score": 19.0, "vtrac_index": 13},
                ]
            },
            "aux_badge_pressure": {
                "top_combo_alerts": [{"combo": "138", "canonical": "138", "draws_since": 92}],
                "index_pressure": {"by_variant": {"midday": {"top_indices": [{"index": 8, "pressure_density": 2.0}]}}},
            },
            "aux_vtrac_pressure": {"overlay_top": {"Combined": [{"index": 8, "draws_since": 122}]}}
            ,
            "aux_blackapple_context": {"control_center_top": [{"ba_score": 3, "examples": ["138"]}]},
            "cc_profit_alert_context": {
                "top_alerts": [
                    {
                        "canonical": "138",
                        "strength": 4,
                        "evidence_summary": {"stable_family_id": "31"},
                    }
                ]
            },
        },
        "inputs": [],
    }
    (analysis_dir / "aux_control_center_arena__tool_only__stable10.json").write_text(json.dumps(aux_payload), encoding="utf-8")

    signals_bundle = {"tools": {"aux_badge_pressure": {"available": False, "by_variant": {}, "midday_evening_intersection": []}}}
    (analysis_dir / "signals_bundle__tool_only__stable10.json").write_text(json.dumps(signals_bundle), encoding="utf-8")

    vtrac_dir = state_dir / "vtrac" / state_key
    vtrac_dir.mkdir(parents=True, exist_ok=True)
    vtrac_payload = {
        "state": state_key,
        "timestamp": "2026-03-18T12:00:00Z",
        "indices_ranked": [{"index": 8, "score": 9.2, "reasons": ["echo"]}, {"index": 13, "score": 8.0}],
        "straights_ranked": [
            {"straight": "138", "index": 8, "score": 8.8, "reasons": ["lane"]},
            {"straight": "344", "index": 13, "score": 7.7, "reasons": ["double"]},
        ],
        "section_summaries": {"Combined": {"top_indices": [8]}},
        "telemetry": {"weights": {"overlap": 1.0}},
    }
    (vtrac_dir / f"{state_key}_vtrac_enhanced_20260318_120000.json").write_text(json.dumps(vtrac_payload), encoding="utf-8")

    compact_payload = {
        "states": [
            {
                "state": state_key,
                "top_indices_by_state": [{"index": 8, "score": 9.4, "why": "echo"}],
                "sections": [
                    {
                        "section": "Combined",
                        "index_hint": 8,
                        "confidence_score": 9.4,
                        "tier": "A",
                        "hot_count": 4,
                        "superhot_count": 2,
                        "stable_cols_count": 3,
                        "mask_drop": True,
                        "mirror_supported": False,
                        "double_hits": 1,
                        "top_tokens": ["138"],
                        "recommended_tokens": ["138"],
                        "why": "lane",
                    }
                ],
            }
        ]
    }
    (day_dir / "vtrac_compact_report.json").write_text(json.dumps(compact_payload), encoding="utf-8")

    hot_dir = state_dir / "hot_zones" / state_key
    hot_dir.mkdir(parents=True, exist_ok=True)
    (hot_dir / f"{state_key}_hot_zones_meta.json").write_text(
        json.dumps({"state": state_key, "date": "2026-03-18", "top_rows": 12, "per_item_rows": 32}),
        encoding="utf-8",
    )
    _write_csv(
        hot_dir / f"{state_key}_hot_zones_top_lanes.csv",
        [
            {
                "triad": "138",
                "vt_triad": "134",
                "support_count": "6",
                "hot_hits": "3",
                "superhot_hits": "1",
                "vertical_hits": "4",
                "set1_hits": "2",
                "col1_hits": "1",
                "precol1_hits": "1",
                "vt_straight_hits": "1",
                "vt_only_lane_hits": "0",
                "guard_hits": "0",
                "literal_hits": "1",
                "variant_span": "3",
                "set_span": "3",
                "column_span": "4",
                "score_mean": "18.4",
                "score_max": "22.0",
                "evidence_tags": "col1,vt_straight",
            }
        ],
        [
            "triad",
            "vt_triad",
            "support_count",
            "hot_hits",
            "superhot_hits",
            "vertical_hits",
            "set1_hits",
            "col1_hits",
            "precol1_hits",
            "vt_straight_hits",
            "vt_only_lane_hits",
            "guard_hits",
            "literal_hits",
            "variant_span",
            "set_span",
            "column_span",
            "score_mean",
            "score_max",
            "evidence_tags",
        ],
    )
    _write_csv(
        hot_dir / f"{state_key}_hot_zones_per_lane.csv",
        [
            {
                "section": "Combined",
                "set_name": "Set1",
                "draw_name": "Draw1",
                "column_index": "1",
                "triad": "138",
                "vt_triad": "134",
                "vertical_support": "4",
                "horizontal_span": "5",
                "set_span": "3",
                "variant_echo": "2",
                "has_straight": "1",
                "has_vt_straight": "1",
                "vt_only_lane": "0",
                "col1_arrival": "1",
                "precol1_funnel": "1",
                "is_starred": "1",
                "star_count": "12",
                "is_superhot_slot": "1",
                "guard_injected": "0",
                "score": "22.4",
                "reasons": "col1,superhot,vt_straight",
            }
        ],
        [
            "section",
            "set_name",
            "draw_name",
            "column_index",
            "triad",
            "vt_triad",
            "vertical_support",
            "horizontal_span",
            "set_span",
            "variant_echo",
            "has_straight",
            "has_vt_straight",
            "vt_only_lane",
            "col1_arrival",
            "precol1_funnel",
            "is_starred",
            "star_count",
            "is_superhot_slot",
            "guard_injected",
            "score",
            "reasons",
        ],
    )
    (hot_dir / "2026-03-18_hot_zones_winner_map.json").write_text(
        json.dumps([{"triad": "138", "score_mean": 18.4, "support_count": 6, "evidence_tags": "col1,vt_straight"}]),
        encoding="utf-8",
    )

    candidate_payload = {"schema_version": "1.0", "union_combos_count": 24, "packs": [{"pack_id": "stable"}], "digit_envelopes": []}
    (state_dir / "candidate_universe__tool_only.json").write_text(json.dumps(candidate_payload), encoding="utf-8")
    play_payload = {
        "schema_version": "1.0",
        "ranked_candidates": [{"combo": "138", "score": 11.2}],
        "strategies": {"v0_2_default": {}, "stable10": {}},
    }
    (state_dir / "play_card__tool_only.json").write_text(json.dumps(play_payload), encoding="utf-8")

    winners_dir = state_dir / "winners" / state_key
    winners_dir.mkdir(parents=True, exist_ok=True)
    (winners_dir / "winner.html").write_text("<html></html>", encoding="utf-8")
    (winners_dir / "winner.json").write_text(json.dumps({"winner": "138"}), encoding="utf-8")

    return sharepacks_root, day_dir


def test_build_aggregated_analysis_arena_payload_from_prebuilt_and_raw_sources(tmp_path: Path) -> None:
    sharepacks_root, day_dir = _build_fixture(tmp_path)

    payload = build_aggregated_analysis_arena_payload(
        day_dir=day_dir,
        state_key="TestState",
        results_date="2026-03-18",
        history_date="2026-03-17",
        profile="tool_only",
        experiment_tag="arena_v0",
        sharepacks_root=sharepacks_root,
        repo_root=tmp_path,
        top_items=8,
    )

    assert payload["schema_version"] == "aggregated_analysis_arena_v0"
    assert payload["metadata"]["contains_winners_artifacts"] is True
    assert payload["string_tools"]["stable"]["available"] is True
    assert payload["string_tools"]["stable"]["source_mode"] == "loaded_prebuilt"
    assert payload["string_tools"]["vtrac_analyzer"]["available"] is True
    assert payload["string_tools"]["hot_zones"]["available"] is True
    assert payload["context_tools"]["aux_control_center"]["available"] is True

    dominant_canonicals = payload["arena_synthesis"]["dominant_canonicals"]
    assert dominant_canonicals
    assert dominant_canonicals[0]["value"] == "138"
    assert dominant_canonicals[0]["string_source_count"] > 0
    assert dominant_canonicals[0]["context_source_count"] > 0

    dominant_indices = payload["arena_synthesis"]["dominant_vtrac_indices"]
    assert dominant_indices
    assert dominant_indices[0]["value"] == "8"
    stable_survivor_context = payload["arena_synthesis"]["stable_survivor_context"]
    assert stable_survivor_context["available"] is True
    assert stable_survivor_context["top_frontier_canonicals"][0] == "138"
    assert stable_survivor_context["top_last_remaining_canonicals"][0] == "138"
    assert stable_survivor_context["top_hidden_terminal_patterns"][0] == "1138"
    watchlist = payload["arena_synthesis"]["vtrac_literal_watchlist"]
    assert watchlist
    assert watchlist[0]["vtrac_index"] == "8"
    assert "138" in watchlist[0]["candidate_canonicals"]
    assert payload["arena_synthesis"]["state_regime"]["survivor_pressure"] is True
    assert payload["arena_synthesis"]["state_regime"]["last_remaining"] is True
    assert payload["arena_synthesis"]["state_regime"]["hidden_terminal_support"] is True
    assert payload["arena_synthesis"]["state_regime"]["vtrac_alignment"] == "aligned"
    r_consensus_context = payload["arena_synthesis"]["r_consensus_context"]
    assert r_consensus_context["available"] is True
    assert r_consensus_context["event_count"] == 2
    assert r_consensus_context["top_tail_values"][0] == "38"
    assert payload["arena_synthesis"]["state_regime"]["tail_consensus_present"] is True
    assert payload["arena_synthesis"]["state_regime"]["tail_consensus_value"] == "38"
    assert payload["arena_synthesis"]["state_regime"]["consensus_trial_eligible"] is True

    md = build_aggregated_analysis_arena_markdown(payload)
    assert "Aggregated Analysis Arena" in md
    assert "Dominant Canonicals" in md
    assert "Dominant VTRAC Indices" in md
    assert "VTRAC Literal Watchlist" in md
    assert "Stable Survivor Context" in md
    assert "R-Consensus Context" in md

    out_json = day_dir / "TestState" / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json"
    json_path, md_path = write_aggregated_analysis_arena_files(out_json_path=out_json, payload=payload, write_md=True)
    assert json_path.exists()
    assert md_path is not None and md_path.exists()
