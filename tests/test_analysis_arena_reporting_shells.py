from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.tools import create_control_center_daily_run_report as cc_daily
from scripts.tools import create_day_synthesis_run_report as day_syn
from scripts.tools import create_master_validation_run_report as state_mv
from scripts.tools import create_predictive_portfolio_report as predictive_portfolio
from scripts.tools import create_predictive_run_report as predictive_run
from scripts.tools import fill_master_validation_run_report as fill_mv


def _write_text(path: Path, text: str = "# Stub\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _patch_predictive_run_paths(monkeypatch, repo_root: Path) -> None:
    monkeypatch.setattr(predictive_run, "REPO_ROOT", repo_root)
    monkeypatch.setattr(predictive_run, "RUNS2_PREDICTIVE_DIR", repo_root / "runs2" / "predictive")
    final_docs = repo_root / "final_docs"
    monkeypatch.setattr(predictive_run, "FINAL_DOCS_DIR", final_docs)
    monkeypatch.setattr(predictive_run, "SYSTEM_MAP_PATH", final_docs / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md")
    monkeypatch.setattr(predictive_run, "OPERATING_FLOW_PATH", final_docs / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md")
    monkeypatch.setattr(predictive_run, "CADENCE_QUICKSTART_PATH", final_docs / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md")
    monkeypatch.setattr(predictive_run, "ARENA_CONTRACT_PATH", final_docs / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md")
    monkeypatch.setattr(predictive_run, "CONTEXT_FEED_PATH", final_docs / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md")
    monkeypatch.setattr(predictive_run, "STRING_FEED_PATH", final_docs / "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md")
    monkeypatch.setattr(
        predictive_run,
        "TRANSLATION_TEMPLATE_PATH",
        final_docs / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )


def _patch_state_mv_paths(monkeypatch, repo_root: Path) -> None:
    monkeypatch.setattr(state_mv, "REPO_ROOT", repo_root)
    monkeypatch.setattr(state_mv, "RUNS2_DIR", repo_root / "runs2" / "validation")
    final_docs = repo_root / "final_docs"
    monkeypatch.setattr(state_mv, "FINAL_DOCS_DIR", final_docs)
    monkeypatch.setattr(state_mv, "STATE_TEMPLATE_PATH", final_docs / "AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md")
    monkeypatch.setattr(state_mv, "ARENA_CONTRACT_PATH", final_docs / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md")
    monkeypatch.setattr(state_mv, "CONTEXT_FEED_PATH", final_docs / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md")
    monkeypatch.setattr(state_mv, "STRING_FEED_PATH", final_docs / "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md")
    monkeypatch.setattr(state_mv, "SYSTEM_MAP_PATH", final_docs / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md")
    monkeypatch.setattr(
        state_mv,
        "TRANSLATION_TEMPLATE_PATH",
        final_docs / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )
    monkeypatch.setattr(state_mv, "BRAIN2_TEMPLATE_PATH", final_docs / "AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md")
    monkeypatch.setattr(
        state_mv,
        "BRAIN2_MV_TEMPLATE_PATH",
        final_docs / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )


def _patch_control_center_paths(monkeypatch, repo_root: Path) -> None:
    monkeypatch.setattr(cc_daily, "REPO_ROOT", repo_root)
    monkeypatch.setattr(cc_daily, "RUNS2_VALIDATION_DIR", repo_root / "runs2" / "validation")
    final_docs = repo_root / "final_docs"
    runs_docs = repo_root / "runs_docs"
    monkeypatch.setattr(cc_daily, "FINAL_DOCS_DIR", final_docs)
    monkeypatch.setattr(cc_daily, "RUNS_DIR", runs_docs)
    monkeypatch.setattr(cc_daily, "CONTROL_CENTER_TEMPLATE_PATH", final_docs / "AAT9_Control_Center_Daily_Template.md")
    monkeypatch.setattr(cc_daily, "BRAIN2_TEMPLATE_PATH", final_docs / "AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md")
    monkeypatch.setattr(
        cc_daily,
        "BRAIN2_MV_TEMPLATE_PATH",
        final_docs / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )
    monkeypatch.setattr(cc_daily, "CONTEXT_FEED_PATH", final_docs / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md")
    monkeypatch.setattr(cc_daily, "SYSTEM_MAP_PATH", final_docs / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md")
    monkeypatch.setattr(cc_daily, "ARENA_CONTRACT_PATH", runs_docs / "2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md")
    monkeypatch.setattr(cc_daily, "ARENA_HANDOFF_PATH", runs_docs / "2026-03-16__AUX_CONTROL_CENTER__HANDOFF.md")
    monkeypatch.setattr(cc_daily, "ARENA_EXPORT_SLICE_PATH", runs_docs / "2026-03-16__AUX_CONTROL_CENTER__EXPORT_SLICE.md")


def _patch_day_synthesis_paths(monkeypatch, repo_root: Path) -> None:
    monkeypatch.setattr(day_syn, "REPO_ROOT", repo_root)
    monkeypatch.setattr(day_syn, "RUNS2_VALIDATION_DIR", repo_root / "runs2" / "validation")
    final_docs = repo_root / "final_docs"
    monkeypatch.setattr(day_syn, "FINAL_DOCS_DIR", final_docs)
    monkeypatch.setattr(day_syn, "SYSTEM_MAP_PATH", final_docs / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md")
    monkeypatch.setattr(day_syn, "OPERATING_FLOW_PATH", final_docs / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md")
    monkeypatch.setattr(day_syn, "STATE_TEMPLATE_PATH", final_docs / "AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md")
    monkeypatch.setattr(
        day_syn,
        "BRAIN2_MV_TEMPLATE_PATH",
        final_docs / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )


def _patch_predictive_portfolio_paths(monkeypatch, repo_root: Path) -> None:
    monkeypatch.setattr(predictive_portfolio, "REPO_ROOT", repo_root)
    monkeypatch.setattr(predictive_portfolio, "RUNS2_PREDICTIVE_DIR", repo_root / "runs2" / "predictive")
    final_docs = repo_root / "final_docs"
    monkeypatch.setattr(predictive_portfolio, "FINAL_DOCS_DIR", final_docs)
    monkeypatch.setattr(predictive_portfolio, "SYSTEM_MAP_PATH", final_docs / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md")
    monkeypatch.setattr(predictive_portfolio, "OPERATING_FLOW_PATH", final_docs / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md")
    monkeypatch.setattr(predictive_portfolio, "CADENCE_QUICKSTART_PATH", final_docs / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md")
    monkeypatch.setattr(predictive_portfolio, "ARENA_CONTRACT_PATH", final_docs / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md")
    monkeypatch.setattr(
        predictive_portfolio,
        "TRANSLATION_TEMPLATE_PATH",
        final_docs / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
    )


def _seed_final_docs(repo_root: Path) -> None:
    final_docs = repo_root / "final_docs"
    for name in [
        "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md",
        "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md",
        "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md",
        "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md",
        "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
        "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
        "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
        "AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
        "AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
        "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
        "AAT9_Control_Center_Daily_Template.md",
    ]:
        _write_text(final_docs / name)
    runs_docs = repo_root / "runs_docs"
    for name in [
        "2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md",
        "2026-03-16__AUX_CONTROL_CENTER__HANDOFF.md",
        "2026-03-16__AUX_CONTROL_CENTER__EXPORT_SLICE.md",
    ]:
        _write_text(runs_docs / name)


def _seed_predictive_state(repo_root: Path, *, date: str, state: str) -> None:
    day_dir = repo_root / "sharepacks" / "_predictive" / date
    state_dir = day_dir / state
    _write_json(day_dir / "control_center" / "meta.json", {"history_date": "2026-01-04"})
    _write_json(
        state_dir / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json",
        {
            "arena_synthesis": {
                "dominant_canonicals": [{"value": "025"}],
                "dominant_families": [{"value": "025"}],
                "dominant_vtrac_indices": [{"value": "3"}],
                "context_reinforced_canonicals": [{"value": "025"}],
                "context_only_pressure": [{"value": "008"}],
                "state_regime": {"dominant_canonical": "025", "tracker_posture": "tracker-rich"},
                "stable_survivor_context": {"available": True, "frontier_rows": 2, "progression_count": 3, "last_remaining_rows": 1, "hidden_terminal_frontier_count": 1, "top_frontier_canonicals": ["005", "008"]},
                "r_consensus_context": {"available": True, "event_count": 2, "signal_strength_class": "strong", "trial_eligible": True, "top_tail_values": ["08"], "top_support_canonicals": ["008"]},
                "vtrac_literal_watchlist": [{"vtrac_index": "3", "candidate_canonicals": ["025"]}],
            }
        },
    )
    _write_text(state_dir / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.md")
    _write_json(
        state_dir / "analysis" / "translation_sandbox_seed__tool_only__arena_v0.json",
        {
            "brain2_context": {
                "scoreboard_row": {
                    "score_rank": 7,
                    "role": "shared_host",
                    "targeting_bucket": "small_shoulder",
                    "tracker_posture": "tracker-rich",
                    "top_canonicals": ["025", "008"],
                    "top_vtrac_indices": ["3", "6"],
                },
                "positional_shortlist_top": [{"canonical": "008"}],
                "blackapple_recommended_canonicals": ["025"],
                "profit_alert_implied_canonicals": ["066"],
                "due_double_families": [{"variant": "Combined", "draws_since_double": 5, "families": [{"family": "0/5-1/6"}]}],
                "due_double_example_canonicals": ["001"],
                "top_profit_alerts": [{"variant": "Midday", "alert_id": "A05", "canonical": "066", "suggested": "BOX"}],
                "compound_events_top": [{"variant": "Combined", "top_event": "ENGINE_GOV", "priority": 85}],
            },
            "sandbox_hypotheses": {
                "diagnostic_boxed_seed": [{"value": "008"}],
                "diagnostic_straight_seed": [{"value": "800"}],
                "diagnostic_vt_box_seed": [{"value": "03"}],
            },
        },
    )
    _write_text(state_dir / "analysis" / "translation_sandbox_seed__tool_only__arena_v0.md")
    _write_json(state_dir / "candidate_universe__tool_only__arena_v0.json", {"packs": [{"method_id": "due_doubles", "canonicals": ["001"]}], "union_combos_count": 12, "contains_winners_artifacts": False})
    _write_json(state_dir / "play_card__tool_only__arena_v0.json", {"strategies": {"analysis_prefix": {"B12": {"boxed_canonicals_count": 2, "boxed_canonicals": ["025", "008"], "combos": ["025", "008"], "vtrac_pack": {"indices": [3], "pack_combos": ["025", "008"]}}}}})
    _write_text(state_dir / "play_card__tool_only__arena_v0.md")
    _write_json(state_dir / "signals_bundle__tool_only__arena_v0.json", {"signals": []})
    _write_json(state_dir / "aux" / state / "summary.json", {"draw_sources": {"snapshot_meta": {"mode": "predictive"}}})
    _write_text(state_dir / "aux" / state / "summary.md")
    _write_text(state_dir / "stable" / state / f"{state}_stable_patterns_scores.csv", "x\n")
    _write_text(state_dir / "stable" / state / f"{state}_stable_patterns_families.csv", "x\n")
    _write_text(state_dir / "stable" / state / f"{state}_stable_patterns_compound.csv", "x\n")
    _write_text(state_dir / "stable" / state / f"{state}_stable_patterns_report.html", "<html></html>\n")
    _write_json(state_dir / "stable" / state / f"{state}_metrics.json", {"ok": True})
    _write_text(state_dir / "digit_reduction" / state / f"{state}_digit_reduction_scores.csv", "x\n")
    _write_text(state_dir / "digit_reduction" / state / f"{state}_digit_reduction_report.html", "<html></html>\n")
    _write_text(state_dir / "digit_reduction" / state / f"{state}_digit_reduction_report_stacked.html", "<html></html>\n")
    _write_json(state_dir / "vtrac" / state / f"{state}_vtrac_enhanced_20260327_000000.json", {"ok": True})
    _write_json(state_dir / "vtrac" / state / "validation_report.json", {"ok": True})
    _write_text(state_dir / "vtrac" / state / "validation_report.md")
    _write_text(state_dir / "hot_zones" / state / f"{state}_hot_zones_top_lanes.csv", "x\n")
    _write_text(state_dir / "hot_zones" / state / f"{state}_hot_zones_per_lane.csv", "x\n")
    _write_json(state_dir / "hot_zones" / state / f"{state}_hot_zones_meta.json", {"ok": True})
    _write_json(state_dir / "hot_zones" / state / "2026-01-05_hot_zones_winner_map.json", {"ok": True})


def _seed_truth_state(repo_root: Path, *, date: str, state: str) -> None:
    _write_text(repo_root / "data" / "results" / f"{date}.txt", "New York\t080\t735\n")
    winners_dir = repo_root / "sharepacks" / date / state / "winners" / state
    _write_text(winners_dir / f"{state}_winner_080_latest.html", "<html></html>\n")
    _write_json(winners_dir / f"{state}_winner_080_latest.json", {"winner": "080"})


def _seed_control_center(repo_root: Path, *, date: str) -> None:
    predictive_cc = repo_root / "sharepacks" / "_predictive" / date / "control_center"
    truth_cc = repo_root / "sharepacks" / date / "control_center"
    _write_json(predictive_cc / "meta.json", {"history_date": "2026-01-04"})
    _write_text(
        predictive_cc / "blackapple_alerts.csv",
        "State,StateKey,Variant,BA-Score,Status,Triggers,#Candidates,Examples\nNew York,NewYork4,Evening,3,ALERT,Mirror,12,016 025 349\n",
    )
    _write_text(
        predictive_cc / "due_doubles.csv",
        "State,StateKey,Variant,Draws Since Double,Family 1,Winner Midday,Winner Evening,Midday Winner In Family,Evening Winner In Family\nNew York,NewYork4,Combined,5,0/5-1/6: 001(RC:1000),-,-,False,False\n",
    )
    _write_text(
        predictive_cc / "vtrac_repeat_watch.csv",
        "StateKey,Variant,Current Index,Current==WinnerVTRAC\nNewYork4,Evening,24,True\n",
    )
    _write_text(
        predictive_cc / "profit_alerts.csv",
        "State,StateKey,Variant,AlertId,Strength,Suggested,CapLines,DecayDraws,Badges,Canonical,ImpliedSet,Evidence\nNew York,NewYork4,Combined,A05,4,BOX,12,3,CONS,066,[\"066\"],{}\n",
    )
    _write_text(
        predictive_cc / "profit_compound_events.csv",
        "results_date,state_key,variant,top_event,priority,candidate_alert_ids\n2026-01-05,NewYork4,Combined,ENGINE_GOV,85,A05\n",
    )
    _write_text(
        truth_cc / "profit_alerts_eval.csv",
        "alert_id,hit_within_decay,hit_any_within_decay\nA05,Y,Y\n",
    )
    _write_text(
        truth_cc / "profit_alerts_eval_merged.csv",
        "state_key,variant,status,hit_any_within_decay,strength_max,alert_ids,promoters\nNewYork4,Combined,HIT,Y,4,A05,A11\n",
    )


def test_build_predictive_run_report_is_arena_native(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_predictive_run_paths(monkeypatch, repo_root)
    _seed_predictive_state(repo_root, date="2026-01-05", state="NewYork4")

    report = predictive_run.build_predictive_run_report(
        results_date="2026-01-05",
        state="NewYork4",
        profile="tool_only",
        experiment_tag="arena_v0",
        sharepacks_root=repo_root / "sharepacks" / "_predictive",
    )

    assert "Analysis Arena Predictive Run Report" in report
    assert "Aggregated arena contract" in report
    assert "Translation sandbox" in report
    assert "SUPERBRAIN_V0_2__DEFAULTS" not in report


def test_build_master_validation_run_report_uses_new_template_and_truth(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_state_mv_paths(monkeypatch, repo_root)
    _seed_predictive_state(repo_root, date="2026-01-05", state="NewYork4")
    _seed_truth_state(repo_root, date="2026-01-05", state="NewYork4")

    report = state_mv.build_master_validation_run_report(
        results_date="2026-01-05",
        state="NewYork4",
        profile="tool_only",
        experiment_tag="arena_v0",
        predictive_sharepacks_root=repo_root / "sharepacks" / "_predictive",
        truth_sharepacks_root=repo_root / "sharepacks",
    )

    assert "Analysis Arena Master Validation Run Report" in report
    assert "Per-state Master Validation template" in report
    assert "master_validation_FINAL_TEMPLATE_FINAL_VERSION" not in report
    assert "R-Consensus context" in report


def test_fill_master_validation_run_report_rewrites_in_place(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_state_mv_paths(monkeypatch, repo_root)
    monkeypatch.setattr(fill_mv, "REPO_ROOT", repo_root)
    monkeypatch.setattr(fill_mv, "RUNS2_DIR", repo_root / "runs2" / "validation")
    monkeypatch.setattr(fill_mv, "parse_iso_date", state_mv.parse_iso_date)
    monkeypatch.setattr(fill_mv, "normalize_tag", state_mv.normalize_tag)
    monkeypatch.setattr(fill_mv, "safe_rel", state_mv.safe_rel)
    monkeypatch.setattr(
        fill_mv,
        "build_master_validation_run_report",
        lambda **_: "# Rebuilt Arena Report\n",
    )
    out_path = repo_root / "runs2" / "validation" / "2026-01-05__NewYork4.md"
    monkeypatch.setattr(
        fill_mv,
        "_parse_args",
        lambda: argparse.Namespace(
            date="2026-01-05",
            state="NewYork4",
            profile="tool_only",
            experiment_tag="arena_v0",
            predictive_sharepacks_root="sharepacks/_predictive",
            truth_sharepacks_root="sharepacks",
            report_path=str(out_path),
        ),
    )

    fill_mv.main()

    assert out_path.read_text(encoding="utf-8") == "# Rebuilt Arena Report\n"


def test_build_control_center_daily_report_uses_predictive_and_truth_layers(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_control_center_paths(monkeypatch, repo_root)
    _seed_predictive_state(repo_root, date="2026-01-05", state="NewYork4")
    _seed_control_center(repo_root, date="2026-01-05")

    report = cc_daily.build_control_center_daily_report(
        results_date="2026-01-05",
        profile="tool_only",
        experiment_tag="arena_v0",
        predictive_sharepacks_root=repo_root / "sharepacks" / "_predictive",
        truth_sharepacks_root=repo_root / "sharepacks",
    )

    assert "Analysis Arena Control Center Daily Run Report" in report
    assert "Predictive Control Center dir" in report
    assert "Post-Results Profit Alert Evaluation" in report
    assert "sharepacks/_predictive/2026-01-05/control_center" in report


def test_build_day_synthesis_report_drops_corpus_summary_dependency(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_day_synthesis_paths(monkeypatch, repo_root)
    _seed_predictive_state(repo_root, date="2026-01-05", state="NewYork4")
    _write_text(repo_root / "data" / "results" / "2026-01-05.txt", "New York\t080\t735\n")
    validation_dir = repo_root / "runs2" / "validation"
    _write_text(validation_dir / "2026-01-05__NewYork4.md")
    _write_text(validation_dir / "2026-01-05__BRAIN2_MASTER_VALIDATION.md")
    _write_text(validation_dir / "2026-01-05__CONTROL_CENTER.md")

    report = day_syn.build_day_synthesis_report(
        results_date="2026-01-05",
        profile="tool_only",
        experiment_tag="arena_v0",
        predictive_sharepacks_root=repo_root / "sharepacks" / "_predictive",
        validation_dir=validation_dir,
    )

    assert "Analysis Arena Day Synthesis" in report
    assert "corpus_summary.csv" not in report
    assert "Validation Artifact Lock" in report


def test_predictive_portfolio_main_writes_arena_first_report(monkeypatch, tmp_path: Path) -> None:
    repo_root = tmp_path
    _seed_final_docs(repo_root)
    _patch_predictive_portfolio_paths(monkeypatch, repo_root)
    _seed_predictive_state(repo_root, date="2026-01-05", state="NewYork4")
    _seed_predictive_state(repo_root, date="2026-01-05", state="Florida4")
    _write_text(
        repo_root / "sharepacks" / "_predictive" / "2026-01-05" / "control_center" / "profit_alerts.csv",
        "State,StateKey,Variant,AlertId,Strength,Suggested,CapLines,DecayDraws,Badges,Canonical,ImpliedSet,Evidence\nNew York,NewYork4,Combined,A05,4,BOX,12,3,CONS,066,[\"066\"],{}\nFlorida,Florida4,Combined,A04,3,BOX,12,3,CONS,344,[\"344\"],{}\n",
    )
    out_path = repo_root / "runs2" / "predictive" / "portfolio.md"
    monkeypatch.setattr(
        predictive_portfolio,
        "parse_args",
        lambda: argparse.Namespace(
            date="2026-01-05",
            sharepacks_root=str(repo_root / "sharepacks" / "_predictive"),
            profile="tool_only",
            experiment_tag="arena_v0",
            rank_by="arena_first",
            out=str(out_path),
            force=True,
            top_n_alerts=3,
            top_n_due_doubles=6,
            play_strategy_b12="analysis_prefix",
            play_strategy_b24="vtrac_pack_boxed_first_laneonly_presetB",
            play_strategy_b36="analysis_prefix",
            prefer_experiment_tags=None,
        ),
    )

    predictive_portfolio.main()

    report = out_path.read_text(encoding="utf-8")
    assert "Analysis Arena Predictive Portfolio" in report
    assert "Arena-First Board Snapshot" in report
    assert "control arm" in report.lower()
