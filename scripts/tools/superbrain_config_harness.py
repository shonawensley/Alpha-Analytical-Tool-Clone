#!/usr/bin/env python3
"""
Superbrain Config Harness (v0.2 selection-layer research)

Goal
----
Compare cross-state ("Brain-2") triage/ranking policies across gold windows without touching analyzers.

This harness answers:
- If we only look at the top N ranked states each day, how often do we cover the winner?
- How do different ranking policies trade off `hit_any` vs `box_hit` visibility?
- Does Aux badge pressure (index-density) help as a triage tie-breaker?

Predictive safety posture
------------------------
- Reads predictive sharepacks as the pre-results evidence snapshot: sharepacks/_predictive/<D>/...
- Uses results only for grading (data/results/<D>.txt)
- Writes outputs only to RUNS.

Inputs
------
- Candidate Universe: sharepacks/_predictive/<D>/<STATE>/candidate_universe__<profile>.json
- Play Card:         sharepacks/_predictive/<D>/<STATE>/play_card__<profile>.json
- Aux pressure rows (optional, precomputed): RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__<A>_to_<B>.csv

Outputs
-------
- RUNS/SUPERBRAIN_CONFIG__HARNESS__<A>_to_<B>.{md,csv}
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import date as date_mod
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    d = _normalize_pick3(draw)
    return "".join(sorted(d)) if d else ""


def _list_dates(start_date: str, end_date: str) -> List[str]:
    a = date_mod.fromisoformat(start_date)
    b = date_mod.fromisoformat(end_date)
    if b < a:
        raise SystemExit(f"--end-date must be >= --start-date (got {start_date}..{end_date})")
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


@dataclass(frozen=True)
class Winners:
    midday: str
    evening: str


def _load_results_winners(results_file: Path) -> Dict[str, Winners]:
    if not results_file.exists():
        return {}
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    text = _read_text(results_file)
    entries = parse_winner_sheet(text)

    winners: Dict[str, Winners] = {}
    for entry in entries:
        canonical = getattr(entry, "canonical", None)
        midday = getattr(entry, "midday", None)
        evening = getattr(entry, "evening", None)
        if not canonical:
            continue
        candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
        if not candidates:
            project_state = getattr(entry, "project_state", None)
            candidates = (project_state,) if project_state else ()
        for state_key in candidates:
            if not state_key:
                continue
            winners[state_key] = Winners(
                midday=_normalize_pick3(midday or ""),
                evening=_normalize_pick3(evening or ""),
            )
    return winners


@dataclass(frozen=True)
class PressureSummary:
    top_k: int
    midday_top: List[int]
    evening_top: List[int]
    intersection: List[int]
    midday_sum: float
    evening_sum: float
    intersection_sum: float

    @property
    def pressure_sum(self) -> float:
        return self.midday_sum + self.evening_sum


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _find_pressure_index_stats(*, start_date: str, end_date: str) -> Optional[Path]:
    runs_dir = _runs_dir()
    cand = runs_dir / f"AUX_BADGE_PRESSURE__INDEX_STATS__{start_date}_to_{end_date}.csv"
    return cand if cand.exists() else None


def _build_pressure_lookup(rows: Sequence[Dict[str, str]]) -> Dict[Tuple[str, str, str], List[Dict[str, str]]]:
    out: Dict[Tuple[str, str, str], List[Dict[str, str]]] = {}
    for r in rows:
        date = (r.get("date") or "").strip()
        state = (r.get("state_key") or "").strip()
        variant = (r.get("variant") or "").strip().lower()
        if not date or not state or variant not in {"midday", "evening"}:
            continue
        out.setdefault((date, state, variant), []).append(r)
    return out


def _pressure_summary_for_state_day(
    lookup: Dict[Tuple[str, str, str], List[Dict[str, str]]],
    *,
    date: str,
    state_key: str,
    top_k: int,
) -> PressureSummary:
    def _top_indices(variant: str) -> Tuple[List[int], float, Dict[int, float]]:
        rows = lookup.get((date, state_key, variant), [])
        scored: List[Tuple[float, int]] = []
        density_by_index: Dict[int, float] = {}
        for r in rows:
            try:
                idx = int(r.get("vtrac_index") or "")
            except Exception:
                continue
            try:
                dens = float(r.get("pressure_density") or 0.0)
            except Exception:
                dens = 0.0
            scored.append((dens, idx))
            density_by_index[idx] = max(density_by_index.get(idx, float("-inf")), dens)
        scored.sort(key=lambda t: (t[0], -t[1]), reverse=True)
        picked = [idx for _, idx in scored[: max(0, int(top_k))] if isinstance(idx, int)]
        sum_dens = sum(float(density_by_index.get(i, 0.0) or 0.0) for i in picked)
        return picked, sum_dens, density_by_index

    m_top, m_sum, m_d = _top_indices("midday")
    e_top, e_sum, e_d = _top_indices("evening")
    inter = sorted(set(m_top).intersection(e_top))
    inter_sum = sum(min(float(m_d.get(i, 0.0) or 0.0), float(e_d.get(i, 0.0) or 0.0)) for i in inter)
    return PressureSummary(
        top_k=int(top_k),
        midday_top=m_top,
        evening_top=e_top,
        intersection=inter,
        midday_sum=round(m_sum, 6),
        evening_sum=round(e_sum, 6),
        intersection_sum=round(inter_sum, 6),
    )


@dataclass(frozen=True)
class CandidateSummary:
    packs_count: int
    union_count: int
    due_doubles_count: int
    top_support_count: int


def _candidate_summary(cu: Dict[str, Any]) -> CandidateSummary:
    packs = cu.get("packs") if isinstance(cu.get("packs"), list) else []
    union_count = cu.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union_list = cu.get("union_combos") if isinstance(cu.get("union_combos"), list) else []
        union_count_int = len(union_list)

    dd_canon: set[str] = set()
    support: Dict[str, int] = {}
    for p in packs:
        if not isinstance(p, dict):
            continue
        method_id = str(p.get("method_id") or "")
        canonicals = p.get("canonicals") if isinstance(p.get("canonicals"), list) else []
        uniq: set[str] = set()
        for c in canonicals:
            cc = _canon(str(c))
            if cc:
                uniq.add(cc)
        for cc in uniq:
            support[cc] = support.get(cc, 0) + 1
        if method_id == "due_doubles":
            dd_canon.update(uniq)
    top_support = max(support.values(), default=0)
    return CandidateSummary(
        packs_count=len(packs),
        union_count=int(union_count_int),
        due_doubles_count=len(dd_canon),
        top_support_count=int(top_support),
    )


def _union_hits(cu: Dict[str, Any], *, winner: str) -> Dict[str, bool]:
    packs = cu.get("packs") if isinstance(cu.get("packs"), list) else []
    union_combos = cu.get("union_combos") if isinstance(cu.get("union_combos"), list) else []
    union_combos_norm = {_normalize_pick3(x) for x in union_combos if _normalize_pick3(x)}

    union_box_canonicals: set[str] = set()
    for p in packs:
        if not isinstance(p, dict):
            continue
        canonicals = p.get("canonicals") if isinstance(p.get("canonicals"), list) else []
        union_box_canonicals.update({_canon(str(x)) for x in canonicals if _canon(str(x))})

    w = _normalize_pick3(winner)
    if not w:
        return {"hit_any": False, "straight_hit": False, "box_hit": False}
    w_canon = _canon(w)
    straight_hit = w in union_combos_norm
    box_hit = bool(w_canon and w_canon in union_box_canonicals)
    return {"hit_any": bool(straight_hit or box_hit), "straight_hit": straight_hit, "box_hit": box_hit}


def _play_card_hits(play_card: Dict[str, Any], *, winner: str, strategy: str, budget: str) -> Dict[str, bool]:
    strategies = play_card.get("strategies") if isinstance(play_card.get("strategies"), dict) else {}
    strat = strategies.get(strategy) if isinstance(strategies.get(strategy), dict) else {}
    card = strat.get(budget) if isinstance(strat.get(budget), dict) else {}

    combos_raw = card.get("combos") if isinstance(card.get("combos"), list) else []
    combos = {_normalize_pick3(x) for x in combos_raw if _normalize_pick3(x)}
    boxed_raw = card.get("boxed_canonicals") if isinstance(card.get("boxed_canonicals"), list) else []
    boxed = {_canon(str(x)) for x in boxed_raw if _canon(str(x))}

    w = _normalize_pick3(winner)
    if not w:
        return {"hit_any": False, "straight_hit": False, "box_hit": False}
    w_canon = _canon(w)
    straight_hit = w in combos
    box_hit = bool(w_canon and w_canon in boxed)
    return {"hit_any": bool(straight_hit or box_hit), "straight_hit": straight_hit, "box_hit": box_hit}


@dataclass
class StateRow:
    date: str
    state_key: str
    cu: CandidateSummary
    pressure: PressureSummary
    cu_mid: Dict[str, bool]
    cu_eve: Dict[str, bool]
    pc_mid: Dict[str, bool]
    pc_eve: Dict[str, bool]


def _rank_key(config: str, row: StateRow) -> Tuple:
    # Baseline matches create_predictive_portfolio_report.py tool_first sorting.
    if config == "baseline_tool_first":
        return (
            -int(row.cu.top_support_count),
            int(row.cu.union_count),
            -int(row.cu.due_doubles_count),
            -int(row.cu.packs_count),
            str(row.state_key),
        )

    # Pressure is a tiebreaker/gate: prefer cross-variant intersection first.
    if config == "pressure_tiebreak":
        return (
            -int(row.cu.top_support_count),
            -int(len(row.pressure.intersection)),
            -float(row.pressure.intersection_sum),
            -float(row.pressure.pressure_sum),
            int(row.cu.union_count),
            -int(row.cu.due_doubles_count),
            -int(row.cu.packs_count),
            str(row.state_key),
        )

    raise ValueError(f"Unknown config: {config}")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Superbrain config harness (cross-state triage policy comparison).")
    ap.add_argument("--start-date", required=True, help="Results/sharepack date A (YYYY-MM-DD)")
    ap.add_argument("--end-date", required=True, help="Results/sharepack date B (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Profile suffix for candidate_universe/play_card inputs (default: tool_only).",
    )
    ap.add_argument(
        "--top-n-states",
        type=int,
        default=4,
        help="Evaluate 'top N ranked states per day' (default: 4).",
    )
    ap.add_argument(
        "--pressure-top-k",
        type=int,
        default=5,
        help="Top K indices per variant for pressure features (default: 5).",
    )
    ap.add_argument(
        "--configs",
        nargs="+",
        default=["baseline_tool_first", "pressure_tiebreak"],
        help="Configs to compare (default: baseline_tool_first pressure_tiebreak).",
    )
    ap.add_argument(
        "--pressure-index-stats",
        default=None,
        help="Optional override path to AUX_BADGE_PRESSURE__INDEX_STATS__<A>_to_<B>.csv",
    )
    ap.add_argument("--out-md", default=None, help="Override output MD path (default: RUNS/SUPERBRAIN_CONFIG__HARNESS__<A>_to_<B>.md)")
    ap.add_argument("--out-csv", default=None, help="Override output CSV path (default: RUNS/SUPERBRAIN_CONFIG__HARNESS__<A>_to_<B>.csv)")
    ap.add_argument(
        "--play-card-strategy",
        default="play_box_first",
        help="Play Card strategy key to grade (default: play_box_first). Example: conversion_box_first.",
    )
    ap.add_argument("--play-card-budget", default="B12", help="Play Card budget key to grade (default: B12).")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    dates = _list_dates(args.start_date, args.end_date)
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_md = Path(args.out_md) if args.out_md else (runs_dir / f"SUPERBRAIN_CONFIG__HARNESS__{args.start_date}_to_{args.end_date}.md")
    out_csv = Path(args.out_csv) if args.out_csv else (runs_dir / f"SUPERBRAIN_CONFIG__HARNESS__{args.start_date}_to_{args.end_date}.csv")
    if (out_md.exists() or out_csv.exists()) and not args.force:
        raise SystemExit(f"Refusing to overwrite existing outputs (use --force): {_safe_rel(out_md)} / {_safe_rel(out_csv)}")

    # Pressure index stats (optional but recommended).
    pressure_path = Path(args.pressure_index_stats) if args.pressure_index_stats else _find_pressure_index_stats(
        start_date=args.start_date, end_date=args.end_date
    )
    pressure_rows: List[Dict[str, str]] = []
    if pressure_path and pressure_path.exists():
        pressure_rows = _load_csv_rows(pressure_path)
    pressure_lookup = _build_pressure_lookup(pressure_rows)

    # Per-day, per-state rows.
    all_rows: List[StateRow] = []
    for d in dates:
        day_dir = sharepacks_root / d
        if not day_dir.exists():
            continue
        results_file = REPO_ROOT / "data" / "results" / f"{d}.txt"
        winners_by_state = _load_results_winners(results_file)

        state_dirs = sorted([p for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"], key=lambda p: p.name)
        for state_dir in state_dirs:
            state_key = state_dir.name
            suffix = "" if args.profile == "mixed" else f"__{args.profile}"
            cu_path = state_dir / f"candidate_universe{suffix}.json"
            pc_path = state_dir / f"play_card{suffix}.json"
            if not cu_path.exists() or not pc_path.exists():
                continue
            raw_cu = _read_json(cu_path)
            raw_pc = _read_json(pc_path)
            if not isinstance(raw_cu, dict) or not isinstance(raw_pc, dict):
                continue

            winners = winners_by_state.get(state_key) or Winners("", "")

            cand = _candidate_summary(raw_cu)
            pressure = _pressure_summary_for_state_day(
                pressure_lookup,
                date=d,
                state_key=state_key,
                top_k=int(args.pressure_top_k),
            )
            cu_mid = _union_hits(raw_cu, winner=winners.midday)
            cu_eve = _union_hits(raw_cu, winner=winners.evening)
            pc_mid = _play_card_hits(raw_pc, winner=winners.midday, strategy=args.play_card_strategy, budget=args.play_card_budget)
            pc_eve = _play_card_hits(raw_pc, winner=winners.evening, strategy=args.play_card_strategy, budget=args.play_card_budget)

            all_rows.append(
                StateRow(
                    date=d,
                    state_key=state_key,
                    cu=cand,
                    pressure=pressure,
                    cu_mid=cu_mid,
                    cu_eve=cu_eve,
                    pc_mid=pc_mid,
                    pc_eve=pc_eve,
                )
            )

    # CSV output: per-(date,state) features and hits (easy to slice later).
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "date",
        "state_key",
        "cu_union_count",
        "cu_packs_count",
        "cu_due_doubles_count",
        "cu_top_support_count",
        "pressure_top_k",
        "pressure_midday_sum",
        "pressure_evening_sum",
        "pressure_intersection_count",
        "pressure_intersection_sum",
        "cu_mid_hit_any",
        "cu_mid_straight_hit",
        "cu_mid_box_hit",
        "cu_eve_hit_any",
        "cu_eve_straight_hit",
        "cu_eve_box_hit",
        "pc_mid_hit_any",
        "pc_mid_straight_hit",
        "pc_mid_box_hit",
        "pc_eve_hit_any",
        "pc_eve_straight_hit",
        "pc_eve_box_hit",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in all_rows:
            w.writerow(
                {
                    "date": r.date,
                    "state_key": r.state_key,
                    "cu_union_count": r.cu.union_count,
                    "cu_packs_count": r.cu.packs_count,
                    "cu_due_doubles_count": r.cu.due_doubles_count,
                    "cu_top_support_count": r.cu.top_support_count,
                    "pressure_top_k": r.pressure.top_k,
                    "pressure_midday_sum": r.pressure.midday_sum,
                    "pressure_evening_sum": r.pressure.evening_sum,
                    "pressure_intersection_count": len(r.pressure.intersection),
                    "pressure_intersection_sum": r.pressure.intersection_sum,
                    "cu_mid_hit_any": int(bool(r.cu_mid.get("hit_any"))),
                    "cu_mid_straight_hit": int(bool(r.cu_mid.get("straight_hit"))),
                    "cu_mid_box_hit": int(bool(r.cu_mid.get("box_hit"))),
                    "cu_eve_hit_any": int(bool(r.cu_eve.get("hit_any"))),
                    "cu_eve_straight_hit": int(bool(r.cu_eve.get("straight_hit"))),
                    "cu_eve_box_hit": int(bool(r.cu_eve.get("box_hit"))),
                    "pc_mid_hit_any": int(bool(r.pc_mid.get("hit_any"))),
                    "pc_mid_straight_hit": int(bool(r.pc_mid.get("straight_hit"))),
                    "pc_mid_box_hit": int(bool(r.pc_mid.get("box_hit"))),
                    "pc_eve_hit_any": int(bool(r.pc_eve.get("hit_any"))),
                    "pc_eve_straight_hit": int(bool(r.pc_eve.get("straight_hit"))),
                    "pc_eve_box_hit": int(bool(r.pc_eve.get("box_hit"))),
                }
            )

    # Config evaluation (rank states within each day, then grade top N).
    by_date: Dict[str, List[StateRow]] = {}
    for r in all_rows:
        by_date.setdefault(r.date, []).append(r)

    top_n = max(1, int(args.top_n_states))
    configs = [c.strip() for c in args.configs if c.strip()]
    for c in configs:
        # Validate early.
        _rank_key(c, all_rows[0]) if all_rows else None

    def _slot_rate(values: List[bool]) -> float:
        return (sum(1 for v in values if v) / len(values)) if values else 0.0

    def _day_rate(by_day_hits: Dict[str, List[bool]]) -> float:
        if not by_day_hits:
            return 0.0
        days = sorted(by_day_hits.keys())
        return sum(1 for d in days if any(by_day_hits[d])) / len(days)

    lines: List[str] = []
    lines.append(f"# Superbrain Config Harness — {args.start_date} to {args.end_date}")
    lines.append("")
    lines.append("Provenance")
    lines.append(f"- Generated: `{_now_iso()}`")
    lines.append(f"- Predictive sharepacks root: `{_safe_rel(sharepacks_root)}`")
    lines.append(f"- Profile: `{args.profile}`")
    lines.append(f"- Top N states per day: `{top_n}`")
    lines.append(f"- Play Card strategy/budget: `{args.play_card_strategy}` / `{args.play_card_budget}`")
    if pressure_path and pressure_path.exists():
        lines.append(f"- Aux pressure index stats: `{_safe_rel(pressure_path)}`")
    else:
        lines.append("- Aux pressure index stats: `(missing; pressure features default to 0)`")
    lines.append("")

    lines.append("## Summary (slot-rate over top-N states)")
    lines.append("")
    lines.append("| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")

    for cfg in configs:
        mid_cu_hit: List[bool] = []
        mid_cu_box: List[bool] = []
        mid_pc_hit: List[bool] = []
        eve_cu_hit: List[bool] = []
        eve_cu_box: List[bool] = []
        eve_pc_hit: List[bool] = []

        for d, rows in sorted(by_date.items()):
            ranked = sorted(rows, key=lambda r: _rank_key(cfg, r))
            picked = ranked[:top_n]
            mid_cu_hit.extend([bool(r.cu_mid.get("hit_any")) for r in picked])
            mid_cu_box.extend([bool(r.cu_mid.get("box_hit")) for r in picked])
            mid_pc_hit.extend([bool(r.pc_mid.get("hit_any")) for r in picked])
            eve_cu_hit.extend([bool(r.cu_eve.get("hit_any")) for r in picked])
            eve_cu_box.extend([bool(r.cu_eve.get("box_hit")) for r in picked])
            eve_pc_hit.extend([bool(r.pc_eve.get("hit_any")) for r in picked])

        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cfg}`",
                    f"{_slot_rate(mid_cu_hit):.3f}",
                    f"{_slot_rate(mid_cu_box):.3f}",
                    f"{_slot_rate(mid_pc_hit):.3f}",
                    f"{_slot_rate(eve_cu_hit):.3f}",
                    f"{_slot_rate(eve_cu_box):.3f}",
                    f"{_slot_rate(eve_pc_hit):.3f}",
                ]
            )
            + " |"
        )

    lines.append("")
    lines.append("## Summary (day-rate: at least one hit in top-N)")
    lines.append("")
    lines.append("| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")

    for cfg in configs:
        mid_cu_hit_by_day: Dict[str, List[bool]] = {}
        mid_cu_box_by_day: Dict[str, List[bool]] = {}
        mid_pc_hit_by_day: Dict[str, List[bool]] = {}
        eve_cu_hit_by_day: Dict[str, List[bool]] = {}
        eve_cu_box_by_day: Dict[str, List[bool]] = {}
        eve_pc_hit_by_day: Dict[str, List[bool]] = {}

        for d, rows in sorted(by_date.items()):
            ranked = sorted(rows, key=lambda r: _rank_key(cfg, r))
            picked = ranked[:top_n]
            mid_cu_hit_by_day[d] = [bool(r.cu_mid.get("hit_any")) for r in picked]
            mid_cu_box_by_day[d] = [bool(r.cu_mid.get("box_hit")) for r in picked]
            mid_pc_hit_by_day[d] = [bool(r.pc_mid.get("hit_any")) for r in picked]
            eve_cu_hit_by_day[d] = [bool(r.cu_eve.get("hit_any")) for r in picked]
            eve_cu_box_by_day[d] = [bool(r.cu_eve.get("box_hit")) for r in picked]
            eve_pc_hit_by_day[d] = [bool(r.pc_eve.get("hit_any")) for r in picked]

        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cfg}`",
                    f"{_day_rate(mid_cu_hit_by_day):.3f}",
                    f"{_day_rate(mid_cu_box_by_day):.3f}",
                    f"{_day_rate(mid_pc_hit_by_day):.3f}",
                    f"{_day_rate(eve_cu_hit_by_day):.3f}",
                    f"{_day_rate(eve_cu_box_by_day):.3f}",
                    f"{_day_rate(eve_pc_hit_by_day):.3f}",
                ]
            )
            + " |"
        )

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- This is a triage/ranking harness (Brain‑2), not an analyzer benchmark.")
    lines.append("- `CU box_hit` measures whether the winning **canonical** is present anywhere in Candidate Universe canonicals (lane visibility).")
    lines.append("- `CU hit_any` (MIXED) is `straight_hit OR box_hit` for the union pack, matching grade semantics.")
    lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
