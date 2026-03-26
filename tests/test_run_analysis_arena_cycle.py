from __future__ import annotations

from pathlib import Path

from scripts.tools.run_analysis_arena_cycle import ARENA_RUNS_DIR, _arena_runs_dir_from_arg, build_pre_commands


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
