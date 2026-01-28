#!/usr/bin/env python3
"""
Create a single side-by-side scoreboard from existing conversion ladder CSVs.

Why:
- We already generate per-strategy ladder reports.
- When iterating quickly, we need one SSOT table that shows:
  signal vs conversion, and the main failure bucket (CU_LANE_BUT_PLAY_MISS).

This is reporting-only:
- Reads: docs/AAT9_KIT/FINAL VALIDATION/RUNS/*__CONVERSION_LADDER__*.csv
- Writes: docs/AAT9_KIT/FINAL VALIDATION/RUNS/*__CONVERSION_SCOREBOARD__*.md
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


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


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _bucket(row: Dict[str, str]) -> str:
    if bool01(row.get("winner_missing")) == 1:
        return "CENSORED"
    cu_hit_any_raw = (row.get("cu_union_hit_any") or "").strip()
    cu_lane_raw = (row.get("cu_union_vtrac_index_hit") or "").strip()
    if not cu_hit_any_raw and not cu_lane_raw:
        return "NO_CU_JOIN"
    if bool01(row.get("play_hit_any_inclusive")) == 1:
        return "HIT_INCLUSIVE"
    if bool01(cu_hit_any_raw) == 1:
        return "CU_EXACT_BUT_PLAY_MISS"
    if bool01(cu_lane_raw) == 1:
        return "CU_LANE_BUT_PLAY_MISS"
    return "CU_MISS"


def _rate(rows: List[Dict[str, str]], key: str) -> Optional[float]:
    if not rows:
        return None
    return sum(bool01(r.get(key)) for r in rows) / float(len(rows))


def _fmt_pct(x: Optional[float]) -> str:
    return "NA" if x is None else f"{x * 100:.1f}%"


def _fmt_frac(n: int, d: int) -> str:
    return "NA" if d <= 0 else f"{(n / float(d)) * 100:.1f}%"


def _scoreboard_path(*, date_from: str, date_to: str, profile: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date_from}_to_{date_to}__CONVERSION_SCOREBOARD__{profile}{suffix}.md"


def _ladder_csv_path(*, date_from: str, date_to: str, profile: str, strategy: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date_from}_to_{date_to}__CONVERSION_LADDER__{profile}__{strategy}{suffix}.csv"


@dataclass(frozen=True)
class BudgetSummary:
    rows: int
    hit_any: Optional[float]
    hit_any_inclusive: Optional[float]
    pack_correct: Optional[float]
    pack_any_correct: Optional[float]
    pack_share_inclusive: str
    bucket_lane_miss: str
    bucket_exact_miss: str


def summarize_strategy(*, rows: List[Dict[str, str]], budget_label: str) -> BudgetSummary:
    focus = [r for r in rows if (r.get("budget_label") or "") == budget_label and bool01(r.get("winner_missing")) == 0]
    hit_any = _rate(focus, "play_hit_any")
    hit_any_inclusive = _rate(focus, "play_hit_any_inclusive")
    pack_correct = _rate(focus, "pack_correct")
    pack_any_correct = _rate(focus, "pack_any_correct")

    inc = sum(bool01(r.get("play_hit_any_inclusive")) for r in focus)
    pack_inc = sum(bool01(r.get("pack_hit_any_inclusive")) for r in focus)
    pack_share = _fmt_frac(pack_inc, inc)

    buckets: Dict[str, int] = {}
    for r in focus:
        buckets[_bucket(r)] = buckets.get(_bucket(r), 0) + 1
    lane_miss = _fmt_frac(buckets.get("CU_LANE_BUT_PLAY_MISS", 0), len(focus))
    exact_miss = _fmt_frac(buckets.get("CU_EXACT_BUT_PLAY_MISS", 0), len(focus))

    return BudgetSummary(
        rows=len(focus),
        hit_any=hit_any,
        hit_any_inclusive=hit_any_inclusive,
        pack_correct=pack_correct,
        pack_any_correct=pack_any_correct,
        pack_share_inclusive=pack_share,
        bucket_lane_miss=lane_miss,
        bucket_exact_miss=exact_miss,
    )


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a conversion scoreboard from existing ladder CSVs.")
    ap.add_argument("--date-from", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--date-to", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only", help="Profile in ladder filenames (default: tool_only).")
    ap.add_argument("--experiment-tag", default="", help="Optional experiment tag suffix (e.g., stable10).")
    ap.add_argument(
        "--strategies",
        required=True,
        help="Comma-separated list of play card strategies to compare (must already have ladder CSVs).",
    )
    ap.add_argument("--budgets", default="B24,B36", help="Comma-separated budget labels (default: B24,B36).")
    ap.add_argument("--out", default=None, help="Override output markdown path.")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    date_from = str(args.date_from).strip()
    date_to = str(args.date_to).strip()
    profile = str(args.profile or "tool_only").strip()
    exp_tag = _normalize_tag(args.experiment_tag)

    strategies = [s.strip() for s in str(args.strategies or "").split(",") if s.strip()]
    if not strategies:
        raise SystemExit("No strategies provided (use --strategies a,b,c)")

    budgets = [b.strip() for b in str(args.budgets or "").split(",") if b.strip()]
    if not budgets:
        raise SystemExit("No budgets provided (use --budgets B24,B36)")

    # Load rows per strategy.
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

    # CU union recall from the first strategy rows (same across strategies).
    # Deduplicate by (results_date, state_key, winner_label) to avoid triple-counting budgets.
    first_rows = rows_by_strategy[strategies[0]]
    seen_outcomes: set[tuple[str, str, str]] = set()
    cu_rows: List[Dict[str, str]] = []
    for r in first_rows:
        if bool01(r.get("winner_missing")) == 1:
            continue
        k = (r.get("results_date", ""), r.get("state_key", ""), r.get("winner_label", ""))
        if k in seen_outcomes:
            continue
        seen_outcomes.add(k)
        cu_rows.append(r)
    outcomes = len(cu_rows)
    cu_hit_any = _rate(cu_rows, "cu_union_hit_any")
    cu_vtrac = _rate(cu_rows, "cu_union_vtrac_index_hit")

    out_path = Path(args.out) if args.out else _scoreboard_path(date_from=date_from, date_to=date_to, profile=profile, experiment_tag=exp_tag)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append(f"# Conversion Scoreboard — {date_from}..{date_to}")
    lines.append("")
    lines.append("Source: conversion ladder CSVs (grade-output driven).")
    lines.append("")
    lines.append("## Candidate Universe (CU) recall (per outcome)")
    lines.append(f"- outcomes: `{outcomes}`")
    lines.append(f"- CU union hit_any: `{_fmt_pct(cu_hit_any)}`")
    lines.append(f"- CU union vtrac_index_hit: `{_fmt_pct(cu_vtrac)}`")
    lines.append("")

    for budget in budgets:
        lines.append(f"## {budget}")
        lines.append("")
        lines.append(
            "| strategy | rows | hit_any | hit_any_inclusive | pack_any_correct | pack_correct | pack_share(inclusive) | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for strat in strategies:
            summary = summarize_strategy(rows=rows_by_strategy[strat], budget_label=budget)
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{strat}`",
                        str(summary.rows),
                        _fmt_pct(summary.hit_any),
                        _fmt_pct(summary.hit_any_inclusive),
                        _fmt_pct(summary.pack_any_correct),
                        _fmt_pct(summary.pack_correct),
                        summary.pack_share_inclusive,
                        summary.bucket_lane_miss,
                        summary.bucket_exact_miss,
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.append("## Notes")
    lines.append("- `hit_any_inclusive` is the coverage contract (lane retained or better).")
    lines.append("- `hit_any` is the strict contract (exact membership in the budgeted list).")
    lines.append("- `pack_any_correct` is the key bridge metric for multi-pack strategies.")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
