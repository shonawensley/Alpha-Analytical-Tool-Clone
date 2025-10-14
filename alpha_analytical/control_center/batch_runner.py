from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata

from pathlib import Path

import pandas as pd
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

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
    min_occ: int = 1,
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
            attrs = getattr(df, "attrs", {})
            metrics_data = attrs.get("metrics")
            metrics_path = attrs.get("metrics_path")
            if metrics_data:
                record["metrics"] = metrics_data
            if metrics_path:
                record["metrics_path"] = metrics_path
            families_path = attrs.get("families_path")
            if winners and csv_path:
                try:
                    from alpha_analytical.stable.winners_enrich import attach_stable_evidence

                    winners_frame = pd.DataFrame([{"Winner": w} for w in winners])
                    evidence_df = attach_stable_evidence(
                        winners_frame,
                        families_path=families_path,
                        scores_path=csv_path,
                    )
                    record["winners_evidence"] = evidence_df.to_dict(orient="records")
                except Exception:  # pragma: no cover - defensive; evidence is supplemental
                    pass
            if write_bundle:
                bundle_info = getattr(df, "attrs", {}).get("training_bundle")
                if bundle_info:
                    record["bundle_dir"] = bundle_info.get("bundle_dir")
                    record["manifest"] = bundle_info.get("manifest")
        results.append(record)
    return results





def _collect_digit_reduction_winners(entry: ParsedWinnerEntry) -> Dict[str, str]:
    winners: Dict[str, str] = {}
    if entry.midday:
        winners["Midday"] = entry.midday
    if entry.evening:
        winners["Evening"] = entry.evening
    for extra in entry.raw_digits[2:]:
        if len(extra) == 3 and extra.isdigit() and extra not in winners.values():
            winners.setdefault("Combined", extra)
    if winners and "Combined" not in winners:
        winners["Combined"] = winners.get("Midday") or winners.get("Evening") or next(iter(winners.values()))
    return {k: v for k, v in winners.items() if v}


def run_digit_reduction_workflow(
    entries: Sequence[ParsedWinnerEntry],
    *,
    run_reducer: bool = True,
    run_overlay: bool = True,
    run_analyzer: bool = True,
    run_bundle: bool = False,
    bundle_stamp: Optional[str] = None,
    mirror_to_winners: bool = True,
    include_overlay_html: bool = False,
    include_hits: bool = True,
    make_zip: bool = False,
) -> List[Dict[str, object]]:
    analysis_root = Path(ph.get_analysis_output_dir())
    tables_root = Path(ph.get_tables_output_dir())
    stamp_input = bundle_stamp.strip() if isinstance(bundle_stamp, str) else None
    results: List[Dict[str, object]] = []

    reducer_fn = None
    analyzer_fn = None
    overlay_fn = None
    bundle_pkg = None
    bundle_exc = None

    for entry in entries:
        state = entry.project_state
        if not state:
            continue
        state_tables = tables_root / state
        state_dir = Path(ph.get_analysis_dir("digit_reduction", state))
        record: Dict[str, object] = {"state": state, "winners": _collect_digit_reduction_winners(entry)}
        reducer_ok = True

        if run_reducer:
            if reducer_fn is None:
                from core.module_b_digit_reduction import run_digit_reduction as reducer_fn  # type: ignore
            if not state_tables.exists():
                record["reducer"] = {"error": f"Missing tables at {state_tables}"}
                reducer_ok = False
            else:
                try:
                    df, html_path, csv_path = reducer_fn(state, state_tables, out_path=state_dir)
                    record["reducer"] = {"rows": int(len(df)), "html": str(html_path), "csv": str(csv_path)}
                except Exception as exc:  # pragma: no cover - integration tested via acceptance suite
                    record["reducer"] = {"error": str(exc)}
                    reducer_ok = False
        else:
            record["reducer"] = {"skipped": True}

        winners_map = record.get("winners") or {}
        overlay_ok = False
        overlay_result: Dict[str, object] | None = None
        stamp_for_bundle = stamp_input or None

        if run_overlay and winners_map:
            if overlay_fn is None:
                from alpha_analytical.digit_reduction.analyzer_v2.winners_overlay import run_winner_overlay_batch as overlay_fn  # type: ignore
            if reducer_ok or not run_reducer:
                try:
                    overlay_result = overlay_fn(
                        state,
                        {k: str(v) for k, v in winners_map.items()},
                        analysis_root=analysis_root,
                        when=stamp_input,
                        mirror_to_winners=mirror_to_winners,
                    )
                    overlay_ok = True
                    stamp_for_bundle = overlay_result.get("stamp") or stamp_for_bundle
                    variant_details: Dict[str, Dict[str, object]] = {}
                    for variant, payload in (overlay_result.get("results") or {}).items():
                        variant_details[variant] = {
                            "winner": payload.get("winner"),
                            "hits": int(payload.get("hits", 0) or 0),
                            "overlay_html": payload.get("overlay_html"),
                            "flags_csv": payload.get("flags_csv"),
                        }
                    record["overlay"] = {"stamp": overlay_result.get("stamp"), "results": variant_details}
                except Exception as exc:  # pragma: no cover - integration tested via acceptance suite
                    record["overlay"] = {"error": str(exc)}
            else:
                record["overlay"] = {"skipped": "reducer failed"}
        elif run_overlay:
            record["overlay"] = {"skipped": "no winners provided"}
        else:
            record["overlay"] = {"skipped": True}

        analyzer_ok = True
        if run_analyzer:
            if analyzer_fn is None:
                from alpha_analytical.digit_reduction.analyzer_v2 import run as analyzer_fn  # type: ignore
            if reducer_ok or not run_reducer:
                try:
                    info = analyzer_fn(state, analysis_root=analysis_root)
                    analyzer_dir = state_dir / "analyzer_v2"
                    record["analyzer"] = {
                        "rows": int(info.get("rows", 0) or 0),
                        "per_item": str(analyzer_dir / f"{state}_analyzer_v2_per_item.csv"),
                        "top_candidates": str(analyzer_dir / f"{state}_analyzer_v2_top_candidates.csv"),
                    }
                except Exception as exc:  # pragma: no cover - integration tested via acceptance suite
                    record["analyzer"] = {"error": str(exc)}
                    analyzer_ok = False
            else:
                record["analyzer"] = {"skipped": "reducer failed"}
                analyzer_ok = False
        else:
            record["analyzer"] = {"skipped": True}

        if run_bundle:
            if bundle_pkg is None or bundle_exc is None:
                from alpha_analytical.digit_reduction.analyzer_v2 import training_bundle as bundle_pkg  # type: ignore
                from alpha_analytical.digit_reduction.analyzer_v2.training_bundle import TrainingBundleError as bundle_exc  # type: ignore
            if analyzer_ok and overlay_ok:
                try:
                    bundle_result = bundle_pkg.package_training_bundle(
                        state,
                        stamp=stamp_for_bundle,
                        analysis_root=analysis_root,
                        include_overlay=include_overlay_html,
                        include_hits=include_hits,
                        make_zip=make_zip,
                    )
                    record["bundle"] = bundle_result
                except bundle_exc as exc:  # type: ignore
                    record["bundle"] = {"error": str(exc)}
                except Exception as exc:  # pragma: no cover - integration tested via acceptance suite
                    record["bundle"] = {"error": str(exc)}
            else:
                record["bundle"] = {"skipped": "overlay/analyzer unavailable"}
        else:
            record["bundle"] = {"skipped": True}

        results.append(record)

    return results
