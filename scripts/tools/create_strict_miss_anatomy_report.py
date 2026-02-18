#!/usr/bin/env python3
"""
Create a "strict miss anatomy" report from existing conversion ladder CSVs.

Why:
- We often debate whether strict misses are mostly because we dropped the winner lane (index set issue)
  or because we retained the lane but failed to convert within it (within-lane issue).
- This report partitions strict misses into:
    - lane dropped (play_vtrac_index_hit=0)
    - lane retained (play_vtrac_index_hit=1)

Inputs:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/*__CONVERSION_LADDER__*.csv

Outputs:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/*__STRICT_MISS_ANATOMY__*.md

Reporting-only:
- Does not modify sharepacks, analyzers, or Play Card selection behavior.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:60]


def bool01(value: object) -> int:
    s = str(value or "").strip().lower()
    if s in {"1", "true", "yes", "y"}:
        return 1
    if s in {"0", "false", "no", "n", ""}:
        return 0
    try:
        return 1 if int(s) else 0
    except Exception:
        return 0


def _fmt_pct(x: Optional[float]) -> str:
    return "NA" if x is None else f"{x * 100:.1f}%"


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _ladder_csv_path(*, date_from: str, date_to: str, profile: str, strategy: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date_from}_to_{date_to}__CONVERSION_LADDER__{profile}__{strategy}{suffix}.csv"


def _default_out_path(*, date_from: str, date_to: str, profile: str, experiment_tag: str, budget_label: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    extra = f"__{budget_label}"
    return RUNS_DIR / f"{date_from}_to_{date_to}__STRICT_MISS_ANATOMY__{profile}{suffix}{extra}.md"


@dataclass(frozen=True)
class StrategySummary:
    outcomes: int
    strict_hit: int
    strict_miss: int
    lane_retained_rate: Optional[float]
    strict_given_lane_retained: Optional[float]
    strict_miss_lane_dropped_share: Optional[float]
    strict_miss_lane_retained_share: Optional[float]


def _rate(n: int, d: int) -> Optional[float]:
    if d <= 0:
        return None
    return n / float(d)


def summarize(*, rows: List[Dict[str, str]], budget_label: str) -> StrategySummary:
    focus = [r for r in rows if (r.get("budget_label") or "") == budget_label and bool01(r.get("winner_missing")) == 0]
    outcomes = len(focus)

    strict_hit = sum(bool01(r.get("play_hit_any")) for r in focus)
    strict_miss = outcomes - strict_hit

    lane_retained = sum(bool01(r.get("play_vtrac_index_hit")) for r in focus)
    lane_retained_rate = _rate(lane_retained, outcomes)

    strict_hit_and_lane = sum(bool01(r.get("play_hit_any")) for r in focus if bool01(r.get("play_vtrac_index_hit")) == 1)
    strict_given_lane = _rate(strict_hit_and_lane, lane_retained)

    miss_lane_dropped = sum(
        1
        for r in focus
        if bool01(r.get("play_hit_any")) == 0 and bool01(r.get("play_vtrac_index_hit")) == 0
    )
    miss_lane_retained = sum(
        1
        for r in focus
        if bool01(r.get("play_hit_any")) == 0 and bool01(r.get("play_vtrac_index_hit")) == 1
    )

    # Conditional shares among strict misses.
    miss_lane_dropped_share = _rate(miss_lane_dropped, strict_miss)
    miss_lane_retained_share = _rate(miss_lane_retained, strict_miss)

    return StrategySummary(
        outcomes=outcomes,
        strict_hit=strict_hit,
        strict_miss=strict_miss,
        lane_retained_rate=lane_retained_rate,
        strict_given_lane_retained=strict_given_lane,
        strict_miss_lane_dropped_share=miss_lane_dropped_share,
        strict_miss_lane_retained_share=miss_lane_retained_share,
    )


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a strict miss anatomy report from existing ladder CSVs.")
    ap.add_argument("--date-from", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--date-to", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only", help="Profile in ladder filenames (default: tool_only).")
    ap.add_argument("--experiment-tag", default="", help="Optional experiment tag suffix (e.g., stable10).")
    ap.add_argument("--strategies", required=True, help="Comma-separated list of strategies to summarize.")
    ap.add_argument("--budget", default="B36", help="Budget label to analyze (default: B36).")
    ap.add_argument("--out", default=None, help="Override output markdown path.")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    date_from = str(args.date_from).strip()
    date_to = str(args.date_to).strip()
    profile = str(args.profile or "tool_only").strip()
    exp_tag = _normalize_tag(args.experiment_tag)
    budget_label = str(args.budget or "B36").strip()

    strategies = [s.strip() for s in str(args.strategies or "").split(",") if s.strip()]
    if not strategies:
        raise SystemExit("No strategies provided (use --strategies a,b,c)")

    rows_by_strategy: Dict[str, List[Dict[str, str]]] = {}
    for strat in strategies:
        path = _ladder_csv_path(
            date_from=date_from,
            date_to=date_to,
            profile=profile,
            strategy=strat,
            experiment_tag=exp_tag,
        )
        if not path.exists():
            raise SystemExit(f"Missing ladder CSV for strategy={strat}: {path}")
        rows_by_strategy[strat] = load_csv_rows(path)

    out_path = Path(args.out) if args.out else _default_out_path(
        date_from=date_from,
        date_to=date_to,
        profile=profile,
        experiment_tag=exp_tag,
        budget_label=budget_label,
    )
    if not out_path.is_absolute():
        out_path = (REPO_ROOT / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append(f"# Strict Miss Anatomy — {date_from}..{date_to}")
    lines.append("")
    lines.append("Source: conversion ladder CSVs (grade-output driven).")
    lines.append("")
    lines.append(f"Budget: `{budget_label}` | Profile: `{profile}` | Experiment tag: `{exp_tag or '<none>'}`")
    lines.append("")
    lines.append("Interpretation:")
    lines.append("- `lane_retained_rate` answers: “did the B36 Play Card touch the winner lane at all?”")
    lines.append("- `strict_given_lane_retained` answers: “once we retained the lane, did we convert to strict?”")
    lines.append("- `strict_miss_lane_*_share` answers: “when strict misses happen, are they mostly lane drops or within-lane misses?”")
    lines.append("")

    lines.append(f"## {budget_label}")
    lines.append("")
    lines.append("| strategy | outcomes | strict_hit | strict_miss | lane_retained_rate | strict_given_lane_retained | strict_miss_lane_dropped_share | strict_miss_lane_retained_share |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")

    for strat in strategies:
        s = summarize(rows=rows_by_strategy[strat], budget_label=budget_label)
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{strat}`",
                    str(s.outcomes),
                    str(s.strict_hit),
                    str(s.strict_miss),
                    _fmt_pct(s.lane_retained_rate),
                    _fmt_pct(s.strict_given_lane_retained),
                    _fmt_pct(s.strict_miss_lane_dropped_share),
                    _fmt_pct(s.strict_miss_lane_retained_share),
                ]
            )
            + " |"
        )

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()

