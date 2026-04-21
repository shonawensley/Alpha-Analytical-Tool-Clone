from __future__ import annotations

from pathlib import Path

from scripts.tools.run_analysis_arena_cycle import (
    ARENA_RUNS_DIR,
    _arena_runs_dir_from_arg,
    _cmd_brain2_master_validation,
    _cmd_doubles_inventory,
    _iter_state_keys_for_date,
    build_cross_window_rollup_command,
    build_fresh_window_readiness_command,
    build_stage4b_replay_readback_command,
    build_stage4c_shadow_translator_command,
    build_stage5_readback_command,
    build_stage5_shadow_evaluator_command,
    build_stage6a_shadow_spec_command,
    build_stage6b_readback_command,
    build_stage6b_shadow_replay_command,
    build_stage6c_confirmation_protocol_command,
    build_stage6d_restraint_calibration_command,
    build_stage6e_support_narrowing_command,
    build_stage6f_integrated_decision_atlas_command,
    build_stage7a_fresh_confirmation_scaffold_command,
    build_stage7b_fixture_replay_harness_command,
    build_stage4_fixture_replay_command,
    build_frontier_negative_control_command,
    build_window_decay_close_command,
    build_tuneup_diagnostics_command,
    build_window_close_commands,
    build_pre_commands,
)


def test_arena_runs_dir_defaults_to_runs2() -> None:
    assert _arena_runs_dir_from_arg("") == ARENA_RUNS_DIR
    assert _arena_runs_dir_from_arg("ANALYSIS_ARENA") == ARENA_RUNS_DIR / "ANALYSIS_ARENA"


def test_build_pre_commands_includes_board_review_and_translation_sandbox(tmp_path: Path) -> None:
    cmds = build_pre_commands(
        history_date="2026-01-19",
        history_file=None,
        results_date="2026-01-20",
        sharepacks_root=str(tmp_path / "sharepacks" / "_predictive"),
        profile="tool_only",
        experiment_tag="arena_v0",
        states=["NewYork4", "NewJersey4"],
        force=True,
        top_n_stable=10,
        write_signals_bundle=True,
        write_evidence=True,
        play_card_write_md=True,
        rank_by=None,
        prefer_experiment_tags=None,
        board_name="analysis_arena_day_review",
        runs_dir=tmp_path / "runs",
        arena_top_items=12,
        board_top_items=8,
        skip_predictive_day=False,
        skip_board_review=False,
        skip_candidate_universe=False,
        skip_play_card=False,
        skip_portfolio=False,
        skip_translation_sandbox=False,
    )

    assert len(cmds) == 6
    assert cmds[0][1].endswith("run_predictive_day.py")
    assert cmds[1][1].endswith("create_day_arena_board_review.py")
    assert "--board-name" in cmds[1]
    assert cmds[2][1].endswith("create_candidate_universe.py")
    assert "--top-n-stable" in cmds[2]
    assert cmds[3][1].endswith("create_play_card.py")
    assert "--write-md" in cmds[3]
    assert cmds[4][1].endswith("create_predictive_portfolio_report.py")
    assert "--prefer-experiment-tags" in cmds[4]
    assert "arena_v0,,vtracpack_v1" in cmds[4]
    assert cmds[5][1].endswith("create_translation_sandbox_seed.py")
    assert "--overlay-json" in cmds[5]
    assert "--decision-policy-json" in cmds[5]


