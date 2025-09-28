from __future__ import annotations
from typing import Dict, Any, List
from collections import Counter
from .types import Item

def _digits(s: str) -> List[str]:
    return [c for c in s if c.isdigit()]

def _canon3(s: str) -> str:
    ds = _digits(s)
    return "".join(sorted(ds)) if ds else ""

def _uniq_count(s: str) -> int:
    return len(set(_digits(s)))

def _has_mirror_pair_raw(s: str) -> bool:
    # canonical 0↔5, 1↔6, 2↔7, 3↔8, 4↔9
    M = {"0":"5","1":"6","2":"7","3":"8","4":"9","5":"0","6":"1","7":"2","8":"3","9":"4"}
    bag = set(_digits(s))
    return any(M[d] in bag for d in bag)

def _first_terminal_index(item: Item) -> int:
    for st in item.steps:
        if st.is_3value or st.length <= 3 or st.unique_digits <= 2:
            return st.step
    return -1

def _survival_fraction_at3(item: Item) -> float:
    idx = _first_terminal_index(item)
    if idx < 0 or not item.steps: return 0.0
    core = set(_digits(item.steps[idx].value))
    orig = set(_digits(item.orig.value))
    return len(core & orig)/max(1, len(orig)) if core else 0.0

def _order_cue_strength(item: Item) -> float:
    # crude signal: fewer distinct values after terminal ⇒ stronger ordering
    idx = _first_terminal_index(item)
    if idx < 0: return 0.0
    tail_vals = [st.value for st in item.steps[idx:]]
    return 1.0 / max(1, len(set(tail_vals)))

def _tail_wobble(item: Item) -> int:
    idx = _first_terminal_index(item)
    if idx < 0: return 0
    base = item.steps[idx].value
    dup = 0
    for st in item.steps[idx+1:]:
        if st.value == base: dup += 1
        else: break
    return dup

def _perm_density(s: str) -> float:
    # 3-digit permutations (with duplicate handling)
    from math import factorial
    ds = _digits(s)[:3]
    if not ds: return 0.0
    if len(ds) < 3: return 0.5
    c = Counter(ds)
    denom = 1
    for v in c.values(): denom *= factorial(v)
    return (factorial(3)/denom)/6.0  # normalize to [0,1]

def compute_item_features(item: Item, early_k: int = 3) -> Dict[str, Any]:
    feats: Dict[str, Any] = {}
    # trajectory & tails
    t3 = _first_terminal_index(item)
    feats["traj.first3"] = t3 if t3 >= 0 else 99
    feats["traj.early_terminal"] = 1 if 0 <= t3 <= early_k else 0
    diffs = [item.steps[i-1].length - item.steps[i].length for i in range(1, len(item.steps))]
    feats["traj.reduction_slope"] = sum(diffs)/len(diffs) if diffs else 0.0

    last = item.steps[-1] if item.steps else None
    feats["tail.final_len"] = last.length if last else 0
    feats["tail.final_unique"] = last.unique_digits if last else 0
    feats["tail.exact_len3"] = 1 if any(st.length == 3 for st in item.steps) else 0
    feats["tail.unique2"] = 1 if any(st.unique_digits == 2 for st in item.steps) else 0
    feats["stability.survival_frac3"] = _survival_fraction_at3(item)
    feats["stability.order_cue"] = _order_cue_strength(item)
    feats["pen.tail_wobble"] = _tail_wobble(item)

    # pre-reduction
    orig = item.orig.value
    feats["pre.mirror_pair"] = 1 if _has_mirror_pair_raw(orig) else 0
    feats["pre.core3_hint"] = 1 if _uniq_count(orig) <= 3 and len(_digits(orig)) >= 3 else 0

    # permutation proxy
    feats["perm.density"] = _perm_density(last.value if last else "")

    # canonical finals
    feats["final.value"] = last.value if last else ""
    feats["final.canon3"] = _canon3(feats["final.value"])
    feats["final.len_is1"] = 1 if feats["tail.final_len"] == 1 else 0
    feats["final.len_is2"] = 1 if feats["tail.final_len"] == 2 else 0
    feats["final.len_is3"] = 1 if feats["tail.final_len"] == 3 else 0

    return feats
