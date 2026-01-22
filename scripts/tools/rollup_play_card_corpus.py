#!/usr/bin/env python3
"""
Roll up Play Card grading outputs across all available days.

This is reporting-only:
- Reads: RUNS/*__PLAY_CARD_GRADE*.csv
- Writes: RUNS/play_card_rollup*.{csv,md}
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple


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


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw)
    cleaned = cleaned.strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --experiment-tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _rate(n: int, d: int) -> str:
    return "" if d == 0 else f"{(n / d):.4f}"


@dataclass
class Agg:
    rows_measured: int = 0
    hit_any: int = 0
    hit_any_box: int = 0
    hit_any_inclusive: int = 0
    straight_hit: int = 0
    box_hit: int = 0
    canon_hit_any_perm: int = 0
    vtrac_index_hit: int = 0
    vtrac_index_hit_only: int = 0
    pack_hit_any_inclusive: int = 0
    filler_hit_any_inclusive: int = 0
    pack_only_hit_any_inclusive: int = 0
    pack_and_filler_hit_any_inclusive: int = 0
    pack_vtrac_index_hit: int = 0
    pack_canon_hit_any_perm: int = 0
    pack_straight_hit: int = 0
    combos_count: List[int] = field(default_factory=list)
    boxed_canonicals_count: List[int] = field(default_factory=list)
    vtrac_pack_size: List[int] = field(default_factory=list)
    filler_size: List[int] = field(default_factory=list)
    dates: Set[str] = field(default_factory=set)

    def add(self, row: Dict[str, str]) -> None:
        if _truthy(row.get("winner_missing", "")):
            return
        self.rows_measured += 1
        self.hit_any += 1 if _truthy(row.get("hit_any", "")) else 0
        self.hit_any_box += 1 if _truthy(row.get("hit_any_box", "")) else 0
        self.hit_any_inclusive += 1 if _truthy(row.get("hit_any_inclusive", "")) else 0
        self.straight_hit += 1 if _truthy(row.get("straight_hit", "")) else 0
        self.box_hit += 1 if _truthy(row.get("box_hit", "")) else 0
        self.canon_hit_any_perm += 1 if _truthy(row.get("canon_hit_any_perm", "")) else 0
        self.vtrac_index_hit += 1 if _truthy(row.get("vtrac_index_hit", "")) else 0
        self.vtrac_index_hit_only += 1 if _truthy(row.get("vtrac_index_hit_only", "")) else 0
        self.pack_hit_any_inclusive += 1 if _truthy(row.get("pack_hit_any_inclusive", "")) else 0
        self.filler_hit_any_inclusive += 1 if _truthy(row.get("filler_hit_any_inclusive", "")) else 0
        self.pack_only_hit_any_inclusive += 1 if _truthy(row.get("pack_only_hit_any_inclusive", "")) else 0
        self.pack_and_filler_hit_any_inclusive += 1 if _truthy(row.get("pack_and_filler_hit_any_inclusive", "")) else 0
        self.pack_vtrac_index_hit += 1 if _truthy(row.get("pack_vtrac_index_hit", "")) else 0
        self.pack_canon_hit_any_perm += 1 if _truthy(row.get("pack_canon_hit_any_perm", "")) else 0
        self.pack_straight_hit += 1 if _truthy(row.get("pack_straight_hit", "")) else 0
        cc = _safe_int(row.get("combos_count", "") or "")
        if cc is not None:
            self.combos_count.append(cc)
        bc = _safe_int(row.get("boxed_canonicals_count", "") or "")
        if bc is not None:
            self.boxed_canonicals_count.append(bc)
        ps = _safe_int(row.get("vtrac_pack_size", "") or "")
        if ps is not None:
            self.vtrac_pack_size.append(ps)
        fs = _safe_int(row.get("filler_size", "") or "")
        if fs is not None:
            self.filler_size.append(fs)
        d = (row.get("results_date") or "").strip()
        if d:
            self.dates.add(d)

    def avg_combos_count(self) -> Optional[float]:
        return sum(self.combos_count) / len(self.combos_count) if self.combos_count else None

    def avg_boxed_canonicals_count(self) -> Optional[float]:
        return sum(self.boxed_canonicals_count) / len(self.boxed_canonicals_count) if self.boxed_canonicals_count else None

    def avg_vtrac_pack_size(self) -> Optional[float]:
        return sum(self.vtrac_pack_size) / len(self.vtrac_pack_size) if self.vtrac_pack_size else None

    def avg_filler_size(self) -> Optional[float]:
        return sum(self.filler_size) / len(self.filler_size) if self.filler_size else None


def _iter_grade_csvs(runs_dir: Path, *, tag_suffix: str = "") -> List[Path]:
    return sorted(runs_dir.glob(f"*__PLAY_CARD_GRADE{tag_suffix}.csv"))


def _iter_grade_csvs_profile(runs_dir: Path, *, profile: str, tag_suffix: str = "") -> List[Path]:
    p = (profile or "mixed").strip()
    if p == "mixed":
        return _iter_grade_csvs(runs_dir, tag_suffix=tag_suffix)
    return sorted(runs_dir.glob(f"*__PLAY_CARD_GRADE__{p}{tag_suffix}.csv"))


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
    ap = argparse.ArgumentParser(description="Roll up Play Card grades across all days in RUNS.")
    ap.add_argument(
        "--runs-dir",
        default=str(_runs_dir()),
        help="RUNS directory (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile to roll up (default: tool_only).",
    )
    ap.add_argument(
        "--experiment-tag",
        default="",
        help="Optional experiment tag suffix selecting grade files + rollup outputs (default: none).",
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
    exp_tag = _normalize_experiment_tag(args.experiment_tag)
    tag_suffix = f"__{exp_tag}" if exp_tag else ""

    grade_csvs = _iter_grade_csvs_profile(runs_dir, profile=profile, tag_suffix=tag_suffix)
    if not grade_csvs:
        raise SystemExit(f"No Play Card grade CSVs found under: {_safe_rel(runs_dir)} (profile={profile}, tag={exp_tag or '—'})")

    by_key: Dict[Tuple[str, str, str], Agg] = {}
    all_dates: Set[str] = set()
    rows_total = 0

    for p in grade_csvs:
        for row in _load_csv_rows(p):
            rows_total += 1
            strategy = (row.get("strategy") or "").strip() or "UNKNOWN"
            budget_label = (row.get("budget_label") or "").strip() or "UNKNOWN"
            winner_label = (row.get("winner_label") or "").strip() or "Unknown"
            key = (strategy, budget_label, winner_label)
            agg = by_key.setdefault(key, Agg())
            agg.add(row)
            all_dates.update(agg.dates)

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"play_card_rollup{out_suffix}{tag_suffix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"play_card_rollup{out_suffix}{tag_suffix}.md"

    out_rows: List[Dict[str, object]] = []
    for (strategy, budget_label, winner_label), agg in by_key.items():
        d = agg.rows_measured
        out_rows.append(
            {
                "strategy": strategy,
                "budget_label": budget_label,
                "winner_label": winner_label,
                "rows_measured": d,
                "dates_covered": len(agg.dates),
                "hit_any": agg.hit_any,
                "hit_any_rate": _rate(agg.hit_any, d),
                "hit_any_box_rate": _rate(agg.hit_any_box, d),
                "hit_any_inclusive_rate": _rate(agg.hit_any_inclusive, d),
                "canon_hit_any_perm_rate": _rate(agg.canon_hit_any_perm, d),
                "straight_hit_rate": _rate(agg.straight_hit, d),
                "box_hit_rate": _rate(agg.box_hit, d),
                "vtrac_index_hit_rate": _rate(agg.vtrac_index_hit, d),
                "vtrac_index_hit_only_rate": _rate(agg.vtrac_index_hit_only, d),
                "pack_hit_any_inclusive_rate": _rate(agg.pack_hit_any_inclusive, d),
                "filler_hit_any_inclusive_rate": _rate(agg.filler_hit_any_inclusive, d),
                "pack_only_hit_any_inclusive_rate": _rate(agg.pack_only_hit_any_inclusive, d),
                "pack_and_filler_hit_any_inclusive_rate": _rate(agg.pack_and_filler_hit_any_inclusive, d),
                "pack_vtrac_index_hit_rate": _rate(agg.pack_vtrac_index_hit, d),
                "pack_canon_hit_any_perm_rate": _rate(agg.pack_canon_hit_any_perm, d),
                "pack_straight_hit_rate": _rate(agg.pack_straight_hit, d),
                "avg_combos_count": _fmt_float(agg.avg_combos_count()),
                "avg_boxed_canonicals_count": _fmt_float(agg.avg_boxed_canonicals_count()),
                "avg_vtrac_pack_size": _fmt_float(agg.avg_vtrac_pack_size()),
                "avg_filler_size": _fmt_float(agg.avg_filler_size()),
            }
        )

    out_rows.sort(
        key=lambda r: (
            str(r["winner_label"]),
            -float(r["hit_any_inclusive_rate"] or 0.0),
            str(r["strategy"]),
            str(r["budget_label"]),
        )
    )

    _write_csv(
        out_csv,
        fieldnames=[
            "strategy",
            "budget_label",
            "winner_label",
            "rows_measured",
            "dates_covered",
            "hit_any",
            "hit_any_rate",
            "hit_any_box_rate",
            "hit_any_inclusive_rate",
            "canon_hit_any_perm_rate",
            "straight_hit_rate",
            "box_hit_rate",
            "vtrac_index_hit_rate",
            "vtrac_index_hit_only_rate",
            "pack_hit_any_inclusive_rate",
            "filler_hit_any_inclusive_rate",
            "pack_only_hit_any_inclusive_rate",
            "pack_and_filler_hit_any_inclusive_rate",
            "pack_vtrac_index_hit_rate",
            "pack_canon_hit_any_perm_rate",
            "pack_straight_hit_rate",
            "avg_combos_count",
            "avg_boxed_canonicals_count",
            "avg_vtrac_pack_size",
            "avg_filler_size",
        ],
        rows=out_rows,
    )

    dates_sorted = sorted(all_dates)
    lines = [
        "# Play Card Rollup",
        "",
        f"- Grade files: `{len(grade_csvs)}`",
        f"- Rows scanned: `{rows_total}`",
        f"- experiment_tag: `{exp_tag}`" if exp_tag else "- experiment_tag: —",
        f"- Dates covered: `{len(dates_sorted)}`",
        f"- Date range: `{dates_sorted[0]}` → `{dates_sorted[-1]}`" if dates_sorted else "- Date range: —",
        "",
        "## By strategy + budget (winner_label)",
        "",
        "| winner_label | strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | perm_hit | closure_hit | straight_hit | vtrac_hit | pack_hit | pack_only | filler_hit | pack_idx_hit | avg_pack |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in out_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["winner_label"]),
                    f"`{r['strategy']}`",
                    str(r["budget_label"]),
                    str(r["rows_measured"]),
                    str(r["hit_any_rate"]),
                    str(r["hit_any_box_rate"]),
                    str(r["hit_any_inclusive_rate"]),
                    str(r["canon_hit_any_perm_rate"]),
                    str(r["box_hit_rate"]),
                    str(r["straight_hit_rate"]),
                    str(r["vtrac_index_hit_rate"]),
                    str(r["pack_hit_any_inclusive_rate"]),
                    str(r["pack_only_hit_any_inclusive_rate"]),
                    str(r["filler_hit_any_inclusive_rate"]),
                    str(r["pack_vtrac_index_hit_rate"]),
                    str(r["avg_vtrac_pack_size"]),
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
