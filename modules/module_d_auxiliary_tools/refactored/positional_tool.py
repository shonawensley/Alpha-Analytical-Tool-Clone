from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple
import itertools
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

try:
    from core.aux_config import POS_SHORTLIST_CONFIG  # type: ignore
except Exception:  # pragma: no cover
    POS_SHORTLIST_CONFIG = None  # type: ignore

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
    mirror_tag: str = "Mirror-Echo"
    consensus_tag: str = "XVAR-Cons"
    double_tag: str = "Double-Pressure"
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


@dataclass(frozen=True)
class ShortlistCaps:
    cartesian: int
    repeat_endcap: int
    lane: int


@dataclass(frozen=True)
class ShortlistWeights:
    rank: float
    xvar: float
    mirror_echo: float
    double_pressure: float
    repeat_endcap: float
    lane_concordance: float
    root: float
    vtrac_index: float
    vtrac_family: float


@dataclass(frozen=True)
class ShortlistFeatures:
    enable_repeat_endcap: bool
    enable_lane_concordance: bool
    enable_vtrac_boosts: bool


@dataclass(frozen=True)
class ShortlistConfig:
    topk_per_pos: int
    pool_per_pos: int
    max_internal: int
    max_rows: int
    caps: ShortlistCaps
    weights: ShortlistWeights
    features: ShortlistFeatures

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "ShortlistConfig":
        caps_map = data.get("caps", {})
        weights_map = data.get("weights", {})
        features_map = data.get("features", {})
        caps = ShortlistCaps(
            cartesian=int(caps_map.get("cartesian", 48)),
            repeat_endcap=int(caps_map.get("repeat_endcap", 36)),
            lane=int(caps_map.get("lane", 36)),
        )
        weights = ShortlistWeights(
            rank=float(weights_map.get("rank", 1.0)),
            xvar=float(weights_map.get("xvar", 2.5)),
            mirror_echo=float(weights_map.get("mirror_echo", 1.0)),
            double_pressure=float(weights_map.get("double_pressure", 1.0)),
            repeat_endcap=float(weights_map.get("repeat_endcap", 0.3)),
            lane_concordance=float(weights_map.get("lane_concordance", 0.15)),
            root=float(weights_map.get("root", 0.0)),
            vtrac_index=float(weights_map.get("vtrac_index", 0.8)),
            vtrac_family=float(weights_map.get("vtrac_family", 0.6)),
        )
        features = ShortlistFeatures(
            enable_repeat_endcap=bool(features_map.get("enable_repeat_endcap", True)),
            enable_lane_concordance=bool(features_map.get("enable_lane_concordance", True)),
            enable_vtrac_boosts=bool(features_map.get("enable_vtrac_boosts", True)),
        )
        return ShortlistConfig(
            topk_per_pos=int(data.get("topk_per_pos", 3)),
            pool_per_pos=int(data.get("pool_per_pos", 6)),
            max_internal=int(data.get("max_internal", 64)),
            max_rows=int(data.get("max_rows", 16)),
            caps=caps,
            weights=weights,
            features=features,
        )


@dataclass(frozen=True)
class CandidateSeed:
    digits: Tuple[int, int, int]
    source: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CandidateRecommendation:
    combo: str
    score: float
    ranks: Tuple[int, int, int]
    tags: List[str]
    digital_root: int
    vtrac_index: Optional[int]
    evidence: List[str] = field(default_factory=list)
    source: str = ""


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
        variant_letters = "".join(sorted({g.variant[0].upper() for g in group}))
        tag_value = f"{cfg.consensus_tag}({variant_letters})" if variant_letters else cfg.consensus_tag
        for entry in group:
            entry.add_component("consensus", bonus, tag_value)
        variants = ", ".join(sorted({g.variant.title() for g in group}))
        notes.append(f"P{pos + 1} digit {digit} aligns across {variants} ({tag_value})")

    for key, group in by_pos_mirror.items():
        pos, pivot_digit = key
        unique_variants = {g.variant for g in group}
        if len(unique_variants) <= 1:
            continue
        bonus = cfg.consensus_mirror * (len(unique_variants) - 1)
        variant_letters = "".join(sorted({g.variant[0].upper() for g in group}))
        mirror_tag_value = f"{cfg.mirror_tag}({variant_letters})" if variant_letters else cfg.mirror_tag
        for entry in group:
            entry.add_component("mirror_consensus", bonus, mirror_tag_value)
        notes.append(f"P{pos + 1} mirror cluster around digit {pivot_digit} ({mirror_tag_value})")

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
        mirror_label = f" (mirror {mirror_digit})" if mirror_digit is not None else ""
        notes.append(f"Digit {digit}{mirror_label} pressuring two positions across {variants} ({cfg.double_tag})")
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


