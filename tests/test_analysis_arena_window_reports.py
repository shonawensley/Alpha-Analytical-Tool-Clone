from __future__ import annotations

import json
import sys
from pathlib import Path


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _winner_report_payload(
    *,
    state: str,
    index: int,
    winner_combo: str,
    patterns: list[str],
    stats: dict[str, dict[str, int]],
    combined_rows: list[dict[str, object]],
) -> dict[str, object]:
    tables: dict[str, list[dict[str, object]]] = {"Combined": []}
    for row in combined_rows:
        cells: dict[str, object] = {}
        for key in ("Set", "Draw", "RowType", "7", "6", "5", "4", "3", "2", "1"):
            value = row.get(key, {"text": "N/A", "tags": []})
            if key in {"Set", "Draw", "RowType"}:
                cells[key] = {"text": str(value), "tags": []}
            else:
                cells[key] = value
        tables["Combined"].append(
            {
                "Set": str(row.get("Set", "")),
                "Draw": str(row.get("Draw", "")),
                "RowType": str(row.get("RowType", "")),
                "cells": cells,
            }
        )
    return {
        "state": state,
        "index": index,
        "winner_combo": winner_combo,
        "score": 0,
        "rank": 0,
        "timestamp": "20260110_010101",
        "patterns": patterns,
        "legend": {
            "hit-winner": "Winner",
            "hit-winner-gap": "Winner (gap)",
            "hit-vt-straight": "V-TRAC straight",
            "hit-vt-straight-gap": "V-TRAC straight (value)",
            "hit-family": "Index family",
            "hit-family-gap": "Family (gap)",
            "ls-box": "Long-string (DR) box",
            "ls-box-edge": "Long-string (DR) box edge",
        },
        "tables": tables,
        "stats": stats,
    }


def _seed_window(tmp_path: Path) -> Path:
    window_root = tmp_path / "runs2" / "WINDOW_2026-01-05_to_2026-01-05"
    analysis_dir = window_root / "ANALYSIS_ARENA"
    validation_dir = window_root / "VALIDATION"

    _write_text(
        tmp_path / "data" / "results" / "2026-01-05.txt",
        "State\tPick 3\nMidday\tEvening\nNew York\t080\t735\nTexas\t958\t572\n",
    )

    _write_json(
        analysis_dir / "2026-01-05__BOARD_SCOREBOARD__analysis_arena_day_review.json",
        {
            "metadata": {
                "profile": "tool_only",
                "experiment_tag": "arena_v0",
            },
            "board_verdict": {
                "top_primary_target": "NewYork4",
                "secondary_target": "NewYork4",
                "best_clean_host": "NewYork4",
                "highest_context_support_state": "NewYork4",
            },
            "scoreboard_rows": [
                {
                    "state_key": "NewYork4",
                    "score_rank": 1,
                    "priority_score": 98.4,
                    "role": "shared_host",
                    "targeting_bucket": "tight_core",
                    "tracker_posture": "tracker-rich",
                    "top_canonicals": ["008", "357"],
                    "top_vtrac_indices": ["6", "24"],
                    "profit_alert_hint": "A05",
                    "compound_event_hint": "ENGINE_GOV",
                    "due_double_hint": "0/5-1/6",
                    "blackapple_reco_hint": "008",
                    "positional_hint": "008",
                    "r_consensus_hint": "tail 08",
                    "survivor_hint": "frontier 008",
                }
            ],
        },
    )
    _write_json(
        analysis_dir / "2026-01-05__SHADOW_DECISION_POLICY__analysis_arena_day_review.json",
        {
            "state_decisions": [
                {
                    "state_key": "NewYork4",
                    "posture": "PLAY",
                    "mode": "BOX_FIRST",
                    "cap_class": "B24",
                    "translator_route": "shadow_only",
                    "reason_codes": ["CONSENSUS_EVENT", "DUE_DOUBLE"],
                }
            ]
        },
    )

    seed_rel = Path("sharepacks/_predictive/2026-01-05/NewYork4/analysis/translation_sandbox_seed__tool_only__arena_v0.json")
    _write_json(
        analysis_dir / "2026-01-05__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json",
        {
            "state_receipts": [
                {
                    "state_key": "NewYork4",
                    "score_rank": 1,
                    "priority_score": 98.4,
                    "role": "shared_host",
                    "posture": "PLAY",
                    "mode": "BOX_FIRST",
                    "seed_json": str(seed_rel),
                    "seed_md": str(seed_rel).replace(".json", ".md"),
                }
            ]
        },
    )

    _write_json(
        tmp_path / seed_rel,
        {
            "brain1_core": {
                "dominant_canonicals": ["008", "357"],
                "context_reinforced_canonicals": ["008", "357"],
                "dominant_vtrac_indices": ["6", "24"],
            },
            "control_arm": {
                "candidate_universe": {
                    "path": "sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only__arena_v0.json"
                },
                "play_card": {
                    "path": "sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json"
                },
                "preserved_not_budgeted_canonicals_top": ["008", "357"],
            },
            "sandbox_hypotheses": {
                "diagnostic_boxed_seed": [{"value": "008"}, {"value": "357"}],
                "diagnostic_straight_seed": [{"value": "080"}, {"value": "735"}],
                "diagnostic_vt_box_seed": [{"value": "6"}, {"value": "24"}],
            },
        },
    )
    _write_json(
        tmp_path / "sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only__arena_v0.json",
        {"union_combos": ["080", "735", "357"], "packs": []},
    )
    _write_json(
        tmp_path / "sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json",
        {
            "strategies": {
                "analysis_prefix": {
                    "B12": {"combos": ["080"], "boxed_canonicals": ["008"]},
                    "B24": {"combos": ["080", "735"], "boxed_canonicals": ["008", "357"]},
                    "B36": {"combos": ["080", "735"], "boxed_canonicals": ["008", "357"]},
                }
            }
        },
    )

    _write_text(
        validation_dir / "2026-01-05_to_2026-01-05__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv",
        "date,state,period,winner,type,has_mirror_pair,mirror_pairs\n"
        "2026-01-05,NewYork4,Midday,080,double,False,\n"
        "2026-01-05,NewYork4,Evening,735,mirror_double,True,2/7\n",
    )
    return window_root


