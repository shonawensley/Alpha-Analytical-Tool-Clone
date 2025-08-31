# modules/sums_analysis.py

from typing import Dict, List, Any
import math

from .sums_reference import (
    SUM_PROB,
    ROOTSUM_PROB,
    sum_of_draw,
    root_sum_of_draw,
)

# ---------- Tunable thresholds ----------
Z_HOT = 1.0         # blue if z >= +1.0
Z_COLD = -1.0       # red  if z <= -1.0
GAP_PURPLE = 25     # purple if draws_since >= 25
# ---------------------------------------

def _draws_since_indices(items: List[int], universe: List[int], default_value: int) -> Dict[int, int]:
    """
    Given a per-draw sequence of category labels (e.g., sum values),
    compute draws-since (0 = newest draw) for every category in `universe`.
    We scan newest->oldest (list is already newest first in our app).
    """
    last_seen: Dict[int, int] = {}
    for i, label in enumerate(items):
        if label not in last_seen:
            last_seen[label] = i
        if len(last_seen) == len(universe):
            break
    return {label: last_seen.get(label, default_value) for label in universe}

def _zscore(observed: int, window: int, p: float) -> float:
    """
    Normal approximation z-score: (obs - E) / sqrt(N p (1-p))
    Safe when 0 < p < 1; otherwise return 0.
    """
    if p <= 0.0 or p >= 1.0 or window <= 0:
        return 0.0
    expected = window * p
    var = window * p * (1 - p)
    if var <= 0.0:
        return 0.0
    return (observed - expected) / math.sqrt(var)

def _class_flags(z: float, gap: int) -> Dict[str, bool]:
    """
    Map z and gap to color semantics used across the Auxiliary UI.
    - blue   -> hot (z >= Z_HOT)
    - red    -> cold (z <= Z_COLD)
    - purple -> pending gap (gap >= GAP_PURPLE)
    Multiple flags may be true simultaneously.
    """
    return {
        "blue":   z >= Z_HOT,
        "red":    z <= Z_COLD,
        "purple": gap >= GAP_PURPLE,
    }

def _analyze_categories(
    labels: List[int],
    probs: Dict[int, float],
    window: int
) -> Dict[int, Dict[str, Any]]:
    """
    Generic analyzer for per-draw labels (sum or root-sum).
    Returns a dict keyed by category with:
      count, expected, hit_rate, exp_rate, z, draws_since, flags{blue,red,purple}
    """
    # Count observed
    counts: Dict[int, int] = {k: 0 for k in probs.keys()}
    for val in labels:
        if val in counts:
            counts[val] += 1

    # Draws-since per category (0..window)
    universe = list(probs.keys())
    draws_since_map = _draws_since_indices(labels, universe, default_value=window)

    # Build results
    out: Dict[int, Dict[str, Any]] = {}
    for k in universe:
        p = probs[k]
        c = counts.get(k, 0)
        z = _zscore(c, window, p)
        gap = draws_since_map[k]
        out[k] = {
            "count": c,
            "expected": window * p,
            "hit_rate": c / window if window else 0.0,
            "exp_rate": p,
            "z": z,
            "draws_since": gap,
            "flags": _class_flags(z, gap),
        }
    return out

def calculate_sums_stats(draws: List[str], window: int = 100) -> Dict[str, Any]:
    """
    Main entry: analyze sums and root-sums over the newest `window` draws.
    Input draws are newest-first, consistent with the rest of the app.
    Returns:
      {
        'window': int,
        'by_sum': { sum:int -> metrics },
        'by_root_sum': { root:int -> metrics }
      }
    """
    if not draws:
        return {"window": 0, "by_sum": {}, "by_root_sum": {}}

    w = min(window, len(draws))
    window_draws = draws[:w]

    sums: List[int] = [sum_of_draw(d) for d in window_draws if d and len(d) == 3]
    roots: List[int] = [root_sum_of_draw(d) for d in window_draws if d and len(d) == 3]

    by_sum = _analyze_categories(sums, SUM_PROB, w)
    by_root = _analyze_categories(roots, ROOTSUM_PROB, w)

    return {"window": w, "by_sum": by_sum, "by_root_sum": by_root}
