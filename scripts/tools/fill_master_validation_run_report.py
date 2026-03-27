#!/usr/bin/env python3
"""
Rewrite a per-state Master Validation report using the arena-native contract.

Historically this script tried to fill a legacy summary-driven scaffold. For the
analysis-arena branch, the active behavior is simpler and safer:

- read the same predictive/runtime + frozen truth artifacts as
  `create_master_validation_run_report.py`
- regenerate the arena-native report in-place at the requested output path

This keeps the old workflow step callable without routing it back through the
old per-tool summary shell.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from scripts.tools.create_master_validation_run_report import (
    REPO_ROOT,
    RUNS2_DIR,
    build_master_validation_run_report,
    normalize_tag,
    parse_iso_date,
    safe_rel,
)


def _default_report_path(*, date: str, state: str) -> Path:
    return RUNS2_DIR / f"{date}__{state}.md"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Rewrite an arena-native Master Validation report in-place.")
    ap.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (for example NewYork4)")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument(
        "--predictive-sharepacks-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--truth-sharepacks-root",
        default="sharepacks",
        help="Frozen/results sharepacks root for winners truth (default: sharepacks)",
    )
    ap.add_argument(
        "--report-path",
        default=None,
        help="Optional explicit report path to rewrite (default: RUNS_2/<D>__<STATE>.md).",
    )
    return ap.parse_args()


def main() -> None:
    args = _parse_args()
    results_date = parse_iso_date(args.date).isoformat()
    predictive_sharepacks_root = Path(args.predictive_sharepacks_root)
    if not predictive_sharepacks_root.is_absolute():
        predictive_sharepacks_root = (REPO_ROOT / predictive_sharepacks_root).resolve()
    truth_sharepacks_root = Path(args.truth_sharepacks_root)
    if not truth_sharepacks_root.is_absolute():
        truth_sharepacks_root = (REPO_ROOT / truth_sharepacks_root).resolve()

    report_path = Path(args.report_path) if args.report_path else _default_report_path(date=results_date, state=args.state)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    report = build_master_validation_run_report(
        results_date=results_date,
        state=args.state,
        profile=str(args.profile or "tool_only").strip(),
        experiment_tag=normalize_tag(args.experiment_tag),
        predictive_sharepacks_root=predictive_sharepacks_root,
        truth_sharepacks_root=truth_sharepacks_root,
    )
    report_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {safe_rel(report_path)}")


if __name__ == "__main__":
    main()