def _seed_legacy_comparison_window(tmp_path: Path) -> tuple[Path, Path]:
    window_root = tmp_path / "runs2" / "WINDOW_2026-01-05_to_2026-01-05"
    analysis_dir = window_root / "ANALYSIS_ARENA"
    legacy_runs = tmp_path / "legacy_runs"

    _write_json(
        analysis_dir / "2026-01-05__BOARD_SCOREBOARD__analysis_arena_day_review.json",
        {
            "metadata": {
                "profile": "tool_only",
                "experiment_tag": "arena_v0",
            },
            "board_verdict": {},
            "scoreboard_rows": [],
        },
    )
    _write_json(
        window_root / "WINDOW_2026-01-05_to_2026-01-05__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        {
            "metadata": {
                "window_root": str(window_root),
                "window_dates": ["2026-01-05"],
            },
            "summary_counts": {
                "winner_events": 2,
                "winner_on_board": 2,
                "board_top5": 1,
                "cu_exact": 1,
                "cu_box": 2,
                "play_card_any_exact": 1,
                "play_card_any_box": 1,
                "opportunity_gap_box": 1,
            },
            "summary_rates": {
                "winner_on_board": 1.0,
                "board_top5": 0.5,
                "cu_exact": 0.5,
                "cu_box": 1.0,
                "play_card_any_exact": 0.5,
                "play_card_any_box": 0.5,
                "opportunity_gap_box": 0.5,
            },
            "tracker_attribution": {},
            "translator_learning": {},
        },
    )

    _write_text(
        legacy_runs / "2026-01-05_to_2026-01-05__CORPUS_DASHBOARD.md",
        "# Corpus Dashboard\n\n"
        "Total graded outcomes (state×period): **2**\n\n"
        "- Stable families present: **2/2** (100.0%)\n"
        "- Hot Zones top lanes present: **2/2** (100.0%)\n"
        "- VTRAC winner index in top10: **1/2** (50.0%)\n"
        "- DR top-candidates contain winner: **0/2** (0.0%)\n"
        "- Blackapple top list contains winner: **0/2** (0.0%)\n"
        "- Winner VTRAC signature has repeat (mirror/double-space): **1/2** (50.0%)\n",
    )
    _write_text(
        legacy_runs / "2026-01-05_to_2026-01-05__DR_LENS_REPORT.md",
        "# DR Lens\n\n"
        "Active rows: **2/2** (100.0%)\n\n"
        "| Tag | Count | % of active |\n"
        "|---|---:|---:|\n"
        "| top.winner_present (any) | 0 | 0.0% |\n"
        "| flags.dr_win_vt_boxed (any) | 2 | 100.0% |\n",
    )
    _write_text(
        legacy_runs / "2026-01-05_to_2026-01-05__CONTROL_CENTER_ROLLUP.md",
        "# CC Rollup\n\n"
        "- Status ALERT: **1/3** (33.3%)\n"
        "- Status WATCH: **1/3** (33.3%)\n"
        "- Midday winner in any family: **1/3** (33.3%)\n"
        "- Evening winner in any family: **2/3** (66.7%)\n",
    )
    _write_text(
        legacy_runs / "blackapple_rollup__N5__2026-01-05_to_2026-01-05.csv",
        "variant,ba_status,period,rows_measured,hit_any_inclusive_rate,boxed_hit_rate,straight_hit_rate,vtrac_hit_rate,hit_any_inclusive_window_rate\n"
        "Combined,ALERT,Midday,1,0.5000,0.5000,0.0000,0.5000,1.0000\n"
        "Combined,ALERT,Evening,1,0.0000,0.0000,0.0000,0.0000,0.0000\n",
    )
    _write_text(
        legacy_runs / "2026-01-05__CANDIDATE_UNIVERSE_GRADE__tool_only.csv",
        "results_date,sharepacks_root,profile,candidate_universe_path,state_key,history_date,winner_label,winner,winner_canonical,winner_vtrac_index,winner_missing,pack_id,method_id,pack_variant,play_mode,combos_count,cost_units,contains_winners_artifacts,hit_any,straight_hit,box_hit,vtrac_index_hit,vtrac_index_hit_only\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,NewYork4,2026-01-04,Midday,080,008,6,0,__UNION__,union,base,boxed,12,12,1,1,1,1,1,0\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,NewYork4,2026-01-04,Evening,735,357,12,0,__UNION__,union,base,boxed,12,12,0,0,0,0,1,1\n",
    )
    _write_text(
        legacy_runs / "play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2026-01-05_to_2026-01-05.csv",
        "strategy,budget_label,rows_measured,hit_any_strict_window_rate,hit_any_box_window_rate,hit_any_inclusive_window_rate,pack_hit_any_inclusive_window_rate,filler_hit_any_inclusive_window_rate,pack_only_hit_any_inclusive_window_rate,pack_and_filler_hit_any_inclusive_window_rate\n"
        "analysis_prefix,B12,14,0.0000,0.1000,0.3000,0.0000,0.0000,0.0000,0.0000\n"
        "analysis_prefix,B24,14,0.0000,0.2000,0.5000,0.0000,0.0000,0.0000,0.0000\n"
        "analysis_prefix,B36,14,0.0000,0.2500,0.6000,0.0000,0.0000,0.0000,0.0000\n"
        "play_box_first,B12,14,0.0000,0.0500,0.2000,0.0000,0.0000,0.0000,0.0000\n"
        "v0_2_default,B36,14,0.1000,0.3500,0.8000,0.0000,0.0000,0.0000,0.0000\n"
        "vtrac_pack_boxed_first_laneonly_presetB,B36,14,0.1000,0.3800,0.8200,0.0000,0.0000,0.0000,0.0000\n",
    )
    _write_text(
        legacy_runs / "play_card_windowed_rollup__tool_only__arena_v0__N5__2026-01-05_to_2026-01-05.csv",
        "strategy,budget_label,rows_measured,hit_any_strict_window_rate,hit_any_box_window_rate,hit_any_inclusive_window_rate,pack_hit_any_inclusive_window_rate,filler_hit_any_inclusive_window_rate,pack_only_hit_any_inclusive_window_rate,pack_and_filler_hit_any_inclusive_window_rate\n"
        "analysis_prefix,B12,14,0.0000,0.0900,0.2500,0.0000,0.0000,0.0000,0.0000\n"
        "analysis_prefix,B24,14,0.0000,0.2400,0.6000,0.0000,0.0000,0.0000,0.0000\n"
        "analysis_prefix,B36,14,0.1000,0.3000,0.7000,0.0000,0.0000,0.0000,0.0000\n"
        "play_box_first,B12,14,0.0000,0.0500,0.2100,0.0000,0.0000,0.0000,0.0000\n"
        "v0_2_default,B36,14,0.1000,0.4000,0.8500,0.0000,0.0000,0.0000,0.0000\n"
        "vtrac_pack_boxed_first_laneonly_presetB,B36,14,0.1000,0.4100,0.8600,0.0000,0.0000,0.0000,0.0000\n",
    )
    _write_text(
        legacy_runs / "DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md",
        "The system is not missing signal; it is losing probability mass in the B36 selection cut.\n",
    )
    _write_text(
        legacy_runs / "2026-01-15_to_2026-01-21__DISCONNECT_ANALYSIS__CODEX.md",
        "DR and Blackapple exact-hit rates were intentionally demoted to lane and triage evidence.\n",
    )
    return window_root, legacy_runs


