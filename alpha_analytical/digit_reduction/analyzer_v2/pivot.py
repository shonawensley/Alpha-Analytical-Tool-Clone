from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, DefaultDict, Dict, Iterable, List, Tuple

from .types import Item

SectionKey = Tuple[str, str, str, str, str, int, str, str]
ModeLessKey = Tuple[str, str, str, str, str, int, str]
LocationKey = Tuple[str, str, str, str, str, str, str]
MethodKey = Tuple[str, str, str, str, str, int, str]


def _digits(value: str) -> List[str]:
    return [ch for ch in value if ch.isdigit()]


def _canon3(value: str) -> str:
    digits = _digits(value)
    return "".join(sorted(digits)) if digits else ""


def _first_terminal_entry(item: Item) -> Tuple[int, str, int]:
    for index, step in enumerate(item.steps):
        if step.is_3value or step.length <= 3 or step.unique_digits <= 2:
            return index, step.value, step.step
    return -1, "", -1


def _section_key(item: Item) -> SectionKey:
    return (
        item.key.state,
        item.key.area,
        item.key.section,
        item.key.set,
        item.key.draw,
        item.key.col,
        item.key.method,
        item.key.mode,
    )


def _group_key_no_section(item: Item) -> Tuple[str, str, str, str, int, str, str]:
    return (
        item.key.state,
        item.key.area,
        item.key.set,
        item.key.draw,
        item.key.col,
        item.key.method,
        item.key.mode,
    )


def _group_key_no_mode(item: Item) -> ModeLessKey:
    return (
        item.key.state,
        item.key.area,
        item.key.section,
        item.key.set,
        item.key.draw,
        item.key.col,
        item.key.method,
    )


def cross_section_pivot(items: Iterable[Item]) -> Dict[Tuple[str, str, str, str, int, str, str], Dict[str, Any]]:
    groups: DefaultDict[Tuple[str, str, str, str, int, str, str], List[Item]] = defaultdict(list)
    for item in items:
        groups[_group_key_no_section(item)].append(item)

    results: Dict[Tuple[str, str, str, str, int, str, str], Dict[str, Any]] = {}
    for key, group in groups.items():
        by_section = {member.key.section: member for member in group}
        canon_sets = {
            section: set(_canon3(_first_terminal_entry(member)[1]))
            for section, member in by_section.items()
            if _first_terminal_entry(member)[1]
        }
        signatures = list(canon_sets.values())
        consensus_any = int(len(signatures) >= 2 and all(sig == signatures[0] for sig in signatures))
        consensus_strong = int(consensus_any and len(signatures) == 3)

        jaccard = 0.0
        comparisons = 0
        sections = list(canon_sets.keys())
        for i in range(len(sections)):
            for j in range(i + 1, len(sections)):
                a = canon_sets[sections[i]]
                b = canon_sets[sections[j]]
                if a or b:
                    jaccard += len(a & b) / max(1, len(a | b))
                    comparisons += 1
        first_hits = [entry for entry in (_first_terminal_entry(member)[2] for member in group) if entry >= 0]
        results[key] = {
            "sec.consensus_any": consensus_any,
            "sec.consensus_strong": consensus_strong,
            "sec.pairwise_jaccard": (jaccard / comparisons) if comparisons else 0.0,
            "sec.time_to3_min": min(first_hits) if first_hits else -1,
            "sec.time_to3_max": max(first_hits) if first_hits else -1,
        }
    return results


