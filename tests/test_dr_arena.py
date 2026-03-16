from __future__ import annotations

import csv
import json
from pathlib import Path

from modules.vtrac_reference import get_vtrac_index
from scripts.tools.dr_arena import build_dr_arena_markdown, build_dr_arena_payload


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _build_dr_bundle(tmp_path: Path) -> tuple[Path, Path]:
    sharepacks_root = tmp_path / "sharepacks" / "_predictive"
    results_date = "2026-03-10"
    state_key = "TestState"
    state_dir = sharepacks_root / results_date / state_key
    dr_dir = state_dir / "digit_reduction" / state_key
    analyzer_dir = dr_dir / "analyzer_v2"
    training_dir = dr_dir / "training"
    analyzer_dir.mkdir(parents=True, exist_ok=True)
    training_dir.mkdir(parents=True, exist_ok=True)

    meta = {
        "cluster_scan": {"max_len": 12},
        "scoring_v2": {"enabled": True},
        "lockscore": {"mode": "v2"},
        "policy": {"top_candidates": 12},
    }
    (analyzer_dir / f"{state_key}_analyzer_v2_meta.json").write_text(json.dumps(meta), encoding="utf-8")

    per_item_rows = [
        {
            "variant": "Combined",
            "family_id": "20",
            "pattern": "028",
            "score_v2": "11.0",
            "dup_bonus": "0.0",
            "method": "own_prev",
            "mode": "full_value",
            "area": "Group2",
            "set_rank": "1",
            "draw_rank": "1",
            "col_rank": "1",
            "area_rank": "1",
            "vt_only_lane": "1",
            "funnel_precol1": "1",
            "set1_terminal": "1",
            "persistence_vtrac_score": "6.0",
            "persistence_exact_score": "1.0",
            "residual_purity": "0.90",
            "final_prob": "0.42",
            "box_family_density": "2.2",
            "cluster_echo_count": "2",
            "variant_echo_count": "2",
            "set_echo_count": "1",
            "set": "Set1",
            "draw": "Draw1",
            "col": "1",
        },
        {
            "variant": "Combined",
            "family_id": "20",
            "pattern": "082",
            "score_v2": "10.0",
            "dup_bonus": "0.0",
            "method": "combined_prev",
            "mode": "single_digit",
            "area": "Group2",
            "set_rank": "1",
            "draw_rank": "2",
            "col_rank": "2",
            "area_rank": "1",
            "vt_only_lane": "1",
            "funnel_precol1": "1",
            "set1_terminal": "0",
            "persistence_vtrac_score": "5.5",
            "persistence_exact_score": "1.0",
            "residual_purity": "0.85",
            "final_prob": "0.31",
            "box_family_density": "1.9",
            "cluster_echo_count": "1",
            "variant_echo_count": "1",
            "set_echo_count": "1",
            "set": "Set1",
            "draw": "Draw2",
            "col": "2",
        },
        {
            "variant": "Combined",
            "family_id": "99",
            "pattern": "994",
            "score_v2": "7.0",
            "dup_bonus": "2.5",
            "method": "combined_prev",
            "mode": "single_digit",
            "area": "Group1",
            "set_rank": "2",
            "draw_rank": "1",
            "col_rank": "6",
            "area_rank": "2",
            "vt_only_lane": "0",
            "funnel_precol1": "0",
            "set1_terminal": "0",
            "persistence_vtrac_score": "2.0",
            "persistence_exact_score": "1.7",
            "residual_purity": "0.48",
            "final_prob": "0.12",
            "box_family_density": "1.1",
            "cluster_echo_count": "0",
            "variant_echo_count": "0",
            "set_echo_count": "0",
            "set": "Set2",
            "draw": "Draw1",
            "col": "6",
        },
        {
            "variant": "Combined",
            "family_id": "34",
            "pattern": "434",
            "score_v2": "8.0",
            "dup_bonus": "3.0",
            "method": "own_prev",
            "mode": "single_digit",
            "area": "Group2",
            "set_rank": "1",
            "draw_rank": "3",
            "col_rank": "1",
            "area_rank": "1",
            "vt_only_lane": "0",
            "funnel_precol1": "1",
            "set1_terminal": "1",
            "persistence_vtrac_score": "3.0",
            "persistence_exact_score": "2.5",
            "residual_purity": "0.74",
            "final_prob": "0.27",
            "box_family_density": "1.4",
            "cluster_echo_count": "1",
            "variant_echo_count": "1",
            "set_echo_count": "1",
            "set": "Set1",
            "draw": "Draw3",
            "col": "1",
        },
        {
            "variant": "Evening",
            "family_id": "77",
            "pattern": "994",
            "score_v2": "5.0",
            "dup_bonus": "1.5",
            "method": "combined_prev",
            "mode": "full_value",
            "area": "Group1",
            "set_rank": "2",
            "draw_rank": "2",
            "col_rank": "7",
            "area_rank": "2",
            "vt_only_lane": "0",
            "funnel_precol1": "0",
            "set1_terminal": "0",
            "persistence_vtrac_score": "1.0",
            "persistence_exact_score": "0.9",
            "residual_purity": "0.22",
            "final_prob": "0.08",
            "box_family_density": "0.6",
            "cluster_echo_count": "0",
            "variant_echo_count": "0",
            "set_echo_count": "0",
            "set": "Set2",
            "draw": "Draw2",
            "col": "7",
        },
    ]
    _write_csv(
        analyzer_dir / f"{state_key}_analyzer_v2_per_item.csv",
        per_item_rows,
        fieldnames=list(per_item_rows[0].keys()),
    )

    top_candidate_rows = [
        {
            "variant": "Combined",
            "rank": "1",
            "best_pattern": "994",
            "family_id": "99",
            "score_v2": "7.0",
            "vt_only_lane": "0",
            "funnel_precol1": "0",
        },
        {
            "variant": "Combined",
            "rank": "2",
            "best_pattern": "028",
            "family_id": "20",
            "score_v2": "11.0",
            "vt_only_lane": "1",
            "funnel_precol1": "1",
        },
        {
            "variant": "Combined",
            "rank": "3",
            "best_pattern": "434",
            "family_id": "34",
            "score_v2": "8.0",
            "vt_only_lane": "0",
            "funnel_precol1": "1",
        },
        {
            "variant": "Evening",
            "rank": "1",
            "best_pattern": "994",
            "family_id": "77",
            "score_v2": "5.0",
            "vt_only_lane": "0",
            "funnel_precol1": "0",
        },
    ]
    _write_csv(
        analyzer_dir / f"{state_key}_analyzer_v2_top_candidates.csv",
        top_candidate_rows,
        fieldnames=list(top_candidate_rows[0].keys()),
    )

    logs = {
        "items": [
            {
                "section": "Combined",
                "location": "Set1|Draw1|col1",
                "area": "Group2",
                "method": "own_prev",
                "mode": "full_value",
                "grid_position": {"set_rank": 1, "draw_rank": 1, "col_rank": 1, "area_rank": 1},
                "sequence_meta": {"first_3value_step": 1, "last_change_step": 2, "steps_kept_after_compaction": 3},
                "steps": [
                    {"value": "4028", "length": 4, "unique_digits": 4, "is_3value": False},
                    {"value": "028", "length": 3, "unique_digits": 3, "is_3value": True},
                    {"value": "028", "length": 3, "unique_digits": 3, "is_3value": True},
                ],
                "final": {"value": "028"},
            },
            {
                "section": "Combined",
                "location": "Set1|Draw3|col1",
                "area": "Group2",
                "method": "own_prev",
                "mode": "single_digit",
                "grid_position": {"set_rank": 1, "draw_rank": 3, "col_rank": 1, "area_rank": 1},
                "sequence_meta": {"first_3value_step": 1, "last_change_step": 2, "steps_kept_after_compaction": 3},
                "steps": [
                    {"value": "4434", "length": 4, "unique_digits": 2, "is_3value": False},
                    {"value": "434", "length": 3, "unique_digits": 2, "is_3value": True},
                    {"value": "434", "length": 3, "unique_digits": 2, "is_3value": True},
                ],
                "final": {"value": "434"},
            },
            {
                "section": "Evening",
                "location": "Set2|Draw2|col7",
                "area": "Group1",
                "method": "combined_prev",
                "mode": "full_value",
                "grid_position": {"set_rank": 2, "draw_rank": 2, "col_rank": 7, "area_rank": 2},
                "sequence_meta": {"first_3value_step": -1, "last_change_step": 0, "steps_kept_after_compaction": 1},
                "steps": [
                    {"value": "9994", "length": 4, "unique_digits": 2, "is_3value": False},
                ],
                "final": {"value": "9994"},
            },
        ]
    }
    (training_dir / f"{state_key}_digit_reduction_logs.json").write_text(json.dumps(logs), encoding="utf-8")
    return sharepacks_root, state_dir