def _seed_hit_analysis_window(tmp_path: Path) -> tuple[Path, Path, Path]:
    window_root = tmp_path / "runs2" / "WINDOW_2026-01-05_to_2026-01-05"
    analysis_dir = window_root / "ANALYSIS_ARENA"
    validation_dir = window_root / "VALIDATION"
    runs_root = tmp_path / "runs"
    sharepacks_root = tmp_path / "sharepacks" / "_predictive"
    cc_dir = sharepacks_root / "2026-01-05" / "control_center"
    winners_root = tmp_path / "reports" / "stable" / "winners_by_date" / "2026-01-05"

    _write_json(
        analysis_dir / "2026-01-05__BOARD_SCOREBOARD__analysis_arena_day_review.json",
        {
            "metadata": {
                "profile": "tool_only",
                "experiment_tag": "arena_v0",
            },
            "board_verdict": {},
            "scoreboard_rows": [
                {"state_key": "NewYork4", "score_rank": 1},
                {"state_key": "Florida4", "score_rank": 5},
            ],
        },
    )

    _write_text(
        window_root / "WINDOW_2026-01-05_to_2026-01-05__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
        "date,state_key,period,winner,winner_canonical,winner_vtrac_index,winner_on_board,board_rank,top_primary_target,secondary_target,best_clean_host,highest_context_support_state,arena_box_signal,arena_exact_signal,sandbox_box_seed,sandbox_exact_seed,sandbox_vt_seed,preserved_not_budgeted\n"
        "2026-01-05,NewYork4,Midday,080,008,6,True,1,True,False,True,True,True,True,True,True,True,True\n"
        "2026-01-05,Florida4,Evening,994,499,18,True,5,False,False,False,False,False,False,False,False,True,False\n",
    )

    _write_text(
        runs_root / "2026-01-05__PLAY_CARD_GRADE__tool_only__arena_v0.csv",
        "results_date,sharepacks_root,profile,play_card_path,state_key,winner_label,winner,winner_canonical,winner_vtrac_index,winner_missing,strategy,budget_label,combos_count,boxed_canonicals_count,hit_any,hit_any_box,hit_any_inclusive,straight_hit,box_hit,canon_hit_any_perm,vtrac_index_hit,vtrac_index_hit_only\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,NewYork4,Midday,080,008,6,0,analysis_prefix,B12,12,2,1,1,1,1,1,1,1,0\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,Florida4,Evening,994,499,18,0,analysis_prefix,B24,24,4,0,0,1,0,0,0,1,1\n",
    )
    _write_text(
        runs_root / "2026-01-05__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.csv",
        "results_date,sharepacks_root,profile,candidate_universe_path,state_key,history_date,winner_label,winner,winner_canonical,winner_vtrac_index,winner_missing,pack_id,method_id,pack_variant,play_mode,combos_count,cost_units,contains_winners_artifacts,hit_any,straight_hit,box_hit,vtrac_index_hit,vtrac_index_hit_only\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,NewYork4,2026-01-04,Midday,080,008,6,0,__UNION__,union,base,boxed,12,12,1,1,1,1,1,0\n"
        "2026-01-05,sharepacks/_predictive,tool_only,p1,Florida4,2026-01-04,Evening,994,499,18,0,__UNION__,union,base,boxed,12,12,0,0,0,0,1,1\n",
    )

    _write_text(
        cc_dir / "due_doubles.csv",
        "State,StateKey,Variant,Draws Since Double,Family 1,Family 2,Family 3,Family 4,Family 5,Winner Midday,Winner Evening,Midday Winner In Family,Evening Winner In Family\n"
        "New York,NewYork4,Midday,8,0/5-4/9: 008,1/6-2/7: 126,,,,-,-,False,False\n"
        "New York,NewYork4,Combined,8,0/5-4/9: 008,1/6-2/7: 126,,,,-,-,False,False\n"
        "Florida,Florida4,Evening,5,4/9-1/6: 994,2/7-3/8: 278,,,,-,-,False,False\n"
        "Florida,Florida4,Combined,5,4/9-1/6: 994,2/7-3/8: 278,,,,-,-,False,False\n",
    )
    _write_text(
        cc_dir / "blackapple_alerts.csv",
        "State,StateKey,Variant,BA-Score,Status,Triggers,#Candidates,Examples,Winner Midday,Winner Evening,Midday Hits,Evening Hits\n"
        "New York,NewYork4,Midday,3,ALERT,Mirror,12,008 080 800,-,-,-,-\n"
        "Florida,Florida4,Evening,2,WATCH,Float 49,12,449 499 949,-,-,-,-\n",
    )
    _write_text(
        cc_dir / "profit_alerts.csv",
        "State,StateKey,Variant,AlertId,Strength,Suggested,CapLines,DecayDraws,Badges,Canonical,ImpliedSet,Evidence,Winner Midday,Winner Evening,Midday Hits,Evening Hits\n"
        "New York,NewYork4,Midday,A01,5,BOX,12,3,CONS/DBL/BA,008,\"[\"\"008\"\",\"\"080\"\",\"\"800\"\"]\",{},-,-,-,-\n"
        "Florida,Florida4,Evening,A04,3,STR8_3,6,2,CONS,449,\"[\"\"449\"\",\"\"494\"\",\"\"944\"\"]\",{},-,-,-,-\n",
    )
    _write_text(
        cc_dir / "profit_compound_events.csv",
        "results_date,state_key,variant,top_event,priority,watchlist_tags,candidate_alert_ids,promoter_alert_ids,a11_star_level_max,a11_star_score_max,a12_pack_sizes,min_implied_set_size,min_cap_lines,strength_max,decay_min,decay_max,merged_rows_total,merged_hits,merged_any_hit_within_decay,merged_hit_types,merged_any_hit_types\n"
        "2026-01-05,NewYork4,Midday,ENGINE_GOV,85,ENGINE_GOV|STRAIGHT_GATE,A01,,2,30.0,4,3,3,5,2,3,0,0,,,\n"
        "2026-01-05,Florida4,Evening,CARRY_PERM,70,CARRY_PERM,A04,,0,0.0,,3,3,3,1,2,0,0,,,\n",
    )
    _write_text(
        validation_dir / "2026-01-05_to_2026-01-05__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv",
        "date,state,period,winner,type,has_mirror_pair,mirror_pairs\n"
        "2026-01-05,NewYork4,Midday,080,double,False,\n"
        "2026-01-05,Florida4,Evening,994,double,True,4/9\n",
    )
    _write_text(
        window_root / "WINDOW_2026-01-05_to_2026-01-05__ANALYSIS_ARENA__HIT_ROSTER.csv",
        "date,state_key,period,winner,play_straight_hit,play_box_any_hit,play_vtrac_hit,arena_final_candidate_signature,blackapple_status,compound_event_present,due_double_draws_since_double,double_context_strength,inventory_type\n"
        "2026-01-05,NewYork4,Midday,080,1,1,1,CLEAR_ARENA_FINALIST,ALERT,1,8,STRONG,double\n"
        "2026-01-05,Florida4,Evening,994,0,1,1,PARTIAL_ARENA_FINALIST,WATCH,1,5,MEDIUM,double\n",
    )

    _write_json(
        winners_root / "NewYork4" / "NewYork4_vtrac4_winner_080_20260110_010101.json",
        _winner_report_payload(
            state="NewYork4",
            index=4,
            winner_combo="080",
            patterns=["008", "080", "800"],
            stats={
                "pattern_occurrence": {"008": 6, "080": 3, "800": 2},
                "pattern_persistence": {"008": 11, "080": 7, "800": 3},
                "pattern_stability": {"008": 4, "080": 3, "800": 1},
                "straight_counts": {"008": 4, "080": 2, "800": 1},
            },
            combined_rows=[
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R2", "4": {"text": "551008", "tags": ["ls-box", "ls-box-edge"]}, "3": {"text": "1008", "tags": ["ls-box", "ls-box-edge"]}, "2": {"text": "080", "tags": ["hit-winner"]}, "1": {"text": "008", "tags": ["hit-family"]}},
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R4", "4": {"text": "5508", "tags": []}, "3": {"text": "1008", "tags": []}, "2": {"text": "080", "tags": ["hit-winner"]}, "1": {"text": "008", "tags": ["hit-family", "hit-vt-straight"]}},
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R6", "4": {"text": "8800", "tags": []}, "3": {"text": "800", "tags": ["hit-family-gap"]}, "2": {"text": "080", "tags": ["hit-winner", "hit-vt-straight"]}, "1": {"text": "008", "tags": ["hit-family"]}},
                {"Set": "Set2", "Draw": "Draw1", "RowType": "R8", "4": {"text": "8800", "tags": []}, "3": {"text": "800", "tags": ["hit-family"]}, "2": {"text": "080", "tags": ["hit-winner-gap"]}, "1": {"text": "008", "tags": ["hit-family", "hit-vt-straight-gap"]}},
            ],
        ),
    )
    _write_json(
        winners_root / "Florida4" / "Florida4_vtrac18_winner_994_20260110_010102.json",
        _winner_report_payload(
            state="Florida4",
            index=18,
            winner_combo="994",
            patterns=["499", "949", "994"],
            stats={
                "pattern_occurrence": {"499": 7, "949": 5, "994": 1},
                "pattern_persistence": {"499": 12, "949": 9, "994": 2},
                "pattern_stability": {"499": 5, "949": 4, "994": 1},
                "straight_counts": {"499": 4, "949": 3, "994": 0},
            },
            combined_rows=[
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R2", "4": {"text": "44994", "tags": ["ls-box", "ls-box-edge"]}, "3": {"text": "4994", "tags": ["ls-box", "ls-box-edge"]}, "2": {"text": "499", "tags": ["hit-family"]}, "1": {"text": "949", "tags": ["hit-family-gap"]}},
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R4", "4": {"text": "94499", "tags": []}, "3": {"text": "9499", "tags": []}, "2": {"text": "499", "tags": ["hit-family"]}, "1": {"text": "949", "tags": ["hit-family", "hit-vt-straight"]}},
                {"Set": "Set1", "Draw": "Draw1", "RowType": "R6", "4": {"text": "99449", "tags": []}, "3": {"text": "9944", "tags": []}, "2": {"text": "499", "tags": ["hit-family"]}, "1": {"text": "994", "tags": ["hit-winner-gap"]}},
                {"Set": "Set2", "Draw": "Draw1", "RowType": "R8", "4": {"text": "94994", "tags": []}, "3": {"text": "9499", "tags": ["hit-family-gap"]}, "2": {"text": "499", "tags": ["hit-family", "hit-vt-straight-gap"]}, "1": {"text": "949", "tags": ["hit-family"]}},
            ],
        ),
    )
    return window_root, runs_root, sharepacks_root


