# alpha_analytical/digit_reduction/analyzer_v2/score.py
from typing import Dict, Any
import math

def score_row(feats: Dict[str, Any], weights: Dict[str, float], penalties: Dict[str,float], caps: Dict[str,float]) -> float:
    s = 0.0
    # positives
    for name, w in weights.items():
        s += w * float(feats.get(name, 0))
    # penalties
    for name, p in penalties.items():
        s += p * float(feats.get(name, 0))
    # --- new: V‑TRAC synergy (v_hot is 0..1, weight key = 'vtrac.hot_index') ---
    s += float(weights.get("vtrac.hot_index", 0.0)) * float(feats.get("vtrac.v_hot", 0.0))

    lo = caps.get("score_min", -1e9); hi = caps.get("score_max", 1e9)
    return max(lo, min(hi, s*10.0))  # scale to ~0..100
