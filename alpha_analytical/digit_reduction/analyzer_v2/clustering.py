from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

Digit = str


def _is_digit(ch: str) -> bool:
    return "0" <= ch <= "9"


def _sanitize(value: str) -> str:
    """Return the digit-only representation of *value*."""
    if not value:
        return ""
    return "".join(ch for ch in value if _is_digit(ch))


def _run_lengths(segment: str) -> Dict[Digit, int]:
    """
    Compute the maximum contiguous run length per digit inside *segment*.
    The lookup is limited to digits that actually appear in the segment.
    """
    best: Dict[Digit, int] = {}
    current_digit: Digit | None = None
    current_run = 0
    for ch in segment:
        if ch == current_digit:
            current_run += 1
        else:
            if current_digit is not None:
                best[current_digit] = max(best.get(current_digit, 0), current_run)
            current_digit = ch
            current_run = 1
    if current_digit is not None:
        best[current_digit] = max(best.get(current_digit, 0), current_run)
    return best


def _unique_key(segment: str) -> str:
    return "".join(sorted(set(segment)))


@dataclass(frozen=True, slots=True)
class Cluster:
    """
    Representation of a contiguous digit window that contains at most three
    distinct digits (the practical range for 3-value family analysis).
    """

    text: str
    span: Tuple[int, int]
    unique: str
    run_lengths: Dict[Digit, int]

    @property
    def length(self) -> int:
        return self.span[1] - self.span[0]

    @property
    def unique_count(self) -> int:
        return len(self.unique)

    @property
    def is_three_value(self) -> bool:
        return self.unique_count == 3

    @property
    def digits(self) -> Tuple[Digit, ...]:
        return tuple(self.text)

    def iter_trigrams(self) -> Iterator[str]:
        """
        Yield the 3-character windows contained within the cluster. Duplicate
        windows are preserved; callers can deduplicate if required.
        """
        window = 3
        if self.length < window:
            return
        for idx in range(self.length - window + 1):
            yield self.text[idx : idx + window]


def extract_clusters(value: str, min_len: int = 3, max_len: int = 12) -> List[Cluster]:
    """
    Return all digit windows in *value* whose unique digit count is between
    two and three (inclusive). Windows shorter than *min_len* or longer than
    *max_len* are ignored.

    The original string may contain formatting characters; only digits are
    considered when producing clusters.
    """
    digits = _sanitize(value)
    if not digits:
        return []

    lo = max(1, min_len)
    hi = max(lo, max_len)
    clusters: List[Cluster] = []
    n = len(digits)
    for window in range(lo, min(hi, n) + 1):
        for start in range(0, n - window + 1):
            segment = digits[start : start + window]
            uniq = _unique_key(segment)
            uniq_count = len(uniq)
            if uniq_count < 2 or uniq_count > 3:
                continue
            clusters.append(
                Cluster(
                    text=segment,
                    span=(start, start + window),
                    unique=uniq,
                    run_lengths=_run_lengths(segment),
                )
            )
    return clusters


def iter_trigrams(value: str) -> Iterator[str]:
    """Yield 3-character digit windows from *value*."""
    digits = _sanitize(value)
    if len(digits) < 3:
        return
    for idx in range(len(digits) - 2):
        yield digits[idx : idx + 3]


def contiguous_runs(value: str) -> List[Tuple[int, int, Digit]]:
    """
    Return spans (start, end, digit) for each contiguous digit run in *value*.
    The coordinates are measured against the digit-only representation.
    """
    digits = _sanitize(value)
    runs: List[Tuple[int, int, Digit]] = []
    if not digits:
        return runs
    start = 0
    current = digits[0]
    for idx in range(1, len(digits)):
        ch = digits[idx]
        if ch == current:
            continue
        runs.append((start, idx, current))
        start = idx
        current = ch
    runs.append((start, len(digits), current))
    return runs


def drop_contiguous_run(value: str, start: int, end: int) -> str:
    """
    Remove the digits between *start* (inclusive) and *end* (exclusive) from
    the digit-only representation of *value* and return the collapsed result.
    """
    digits = _sanitize(value)
    if start < 0 or end <= start or end > len(digits):
        return digits
    return digits[:start] + digits[end:]


def drop_variants(value: str) -> List[Tuple[str, Digit, int]]:
    """
    Produce unique strings resulting from removing each contiguous digit run.
    The tuple contains (collapsed, digit_removed, run_length).
    """
    seen = set()
    variants: List[Tuple[str, Digit, int]] = []
    for start, end, digit in contiguous_runs(value):
        collapsed = drop_contiguous_run(value, start, end)
        if not collapsed:
            continue
        key = (collapsed, digit, end - start)
        if key in seen:
            continue
        seen.add(key)
        variants.append(key)
    return variants
