from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
import re
import unicodedata

from pathlib import Path

from utils import path_handler as ph

STATE_ORDER: Tuple[str, ...] = (
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maryland",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Nebraska",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "Ohio",
    "Oklahoma",
    "Ontario",
    "Pennsylvania",
    "Puerto Rico",
    "Quebec",
    "South Carolina",
    "Tennessee",
    "Texas",
    "Tri-State (ME, NH & VT)",
    "Virginia",
    "Washington",
    "Washington, D.C.",
    "West Virginia",
    "Western Canada",
    "Wisconsin",
)

# Each entry maps the canonical state label (as it appears in STATE_ORDER)
# to the candidate project-level state identifiers (the folder names used by the
# analysis pipeline). The first entry in each tuple is preferred; additional items
# act as fallbacks for legacy directory names.
_PROJECT_STATE_CANDIDATES: Dict[str, Tuple[str, ...]] = {
    "Connecticut": ("Connecticut4",),
    "Delaware": ("Delaware4",),
    "Florida": ("Florida4",),
    "Georgia": ("Georgia4",),
    "Indiana": ("Indiana4",),
    "Michigan": ("Michigan4",),
    "New Jersey": ("NewJersey4",),
    "New York": ("NewYork4",),
    "North Carolina": ("NorthCarolina4",),
    "Ohio": ("Ohio4",),
    "Ontario": ("Ontario4", "OntarioCanada4"),
    "Pennsylvania": ("Pennsylvania4",),
    "Puerto Rico": ("PuertoRico4",),
    "South Carolina": ("SouthCarolina4",),
    "Texas": ("Texas4",),
    "Virginia": ("Virginia4",),
    "West Virginia": ("WestVirginia4",),
}


def _normalize_token(label: str) -> str:
    if not label:
        return ""
    text = unicodedata.normalize("NFKD", label)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", text.lower())


# Build lookup maps for canonical labels.
_STATE_LOOKUP: Dict[str, str] = {
    _normalize_token(label): label for label in STATE_ORDER
}


@dataclass
class ParsedWinnerEntry:
    label: str
    canonical: str
    project_state: Optional[str]
    midday: Optional[str]
    evening: Optional[str]
    raw_digits: Tuple[str, ...]

    @property
    def tracked(self) -> bool:
        return self.project_state is not None

    def winners(self) -> List[str]:
        seen = []
        for winner in (self.midday, self.evening):
            if winner and winner not in seen:
                seen.append(winner)
        return seen


def resolve_project_state(canonical: str) -> Optional[str]:
    candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
    if not candidates:
        return None
    tables_root = Path(ph.get_tables_output_dir())
    for candidate in candidates:
        if (tables_root / candidate).exists():
            return candidate
    return candidates[0] if candidates else None


def parse_winner_sheet(text: str) -> List[ParsedWinnerEntry]:
    if not text or not text.strip():
        return []
    pattern = re.compile(
        "(" + "|".join(re.escape(label) for label in STATE_ORDER) + ")",
        flags=re.IGNORECASE,
    )
    parts = pattern.split(text)
    if len(parts) <= 1:
        return []
    entries: List[ParsedWinnerEntry] = []
    for idx in range(1, len(parts), 2):
        label = parts[idx].strip()
        chunk = parts[idx + 1] if idx + 1 < len(parts) else ""
        canonical = _STATE_LOOKUP.get(_normalize_token(label), label)
        digits = tuple(re.findall(r"\d{3}", chunk))
        midday = digits[0] if len(digits) >= 1 else None
        evening = digits[1] if len(digits) >= 2 else None
        project_state = resolve_project_state(canonical)
        entries.append(
            ParsedWinnerEntry(
                label=label,
                canonical=canonical,
                project_state=project_state,
                midday=midday,
                evening=evening,
                raw_digits=digits,
            )
        )
    return entries


def filter_tracked(entries: Sequence[ParsedWinnerEntry]) -> List[ParsedWinnerEntry]:
    return [entry for entry in entries if entry.tracked]


def run_winner_reports(entries: Sequence[ParsedWinnerEntry]) -> List[Dict[str, str]]:
    from modules.winner_report_full import write_winner_full_report  # local import

    results: List[Dict[str, str]] = []
    for entry in entries:
        state = entry.project_state
        if not state:
            continue
        for label, winner in (("Midday", entry.midday), ("Evening", entry.evening)):
            if not winner:
                continue
            record: Dict[str, str] = {
                "state": state,
                "label": label,
                "winner": winner,
            }
            try:
                out_path = write_winner_full_report(state, winner)
            except Exception as exc:  # pragma: no cover - rely on smoke tests
                record["error"] = str(exc)
            else:
                record["path"] = out_path
            results.append(record)
    return results


def run_stable_bundles(
    entries: Sequence[ParsedWinnerEntry],
    *,
    min_occ: int = 3,
    bundle_stamp: Optional[str] = None,
    write_bundle: bool = True,
) -> List[Dict[str, object]]:
    from src.core import stable_pattern_extractor as stable  # local import

    results: List[Dict[str, object]] = []
    for entry in entries:
        state = entry.project_state
        if not state:
            continue
        tables_dir = Path(ph.get_state_tables_dir(state))
        out_dir = Path(ph.get_analysis_dir("patterns", state))
        winners = entry.winners()
        record: Dict[str, object] = {
            "state": state,
            "winners": winners,
        }
        try:
            df, html_path, csv_path = stable.run_stable_pattern_extraction(
                state=state,
                tables_path=tables_dir,
                out_path=out_dir,
                min_occ=min_occ,
                winners=winners or None,
                bundle_stamp=bundle_stamp,
                write_bundle=write_bundle,
            )
        except Exception as exc:  # pragma: no cover - integration tested via smokes
            record["error"] = str(exc)
        else:
            record.update(
                {
                    "patterns": int(len(df)),
                    "html": html_path,
                    "csv": csv_path,
                }
            )
            if write_bundle:
                bundle_info = getattr(df, "attrs", {}).get("training_bundle")
                if bundle_info:
                    record["bundle_dir"] = bundle_info.get("bundle_dir")
                    record["manifest"] = bundle_info.get("manifest")
        results.append(record)
    return results

