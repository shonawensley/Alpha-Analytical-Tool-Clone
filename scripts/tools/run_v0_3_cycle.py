#!/usr/bin/env python3
"""
Run the v0.3 daily cadence for predictive + grading (no analyzer edits).

This is a workflow orchestrator that shells out to existing tools:
  - run_predictive_day.py (build sharepacks/_predictive/<D>/ from history workbook H)
  - create_candidate_universe.py (build per-state candidate_universe*.json)
  - create_play_card.py (build per-state play_card*.json)
  - create_predictive_portfolio_report.py (build cross-state triage markdown)
  - grade_candidate_universe.py / grade_play_card.py (write grading to RUNS)
  - rollup_candidate_universe_corpus.py / rollup_play_card_corpus.py (optional)
  - grade_play_card_windowed.py (optional, windowed grading)

It writes lightweight receipts into RUNS so runs are reproducible without relying on chat logs.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

def _runs_dir_from_arg(value: str) -> Path:
    raw = str(value or "").strip()
    if not raw:
        return RUNS_DIR
    sub = Path(raw)
    if sub.is_absolute() or any(part == ".." for part in sub.parts):
        raise SystemExit(f"Invalid --runs-subdir: {value!r} (must be a relative subdir under RUNS/)")
    return RUNS_DIR / sub


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")


def _compute_results_date(history_date: str) -> str:
    dt = datetime.strptime(history_date, "%Y-%m-%d")
    return (dt + timedelta(days=1)).strftime("%Y-%m-%d")


def _history_date_from_file(history_file: str) -> str:
    return (
        history_file.strip()
        .replace("Pick3StatsC4_", "")
        .replace(".xlsm", "")
        .replace("_", "-")
    )


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _git_sha() -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(REPO_ROOT))
            .decode("utf-8", errors="replace")
            .strip()
        )
    except Exception:
        return "UNKNOWN"


def _base_env() -> dict[str, str]:
    env = dict(os.environ)
    existing = env.get("PYTHONPATH", "")
    prefix = os.pathsep.join([".", "src"])
    if existing:
        env["PYTHONPATH"] = prefix + os.pathsep + existing
    else:
        env["PYTHONPATH"] = prefix
    return env


def _run(cmd: Sequence[str], *, dry_run: bool) -> None:
    printable = " ".join(str(c) for c in cmd)
    print(f"[CMD] {printable}")
    if dry_run:
        return
    subprocess.run(list(cmd), cwd=str(REPO_ROOT), env=_base_env(), check=True)


def _write_receipt(path: Path, lines: List[str], *, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _pre_receipt_path(*, runs_dir: Path, results_date: str, profile: str, experiment_tag: str) -> Path:
    suffix = f"__{experiment_tag}" if experiment_tag else ""
    return runs_dir / f"V0_3__CYCLE__PRE__{results_date}__{profile}{suffix}.md"


def _post_receipt_path(*, runs_dir: Path, results_date: str, profile: str, experiment_tag: str) -> Path:
    suffix = f"__{experiment_tag}" if experiment_tag else ""
    return runs_dir / f"V0_3__CYCLE__POST__{results_date}__{profile}{suffix}.md"


def _add_common_sharepack_args(p: argparse.ArgumentParser) -> None:
    p.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive).",
    )
    p.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile (default: tool_only).",
    )
    p.add_argument(
        "--experiment-tag",
        default="",
        help="Optional experiment tag applied to candidate_universe/play_card files (default: none).",
    )
    p.add_argument(
        "--runs-subdir",
        default="",
        help="Optional subdir under RUNS/ to write receipts (default: RUNS root).",
    )
    p.add_argument("--states", nargs="*", help="Optional subset of states to run.")
    p.add_argument("--force", action="store_true", help="Pass --force to downstream tools (overwrite outputs).")
    p.add_argument("--dry-run", action="store_true", help="Print commands only (no filesystem writes).")


def _cmd_run_predictive_day(
    *,
    history_date: Optional[str],
    history_file: Optional[str],
    results_date: str,
    sharepacks_root: str,
    states: Sequence[str],
) -> List[str]:
    cmd: List[str] = ["python3", "scripts/tools/run_predictive_day.py"]
    if history_date:
        cmd += ["--history-date", history_date]
    elif history_file:
        cmd += ["--history-file", history_file]
    else:
        raise SystemExit("Missing history input (expected --history-date or --history-file)")
    cmd += ["--results-date", results_date]
    cmd += ["--sharepacks-root", sharepacks_root]
    if states:
        cmd += ["--states", *states]
    return cmd


def _cmd_create_candidate_universe(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    top_n_stable: Optional[int],
    states: Sequence[str],
    force: bool,
    write_signals_bundle: bool,
    write_evidence: bool,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/create_candidate_universe.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
        # Candidate Universe policy: DR is demoted by default for v0.3 runs.
        "--top-n-dr",
        "0",
    ]
    if top_n_stable is not None:
        cmd += ["--top-n-stable", str(int(top_n_stable))]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    if states:
        cmd += ["--states", *states]
    if write_signals_bundle:
        cmd += ["--write-signals-bundle"]
    if write_evidence:
        cmd += ["--write-evidence"]
    if force:
        cmd += ["--force"]
    return cmd


def _cmd_create_play_card(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    states: Sequence[str],
    force: bool,
    write_md: bool,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/create_play_card.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
    ]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    if states:
        cmd += ["--states", *states]
    if write_md:
        cmd += ["--write-md"]
    if force:
        cmd += ["--force"]
    return cmd


def _cmd_create_predictive_portfolio(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    force: bool,
    rank_by: Optional[str],
    prefer_experiment_tags: Optional[str],
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/create_predictive_portfolio_report.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
    ]
    if rank_by:
        cmd += ["--rank-by", rank_by]
    if prefer_experiment_tags:
        cmd += ["--prefer-experiment-tags", prefer_experiment_tags]
    if force:
        cmd += ["--force"]
    return cmd


def _cmd_grade_candidate_universe(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    states: Sequence[str],
    results_file: Optional[str],
    force: bool,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/grade_candidate_universe.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
    ]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    if states:
        cmd += ["--states", *states]
    if results_file:
        cmd += ["--results-file", results_file]
    if force:
        cmd += ["--force"]
    return cmd


def _cmd_grade_play_card(
    *,
    results_date: str,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    states: Sequence[str],
    results_file: Optional[str],
    force: bool,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/grade_play_card.py",
        "--date",
        results_date,
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
    ]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    if states:
        cmd += ["--states", *states]
    if results_file:
        cmd += ["--results-file", results_file]
    if force:
        cmd += ["--force"]
    return cmd


def _cmd_rollup_candidate_universe(*, profile: str, experiment_tag: str) -> List[str]:
    cmd: List[str] = ["python3", "scripts/tools/rollup_candidate_universe_corpus.py", "--profile", profile]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    return cmd


def _cmd_rollup_play_card(*, profile: str, experiment_tag: str) -> List[str]:
    cmd: List[str] = ["python3", "scripts/tools/rollup_play_card_corpus.py", "--profile", profile]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    return cmd


def _cmd_grade_play_card_windowed(
    *,
    start_date: str,
    end_date: str,
    window_draws: int,
    sharepacks_root: str,
    profile: str,
    experiment_tag: str,
    states: Sequence[str],
    force: bool,
) -> List[str]:
    cmd: List[str] = [
        "python3",
        "scripts/tools/grade_play_card_windowed.py",
        "--start-date",
        start_date,
        "--end-date",
        end_date,
        "--window-draws",
        str(int(window_draws)),
        "--sharepacks-root",
        sharepacks_root,
        "--profile",
        profile,
    ]
    if experiment_tag:
        cmd += ["--experiment-tag", experiment_tag]
    if states:
        cmd += ["--states", *states]
    if force:
        cmd += ["--force"]
    return cmd


def _parse_date_ymd(s: str) -> date:
    try:
        return datetime.strptime(str(s).strip(), "%Y-%m-%d").date()
    except Exception as exc:
        raise SystemExit(f"Invalid date: {s!r} (expected YYYY-MM-DD)") from exc


def _iter_dates(start: date, end: date) -> List[str]:
    out: List[str] = []
    d = start
    while d <= end:
        out.append(d.isoformat())
        d = d + timedelta(days=1)
    return out


def _results_file_path(results_date: str) -> Path:
    return REPO_ROOT / "data" / "results" / f"{results_date}.txt"


def _windowed_offset_days(window_draws: int) -> int:
    n = int(window_draws)
    if n <= 0:
        raise SystemExit("--windowed-draws must be >= 1")
    days_needed = (n + 1) // 2  # ceil(n/2) Midday/Evening slots per day
    return max(0, int(days_needed) - 1)


def _windowed_auto_end_date(*, start_date: str, requested_end: str, window_draws: int) -> tuple[Optional[str], str]:
    """
    Returns (end_date_covered, note). If end_date_covered is None, skip windowed grading.

    We require contiguous results coverage from start_date through (end_date + offset_days) to
    avoid misleading partial windows.
    """
    start = _parse_date_ymd(start_date)
    end_req = _parse_date_ymd(requested_end)
    if end_req < start:
        return None, "requested_end < start_date"

    offset_days = _windowed_offset_days(window_draws)
    needed_end = end_req + timedelta(days=offset_days)

    # Determine contiguous results coverage starting at start_date.
    d = start
    last_ok: Optional[date] = None
    while d <= needed_end:
        if not _results_file_path(d.isoformat()).exists():
            break
        last_ok = d
        d = d + timedelta(days=1)

    if last_ok is None:
        return None, f"missing results file: {_safe_rel(_results_file_path(start.isoformat()))}"

    max_end = last_ok - timedelta(days=offset_days)
    if max_end < start:
        return None, f"insufficient contiguous results coverage for N={window_draws} (need through {needed_end.isoformat()})"

    end_cov = min(end_req, max_end)
    if end_cov < end_req:
        return end_cov.isoformat(), f"clamped end_date to {end_cov.isoformat()} (need contiguous results through {(end_cov + timedelta(days=offset_days)).isoformat()})"
    return end_cov.isoformat(), f"coverage OK through {needed_end.isoformat()}"


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run the v0.3 cadence (pre + post).")
    sub = p.add_subparsers(dest="cmd", required=True)

    pre = sub.add_parser("pre", help="Build predictive day artifacts (no results needed).")
    g = pre.add_mutually_exclusive_group(required=True)
    g.add_argument("--history-date", help="History date H (YYYY-MM-DD) to infer Pick3StatsC4_*.xlsm")
    g.add_argument("--history-file", help="Explicit history workbook filename under data/history/")
    pre.add_argument("--results-date", default=None, help="Override results date D (default: H+1)")
    _add_common_sharepack_args(pre)
    pre.add_argument("--skip-predictive-day", action="store_true", help="Skip running run_predictive_day.py.")
    pre.add_argument("--skip-candidate-universe", action="store_true", help="Skip creating candidate_universe*.json.")
    pre.add_argument("--skip-play-card", action="store_true", help="Skip creating play_card*.json.")
    pre.add_argument("--skip-portfolio", action="store_true", help="Skip creating predictive portfolio markdown.")
    pre.add_argument(
        "--stable10",
        action="store_true",
        help="Convenience: set --experiment-tag stable10 and pass --top-n-stable 10 to Candidate Universe (default: off).",
    )
    pre.add_argument(
        "--top-n-stable",
        type=int,
        default=None,
        help="Override --top-n-stable passed to create_candidate_universe.py (default: tool default; recommended: 10 for stable10).",
    )
    pre.add_argument(
        "--write-signals-bundle",
        action="store_true",
        help="Also write signals_bundle*.json during Candidate Universe creation (default: off).",
    )
    pre.add_argument(
        "--write-audit-evidence",
        action="store_true",
        help="Convenience: also write candidate_universe_evidence.* and signals_bundle*.json (default: off).",
    )
    pre.add_argument("--play-card-write-md", action="store_true", help="Also write play_card*.md (default: off).")
    pre.add_argument(
        "--rank-by",
        choices=["profit_alerts", "tool_first"],
        default=None,
        help="Portfolio ranking mode (default: tool_first for tool_only; profit_alerts for mixed).",
    )
    pre.add_argument(
        "--prefer-experiment-tags",
        default=None,
        help=(
            "Optional comma-separated play_card experiment tags to prefer when building the portfolio "
            "(default: <unset> uses the tool's internal defaults)."
        ),
    )
    pre.add_argument("--no-receipt", action="store_true", help="Do not write a RUNS receipt (default: write).")

    pre_range = sub.add_parser("pre-range", help="Run PRE across a history date range (H0..H1).")
    pre_range.add_argument("--start-history-date", required=True, help="Start history date H0 (YYYY-MM-DD)")
    pre_range.add_argument("--end-history-date", required=True, help="End history date H1 (YYYY-MM-DD)")
    _add_common_sharepack_args(pre_range)
    pre_range.add_argument("--skip-missing-history", action="store_true", help="Skip days with missing workbooks (default: fail).")
    pre_range.add_argument("--skip-predictive-day", action="store_true", help="Skip running run_predictive_day.py.")
    pre_range.add_argument("--skip-candidate-universe", action="store_true", help="Skip creating candidate_universe*.json.")
    pre_range.add_argument("--skip-play-card", action="store_true", help="Skip creating play_card*.json.")
    pre_range.add_argument("--skip-portfolio", action="store_true", help="Skip creating predictive portfolio markdown.")
    pre_range.add_argument(
        "--stable10",
        action="store_true",
        help="Convenience: set --experiment-tag stable10 and pass --top-n-stable 10 to Candidate Universe (default: off).",
    )
    pre_range.add_argument(
        "--top-n-stable",
        type=int,
        default=None,
        help="Override --top-n-stable passed to create_candidate_universe.py (default: tool default; recommended: 10 for stable10).",
    )
    pre_range.add_argument(
        "--write-signals-bundle",
        action="store_true",
        help="Also write signals_bundle*.json during Candidate Universe creation (default: off).",
    )
    pre_range.add_argument(
        "--write-audit-evidence",
        action="store_true",
        help="Convenience: also write candidate_universe_evidence.* and signals_bundle*.json (default: off).",
    )
    pre_range.add_argument("--play-card-write-md", action="store_true", help="Also write play_card*.md (default: off).")
    pre_range.add_argument(
        "--rank-by",
        choices=["profit_alerts", "tool_first"],
        default=None,
        help="Portfolio ranking mode (default: tool_first for tool_only; profit_alerts for mixed).",
    )
    pre_range.add_argument(
        "--prefer-experiment-tags",
        default=None,
        help=(
            "Optional comma-separated play_card experiment tags to prefer when building the portfolio "
            "(default: <unset> uses the tool's internal defaults)."
        ),
    )
    pre_range.add_argument("--no-per-day-receipts", action="store_true", help="Do not write per-day PRE receipts (default: write).")
    pre_range.add_argument("--no-receipt", action="store_true", help="Do not write a range RUNS receipt (default: write).")

    post = sub.add_parser("post", help="Grade artifacts after results exist for date D.")
    post.add_argument("--date", required=True, help="Results date D to grade (YYYY-MM-DD)")
    _add_common_sharepack_args(post)
    post.add_argument(
        "--stable10",
        action="store_true",
        help="Convenience: set --experiment-tag stable10 (default: off).",
    )
    post.add_argument(
        "--results-file",
        default=None,
        help="Override results file (default: data/results/<D>.txt).",
    )
    post.add_argument("--skip-candidate-universe-grade", action="store_true", help="Skip Candidate Universe grading.")
    post.add_argument("--skip-play-card-grade", action="store_true", help="Skip Play Card grading.")
    post.add_argument("--rollup", action="store_true", help="Also run corpus rollups (default: off).")
    post.add_argument("--windowed-start-date", default=None, help="Optional windowed grading start date (YYYY-MM-DD).")
    post.add_argument("--windowed-end-date", default=None, help="Optional windowed grading end date (YYYY-MM-DD).")
    post.add_argument("--windowed-draws", type=int, default=5, help="Windowed grading draw slots N (default: 5).")
    post.add_argument(
        "--windowed-auto",
        action="store_true",
        help="Auto-run windowed grading for D if contiguous results coverage exists (avoids partial windows).",
    )
    post.add_argument("--skip-windowed", action="store_true", help="Skip windowed grading even if dates are provided.")
    post.add_argument("--no-receipt", action="store_true", help="Do not write a RUNS receipt (default: write).")

    post_range = sub.add_parser("post-range", help="Run POST across a results date range (D0..D1).")
    post_range.add_argument("--start-date", required=True, help="Start results date D0 (YYYY-MM-DD)")
    post_range.add_argument("--end-date", required=True, help="End results date D1 (YYYY-MM-DD)")
    _add_common_sharepack_args(post_range)
    post_range.add_argument(
        "--stable10",
        action="store_true",
        help="Convenience: set --experiment-tag stable10 (default: off).",
    )
    post_range.add_argument("--skip-missing-results", action="store_true", help="Skip days with missing data/results/<D>.txt (default: fail).")
    post_range.add_argument("--skip-candidate-universe-grade", action="store_true", help="Skip Candidate Universe grading.")
    post_range.add_argument("--skip-play-card-grade", action="store_true", help="Skip Play Card grading.")
    post_range.add_argument("--rollup", action="store_true", help="Also run corpus rollups (default: off).")
    post_range.add_argument("--windowed-start-date", default=None, help="Optional windowed grading start date (YYYY-MM-DD).")
    post_range.add_argument("--windowed-end-date", default=None, help="Optional windowed grading end date (YYYY-MM-DD).")
    post_range.add_argument("--windowed-draws", type=int, default=5, help="Windowed grading draw slots N (default: 5).")
    post_range.add_argument(
        "--windowed-auto",
        action="store_true",
        help="Auto-run windowed grading for D0..D1 if contiguous results coverage exists (avoids partial windows).",
    )
    post_range.add_argument("--skip-windowed", action="store_true", help="Skip windowed grading even if dates are provided.")
    post_range.add_argument("--no-per-day-receipts", action="store_true", help="Do not write per-day POST receipts (default: write).")
    post_range.add_argument("--no-receipt", action="store_true", help="Do not write a range RUNS receipt (default: write).")

    return p.parse_args()


def _normalize_sharepacks_root(value: str) -> str:
    root = Path(value)
    if not root.is_absolute():
        root = (REPO_ROOT / root).resolve()
    return str(root)


def main() -> None:
    args = _parse_args()
    runs_subdir = str(getattr(args, "runs_subdir", "") or "").strip()
    runs_dir = _runs_dir_from_arg(runs_subdir)

    if args.cmd == "pre":
        history_date = (args.history_date or "").strip() or None
        history_file = (args.history_file or "").strip() or None
        inferred_history_date = history_date or (_history_date_from_file(history_file) if history_file else None)
        if not inferred_history_date:
            raise SystemExit("Could not infer history date (provide --history-date or a Pick3StatsC4_*.xlsm --history-file)")

        results_date = (args.results_date or "").strip() or _compute_results_date(inferred_history_date)
        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "").strip()
        top_n_stable = args.top_n_stable
        if bool(args.stable10) and not experiment_tag:
            experiment_tag = "stable10"
        if experiment_tag == "stable10" and top_n_stable is None:
            top_n_stable = 10
        states = list(args.states or [])
        write_signals_bundle = bool(args.write_signals_bundle) or bool(args.write_audit_evidence)
        write_evidence = bool(args.write_audit_evidence)

        receipt_lines: List[str] = []
        receipt_lines.append(f"# v0.3 cycle — PRE — D={results_date}")
        receipt_lines.append("")
        receipt_lines.append("## Metadata")
        receipt_lines.append(f"- generated_at: `{_now_iso()}`")
        receipt_lines.append(f"- git_sha: `{_git_sha()}`")
        receipt_lines.append(f"- history_date(H): `{inferred_history_date}`")
        receipt_lines.append(f"- history_file: `{history_file or '-'} `")
        receipt_lines.append(f"- results_date(D): `{results_date}`")
        receipt_lines.append(f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`")
        receipt_lines.append(f"- profile: `{profile}`")
        receipt_lines.append(f"- experiment_tag: `{experiment_tag or '-'} `")
        receipt_lines.append(f"- top_n_stable: `{top_n_stable if top_n_stable is not None else '-'} `")
        receipt_lines.append(f"- runs_subdir: `{runs_subdir or '-'} `")
        receipt_lines.append(f"- states: `{', '.join(states) if states else 'ALL'}`")
        receipt_lines.append(f"- force: `{bool(args.force)}`")
        receipt_lines.append(f"- dry_run: `{bool(args.dry_run)}`")
        receipt_lines.append("")
        receipt_lines.append("## Commands")
        receipt_lines.append("")

        cmds: List[List[str]] = []
        if not args.skip_predictive_day:
            cmds.append(
                _cmd_run_predictive_day(
                    history_date=history_date,
                    history_file=history_file,
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    states=states,
                )
            )
        if not args.skip_candidate_universe:
            cmds.append(
                _cmd_create_candidate_universe(
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    top_n_stable=top_n_stable,
                    states=states,
                    force=bool(args.force),
                    write_signals_bundle=write_signals_bundle,
                    write_evidence=write_evidence,
                )
            )
        if not args.skip_play_card:
            cmds.append(
                _cmd_create_play_card(
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    states=states,
                    force=bool(args.force),
                    write_md=bool(args.play_card_write_md),
                )
            )
        if not args.skip_portfolio:
            rank_by = args.rank_by
            if not rank_by and profile in {"tool_only", "profit_only"}:
                rank_by = "tool_first"
            prefer_tags = args.prefer_experiment_tags
            if prefer_tags is None and experiment_tag:
                # Prefer the current run's experiment tag first, but keep the historical fallbacks.
                prefer_tags = f"{experiment_tag},,vtracpack_v1"
            cmds.append(
                _cmd_create_predictive_portfolio(
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    force=bool(args.force),
                    rank_by=rank_by,
                    prefer_experiment_tags=prefer_tags,
                )
            )

        for cmd in cmds:
            receipt_lines.append(f"- `{(' '.join(cmd))}`")
        receipt_lines.append("")

        for cmd in cmds:
            _run(cmd, dry_run=bool(args.dry_run))

        if not args.no_receipt:
            receipt_path = _pre_receipt_path(runs_dir=runs_dir, results_date=results_date, profile=profile, experiment_tag=experiment_tag)
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
        experiment_tag = str(args.experiment_tag or "").strip()
        top_n_stable = args.top_n_stable
        if bool(args.stable10) and not experiment_tag:
            experiment_tag = "stable10"
        if experiment_tag == "stable10" and top_n_stable is None:
            top_n_stable = 10
        states = list(args.states or [])

        receipt_lines: List[str] = []
        receipt_lines.append(f"# v0.3 cycle — PRE RANGE — H={start_h.isoformat()}..{end_h.isoformat()}")
        receipt_lines.append("")
        receipt_lines.append("## Metadata")
        receipt_lines.append(f"- generated_at: `{_now_iso()}`")
        receipt_lines.append(f"- git_sha: `{_git_sha()}`")
        receipt_lines.append(f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`")
        receipt_lines.append(f"- profile: `{profile}`")
        receipt_lines.append(f"- experiment_tag: `{experiment_tag or '-'} `")
        receipt_lines.append(f"- top_n_stable: `{top_n_stable if top_n_stable is not None else '-'} `")
        receipt_lines.append(f"- runs_subdir: `{runs_subdir or '-'} `")
        receipt_lines.append(f"- states: `{', '.join(states) if states else 'ALL'}`")
        receipt_lines.append(f"- force: `{bool(args.force)}`")
        receipt_lines.append(f"- dry_run: `{bool(args.dry_run)}`")
        receipt_lines.append(f"- skip_missing_history: `{bool(args.skip_missing_history)}`")
        receipt_lines.append(f"- no_per_day_receipts: `{bool(args.no_per_day_receipts)}`")
        receipt_lines.append("")
        receipt_lines.append("## Days")
        receipt_lines.append("")

        for h in _iter_dates(start_h, end_h):
            receipt_lines.append(f"- H={h} → D={_compute_results_date(h)}")
        receipt_lines.append("")
        receipt_lines.append("## Commands")
        receipt_lines.append("")

        base_cmd = [
            "python3",
            "scripts/tools/run_v0_3_cycle.py",
            "pre",
            "--sharepacks-root",
            sharepacks_root,
            "--profile",
            profile,
        ]
        if experiment_tag:
            base_cmd += ["--experiment-tag", experiment_tag]
        if top_n_stable is not None:
            base_cmd += ["--top-n-stable", str(int(top_n_stable))]
        if bool(args.stable10):
            base_cmd += ["--stable10"]
        if runs_subdir:
            base_cmd += ["--runs-subdir", runs_subdir]
        if states:
            base_cmd += ["--states", *states]
        if bool(args.force):
            base_cmd += ["--force"]
        if bool(args.dry_run):
            base_cmd += ["--dry-run"]
        if bool(args.skip_predictive_day):
            base_cmd += ["--skip-predictive-day"]
        if bool(args.skip_candidate_universe):
            base_cmd += ["--skip-candidate-universe"]
        if bool(args.skip_play_card):
            base_cmd += ["--skip-play-card"]
        if bool(args.skip_portfolio):
            base_cmd += ["--skip-portfolio"]
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
        if bool(args.no_per_day_receipts):
            base_cmd += ["--no-receipt"]

        for h in _iter_dates(start_h, end_h):
            cmd = base_cmd + ["--history-date", h]
            receipt_lines.append(f"- `{(' '.join(cmd))}`")
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
            cmd = base_cmd + ["--history-date", h]
            try:
                _run(cmd, dry_run=bool(args.dry_run))
            except subprocess.CalledProcessError:
                if bool(args.skip_missing_history):
                    print(f"[SKIP] PRE failed for H={h} (skip_missing_history=true)")
                    continue
                raise

        if not bool(args.no_receipt):
            suffix = f"__{experiment_tag}" if experiment_tag else ""
            receipt_path = runs_dir / f"V0_3__CYCLE__PRE_RANGE__{start_h.isoformat()}_to_{end_h.isoformat()}__{profile}{suffix}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")

        return

    if args.cmd == "post":
        results_date = args.date.strip()
        sharepacks_root = _normalize_sharepacks_root(args.sharepacks_root)
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "").strip()
        if bool(args.stable10) and not experiment_tag:
            experiment_tag = "stable10"
        states = list(args.states or [])
        results_file = str(args.results_file).strip() if args.results_file else None

        receipt_lines: List[str] = []
        receipt_lines.append(f"# v0.3 cycle — POST — D={results_date}")
        receipt_lines.append("")
        receipt_lines.append("## Metadata")
        receipt_lines.append(f"- generated_at: `{_now_iso()}`")
        receipt_lines.append(f"- git_sha: `{_git_sha()}`")
        receipt_lines.append(f"- results_date(D): `{results_date}`")
        receipt_lines.append(f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`")
        receipt_lines.append(f"- profile: `{profile}`")
        receipt_lines.append(f"- experiment_tag: `{experiment_tag or '-'} `")
        receipt_lines.append(f"- runs_subdir: `{runs_subdir or '-'} `")
        receipt_lines.append(f"- states: `{', '.join(states) if states else 'ALL'}`")
        receipt_lines.append(f"- results_file: `{results_file or 'data/results/<D>.txt'}`")
        receipt_lines.append(f"- force: `{bool(args.force)}`")
        receipt_lines.append(f"- dry_run: `{bool(args.dry_run)}`")
        receipt_lines.append(f"- windowed_auto: `{bool(args.windowed_auto)}`")
        receipt_lines.append("")
        receipt_lines.append("## Commands")
        receipt_lines.append("")

        cmds: List[List[str]] = []
        if not args.skip_candidate_universe_grade:
            cmds.append(
                _cmd_grade_candidate_universe(
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    states=states,
                    results_file=results_file,
                    force=bool(args.force),
                )
            )
        if not args.skip_play_card_grade:
            cmds.append(
                _cmd_grade_play_card(
                    results_date=results_date,
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    states=states,
                    results_file=results_file,
                    force=bool(args.force),
                )
            )
        if bool(args.rollup):
            cmds.append(
                _cmd_rollup_candidate_universe(profile=profile, experiment_tag=experiment_tag)
            )
            cmds.append(_cmd_rollup_play_card(profile=profile, experiment_tag=experiment_tag))

        windowed_start = (args.windowed_start_date or "").strip()
        windowed_end = (args.windowed_end_date or "").strip()
        if bool(args.windowed_auto) and (windowed_start or windowed_end):
            raise SystemExit("Use either --windowed-auto or --windowed-start-date/--windowed-end-date (not both).")
        if not args.skip_windowed:
            if windowed_start and windowed_end:
                cmds.append(
                    _cmd_grade_play_card_windowed(
                        start_date=windowed_start,
                        end_date=windowed_end,
                        window_draws=int(args.windowed_draws),
                        sharepacks_root=sharepacks_root,
                        profile=profile,
                        experiment_tag=experiment_tag,
                        states=states,
                        force=bool(args.force),
                    )
                )
            elif bool(args.windowed_auto):
                end_cov, note = _windowed_auto_end_date(
                    start_date=results_date,
                    requested_end=results_date,
                    window_draws=int(args.windowed_draws),
                )
                receipt_lines.append(f"- windowed_auto_note: `{note}`")
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

        for cmd in cmds:
            receipt_lines.append(f"- `{(' '.join(cmd))}`")
        receipt_lines.append("")

        for cmd in cmds:
            _run(cmd, dry_run=bool(args.dry_run))

        if not args.no_receipt:
            receipt_path = _post_receipt_path(runs_dir=runs_dir, results_date=results_date, profile=profile, experiment_tag=experiment_tag)
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
        profile = str(args.profile or "tool_only").strip()
        experiment_tag = str(args.experiment_tag or "").strip()
        if bool(args.stable10) and not experiment_tag:
            experiment_tag = "stable10"
        states = list(args.states or [])

        receipt_lines: List[str] = []
        receipt_lines.append(f"# v0.3 cycle — POST RANGE — D={start_d.isoformat()}..{end_d.isoformat()}")
        receipt_lines.append("")
        receipt_lines.append("## Metadata")
        receipt_lines.append(f"- generated_at: `{_now_iso()}`")
        receipt_lines.append(f"- git_sha: `{_git_sha()}`")
        receipt_lines.append(f"- sharepacks_root: `{_safe_rel(Path(sharepacks_root))}`")
        receipt_lines.append(f"- profile: `{profile}`")
        receipt_lines.append(f"- experiment_tag: `{experiment_tag or '-'} `")
        receipt_lines.append(f"- runs_subdir: `{runs_subdir or '-'} `")
        receipt_lines.append(f"- states: `{', '.join(states) if states else 'ALL'}`")
        receipt_lines.append(f"- force: `{bool(args.force)}`")
        receipt_lines.append(f"- dry_run: `{bool(args.dry_run)}`")
        receipt_lines.append(f"- rollup: `{bool(args.rollup)}`")
        receipt_lines.append(f"- windowed_auto: `{bool(args.windowed_auto)}`")
        receipt_lines.append(f"- skip_missing_results: `{bool(args.skip_missing_results)}`")
        receipt_lines.append(f"- no_per_day_receipts: `{bool(args.no_per_day_receipts)}`")
        receipt_lines.append("")
        receipt_lines.append("## Days")
        receipt_lines.append("")
        for d in _iter_dates(start_d, end_d):
            receipt_lines.append(f"- D={d}")
        receipt_lines.append("")
        receipt_lines.append("## Commands")
        receipt_lines.append("")

        base_cmd = [
            "python3",
            "scripts/tools/run_v0_3_cycle.py",
            "post",
            "--sharepacks-root",
            sharepacks_root,
            "--profile",
            profile,
        ]
        if experiment_tag:
            base_cmd += ["--experiment-tag", experiment_tag]
        if runs_subdir:
            base_cmd += ["--runs-subdir", runs_subdir]
        if states:
            base_cmd += ["--states", *states]
        if bool(args.force):
            base_cmd += ["--force"]
        if bool(args.dry_run):
            base_cmd += ["--dry-run"]
        if bool(args.skip_candidate_universe_grade):
            base_cmd += ["--skip-candidate-universe-grade"]
        if bool(args.skip_play_card_grade):
            base_cmd += ["--skip-play-card-grade"]
        # Rollup and windowed are handled at the range layer.
        base_cmd += ["--skip-windowed"]
        if bool(args.no_per_day_receipts):
            base_cmd += ["--no-receipt"]

        for d in _iter_dates(start_d, end_d):
            cmd = base_cmd + ["--date", d]
            receipt_lines.append(f"- `{(' '.join(cmd))}`")

        if bool(args.rollup):
            receipt_lines.append(f"- `{(' '.join(_cmd_rollup_candidate_universe(profile=profile, experiment_tag=experiment_tag)))}`")
            receipt_lines.append(f"- `{(' '.join(_cmd_rollup_play_card(profile=profile, experiment_tag=experiment_tag)))}`")

        windowed_start = (args.windowed_start_date or "").strip()
        windowed_end = (args.windowed_end_date or "").strip()
        if bool(args.windowed_auto) and (windowed_start or windowed_end):
            raise SystemExit("Use either --windowed-auto or --windowed-start-date/--windowed-end-date (not both).")

        windowed_cmd: Optional[List[str]] = None
        if not bool(args.skip_windowed):
            if windowed_start and windowed_end:
                windowed_cmd = _cmd_grade_play_card_windowed(
                    start_date=windowed_start,
                    end_date=windowed_end,
                    window_draws=int(args.windowed_draws),
                    sharepacks_root=sharepacks_root,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    states=states,
                    force=bool(args.force),
                )
                receipt_lines.append(f"- `{(' '.join(windowed_cmd))}`")
            elif bool(args.windowed_auto):
                end_cov, note = _windowed_auto_end_date(
                    start_date=start_d.isoformat(),
                    requested_end=end_d.isoformat(),
                    window_draws=int(args.windowed_draws),
                )
                receipt_lines.append(f"- windowed_auto_note: `{note}`")
                if end_cov:
                    windowed_cmd = _cmd_grade_play_card_windowed(
                        start_date=start_d.isoformat(),
                        end_date=end_cov,
                        window_draws=int(args.windowed_draws),
                        sharepacks_root=sharepacks_root,
                        profile=profile,
                        experiment_tag=experiment_tag,
                        states=states,
                        force=bool(args.force),
                    )
                    receipt_lines.append(f"- `{(' '.join(windowed_cmd))}`")
        receipt_lines.append("")

        for d in _iter_dates(start_d, end_d):
            if bool(args.skip_missing_results) and not _results_file_path(d).exists():
                print(f"[SKIP] Missing results for D={d}: {_safe_rel(_results_file_path(d))}")
                continue
            cmd = base_cmd + ["--date", d]
            try:
                _run(cmd, dry_run=bool(args.dry_run))
            except subprocess.CalledProcessError:
                if bool(args.skip_missing_results):
                    print(f"[SKIP] POST failed for D={d} (skip_missing_results=true)")
                    continue
                raise

        if bool(args.rollup):
            _run(_cmd_rollup_candidate_universe(profile=profile, experiment_tag=experiment_tag), dry_run=bool(args.dry_run))
            _run(_cmd_rollup_play_card(profile=profile, experiment_tag=experiment_tag), dry_run=bool(args.dry_run))

        if windowed_cmd:
            _run(windowed_cmd, dry_run=bool(args.dry_run))

        if not bool(args.no_receipt):
            suffix = f"__{experiment_tag}" if experiment_tag else ""
            receipt_path = runs_dir / f"V0_3__CYCLE__POST_RANGE__{start_d.isoformat()}_to_{end_d.isoformat()}__{profile}{suffix}.md"
            _write_receipt(receipt_path, receipt_lines, dry_run=bool(args.dry_run))
            if bool(args.dry_run):
                print(f"[DRY] Would write receipt: {_safe_rel(receipt_path)}")
            else:
                print(f"[OK] Wrote receipt: {_safe_rel(receipt_path)}")

        return

    raise SystemExit(f"Unknown command: {args.cmd!r}")


if __name__ == "__main__":
    main()