def test_build_pre_commands_can_skip_new_layers(tmp_path: Path) -> None:
    cmds = build_pre_commands(
        history_date="2026-01-19",
        history_file=None,
        results_date="2026-01-20",
        sharepacks_root=str(tmp_path / "sharepacks" / "_predictive"),
        profile="tool_only",
        experiment_tag="arena_v0",
        states=[],
        force=False,
        top_n_stable=None,
        write_signals_bundle=False,
        write_evidence=False,
        play_card_write_md=False,
        rank_by="tool_first",
        prefer_experiment_tags="arena_v0",
        board_name="analysis_arena_day_review",
        runs_dir=tmp_path / "runs",
        arena_top_items=12,
        board_top_items=8,
        skip_predictive_day=True,
        skip_board_review=True,
        skip_candidate_universe=False,
        skip_play_card=True,
        skip_portfolio=True,
        skip_translation_sandbox=True,
    )

    assert len(cmds) == 1
    assert cmds[0][1].endswith("create_candidate_universe.py")


def test_iter_state_keys_for_date_uses_sharepack_dirs(tmp_path: Path) -> None:
    day_dir = tmp_path / "sharepacks" / "_predictive" / "2026-01-05"
    (day_dir / "NewYork4").mkdir(parents=True)
    (day_dir / "Florida4").mkdir(parents=True)
    (day_dir / "control_center").mkdir(parents=True)

    states = _iter_state_keys_for_date(
        sharepacks_root=str(tmp_path / "sharepacks" / "_predictive"),
        results_date="2026-01-05",
        states=[],
    )

    assert states == ["Florida4", "NewYork4"]


def test_cmd_doubles_inventory_targets_results_and_validation_dirs(tmp_path: Path) -> None:
    cmd = _cmd_doubles_inventory(
        start_date="2026-01-05",
        end_date="2026-01-09",
        validation_dir=tmp_path / "validation",
        control_arm_runs_dir=tmp_path / "runs",
        predictive_sharepacks_root="sharepacks/_predictive",
        truth_sharepacks_root="sharepacks",
        out_csv=tmp_path / "validation" / "inventory.csv",
        out_md=tmp_path / "validation" / "inventory.md",
        out_deep=tmp_path / "validation" / "deep.md",
        out_study=tmp_path / "validation" / "study.md",
    )

    assert cmd[1].endswith("create_doubles_mirror_doubles_inventory.py")
    assert "--results-root" in cmd
    assert "data/results" in cmd
    assert "--run-report-dir" in cmd
    assert str(tmp_path / "validation") in cmd


def test_cmd_brain2_master_validation_writes_tracker_ledger(tmp_path: Path) -> None:
    cmd = _cmd_brain2_master_validation(
        results_date="2026-01-05",
        analysis_arena_dir=tmp_path / "analysis",
        board_name="analysis_arena_day_review",
        validation_out=tmp_path / "validation" / "2026-01-05__BRAIN2_MASTER_VALIDATION.md",
        tracker_ledger_out=tmp_path / "validation" / "2026-01-05__BRAIN2_TRACKER_LEDGER.json",
        control_arm_runs_dir=tmp_path / "runs",
        doubles_inventory_md=None,
        doubles_inventory_csv=None,
    )

    assert cmd[1].endswith("create_brain2_master_validation_run_report.py")
    assert "--out" in cmd
    assert "--out-json" in cmd
    assert str(tmp_path / "validation" / "2026-01-05__BRAIN2_TRACKER_LEDGER.json") in cmd


def test_build_window_close_commands_includes_all_six_reports(tmp_path: Path) -> None:
    cmds = build_window_close_commands(
        window_root=tmp_path / "WINDOW_2026-01-05_to_2026-01-09",
        runs_root=tmp_path / "RUNS",
        sharepacks_root="sharepacks/_predictive",
        profile="tool_only",
        experiment_tag="arena_v0",
        force=True,
    )

    assert len(cmds) == 6
    assert cmds[0][1].endswith("create_window_performance_gap_report.py")
    assert "--window-root" in cmds[0]
    assert "--force" in cmds[0]

    assert cmds[1][1].endswith("create_window_deep_hit_analysis_report.py")
    assert "--runs-root" in cmds[1]
    assert str(tmp_path / "RUNS") in cmds[1]
    assert "--sharepacks-root" in cmds[1]
    assert "sharepacks/_predictive" in cmds[1]
    assert "--profile" in cmds[1]
    assert "tool_only" in cmds[1]
    assert "--experiment-tag" in cmds[1]
    assert "arena_v0" in cmds[1]
    assert "--force" in cmds[1]

    assert cmds[2][1].endswith("create_window_c1_c2_frontier_harness_report.py")
    assert "--window-root" in cmds[2]
    assert "--force" in cmds[2]

    assert cmds[3][1].endswith("create_window_pure_arena_finalist_scorecard.py")
    assert "--window-root" in cmds[3]
    assert "--force" in cmds[3]

    assert cmds[4][1].endswith("create_window_translator_learning_ledger.py")
    assert "--window-root" in cmds[4]
    assert "--force" in cmds[4]

    assert cmds[5][1].endswith("create_window_deep_analysis_report.py")
    assert "--window-root" in cmds[5]
    assert "--force" in cmds[5]