def own_vs_combined(items: Iterable[Item]) -> Tuple[Dict[SectionKey, Dict[str, Any]], List[Dict[str, Any]]]:
    groups: DefaultDict[ModeLessKey, List[Item]] = defaultdict(list)
    for item in items:
        groups[_group_key_no_mode(item)].append(item)

    features: Dict[SectionKey, Dict[str, Any]] = {}
    delta_rows: List[Dict[str, Any]] = []

    for key, group in groups.items():
        by_mode = {member.key.mode: member for member in group}
        own_entry = by_mode.get("own")
        combined_entry = by_mode.get("combined")

        own_idx, own_core, own_first_step = _first_terminal_entry(own_entry) if own_entry else (-1, "", -1)
        combined_idx, combined_core, combined_first_step = _first_terminal_entry(combined_entry) if combined_entry else (-1, "", -1)

        len_delta = 0
        if own_entry and combined_entry:
            own_len = own_entry.steps[-1].length if own_entry.steps else 0
            combined_len = combined_entry.steps[-1].length if combined_entry.steps else 0
            len_delta = abs(own_len - combined_len)
        time_delta = 0
        if own_entry and combined_entry:
            a = own_first_step if own_first_step >= 0 else 99
            b = combined_first_step if combined_first_step >= 0 else 99
            time_delta = abs(a - b)
        agree_core = int(own_core and combined_core and _canon3(own_core) == _canon3(combined_core))
        mode_only_one = int(not (own_entry and combined_entry))

        for entry in group:
            features[_section_key(entry)] = {
                "mode.only_one": mode_only_one,
                "mode.agree_core": agree_core,
                "mode.time_to3_delta_abs": time_delta,
                "mode.len_delta_abs": len_delta,
            }

        delta_rows.append(
            {
                "state": key[0],
                "area": key[1],
                "section": key[2],
                "set": key[3],
                "draw": key[4],
                "col": key[5],
                "method": key[6],
                "own.first3_step": own_first_step,
                "combined.first3_step": combined_first_step,
                "own.core": _canon3(own_core) if own_core else "",
                "combined.core": _canon3(combined_core) if combined_core else "",
                "mode.time_to3_delta_abs": time_delta,
                "mode.len_delta_abs": len_delta,
                "mode.agree_core": agree_core,
                "mode.only_one": mode_only_one,
            }
        )

    return features, delta_rows


def set_memory(items: Iterable[Item]) -> Dict[SectionKey, Dict[str, Any]]:
    groups: DefaultDict[Tuple[str, str, str, str, str, str], List[Item]] = defaultdict(list)
    for item in items:
        groups[(item.key.state, item.key.area, item.key.section, item.key.col, item.key.method, item.key.mode)].append(item)

    results: Dict[SectionKey, Dict[str, Any]] = {}
    set_order = {"Set3": 3, "Set2": 2, "Set1": 1}
    for group_key, group in groups.items():
        group.sort(key=lambda member: set_order.get(member.key.set, 0), reverse=True)
        cores = [_canon3(_first_terminal_entry(member)[1]) for member in group if _first_terminal_entry(member)[1]]
        mem_strength = int(len(cores) >= 2 and len(set(cores)) == 1)
        linger = int(len(cores) >= 1 and len(set(cores)) == 1)
        payload = {
            "set.memory_strength": mem_strength,
            "set.repeat_new_box": mem_strength,
            "set.linger": linger,
        }
        for member in group:
            results[_section_key(member)] = payload.copy()
    return results


def cross_col_agree(items: Iterable[Item]) -> Dict[SectionKey, Dict[str, Any]]:
    groups: DefaultDict[LocationKey, Dict[int, str]] = defaultdict(dict)
    for item in items:
        location = (
            item.key.state,
            item.key.area,
            item.key.section,
            item.key.set,
            item.key.draw,
            item.key.method,
            item.key.mode,
        )
        _, core, _ = _first_terminal_entry(item)
        groups[location][item.key.col] = _canon3(core) if core else ""

    results: Dict[SectionKey, Dict[str, Any]] = {}
    for location, col_map in groups.items():
        area = location[1]
        focus_cols = [7, 6, 5] if area == "LS1" else [3, 1]
        signatures = [col_map.get(col, "") for col in focus_cols if col in col_map]
        agree_count = 0
        if signatures:
            anchor = signatures[0]
            agree_count = sum(1 for sig in signatures[1:] if sig and sig == anchor)
        for col, _canon in col_map.items():
            results[(
                location[0],
                location[1],
                location[2],
                location[3],
                location[4],
                col,
                location[5],
                location[6],
            )] = {"xcol.agree_count": agree_count}
    return results


def methods_consensus(items: Iterable[Item], early_k: int) -> Dict[MethodKey, Dict[str, Any]]:
    groups: DefaultDict[MethodKey, List[Item]] = defaultdict(list)
    for item in items:
        groups[(
            item.key.state,
            item.key.area,
            item.key.section,
            item.key.set,
            item.key.draw,
            item.key.col,
            item.key.mode,
        )].append(item)

    results: Dict[MethodKey, Dict[str, Any]] = {}
    for key, group in groups.items():
        cores = [_canon3(_first_terminal_entry(member)[1]) for member in group if _first_terminal_entry(member)[1]]
        counts = Counter([core for core in cores if core])
        best = max(counts.values()) if counts else 0
        early_hits = sum(1 for member in group if 0 <= _first_terminal_entry(member)[2] <= early_k)
        total = len(group) if group else 1
        results[key] = {
            "methods.core_agreement": best,
            "methods.early_fraction": early_hits / total,
            "method.agree_count": best,
        }
    return results