def _seed_cross_window_rollup_window(tmp_path: Path, name: str, *, cand_rate: float, box_rate: float) -> Path:
    window_root = tmp_path / "runs2" / f"WINDOW_{name}"
    stem = window_root.name
    analysis_dir = window_root / "ANALYSIS_ARENA"
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        {
            "metadata": {"day_count": 5, "window_root": str(window_root)},
            "summary_counts": {
                "winner_events": 10,
            },
            "summary_rates": {
                "cu_exact": cand_rate / 2.0,
                "cu_box": cand_rate,
                "play_card_any_box": box_rate,
                "opportunity_gap_box": 0.2,
                "top_primary_target": 0.1,
            },
        },
    )
    _write_text(
        window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
        "date,state_key,period,winner,board_rank,top_primary_target,best_clean_host,highest_context_support_state,arena_primary_box,arena_primary_vt,sandbox_box_seed,sandbox_exact_seed,sandbox_vt_seed,preserved_not_budgeted,arena_box_signal,arena_exact_signal,play_card_any_exact,play_card_any_box,opportunity_gap_box,opportunity_gap_exact,profit_alert_support,compound_event_support,due_double_support,blackapple_support,r_consensus_support,survivor_support\n"
        "2026-01-05,NewYork4,Midday,080,1,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True\n"
        "2026-01-05,Texas4,Evening,735,5,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True\n",
    )
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
        {
            "metadata": {"credited_hits": 6},
            "hit_inventory": {
                "strict_box_hits": 2,
                "straight_hits": 1,
                "vtrac_only_hits": 3,
            },
            "ranking": {
                "median_rank_all_hits": 7.0,
                "median_rank_high_conviction": 5.0,
            },
        },
    )
    _write_text(
        window_root / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv",
        "date,state_key,period,winner,board_rank,top_primary_target,best_clean_host,arena_primary_box,arena_primary_vt,sandbox_box_seed,sandbox_exact_seed,sandbox_vt_seed,preserved_not_budgeted,arena_box_signal,arena_exact_signal,play_straight_hit,play_box_strict_hit,play_box_any_hit,play_card_any_box,play_card_any_exact,arena_final_candidate_signature,profit_alert_direct_match,profit_alert_implied_match,compound_event_present,blackapple_status,due_double_support,inventory_type,due_double_period_rank,due_double_combined_rank,due_double_family_match_rank,double_context_strength,hit_primary_class\n"
        "2026-01-05,NewYork4,Midday,080,1,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,CLEAR_ARENA_FINALIST,True,False,False,ALERT,True,double,2,3,1,STRONG,STRAIGHT\n"
        "2026-01-05,Texas4,Evening,735,5,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,PARTIAL_ARENA_FINALIST,False,True,True,WATCH,False,mirror_double,7,8,6,MEDIUM,VTRAC_ONLY\n",
    )
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
        {
            "event_layer": {
                "any_candidate_like_events": {"count": 4, "denominator": 10, "rate": 0.4},
                "vt_like_events": {"count": 3, "denominator": 10, "rate": 0.3},
                "boxlike_events": {"count": 2, "denominator": 10, "rate": 0.2},
            },
            "hit_layer": {
                "finalist_supported_hits": {"count": 5, "denominator": 6, "rate": 5 / 6},
                "straight_with_finalist_support": {"count": 1, "denominator": 1, "rate": 1.0},
                "strict_box_with_finalist_support": {"count": 2, "denominator": 2, "rate": 1.0},
            },
            "opportunity_layer": {
                "gap_rows_with_explicit_arena_box": {"count": 2, "denominator": 2, "rate": 1.0},
            },
        },
    )
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        {
            "signature_mix": {
                "signature_counts": {
                    "HIDDEN_COMPRESSED_FRONTIER": 4,
                    "FEEDER_TO_FRONTIER": 3,
                    "VTRAC_FRONTIER": 2,
                }
            }
        },
    )
    _write_text(
        window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv",
        "date,state_key,winner,best_board_rank,frontier_signature_type,signature_strength,literal_frontier_score,family_frontier_score,vtrac_frontier_score,frontier_purity_score,vertical_stability_score,cross_variant_echo_score,compression_score,hidden_winner_score,feeder_progression_score,double_anchor_score,frontier_strength_score,credited_event_count,hit_class_rollup,arena_final_candidate_signature_best,double_context_strength_best,inventory_types,fired_tests\n"
        "2026-01-05,NewYork4,080,1,HIDDEN_COMPRESSED_FRONTIER,STRONG,0.22,0.46,0.41,0.65,1.0,0.66,1.0,0.78,0.61,0.72,82.0,1,STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED,CLEAR_ARENA_FINALIST,STRONG,double,\"hidden_mask_v1,feeder_progression_v1,vtrac_frontier_v1,double_anchor_v1\"\n"
        "2026-01-05,Texas4,735,5,VTRAC_FRONTIER,MEDIUM,0.04,0.18,0.39,0.33,1.0,0.50,1.0,0.31,0.42,0.48,61.0,1,NONE,PARTIAL_ARENA_FINALIST,MEDIUM,mirror_double,\"vtrac_frontier_v1,feeder_progression_v1\"\n"
        "2026-01-05,Florida4,994,7,FEEDER_TO_FRONTIER,MEDIUM,0.01,0.24,0.28,0.29,1.0,0.40,1.0,0.36,0.71,0.30,58.0,0,NONE,LIGHT_ARENA_FINALIST,MEDIUM,double,\"family_frontier_v1,feeder_progression_v1\"\n"
        "2026-01-05,Ohio4,222,11,HIDDEN_COMPRESSED_FRONTIER,MEDIUM,0.03,0.17,0.26,0.21,1.0,0.38,1.0,0.54,0.46,0.22,55.0,0,NONE,,WEAK,,\"hidden_mask_v1,feeder_progression_v1\"\n",
    )
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        {
            "summary": {
                "winner_events": 10,
                "translator_rows": 3,
                "cohort_counts": {"BOX_GAP": 1, "BOX_CONVERTED": 1, "VT_FINALIST": 1},
            }
        },
    )
    _write_text(
        window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv",
        "date,state_key,period,winner,board_rank,primary_cohort,cohort_tags,frontier_signature_type,arena_final_candidate_signature,double_context_strength,inventory_type,due_double_period_rank,due_double_combined_rank,due_double_family_match_rank\n"
        "2026-01-05,NewYork4,Midday,080,1,BOX_CONVERTED,BOX_CONVERTED|ARENA_EXPLICIT,HIDDEN_COMPRESSED_FRONTIER,CLEAR_ARENA_FINALIST,STRONG,double,2,3,1\n"
        "2026-01-05,Texas4,Evening,735,5,VT_FINALIST,VT_FINALIST|VT_CONVERTED,VTRAC_FRONTIER,PARTIAL_ARENA_FINALIST,MEDIUM,mirror_double,7,8,6\n"
        "2026-01-05,Florida4,Evening,994,7,BOX_GAP,BOX_GAP|ARENA_EXPLICIT,FEEDER_TO_FRONTIER,LIGHT_ARENA_FINALIST,MEDIUM,double,5,6,4\n",
    )
    _write_json(
        window_root / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json",
        {
            "window_overview": {"winner_events": 10},
            "translator_learning_ledger": {"summary": {"cohort_counts": {"BOX_GAP": 1}}},
            "winner_html_frontier": {"case_count": 4},
        },
    )
    _write_json(
        analysis_dir / "2026-01-05__BOARD_SCOREBOARD__analysis_arena_day_review.json",
        {
            "board_verdict": {
                "top_primary_target": "NewYork4",
                "best_clean_host": "NewYork4",
                "highest_context_support_state": "NewYork4",
            },
            "scoreboard_rows": [
                {"state_key": "NewYork4", "score_rank": 1},
                {"state_key": "Texas4", "score_rank": 5},
            ],
        },
    )
    return window_root


