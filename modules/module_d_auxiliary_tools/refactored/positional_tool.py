from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Tuple
import math
import statistics

try:
    from typing import Literal
except ImportError:  # Python <3.8 fallback (should not happen on project runtime)
    from typing_extensions import Literal  # type: ignore

# Optional V-TRAC support; degrade gracefully when unavailable
try:
    from modules.vtrac_reference import get_vtrac_index  # type: ignore
except Exception:  # pragma: no cover - staged Aux path may not exist outside app runtime
    get_vtrac_index = None  # type: ignore

Variant = Literal["combined", "midday", "evening"]
PositionIndex = Literal[0, 1, 2]

MIRROR_MAP: Dict[int, int] = {0: 5, 5: 0, 1: 6, 6: 1, 2: 7, 7: 2, 3: 8, 8: 3, 4: 9, 9: 4}


HARD_DUE_THRESHOLDS: Dict[Variant, int] = {
    "combined": 55,
    "midday": 40,
    "evening": 40,
}


@dataclass(frozen=True)
class PositionalTrackerCell:
    digit: int
    draws_since: int
    hard_due: bool


@dataclass(frozen=True)
class WeightsConfig:
    """Tunable scoring weights for positional pressure."""

    variant: Dict[Variant, float] = field(
        default_factory=lambda: {"combined": 1.0, "midday": 0.95, "evening": 0.95}
    )
    rank: Dict[int, float] = field(default_factory=lambda: {1: 1.0, 2: 0.7, 3: 0.45})
    lag_full_weight_at: float = 35.0
    mirror_same_variant: float = 0.5
    consensus_exact: float = 0.4
    consensus_mirror: float = 0.25
    double_pressure: float = 0.6
    double_due_bonus: float = 0.4
    swap_echo: float = 0.10
    swap_echo_mirror: float = 0.07
    recent_heat_brake: int = 3  # draws
    mirror_tag: str = "Mirror"
    consensus_tag: str = "Consensus"
    double_tag: str = "Double"
    swap_tag: str = "Swap"
    max_candidate_per_position: int = 2
    max_candidates: int = 12

    def rank_weight(self, rank: int) -> float:
        return self.rank.get(rank, 0.0)

    def variant_weight(self, variant: Variant) -> float:
        return self.variant.get(variant, 1.0)


@dataclass
class PositionTopDigit:
    variant: Variant
    position: PositionIndex
    digit: int
    rank: int
    gap: int
    gap_percentile: float
    lag_weight: float
    occurrence_count: int
    last_seen_index: Optional[int]
    score_components: Dict[str, float] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)

    def add_component(self, name: str, value: float, tag: Optional[str] = None) -> None:
        if not value:
            return
        self.score_components[name] = self.score_components.get(name, 0.0) + value
        if tag and tag not in self.tags:
            self.tags.append(tag)

    @property
    def score(self) -> float:
        return sum(self.score_components.values())


@dataclass
class PositionSummary:
    position: PositionIndex
    top_digits: List[PositionTopDigit]
    population: int
    window: int


@dataclass
class VariantPositionalResult:
    variant: Variant
    window: int
    draws_used: int
    position_summaries: Dict[PositionIndex, PositionSummary]
    tracker_grid: Dict[PositionIndex, List[PositionalTrackerCell]]

    def iter_top_digits(self) -> Iterable[PositionTopDigit]:
        for summary in self.position_summaries.values():
            for digit in summary.top_digits:
                yield digit


@dataclass
class AggregatedDigit:
    digit: int
    position: PositionIndex
    score: float
    occurrences: List[Tuple[Variant, int]]  # (variant, rank)
    tags: List[str] = field(default_factory=list)


@dataclass
class CandidateRecommendation:
    combo: str
    score: float
    ranks: Tuple[int, int, int]
    tags: List[str]
    digital_root: int
    vtrac_index: Optional[int]


@dataclass
class StatePositionalReport:
    variant_results: Dict[Variant, VariantPositionalResult]
    aggregated_digits: Dict[PositionIndex, List[AggregatedDigit]]
    consensus_notes: List[str]
    double_pressure_notes: List[str]
    candidates: List[CandidateRecommendation]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _normalize_draw(draw: str) -> Optional[str]:
    if not draw or len(draw) != 3:
        return None
    stripped = draw.strip()
    if len(stripped) != 3 or not stripped.isdigit():
        return None
    return stripped


