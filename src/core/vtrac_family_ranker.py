from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from .vtrac_families import VTRAC_DOUBLE_FAMILIES


def _canon_combo(combo: str) -> str:
    value = (combo or "").strip()
    if len(value) != 3 or not value.isdigit():
        return ""
    return "".join(sorted(value))


def _classify_double_gap(draws_since: int, *, red_threshold: int, blue_threshold: int) -> str | None:
    if draws_since >= red_threshold:
        return "R"
    if draws_since >= blue_threshold:
        return "B"
    return None


def rank_double_families(
    variant_draws: Dict[str, List[str]],
    *,
    red_threshold: int,
    blue_threshold: int,
    limit: int = 5,
) -> List[dict]:
    stats_by_variant: Dict[str, Dict[str, dict]] = {}
    family_combos = {combo for fam in VTRAC_DOUBLE_FAMILIES for combo in fam.combos}

    for variant_key, draws in variant_draws.items():
        if not draws:
            continue
        seen_first: Dict[str, int] = {}
        for idx, draw in enumerate(draws):
            canonical = _canon_combo(draw)
            if canonical and canonical not in seen_first:
                seen_first[canonical] = idx
        combo_status: Dict[str, dict] = {}
        default_gap = len(draws)
        for combo in family_combos:
            gap = seen_first.get(combo, default_gap)
            unseen = combo not in seen_first
            severity = _classify_double_gap(gap, red_threshold=red_threshold, blue_threshold=blue_threshold)
            if severity:
                combo_status[combo] = {
                    "severity": severity,
                    "draws_since": gap,
                    "unseen": unseen,
                }
        if combo_status:
            stats_by_variant[variant_key] = combo_status

    rankings: List[dict] = []
    for family in VTRAC_DOUBLE_FAMILIES:
        members: List[dict] = []
        score = 0
        best_gap = 0
        for variant_key, combo_stats in stats_by_variant.items():
            for combo in family.combos:
                status = combo_stats.get(combo)
                if not status:
                    continue
                severity = status["severity"]
                gap = int(status["draws_since"])
                unseen = bool(status.get("unseen"))
                score += 2 if severity == "R" else 1
                if gap > best_gap:
                    best_gap = gap
                members.append(
                    {
                        "combo": combo,
                        "canonical": _canon_combo(combo),
                        "severity": severity,
                        "variant": variant_key,
                        "draws_since": gap,
                        "unseen": unseen,
                    }
                )
        if members:
            rankings.append(
                {
                    "label": family.label,
                    "score": score,
                    "best_gap": best_gap,
                    "members": members,
                }
            )

    rankings.sort(key=lambda item: (item["score"], item["best_gap"]), reverse=True)
    return rankings[:limit]