def _collect_digit_variants(entries: List[PositionTopDigit]) -> Dict[PositionIndex, Dict[int, Set[Variant]]]:
    mapping: Dict[PositionIndex, Dict[int, Set[Variant]]] = {0: {}, 1: {}, 2: {}}
    for entry in entries:
        slot = mapping[entry.position].setdefault(entry.digit, set())
        slot.add(entry.variant)
    return mapping


def _collect_lane_hits(
    variant_results: Dict[Variant, VariantPositionalResult],
    topk: int,
) -> Dict[Variant, Dict[PositionIndex, List[int]]]:
    lane_hits: Dict[Variant, Dict[PositionIndex, List[int]]] = {}
    for variant, result in variant_results.items():
        lane_hits[variant] = {}
        for pos in (0, 1, 2):
            summary = result.position_summaries.get(pos)
            digits: List[int] = []
            if summary:
                digits = [digit_entry.digit for digit_entry in summary.top_digits[:topk]]
            lane_hits[variant][pos] = digits
    return lane_hits


def _build_union_pool(
    aggregated_sorted: Dict[PositionIndex, List[AggregatedDigit]],
    cfg: ShortlistConfig,
) -> Dict[PositionIndex, List[AggregatedDigit]]:
    pool: Dict[PositionIndex, List[AggregatedDigit]] = {}
    for pos, items in aggregated_sorted.items():
        selected: List[AggregatedDigit] = []
        seen: Set[int] = set()
        for agg in items:
            if agg.digit in seen:
                continue
            seen.add(agg.digit)
            selected.append(agg)
            if len(selected) >= cfg.pool_per_pos:
                break
        pool[pos] = selected
    return pool


def _generate_cartesian_seeds(
    pool: Dict[PositionIndex, List[AggregatedDigit]],
    limit: int,
) -> List[CandidateSeed]:
    seeds: List[CandidateSeed] = []
    if limit <= 0:
        return seeds
    for agg0 in pool.get(0, []):
        for agg1 in pool.get(1, []):
            for agg2 in pool.get(2, []):
                seeds.append(CandidateSeed((agg0.digit, agg1.digit, agg2.digit), "cartesian"))
                if len(seeds) >= limit:
                    return seeds
    return seeds


def _generate_repeat_endcap_seeds(
    pool: Dict[PositionIndex, List[AggregatedDigit]],
    aggregated_map: Dict[PositionIndex, Dict[int, AggregatedDigit]],
    digit_variants: Dict[PositionIndex, Dict[int, Set[Variant]]],
    lane_hits: Dict[Variant, Dict[PositionIndex, List[int]]],
    cfg: ShortlistConfig,
    limit: int,
) -> List[CandidateSeed]:
    seeds: List[CandidateSeed] = []
    if limit <= 0:
        return seeds
    shared: List[Tuple[int, float]] = []
    for agg0 in pool.get(0, []):
        digit = agg0.digit
        agg2 = aggregated_map[2].get(digit)
        if agg2 is None:
            continue
        shared.append((digit, agg0.score + agg2.score))
    shared.sort(key=lambda item: item[1], reverse=True)
    for digit, _score in shared:
        lanes = set()
        lanes.update(digit_variants[0].get(digit, set()))
        lanes.update(digit_variants[2].get(digit, set()))
        bridge_candidates: List[Tuple[int, float]] = []
        seen: Set[int] = set()
        for agg in pool.get(1, []):
            if agg.digit in seen:
                continue
            bridge_candidates.append((agg.digit, agg.score))
            seen.add(agg.digit)
        for lane in lanes:
            for candidate_digit in lane_hits.get(lane, {}).get(1, []):
                if candidate_digit in seen:
                    continue
                agg = aggregated_map[1].get(candidate_digit)
                if agg is None:
                    continue
                bridge_candidates.append((candidate_digit, agg.score))
                seen.add(candidate_digit)
        bridge_candidates.sort(key=lambda item: item[1], reverse=True)
        for bridge_digit, _ in bridge_candidates[: cfg.pool_per_pos]:
            seeds.append(
                CandidateSeed(
                    (digit, bridge_digit, digit),
                    "repeat_endcap",
                    metadata={"lanes": sorted(lanes)},
                )
            )
            if len(seeds) >= limit:
                return seeds
    return seeds


