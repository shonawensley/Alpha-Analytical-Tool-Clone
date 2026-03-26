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
    _cmd_run_predictive_day,
    _compute_results_date,
    _git_sha,
    _history_date_from_file,
    _iter_dates,
    _normalize_sharepacks_root,
    _now_iso,
    _parse_date_ymd,
    _run,
    _safe_rel,
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
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    runs_subdir = str(getattr(args, "runs_subdir", "") or "ANALYSIS_ARENA").strip()
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

    raise SystemExit(f"Unsupported command: {args.cmd}")


if __name__ == "__main__":
    main()
