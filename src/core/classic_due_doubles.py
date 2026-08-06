"""Pure calculations for the human-readable classic due-doubles table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

from .aux_config import (
    COMBINATION_WINDOW,
    COMBO_DOUBLE_VERY_LATE,
    PAIRS_WINDOW,
    PAIR_PENDING,
    REPEATING_LATE,
    REPEATING_VERY_LATE,
)

VARIANT_ORDER = ("combined", "midday", "evening")
VARIANT_BADGES = {"combined": "C", "midday": "M", "evening": "E"}
VARIANT_LABELS = {"combined": "Combined", "midday": "Midday", "evening": "Evening"}


@dataclass(frozen=True)
class VariantCoverage:
    variant: str
    badge: str
    draws_used: int
    red_eligible: bool


@dataclass(frozen=True)
class RedBoxEntry:
    combo: str
    variant: str
    badge: str
    draws_since: int
    unseen: bool


@dataclass(frozen=True)
class DuePairSlot:
    rank: int
    pair: str
    draws_since: int
    band: str
    red_boxes: tuple[RedBoxEntry, ...]


@dataclass(frozen=True)
class ClassicDueDoublesReview:
    state: str
    pair_window: int
    combination_window: int
    red_threshold: int
    pair_slots: tuple[DuePairSlot, ...]
    closure: tuple[str, ...]
    coverage: tuple[VariantCoverage, ...]

    @property
    def red_badges_by_combo(self) -> dict[str, tuple[str, ...]]:
        return dict(
            group_red_box_entries(
                entry
                for slot in self.pair_slots
                for entry in slot.red_boxes
            )
        )


@dataclass(frozen=True)
class _VariantSnapshot:
    coverage: VariantCoverage
    first_seen: Mapping[str, int]


def canonical_box(value: str) -> str:
    """Return the canonical three-digit box, or an empty string when invalid."""
    draw = str(value or "").strip()
    if len(draw) != 3 or not draw.isdigit():
        return ""
    return "".join(sorted(draw))


def group_red_box_entries(
    entries: Iterable[RedBoxEntry],
) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """Group source-specific red entries by canonical box."""
    badges: dict[str, set[str]] = {}
    for entry in entries:
        badges.setdefault(entry.combo, set()).add(entry.badge)
    badge_order = {badge: index for index, badge in enumerate(("C", "M", "E"))}
    return tuple(
        (
            combo,
            tuple(sorted(values, key=lambda badge: badge_order.get(badge, 99))),
        )
        for combo, values in sorted(badges.items())
    )


def pair_band(draws_since: int) -> str:
    if draws_since >= REPEATING_VERY_LATE:
        return "RED"
    if draws_since >= REPEATING_LATE:
        return "BLUE"
    if draws_since >= PAIR_PENDING:
        return "PURPLE"
    return "TOP-4"


def rank_due_repeating_pairs(
    draws: Sequence[str],
    *,
    window: int = PAIRS_WINDOW,
    limit: int = 4,
) -> tuple[tuple[str, int], ...]:
    """Rank repeated pairs from newest-first Combined draws."""
    history = list(draws[:window]) if window > 0 else list(draws)
    if not history:
        return ()
    first_seen: dict[str, int] = {}
    for index, raw_draw in enumerate(history):
        draw = str(raw_draw or "").strip()
        if len(draw) != 3 or not draw.isdigit():
            continue
        for digit in set(draw):
            if draw.count(digit) >= 2:
                first_seen.setdefault(digit * 2, index)

    default_gap = len(history)
    ranked = [
        (str(digit) * 2, first_seen.get(str(digit) * 2, default_gap))
        for digit in range(10)
    ]
    ranked.sort(key=lambda item: (-item[1], item[0]))
    return tuple(ranked[: max(0, limit)])


def double_boxes_for_pair(pair: str) -> tuple[str, ...]:
    """Return the nine canonical double boxes associated with a repeated pair."""
    value = str(pair or "").strip()
    if len(value) != 2 or not value.isdigit() or value[0] != value[1]:
        return ()
    repeated = value[0]
    return tuple(
        sorted(
            canonical_box(repeated * 2 + singleton)
            for singleton in "0123456789"
            if singleton != repeated
        )
    )


def build_due_pair_boxed_closure(pairs: Sequence[str]) -> tuple[str, ...]:
    """Build unique boxes using one due digit twice and another due digit once."""
    digits: list[str] = []
    for pair in pairs:
        value = str(pair or "").strip()
        if (
            len(value) == 2
            and value.isdigit()
            and value[0] == value[1]
            and value[0] not in digits
        ):
            digits.append(value[0])

    closure = {
        canonical_box(repeated * 2 + singleton)
        for repeated in digits
        for singleton in digits
        if singleton != repeated
    }
    closure.discard("")
    return tuple(sorted(closure))


def _variant_snapshot(
    variant: str,
    draws: Sequence[str],
    *,
    combination_window: int,
    red_threshold: int,
) -> _VariantSnapshot:
    valid_history = [
        str(draw).strip()
        for draw in draws
        if len(str(draw).strip()) == 3 and str(draw).strip().isdigit()
    ][:combination_window]
    first_seen: dict[str, int] = {}
    for index, draw in enumerate(valid_history):
        canonical = canonical_box(draw)
        if canonical:
            first_seen.setdefault(canonical, index)
    badge = VARIANT_BADGES.get(variant, variant[:1].upper())
    return _VariantSnapshot(
        coverage=VariantCoverage(
            variant=variant,
            badge=badge,
            draws_used=len(valid_history),
            red_eligible=len(valid_history) >= red_threshold,
        ),
        first_seen=first_seen,
    )


def build_classic_due_doubles_review(
    state: str,
    variant_draws: Mapping[str, Sequence[str]],
    *,
    pair_window: int = PAIRS_WINDOW,
    pair_limit: int = 4,
    combination_window: int = COMBINATION_WINDOW,
    red_threshold: int = COMBO_DOUBLE_VERY_LATE,
) -> ClassicDueDoublesReview:
    """Build one state's classic top-pair and red-box review."""
    ranked_pairs = rank_due_repeating_pairs(
        variant_draws.get("combined", ()),
        window=pair_window,
        limit=pair_limit,
    )
    snapshots = {
        variant: _variant_snapshot(
            variant,
            variant_draws.get(variant, ()),
            combination_window=combination_window,
            red_threshold=red_threshold,
        )
        for variant in VARIANT_ORDER
        if variant in variant_draws
    }

    slots: list[DuePairSlot] = []
    variant_rank = {variant: index for index, variant in enumerate(VARIANT_ORDER)}
    for rank, (pair, draws_since) in enumerate(ranked_pairs, start=1):
        red_entries: list[RedBoxEntry] = []
        for combo in double_boxes_for_pair(pair):
            for variant, snapshot in snapshots.items():
                if not snapshot.coverage.red_eligible:
                    continue
                gap = snapshot.first_seen.get(combo, snapshot.coverage.draws_used)
                if gap < red_threshold:
                    continue
                red_entries.append(
                    RedBoxEntry(
                        combo=combo,
                        variant=variant,
                        badge=snapshot.coverage.badge,
                        draws_since=gap,
                        unseen=combo not in snapshot.first_seen,
                    )
                )
        red_entries.sort(key=lambda entry: (entry.combo, variant_rank.get(entry.variant, 99)))
        slots.append(
            DuePairSlot(
                rank=rank,
                pair=pair,
                draws_since=draws_since,
                band=pair_band(draws_since),
                red_boxes=tuple(red_entries),
            )
        )

    return ClassicDueDoublesReview(
        state=state,
        pair_window=pair_window,
        combination_window=combination_window,
        red_threshold=red_threshold,
        pair_slots=tuple(slots),
        closure=build_due_pair_boxed_closure([slot.pair for slot in slots]),
        coverage=tuple(
            snapshots[variant].coverage
            for variant in VARIANT_ORDER
            if variant in snapshots
        ),
    )


__all__ = [
    "ClassicDueDoublesReview",
    "DuePairSlot",
    "RedBoxEntry",
    "VARIANT_BADGES",
    "VARIANT_LABELS",
    "VariantCoverage",
    "build_classic_due_doubles_review",
    "build_due_pair_boxed_closure",
    "canonical_box",
    "double_boxes_for_pair",
    "group_red_box_entries",
    "pair_band",
    "rank_due_repeating_pairs",
]
