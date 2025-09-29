from __future__ import annotations

from collections import Counter
from math import factorial
from typing import Any, Dict, List, Tuple

from .types import Item, Step

_MIRROR = {
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


def _digits(value: str) -> List[str]:
    return [ch for ch in value if ch.isdigit()]


def _canon_sort(value: str) -> str:
    digits = _digits(value)
    return "".join(sorted(digits)) if digits else ""


def _uniq_count(value: str) -> int:
    return len(set(_digits(value)))


def _first_terminal_entry(item: Item) -> Tuple[int, Step | None]:
    for index, step in enumerate(item.steps):
        if step.is_3value or step.length <= 3 or step.unique_digits <= 2:
            return index, step
    return -1, None


def _survival_fraction_at3(item: Item) -> float:
    index, step = _first_terminal_entry(item)
    if index < 0 or step is None:
        return 0.0
    core = set(_digits(step.value))
    origin = set(_digits(item.orig.value))
    return (len(core & origin) / max(1, len(origin))) if core else 0.0


def _order_cue_strength(item: Item) -> float:
    index, step = _first_terminal_entry(item)
    if index < 0 or step is None:
        return 0.0
    tail_values = [node.value for node in item.steps[index:]]
    return 1.0 / max(1, len(set(tail_values)))


def _tail_wobble(item: Item) -> int:
    index, step = _first_terminal_entry(item)
    if index < 0 or step is None:
        return 0
    duplicates = 0
    for node in item.steps[index + 1:]:
        if node.value == step.value:
            duplicates += 1
        else:
            break
    return duplicates


def _perm_density(value: str) -> float:
    digits = _digits(value)[:3]
    if not digits:
        return 0.0
    if len(digits) < 3:
        return 0.5
    counts = Counter(digits)
    denom = 1
    for count in counts.values():
        denom *= factorial(count)
    return (factorial(3) / denom) / 6.0


def _permutation_count(value: str) -> float:
    digits = _digits(value)
    if not digits:
        return 0.0
    counts = Counter(digits)
    denom = 1
    for count in counts.values():
        denom *= factorial(count)
    return float(factorial(len(digits)) / denom)


def _has_mirror_pair(value: str) -> int:
    bag = set(_digits(value))
    return int(any(_MIRROR[d] in bag for d in bag)) if bag else 0


def _part1_features(item: Item, early_k: int) -> Dict[str, Any]:
    features: Dict[str, Any] = {}
    index, step = _first_terminal_entry(item)
    first_step_number = step.step if step else 99
    diffs = [item.steps[i - 1].length - item.steps[i].length for i in range(1, len(item.steps))]
    last_step = item.steps[-1] if item.steps else Step(0, "", 0, 0, False)

    features["traj.first3"] = first_step_number
    features["traj.early_terminal"] = int(0 <= first_step_number <= early_k)
    features["traj.reduction_slope"] = sum(diffs) / len(diffs) if diffs else 0.0
    features["tail.final_len"] = last_step.length
    features["tail.final_unique"] = last_step.unique_digits
    features["tail.exact_len3"] = int(any(node.length == 3 for node in item.steps))
    features["tail.unique2"] = int(any(node.unique_digits == 2 for node in item.steps))
    features["stability.survival_frac3"] = _survival_fraction_at3(item)
    features["stability.order_cue"] = _order_cue_strength(item)
    features["tail.wobble"] = _tail_wobble(item)
    features["pre.mirror_pair"] = _has_mirror_pair(item.orig.value)
    features["pre.core3_hint"] = int(_uniq_count(item.orig.value) <= 3 and len(_digits(item.orig.value)) >= 3)
    features["perm.density"] = _perm_density(last_step.value)
    features["final.value"] = last_step.value
    features["final.canon3"] = _canon_sort(last_step.value)
    features["final.len_is1"] = int(last_step.length == 1)
    features["final.len_is2"] = int(last_step.length == 2)
    features["final.len_is3"] = int(last_step.length == 3)

    return features


def _part2_features(item: Item) -> Dict[str, Any]:
    features: Dict[str, Any] = {}
    seq = item.sequence_meta or {}
    final = item.final or {}
    steps = item.steps or []

    _, terminal_step = _first_terminal_entry(item)
    time_to_3 = seq.get("first_3value_step")
    if time_to_3 is None:
        time_to_3 = terminal_step.step if terminal_step else 99

    last_change = seq.get("last_change_step")
    if last_change is None and steps:
        last_change = max(node.step for node in steps)

    post3_span = 0
    if isinstance(last_change, int) and isinstance(time_to_3, int) and time_to_3 != 99:
        post3_span = max(0, last_change - time_to_3)

    terminal_len = final.get("length")
    if terminal_len is None and steps:
        terminal_len = steps[-1].length
    terminal_unique = final.get("unique_digits")
    if terminal_unique is None and steps:
        terminal_unique = steps[-1].unique_digits
    is_terminal_three = final.get("is_3value")
    if is_terminal_three is None and steps:
        is_terminal_three = steps[-1].is_3value

    features.update(
        {
            "time_to_3": int(time_to_3 if isinstance(time_to_3, int) else 99),
            "post3_span": float(post3_span),
            "terminal.len": int(terminal_len or 0),
            "terminal.unique": int(terminal_unique or 0),
            "terminal.is_3value": int(bool(is_terminal_three)),
            "terminal.unique_1": int((terminal_unique or 0) == 1),
            "terminal.unique_2": int((terminal_unique or 0) == 2),
            "pre.orig_unique": int(item.orig.unique_digits if steps else 0),
            "sequence.steps_total": int(seq.get("steps_total_before_compaction", len(steps))),
            "sequence.steps_kept": int(seq.get("steps_kept_after_compaction", len(steps))),
            "perm.count": _permutation_count(final.get("value", "")),
        }
    )
    features["terminal.len_is1"] = int(features["terminal.len"] == 1)
    features["terminal.len_is2"] = int(features["terminal.len"] == 2)
    features["terminal.len_is3"] = int(features["terminal.len"] == 3)
    return features


def compute_features_union(item: Item, thresholds: Dict[str, Any]) -> Dict[str, Any]:
    early_k = int(thresholds.get("early_step_k", 3))
    features = _part1_features(item, early_k)
    features.update(_part2_features(item))

    # harmonise trajectory timings
    candidate_times = [features.get("traj.first3"), features.get("time_to_3")]
    candidate_times = [value for value in candidate_times if isinstance(value, int)]
    traj_time = min(candidate_times) if candidate_times else 99
    features["traj.time_to_3"] = traj_time
    features["time_to_3_fast"] = int(traj_time <= int(thresholds.get("time_to_3_fast", 3)))

    # harmonise terminal/final values
    features["terminal.len"] = int(features.get("terminal.len", features.get("tail.final_len", 0)))
    features["terminal.unique"] = int(features.get("terminal.unique", features.get("tail.final_unique", 0)))
    features["terminal.unique_1"] = int(features["terminal.unique"] == 1)
    features["terminal.unique_2"] = int(features["terminal.unique"] == 2)
    features["terminal.len_is1"] = int(features["terminal.len"] == 1)
    features["terminal.len_is2"] = int(features["terminal.len"] == 2)
    features["terminal.len_is3"] = int(features["terminal.len"] == 3)

    final_value = features.get("final.value", "")
    digits_only = "".join(_digits(final_value))
    features["degenerate.empty"] = int(len(digits_only) == 0)
    if not features.get("final.canon3"):
        features["final.canon3"] = _canon_sort(final_value)
    features["final_3canon"] = features["final.canon3"]

    features.setdefault("perm.density", _perm_density(final_value))
    features.setdefault("tail.wobble", 0)
    features.setdefault("pre.orig_unique", _uniq_count(item.orig.value))
    features.setdefault("post3_span", 0.0)

    return features
