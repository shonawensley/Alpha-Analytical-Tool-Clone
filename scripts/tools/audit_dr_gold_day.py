#!/usr/bin/env python3
"""
Winner-aware Digit Reduction gold-day audit.

Why this exists:
  - `DR Arena v1.1` now preserves richer predictive-side structure, but the next
    optimization phase needs a frozen, winner-aware scoreboard across the gold-day
    windows.
  - The historical sharepacks already contain:
      * DR per-item/top/meta/training artifacts
      * DR winner stamps / hits / flags / overlays
      * winners HTML/JSON artifacts with structured table cells and tags
  - This script joins those into one reusable audit report.

What it measures:
  - whether the winning literal / VTRAC family shows up in DR receipts
  - whether the winner-family corridor is visibly present in the structured winners JSON
  - whether `DR Arena v1.1` top trace / corridor / double layers align to the winner VTRAC lane
  - whether the DR summary looks empty even though the winners tables are structurally active

Scope:
  - reporting / instrumentation only
  - does not change analyzer behavior
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import itertools
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from modules.vtrac_reference import get_vtrac_index  # noqa: E402
from scripts.tools.dr_arena import build_dr_arena_payload  # noqa: E402


SIGNAL_TAGS = {
    "hit-winner",
    "hit-winner-gap",
    "hit-family",
    "hit-family-gap",
    "hit-vt-straight",
    "hit-vt-straight-gap",
}

STRICT_SIGNAL_TAGS = {
    "hit-winner",
    "hit-family",
    "hit-vt-straight",
}

GAP_SIGNAL_TAGS = {
    "hit-winner-gap",
    "hit-family-gap",
    "hit-vt-straight-gap",
}


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def daterange(start: str, end: str) -> List[str]:
    cur = parse_date(start)
    stop = parse_date(end)
    if stop < cur:
        raise SystemExit("--end must be >= --start")
    out: List[str] = []
    while cur <= stop:
        out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def normalize_pick3_literal(value: Any) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def canonical_of_literal(value: Any) -> str:
    literal = normalize_pick3_literal(value)
    return "".join(sorted(literal)) if literal else ""


def permutations_of_winner(value: str) -> set[str]:
    literal = normalize_pick3_literal(value)
    if len(literal) != 3:
        return set()
    return {"".join(p) for p in itertools.permutations(literal, 3)}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _to_int(value: Any, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)


def _extract_stamp_from_name(name: str) -> str:
    match = re.search(r"_(\d{8}_\d{6})", name)
    return match.group(1) if match else ""


def _detect_latest_dr_stamp(winners_dir: Path) -> Optional[str]:
    stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_stamp.json")})
    if not stamps:
        return None
    return stamps[-1]


def _select_latest_winner_json(winners_dir: Path, winner_literal: str) -> Optional[Path]:
    winner_literal = normalize_pick3_literal(winner_literal)
    candidates = sorted(winners_dir.glob(f"*_winner_{winner_literal}_*.json"))
    if not candidates:
        return None

    def _key(path: Path) -> Tuple[str, str]:
        try:
            data = load_json(path)
            stamp = str(data.get("timestamp") or "")
        except Exception:
            stamp = ""
        if not re.fullmatch(r"\d{8}_\d{6}", stamp):
            stamp = _extract_stamp_from_name(path.name)
        return (stamp, path.name)

    return sorted(candidates, key=_key)[-1]


def _winner_json_status(winners_dir: Path, winner_literal: str, winner_json_path: Optional[Path]) -> str:
    if winner_json_path is not None:
        return "matched_literal"
    if not winners_dir.exists():
        return "missing_dir"
    if any(winners_dir.glob("*_winner_*.json")):
        return "unmatched_literal"
    return "missing_files"


def _winner_json_stats_ranks(data: Dict[str, Any], *, winner_literal: str) -> Dict[str, Any]:
    winner_literal = normalize_pick3_literal(winner_literal)
    winner_perms = permutations_of_winner(winner_literal)
    family = {normalize_pick3_literal(v) for v in data.get("patterns") or [] if len(normalize_pick3_literal(v)) == 3}

    out: Dict[str, Any] = {
        "best_literal_rank": None,
        "best_perm_rank": None,
        "best_family_rank": None,
        "best_family_token": None,
        "best_metric": None,
        "best_family_metric": None,
    }

    for metric, mapping in (data.get("stats") or {}).items():
        if not isinstance(mapping, dict) or not mapping:
            continue
        ordered: List[Tuple[str, float]] = []
        for raw_key, raw_value in mapping.items():
            token = normalize_pick3_literal(raw_key)
            if len(token) != 3:
                continue
            try:
                value = float(raw_value)
            except Exception:
                continue
            ordered.append((token, value))
        if not ordered:
            continue
        ordered.sort(key=lambda kv: (-kv[1], kv[0]))
        ranks = {token: idx for idx, (token, _) in enumerate(ordered, start=1)}

        literal_rank = ranks.get(winner_literal)
        if literal_rank is not None and (out["best_literal_rank"] is None or literal_rank < out["best_literal_rank"]):
            out["best_literal_rank"] = literal_rank
            out["best_metric"] = metric

        perm_ranks = [ranks[token] for token in winner_perms if token in ranks]
        if perm_ranks:
            best_perm_rank = min(perm_ranks)
            if out["best_perm_rank"] is None or best_perm_rank < out["best_perm_rank"]:
                out["best_perm_rank"] = best_perm_rank
                out["best_metric"] = metric

        family_hits = [(token, ranks[token]) for token in family if token in ranks]
        if family_hits:
            best_token, best_family_rank = sorted(family_hits, key=lambda item: (item[1], item[0]))[0]
            if out["best_family_rank"] is None or best_family_rank < out["best_family_rank"]:
                out["best_family_rank"] = best_family_rank
                out["best_family_token"] = best_token
                out["best_family_metric"] = metric

    return out


def _analyze_winner_json(data: Dict[str, Any]) -> Dict[str, Any]:
    counts = Counter()
    variants_with_signal: set[str] = set()
    ls_variants_with_signal: set[str] = set()
    rowtypes_with_ls_signal: set[str] = set()
    signal_variants_by_kind: Dict[str, set[str]] = defaultdict(set)

    for variant, rows in (data.get("tables") or {}).items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            row_type = str(row.get("RowType") or "")
            cells = row.get("cells") or {}
            if not isinstance(cells, dict):
                continue
            for cell in cells.values():
                if not isinstance(cell, dict):
                    continue
                tags = set(cell.get("tags") or [])
                if not tags:
                    continue
                is_ls = "ls-box" in tags or "ls-box-edge" in tags
                has_signal = bool(tags & SIGNAL_TAGS)
                if is_ls:
                    counts["ls_box_cells"] += 1
                if has_signal:
                    counts["signal_cells"] += 1
                    variants_with_signal.add(variant)
                if has_signal and is_ls:
                    counts["ls_signal_cells"] += 1
                    ls_variants_with_signal.add(variant)
                    if row_type:
                        rowtypes_with_ls_signal.add(row_type)
                if "hit-winner" in tags:
                    counts["winner_strict_cells"] += 1
                    signal_variants_by_kind["winner"].add(variant)
                if "hit-winner-gap" in tags:
                    counts["winner_gap_cells"] += 1
                    signal_variants_by_kind["winner"].add(variant)
                if "hit-family" in tags:
                    counts["family_strict_cells"] += 1
                    signal_variants_by_kind["family"].add(variant)
                if "hit-family-gap" in tags:
                    counts["family_gap_cells"] += 1
                    signal_variants_by_kind["family"].add(variant)
                if "hit-vt-straight" in tags:
                    counts["vt_straight_strict_cells"] += 1
                    signal_variants_by_kind["vt_straight"].add(variant)
                if "hit-vt-straight-gap" in tags:
                    counts["vt_straight_gap_cells"] += 1
                    signal_variants_by_kind["vt_straight"].add(variant)

    strict_total = (
        counts["winner_strict_cells"]
        + counts["family_strict_cells"]
        + counts["vt_straight_strict_cells"]
    )
    gap_total = (
        counts["winner_gap_cells"]
        + counts["family_gap_cells"]
        + counts["vt_straight_gap_cells"]
    )
    signal_score = (
        2.0 * strict_total
        + 1.0 * gap_total
        + 1.5 * counts["ls_signal_cells"]
        + 2.0 * len(variants_with_signal)
        + 1.0 * len(ls_variants_with_signal)
    )
    if counts["ls_signal_cells"] >= 6 or signal_score >= 18 or (len(ls_variants_with_signal) >= 2 and gap_total >= 6):
        signal_class = "strong"
    elif counts["ls_signal_cells"] >= 2 or signal_score >= 8 or gap_total >= 4:
        signal_class = "moderate"
    elif counts["signal_cells"] > 0:
        signal_class = "mild"
    else:
        signal_class = "none"

    return {
        "winner_strict_cells": int(counts["winner_strict_cells"]),
        "winner_gap_cells": int(counts["winner_gap_cells"]),
        "family_strict_cells": int(counts["family_strict_cells"]),
        "family_gap_cells": int(counts["family_gap_cells"]),
        "vt_straight_strict_cells": int(counts["vt_straight_strict_cells"]),
        "vt_straight_gap_cells": int(counts["vt_straight_gap_cells"]),
        "ls_box_cells": int(counts["ls_box_cells"]),
        "signal_cells": int(counts["signal_cells"]),
        "ls_signal_cells": int(counts["ls_signal_cells"]),
        "variants_with_signal": len(variants_with_signal),
        "ls_variants_with_signal": len(ls_variants_with_signal),
        "rowtypes_with_ls_signal": sorted(rowtypes_with_ls_signal),
        "signal_variants_winner": len(signal_variants_by_kind["winner"]),
        "signal_variants_family": len(signal_variants_by_kind["family"]),
        "signal_variants_vt_straight": len(signal_variants_by_kind["vt_straight"]),
        "signal_score": round(signal_score, 3),
        "signal_class": signal_class,
    }


def _winner_rank_for_family_rows(rows: Sequence[Dict[str, Any]], *, winner_canon: str, winner_vtrac_index: Optional[int]) -> Tuple[Optional[int], Optional[int]]:
    canon_rank: Optional[int] = None
    vtrac_rank: Optional[int] = None
    for idx, row in enumerate(rows, start=1):
        family_id = canonical_of_literal(row.get("family_id"))
        if canon_rank is None and family_id and family_id == winner_canon:
            canon_rank = idx
        if vtrac_rank is None and winner_vtrac_index is not None and family_id and get_vtrac_index(family_id) == winner_vtrac_index:
            vtrac_rank = idx
        if canon_rank is not None and vtrac_rank is not None:
            break
    return canon_rank, vtrac_rank


def _winner_rank_for_pattern_rows(rows: Sequence[Dict[str, Any]], *, winner_canon: str, winner_vtrac_index: Optional[int]) -> Tuple[Optional[int], Optional[int]]:
    canon_rank: Optional[int] = None
    vtrac_rank: Optional[int] = None
    for idx, row in enumerate(rows, start=1):
        token = normalize_pick3_literal(row.get("pattern") or row.get("best_pattern") or row.get("value"))
        canon = canonical_of_literal(token)
        if canon_rank is None and canon and canon == winner_canon:
            canon_rank = idx
        if vtrac_rank is None and winner_vtrac_index is not None and token and get_vtrac_index(token) == winner_vtrac_index:
            vtrac_rank = idx
        if canon_rank is not None and vtrac_rank is not None:
            break
    return canon_rank, vtrac_rank


def _winner_rank_for_index_rows(rows: Sequence[Dict[str, Any]], *, winner_vtrac_index: Optional[int]) -> Optional[int]:
    if winner_vtrac_index is None:
        return None
    for idx, row in enumerate(rows, start=1):
        if int(row.get("vtrac_index") or -1) == int(winner_vtrac_index):
            return idx
    return None


def _winner_rank_for_gateway_rows(rows: Sequence[Dict[str, Any]], *, winner_vtrac_index: Optional[int]) -> Optional[int]:
    return _winner_rank_for_index_rows(rows, winner_vtrac_index=winner_vtrac_index)


def _winner_rank_for_cluster_rows(rows: Sequence[Dict[str, Any]], *, winner_vtrac_index: Optional[int]) -> Optional[int]:
    return _winner_rank_for_index_rows(rows, winner_vtrac_index=winner_vtrac_index)


def _winner_score_for_index_rows(
    rows: Sequence[Dict[str, Any]],
    *,
    winner_vtrac_index: Optional[int],
    score_key: str,
) -> Optional[float]:
    if winner_vtrac_index is None:
        return None
    for row in rows:
        if int(row.get("vtrac_index") or -1) == int(winner_vtrac_index):
            try:
                return float(row.get(score_key) or 0.0)
            except Exception:
                return None
    return None


def _top_index_row_score(rows: Sequence[Dict[str, Any]], *, score_key: str) -> Tuple[Optional[int], Optional[float]]:
    if not rows:
        return None, None
    row = rows[0]
    try:
        score = float(row.get(score_key) or 0.0)
    except Exception:
        score = None
    return _to_int(row.get("vtrac_index"), -1), score


def _rank_band(rank: Optional[int]) -> str:
    if rank is None:
        return "unranked"
    if rank <= 3:
        return "top3"
    if rank <= 5:
        return "top5"
    if rank <= 8:
        return "top8"
    if rank <= 10:
        return "top10"
    if rank <= 20:
        return "top20"
    return "deep"


def _classify_overlay_mismatch(*, stamp_counts: Dict[str, Any], winner_json_signal: Dict[str, Any]) -> str:
    if str(winner_json_signal.get("signal_class") or "") == "unavailable":
        return "unavailable"
    any_total = int(stamp_counts.get("exact_any") or 0) + int(stamp_counts.get("vtrac_any") or 0) + int(stamp_counts.get("family_vtrac_any") or 0)
    if any_total > 0:
        return "none"
    signal_class = str(winner_json_signal.get("signal_class") or "none")
    if signal_class == "strong":
        return "strong"
    if signal_class == "moderate":
        return "moderate"
    if signal_class == "mild":
        return "mild"
    return "none"


def _derive_alignment_class(
    *,
    stamp_counts: Dict[str, Any],
    empty_class: str,
    winner_json_signal: Dict[str, Any],
    trace_canon_rank: Optional[int],
    trace_vtrac_rank: Optional[int],
    corridor_canon_rank: Optional[int],
    corridor_vtrac_rank: Optional[int],
    double_vtrac_rank: Optional[int],
    candidate_vtrac_rank: Optional[int],
    gateway_vtrac_rank: Optional[int],
    cluster_vtrac_rank: Optional[int],
    box_vtrac_rank: Optional[int],
) -> str:
    exact_any = int(stamp_counts.get("exact_any") or 0)
    vtrac_any = int(stamp_counts.get("vtrac_any") or 0)
    family_vtrac_any = int(stamp_counts.get("family_vtrac_any") or 0)

    if exact_any > 0 or (trace_canon_rank is not None and trace_canon_rank <= 3) or (corridor_canon_rank is not None and corridor_canon_rank <= 3):
        return "literal_capture"
    if (
        vtrac_any > 0
        or family_vtrac_any > 0
        or (trace_vtrac_rank is not None and trace_vtrac_rank <= 3)
        or (corridor_vtrac_rank is not None and corridor_vtrac_rank <= 3)
        or (double_vtrac_rank is not None and double_vtrac_rank <= 3)
        or (candidate_vtrac_rank is not None and candidate_vtrac_rank <= 3)
        or (gateway_vtrac_rank is not None and gateway_vtrac_rank <= 3)
        or (cluster_vtrac_rank is not None and cluster_vtrac_rank <= 3)
        or (box_vtrac_rank is not None and box_vtrac_rank <= 3)
    ):
        return "vtrac_capture"
    if empty_class == "true_empty" and winner_json_signal.get("signal_class") == "none":
        return "true_empty"
    if int(stamp_counts.get("items_total") or 0) == 0 and winner_json_signal.get("signal_class") in {"strong", "moderate"}:
        return "false_empty"
    if empty_class == "active_low_trust":
        return "active_low_trust"
    return "miss"


def _iter_state_dirs(day_dir: Path) -> Iterable[Tuple[str, Path]]:
    for child in sorted(day_dir.iterdir(), key=lambda p: p.name):
        if not child.is_dir():
            continue
        if child.name == "control_center":
            continue
        if (child / "digit_reduction" / child.name).exists():
            yield child.name, child


def _date_rows_payload(day_dir: Path, *, profile: str, experiment_tag: str) -> Iterable[Dict[str, Any]]:
    meta_path = day_dir / "control_center" / "meta.json"
    meta = load_json(meta_path) if meta_path.exists() else {}
    results_date = day_dir.name
    history_date = meta.get("history_date")

    for state_key, state_dir in _iter_state_dirs(day_dir):
        payload = build_dr_arena_payload(
            state_dir=state_dir,
            state_key=state_key,
            results_date=results_date,
            history_date=history_date,
            profile=profile,
            experiment_tag=experiment_tag,
            sharepacks_root=ROOT / "sharepacks",
            contains_winners_artifacts=True,
            repo_root=ROOT,
            top_trace=20,
            top_lane=20,
            top_competing=20,
            top_double=20,
            top_vtrac_gateway=20,
            top_vtrac_cluster=20,
            top_assigned_box_vtrac=20,
        )
        if payload is None:
            continue

        dr_winners_dir = state_dir / "digit_reduction" / state_key / "analyzer_v2" / "winners"
        latest_stamp = _detect_latest_dr_stamp(dr_winners_dir)
        winners_json_dir = state_dir / "winners" / state_key

        for variant in ("Midday", "Evening"):
            if latest_stamp is None:
                continue
            stamp_path = dr_winners_dir / f"{latest_stamp}_{variant}_winner_stamp.json"
            if not stamp_path.exists():
                continue
            stamp_data = load_json(stamp_path)
            winner_literal = normalize_pick3_literal(stamp_data.get("winner"))
            if len(winner_literal) != 3:
                continue
            winner_canon = canonical_of_literal(winner_literal)
            winner_vtrac_index = get_vtrac_index(winner_literal)

            winner_json_path = _select_latest_winner_json(winners_json_dir, winner_literal) if winners_json_dir.exists() else None
            winner_json_status = _winner_json_status(winners_json_dir, winner_literal, winner_json_path)
            winner_json = load_json(winner_json_path) if winner_json_path else {}
            if winner_json_path:
                winner_json_signal = _analyze_winner_json(winner_json)
                winner_json_ranks = _winner_json_stats_ranks(winner_json, winner_literal=winner_literal)
            else:
                winner_json_signal = {
                    "winner_strict_cells": 0,
                    "winner_gap_cells": 0,
                    "family_strict_cells": 0,
                    "family_gap_cells": 0,
                    "vt_straight_strict_cells": 0,
                    "vt_straight_gap_cells": 0,
                    "ls_box_cells": 0,
                    "signal_cells": 0,
                    "ls_signal_cells": 0,
                    "variants_with_signal": 0,
                    "ls_variants_with_signal": 0,
                    "rowtypes_with_ls_signal": [],
                    "signal_variants_winner": 0,
                    "signal_variants_family": 0,
                    "signal_variants_vt_straight": 0,
                    "signal_score": 0.0,
                    "signal_class": "unavailable",
                }
                winner_json_ranks = {}

            section = payload.get("sections", {}).get(variant) or {}
            summary = dict(section.get("summary") or {})
            trace_rows = list(section.get("dr_trace_strength") or [])
            corridor_rows = list(section.get("dr_corridor_strength") or [])
            double_rows = list(section.get("dr_double_pressure") or [])
            gateway_rows = list(section.get("dr_vtrac_lane_gateway") or [])
            cluster_rows = list(section.get("dr_vtrac_cluster_strength") or [])
            box_rows = list(section.get("dr_assigned_box_vtrac_strength") or [])
            fusion_rows = list(section.get("dr_vtrac_fusion_strength") or [])
            candidate_rows = list(summary.get("top_candidate_preview") or [])
            empty_lens = dict(section.get("dr_empty_lens") or {})
            stamp_counts = dict(stamp_data.get("counts") or {})
            stamp_counts.setdefault("items_total", 0)

            trace_canon_rank, trace_vtrac_rank = _winner_rank_for_family_rows(
                trace_rows,
                winner_canon=winner_canon,
                winner_vtrac_index=winner_vtrac_index,
            )
            corridor_canon_rank, corridor_vtrac_rank = _winner_rank_for_family_rows(
                corridor_rows,
                winner_canon=winner_canon,
                winner_vtrac_index=winner_vtrac_index,
            )
            _, double_vtrac_rank = _winner_rank_for_pattern_rows(
                double_rows,
                winner_canon=winner_canon,
                winner_vtrac_index=winner_vtrac_index,
            )
            _, candidate_vtrac_rank = _winner_rank_for_pattern_rows(
                candidate_rows,
                winner_canon=winner_canon,
                winner_vtrac_index=winner_vtrac_index,
            )
            gateway_vtrac_rank = _winner_rank_for_gateway_rows(
                gateway_rows,
                winner_vtrac_index=winner_vtrac_index,
            )
            cluster_vtrac_rank = _winner_rank_for_cluster_rows(
                cluster_rows,
                winner_vtrac_index=winner_vtrac_index,
            )
            box_vtrac_rank = _winner_rank_for_index_rows(
                box_rows,
                winner_vtrac_index=winner_vtrac_index,
            )
            fusion_vtrac_rank = _winner_rank_for_index_rows(
                fusion_rows,
                winner_vtrac_index=winner_vtrac_index,
            )
            gateway_winner_score = _winner_score_for_index_rows(
                gateway_rows,
                winner_vtrac_index=winner_vtrac_index,
                score_key="gateway_score",
            )
            cluster_winner_score = _winner_score_for_index_rows(
                cluster_rows,
                winner_vtrac_index=winner_vtrac_index,
                score_key="cluster_score",
            )
            box_winner_score = _winner_score_for_index_rows(
                box_rows,
                winner_vtrac_index=winner_vtrac_index,
                score_key="assigned_box_score",
            )
            fusion_winner_score = _winner_score_for_index_rows(
                fusion_rows,
                winner_vtrac_index=winner_vtrac_index,
                score_key="fusion_score",
            )
            gateway_top_index, gateway_top_score = _top_index_row_score(
                gateway_rows,
                score_key="gateway_score",
            )
            cluster_top_index, cluster_top_score = _top_index_row_score(
                cluster_rows,
                score_key="cluster_score",
            )
            box_top_index, box_top_score = _top_index_row_score(
                box_rows,
                score_key="assigned_box_score",
            )
            fusion_top_index, fusion_top_score = _top_index_row_score(
                fusion_rows,
                score_key="fusion_score",
            )
            visible_ranks = [
                rank
                for rank in (
                    trace_vtrac_rank,
                    corridor_vtrac_rank,
                    double_vtrac_rank,
                    candidate_vtrac_rank,
                    gateway_vtrac_rank,
                    cluster_vtrac_rank,
                    box_vtrac_rank,
                    fusion_vtrac_rank,
                )
                if rank is not None
            ]
            best_surface_vtrac_rank = min(visible_ranks) if visible_ranks else None

            mismatch_class = _classify_overlay_mismatch(
                stamp_counts=stamp_counts,
                winner_json_signal=winner_json_signal,
            )
            alignment_class = _derive_alignment_class(
                stamp_counts=stamp_counts,
                empty_class=str(empty_lens.get("classification") or "unknown"),
                winner_json_signal=winner_json_signal,
                trace_canon_rank=trace_canon_rank,
                trace_vtrac_rank=trace_vtrac_rank,
                corridor_canon_rank=corridor_canon_rank,
                corridor_vtrac_rank=corridor_vtrac_rank,
                double_vtrac_rank=double_vtrac_rank,
                candidate_vtrac_rank=candidate_vtrac_rank,
                gateway_vtrac_rank=gateway_vtrac_rank,
                cluster_vtrac_rank=cluster_vtrac_rank,
                box_vtrac_rank=box_vtrac_rank,
            )

            yield {
                "date": results_date,
                "history_date": history_date or "",
                "state": state_key,
                "variant": variant,
                "winner": winner_literal,
                "winner_canon": winner_canon,
                "winner_vtrac_index": winner_vtrac_index if winner_vtrac_index is not None else "",
                "items_total": int(stamp_counts.get("items_total") or 0),
                "exact_any": int(stamp_counts.get("exact_any") or 0),
                "vtrac_any": int(stamp_counts.get("vtrac_any") or 0),
                "family_vtrac_any": int(stamp_counts.get("family_vtrac_any") or 0),
                "exact_final": int(stamp_counts.get("exact_final") or 0),
                "vtrac_final": int(stamp_counts.get("vtrac_final") or 0),
                "family_vtrac_final": int(stamp_counts.get("family_vtrac_final") or 0),
                "empty_class": str(empty_lens.get("classification") or "unknown"),
                "empty_confidence": float(empty_lens.get("confidence") or 0.0),
                "trace_winner_canon_rank": trace_canon_rank or "",
                "trace_winner_vtrac_rank": trace_vtrac_rank or "",
                "corridor_winner_canon_rank": corridor_canon_rank or "",
                "corridor_winner_vtrac_rank": corridor_vtrac_rank or "",
                "double_winner_vtrac_rank": double_vtrac_rank or "",
                "candidate_winner_vtrac_rank": candidate_vtrac_rank or "",
                "gateway_winner_vtrac_rank": gateway_vtrac_rank or "",
                "cluster_winner_vtrac_rank": cluster_vtrac_rank or "",
                "box_winner_vtrac_rank": box_vtrac_rank or "",
                "fusion_winner_vtrac_rank": fusion_vtrac_rank or "",
                "gateway_winner_score": round(gateway_winner_score, 3) if gateway_winner_score is not None else "",
                "cluster_winner_score": round(cluster_winner_score, 3) if cluster_winner_score is not None else "",
                "box_winner_score": round(box_winner_score, 3) if box_winner_score is not None else "",
                "fusion_winner_score": round(fusion_winner_score, 3) if fusion_winner_score is not None else "",
                "gateway_top_vtrac_index": gateway_top_index if gateway_top_index is not None and gateway_top_index >= 0 else "",
                "cluster_top_vtrac_index": cluster_top_index if cluster_top_index is not None and cluster_top_index >= 0 else "",
                "box_top_vtrac_index": box_top_index if box_top_index is not None and box_top_index >= 0 else "",
                "fusion_top_vtrac_index": fusion_top_index if fusion_top_index is not None and fusion_top_index >= 0 else "",
                "gateway_top_score": round(gateway_top_score, 3) if gateway_top_score is not None else "",
                "cluster_top_score": round(cluster_top_score, 3) if cluster_top_score is not None else "",
                "box_top_score": round(box_top_score, 3) if box_top_score is not None else "",
                "fusion_top_score": round(fusion_top_score, 3) if fusion_top_score is not None else "",
                "gateway_score_gap": round((gateway_top_score or 0.0) - gateway_winner_score, 3)
                if gateway_top_score is not None and gateway_winner_score is not None
                else "",
                "cluster_score_gap": round((cluster_top_score or 0.0) - cluster_winner_score, 3)
                if cluster_top_score is not None and cluster_winner_score is not None
                else "",
                "box_score_gap": round((box_top_score or 0.0) - box_winner_score, 3)
                if box_top_score is not None and box_winner_score is not None
                else "",
                "fusion_score_gap": round((fusion_top_score or 0.0) - fusion_winner_score, 3)
                if fusion_top_score is not None and fusion_winner_score is not None
                else "",
                "gateway_rank_band": _rank_band(gateway_vtrac_rank),
                "cluster_rank_band": _rank_band(cluster_vtrac_rank),
                "box_rank_band": _rank_band(box_vtrac_rank),
                "fusion_rank_band": _rank_band(fusion_vtrac_rank),
                "best_surface_winner_vtrac_rank": best_surface_vtrac_rank or "",
                "best_surface_rank_band": _rank_band(best_surface_vtrac_rank),
                "winner_json_signal_class": winner_json_signal.get("signal_class") or "none",
                "winner_json_status": winner_json_status,
                "winner_json_signal_score": float(winner_json_signal.get("signal_score") or 0.0),
                "winner_json_ls_signal_cells": int(winner_json_signal.get("ls_signal_cells") or 0),
                "winner_json_variants_with_signal": int(winner_json_signal.get("variants_with_signal") or 0),
                "winner_json_ls_variants_with_signal": int(winner_json_signal.get("ls_variants_with_signal") or 0),
                "winner_json_family_gap_cells": int(winner_json_signal.get("family_gap_cells") or 0),
                "winner_json_vt_gap_cells": int(winner_json_signal.get("vt_straight_gap_cells") or 0),
                "winner_json_best_perm_rank": winner_json_ranks.get("best_perm_rank") or "",
                "winner_json_best_family_rank": winner_json_ranks.get("best_family_rank") or "",
                "winner_json_best_metric": winner_json_ranks.get("best_metric") or "",
                "winner_json_best_family_metric": winner_json_ranks.get("best_family_metric") or "",
                "overlay_summary_mismatch": mismatch_class,
                "alignment_class": alignment_class,
                "top_trace_family_1": (trace_rows[0].get("family_id") if trace_rows else ""),
                "top_corridor_family_1": (corridor_rows[0].get("family_id") if corridor_rows else ""),
                "top_double_pattern_1": (double_rows[0].get("pattern") if double_rows else ""),
                "winner_html_json": _safe_rel(winner_json_path) if winner_json_path else "",
                "winner_overlay_html": _safe_rel(Path(stamp_data.get("paths", {}).get("overlay_html", ""))) if stamp_data.get("paths", {}).get("overlay_html") else "",
                "winner_stamp_json": _safe_rel(stamp_path),
            }


def _pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def _emit_table(lines: List[str], headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> None:
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    lines.append("")


def _write_markdown(*, rows: List[Dict[str, Any]], out_path: Path, dates: List[str]) -> None:
    lines: List[str] = []
    lines.append("# DR Gold-Day Winner Audit")
    lines.append("")
    lines.append("- Purpose: winner-aware audit of `DR Arena v1.1` over frozen gold-day sharepacks.")
    lines.append(f"- Dates audited: `{', '.join(dates)}`")
    lines.append("- Rows are Midday/Evening state outcomes only; Combined is excluded from grading.")
    lines.append("")

    total = len(rows)
    exact_any_rows = sum(1 for row in rows if int(row["exact_any"]) > 0)
    vtrac_any_rows = sum(1 for row in rows if int(row["vtrac_any"]) > 0)
    family_vtrac_rows = sum(1 for row in rows if int(row["family_vtrac_any"]) > 0)
    trace_vtrac_top3 = sum(1 for row in rows if row["trace_winner_vtrac_rank"] and int(row["trace_winner_vtrac_rank"]) <= 3)
    corridor_vtrac_top3 = sum(1 for row in rows if row["corridor_winner_vtrac_rank"] and int(row["corridor_winner_vtrac_rank"]) <= 3)
    double_vtrac_top3 = sum(1 for row in rows if row["double_winner_vtrac_rank"] and int(row["double_winner_vtrac_rank"]) <= 3)
    strong_mismatch = sum(1 for row in rows if row["overlay_summary_mismatch"] == "strong")
    moderate_mismatch = sum(1 for row in rows if row["overlay_summary_mismatch"] == "moderate")
    winner_json_matched = sum(1 for row in rows if row["winner_json_status"] == "matched_literal")
    winner_json_unavailable = sum(1 for row in rows if row["winner_json_status"] != "matched_literal")
    strong_signal = sum(1 for row in rows if row["winner_json_signal_class"] == "strong")
    gateway_vtrac_top3 = sum(1 for row in rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 3)
    cluster_vtrac_top3 = sum(1 for row in rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 3)
    box_vtrac_top3 = sum(1 for row in rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 3)
    fusion_vtrac_top3 = sum(1 for row in rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 3)
    gateway_vtrac_top5 = sum(1 for row in rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 5)
    cluster_vtrac_top5 = sum(1 for row in rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 5)
    box_vtrac_top5 = sum(1 for row in rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 5)
    fusion_vtrac_top5 = sum(1 for row in rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 5)
    gateway_vtrac_top8 = sum(1 for row in rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 8)
    cluster_vtrac_top8 = sum(1 for row in rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 8)
    box_vtrac_top8 = sum(1 for row in rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 8)
    fusion_vtrac_top8 = sum(1 for row in rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 8)
    gateway_vtrac_top10 = sum(1 for row in rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 10)
    cluster_vtrac_top10 = sum(1 for row in rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 10)
    box_vtrac_top10 = sum(1 for row in rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 10)
    fusion_vtrac_top10 = sum(1 for row in rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 10)
    gateway_vtrac_top20 = sum(1 for row in rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 20)
    cluster_vtrac_top20 = sum(1 for row in rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 20)
    box_vtrac_top20 = sum(1 for row in rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 20)
    fusion_vtrac_top20 = sum(1 for row in rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 20)
    best_surface_top3 = sum(1 for row in rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 3)
    best_surface_top5 = sum(1 for row in rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 5)
    best_surface_top8 = sum(1 for row in rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 8)
    best_surface_top10 = sum(1 for row in rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 10)
    best_surface_top20 = sum(1 for row in rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 20)

    lines.append("## Overview")
    lines.append("")
    _emit_table(
        lines,
        ("Metric", "Count", "%"),
        (
            ("Rows audited", total, "100.0%"),
            ("exact_any > 0", exact_any_rows, _pct(exact_any_rows, total)),
            ("vtrac_any > 0", vtrac_any_rows, _pct(vtrac_any_rows, total)),
            ("family_vtrac_any > 0", family_vtrac_rows, _pct(family_vtrac_rows, total)),
            ("trace winner VTRAC rank <= 3", trace_vtrac_top3, _pct(trace_vtrac_top3, total)),
            ("corridor winner VTRAC rank <= 3", corridor_vtrac_top3, _pct(corridor_vtrac_top3, total)),
            ("double winner VTRAC rank <= 3", double_vtrac_top3, _pct(double_vtrac_top3, total)),
            ("gateway winner VTRAC rank <= 3", gateway_vtrac_top3, _pct(gateway_vtrac_top3, total)),
            ("cluster winner VTRAC rank <= 3", cluster_vtrac_top3, _pct(cluster_vtrac_top3, total)),
            ("assigned-box winner VTRAC rank <= 3", box_vtrac_top3, _pct(box_vtrac_top3, total)),
            ("fusion winner VTRAC rank <= 3", fusion_vtrac_top3, _pct(fusion_vtrac_top3, total)),
            ("gateway winner VTRAC rank <= 5", gateway_vtrac_top5, _pct(gateway_vtrac_top5, total)),
            ("cluster winner VTRAC rank <= 5", cluster_vtrac_top5, _pct(cluster_vtrac_top5, total)),
            ("assigned-box winner VTRAC rank <= 5", box_vtrac_top5, _pct(box_vtrac_top5, total)),
            ("fusion winner VTRAC rank <= 5", fusion_vtrac_top5, _pct(fusion_vtrac_top5, total)),
            ("gateway winner VTRAC rank <= 8", gateway_vtrac_top8, _pct(gateway_vtrac_top8, total)),
            ("cluster winner VTRAC rank <= 8", cluster_vtrac_top8, _pct(cluster_vtrac_top8, total)),
            ("assigned-box winner VTRAC rank <= 8", box_vtrac_top8, _pct(box_vtrac_top8, total)),
            ("fusion winner VTRAC rank <= 8", fusion_vtrac_top8, _pct(fusion_vtrac_top8, total)),
            ("gateway winner VTRAC rank <= 10", gateway_vtrac_top10, _pct(gateway_vtrac_top10, total)),
            ("cluster winner VTRAC rank <= 10", cluster_vtrac_top10, _pct(cluster_vtrac_top10, total)),
            ("assigned-box winner VTRAC rank <= 10", box_vtrac_top10, _pct(box_vtrac_top10, total)),
            ("fusion winner VTRAC rank <= 10", fusion_vtrac_top10, _pct(fusion_vtrac_top10, total)),
            ("gateway winner VTRAC rank <= 20", gateway_vtrac_top20, _pct(gateway_vtrac_top20, total)),
            ("cluster winner VTRAC rank <= 20", cluster_vtrac_top20, _pct(cluster_vtrac_top20, total)),
            ("assigned-box winner VTRAC rank <= 20", box_vtrac_top20, _pct(box_vtrac_top20, total)),
            ("fusion winner VTRAC rank <= 20", fusion_vtrac_top20, _pct(fusion_vtrac_top20, total)),
            ("best surface winner VTRAC rank <= 3", best_surface_top3, _pct(best_surface_top3, total)),
            ("best surface winner VTRAC rank <= 5", best_surface_top5, _pct(best_surface_top5, total)),
            ("best surface winner VTRAC rank <= 8", best_surface_top8, _pct(best_surface_top8, total)),
            ("best surface winner VTRAC rank <= 10", best_surface_top10, _pct(best_surface_top10, total)),
            ("best surface winner VTRAC rank <= 20", best_surface_top20, _pct(best_surface_top20, total)),
            ("winner JSON matched", winner_json_matched, _pct(winner_json_matched, total)),
            ("winner JSON unavailable/unmatched", winner_json_unavailable, _pct(winner_json_unavailable, total)),
            ("winner tables strong signal", strong_signal, _pct(strong_signal, total)),
            ("strong overlay-summary mismatch", strong_mismatch, _pct(strong_mismatch, total)),
            ("moderate overlay-summary mismatch", moderate_mismatch, _pct(moderate_mismatch, total)),
        ),
    )

    lines.append("## Alignment Classes")
    lines.append("")
    class_counts = Counter(str(row["alignment_class"]) for row in rows)
    _emit_table(
        lines,
        ("Class", "Count", "%"),
        tuple((label, class_counts[label], _pct(class_counts[label], total)) for label in sorted(class_counts)),
    )

    by_date: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_date[str(row["date"])].append(row)

    lines.append("## By Date")
    lines.append("")
    date_rows: List[Tuple[Any, ...]] = []
    for date in sorted(by_date):
        day_rows = by_date[date]
        n = len(day_rows)
        date_rows.append(
            (
                date,
                n,
                sum(1 for row in day_rows if int(row["vtrac_any"]) > 0),
                sum(1 for row in day_rows if row["trace_winner_vtrac_rank"] and int(row["trace_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["corridor_winner_vtrac_rank"] and int(row["corridor_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["gateway_winner_vtrac_rank"] and int(row["gateway_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 3),
                sum(1 for row in day_rows if row["cluster_winner_vtrac_rank"] and int(row["cluster_winner_vtrac_rank"]) <= 10),
                sum(1 for row in day_rows if row["box_winner_vtrac_rank"] and int(row["box_winner_vtrac_rank"]) <= 10),
                sum(1 for row in day_rows if row["fusion_winner_vtrac_rank"] and int(row["fusion_winner_vtrac_rank"]) <= 10),
                sum(1 for row in day_rows if row["best_surface_winner_vtrac_rank"] and int(row["best_surface_winner_vtrac_rank"]) <= 10),
                sum(1 for row in day_rows if row["winner_json_status"] == "matched_literal"),
                sum(1 for row in day_rows if row["overlay_summary_mismatch"] in {"strong", "moderate"}),
                sum(1 for row in day_rows if row["winner_json_signal_class"] == "strong"),
            )
        )
    _emit_table(
        lines,
        ("Date", "Rows", "vtrac_any", "trace_vtrac_top3", "corridor_vtrac_top3", "gateway_vtrac_top3", "cluster_vtrac_top3", "box_vtrac_top3", "fusion_vtrac_top3", "cluster_vtrac_top10", "box_vtrac_top10", "fusion_vtrac_top10", "best_surface_top10", "winner_json_matched", "mismatch>=moderate", "strong_signal"),
        date_rows,
    )

    def _top_rows(predicate, *, sort_key, limit: int = 12) -> List[Dict[str, Any]]:
        return sorted([row for row in rows if predicate(row)], key=sort_key)[:limit]

    mismatch_rows = _top_rows(
        lambda row: row["overlay_summary_mismatch"] in {"strong", "moderate"},
        sort_key=lambda row: (
            {"strong": 0, "moderate": 1, "mild": 2, "none": 3}[str(row["overlay_summary_mismatch"])],
            -float(row["winner_json_signal_score"]),
            row["date"],
            row["state"],
            row["variant"],
        ),
    )
    lines.append("## Strongest False-Empty / Mismatch Cases")
    lines.append("")
    if mismatch_rows:
        _emit_table(
            lines,
            (
                "Date",
                "State",
                "Var",
                "Winner",
                "Empty",
                "Mismatch",
                "Signal",
                "JSON",
                "LS signal",
                "Trace VT",
                "Corridor VT",
            ),
            tuple(
                (
                    row["date"],
                    row["state"],
                    row["variant"],
                    row["winner"],
                    row["empty_class"],
                    row["overlay_summary_mismatch"],
                    row["winner_json_signal_class"],
                    row["winner_json_status"],
                    row["winner_json_ls_signal_cells"],
                    row["trace_winner_vtrac_rank"] or "-",
                    row["corridor_winner_vtrac_rank"] or "-",
                )
                for row in mismatch_rows
            ),
        )
    else:
        lines.append("_None_")
        lines.append("")

    vtrac_rows = _top_rows(
        lambda row: row["alignment_class"] == "vtrac_capture",
        sort_key=lambda row: (
            min(
                int(row["trace_winner_vtrac_rank"]) if row["trace_winner_vtrac_rank"] else 99,
                int(row["corridor_winner_vtrac_rank"]) if row["corridor_winner_vtrac_rank"] else 99,
                int(row["double_winner_vtrac_rank"]) if row["double_winner_vtrac_rank"] else 99,
                int(row["gateway_winner_vtrac_rank"]) if row["gateway_winner_vtrac_rank"] else 99,
                int(row["cluster_winner_vtrac_rank"]) if row["cluster_winner_vtrac_rank"] else 99,
                int(row["box_winner_vtrac_rank"]) if row["box_winner_vtrac_rank"] else 99,
                int(row["fusion_winner_vtrac_rank"]) if row["fusion_winner_vtrac_rank"] else 99,
            ),
            row["date"],
            row["state"],
            row["variant"],
        ),
    )
    lines.append("## Strongest VTRAC-Lane Captures")
    lines.append("")
    if vtrac_rows:
        _emit_table(
            lines,
            (
                "Date",
                "State",
                "Var",
                "Winner",
                "VTRAC idx",
                "trace VT",
                "corridor VT",
                "double VT",
                "gateway VT",
                "cluster VT",
                "box VT",
                "fusion VT",
                "best VT",
                "Signal",
                "JSON",
                "Top corridor",
            ),
            tuple(
                (
                    row["date"],
                    row["state"],
                    row["variant"],
                    row["winner"],
                    row["winner_vtrac_index"],
                    row["trace_winner_vtrac_rank"] or "-",
                    row["corridor_winner_vtrac_rank"] or "-",
                    row["double_winner_vtrac_rank"] or "-",
                    row["gateway_winner_vtrac_rank"] or "-",
                    row["cluster_winner_vtrac_rank"] or "-",
                    row["box_winner_vtrac_rank"] or "-",
                    row["fusion_winner_vtrac_rank"] or "-",
                    row["best_surface_winner_vtrac_rank"] or "-",
                    row["winner_json_signal_class"],
                    row["winner_json_status"],
                    row["top_corridor_family_1"] or "-",
                )
                for row in vtrac_rows
            ),
        )
    else:
        lines.append("_None_")
        lines.append("")

    near_miss_rows = _top_rows(
        lambda row: row["cluster_winner_vtrac_rank"] and 6 <= int(row["cluster_winner_vtrac_rank"]) <= 20,
        sort_key=lambda row: (
            int(row["cluster_winner_vtrac_rank"]),
            float(row["cluster_score_gap"]) if row["cluster_score_gap"] != "" else 9999.0,
            -float(row["winner_json_signal_score"]),
            row["date"],
            row["state"],
            row["variant"],
        ),
    )
    lines.append("## Visible But Under-Promoted Winner Lanes")
    lines.append("")
    if near_miss_rows:
        _emit_table(
            lines,
            (
                "Date",
                "State",
                "Var",
                "Winner",
                "VT idx",
                "cluster rank",
                "cluster band",
                "cluster gap",
                "gateway rank",
                "box rank",
                "fusion rank",
                "best VT",
                "Signal",
                "Top attractor",
            ),
            tuple(
                (
                    row["date"],
                    row["state"],
                    row["variant"],
                    row["winner"],
                    row["winner_vtrac_index"],
                    row["cluster_winner_vtrac_rank"] or "-",
                    row["cluster_rank_band"],
                    row["cluster_score_gap"] or "-",
                    row["gateway_winner_vtrac_rank"] or "-",
                    row["box_winner_vtrac_rank"] or "-",
                    row["fusion_winner_vtrac_rank"] or "-",
                    row["best_surface_winner_vtrac_rank"] or "-",
                    row["winner_json_signal_class"],
                    row["top_corridor_family_1"] or row["top_trace_family_1"] or "-",
                )
                for row in near_miss_rows
            ),
        )
    else:
        lines.append("_None_")
        lines.append("")

    assigned_box_rows = _top_rows(
        lambda row: int(row["winner_json_ls_signal_cells"]) > 0,
        sort_key=lambda row: (
            -int(row["winner_json_ls_signal_cells"]),
            -float(row["winner_json_signal_score"]),
            row["date"],
            row["state"],
            row["variant"],
        ),
    )
    lines.append("## Strongest Assigned-Box Winner Corridors")
    lines.append("")
    if assigned_box_rows:
        _emit_table(
            lines,
            (
                "Date",
                "State",
                "Var",
                "Winner",
                "LS signal",
                "Signal",
                "JSON",
                "Best perm rank",
                "Best family rank",
                "Assigned-box VT",
                "Fusion VT",
                "Top trace",
                "Top corridor",
            ),
            tuple(
                (
                    row["date"],
                    row["state"],
                    row["variant"],
                    row["winner"],
                    row["winner_json_ls_signal_cells"],
                    row["winner_json_signal_class"],
                    row["winner_json_status"],
                    row["winner_json_best_perm_rank"] or "-",
                    row["winner_json_best_family_rank"] or "-",
                    row["box_winner_vtrac_rank"] or "-",
                    row["fusion_winner_vtrac_rank"] or "-",
                    row["top_trace_family_1"] or "-",
                    row["top_corridor_family_1"] or "-",
                )
                for row in assigned_box_rows
            ),
        )
    else:
        lines.append("_None_")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- `winner_json_signal_class` comes from the structured winners JSON tables, not from DR receipts.")
    lines.append("- `winner_json_status=unmatched_literal` means the sharepack has winners JSON files, but not for the actual stamped winner; treat those rows as artifact gaps, not genuine dead environments.")
    lines.append("- `overlay_summary_mismatch` is winner-aware here: it flags rows where DR receipts stay at zero while the winner tables still show meaningful corridor activity.")
    lines.append("- Audit-only payload depth is widened to `top20` for trace/lane/competing/double/gateway/cluster/assigned-box/fusion so broader visibility can be measured without narrowing the evaluation window.")
    lines.append("- `trace/corridor/double/gateway/cluster/assigned-box/fusion winner VTRAC rank` checks whether the strongest predictive DR surfaces align to the eventual winner’s VTRAC lane, even when the literal winner is absent.")
    lines.append("- `assigned-box` is a predictive surface built from 3-digit windows inside raw DR `box_id` / `final_value` strings; it is intended to preserve buried assigned-box corridor truth without using winner artifacts.")
    lines.append("- `fusion` is a bounded promotion surface: it boosts lanes when assigned-box agrees with cluster/gateway, and it allows guarded assigned-box rescue when cluster/gateway are still dead.")
    lines.append("- `best surface winner VTRAC rank` is the minimum visible rank across trace/corridor/double/candidate/gateway/cluster/assigned-box/fusion for that row.")
    lines.append("- `gateway_score_gap` / `cluster_score_gap` / `box_score_gap` / `fusion_score_gap` measure how far the visible top score sits above the winner lane when the winner lane is present in that broader audit view.")
    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Winner-aware DR Arena gold-day audit.")
    ap.add_argument("--dates", nargs="*", help="Explicit sharepack/results dates to audit.")
    ap.add_argument("--start", help="Start sharepack/results date (inclusive).")
    ap.add_argument("--end", help="End sharepack/results date (inclusive).")
    ap.add_argument(
        "--out-csv",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2026-03-15__DR_GOLD_DAY_AUDIT__V1_1.csv"),
        help="Output CSV path.",
    )
    ap.add_argument(
        "--out-md",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2026-03-15__DR_GOLD_DAY_AUDIT__V1_1.md"),
        help="Output Markdown path.",
    )
    ap.add_argument(
        "--profile",
        default="gold_day_audit",
        help="Profile label recorded inside temporary arena payloads.",
    )
    ap.add_argument(
        "--experiment-tag",
        default="dr_gold_day_audit_v1_1",
        help="Experiment tag recorded inside temporary arena payloads.",
    )
    args = ap.parse_args()

    dates: List[str] = []
    if args.dates:
        dates.extend(args.dates)
    if args.start and args.end:
        dates.extend(daterange(args.start, args.end))
    dates = sorted(dict.fromkeys(dates))
    if not dates:
        raise SystemExit("Provide --dates or --start/--end")

    rows: List[Dict[str, Any]] = []
    for date in dates:
        day_dir = ROOT / "sharepacks" / date
        if not day_dir.exists():
            continue
        rows.extend(
            _date_rows_payload(
                day_dir,
                profile=args.profile,
                experiment_tag=args.experiment_tag,
            )
        )

    if not rows:
        raise SystemExit("No audit rows found for the requested dates.")

    csv_path = Path(args.out_csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _write_markdown(rows=rows, out_path=Path(args.out_md), dates=dates)

    print(f"rows={len(rows)}")
    print(f"csv={csv_path}")
    print(f"md={args.out_md}")


if __name__ == "__main__":
    main()