def _build_position_stream(draws: List[str], position: PositionIndex, window: int) -> List[int]:
    limit = min(window, len(draws))
    stream: List[int] = []
    for idx in range(limit):
        val = draws[idx]
        if len(val) == 3 and val.isdigit():
            stream.append(int(val[position]))
    return stream


def _scan_intervals(stream: List[int], digit: int) -> List[int]:
    prev: Optional[int] = None
    intervals: List[int] = []
    for idx, value in enumerate(stream):
        if value == digit:
            if prev is not None:
                intervals.append(idx - prev)
            prev = idx
    return intervals


def _current_gap(stream: List[int], digit: int) -> Tuple[int, Optional[int]]:
    for idx, value in enumerate(stream):
        if value == digit:
            return idx, idx
    return len(stream), None


def _percentile(values: List[int], p: float, default: float) -> float:
    if not values:
        return default
    ordered = sorted(values)
    k = p * (len(ordered) - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(ordered[int(k)])
    return ordered[f] + (ordered[c] - ordered[f]) * (k - f)


def _recent_heat_tag(gap: int, recent_brake: int) -> Optional[str]:
    if recent_brake <= 0:
        return None
    if gap <= recent_brake:
        return f"Fresh({gap})"
    return None


def _digital_root(combo: str) -> int:
    total = sum(int(ch) for ch in combo)
    while total > 9:
        total = sum(int(ch) for ch in str(total))
    return total if total != 0 else 9


# ---------------------------------------------------------------------------
# Core positional analysis
# ---------------------------------------------------------------------------

def analyze_variant(
    draws_newest_first: List[str],
    variant: Variant,
    *,
    window: int = 150,
    topk: int = 3,
    weights: Optional[WeightsConfig] = None,
) -> VariantPositionalResult:
    """Compute positional pressure for a single variant (Combined/Midday/Evening).

    Returns newest-first statistics so callers can later fuse cross-variant signals."""
    cfg = weights or WeightsConfig()
    clean = [_normalize_draw(d) for d in draws_newest_first]
    clean = [d for d in clean if d is not None]
    if not clean:
        summaries = {pos: PositionSummary(pos, [], 0, window) for pos in (0, 1, 2)}
        return VariantPositionalResult(
            variant=variant, window=window, draws_used=0, position_summaries=summaries
        )

    summaries: Dict[PositionIndex, PositionSummary] = {}
    tracker_grid: Dict[PositionIndex, List[PositionalTrackerCell]] = {}
    variant_weight = cfg.variant_weight(variant)

    for pos in (0, 1, 2):
        stream = _build_position_stream(clean, pos, window)
        population = len(stream)
        if population == 0:
            summaries[pos] = PositionSummary(pos, [], population, window)
            continue

        digits: List[PositionTopDigit] = []
        for digit in range(10):
            gap, last_idx = _current_gap(stream, digit)
            intervals = _scan_intervals(stream, digit)
            if intervals:
                p75_gap = _percentile(intervals, 0.75, default=0.75 * population)
            else:
                p75_gap = 0.75 * population

            lag_weight = min(1.0, gap / max(cfg.lag_full_weight_at, 1.0))
            gap_percentile = gap / max(p75_gap + 1.0, 1.0)

            entry = PositionTopDigit(
                variant=variant,
                position=pos,
                digit=digit,
                rank=0,
                gap=gap,
                gap_percentile=float(gap_percentile),
                lag_weight=float(lag_weight),
                occurrence_count=len(intervals),
                last_seen_index=last_idx,
            )
            base = variant_weight * cfg.rank_weight(1) * max(lag_weight, 0.0)
            entry.score_components["base"] = base
            digits.append(entry)

        digits.sort(key=lambda item: (item.gap, item.digit), reverse=True)

        top_raw = digits[:topk]
        for idx, entry in enumerate(top_raw, start=1):
            entry.rank = idx
            base = variant_weight * cfg.rank_weight(idx) * max(entry.lag_weight, 0.0)
            entry.score_components["base"] = base
            entry.tags.append(f"R{idx}")
            fresh_tag = _recent_heat_tag(entry.gap, cfg.recent_heat_brake)
            if fresh_tag:
                entry.add_component("recent_brake", -0.2 * base, fresh_tag)
            else:
                entry.add_component("lag", 0.1 * base)

        digits_in_position = {e.digit: e for e in top_raw}
        for entry in top_raw:
            mirror_digit = MIRROR_MAP.get(entry.digit)
            if mirror_digit is None:
                continue
            friend = digits_in_position.get(mirror_digit)
            if friend is None:
                continue
            bonus = cfg.mirror_same_variant * friend.score_components.get("base", 0.0)
            entry.add_component("mirror_local", bonus, cfg.mirror_tag)

        tracker_grid[pos] = [
            PositionalTrackerCell(
                digit=entry.digit,
                draws_since=entry.gap,
                hard_due=entry.gap >= HARD_DUE_THRESHOLDS.get(variant, 55),
            )
            for entry in top_raw
        ]
        summaries[pos] = PositionSummary(
            position=pos, top_digits=top_raw, population=population, window=window
        )

    return VariantPositionalResult(
        variant=variant,
        window=window,
        draws_used=len(clean),
        position_summaries=summaries,
        tracker_grid=tracker_grid,
    )


def _collect_entries(results: Dict[Variant, VariantPositionalResult]) -> List[PositionTopDigit]:
    collected: List[PositionTopDigit] = []
    for result in results.values():
        collected.extend(list(result.iter_top_digits()))
    return collected


def _apply_cross_variant_consensus(entries: List[PositionTopDigit], cfg: WeightsConfig) -> List[str]:
    notes: List[str] = []
    by_pos_digit: Dict[Tuple[PositionIndex, int], List[PositionTopDigit]] = {}
    by_pos_mirror: Dict[Tuple[PositionIndex, int], List[PositionTopDigit]] = {}

    for entry in entries:
        key = (entry.position, entry.digit)
        by_pos_digit.setdefault(key, []).append(entry)
        mirror_key = (entry.position, MIRROR_MAP.get(entry.digit, entry.digit))
        by_pos_mirror.setdefault(mirror_key, []).append(entry)

    for key, group in by_pos_digit.items():
        if len(group) <= 1:
            continue
        bonus = cfg.consensus_exact * (len(group) - 1)
        pos, digit = key
        for entry in group:
            entry.add_component("consensus", bonus, cfg.consensus_tag)
        variants = ", ".join(sorted({g.variant.title() for g in group}))
        notes.append(f"P{pos + 1} digit {digit} aligns across {variants}")

    for key, group in by_pos_mirror.items():
        pos, pivot_digit = key
        unique_variants = {g.variant for g in group}
        if len(unique_variants) <= 1:
            continue
        bonus = cfg.consensus_mirror * (len(unique_variants) - 1)
        for entry in group:
            entry.add_component("mirror_consensus", bonus, cfg.mirror_tag)
        notes.append(f"P{pos + 1} mirror cluster around digit {pivot_digit}")

    return notes


def _apply_double_pressure(entries: List[PositionTopDigit], cfg: WeightsConfig, *, due_doubles_active: bool = False) -> List[str]:
    notes: List[str] = []
    exposures: Dict[int, List[PositionTopDigit]] = {d: [] for d in range(10)}
    for entry in entries:
        if entry.rank <= 2:
            exposures[entry.digit].append(entry)
    handled: set = set()
    for digit in range(10):
        items = list(exposures[digit])
        mirror_digit = MIRROR_MAP.get(digit)
        if mirror_digit is not None:
            items.extend(exposures.get(mirror_digit, []))
        unique_positions = {(item.variant, item.position) for item in items}
        if len(unique_positions) < 2:
            continue
        key = tuple(sorted(unique_positions))
        if key in handled:
            continue
        handled.add(key)
        for item in items:
            item.add_component("double", cfg.double_pressure, cfg.double_tag)
            if due_doubles_active:
                item.add_component("double_due", cfg.double_due_bonus, cfg.double_tag)
        variants = ", ".join(sorted({v for v, _ in unique_positions}))
        notes.append(f"Digit {digit} (mirror {mirror_digit}) pressuring two positions across {variants}")
    return notes


def _apply_swap_echo(entries: List[PositionTopDigit], cfg: WeightsConfig) -> None:
    for entry in entries:
        has_swap = False
        has_mirror_swap = False
        for candidate in entries:
            if candidate is entry:
                continue
            if candidate.variant == entry.variant:
                continue
            if abs(candidate.position - entry.position) != 1:
                continue
            if candidate.digit == entry.digit:
                has_swap = True
            elif MIRROR_MAP.get(candidate.digit) == entry.digit:
                has_mirror_swap = True
        if has_swap:
            entry.add_component("swap", cfg.swap_echo, cfg.swap_tag)
        elif has_mirror_swap:
            entry.add_component("swap_mirror", cfg.swap_echo_mirror, cfg.swap_tag)


def _aggregate_scores(entries: List[PositionTopDigit]) -> Dict[PositionIndex, Dict[int, AggregatedDigit]]:
    aggregated: Dict[PositionIndex, Dict[int, AggregatedDigit]] = {0: {}, 1: {}, 2: {}}
    for entry in entries:
        bucket = aggregated[entry.position]
        agg = bucket.get(entry.digit)
        if agg is None:
            agg = AggregatedDigit(
                digit=entry.digit,
                position=entry.position,
                score=0.0,
                occurrences=[],
                tags=list(entry.tags),
            )
            bucket[entry.digit] = agg
        agg.score += entry.score
        agg.occurrences.append((entry.variant, entry.rank))
        for tag in entry.tags:
            if tag not in agg.tags:
                agg.tags.append(tag)
    return aggregated


def _build_candidates(
    aggregated: Dict[PositionIndex, Dict[int, AggregatedDigit]],
    entries: List[PositionTopDigit],
    cfg: WeightsConfig,
) -> List[CandidateRecommendation]:
    import itertools

    position_digits: Dict[PositionIndex, List[AggregatedDigit]] = {}
    for pos, digit_map in aggregated.items():
        ranked = sorted(digit_map.values(), key=lambda item: (item.score, -item.digit), reverse=True)
        position_digits[pos] = ranked[: cfg.max_candidate_per_position]

    if not all(position_digits.values()):
        return []

    combos: List[CandidateRecommendation] = []
    for choice in itertools.product(position_digits[0], position_digits[1], position_digits[2]):
        digits = [item.digit for item in choice]
        combo = f"{digits[0]}{digits[1]}{digits[2]}"
        score = sum(item.score for item in choice)
        ranks: List[int] = []
        tags: List[str] = []
        top1_count = 0
        for agg in choice:
            for _, rank in agg.occurrences:
                ranks.append(rank)
                if rank == 1:
                    top1_count += 1
            tags.extend(agg.tags)
        if top1_count >= 2:
            score += 0.5
            tags.append(f"TOP1x{top1_count}")

        digital_root = _digital_root(combo)
        vtrac_idx: Optional[int] = None
        if callable(get_vtrac_index):  # pragma: no cover - relies on staged module
            try:
                vtrac_idx = int(get_vtrac_index(combo))
            except Exception:
                vtrac_idx = None
        candidate = CandidateRecommendation(
            combo=combo,
            score=float(score),
            ranks=(ranks[0] if len(ranks) > 0 else 0, ranks[1] if len(ranks) > 1 else 0, ranks[2] if len(ranks) > 2 else 0),
            tags=sorted(set(tags)),
            digital_root=digital_root,
            vtrac_index=vtrac_idx,
        )
        combos.append(candidate)

    combos.sort(key=lambda c: (c.score, -c.digital_root, c.combo), reverse=True)
    return combos[: cfg.max_candidates]


def analyze_state_variants(
    draws_by_variant: Dict[Variant, List[str]],
    *,
    window: int = 150,
    topk: int = 3,
    weights: Optional[WeightsConfig] = None,
    due_doubles_active: bool = False,
) -> StatePositionalReport:
    cfg = weights or WeightsConfig()
    variant_results: Dict[Variant, VariantPositionalResult] = {}
    for variant, draws in draws_by_variant.items():
        variant_results[variant] = analyze_variant(draws, variant, window=window, topk=topk, weights=cfg)

    entries = _collect_entries(variant_results)
    consensus_notes = _apply_cross_variant_consensus(entries, cfg)
    double_notes = _apply_double_pressure(entries, cfg, due_doubles_active=due_doubles_active)
    if double_notes:
        consensus_notes.extend(double_notes)
    _apply_swap_echo(entries, cfg)

    aggregated = _aggregate_scores(entries)
    candidates = _build_candidates(aggregated, entries, cfg)

    sorted_aggregated: Dict[PositionIndex, List[AggregatedDigit]] = {}
    for pos, digit_map in aggregated.items():
        sorted_aggregated[pos] = sorted(digit_map.values(), key=lambda item: (item.score, -item.digit), reverse=True)

    return StatePositionalReport(
        variant_results=variant_results,
        aggregated_digits=sorted_aggregated,
        consensus_notes=consensus_notes,
        double_pressure_notes=double_notes,
        candidates=candidates,
    )


__all__ = [
    "WeightsConfig",
    "PositionTopDigit",
    "PositionSummary",
    "VariantPositionalResult",
    "PositionalTrackerCell",
    "AggregatedDigit",
    "CandidateRecommendation",
    "StatePositionalReport",
    "analyze_variant",
    "analyze_state_variants",
]
