from __future__ import annotations

from itertools import permutations
from typing import Dict, Iterable, List, Set, Tuple

# V‑TRAC map: (0,5)->1, (1,6)->2, (2,7)->3, (3,8)->4, (4,9)->5
DIGIT_TO_V: Dict[str, int] = {
    "0": 1,
    "5": 1,
    "1": 2,
    "6": 2,
    "2": 3,
    "7": 3,
    "3": 4,
    "8": 4,
    "4": 5,
    "9": 5,
}

MIRROR_MAP: Dict[str, str] = {
    "0": "5", "5": "0",
    "1": "6", "6": "1",
    "2": "7", "7": "2",
    "3": "8", "8": "3",
    "4": "9", "9": "4",
}

def v_of_digit(d: str) -> int:
    if d not in DIGIT_TO_V:
        raise ValueError(f"Invalid digit '{d}' for V-TRAC mapping")
    return DIGIT_TO_V[d]

def map_digits_to_v(s: str) -> List[int]:
    return [v_of_digit(ch) for ch in s if ch.isdigit()]

def _top_three_by_frequency(digits: Iterable[str]) -> List[str]:
    from collections import Counter
    c = Counter([d for d in digits if d.isdigit()])
    if not c:
        return []
    ordered = sorted(c.items(), key=lambda kv: (-kv[1], int(kv[0])))
    return [k for k, _ in ordered[:3]]

def canonical_vtriad_from_string(s: str) -> Tuple[Tuple[int, ...], Tuple[str, ...]]:
    uniq = sorted(set(ch for ch in s if ch.isdigit()), key=int)
    if not uniq:
        return tuple(), tuple()
    if len(uniq) <= 3:
        base = uniq
    else:
        base = _top_three_by_frequency(s)
    vtriad = tuple(sorted(v_of_digit(d) for d in base))
    raw_sorted = tuple(sorted(base, key=int))
    return vtriad, raw_sorted

def vt_family_id(vtriad: Tuple[int, ...]) -> str:
    if not vtriad:
        return "v—"
    return "v" + "".join(str(v) for v in vtriad)

def vt_permutations_for_digits(d1: str, d2: str, d3: str) -> Set[Tuple[str, str, str]]:
    return set(permutations([d1, d2, d3], 3))

def has_vt_straight_lane(s: str, vt_sequence: Tuple[int, int, int]) -> bool:
    if len(vt_sequence) != 3:
        return False
    seq = map_digits_to_v(s)
    if len(seq) < 3:
        return False
    target = list(vt_sequence)
    for i in range(0, len(seq) - 2):
        if seq[i:i+3] == target:
            return True
    return False
