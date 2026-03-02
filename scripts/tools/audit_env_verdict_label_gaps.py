#!/usr/bin/env python3
"""
Audit missing MV env_verdict labels for outcomes that appear in __PORTFOLIO_VS_RESULTS__ windows.

Why this exists (plain English)
------------------------------
Some reports (e.g., env-verdict scoreboards) join objective outcome metrics
(`__PORTFOLIO_VS_RESULTS__*.csv`) against a human MV synthesis label (`env_verdict`)
stored in `RUNS/corpus_summary.csv`.

If a (date, state, period) row has no label in `corpus_summary.csv`, it shows up as
`UNLABELED` and can dilute posture/regime conclusions.

This script produces a concrete "here are the missing rows + what to open" report,
so you can fill labels without hunting.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


RowKey = Tuple[str, str, str]  # (date, state_key, period)


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _as_int(value: str) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _load_env_map(corpus_summary_csv: Path) -> Dict[RowKey, str]:
    env: Dict[RowKey, str] = {}
    with corpus_summary_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key: RowKey = (row["date"], row["state"], row["period"])
            env[key] = (row.get("env_verdict") or "").strip()
    return env


def _iter_budget_rows(window_csv: Path, *, budget_label: str) -> Iterable[dict]:
    with window_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("winner_missing", "0") == "1":
                continue
            if row.get("budget_label") != budget_label:
                continue
            yield row


@dataclass(frozen=True)
class GapRow:
    window: str
    date: str
    state: str
    period: str
    winner: str
    winner_canon: str
    winner_vtrac_index: str
    run_report_guess: str
    run_report_exists: bool
    results_path: str
    portfolio_path: str
    portfolio_dc1_path: str


def _guess_run_report(date: str, state: str) -> Path:
    return _runs_dir() / f"{date}__{state}.md"


def _guess_portfolio(date: str, *, dc1: bool) -> Path:
    if dc1:
        return _runs_dir() / f"{date}__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md"
    return _runs_dir() / f"{date}__PREDICTIVE_PORTFOLIO__tool_only.md"


def _guess_results(date: str) -> Path:
    return REPO_ROOT / "data" / "results" / f"{date}.txt"


def _collect_gaps(
    *,
    env_map: Dict[RowKey, str],
    budget_label: str,
    windows: Sequence[Tuple[str, Path]],
) -> Tuple[List[GapRow], Dict[str, int], Dict[str, int]]:
    gaps: List[GapRow] = []
    labeled_by_window: Dict[str, int] = {}
    total_by_window: Dict[str, int] = {}

    for label, window_csv in windows:
        labeled = 0
        total = 0
        for row in _iter_budget_rows(window_csv, budget_label=budget_label):
            total += 1
            key: RowKey = (row["results_date"], row["state_key"], row["winner_label"])
            verdict = env_map.get(key, "")
            if verdict.strip():
                labeled += 1
                continue

            date = row["results_date"]
            state = row["state_key"]
            period = row["winner_label"]

            run_report = _guess_run_report(date, state)
            results_path = _guess_results(date)
            portfolio = _guess_portfolio(date, dc1=False)
            portfolio_dc1 = _guess_portfolio(date, dc1=True)

            gaps.append(
                GapRow(
                    window=label,
                    date=date,
                    state=state,
                    period=period,
                    winner=row.get("winner", ""),
                    winner_canon=row.get("winner_canonical", ""),
                    winner_vtrac_index=row.get("winner_vtrac_index", ""),
                    run_report_guess=_safe_rel(run_report),
                    run_report_exists=run_report.exists(),
                    results_path=_safe_rel(results_path),
                    portfolio_path=_safe_rel(portfolio),
                    portfolio_dc1_path=_safe_rel(portfolio_dc1),
                )
            )

        labeled_by_window[label] = labeled
        total_by_window[label] = total

    return gaps, total_by_window, labeled_by_window


def _write_md(
    out_md: Path,
    *,
    corpus_summary_csv: Path,
    budget_label: str,
    windows: Sequence[Tuple[str, Path]],
    gaps: Sequence[GapRow],
    total_by_window: Dict[str, int],
    labeled_by_window: Dict[str, int],
) -> None:
    lines: List[str] = []
    lines.append(f"# Env Verdict Label Gaps — {budget_label} (MV synthesis)")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Identify which outcome rows (date/state/period) are **missing** `env_verdict` labels in MV synthesis.")
    lines.append("- This explains `UNLABELED` buckets in posture scoreboards and tells you exactly what to open to label them.")
    lines.append("")
    lines.append("Inputs")
    lines.append(f"- MV synthesis labels: `{_safe_rel(corpus_summary_csv)}`")
    for label, window_csv in windows:
        lines.append(f"- Window `{label}`: `{_safe_rel(window_csv)}`")
    lines.append("")
    lines.append("How to use")
    lines.append("1) Pick a missing row below.")
    lines.append("2) Open the suggested `run_report_guess` if it exists (best), otherwise open the portfolio + results for context.")
    lines.append("3) Add (or fill) the `env_verdict` for that (date, state, period) row in `corpus_summary.csv`.")
    lines.append("")
    lines.append("## Coverage summary")
    lines.append("")
    lines.append("| Window | Rows (winner-present) | Rows with non-empty env_verdict | Missing |")
    lines.append("|---|---:|---:|---:|")
    for label, _ in windows:
        total = total_by_window.get(label, 0)
        labeled = labeled_by_window.get(label, 0)
        missing = max(total - labeled, 0)
        lines.append(f"| {label} | {total} | {labeled} | {missing} |")
    lines.append("")

    if not gaps:
        lines.append("No gaps found for the requested windows/budget.")
        lines.append("")
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    # Group by date for operator convenience
    gaps_by_date: Dict[str, List[GapRow]] = {}
    for g in gaps:
        gaps_by_date.setdefault(g.date, []).append(g)

    lines.append("## Missing rows (grouped by date)")
    lines.append("")
    for date in sorted(gaps_by_date.keys()):
        rows = gaps_by_date[date]
        lines.append(f"### {date} ({len(rows)} missing)")
        lines.append("")
        lines.append("| State | Period | Winner | Canon | idx | run_report_guess | report_exists | portfolio | portfolio_dc1 | results |")
        lines.append("|---|---|---:|---:|---:|---|---:|---|---|---|")
        for g in sorted(rows, key=lambda r: (r.state, r.period)):
            lines.append(
                "| "
                + " | ".join(
                    [
                        g.state,
                        g.period,
                        g.winner or "-",
                        g.winner_canon or "-",
                        g.winner_vtrac_index or "-",
                        f"`{g.run_report_guess}`",
                        "1" if g.run_report_exists else "0",
                        f"`{g.portfolio_path}`",
                        f"`{g.portfolio_dc1_path}`",
                        f"`{g.results_path}`",
                    ]
                )
                + " |"
            )
        lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_csv(out_csv: Path, *, gaps: Sequence[GapRow]) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "window",
        "date",
        "state",
        "period",
        "winner",
        "winner_canon",
        "winner_vtrac_index",
        "run_report_guess",
        "run_report_exists",
        "portfolio_path",
        "portfolio_dc1_path",
        "results_path",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for g in gaps:
            writer.writerow(
                {
                    "window": g.window,
                    "date": g.date,
                    "state": g.state,
                    "period": g.period,
                    "winner": g.winner,
                    "winner_canon": g.winner_canon,
                    "winner_vtrac_index": g.winner_vtrac_index,
                    "run_report_guess": g.run_report_guess,
                    "run_report_exists": "1" if g.run_report_exists else "0",
                    "portfolio_path": g.portfolio_path,
                    "portfolio_dc1_path": g.portfolio_dc1_path,
                    "results_path": g.results_path,
                }
            )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-md", required=True, help="Output markdown path.")
    parser.add_argument("--out-csv", default="", help="Optional output CSV path.")
    parser.add_argument(
        "--corpus-summary",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv",
        help="Path to corpus_summary.csv (env_verdict labels).",
    )
    parser.add_argument("--budget", default="B36", help="Budget label to audit (default: B36).")
    parser.add_argument(
        "--window",
        action="append",
        required=True,
        help="Window pair: LABEL:WINDOW_CSV",
    )
    args = parser.parse_args(argv)

    corpus_summary_csv = REPO_ROOT / args.corpus_summary
    out_md = REPO_ROOT / args.out_md
    out_csv = (REPO_ROOT / args.out_csv) if args.out_csv else None
    budget_label = args.budget

    windows: List[Tuple[str, Path]] = []
    for spec in args.window:
        parts = spec.split(":")
        if len(parts) != 2:
            raise SystemExit(f"Invalid --window spec: {spec} (expected LABEL:WINDOW_CSV)")
        label, window_csv = parts
        windows.append((label, REPO_ROOT / window_csv))

    env_map = _load_env_map(corpus_summary_csv)
    gaps, total_by_window, labeled_by_window = _collect_gaps(
        env_map=env_map, budget_label=budget_label, windows=windows
    )

    _write_md(
        out_md,
        corpus_summary_csv=corpus_summary_csv,
        budget_label=budget_label,
        windows=windows,
        gaps=gaps,
        total_by_window=total_by_window,
        labeled_by_window=labeled_by_window,
    )

    if out_csv is not None:
        _write_csv(out_csv, gaps=gaps)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