def test_dr_arena_surfaces_predictive_evidence_classes(tmp_path: Path):
    sharepacks_root, state_dir = _build_dr_bundle(tmp_path)

    payload = build_dr_arena_payload(
        state_dir=state_dir,
        state_key="TestState",
        results_date="2026-03-10",
        history_date="2026-03-09",
        profile="tool_only",
        experiment_tag="dr_arena_v1",
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=False,
        repo_root=tmp_path,
    )

    assert payload is not None
    assert payload["schema_revision"] == "v1.1"
    combined = payload["sections"]["Combined"]
    evening = payload["sections"]["Evening"]

    assert combined["dr_trace_strength"]
    assert combined["dr_trace_strength"][0]["family_id"] == "20"

    assert combined["dr_lane_only_confidence"]
    assert combined["dr_lane_only_confidence"][0]["family_id"] == "20"

    pressure_patterns = {item["pattern"] for item in combined["dr_competing_literal_pressure"]}
    assert {"994", "434"}.issubset(pressure_patterns)

    double_patterns = {item["pattern"] for item in combined["dr_double_pressure"]}
    assert {"994", "434"}.issubset(double_patterns)

    assert combined["dr_row_repeat_and_final_survival"]
    assert any(item["value"] == "434" and item["terminal_hits"] >= 1 for item in combined["dr_row_repeat_and_final_survival"])

    assert combined["fourth_variable_candidates"]
    assert any(
        item["core_value"] == "028" and item["extra_digits"] == "4"
        for item in combined["fourth_variable_candidates"]
    )
    assert combined["dr_corridor_strength"]
    assert combined["dr_corridor_strength"][0]["family_id"] == "20"
    assert combined["dr_corridor_strength"][0]["corridor_band"] == "set1_current_day"
    assert combined["dr_corridor_strength"][0]["corridor_scope"] in {"vtrac_corridor", "family_neighborhood", "exact_corridor"}
    assert combined["dr_vtrac_lane_gateway"]
    assert combined["dr_vtrac_lane_gateway"][0]["vtrac_index"] == get_vtrac_index("028")
    assert combined["dr_vtrac_lane_gateway"][0]["member_count"] >= 1
    assert combined["dr_vtrac_cluster_strength"]
    assert combined["dr_vtrac_cluster_strength"][0]["vtrac_index"] == get_vtrac_index("028")
    assert combined["dr_vtrac_cluster_strength"][0]["support_class_count"] >= 2
    assert "raw_cluster_score" in combined["dr_vtrac_cluster_strength"][0]
    assert "cluster_adjustment" in combined["dr_vtrac_cluster_strength"][0]
    assert combined["dr_assigned_box_vtrac_strength"]
    assert combined["dr_assigned_box_vtrac_strength"][0]["vtrac_index"] == get_vtrac_index("028")
    assert combined["dr_assigned_box_vtrac_strength"][0]["row_count"] >= 1
    assert combined["dr_assigned_box_vtrac_strength"][0]["top_windows"]
    assert combined["dr_vtrac_fusion_strength"]
    assert combined["dr_vtrac_fusion_strength"][0]["vtrac_index"] == get_vtrac_index("028")
    assert combined["dr_vtrac_fusion_strength"][0]["fusion_score"] > 0
    assert "vtrac_fusion_strength" in combined["dr_vtrac_fusion_strength"][0]["why_tags"]

    structural = combined["dr_structural_signals"]
    assert structural["raw_exposure_count"] == 4
    assert structural["path_summary_count"] == 2
    assert structural["early_activation_strength"] > 0
    assert structural["neighbor_box_support"] >= 0
    assert structural["overlay_summary_mismatch"]["available"] is False

    assert combined["dr_empty_lens"]["classification"] == "positive_trace"
    assert combined["dr_empty_lens"]["is_sparse"] is False

    assert evening["dr_empty_lens"]["is_sparse"] is False
    assert evening["dr_empty_lens"]["classification"] == "active_low_trust"
    assert "all_locations_cold" in evening["dr_empty_lens"]["reasons"]


def test_dr_arena_markdown_is_human_readable(tmp_path: Path):
    sharepacks_root, state_dir = _build_dr_bundle(tmp_path)
    payload = build_dr_arena_payload(
        state_dir=state_dir,
        state_key="TestState",
        results_date="2026-03-10",
        history_date="2026-03-09",
        profile="tool_only",
        experiment_tag="dr_arena_v1",
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=False,
        repo_root=tmp_path,
    )
    assert payload is not None

    md = build_dr_arena_markdown(payload)
    assert "DR Arena" in md
    assert "Trace Strength" in md
    assert "Corridor Strength" in md
    assert "Competing Literal Pressure" in md
    assert "Double Pressure" in md
    assert "VTRAC Lane Gateway" in md
    assert "VTRAC Cluster Strength" in md
    assert "Fourth Variable" in md
    assert "Structural Signals" in md
