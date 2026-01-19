#!/usr/bin/env python3
"""
Hot Zones weight sweep harness (reporting-only).

Purpose
-------
Quantify whether small Hot Zones weight changes (especially `w_vt_only_lane_bonus`) move
winners into the top-K list *without* “winning by widening”.

This script:
- Reads frozen sharepack JSON tables: `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`
- Reads official results: `data/results/<D>.txt`
- Re-runs the Hot Zones scanner using the current engine code under multiple weight variants
- Writes CSV + Markdown to RUNS (no sharepack writes; no analyzer changes)

Default intent (HOTZ-003):
- Sweep `w_vt_only_lane_bonus` across a small range (0.8 baseline, 0.9, 1.0, 1.1)
- Measure top-K presence + rank movement, with explicit vt-only visibility and guard attribution
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


from alpha_analytical.control_center.batch_runner import parse_winner_sheet  # noqa: E402
from alpha_analytical.hot_zones import (  # noqa: E402
    HotScanConfig,
    HotZoneScanner,
    HotZoneWeights,
    load_table_env_from_json,
)

import modules.vtrac_reference as vr  # noqa: E402


DEFAULT_STATES: List[str] = [
    "Connecticut4",
    "Delaware4",
    "Florida4",
    "Indiana4",
    "Michigan4",
    "NewJersey4",
    "NewYork4",
    "NorthCarolina4",
    "Ohio4",
    "OntarioCanada4",
    "Pennsylvania4",
    "PuertoRico4",
    "SouthCarolina4",
    "Virginia4",
]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _canon(value: str) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if len(digits) != 3:
        return ""
    return "".join(sorted(digits))


def _iter_dates(start: str, end: str) -> List[str]:
    a = datetime.strptime(start, "%Y-%m-%d")
    b = datetime.strptime(end, "%Y-%m-%d")
    if b < a:
        a, b = b, a
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return out


def _parse_csv_floats(values: Sequence[str]) -> List[float]:
    out: List[float] = []
    for v in values:
        if v is None:
            continue
        s = str(v).strip()
        if not s:
            continue
        # allow comma-separated lists passed as a single token
        parts = [p.strip() for p in s.split(",") if p.strip()]
        for p in parts:
            try:
                out.append(float(p))
            except Exception:
                raise SystemExit(f"Invalid float value: {p!r}")
    return out


def _read_results_winners(results_date: str) -> Dict[str, Dict[str, str]]:
    """
    Return: project_state -> {"Midday": "123", "Evening": "456"} (as available).
    """
    results_path = REPO_ROOT / "data" / "results" / f"{results_date}.txt"
    if not results_path.exists():
        return {}
    entries = parse_winner_sheet(results_path.read_text(encoding="utf-8", errors="replace"))
    out: Dict[str, Dict[str, str]] = {}
    for e in entries:
        if not e.project_state:
            continue
        m: Dict[str, str] = {}
        if e.midday:
            m["Midday"] = e.midday
        if e.evening:
            m["Evening"] = e.evening
        if m:
            out[e.project_state] = m
    return out


def _json_tables_path(day_dir: Path, state: str) -> Path:
    return day_dir / state / "json" / f"{state}_tables.json"


def _hz_scan_from_sharepack(*, day_dir: Path, state: str, weights: HotZoneWeights) -> Tuple[List[object], List[object]]:
    json_path = _json_tables_path(day_dir, state)
    env = load_table_env_from_json(json_path)
    scanner = HotZoneScanner(env, HotScanConfig(), weights)
    return scanner.scan()


@dataclass(frozen=True)
class WeightVariant:
    label: str
    weights: HotZoneWeights


@dataclass
class WinnerMetrics:
    winner_present: bool
    winner_rank: Optional[int]
    winner_rank_fraction: Optional[float]
    in_top8: bool
    in_top12: bool
    in_top20: bool
    winner_score_max: Optional[float]
    winner_score_mean: Optional[float]
    delta_to_top: Optional[float]
    has_straight_evidence: bool
    vt_only_any: bool
    vt_only_visible: bool
    guard_attributed: bool
    triads_total: int
    top_score_max: Optional[float]
    pool_within_1: Optional[int]
    pool_within_2: Optional[int]
    pool_within_3: Optional[int]


def _pool_counts_by_delta(tops: Sequence[object]) -> Tuple[Optional[float], Optional[int], Optional[int], Optional[int]]:
    if not tops:
        return None, None, None, None
    # TopCandidateRow has score_max
    top_score = float(getattr(tops[0], "score_max", 0.0) or 0.0)
    within_1 = sum(1 for t in tops if float(getattr(t, "score_max", 0.0) or 0.0) >= top_score - 1.0)
    within_2 = sum(1 for t in tops if float(getattr(t, "score_max", 0.0) or 0.0) >= top_score - 2.0)
    within_3 = sum(1 for t in tops if float(getattr(t, "score_max", 0.0) or 0.0) >= top_score - 3.0)
    return top_score, within_1, within_2, within_3


def _compute_winner_metrics(
    *,
    outcome: str,
    winner_literal: str,
    per_items: Sequence[object],
    tops: Sequence[object],
) -> WinnerMetrics:
    canon = _canon(winner_literal)
    triads_total = len(tops)

    top_score, within_1, within_2, within_3 = _pool_counts_by_delta(tops)

    # Determine evidence-type visibility from per-item rows.
    vt_only_any = False
    has_straight_evidence = False
    guard_hits = 0
    for row in per_items:
        if getattr(row, "triad", "") != canon:
            continue
        vt_only_any = vt_only_any or bool(int(getattr(row, "vt_only_lane", 0) or 0))
        has_straight_evidence = has_straight_evidence or bool(int(getattr(row, "has_straight", 0) or 0))
        guard_hits += int(getattr(row, "guard_injected", 0) or 0)

    # Spec says: vt-only visibility even if no literal straight.
    vt_only_only = bool(vt_only_any and not has_straight_evidence)

    # Rank winner in top list.
    winner_rank: Optional[int] = None
    winner_score_max: Optional[float] = None
    winner_score_mean: Optional[float] = None
    winner_guard_attrib = False
    for i, t in enumerate(tops, start=1):
        if getattr(t, "triad", "") != canon:
            continue
        winner_rank = i
        winner_score_max = float(getattr(t, "score_max", 0.0) or 0.0)
        winner_score_mean = float(getattr(t, "score_mean", 0.0) or 0.0)
        winner_guard_attrib = bool(int(getattr(t, "guard_hits", 0) or 0))
        break

    winner_present = winner_rank is not None
    winner_rank_fraction = (winner_rank / triads_total) if (winner_rank and triads_total > 0) else None

    in_top8 = bool(winner_rank and winner_rank <= 8)
    in_top12 = bool(winner_rank and winner_rank <= 12)
    in_top20 = bool(winner_rank and winner_rank <= 20)

    delta_to_top = None
    if top_score is not None and winner_score_max is not None:
        delta_to_top = float(top_score - winner_score_max)

    return WinnerMetrics(
        winner_present=winner_present,
        winner_rank=winner_rank,
        winner_rank_fraction=winner_rank_fraction,
        in_top8=in_top8,
        in_top12=in_top12,
        in_top20=in_top20,
        winner_score_max=winner_score_max,
        winner_score_mean=winner_score_mean,
        delta_to_top=delta_to_top,
        has_straight_evidence=has_straight_evidence,
        vt_only_any=vt_only_any,
        vt_only_visible=vt_only_only,
        guard_attributed=bool(winner_guard_attrib or (guard_hits > 0)),
        triads_total=triads_total,
        top_score_max=top_score,
        pool_within_1=within_1,
        pool_within_2=within_2,
        pool_within_3=within_3,
    )


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def _fmt_float(v: Optional[float], *, places: int = 3) -> str:
    if v is None:
        return ""
    return f"{v:.{places}f}"


def _fmt_int(v: Optional[int]) -> str:
    return "" if v is None else str(int(v))


def _truthy(v: object) -> bool:
    return bool(v)


def main() -> None:
    ap = argparse.ArgumentParser(description="Hot Zones weight sweep harness (reporting-only).")
    ap.add_argument(
        "--sharepacks-root",
        default=str(REPO_ROOT / "sharepacks"),
        help="Sharepacks root directory (default: sharepacks/)",
    )
    ap.add_argument("--date", action="append", default=[], help="Results date D (repeatable).")
    ap.add_argument("--start-date", default=None, help="Start date (YYYY-MM-DD) for an inclusive range.")
    ap.add_argument("--end-date", default=None, help="End date (YYYY-MM-DD) for an inclusive range.")
    ap.add_argument("--states", nargs="*", default=None, help="Optional subset of states (default: tracked list).")
    ap.add_argument(
        "--vt-only-bonus",
        nargs="*",
        default=["0.8", "0.9", "1.0", "1.1"],
        help="Sweep values for w_vt_only_lane_bonus (comma-separated or repeated; default: 0.8,0.9,1.0,1.1).",
    )
    ap.add_argument(
        "--col1-arrival",
        nargs="*",
        default=[],
        help=(
            "Optional sweep values for w_col1_arrival (comma-separated or repeated). "
            "If omitted, uses the HotZoneWeights default (no sweep)."
        ),
    )
    ap.add_argument(
        "--runs-dir",
        default=str(_runs_dir()),
        help="RUNS directory (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS).",
    )
    ap.add_argument(
        "--out-prefix",
        default="HOT_ZONES_V0__WEIGHT_SWEEP",
        help="Output filename prefix under RUNS when --out-csv/--out-md are not provided (default: HOT_ZONES_V0__WEIGHT_SWEEP).",
    )
    ap.add_argument("--out-csv", default=None, help="Override output CSV path.")
    ap.add_argument("--out-md", default=None, help="Override output Markdown path.")
    args = ap.parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    runs_dir = Path(args.runs_dir)
    if not runs_dir.is_absolute():
        runs_dir = (REPO_ROOT / runs_dir).resolve()
    runs_dir.mkdir(parents=True, exist_ok=True)

    dates: List[str] = [d.strip() for d in (args.date or []) if str(d).strip()]
    if args.start_date and args.end_date:
        dates.extend(_iter_dates(args.start_date.strip(), args.end_date.strip()))
    dates = sorted(set(dates))
    if not dates:
        raise SystemExit("Provide --date (repeatable) or --start-date + --end-date.")

    states: List[str] = list(args.states) if args.states else list(DEFAULT_STATES)

    vt_only_bonuses = _parse_csv_floats(args.vt_only_bonus)
    if not vt_only_bonuses:
        raise SystemExit("Invalid --vt-only-bonus: empty list")

    base_weights = HotZoneWeights()
    col1_arrivals = _parse_csv_floats(args.col1_arrival)
    if not col1_arrivals:
        col1_arrivals = [float(base_weights.w_col1_arrival)]

    variants: List[WeightVariant] = []
    baseline_label = f"vt_only={base_weights.w_vt_only_lane_bonus:g},col1={base_weights.w_col1_arrival:g}"
    variants.append(WeightVariant(label=baseline_label, weights=base_weights))
    for b in vt_only_bonuses:
        for c in col1_arrivals:
            if float(b) == float(base_weights.w_vt_only_lane_bonus) and float(c) == float(base_weights.w_col1_arrival):
                continue
            w = HotZoneWeights()
            w.w_vt_only_lane_bonus = float(b)
            w.w_col1_arrival = float(c)
            variants.append(WeightVariant(label=f"vt_only={b:g},col1={c:g}", weights=w))

    window_label = f"{dates[0]}_to_{dates[-1]}" if len(dates) > 1 else dates[0]
    out_csv = (
        Path(args.out_csv)
        if args.out_csv
        else runs_dir / f"{args.out_prefix}__{window_label}.csv"
    )
    out_md = (
        Path(args.out_md)
        if args.out_md
        else runs_dir / f"{args.out_prefix}__{window_label}.md"
    )

    # Collect results.
    rows: List[Dict[str, object]] = []
    baseline_rank: Dict[Tuple[str, str, str], Optional[int]] = {}

    for date in dates:
        day_dir = sharepacks_root / date
        if not day_dir.exists():
            continue
        winners_map = _read_results_winners(date)
        for state in states:
            json_path = _json_tables_path(day_dir, state)
            if not json_path.exists():
                continue
            winners = winners_map.get(state) or {}
            state_winners: Dict[str, str] = {}
            for outcome in ("Midday", "Evening"):
                winner_literal = str(winners.get(outcome) or "").strip()
                if winner_literal:
                    state_winners[outcome] = winner_literal
            if not state_winners:
                continue

            # Hot Zones scanning is global across sections; scan once per weight variant and grade both outcomes.
            for variant in variants:
                per_items, tops = _hz_scan_from_sharepack(day_dir=day_dir, state=state, weights=variant.weights)
                for outcome, winner_literal in state_winners.items():
                    winner_canon = _canon(winner_literal)
                    winner_idx = vr.get_vtrac_index(winner_literal)
                    key = (date, state, outcome)
                    wm = _compute_winner_metrics(
                        outcome=outcome,
                        winner_literal=winner_literal,
                        per_items=per_items,
                        tops=tops,
                    )

                    def index_hit_topk(k: int) -> bool:
                        if winner_idx is None:
                            return False
                        target = int(winner_idx)
                        for t in tops[:k]:
                            triad = str(getattr(t, "triad", "") or "")
                            idx = vr.get_vtrac_index(triad)
                            if idx is None:
                                continue
                            if int(idx) == target:
                                return True
                        return False

                    idx_hit8 = index_hit_topk(8)
                    idx_hit12 = index_hit_topk(12)
                    idx_hit20 = index_hit_topk(20)
                    idx_hit_only8 = bool(idx_hit8 and not wm.in_top8)
                    idx_hit_only12 = bool(idx_hit12 and not wm.in_top12)
                    idx_hit_only20 = bool(idx_hit20 and not wm.in_top20)
                    if variant.label == baseline_label:
                        baseline_rank[key] = wm.winner_rank

                    rows.append(
                        {
                            "results_date": date,
                            "state": state,
                            "outcome": outcome,
                            "weights": variant.label,
                            "w_vt_only_lane_bonus": _fmt_float(variant.weights.w_vt_only_lane_bonus, places=2),
                            "w_col1_arrival": _fmt_float(variant.weights.w_col1_arrival, places=2),
                            "winner": winner_literal,
                            "winner_canon": winner_canon,
                            "winner_vtrac_index": "" if winner_idx is None else str(int(winner_idx)),
                            "triads_total": wm.triads_total,
                            "winner_present": "1" if wm.winner_present else "0",
                            "winner_rank": _fmt_int(wm.winner_rank),
                            "winner_rank_fraction": _fmt_float(wm.winner_rank_fraction),
                            "winner_in_top8": "1" if wm.in_top8 else "0",
                            "winner_in_top12": "1" if wm.in_top12 else "0",
                            "winner_in_top20": "1" if wm.in_top20 else "0",
                            "vtrac_index_hit_top8": "1" if idx_hit8 else "0",
                            "vtrac_index_hit_top12": "1" if idx_hit12 else "0",
                            "vtrac_index_hit_top20": "1" if idx_hit20 else "0",
                            "vtrac_index_hit_only_top8": "1" if idx_hit_only8 else "0",
                            "vtrac_index_hit_only_top12": "1" if idx_hit_only12 else "0",
                            "vtrac_index_hit_only_top20": "1" if idx_hit_only20 else "0",
                            "winner_score_max": _fmt_float(wm.winner_score_max),
                            "winner_score_mean": _fmt_float(wm.winner_score_mean),
                            "delta_to_top": _fmt_float(wm.delta_to_top),
                            "has_straight_evidence": "1" if wm.has_straight_evidence else "0",
                            "vt_only_any": "1" if wm.vt_only_any else "0",
                            "vt_only_visible": "1" if wm.vt_only_visible else "0",
                            "guard_attributed": "1" if wm.guard_attributed else "0",
                            "top_score_max": _fmt_float(wm.top_score_max),
                            "pool_within_1": _fmt_int(wm.pool_within_1),
                            "pool_within_2": _fmt_int(wm.pool_within_2),
                            "pool_within_3": _fmt_int(wm.pool_within_3),
                        }
                    )

    if not rows:
        raise SystemExit("No rows produced (no matching sharepacks/results found for given dates/states).")

    # Add delta columns vs baseline.
    for r in rows:
        key = (str(r.get("results_date") or ""), str(r.get("state") or ""), str(r.get("outcome") or ""))
        base = baseline_rank.get(key)
        try:
            cur = int(str(r.get("winner_rank") or "")) if str(r.get("winner_rank") or "").strip() else None
        except Exception:
            cur = None
        r["baseline_rank"] = "" if base is None else str(base)
        if base is None or cur is None:
            r["delta_rank_vs_baseline"] = ""
        else:
            r["delta_rank_vs_baseline"] = str(base - cur)

    _write_csv(
        out_csv,
        fieldnames=[
            "results_date",
            "state",
            "outcome",
            "weights",
            "w_vt_only_lane_bonus",
            "w_col1_arrival",
            "winner",
            "winner_canon",
            "winner_vtrac_index",
            "triads_total",
            "winner_present",
            "winner_rank",
            "baseline_rank",
            "delta_rank_vs_baseline",
            "winner_rank_fraction",
            "winner_in_top8",
            "winner_in_top12",
            "winner_in_top20",
            "vtrac_index_hit_top8",
            "vtrac_index_hit_top12",
            "vtrac_index_hit_top20",
            "vtrac_index_hit_only_top8",
            "vtrac_index_hit_only_top12",
            "vtrac_index_hit_only_top20",
            "winner_score_max",
            "winner_score_mean",
            "delta_to_top",
            "has_straight_evidence",
            "vt_only_any",
            "vt_only_visible",
            "guard_attributed",
            "top_score_max",
            "pool_within_1",
            "pool_within_2",
            "pool_within_3",
        ],
        rows=rows,
    )

    # Build Markdown summary.
    # Aggregate by weight label.
    by_weight: Dict[str, Dict[str, int]] = {}
    by_weight_rank_delta_sum: Dict[str, int] = {}
    by_weight_rank_delta_n: Dict[str, int] = {}
    by_weight_rank_delta_sum_vt_only: Dict[str, int] = {}
    by_weight_rank_delta_n_vt_only: Dict[str, int] = {}
    by_weight_rank_delta_sum_vt_any: Dict[str, int] = {}
    by_weight_rank_delta_n_vt_any: Dict[str, int] = {}

    for r in rows:
        w = str(r.get("weights") or "")
        agg = by_weight.setdefault(w, {})
        agg.setdefault("rows", 0)
        agg.setdefault("top8", 0)
        agg.setdefault("top12", 0)
        agg.setdefault("top20", 0)
        agg.setdefault("idx_top8", 0)
        agg.setdefault("idx_top12", 0)
        agg.setdefault("idx_top20", 0)
        agg.setdefault("idx_only_top8", 0)
        agg.setdefault("idx_only_top12", 0)
        agg.setdefault("idx_only_top20", 0)
        agg.setdefault("vt_only_rows", 0)
        agg.setdefault("vt_only_top8", 0)
        agg.setdefault("vt_only_top12", 0)
        agg.setdefault("vt_only_top20", 0)
        agg.setdefault("vt_any_rows", 0)
        agg.setdefault("vt_any_top8", 0)
        agg.setdefault("vt_any_top12", 0)
        agg.setdefault("vt_any_top20", 0)

        vt_any_flag = str(r.get("vt_only_any") or "").strip() == "1"
        vt_only_flag = str(r.get("vt_only_visible") or "").strip() == "1"  # vt_only AND no straight evidence
        in8 = str(r.get("winner_in_top8") or "").strip() == "1"
        in12 = str(r.get("winner_in_top12") or "").strip() == "1"
        in20 = str(r.get("winner_in_top20") or "").strip() == "1"
        idx8 = str(r.get("vtrac_index_hit_top8") or "").strip() == "1"
        idx12 = str(r.get("vtrac_index_hit_top12") or "").strip() == "1"
        idx20 = str(r.get("vtrac_index_hit_top20") or "").strip() == "1"
        idx_only8 = str(r.get("vtrac_index_hit_only_top8") or "").strip() == "1"
        idx_only12 = str(r.get("vtrac_index_hit_only_top12") or "").strip() == "1"
        idx_only20 = str(r.get("vtrac_index_hit_only_top20") or "").strip() == "1"

        agg["rows"] += 1
        agg["top8"] += 1 if in8 else 0
        agg["top12"] += 1 if in12 else 0
        agg["top20"] += 1 if in20 else 0
        agg["idx_top8"] += 1 if idx8 else 0
        agg["idx_top12"] += 1 if idx12 else 0
        agg["idx_top20"] += 1 if idx20 else 0
        agg["idx_only_top8"] += 1 if idx_only8 else 0
        agg["idx_only_top12"] += 1 if idx_only12 else 0
        agg["idx_only_top20"] += 1 if idx_only20 else 0
        if vt_any_flag:
            agg["vt_any_rows"] += 1
            agg["vt_any_top8"] += 1 if in8 else 0
            agg["vt_any_top12"] += 1 if in12 else 0
            agg["vt_any_top20"] += 1 if in20 else 0
        if vt_only_flag:
            agg["vt_only_rows"] += 1
            agg["vt_only_top8"] += 1 if in8 else 0
            agg["vt_only_top12"] += 1 if in12 else 0
            agg["vt_only_top20"] += 1 if in20 else 0

        # Average delta_rank vs baseline (positive is improvement).
        dr = str(r.get("delta_rank_vs_baseline") or "").strip()
        if dr and dr.lstrip("-").isdigit():
            by_weight_rank_delta_sum[w] = by_weight_rank_delta_sum.get(w, 0) + int(dr)
            by_weight_rank_delta_n[w] = by_weight_rank_delta_n.get(w, 0) + 1
            if vt_only_flag:
                by_weight_rank_delta_sum_vt_only[w] = by_weight_rank_delta_sum_vt_only.get(w, 0) + int(dr)
                by_weight_rank_delta_n_vt_only[w] = by_weight_rank_delta_n_vt_only.get(w, 0) + 1
            if vt_any_flag:
                by_weight_rank_delta_sum_vt_any[w] = by_weight_rank_delta_sum_vt_any.get(w, 0) + int(dr)
                by_weight_rank_delta_n_vt_any[w] = by_weight_rank_delta_n_vt_any.get(w, 0) + 1

    def rate(n: int, d: int) -> str:
        return "" if d == 0 else f"{(n / d):.3f}"

    md_lines: List[str] = []
    md_lines.append("# Hot Zones — Weight Sweep (HOTZ-003 harness)\n")
    md_lines.append("Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.\n")
    md_lines.append("## Inputs\n")
    md_lines.append(f"- Sharepacks root: `{_safe_rel(sharepacks_root)}`")
    md_lines.append(f"- Dates: `{dates[0]}` → `{dates[-1]}` ({len(dates)} days requested)")
    md_lines.append(f"- States (requested): {len(states)}")
    md_lines.append(
        f"- Sweep: `w_vt_only_lane_bonus` = {', '.join(f'{b:g}' for b in vt_only_bonuses)}; "
        f"`w_col1_arrival` = {', '.join(f'{c:g}' for c in col1_arrivals)} (baseline={baseline_label})\n"
    )
    md_lines.append("## Summary (all winners; winner canonical in top-K)\n")
    md_lines.append("| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |")
    md_lines.append("|---|---:|---:|---:|---:|---:|")
    for w in variants:
        a = by_weight.get(w.label, {})
        rows_n = int(a.get("rows", 0))
        top8 = int(a.get("top8", 0))
        top12 = int(a.get("top12", 0))
        top20 = int(a.get("top20", 0))
        dsum = by_weight_rank_delta_sum.get(w.label, 0)
        dn = by_weight_rank_delta_n.get(w.label, 0)
        avg_delta = (dsum / dn) if dn else None
        md_lines.append(
            f"| {w.label} | {rows_n} | {rate(top8, rows_n)} | {rate(top12, rows_n)} | {rate(top20, rows_n)} | {_fmt_float(avg_delta)} |"
        )

    md_lines.append("\n## VTRAC index hit (winner index present in top-K)\n")
    md_lines.append("| Weights | Rows | Top8% | Top12% | Top20% |")
    md_lines.append("|---|---:|---:|---:|---:|")
    for w in variants:
        a = by_weight.get(w.label, {})
        rows_n = int(a.get("rows", 0))
        top8 = int(a.get("idx_top8", 0))
        top12 = int(a.get("idx_top12", 0))
        top20 = int(a.get("idx_top20", 0))
        md_lines.append(f"| {w.label} | {rows_n} | {rate(top8, rows_n)} | {rate(top12, rows_n)} | {rate(top20, rows_n)} |")

    md_lines.append("\n## VTRAC index hit only (index present but winner canonical not in top-K)\n")
    md_lines.append("| Weights | Rows | Top8% | Top12% | Top20% |")
    md_lines.append("|---|---:|---:|---:|---:|")
    for w in variants:
        a = by_weight.get(w.label, {})
        rows_n = int(a.get("rows", 0))
        top8 = int(a.get("idx_only_top8", 0))
        top12 = int(a.get("idx_only_top12", 0))
        top20 = int(a.get("idx_only_top20", 0))
        md_lines.append(f"| {w.label} | {rows_n} | {rate(top8, rows_n)} | {rate(top12, rows_n)} | {rate(top20, rows_n)} |")

    md_lines.append("\n## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)\n")
    md_lines.append("| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |")
    md_lines.append("|---|---:|---:|---:|---:|---:|")
    for w in variants:
        a = by_weight.get(w.label, {})
        vt_rows = int(a.get("vt_only_rows", 0))
        vt_top8 = int(a.get("vt_only_top8", 0))
        vt_top12 = int(a.get("vt_only_top12", 0))
        vt_top20 = int(a.get("vt_only_top20", 0))
        dsum = by_weight_rank_delta_sum_vt_only.get(w.label, 0)
        dn = by_weight_rank_delta_n_vt_only.get(w.label, 0)
        avg_delta = (dsum / dn) if dn else None
        md_lines.append(
            f"| {w.label} | {vt_rows} | {rate(vt_top8, vt_rows)} | {rate(vt_top12, vt_rows)} | {rate(vt_top20, vt_rows)} | {_fmt_float(avg_delta)} |"
        )

    md_lines.append("\n## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)\n")
    md_lines.append("| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |")
    md_lines.append("|---|---:|---:|---:|---:|---:|")
    for w in variants:
        a = by_weight.get(w.label, {})
        vt_rows = int(a.get("vt_any_rows", 0))
        vt_top8 = int(a.get("vt_any_top8", 0))
        vt_top12 = int(a.get("vt_any_top12", 0))
        vt_top20 = int(a.get("vt_any_top20", 0))
        dsum = by_weight_rank_delta_sum_vt_any.get(w.label, 0)
        dn = by_weight_rank_delta_n_vt_any.get(w.label, 0)
        avg_delta = (dsum / dn) if dn else None
        md_lines.append(
            f"| {w.label} | {vt_rows} | {rate(vt_top8, vt_rows)} | {rate(vt_top12, vt_rows)} | {rate(vt_top20, vt_rows)} | {_fmt_float(avg_delta)} |"
        )

    md_lines.append("\n## Outputs\n")
    md_lines.append(f"- CSV: `{_safe_rel(out_csv)}`")
    md_lines.append(f"- MD: `{_safe_rel(out_md)}`\n")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
