#!/usr/bin/env python3
"""Run the analysis-arena predictive cadence.

This is the arena-era operator wrapper. It preserves the older Candidate
Universe / Play Card path as a downstream control arm, while making the new
Brain 1 -> Brain 2 -> shadow DPL review flow first-class in the daily run.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
ARENA_RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.build_board_spillover_overlay import _default_out_name as _overlay_default_out_name
from scripts.tools.build_shadow_decision_policy import _default_out_name as _dpl_default_out_name
from scripts.tools.create_board_review_bundle import _bundle_out_name
from scripts.tools.create_board_scoreboard import _default_out_name as _scoreboard_default_out_name
from scripts.tools.create_translation_sandbox_seed import (
    _default_manifest_out_name as _sandbox_manifest_out_name,
    _default_state_out_name,
)
from scripts.tools.run_v0_3_cycle import (
    _add_common_sharepack_args,
    _cmd_create_candidate_universe,
    _cmd_create_play_card,
    _cmd_create_predictive_portfolio,
    _cmd_grade_candidate_universe,
    _cmd_grade_play_card,
    _cmd_grade_play_card_windowed,
    _cmd_rollup_candidate_universe,
    _cmd_rollup_play_card,
    _cmd_run_predictive_day,
    _compute_results_date,
    _git_sha,
    _history_date_from_file,
    _iter_dates,
    _normalize_sharepacks_root,
    _now_iso,
    _parse_date_ymd,
    _results_file_path,
    _run,
    _safe_rel,
    _windowed_auto_end_date,
    _write_receipt,
)


def _arena_runs_dir_from_arg(value: str) -> Path:
    raw = str(value or "").strip()
    if not raw:
        return ARENA_RUNS_DIR
    sub = Path(raw)
    if sub.is_absolute() or any(part == ".." for part in sub.parts):
        raise SystemExit(f"Invalid --runs-subdir: {value!r} (must be a relative subdir under RUNS_2/)")
    return ARENA_RUNS_DIR / sub

def _arena_pre_receipt_path(*, runs_dir: Path, results_date: str, profile: str, experiment_tag: str) -> Path:
    suffix = f"__{experiment_tag}" if experiment_tag else ""
    return runs_dir / f"ANALYSIS_ARENA__CYCLE__PRE__{results_date}__{profile}{suffix}.md"


def _cmd_day_board_review(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    board_name: str,
    runs_dir: Path,
    history_date: Optional[str],
    states: Sequence[str],
    arena_top_items: int,
    board_top_items: int,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/create_day_arena_board_review.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
        "--board-name",
        board_name,
        "--arena-top-items",
        str(int(arena_top_items)),
        "--board-top-items",
        str(int(board_top_items)),
        "--out-dir",
        str(runs_dir),
    ]
    if history_date:
        cmd += ["--history-date", history_date]
    if states:
        cmd += ["--states", *states]
    return cmd


def _cmd_translation_sandbox(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    board_name: str,
    runs_dir: Path,
    states: Sequence[str],
) -> List[str]:
    overlay_json = runs_dir / _overlay_default_out_name(results_date, board_name)
    scoreboard_json = runs_dir / _scoreboard_default_out_name(
        {
            "results_date": results_date,
            "generated_from_overlay": board_name,
        }
    ).replace(".md", ".json")
    decision_json = runs_dir / _dpl_default_out_name(results_date, board_name).replace(".md", ".json")
    cmd: List[str] = [
        "python3",
        "scripts/tools/create_translation_sandbox_seed.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
        "--board-name",
        board_name,
        "--runs-dir",
        str(runs_dir),
        "--overlay-json",
        str(overlay_json),
        "--scoreboard-json",
        str(scoreboard_json),
        "--decision-policy-json",
        str(decision_json),
    ]
    if states:
        cmd += ["--states", *states]
    return cmd


def _predicted_board_outputs(*, runs_dir: Path, results_date: str, board_name: str) -> dict[str, str]:
    overlay_json = runs_dir / _overlay_default_out_name(results_date, board_name)
    scoreboard_md = runs_dir / _scoreboard_default_out_name(
        {
            "results_date": results_date,
            "generated_from_overlay": board_name,
        }
    )
    decision_md = runs_dir / _dpl_default_out_name(results_date, board_name)
    bundle_md = runs_dir / _bundle_out_name(results_date, board_name)
    sandbox_manifest = runs_dir / _sandbox_manifest_out_name(results_date, board_name)
    return {
        "overlay_json": _safe_rel(overlay_json),
        "scoreboard_md": _safe_rel(scoreboard_md),
        "shadow_dpl_md": _safe_rel(decision_md),
        "board_review_bundle_md": _safe_rel(bundle_md),
        "translation_sandbox_manifest_md": _safe_rel(sandbox_manifest),
    }


def _window_label(start_date: str, end_date: str) -> str:
    return start_date if start_date == end_date else f"{start_date}_to_{end_date}"


def _window_root_from_arg(value: str) -> Path:
    raw = str(value or "").strip()
    if not raw:
        raise SystemExit("--window-root is required")
    path = Path(raw)
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _iter_state_keys_for_date(*, sharepacks_root: str, results_date: str, states: Sequence[str]) -> list[str]:
    if states:
        return list(states)
    day_dir = Path(sharepacks_root) / results_date
    if not day_dir.exists():
        return []
    return sorted(p.name for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center")


def _cmd_control_center_daily(
    *,
    results_date: str,
    predictive_sharepacks_root: str,
    truth_sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    out_path: Path,
) -> list[str]:
    return [
        "python3",
        "scripts/tools/create_control_center_daily_run_report.py",
        "--date",
        results_date,
        "--predictive-sharepacks-root",
        predictive_sharepacks_root,
        "--truth-sharepacks-root",
        truth_sharepacks_root,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
        "--out",
        str(out_path),
        "--force",
    ]


def _cmd_state_master_validation(
    *,
    results_date: str,
    state: str,
    predictive_sharepacks_root: str,
    truth_sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    out_path: Path,
) -> list[str]:
    return [
        "python3",
        "scripts/tools/create_master_validation_run_report.py",
        "--date",
        results_date,
        "--state",
        state,
        "--predictive-sharepacks-root",
        predictive_sharepacks_root,
        "--truth-sharepacks-root",
        truth_sharepacks_root,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
        "--out",
        str(out_path),
        "--force",
    ]


def _cmd_day_synthesis(
    *,
    results_date: str,
    predictive_sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    validation_dir: Path,
    out_path: Path,
) -> list[str]:
    return [
        "python3",
        "scripts/tools/create_day_synthesis_run_report.py",
        "--date",
        results_date,
        "--predictive-sharepacks-root",
        predictive_sharepacks_root,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
        "--validation-dir",
        str(validation_dir),
        "--out",
        str(out_path),
        "--force",
    ]


def _cmd_brain2_master_validation(
    *,
    results_date: str,
    analysis_arena_dir: Path,
    board_name: str,
    validation_out: Path,
    tracker_ledger_out: Path,
    control_arm_runs_dir: Path,
    doubles_inventory_md: Path | None,
    doubles_inventory_csv: Path | None,
) -> list[str]:
    cmd: list[str] = [
        "python3",
        "scripts/tools/create_brain2_master_validation_run_report.py",
        "--date",
        results_date,
        "--analysis-arena-dir",
        str(analysis_arena_dir),
        "--board-name",
        board_name,
        "--control-arm-runs-dir",
        str(control_arm_runs_dir),
        "--out",
        str(validation_out),
        "--out-json",
        str(tracker_ledger_out),
        "--force",
    ]
    if doubles_inventory_md:
        cmd += ["--doubles-inventory-md", str(doubles_inventory_md)]
    if doubles_inventory_csv:
        cmd += ["--doubles-inventory-csv", str(doubles_inventory_csv)]
    return cmd


def _cmd_doubles_inventory(
    *,
    start_date: str,
    end_date: str,
    validation_dir: Path,
    control_arm_runs_dir: Path,
    predictive_sharepacks_root: str,
    truth_sharepacks_root: str,
    out_csv: Path,
    out_md: Path,
    out_deep: Path,
    out_study: Path,
) -> list[str]:
    return [
        "python3",
        "scripts/tools/create_doubles_mirror_doubles_inventory.py",
        "--from-date",
        start_date,
        "--to-date",
        end_date,
        "--runs-dir",
        str(validation_dir),
        "--grades-runs-dir",
        str(control_arm_runs_dir),
        "--results-root",
        "data/results",
        "--predictive-sharepacks-root",
        predictive_sharepacks_root,
        "--truth-sharepacks-root",
        truth_sharepacks_root,
        "--run-report-dir",
        str(validation_dir),
        "--out-csv",
        str(out_csv),
        "--out-md",
        str(out_md),
        "--out-deep-dive",
        str(out_deep),
        "--out-study-queue",
        str(out_study),
    ]


def build_window_close_commands(
    *,
    window_root: Path,
    runs_root: Path,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    force: bool,
) -> List[List[str]]:
    commands: List[List[str]] = [
        [
            "python3",
            "scripts/tools/create_window_performance_gap_report.py",
            "--window-root",
            str(window_root),
        ],
        [
            "python3",
            "scripts/tools/create_window_deep_hit_analysis_report.py",
            "--window-root",
            str(window_root),
            "--runs-root",
            str(runs_root),
            "--sharepacks-root",
            sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
        ],
        [
            "python3",
            "scripts/tools/create_window_c1_c2_frontier_harness_report.py",
            "--window-root",
            str(window_root),
        ],
        [
            "python3",
            "scripts/tools/create_window_pure_arena_finalist_scorecard.py",
            "--window-root",
            str(window_root),
        ],
        [
            "python3",
            "scripts/tools/create_window_deep_analysis_report.py",
            "--window-root",
            str(window_root),
        ],
    ]
    if force:
        for cmd in commands:
            cmd.append("--force")
    return commands


def build_pre_commands(
    *,
    history_date: Optional[str],
    history_file: Optional[str],
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    states: Sequence[str],
    force: bool,
    top_n_stable: Optional[int],
    write_signals_bundle: bool,
    write_evidence: bool,
    play_card_write_md: bool,
    rank_by: Optional[str],
    prefer_experiment_tags: Optional[str],
    board_name: str,
    runs_dir: Path,
    arena_top_items: int,
    board_top_items: int,
    skip_predictive_day: bool,
    skip_board_review: bool,
    skip_candidate_universe: bool,
    skip_play_card: bool,
    skip_portfolio: bool,
    skip_translation_sandbox: bool,
) -> List[List[str]]:
    cmds: List[List[str]] = []
    if not skip_predictive_day:
        cmds.append(
            _cmd_run_predictive_day(
                history_date=history_date,
                history_file=history_file,
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                states=states,
                force=force,
            )
        )
    if not skip_board_review:
        cmds.append(
            _cmd_day_board_review(
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                profile=profile,
                experiment_tag=experiment_tag,
                board_name=board_name,
                runs_dir=runs_dir,
                history_date=history_date or (_history_date_from_file(history_file) if history_file else None),
                states=states,
                arena_top_items=arena_top_items,
                board_top_items=board_top_items,
            )
        )
    if not skip_candidate_universe:
        cmds.append(
            _cmd_create_candidate_universe(
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                profile=profile,
                experiment_tag=experiment_tag,
                top_n_stable=top_n_stable,
                states=states,
                force=force,
                write_signals_bundle=write_signals_bundle,
                write_evidence=write_evidence,
            )
        )
    if not skip_play_card:
        cmds.append(
            _cmd_create_play_card(
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                profile=profile,
                experiment_tag=experiment_tag,
                states=states,
                force=force,
                write_md=play_card_write_md,
            )
        )
    if not skip_portfolio:
        effective_rank = rank_by
        if not effective_rank and profile in {"tool_only", "profit_only"}:
            effective_rank = "tool_first"
        effective_prefer_tags = prefer_experiment_tags
        if effective_prefer_tags is None and experiment_tag:
            effective_prefer_tags = f"{experiment_tag},,vtracpack_v1"
        cmds.append(
            _cmd_create_predictive_portfolio(
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                profile=profile,
                force=force,
                rank_by=effective_rank,
                prefer_experiment_tags=effective_prefer_tags,
            )
        )
    if not skip_translation_sandbox:
        cmds.append(
            _cmd_translation_sandbox(
                results_date=results_date,
                sharepacks_root=sharepacks_root,
                profile=profile,
                experiment_tag=experiment_tag,
                board_name=board_name,
                runs_dir=runs_dir,
                states=states,
            )
        )
    return cmds


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run the analysis-arena predictive cadence.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pre = sub.add_parser("pre", help="Run the arena-era predictive cadence for one history day.")
    g = pre.add_mutually_exclusive_group(required=True)
    g.add_argument("--history-date", help="History date H (YYYY-MM-DD).")
    g.add_argument("--history-file", help="Explicit Pick3StatsC4 workbook filename under data/history/.")
    pre.add_argument("--results-date", default=None, help="Override results date D (default: H+1).")
    _add_common_sharepack_args(pre)
    pre.add_argument("--skip-predictive-day", action="store_true")
    pre.add_argument("--skip-board-review", action="store_true")
    pre.add_argument("--skip-candidate-universe", action="store_true")
    pre.add_argument("--skip-play-card", action="store_true")
    pre.add_argument("--skip-portfolio", action="store_true")
    pre.add_argument("--skip-translation-sandbox", action="store_true")
    pre.add_argument("--board-name", default="analysis_arena_day_review")
    pre.add_argument("--arena-top-items", type=int, default=12)
    pre.add_argument("--board-top-items", type=int, default=8)
    pre.add_argument("--stable10", action="store_true", help="Convenience: pass --top-n-stable 10 when not overridden.")
    pre.add_argument("--top-n-stable", type=int, default=None)
    pre.add_argument("--write-signals-bundle", action="store_true")
    pre.add_argument("--write-audit-evidence", action="store_true")
    pre.add_argument("--play-card-write-md", action="store_true")
    pre.add_argument("--rank-by", choices=["profit_alerts", "tool_first"], default=None)
    pre.add_argument("--prefer-experiment-tags", default=None)
    pre.add_argument("--no-receipt", action="store_true")

    pre_range = sub.add_parser("pre-range", help="Run the arena-era predictive cadence across a history-date range.")
    pre_range.add_argument("--start-history-date", required=True)
    pre_range.add_argument("--end-history-date", required=True)
    _add_common_sharepack_args(pre_range)
    pre_range.add_argument("--skip-missing-history", action="store_true")
    pre_range.add_argument("--skip-predictive-day", action="store_true")
    pre_range.add_argument("--skip-board-review", action="store_true")
    pre_range.add_argument("--skip-candidate-universe", action="store_true")
    pre_range.add_argument("--skip-play-card", action="store_true")
    pre_range.add_argument("--skip-portfolio", action="store_true")
    pre_range.add_argument("--skip-translation-sandbox", action="store_true")
    pre_range.add_argument("--board-name", default="analysis_arena_day_review")
    pre_range.add_argument("--arena-top-items", type=int, default=12)
    pre_range.add_argument("--board-top-items", type=int, default=8)
    pre_range.add_argument("--stable10", action="store_true", help="Convenience: pass --top-n-stable 10 when not overridden.")
    pre_range.add_argument("--top-n-stable", type=int, default=None)
    pre_range.add_argument("--write-signals-bundle", action="store_true")
    pre_range.add_argument("--write-audit-evidence", action="store_true")
    pre_range.add_argument("--play-card-write-md", action="store_true")
    pre_range.add_argument("--rank-by", choices=["profit_alerts", "tool_first"], default=None)
    pre_range.add_argument("--prefer-experiment-tags", default=None)
    pre_range.add_argument("--no-per-day-receipts", action="store_true")
    pre_range.add_argument("--no-receipt", action="store_true")

    post = sub.add_parser("post", help="Run the arena-era post-results cadence for one results day.")
    post.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD).")
    _add_common_sharepack_args(post)
    post.add_argument("--results-file", default=None, help="Override results file (default: data/results/<D>.txt).")
    post.add_argument("--truth-sharepacks-root", default="sharepacks", help="Truth/frozen sharepacks root (default: sharepacks).")
    post.add_argument("--analysis-runs-subdir", default="ANALYSIS_ARENA", help="Subdir under RUNS_2 holding pre-built arena runtime receipts.")
    post.add_argument("--control-arm-runs-dir", default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"))
    post.add_argument("--board-name", default="analysis_arena_day_review")
    post.add_argument("--skip-candidate-universe-grade", action="store_true")
    post.add_argument("--skip-play-card-grade", action="store_true")
    post.add_argument("--skip-master-validation", action="store_true")
    post.add_argument("--skip-control-center", action="store_true")
    post.add_argument("--skip-doubles-inventory", action="store_true")
    post.add_argument("--skip-brain2-master-validation", action="store_true")
    post.add_argument("--skip-day-synthesis", action="store_true")
    post.add_argument("--rollup", action="store_true")
    post.add_argument("--windowed-auto", action="store_true")
    post.add_argument("--windowed-start-date", default=None)
    post.add_argument("--windowed-end-date", default=None)
    post.add_argument("--windowed-draws", type=int, default=5)
    post.add_argument("--skip-windowed", action="store_true")
    post.add_argument("--no-receipt", action="store_true")

    post_range = sub.add_parser("post-range", help="Run the arena-era post-results cadence across a results-date range.")
    post_range.add_argument("--start-date", required=True, help="Start results date D0 (YYYY-MM-DD).")
    post_range.add_argument("--end-date", required=True, help="End results date D1 (YYYY-MM-DD).")
    _add_common_sharepack_args(post_range)
    post_range.add_argument("--truth-sharepacks-root", default="sharepacks", help="Truth/frozen sharepacks root (default: sharepacks).")
    post_range.add_argument("--analysis-runs-subdir", default="ANALYSIS_ARENA", help="Subdir under RUNS_2 holding pre-built arena runtime receipts.")
    post_range.add_argument("--control-arm-runs-dir", default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"))
    post_range.add_argument("--board-name", default="analysis_arena_day_review")
    post_range.add_argument("--skip-missing-results", action="store_true")
    post_range.add_argument("--skip-candidate-universe-grade", action="store_true")
    post_range.add_argument("--skip-play-card-grade", action="store_true")
    post_range.add_argument("--skip-master-validation", action="store_true")
    post_range.add_argument("--skip-control-center", action="store_true")
    post_range.add_argument("--skip-doubles-inventory", action="store_true")
    post_range.add_argument("--skip-brain2-master-validation", action="store_true")
    post_range.add_argument("--skip-day-synthesis", action="store_true")
    post_range.add_argument("--rollup", action="store_true")
    post_range.add_argument("--windowed-auto", action="store_true")
    post_range.add_argument("--windowed-start-date", default=None)
    post_range.add_argument("--windowed-end-date", default=None)
    post_range.add_argument("--windowed-draws", type=int, default=5)
    post_range.add_argument("--skip-windowed", action="store_true")
    post_range.add_argument("--no-per-day-receipts", action="store_true")
    post_range.add_argument("--no-receipt", action="store_true")

    window_close = sub.add_parser("window-close", help="Generate the full arena-era window-close report set for an existing RUNS_2 window.")
    window_close.add_argument("--window-root", required=True, help="RUNS_2 window root, e.g. docs/.../RUNS_2/WINDOW_<...>")
    window_close.add_argument("--runs-root", default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"))
    window_close.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    window_close.add_argument("--profile", default="tool_only")
    window_close.add_argument("--experiment-tag", default="arena_v0")
    window_close.add_argument("--skip-performance-gap", action="store_true")
    window_close.add_argument("--skip-deep-hit-analysis", action="store_true")
    window_close.add_argument("--skip-frontier-harness", action="store_true")
    window_close.add_argument("--skip-pure-arena-scorecard", action="store_true")
    window_close.add_argument("--skip-deep-analysis", action="store_true")
    window_close.add_argument("--no-receipt", action="store_true")
    window_close.add_argument("--force", action="store_true")
    window_close.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    default_runs_subdir = "ANALYSIS_ARENA" if args.cmd in {"pre", "pre-range"} else "VALIDATION"
    runs_subdir = str(getattr(args, "runs_subdir", "") or default_runs_subdir).strip()
    runs_dir = _arena_runs_dir_from_arg(runs_subdir)

    if args.cmd == "pre":
        history_date = (args.history_date or "").strip() or None
        history_file = (args.history_file or "").strip() or None
        inferred_history_date = history_date or (_history_date_from_file(history_file) if history_file else None)
        if not inferred_history_date:
            raise SystemExit("Could not infer history date (provide --history-date or --history-file).")

        results_date = (args.results_date or "").strip() or _compute_results_date(inferred_history_date)
        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "arena_v0").strip() or "arena_v0"
        top_n_stable = args.top_n_stable
        if bool(args.stable10) and top_n_stable is None:
            top_n_stable = 10
        states = list(args.states or [])
        write_signals_bundle = bool(args.write_signals_bundle) or bool(args.write_audit_evidence)
        write_evidence = bool(args.write_audit_evidence)
        outputs = _predicted_board_outputs(
            runs_dir=runs_dir,
            results_date=results_date,
            board_name=str(args.board_name or "analysis_arena_day_review"),
        )

        cmds = build_pre_commands(
            history_date=history_date,
            history_file=history_file,
            results_date=results_date,
            sharepacks_root=sharepacks_root,
            profile=profile,
            experiment_tag=experiment_tag,
            states=states,
            force=bool(args.force),
            top_n_stable=top_n_stable,
            write_signals_bundle=write_signals_bundle,
            write_evidence=write_evidence,
            play_card_write_md=bool(args.play_card_write_md),
            rank_by=args.rank_by,
            prefer_experiment_tags=args.prefer_experiment_tags,
            board_name=str(args.board_name or "analysis_arena_day_review"),
            runs_dir=runs_dir,
            arena_top_items=int(args.arena_top_items),
            board_top_items=int(args.board_top_items),
            skip_predictive_day=bool(args.skip_predictive_day),
            skip_board_review=bool(args.skip_board_review),
            skip_candidate_universe=bool(args.skip_candidate_universe),
            skip_play_card=bool(args.skip_play_card),
            skip_portfolio=bool(args.skip_portfolio),
            skip_translation_sandbox=bool(args.skip_translation_sandbox),
        )

        receipt_lines: List[str] = [
            f"# Analysis Arena cycle — PRE — D={results_date}",
            "",
            "## Metadata",
            f"- generated_at: `{_now_iso()}`",
            f"- git_sha: `{_git_sha()}`",
            f"- history_date(H): `{inferred_history_date}`",
            f"- history_file: `{history_file or '-'} `",
            f"- results_date(D): `{results_date}`",
            f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`",
            f"- profile: `{profile}`",
            f"- experiment_tag: `{experiment_tag}`",
            f"- board_name: `{str(args.board_name or 'analysis_arena_day_review')}`",
            f"- top_n_stable: `{top_n_stable if top_n_stable is not None else '-'} `",
            f"- runs_subdir: `{runs_subdir}`",
            f"- states: `{', '.join(states) if states else 'ALL'}`",
            f"- force: `{bool(args.force)}`",
            f"- dry_run: `{bool(args.dry_run)}`",
            "",
            "## Operating Picture",
            "- Primary runtime branch: `Brain 1 -> Brain 2 -> shadow DPL`",
            "- Downstream control arm retained: `Candidate Universe -> Play Card -> Portfolio`",
            "- B12/B24/B36 remain comparative/baseline outputs, not the definition of arena truth.",
            "",
            "## Expected Arena-Era Outputs",
            f"- board overlay: `{outputs['overlay_json']}`",
            f"- board scoreboard: `{outputs['scoreboard_md']}`",
            f"- shadow DPL: `{outputs['shadow_dpl_md']}`",
            f"- board review bundle: `{outputs['board_review_bundle_md']}`",
            f"- translation sandbox manifest: `{outputs['translation_sandbox_manifest_md']}`",
            f"- state-local translation sandbox seeds: `sharepacks/_predictive/<D>/<STATE>/analysis/{_default_state_out_name(profile, experiment_tag)}`",
            "",
            "## Commands",
            "",
        ]
        for cmd in cmds:
            receipt_lines.append(f"- `{(' '.join(str(c) for c in cmd))}`")
        receipt_lines.append("")

        for cmd in cmds:
            _run(cmd, dry_run=bool(args.dry_run))

        if not args.no_receipt:
            receipt_path = _arena_pre_receipt_path(
                runs_dir=runs_dir,
                results_date=results_date,
                profile=profile,
                experiment_tag=experiment_tag,
            )
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")
        return

    if args.cmd == "pre-range":
        start_h = _parse_date_ymd(args.start_history_date)
        end_h = _parse_date_ymd(args.end_history_date)
        if end_h < start_h:
            raise SystemExit("--end-history-date must be >= --start-history-date")

        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "arena_v0").strip() or "arena_v0"
        top_n_stable = args.top_n_stable
        if bool(args.stable10) and top_n_stable is None:
            top_n_stable = 10
        states = list(args.states or [])

        base_cmd = [
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "pre",
            "--sharepacks-root",
            sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--board-name",
            str(args.board_name or "analysis_arena_day_review"),
            "--arena-top-items",
            str(int(args.arena_top_items)),
            "--board-top-items",
            str(int(args.board_top_items)),
            "--runs-subdir",
            runs_subdir,
        ]
        if top_n_stable is not None:
            base_cmd += ["--top-n-stable", str(int(top_n_stable))]
        if bool(args.force):
            base_cmd += ["--force"]
        if bool(args.dry_run):
            base_cmd += ["--dry-run"]
        if bool(args.skip_predictive_day):
            base_cmd += ["--skip-predictive-day"]
        if bool(args.skip_board_review):
            base_cmd += ["--skip-board-review"]
        if bool(args.skip_candidate_universe):
            base_cmd += ["--skip-candidate-universe"]
        if bool(args.skip_play_card):
            base_cmd += ["--skip-play-card"]
        if bool(args.skip_portfolio):
            base_cmd += ["--skip-portfolio"]
        if bool(args.skip_translation_sandbox):
            base_cmd += ["--skip-translation-sandbox"]
        if bool(args.write_audit_evidence):
            base_cmd += ["--write-audit-evidence"]
        elif bool(args.write_signals_bundle):
            base_cmd += ["--write-signals-bundle"]
        if bool(args.play_card_write_md):
            base_cmd += ["--play-card-write-md"]
        if args.rank_by:
            base_cmd += ["--rank-by", str(args.rank_by)]
        if args.prefer_experiment_tags:
            base_cmd += ["--prefer-experiment-tags", str(args.prefer_experiment_tags)]
        if states:
            base_cmd += ["--states", *states]
        if bool(args.no_per_day_receipts):
            base_cmd += ["--no-receipt"]

        receipt_lines: List[str] = [
            f"# Analysis Arena cycle — PRE RANGE — H={start_h.isoformat()}..{end_h.isoformat()}",
            "",
            "## Metadata",
            f"- generated_at: `{_now_iso()}`",
            f"- git_sha: `{_git_sha()}`",
            f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`",
            f"- profile: `{profile}`",
            f"- experiment_tag: `{experiment_tag}`",
            f"- runs_subdir: `{runs_subdir}`",
            f"- states: `{', '.join(states) if states else 'ALL'}`",
            f"- force: `{bool(args.force)}`",
            f"- dry_run: `{bool(args.dry_run)}`",
            f"- skip_missing_history: `{bool(args.skip_missing_history)}`",
            "",
            "## Commands",
            "",
        ]
        for h in _iter_dates(start_h, end_h):
            receipt_lines.append(f"- `{(' '.join(base_cmd + ['--history-date', h]))}`")
        receipt_lines.append("")

        for h in _iter_dates(start_h, end_h):
            if bool(args.skip_missing_history):
                candidates = [
                    REPO_ROOT / "data" / "history" / f"Pick3StatsC4_{h}.xlsm",
                    REPO_ROOT / "data" / "history" / f"Pick3StatsC4_{h.replace('-', '_')}.xlsm",
                ]
                if not any(p.exists() for p in candidates):
                    print(f"[SKIP] Missing history workbook for H={h}")
                    continue
            _run(base_cmd + ["--history-date", h], dry_run=bool(args.dry_run))

        if not bool(args.no_receipt):
            suffix = f"__{experiment_tag}" if experiment_tag else ""
            receipt_path = runs_dir / f"ANALYSIS_ARENA__CYCLE__PRE_RANGE__{start_h.isoformat()}_to_{end_h.isoformat()}__{profile}{suffix}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")
        return

    if args.cmd == "post":
        results_date = str(args.date or "").strip()
        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        truth_sharepacks_root = str(args.truth_sharepacks_root or "sharepacks").strip() or "sharepacks"
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "arena_v0").strip() or "arena_v0"
        analysis_runs_dir = _arena_runs_dir_from_arg(str(args.analysis_runs_subdir or "ANALYSIS_ARENA").strip())
        control_arm_runs_dir = Path(str(args.control_arm_runs_dir))
        states = _iter_state_keys_for_date(sharepacks_root=sharepacks_root, results_date=results_date, states=list(args.states or []))
        results_file = str(args.results_file).strip() if args.results_file else None
        window_label = _window_label(results_date, results_date)
        doubles_prefix = runs_dir / f"{window_label}__DOUBLES_MIRROR_DOUBLES"
        doubles_md = doubles_prefix.with_name(f"{window_label}__DOUBLES_MIRROR_DOUBLES__INVENTORY.md")
        doubles_csv = doubles_prefix.with_name(f"{window_label}__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv")
        doubles_deep = doubles_prefix.with_name(f"{window_label}__DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md")
        doubles_study = doubles_prefix.with_name(f"{window_label}__DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md")

        receipt_lines: List[str] = [
            f"# Analysis Arena cycle — POST — D={results_date}",
            "",
            "## Metadata",
            f"- generated_at: `{_now_iso()}`",
            f"- git_sha: `{_git_sha()}`",
            f"- results_date(D): `{results_date}`",
            f"- predictive_sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`",
            f"- truth_sharepacks_root: `{_safe_rel(Path(truth_sharepacks_root))}`",
            f"- profile: `{profile}`",
            f"- experiment_tag: `{experiment_tag}`",
            f"- validation_runs_subdir: `{runs_subdir}`",
            f"- analysis_runs_subdir: `{str(args.analysis_runs_subdir or 'ANALYSIS_ARENA')}`",
            f"- states: `{', '.join(states) if states else 'ALL'}`",
            f"- force: `{bool(args.force)}`",
            f"- dry_run: `{bool(args.dry_run)}`",
            "",
            "## Operating Picture",
            "- Control arm grading still runs through the legacy baseline shell.",
            "- Arena-native post-results artifacts are written into RUNS_2/VALIDATION.",
            "- Brain 2 validation reads the pre-built arena runtime receipts from RUNS_2/ANALYSIS_ARENA.",
            "",
            "## Commands",
            "",
        ]

        cmds: List[List[str]] = []
        if not args.skip_candidate_universe_grade or not args.skip_play_card_grade or bool(args.rollup) or bool(args.windowed_auto) or (args.windowed_start_date and args.windowed_end_date):
            v03_cmd: List[str] = [
                "python3",
                "scripts/tools/run_v0_3_cycle.py",
                "post",
                "--date",
                results_date,
                "--sharepacks-root",
                sharepacks_root,
                "--profile",
                profile,
                "--experiment-tag",
                experiment_tag,
                "--skip-windowed",
                "--no-receipt",
            ]
            if results_file:
                v03_cmd += ["--results-file", results_file]
            if states:
                v03_cmd += ["--states", *states]
            if bool(args.force):
                v03_cmd += ["--force"]
            if bool(args.dry_run):
                v03_cmd += ["--dry-run"]
            if bool(args.skip_candidate_universe_grade):
                v03_cmd += ["--skip-candidate-universe-grade"]
            if bool(args.skip_play_card_grade):
                v03_cmd += ["--skip-play-card-grade"]
            if bool(args.rollup):
                v03_cmd += ["--rollup"]
            cmds.append(v03_cmd)
            if not bool(args.skip_windowed):
                if args.windowed_start_date and args.windowed_end_date:
                    cmds.append(
                        _cmd_grade_play_card_windowed(
                            start_date=str(args.windowed_start_date),
                            end_date=str(args.windowed_end_date),
                            window_draws=int(args.windowed_draws),
                            sharepacks_root=sharepacks_root,
                            profile=profile,
                            experiment_tag=experiment_tag,
                            states=states,
                            force=bool(args.force),
                        )
                    )
                elif bool(args.windowed_auto):
                    end_cov, _note = _windowed_auto_end_date(
                        start_date=results_date,
                        requested_end=results_date,
                        window_draws=int(args.windowed_draws),
                    )
                    if end_cov:
                        cmds.append(
                            _cmd_grade_play_card_windowed(
                                start_date=results_date,
                                end_date=end_cov,
                                window_draws=int(args.windowed_draws),
                                sharepacks_root=sharepacks_root,
                                profile=profile,
                                experiment_tag=experiment_tag,
                                states=states,
                                force=bool(args.force),
                            )
                        )

        if not bool(args.skip_master_validation):
            for state in states:
                cmds.append(
                    _cmd_state_master_validation(
                        results_date=results_date,
                        state=state,
                        predictive_sharepacks_root=sharepacks_root,
                        truth_sharepacks_root=truth_sharepacks_root,
                        profile=profile,
                        experiment_tag=experiment_tag,
                        out_path=runs_dir / f"{results_date}__{state}.md",
                    )
                )
        if not bool(args.skip_control_center):
            cmds.append(
                _cmd_control_center_daily(
                    results_date=results_date,
                    predictive_sharepacks_root=sharepacks_root,
                    truth_sharepacks_root=truth_sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    out_path=runs_dir / f"{results_date}__CONTROL_CENTER.md",
                )
            )
        if not bool(args.skip_doubles_inventory):
            cmds.append(
                _cmd_doubles_inventory(
                    start_date=results_date,
                    end_date=results_date,
                    validation_dir=runs_dir,
                    control_arm_runs_dir=control_arm_runs_dir,
                    predictive_sharepacks_root=sharepacks_root,
                    truth_sharepacks_root=truth_sharepacks_root,
                    out_csv=doubles_csv,
                    out_md=doubles_md,
                    out_deep=doubles_deep,
                    out_study=doubles_study,
                )
            )
        if not bool(args.skip_brain2_master_validation):
            cmds.append(
                _cmd_brain2_master_validation(
                    results_date=results_date,
                    analysis_arena_dir=analysis_runs_dir,
                    board_name=str(args.board_name or "analysis_arena_day_review"),
                    validation_out=runs_dir / f"{results_date}__BRAIN2_MASTER_VALIDATION.md",
                    tracker_ledger_out=runs_dir / f"{results_date}__BRAIN2_TRACKER_LEDGER.json",
                    control_arm_runs_dir=control_arm_runs_dir,
                    doubles_inventory_md=None if bool(args.skip_doubles_inventory) else doubles_md,
                    doubles_inventory_csv=None if bool(args.skip_doubles_inventory) else doubles_csv,
                )
            )
        if not bool(args.skip_day_synthesis):
            cmds.append(
                _cmd_day_synthesis(
                    results_date=results_date,
                    predictive_sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    validation_dir=runs_dir,
                    out_path=runs_dir / f"{results_date}__DAY_SYNTHESIS.md",
                )
            )

        for cmd in cmds:
            receipt_lines.append(f"- `{(' '.join(str(c) for c in cmd))}`")
        receipt_lines.append("")

        for cmd in cmds:
            _run(cmd, dry_run=bool(args.dry_run))

        if not args.no_receipt:
            receipt_path = runs_dir / f"ANALYSIS_ARENA__CYCLE__POST__{results_date}__{profile}__{experiment_tag}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")
        return

    if args.cmd == "post-range":
        start_d = _parse_date_ymd(args.start_date)
        end_d = _parse_date_ymd(args.end_date)
        if end_d < start_d:
            raise SystemExit("--end-date must be >= --start-date")

        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        truth_sharepacks_root = str(args.truth_sharepacks_root or "sharepacks").strip() or "sharepacks"
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "arena_v0").strip() or "arena_v0"
        analysis_runs_dir = _arena_runs_dir_from_arg(str(args.analysis_runs_subdir or "ANALYSIS_ARENA").strip())
        control_arm_runs_dir = Path(str(args.control_arm_runs_dir))
        states = list(args.states or [])
        window_label = _window_label(start_d.isoformat(), end_d.isoformat())
        doubles_csv = runs_dir / f"{window_label}__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"
        doubles_md = runs_dir / f"{window_label}__DOUBLES_MIRROR_DOUBLES__INVENTORY.md"
        doubles_deep = runs_dir / f"{window_label}__DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md"
        doubles_study = runs_dir / f"{window_label}__DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md"

        receipt_lines: List[str] = [
            f"# Analysis Arena cycle — POST RANGE — D={start_d.isoformat()}..{end_d.isoformat()}",
            "",
            "## Metadata",
            f"- generated_at: `{_now_iso()}`",
            f"- git_sha: `{_git_sha()}`",
            f"- predictive_sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`",
            f"- truth_sharepacks_root: `{_safe_rel(Path(truth_sharepacks_root))}`",
            f"- profile: `{profile}`",
            f"- experiment_tag: `{experiment_tag}`",
            f"- validation_runs_subdir: `{runs_subdir}`",
            f"- analysis_runs_subdir: `{str(args.analysis_runs_subdir or 'ANALYSIS_ARENA')}`",
            f"- states: `{', '.join(states) if states else 'ALL'}`",
            f"- force: `{bool(args.force)}`",
            f"- dry_run: `{bool(args.dry_run)}`",
            "",
            "## Commands",
            "",
        ]

        v03_range_cmd: List[str] = [
            "python3",
            "scripts/tools/run_v0_3_cycle.py",
            "post-range",
            "--start-date",
            start_d.isoformat(),
            "--end-date",
            end_d.isoformat(),
            "--sharepacks-root",
            sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--no-receipt",
        ]
        if states:
            v03_range_cmd += ["--states", *states]
        if bool(args.force):
            v03_range_cmd += ["--force"]
        if bool(args.dry_run):
            v03_range_cmd += ["--dry-run"]
        if bool(args.skip_missing_results):
            v03_range_cmd += ["--skip-missing-results"]
        if bool(args.skip_candidate_universe_grade):
            v03_range_cmd += ["--skip-candidate-universe-grade"]
        if bool(args.skip_play_card_grade):
            v03_range_cmd += ["--skip-play-card-grade"]
        if bool(args.rollup):
            v03_range_cmd += ["--rollup"]
        if bool(args.skip_windowed):
            v03_range_cmd += ["--skip-windowed"]
        elif args.windowed_start_date and args.windowed_end_date:
            v03_range_cmd += ["--windowed-start-date", str(args.windowed_start_date), "--windowed-end-date", str(args.windowed_end_date), "--windowed-draws", str(int(args.windowed_draws))]
        elif bool(args.windowed_auto):
            v03_range_cmd += ["--windowed-auto", "--windowed-draws", str(int(args.windowed_draws))]

        receipt_lines.append(f"- `{(' '.join(str(c) for c in v03_range_cmd))}`")
        receipt_lines.append("")
        _run(v03_range_cmd, dry_run=bool(args.dry_run))

        for results_date in _iter_dates(start_d, end_d):
            if bool(args.skip_missing_results) and not _results_file_path(results_date).exists():
                print(f"[SKIP] Missing results for D={results_date}: {_safe_rel(_results_file_path(results_date))}")
                continue
            state_keys = _iter_state_keys_for_date(sharepacks_root=sharepacks_root, results_date=results_date, states=states)
            day_cmds: List[List[str]] = []
            if not bool(args.skip_master_validation):
                for state in state_keys:
                    day_cmds.append(
                        _cmd_state_master_validation(
                            results_date=results_date,
                            state=state,
                            predictive_sharepacks_root=sharepacks_root,
                            truth_sharepacks_root=truth_sharepacks_root,
                            profile=profile,
                            experiment_tag=experiment_tag,
                            out_path=runs_dir / f"{results_date}__{state}.md",
                        )
                    )
            if not bool(args.skip_control_center):
                day_cmds.append(
                    _cmd_control_center_daily(
                        results_date=results_date,
                        predictive_sharepacks_root=sharepacks_root,
                        truth_sharepacks_root=truth_sharepacks_root,
                        profile=profile,
                        experiment_tag=experiment_tag,
                        out_path=runs_dir / f"{results_date}__CONTROL_CENTER.md",
                    )
                )
            for cmd in day_cmds:
                receipt_lines.append(f"- `{(' '.join(str(c) for c in cmd))}`")
                _run(cmd, dry_run=bool(args.dry_run))

        if not bool(args.skip_doubles_inventory):
            inv_cmd = _cmd_doubles_inventory(
                start_date=start_d.isoformat(),
                end_date=end_d.isoformat(),
                validation_dir=runs_dir,
                control_arm_runs_dir=control_arm_runs_dir,
                predictive_sharepacks_root=sharepacks_root,
                truth_sharepacks_root=truth_sharepacks_root,
                out_csv=doubles_csv,
                out_md=doubles_md,
                out_deep=doubles_deep,
                out_study=doubles_study,
            )
            receipt_lines.append(f"- `{(' '.join(str(c) for c in inv_cmd))}`")
            _run(inv_cmd, dry_run=bool(args.dry_run))

        for results_date in _iter_dates(start_d, end_d):
            if bool(args.skip_missing_results) and not _results_file_path(results_date).exists():
                continue
            tail_cmds: List[List[str]] = []
            if not bool(args.skip_brain2_master_validation):
                tail_cmds.append(
                    _cmd_brain2_master_validation(
                        results_date=results_date,
                        analysis_arena_dir=analysis_runs_dir,
                        board_name=str(args.board_name or "analysis_arena_day_review"),
                        validation_out=runs_dir / f"{results_date}__BRAIN2_MASTER_VALIDATION.md",
                        tracker_ledger_out=runs_dir / f"{results_date}__BRAIN2_TRACKER_LEDGER.json",
                        control_arm_runs_dir=control_arm_runs_dir,
                        doubles_inventory_md=None if bool(args.skip_doubles_inventory) else doubles_md,
                        doubles_inventory_csv=None if bool(args.skip_doubles_inventory) else doubles_csv,
                    )
                )
            if not bool(args.skip_day_synthesis):
                tail_cmds.append(
                    _cmd_day_synthesis(
                        results_date=results_date,
                        predictive_sharepacks_root=sharepacks_root,
                        profile=profile,
                        experiment_tag=experiment_tag,
                        validation_dir=runs_dir,
                        out_path=runs_dir / f"{results_date}__DAY_SYNTHESIS.md",
                    )
                )
            for cmd in tail_cmds:
                receipt_lines.append(f"- `{(' '.join(str(c) for c in cmd))}`")
                _run(cmd, dry_run=bool(args.dry_run))

        if not bool(args.no_receipt):
            receipt_path = runs_dir / f"ANALYSIS_ARENA__CYCLE__POST_RANGE__{start_d.isoformat()}_to_{end_d.isoformat()}__{profile}__{experiment_tag}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")
        return

    if args.cmd == "window-close":
        window_root = _window_root_from_arg(str(args.window_root))
        runs_root = Path(str(args.runs_root)).resolve()
        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "arena_v0").strip() or "arena_v0"

        all_cmds = build_window_close_commands(
            window_root=window_root,
            runs_root=runs_root,
            sharepacks_root=sharepacks_root,
            profile=profile,
            experiment_tag=experiment_tag,
            force=bool(args.force),
        )
        cmds: List[List[str]] = []
        if not bool(args.skip_performance_gap):
            cmds.append(all_cmds[0])
        if not bool(args.skip_deep_hit_analysis):
            cmds.append(all_cmds[1])
        if not bool(args.skip_frontier_harness):
            cmds.append(all_cmds[2])
        if not bool(args.skip_pure_arena_scorecard):
            cmds.append(all_cmds[3])
        if not bool(args.skip_deep_analysis):
            cmds.append(all_cmds[4])

        receipt_lines: List[str] = [
            f"# Analysis Arena cycle — WINDOW CLOSE — {window_root.name}",
            "",
            "## Metadata",
            f"- generated_at: `{_now_iso()}`",
            f"- git_sha: `{_git_sha()}`",
            f"- window_root: `{_safe_rel(window_root)}`",
            f"- runs_root: `{_safe_rel(runs_root)}`",
            f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`",
            f"- profile: `{profile}`",
            f"- experiment_tag: `{experiment_tag}`",
            f"- force: `{bool(args.force)}`",
            f"- dry_run: `{bool(args.dry_run)}`",
            "",
            "## Window-Close Artifacts",
            "- Performance / opportunity gap report",
            "- Deep hit analysis + hit roster",
            "- C1/C2 frontier harness analysis + case roster",
            "- Pure arena finalist / candidate scorecard",
            "- Window deep analysis / Codex report",
            "",
            "## Commands",
            "",
        ]
        for cmd in cmds:
            receipt_lines.append(f"- `{(' '.join(str(c) for c in cmd))}`")
        receipt_lines.append("")

        for cmd in cmds:
            _run(cmd, dry_run=bool(args.dry_run))

        if not bool(args.no_receipt):
            receipt_path = window_root / f"ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__{profile}__{experiment_tag}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")
        return

    raise SystemExit(f"Unsupported command: {args.cmd}")


if __name__ == "__main__":
    main()