def test_build_cross_window_rollup_command_uses_explicit_windows(tmp_path: Path) -> None:
    cmd = build_cross_window_rollup_command(
        runs2_root=tmp_path / "RUNS_2",
        window_roots=[
            tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09",
            tmp_path / "RUNS_2" / "WINDOW_2026-01-15_to_2026-01-22",
        ],
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_cross_window_rollup.py")
    assert "--runs2-root" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert cmd.count("--window-root") == 2
    assert "--force" in cmd


def test_build_tuneup_diagnostics_command_uses_explicit_windows(tmp_path: Path) -> None:
    cmd = build_tuneup_diagnostics_command(
        runs2_root=tmp_path / "RUNS_2",
        window_roots=[
            tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09",
            tmp_path / "RUNS_2" / "WINDOW_2026-01-15_to_2026-01-22",
        ],
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_tuneup_diagnostics.py")
    assert "--runs2-root" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert cmd.count("--window-root") == 2
    assert "--force" in cmd


def test_build_frontier_negative_control_command_uses_explicit_windows(tmp_path: Path) -> None:
    cmd = build_frontier_negative_control_command(
        runs2_root=tmp_path / "RUNS_2",
        window_roots=[
            tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09",
            tmp_path / "RUNS_2" / "WINDOW_2026-01-15_to_2026-01-22",
        ],
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_frontier_negative_control_study.py")
    assert "--runs2-root" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert cmd.count("--window-root") == 2
    assert "--force" in cmd


def test_build_fresh_window_readiness_command_uses_explicit_windows(tmp_path: Path) -> None:
    cmd = build_fresh_window_readiness_command(
        runs2_root=tmp_path / "RUNS_2",
        window_roots=[
            tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09",
            tmp_path / "RUNS_2" / "WINDOW_2026-01-15_to_2026-01-22",
        ],
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_fresh_window_readiness_report.py")
    assert "--runs2-root" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert cmd.count("--window-root") == 2
    assert "--force" in cmd


def test_build_stage4_fixture_replay_command_uses_output_dir_and_limit(tmp_path: Path) -> None:
    cmd = build_stage4_fixture_replay_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage4",
        max_replay_rows=25,
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage4_fixture_replay_harness.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage4") in cmd
    assert "--max-replay-rows" in cmd
    assert "25" in cmd
    assert "--force" in cmd


def test_build_stage4b_replay_readback_command_uses_casebook_limit(tmp_path: Path) -> None:
    cmd = build_stage4b_replay_readback_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage4b",
        casebook_limit=48,
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage4b_replay_readback.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage4b") in cmd
    assert "--casebook-limit" in cmd
    assert "48" in cmd
    assert "--force" in cmd


def test_build_stage4c_shadow_translator_command_uses_casebook_limit(tmp_path: Path) -> None:
    cmd = build_stage4c_shadow_translator_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage4c",
        casebook_limit=72,
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage4c_shadow_translator_prototype.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage4c") in cmd
    assert "--casebook-limit" in cmd
    assert "72" in cmd
    assert "--force" in cmd


def test_build_stage5_shadow_evaluator_command_uses_casebook_limit_and_row_limit(tmp_path: Path) -> None:
    cmd = build_stage5_shadow_evaluator_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage5",
        casebook_limit=84,
        max_value_rows=250,
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage5_shadow_translator_fixture_evaluator.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage5") in cmd
    assert "--casebook-limit" in cmd
    assert "84" in cmd
    assert "--max-value-rows" in cmd
    assert "250" in cmd
    assert "--force" in cmd


def test_build_stage5_readback_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage5_readback_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage5_readback",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage5_readback_decision_memo.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage5_readback") in cmd
    assert "--force" in cmd


def test_build_stage6a_shadow_spec_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6a_shadow_spec_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6a",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6a_shadow_translator_specification.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6a") in cmd
    assert "--force" in cmd


def test_build_stage6b_shadow_replay_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6b_shadow_replay_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6b",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6b_shadow_replay_simulator.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6b") in cmd
    assert "--force" in cmd


def test_build_stage6b_readback_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6b_readback_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6b_readback",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6b_readback_decision_memo.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6b_readback") in cmd
    assert "--force" in cmd


