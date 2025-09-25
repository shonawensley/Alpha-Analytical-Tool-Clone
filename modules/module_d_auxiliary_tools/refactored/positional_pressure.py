# modules/module_d_auxiliary_tools/refactored/positional_pressure.py
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple

Digit = int  # 0..9
Pos = int    # 0,1,2  (P1,P2,P3)

@dataclass(frozen=True)
class PosRank:
    rank: int           # 1..k
    digit: Digit        # 0..9
    gap: int            # draws since last seen at this position (0 means seen in latest draw)
    last_seen_idx: Optional[int]  # 0=latest, None=not seen in window
    # reserve for future flags (e.g., consensus, overlay tags)
    tags: Tuple[str, ...] = ()

@dataclass
class PositionTop:
    position: Pos                    # 0,1,2
    top: List[PosRank]               # length k
    population: Dict[Digit, int]     # times each digit appeared in window at this position
    window: int                      # window used
    total_draws: int                 # total draws provided

@dataclass
class PositionalPressureResult:
    k: int
    window: int
    total_draws: int
    per_position: Dict[Pos, PositionTop]  # keys 0,1,2

def _normalize_draw(draw: str) -> Optional[str]:
    if not draw or len(draw) != 3:
        return None
    s = draw.strip()
    if len(s) != 3 or any(ch < '0' or ch > '9' for ch in s):
        return None
    return s

def _compute_gap_for_digit_at_pos(draws: List[str], pos: Pos, digit: Digit, window: int) -> Tuple[int, Optional[int]]:
    """
    Returns (gap, last_seen_idx). gap = number of draws since digit was last seen at 'pos'.
    If seen in the latest draw at pos -> gap=0, last_seen_idx=0.
    If not seen within 'window' draws -> gap=window, last_seen_idx=None.
    """
    limit = min(window, len(draws))
    for idx in range(limit):
        if int(draws[idx][pos]) == digit:
            return idx, idx
    return limit, None

def _population(draws: List[str], pos: Pos, window: int) -> Dict[Digit, int]:
    limit = min(window, len(draws))
    counts = {d: 0 for d in range(10)}
    for i in range(limit):
        d = int(draws[i][pos])
        counts[d] += 1
    return counts

def compute_positional_pressure(draws: List[str], window: int = 150, k: int = 3) -> PositionalPressureResult:
    """
    Core engine: given newest-first draws, compute top-k most-due digits for each position.
    - window: how many recent draws to scan (newest-first).
    - k: number of ranks per position (1..k).
    """
    clean = [_normalize_draw(d) for d in draws]
    clean = [d for d in clean if d is not None]
    ww = min(window, len(clean))
    result: Dict[Pos, PositionTop] = {}

    for pos in (0, 1, 2):
        # compute gap & last_seen for all digits 0..9 at this position
        items: List[PosRank] = []
        pop = _population(clean, pos, ww)
        for digit in range(10):
            gap, last_idx = _compute_gap_for_digit_at_pos(clean, pos, digit, ww)
            items.append(PosRank(rank=0, digit=digit, gap=gap, last_seen_idx=last_idx))

        # sort by (gap desc, digit asc) for stable tie-break
        items.sort(key=lambda r: (-r.gap, r.digit))
        topk = []
        for i, itm in enumerate(items[:k], start=1):
            topk.append(PosRank(rank=i, digit=itm.digit, gap=itm.gap, last_seen_idx=itm.last_seen_idx, tags=()))

        result[pos] = PositionTop(position=pos, top=topk, population=pop, window=ww, total_draws=len(clean))

    return PositionalPressureResult(k=k, window=ww, total_draws=len(clean), per_position=result)

# Optional pretty helpers (safe to ignore by callers)
def as_rows(res: PositionalPressureResult) -> Dict[Pos, List[Dict]]:
    out: Dict[Pos, List[Dict]] = {}
    for pos, pt in res.per_position.items():
        out[pos] = [asdict(r) for r in pt.top]
    return out
