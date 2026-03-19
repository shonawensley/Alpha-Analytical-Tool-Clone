from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.build_aggregated_analysis_arena import build_aggregated_analysis_arena_payload, write_aggregated_analysis_arena_files
from scripts.tools.review_aggregated_analysis_arena_decay import build_decay_rows


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _build_snapshot_fixture(tmp_path: Path) -> tuple[Path, str]:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks"
    state_key = "TestState"

    day1 = sharepacks_root / "2026-03-18"
    state_dir = day1 / state_key
    analysis_dir = state_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)
    (day1 / "control_center").mkdir(parents=True, exist_ok=True)
    (day1 / "control_center" / "meta.json").write_text(
        json.dumps(
            {
                "history_date": "2026-03-17",
                "states": [{"state_key": state_key, "winners": {"Midday": "000", "Evening": "111"}}],
            }
        ),
        encoding="utf-8",
    )

    stable_dir = state_dir / "stable" / state_key
    stable_dir.mkdir(parents=True, exist_ok=True)
    (stable_dir / f"{state_key}_metrics.json").write_text(json.dumps({"winner_family_ids": [1, 2]}), encoding="utf-8")
    (analysis_dir / "stable_arena__tool_only__stable10.json").write_text(
        json.dumps(
            {
                "schema": "stable_arena_v1",
                "metrics_summary": {},
                "sections": {
                    "Combined": {
                        "top_row_patterns": [{"canonical": "138", "score": 21.0}],
                        "top_compound_patterns": [{"canonical": "344", "compound_score": 18.0}],
                        "family_rollups_top": [{"family_id": 8, "family_score_total": 40.0}],
                    }
                },
                "evidence_paths": [],
            }
        ),
        encoding="utf-8",
    )
    (analysis_dir / "dr_arena__tool_only__stable10.json").write_text(
        json.dumps(
            {
                "schema_revision": "v1.1",
                "meta": {},
                "sections": {"Combined": {"summary": {"top_candidate_preview": [{"best_pattern": "138", "family_id": "8", "score_v2": 9.5}]}}},
                "paths": {},
            }
        ),
        encoding="utf-8",
    )
    (analysis_dir / "aux_control_center_arena__tool_only__stable10.json").write_text(
        json.dumps(
            {
                "available": True,
                "schema_version": "aux_control_center_arena_v1",
                "arena_objects": {
                    "aux_positional_pressure": {"shortlist_top": [{"combo": "138", "canonical": "138", "score": 11.0, "vtrac_index": 23}]},
                    "aux_badge_pressure": {
                        "top_combo_alerts": [{"combo": "138", "canonical": "138", "draws_since": 55}],
                        "index_pressure": {"by_variant": {"Combined": {"top_indices": [{"index": 23, "pressure_density": 2.0}]}}},
                    },
                    "aux_vtrac_pressure": {"overlay_top": {"Combined": [{"index": 23, "draws_since": 88}]}, "heatboard_top": {}},
                    "aux_due_doubles_family_pressure": {
                        "by_variant": {"Combined": {"draws_since_double": 44, "families": [{"slot": "Family 1", "family": "0/5-1/6", "examples": ["138"]}]}}
                    },
                    "aux_repeat_watch_context": {
                        "aux_by_variant": {"Combined": {"current_index": 23, "current_streak": 2, "last_repeat_gap": 4, "last_repeat_index": 7, "max_streak": 3, "window": 5}},
                        "control_center_top": [{"variant": "Combined", "current_index": 23, "heat_index": 13, "current_streak": 2, "heat_hazard": 0.4, "last_repeat_draws": 4, "max_streak": 3}],
                    },
                    "aux_blackapple_context": {"control_center_top": [{"variant": "Combined", "ba_score": 7, "examples": ["138"]}]},
                    "cc_profit_alert_context": {"top_alerts": [{"canonical": "138", "strength": 4, "evidence_summary": {"stable_family_id": "8"}}]},
                },
                "inputs": [],
            }
        ),
        encoding="utf-8",
    )
    (analysis_dir / "signals_bundle__tool_only__stable10.json").write_text(json.dumps({"tools": {}}), encoding="utf-8")

    vtrac_dir = state_dir / "vtrac" / state_key
    vtrac_dir.mkdir(parents=True, exist_ok=True)
    (vtrac_dir / f"{state_key}_vtrac_enhanced_20260318_120000.json").write_text(
        json.dumps(
            {
                "indices_ranked": [{"index": 23, "score": 10.0}],
                "straights_ranked": [{"straight": "138", "index": 23, "score": 8.0}],
                "section_summaries": {},
                "telemetry": {},
            }
        ),
        encoding="utf-8",
    )
    (day1 / "vtrac_compact_report.json").write_text(
        json.dumps({"states": [{"state": state_key, "top_indices_by_state": [{"index": 23, "score": 10.2}], "sections": []}]}),
        encoding="utf-8",
    )

    hot_dir = state_dir / "hot_zones" / state_key
    hot_dir.mkdir(parents=True, exist_ok=True)
    (hot_dir / f"{state_key}_hot_zones_meta.json").write_text(json.dumps({"state": state_key}), encoding="utf-8")
    _write_csv(
        hot_dir / f"{state_key}_hot_zones_top_lanes.csv",
        [{"triad": "138", "vt_triad": "134", "support_count": "6", "hot_hits": "2", "superhot_hits": "1", "vertical_hits": "3", "set1_hits": "2", "col1_hits": "1", "precol1_hits": "1", "vt_straight_hits": "1", "vt_only_lane_hits": "0", "guard_hits": "0", "literal_hits": "1", "variant_span": "3", "set_span": "2", "column_span": "4", "score_mean": "14.2", "score_max": "18.0", "evidence_tags": "col1,vt_straight"}],
        ["triad", "vt_triad", "support_count", "hot_hits", "superhot_hits", "vertical_hits", "set1_hits", "col1_hits", "precol1_hits", "vt_straight_hits", "vt_only_lane_hits", "guard_hits", "literal_hits", "variant_span", "set_span", "column_span", "score_mean", "score_max", "evidence_tags"],
    )
    _write_csv(
        hot_dir / f"{state_key}_hot_zones_per_lane.csv",
        [{"section": "Combined", "set_name": "Set1", "draw_name": "Draw1", "column_index": "1", "triad": "138", "vt_triad": "134", "vertical_support": "3", "horizontal_span": "5", "set_span": "2", "variant_echo": "2", "has_straight": "1", "has_vt_straight": "1", "vt_only_lane": "0", "col1_arrival": "1", "precol1_funnel": "1", "is_starred": "1", "star_count": "10", "is_superhot_slot": "1", "guard_injected": "0", "score": "18.0", "reasons": "col1,vt_straight"}],
        ["section", "set_name", "draw_name", "column_index", "triad", "vt_triad", "vertical_support", "horizontal_span", "set_span", "variant_echo", "has_straight", "has_vt_straight", "vt_only_lane", "col1_arrival", "precol1_funnel", "is_starred", "star_count", "is_superhot_slot", "guard_injected", "score", "reasons"],
    )
    (hot_dir / "2026-03-18_hot_zones_winner_map.json").write_text(json.dumps([{"triad": "138", "score_mean": 14.2, "support_count": 6}]), encoding="utf-8")

    payload = build_aggregated_analysis_arena_payload(
        day_dir=day1,
        state_key=state_key,
        results_date="2026-03-18",
        history_date="2026-03-17",
        profile="tool_only",
        experiment_tag="arena_v0",
        sharepacks_root=sharepacks_root,
        repo_root=tmp_path,
        top_items=8,
    )
    write_aggregated_analysis_arena_files(
        out_json_path=state_dir / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json",
        payload=payload,
        write_md=True,
    )

    day2 = sharepacks_root / "2026-03-19"
    (day2 / "control_center").mkdir(parents=True, exist_ok=True)
    (day2 / "control_center" / "meta.json").write_text(
        json.dumps(
            {
                "history_date": "2026-03-18",
                "states": [{"state_key": state_key, "winners": {"Midday": "831", "Evening": "555"}}],
            }
        ),
        encoding="utf-8",
    )
    future_stable = day2 / state_key / "stable" / state_key
    future_stable.mkdir(parents=True, exist_ok=True)
    (future_stable / f"{state_key}_metrics.json").write_text(json.dumps({"winner_family_ids": [8, 9]}), encoding="utf-8")
    return sharepacks_root, state_key


