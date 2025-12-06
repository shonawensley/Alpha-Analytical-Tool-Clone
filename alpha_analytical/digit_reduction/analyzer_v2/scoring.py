from __future__ import annotations

from math import exp
from typing import Any, Dict, List


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        if isinstance(value, bool):
            return 1.0 if value else 0.0
        return float(value)
    except (TypeError, ValueError):
        return default


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _is_truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return False


def _sigmoid(z: float) -> float:
    if z >= 0:
        ez = exp(-z)
        return 1.0 / (1.0 + ez)
    ez = exp(z)
    return ez / (1.0 + ez)


def apply_linear_scoring(rows: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    """Add final_linear/final_prob/lock_decision when enabled."""
    cfg = config.get("scoring_linear", {})
    if not cfg.get("enabled"):
        for row in rows:
            row.setdefault("final_linear", 0.0)
            row.setdefault("final_prob", 0.0)
            row.setdefault("lock_decision", row.get("lock_decision", ""))
        return

    weights = cfg.get("weights", {})
    thresholds = cfg.get("thresholds", {})
    bias = _as_float(cfg.get("final_logit_bias"), 0.0)
    scale = _as_float(cfg.get("final_logit_scale"), 1.0)
    lock_thr = _as_float(thresholds.get("lock"), 0.92)
    hold_thr = _as_float(thresholds.get("hold"), 0.85)

    for row in rows:
        linear = 0.0
        linear += weights.get("w_recency_carryover", 0.0) * (1.0 if _is_truthy(row.get("recency_carryover")) else 0.0)
        linear += weights.get("w_set_echo", 0.0) * _as_float(row.get("set_echo_count"))
        linear += weights.get("w_variant_echo", 0.0) * _as_float(row.get("variant_echo_count"))
        if _as_int(row.get("cols_hit"), 0) == 1:
            linear += weights.get("w_single_column_rescue", 0.0)
        linear += weights.get("w_vtrac_hot", 0.0) * _as_float(row.get("vtrac.v_hot"))
        linear += weights.get("w_vtrac_local_set", 0.0) * (_as_float(row.get("vtrac.set")) / 15.0)
        if (row.get("mode") or "").lower() == "own":
            linear += weights.get("w_mode_own_bonus", 0.0)
        if (row.get("section") or "").lower() == "combined":
            linear += weights.get("w_section_combined_penalty", 0.0)
        linear += weights.get("w_box_family_density", 0.0) * _as_float(row.get("box_family_density"))
        linear += weights.get("w_dup_bonus", 0.0) * _as_float(row.get("dup_bonus"))

        row["final_linear"] = round(linear, 6)
        prob = _sigmoid(bias + scale * linear)
        row["final_prob"] = prob

        decision = ""
        if prob >= lock_thr:
            decision = "lock"
        elif prob >= hold_thr:
            decision = "hold"
        row["lock_decision"] = decision
        if decision == "lock":
            row["lock_reason"] = "final_prob>=lock"
        elif decision == "hold":
            row["lock_reason"] = "final_prob>=hold"


def apply_post_score(rows: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    """Add score_v2 based on recency/persistence/single-column heuristics."""
    cfg = config.get("scoring_v2", {})
    if not cfg.get("enabled"):
        for row in rows:
            row.setdefault("score_v2", row.get("score"))
        return

    weights = cfg.get("weights", {})
    guards = cfg.get("guards", {})
    drop_only_multiplier = _as_float(guards.get("drop_only_multiplier", 1.0), 1.0)
    for row in rows:
        base = _as_float(row.get("score_raw"), row.get("score", 0.0))
        score2 = base

        if _is_truthy(row.get("recency_carryover")):
            score2 += weights.get("recency_bonus", 0.0)

        fam_persist = _as_float(row.get("persistence_family_exact")) + _as_float(row.get("persistence_family_vtrac"))
        score2 += weights.get("family_persistence", 0.0) * fam_persist

        density = _as_float(row.get("box_family_density"))
        if _as_int(row.get("cols_hit"), 0) == 1 and density >= weights.get("density_min", 0.0):
            score2 += weights.get("singlecol_rescue", 0.0)

        late = min(7, max(0, _as_int(row.get("earliest_exact_step"), 7)))
        score2 -= weights.get("late_penalty", 0.0) * (late / 7.0)

        score2 += weights.get("vhot", 0.0) * _as_float(row.get("vtrac.v_hot"))
        min_drop_len = _as_int(guards.get("min_drop_run_len", 5), 5)
        drop_len = _as_int(row.get("drop_run_len"), 0)
        if _is_truthy(row.get("is_extended_cluster")) and drop_len >= min_drop_len:
            score2 += weights.get("extended_cluster_bonus", 0.0)
        if _is_truthy(row.get("final_vtrac_match")) or _is_truthy(row.get("final_family_vtrac_match")):
            score2 += weights.get("vtrac_family_rescue", 0.0)

        if _is_truthy(row.get("final_exact_match")):
            score2 += guards.get("boost_exact_match", 0.0)
        if _is_truthy(row.get("final_vtrac_match")):
            score2 += guards.get("boost_vtrac_match", 0.0)

        # Optional: down-weight pure drop-vtrac boxes (no exact/VT/family VT evidence).
        # This is config-gated via scoring_v2.guards.drop_only_multiplier.
        if drop_only_multiplier < 1.0:
            if _is_truthy(row.get("final_drop_vtrac_match")) and not (
                _is_truthy(row.get("final_exact_match"))
                or _is_truthy(row.get("final_vtrac_match"))
                or _is_truthy(row.get("final_family_vtrac_match"))
                or _is_truthy(row.get("final_family_exact_match"))
            ):
                score2 *= drop_only_multiplier

        row["score_v2"] = round(score2, 6)


def attach_lockscore(rows: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    cfg = config.get("lockscore", {})
    if not cfg.get("enabled"):
        for row in rows:
            row.setdefault("lockscore_v2", row.get("score"))
            row.setdefault("lockscore_prob", row.get("score"))
        return

    weights = cfg.get("weights", {})
    guards = cfg.get("guards", {})
    cols_threshold = _as_int(guards.get("t_cols_hit_rescue", 1), 1)
    early_threshold = _as_float(guards.get("t_early", 3), 3.0)
    penalty_combined = _as_float(guards.get("penalty_combined_bias", 0.0))
    min_lock = _as_float(cfg.get("min_lockscore_to_lock"), 0.85)

    for row in rows:
        score_raw = _as_float(row.get("score"))
        earliest_exact = _as_float(row.get("earliest_exact_step"), 99.0)
        earliest_vtrac = _as_float(row.get("earliest_vtrac_step"), 99.0)
        persistence = max(
            _as_float(row.get("persistence_exact")),
            _as_float(row.get("persistence_family_exact")),
            _as_float(row.get("persistence_vtrac")),
        )
        density = _as_float(row.get("box_family_density"))
        set_echo = _as_float(row.get("set_echo_count"))
        variant_echo = _as_float(row.get("variant_echo_count"))
        recency = 1.0 if _is_truthy(row.get("recency_carryover")) else 0.0
        v_hot = _as_float(row.get("vtrac.v_hot"))
        cols_hit = _as_int(row.get("cols_hit"))
        section = (row.get("section") or "").strip().lower()
        final_val = str(row.get("final_value") or "")
        is_double = 1.0 if len(set(final_val)) == 2 and final_val else 0.0

        early_exact = 1.0 / (1.0 + earliest_exact) if earliest_exact < 99 else 0.0
        early_vtrac = 1.0 / (1.0 + earliest_vtrac) if earliest_vtrac < 99 else 0.0

        rescue = 0.0
        if cols_hit <= cols_threshold and min(earliest_exact, earliest_vtrac) <= early_threshold:
            rescue = weights.get("w_single_col_rescue", 0.0)

        penalty = penalty_combined if section == "combined" else 0.0

        lockscore = (
            weights.get("w_score_raw", 0.0) * score_raw
            + weights.get("w_earliest_exact", 0.0) * early_exact
            + weights.get("w_earliest_vtrac", 0.0) * early_vtrac
            + weights.get("w_persistence", 0.0) * persistence
            + weights.get("w_box_density", 0.0) * density
            + weights.get("w_set_echo", 0.0) * set_echo
            + weights.get("w_variant_echo", 0.0) * variant_echo
            + weights.get("w_recency", 0.0) * recency
            + weights.get("w_vtrac_hot", 0.0) * v_hot
            + (
                weights.get("w_extended_cluster", 0.0)
                if (_is_truthy(row.get("is_extended_cluster")) and _as_int(row.get("drop_run_len"), 0) >= _as_int(guards.get("min_drop_run_len", 5), 5))
                else 0.0
            )
            + rescue
            + weights.get("w_double_guard", 0.0) * is_double
            - penalty
        )

        row["lockscore_v2"] = round(lockscore, 6)
        row["lockscore_prob"] = max(0.0, min(1.0, lockscore))
        row["lockscore_decision"] = "lock" if row["lockscore_prob"] >= min_lock else ""


def top_score_key(cfg: Dict[str, Any], rows: List[Dict[str, Any]]) -> str:
    lock_cfg = cfg.get("lockscore", {})
    if lock_cfg.get("enabled") and lock_cfg.get("use_for_top"):
        if any("lockscore_prob" in row for row in rows):
            return "lockscore_prob"
    scoring_cfg = cfg.get("scoring_v2", {})
    if scoring_cfg.get("enabled") and scoring_cfg.get("use_for_top"):
        if any("score_v2" in row for row in rows):
            return "score_v2"
    linear_cfg = cfg.get("scoring_linear", {})
    if linear_cfg.get("enabled") and linear_cfg.get("use_for_top"):
        if any("final_prob" in row for row in rows):
            return "final_prob"
    return "score"
