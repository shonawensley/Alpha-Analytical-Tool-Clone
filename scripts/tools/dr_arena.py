#!/usr/bin/env python3
"""Build a Digit Reduction analysis arena from frozen predictive sharepack artifacts.

The arena is intentionally predictive-side and budget-blind. It preserves the
stronger DR evidence classes learned through the DR super-harness without
changing DR extraction or candidate pack logic.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from modules.vtrac_reference import get_vtrac_index


SECTION_ORDER: Tuple[str, ...] = ("Midday", "Evening", "Combined")
STEP_COUNT_KEYS: Tuple[str, ...] = (
    "exact_any",
    "vtrac_any",
    "drop_exact_any",
    "drop_vtrac_any",
    "family_exact_any",
    "family_vtrac_any",
    "exact_final",
    "vtrac_final",
    "drop_exact_final",
    "drop_vtrac_final",
    "family_exact_final",
    "family_vtrac_final",
)
MIRROR_MAP: Dict[str, str] = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}
DIGIT_TO_VTRAC_VALUE: Dict[str, int] = {
    "0": 1,
    "5": 1,
    "1": 2,
    "6": 2,
    "2": 3,
    "7": 3,
    "3": 4,
    "8": 4,
    "4": 5,
    "9": 5,
}


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _safe_rel(path: Path, repo_root: Path) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _digits_only(value: object) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _to_bool(value: object) -> bool:
    text = str(value or "").strip().lower()
    if text in {"1", "true", "t", "yes", "y"}:
        return True
    if text in {"0", "false", "f", "no", "n", ""}:
        return False
    try:
        return float(text) != 0.0
    except Exception:
        return False


def _section_sort_key(section: str) -> Tuple[int, str]:
    try:
        return (SECTION_ORDER.index(section), section)
    except ValueError:
        return (len(SECTION_ORDER), section)


def _hash_inputs(paths: Sequence[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.name).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _currentness_score(
    *,
    set_rank: int,
    draw_rank: int,
    col_rank: int,
    area_rank: int,
    set1_terminal: bool = False,
    funnel_precol1: bool = False,
) -> float:
    score = 0.0
    score += max(0, 4 - set_rank) * 1.5
    score += max(0, 8 - draw_rank) * 0.35
    score += max(0, 8 - col_rank) * 0.45
    score += max(0, 4 - area_rank) * 0.25
    if set1_terminal:
        score += 1.25
    if funnel_precol1:
        score += 1.0
    return round(score, 3)


def _is_duplicate_pattern(pattern: str) -> bool:
    digits = _digits_only(pattern)
    return bool(digits) and len(set(digits)) < len(digits)


def _mirror_digits(pattern: str) -> str:
    return "".join(MIRROR_MAP.get(ch, "") for ch in _digits_only(pattern))


def _vtrac_signature(pattern: str) -> str:
    vals = [str(DIGIT_TO_VTRAC_VALUE[ch]) for ch in _digits_only(pattern) if ch in DIGIT_TO_VTRAC_VALUE]
    return "".join(vals)


def _window_tokens(value: object, *, width: int = 3) -> List[str]:
    digits = _digits_only(value)
    if len(digits) < width:
        return []
    return [digits[idx : idx + width] for idx in range(0, len(digits) - width + 1)]


def _vtrac_index_of_token(value: object) -> Optional[int]:
    digits = _digits_only(value)
    if len(digits) != 3:
        return None
    return get_vtrac_index(digits)


def _counter_top(counter: Counter[str], top_n: int = 6) -> List[Dict[str, Any]]:
    items = sorted(counter.items(), key=lambda kv: (-int(kv[1]), kv[0]))
    return [{"value": key, "count": int(count)} for key, count in items[:top_n]]


def _row_location(row: Dict[str, Any]) -> str:
    return "|".join(
        [
            str(row.get("section") or row.get("variant") or ""),
            str(row.get("set") or ""),
            str(row.get("draw") or ""),
            f"col{row.get('col') or ''}",
        ]
    )


def _parse_row_location(location: str) -> Dict[str, str]:
    parts = [part.strip() for part in str(location or "").split("|")]
    section = parts[0] if len(parts) > 0 else ""
    set_name = parts[1] if len(parts) > 1 else ""
    draw_name = parts[2] if len(parts) > 2 else ""
    col_name = parts[3] if len(parts) > 3 else ""
    return {
        "section": section,
        "set": set_name,
        "draw": draw_name,
        "col": col_name,
    }


def _label_rank(label: str, prefix: str, default: int) -> int:
    text = str(label or "").strip()
    if not text:
        return int(default)
    if text.lower().startswith(prefix.lower()):
        text = text[len(prefix) :]
    return _to_int(text, default=default)


def _max_consecutive_run(values: Iterable[int]) -> int:
    ordered = sorted({int(v) for v in values})
    if not ordered:
        return 0
    best = 1
    current = 1
    for idx in range(1, len(ordered)):
        if ordered[idx] == ordered[idx - 1] + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best


def _load_dr_bundle(state_dir: Path, state_key: str) -> Optional[Dict[str, Any]]:
    dr_dir = state_dir / "digit_reduction" / state_key
    analyzer_dir = dr_dir / "analyzer_v2"
    training_dir = dr_dir / "training"
    meta_path = analyzer_dir / f"{state_key}_analyzer_v2_meta.json"
    per_item_path = analyzer_dir / f"{state_key}_analyzer_v2_per_item.csv"
    top_candidates_path = analyzer_dir / f"{state_key}_analyzer_v2_top_candidates.csv"
    logs_path = training_dir / f"{state_key}_digit_reduction_logs.json"
    steps_path = training_dir / f"{state_key}_digit_reduction_steps.csv"
    scores_path = dr_dir / f"{state_key}_digit_reduction_scores.csv"

    required = [meta_path, per_item_path, top_candidates_path, logs_path]
    if any(not path.exists() for path in required):
        return None

    bundle = {
        "meta_path": meta_path,
        "per_item_path": per_item_path,
        "top_candidates_path": top_candidates_path,
        "logs_path": logs_path,
        "steps_path": steps_path if steps_path.exists() else None,
        "scores_path": scores_path if scores_path.exists() else None,
        "meta": _read_json(meta_path),
        "per_item": _load_csv_rows(per_item_path),
        "top_candidates": _load_csv_rows(top_candidates_path),
        "logs": _read_json(logs_path),
        "steps": _load_csv_rows(steps_path) if steps_path.exists() else [],
    }
    return bundle


def _aggregate_family_rows(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        family_id = str(row.get("family_id") or row.get("family_unique") or row.get("pattern") or "")
        if not family_id:
            continue
        bucket = grouped.setdefault(
            family_id,
            {
                "family_id": family_id,
                "score_total": 0.0,
                "score_max": 0.0,
                "rows": 0,
                "locations": set(),
                "methods": Counter(),
                "modes": Counter(),
                "areas": Counter(),
                "patterns": Counter(),
                "vt_only_rows": 0,
                "dup_rows": 0,
                "dup_bonus_total": 0.0,
                "dup_bonus_max": 0.0,
                "funnel_rows": 0,
                "set1_terminal_rows": 0,
                "currentness_max": 0.0,
                "currentness_total": 0.0,
                "vtrac_bias_total": 0.0,
                "residual_purity_max": 0.0,
                "final_prob_max": 0.0,
                "box_family_density_max": 0.0,
                "cluster_echo_max": 0,
                "variant_echo_max": 0,
                "set_echo_max": 0,
                "sample_locators": [],
            },
        )
        score_v2 = _to_float(row.get("score_v2"))
        dup_bonus = _to_float(row.get("dup_bonus"))
        currentness = _currentness_score(
            set_rank=_to_int(row.get("set_rank"), 3),
            draw_rank=_to_int(row.get("draw_rank"), 3),
            col_rank=_to_int(row.get("col_rank"), 7),
            area_rank=_to_int(row.get("area_rank"), 3),
            set1_terminal=_to_bool(row.get("set1_terminal")),
            funnel_precol1=_to_bool(row.get("funnel_precol1")),
        )
        pattern = _digits_only(row.get("pattern"))
        locator = _row_location(row)

        bucket["score_total"] += score_v2
        bucket["score_max"] = max(bucket["score_max"], score_v2)
        bucket["rows"] += 1
        bucket["locations"].add(locator)
        bucket["methods"][str(row.get("method") or "")] += 1
        bucket["modes"][str(row.get("mode") or "")] += 1
        bucket["areas"][str(row.get("area") or "")] += 1
        if pattern:
            bucket["patterns"][pattern] += 1
        if _to_bool(row.get("vt_only_lane")):
            bucket["vt_only_rows"] += 1
        if _is_duplicate_pattern(pattern) or dup_bonus > 0.0:
            bucket["dup_rows"] += 1
        bucket["dup_bonus_total"] += dup_bonus
        bucket["dup_bonus_max"] = max(bucket["dup_bonus_max"], dup_bonus)
        if _to_bool(row.get("funnel_precol1")):
            bucket["funnel_rows"] += 1
        if _to_bool(row.get("set1_terminal")):
            bucket["set1_terminal_rows"] += 1
        bucket["currentness_max"] = max(bucket["currentness_max"], currentness)
        bucket["currentness_total"] += currentness
        bucket["vtrac_bias_total"] += max(
            0.0,
            _to_float(row.get("persistence_vtrac_score")) - _to_float(row.get("persistence_exact_score")),
        )
        bucket["residual_purity_max"] = max(bucket["residual_purity_max"], _to_float(row.get("residual_purity")))
        bucket["final_prob_max"] = max(bucket["final_prob_max"], _to_float(row.get("final_prob")))
        bucket["box_family_density_max"] = max(
            bucket["box_family_density_max"], _to_float(row.get("box_family_density"))
        )
        bucket["cluster_echo_max"] = max(bucket["cluster_echo_max"], _to_int(row.get("cluster_echo_count")))
        bucket["variant_echo_max"] = max(bucket["variant_echo_max"], _to_int(row.get("variant_echo_count")))
        bucket["set_echo_max"] = max(bucket["set_echo_max"], _to_int(row.get("set_echo_count")))
        if len(bucket["sample_locators"]) < 6 and locator not in bucket["sample_locators"]:
            bucket["sample_locators"].append(locator)

    out: List[Dict[str, Any]] = []
    for family_id, bucket in grouped.items():
        rows_count = max(1, int(bucket["rows"]))
        out.append(
            {
                "family_id": family_id,
                "score_total": round(float(bucket["score_total"]), 3),
                "score_max": round(float(bucket["score_max"]), 3),
                "rows": rows_count,
                "box_count": len(bucket["locations"]),
                "method_count": len([k for k in bucket["methods"] if k]),
                "mode_count": len([k for k in bucket["modes"] if k]),
                "area_count": len([k for k in bucket["areas"] if k]),
                "vt_only_rows": int(bucket["vt_only_rows"]),
                "dup_rows": int(bucket["dup_rows"]),
                "dup_bonus_total": round(float(bucket["dup_bonus_total"]), 3),
                "dup_bonus_max": round(float(bucket["dup_bonus_max"]), 3),
                "funnel_rows": int(bucket["funnel_rows"]),
                "set1_terminal_rows": int(bucket["set1_terminal_rows"]),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "currentness_avg": round(float(bucket["currentness_total"]) / float(rows_count), 3),
                "vtrac_bias_total": round(float(bucket["vtrac_bias_total"]), 3),
                "residual_purity_max": round(float(bucket["residual_purity_max"]), 3),
                "final_prob_max": round(float(bucket["final_prob_max"]), 6),
                "box_family_density_max": round(float(bucket["box_family_density_max"]), 3),
                "cluster_echo_max": int(bucket["cluster_echo_max"]),
                "variant_echo_max": int(bucket["variant_echo_max"]),
                "set_echo_max": int(bucket["set_echo_max"]),
                "top_patterns": _counter_top(bucket["patterns"], top_n=6),
                "top_methods": _counter_top(bucket["methods"], top_n=3),
                "top_modes": _counter_top(bucket["modes"], top_n=3),
                "top_areas": _counter_top(bucket["areas"], top_n=3),
                "sample_locators": list(bucket["sample_locators"]),
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["score_total"]),
            -int(item["rows"]),
            -float(item["currentness_max"]),
            item["family_id"],
        )
    )
    return out


def _aggregate_pattern_rows(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        pattern = _digits_only(row.get("pattern"))
        if not pattern:
            continue
        bucket = grouped.setdefault(
            pattern,
            {
                "pattern": pattern,
                "family_ids": Counter(),
                "score_total": 0.0,
                "score_max": 0.0,
                "rows": 0,
                "locations": set(),
                "dup_bonus_total": 0.0,
                "dup_bonus_max": 0.0,
                "currentness_max": 0.0,
                "funnel_rows": 0,
                "set1_terminal_rows": 0,
                "vt_only_rows": 0,
                "cluster_echo_max": 0,
                "sample_locators": [],
            },
        )
        score_v2 = _to_float(row.get("score_v2"))
        currentness = _currentness_score(
            set_rank=_to_int(row.get("set_rank"), 3),
            draw_rank=_to_int(row.get("draw_rank"), 3),
            col_rank=_to_int(row.get("col_rank"), 7),
            area_rank=_to_int(row.get("area_rank"), 3),
            set1_terminal=_to_bool(row.get("set1_terminal")),
            funnel_precol1=_to_bool(row.get("funnel_precol1")),
        )
        locator = _row_location(row)

        bucket["family_ids"][str(row.get("family_id") or "")] += 1
        bucket["score_total"] += score_v2
        bucket["score_max"] = max(bucket["score_max"], score_v2)
        bucket["rows"] += 1
        bucket["locations"].add(locator)
        dup_bonus = _to_float(row.get("dup_bonus"))
        bucket["dup_bonus_total"] += dup_bonus
        bucket["dup_bonus_max"] = max(bucket["dup_bonus_max"], dup_bonus)
        bucket["currentness_max"] = max(bucket["currentness_max"], currentness)
        if _to_bool(row.get("funnel_precol1")):
            bucket["funnel_rows"] += 1
        if _to_bool(row.get("set1_terminal")):
            bucket["set1_terminal_rows"] += 1
        if _to_bool(row.get("vt_only_lane")):
            bucket["vt_only_rows"] += 1
        bucket["cluster_echo_max"] = max(bucket["cluster_echo_max"], _to_int(row.get("cluster_echo_count")))
        if len(bucket["sample_locators"]) < 6 and locator not in bucket["sample_locators"]:
            bucket["sample_locators"].append(locator)

    out: List[Dict[str, Any]] = []
    for pattern, bucket in grouped.items():
        out.append(
            {
                "pattern": pattern,
                "family_id": _counter_top(bucket["family_ids"], top_n=1)[0]["value"] if bucket["family_ids"] else "",
                "score_total": round(float(bucket["score_total"]), 3),
                "score_max": round(float(bucket["score_max"]), 3),
                "rows": int(bucket["rows"]),
                "box_count": len(bucket["locations"]),
                "dup_bonus_total": round(float(bucket["dup_bonus_total"]), 3),
                "dup_bonus_max": round(float(bucket["dup_bonus_max"]), 3),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "funnel_rows": int(bucket["funnel_rows"]),
                "set1_terminal_rows": int(bucket["set1_terminal_rows"]),
                "vt_only_rows": int(bucket["vt_only_rows"]),
                "cluster_echo_max": int(bucket["cluster_echo_max"]),
                "is_duplicate_pattern": _is_duplicate_pattern(pattern),
                "mirror_pattern": _mirror_digits(pattern),
                "vtrac_signature": _vtrac_signature(pattern),
                "sample_locators": list(bucket["sample_locators"]),
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["score_total"]),
            -int(item["rows"]),
            -float(item["dup_bonus_total"]),
            item["pattern"],
        )
    )
    return out


def _derive_trace_strength(families: Sequence[Dict[str, Any]], top_n: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for idx, item in enumerate(families[:top_n], start=1):
        trace_score = (
            float(item["score_total"])
            + 0.75 * float(item["rows"])
            + 0.5 * float(item["box_count"])
            + 0.35 * float(item["currentness_max"])
            + 0.25 * float(item["variant_echo_max"])
            + 0.25 * float(item["set_echo_max"])
        )
        out.append(
            {
                **item,
                "trace_rank": idx,
                "trace_score": round(trace_score, 3),
                "why_tags": [
                    "trace_strength",
                    f"rows={int(item['rows'])}",
                    f"boxes={int(item['box_count'])}",
                    f"currentness={float(item['currentness_max']):.3f}",
                ],
            }
        )
    return out


def _derive_lane_only_confidence(families: Sequence[Dict[str, Any]], top_n: int) -> List[Dict[str, Any]]:
    scored: List[Dict[str, Any]] = []
    for item in families:
        lane_score = (
            float(item["vtrac_bias_total"])
            + 1.5 * float(item["vt_only_rows"])
            + 0.4 * float(item["box_family_density_max"])
            + 0.25 * float(item["cluster_echo_max"])
            + 0.2 * float(item["currentness_max"])
        )
        if lane_score <= 0:
            continue
        scored.append(
            {
                **item,
                "lane_confidence_score": round(lane_score, 3),
                "lane_confidence_reason": [
                    f"vtrac_bias={float(item['vtrac_bias_total']):.3f}",
                    f"vt_only_rows={int(item['vt_only_rows'])}",
                    f"box_density={float(item['box_family_density_max']):.3f}",
                ],
            }
        )
    scored.sort(
        key=lambda item: (
            -float(item["lane_confidence_score"]),
            -float(item["score_total"]),
            item["family_id"],
        )
    )
    return scored[:top_n]


def _derive_competing_literal_pressure(
    patterns: Sequence[Dict[str, Any]],
    top_candidate_rows: Sequence[Dict[str, Any]],
    top_n: int,
) -> List[Dict[str, Any]]:
    ranks_by_pattern: Dict[str, List[int]] = defaultdict(list)
    for row in top_candidate_rows:
        pattern = _digits_only(row.get("best_pattern"))
        if pattern:
            ranks_by_pattern[pattern].append(_to_int(row.get("rank"), 9999))
    out: List[Dict[str, Any]] = []
    for item in patterns:
        pressure = (
            float(item["score_total"])
            + 1.0 * float(item["dup_bonus_total"])
            + 0.6 * float(item["box_count"])
            + 0.3 * float(item["funnel_rows"])
            + 0.25 * float(item["set1_terminal_rows"])
        )
        if item["is_duplicate_pattern"]:
            pressure += 1.5
        if ranks_by_pattern.get(item["pattern"]):
            pressure += max(0.0, 4.0 - min(ranks_by_pattern[item["pattern"]]) * 0.2)
        out.append(
            {
                **item,
                "pressure_score": round(pressure, 3),
                "top_candidate_ranks": sorted(ranks_by_pattern.get(item["pattern"], []))[:5],
                "why_tags": [
                    "competing_literal_pressure",
                    f"dup={float(item['dup_bonus_total']):.3f}",
                    f"boxes={int(item['box_count'])}",
                ],
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["pressure_score"]),
            -float(item["score_total"]),
            item["pattern"],
        )
    )
    return out[:top_n]


def _derive_double_pressure(patterns: Sequence[Dict[str, Any]], top_n: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for item in patterns:
        if not item["is_duplicate_pattern"] and float(item["dup_bonus_total"]) <= 0.0:
            continue
        double_score = (
            float(item["dup_bonus_total"])
            + 0.75 * float(item["rows"])
            + 0.5 * float(item["box_count"])
            + 0.4 * float(item["score_max"])
        )
        out.append(
            {
                **item,
                "double_score": round(double_score, 3),
                "duplicate_depth": int(len(_digits_only(item["pattern"])) - len(set(_digits_only(item["pattern"])))),
                "mirror_pattern": _mirror_digits(item["pattern"]),
                "why_tags": [
                    "double_pressure",
                    f"dup_bonus={float(item['dup_bonus_total']):.3f}",
                    f"rows={int(item['rows'])}",
                ],
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["double_score"]),
            -float(item["dup_bonus_total"]),
            item["pattern"],
        )
    )
    return out[:top_n]


def _derive_corridors(families: Sequence[Dict[str, Any]], top_n: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for item in families:
        top_patterns = list(item.get("top_patterns") or [])
        family_total = sum(_to_int(entry.get("count")) for entry in top_patterns)
        leader_count = _to_int(top_patterns[0].get("count")) if top_patterns else 0
        neighbor_box_support = 0
        draw_ranks: List[int] = []
        col_ranks: List[int] = []
        for locator in item.get("sample_locators") or []:
            parsed = _parse_row_location(locator)
            col_rank = _label_rank(parsed.get("col", ""), "col", default=0)
            draw_rank = _label_rank(parsed.get("draw", ""), "Draw", default=0)
            if col_rank in {2, 4}:
                neighbor_box_support += 1
            if draw_rank > 0:
                draw_ranks.append(draw_rank)
            if col_rank > 0:
                col_ranks.append(col_rank)
        draw_progression = _max_consecutive_run(draw_ranks)
        col_progression = _max_consecutive_run(col_ranks)
        consecutive_box_progression = max(draw_progression, col_progression)

        if int(item["vt_only_rows"]) >= max(1, int(item["rows"]) // 2) and float(item["vtrac_bias_total"]) > 0.0:
            scope = "vtrac_corridor"
        elif int(item["dup_rows"]) >= max(1, int(item["rows"]) // 3):
            scope = "compact_double_corridor"
        elif len(top_patterns) >= 2 and family_total >= 3:
            scope = "family_neighborhood"
        else:
            scope = "exact_corridor"

        frontier_rows = int(item["set1_terminal_rows"]) + int(item["funnel_rows"])
        if frontier_rows >= max(1, int(item["rows"]) // 2):
            band = "set1_current_day"
        elif float(item["currentness_max"]) >= 4.5:
            band = "mixed"
        else:
            band = "7_6_5_band"

        family_asymmetry = 0.0
        if family_total > 0:
            family_asymmetry = float(leader_count) / float(family_total)

        corridor_strength = (
            float(item["score_total"])
            + 0.75 * float(item["rows"])
            + 0.5 * float(item["box_count"])
            + 0.45 * float(item["currentness_max"])
            + 0.35 * float(item["residual_purity_max"])
            + 0.3 * float(frontier_rows)
            + 0.25 * float(consecutive_box_progression)
        )

        out.append(
            {
                "family_id": item["family_id"],
                "corridor_strength_score": round(corridor_strength, 3),
                "corridor_scope": scope,
                "corridor_band": band,
                "corridor_variant_profile": "section_local",
                "raw_exposure_count": int(item["rows"]),
                "path_summary_count": int(item["box_count"]),
                "neighbor_box_support": int(neighbor_box_support),
                "consecutive_box_progression": int(consecutive_box_progression),
                "family_neighborhood_saturation": round(float(family_total), 3),
                "family_asymmetry_inside_corridor": round(family_asymmetry, 3),
                "currentness_max": item["currentness_max"],
                "top_patterns": top_patterns,
                "sample_locators": list(item.get("sample_locators") or []),
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["corridor_strength_score"]),
            -int(item["raw_exposure_count"]),
            -int(item["path_summary_count"]),
            item["family_id"],
        )
    )
    return out[:top_n]


def _derive_vtrac_lane_gateway(
    *,
    families: Sequence[Dict[str, Any]],
    patterns: Sequence[Dict[str, Any]],
    candidate_rows: Sequence[Dict[str, Any]],
    corridors: Sequence[Dict[str, Any]],
    top_n: int,
) -> List[Dict[str, Any]]:
    corridor_by_family = {str(item.get("family_id") or ""): item for item in corridors}
    grouped: Dict[int, Dict[str, Any]] = {}

    def _bucket_for(idx: int) -> Dict[str, Any]:
        return grouped.setdefault(
            idx,
            {
                "vtrac_index": idx,
                "families": Counter(),
                "patterns": Counter(),
                "scopes": Counter(),
                "bands": Counter(),
                "score_total": 0.0,
                "rows_total": 0,
                "box_total": 0,
                "vt_only_rows": 0,
                "vtrac_bias_total": 0.0,
                "currentness_max": 0.0,
                "corridor_strength_max": 0.0,
                "corridor_strength_total": 0.0,
                "candidate_rank_bonus": 0.0,
                "candidate_count": 0,
                "member_count": 0,
            },
        )

    for item in families:
        family_id = str(item.get("family_id") or "")
        idx = _vtrac_index_of_token(family_id)
        if idx is None:
            top_patterns = list(item.get("top_patterns") or [])
            if top_patterns:
                idx = _vtrac_index_of_token(top_patterns[0].get("value"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        bucket["families"][family_id] += 1
        for pattern_row in item.get("top_patterns") or []:
            token = _digits_only(pattern_row.get("value"))
            if token:
                bucket["patterns"][token] += _to_int(pattern_row.get("count"), 1)
        bucket["score_total"] += float(item.get("score_total") or 0.0)
        bucket["rows_total"] += _to_int(item.get("rows"), 0)
        bucket["box_total"] += _to_int(item.get("box_count"), 0)
        bucket["vt_only_rows"] += _to_int(item.get("vt_only_rows"), 0)
        bucket["vtrac_bias_total"] += float(item.get("vtrac_bias_total") or 0.0)
        bucket["currentness_max"] = max(bucket["currentness_max"], float(item.get("currentness_max") or 0.0))
        bucket["member_count"] = len(bucket["families"])
        corridor = corridor_by_family.get(family_id)
        if corridor:
            scope = str(corridor.get("corridor_scope") or "")
            band = str(corridor.get("corridor_band") or "")
            if scope:
                bucket["scopes"][scope] += 1
            if band:
                bucket["bands"][band] += 1
            bucket["corridor_strength_max"] = max(
                bucket["corridor_strength_max"], float(corridor.get("corridor_strength_score") or 0.0)
            )
            bucket["corridor_strength_total"] += float(corridor.get("corridor_strength_score") or 0.0)

    for item in patterns:
        idx = _vtrac_index_of_token(item.get("pattern"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        token = _digits_only(item.get("pattern"))
        if token:
            bucket["patterns"][token] += max(1, _to_int(item.get("rows"), 0))

    for row in candidate_rows:
        idx = _vtrac_index_of_token(row.get("best_pattern"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        rank = _to_int(row.get("rank"), 9999)
        bonus = max(0.0, 4.0 - float(rank) * 0.35)
        bucket["candidate_rank_bonus"] += bonus
        bucket["candidate_count"] += 1
        token = _digits_only(row.get("best_pattern"))
        if token:
            bucket["patterns"][token] += 1

    out: List[Dict[str, Any]] = []
    for idx, bucket in grouped.items():
        member_count = max(1, int(bucket["member_count"]))
        scope_diversity = len([k for k in bucket["scopes"] if k])
        gateway_score = (
            float(bucket["score_total"])
            + 0.85 * float(bucket["rows_total"])
            + 0.55 * float(bucket["box_total"])
            + 1.75 * float(member_count)
            + 1.5 * float(bucket["candidate_rank_bonus"])
            + 0.85 * float(bucket["vt_only_rows"])
            + 0.45 * float(bucket["vtrac_bias_total"])
            + 0.35 * float(bucket["currentness_max"])
            + 0.16 * float(bucket["corridor_strength_total"])
            + 0.75 * float(scope_diversity)
        )
        out.append(
            {
                "vtrac_index": int(idx),
                "gateway_score": round(gateway_score, 3),
                "member_count": int(member_count),
                "rows_total": int(bucket["rows_total"]),
                "box_total": int(bucket["box_total"]),
                "candidate_count": int(bucket["candidate_count"]),
                "candidate_rank_bonus": round(float(bucket["candidate_rank_bonus"]), 3),
                "vt_only_rows": int(bucket["vt_only_rows"]),
                "vtrac_bias_total": round(float(bucket["vtrac_bias_total"]), 3),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "corridor_strength_max": round(float(bucket["corridor_strength_max"]), 3),
                "top_families": _counter_top(bucket["families"], top_n=4),
                "top_patterns": _counter_top(bucket["patterns"], top_n=5),
                "scope_mix": _counter_top(bucket["scopes"], top_n=3),
                "band_mix": _counter_top(bucket["bands"], top_n=3),
                "why_tags": [
                    "vtrac_lane_gateway",
                    f"members={member_count}",
                    f"candidate_bonus={float(bucket['candidate_rank_bonus']):.3f}",
                    f"corridor_total={float(bucket['corridor_strength_total']):.3f}",
                ],
            }
        )
    out.sort(
        key=lambda item: (
            -float(item["gateway_score"]),
            -int(item["member_count"]),
            -int(item["rows_total"]),
            int(item["vtrac_index"]),
        )
    )
    return out[:top_n]


def _derive_assigned_box_vtrac_strength(
    *,
    variant_rows: Sequence[Dict[str, Any]],
    top_n: int,
) -> List[Dict[str, Any]]:
    grouped: Dict[int, Dict[str, Any]] = {}

    def _bucket_for(idx: int) -> Dict[str, Any]:
        return grouped.setdefault(
            idx,
            {
                "vtrac_index": idx,
                "score_total": 0.0,
                "row_hits": 0,
                "currentness_max": 0.0,
                "box_pair_agree_max": 0.0,
                "cluster_echo_max": 0,
                "variant_echo_max": 0,
                "windows": Counter(),
                "boxes": Counter(),
                "columns": Counter(),
                "methods": Counter(),
                "modes": Counter(),
                "areas": Counter(),
                "sections": Counter(),
                "locations": set(),
            },
        )

    for row in variant_rows:
        currentness = _currentness_score(
            set_rank=_to_int(row.get("set_rank"), 3),
            draw_rank=_to_int(row.get("draw_rank"), 3),
            col_rank=_to_int(row.get("col_rank"), 7),
            area_rank=_to_int(row.get("area_rank"), 3),
            set1_terminal=_to_bool(row.get("set1_terminal")),
            funnel_precol1=_to_bool(row.get("funnel_precol1")),
        )
        base_score = (
            1.0
            + 0.25 * currentness
            + 0.15 * _to_float(row.get("cluster_echo_count"))
            + 0.10 * _to_float(row.get("variant_echo_count"))
            + 0.10 * _to_float(row.get("box_pair_agree"))
            + 0.05 * _to_float(row.get("box_family_density"))
        )
        location = _row_location(row)
        column = str(row.get("col") or "")
        method = str(row.get("method") or "")
        mode = str(row.get("mode") or "")
        area = str(row.get("area") or "")
        section = str(row.get("section") or row.get("variant") or "")
        box_id = _digits_only(row.get("box_id"))

        window_hits: Dict[int, Counter[str]] = defaultdict(Counter)
        sources = [row.get("box_id"), row.get("final_value")]
        if not any(_digits_only(source) for source in sources):
            sources.append(row.get("pattern"))
        for source in sources:
            for token in set(_window_tokens(source, width=3)):
                idx = _vtrac_index_of_token(token)
                if idx is not None:
                    window_hits[idx][token] += 1

        for idx, tokens in window_hits.items():
            bucket = _bucket_for(idx)
            bucket["score_total"] += base_score
            bucket["row_hits"] += 1
            bucket["currentness_max"] = max(bucket["currentness_max"], currentness)
            bucket["box_pair_agree_max"] = max(bucket["box_pair_agree_max"], _to_float(row.get("box_pair_agree")))
            bucket["cluster_echo_max"] = max(bucket["cluster_echo_max"], _to_int(row.get("cluster_echo_count")))
            bucket["variant_echo_max"] = max(bucket["variant_echo_max"], _to_int(row.get("variant_echo_count")))
            bucket["locations"].add(location)
            if box_id:
                bucket["boxes"][box_id] += 1
            if column:
                bucket["columns"][column] += 1
            if method:
                bucket["methods"][method] += 1
            if mode:
                bucket["modes"][mode] += 1
            if area:
                bucket["areas"][area] += 1
            if section:
                bucket["sections"][section] += 1
            for token, count in tokens.items():
                bucket["windows"][token] += int(count)

    out: List[Dict[str, Any]] = []
    for idx, bucket in grouped.items():
        row_count = len(bucket["locations"])
        box_count = len(bucket["boxes"])
        column_count = len(bucket["columns"])
        method_count = len(bucket["methods"])
        window_count = len(bucket["windows"])
        assigned_box_score = (
            float(bucket["score_total"])
            + 0.75 * float(row_count)
            + 0.35 * float(box_count)
            + 0.25 * float(column_count)
            + 0.30 * float(method_count)
            + 0.15 * float(len(bucket["modes"]))
            + 0.15 * float(len(bucket["areas"]))
            + 0.30 * float(bucket["currentness_max"])
        )
        out.append(
            {
                "vtrac_index": int(idx),
                "assigned_box_score": round(assigned_box_score, 3),
                "row_count": int(row_count),
                "box_count": int(box_count),
                "column_count": int(column_count),
                "window_count": int(window_count),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "box_pair_agree_max": round(float(bucket["box_pair_agree_max"]), 3),
                "cluster_echo_max": int(bucket["cluster_echo_max"]),
                "variant_echo_max": int(bucket["variant_echo_max"]),
                "top_windows": _counter_top(bucket["windows"], top_n=6),
                "top_boxes": _counter_top(bucket["boxes"], top_n=4),
                "column_mix": _counter_top(bucket["columns"], top_n=4),
                "method_mix": _counter_top(bucket["methods"], top_n=4),
                "mode_mix": _counter_top(bucket["modes"], top_n=3),
                "why_tags": [
                    "assigned_box_vtrac_strength",
                    f"rows={row_count}",
                    f"boxes={box_count}",
                    f"windows={window_count}",
                ],
            }
        )

    out.sort(
        key=lambda item: (
            -float(item["assigned_box_score"]),
            -int(item["row_count"]),
            -int(item["window_count"]),
            int(item["vtrac_index"]),
        )
    )
    return out[:top_n]


def _derive_vtrac_fusion_strength(
    *,
    gateway_rows: Sequence[Dict[str, Any]],
    cluster_rows: Sequence[Dict[str, Any]],
    assigned_box_rows: Sequence[Dict[str, Any]],
    structural_signals: Dict[str, Any],
    top_n: int,
) -> List[Dict[str, Any]]:
    grouped: Dict[int, Dict[str, Any]] = {}

    def _bucket_for(idx: int) -> Dict[str, Any]:
        return grouped.setdefault(
            idx,
            {
                "vtrac_index": idx,
                "gateway_score": 0.0,
                "gateway_rank": 999,
                "gateway_members": 0,
                "cluster_score": 0.0,
                "cluster_rank": 999,
                "cluster_supports": 0,
                "assigned_box_score": 0.0,
                "assigned_box_rank": 999,
                "box_rows": 0,
                "box_count": 0,
                "column_count": 0,
                "box_currentness": 0.0,
                "box_cluster_echo": 0,
                "box_variant_echo": 0,
                "top_families": Counter(),
                "top_patterns": Counter(),
                "top_windows": Counter(),
                "why_tags": [],
            },
        )

    top_gateway_score = max((float(item.get("gateway_score") or 0.0) for item in gateway_rows), default=0.0)
    top_cluster_score = max((float(item.get("cluster_score") or 0.0) for item in cluster_rows), default=0.0)
    top_box_score = max((float(item.get("assigned_box_score") or 0.0) for item in assigned_box_rows), default=0.0)

    for rank, row in enumerate(gateway_rows, start=1):
        idx = _to_int(row.get("vtrac_index"), -1)
        if idx < 0:
            continue
        bucket = _bucket_for(idx)
        bucket["gateway_score"] = float(row.get("gateway_score") or 0.0)
        bucket["gateway_rank"] = rank
        bucket["gateway_members"] = _to_int(row.get("member_count"), 0)
        for entry in row.get("top_families") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["top_families"][token] += max(1, _to_int(entry.get("count"), 1))
        for entry in row.get("top_patterns") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["top_patterns"][token] += max(1, _to_int(entry.get("count"), 1))

    for rank, row in enumerate(cluster_rows, start=1):
        idx = _to_int(row.get("vtrac_index"), -1)
        if idx < 0:
            continue
        bucket = _bucket_for(idx)
        bucket["cluster_score"] = float(row.get("cluster_score") or 0.0)
        bucket["cluster_rank"] = rank
        bucket["cluster_supports"] = _to_int(row.get("support_class_count"), 0)
        for entry in row.get("top_families") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["top_families"][token] += max(1, _to_int(entry.get("count"), 1))
        for entry in row.get("top_patterns") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["top_patterns"][token] += max(1, _to_int(entry.get("count"), 1))

    for rank, row in enumerate(assigned_box_rows, start=1):
        idx = _to_int(row.get("vtrac_index"), -1)
        if idx < 0:
            continue
        bucket = _bucket_for(idx)
        bucket["assigned_box_score"] = float(row.get("assigned_box_score") or 0.0)
        bucket["assigned_box_rank"] = rank
        bucket["box_rows"] = _to_int(row.get("row_count"), 0)
        bucket["box_count"] = _to_int(row.get("box_count"), 0)
        bucket["column_count"] = _to_int(row.get("column_count"), 0)
        bucket["box_currentness"] = float(row.get("currentness_max") or 0.0)
        bucket["box_cluster_echo"] = _to_int(row.get("cluster_echo_max"), 0)
        bucket["box_variant_echo"] = _to_int(row.get("variant_echo_max"), 0)
        for entry in row.get("top_windows") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["top_windows"][token] += max(1, _to_int(entry.get("count"), 1))

    progression = _to_int(structural_signals.get("consecutive_box_progression"), 0)
    neighbor_support = _to_int(structural_signals.get("neighbor_box_support"), 0)
    reveal_purity = _to_int(structural_signals.get("reveal_purity"), 0)
    precluster_strength = float(structural_signals.get("pre_reduction_cluster_strength") or 0.0)
    early_activation = float(structural_signals.get("early_activation_strength") or 0.0)
    section_structural_support = (
        1.5 * float(max(0, progression - 1))
        + 0.9 * float(max(0, neighbor_support))
        + 0.55 * float(max(0, reveal_purity))
        + 0.45 * float(max(0.0, precluster_strength))
        + 5.0 * float(max(0.0, early_activation))
    )
    structural_ready = (
        progression >= 2
        or neighbor_support >= 1
        or reveal_purity >= 1
        or precluster_strength >= 1.0
        or early_activation >= 0.15
    )

    out: List[Dict[str, Any]] = []
    for idx, bucket in grouped.items():
        gateway_rank = int(bucket["gateway_rank"])
        cluster_rank = int(bucket["cluster_rank"])
        box_rank = int(bucket["assigned_box_rank"])
        gateway_visible = gateway_rank <= 20
        cluster_visible = cluster_rank <= 20
        box_visible = box_rank <= 20

        gateway_norm = float(bucket["gateway_score"]) / float(top_gateway_score or 1.0)
        cluster_norm = float(bucket["cluster_score"]) / float(top_cluster_score or 1.0)
        box_norm = float(bucket["assigned_box_score"]) / float(top_box_score or 1.0)

        gateway_rank_bonus = max(0.0, 10.5 - 0.65 * float(gateway_rank)) if gateway_visible else 0.0
        cluster_rank_bonus = max(0.0, 11.5 - 0.70 * float(cluster_rank)) if cluster_visible else 0.0
        box_rank_bonus = max(0.0, 12.0 - 0.62 * float(box_rank)) if box_visible else 0.0

        fusion_score = (
            11.0 * box_norm
            + 9.0 * cluster_norm
            + 7.0 * gateway_norm
            + 0.85 * box_rank_bonus
            + 0.75 * cluster_rank_bonus
            + 0.55 * gateway_rank_bonus
        )

        agreement_bonus = 0.0
        rescue_bonus = 0.0
        penalty = 0.0
        why_tags = ["vtrac_fusion_strength"]

        if box_visible and cluster_visible:
            agreement_bonus += 10.0
            if box_rank <= 10 and cluster_rank <= 10:
                agreement_bonus += 4.0
            if box_rank <= 5 and cluster_rank <= 5:
                agreement_bonus += 6.0
            why_tags.append("box_cluster_agree")
        if box_visible and gateway_visible:
            agreement_bonus += 4.5
            if box_rank <= 10 and gateway_rank <= 10:
                agreement_bonus += 2.5
            why_tags.append("box_gateway_agree")
        if cluster_visible and gateway_visible:
            agreement_bonus += 3.0
            why_tags.append("cluster_gateway_agree")

        rescue_ready = (
            box_rank <= 10
            and not cluster_visible
            and not gateway_visible
            and int(bucket["box_rows"]) >= 3
            and int(bucket["box_count"]) >= 2
            and (
                int(bucket["box_cluster_echo"]) >= 1
                or int(bucket["box_variant_echo"]) >= 1
                or int(bucket["column_count"]) >= 2
            )
        )
        if rescue_ready:
            rescue_bonus += 8.0
            if box_rank <= 5:
                rescue_bonus += 3.5
            if int(bucket["box_rows"]) >= 5:
                rescue_bonus += 2.5
            if structural_ready:
                rescue_bonus += min(6.0, 0.55 * section_structural_support)
            why_tags.append("assigned_box_rescue")
        elif box_visible and not cluster_visible and not gateway_visible:
            # Keep box-only lanes visible, but avoid over-promoting thin box-only echoes.
            if int(bucket["box_rows"]) <= 2 or int(bucket["box_count"]) <= 1:
                penalty += 4.0
                why_tags.append("thin_box_only_penalty")

        fusion_score += agreement_bonus + rescue_bonus - penalty

        out.append(
            {
                "vtrac_index": int(idx),
                "fusion_score": round(fusion_score, 3),
                "agreement_bonus": round(agreement_bonus, 3),
                "rescue_bonus": round(rescue_bonus, 3),
                "penalty": round(penalty, 3),
                "gateway_rank": gateway_rank if gateway_visible else None,
                "cluster_rank": cluster_rank if cluster_visible else None,
                "assigned_box_rank": box_rank if box_visible else None,
                "gateway_score_component": round(float(bucket["gateway_score"]), 3),
                "cluster_score_component": round(float(bucket["cluster_score"]), 3),
                "assigned_box_score_component": round(float(bucket["assigned_box_score"]), 3),
                "box_rows": int(bucket["box_rows"]),
                "box_count": int(bucket["box_count"]),
                "column_count": int(bucket["column_count"]),
                "box_currentness_max": round(float(bucket["box_currentness"]), 3),
                "box_cluster_echo_max": int(bucket["box_cluster_echo"]),
                "box_variant_echo_max": int(bucket["box_variant_echo"]),
                "top_families": _counter_top(bucket["top_families"], top_n=5),
                "top_patterns": _counter_top(bucket["top_patterns"], top_n=6),
                "top_windows": _counter_top(bucket["top_windows"], top_n=6),
                "why_tags": why_tags[:8],
            }
        )

    out.sort(
        key=lambda item: (
            -float(item["fusion_score"]),
            -float(item["assigned_box_score_component"]),
            -float(item["cluster_score_component"]),
            int(item["vtrac_index"]),
        )
    )
    return out[:top_n]


def _derive_vtrac_cluster_strength(
    *,
    trace_rows: Sequence[Dict[str, Any]],
    lane_rows: Sequence[Dict[str, Any]],
    corridor_rows: Sequence[Dict[str, Any]],
    gateway_rows: Sequence[Dict[str, Any]],
    double_rows: Sequence[Dict[str, Any]],
    row_repeat_rows: Sequence[Dict[str, Any]],
    fourth_rows: Sequence[Dict[str, Any]],
    top_n: int,
) -> List[Dict[str, Any]]:
    grouped: Dict[int, Dict[str, Any]] = {}

    def _bucket_for(idx: int) -> Dict[str, Any]:
        return grouped.setdefault(
            idx,
            {
                "vtrac_index": idx,
                "support_classes": set(),
                "families": Counter(),
                "patterns": Counter(),
                "bands": Counter(),
                "scopes": Counter(),
                "trace_score": 0.0,
                "lane_score": 0.0,
                "corridor_score": 0.0,
                "gateway_score": 0.0,
                "double_score": 0.0,
                "row_repeat_score": 0.0,
                "fourth_score": 0.0,
                "currentness_max": 0.0,
                "member_family_count": 0,
                "member_pattern_count": 0,
            },
        )

    def _add_family_rows(
        rows: Sequence[Dict[str, Any]],
        *,
        row_score_key: str,
        bucket_score_key: str,
        support_label: str,
    ) -> None:
        for row in rows:
            idx = _vtrac_index_of_token(row.get("family_id"))
            if idx is None:
                top_patterns = list(row.get("top_patterns") or [])
                if top_patterns:
                    idx = _vtrac_index_of_token(top_patterns[0].get("value"))
            if idx is None:
                continue
            bucket = _bucket_for(idx)
            bucket["support_classes"].add(support_label)
            family_id = str(row.get("family_id") or "")
            if family_id:
                bucket["families"][family_id] += 1
            for entry in row.get("top_patterns") or []:
                token = _digits_only(entry.get("value"))
                if token:
                    bucket["patterns"][token] += max(1, _to_int(entry.get("count"), 1))
            bucket[bucket_score_key] += float(row.get(row_score_key) or 0.0)
            bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    _add_family_rows(trace_rows, row_score_key="trace_score", bucket_score_key="trace_score", support_label="trace")
    _add_family_rows(
        lane_rows,
        row_score_key="lane_confidence_score",
        bucket_score_key="lane_score",
        support_label="lane",
    )

    for row in corridor_rows:
        idx = _vtrac_index_of_token(row.get("family_id"))
        if idx is None:
            top_patterns = list(row.get("top_patterns") or [])
            if top_patterns:
                idx = _vtrac_index_of_token(top_patterns[0].get("value"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        bucket["support_classes"].add("corridor")
        family_id = str(row.get("family_id") or "")
        if family_id:
            bucket["families"][family_id] += 1
        for entry in row.get("top_patterns") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["patterns"][token] += max(1, _to_int(entry.get("count"), 1))
        scope = str(row.get("corridor_scope") or "")
        band = str(row.get("corridor_band") or "")
        if scope:
            bucket["scopes"][scope] += 1
        if band:
            bucket["bands"][band] += 1
        bucket["corridor_score"] += float(row.get("corridor_strength_score") or 0.0)
        bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    for row in gateway_rows:
        idx = _to_int(row.get("vtrac_index"), -1)
        if idx < 0:
            continue
        bucket = _bucket_for(idx)
        bucket["support_classes"].add("gateway")
        bucket["gateway_score"] += float(row.get("gateway_score") or 0.0)
        for entry in row.get("top_families") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["families"][token] += max(1, _to_int(entry.get("count"), 1))
        for entry in row.get("top_patterns") or []:
            token = _digits_only(entry.get("value"))
            if token:
                bucket["patterns"][token] += max(1, _to_int(entry.get("count"), 1))
        for entry in row.get("scope_mix") or []:
            scope = str(entry.get("value") or "")
            if scope:
                bucket["scopes"][scope] += max(1, _to_int(entry.get("count"), 1))
        for entry in row.get("band_mix") or []:
            band = str(entry.get("value") or "")
            if band:
                bucket["bands"][band] += max(1, _to_int(entry.get("count"), 1))
        bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    for row in double_rows:
        idx = _vtrac_index_of_token(row.get("pattern"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        bucket["support_classes"].add("double")
        token = _digits_only(row.get("pattern"))
        if token:
            bucket["patterns"][token] += max(1, _to_int(row.get("rows"), 1))
        family_id = str(row.get("family_id") or "")
        if family_id:
            bucket["families"][family_id] += 1
        bucket["double_score"] += float(row.get("double_score") or 0.0)
        bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    for row in row_repeat_rows:
        idx = _vtrac_index_of_token(row.get("value"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        bucket["support_classes"].add("row_repeat")
        token = _digits_only(row.get("value"))
        if token:
            bucket["patterns"][token] += max(1, _to_int(row.get("rows_repeated"), 1))
        bucket["row_repeat_score"] += float(row.get("score") or 0.0)
        bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    for row in fourth_rows:
        idx = _vtrac_index_of_token(row.get("core_value"))
        if idx is None:
            continue
        bucket = _bucket_for(idx)
        bucket["support_classes"].add("fourth")
        token = _digits_only(row.get("core_value"))
        if token:
            bucket["patterns"][token] += max(1, _to_int(row.get("support_count"), 1))
        bucket["fourth_score"] += float(row.get("score") or 0.0)
        bucket["currentness_max"] = max(bucket["currentness_max"], float(row.get("currentness_max") or 0.0))

    out: List[Dict[str, Any]] = []
    for idx, bucket in grouped.items():
        bucket["member_family_count"] = len([k for k in bucket["families"] if k])
        bucket["member_pattern_count"] = len([k for k in bucket["patterns"] if k])
        support_class_count = len(bucket["support_classes"])

        cluster_score = (
            0.9 * (float(bucket["trace_score"]) ** 0.5)
            + 1.2 * (float(bucket["lane_score"]) ** 0.5)
            + 0.75 * (float(bucket["corridor_score"]) ** 0.5)
            + 0.9 * (float(bucket["gateway_score"]) ** 0.5)
            + 1.1 * (float(bucket["double_score"]) ** 0.5)
            + 1.0 * (float(bucket["row_repeat_score"]) ** 0.5)
            + 0.85 * (float(bucket["fourth_score"]) ** 0.5)
            + 1.8 * float(support_class_count)
            + 0.9 * float(bucket["member_family_count"])
            + 0.35 * float(bucket["member_pattern_count"])
            + 0.6 * float(len([k for k in bucket["scopes"] if k]))
            + 0.4 * float(len([k for k in bucket["bands"] if k]))
            + 0.25 * float(bucket["currentness_max"])
        )

        out.append(
            {
                "vtrac_index": int(idx),
                "cluster_score": round(cluster_score, 3),
                "raw_cluster_score": round(cluster_score, 3),
                "cluster_adjustment": 0.0,
                "support_class_count": int(support_class_count),
                "support_classes": sorted(bucket["support_classes"]),
                "member_family_count": int(bucket["member_family_count"]),
                "member_pattern_count": int(bucket["member_pattern_count"]),
                "trace_score_component": round(float(bucket["trace_score"]), 3),
                "lane_score_component": round(float(bucket["lane_score"]), 3),
                "corridor_score_component": round(float(bucket["corridor_score"]), 3),
                "gateway_score_component": round(float(bucket["gateway_score"]), 3),
                "double_score_component": round(float(bucket["double_score"]), 3),
                "row_repeat_score_component": round(float(bucket["row_repeat_score"]), 3),
                "fourth_score_component": round(float(bucket["fourth_score"]), 3),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "top_families": _counter_top(bucket["families"], top_n=5),
                "top_patterns": _counter_top(bucket["patterns"], top_n=6),
                "scope_mix": _counter_top(bucket["scopes"], top_n=4),
                "band_mix": _counter_top(bucket["bands"], top_n=4),
                "why_tags": [
                    "vtrac_cluster_strength",
                    f"supports={support_class_count}",
                    f"families={bucket['member_family_count']}",
                    f"patterns={bucket['member_pattern_count']}",
                ],
            }
        )

    if out:
        # Bounded promotion review:
        # when a single compact double-driven cluster dominates the raw score,
        # lightly rebalance toward structurally rich challengers instead of
        # letting compact attractors monopolize the top surface.
        top_raw = max(out, key=lambda item: float(item.get("raw_cluster_score") or 0.0))
        top_support = int(top_raw.get("support_class_count") or 0)
        top_families = int(top_raw.get("member_family_count") or 0)
        top_patterns = int(top_raw.get("member_pattern_count") or 0)
        top_currentness = float(top_raw.get("currentness_max") or 0.0)
        top_supports = set(top_raw.get("support_classes") or [])
        compact_monopoly = (
            top_support >= 5
            and top_families <= 1
            and top_patterns <= 1
            and "double" in top_supports
        )
        if compact_monopoly:
            challengers: List[Dict[str, Any]] = []
            for item in out:
                if item is top_raw:
                    continue
                support = int(item.get("support_class_count") or 0)
                families = int(item.get("member_family_count") or 0)
                patterns = int(item.get("member_pattern_count") or 0)
                currentness = float(item.get("currentness_max") or 0.0)
                currentness_gap = top_currentness - currentness
                if support >= 4 and (
                    currentness_gap <= 1.25
                    or families >= 2
                    or patterns >= 2
                ):
                    bonus = (
                        8.0
                        + 3.0 * float(max(0, support - 4))
                        + 3.0 * float(max(0, families - 1))
                        + 1.5 * float(max(0, patterns - 1))
                        + 4.0 * max(0.0, 1.25 - currentness_gap)
                    )
                    if "double" not in set(item.get("support_classes") or []):
                        bonus += 2.0
                    item["cluster_adjustment"] = round(float(item.get("cluster_adjustment") or 0.0) + bonus, 3)
                    item["cluster_score"] = round(float(item.get("raw_cluster_score") or 0.0) + float(item["cluster_adjustment"]), 3)
                    item.setdefault("why_tags", []).append("challenger_rebalance")
                    item["why_tags"].append(f"bonus={bonus:.3f}")
                    challengers.append(item)
            if challengers:
                top_penalty = 8.0
                top_raw["cluster_adjustment"] = round(float(top_raw.get("cluster_adjustment") or 0.0) - top_penalty, 3)
                top_raw["cluster_score"] = round(
                    float(top_raw.get("raw_cluster_score") or 0.0) + float(top_raw["cluster_adjustment"]),
                    3,
                )
                top_raw.setdefault("why_tags", []).append("compact_monopoly_penalty")
                top_raw["why_tags"].append(f"penalty={top_penalty:.3f}")

    out.sort(
        key=lambda item: (
            -float(item["cluster_score"]),
            -int(item["support_class_count"]),
            -int(item["member_family_count"]),
            int(item["vtrac_index"]),
        )
    )
    return out[:top_n]


def _derive_structural_signals(
    *,
    variant_rows: Sequence[Dict[str, Any]],
    candidate_rows: Sequence[Dict[str, Any]],
    training_ledgers: Dict[str, Any],
    corridors: Sequence[Dict[str, Any]],
    contains_winners_artifacts: bool,
) -> Dict[str, Any]:
    box_rows = list(training_ledgers.get("box_validity_ledger") or [])
    reveal_rows = list(training_ledgers.get("reduction_reveal_ledger") or [])
    precluster_rows = list(training_ledgers.get("precluster_ledger") or [])
    path_summary_count = len(box_rows)
    raw_exposure_count = len(variant_rows)

    early_hits = 0
    early_activation = 0.0
    if path_summary_count:
        for row in box_rows:
            if _to_int(row.get("first_3value_step"), -1) in {0, 1}:
                early_hits += 1
        early_activation = float(early_hits) / float(path_summary_count)

    grouped_draws: Dict[str, List[int]] = defaultdict(list)
    grouped_cols: Dict[str, List[int]] = defaultdict(list)
    neighbor_box_support = 0
    for row in box_rows:
        set_name = str(row.get("set") or "")
        draw_rank = _label_rank(row.get("draw"), "Draw", default=0)
        col_rank = _to_int(row.get("column"), 0)
        if draw_rank > 0:
            grouped_draws[set_name].append(draw_rank)
        if col_rank > 0:
            grouped_cols[f"{set_name}|{row.get('draw') or ''}"].append(col_rank)
        if bool(row.get("has_3value_reveal")) and col_rank in {2, 4}:
            neighbor_box_support += 1

    consecutive_draw_progression = max((_max_consecutive_run(values) for values in grouped_draws.values()), default=0)
    consecutive_col_progression = max((_max_consecutive_run(values) for values in grouped_cols.values()), default=0)
    consecutive_box_progression = max(consecutive_draw_progression, consecutive_col_progression)

    family_neighborhood_saturation = 0.0
    family_asymmetry = 0.0
    if corridors:
        family_neighborhood_saturation = max(float(item.get("family_neighborhood_saturation") or 0.0) for item in corridors)
        family_asymmetry = max(float(item.get("family_asymmetry_inside_corridor") or 0.0) for item in corridors)

    core_vs_clutter = 0.0
    if reveal_rows:
        core_vs_clutter = max(
            (
                float(_to_float(row.get("reveal_score")))
                + 0.75 * float(_to_int(row.get("purity_gain")))
                + 0.25 * float(_to_float(row.get("currentness_score")))
            )
            for row in reveal_rows
        )

    reveal_purity = max((_to_int(row.get("purity_gain")) for row in reveal_rows), default=0)
    precluster_strength = max((_to_float(row.get("precluster_score")) for row in precluster_rows), default=0.0)
    candidate_preview_count = len(candidate_rows)

    return {
        "raw_exposure_count": int(raw_exposure_count),
        "path_summary_count": int(path_summary_count),
        "early_activation_strength": round(float(early_activation), 3),
        "early_activation_hits": int(early_hits),
        "consecutive_box_progression": int(consecutive_box_progression),
        "neighbor_box_support": int(neighbor_box_support),
        "family_neighborhood_saturation": round(float(family_neighborhood_saturation), 3),
        "family_asymmetry_inside_corridor": round(float(family_asymmetry), 3),
        "core_vs_clutter_transit_score": round(float(core_vs_clutter), 3),
        "reveal_purity": int(reveal_purity),
        "pre_reduction_cluster_strength": round(float(precluster_strength), 3),
        "candidate_preview_count": int(candidate_preview_count),
        "overlay_summary_mismatch": {
            "available": False,
            "status": "requires_winner_artifacts",
            "reason": (
                "predictive_writer_has_no_winner_overlay_context"
                if not contains_winners_artifacts
                else "winner_overlay_audit_not_yet_attached_to_predictive_writer"
            ),
        },
    }


def _classify_empty_lens(
    *,
    strong_trace: Sequence[Dict[str, Any]],
    lane_only: Sequence[Dict[str, Any]],
    doubles: Sequence[Dict[str, Any]],
    row_repeat: Sequence[Dict[str, Any]],
    corridors: Sequence[Dict[str, Any]],
    training_ledgers: Dict[str, Any],
    structural_signals: Dict[str, Any],
    log_rows: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    raw_exposure_count = _to_int(structural_signals.get("raw_exposure_count"), 0)
    path_summary_count = _to_int(structural_signals.get("path_summary_count"), 0)
    cold_location_count = _to_int(training_ledgers.get("cold_location_count"), 0)
    cold_ratio = float(cold_location_count) / float(max(1, path_summary_count))
    trace_score = float(strong_trace[0]["trace_score"]) if strong_trace else 0.0
    lane_score = float(lane_only[0]["lane_confidence_score"]) if lane_only else 0.0
    double_score = float(doubles[0]["double_score"]) if doubles else 0.0
    row_repeat_score = float(row_repeat[0]["score"]) if row_repeat else 0.0
    corridor_score = float(corridors[0]["corridor_strength_score"]) if corridors else 0.0
    early_activation = float(structural_signals.get("early_activation_strength") or 0.0)
    reveal_purity = _to_int(structural_signals.get("reveal_purity"), 0)
    precluster_strength = float(structural_signals.get("pre_reduction_cluster_strength") or 0.0)
    core_vs_clutter = float(structural_signals.get("core_vs_clutter_transit_score") or 0.0)
    neighbor_support = _to_int(structural_signals.get("neighbor_box_support"), 0)
    progression = _to_int(structural_signals.get("consecutive_box_progression"), 0)
    candidate_preview_count = _to_int(structural_signals.get("candidate_preview_count"), 0)

    positive_score = (
        0.22 * trace_score
        + 0.85 * lane_score
        + 0.45 * double_score
        + 0.45 * row_repeat_score
        + 0.18 * corridor_score
        + 4.0 * early_activation
        + 0.7 * precluster_strength
        + 0.6 * core_vs_clutter
        + 0.9 * reveal_purity
        + 0.35 * neighbor_support
        + 0.3 * progression
    )
    positive_score += min(3.0, raw_exposure_count * 0.1)

    reasons: List[str] = []
    if not strong_trace:
        reasons.append("no_strong_trace_families")
    if not training_ledgers["precluster_ledger"]:
        reasons.append("no_preclusters")
    if not training_ledgers["reduction_reveal_ledger"]:
        reasons.append("no_reveals")
    if cold_ratio >= 0.95 and path_summary_count > 0:
        reasons.append("all_locations_cold")
    elif cold_ratio >= 0.65:
        reasons.append("mostly_cold_locations")
    if candidate_preview_count == 0:
        reasons.append("no_candidate_preview")

    if raw_exposure_count == 0 and path_summary_count == 0:
        classification = "true_empty"
    elif (
        not strong_trace
        and not lane_only
        and not training_ledgers["reduction_reveal_ledger"]
        and row_repeat_score <= 1.0
        and cold_ratio >= 0.9
    ):
        classification = "true_empty"
    elif positive_score >= 9.0 and cold_ratio < 0.9:
        classification = "positive_trace"
    elif positive_score >= 5.5 or (trace_score > 0.0 and path_summary_count > 0):
        classification = "active_low_trust"
    else:
        classification = "true_empty"

    if classification == "positive_trace":
        confidence = min(1.0, 0.45 + positive_score / 22.0)
    elif classification == "active_low_trust":
        confidence = min(1.0, 0.35 + positive_score / 18.0)
    else:
        confidence = min(1.0, 0.45 + (cold_ratio * 0.35) + (0.2 if raw_exposure_count <= 2 else 0.0))

    return {
        "classification": classification,
        "is_sparse": classification == "true_empty",
        "confidence": round(float(confidence), 3),
        "positive_signal_score": round(float(positive_score), 3),
        "reasons": reasons or ["none"],
        "cold_location_count": int(cold_location_count),
        "cold_ratio": round(float(cold_ratio), 3),
        "raw_exposure_count": int(raw_exposure_count),
        "path_summary_count": int(path_summary_count),
    }


def _build_training_ledgers(
    items: Sequence[Dict[str, Any]],
    *,
    top_preclusters: int,
    top_reveals: int,
    top_row_repeat: int,
    top_fourth: int,
) -> Dict[str, Any]:
    preclusters: List[Dict[str, Any]] = []
    reveals: List[Dict[str, Any]] = []
    box_activity: List[Dict[str, Any]] = []
    row_repeat_counter: Dict[str, Dict[str, Any]] = {}
    fourth_counter: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    cold_locations = 0

    for item in items:
        location = str(item.get("location") or "")
        section = str(item.get("section") or "")
        area = str(item.get("area") or "")
        method = str(item.get("method") or "")
        mode = str(item.get("mode") or "")
        steps = list(item.get("steps") or [])
        if not location or not steps:
            continue
        grid = dict(item.get("grid_position") or {})
        seq_meta = dict(item.get("sequence_meta") or {})
        step0 = dict(steps[0]) if steps else {}
        set_rank = _to_int(grid.get("set_rank"), 3)
        draw_rank = _to_int(grid.get("draw_rank"), 3)
        col_rank = _to_int(grid.get("col_rank"), 7)
        area_rank = _to_int(grid.get("area_rank"), 3)
        currentness = _currentness_score(
            set_rank=set_rank,
            draw_rank=draw_rank,
            col_rank=col_rank,
            area_rank=area_rank,
        )
        first_3value_step = _to_int(seq_meta.get("first_3value_step"), -1)
        last_change_step = _to_int(seq_meta.get("last_change_step"), -1)
        final_value = _digits_only((item.get("final") or {}).get("value"))

        precluster_score = (
            _to_float(step0.get("length"))
            + 0.4 * _to_float(step0.get("unique_digits"))
            + 0.7 * currentness
        )
        preclusters.append(
            {
                "location": location,
                "section": section,
                "area": area,
                "method": method,
                "mode": mode,
                "step0_value": _digits_only(step0.get("value")),
                "step0_length": _to_int(step0.get("length")),
                "step0_unique_digits": _to_int(step0.get("unique_digits")),
                "first_3value_step": first_3value_step,
                "last_change_step": last_change_step,
                "final_value": final_value,
                "currentness_score": currentness,
                "precluster_score": round(precluster_score, 3),
            }
        )

        if first_3value_step >= 0 and first_3value_step < len(steps):
            core_step = dict(steps[first_3value_step])
            previous_step = dict(steps[first_3value_step - 1]) if first_3value_step > 0 else {}
            core_value = _digits_only(core_step.get("value"))
            before_value = _digits_only(previous_step.get("value"))
            reveal_score = (
                max(0.0, _to_float(previous_step.get("length")) - _to_float(core_step.get("length")))
                + max(0.0, _to_float(previous_step.get("unique_digits")) - _to_float(core_step.get("unique_digits")))
                + 0.5 * currentness
            )
            reveals.append(
                {
                    "location": location,
                    "section": section,
                    "area": area,
                    "method": method,
                    "mode": mode,
                    "core_step": first_3value_step,
                    "before_value": before_value,
                    "core_value": core_value,
                    "final_value": final_value,
                    "purity_gain": max(
                        0,
                        _to_int(previous_step.get("unique_digits")) - _to_int(core_step.get("unique_digits")),
                    ),
                    "reveal_score": round(reveal_score, 3),
                    "currentness_score": currentness,
                }
            )

            # Build fourth-variable evidence from the step immediately before the first 3-value-like core.
            if before_value and core_value:
                core_counter = Counter(core_value)
                before_counter = Counter(before_value)
                extras: List[str] = []
                for digit, count in before_counter.items():
                    extra_count = count - core_counter.get(digit, 0)
                    if extra_count > 0:
                        extras.extend([digit] * extra_count)
                if 1 <= len(extras) <= 2:
                    extra_digits = "".join(sorted(extras))
                    extra_vtrac = "".join(
                        sorted(
                            {
                                str(DIGIT_TO_VTRAC_VALUE[d])
                                for d in extra_digits
                                if d in DIGIT_TO_VTRAC_VALUE
                            }
                        )
                    )
                    key = ("".join(sorted(core_value)), extra_digits, extra_vtrac)
                    bucket = fourth_counter.setdefault(
                        key,
                        {
                            "core_value": "".join(sorted(core_value)),
                            "extra_digits": extra_digits,
                            "extra_vtrac_digits": extra_vtrac,
                            "locations": set(),
                            "methods": Counter(),
                            "modes": Counter(),
                            "sections": Counter(),
                            "currentness_max": 0.0,
                            "support_count": 0,
                            "examples": [],
                        },
                    )
                    bucket["locations"].add(location)
                    bucket["methods"][method] += 1
                    bucket["modes"][mode] += 1
                    bucket["sections"][section] += 1
                    bucket["currentness_max"] = max(bucket["currentness_max"], currentness)
                    bucket["support_count"] += 1
                    if len(bucket["examples"]) < 4:
                        bucket["examples"].append(
                            {
                                "location": location,
                                "before_value": before_value,
                                "core_value": core_value,
                                "step": first_3value_step,
                            }
                        )
        else:
            cold_locations += 1

        # row-repeat and final-survival objects
        seen_values: Counter[str] = Counter()
        for step in steps:
            value = _digits_only(step.get("value"))
            if not value:
                continue
            if _to_bool(step.get("is_3value")) or len(set(value)) <= 3:
                seen_values[value] += 1
        for value, count in seen_values.items():
            bucket = row_repeat_counter.setdefault(
                value,
                {
                    "value": value,
                    "rows_repeated": 0,
                    "locations": set(),
                    "methods": Counter(),
                    "modes": Counter(),
                    "sections": Counter(),
                    "terminal_hits": 0,
                    "currentness_max": 0.0,
                    "examples": [],
                },
            )
            bucket["rows_repeated"] += count
            bucket["locations"].add(location)
            bucket["methods"][method] += 1
            bucket["modes"][mode] += 1
            bucket["sections"][section] += 1
            if final_value == value:
                bucket["terminal_hits"] += 1
            bucket["currentness_max"] = max(bucket["currentness_max"], currentness)
            if len(bucket["examples"]) < 4:
                bucket["examples"].append({"location": location, "count": count})

        box_activity.append(
            {
                "location": location,
                "section": section,
                "area": area,
                "method": method,
                "mode": mode,
                "set": str(item.get("set") or ""),
                "draw": str(item.get("draw") or ""),
                "column": str(item.get("col") or ""),
                "first_3value_step": first_3value_step,
                "last_change_step": last_change_step,
                "steps_total": _to_int(seq_meta.get("steps_kept_after_compaction")),
                "final_value": final_value,
                "has_3value_reveal": first_3value_step >= 0,
                "currentness_score": currentness,
            }
        )

    preclusters.sort(key=lambda item: (-float(item["precluster_score"]), item["location"]))
    reveals.sort(key=lambda item: (-float(item["reveal_score"]), item["location"]))
    box_activity.sort(
        key=lambda item: (-float(item["currentness_score"]), int(not item["has_3value_reveal"]), item["location"])
    )

    row_repeat_out: List[Dict[str, Any]] = []
    for value, bucket in row_repeat_counter.items():
        score = (
            float(bucket["rows_repeated"])
            + 2.0 * float(bucket["terminal_hits"])
            + 0.5 * float(len(bucket["locations"]))
            + 0.25 * float(bucket["currentness_max"])
        )
        row_repeat_out.append(
            {
                "value": value,
                "rows_repeated": int(bucket["rows_repeated"]),
                "location_count": len(bucket["locations"]),
                "terminal_hits": int(bucket["terminal_hits"]),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "score": round(score, 3),
                "top_methods": _counter_top(bucket["methods"], top_n=3),
                "top_modes": _counter_top(bucket["modes"], top_n=3),
                "top_sections": _counter_top(bucket["sections"], top_n=3),
                "examples": bucket["examples"],
                "is_duplicate_pattern": _is_duplicate_pattern(value),
                "vtrac_signature": _vtrac_signature(value),
            }
        )
    row_repeat_out.sort(key=lambda item: (-float(item["score"]), item["value"]))

    fourth_out: List[Dict[str, Any]] = []
    for (_, _, _), bucket in fourth_counter.items():
        score = (
            float(bucket["support_count"])
            + 0.75 * float(len(bucket["locations"]))
            + 0.35 * float(bucket["currentness_max"])
        )
        fourth_out.append(
            {
                "core_value": bucket["core_value"],
                "extra_digits": bucket["extra_digits"],
                "extra_vtrac_digits": bucket["extra_vtrac_digits"],
                "support_count": int(bucket["support_count"]),
                "location_count": len(bucket["locations"]),
                "currentness_max": round(float(bucket["currentness_max"]), 3),
                "score": round(score, 3),
                "top_methods": _counter_top(bucket["methods"], top_n=3),
                "top_modes": _counter_top(bucket["modes"], top_n=3),
                "top_sections": _counter_top(bucket["sections"], top_n=3),
                "examples": list(bucket["examples"]),
            }
        )
    fourth_out.sort(key=lambda item: (-float(item["score"]), item["core_value"], item["extra_digits"]))

    return {
        "precluster_ledger": preclusters[:top_preclusters],
        "reduction_reveal_ledger": reveals[:top_reveals],
        "row_repeat_and_final_survival": row_repeat_out[:top_row_repeat],
        "fourth_variable_candidates": fourth_out[:top_fourth],
        "box_validity_ledger": box_activity[: min(len(box_activity), max(top_preclusters, 25))],
        "cold_location_count": cold_locations,
    }


def build_dr_arena_payload(
    *,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: Optional[str],
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
    top_trace: int = 10,
    top_lane: int = 10,
    top_competing: int = 10,
    top_double: int = 10,
    top_vtrac_gateway: int = 10,
    top_vtrac_cluster: int = 10,
    top_assigned_box_vtrac: int = 10,
    top_vtrac_fusion: int = 10,
    top_row_repeat: int = 10,
    top_preclusters: int = 12,
    top_reveals: int = 12,
    top_fourth: int = 10,
) -> Optional[Dict[str, Any]]:
    bundle = _load_dr_bundle(state_dir=state_dir, state_key=state_key)
    if bundle is None:
        return None

    input_paths: List[Path] = [
        bundle["meta_path"],
        bundle["per_item_path"],
        bundle["top_candidates_path"],
        bundle["logs_path"],
    ]
    if bundle["steps_path"] is not None:
        input_paths.append(bundle["steps_path"])
    if bundle["scores_path"] is not None:
        input_paths.append(bundle["scores_path"])

    logs_items = list((bundle["logs"] or {}).get("items") or [])
    payload: Dict[str, Any] = {
        "tool": "digit_reduction_arena",
        "version": 1,
        "schema_revision": "v1.1",
        "state": state_key,
        "results_date": results_date,
        "history_date": history_date,
        "profile": profile,
        "experiment_tag": experiment_tag or None,
        "contains_winners_artifacts": contains_winners_artifacts,
        "inputs_hash": _hash_inputs(input_paths),
        "paths": {
            "sharepacks_root": _safe_rel(sharepacks_root, repo_root),
            "state_dir": _safe_rel(state_dir, repo_root),
            "digit_reduction_dir": _safe_rel(state_dir / "digit_reduction" / state_key, repo_root),
            "per_item_csv": _safe_rel(bundle["per_item_path"], repo_root),
            "top_candidates_csv": _safe_rel(bundle["top_candidates_path"], repo_root),
            "meta_json": _safe_rel(bundle["meta_path"], repo_root),
            "training_logs_json": _safe_rel(bundle["logs_path"], repo_root),
            "training_steps_csv": _safe_rel(bundle["steps_path"], repo_root) if bundle["steps_path"] else None,
        },
        "meta": {
            "cluster_scan": dict((bundle["meta"] or {}).get("cluster_scan") or {}),
            "scoring_v2": dict((bundle["meta"] or {}).get("scoring_v2") or {}),
            "lockscore": dict((bundle["meta"] or {}).get("lockscore") or {}),
            "policy": dict((bundle["meta"] or {}).get("policy") or {}),
        },
        "sections": {},
    }

    per_item_rows = list(bundle["per_item"])
    top_candidate_rows = list(bundle["top_candidates"])
    for section in sorted({str(r.get("variant") or "") for r in per_item_rows + top_candidate_rows if str(r.get("variant") or "").strip()}, key=_section_sort_key):
        variant_rows = [r for r in per_item_rows if str(r.get("variant") or "") == section]
        candidate_rows = [r for r in top_candidate_rows if str(r.get("variant") or "") == section]
        log_rows = [item for item in logs_items if str(item.get("section") or "") == section]
        families = _aggregate_family_rows(variant_rows)
        patterns = _aggregate_pattern_rows(variant_rows)
        training_ledgers = _build_training_ledgers(
            log_rows,
            top_preclusters=top_preclusters,
            top_reveals=top_reveals,
            top_row_repeat=top_row_repeat,
            top_fourth=top_fourth,
        )

        strong_trace = _derive_trace_strength(families, top_n=top_trace)
        lane_only = _derive_lane_only_confidence(families, top_n=top_lane)
        competing = _derive_competing_literal_pressure(patterns, candidate_rows, top_n=top_competing)
        doubles = _derive_double_pressure(patterns, top_n=top_double)
        corridors = _derive_corridors(families, top_n=top_trace)
        vtrac_gateway = _derive_vtrac_lane_gateway(
            families=families,
            patterns=patterns,
            candidate_rows=candidate_rows,
            corridors=corridors,
            top_n=top_vtrac_gateway,
        )
        assigned_box_vtrac = _derive_assigned_box_vtrac_strength(
            variant_rows=variant_rows,
            top_n=top_assigned_box_vtrac,
        )
        structural_signals = _derive_structural_signals(
            variant_rows=variant_rows,
            candidate_rows=candidate_rows,
            training_ledgers=training_ledgers,
            corridors=corridors,
            contains_winners_artifacts=contains_winners_artifacts,
        )
        vtrac_clusters = _derive_vtrac_cluster_strength(
            trace_rows=strong_trace,
            lane_rows=lane_only,
            corridor_rows=corridors,
            gateway_rows=vtrac_gateway,
            double_rows=doubles,
            row_repeat_rows=training_ledgers["row_repeat_and_final_survival"],
            fourth_rows=training_ledgers["fourth_variable_candidates"],
            top_n=top_vtrac_cluster,
        )
        vtrac_fusion = _derive_vtrac_fusion_strength(
            gateway_rows=vtrac_gateway,
            cluster_rows=vtrac_clusters,
            assigned_box_rows=assigned_box_vtrac,
            structural_signals=structural_signals,
            top_n=top_vtrac_fusion,
        )
        empty_lens = _classify_empty_lens(
            strong_trace=strong_trace,
            lane_only=lane_only,
            doubles=doubles,
            row_repeat=training_ledgers["row_repeat_and_final_survival"],
            corridors=corridors,
            training_ledgers=training_ledgers,
            structural_signals=structural_signals,
            log_rows=log_rows,
        )

        payload["sections"][section] = {
            "summary": {
                "per_item_rows": len(variant_rows),
                "raw_exposure_count": int(structural_signals["raw_exposure_count"]),
                "path_summary_count": int(structural_signals["path_summary_count"]),
                "top_candidate_rows": len(candidate_rows),
                "training_locations": len(log_rows),
                "unique_patterns": len(patterns),
                "unique_families": len(families),
                "max_score_v2": max((_to_float(r.get("score_v2")) for r in variant_rows), default=0.0),
                "top_candidate_preview": [
                    {
                        "rank": _to_int(row.get("rank")),
                        "best_pattern": _digits_only(row.get("best_pattern")),
                        "family_id": str(row.get("family_id") or ""),
                        "score_v2": round(_to_float(row.get("score_v2")), 3),
                        "vt_only_lane": _to_bool(row.get("vt_only_lane")),
                        "funnel_precol1": _to_bool(row.get("funnel_precol1")),
                    }
                    for row in candidate_rows[:6]
                ],
            },
            "dr_trace_strength": strong_trace,
            "dr_lane_only_confidence": lane_only,
            "dr_competing_literal_pressure": competing,
            "dr_double_pressure": doubles,
            "dr_vtrac_lane_gateway": vtrac_gateway,
            "dr_vtrac_cluster_strength": vtrac_clusters,
            "dr_assigned_box_vtrac_strength": assigned_box_vtrac,
            "dr_vtrac_fusion_strength": vtrac_fusion,
            "dr_row_repeat_and_final_survival": training_ledgers["row_repeat_and_final_survival"],
            "dr_corridor_strength": corridors,
            "dr_empty_lens": empty_lens,
            "dr_structural_signals": structural_signals,
            "precluster_ledger": training_ledgers["precluster_ledger"],
            "reduction_reveal_ledger": training_ledgers["reduction_reveal_ledger"],
            "box_validity_ledger": training_ledgers["box_validity_ledger"],
            "fourth_variable_candidates": training_ledgers["fourth_variable_candidates"],
        }

    return payload


def build_dr_arena_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append(f"# DR Arena — {payload.get('state', 'Unknown')} ({payload.get('results_date', '')})")
    lines.append("")
    lines.append("- Predictive-side DR evidence canvas (winners-free)")
    lines.append(
        f"- inputs_hash: `{payload.get('inputs_hash', '')[:16]}` | profile: `{payload.get('profile', '')}` | experiment: `{payload.get('experiment_tag') or 'none'}` | schema: `{payload.get('schema_revision', 'v1')}`"
    )
    lines.append("")

    for section, section_payload in sorted(payload.get("sections", {}).items(), key=lambda kv: _section_sort_key(kv[0])):
        summary = dict(section_payload.get("summary") or {})
        lines.append(f"## {section}")
        lines.append("")
        lines.append(
            f"- rows={summary.get('per_item_rows', 0)} | raw_exposure={summary.get('raw_exposure_count', 0)} | path_summary={summary.get('path_summary_count', 0)} | top_candidates={summary.get('top_candidate_rows', 0)} | "
            f"locations={summary.get('training_locations', 0)} | families={summary.get('unique_families', 0)} | "
            f"patterns={summary.get('unique_patterns', 0)} | max_score_v2={summary.get('max_score_v2', 0.0):.3f}"
        )
        empty = dict(section_payload.get("dr_empty_lens") or {})
        lines.append(
            f"- empty_lens={empty.get('classification', 'unknown')} | sparse={bool(empty.get('is_sparse'))} | reasons={', '.join(empty.get('reasons') or ['none'])}"
        )
        lines.append("")

        def _emit_table(title: str, rows: Sequence[Dict[str, Any]], cols: Sequence[Tuple[str, str]]) -> None:
            lines.append(f"### {title}")
            lines.append("")
            if not rows:
                lines.append("_None_")
                lines.append("")
                return
            lines.append("| " + " | ".join(label for label, _ in cols) + " |")
            lines.append("|" + "|".join(["---"] * len(cols)) + "|")
            for row in rows:
                values: List[str] = []
                for _, key in cols:
                    value = row.get(key, "")
                    if isinstance(value, float):
                        values.append(f"{value:.3f}")
                    elif isinstance(value, list):
                        if value and isinstance(value[0], dict) and "value" in value[0]:
                            values.append(", ".join(str(item.get("value")) for item in value[:3]))
                        else:
                            values.append(", ".join(str(v) for v in value[:3]))
                    else:
                        values.append(str(value))
                lines.append("| " + " | ".join(values) + " |")
            lines.append("")

        _emit_table(
            "Trace Strength",
            section_payload.get("dr_trace_strength", [])[:6],
            (
                ("Family", "family_id"),
                ("Trace", "trace_score"),
                ("Rows", "rows"),
                ("Boxes", "box_count"),
                ("Top Patterns", "top_patterns"),
            ),
        )
        _emit_table(
            "Lane Only",
            section_payload.get("dr_lane_only_confidence", [])[:6],
            (
                ("Family", "family_id"),
                ("Lane", "lane_confidence_score"),
                ("VT Rows", "vt_only_rows"),
                ("VTRAC Bias", "vtrac_bias_total"),
                ("Top Patterns", "top_patterns"),
            ),
        )
        _emit_table(
            "Corridor Strength",
            section_payload.get("dr_corridor_strength", [])[:6],
            (
                ("Family", "family_id"),
                ("Strength", "corridor_strength_score"),
                ("Scope", "corridor_scope"),
                ("Band", "corridor_band"),
                ("Boxes", "path_summary_count"),
            ),
        )
        _emit_table(
            "Competing Literal Pressure",
            section_payload.get("dr_competing_literal_pressure", [])[:6],
            (
                ("Pattern", "pattern"),
                ("Pressure", "pressure_score"),
                ("Rows", "rows"),
                ("Dup", "dup_bonus_total"),
                ("Ranks", "top_candidate_ranks"),
            ),
        )
        _emit_table(
            "Double Pressure",
            section_payload.get("dr_double_pressure", [])[:6],
            (
                ("Pattern", "pattern"),
                ("Double", "double_score"),
                ("Rows", "rows"),
                ("Dup Depth", "duplicate_depth"),
                ("Mirror", "mirror_pattern"),
            ),
        )
        _emit_table(
            "VTRAC Lane Gateway",
            section_payload.get("dr_vtrac_lane_gateway", [])[:6],
            (
                ("Index", "vtrac_index"),
                ("Gateway", "gateway_score"),
                ("Members", "member_count"),
                ("Rows", "rows_total"),
                ("Top Families", "top_families"),
            ),
        )
        _emit_table(
            "VTRAC Cluster Strength",
            section_payload.get("dr_vtrac_cluster_strength", [])[:6],
            (
                ("Index", "vtrac_index"),
                ("Cluster", "cluster_score"),
                ("Supports", "support_class_count"),
                ("Families", "member_family_count"),
                ("Top Families", "top_families"),
            ),
        )
        _emit_table(
            "Assigned-Box VTRAC Strength",
            section_payload.get("dr_assigned_box_vtrac_strength", [])[:6],
            (
                ("Index", "vtrac_index"),
                ("Assigned Box", "assigned_box_score"),
                ("Rows", "row_count"),
                ("Boxes", "box_count"),
                ("Top Windows", "top_windows"),
            ),
        )
        _emit_table(
            "VTRAC Fusion Strength",
            section_payload.get("dr_vtrac_fusion_strength", [])[:6],
            (
                ("Index", "vtrac_index"),
                ("Fusion", "fusion_score"),
                ("Agree", "agreement_bonus"),
                ("Rescue", "rescue_bonus"),
                ("Top Windows", "top_windows"),
            ),
        )
        _emit_table(
            "Row Repeat / Final Survival",
            section_payload.get("dr_row_repeat_and_final_survival", [])[:6],
            (
                ("Value", "value"),
                ("Score", "score"),
                ("Rows", "rows_repeated"),
                ("Terminal", "terminal_hits"),
                ("Methods", "top_methods"),
            ),
        )
        _emit_table(
            "Fourth Variable",
            section_payload.get("fourth_variable_candidates", [])[:6],
            (
                ("Core", "core_value"),
                ("Extra", "extra_digits"),
                ("VTRAC", "extra_vtrac_digits"),
                ("Support", "support_count"),
                ("Score", "score"),
            ),
        )
        structural = dict(section_payload.get("dr_structural_signals") or {})
        if structural:
            lines.append("### Structural Signals")
            lines.append("")
            lines.append(f"- early_activation_strength={structural.get('early_activation_strength', 0)}")
            lines.append(f"- consecutive_box_progression={structural.get('consecutive_box_progression', 0)}")
            lines.append(f"- neighbor_box_support={structural.get('neighbor_box_support', 0)}")
            lines.append(f"- family_neighborhood_saturation={structural.get('family_neighborhood_saturation', 0)}")
            lines.append(f"- family_asymmetry_inside_corridor={structural.get('family_asymmetry_inside_corridor', 0)}")
            lines.append(f"- core_vs_clutter_transit_score={structural.get('core_vs_clutter_transit_score', 0)}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_dr_arena_files(
    *,
    out_json_path: Path,
    payload: Dict[str, Any],
    write_md: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_json_path.parent.mkdir(parents=True, exist_ok=True)
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path: Optional[Path] = None
    if write_md:
        md_path = out_json_path.with_suffix(".md")
        md_path.write_text(build_dr_arena_markdown(payload), encoding="utf-8")
    return out_json_path, md_path
