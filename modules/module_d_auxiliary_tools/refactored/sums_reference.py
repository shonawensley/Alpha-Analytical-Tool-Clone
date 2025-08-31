# modules/sums_reference.py

from typing import Dict, Tuple

__all__ = [
    "SUM_COUNTS",
    "SUM_PROB",
    "ROOTSUM_COUNTS",
    "ROOTSUM_PROB",
    "digital_root",
    "sum_of_draw",
    "root_sum_of_draw",
]

def digital_root(n: int) -> int:
    """
    Digital root of a non-negative integer.
    Conventional mapping: 0 stays 0; otherwise 1..9.
    """
    if n <= 0:
        return 0
    return 1 + ((n - 1) % 9)

def sum_of_draw(draw: str) -> int:
    """
    Sum the digits of a 3-digit draw string, e.g., '042' -> 6.
    """
    if not draw or len(draw) != 3 or not draw.isdigit():
        raise ValueError(f"Invalid draw: {draw!r}")
    return int(draw[0]) + int(draw[1]) + int(draw[2])

def root_sum_of_draw(draw: str) -> int:
    """
    Digital root of the sum of digits for the draw.
    '000' -> 0; others -> 1..9.
    """
    return digital_root(sum_of_draw(draw))

def _build_sum_and_rootsum_counts() -> Tuple[Dict[int, int], Dict[int, int]]:
    """
    Enumerate all ordered 3-digit numbers 000..999 to count:
      - counts per sum (0..27)
      - counts per root-sum (0..9; 0 occurs only for 000)
    """
    sum_counts: Dict[int, int] = {s: 0 for s in range(0, 28)}
    rootsum_counts: Dict[int, int] = {r: 0 for r in range(0, 10)}
    for a in range(10):
        for b in range(10):
            for c in range(10):
                s = a + b + c
                sum_counts[s] += 1
                r = digital_root(s)
                rootsum_counts[r] += 1
    return sum_counts, rootsum_counts

# Build tables once at import
SUM_COUNTS, ROOTSUM_COUNTS = _build_sum_and_rootsum_counts()

# Convert to probabilities (over 1000 outcomes)
SUM_PROB: Dict[int, float] = {k: v / 1000.0 for k, v in SUM_COUNTS.items()}
ROOTSUM_PROB: Dict[int, float] = {k: v / 1000.0 for k, v in ROOTSUM_COUNTS.items()}
