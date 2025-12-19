"""Column mappings for Pick3StatsC4.xlsm P3Draws sheet.

Provides canonical state lookup and helpers so downstream extractors can
load Combined, Midday, Evening, and special draw categories without
duplicating hard-coded column letters.
"""

from __future__ import annotations

from typing import Dict, List, Optional

# Locked Combined column letters (existing Aux behaviour).
COMBINED_LOCKED: Dict[str, str] = {
    "Connecticut": "N",
    "Delaware": "O",
    "Florida": "P",
    "Georgia": "Q",
    "Indiana": "T",
    "Michigan": "Y",
    "New Jersey": "AB",
    "New York": "AD",
    "North Carolina": "AE",
    "Ohio": "AF",
    "Ontario": "AG",
    "Pennsylvania": "AH",
    "Puerto Rico": "AI",
    "South Carolina": "AJ",
    "Texas": "AL",
    "Tri-State": "AM",
    "Virginia": "AN",
    "West Virginia": "CF",
}

# Midday column letters (Noon columns normalized into Midday where applicable).
MIDDAY_COL: Dict[str, str] = {
    "Connecticut": "CL",
    "Delaware": "CM",
    "Florida": "CN",
    "Georgia": "CO",
    "Indiana": "CR",
    "Michigan": "CW",
    "New Jersey": "CZ",
    "New York": "DB",
    "North Carolina": "DC",
    "Ohio": "DD",
    "Ontario": "DE",
    "Pennsylvania": "DF",
    "Puerto Rico": "DG",
    "South Carolina": "DH",
    "Texas": "DL",
    "Tri-State": "DM",
    "Virginia": "DN",
}

# Evening column letters (entries may contain multiple draws such as Evening + Nite).
EVENING_COLS: Dict[str, List[str]] = {
    "Connecticut": ["AU"],
    "Delaware": ["AV"],
    "Florida": ["AW"],
    "Georgia": ["AX", "AY"],
    "Indiana": ["BB"],
    "Michigan": ["BH"],
    "New Jersey": ["BM"],
    "New York": ["BO"],
    "North Carolina": ["BP"],
    "Ohio": ["BQ"],
    "Ontario": ["BS"],
    "Pennsylvania": ["BT"],
    "Puerto Rico": ["BU"],
    "South Carolina": ["BW"],
    "Texas": ["BY", "BZ"],
    "Tri-State": ["CA"],
    "Virginia": ["CB"],
    "West Virginia": ["CF"],
}

# Additional draw categories for states with more than two draws per day.
EXTRA_COLS: Dict[str, Dict[str, str]] = {
    "Georgia": {"nite": "AY"},
    "Texas": {"morning": "DK", "noon": "DL", "nite": "BZ"},
}

_TRACKED_STATES: List[str] = sorted(COMBINED_LOCKED.keys())


def _normalize(label: str) -> str:
    """Return a normalized key (alphanumeric lowercase)."""
    return "".join(ch.lower() for ch in label if ch.isalnum())


_CANONICAL_INDEX: Dict[str, str] = {}
for state_name in _TRACKED_STATES:
    key = _normalize(state_name)
    _CANONICAL_INDEX[key] = state_name
    _CANONICAL_INDEX[f"{key}4"] = state_name
    _CANONICAL_INDEX[key.replace("-", "")] = state_name
    _CANONICAL_INDEX[f"{key.replace('-', '')}4"] = state_name


def canonical_state(label: str) -> Optional[str]:
    """Return the canonical state name for a UI/state label."""
    if not label:
        return None
    key = _normalize(label)
    return _CANONICAL_INDEX.get(key)


def state_to_filename(label: str) -> str:
    """Return the standard filename stem for a state (spaces -> underscore)."""
    canonical = canonical_state(label)
    target = canonical if canonical else label.replace("4", "")
    return (
        target.replace(" ", "_")
        .replace("-", "-")
        .replace("(", "")
        .replace(")", "")
    )


def get_tracked_states() -> List[str]:
    """Return the sorted list of canonical states tracked by Aux draws."""
    return list(_TRACKED_STATES)


def get_columns_for(state_label: str, category: str = "combined") -> List[str]:
    """Return Excel column letters for the requested draw category."""
    canonical = canonical_state(state_label)
    if not canonical:
        return []
    category_key = (category or "").lower()

    if category_key == "combined":
        col = COMBINED_LOCKED.get(canonical)
        return [col] if col else []

    if category_key == "midday":
        col = MIDDAY_COL.get(canonical)
        return [col] if col else []

    if category_key == "evening":
        return EVENING_COLS.get(canonical, [])

    if category_key in ("nite", "night"):
        extra = EXTRA_COLS.get(canonical, {})
        col = extra.get("nite")
        return [col] if col else []

    if category_key == "morning":
        extra = EXTRA_COLS.get(canonical, {})
        col = extra.get("morning")
        return [col] if col else []

    if category_key == "noon":
        extra = EXTRA_COLS.get(canonical, {})
        col = extra.get("noon")
        return [col] if col else []

    return []


__all__ = [
    "COMBINED_LOCKED",
    "MIDDAY_COL",
    "EVENING_COLS",
    "EXTRA_COLS",
    "canonical_state",
    "state_to_filename",
    "get_columns_for",
    "get_tracked_states",
]