def test_window_performance_gap_and_deep_analysis_reports(tmp_path, monkeypatch) -> None:
    from scripts.tools import analysis_arena_window_utils as util
    from scripts.tools import create_window_deep_analysis_report as deep
    from scripts.tools import create_window_pure_arena_finalist_scorecard as scorecard
    from scripts.tools import create_window_performance_gap_report as gap

    window_root = _seed_window(tmp_path)

    monkeypatch.setattr(util, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "UTILS_REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "DEFAULT_RESULTS_ROOT", tmp_path / "data" / "results")
    monkeypatch.setattr(deep, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(scorecard, "REPO_ROOT", tmp_path)

    perf_md = window_root / "gap.md"
    perf_json = window_root / "gap.json"
    perf_ledger = window_root / "gap.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_performance_gap_report.py",
            "--window-root",
            str(window_root),
            "--results-root",
            str(tmp_path / "data" / "results"),
            "--out-md",
            str(perf_md),
            "--out-json",
            str(perf_json),
            "--out-ledger",
            str(perf_ledger),
            "--force",
        ],
    )
    gap.main()

    perf_payload = json.loads(perf_json.read_text(encoding="utf-8"))
    assert perf_payload["summary_counts"]["winner_events"] == 2
    assert perf_payload["summary_counts"]["winner_on_board"] == 2
    assert perf_payload["summary_counts"]["play_card_any_box"] == 2
    assert perf_payload["summary_counts"]["cu_exact"] == 2
    assert "Arena Intrinsic Quality" in perf_md.read_text(encoding="utf-8")

    _write_text(
        window_root / f"{window_root.name}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
        perf_ledger.read_text(encoding="utf-8"),
    )
    _write_text(
        window_root / f"{window_root.name}__ANALYSIS_ARENA__HIT_ROSTER.csv",
        "date,state_key,period,winner,board_rank,top_primary_target,best_clean_host,arena_primary_box,arena_primary_vt,sandbox_box_seed,sandbox_exact_seed,sandbox_vt_seed,preserved_not_budgeted,arena_box_signal,arena_exact_signal,play_straight_hit,play_box_strict_hit,play_box_any_hit,play_card_any_box,play_card_any_exact,arena_final_candidate_signature,arena_final_candidate_signature_score\n"
        "2026-01-05,NewYork4,Midday,080,1,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,CLEAR_ARENA_FINALIST,4\n"
        "2026-01-05,Texas4,Evening,735,5,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,PARTIAL_ARENA_FINALIST,2\n",
    )

    frontier_json = window_root / "frontier.json"
    _write_json(
        frontier_json,
        {
            "metadata": {
                "case_count": 2,
                "warnings": [],
                "window_dates": ["2026-01-05"],
                "window_root": str(window_root),
            },
            "signature_mix": {
                "signature_counts": {
                    "HIDDEN_COMPRESSED_FRONTIER": 1,
                    "VTRAC_FRONTIER": 1,
                },
                "hit_class_counts": {
                    "STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED": 1,
                    "BOXED|VTRAC_BOXED": 1,
                },
                "inventory_type_counts": {
                    "double": 1,
                    "mirror_double": 1,
                },
                "signature_strength_counts": {
                    "HIGH": 2,
                },
                "blackapple_status_counts": {
                    "ALERT": 1,
                    "WATCH": 1,
                },
            },
            "score_averages": {
                "vertical_stability_score": 0.95,
                "hidden_winner_score": 0.44,
                "feeder_progression_score": 0.51,
                "frontier_strength_score": 64.2,
            },
            "promotion_queue": [
                {
                    "action": "TEST_IN_TRANSLATOR",
                    "theme": "Hidden compressed frontier",
                    "reason": "Repeated hidden winner-family survival.",
                }
            ],
            "notable_cases": {
                "strongest": {
                    "date": "2026-01-05",
                    "state": "NewYork4",
                    "winner": "080",
                    "frontier_signature_type": "VTRAC_FRONTIER",
                    "signature_strength": "HIGH",
                }
            },
            "cases": [],
        },
    )

    pure_arena_json = window_root / "pure_arena.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_pure_arena_finalist_scorecard.py",
            "--window-root",
            str(window_root),
            "--frontier-json",
            str(frontier_json),
            "--out-md",
            str(window_root / "pure_arena.md"),
            "--out-json",
            str(pure_arena_json),
            "--force",
        ],
    )
    scorecard.main()

    translator_json = window_root / "translator.json"
    _write_json(
        translator_json,
        {
            "summary": {
                "winner_events": 2,
                "translator_rows": 2,
                "cohort_counts": {
                    "BOX_GAP": 1,
                    "BOX_CONVERTED": 1,
                },
                "frontier_signature_counts": {
                    "HIDDEN_COMPRESSED_FRONTIER": 1,
                    "VTRAC_FRONTIER": 1,
                },
                "rates": {
                    "box_gap_rows": 0.5,
                    "exact_gap_rows": 0.0,
                    "box_converted_rows": 0.5,
                    "vt_converted_rows": 0.0,
                },
            },
            "examples": {
                "priority_rows": [
                    {
                        "date": "2026-01-05",
                        "state": "NewYork4",
                        "period": "Midday",
                        "winner": "080",
                        "board_rank": 1,
                        "primary_cohort": "BOX_GAP",
                        "frontier_signature_type": "HIDDEN_COMPRESSED_FRONTIER",
                    }
                ]
            },
            "interpretation": ["Use this ledger as a translator teaching cohort."],
        },
    )

    _write_json(
        (window_root / "VALIDATION" / "2026-01-05__BRAIN2_TRACKER_LEDGER.json"),
        {
            "metadata": {
                "results_date": "2026-01-05",
                "history_date": "2026-01-04",
            },
            "profit_alerts": {
                "top_states": [
                    {"state_key": "NewYork4", "board_rank": 1, "alert_count": 2, "strength_sum": 7.0},
                ],
                "scoreboard_carries": [
                    {"state_key": "NewYork4", "board_rank": 1, "hint": "A05"},
                ],
            },
            "compound_events": {
                "top_rows": [
                    {"state_key": "NewYork4", "variant": "Combined", "top_event": "ENGINE_GOV", "priority": 3},
                ],
                "scoreboard_carries": [
                    {"state_key": "NewYork4", "board_rank": 1, "hint": "ENGINE_GOV"},
                ],
            },
            "blackapple": {
                "alert_states": [
                    {"state_key": "NewYork4", "variant": "Combined", "ba_score": 4},
                ],
                "watch_states": [],
                "scoreboard_carries": [
                    {"state_key": "NewYork4", "board_rank": 1, "hint": "008"},
                ],
            },
            "due_doubles": {
                "threshold_states": [
                    {"state_key": "NewYork4", "board_rank": 1, "draws_since_double": 8},
                ],
                "daily_double_events": ["`NewYork4` `Midday` winner=`080` type=`double` rank=`1` DS=`8` mirror_pairs=`-`"],
                "scoreboard_carries": [
                    {"state_key": "NewYork4", "board_rank": 1, "hint": "0/5-1/6"},
                ],
            },
            "repeat_watch": {
                "top_rows": [
                    {"state_key": "NewYork4", "variant": "Combined", "current_index": "6", "current_equals_winner_vtrac": True},
                ],
                "exact_hits": [
                    {"state_key": "NewYork4", "variant": "Combined", "current_index": "6", "current_equals_winner_vtrac": True},
                ],
            },
            "consensus": {
                "scoreboard_carries": [
                    {"state_key": "NewYork4", "board_rank": 1, "hint": "tail 08"},
                ],
            },
        },
    )

    deep_md = window_root / "deep.md"
    deep_json = window_root / "deep.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_deep_analysis_report.py",
            "--window-root",
            str(window_root),
            "--performance-gap-json",
            str(perf_json),
            "--frontier-json",
            str(frontier_json),
            "--pure-arena-scorecard-json",
            str(pure_arena_json),
            "--translator-ledger-json",
            str(translator_json),
            "--out-md",
            str(deep_md),
            "--out-json",
            str(deep_json),
            "--force",
        ],
    )
    deep.main()

    deep_payload = json.loads(deep_json.read_text(encoding="utf-8"))
    assert deep_payload["window_overview"]["winner_events"] == 2
    assert deep_payload["tracker_families"]["doubles_result_types"]["double"] == 1
    assert deep_payload["tracker_families"]["daily_tracker_ledgers_present"]["count"] == 1
    assert deep_payload["tracker_families"]["daily_tracker_rollup"]["profit_alert_states"][0]["value"] == "NewYork4"
    assert deep_payload["winner_html_frontier"]["case_count"] == 2
    assert deep_payload["winner_html_frontier"]["signature_counts"]["HIDDEN_COMPRESSED_FRONTIER"] == 1
    assert deep_payload["winner_html_frontier"]["promotion_queue"][0]["action"] == "TEST_IN_TRANSLATOR"
    assert deep_payload["pure_arena_finalist_layer"]["event_layer"]["winner_events"] == 2
    assert deep_payload["translator_learning_ledger"]["summary"]["cohort_counts"]["BOX_GAP"] == 1
    assert "Shared Complexes / Carryover / Decay" in deep_md.read_text(encoding="utf-8")
    assert "Winner HTML Frontier" in deep_md.read_text(encoding="utf-8")
    assert "Pure Arena Finalist / Candidate Layer" in deep_md.read_text(encoding="utf-8")
    assert "Translator Learning Ledger" in deep_md.read_text(encoding="utf-8")
    assert "Daily tracker ledgers present" in deep_md.read_text(encoding="utf-8")