def _generate_lane_concordance_seeds(
    aggregated_map: Dict[PositionIndex, Dict[int, AggregatedDigit]],
    lane_hits: Dict[Variant, Dict[PositionIndex, List[int]]],
    cfg: ShortlistConfig,
    limit: int,
) -> List[CandidateSeed]:
    seeds: List[CandidateSeed] = []
    if limit <= 0:
        return seeds
    for lane, pos_map in lane_hits.items():
        lane_lists: List[List[int]] = []
        for pos in (0, 1, 2):
            digits: List[Tuple[int, float]] = []
            for digit in pos_map.get(pos, []):
                agg = aggregated_map[pos].get(digit)
                if agg is None:
                    continue
                digits.append((digit, agg.score))
            if not digits:
                lane_lists = []
                break
            digits.sort(key=lambda item: item[1], reverse=True)
            lane_lists.append([val for val, _ in digits[: cfg.pool_per_pos]])
        if not lane_lists or len(lane_lists) != 3:
            continue
        for combo in itertools.product(*lane_lists):
            seeds.append(CandidateSeed(tuple(combo), "lane", metadata={"lane": lane}))
            if len(seeds) >= limit:
                return seeds
    return seeds


def _merge_nested(base: Mapping[str, Any], override: Mapping[str, Any], key: str) -> Dict[str, Any]:
    result = dict(base.get(key, {})) if isinstance(base.get(key, {}), Mapping) else dict()
    updates = override.get(key, {}) if isinstance(override.get(key, {}), Mapping) else {}
    result.update(updates)
    return result


def _load_shortlist_config(user_cfg: Optional[Mapping[str, Any]]) -> ShortlistConfig:
    base_mapping: Mapping[str, Any] = POS_SHORTLIST_CONFIG or {}
    override = user_cfg or {}
    merged = dict(base_mapping)
    merged.update(override)
    merged['caps'] = _merge_nested(base_mapping, override, 'caps')
    merged['weights'] = _merge_nested(base_mapping, override, 'weights')
    merged['features'] = _merge_nested(base_mapping, override, 'features')
    return ShortlistConfig.from_mapping(merged)


def _score_candidate_seed(
    seed: CandidateSeed,
    aggregated_map: Dict[PositionIndex, Dict[int, AggregatedDigit]],
    digit_variants: Dict[PositionIndex, Dict[int, Set[Variant]]],
    cfg: ShortlistConfig,
    vtrac_hot_indices: Set[int],
    vtrac_hot_families: Dict[str, str],
) -> Optional[CandidateRecommendation]:
    digits = seed.digits
    combo = f"{digits[0]}{digits[1]}{digits[2]}"
    total = 0.0
    tags: Set[str] = set()
    evidence: List[str] = []
    ranks: List[int] = []
    weights = cfg.weights
    features = cfg.features
    for pos, digit in enumerate(digits):
        agg = aggregated_map[pos].get(digit)
        if agg is None:
            return None
        total += weights.rank * agg.score
        occ = sorted(f"{variant[:1].upper()}#{rank}" for variant, rank in agg.occurrences)
        ranks.extend(rank for _, rank in agg.occurrences)
        lane_marks = digit_variants[pos].get(digit, set())
        if lane_marks:
            total += weights.xvar * len(lane_marks)
        descriptor = f"P{pos + 1}:{digit}"
        if occ:
            descriptor += f" [{', '.join(occ)}]"
        if lane_marks:
            descriptor += f" | lanes {'/'.join(sorted(v[:1].upper() for v in lane_marks))}"
        evidence.append(descriptor)
        for tag in agg.tags:
            tags.add(tag)
        if 'Mirror-Echo' in agg.tags:
            total += weights.mirror_echo
        if 'Double-Pressure' in agg.tags:
            total += weights.double_pressure
    if digits[0] == digits[2]:
        bonus = weights.repeat_endcap * (
            aggregated_map[0][digits[0]].score + aggregated_map[2][digits[2]].score
        )
        total += bonus
        tags.add('Repeat-Endcap')
        lanes = seed.metadata.get('lanes')
        if lanes:
            evidence.append(f"Repeat endcap lanes: {'/'.join(lanes)}")
        else:
            evidence.append("Repeat endcap")
    lane_label = seed.metadata.get('lane')
    if lane_label:
        lane_bonus = weights.lane_concordance * (
            aggregated_map[0][digits[0]].score
            + aggregated_map[1][digits[1]].score
            + aggregated_map[2][digits[2]].score
        )
        total += lane_bonus
        tags.add(f"Lane-{str(lane_label)[:1].upper()}")
        evidence.append(f"Lane concordance: {lane_label}")
    digital_root = _digital_root(combo)
    if weights.root:
        root_bonus = weights.root * (9 - digital_root) / 9.0
        if root_bonus:
            total += root_bonus
            evidence.append(f"Root bonus ({digital_root})")
    vtrac_idx: Optional[int] = None
    if callable(get_vtrac_index):  # pragma: no cover
        try:
            vtrac_idx = int(get_vtrac_index(combo))
        except Exception:
            vtrac_idx = None
    if features.enable_vtrac_boosts and vtrac_idx is not None:
        if vtrac_idx in vtrac_hot_indices:
            total += weights.vtrac_index
            tags.add('VTRAC-Hot')
            evidence.append(f"V-TRAC idx {vtrac_idx} hot")
    if features.enable_vtrac_boosts:
        canonical = ''.join(sorted(combo))
        family_label = vtrac_hot_families.get(canonical)
        if family_label:
            total += weights.vtrac_family
            tags.add(f"Family-{family_label}")
            evidence.append(f"Family {family_label} hot")
    ranks_tuple = (
        ranks[0] if len(ranks) > 0 else 0,
        ranks[1] if len(ranks) > 1 else 0,
        ranks[2] if len(ranks) > 2 else 0,
    )
    return CandidateRecommendation(
        combo=combo,
        score=float(total),
        ranks=ranks_tuple,
        tags=sorted(tags),
        digital_root=digital_root,
        vtrac_index=vtrac_idx,
        evidence=evidence,
        source=seed.source,
    )


