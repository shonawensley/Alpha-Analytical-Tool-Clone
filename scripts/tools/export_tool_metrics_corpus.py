#!/usr/bin/env python3
"""
Export a machine-readable, numeric corpus from sharepack summary.json files.

Why:
  - `docs/.../RUNS/corpus_summary.csv` is derived from narrative run reports and is
    intentionally human-first.
  - For "superbrain" work we also need *numeric evidence* to quantify:
      - tool coverage vs rank vs strength,
      - cross-variant (Combined/Midday/Evening) contribution,
      - and simple outcome metadata (double/triple/mirror-double).

Scope:
  - Reporting/instrumentation only. Does NOT change any analyzer behavior.
  - Reads from sharepack SSOT summaries:
      sharepacks/<D>/<STATE>/*/<STATE>/summary.json
      sharepacks/<D>/control_center/meta.json

Usage:
  python3 scripts/tools/export_tool_metrics_corpus.py --dates 2025-12-30 2025-12-31 2026-01-01
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def canonical_of_literal(literal: str) -> str:
    literal = normalize_pick3_literal(literal)
    return "".join(sorted(literal)) if literal else ""


def is_double(literal: str) -> bool:
    literal = normalize_pick3_literal(literal)
    return len(set(literal)) == 2 if len(literal) == 3 else False


def is_triple(literal: str) -> bool:
    literal = normalize_pick3_literal(literal)
    return len(set(literal)) == 1 if len(literal) == 3 else False


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def safe_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except Exception:
        return None


def safe_float(value: Any) -> Optional[float]:
    try:
        if value is None:
            return None
        return float(value)
    except Exception:
        return None


def safe_bool(value: Any) -> Optional[bool]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        if value.strip().lower() in {"true", "t", "1", "yes", "y"}:
            return True
        if value.strip().lower() in {"false", "f", "0", "no", "n"}:
            return False
    return None


def iter_sharepack_days(*, root: Path, dates: List[str] | None) -> Iterable[Tuple[str, Path]]:
    sharepacks_dir = root / "sharepacks"
    if dates is not None:
        for date in dates:
            day_dir = sharepacks_dir / date
            if day_dir.exists():
                yield date, day_dir
        return

    for day_dir in sorted(sharepacks_dir.iterdir(), key=lambda p: p.name):
        if not day_dir.is_dir():
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day_dir.name):
            continue
        if not (day_dir / "control_center" / "meta.json").exists():
            continue
        yield day_dir.name, day_dir


@dataclass(frozen=True)
class ResultsEntry:
    canonical_state: str
    midday: str | None
    evening: str | None


def load_results_for_day(*, date: str) -> Tuple[Dict[str, ResultsEntry], Dict[str, str]]:
    """
    Returns:
      - results_by_canonical: canonical_state -> ResultsEntry(midday, evening)
      - project_to_canonical: project_state_label -> canonical_state
    """
    results_path = ROOT / "data" / "results" / f"{date}.txt"
    try:
        from alpha_analytical.control_center import batch_runner as br
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"Failed to import batch_runner.parse_winner_sheet: {exc}")

    text = results_path.read_text(encoding="utf-8", errors="replace") if results_path.exists() else ""
    entries = br.parse_winner_sheet(text) if text else []

    results_by_canonical: Dict[str, ResultsEntry] = {}
    for entry in entries:
        results_by_canonical[entry.canonical] = ResultsEntry(
            canonical_state=entry.canonical,
            midday=normalize_pick3_literal(entry.midday or "") or None,
            evening=normalize_pick3_literal(entry.evening or "") or None,
        )

    project_to_canonical: Dict[str, str] = {}
    for canonical, candidates in getattr(br, "_PROJECT_STATE_CANDIDATES", {}).items():
        for candidate in candidates:
            project_to_canonical[candidate] = canonical

    return results_by_canonical, project_to_canonical


def pick_stable_winner_block(stable_summary: Dict[str, Any], *, label: str) -> Dict[str, Any] | None:
    for w in stable_summary.get("winners", []) or []:
        if w.get("label") == label:
            return w
    return None


def pick_hot_zones_winner_block(hz_summary: Dict[str, Any], *, label: str) -> Dict[str, Any] | None:
    for w in hz_summary.get("winners", []) or []:
        if w.get("label") == label:
            return w
    return None


def pick_dr_winner_block(dr_summary: Dict[str, Any], *, variant: str) -> Dict[str, Any] | None:
    for w in dr_summary.get("winners", []) or []:
        if w.get("variant") == variant:
            return w
    return None


def pick_vtrac_winner_rows(vtrac_summary: Dict[str, Any], *, winner_combo: str) -> Tuple[Dict[str, Any] | None, Dict[str, Any] | None]:
    winner_combo = normalize_pick3_literal(winner_combo)
    wl = None
    for row in vtrac_summary.get("winners_lens", []) or []:
        if normalize_pick3_literal(str(row.get("winner_combo") or "")) == winner_combo:
            wl = row
            break

    placement = None
    for row in vtrac_summary.get("winner_index_placements", []) or []:
        if normalize_pick3_literal(str(row.get("winner_combo") or "")) == winner_combo:
            placement = row
            break

    return wl, placement


def find_top_index_row(vtrac_summary: Dict[str, Any], *, index: int) -> Tuple[int | None, Dict[str, Any] | None]:
    rows = vtrac_summary.get("top_indices", []) or []
    for i, row in enumerate(rows):
        if safe_int(row.get("index")) == index:
            return i + 1, row  # 1-based rank within top_indices list
    return None, None


def aux_repeat_watch_row(aux_summary: Dict[str, Any], *, variant: str) -> Dict[str, Any]:
    rw = aux_summary.get("repeat_watch") or {}
    return rw.get(variant.lower()) if isinstance(rw, dict) else {}


def blackapple_top_list(aux_summary: Dict[str, Any], *, variant: str) -> List[Dict[str, Any]]:
    ba = aux_summary.get("blackapple") or {}
    top_by_variant = ba.get("top_by_variant") if isinstance(ba, dict) else None
    if not isinstance(top_by_variant, dict):
        return []
    value = top_by_variant.get(variant.lower())
    return value if isinstance(value, list) else []


def blackapple_winner_rank(top_list: List[Dict[str, Any]], *, winner: str) -> Tuple[bool | None, int | None]:
    winner = normalize_pick3_literal(winner)
    if not winner:
        return None, None
    for i, row in enumerate(top_list, start=1):
        combo = normalize_pick3_literal(str(row.get("combo") or ""))
        if combo == winner:
            return True, i
    return False, None


def vtrac_signature_of_literal(literal: str) -> str:
    # Mirror pairs collapse under mod-5 (0<->5,1<->6,...).
    literal = normalize_pick3_literal(literal)
    if len(literal) != 3:
        return ""
    try:
        ds = [int(ch) % 5 for ch in literal]
    except Exception:
        return ""
    return "".join(map(str, sorted(ds)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dates", nargs="*", help="Results dates D to export (default: infer from sharepacks/*).")
    ap.add_argument(
        "--out",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "corpus_tool_metrics.csv"),
        help="Output CSV path (default: RUNS/corpus_tool_metrics.csv)",
    )
    args = ap.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "date",
        "history_date",
        "state",
        "canonical_state",
        "period",
        "winner_literal",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_is_double",
        "winner_is_triple",
        "winner_vtrac_signature",
        "winner_vtrac_signature_has_repeat",
        # Stable
        "stable_families_present",
        "stable_families_best_rank",
        "stable_families_rank_fraction",
        "stable_families_section",
        "stable_scores_present",
        "stable_compound_present",
        "stable_exact_boxed",
        "stable_exact_straight",
        "stable_vt_boxed_count",
        # Hot Zones
        "hz_top_lanes_present",
        "hz_top_lanes_best_rank",
        "hz_top_lanes_rank_fraction",
        "hz_top_lanes_rows_total",
        # Digit Reduction
        "dr_stamp_items_total",
        "dr_stamp_vtrac_any",
        "dr_stamp_family_vtrac_any",
        "dr_per_item_present",
        "dr_best_area_rank_vtrac_any",
        "dr_top_winner_present",
        "dr_top_winner_best_rank",
        # VTRAC
        "vtrac_index_rank",
        "vtrac_index_rank_fraction",
        "vtrac_score_ratio_to_top",
        "vtrac_top10_rank",
        "vtrac_top10_sections",
        "vtrac_top10_mirror_supported",
        # Aux
        "aux_repeat_current_index",
        "aux_repeat_current_streak",
        "aux_repeat_last_repeat_gap",
        "blackapple_top_contains_winner",
        "blackapple_winner_rank",
    ]

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for date, day_dir in iter_sharepack_days(root=ROOT, dates=args.dates):
            results_by_canonical, project_to_canonical = load_results_for_day(date=date)

            meta = {}
            meta_path = day_dir / "control_center" / "meta.json"
            if meta_path.exists():
                try:
                    meta = load_json(meta_path)
                except Exception:
                    meta = {}
            history_date = str(meta.get("history_date") or "")

            state_dirs = sorted([p for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"], key=lambda p: p.name)
            for state_dir in state_dirs:
                state = state_dir.name
                canonical_state = project_to_canonical.get(state, state)
                res = results_by_canonical.get(canonical_state)
                midday = res.midday if res else None
                evening = res.evening if res else None

                # Load tool summaries once per state/day.
                stable_path = state_dir / "stable" / state / "summary.json"
                hz_path = state_dir / "hot_zones" / state / "summary.json"
                dr_path = state_dir / "digit_reduction" / state / "summary.json"
                vtrac_path = state_dir / "vtrac" / state / "summary.json"
                aux_path = state_dir / "aux" / state / "summary.json"

                stable_summary = load_json(stable_path) if stable_path.exists() else {}
                hz_summary = load_json(hz_path) if hz_path.exists() else {}
                dr_summary = load_json(dr_path) if dr_path.exists() else {}
                vtrac_summary = load_json(vtrac_path) if vtrac_path.exists() else {}
                aux_summary = load_json(aux_path) if aux_path.exists() else {}

                for period, winner in [("Midday", midday), ("Evening", evening)]:
                    winner_literal = normalize_pick3_literal(winner or "")
                    winner_canonical = canonical_of_literal(winner_literal)

                    row: Dict[str, Any] = {k: "" for k in fields}
                    row["date"] = date
                    row["history_date"] = history_date
                    row["state"] = state
                    row["canonical_state"] = canonical_state
                    row["period"] = period
                    row["winner_literal"] = winner_literal
                    row["winner_canonical"] = winner_canonical
                    row["winner_is_double"] = "1" if is_double(winner_literal) else "0" if winner_literal else ""
                    row["winner_is_triple"] = "1" if is_triple(winner_literal) else "0" if winner_literal else ""
                    sig = vtrac_signature_of_literal(winner_literal)
                    row["winner_vtrac_signature"] = sig
                    row["winner_vtrac_signature_has_repeat"] = "1" if sig and len(set(sig)) < 3 else "0" if sig else ""

                    # Stable
                    sw = pick_stable_winner_block(stable_summary, label=period) if stable_summary else None
                    if sw:
                        fam = sw.get("families") or {}
                        row["stable_families_present"] = "1" if safe_bool(fam.get("present")) else "0"
                        row["stable_families_best_rank"] = safe_int(fam.get("best_rank")) or ""
                        row["stable_families_rank_fraction"] = safe_float(fam.get("winner_rank_fraction")) or ""
                        row["stable_families_section"] = fam.get("section") or ""

                        row["stable_scores_present"] = "1" if safe_bool((sw.get("scores") or {}).get("present")) else "0"
                        row["stable_compound_present"] = "1" if safe_bool((sw.get("compound") or {}).get("present")) else "0"

                        mh = sw.get("metrics_hits") or {}
                        row["stable_exact_boxed"] = "1" if safe_bool(mh.get("exact_boxed")) else "0"
                        row["stable_exact_straight"] = "1" if safe_bool(mh.get("exact_straight")) else "0"
                        row["stable_vt_boxed_count"] = safe_int(mh.get("vt_boxed_count")) or ""

                    # Hot Zones
                    hw = pick_hot_zones_winner_block(hz_summary, label=period) if hz_summary else None
                    if hw:
                        tl = hw.get("top_lanes") or {}
                        row["hz_top_lanes_present"] = "1" if safe_bool(tl.get("present")) else "0"
                        row["hz_top_lanes_best_rank"] = safe_int(tl.get("best_rank")) or ""
                        row["hz_top_lanes_rank_fraction"] = safe_float(tl.get("winner_rank_fraction")) or ""
                        row["hz_top_lanes_rows_total"] = safe_int(tl.get("rows_total")) or ""

                    # Digit Reduction
                    dw = pick_dr_winner_block(dr_summary, variant=period) if dr_summary else None
                    if dw:
                        stamp = dw.get("stamp") or {}
                        counts = stamp.get("counts") if isinstance(stamp, dict) else {}
                        if isinstance(counts, dict):
                            row["dr_stamp_items_total"] = safe_int(counts.get("items_total")) or ""
                            row["dr_stamp_vtrac_any"] = safe_int(counts.get("vtrac_any")) or ""
                            row["dr_stamp_family_vtrac_any"] = safe_int(counts.get("family_vtrac_any")) or ""

                        per_item = dw.get("per_item") or {}
                        row["dr_per_item_present"] = "1" if safe_bool(per_item.get("present")) else "0"
                        row["dr_best_area_rank_vtrac_any"] = safe_int(per_item.get("best_area_rank_vtrac_any")) or safe_int(per_item.get("best_area_rank_vtrac_any".replace("_vtrac_", "_"))) or ""

                        top = dw.get("top") or {}
                        row["dr_top_winner_present"] = "1" if safe_bool(top.get("winner_present")) else "0"
                        row["dr_top_winner_best_rank"] = safe_int(top.get("winner_best_rank")) or ""

                    # VTRAC
                    wl, placement = pick_vtrac_winner_rows(vtrac_summary, winner_combo=winner_literal) if vtrac_summary else (None, None)
                    if wl:
                        row["winner_vtrac_index"] = safe_int(wl.get("index")) or ""
                    if placement:
                        row["winner_vtrac_index"] = row["winner_vtrac_index"] or (safe_int(placement.get("index")) or "")
                        row["vtrac_index_rank"] = safe_int(placement.get("index_rank")) or ""
                        row["vtrac_index_rank_fraction"] = safe_float(placement.get("rank_fraction")) or ""
                        row["vtrac_score_ratio_to_top"] = safe_float(placement.get("score_ratio_to_top")) or ""

                    winner_index = safe_int(row["winner_vtrac_index"]) if row["winner_vtrac_index"] else None
                    if winner_index is not None:
                        top10_rank, top_row = find_top_index_row(vtrac_summary, index=winner_index)
                        if top10_rank is not None:
                            row["vtrac_top10_rank"] = top10_rank
                        if top_row:
                            evidence = top_row.get("evidence") or {}
                            raw = evidence.get("raw") if isinstance(evidence, dict) else {}
                            sections = raw.get("sections") if isinstance(raw, dict) else None
                            if isinstance(sections, list):
                                row["vtrac_top10_sections"] = "|".join([str(s) for s in sections])
                            row["vtrac_top10_mirror_supported"] = "1" if safe_bool(raw.get("mirror_supported") if isinstance(raw, dict) else None) else "0"

                    # Aux (repeat watch + BA top list membership)
                    rw = aux_repeat_watch_row(aux_summary, variant=period)
                    if isinstance(rw, dict):
                        row["aux_repeat_current_index"] = safe_int(rw.get("current_index")) or ""
                        row["aux_repeat_current_streak"] = safe_int(rw.get("current_streak")) or ""
                        row["aux_repeat_last_repeat_gap"] = safe_int(rw.get("last_repeat_gap")) or ""

                    top_list = blackapple_top_list(aux_summary, variant=period)
                    present, rank = blackapple_winner_rank(top_list, winner=winner_literal) if top_list else (None, None)
                    if present is not None:
                        row["blackapple_top_contains_winner"] = "1" if present else "0"
                    if rank is not None:
                        row["blackapple_winner_rank"] = rank

                    writer.writerow(row)


if __name__ == "__main__":
    main()

