from typing import Dict, Any

def score_row(r: Dict[str, Any], W: Dict[str, float], P: Dict[str, float], C: Dict[str, float]) -> float:
    s = 0.0

    # tails / terminal quality
    s += W.get("tail.exact_len3", 0.0) * float(r.get("tail.exact_len3", 0))
    s += W.get("tail.unique2", 0.0)    * float(r.get("tail.unique2", 0))
    s += W.get("tail.final_len_is1",0) * float(r.get("final.len_is1", 0))
    s += W.get("tail.final_len_is2",0) * float(r.get("final.len_is2", 0))
    s += W.get("tail.final_len_is3",0) * float(r.get("final.len_is3", 0))

    # trajectory
    s += W.get("traj.early_terminal",0) * float(r.get("traj.early_terminal", 0))
    s += W.get("traj.reduction_slope",0) * float(r.get("traj.reduction_slope", 0.0))

    # pre-reduction
    s += W.get("pre.mirror_pair",0) * float(r.get("pre.mirror_pair", 0))
    s += W.get("pre.core3_hint",0)  * float(r.get("pre.core3_hint", 0))

    # cross-section
    s += W.get("sec.consensus_any",0)    * float(r.get("sec.consensus_any", 0))
    s += W.get("sec.consensus_strong",0) * float(r.get("sec.consensus_strong", 0))
    s += W.get("sec.pairwise_jaccard",0) * float(r.get("sec.pairwise_jaccard", 0.0))

    # own vs combined
    s += W.get("mode.agree_core",0)            * float(r.get("mode.agree_core", 0))
    s += W.get("mode.time_to3_delta_abs",0)    * float(r.get("mode.time_to3_delta_abs", 0.0))
    s += W.get("mode.len_delta_abs",0)         * float(r.get("mode.len_delta_abs", 0.0))

    # across methods / sets / columns
    s += W.get("methods.core_agreement",0) * float(r.get("methods.core_agreement", 0))
    s += W.get("methods.early_fraction",0) * float(r.get("methods.early_fraction", 0.0))
    s += W.get("set.memory_strength",0)   * float(r.get("set.memory_strength", 0))
    s += W.get("set.repeat_new_box",0)    * float(r.get("set.repeat_new_box", 0))
    s += W.get("xcol.agree_count",0)      * float(r.get("xcol.agree_count", 0))

    # stability / perms
    s += W.get("stability.order_cue",0)    * float(r.get("stability.order_cue", 0.0))
    s += W.get("stability.horiz_persist",0)* float(r.get("stability.horiz_persist", 0.0))
    s += W.get("perm.density",0)           * float(r.get("perm.density", 0.0))
    s += W.get("stability.survival_frac3",0)* float(r.get("stability.survival_frac3", 0.0))

    # penalties
    s += P.get("degenerate.empty",0) * float(1 if r.get("final.value","")=="" else 0)
    s += P.get("tail.wobble",0)      * float(r.get("pen.tail_wobble", 0))
    s += P.get("mode.only_one",0)    * float(r.get("mode.only_one", 0))

    # clamp & scale to 0..100
    lo = C.get("score_min", 0.0); hi = C.get("score_max", 100.0)
    s = max(lo, min(hi, s * 10.0))
    return float(s)
