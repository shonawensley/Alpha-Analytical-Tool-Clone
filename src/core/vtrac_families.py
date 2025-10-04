from __future__ import annotations

"""Utilities for grouping boxed V-TRAC doubles into mirror families."""

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, Tuple

from modules.vtrac_reference import VTRAC_DISPLAY

# Mirror classes map each digit to its 0/5, 1/6, etc. family
_MIRROR_CLASS: Dict[int, int] = {
    0: 0,
    5: 0,
    1: 1,
    6: 1,
    2: 2,
    7: 2,
    3: 3,
    8: 3,
    4: 4,
    9: 4,
}


@dataclass(frozen=True)
class VtracDoubleFamily:
    """Represents the union of two mirror classes of V-TRAC doubles."""

    key: Tuple[int, int]
    label: str
    indices: Tuple[int, ...]
    combos: Tuple[str, ...]

    def combo_set(self) -> Tuple[str, ...]:
        return self.combos


def _canonical_combo(combo: str) -> str:
    combo = (combo or "").strip()
    if len(combo) != 3 or not combo.isdigit():
        return ""
    return "".join(sorted(combo))


def _class_pair(c1: int, c2: int) -> Tuple[int, int]:
    return tuple(sorted((c1, c2)))


def _label_for_classes(classes: Tuple[int, int]) -> str:
    a, b = classes
    if a == b:
        digits = _mirror_pair_label(a)
        return digits
    return f"{_mirror_pair_label(a)}-{_mirror_pair_label(b)}"


def _mirror_pair_label(class_idx: int) -> str:
    mapping = {
        0: "0/5",
        1: "1/6",
        2: "2/7",
        3: "3/8",
        4: "4/9",
    }
    return mapping[class_idx]


def _family_data() -> Iterable[VtracDoubleFamily]:
    families: Dict[Tuple[int, int], Dict[str, set]] = {}
    index_lookup: Dict[int, Tuple[int, int]] = {}

    for entry in VTRAC_DISPLAY:
        idx = entry.get("Index")
        doubles_str = entry.get("Doubles", "")
        if not doubles_str or not idx:
            continue
        combos = [token for token in doubles_str.split() if token]
        for combo in combos:
            canonical = _canonical_combo(combo)
            if not canonical:
                continue
            # Identify repeated and singleton digits
            counts = Counter(canonical)
            repeated_digit = next(d for d, c in counts.items() if c >= 2)
            other_digit = next(d for d, c in counts.items() if d != repeated_digit)
            
            rep_class = _MIRROR_CLASS[int(repeated_digit)]
            other_class = _MIRROR_CLASS[int(other_digit)]
            key = _class_pair(rep_class, other_class)
            bucket = families.setdefault(key, {"indices": set(), "combos": set()})
            bucket["indices"].add(idx)
            bucket["combos"].add(canonical)
            index_lookup[idx] = key

    for key, payload in families.items():
        label = _label_for_classes(key)
        indices = tuple(sorted(payload["indices"]))
        combos = tuple(sorted(payload["combos"]))
        yield VtracDoubleFamily(key=key, label=label, indices=indices, combos=combos)


@lru_cache(maxsize=1)
def get_double_families() -> Tuple[VtracDoubleFamily, ...]:
    return tuple(_family_data())


VTRAC_DOUBLE_FAMILIES: Tuple[VtracDoubleFamily, ...] = get_double_families()
COMBO_TO_FAMILY: Dict[str, VtracDoubleFamily] = {}
INDEX_TO_FAMILY: Dict[int, VtracDoubleFamily] = {}
for fam in VTRAC_DOUBLE_FAMILIES:
    for combo in fam.combos:
        COMBO_TO_FAMILY[combo] = fam
    for idx in fam.indices:
        INDEX_TO_FAMILY.setdefault(idx, fam)