def test_arena_vs_legacy_window_comparison_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_arena_vs_legacy_window_comparison_report as compare

    window_root, legacy_runs = _seed_legacy_comparison_window(tmp_path)
    monkeypatch.setattr(compare, "REPO_ROOT", tmp_path)

    out_md = window_root / "compare.md"
    out_json = window_root / "compare.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_arena_vs_legacy_window_comparison_report.py",
            "--window-root",
            str(window_root),
            "--legacy-runs-root",
            str(legacy_runs),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--force",
        ],
    )
    compare.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["legacy"]["candidate_universe"]["counts"]["box_hit"] == 1
    assert payload["legacy"]["dashboard"]["total_graded_outcomes"] == 2
    assert any(
        row["strategy"] == "v0_2_default" and row["budget_label"] == "B36"
        for row in payload["downstream_replay"]["curated_strategy_rows"]
    )
    text = out_md.read_text(encoding="utf-8")
    assert "Shared Downstream Strategy Replay" in text
    assert "Historical Codex Context" in text


def test_window_deep_hit_analysis_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_window_deep_hit_analysis_report as hit

    window_root, runs_root, sharepacks_root = _seed_hit_analysis_window(tmp_path)
    monkeypatch.setattr(hit, "REPO_ROOT", tmp_path)

    out_md = window_root / "hits.md"
    out_json = window_root / "hits.json"
    out_csv = window_root / "hits.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_deep_hit_analysis_report.py",
            "--window-root",
            str(window_root),
            "--runs-root",
            str(runs_root),
            "--sharepacks-root",
            str(sharepacks_root),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-csv",
            str(out_csv),
            "--force",
        ],
    )
    hit.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["metadata"]["credited_hits"] == 2
    assert payload["hit_inventory"]["straight_hits"] == 1
    assert payload["hit_inventory"]["vtrac_only_hits"] == 1
    assert payload["hit_inventory"]["credit_signature_counts"]["STRAIGHT+VTRAC"] == 1
    roster = out_csv.read_text(encoding="utf-8")
    assert "hit_class" in roster
    assert "credit_signature" in roster
    assert "budget_floor" in roster
    assert "STRAIGHT" in roster
    assert "VTRAC_ONLY" in roster
    text = out_md.read_text(encoding="utf-8")
    assert "Hit Inventory" in text
    assert "Arena Final-Candidate Signatures" in text