def test_build_stage6c_confirmation_protocol_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6c_confirmation_protocol_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6c",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6c_confirmation_protocol.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6c") in cmd
    assert "--force" in cmd


def test_build_stage6d_restraint_calibration_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6d_restraint_calibration_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6d",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6d_restraint_calibration_workbench.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6d") in cmd
    assert "--force" in cmd


def test_build_stage6e_support_narrowing_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage6e_support_narrowing_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6e",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6e_support_modifier_narrowing_workbench.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6e") in cmd
    assert "--force" in cmd


def test_build_stage6f_integrated_decision_atlas_command_uses_output_dir_and_limits(tmp_path: Path) -> None:
    cmd = build_stage6f_integrated_decision_atlas_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage6f",
        casebook_limit_per_bucket=6,
        max_ledger_rows=250,
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage6f_integrated_decision_atlas.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage6f") in cmd
    assert "--casebook-limit-per-bucket" in cmd
    assert "6" in cmd
    assert "--max-ledger-rows" in cmd
    assert "250" in cmd
    assert "--force" in cmd


def test_build_stage7a_fresh_confirmation_scaffold_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage7a_fresh_confirmation_scaffold_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage7a",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage7a_fresh_confirmation_scaffold.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage7a") in cmd
    assert "--force" in cmd


def test_build_stage7b_fixture_replay_harness_command_uses_output_dir(tmp_path: Path) -> None:
    cmd = build_stage7b_fixture_replay_harness_command(
        runs2_root=tmp_path / "RUNS_2",
        output_dir=tmp_path / "RUNS_2" / "stage7b",
        force=True,
    )

    assert cmd[1].endswith("create_analysis_arena_stage7b_fixture_replay_harness.py")
    assert "--runs2-dir" in cmd
    assert str(tmp_path / "RUNS_2") in cmd
    assert "--output-dir" in cmd
    assert str(tmp_path / "RUNS_2" / "stage7b") in cmd
    assert "--force" in cmd


def test_build_window_decay_close_command_uses_explicit_horizon(tmp_path: Path) -> None:
    cmd = build_window_decay_close_command(
        window_root=tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09",
        results_root=tmp_path / "data" / "results",
        decay_upload_days_total=5,
        force=True,
    )

    assert cmd[1].endswith("create_window_decay_carryover_scorecard.py")
    assert "--window-root" in cmd
    assert str(tmp_path / "RUNS_2" / "WINDOW_2026-01-05_to_2026-01-09") in cmd
    assert "--results-root" in cmd
    assert str(tmp_path / "data" / "results") in cmd
    assert "--decay-upload-days-total" in cmd
    assert "5" in cmd
    assert "--force" in cmd
