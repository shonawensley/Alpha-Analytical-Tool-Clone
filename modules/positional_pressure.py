from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional, Any
import math
import statistics

# Optional V-TRAC overlay (degrades gracefully if not available)
try:
    # In Aux we prefer the staged working ref; but if the canonical one is on sys.path, this still works.
    from modules.vtrac_reference import get_vtrac_index  # type: ignore
except Exception:
    get_vtrac_index = None  # type: ignore


Digit = int  # 0..9
Draw = str   # "507" newest-first


@dataclass
class PosDigitStat:
    digit: Digit
    gap: int
    median_gap: float
    p75_gap: float
    pressure: float
    last_seen_idx: Optional[int]  # 0 = seen on latest draw, None = not seen in window


@dataclass
class PositionSummary:
    pos: int  # 1,2,3 for display
    top: List[PosDigitStat]  # length <= 3
    population_size: int     # how many draws considered in the stream


@dataclass
class Candidate:
    combo: str        # e.g. "617" (pos1-pos2-pos3)
    score: float
    ranks: Tuple[int, int, int]  # 1-based ranks per position (1,2,3)
    dr: int            # digital root (1..9, with 9 kept as 9)
    vtrac: Optional[int]  # V-TRAC index if available
    tags: List[str]    # textual flags, e.g., ["TOP1x2", "P75x2"]


@dataclass
class PositionalPressureResult:
    n_draws_used: int
    per_position: List[PositionSummary]
    candidates: List[Candidate]  # sorted desc by score

    def to_dict(self) -> Dict[str, Any]:
        return {
            "n_draws_used": self.n_draws_used,
            "per_position": [
                {
                    "pos": s.pos,
                    "population_size": s.population_size,
                    "top": [
                        {
                            "digit": t.digit,
                            "gap": t.gap,
                            "median_gap": t.median_gap,
                            "p75_gap": t.p75_gap,
                            "pressure": round(t.pressure, 3),
                            "last_seen_idx": t.last_seen_idx,
                        }
                        for t in s.top
                    ],
                }
                for s in self.per_position
            ],
            "candidates": [
                {
                    "combo": c.combo,
                    "score": round(c.score, 3),
                    "ranks": c.ranks,
                    "dr": c.dr,
                    "vtrac": c.vtrac,
                    "tags": c.tags,
                }
                for c in self.candidates
            ],
        }


# ---------- Core utilities ----------

_MIRRORS = {0: 5, 5: 0, 1: 6, 6: 1, 2: 7, 7: 2, 3: 8, 8: 3, 4: 9, 9: 4}

def _is_draw(s: str) -> bool:
    return isinstance(s, str) and len(s) == 3 and s.isdigit()

def _digit_at(draw: Draw, pos_idx: int) -> Digit:
    # pos_idx: 0,1,2
    return int(draw[pos_idx])

def _digital_root(n_str: str) -> int:
    s = sum(int(ch) for ch in n_str)
    # keep 9 as 9 (not 0)
    while s > 9:
        s = sum(int(ch) for ch in str(s))
    return s if s != 0 else 9

