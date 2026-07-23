#!/usr/bin/env python3
"""Build a board-level spillover overlay from per-state aggregated arena artifacts.

The spillover overlay is the first runtime Brain 2 object for the arena branch.
It sits above per-state arena synthesis and below any future final-findings or
combination-forming layers. The goal is to compare strong states on one board,
surface shared lane/family complexes, and classify simple spent-vs-unspent
conditions once Midday truth exists.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index
from scripts.tools.brain2_rank_contract import (
    DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    legacy_rank_fields,
    unavailable_rank_contract,
)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _safe_rel(path: Path, repo_root: Path = REPO_ROOT) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _hash_inputs(paths: Sequence[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted({str(p.resolve()) for p in paths}):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        file_path = Path(path)
        if file_path.exists():
            digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _normalize_pick3_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    if len(digits) <= 3:
        digits = digits.zfill(3)
    return digits if len(digits) == 3 else ""


def _canon(value: object) -> str:
    digits = _normalize_pick3_literal(value)
    return "".join(sorted(digits)) if digits else ""


def _vtrac_index_for(value: object) -> Optional[str]:
    digits = _normalize_pick3_literal(value)
    if not digits:
        return None
    try:
        return str(get_vtrac_index(digits))
    except Exception:
        return None


def _parse_json_list(value: object) -> List[str]:
    raw = str(value or "").strip()
    if not raw.startswith("["):
        return []
    try:
        parsed = json.loads(raw)
    except Exception:
        return []
    if not isinstance(parsed, list):
        return []
    out: List[str] = []
    for item in parsed:
        digits = _normalize_pick3_literal(item)
        if digits:
            out.append(digits)
    return out


def _ordered_unique(values: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    out: List[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _top_slice(values: Sequence[str], limit: int) -> List[str]:
    return _ordered_unique(list(values)[: max(0, int(limit))])


def _slugify(value: str) -> str:
    lowered = re.sub(r"[^a-zA-Z0-9]+", "_", str(value or "").strip()).strip("_").lower()
    return lowered or "board"


def _normalize_state_alias(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def _prettify_state_key(state_key: str) -> str:
    base = re.sub(r"\d+$", "", str(state_key or "").strip())
    base = re.sub(r"(?<!^)(?=[A-Z])", " ", base)
    return base.replace("  ", " ").strip() or str(state_key or "")


def _state_aliases(state_key: str, display_name: Optional[str] = None) -> Set[str]:
    aliases = {
        _normalize_state_alias(state_key),
        _normalize_state_alias(re.sub(r"\d+$", "", state_key)),
        _normalize_state_alias(_prettify_state_key(state_key)),
    }
    if display_name:
        aliases.add(_normalize_state_alias(display_name))
    if state_key == "OntarioCanada4":
        aliases.add(_normalize_state_alias("Ontario"))
        aliases.add(_normalize_state_alias("Ontario Canada"))
    return {alias for alias in aliases if alias}


def _find_arena_path(state_dir: Path, profile: str, experiment_tag: str) -> Optional[Path]:
    preferred = state_dir / "analysis" / f"aggregated_analysis_arena__{profile}__{experiment_tag}.json"
    if preferred.exists():
        return preferred
    analysis_dir = state_dir / "analysis"
    if not analysis_dir.exists():
        return None
    candidates = sorted(analysis_dir.glob(f"aggregated_analysis_arena__{profile}__*.json"))
    if candidates:
        return candidates[-1]
    fallback = sorted(analysis_dir.glob("aggregated_analysis_arena__*.json"))
    return fallback[-1] if fallback else None


def _load_profit_alert_rows(day_dir: Path, states: Sequence[str]) -> Tuple[List[Dict[str, str]], Optional[Path]]:
    path = day_dir / "control_center" / "profit_alerts.csv"
    rows = _load_csv_rows(path)
    state_set = {str(state).strip() for state in states}
    filtered = [row for row in rows if str(row.get("StateKey") or "").strip() in state_set]
    return filtered, path if path.exists() else None


def _build_state_alias_map(states: Sequence[str], profit_alert_rows: Sequence[Dict[str, str]]) -> Dict[str, str]:
    alias_map: Dict[str, str] = {}
    for state_key in states:
        for alias in _state_aliases(state_key):
            alias_map.setdefault(alias, state_key)
    for row in profit_alert_rows:
        state_key = str(row.get("StateKey") or "").strip()
        if not state_key:
            continue
        for alias in _state_aliases(state_key, display_name=str(row.get("State") or "")):
            alias_map.setdefault(alias, state_key)
    return alias_map


def _parse_midday_results(path: Optional[Path], alias_map: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    if path is None or not path.exists():
        return {}
    out: Dict[str, Dict[str, str]] = {}
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.lower().startswith("pick ") or line.lower().startswith("midday"):
            continue
        parts = [part.strip() for part in raw_line.split("\t")]
        parts = [part for part in parts if part.strip()]
        if len(parts) >= 2 and _normalize_pick3_literal(parts[1]):
            state_name, midday = parts[0], _normalize_pick3_literal(parts[1])
        else:
            bits = re.split(r"\s{2,}", line)
            if len(bits) < 2:
                continue
            state_name, midday = bits[0], _normalize_pick3_literal(bits[1])
        if not midday:
            continue
        state_key = alias_map.get(_normalize_state_alias(state_name))
        if not state_key:
            continue
        out[state_key] = {
            "display_name": state_name,
            "winner_literal": midday,
            "winner_canonical": _canon(midday),
            "winner_vtrac_index": _vtrac_index_for(midday) or "",
        }
    return out


def _top_values(rows: Sequence[Dict[str, Any]], key: str, limit: int) -> List[str]:
    values: List[str] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        text = str(row.get(key) or "").strip()
        if text:
            values.append(text)
    return _ordered_unique(values)


def _top_canonicals(rows: Sequence[Dict[str, Any]], limit: int) -> List[str]:
    out: List[str] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        value = _canon(row.get("value"))
        if value:
            out.append(value)
    return _ordered_unique(out)


def _extract_due_double_families(arena_objects: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    ctx = arena_objects.get("aux_due_doubles_family_pressure")
    if not isinstance(ctx, dict):
        return []
    by_variant = ctx.get("by_variant") if isinstance(ctx.get("by_variant"), dict) else {}
    out: List[Dict[str, Any]] = []
    for variant, payload in by_variant.items():
        if not isinstance(payload, dict):
            continue
        families = payload.get("families") if isinstance(payload.get("families"), list) else []
        out.append(
            {
                "variant": str(variant),
                "draws_since_double": _to_int(payload.get("draws_since_double"), default=0),
                "families": [
                    {
                        "family": str(row.get("family") or ""),
                        "slot": str(row.get("slot") or ""),
                        "examples": [str(example) for example in (row.get("examples") or []) if str(example)]
                    }
                    for row in families[: max(0, int(limit))]
                    if isinstance(row, dict)
                ],
            }
        )
    out.sort(key=lambda item: (item.get("variant") != "Combined", str(item.get("variant") or "")))
    return out


def _extract_blackapple_statuses(arena_objects: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    ctx = arena_objects.get("aux_blackapple_context")
    if not isinstance(ctx, dict):
        return []
    rows = ctx.get("control_center_top") if isinstance(ctx.get("control_center_top"), list) else []
    out: List[Dict[str, Any]] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        out.append(
            {
                "variant": str(row.get("variant") or ""),
                "status": str(row.get("status") or ""),
                "ba_score": _to_int(row.get("ba_score"), default=0),
                "candidate_count": _to_int(row.get("candidate_count"), default=0),
                "examples": [str(example) for example in (row.get("examples") or []) if str(example)],
                "triggers": str(row.get("triggers") or ""),
            }
        )
    return out


def _extract_blackapple_recommended_canonicals(arena_objects: Dict[str, Any], limit: int) -> List[str]:
    ctx = arena_objects.get("aux_blackapple_context")
    if not isinstance(ctx, dict):
        return []
    values = ctx.get("recommended_canonicals_top") if isinstance(ctx.get("recommended_canonicals_top"), list) else []
    return _ordered_unique([_canon(value) for value in values if _canon(value)])[: max(0, int(limit))]


def _extract_positional_shortlist(arena_objects: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    ctx = arena_objects.get("aux_positional_pressure")
    if not isinstance(ctx, dict):
        return []
    rows = ctx.get("shortlist_top") if isinstance(ctx.get("shortlist_top"), list) else []
    out: List[Dict[str, Any]] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo"))
        out.append(
            {
                "combo": combo,
                "canonical": _canon(combo) or _canon(row.get("canonical")),
                "score": round(_to_float(row.get("score")), 6),
                "tags": [str(tag) for tag in (row.get("tags") or []) if str(tag)],
                "vtrac_index": str(row.get("vtrac_index") or ""),
            }
        )
    return out


def _extract_positional_signal_notes(arena_objects: Dict[str, Any], limit: int) -> List[str]:
    ctx = arena_objects.get("aux_positional_pressure")
    if not isinstance(ctx, dict):
        return []
    notes = ctx.get("signal_notes_top") if isinstance(ctx.get("signal_notes_top"), list) else []
    return _ordered_unique([str(note) for note in notes if str(note).strip()])[: max(0, int(limit))]


def _extract_due_double_examples(arena_objects: Dict[str, Any], limit: int) -> List[str]:
    ctx = arena_objects.get("aux_due_doubles_family_pressure")
    if not isinstance(ctx, dict):
        return []
    values = ctx.get("top_example_canonicals") if isinstance(ctx.get("top_example_canonicals"), list) else []
    return _ordered_unique([_canon(value) for value in values if _canon(value)])[: max(0, int(limit))]


def _extract_due_double_family_names(arena_objects: Dict[str, Any], limit: int) -> List[str]:
    ctx = arena_objects.get("aux_due_doubles_family_pressure")
    if not isinstance(ctx, dict):
        return []
    by_variant = ctx.get("by_variant") if isinstance(ctx.get("by_variant"), dict) else {}
    out: List[str] = []
    for payload in by_variant.values():
        if not isinstance(payload, dict):
            continue
        families = payload.get("families") if isinstance(payload.get("families"), list) else []
        for row in families:
            if not isinstance(row, dict):
                continue
            text = str(row.get("family") or "").strip()
            if text:
                out.append(text)
    return _ordered_unique(out)[: max(0, int(limit))]


def _extract_compound_events(arena_objects: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    ctx = arena_objects.get("cc_compound_event_context")
    if not isinstance(ctx, dict):
        return []
    rows = ctx.get("top_events") if isinstance(ctx.get("top_events"), list) else []
    out: List[Dict[str, Any]] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        out.append(
            {
                "variant": str(row.get("variant") or ""),
                "top_event": str(row.get("top_event") or ""),
                "priority": _to_int(row.get("priority"), default=0),
                "candidate_alert_ids": [str(item) for item in (row.get("candidate_alert_ids") or []) if str(item)],
                "promoter_alert_ids": [str(item) for item in (row.get("promoter_alert_ids") or []) if str(item)],
                "watchlist_tags": [str(item) for item in (row.get("watchlist_tags") or []) if str(item)],
                "strength_max": _to_int(row.get("strength_max"), default=0),
            }
        )
    return out


def _extract_profit_alert_rows(
    *,
    state_key: str,
    arena_objects: Dict[str, Any],
    raw_rows: Sequence[Dict[str, str]],
    limit: int,
) -> Tuple[List[Dict[str, Any]], List[str], List[str]]:
    compact = arena_objects.get("cc_profit_alert_context")
    compact_rows = compact.get("top_alerts") if isinstance(compact, dict) and isinstance(compact.get("top_alerts"), list) else []
    top_alerts: List[Dict[str, Any]] = []
    for row in compact_rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        top_alerts.append(
            {
                "alert_id": str(row.get("alert_id") or ""),
                "variant": str(row.get("variant") or ""),
                "canonical": _canon(row.get("canonical")),
                "strength": _to_int(row.get("strength"), default=0),
                "badges": [str(badge) for badge in (row.get("badges") or []) if str(badge)],
                "suggested": str(row.get("suggested") or ""),
                "implied_set_size": _to_int(row.get("implied_set_size"), default=0),
            }
        )

    implied_literals: List[str] = []
    alert_canonicals: List[str] = []
    for row in raw_rows:
        if str(row.get("StateKey") or "").strip() != state_key:
            continue
        canonical = _canon(row.get("Canonical"))
        if canonical:
            alert_canonicals.append(canonical)
        implied_literals.extend(_parse_json_list(row.get("ImpliedSet")))
    implied_canonicals = [_canon(item) for item in implied_literals if _canon(item)]
    return top_alerts, _ordered_unique(alert_canonicals), _ordered_unique(implied_canonicals)


def _extract_context_reinforced(synthesis: Dict[str, Any], limit: int) -> List[str]:
    rows = synthesis.get("context_reinforced_canonicals")
    if not isinstance(rows, list):
        return []
    return _top_canonicals(rows, limit)


def _extract_context_only_pressure(synthesis: Dict[str, Any], limit: int) -> List[str]:
    rows = synthesis.get("context_only_pressure")
    if not isinstance(rows, list):
        return []
    out: List[str] = []
    for row in rows[: max(0, int(limit))]:
        if not isinstance(row, dict):
            continue
        value = _canon(row.get("value") or row.get("canonical"))
        if value:
            out.append(value)
    return _ordered_unique(out)


def _extract_r_consensus_context(synthesis: Dict[str, Any]) -> Dict[str, Any]:
    ctx = synthesis.get("r_consensus_context")
    if not isinstance(ctx, dict):
        return {
            "available": False,
            "event_count": 0,
            "trial_eligible": False,
            "signal_strength_class": "none",
        }
    return {
        "available": bool(ctx.get("available")),
        "event_count": _to_int(ctx.get("event_count"), 0),
        "single_digit_count": _to_int(ctx.get("single_digit_count"), 0),
        "two_digit_count": _to_int(ctx.get("two_digit_count"), 0),
        "col1_count": _to_int(ctx.get("col1_count"), 0),
        "col2_count": _to_int(ctx.get("col2_count"), 0),
        "top_tail_values": [str(value) for value in (ctx.get("top_tail_values") or []) if str(value).strip()],
        "cross_variant_tail_values": [str(value) for value in (ctx.get("cross_variant_tail_values") or []) if str(value).strip()],
        "top_support_canonicals": [_canon(value) for value in (ctx.get("top_support_canonicals") or []) if _canon(value)],
        "top_support_vtrac_indices": [str(value) for value in (ctx.get("top_support_vtrac_indices") or []) if str(value).strip()],
        "signal_strength_class": str(ctx.get("signal_strength_class") or "none"),
        "trial_eligible": bool(ctx.get("trial_eligible")),
    }


def _primary_canonicals(
    *,
    dominant_canonicals: Sequence[str],
    watchlist_canonicals: Sequence[str],
    survivor_frontier_canonicals: Sequence[str],
    survivor_last_remaining_canonicals: Sequence[str],
    context_reinforced_canonicals: Sequence[str],
    profit_alert_canonicals: Sequence[str],
) -> List[str]:
    return _ordered_unique(
        [
            *_top_slice(dominant_canonicals, 6),
            *_top_slice(watchlist_canonicals, 6),
            *_top_slice(survivor_last_remaining_canonicals, 4),
            *_top_slice(survivor_frontier_canonicals, 4),
            *_top_slice(context_reinforced_canonicals, 4),
            *_top_slice(profit_alert_canonicals, 4),
        ]
    )


def _secondary_canonicals(
    *,
    context_only_pressure: Sequence[str],
    profit_alert_implied_canonicals: Sequence[str],
    positional_shortlist_top: Sequence[Dict[str, Any]],
    blackapple_recommended_canonicals: Sequence[str],
    due_double_example_canonicals: Sequence[str],
) -> List[str]:
    return _ordered_unique(
        [
            *_top_slice(context_only_pressure, 4),
            *_top_slice(profit_alert_implied_canonicals, 10),
            *_top_slice(blackapple_recommended_canonicals, 6),
            *_top_slice(due_double_example_canonicals, 6),
            *[
                _canon(row.get("canonical"))
                for row in list(positional_shortlist_top)[:4]
                if isinstance(row, dict) and _canon(row.get("canonical"))
            ],
        ]
    )


def _primary_vtrac_indices(
    *,
    dominant_vtrac_indices: Sequence[str],
    watchlist_indices: Sequence[str],
    survivor_frontier_vtrac_indices: Sequence[str],
    survivor_last_remaining_vtrac_indices: Sequence[str],
    primary_canonicals: Sequence[str],
) -> List[str]:
    return _ordered_unique(
        [
            *_top_slice(dominant_vtrac_indices, 5),
            *_top_slice(watchlist_indices, 4),
            *_top_slice(survivor_last_remaining_vtrac_indices, 4),
            *_top_slice(survivor_frontier_vtrac_indices, 4),
            *[_vtrac_index_for(value) or "" for value in list(primary_canonicals)[:8] if _vtrac_index_for(value)],
        ]
    )


def _secondary_vtrac_indices(
    *,
    secondary_canonicals: Sequence[str],
    positional_shortlist_top: Sequence[Dict[str, Any]],
) -> List[str]:
    return _ordered_unique(
        [
            *[_vtrac_index_for(value) or "" for value in list(secondary_canonicals)[:10] if _vtrac_index_for(value)],
            *[
                str(row.get("vtrac_index") or "")
                for row in list(positional_shortlist_top)[:4]
                if isinstance(row, dict) and str(row.get("vtrac_index") or "").strip() not in {"", "-1"}
            ],
        ]
    )


def _relationship_score(row: Dict[str, Any]) -> int:
    relationship_type = str(row.get("relationship_type") or "")
    directness = str(row.get("directness") or "")
    support_count = _to_int(row.get("support_count"), default=0)
    overlap_tier = str(row.get("overlap_tier") or "primary")
    if relationship_type == "alert_implied_echo" and directness == "direct-cross-state":
        return 12 + support_count
    if relationship_type == "alert_implied_echo":
        return 6 + support_count if overlap_tier == "primary" else 3 + support_count
    if relationship_type == "shared_box_family":
        return 5 + support_count if overlap_tier == "primary" else 2 + support_count
    if relationship_type == "shared_lane":
        return 4 + support_count if overlap_tier == "primary" else 1 + support_count
    return support_count


def _build_state_summary(
    *,
    state_key: str,
    input_rank: int,
    payload: Dict[str, Any],
    raw_profit_alert_rows: Sequence[Dict[str, str]],
    top_items: int,
) -> Dict[str, Any]:
    synthesis = payload.get("arena_synthesis") if isinstance(payload.get("arena_synthesis"), dict) else {}
    arena_objects = (
        ((payload.get("context_tools") or {}).get("aux_control_center") or {}).get("arena_objects")
        if isinstance((payload.get("context_tools") or {}).get("aux_control_center"), dict)
        else {}
    )
    if not isinstance(arena_objects, dict):
        arena_objects = {}

    dominant_canonicals = _top_canonicals(synthesis.get("dominant_canonicals") or [], top_items)
    dominant_vtrac_indices = _top_values(synthesis.get("dominant_vtrac_indices") or [], "value", top_items)
    dominant_families = _top_values(synthesis.get("dominant_families") or [], "value", top_items)
    stable_survivor_context = synthesis.get("stable_survivor_context") if isinstance(synthesis.get("stable_survivor_context"), dict) else {}
    r_consensus_context = _extract_r_consensus_context(synthesis)
    survivor_frontier_canonicals = _top_slice(stable_survivor_context.get("top_frontier_canonicals") or [], top_items)
    survivor_last_remaining_canonicals = _top_slice(stable_survivor_context.get("top_last_remaining_canonicals") or [], top_items)
    survivor_frontier_vtrac_indices = _top_slice(stable_survivor_context.get("top_frontier_vtrac_indices") or [], top_items)
    survivor_last_remaining_vtrac_indices = _top_slice(stable_survivor_context.get("top_last_remaining_vtrac_indices") or [], top_items)
    survivor_terminal_profiles = [
        str(item.get("profile") or "")
        for item in (stable_survivor_context.get("last_remaining_examples") or [])[: max(0, int(top_items))]
        if isinstance(item, dict) and str(item.get("profile") or "").strip()
    ]

    watchlist = synthesis.get("vtrac_literal_watchlist") if isinstance(synthesis.get("vtrac_literal_watchlist"), list) else []
    watchlist_indices: List[str] = []
    watchlist_canonicals: List[str] = []
    for row in watchlist[: max(0, int(top_items))]:
        if not isinstance(row, dict):
            continue
        index = str(row.get("vtrac_index") or "").strip()
        if index:
            watchlist_indices.append(index)
        watchlist_canonicals.extend([_canon(value) for value in (row.get("candidate_canonicals") or []) if _canon(value)])

    context_reinforced_canonicals = _extract_context_reinforced(synthesis, top_items)
    context_only_pressure = _extract_context_only_pressure(synthesis, top_items)
    top_profit_alerts, profit_alert_canonicals, profit_alert_implied_canonicals = _extract_profit_alert_rows(
        state_key=state_key,
        arena_objects=arena_objects,
        raw_rows=raw_profit_alert_rows,
        limit=top_items,
    )
    blackapple_statuses = _extract_blackapple_statuses(arena_objects, limit=top_items)
    blackapple_recommended_canonicals = _extract_blackapple_recommended_canonicals(arena_objects, limit=top_items)
    positional_shortlist_top = _extract_positional_shortlist(arena_objects, limit=top_items)
    positional_signal_notes = _extract_positional_signal_notes(arena_objects, limit=top_items)
    due_double_families = _extract_due_double_families(arena_objects, limit=min(top_items, 5))
    due_double_example_canonicals = _extract_due_double_examples(arena_objects, limit=top_items)
    due_double_family_names = _extract_due_double_family_names(arena_objects, limit=top_items)
    compound_events_top = _extract_compound_events(arena_objects, limit=top_items)
    primary_canonicals = _primary_canonicals(
        dominant_canonicals=dominant_canonicals,
        watchlist_canonicals=watchlist_canonicals,
        survivor_frontier_canonicals=survivor_frontier_canonicals,
        survivor_last_remaining_canonicals=survivor_last_remaining_canonicals,
        context_reinforced_canonicals=context_reinforced_canonicals,
        profit_alert_canonicals=profit_alert_canonicals,
    )
    secondary_canonicals = _secondary_canonicals(
        context_only_pressure=context_only_pressure,
        profit_alert_implied_canonicals=profit_alert_implied_canonicals,
        positional_shortlist_top=positional_shortlist_top,
        blackapple_recommended_canonicals=blackapple_recommended_canonicals,
        due_double_example_canonicals=due_double_example_canonicals,
    )
    primary_vtrac_indices = _primary_vtrac_indices(
        dominant_vtrac_indices=dominant_vtrac_indices,
        watchlist_indices=watchlist_indices,
        survivor_frontier_vtrac_indices=survivor_frontier_vtrac_indices,
        survivor_last_remaining_vtrac_indices=survivor_last_remaining_vtrac_indices,
        primary_canonicals=primary_canonicals,
    )
    secondary_vtrac_indices = _secondary_vtrac_indices(
        secondary_canonicals=secondary_canonicals,
        positional_shortlist_top=positional_shortlist_top,
    )

    surface_canonicals = _ordered_unique(
        [
            *primary_canonicals,
            *secondary_canonicals,
        ]
    )
    surface_vtrac_indices = _ordered_unique(
        [
            *primary_vtrac_indices,
            *secondary_vtrac_indices,
            *[_vtrac_index_for(value) or "" for value in surface_canonicals if _vtrac_index_for(value)],
        ]
    )

    state_regime = synthesis.get("state_regime") if isinstance(synthesis.get("state_regime"), dict) else {}
    return {
        "state_key": state_key,
        "state_name": _prettify_state_key(state_key),
        "input_rank": input_rank,
        "dominant_canonicals": dominant_canonicals,
        "dominant_vtrac_indices": dominant_vtrac_indices,
        "dominant_families": dominant_families,
        "stable_survivor_context": stable_survivor_context,
        "survivor_frontier_canonicals": survivor_frontier_canonicals,
        "survivor_last_remaining_canonicals": survivor_last_remaining_canonicals,
        "survivor_frontier_vtrac_indices": survivor_frontier_vtrac_indices,
        "survivor_last_remaining_vtrac_indices": survivor_last_remaining_vtrac_indices,
        "survivor_terminal_profiles": _ordered_unique(survivor_terminal_profiles),
        "r_consensus_context": r_consensus_context,
        "r_consensus_top_tail_values": _top_slice(r_consensus_context.get("top_tail_values") or [], top_items),
        "r_consensus_cross_variant_tail_values": _top_slice(r_consensus_context.get("cross_variant_tail_values") or [], top_items),
        "r_consensus_support_canonicals": _top_slice(r_consensus_context.get("top_support_canonicals") or [], top_items),
        "r_consensus_support_vtrac_indices": _top_slice(r_consensus_context.get("top_support_vtrac_indices") or [], top_items),
        "watchlist_indices": _ordered_unique(watchlist_indices),
        "watchlist_canonicals": _ordered_unique(watchlist_canonicals),
        "context_reinforced_canonicals": context_reinforced_canonicals,
        "context_only_pressure": context_only_pressure,
        "top_profit_alerts": top_profit_alerts,
        "profit_alert_canonicals": profit_alert_canonicals,
        "profit_alert_implied_canonicals": profit_alert_implied_canonicals,
        "blackapple_statuses": blackapple_statuses,
        "blackapple_recommended_canonicals": blackapple_recommended_canonicals,
        "positional_shortlist_top": positional_shortlist_top,
        "positional_signal_notes": positional_signal_notes,
        "due_double_families": due_double_families,
        "due_double_example_canonicals": due_double_example_canonicals,
        "due_double_family_names": due_double_family_names,
        "compound_events_top": compound_events_top,
        "primary_canonicals": primary_canonicals,
        "secondary_canonicals": secondary_canonicals,
        "primary_vtrac_indices": primary_vtrac_indices,
        "secondary_vtrac_indices": secondary_vtrac_indices,
        "surface_canonicals": surface_canonicals,
        "surface_vtrac_indices": surface_vtrac_indices,
        "state_regime": {
            "dominant_canonical": str(state_regime.get("dominant_canonical") or ""),
            "dominant_vtrac_index": str(state_regime.get("dominant_vtrac_index") or ""),
            "dominant_family": str(state_regime.get("dominant_family") or ""),
            "double_heavy": bool(state_regime.get("double_heavy")),
            "context_reinforced": bool(state_regime.get("context_reinforced")),
            "vtrac_alignment": str(state_regime.get("vtrac_alignment") or ""),
            "tail_consensus_present": bool(state_regime.get("tail_consensus_present")),
            "tail_consensus_value": str(state_regime.get("tail_consensus_value") or ""),
            "tail_consensus_column": str(state_regime.get("tail_consensus_column") or ""),
            "consensus_strength_class": str(state_regime.get("consensus_strength_class") or ""),
            "consensus_trial_eligible": bool(state_regime.get("consensus_trial_eligible")),
            "survivor_pressure": bool(state_regime.get("survivor_pressure")),
            "survivor_progression": bool(state_regime.get("survivor_progression")),
            "last_remaining": bool(state_regime.get("last_remaining")),
            "hidden_terminal_support": bool(state_regime.get("hidden_terminal_support")),
            "survivor_frontier_count": _to_int(state_regime.get("survivor_frontier_count"), 0),
            "survivor_progression_count": _to_int(state_regime.get("survivor_progression_count"), 0),
            "last_remaining_rows": _to_int(state_regime.get("last_remaining_rows"), 0),
            "r_consensus_event_count": _to_int(state_regime.get("r_consensus_event_count"), 0),
            "r_consensus_cross_variant_tail_count": _to_int(state_regime.get("r_consensus_cross_variant_tail_count"), 0),
        },
    }


def _midday_status_for_state(
    *,
    state_key: str,
    summary: Dict[str, Any],
    midday_results: Dict[str, Dict[str, str]],
    summaries_by_state: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    result = midday_results.get(state_key)
    if not result:
        return {"available": False}
    winner_canonical = str(result.get("winner_canonical") or "")
    winner_vtrac_index = str(result.get("winner_vtrac_index") or "")
    local_canonical_hit = winner_canonical in set(summary.get("primary_canonicals") or [])
    local_vtrac_hit = winner_vtrac_index in set(summary.get("primary_vtrac_indices") or [])
    local_watchlist_hit = winner_canonical in set(summary.get("watchlist_canonicals") or [])

    cross_state_hosts: List[str] = []
    for other_key, other in summaries_by_state.items():
        if other_key == state_key:
            continue
        other_canons = set(other.get("primary_canonicals") or []) | set(other.get("profit_alert_implied_canonicals") or [])
        other_indices = set(other.get("primary_vtrac_indices") or [])
        if winner_canonical in other_canons or winner_vtrac_index in other_indices:
            cross_state_hosts.append(other_key)

    if local_canonical_hit:
        spent_status = "locally_spent"
    elif local_vtrac_hit or local_watchlist_hit:
        spent_status = "lane_spent"
    elif cross_state_hosts:
        spent_status = "cross_state_spent"
    else:
        spent_status = "mostly_unspent"

    if spent_status == "locally_spent":
        evening_bias = "de_emphasize"
    elif spent_status == "lane_spent":
        evening_bias = "soft_watch"
    else:
        evening_bias = "still_live"

    return {
        "available": True,
        "winner_literal": str(result.get("winner_literal") or ""),
        "winner_canonical": winner_canonical,
        "winner_vtrac_index": winner_vtrac_index,
        "local_canonical_hit": local_canonical_hit,
        "local_vtrac_hit": local_vtrac_hit,
        "local_watchlist_hit": local_watchlist_hit,
        "cross_state_hosts": _ordered_unique(cross_state_hosts),
        "spent_status": spent_status,
        "evening_bias": evening_bias,
    }


def _pair_support(shared_lanes: List[str], shared_canonicals: List[str], echo_canonicals: List[str]) -> int:
    return len(shared_lanes) + len(shared_canonicals) + len(echo_canonicals)


def _build_relationships(
    *,
    state_order: Sequence[str],
    summaries_by_state: Dict[str, Dict[str, Any]],
    midday_results: Dict[str, Dict[str, str]],
) -> List[Dict[str, Any]]:
    relationships: List[Dict[str, Any]] = []
    for index, state_a in enumerate(state_order):
        summary_a = summaries_by_state[state_a]
        for state_b in state_order[index + 1 :]:
            summary_b = summaries_by_state[state_b]
            primary_lanes = sorted(set(summary_a.get("primary_vtrac_indices") or []) & set(summary_b.get("primary_vtrac_indices") or []))
            secondary_lanes = sorted(
                (set(summary_a.get("surface_vtrac_indices") or []) & set(summary_b.get("surface_vtrac_indices") or []))
                - set(primary_lanes)
            )
            shared_lanes = primary_lanes[:10]
            top_lane_a = set(list(summary_a.get("dominant_vtrac_indices") or [])[:2])
            top_lane_b = set(list(summary_b.get("dominant_vtrac_indices") or [])[:2])
            if shared_lanes and (len(shared_lanes) >= 2 or bool(set(shared_lanes) & (top_lane_a | top_lane_b))):
                midday_consumed = (
                    midday_results.get(state_a, {}).get("winner_vtrac_index") in shared_lanes
                    or midday_results.get(state_b, {}).get("winner_vtrac_index") in shared_lanes
                )
                relationships.append(
                    {
                        "state_a": state_a,
                        "state_b": state_b,
                        "relationship_type": "shared_lane",
                        "directness": "lane/family",
                        "vtrac_indices": shared_lanes,
                        "canonical_families": [],
                        "source_surface": ["dominant_vtrac_indices", "vtrac_literal_watchlist", "context surfaces"],
                        "support_count": len(shared_lanes),
                        "overlap_tier": "primary",
                        "secondary_vtrac_indices": secondary_lanes[:6],
                        "midday_consumed": bool(midday_consumed),
                        "still_live_evening": not bool(midday_consumed),
                        "explanation": f"States share live VTRAC lane(s): {', '.join(shared_lanes[:6])}.",
                    }
                )

            primary_canonicals = sorted(set(summary_a.get("primary_canonicals") or []) & set(summary_b.get("primary_canonicals") or []))
            secondary_canonicals = sorted(
                (set(summary_a.get("surface_canonicals") or []) & set(summary_b.get("surface_canonicals") or []))
                - set(primary_canonicals)
            )
            top_canonical_a = set(list(summary_a.get("dominant_canonicals") or [])[:2])
            top_canonical_b = set(list(summary_b.get("dominant_canonicals") or [])[:2])
            shared_canonicals = primary_canonicals[:12]
            if shared_canonicals and (len(shared_canonicals) >= 2 or bool(set(shared_canonicals) & (top_canonical_a | top_canonical_b))):
                midday_consumed = (
                    midday_results.get(state_a, {}).get("winner_canonical") in shared_canonicals
                    or midday_results.get(state_b, {}).get("winner_canonical") in shared_canonicals
                )
                relationships.append(
                    {
                        "state_a": state_a,
                        "state_b": state_b,
                        "relationship_type": "shared_box_family",
                        "directness": "lane/family",
                        "vtrac_indices": [],
                        "canonical_families": shared_canonicals[:12],
                        "source_surface": ["dominant_canonicals", "watchlists", "context reinforced", "profit alerts"],
                        "support_count": len(shared_canonicals),
                        "overlap_tier": "primary",
                        "secondary_canonical_families": secondary_canonicals[:6],
                        "midday_consumed": bool(midday_consumed),
                        "still_live_evening": not bool(midday_consumed),
                        "explanation": f"States share canonical family/families: {', '.join(shared_canonicals[:6])}.",
                    }
                )

        for state_b in state_order:
            if state_a == state_b:
                continue
            implied_set = set(summary_a.get("profit_alert_implied_canonicals") or [])
            if not implied_set:
                continue
            target_winner = midday_results.get(state_b, {}).get("winner_canonical") if midday_results else None
            target_primary_surface = set(summaries_by_state[state_b].get("primary_canonicals") or [])
            target_secondary_surface = set(summaries_by_state[state_b].get("secondary_canonicals") or [])
            comparison_surface = set(target_primary_surface)
            if target_winner:
                comparison_surface.add(str(target_winner))
            echo_canonicals = sorted(implied_set & comparison_surface)
            composite_canonicals = sorted((implied_set & target_secondary_surface) - set(echo_canonicals))
            if not echo_canonicals and not composite_canonicals:
                continue
            direct_cross = bool(target_winner and target_winner in implied_set)
            overlap_tier = "primary" if echo_canonicals else "secondary"
            surfaced = echo_canonicals if echo_canonicals else composite_canonicals[:6]
            relationships.append(
                {
                    "state_a": state_a,
                    "state_b": state_b,
                    "relationship_type": "alert_implied_echo",
                    "directness": "direct-cross-state" if direct_cross else ("lane/family" if echo_canonicals else "composite"),
                    "vtrac_indices": _ordered_unique([_vtrac_index_for(value) or "" for value in surfaced if _vtrac_index_for(value)]),
                    "canonical_families": surfaced[:12],
                    "source_surface": ["profit_alert_implied_set", "target primary canonicals"],
                    "support_count": len(surfaced),
                    "overlap_tier": overlap_tier,
                    "secondary_canonical_families": composite_canonicals[:6],
                    "midday_consumed": bool(direct_cross),
                    "still_live_evening": not bool(direct_cross),
                    "explanation": (
                        f"{state_a} profit-alert implied set echoes {state_b}: {', '.join(surfaced[:6])}."
                        if not direct_cross
                        else f"{state_a} profit-alert implied set directly captured {state_b}'s Midday family: {target_winner}."
                    ),
                }
            )
    relationships.sort(
        key=lambda item: (
            -_relationship_score(item),
            str(item.get("relationship_type") or ""),
            str(item.get("state_a") or ""),
            str(item.get("state_b") or ""),
        )
    )
    return relationships


def _build_board_summary(
    *,
    state_order: Sequence[str],
    summaries_by_state: Dict[str, Dict[str, Any]],
    relationships: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    pair_scores: Dict[Tuple[str, str], int] = defaultdict(int)
    pair_types: Dict[Tuple[str, str], Set[str]] = defaultdict(set)
    state_overlap_counts: Dict[str, int] = defaultdict(int)
    state_overlap_scores: Dict[str, int] = defaultdict(int)
    state_direct_cross_hits: Dict[str, int] = defaultdict(int)
    state_primary_overlap_hits: Dict[str, int] = defaultdict(int)
    for row in relationships:
        state_a = str(row.get("state_a") or "")
        state_b = str(row.get("state_b") or "")
        if not state_a or not state_b:
            continue
        key = tuple(sorted((state_a, state_b)))
        relationship_score = _relationship_score(row)
        pair_scores[key] += relationship_score
        pair_types[key].add(str(row.get("relationship_type") or ""))
        state_overlap_counts[state_a] += 1
        state_overlap_counts[state_b] += 1
        state_overlap_scores[state_a] += relationship_score
        state_overlap_scores[state_b] += relationship_score
        if str(row.get("directness") or "") == "direct-cross-state":
            state_direct_cross_hits[state_a] += 1
            state_direct_cross_hits[state_b] += 1
        if str(row.get("overlap_tier") or "primary") == "primary":
            state_primary_overlap_hits[state_a] += 1
            state_primary_overlap_hits[state_b] += 1

    strongest_overlap_pairs = [
        {
            "state_a": key[0],
            "state_b": key[1],
            "pair_score": score,
            "relationship_types": sorted(pair_types.get(key) or []),
        }
        for key, score in sorted(pair_scores.items(), key=lambda item: (-item[1], item[0]))
    ][:10]

    likely_duplicated_pairs = [
        row
        for row in strongest_overlap_pairs
        if row.get("pair_score", 0) >= 2 or len(row.get("relationship_types") or []) >= 2
    ][:10]

    input_order_by_state = {state_key: index for index, state_key in enumerate(state_order, start=1)}
    state_role_hints: List[Dict[str, Any]] = []
    board_scoreboard: List[Dict[str, Any]] = []
    for state_key in state_order:
        summary = summaries_by_state[state_key]
        midday_status = summary.get("midday_status") if isinstance(summary.get("midday_status"), dict) else {}
        spent_status = str(midday_status.get("spent_status") or "unknown")
        overlap_count = _to_int(state_overlap_counts.get(state_key), default=0)
        overlap_score = _to_int(state_overlap_scores.get(state_key), default=0)
        direct_cross_hits = _to_int(state_direct_cross_hits.get(state_key), default=0)
        primary_overlap_hits = _to_int(state_primary_overlap_hits.get(state_key), default=0)
        if spent_status == "locally_spent":
            role = "low_priority"
        elif spent_status == "mostly_unspent" and overlap_score <= 8:
            role = "clean_host"
        elif spent_status == "mostly_unspent":
            role = "shared_host"
        elif spent_status == "cross_state_spent" and direct_cross_hits > 0:
            role = "echo"
        elif spent_status == "cross_state_spent":
            role = "composite_interest"
        elif overlap_count > 0:
            role = "shared_host"
        else:
            role = "low_priority"
        input_order = input_order_by_state[state_key]
        rank_points = (len(state_order) - input_order + 1) * 10
        spent_adjustment = {
            "mostly_unspent": 6,
            "cross_state_spent": 2,
            "lane_spent": -3,
            "locally_spent": -10,
        }.get(spent_status, 0)
        priority_score = rank_points + spent_adjustment + (direct_cross_hits * 2) - min(12, overlap_score // 4)
        state_role_hints.append(
            {
                "state_key": state_key,
                "role": role,
                "overlap_count": overlap_count,
                "overlap_score": overlap_score,
                "primary_overlap_hits": primary_overlap_hits,
                "direct_cross_hits": direct_cross_hits,
                "spent_status": spent_status,
            }
        )
        board_scoreboard.append(
            {
                "state_key": state_key,
                "role": role,
                "spent_status": spent_status,
                "evening_bias": str(midday_status.get("evening_bias") or ""),
                "overlap_count": overlap_count,
                "overlap_score": overlap_score,
                "primary_overlap_hits": primary_overlap_hits,
                "direct_cross_hits": direct_cross_hits,
                "input_order": input_order,
                "legacy_priority_score": priority_score,
            }
        )

    cleanest_unspent_states = [
        row
        for row in sorted(
            state_role_hints,
            key=lambda item: (
                0 if item.get("spent_status") == "mostly_unspent" else 1,
                item.get("overlap_score", 0),
                str(item.get("state_key") or ""),
            ),
        )
        if row.get("spent_status") in {"mostly_unspent", "cross_state_spent"}
    ][:10]

    legacy_ranked = sorted(
        board_scoreboard,
        key=lambda item: (
            -_to_int(item.get("legacy_priority_score"), default=0),
            _to_int(item.get("input_order"), default=999),
            str(item.get("state_key") or ""),
        )
    )
    legacy_rank_by_state = {
        str(row.get("state_key") or ""): rank
        for rank, row in enumerate(legacy_ranked, start=1)
    }
    for row in board_scoreboard:
        row.update(
            legacy_rank_fields(
                input_order=_to_int(row.get("input_order"), default=999),
                legacy_static_rank=legacy_rank_by_state[str(row.get("state_key") or "")],
                legacy_priority_score=_to_int(row.get("legacy_priority_score"), default=0),
            )
        )
    board_scoreboard.sort(key=lambda item: (_to_int(item.get("input_order"), 999), str(item.get("state_key") or "")))

    return {
        "strongest_overlap_pairs": strongest_overlap_pairs,
        "likely_duplicated_pairs": likely_duplicated_pairs,
        "state_role_hints": state_role_hints,
        "cleanest_unspent_states": cleanest_unspent_states,
        "board_scoreboard": board_scoreboard,
    }


def build_board_spillover_overlay_payload(
    *,
    day_dir: Path,
    results_date: str,
    states: Sequence[str],
    profile: str,
    experiment_tag: str,
    board_name: str,
    sharepacks_root: Path,
    repo_root: Path,
    midday_results_path: Optional[Path] = None,
    top_items: int = 8,
) -> Dict[str, Any]:
    state_order = [str(state).strip() for state in states if str(state).strip()]
    if not state_order:
        raise ValueError("states is required")

    raw_profit_alert_rows, profit_alert_path = _load_profit_alert_rows(day_dir, state_order)
    alias_map = _build_state_alias_map(state_order, raw_profit_alert_rows)
    midday_results = _parse_midday_results(midday_results_path, alias_map)

    summaries_by_state: Dict[str, Dict[str, Any]] = {}
    evidence_paths: List[Path] = []
    for rank, state_key in enumerate(state_order, start=1):
        state_dir = day_dir / state_key
        arena_path = _find_arena_path(state_dir, profile, experiment_tag)
        if arena_path is None:
            raise FileNotFoundError(f"Aggregated arena not found for {state_key} under {state_dir / 'analysis'}")
        payload = _read_json(arena_path)
        if not isinstance(payload, dict):
            raise ValueError(f"Aggregated arena payload is not a dict: {arena_path}")
        evidence_paths.append(arena_path)
        summary = _build_state_summary(
            state_key=state_key,
            input_rank=rank,
            payload=payload,
            raw_profit_alert_rows=raw_profit_alert_rows,
            top_items=top_items,
        )
        summaries_by_state[state_key] = summary

    if profit_alert_path is not None:
        evidence_paths.append(profit_alert_path)
    if midday_results_path is not None and midday_results_path.exists():
        evidence_paths.append(midday_results_path)

    for state_key in state_order:
        summaries_by_state[state_key]["midday_status"] = _midday_status_for_state(
            state_key=state_key,
            summary=summaries_by_state[state_key],
            midday_results=midday_results,
            summaries_by_state=summaries_by_state,
        )

    relationships = _build_relationships(
        state_order=state_order,
        summaries_by_state=summaries_by_state,
        midday_results=midday_results,
    )
    board_summary = _build_board_summary(
        state_order=state_order,
        summaries_by_state=summaries_by_state,
        relationships=relationships,
    )

    unique_inputs: List[Path] = []
    seen: Set[str] = set()
    for path in evidence_paths:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique_inputs.append(path)

    return {
        "schema_version": "board_spillover_overlay_v1",
        "metadata": {
            "generated_at": _now_utc_iso(),
            "results_date": results_date,
            "profile": profile,
            "experiment_tag": experiment_tag,
            "board_name": board_name,
            "sharepack_root": _safe_rel(sharepacks_root, repo_root),
            "states": state_order,
            "midday_results_path": _safe_rel(midday_results_path, repo_root) if midday_results_path and midday_results_path.exists() else None,
            "rank_integrity_status": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        },
        "provenance": {
            "inputs_hash": _hash_inputs(unique_inputs),
            "evidence_paths": [_safe_rel(path, repo_root) for path in unique_inputs],
            "contract_refs": [
                "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md",
                "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_FINDINGS_RELATIONSHIP_LAYER__ARENA_BRANCH.md",
                "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md",
            ],
        },
        "board_context": {
            "midday_results_available": bool(midday_results),
            "midday_results": midday_results,
        },
        "rank_contract": unavailable_rank_contract(),
        "display_order_contract": {
            "display_order_source": DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
            "display_order_is_analytical": False,
        },
        "state_summaries": [summaries_by_state[state_key] for state_key in state_order],
        "relationships": relationships,
        "board_summary": board_summary,
    }


def build_board_spillover_overlay_markdown(payload: Dict[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    board_context = payload.get("board_context") if isinstance(payload.get("board_context"), dict) else {}
    state_summaries = payload.get("state_summaries") if isinstance(payload.get("state_summaries"), list) else []
    relationships = payload.get("relationships") if isinstance(payload.get("relationships"), list) else []
    board_summary = payload.get("board_summary") if isinstance(payload.get("board_summary"), dict) else {}
    provenance = payload.get("provenance") if isinstance(payload.get("provenance"), dict) else {}

    lines: List[str] = []
    lines.append(f"# Board Spillover Overlay — {metadata.get('board_name', 'Board')} — D={metadata.get('results_date', '?')}")
    lines.append("")
    lines.append("Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.")
    lines.append("")
    lines.append("**RANK INTEGRITY STATUS: `INVALID_STATIC_ORDER`.** Legacy rank/priority fields are diagnostic receipts only; analytical state rank is unavailable and contributes `0.0`.")
    lines.append("**DISPLAY ORDER:** `INPUT_ROSTER_NON_ANALYTICAL`; navigation only, with no analytical meaning.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- schema_version: `{payload.get('schema_version', '')}`")
    lines.append(f"- profile: `{metadata.get('profile') or '-'}`")
    lines.append(f"- experiment_tag: `{metadata.get('experiment_tag') or '-'}`")
    lines.append(f"- midday_results_available: `{board_context.get('midday_results_available')}`")
    lines.append(f"- inputs_hash: `{str(provenance.get('inputs_hash') or '')[:16]}`")

    lines.append("")
    lines.append("## State Summaries")
    lines.append("")
    lines.append("| Input Order | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |")
    lines.append("|---:|---|---|---|---|---|---|---|")
    role_map = {
        str(row.get("state_key") or ""): str(row.get("role") or "")
        for row in (board_summary.get("state_role_hints") or [])
        if isinstance(row, dict)
    }
    for row in state_summaries:
        if not isinstance(row, dict):
            continue
        state_key = str(row.get("state_key") or "")
        midday = row.get("midday_status") if isinstance(row.get("midday_status"), dict) else {}
        ba = row.get("blackapple_statuses") if isinstance(row.get("blackapple_statuses"), list) else []
        ba_text = ", ".join(
            f"{item.get('variant')}:{item.get('status')}/{item.get('ba_score')}"
            for item in ba[:3]
            if isinstance(item, dict)
        ) or "-"
        lines.append(
            f"| {row.get('input_rank')} | {state_key} | {', '.join(row.get('dominant_canonicals') or []) or '-'} | {', '.join(row.get('dominant_vtrac_indices') or []) or '-'} | {midday.get('spent_status') or '-'} | {midday.get('evening_bias') or '-'} | {role_map.get(state_key) or '-'} | {ba_text} |"
        )

    scoreboard = board_summary.get("board_scoreboard") if isinstance(board_summary.get("board_scoreboard"), list) else []
    if scoreboard:
        lines.append("")
        lines.append("## Legacy Board Priority Receipt")
        lines.append("")
        lines.append("| Input Order | Legacy Rank | State | Legacy Priority | Analytical Rank | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |")
        lines.append("|---:|---:|---|---:|---:|---|---|---|---:|---:|---:|")
        for row in scoreboard[:10]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"| {row.get('input_order')} | {row.get('legacy_static_rank')} | {row.get('state_key')} | {row.get('legacy_priority_score')} | {row.get('analytical_rank') or '-'} | {row.get('role')} | {row.get('spent_status')} | {row.get('evening_bias') or '-'} | {row.get('overlap_score')} | {row.get('primary_overlap_hits')} | {row.get('direct_cross_hits')} |"
            )

    if relationships:
        lines.append("")
        lines.append("## Relationships")
        lines.append("")
        lines.append("| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |")
        lines.append("|---|---|---|---|---|---|---|---:|---:|---|---|")
        for row in relationships[:40]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"| {row.get('state_a')} | {row.get('state_b')} | {row.get('relationship_type')} | {row.get('directness')} | {row.get('overlap_tier') or '-'} | {', '.join(row.get('vtrac_indices') or []) or '-'} | {', '.join(row.get('canonical_families') or []) or '-'} | {row.get('support_count')} | {_relationship_score(row)} | {row.get('midday_consumed')} | {row.get('still_live_evening')} |"
            )

    strongest_pairs = board_summary.get("strongest_overlap_pairs") if isinstance(board_summary.get("strongest_overlap_pairs"), list) else []
    if strongest_pairs:
        lines.append("")
        lines.append("## Strongest Overlap Pairs")
        lines.append("")
        for row in strongest_pairs[:10]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_a')} ↔ {row.get('state_b')}` score=`{row.get('pair_score')}` types=`{', '.join(row.get('relationship_types') or []) or '-'}`"
            )

    cleanest = board_summary.get("cleanest_unspent_states") if isinstance(board_summary.get("cleanest_unspent_states"), list) else []
    if cleanest:
        lines.append("")
        lines.append("## Cleanest Unspent States")
        lines.append("")
        for row in cleanest[:10]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_key')}` role=`{row.get('role')}` spent=`{row.get('spent_status')}` overlap_score=`{row.get('overlap_score')}`"
            )

    return "\n".join(lines).rstrip() + "\n"


def write_board_spillover_overlay_files(
    *,
    out_json_path: Path,
    payload: Dict[str, Any],
    write_md: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_json_path.parent.mkdir(parents=True, exist_ok=True)
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path: Optional[Path] = None
    if write_md:
        md_path = out_json_path.with_suffix(".md")
        md_path.write_text(build_board_spillover_overlay_markdown(payload), encoding="utf-8")
    return out_json_path, md_path


def _default_out_name(results_date: str, board_name: str) -> str:
    return f"{results_date}__BOARD_SPILLOVER_OVERLAY__{_slugify(board_name)}.json"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Build a board spillover overlay from per-state aggregated arenas.")
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--date", required=True)
    ap.add_argument("--states", nargs="+", required=True)
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--board-name", default="board")
    ap.add_argument("--midday-results")
    ap.add_argument("--top-items", type=int, default=8)
    ap.add_argument("--out-dir", default="docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA")
    ap.add_argument("--no-md", action="store_true")
    args = ap.parse_args(argv)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Day directory not found: {day_dir}")

    midday_results_path = Path(args.midday_results).resolve() if args.midday_results else None
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()

    payload = build_board_spillover_overlay_payload(
        day_dir=day_dir,
        results_date=args.date,
        states=args.states,
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        board_name=args.board_name,
        sharepacks_root=sharepacks_root,
        repo_root=REPO_ROOT,
        midday_results_path=midday_results_path,
        top_items=int(args.top_items),
    )
    out_json = out_dir / _default_out_name(args.date, args.board_name)
    json_path, md_path = write_board_spillover_overlay_files(
        out_json_path=out_json,
        payload=payload,
        write_md=not args.no_md,
    )
    print(f"[ok] overlay -> {_safe_rel(json_path)}")
    if md_path is not None:
        print(f"     md -> {_safe_rel(md_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
