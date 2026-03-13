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

        sparse_reasons: List[str] = []
        if not strong_trace:
            sparse_reasons.append("no_strong_trace_families")
        if not training_ledgers["precluster_ledger"]:
            sparse_reasons.append("no_preclusters")
        if not training_ledgers["reduction_reveal_ledger"]:
            sparse_reasons.append("no_reveals")
        if training_ledgers["cold_location_count"] >= max(1, len(log_rows)):
            sparse_reasons.append("all_locations_cold")

        payload["sections"][section] = {
            "summary": {
                "per_item_rows": len(variant_rows),
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
            "dr_row_repeat_and_final_survival": training_ledgers["row_repeat_and_final_survival"],
            "dr_empty_lens": {
                "is_sparse": bool(sparse_reasons),
                "reasons": sparse_reasons,
                "cold_location_count": int(training_ledgers["cold_location_count"]),
            },
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
        f"- inputs_hash: `{payload.get('inputs_hash', '')[:16]}` | profile: `{payload.get('profile', '')}` | experiment: `{payload.get('experiment_tag') or 'none'}`"
    )
    lines.append("")

    for section, section_payload in sorted(payload.get("sections", {}).items(), key=lambda kv: _section_sort_key(kv[0])):
        summary = dict(section_payload.get("summary") or {})
        lines.append(f"## {section}")
        lines.append("")
        lines.append(
            f"- rows={summary.get('per_item_rows', 0)} | top_candidates={summary.get('top_candidate_rows', 0)} | "
            f"locations={summary.get('training_locations', 0)} | families={summary.get('unique_families', 0)} | "
            f"patterns={summary.get('unique_patterns', 0)} | max_score_v2={summary.get('max_score_v2', 0.0):.3f}"
        )
        empty = dict(section_payload.get("dr_empty_lens") or {})
        lines.append(
            f"- empty_lens={bool(empty.get('is_sparse'))} | reasons={', '.join(empty.get('reasons') or ['none'])}"
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