def _percentile_75(xs: List[int]) -> float:
    if not xs:
        return 0.0
    xs_sorted = sorted(xs)
    k = 0.75 * (len(xs_sorted) - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(xs_sorted[int(k)])
    return xs_sorted[f] + (xs_sorted[c] - xs_sorted[f]) * (k - f)


def _position_stream(draws: List[Draw], pos_idx: int) -> List[Digit]:
    # newest-first draws -> newest-first digits stream for a position
    return [_digit_at(d, pos_idx) for d in draws if _is_draw(d)]


def _scan_intervals_for_digit(stream: List[Digit], d: Digit) -> List[int]:
    """
    Inter-arrival intervals between occurrences of digit d in the stream.
    Stream is newest-first; indices increase with age.
    Interval measured as i - prev_i (so "gap" semantics match current index when seen).
    """
    prev_idx = None
    intervals: List[int] = []
    for i, val in enumerate(stream):
        if val == d:
            if prev_idx is not None:
                intervals.append(i - prev_idx)
            prev_idx = i
    return intervals


def _current_gap_for_digit(stream: List[Digit], d: Digit) -> Tuple[int, Optional[int]]:
    """
    Returns (gap, last_seen_index). If never seen, gap == len(stream) and last_seen_index is None.
    """
    for i, val in enumerate(stream):
        if val == d:
            return i, i  # i draws since last occurrence, last_seen at i
    return len(stream), None


def _topk_for_position(stream: List[Digit], k: int) -> List[PosDigitStat]:
    stats: List[PosDigitStat] = []
    for d in range(10):
        gap, last_idx = _current_gap_for_digit(stream, d)
        intervals = _scan_intervals_for_digit(stream, d)
        median_gap = float(statistics.median(intervals)) if intervals else float(len(stream) / 2.0)
        p75_gap = float(_percentile_75(intervals)) if intervals else float(0.75 * len(stream))
        pressure = (gap + 1.0) / (p75_gap + 1.0)
        stats.append(PosDigitStat(digit=d, gap=gap, median_gap=median_gap, p75_gap=p75_gap,
                                  pressure=pressure, last_seen_idx=last_idx))
    # Sort primarily by gap desc, then pressure desc, then digit desc (stable)
    stats.sort(key=lambda s: (s.gap, s.pressure, s.digit), reverse=True)
    return stats[:k]


def _rank_weight(rank_1_based: int) -> int:
    return {1: 3, 2: 2, 3: 1}.get(rank_1_based, 0)


def _build_candidates(p1: List[PosDigitStat], p2: List[PosDigitStat], p3: List[PosDigitStat],
                      top_n: int = 12) -> List[Candidate]:
    # Pre-index ranks and p75 flags for scoring
    rank1 = {s.digit: i + 1 for i, s in enumerate(p1)}  # digit -> 1..3
    rank2 = {s.digit: i + 1 for i, s in enumerate(p2)}
    rank3 = {s.digit: i + 1 for i, s in enumerate(p3)}

    p75_1 = {s.digit: (s.gap >= s.p75_gap) for s in p1}
    p75_2 = {s.digit: (s.gap >= s.p75_gap) for s in p2}
    p75_3 = {s.digit: (s.gap >= s.p75_gap) for s in p3}

    cands: List[Candidate] = []
    for d1 in rank1:
        for d2 in rank2:
            for d3 in rank3:
                combo = f"{d1}{d2}{d3}"
                r1, r2, r3 = rank1[d1], rank2[d2], rank3[d3]

                score = float(_rank_weight(r1) + _rank_weight(r2) + _rank_weight(r3))
                tags: List[str] = []

                # Boosts for "beyond typical" pressure per position
                boost = 0.0
                if p75_1.get(d1, False): boost += 0.25; tags.append("P1>P75")
                if p75_2.get(d2, False): boost += 0.25; tags.append("P2>P75")
                if p75_3.get(d3, False): boost += 0.25; tags.append("P3>P75")

                # Tag if multiple TOP1s present
                top1_count = sum(1 for rk in (r1, r2, r3) if rk == 1)
                if top1_count >= 2:
                    boost += 0.25
                    tags.append(f"TOP1x{top1_count}")

                dr = _digital_root(combo)
                vtrac = int(get_vtrac_index(combo)) if callable(get_vtrac_index) else None

                cands.append(Candidate(combo=combo, score=score + boost,
                                       ranks=(r1, r2, r3), dr=dr, vtrac=vtrac, tags=tags))

    # Sort by score desc, then prefer combos with more TOP1s, then by simple tie-breakers
    def _tie_key(c: Candidate):
        top1s = sum(1 for r in c.ranks if r == 1)
        return (c.score, top1s, -c.dr, c.combo)  # favor higher score, more TOP1s, then deterministic
    cands.sort(key=_tie_key, reverse=True)
    return cands[:top_n]


def analyze_positional_pressure(
    draws_newest_first: List[Draw],
    window: int = 150,
    topk_per_pos: int = 3,
    top_n_candidates: int = 12
) -> PositionalPressureResult:
    """
    Main entry: compute positional stats & candidates from newest-first draws.
    """
    if not draws_newest_first:
        return PositionalPressureResult(n_draws_used=0, per_position=[], candidates=[])

    # Clamp window, sanitize draws
    draws = [d for d in draws_newest_first if _is_draw(d)]
    if not draws:
        return PositionalPressureResult(n_draws_used=0, per_position=[], candidates=[])

    use = draws[:window] if len(draws) > window else draws
    s1 = _position_stream(use, 0)  # P1 = leftmost digit
    s2 = _position_stream(use, 1)  # P2 = middle
    s3 = _position_stream(use, 2)  # P3 = rightmost

    top1 = _topk_for_position(s1, topk_per_pos)
    top2 = _topk_for_position(s2, topk_per_pos)
    top3 = _topk_for_position(s3, topk_per_pos)

    per_pos = [
        PositionSummary(pos=1, top=top1, population_size=len(s1)),
        PositionSummary(pos=2, top=top2, population_size=len(s2)),
        PositionSummary(pos=3, top=top3, population_size=len(s3)),
    ]

    cands = _build_candidates(top1, top2, top3, top_n=top_n_candidates)
    return PositionalPressureResult(n_draws_used=len(use), per_position=per_pos, candidates=cands)
