#!/usr/bin/env python3
"""
Create a Play Card "geometry invariants" report for a graded window.

Why:
- We are iterating on selection geometry under fixed posture (tool_only + stable10 + B36).
- When we change within-lane selection (spine chooser variants), we want to *prove*:
    - spine cap was respected (pack-level and total-card),
    - breadth did not silently collapse,
    - the variant actually changed lines (no-op detection),
    - and how much of the spine pack came from VTRAC display members vs evidence rows.

Inputs:
- A window-level conversion ladder CSV (used as the roster of outcomes + play_card_path).
- The referenced Play Card JSONs in sharepacks/_predictive.

Outputs:
- RUNS/*__PLAY_CARD_GEOMETRY__*.csv + .md (window-level summary + per-outcome rows).

Notes:
- Reporting-only; does not change analyzers or sharepacks.
- This report is designed to be zipped into the Deep Research upload pack (gitignore-safe).
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import modules.vtrac_reference as vr  # noqa: E402


def _normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:60]


def _normalize_label(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:80]


def _normalize_pick3_literal(value: str) -> str:
    s = str(value or "").strip()
    digits = "".join(ch for ch in s if ch.isdigit())
    if not digits:
        return ""
    if len(digits) >= 3:
        digits = digits[-3:]
    return digits.zfill(3)


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


def safe_int(value: object) -> Optional[int]:
    try:
        s = str(value or "").strip()
        if not s:
            return None
        return int(s)
    except Exception:
        return None


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        raw = json.load(f)
    return raw if isinstance(raw, dict) else {}


def _ladder_csv_path(*, date_from: str, date_to: str, profile: str, strategy: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date_from}_to_{date_to}__CONVERSION_LADDER__{profile}__{strategy}{suffix}.csv"


def _out_base_path(
    *,
    date_from: str,
    date_to: str,
    profile: str,
    experiment_tag: str,
    budget_label: str,
    label: str,
) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    lbl = _normalize_label(label)
    extra = f"__{budget_label}"
    if lbl:
        extra += f"__{lbl}"
    return RUNS_DIR / f"{date_from}_to_{date_to}__PLAY_CARD_GEOMETRY__{profile}{suffix}{extra}"


def _vtrac_display_members(*, index: int) -> set[str]:
    """
    Return the boxed-member display set for a VTRAC index (matches create_play_card._vtrac_display_pack).
    """
    want = int(index)
    for row in vr.VTRAC_DISPLAY:
        try:
            if int(row.get("Index")) != want:
                continue
        except Exception:
            continue
        combos: set[str] = set()
        for key in ("Singles", "Doubles"):
            raw = str(row.get(key) or "").strip()
            if not raw:
                continue
            for token in raw.split():
                c = _normalize_pick3_literal(token)
                if c:
                    combos.add(c)
        return combos
    return set()


def _counts_by_index(combos: Sequence[str]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for combo in combos:
        c = _normalize_pick3_literal(combo)
        if not c:
            continue
        idx = vr.get_vtrac_index(c)
        if isinstance(idx, int):
            out[int(idx)] = out.get(int(idx), 0) + 1
    return out


def _get_budget_obj(payload: Dict[str, Any], *, strategy: str, budget_label: str) -> Optional[Dict[str, Any]]:
    strategies = payload.get("strategies")
    if not isinstance(strategies, dict):
        return None
    strat = strategies.get(strategy)
    if not isinstance(strat, dict):
        return None
    obj = strat.get(budget_label)
    return obj if isinstance(obj, dict) else None


def _pack_combos_by_index(obj: Dict[str, Any]) -> Dict[int, List[str]]:
    vtrac_pack = obj.get("vtrac_pack")
    if not isinstance(vtrac_pack, dict):
        return {}
    raw = vtrac_pack.get("pack_combos_by_index")
    if not isinstance(raw, dict):
        return {}
    out: Dict[int, List[str]] = {}
    for k, v in raw.items():
        idx = safe_int(k)
        if idx is None:
            continue
        if isinstance(v, list):
            out[int(idx)] = [_normalize_pick3_literal(x) for x in v if _normalize_pick3_literal(x)]
    return out


def _spine_indices(obj: Dict[str, Any]) -> List[int]:
    vtrac_pack = obj.get("vtrac_pack")
    if not isinstance(vtrac_pack, dict):
        return []
    packs_target = safe_int(vtrac_pack.get("packs_target")) or 0
    chooser = vtrac_pack.get("chooser")
    if not isinstance(chooser, dict):
        return []
    ranked_snapshot = chooser.get("ranked_indices")
    if not isinstance(ranked_snapshot, dict):
        return []
    chosen = ranked_snapshot.get("chosen_indices")
    indices = [safe_int(x) for x in chosen] if isinstance(chosen, list) else []
    indices = [int(x) for x in indices if isinstance(x, int)]
    if packs_target <= 0:
        return indices[:4]
    return indices[:packs_target]


def _spine_alloc_meta(obj: Dict[str, Any]) -> Tuple[int, str, str]:
    vtrac_pack = obj.get("vtrac_pack")
    if not isinstance(vtrac_pack, dict):
        return 0, "", ""
    allocation = vtrac_pack.get("allocation")
    if not isinstance(allocation, dict):
        return 0, "", ""
    cap = safe_int(allocation.get("spine_max_lines_per_index")) or 0
    mode = str(allocation.get("spine_pick_mode") or "").strip()
    taper = str(allocation.get("spine_taper_caps") or "").strip()
    taper = taper.replace(" ", "")
    return cap, mode, taper


@dataclass(frozen=True)
class RowOut:
    results_date: str
    state_key: str
    winner_label: str
    play_card_path: str
    strategy: str
    budget_label: str
    combos_count: int
    indices_touched_count: int
    max_lines_single_index: int
    spine_indices: str
    spine_cap: int
    spine_pick_mode: str
    spine_taper_caps: str
    spine_pack_counts: str
    spine_total_counts: str
    spine_cap_violations_pack: int
    spine_cap_violations_total: int
    spine_taper_violations_pack: int
    spine_taper_violations_total: int
    spine_pack_display_lines: int
    spine_pack_evidence_lines: int
    spine_pack_display_share: float
    diff_new_lines: int
    diff_dropped_lines: int
    diff_noop: int


def _pct(values: List[int], p: float) -> Optional[float]:
    if not values:
        return None
    xs = sorted(values)
    if len(xs) == 1:
        return float(xs[0])
    k = (len(xs) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(xs[int(k)])
    return xs[f] * (c - k) + xs[c] * (k - f)


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a Play Card geometry invariants report for a graded window.")
    ap.add_argument("--date-from", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--date-to", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only", help="Profile in ladder filenames (default: tool_only).")
    ap.add_argument("--experiment-tag", default="", help="Optional experiment tag suffix (e.g., stable10).")
    ap.add_argument("--roster-strategy", required=True, help="Strategy whose ladder CSV is used as the outcome roster.")
    ap.add_argument("--strategies", required=True, help="Comma-separated list of strategies to audit.")
    ap.add_argument("--baseline-strategy", required=True, help="Baseline strategy used for line-diff comparisons.")
    ap.add_argument("--budget", default="B36", help="Budget label to analyze (default: B36).")
    ap.add_argument("--label", default="", help="Optional short label added to output filenames.")
    ap.add_argument("--out", default=None, help="Override output path base (without extension).")
    args = ap.parse_args()

    date_from = str(args.date_from).strip()
    date_to = str(args.date_to).strip()
    profile = str(args.profile or "tool_only").strip()
    exp_tag = _normalize_tag(args.experiment_tag)
    roster_strategy = str(args.roster_strategy).strip()
    baseline_strategy = str(args.baseline_strategy).strip()
    budget_label = str(args.budget or "B36").strip()
    label = str(args.label or "").strip()

    strategies = [s.strip() for s in str(args.strategies or "").split(",") if s.strip()]
    if not strategies:
        raise SystemExit("--strategies is required")

    ladder_csv = _ladder_csv_path(
        date_from=date_from,
        date_to=date_to,
        profile=profile,
        strategy=roster_strategy,
        experiment_tag=exp_tag,
    )
    if not ladder_csv.exists():
        raise SystemExit(f"Missing ladder CSV: {ladder_csv}")

    out_base = (
        Path(args.out)
        if args.out
        else _out_base_path(
            date_from=date_from,
            date_to=date_to,
            profile=profile,
            experiment_tag=exp_tag,
            budget_label=budget_label,
            label=label,
        )
    )
    if not out_base.is_absolute():
        out_base = (REPO_ROOT / out_base).resolve()
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_csv = out_base.with_suffix(".csv")
    out_md = out_base.with_suffix(".md")

    ladder_rows = load_csv_rows(ladder_csv)
    roster = [
        r
        for r in ladder_rows
        if (r.get("budget_label") or "") == budget_label and bool01(r.get("winner_missing")) == 0 and (r.get("play_card_path") or "").strip()
    ]

    derived: List[RowOut] = []
    missing_play_cards = 0
    missing_budget_objs: Dict[str, int] = {s: 0 for s in strategies}
    missing_budget_objs.setdefault(baseline_strategy, 0)

    for r in roster:
        pc_rel = (r.get("play_card_path") or "").strip()
        pc_path = (REPO_ROOT / pc_rel).resolve()
        if not pc_path.exists():
            missing_play_cards += 1
            continue
        payload = load_json(pc_path)

        base_obj = _get_budget_obj(payload, strategy=baseline_strategy, budget_label=budget_label)
        if not base_obj:
            missing_budget_objs[baseline_strategy] = missing_budget_objs.get(baseline_strategy, 0) + 1
            continue
        base_combos_raw = base_obj.get("combos")
        base_combos = [str(x) for x in base_combos_raw] if isinstance(base_combos_raw, list) else []
        base_set = {c for c in (_normalize_pick3_literal(x) for x in base_combos) if c}

        for strat in strategies:
            obj = _get_budget_obj(payload, strategy=strat, budget_label=budget_label)
            if not obj:
                missing_budget_objs[strat] = missing_budget_objs.get(strat, 0) + 1
                continue
            combos_raw = obj.get("combos")
            combos = [str(x) for x in combos_raw] if isinstance(combos_raw, list) else []
            combos_norm = [c for c in (_normalize_pick3_literal(x) for x in combos) if c]
            counts = _counts_by_index(combos_norm)

            spine_idxs = _spine_indices(obj)
            spine_idxs_str = ",".join(str(i) for i in spine_idxs)
            spine_cap, spine_mode, taper_str = _spine_alloc_meta(obj)
            pack_by_idx = _pack_combos_by_index(obj)
            spine_pack_counts: Dict[int, int] = {i: len(pack_by_idx.get(int(i), [])) for i in spine_idxs}
            spine_total_counts: Dict[int, int] = {i: int(counts.get(int(i), 0)) for i in spine_idxs}

            viol_pack = 0
            viol_total = 0
            if spine_cap > 0:
                viol_pack = sum(1 for i in spine_idxs if spine_pack_counts.get(int(i), 0) > spine_cap)
                viol_total = sum(1 for i in spine_idxs if spine_total_counts.get(int(i), 0) > spine_cap)

            taper_caps: List[int] = []
            if taper_str:
                for part in taper_str.split(","):
                    n = safe_int(part.strip())
                    if isinstance(n, int):
                        taper_caps.append(int(n))

            taper_viol_pack = 0
            taper_viol_total = 0
            if taper_caps:
                for i, lane_idx in enumerate(spine_idxs):
                    cap_i = taper_caps[i] if i < len(taper_caps) else spine_cap
                    if cap_i > 0 and spine_pack_counts.get(int(lane_idx), 0) > cap_i:
                        taper_viol_pack += 1
                    if cap_i > 0 and spine_total_counts.get(int(lane_idx), 0) > cap_i:
                        taper_viol_total += 1

            spine_pack_display = 0
            spine_pack_total = 0
            for i in spine_idxs:
                members = _vtrac_display_members(index=int(i))
                for c in pack_by_idx.get(int(i), []):
                    spine_pack_total += 1
                    if c in members:
                        spine_pack_display += 1
            spine_pack_evidence = max(0, spine_pack_total - spine_pack_display)
            display_share = (float(spine_pack_display) / float(spine_pack_total)) if spine_pack_total else 0.0

            cand_set = set(combos_norm)
            diff_new = len(cand_set - base_set)
            diff_drop = len(base_set - cand_set)
            noop = 1 if cand_set == base_set else 0

            derived.append(
                RowOut(
                    results_date=r.get("results_date", ""),
                    state_key=r.get("state_key", ""),
                    winner_label=r.get("winner_label", ""),
                    play_card_path=pc_rel,
                    strategy=strat,
                    budget_label=budget_label,
                    combos_count=len(combos_norm),
                    indices_touched_count=len(counts),
                    max_lines_single_index=max(counts.values()) if counts else 0,
                    spine_indices=spine_idxs_str,
                    spine_cap=spine_cap,
                    spine_pick_mode=spine_mode,
                    spine_taper_caps=taper_str,
                    spine_pack_counts=" ".join(f"{k}:{v}" for k, v in spine_pack_counts.items()),
                    spine_total_counts=" ".join(f"{k}:{v}" for k, v in spine_total_counts.items()),
                    spine_cap_violations_pack=int(viol_pack),
                    spine_cap_violations_total=int(viol_total),
                    spine_taper_violations_pack=int(taper_viol_pack),
                    spine_taper_violations_total=int(taper_viol_total),
                    spine_pack_display_lines=int(spine_pack_display),
                    spine_pack_evidence_lines=int(spine_pack_evidence),
                    spine_pack_display_share=round(display_share, 4),
                    diff_new_lines=int(diff_new),
                    diff_dropped_lines=int(diff_drop),
                    diff_noop=int(noop),
                )
            )

    # Write CSV (one row per outcome+strategy)
    cols = [f.name for f in RowOut.__dataclass_fields__.values()]  # type: ignore[attr-defined]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for row in derived:
            w.writerow({c: getattr(row, c) for c in cols})

    # Summary MD
    by_strat: Dict[str, List[RowOut]] = {}
    for row in derived:
        by_strat.setdefault(row.strategy, []).append(row)

    lines: List[str] = []
    lines.append(f"# Play Card Geometry — {date_from}..{date_to}")
    lines.append("")
    lines.append("Source: conversion ladder roster + referenced Play Card JSONs.")
    lines.append("")
    lines.append("## Parameters")
    lines.append("")
    lines.append(f"- roster_strategy: `{roster_strategy}`")
    lines.append(f"- baseline_strategy: `{baseline_strategy}`")
    lines.append(f"- strategies: `{', '.join(strategies)}`")
    lines.append(f"- profile: `{profile}`")
    lines.append(f"- experiment_tag: `{exp_tag}`")
    lines.append(f"- budget_label: `{budget_label}`")
    lines.append("")
    lines.append("## Roster")
    lines.append("")
    lines.append(f"- ladder_csv: `{ladder_csv}`")
    lines.append(f"- outcomes_in_roster: `{len(roster)}`")
    lines.append(f"- missing_play_cards: `{missing_play_cards}`")
    lines.append("")
    lines.append("## Missing budget objects (per strategy)")
    lines.append("")
    for k in [baseline_strategy] + [s for s in strategies if s != baseline_strategy]:
        lines.append(f"- `{k}`: `{missing_budget_objs.get(k, 0)}`")
    lines.append("")

    lines.append("## Strategy summaries (diff/no-op + invariants)")
    lines.append("")
    for strat in strategies:
        rows = by_strat.get(strat, [])
        if not rows:
            lines.append(f"- `{strat}`: (no rows)")
            continue
        noops = [r.diff_noop for r in rows]
        diff_new = [r.diff_new_lines for r in rows]
        diff_drop = [r.diff_dropped_lines for r in rows]
        viol_pack = [r.spine_cap_violations_pack for r in rows]
        viol_total = [r.spine_cap_violations_total for r in rows]
        taper_viol_pack = [r.spine_taper_violations_pack for r in rows]
        taper_viol_total = [r.spine_taper_violations_total for r in rows]
        display_share = [r.spine_pack_display_share for r in rows]
        max_lines = [r.max_lines_single_index for r in rows]
        touched = [r.indices_touched_count for r in rows]

        lines.append(f"### `{strat}`")
        lines.append("")
        lines.append(f"- rows: `{len(rows)}` | no_op_rate: `{round(sum(noops)/len(noops), 4)}`")
        lines.append(
            f"- diff_new_lines (mean/p50/p90): `{round(statistics.mean(diff_new), 3)}` / `{_pct(diff_new, 0.5)}` / `{_pct(diff_new, 0.9)}`"
        )
        lines.append(
            f"- diff_dropped_lines (mean/p50/p90): `{round(statistics.mean(diff_drop), 3)}` / `{_pct(diff_drop, 0.5)}` / `{_pct(diff_drop, 0.9)}`"
        )
        lines.append(f"- spine_cap_violations_pack (sum): `{sum(viol_pack)}` | spine_cap_violations_total (sum): `{sum(viol_total)}`")
        if sum(taper_viol_pack) or sum(taper_viol_total):
            lines.append(
                f"- spine_taper_violations_pack (sum): `{sum(taper_viol_pack)}` | spine_taper_violations_total (sum): `{sum(taper_viol_total)}`"
            )
        lines.append(
            f"- spine_pack_display_share (mean/p50/p90): `{round(statistics.mean(display_share), 3)}` / `{_pct(display_share, 0.5)}` / `{_pct(display_share, 0.9)}`"
        )
        lines.append(
            f"- indices_touched_count (mean/p50/p90): `{round(statistics.mean(touched), 3)}` / `{_pct(touched, 0.5)}` / `{_pct(touched, 0.9)}`"
        )
        lines.append(
            f"- max_lines_single_index (mean/p50/p90): `{round(statistics.mean(max_lines), 3)}` / `{_pct(max_lines, 0.5)}` / `{_pct(max_lines, 0.9)}`"
        )
        lines.append("")

    lines.append("## Output files")
    lines.append("")
    lines.append(f"- CSV: `{out_csv}`")
    lines.append(f"- MD: `{out_md}`")
    lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"[OK] Wrote: {out_csv}")
    print(f"[OK] Wrote: {out_md}")


if __name__ == "__main__":
    main()
