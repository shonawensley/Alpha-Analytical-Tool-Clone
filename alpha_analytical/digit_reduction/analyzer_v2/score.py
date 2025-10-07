from __future__ import annotations

from typing import Any, Dict


def _as_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _as_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def score_row(
    row: Dict[str, Any],
    weights: Dict[str, float],
    penalties: Dict[str, float],
    caps: Dict[str, float],
    thresholds: Dict[str, Any],
) -> float:
    s = 0.0

    def w(name: str) -> float:
        return float(weights.get(name, 0.0))

    # Tail / terminal qualities
    s += w("tail.exact_len3") * _as_float(row.get("tail.exact_len3"))
    s += w("tail.unique2") * _as_float(row.get("tail.unique2"))
    s += w("final.len_is1") * _as_float(row.get("final.len_is1"))
    s += w("final.len_is2") * _as_float(row.get("final.len_is2"))
    s += w("final.len_is3") * _as_float(row.get("final.len_is3"))
    s += w("terminal.is_3value") * _as_float(row.get("terminal.is_3value"))
    s += w("terminal.unique_1") * _as_float(row.get("terminal.unique_1"))
    s += w("terminal.unique_2") * _as_float(row.get("terminal.unique_2"))

    # Trajectory
    s += w("traj.early_terminal") * _as_float(row.get("traj.early_terminal"))
    s += w("traj.reduction_slope") * _as_float(row.get("traj.reduction_slope"))
    s += w("time_to_3_fast") * _as_float(row.get("time_to_3_fast"))
    span = _as_float(row.get("post3_span"))
    if span > 0:
        s += w("post3_span")

    # Pre-reduction
    s += w("pre.mirror_pair") * _as_float(row.get("pre.mirror_pair"))
    s += w("pre.core3_hint") * _as_float(row.get("pre.core3_hint"))
    s += w("pre.orig_unique") * _as_float(row.get("pre.orig_unique"))

    # Consensus
    s += w("sec.consensus_any") * _as_float(row.get("sec.consensus_any"))
    s += w("sec.consensus_strong") * _as_float(row.get("sec.consensus_strong"))
    s += w("sec.pairwise_jaccard") * _as_float(row.get("sec.pairwise_jaccard"))

    # Own vs combined
    s += w("mode.agree_core") * _as_float(row.get("mode.agree_core"))
    s += w("mode.time_to3_delta_abs") * _as_float(row.get("mode.time_to3_delta_abs"))
    s += w("mode.len_delta_abs") * _as_float(row.get("mode.len_delta_abs"))

    # Methods / sets / columns
    s += w("methods.core_agreement") * _as_float(row.get("methods.core_agreement"))
    s += w("methods.early_fraction") * _as_float(row.get("methods.early_fraction"))
    s += w("method.agree_count") * _as_float(row.get("method.agree_count"))
    s += w("set.memory_strength") * _as_float(row.get("set.memory_strength"))
    s += w("set.repeat_new_box") * _as_float(row.get("set.repeat_new_box"))
    s += w("set.linger") * _as_float(row.get("set.linger"))
    s += w("xcol.agree_count") * _as_float(row.get("xcol.agree_count"))

    # Stability / permutation
    s += w("stability.order_cue") * _as_float(row.get("stability.order_cue"))
    s += w("stability.horiz_persist") * _as_float(row.get("stability.horiz_persist"))
    s += w("stability.survival_frac3") * _as_float(row.get("stability.survival_frac3"))
    s += w("perm.density") * _as_float(row.get("perm.density"))

    # Optional V-TRAC synergy
    s += w("vtrac.v_hot") * _as_float(row.get("vtrac.v_hot"))

    # Winner overlay signals
    max_step = _as_int(thresholds.get('dr_max_step', 10))
    if max_step <= 0:
        max_step = 10
    s += w('dr.win_exact') * _as_float(row.get('dr.win_exact'))
    s += w('dr.win_vtrac') * _as_float(row.get('dr.win_vtrac'))
    s += w('dr.win_drop_exact') * _as_float(row.get('dr.win_drop_exact'))
    s += w('dr.win_drop_vtrac') * _as_float(row.get('dr.win_drop_vtrac'))
    s += w('dr.win_3val_exact') * _as_float(row.get('dr.win_three_value_exact', row.get('dr.win_3val_exact', 0)))
    s += w('dr.win_3val_vtrac') * _as_float(row.get('dr.win_three_value_vtrac', row.get('dr.win_3val_vtrac', 0)))
    step_exact = _as_int(row.get('dr.win_step_exact', -1))
    if step_exact >= 0:
        normalized = (max_step + 1 - min(step_exact, max_step)) / (max_step + 1)
        s += w('dr.win_early_exact') * normalized
    step_vtrac = _as_int(row.get('dr.win_step_vtrac', -1))
    if step_vtrac >= 0:
        normalized = (max_step + 1 - min(step_vtrac, max_step)) / (max_step + 1)
        s += w('dr.win_early_vtrac') * normalized

    step_drop_exact = _as_int(row.get('dr.win_step_drop_exact', -1))
    if step_drop_exact >= 0:
        normalized = (max_step + 1 - min(step_drop_exact, max_step)) / (max_step + 1)
        s += w('dr.win_early_drop_exact') * normalized
    step_drop_vtrac = _as_int(row.get('dr.win_step_drop_vtrac', -1))
    if step_drop_vtrac >= 0:
        normalized = (max_step + 1 - min(step_drop_vtrac, max_step)) / (max_step + 1)
        s += w('dr.win_early_drop_vtrac') * normalized
    step_family_exact = _as_int(row.get('dr.win_step_family_exact', -1))
    if step_family_exact >= 0:
        normalized = (max_step + 1 - min(step_family_exact, max_step)) / (max_step + 1)
        s += w('dr.win_early_3val_exact') * normalized
    step_family_vtrac = _as_int(row.get('dr.win_step_family_vtrac', -1))
    if step_family_vtrac >= 0:
        normalized = (max_step + 1 - min(step_family_vtrac, max_step)) / (max_step + 1)
        s += w('dr.win_early_3val_vtrac') * normalized

    # Penalties
    s += float(penalties.get("pen.degenerate_empty", 0.0)) * (1.0 if _as_int(row.get("degenerate.empty")) else 0.0)
    s += float(penalties.get("pen.tail_wobble", 0.0)) * _as_float(row.get("tail.wobble"))
    s += float(penalties.get("pen.mode_only_one", 0.0)) * _as_float(row.get("mode.only_one"))

    # Clamp to configured caps
    lo = float(caps.get("score_min", 0.0))
    hi = float(caps.get("score_max", 100.0))
    return float(max(lo, min(hi, s * 10.0)))