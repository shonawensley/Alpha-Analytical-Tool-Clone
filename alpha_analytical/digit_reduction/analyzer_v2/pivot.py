from __future__ import annotations
from typing import Dict, Any, Iterable, Tuple, List, DefaultDict
from collections import defaultdict, Counter
from .types import Item

def _key_no_section(k) -> Tuple:
    return (k.state, k.area, k.set, k.draw, k.col, k.method, k.mode)

def _key_no_mode(k) -> Tuple:
    return (k.state, k.area, k.section, k.set, k.draw, k.col, k.method)

def _canon3(s: str) -> str:
    ds = [c for c in s if c.isdigit()]
    return "".join(sorted(ds)) if ds else ""

def _first3(it: Item) -> int:
    for st in it.steps:
        if st.is_3value or st.length <= 3 or st.unique_digits <= 2:
            return st.step
    return -1

def _first3_core(it: Item) -> str:
    i = _first3(it)
    return it.steps[i].value if i >= 0 and it.steps else ""

def cross_section_pivot(items: Iterable[Item]) -> Dict[Tuple, Dict[str, Any]]:
    """
    Compare Midday / Evening / Combined for same (area,set,draw,col,method,mode).
    Emits sec.consensus_* and pairwise Jaccard on 3-digit sets.
    """
    groups: DefaultDict[Tuple, List[Item]] = defaultdict(list)
    for it in items:
        groups[_key_no_section(it.key)].append(it)

    out: Dict[Tuple, Dict[str, Any]] = {}
    for k, group in groups.items():
        by_sec = {it.key.section: it for it in group}
        sets = {sec: set(_canon3(_first3_core(it))) for sec, it in by_sec.items() if _first3_core(it)}
        vals = list(sets.values())
        consensus_any = int(len(vals) >= 2 and all(v == vals[0] for v in vals))
        consensus_strong = int(consensus_any and len(vals) == 3)

        # average pairwise Jaccard across available sections
        jacc = 0.0; n = 0
        secs = list(sets.keys())
        for i in range(len(secs)):
            for j in range(i+1, len(secs)):
                a, b = sets[secs[i]], sets[secs[j]]
                if a or b:
                    jacc += len(a & b)/max(1, len(a | b)); n += 1
        out[k] = {
            "sec.consensus_any": consensus_any,
            "sec.consensus_strong": consensus_strong,
            "sec.pairwise_jaccard": (jacc/n) if n else 0.0,
            "sec.time_to3_min": min((_first3(it) for it in group if _first3(it) >= 0), default=-1),
            "sec.time_to3_max": max((_first3(it) for it in group if _first3(it) >= 0), default=-1),
        }
    return out

def own_vs_combined(items: Iterable[Item]) -> Dict[Tuple, Dict[str, Any]]:
    """
    Within same section: compare own vs combined for same (area,set,draw,col,method).
    """
    groups: DefaultDict[Tuple, List[Item]] = defaultdict(list)
    for it in items:
        groups[(it.key.state, it.key.area, it.key.section, it.key.set, it.key.draw, it.key.col, it.key.method)].append(it)
    out: Dict[Tuple, Dict[str, Any]] = {}
    for k, group in groups.items():
        by_mode = {it.key.mode: it for it in group}
        v: Dict[str, Any] = {}
        a = by_mode.get("own"); b = by_mode.get("combined")
        if a and b:
            v["mode.only_one"] = 0
            v["mode.agree_core"] = int(_canon3(_first3_core(a)) == _canon3(_first3_core(b)) and _first3_core(a) != "")
            t_a, t_b = _first3(a), _first3(b)
            v["mode.time_to3_delta_abs"] = abs((t_a if t_a>=0 else 99) - (t_b if t_b>=0 else 99))
            la = a.steps[-1].length if a.steps else 0
            lb = b.steps[-1].length if b.steps else 0
            v["mode.len_delta_abs"] = abs(la - lb)
        else:
            v["mode.only_one"] = 1
        out[k] = v
    return out

def set_memory(items: Iterable[Item]) -> Dict[Tuple, Dict[str, Any]]:
    """
    Same (area,section,col,method,mode) across Set3→2→1.
    Memory = same canon core appears in ≥2 sets; repeat_new_box proxy = same canon with column change.
    """
    groups: DefaultDict[Tuple, List[Item]] = defaultdict(list)
    for it in items:
        groups[(it.key.state, it.key.area, it.key.section, it.key.col, it.key.method, it.key.mode)].append(it)

    out: Dict[Tuple, Dict[str, Any]] = {}
    order = {"Set3": 3, "Set2": 2, "Set1": 1}
    for k, group in groups.items():
        group.sort(key=lambda it: order.get(it.key.set, 0), reverse=True)  # 3→2→1
        cores = [(it.key.set, _canon3(_first3_core(it))) for it in group if _first3_core(it)]
        canon_nonempty = [c for _, c in cores if c]
        mem = int(len(canon_nonempty) >= 2 and len(set(canon_nonempty)) == 1)
        out[k] = {"set.memory_strength": mem, "set.repeat_new_box": mem}
    return out

def cross_col_agree(items: Iterable[Item]) -> Dict[Tuple, Dict[str, Any]]:
    """
    Cross-column stability within LS area:
      - LS1: columns 7/6/5
      - LS2: columns 3/1
    Emits xcol.agree_count per (area,section,set,draw,method,mode).
    """
    groups: DefaultDict[Tuple, List[Item]] = defaultdict(list)
    for it in items:
        groups[(it.key.state, it.key.area, it.key.section, it.key.set, it.key.draw, it.key.method, it.key.mode)].append(it)

    out: Dict[Tuple, Dict[str, Any]] = {}
    for k, group in groups.items():
        # map col -> canon core
        by_col = {it.key.col: _canon3(_first3_core(it)) for it in group if _first3_core(it)}
        cols = [7,6,5] if (group[0].key.area == "LS1") else [3,1]
        sigs = [by_col.get(c, "") for c in cols if c in by_col]
        agree_count = 0
        if len(sigs) >= 2:
            base = sigs[0]
            agree_count = sum(1 for s in sigs[1:] if s == base and s != "")
        out[k] = {"xcol.agree_count": agree_count}
    return out

def methods_consensus(items: Iterable[Item], early_k: int) -> Dict[Tuple, Dict[str, Any]]:
    """
    Across methods for the same location (area,section,set,draw,col,mode):
      - methods.core_agreement: count of methods sharing the same canon3 core (>= threshold later).
      - methods.early_fraction: fraction of methods with first3 <= early_k.
    """
    groups: DefaultDict[Tuple, List[Item]] = defaultdict(list)
    for it in items:
        groups[(it.key.state, it.key.area, it.key.section, it.key.set, it.key.draw, it.key.col, it.key.mode)].append(it)

    out: Dict[Tuple, Dict[str, Any]] = {}
    for k, group in groups.items():
        cores = [_canon3(_first3_core(it)) for it in group if _first3_core(it)]
        core_cnt = Counter([c for c in cores if c])
        best_agree = max(core_cnt.values()) if core_cnt else 0
        early_hits = sum(1 for it in group if 0 <= _first3(it) <= early_k)
        total = len(group) if group else 1
        out[k] = {
            "methods.core_agreement": best_agree,
            "methods.early_fraction": early_hits / total
        }
    return out
