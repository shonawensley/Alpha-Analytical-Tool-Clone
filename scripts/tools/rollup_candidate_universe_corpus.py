#!/usr/bin/env python3
"""
Roll up Candidate Universe grading outputs across all available days.

This is reporting-only:
- Reads: RUNS/*__CANDIDATE_UNIVERSE_GRADE*.csv
- Writes: RUNS/candidate_universe_rollup*.{csv,md}

No analyzer changes, no sharepack writes.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def _truthy(value: str) -> bool:
    return str(value).strip() == "1"


def _rate(n: int, d: int) -> str:
    return "" if d == 0 else f"{(n / d):.4f}"


@dataclass
class Agg:
    rows_measured: int = 0
    hit_any: int = 0
    straight_hit: int = 0
    box_hit: int = 0
    vtrac_index_hit: int = 0
    vtrac_index_hit_only: int = 0
    cost_units: List[int] = field(default_factory=list)
    combos_count: List[int] = field(default_factory=list)
    dates: Set[str] = field(default_factory=set)

    def add(self, row: Dict[str, str]) -> None:
        if _truthy(row.get("winner_missing", "")):
            return
        self.rows_measured += 1
        self.hit_any += 1 if _truthy(row.get("hit_any", "")) else 0
        self.straight_hit += 1 if _truthy(row.get("straight_hit", "")) else 0
        self.box_hit += 1 if _truthy(row.get("box_hit", "")) else 0
        self.vtrac_index_hit += 1 if _truthy(row.get("vtrac_index_hit", "")) else 0
        self.vtrac_index_hit_only += 1 if _truthy(row.get("vtrac_index_hit_only", "")) else 0
        cu = _safe_int(row.get("cost_units", "") or "")
        if cu is not None:
            self.cost_units.append(cu)
        cc = _safe_int(row.get("combos_count", "") or "")
        if cc is not None:
            self.combos_count.append(cc)
        d = (row.get("results_date") or "").strip()
        if d:
            self.dates.add(d)

    def avg_cost_units(self) -> Optional[float]:
        return sum(self.cost_units) / len(self.cost_units) if self.cost_units else None

    def avg_combos_count(self) -> Optional[float]:
        return sum(self.combos_count) / len(self.combos_count) if self.combos_count else None


def _iter_grade_csvs(runs_dir: Path) -> List[Path]:
    return sorted(runs_dir.glob("*__CANDIDATE_UNIVERSE_GRADE.csv"))


def _iter_grade_csvs_profile(runs_dir: Path, *, profile: str) -> List[Path]:
    p = (profile or "mixed").strip()
    if p == "mixed":
        return _iter_grade_csvs(runs_dir)
    return sorted(runs_dir.glob(f"*__CANDIDATE_UNIVERSE_GRADE__{p}.csv"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def _fmt_float(v: Optional[float]) -> str:
    return "" if v is None else f"{v:.3f}"


def main() -> None:
    ap = argparse.ArgumentParser(description="Roll up Candidate Universe grades across all days in RUNS.")
    ap.add_argument(
        "--runs-dir",
        default=str(_runs_dir()),
        help="RUNS directory (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="mixed",
        help="Ablation profile to roll up (default: mixed).",
    )
    ap.add_argument("--out-csv", default=None, help="Override output CSV path")
    ap.add_argument("--out-md", default=None, help="Override output Markdown path")
    args = ap.parse_args()

    runs_dir = Path(args.runs_dir)
    if not runs_dir.is_absolute():
        runs_dir = (REPO_ROOT / runs_dir).resolve()
    runs_dir.mkdir(parents=True, exist_ok=True)

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"

    grade_csvs = _iter_grade_csvs_profile(runs_dir, profile=profile)
    if not grade_csvs:
        raise SystemExit(f"No Candidate Universe grade CSVs found under: {_safe_rel(runs_dir)} (profile={profile})")

    by_key: Dict[Tuple[str, str, str], Agg] = {}
    all_dates: Set[str] = set()
    rows_total = 0

    for p in grade_csvs:
        for row in _load_csv_rows(p):
            rows_total += 1
            method_id = (row.get("method_id") or "").strip() or "UNKNOWN"
            winner_label = (row.get("winner_label") or "").strip() or "Unknown"
            play_mode = (row.get("play_mode") or "").strip() or "Unknown"
            key = (method_id, winner_label, play_mode)
            agg = by_key.setdefault(key, Agg())
            agg.add(row)
            all_dates.update(agg.dates)

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"candidate_universe_rollup{out_suffix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"candidate_universe_rollup{out_suffix}.md"

    out_rows: List[Dict[str, object]] = []
    for (method_id, winner_label, play_mode), agg in by_key.items():
        d = agg.rows_measured
        out_rows.append(
            {
                "method_id": method_id,
                "winner_label": winner_label,
                "play_mode": play_mode,
                "rows_measured": d,
                "dates_covered": len(agg.dates),
                "hit_any": agg.hit_any,
                "hit_any_rate": _rate(agg.hit_any, d),
                "straight_hit": agg.straight_hit,
                "straight_hit_rate": _rate(agg.straight_hit, d),
                "box_hit": agg.box_hit,
                "box_hit_rate": _rate(agg.box_hit, d),
                "vtrac_index_hit": agg.vtrac_index_hit,
                "vtrac_index_hit_rate": _rate(agg.vtrac_index_hit, d),
                "vtrac_index_hit_only": agg.vtrac_index_hit_only,
                "vtrac_index_hit_only_rate": _rate(agg.vtrac_index_hit_only, d),
                "avg_cost_units": _fmt_float(agg.avg_cost_units()),
                "avg_combos_count": _fmt_float(agg.avg_combos_count()),
            }
        )

    out_rows.sort(
        key=lambda r: (
            str(r["winner_label"]),
            -float(r["hit_any_rate"] or 0.0),
            -int(r["rows_measured"] or 0),
            str(r["method_id"]),
            str(r["play_mode"]),
        )
    )

    _write_csv(
        out_csv,
        fieldnames=[
            "method_id",
            "winner_label",
            "play_mode",
            "rows_measured",
            "dates_covered",
            "hit_any",
            "hit_any_rate",
            "straight_hit",
            "straight_hit_rate",
            "box_hit",
            "box_hit_rate",
            "vtrac_index_hit",
            "vtrac_index_hit_rate",
            "vtrac_index_hit_only",
            "vtrac_index_hit_only_rate",
            "avg_cost_units",
            "avg_combos_count",
        ],
        rows=out_rows,
    )

    # Minimal Markdown surface.
    dates_sorted = sorted(all_dates)
    lines = [
        "# Candidate Universe Rollup",
        "",
        f"- Grade files: `{len(grade_csvs)}`",
        f"- Rows scanned: `{rows_total}`",
        f"- Dates covered: `{len(dates_sorted)}`",
        f"- Date range: `{dates_sorted[0]}` → `{dates_sorted[-1]}`" if dates_sorted else "- Date range: —",
        "",
        "## By method (winner_label + play_mode)",
        "",
        "| winner_label | method_id | play_mode | rows | hit_any | box_hit | straight_hit | vtrac_hit |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in out_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["winner_label"]),
                    f"`{r['method_id']}`",
                    str(r["play_mode"]),
                    str(r["rows_measured"]),
                    str(r["hit_any_rate"]),
                    str(r["box_hit_rate"]),
                    str(r["straight_hit_rate"]),
                    str(r["vtrac_index_hit_rate"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append(f"- CSV: `{_safe_rel(out_csv)}`")
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