def test_window_pure_arena_finalist_scorecard_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_window_pure_arena_finalist_scorecard as scorecard

    window_root, _runs_root, _sharepacks_root = _seed_hit_analysis_window(tmp_path)
    monkeypatch.setattr(scorecard, "REPO_ROOT", tmp_path)

    frontier_json = window_root / "frontier.json"
    _write_json(
        frontier_json,
        {
            "signature_mix": {
                "signature_counts": {
                    "HIDDEN_COMPRESSED_FRONTIER": 1,
                    "VTRAC_FRONTIER": 1,
                }
            },
            "promotion_queue": [
                {"signal": "Hidden compressed winner-family frontier"},
                {"signal": "Feeder-to-frontier progression"},
            ],
        },
    )

    out_md = window_root / "pure_finalist.md"
    out_json = window_root / "pure_finalist.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_pure_arena_finalist_scorecard.py",
            "--window-root",
            str(window_root),
            "--frontier-json",
            str(frontier_json),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--force",
        ],
    )
    scorecard.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["event_layer"]["winner_events"] == 2
    assert payload["event_layer"]["vt_like_events"]["count"] == 2
    assert payload["event_layer"]["boxlike_events"]["count"] == 1
    assert payload["hit_layer"]["finalist_supported_hits"]["count"] == 2
    assert payload["opportunity_layer"]["opportunity_gap_box_rows"]["count"] == 0
    assert payload["frontier_context"]["signature_counts"]["HIDDEN_COMPRESSED_FRONTIER"] == 1
    text = out_md.read_text(encoding="utf-8")
    assert "Pure Arena Finalist / Candidate Scorecard" in text
    assert "Event-Level Finalist Territory" in text


def test_window_translator_learning_ledger_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_window_translator_learning_ledger as ledger

    window_root, _runs_root, _sharepacks_root = _seed_hit_analysis_window(tmp_path)
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)

    out_md = window_root / "translator.md"
    out_json = window_root / "translator.json"
    out_csv = window_root / "translator.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_translator_learning_ledger.py",
            "--window-root",
            str(window_root),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-csv",
            str(out_csv),
            "--force",
        ],
    )
    ledger.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["summary"]["translator_rows"] == 2
    assert payload["summary"]["cohort_counts"]["VT_FINALIST"] == 2
    assert payload["summary"]["cohort_counts"]["PRESERVED"] == 1
    assert "cohort_tags" in out_csv.read_text(encoding="utf-8")
    assert "Translator-Learning Ledger" in out_md.read_text(encoding="utf-8")


def test_window_c1_c2_frontier_harness_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_window_c1_c2_frontier_harness_report as frontier

    window_root, _runs_root, _sharepacks_root = _seed_hit_analysis_window(tmp_path)
    monkeypatch.setattr(frontier, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(frontier, "DEFAULT_WINNER_HTML_ROOT", tmp_path / "reports" / "stable" / "winners_by_date")
    monkeypatch.setattr(frontier, "DEFAULT_TRUTH_SHAREPACKS_ROOT", tmp_path / "sharepacks")

    out_md = window_root / "frontier.md"
    out_json = window_root / "frontier.json"
    out_csv = window_root / "frontier.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_c1_c2_frontier_harness_report.py",
            "--window-root",
            str(window_root),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-csv",
            str(out_csv),
            "--force",
        ],
    )
    frontier.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["metadata"]["case_count"] == 2
    assert payload["signature_mix"]["signature_counts"]["FEEDER_TO_FRONTIER"] == 1
    assert payload["signature_mix"]["signature_counts"]["HIDDEN_COMPRESSED_FRONTIER"] == 1
    assert payload["promotion_queue"]
    roster = out_csv.read_text(encoding="utf-8")
    assert "frontier_signature_type" in roster
    assert "literal_frontier_score" in roster
    assert "hit_class_rollup" in roster
    assert "VTRAC_STRAIGHT" in roster
    assert "VTRAC_BOXED" in roster
    text = out_md.read_text(encoding="utf-8")
    assert "Promotion Queue" in text
    assert "Signature Mix" in text


def test_cross_window_rollup_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_analysis_arena_cross_window_rollup as rollup

    w1 = _seed_cross_window_rollup_window(tmp_path, "2026-01-01_to_2026-01-03", cand_rate=0.4, box_rate=0.1)
    w2 = _seed_cross_window_rollup_window(tmp_path, "2026-01-05_to_2026-01-09", cand_rate=0.5, box_rate=0.2)
    monkeypatch.setattr(rollup, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(rollup, "DEFAULT_RUNS2_ROOT", tmp_path / "runs2")
    monkeypatch.setattr(rollup, "DEFAULT_FINAL_DOCS", tmp_path / "final_docs")

    out_md = tmp_path / "final_docs" / "rollup.md"
    out_json = tmp_path / "final_docs" / "rollup.json"
    out_csv = tmp_path / "final_docs" / "rollup.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_analysis_arena_cross_window_rollup.py",
            "--runs2-root",
            str(tmp_path / "runs2"),
            "--window-root",
            str(w1),
            "--window-root",
            str(w2),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-csv",
            str(out_csv),
            "--force",
        ],
    )
    rollup.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["summary"]["window_count"] == 2
    assert payload["summary"]["winner_events"] == 20
    assert payload["rows"][0]["frontier_top_signature"] == "HIDDEN_COMPRESSED_FRONTIER"
    assert "Window Table" in out_md.read_text(encoding="utf-8")
    assert "candidate_like_event_rate" in out_csv.read_text(encoding="utf-8")