def test_decay_rows_capture_next_day_resolution(tmp_path: Path) -> None:
    sharepacks_root, state_key = _build_snapshot_fixture(tmp_path)
    rows = build_decay_rows(
        sharepacks_root=sharepacks_root,
        dates=["2026-03-18"],
        states=[state_key],
        profile="tool_only",
        experiment_tag="arena_v0",
        build_missing=False,
        rebuild=False,
        top_items=8,
        decay_days=1,
    )
    assert len(rows) == 1
    row = rows[0]
    assert row["dominant_canonical_box_hit"] == "1"
    assert row["dominant_canonical_box_day_offset"] == "1"
    assert row["dominant_canonical_box_draw_offset"] == "2"
    assert row["watchlist_box_hit"] == "1"
    assert row["watchlist_box_day_offset"] == "1"
    assert row["dominant_vtrac_hit"] == "1"
    assert row["dominant_vtrac_day_offset"] == "1"
    assert row["dominant_family_hit"] == "1"
    assert row["profit_alert_box_hit"] == "1"
    assert row["blackapple_box_hit"] == "1"
    assert row["due_doubles_box_hit"] == "1"
    assert row["repeat_watch_vtrac_hit"] == "1"
    assert row["aux_overdue_vtrac_hit"] == "1"
    assert row["badge_box_hit"] == "1"
    assert row["badge_vtrac_hit"] == "1"