def _build_shortlist_candidates(
    aggregated_sorted: Dict[PositionIndex, List[AggregatedDigit]],
    aggregated_map: Dict[PositionIndex, Dict[int, AggregatedDigit]],
    digit_variants: Dict[PositionIndex, Dict[int, Set[Variant]]],
    lane_hits: Dict[Variant, Dict[PositionIndex, List[int]]],
    cfg: ShortlistConfig,
    vtrac_hot_indices: Set[int],
    vtrac_hot_families: Dict[str, str],
) -> List[CandidateRecommendation]:
    if not aggregated_sorted or not all(aggregated_sorted.values()):
        return []
    pool = _build_union_pool(aggregated_sorted, cfg)
    if not all(pool.values()):
        return []
    seeds: List[CandidateSeed] = []
    remaining = cfg.max_internal

    def extend_with(new_seeds: List[CandidateSeed]) -> None:
        nonlocal remaining
        for seed in new_seeds:
            if remaining <= 0:
                break
            seeds.append(seed)
            remaining -= 1

    extend_with(_generate_cartesian_seeds(pool, min(cfg.caps.cartesian, remaining)))
    if cfg.features.enable_repeat_endcap and remaining > 0:
        extend_with(
            _generate_repeat_endcap_seeds(
                pool,
                aggregated_map,
                digit_variants,
                lane_hits,
                cfg,
                min(cfg.caps.repeat_endcap, remaining),
            )
        )
    if cfg.features.enable_lane_concordance and remaining > 0:
        extend_with(
            _generate_lane_concordance_seeds(
                aggregated_map,
                lane_hits,
                cfg,
                min(cfg.caps.lane, remaining),
            )
        )

    best: Dict[str, CandidateRecommendation] = {}
    for seed in seeds:
        candidate = _score_candidate_seed(
            seed,
            aggregated_map,
            digit_variants,
            cfg,
            vtrac_hot_indices,
            vtrac_hot_families,
        )
        if candidate is None:
            continue
        existing = best.get(candidate.combo)
        if existing is None or candidate.score > existing.score:
            best[candidate.combo] = candidate
    shortlist = sorted(
        best.values(),
        key=lambda item: (item.score, -item.digital_root, item.combo),
        reverse=True,
    )
    return shortlist[: cfg.max_rows]


def analyze_state_variants(
    draws_by_variant: Dict[Variant, List[str]],
    *,
    window: int = 150,
    topk: int = 3,
    weights: Optional[WeightsConfig] = None,
    due_doubles_active: bool = False,
    shortlist_cfg: Optional[Mapping[str, Any]] = None,
    vtrac_hot_indices: Optional[Iterable[int]] = None,
    vtrac_hot_families: Optional[Mapping[str, str]] = None,
) -> StatePositionalReport:
    cfg = weights or WeightsConfig()
    shortlist_config = _load_shortlist_config(shortlist_cfg)
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
    aggregated_map: Dict[PositionIndex, Dict[int, AggregatedDigit]] = {
        pos: dict(digit_map) for pos, digit_map in aggregated.items()
    }
    sorted_aggregated: Dict[PositionIndex, List[AggregatedDigit]] = {}
    for pos, digit_map in aggregated_map.items():
        sorted_aggregated[pos] = sorted(
            digit_map.values(),
            key=lambda item: (item.score, -item.digit),
            reverse=True,
        )

    digit_variants = _collect_digit_variants(entries)
    lane_hits = _collect_lane_hits(variant_results, shortlist_config.topk_per_pos)
    hot_indices = set(vtrac_hot_indices or [])
    hot_families = dict(vtrac_hot_families or {})

    candidates = _build_shortlist_candidates(
        sorted_aggregated,
        aggregated_map,
        digit_variants,
        lane_hits,
        shortlist_config,
        hot_indices,
        hot_families,
    )

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
    "ShortlistConfig",
    "StatePositionalReport",
    "analyze_variant",
    "analyze_state_variants",
]
