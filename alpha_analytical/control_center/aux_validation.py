"""Validation helpers for Aux double/draw metrics."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

import sys

try:
    from core.aux_config import (
        COMBO_DOUBLE_LATE,
        COMBO_DOUBLE_VERY_LATE,
        PAIRS_WINDOW,
        REPEATING_LATE,
        REPEATING_VERY_LATE,
        NONREPEATING_LATE,
        NONREPEATING_VERY_LATE,
        PAIR_PENDING,
        VTRAC_INDEX_WINDOW,
        POSITIONAL_WINDOW,
        POS_SHORTLIST_CONFIG,
    )
    from core.vtrac_families import VTRAC_DOUBLE_FAMILIES
except ModuleNotFoundError:
    ROOT = Path(__file__).resolve().parents[2]
    SRC = ROOT / "src"
    if SRC.exists() and str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    from core.aux_config import (
        COMBO_DOUBLE_LATE,
        COMBO_DOUBLE_VERY_LATE,
        PAIRS_WINDOW,
        REPEATING_LATE,
        REPEATING_VERY_LATE,
        NONREPEATING_LATE,
        NONREPEATING_VERY_LATE,
        PAIR_PENDING,
        VTRAC_INDEX_WINDOW,
        POSITIONAL_WINDOW,
        POS_SHORTLIST_CONFIG,
    )
    from core.vtrac_families import VTRAC_DOUBLE_FAMILIES

from modules.aux_loaders import load_state_draws

try:
    from modules.vtrac_reference import get_vtrac_index  # type: ignore
except Exception:  # pragma: no cover - staged Aux path may not resolve during tests
    ROOT = Path(__file__).resolve().parents[2]
    SRC = ROOT / "src"
    if SRC.exists() and str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    try:
        from modules.vtrac_reference import get_vtrac_index  # type: ignore
    except Exception:  # pragma: no cover
        get_vtrac_index = None  # type: ignore

try:
    from modules.module_d_auxiliary_tools.refactored.positional_tool import analyze_variant, analyze_state_variants  # type: ignore
except Exception:  # pragma: no cover
    analyze_variant = None  # type: ignore
    analyze_state_variants = None  # type: ignore

VARIANTS: Sequence[str] = ("combined", "midday", "evening")

COLOR_LATE = "red"
COLOR_VERY_LATE = "blue"
COLOR_PENDING = "purple"


def _percentile(sorted_values: Sequence[int], quantile: float) -> float | None:
    if not sorted_values:
        return None
    if quantile <= 0:
        return float(sorted_values[0])
    if quantile >= 1:
        return float(sorted_values[-1])
    pos = (len(sorted_values) - 1) * quantile
    lower = int(pos // 1)
    upper = int(-(-pos // 1))
    if lower == upper:
        return float(sorted_values[lower])
    lower_val = sorted_values[lower]
    upper_val = sorted_values[upper]
    return float(lower_val + (upper_val - lower_val) * (pos - lower))


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
    return {variant: compute_double_stats(draws) for variant, draws in draws_by_variant.items() if draws}


def combos_flagged_by_variant(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    return collect_variant_stats(state, base=base, max_n=max_n)


def multi_variant_alerts(state: str, *, base: Path | None = None, max_n: int = 1000) -> Dict[str, Dict[str, Dict[str, int]]]:
    stats = collect_variant_stats(state, base=base, max_n=max_n)
    alerts: Dict[str, Dict[str, Dict[str, int]]] = {}
    all_combos = {combo for variant_stats in stats.values() for combo in variant_stats.keys()}
    for combo in sorted(all_combos):
        flags = {variant: variant_stats[combo] for variant, variant_stats in stats.items() if combo in variant_stats}
        if len(flags) > 1:
            alerts[combo] = flags
    return alerts


def _iter_all_pairs() -> Iterable[str]:
    for p in range(10):
        for q in range(p, 10):
            yield f"{p}{q}"


def compute_pair_stats(draws: Sequence[str], *, window: int = PAIRS_WINDOW) -> Dict[str, Dict[str, Dict[str, int]] | Dict[str, str]]:
    if not draws:
        return {"repeating": {}, "non_repeating": {}, "status": {}, "times_seen": {}}
    if window and window > 0:
        analysis = list(draws[:window])
    else:
        analysis = list(draws)
    total = len(analysis)
    if total == 0:
        return {"repeating": {}, "non_repeating": {}, "status": {}, "times_seen": {}}

    last_seen: Dict[str, int] = {}
    times_drawn: Dict[str, int] = defaultdict(int)
    for idx, draw in enumerate(analysis):
        if not isinstance(draw, str) or len(draw) != 3:
            continue
        if not draw.isdigit():
            continue
        d1, d2, d3 = draw[0], draw[1], draw[2]
        raw_pairs = (d1 + d2, d2 + d3, d1 + d3)
        for raw_pair in raw_pairs:
            pair = "".join(sorted(raw_pair))
            times_drawn[pair] += 1
            if pair not in last_seen:
                last_seen[pair] = idx

    repeating_overdue: Dict[str, int] = {}
    non_repeating_overdue: Dict[str, int] = {}
    pair_status: Dict[str, str] = {}

    for pair in _iter_all_pairs():
        overdue = last_seen.get(pair, total)
        severity = None
        if pair[0] == pair[1]:
            repeating_overdue[pair] = overdue
            if overdue >= REPEATING_VERY_LATE:
                severity = COLOR_LATE
            elif overdue >= REPEATING_LATE:
                severity = COLOR_VERY_LATE
            elif overdue >= PAIR_PENDING:
                severity = COLOR_PENDING
        else:
            non_repeating_overdue[pair] = overdue
            if overdue >= NONREPEATING_VERY_LATE:
                severity = COLOR_LATE
            elif overdue >= NONREPEATING_LATE:
                severity = COLOR_VERY_LATE
            elif overdue >= PAIR_PENDING:
                severity = COLOR_PENDING
        if severity:
            pair_status[pair] = severity

    return {
        "repeating": repeating_overdue,
        "non_repeating": non_repeating_overdue,
        "status": pair_status,
        "times_seen": dict(times_drawn),
    }


def top_repeating_pairs(draws: Sequence[str], *, window: int = PAIRS_WINDOW, limit: int = 5) -> List[tuple[str, int]]:
    stats = compute_pair_stats(draws, window=window)
    repeating = stats["repeating"]
    return sorted(repeating.items(), key=lambda kv: kv[1], reverse=True)[:limit]


def top_non_repeating_pairs(draws: Sequence[str], *, window: int = PAIRS_WINDOW, limit: int = 5) -> List[tuple[str, int]]:
    stats = compute_pair_stats(draws, window=window)
    non_repeating = stats["non_repeating"]
    return sorted(non_repeating.items(), key=lambda kv: kv[1], reverse=True)[:limit]


def collect_pair_stats_for_state(state: str, *, base: Path | None = None, max_n: int = 1000, window: int = PAIRS_WINDOW) -> Dict[str, Dict[str, Dict[str, int]] | Dict[str, str]]:
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    result: Dict[str, Dict[str, Dict[str, int]] | Dict[str, str]] = {}
    for variant, draws in draws_by_variant.items():
        if draws:
            result[variant] = compute_pair_stats(draws, window=window)
    return result


def pair_multi_variant_alerts(state: str, *, base: Path | None = None, max_n: int = 1000, window: int = PAIRS_WINDOW) -> Dict[str, Dict[str, Dict[str, object]]]:
    variant_stats = collect_pair_stats_for_state(state, base=base, max_n=max_n, window=window)
    alerts: Dict[str, Dict[str, Dict[str, object]]] = {}
    for variant, stats in variant_stats.items():
        status = stats.get("status", {})
        for pair, severity in status.items():
            ds_map = stats["repeating"] if pair[0] == pair[1] else stats["non_repeating"]
            draws_since = ds_map.get(pair)
            alerts.setdefault(pair, {})[variant] = {
                "severity": severity,
                "draws_since": draws_since,
            }
    return {pair: data for pair, data in alerts.items() if len(data) > 1}




def summarize_repeat_watch(draws: Sequence[str], *, window: int = VTRAC_INDEX_WINDOW) -> Dict[str, int | None]:
    """Return repeat streak metrics for a newest-first draw stream."""
    trimmed = list(draws[:window]) if window else list(draws)
    if not trimmed:
        return {
            "current_index": None,
            "current_streak": 0,
            "last_repeat_gap": None,
            "last_repeat_index": None,
            "max_streak": 0,
            "window": 0,
        }

    resolver = get_vtrac_index
    stream: List[int | None] = []
    for draw in trimmed:
        idx = None
        if resolver:
            try:
                candidate = resolver(draw)  # type: ignore[arg-type]
            except Exception:
                candidate = None
            if isinstance(candidate, int):
                idx = candidate
        stream.append(idx)

    current_index = None
    current_streak = 0
    for value in stream:
        if value is None:
            if current_index is None:
                continue
            break
        if current_index is None:
            current_index = value
            current_streak = 1
        elif value == current_index:
            current_streak += 1
        else:
            break

    last_repeat_gap = None
    last_repeat_index = None
    max_streak = current_streak
    prev_idx = None
    streak = 0
    for offset, value in enumerate(stream):
        if value is None:
            prev_idx = None
            streak = 0
            continue
        if value == prev_idx:
            streak += 1
        else:
            streak = 1
            prev_idx = value
        if streak > max_streak:
            max_streak = streak
        if streak >= 2 and last_repeat_gap is None:
            last_repeat_gap = offset
            last_repeat_index = value

    return {
        "current_index": current_index,
        "current_streak": current_streak,
        "last_repeat_gap": last_repeat_gap,
        "last_repeat_index": last_repeat_index,
        "max_streak": max_streak,
        "window": len(trimmed),
    }


def repeat_summary_by_variant(state: str, *, base: Path | None = None, max_n: int = VTRAC_INDEX_WINDOW) -> Dict[str, Dict[str, int | None]]:
    """Summarize repeat watch metrics for each variant of a state."""
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    return {variant: summarize_repeat_watch(draws) for variant, draws in draws_by_variant.items() if draws}


def positional_hard_due(draws: Sequence[str], variant: str, *, window: int = 150) -> List[Dict[str, int]]:
    """Return positional cells flagged as hard-due for a given variant stream."""
    if not analyze_variant:
        return []
    result = analyze_variant(list(draws), variant, window=window)  # type: ignore[arg-type]
    flagged: List[Dict[str, int]] = []
    tracker_grid = getattr(result, "tracker_grid", {})
    for position, cells in tracker_grid.items():
        for cell in cells:
            if getattr(cell, "hard_due", False):
                flagged.append(
                    {
                        "position": int(position),
                        "digit": int(getattr(cell, "digit", -1)),
                        "draws_since": int(getattr(cell, "draws_since", 0)),
                    }
                )
    flagged.sort(key=lambda item: (item["position"], item["digit"]))
    return flagged


def positional_hard_due_by_variant(
    state: str, *, base: Path | None = None, max_n: int = 1000, window: int = 150
) -> Dict[str, List[Dict[str, int]]]:
    """Collect positional hard-due cells for each variant of a state."""
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    return {
        variant: positional_hard_due(draws, variant, window=window)
        for variant, draws in draws_by_variant.items()
        if draws
    }



def vtrac_overlay(draws: Sequence[str], *, window: int = VTRAC_INDEX_WINDOW) -> Dict[int, int]:
    """Compute draws-since for each V-TRAC index (1..35) from a newest-first stream."""
    trimmed = list(draws[:window]) if window else list(draws)
    total_len = len(trimmed)
    resolver = get_vtrac_index
    index_first_seen: Dict[int, int] = {}
    for offset, draw in enumerate(trimmed):
        idx = None
        if resolver and isinstance(draw, str):
            try:
                candidate = resolver(draw)  # type: ignore[arg-type]
            except Exception:
                candidate = None
            if isinstance(candidate, int) and 1 <= candidate <= 35:
                idx = candidate
        if idx is not None and idx not in index_first_seen:
            index_first_seen[idx] = offset
    return {idx: index_first_seen.get(idx, total_len) for idx in range(1, 36)}


def vtrac_overlay_by_variant(
    state: str,
    *,
    base: Path | None = None,
    max_n: int = VTRAC_INDEX_WINDOW,
) -> Dict[str, Dict[int, int]]:
    """Return draws-since maps for each variant of a state."""
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    return {variant: vtrac_overlay(draws) for variant, draws in draws_by_variant.items() if draws}


def vtrac_heatboard(
    draws: Sequence[str],
    *,
    overlay: Dict[int, int] | None = None,
    window: int = VTRAC_INDEX_WINDOW,
    short_threshold: int = 100,
    long_threshold: int = 200,
) -> Dict[int, Dict[str, float | int | None]]:
    """Rebuild the V-TRAC heatboard stats used in Aux/Control Center."""
    trimmed = list(draws[:window]) if window else list(draws)
    resolver = get_vtrac_index
    gap_history: Dict[int, List[int]] = {idx: [] for idx in range(1, 36)}
    last_seen: Dict[int, int | None] = {idx: None for idx in range(1, 36)}
    for offset, draw in enumerate(trimmed):
        idx = None
        if resolver and isinstance(draw, str):
            try:
                candidate = resolver(draw)  # type: ignore[arg-type]
            except Exception:
                candidate = None
            if isinstance(candidate, int) and 1 <= candidate <= 35:
                idx = candidate
        if idx is None:
            continue
        prev = last_seen[idx]
        if isinstance(prev, int):
            gap = offset - prev
            if gap > 0:
                gap_history[idx].append(gap)
        last_seen[idx] = offset
    draws_since_map = overlay if overlay is not None else vtrac_overlay(draws, window=window)
    stats: Dict[int, Dict[str, float | int | None]] = {}
    for idx in range(1, 36):
        gaps = gap_history[idx]
        avg_gap = float(sum(gaps)) / len(gaps) if gaps else None
        q80 = _percentile(sorted(gaps), 0.8) if gaps else None
        freq_short = sum(1 for gap in gaps if gap <= short_threshold)
        freq_long = sum(1 for gap in gaps if short_threshold < gap <= long_threshold)
        hazard = 0.0
        if avg_gap:
            hazard = 1.0 / max(1.0, avg_gap)
        draws_since = draws_since_map.get(idx, len(trimmed)) if isinstance(draws_since_map, dict) else len(trimmed)
        stats[idx] = {
            "ds": draws_since,
            "freq_short": freq_short,
            "freq_long": freq_long,
            "avg_gap": avg_gap,
            "q80_gap": q80,
            "hazard": hazard,
            "trend": freq_short - freq_long,
            "sample_size": len(gaps),
        }
    return stats


def vtrac_heatboard_by_variant(
    state: str,
    *,
    base: Path | None = None,
    max_n: int = VTRAC_INDEX_WINDOW,
    window: int = VTRAC_INDEX_WINDOW,
) -> Dict[str, Dict[int, Dict[str, float | int | None]]]:
    """Return heatboard stats per variant using the supplied draw CSVs."""
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    results: Dict[str, Dict[int, Dict[str, float | int | None]]] = {}
    for variant, draws in draws_by_variant.items():
        if not draws:
            continue
        overlay_map = vtrac_overlay(draws, window=window)
        results[variant] = vtrac_heatboard(draws, overlay=overlay_map, window=window)
    return results


def sums_stats(draws: Sequence[str], *, window: int = 100) -> Dict[str, Any]:
    """Wrapper around the refactored sums analysis module."""
    if not draws:
        return {"window": 0, "by_sum": {}, "by_root_sum": {}}
    try:
        from modules.module_d_auxiliary_tools.refactored.sums_analysis import calculate_sums_stats
    except Exception:  # pragma: no cover - staged Aux path may differ in CI
        return {"window": 0, "by_sum": {}, "by_root_sum": {}}
    return calculate_sums_stats(list(draws), window=window)


def sums_stats_by_variant(
    state: str,
    *,
    base: Path | None = None,
    max_n: int = 1000,
    window: int = 100,
) -> Dict[str, Dict[str, Any]]:
    """Compute sums/root-sum stats for each variant of a state."""
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    return {
        variant: sums_stats(draws, window=window)
        for variant, draws in draws_by_variant.items()
        if draws
    }





def positional_shortlist_report(
    state: str,
    *,
    base: Path | None = None,
    max_n: int = 1000,
    window: int = POSITIONAL_WINDOW,
    topk: Optional[int] = None,
    shortlist_config: Optional[Mapping[str, Any]] = None,
    due_doubles_active: Optional[bool] = None,
    vtrac_hot_indices: Optional[Iterable[int]] = None,
    vtrac_hot_families: Optional[Mapping[str, str]] = None,
) -> Dict[str, Any]:
    """Compute a backward-compatible, lossless Positional state summary."""
    if not analyze_state_variants:
        return {}
    draws_by_variant = load_variant_draws(state, base=base, max_n=max_n)
    if not draws_by_variant:
        return {}
    cfg = dict(POS_SHORTLIST_CONFIG or {})
    if shortlist_config:
        cfg.update(shortlist_config)
    topk_val = int(topk if topk is not None else cfg.get("topk_per_pos", 3))
    due_active = bool(due_doubles_active)
    hot_indices = sorted({int(value) for value in (vtrac_hot_indices or [])})
    hot_families = {
        str(key): str(value)
        for key, value in sorted((vtrac_hot_families or {}).items())
    }
    report = analyze_state_variants(
        draws_by_variant,
        window=window,
        topk=topk_val,
        shortlist_cfg=cfg,
        due_doubles_active=due_active,
        vtrac_hot_indices=hot_indices,
        vtrac_hot_families=hot_families,
    )

    variant_position_grid: Dict[str, Dict[str, Any]] = {}
    variant_top_digits: Dict[str, List[Dict[str, int]]] = {}
    for variant, result in report.variant_results.items():
        positions: Dict[str, Any] = {}
        top_list: List[Dict[str, int]] = []
        summaries = getattr(result, "position_summaries", {})
        tracker_grid = getattr(result, "tracker_grid", {})
        for position in (0, 1, 2):
            summary = summaries.get(position)
            hard_due_by_digit = {
                int(getattr(cell, "digit", -1)): bool(
                    getattr(cell, "hard_due", False)
                )
                for cell in tracker_grid.get(position, [])
            }
            full_rows: List[Dict[str, Any]] = []
            if summary and summary.top_digits:
                for item in summary.top_digits:
                    digit = int(getattr(item, "digit", -1))
                    full_rows.append(
                        {
                            "digit": digit,
                            "rank": int(getattr(item, "rank", 0)),
                            "gap": int(getattr(item, "gap", 0)),
                            "gap_percentile": float(
                                getattr(item, "gap_percentile", 0.0)
                            ),
                            "lag_weight": float(getattr(item, "lag_weight", 0.0)),
                            "occurrence_count": int(
                                getattr(item, "occurrence_count", 0)
                            ),
                            "last_seen_index": getattr(item, "last_seen_index", None),
                            "score": float(getattr(item, "score", 0.0)),
                            "score_components": {
                                str(key): float(value)
                                for key, value in sorted(
                                    getattr(item, "score_components", {}).items()
                                )
                            },
                            "tags": list(getattr(item, "tags", [])),
                            "hard_due": hard_due_by_digit.get(digit, False),
                        }
                    )
                top_digit = full_rows[0]
                top_list.append(
                    {
                        "position": position,
                        "digit": int(top_digit["digit"]),
                        "gap": int(top_digit["gap"]),
                        "rank": int(top_digit["rank"]),
                    }
                )
            positions[str(position)] = {
                "position": position,
                "population": int(getattr(summary, "population", 0)),
                "window": int(getattr(summary, "window", window)),
                "top_digits": full_rows,
            }
        variant_position_grid[variant] = {
            "draws_used": int(getattr(result, "draws_used", 0)),
            "window": int(getattr(result, "window", window)),
            "positions": positions,
        }
        if top_list:
            variant_top_digits[variant] = top_list

    aggregated_position_ladders: Dict[str, List[Dict[str, Any]]] = {}
    aggregated_summary: Dict[int, List[Dict[str, Any]]] = {}
    for position, digits in getattr(report, "aggregated_digits", {}).items():
        full_ladder = [
            {
                "rank": rank,
                "digit": int(item.digit),
                "score": float(item.score),
                "tags": list(getattr(item, "tags", [])),
                "occurrences": [
                    {
                        "variant": str(variant),
                        "rank": int(native_rank),
                    }
                    for variant, native_rank in getattr(item, "occurrences", [])
                ],
            }
            for rank, item in enumerate(digits, start=1)
        ]
        aggregated_position_ladders[str(position)] = full_ladder
        aggregated_summary[position] = [
            {
                "digit": row["digit"],
                "score": row["score"],
                "tags": row["tags"],
                "occurrences": [
                    (item["variant"], item["rank"])
                    for item in row["occurrences"]
                ],
            }
            for row in full_ladder[:5]
        ]

    candidate_payload: List[Dict[str, Any]] = []
    for rank, cand in enumerate(getattr(report, "candidates", []), start=1):
        combo = str(getattr(cand, "combo", ""))
        source = str(getattr(cand, "source", ""))
        candidate_payload.append(
            {
                "rank": rank,
                "combo": combo,
                "canonical": _canonical(combo),
                "score": float(getattr(cand, "score", 0.0)),
                "native_ranks": [
                    int(value) for value in getattr(cand, "ranks", ())
                ],
                "digital_root": int(getattr(cand, "digital_root", 0)),
                "vtrac_index": getattr(cand, "vtrac_index", None),
                "tags": list(getattr(cand, "tags", [])),
                "evidence": list(getattr(cand, "evidence", [])),
                "source": source,
                "lineage": {
                    "source_family": "aux_positional",
                    "source_object": "state_shortlist",
                    "state_key": state,
                    "variant_scope": list(VARIANTS),
                    "native_rank": rank,
                    "construction_source": source,
                },
            }
        )

    context_receipt = {
        "due_doubles": {
            "input_available": due_doubles_active is not None,
            "active": due_active,
        },
        "vtrac_hot_indices": {
            "input_available": vtrac_hot_indices is not None,
            "values": hot_indices,
        },
        "vtrac_hot_families": {
            "input_available": vtrac_hot_families is not None,
            "values": hot_families,
        },
        "any_optional_context_applied": bool(
            due_active or hot_indices or hot_families
        ),
    }
    return {
        "schema_version": "positional_shortlist_report_v2",
        "source_scope": "STATE",
        "variant_scope": list(VARIANTS),
        "context_receipt": context_receipt,
        "variant_position_grid": variant_position_grid,
        "variant_top_digits": variant_top_digits,
        "aggregated_position_ladders": aggregated_position_ladders,
        "aggregated_digits": aggregated_summary,
        "candidates": candidate_payload,
        "consensus_notes": list(getattr(report, "consensus_notes", [])),
        "double_pressure_notes": list(getattr(report, "double_pressure_notes", [])),
    }


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


__all__ = [
    "compute_double_stats",
    "collect_variant_stats",
    "combos_flagged_by_variant",
    "multi_variant_alerts",
    "compute_pair_stats",
    "top_repeating_pairs",
    "top_non_repeating_pairs",
    "collect_pair_stats_for_state",
    "pair_multi_variant_alerts",
    "summarize_repeat_watch",
    "repeat_summary_by_variant",
    "positional_hard_due",
    "positional_hard_due_by_variant",
    "positional_shortlist_report",
    "vtrac_overlay",
    "vtrac_overlay_by_variant",
    "vtrac_heatboard",
    "vtrac_heatboard_by_variant",
    "sums_stats",
    "sums_stats_by_variant",
    "family_badge_matrix",
]
