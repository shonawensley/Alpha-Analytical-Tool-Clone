from __future__ import annotations

from dataclasses import dataclass
import itertools
import re
from typing import Dict, Iterable, List, Sequence, Tuple

DIGIT_TO_VT: Dict[str, str] = {
    '0': '1', '5': '1',
    '1': '2', '6': '2',
    '2': '3', '7': '3',
    '3': '4', '8': '4',
    '4': '5', '9': '5',
}


@dataclass(frozen=True)
class WinnerTargets:
    straights: Sequence[str]
    family: Sequence[str]
    straights_gap_regexes: Sequence[re.Pattern[str]]
    family_gap_regexes: Sequence[re.Pattern[str]]
    vt_pair: Tuple[str, str] | None = None


def digits_only(value: str) -> str:
    return ''.join(ch for ch in str(value or '') if ch.isdigit())


def permutations_of_winner(combo: str) -> List[str]:
    digits = digits_only(combo)
    if len(digits) != 3:
        return []
    return sorted({''.join(p) for p in itertools.permutations(digits, 3)})


def _gap_regex(token: str) -> re.Pattern[str]:
    a, b, c = token
    return re.compile(fr"{a}\d?{b}\d?{c}")


def _winner_vt_pair(winner: str) -> Tuple[str, str] | None:
    digits = digits_only(winner)
    if len(digits) != 3:
        return None
    vt_digits: List[str] = []
    for ch in digits:
        mapped = DIGIT_TO_VT.get(ch)
        if mapped is None:
            return None
        vt_digits.append(mapped)
    seen: List[str] = []
    for vt in vt_digits:
        if vt not in seen:
            seen.append(vt)
    if len(seen) == 2:
        return seen[0], seen[1]
    return None


def build_winner_targets(winner: str, index_family: Iterable[str]) -> WinnerTargets:
    straights = permutations_of_winner(winner)
    family = sorted({digits_only(value) for value in index_family if len(digits_only(value)) == 3})
    return WinnerTargets(
        straights=straights,
        family=family,
        straights_gap_regexes=[_gap_regex(token) for token in straights],
        family_gap_regexes=[_gap_regex(token) for token in family],
        vt_pair=_winner_vt_pair(winner),
    )


def _scan_cell_tokens(cleaned: str, tokens: Sequence[str], gap_regexes: Sequence[re.Pattern[str]]) -> Tuple[set[str], set[str]]:
    if len(cleaned) < 3:
        return set(), set()
    strict_hits = {token for token in tokens if token in cleaned}
    gap_hits = {
        token
        for token, rx in zip(tokens, gap_regexes)
        if token not in strict_hits and rx.search(cleaned)
    }
    return strict_hits, gap_hits


def analyze_cell(cell: str, targets: WinnerTargets) -> Tuple[set[str], set[str], set[str], set[str]]:
    cleaned = digits_only(cell)
    straights_strict, straights_gap = _scan_cell_tokens(cleaned, targets.straights, targets.straights_gap_regexes)
    family_strict, family_gap = _scan_cell_tokens(cleaned, targets.family, targets.family_gap_regexes)
    return straights_strict, straights_gap, family_strict, family_gap


def _vt_straight_spans(cleaned: str, positions: Sequence[int], vt_pair: Tuple[str, str]) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    if len(cleaned) < 4 or len(positions) < 4:
        return [], []

    runs: List[Tuple[str, str, int, int]] = []  # (digit, vt_digit, start_idx, end_idx)
    idx = 0
    while idx < len(cleaned):
        digit = cleaned[idx]
        vt_digit = DIGIT_TO_VT.get(digit)
        if vt_digit is None:
            idx += 1
            continue
        start = idx
        while idx < len(cleaned) and cleaned[idx] == digit:
            idx += 1
        end = idx
        runs.append((digit, vt_digit, start, end))

    if len(runs) < 2:
        return [], []

    strict_hits: set[Tuple[int, int]] = set()
    tolerant_hits: set[Tuple[int, int]] = set()
    a, b = vt_pair

    for first, second in zip(runs, runs[1:]):
        _, vt1, start1, end1 = first
        _, vt2, start2, end2 = second
        len1 = end1 - start1
        len2 = end2 - start2
        if len1 >= 2 and len2 >= 2 and ((vt1 == a and vt2 == b) or (vt1 == b and vt2 == a)):
            strict_hits.add((positions[start1], positions[end2 - 1] + 1))

    for r1, r2, r3 in zip(runs, runs[1:], runs[2:]):
        _, vt1, start1, end1 = r1
        _, vt2, start2, end2 = r2
        _, vt3, start3, end3 = r3
        len1 = end1 - start1
        len2 = end2 - start2
        len3 = end3 - start3
        if len1 < 2 or len3 < 2 or len2 < 2:
            continue
        if {vt1, vt3} == {a, b} and vt2 not in {a, b}:
            tolerant_hits.add((positions[start1], positions[end3 - 1] + 1))

    return sorted(strict_hits), sorted(tolerant_hits)


def collect_spans(cell: str, targets: WinnerTargets) -> Dict[str, List[Tuple[int, int]]]:
    cleaned = digits_only(cell)
    positions = [idx for idx, ch in enumerate(str(cell)) if ch.isdigit()]
    if len(cleaned) < 3:
        return {
            'winner_strict': [],
            'winner_gap': [],
            'family_strict': [],
            'family_gap': [],
            'vt_straight_strict': [],
            'vt_straight_gap': [],
        }

    def spans(tokens: Sequence[str], regexes: Sequence[re.Pattern[str]]) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        strict_ranges: set[Tuple[int, int]] = set()
        gap_ranges: set[Tuple[int, int]] = set()
        for token in tokens:
            if not token:
                continue
            for match in re.finditer(re.escape(token), cleaned):
                start_digit = match.start()
                end_digit = match.end() - 1
                if end_digit < len(positions):
                    strict_ranges.add((positions[start_digit], positions[end_digit] + 1))
        for token, rx in zip(tokens, regexes):
            if not token:
                continue
            for match in rx.finditer(cleaned):
                start_digit = match.start()
                end_digit = match.end() - 1
                if end_digit < len(positions):
                    gap_ranges.add((positions[start_digit], positions[end_digit] + 1))
        return sorted(strict_ranges), sorted(gap_ranges)

    winner_strict, winner_gap = spans(targets.straights, targets.straights_gap_regexes)
    family_strict, family_gap = spans(targets.family, targets.family_gap_regexes)
    vt_straight_strict: List[Tuple[int, int]] = []
    vt_straight_gap: List[Tuple[int, int]] = []
    if targets.vt_pair is not None:
        vt_straight_strict, vt_straight_gap = _vt_straight_spans(cleaned, positions, targets.vt_pair)

    return {
        'winner_strict': winner_strict,
        'winner_gap': winner_gap,
        'family_strict': family_strict,
        'family_gap': family_gap,
        'vt_straight_strict': vt_straight_strict,
        'vt_straight_gap': vt_straight_gap,
    }
