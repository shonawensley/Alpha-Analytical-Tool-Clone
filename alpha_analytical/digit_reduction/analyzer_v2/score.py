from __future__ import annotations

import math
from typing import Any, Dict, Iterable, Tuple


_PRIMARY_KINDS: Tuple[str, ...] = (
    "exact",
    "vtrac",
    "drop_exact",
    "drop_vtrac",
    "family_exact",
    "family_vtrac",
)


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _as_int(value: Any, default: int = -1) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _earliest_step(row: Dict[str, Any], kind: str) -> int:
    return _as_int(row.get(f"earliest_{kind}_step"), -1)


def _persistence(row: Dict[str, Any], kind: str) -> int:
    return _as_int(row.get(f"persistence_{kind}"), 0)


def _early_score(step: int, ceiling: int) -> float:
    if step < 0:
        return 0.0
    window = max(1, ceiling + 1)
    return max(0.0, (window - min(step, window)) / window)


def _detection_component(row: Dict[str, Any], kind: str, ceiling: int) -> float:
    return _early_score(_earliest_step(row, kind), ceiling)


def _capped(value: float, cap: float) -> float:
    if cap <= 0:
        return value
    return max(-cap, min(cap, value))


def score_row(row: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
    weights = config.get("weights", {})
    caps = config.get("caps", {})
    gates = config.get("gates", {})
    feature_cfg = config.get("features", {})

    ceiling = int(feature_cfg.get("variants_step_ceiling", 3))
    score = 0.0

    score += weights.get("w_exact", 0.0) * _detection_component(row, "exact", ceiling)
    score += weights.get("w_vtrac", 0.0) * _detection_component(row, "vtrac", ceiling)
    score += weights.get("w_drop_exact", 0.0) * _detection_component(row, "drop_exact", ceiling)
    score += weights.get("w_drop_vtrac", 0.0) * _detection_component(row, "drop_vtrac", ceiling)
    score += weights.get("w_family_exact", 0.0) * _detection_component(row, "family_exact", ceiling)
    score += weights.get("w_family_vtrac", 0.0) * _detection_component(row, "family_vtrac", ceiling)

    density = _capped(_as_float(row.get("box_family_density")), _as_float(caps.get("density_max", 1.0)))
    score += weights.get("w_box_family_density", 0.0) * density

    dup_bonus = _capped(_as_float(row.get("dup_bonus")), _as_float(caps.get("dup_bonus_max", 1.0)))
    score += weights.get("w_dup_bonus", 0.0) * dup_bonus

    score += weights.get("w_residual_purity", 0.0) * _as_float(row.get("residual_purity"))

    cols_hit = _as_int(row.get("cols_hit"), 0)
    if cols_hit >= 3:
        score += weights.get("w_cols_hit_3", 0.0)
    elif cols_hit >= 2:
        score += weights.get("w_cols_hit_2", 0.0)

    variants_hit = _as_int(row.get("variants_hit"), 0)
    if variants_hit >= 3:
        score += weights.get("w_variants_hit_3", 0.0)
    elif variants_hit >= 2:
        score += weights.get("w_variants_hit_2", 0.0)

    score += weights.get("w_method_consensus", 0.0) * _as_float(row.get("method_consensus"))
    score += weights.get("w_cluster_echo", 0.0) * _as_float(row.get("cluster_echo_count"))
    score += weights.get("w_variant_echo", 0.0) * _as_float(row.get("variant_echo_count"))
    score += weights.get("w_set_echo", 0.0) * _as_float(row.get("set_echo_count"))
    score += weights.get("w_box_pair_agree", 0.0) * _as_float(row.get("box_pair_agree"))

    run_len = _as_int(row.get("drop_run_len"), 0)
    if run_len in (2, 3):
        score += weights.get("w_drop_run_len_2_3", 0.0)
    elif run_len >= 4:
        score += weights.get("w_drop_run_len_ge4", 0.0)

    if _as_int(row.get("drop_digit_mode_stability"), 0) >= 2:
        score += weights.get("w_drop_digit_mode_stable", 0.0)

    if _earliest_step(row, "drop_vtrac") >= 0 and cols_hit >= 2 and _earliest_step(row, "drop_vtrac") <= ceiling:
        score += weights.get("w_drop_vtrac_multi_col_early_bonus", 0.0)

    score += weights.get("w_set2_carryover", 0.0) * _as_float(row.get("recency_carryover"))

    tanh_scale = max(1e-6, _as_float(gates.get("tanh_scale", 4.0)))
    normalized = math.tanh(score / tanh_scale)

    lock_threshold = _as_float(gates.get("early_lock"), 0.85)
    unlock_threshold = _as_float(gates.get("early_unlock"), 0.25)

    decision = "hold"
    reason = ""
    if normalized >= lock_threshold:
        decision = "lock"
        reason = "score>=lock"
    elif normalized <= unlock_threshold:
        decision = "unlock"
        reason = "score<=unlock"

    return {
        "score_raw": score,
        "score": normalized,
        "lock_decision": decision,
        "lock_reason": reason,
    }