def test_tuneup_diagnostics_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_analysis_arena_tuneup_diagnostics as tuneup

    w1 = _seed_cross_window_rollup_window(tmp_path, "2026-01-01_to_2026-01-03", cand_rate=0.4, box_rate=0.1)
    w2 = _seed_cross_window_rollup_window(tmp_path, "2026-01-05_to_2026-01-09", cand_rate=0.5, box_rate=0.2)
    monkeypatch.setattr(tuneup, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(tuneup, "DEFAULT_RUNS2_ROOT", tmp_path / "runs2")
    monkeypatch.setattr(tuneup, "DEFAULT_FINAL_DOCS", tmp_path / "final_docs")

    out_md = tmp_path / "final_docs" / "tuneup.md"
    out_json = tmp_path / "final_docs" / "tuneup.json"
    out_rank = tmp_path / "final_docs" / "ranking.csv"
    out_track = tmp_path / "final_docs" / "tracker.csv"
    out_double = tmp_path / "final_docs" / "doubles.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_analysis_arena_tuneup_diagnostics.py",
            "--runs2-root",
            str(tmp_path / "runs2"),
            "--window-root",
            str(w1),
            "--window-root",
            str(w2),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-ranking-csv",
            str(out_rank),
            "--out-tracker-csv",
            str(out_track),
            "--out-doubles-csv",
            str(out_double),
            "--force",
        ],
    )
    tuneup.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["brain2_ranking"]["repeated_false_positive_top_states"][0]["state_key"] == "NewYork4"
    assert payload["tracker_lift"]["rows"]
    assert payload["doubles_subtype"]["rows"]
    assert "Brain 2 Ranking Diagnostic" in out_md.read_text(encoding="utf-8")
    assert "state_key" in out_rank.read_text(encoding="utf-8")
    assert "signal" in out_track.read_text(encoding="utf-8")
    assert "dimension" in out_double.read_text(encoding="utf-8")


def test_frontier_negative_control_study_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_analysis_arena_frontier_negative_control_study as study

    w1 = _seed_cross_window_rollup_window(tmp_path, "2026-01-01_to_2026-01-03", cand_rate=0.4, box_rate=0.1)
    w2 = _seed_cross_window_rollup_window(tmp_path, "2026-01-05_to_2026-01-09", cand_rate=0.5, box_rate=0.2)
    monkeypatch.setattr(study, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(study, "DEFAULT_RUNS2_ROOT", tmp_path / "runs2")
    monkeypatch.setattr(study, "DEFAULT_FINAL_DOCS", tmp_path / "final_docs")

    out_md = tmp_path / "final_docs" / "frontier_negative_control.md"
    out_json = tmp_path / "final_docs" / "frontier_negative_control.json"
    out_cases = tmp_path / "final_docs" / "frontier_negative_control_cases.csv"
    out_lifts = tmp_path / "final_docs" / "frontier_negative_control_lifts.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_analysis_arena_frontier_negative_control_study.py",
            "--runs2-root",
            str(tmp_path / "runs2"),
            "--window-root",
            str(w1),
            "--window-root",
            str(w2),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--out-cases-csv",
            str(out_cases),
            "--out-lifts-csv",
            str(out_lifts),
            "--force",
        ],
    )
    study.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["metadata"]["case_count"] == 8
    assert payload["cohort_counts"]["strict_box"] == 2
    assert payload["cohort_counts"]["box_gap"] == 2
    assert payload["cohort_counts"]["vt_only"] == 2
    assert payload["cohort_counts"]["no_conversion"] == 2
    assert payload["top_discriminative_features"]["box_gap_vs_no_conversion"]
    assert "Cohort Inventory" in out_md.read_text(encoding="utf-8")
    assert "feature_label" in out_lifts.read_text(encoding="utf-8")
    assert "frontier_signature_type" in out_cases.read_text(encoding="utf-8")


def test_fresh_window_readiness_report(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_analysis_arena_fresh_window_readiness_report as readiness

    w1 = _seed_cross_window_rollup_window(tmp_path, "2026-01-01_to_2026-01-03", cand_rate=0.4, box_rate=0.1)
    w2 = _seed_cross_window_rollup_window(tmp_path, "2026-01-05_to_2026-01-09", cand_rate=0.5, box_rate=0.2)
    w3 = _seed_cross_window_rollup_window(tmp_path, "2026-01-15_to_2026-01-22", cand_rate=0.45, box_rate=0.15)
    monkeypatch.setattr(readiness, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(readiness, "DEFAULT_RUNS2_ROOT", tmp_path / "runs2")
    monkeypatch.setattr(readiness, "DEFAULT_FINAL_DOCS", tmp_path / "final_docs")

    final_docs = tmp_path / "final_docs"
    _write_text(final_docs / "AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md", "# index\n")
    _write_text(final_docs / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md", "# quickstart\n")
    _write_text(final_docs / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md", "# flow\n")
    _write_text(final_docs / "README.md", "# readme\n")
    _write_text(final_docs / "AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md", "# macro\n")
    _write_text(tmp_path / "runs2" / "PORTAL.md", "# portal\n")
    _write_json(final_docs / "AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.json", {"summary": {"window_count": 3, "winner_events": 30, "credited_hits": 18}})
    _write_json(
        final_docs / "AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.json",
        {
            "brain2_ranking": {
                "repeated_false_positive_top_states": [{"state_key": "NewYork4"}],
                "productive_non_primary_states": [{"state_key": "Texas4"}],
            },
            "tracker_lift": {"rows": [{"signal": "arena_box_signal"}]},
            "doubles_subtype": {"rows": [{"dimension": "all_hits"}]},
        },
    )
    _write_json(
        final_docs / "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.json",
        {
            "metadata": {"case_count": 12},
            "cohort_counts": {"strict_box": 3, "box_gap": 2, "no_conversion": 4},
        },
    )

    out_md = final_docs / "fresh_window_readiness.md"
    out_json = final_docs / "fresh_window_readiness.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_analysis_arena_fresh_window_readiness_report.py",
            "--runs2-root",
            str(tmp_path / "runs2"),
            "--window-root",
            str(w1),
            "--window-root",
            str(w2),
            "--window-root",
            str(w3),
            "--out-md",
            str(out_md),
            "--out-json",
            str(out_json),
            "--force",
        ],
    )
    readiness.main()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["metadata"]["ready_for_fresh_windows"] is True
    assert payload["readiness_checks"]["minimum_completed_windows_met"] is True
    assert payload["readiness_checks"]["frontier_control_populated"] is True
    assert payload["rollup_summary"]["window_count"] == 3
    assert "Ready for fresh windows" in out_md.read_text(encoding="utf-8")
