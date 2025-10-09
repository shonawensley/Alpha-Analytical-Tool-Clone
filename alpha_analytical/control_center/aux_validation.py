"""Validation helpers for Aux double/draw metrics."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

import sys

try:
    from core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
    from core.vtrac_families import VTRAC_DOUBLE_FAMILIES
except ModuleNotFoundError:
    ROOT = Path(__file__).resolve().parents[2]
    SRC = ROOT / "src"
    if SRC.exists() and str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    from core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
    from core.vtrac_families import VTRAC_DOUBLE_FAMILIES

from modules.aux_loaders import load_state_draws

VARIANTS: Sequence[str] = ("combined", "midday", "evening")


def _canonical(combo: str) -> str:
    value = (combo or "").strip()
    if len(value) != 3 or not value.isdigit():
        return ""
    return "".join(sorted(value))


def _classify_gap(draws_since: int) -> str | None:
    if draws_since >= COMBO_DOUBLE_VERY_LATE:
        return "R"
    if draws_since >= COMBO_DOUBLE_LATE:
        return "B"
    return None


def compute_double_stats(draws: Sequence[str]) -> Dict[str, Dict[str, int]]:
    """Return draws-since + severity for each canonical double in the stream."""
    if not draws:
        return {}
    default_gap = len(draws)
    gap_map: Dict[str, int] = defaultdict(lambda: default_gap)
    for idx, draw in enumerate(draws):
        canon = _canonical(draw)
        if canon and gap_map[canon] == default_gap:
            gap_map[canon] = idx
    result: Dict[str, Dict[str, int]] = {}
    for combo, gap in gap_map.items():
        severity = _classify_gap(gap)
        if severity:
            result[combo] = {"draws_since": gap, "severity": severity}
    return result


def load_variant_draws(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, List[str]]:
    data: Dict[str, List[str]] = {}
    for variant in VARIANTS:
        draws, _ = load_state_draws(state, variant=variant, base=base, max_n=max_n)
        data[variant] = draws
    return data


def collect_variant_stats(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    stats = {variant: compute_double_stats(draws) for variant, draws in draws_by_variant.items() if draws}
    return stats


def combos_flagged_by_variant(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    return collect_variant_stats(state, base=base, max_n=max_n)


def multi_variant_alerts(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    stats = collect_variant_stats(state, base=base, max_n=max_n)
    alerts: Dict[str, Dict[str, Dict[str, int]]] = {}
    all_combos = set(combo for variant_stats in stats.values() for combo in variant_stats.keys())
    for combo in sorted(all_combos):
        flags = {variant: variant_stats[combo] for variant, variant_stats in stats.items() if combo in variant_stats}
        if len(flags) > 1:
            alerts[combo] = flags
    return alerts


def family_badge_matrix(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    """Map each family label to combos/variant stats used in the Control Center."""
    stats = collect_variant_stats(state, base=base, max_n=max_n)
    families: Dict[str, Dict[str, Dict[str, int]]] = {}
    for family in VTRAC_DOUBLE_FAMILIES:
        fam_data: Dict[str, Dict[str, int]] = {}
        for variant, variant_stats in stats.items():
            for combo in family.combos:
                if combo in variant_stats:
                    key = f"{combo}:{variant}"
                    fam_data[key] = variant_stats[combo]
        if fam_data:
            families[family.label] = fam_data
    return families
