from __future__ import annotations

from pathlib import Path

from scripts.tools.run_analysis_arena_cycle import (
    ARENA_RUNS_DIR,
    _arena_runs_dir_from_arg,
    _cmd_doubles_inventory,
    _iter_state_keys_for_date,
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


def test_build_window_close_commands_includes_all_five_reports(tmp_path: Path) -> None:
    cmds = build_window_close_commands(
        window_root=tmp_path / "WINDOW_2026-01-05_to_2026-01-09",
        runs_root=tmp_path / "RUNS",
        sharepacks_root="sharepacks/_predictive",
        profile="tool_only",
        experiment_tag="arena_v0",
        force=True,
    )

    assert len(cmds) == 5
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

    assert cmds[4][1].endswith("create_window_deep_analysis_report.py")
    assert "--window-root" in cmds[4]
    assert "--force" in cmds[4]
