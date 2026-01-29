#!/usr/bin/env python3
"""
Create a "winner lane rank" diagnostic report.

Purpose:
  - Separate "lane ranking" issues from "within-lane conversion" issues.
  - For each outcome (state + Midday/Evening winner), report:
      - winner VTRAC index,
      - rank of that index under multiple chooser lenses (methods_first / packs_first / score_total_first),
      - whether the chosen Play Card retained the lane and/or the exact winner,
      - whether the winner was selected via pack vs filler (and MoP source if present).

This is reporting-only. It does not change analyzers.

Usage:
  python3 scripts/tools/create_winner_lane_rank_report.py \
    --date-from 2026-01-15 --date-to 2026-01-22 \
    --profile tool_only --experiment-tag stable10 \
    --strategies v0_2_default_multi_pack_packheavy_lane_diverse_filler,v0_2_default_multi_pack_mop_24_12
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC_ROOT = ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def daterange(start: str, end: str) -> List[str]:
    s = parse_date(start)
    e = parse_date(end)
    if e < s:
        raise SystemExit("--date-to must be >= --date-from")
    out: List[str] = []
    cur = s
    while cur <= e:
        out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return path.read_text(errors="replace")


def _normalize_pick3_literal(value: str) -> str:
    s = str(value or "").strip()
    digits = "".join(ch for ch in s if ch.isdigit())
    if not digits:
        return ""
    if len(digits) >= 3:
        digits = digits[-3:]
    return digits.zfill(3)


def _canon(value: str) -> str:
    c = _normalize_pick3_literal(value)
    if not c:
        return ""
    return "".join(sorted(c))


def _unique_perms(triad: str) -> set[str]:
    from itertools import permutations

    triad = _normalize_pick3_literal(triad)
    if not triad:
        return set()
    return {"".join(p) for p in permutations(triad, 3)}


def _boxed_canonicals(combos: Sequence[str]) -> set[str]:
    by_canon: Dict[str, set[str]] = {}
    for c in combos:
        c = _normalize_pick3_literal(c)
        if not c:
            continue
        by_canon.setdefault(_canon(c), set()).add(c)
    boxed: set[str] = set()
    for canon, members in by_canon.items():
        perms = _unique_perms(canon)
        if perms and perms.issubset(members):
            boxed.add(canon)
    return boxed


def _pack_vtrac_indices(combos: Sequence[str]) -> set[int]:
    import modules.vtrac_reference as vr

    indices: set[int] = set()
    for combo in combos:
        c = _normalize_pick3_literal(combo)
        if not c:
            continue
        idx = vr.get_vtrac_index(c)
        if isinstance(idx, int):
            indices.add(idx)
    return indices


def _winner_vtrac_index(winner: str) -> Optional[int]:
    import modules.vtrac_reference as vr

    w = _normalize_pick3_literal(winner)
    if not w:
        return None
    idx = vr.get_vtrac_index(w)
    return idx if isinstance(idx, int) else None


@dataclass(frozen=True)
class Winner:
    midday: Optional[str]
    evening: Optional[str]


def _load_results_winners(results_file: Path) -> Dict[str, Winner]:
    """
    Map project state_key -> Winner(midday, evening).
    Treat missing/empty files as no-winners.
    """
    if not results_file.exists() or results_file.stat().st_size <= 0:
        return {}

    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    text = _read_text(results_file)
    entries = parse_winner_sheet(text)

    winners: Dict[str, Winner] = {}
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
            winners[state_key] = Winner(
                midday=_normalize_pick3_literal(midday or ""),
                evening=_normalize_pick3_literal(evening or ""),
            )
    return winners


def _play_card_path(*, state_dir: Path, profile: str, experiment_tag: str) -> Path:
    suffix = f"__{experiment_tag}" if experiment_tag else ""
    return state_dir / f"play_card__{profile}{suffix}.json"


def _lane_scored(
    *,
    ranked: Sequence[Dict[str, Any]],
    scan_limit: int,
) -> List[Dict[str, Any]]:
    """
    Build lane evidence rows matching the core chooser inputs.

    This is intentionally aligned with the lane evidence aggregation in create_play_card.py:
    - group combos by VTRAC index,
    - aggregate support methods/variants/packs and score_total.
    """
    import modules.vtrac_reference as vr

    evidence: Dict[int, Dict[str, Any]] = {}
    for row in list(ranked)[: int(scan_limit)]:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue

        methods = row.get("support_methods") or []
        methods_norm = [str(m) for m in methods] if isinstance(methods, list) else []
        methods_norm = [m for m in methods_norm if m != "blackapple"]

        ev = evidence.setdefault(
            int(idx),
            {
                "rows_count": 0,
                "score_total": 0.0,
                "packs_total": 0,
                "methods": set(),
                "variants": set(),
            },
        )

        ev["rows_count"] += 1
        ev["score_total"] += float(row.get("score") or 0.0)
        ev["packs_total"] += int(row.get("support_packs_count") or 0)
        if methods_norm:
            ev["methods"].update(methods_norm)
        variants = row.get("support_variants") or []
        if isinstance(variants, list):
            ev["variants"].update(str(v or "Unknown") for v in variants)

    scored: List[Dict[str, Any]] = []
    for idx, ev in evidence.items():
        methods_count = len(ev["methods"])
        variants_set = set(ev["variants"])
        variants_non_unknown = len({v for v in variants_set if v != "Unknown"})
        variants_total = len(variants_set)
        scored.append(
            {
                "index": int(idx),
                "rows_count": int(ev["rows_count"]),
                "methods_count": int(methods_count),
                "variants_non_unknown": int(variants_non_unknown),
                "variants_total": int(variants_total),
                "packs_total": int(ev["packs_total"]),
                "score_total": float(ev["score_total"]),
            }
        )
    return scored


def _lane_order(scored: List[Dict[str, Any]], *, preset: str) -> List[int]:
    p = str(preset or "methods_first").strip().lower()
    if p not in {"methods_first", "packs_first", "score_total_first"}:
        raise SystemExit(f"Invalid preset: {preset!r} (expected methods_first|packs_first|score_total_first)")

    rows = list(scored)
    if p == "score_total_first":
        rows.sort(
            key=lambda r: (
                -float(r["score_total"]),
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                int(r["index"]),
            )
        )
    elif p == "packs_first":
        rows.sort(
            key=lambda r: (
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                -float(r["score_total"]),
                int(r["index"]),
            )
        )
    else:
        rows.sort(
            key=lambda r: (
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                -int(r["packs_total"]),
                -float(r["score_total"]),
                int(r["index"]),
            )
        )
    return [int(r["index"]) for r in rows]


def _rank_of(index: Optional[int], order: Sequence[int]) -> Optional[int]:
    if index is None:
        return None
    try:
        return int(order.index(int(index)) + 1)
    except ValueError:
        return None


def _pct(n: int, d: int) -> str:
    return f"{(100.0 * n / d):.1f}%" if d else "NA"


def _count_leq(values: Iterable[Optional[int]], threshold: int) -> int:
    return sum(1 for v in values if isinstance(v, int) and v <= threshold)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date-from", required=True, help="Start results date D0 (YYYY-MM-DD)")
    ap.add_argument("--date-to", required=True, help="End results date D1 (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default=str(ROOT / "sharepacks" / "_predictive"),
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        default="tool_only",
        choices=("mixed", "tool_only", "profit_only"),
        help="Profile for play_card filenames (default: tool_only)",
    )
    ap.add_argument("--experiment-tag", default="", help="Optional experiment tag (e.g., stable10)")
    ap.add_argument(
        "--strategies",
        required=True,
        help="Comma-separated strategy keys to include (must exist in play_card.json)",
    )
    ap.add_argument("--budget", default="B36", help="Budget label to report (default: B36)")
    ap.add_argument("--scan-limit", type=int, default=350, help="How many ranked candidates to scan (default: 350)")
    ap.add_argument(
        "--out-csv",
        default="",
        help="Override output CSV path (default: docs/.../RUNS/<range>__WINNER_LANE_RANK__...csv)",
    )
    ap.add_argument(
        "--out-md",
        default="",
        help="Override output Markdown path (default: docs/.../RUNS/<range>__WINNER_LANE_RANK__...md)",
    )
    args = ap.parse_args()

    dates = daterange(args.date_from, args.date_to)
    sharepacks_root = Path(args.sharepacks_root)
    profile = str(args.profile).strip()
    experiment_tag = str(args.experiment_tag or "").strip()
    strategies = [s.strip() for s in str(args.strategies).split(",") if s.strip()]
    budget_label = str(args.budget or "B36").strip()
    scan_limit = int(args.scan_limit)

    tag_part = f"__{experiment_tag}" if experiment_tag else ""
    default_base = ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
    out_csv = Path(args.out_csv) if args.out_csv else default_base / f"{args.date_from}_to_{args.date_to}__WINNER_LANE_RANK__{profile}{tag_part}__{budget_label}.csv"
    out_md = Path(args.out_md) if args.out_md else default_base / f"{args.date_from}_to_{args.date_to}__WINNER_LANE_RANK__{profile}{tag_part}__{budget_label}.md"
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "results_date",
        "state_key",
        "winner_label",
        "winner",
        "winner_missing",
        "winner_vtrac_index",
        "lane_present",
        "lane_rank_methods_first",
        "lane_rank_packs_first",
        "lane_rank_score_total_first",
        "strategy",
        "budget_label",
        "hit_any",
        "hit_any_inclusive",
        "straight_hit",
        "box_hit",
        "vtrac_index_hit",
        "winner_in_pack_indices",
        "winner_selected_by",
        "winner_combo_source",
        "play_card_path",
    ]

    rows_out: List[Dict[str, str]] = []

    for d in dates:
        results_file = ROOT / "data" / "results" / f"{d}.txt"
        winners_by_state = _load_results_winners(results_file)
        day_dir = sharepacks_root / d
        if not day_dir.exists():
            continue

        for state_key, winners in sorted(winners_by_state.items(), key=lambda kv: kv[0]):
            state_dir = day_dir / state_key
            if not state_dir.exists():
                continue
            pc_path = _play_card_path(state_dir=state_dir, profile=profile, experiment_tag=experiment_tag)
            if not pc_path.exists():
                continue

            payload: Dict[str, Any]
            try:
                payload = __import__("json").loads(_read_text(pc_path))
            except Exception:
                continue

            ranked = payload.get("ranked_candidates") or []
            ranked_list = ranked if isinstance(ranked, list) else []
            scored = _lane_scored(ranked=ranked_list, scan_limit=scan_limit)
            order_methods = _lane_order(scored, preset="methods_first")
            order_packs = _lane_order(scored, preset="packs_first")
            order_score = _lane_order(scored, preset="score_total_first")

            strategies_payload = payload.get("strategies") or {}
            if not isinstance(strategies_payload, dict):
                continue

            for winner_label, winner in (("Midday", winners.midday), ("Evening", winners.evening)):
                w = _normalize_pick3_literal(winner or "")
                missing = not bool(w)
                wcanon = _canon(w) if w else ""
                wvt = _winner_vtrac_index(w) if w else None

                r_m = _rank_of(wvt, order_methods)
                r_p = _rank_of(wvt, order_packs)
                r_s = _rank_of(wvt, order_score)
                lane_present = "1" if (wvt is not None and (r_m is not None or r_p is not None or r_s is not None)) else "0"

                for strat in strategies:
                    strat_payload = strategies_payload.get(strat)
                    if not isinstance(strat_payload, dict):
                        continue
                    card = strat_payload.get(budget_label)
                    if not isinstance(card, dict):
                        continue

                    combos = [_normalize_pick3_literal(c) for c in (card.get("combos") or [])]
                    combos = [c for c in combos if c]
                    combos_set = set(combos)
                    canonicals_any_perm = {c for c in (_canon(x) for x in combos_set) if c}
                    boxed = _boxed_canonicals(combos)
                    indices = _pack_vtrac_indices(combos)

                    vtrac_pack = card.get("vtrac_pack") if isinstance(card, dict) else None
                    pack_raw = []
                    pack_indices: List[int] = []
                    if isinstance(vtrac_pack, dict):
                        indices_raw = vtrac_pack.get("indices")
                        if isinstance(indices_raw, list):
                            for x in indices_raw:
                                try:
                                    pack_indices.append(int(x))
                                except Exception:
                                    continue
                        pack_raw = vtrac_pack.get("pack_combos") or []
                    pack_norm = [_normalize_pick3_literal(c) for c in pack_raw] if isinstance(pack_raw, list) else []
                    pack_norm = [c for c in pack_norm if c]
                    pack_set = set(pack_norm) & combos_set
                    filler_set = combos_set - pack_set

                    straight_hit = bool(w and w in combos_set)
                    box_hit = bool(wcanon and wcanon in boxed)
                    hit_any = bool((straight_hit or box_hit) and not missing)
                    canon_hit_any_perm = bool(wcanon and wcanon in canonicals_any_perm and not missing)
                    vtrac_hit = bool(wvt is not None and wvt in indices)
                    hit_any_inclusive = bool((straight_hit or canon_hit_any_perm or vtrac_hit) and not missing)

                    winner_in_pack_indices = "1" if (not missing and wvt is not None and int(wvt) in set(pack_indices)) else "0"
                    winner_selected_by = ""
                    if not missing:
                        if w and w in pack_set:
                            winner_selected_by = "pack"
                        elif w and w in filler_set:
                            winner_selected_by = "filler"
                        else:
                            winner_selected_by = "none"

                    combo_source = ""
                    mop = card.get("mop") if isinstance(card, dict) else None
                    if isinstance(mop, dict):
                        src_map = mop.get("combo_source")
                        if isinstance(src_map, dict) and w and w in src_map:
                            combo_source = str(src_map.get(w) or "")

                    rows_out.append(
                        {
                            "results_date": d,
                            "state_key": state_key,
                            "winner_label": winner_label,
                            "winner": w,
                            "winner_missing": "1" if missing else "0",
                            "winner_vtrac_index": str(wvt) if wvt is not None else "",
                            "lane_present": lane_present,
                            "lane_rank_methods_first": str(r_m) if r_m is not None else "",
                            "lane_rank_packs_first": str(r_p) if r_p is not None else "",
                            "lane_rank_score_total_first": str(r_s) if r_s is not None else "",
                            "strategy": strat,
                            "budget_label": budget_label,
                            "hit_any": "1" if hit_any else "0",
                            "hit_any_inclusive": "1" if hit_any_inclusive else "0",
                            "straight_hit": "1" if straight_hit else "0",
                            "box_hit": "1" if box_hit else "0",
                            "vtrac_index_hit": "1" if (vtrac_hit and not missing) else "0",
                            "winner_in_pack_indices": winner_in_pack_indices,
                            "winner_selected_by": winner_selected_by,
                            "winner_combo_source": combo_source,
                            "play_card_path": _safe_rel(pc_path),
                        }
                    )

    rows_out.sort(key=lambda r: (r["results_date"], r["state_key"], r["winner_label"], r["strategy"]))

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    # Markdown summary: rank distributions per lens and strategy (winner-present only).
    lines: List[str] = []
    lines.append(f"# Winner Lane Rank — {args.date_from}..{args.date_to}")
    lines.append("")
    lines.append("This report answers: **where does the winner lane rank, and how does selection retain it?**")
    lines.append("")
    lines.append("## Inputs")
    lines.append("")
    lines.append(f"- sharepacks_root: `{_safe_rel(sharepacks_root)}`")
    lines.append(f"- profile: `{profile}`")
    lines.append(f"- experiment_tag: `{experiment_tag or '<none>'}`")
    lines.append(f"- strategies: `{', '.join(strategies)}`")
    lines.append(f"- budget: `{budget_label}`")
    lines.append(f"- scan_limit: `{scan_limit}`")
    lines.append("")
    lines.append(f"- CSV: `{_safe_rel(out_csv)}`")
    lines.append("")

    # Build per-strategy summaries on winner-present rows.
    lines.append("## Summary (winner present only)")
    lines.append("")
    lines.append("| strategy | rows | lane_present | hit_any | hit_any_inclusive | winner_in_pack_indices | rank<=1 (methods/packs/score) | rank<=2 | rank<=3 | rank<=5 | rank<=10 |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    by_strategy: Dict[str, List[Dict[str, str]]] = {s: [] for s in strategies}
    for r in rows_out:
        if r.get("winner_missing") == "1":
            continue
        s = r.get("strategy") or ""
        if s in by_strategy:
            by_strategy[s].append(r)

    for s in strategies:
        rows = by_strategy.get(s) or []
        n = len(rows)
        lane_present_n = sum(1 for r in rows if r.get("lane_present") == "1")
        hit_any_n = sum(1 for r in rows if r.get("hit_any") == "1")
        hit_inc_n = sum(1 for r in rows if r.get("hit_any_inclusive") == "1")
        in_pack_idx_n = sum(1 for r in rows if r.get("winner_in_pack_indices") == "1")

        ranks_m = [int(r["lane_rank_methods_first"]) if r.get("lane_rank_methods_first") else None for r in rows]
        ranks_p = [int(r["lane_rank_packs_first"]) if r.get("lane_rank_packs_first") else None for r in rows]
        ranks_s = [int(r["lane_rank_score_total_first"]) if r.get("lane_rank_score_total_first") else None for r in rows]

        def trio_leq(t: int) -> str:
            return f"{_pct(_count_leq(ranks_m, t), n)}/{_pct(_count_leq(ranks_p, t), n)}/{_pct(_count_leq(ranks_s, t), n)}"

        lines.append(
            "| "
            + " | ".join(
                [
                    s,
                    str(n),
                    _pct(lane_present_n, n),
                    _pct(hit_any_n, n),
                    _pct(hit_inc_n, n),
                    _pct(in_pack_idx_n, n),
                    trio_leq(1),
                    trio_leq(2),
                    trio_leq(3),
                    trio_leq(5),
                    trio_leq(10),
                ]
            )
            + " |"
        )

    lines.append("")
    lines.append("Notes:")
    lines.append("- `lane_present` means the winner VTRAC index appears in lane evidence within the scan limit.")
    lines.append("- Rank columns show `methods_first/packs_first/score_total_first` side-by-side.")
    lines.append("")

    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
