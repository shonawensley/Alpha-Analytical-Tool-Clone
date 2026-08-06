#!/usr/bin/env python
"""
Alpha Analytical Tool with V-TRAC Analysis
Provides data processing, table generation, and pattern analysis for numerical datasets
"""

# --- ensure we can import utils.* no matter where Streamlit is launched ---
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
# --------------------------------------------------------------------------

import os
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter
import webbrowser
from PIL import Image
import time
import json  # Added for JSON export
from functools import lru_cache

# Import utility modules
from utils.extract_data import process_state
from utils.table_generator import build_section_table, build_r2_only_table
from utils.path_handler import (
    get_excel_path,
    create_output_directories,
    get_cleaned_data_dir,
    get_tables_output_dir,
    get_winners_output_dir
)
from utils.state_utils import STATES, get_state_file_name
from modules.vtrac_matchers import WinnerTargets, build_winner_targets
from modules.vtrac_straight_map import (
    boxed_index_for_vcode,
    ordered_vcode_for_combo,
    vstraight_lane_for_combo,
)
from modules.vtrac_enhanced.evidence import (
    BoxKey as EvidenceBoxKey,
    build_grid as build_evidence_grid,
    HIGHLIGHT_CLASS,
)
from alpha_analytical.digit_reduction.long_string_windows import get_long_string_boxes
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables
from utils.vtrac_utils import (
    BOXED_VTRAC_REFERENCE,
    find_vtrac_index_and_combos,
    highlight_winners_in_table,
    highlight_string_with_matches
)
from utils.bundler import bundle_day
_LONG_STRING_TABLES = ("midday", "evening", "combined")


def _normalize_set(value: str) -> str:
    return str(value or "").strip().replace(" ", "").lower()


def _normalize_draw(value: str) -> str:
    raw = str(value or "").strip().replace(" ", "")
    if not raw:
        return ""
    raw_lower = raw.lower()
    if raw_lower.startswith("draw"):
        return raw_lower
    if raw.isdigit():
        return f"draw{raw}"
    return raw_lower


def _normalize_row_type(value: str) -> str:
    raw = ''.join(ch for ch in str(value or "") if ch.isalnum())
    return raw.upper()


@lru_cache(maxsize=None)
def _long_string_lookup() -> dict:
    mapping: dict[str, frozenset[tuple[str, str, str, int]]] = {}
    for table in _LONG_STRING_TABLES:
        coords = set()
        for box in get_long_string_boxes(table):
            for set_name in box.sets:
                for draw_name in box.draws:
                    for row_type in box.row_types:
                        for column in box.columns:
                            coords.add(
                                (
                                    _normalize_set(set_name),
                                    _normalize_draw(draw_name),
                                    _normalize_row_type(row_type),
                                    int(column),
                                )
                            )
        mapping[table] = frozenset(coords)
    return mapping


def _is_long_string_cell(
    table_kind: str,
    set_name: str,
    draw_name: str,
    row_type: str,
    column: int,
) -> bool:
    table_key = str(table_kind or "").lower()
    coords = _long_string_lookup().get(table_key)
    if not coords:
        return False
    return (
        _normalize_set(set_name),
        _normalize_draw(draw_name),
        _normalize_row_type(row_type),
        int(column),
    ) in coords

# (Page config now handled centrally in src/app.py)

# ------------------------------------------------------------------------------
# JSON EXPORT FUNCTIONS FOR AI TRAINING
# ------------------------------------------------------------------------------

def get_predictions_output_dir():
    """Get the directory for prediction outputs"""
    output_dir = os.path.join("data", "outputs", "predictions")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def get_winners_json_output_dir():
    """Get the directory for winner JSON outputs"""
    output_dir = os.path.join("data", "outputs", "winners_json")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def save_predictions_as_json(state_name, results, top_n=3):
    """
    Save V-TRAC predictions as JSON for AI training
    
    Args:
        state_name: Name of the state
        results: Analysis results from analyze_all_indexes
        top_n: Number of top predictions to save
    """
    if not results or len(results) == 0:
        return None
    
    # Get today's date
    date_str = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Prepare predictions data
    predictions_data = {
        "date": date_str,
        "timestamp": timestamp,
        "state": state_name,
        "predictions": []
    }
    
    # Add top N predictions
    for i, result in enumerate(results[:top_n]):
        prediction = {
            "rank": i + 1,
            "index": result["index"],
            "score": result["score"],
            "patterns": sorted(list(result["patterns"])),
            "pattern_count": len(result["patterns"])
        }
        predictions_data["predictions"].append(prediction)
    
    # Save to JSON file
    output_dir = get_predictions_output_dir()
    filename = f"{state_name}_{date_str}_predictions.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(predictions_data, f, indent=2)
    
    return filepath

def save_winners_as_json(state_name, midday_winner, evening_winner, date_str=None):
    """
    Save winning numbers as JSON for AI training
    
    Args:
        state_name: Name of the state
        midday_winner: Midday winning number (string)
        evening_winner: Evening winning number (string)
        date_str: Date string (YYYY-MM-DD format), defaults to today
    """
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Prepare winners data
    winners_data = {
        "date": date_str,
        "timestamp": timestamp,
        "state": state_name,
        "winners": {
            "midday": midday_winner if midday_winner else "",
            "evening": evening_winner if evening_winner else ""
        }
    }
    
    # Save to JSON file
    output_dir = get_winners_json_output_dir()
    filename = f"{state_name}_{date_str}_winners.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(winners_data, f, indent=2)
    
    return filepath

def parse_winners_input(winners_text):
    """
    Parse the winners input text format from the document
    Returns a dictionary of state: (midday, evening) tuples
    """
    winners_dict = {}
    lines = winners_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Split by tabs or multiple spaces
        parts = line.split('\t') if '\t' in line else line.split()
        
        if len(parts) >= 2:
            state = parts[0]
            # Handle cases with 2 or 3 columns (midday, evening, or both)
            if len(parts) == 2:
                # Could be just midday or just evening
                winners_dict[state] = (parts[1], "")
            elif len(parts) >= 3:
                winners_dict[state] = (parts[1], parts[2])
        elif len(parts) == 1 and parts[0]:
            # State with no numbers
            winners_dict[parts[0]] = ("", "")
    
    return winners_dict

# ------------------------------------------------------------------------------
# MAIN APP FUNCTIONS (from streamlit_app.py)
# ------------------------------------------------------------------------------

def format_time(seconds):
    """Format time in seconds to human-readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    else:
        minutes = int(seconds // 60)
        sec = seconds % 60
        return f"{minutes} min {sec:.2f} sec"

def check_excel_file():
    """Check if the Excel file exists and return its path"""
    excel_path = get_excel_path()
    excel_exists = os.path.exists(excel_path)
    return excel_path, excel_exists

@st.cache_data(show_spinner=False)
def load_state_data(state_name: str):
    """Load the combined tables for a state from the canonical tables directory."""
    root = Path(get_tables_output_dir())
    if not root.exists():
        print(f"[ERROR] Tables root does not exist: {root}")
        return None

def _normalize_state_slug(state: str) -> str:
    slug = get_state_file_name(state)
    return slug or state


def _ensure_vtrac_session_state() -> None:
    if 'vtrac_results' not in st.session_state:
        st.session_state.vtrac_results = {}
    if 'vtrac_reports' not in st.session_state:
        st.session_state.vtrac_reports = {}
    if 'last_analysis_time' not in st.session_state:
        st.session_state.last_analysis_time = {}


def _clear_vtrac_cache(state: str) -> None:
    _ensure_vtrac_session_state()
    for key in ('vtrac_results', 'vtrac_reports', 'last_analysis_time'):
        cache = st.session_state.get(key)
        if isinstance(cache, dict):
            cache.pop(state, None)


    # Normalise the state slug (Connecticut4 -> Connecticut4, etc.)
    slugs = []
    slug = get_state_file_name(state_name)
    if slug:
        slugs.append(slug)
    if state_name:
        slugs.append(state_name)
    if slug.endswith("4"):
        slugs.append(slug[:-1])

    tables: dict[str, pd.DataFrame] = {}
    for candidate in slugs:
        state_dir = (root / candidate).resolve()
        if not state_dir.exists() or not state_dir.is_dir():
            continue

        combined_tables: dict[str, pd.DataFrame] = {}
        for csv_path in sorted(state_dir.glob("*_combined.csv")):
            parts = csv_path.stem.split("_")
            if len(parts) < 3:
                continue
            section = parts[-2]
            key = f"{section}_combined"
            try:
                combined_tables[key] = pd.read_csv(csv_path)
            except Exception as exc:
                print(f"[ERROR] Failed to load {csv_path}: {exc}")
        if combined_tables:
            return combined_tables

    print(f"[ERROR] No valid combined tables found for {state_name} under {root}")
    return None

# ------------------------------------------------------------------------------
# V-TRAC ANALYZER FUNCTIONS (from vtrac_analyzer.py)
# ------------------------------------------------------------------------------

def get_all_combinations_for_index(index):
    """Get all pattern combinations for a specific V-TRAC index"""
    vtrac_entry = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == index), None)
    
    if vtrac_entry:
        combinations = set()
        combinations.update(vtrac_entry.get("Singles", []))
        combinations.update(vtrac_entry.get("Doubles", []))
        return combinations
    
    return set()

def count_patterns_in_table(df, patterns):
    """Count occurrences of patterns in a table"""
    # Initialize counter
    pattern_counts = {pattern: 0 for pattern in patterns}
    total_matches = 0
    
    # Check each cell for patterns
    for col in ['7', '6', '5', '4', '3', '2', '1']:
        if col in df.columns:
            for value in df[col].astype(str):
                for pattern in patterns:
                    count = value.count(pattern)
                    if count > 0:
                        pattern_counts[pattern] += count
                        total_matches += count
    
    return pattern_counts, total_matches

def analyze_pattern_persistence(df, patterns):
    """Analyze how patterns persist across columns (7-1)"""
    persistence_scores = {pattern: 0 for pattern in patterns}
    
    # Define columns to check
    columns = ['7', '6', '5', '4', '3', '2', '1']
    valid_columns = [col for col in columns if col in df.columns]
    
    # Check each pattern
    for pattern in patterns:
        for _, row in df.iterrows():
            consecutive_count = 0
            max_consecutive = 0
            
            for col in valid_columns:
                if pattern in str(row[col]):
                    consecutive_count += 1
                else:
                    max_consecutive = max(max_consecutive, consecutive_count)
                    consecutive_count = 0
            
            # Check final streak
            max_consecutive = max(max_consecutive, consecutive_count)
            
            # Score based on max consecutive columns (squared to give more weight)
            persistence_scores[pattern] += max_consecutive ** 2
    
    return persistence_scores

def analyze_pattern_stability(df, patterns):
    """Analyze stability of patterns within R2/R4/R6/R8 rows"""
    stability_scores = {pattern: 0 for pattern in patterns}
    
    # Group rows by Set and Draw
    grouped = df.groupby(['Set', 'Draw'])
    
    for _, group in grouped:
        # Skip groups without at least 2 row types
        row_types = group['RowType'].unique()
        if len(row_types) < 2:
            continue
            
        for pattern in patterns:
            row_type_count = 0
            for row_type in ['R2', 'R4', 'R6', 'R8']:
                row_type_rows = group[group['RowType'] == row_type]
                if row_type_rows.empty:
                    continue
                    
                # Check if pattern exists in any column of this row type
                pattern_found = False
                for col in ['7', '6', '5', '4', '3', '2', '1']:
                    if col in df.columns:
                        for value in row_type_rows[col].astype(str):
                            if pattern in value:
                                pattern_found = True
                                break
                    if pattern_found:
                        break
                
                if pattern_found:
                    row_type_count += 1
            
            # Score based on number of row types (squared for weight)
            stability_scores[pattern] += row_type_count ** 2
    
    return stability_scores

def detect_straight_combinations(df, pattern):
    """Detect instances where a pattern appears in the same order multiple times"""
    straight_count = 0
    
    columns = ['7', '6', '5', '4', '3', '2', '1']
    valid_columns = [col for col in columns if col in df.columns]
    
    for _, row in df.iterrows():
        occurrences = 0
        for col in valid_columns:
            if pattern in str(row[col]):
                occurrences += 1
        
        # If pattern appears multiple times in the same row, count as straight
        if occurrences > 1:
            straight_count += occurrences
    
    return straight_count


_REPORT_VARIANTS = ("Midday", "Evening", "Combined")
_REPORT_PATTERN_ROWS = frozenset({"R2", "R4", "R6", "R8"})
_REPORT_NUMERIC_COLUMNS = ("7", "6", "5", "4", "3", "2", "1")


def _report_population(df, population):
    """Return one explicit winner-report row population."""
    if df is None or df.empty or "RowType" not in df.columns:
        return df.iloc[0:0].copy() if df is not None else pd.DataFrame()
    row_types = df["RowType"].astype(str)
    if population == "r_pattern":
        return df[row_types.isin(_REPORT_PATTERN_ROWS)].copy()
    if population == "draw_data":
        return df[row_types == "draw_data"].copy()
    raise ValueError(f"Unsupported report population: {population}")


def _report_occurrence_details(df, patterns):
    """Count raw occurrences and unique pattern/cell locations."""
    ordered_patterns = sorted({str(pattern) for pattern in patterns})
    occurrence = {pattern: 0 for pattern in ordered_patterns}
    locations = {pattern: set() for pattern in ordered_patterns}
    if df is None or df.empty:
        return occurrence, {pattern: 0 for pattern in ordered_patterns}

    for row_position, (_, row) in enumerate(df.iterrows()):
        for column in _REPORT_NUMERIC_COLUMNS:
            if column not in df.columns:
                continue
            text = str(row[column])
            for pattern in ordered_patterns:
                count = text.count(pattern)
                if not count:
                    continue
                occurrence[pattern] += count
                locations[pattern].add(
                    (
                        row_position,
                        str(row.get("Set", "")),
                        str(row.get("Draw", "")),
                        str(row.get("RowType", "")),
                        column,
                    )
                )
    return occurrence, {
        pattern: len(pattern_locations)
        for pattern, pattern_locations in locations.items()
    }


def _report_population_statistics(df, patterns, population):
    """Build report-only statistics for one declared row population."""
    population_df = _report_population(df, population)
    occurrence, unique_locations = _report_occurrence_details(
        population_df, patterns
    )
    if population_df.empty:
        persistence = {pattern: 0 for pattern in patterns}
        straight_counts = {pattern: 0 for pattern in patterns}
        stability = (
            {pattern: 0 for pattern in patterns}
            if population == "r_pattern"
            else {}
        )
    else:
        persistence = analyze_pattern_persistence(population_df, patterns)
        straight_counts = {
            pattern: detect_straight_combinations(population_df, pattern)
            for pattern in patterns
        }
        stability = (
            analyze_pattern_stability(population_df, patterns)
            if population == "r_pattern"
            else {}
        )
    if population == "r_pattern":
        stability_status = "APPLICABLE_R2_R4_R6_R8_ONLY"
    else:
        stability_status = "NOT_APPLICABLE_TO_DRAW_DATA"

    return {
        "population": population,
        "included_row_types": (
            sorted(_REPORT_PATTERN_ROWS)
            if population == "r_pattern"
            else ["draw_data"]
        ),
        "row_count": int(len(population_df.index)),
        "numeric_cell_count": int(
            len(population_df.index)
            * sum(column in population_df.columns for column in _REPORT_NUMERIC_COLUMNS)
        ),
        "pattern_occurrence": occurrence,
        "pattern_occurrence_total": int(sum(occurrence.values())),
        "pattern_unique_locations": unique_locations,
        "pattern_unique_location_total": int(sum(unique_locations.values())),
        "unique_pattern_identities_present": sorted(
            pattern for pattern, count in occurrence.items() if count
        ),
        "pattern_persistence": persistence,
        "pattern_stability": stability,
        "pattern_stability_status": stability_status,
        "straight_counts": straight_counts,
    }


def _aggregate_report_populations(variant_stats, population):
    """Aggregate variants without claiming independent corroboration."""
    occurrence = Counter()
    unique_locations = Counter()
    variants_present = {}
    persistence = Counter()
    stability = Counter()
    straight_counts = Counter()

    all_patterns = sorted(
        {
            pattern
            for variant in _REPORT_VARIANTS
            for pattern in variant_stats[variant][population][
                "pattern_occurrence"
            ]
        }
    )
    for pattern in all_patterns:
        present = []
        for variant in _REPORT_VARIANTS:
            stats = variant_stats[variant][population]
            occurrence[pattern] += stats["pattern_occurrence"].get(pattern, 0)
            unique_locations[pattern] += stats["pattern_unique_locations"].get(
                pattern, 0
            )
            persistence[pattern] += stats["pattern_persistence"].get(pattern, 0)
            stability[pattern] += stats["pattern_stability"].get(pattern, 0)
            straight_counts[pattern] += stats["straight_counts"].get(pattern, 0)
            if stats["pattern_occurrence"].get(pattern, 0):
                present.append(variant)
        variants_present[pattern] = present

    return {
        "population": population,
        "aggregation": "SUM_ACROSS_SEPARATELY_ATTRIBUTED_VARIANTS",
        "pattern_occurrence": dict(occurrence),
        "all_variant_occurrence_total": int(sum(occurrence.values())),
        "pattern_unique_locations": dict(unique_locations),
        "all_variant_unique_locations": int(sum(unique_locations.values())),
        "variants_present": variants_present,
        "unique_pattern_identities_present": sorted(
            pattern for pattern, count in occurrence.items() if count
        ),
        "pattern_persistence_sum": dict(persistence),
        "pattern_stability_sum": (
            dict(stability) if population == "r_pattern" else {}
        ),
        "straight_counts_sum": dict(straight_counts),
        "independence_warning": (
            "Variant sums are descriptive. Midday, Evening, and Combined are "
            "related views and do not become independent support merely by "
            "being added."
        ),
    }


def build_report_statistics(tables, patterns):
    """Build explicit per-variant report statistics without changing scoring."""
    variant_stats = {}
    for variant in _REPORT_VARIANTS:
        df = tables.get(f"{variant}_combined")
        variant_stats[variant] = {
            population: _report_population_statistics(df, patterns, population)
            for population in ("r_pattern", "draw_data")
        }

    combined = tables.get("Combined_combined")
    if combined is None or combined.empty:
        legacy = {
            "pattern_occurrence": {},
            "pattern_persistence": {},
            "pattern_stability": {},
            "straight_counts": {},
        }
    else:
        occurrence, _ = count_patterns_in_table(combined, patterns)
        legacy = {
            "pattern_occurrence": occurrence,
            "pattern_persistence": analyze_pattern_persistence(combined, patterns),
            "pattern_stability": analyze_pattern_stability(combined, patterns),
            "straight_counts": {
                pattern: detect_straight_combinations(combined, pattern)
                for pattern in patterns
            },
        }

    return {
        "schema_version": "winner_report_statistics_v2",
        "contract": {
            "variant_scopes": list(_REPORT_VARIANTS),
            "row_populations": {
                "r_pattern": sorted(_REPORT_PATTERN_ROWS),
                "draw_data": ["draw_data"],
            },
            "occurrence_denominator": (
                "Raw contiguous substring occurrences in numeric cells."
            ),
            "unique_location_denominator": (
                "Unique variant/row/column cells containing each pattern."
            ),
            "all_variant_semantics": (
                "Descriptive sum across separately attributed related variants; "
                "not independent support or stability."
            ),
            "legacy_stats_semantics": (
                "Combined variant, R-pattern and draw_data rows mixed. Preserved "
                "for compatibility only."
            ),
        },
        "variants": variant_stats,
        "all_variant": {
            population: _aggregate_report_populations(
                variant_stats, population
            )
            for population in ("r_pattern", "draw_data")
        },
        "legacy_combined_all_rows": legacy,
    }


def _ordered_lane_locations(df, members, population):
    population_df = _report_population(df, population)
    counts = {member: 0 for member in members}
    locations = []
    for row_position, (_, row) in enumerate(population_df.iterrows()):
        for column in _REPORT_NUMERIC_COLUMNS:
            if column not in population_df.columns:
                continue
            raw_value = str(row[column])
            text = "".join(char for char in raw_value if char.isdigit())
            for member in members:
                start = 0
                while True:
                    offset = text.find(member, start)
                    if offset < 0:
                        break
                    counts[member] += 1
                    locations.append(
                        {
                            "row_position": row_position,
                            "set": str(row.get("Set", "")),
                            "draw": str(row.get("Draw", "")),
                            "row_type": str(row.get("RowType", "")),
                            "column": int(column),
                            "member": member,
                            "raw_cell": raw_value,
                            "normalized_cell": text,
                            "start_offset": offset,
                        }
                    )
                    start = offset + 1
    return {
        "member_occurrence": counts,
        "occurrence_total": int(sum(counts.values())),
        "unique_location_total": len(
            {
                (
                    location["row_position"],
                    location["column"],
                    location["member"],
                    location["start_offset"],
                )
                for location in locations
            }
        ),
        "locations": locations,
    }


def build_ordered_lane_report(winner_combo, tables, legacy_vt_pair=None):
    """Build a generic modern ordered-lane report for any Pick-3 winner."""
    vcode = ordered_vcode_for_combo(winner_combo)
    members = vstraight_lane_for_combo(winner_combo)
    if not vcode or not members:
        return {
            "status": "UNAVAILABLE_INVALID_WINNER",
            "winner_literal": winner_combo,
            "ordered_vcode": None,
            "lane_members": [],
            "legacy_marker": {
                "status": "AVAILABLE" if legacy_vt_pair else "UNAVAILABLE",
                "vt_pair": list(legacy_vt_pair) if legacy_vt_pair else None,
            },
        }

    variants = {}
    for variant in _REPORT_VARIANTS:
        df = tables.get(f"{variant}_combined")
        variants[variant] = {
            population: _ordered_lane_locations(df, members, population)
            for population in ("r_pattern", "draw_data")
        }

    all_variant = {}
    for population in ("r_pattern", "draw_data"):
        member_counts = Counter()
        variants_present = []
        for variant in _REPORT_VARIANTS:
            stats = variants[variant][population]
            member_counts.update(stats["member_occurrence"])
            if stats["occurrence_total"]:
                variants_present.append(variant)
        all_variant[population] = {
            "member_occurrence": dict(member_counts),
            "all_variant_occurrence_total": int(sum(member_counts.values())),
            "all_variant_unique_locations": int(
                sum(
                    variants[variant][population]["unique_location_total"]
                    for variant in _REPORT_VARIANTS
                )
            ),
            "variants_present": variants_present,
            "independence_warning": (
                "Variant totals are descriptive and are not independent support."
            ),
        }

    return {
        "status": "AVAILABLE",
        "winner_literal": str(winner_combo),
        "ordered_vcode": vcode,
        "boxed_vtrac_index": boxed_index_for_vcode(vcode),
        "lane_members": members,
        "counting_contract": {
            "r_pattern": sorted(_REPORT_PATTERN_ROWS),
            "draw_data": ["draw_data"],
            "match": "contiguous literal occurrence in digits-only cell text",
        },
        "variants": variants,
        "all_variant": all_variant,
        "legacy_marker": {
            "status": "AVAILABLE" if legacy_vt_pair else "UNAVAILABLE",
            "vt_pair": list(legacy_vt_pair) if legacy_vt_pair else None,
            "definition": (
                "Historical two-distinct-VTRAC run marker. It is preserved but "
                "is not the modern ordered three-position lane."
            ),
        },
    }

def calculate_index_score(tables: dict, patterns: set) -> float:
    """Compute a combined weighting across Midday, Evening, Combined."""
    if not tables or not patterns:
        return 0
    # Weighted references
    table_weights = {
        "Combined_combined": 3.0,
        "Midday_combined":   1.5,
        "Evening_combined":  1.5
    }
    occ_score = 0
    pers_score = 0
    stab_score = 0
    straight_score = 0
    found_tables = 0

    for tkey, weight in table_weights.items():
        df = tables.get(tkey)
        if df is None or df.empty:
            continue
        found_tables += 1
        # Occurrence
        _, match_cnt = count_patterns_in_table(df, patterns)
        occ_score += (match_cnt * weight)
        # Persistence
        psc = analyze_pattern_persistence(df, patterns)
        pers_score += (sum(psc.values()) * weight)
        # Stability
        if "RowType" in df.columns:
            stb = analyze_pattern_stability(df, patterns)
            stab_score += (sum(stb.values()) * weight)
        # Straight
        for p in patterns:
            s = detect_straight_combinations(df, p)
            straight_score += (s * weight)

    if found_tables == 0:
        return 0

    overall = (
        occ_score * 0.35 +
        pers_score * 0.30 +
        stab_score * 0.25 +
        straight_score * 0.10
    )
    return overall

# --- FAST OCCURRENCE PASS -----------------------------------------------
def rank_by_occurrence(tables, top=10):
    combined = tables.get("Combined_combined")
    if combined is None or combined.empty:
        return []
    counts = []
    for entry in BOXED_VTRAC_REFERENCE:
        idx = entry["Index"]
        pats = get_all_combinations_for_index(idx)
        _, cnt = count_patterns_in_table(combined, pats)
        counts.append((idx, cnt))
    counts.sort(key=lambda x: x[1], reverse=True)
    return [idx for idx, _ in counts[:top]]

WINNER_STYLE_BLOCK = """
<style>
  .legend { margin: 8px 0 12px; font: 13px/1.3 system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial; }
  .legend .chip { display:inline-block; margin-right:10px; padding:2px 6px; border-radius:4px; font-weight:600; border:1px solid #bbb; }
  .hit-winner { background-color:#e1f7d5; color:#0b6b00; border-color:#74c476; }
  .hit-winner-gap { background-color:#f1fde7; color:#23690c; border-style:dashed; border-color:#74c476; }
  .hit-vt-straight { color:#0d47a1; background:#e6f0ff; border:1px solid #0d47a1; }
  .hit-vt-straight-gap { color:#1565c0; background:#f0f6ff; border:1px dashed #1565c0; }
  .ls-box { background-color:#fff7bf; color:#111; }
  .ls-box-edge { box-shadow: inset 0 0 0 1px #e6c94f; }
  .hit-family { background-color:#ede3ff; color:#4b0082; border-color:#b39ddb; }
  .hit-family-gap { background-color:#f2ecff; color:#4b0082; border-style:dashed; border-color:#b39ddb; }
  td .hit-winner, td .hit-winner-gap, td .hit-vt-straight, td .hit-vt-straight-gap, td .hit-family, td .hit-family-gap { padding:0 2px; border-radius:2px; }
</style>
<div class="legend">
  <span class="chip hit-winner">Winner</span>
  <span class="chip hit-winner-gap">Winner (gap)</span>
  <span class="chip hit-vt-straight">V-TRAC straight</span>
  <span class="chip hit-vt-straight-gap">V-TRAC straight (value)</span>
  <span class="chip hit-family">Index family</span>
  <span class="chip hit-family-gap">Family (gap)</span>
  <span class="chip" style="background:#FFF7BF;border:1px solid #E6C94F">Long-string (DR) box</span>
</div>
"""

def analyze_all_indexes(state_name: str) -> list:
    """Loop all VTRAC indices, compute score, produce final sorted list of results."""
    tables = load_state_data(state_name)
    if not tables:
        print(f"[ERROR] No tables loaded for {state_name}")
        return []

    # First pass: quick occurrence ranking
    candidate_idxs = rank_by_occurrence(tables, top=10)
    if not candidate_idxs:
        return []

    # Second pass: detailed scoring only for top candidates
    results = []
    for idx in candidate_idxs:
        combos = get_all_combinations_for_index(idx)
        score = calculate_index_score(tables, combos)
        results.append({
            "index": idx,
            "score": score,
            "patterns": combos
        })

    # sort
    results.sort(key=lambda x: x["score"], reverse=True)
    # rank
    for i, r in enumerate(results):
        r["rank"] = i+1
    return results

def generate_index_html_report(state_name, index, patterns, tables, score, rank, timestamp=None, winner_combo: str | None = None):
    """Generate an HTML report for a specific V-TRAC index"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    targets = build_winner_targets(winner_combo or "", patterns)
    evidence_grid = build_evidence_grid(tables).evaluate(targets)
    report_statistics = build_report_statistics(tables, patterns)
    ordered_lane_report = build_ordered_lane_report(
        winner_combo, tables, legacy_vt_pair=targets.vt_pair
    )
    legacy_stats = report_statistics["legacy_combined_all_rows"]

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>V-TRAC Analysis - Index {index}</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 20px;
        }}
        table {{ 
            border-collapse: collapse; 
            margin: 10px 0; 
            width: 100%;
        }}
        th, td {{ 
            border: 1px solid black; 
            padding: 6px; 
            text-align: center; 
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .version {{ 
            color: gray; 
            font-size: 0.9em; 
            margin-bottom: 10px; 
        }}
        .highlight {{
            color: #800080;
            font-weight: 800;
        }}
        .stats {{
            background-color: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            margin-top: 30px;
        }}
        .horizontal-layout {{
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;
            margin: 0;
            padding: 0;
        }}
        .section {{
            flex: 1;
            margin: 0 2px;
        }}
        @media (max-width: 1200px) {{
            .horizontal-layout {{
                flex-direction: column;
            }}
            .section {{
                margin: 10px 0;
            }}
        }}
        .rank-badge {{
            display: inline-block;
            background-color: #800080;
            color: white;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 20px;
            margin-right: 10px;
        }}
        .tables-section {{
            margin-bottom: 40px;
        }}
        .tables-section h2 {{
            color: #800080;
            border-bottom: 2px solid #800080;
            padding-bottom: 5px;
        }}
        .pattern-list {{
            margin: 10px 0;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
"""
    html += WINNER_STYLE_BLOCK

    def generate_table_html(df, title, table_kind):
        if df is None or df.empty:
            return f"<h2>{title}</h2><p>No data available</p>"

        variant_label = str(table_kind or "").capitalize()
        table_key = str(table_kind).lower()
        header_cols = ['Set', 'Draw', 'RowType', '7', '6', '5', '4', '3', '2', '1']
        table_html = f"<h2>{title}</h2><table>"
        table_html += "<tr>" + "".join([f"<th>{col}</th>" for col in header_cols if col in df.columns]) + "</tr>"

        for _, row in df.iterrows():
            set_name = str(row.get("Set", ""))
            draw_name = str(row.get("Draw", ""))
            row_type = str(row.get("RowType", ""))
            table_html += "<tr>"
            for col in header_cols:
                if col in df.columns:
                    raw_value = str(row[col])
                    display_value = raw_value
                    if col.isdigit() and any(ch.isdigit() for ch in raw_value):
                        column_index = int(col)
                        box_key = EvidenceBoxKey(
                            variant=variant_label,
                            set_name=set_name,
                            draw=draw_name,
                            column=column_index,
                        )
                        box = evidence_grid.boxes.get(box_key)
                        if box:
                            cell = box.cells.get(row_type)
                            if cell and cell.spans:
                                display_value = cell.render_highlighted()

                    cell_classes = []
                    if col.isdigit():
                        col_idx = int(col)
                        if _is_long_string_cell(table_key, set_name, draw_name, row_type, col_idx):
                            cell_classes.extend(["ls-box", "ls-box-edge"])

                    if cell_classes:
                        class_attr = " class=\"" + " ".join(cell_classes) + "\""
                    else:
                        class_attr = ""

                    table_html += f"<td{class_attr}>{display_value}</td>"
            table_html += "</tr>"

        table_html += "</table>"
        return table_html
    # Horizontal layout styling
    html += '<style>.horizontal-layout{display:flex; flex-direction:row; justify-content:space-between; width:100%; margin:0; padding:0;} .section{flex:1; margin:0 2px;}</style>'
    
    # Three sections (Midday/Evening/Combined) at the top
    html += '<div class="horizontal-layout">'
    
    # Midday
    html += '<div class="section">'
    html += '<h2>Midday Data</h2>'
    if "Midday_combined" in tables:
        html += generate_table_html(tables["Midday_combined"], f"{state_name} Midday Combined Table", "midday")
    if "Midday_r2" in tables:
        html += f"<h5>Midday - R2-only</h5>"
        html += generate_table_html(tables["Midday_r2"], f"{state_name} Midday R2-only Table", "midday")
    html += '</div>'
    
    # Evening
    html += '<div class="section">'
    html += '<h2>Evening Data</h2>'
    if "Evening_combined" in tables:
        html += generate_table_html(tables["Evening_combined"], f"{state_name} Evening Combined Table", "evening")
    if "Evening_r2" in tables:
        html += f"<h5>Evening - R2-only</h5>"
        html += generate_table_html(tables["Evening_r2"], f"{state_name} Evening R2-only Table", "evening")
    html += '</div>'
    
    # Combined
    html += '<div class="section">'
    html += '<h2>Combined Data</h2>'
    if "Combined_combined" in tables:
        html += generate_table_html(tables["Combined_combined"], f"{state_name} Combined Combined Table", "combined")
    if "Combined_r2" in tables:
        html += f"<h5>Combined - R2-only</h5>"
        html += generate_table_html(tables["Combined_r2"], f"{state_name} Combined R2-only Table", "combined")
    html += '</div>'
    
    html += '</div>'  # close horizontal-layout

    # V-TRAC info below tables
    html += f'<div class="version">Version: v{timestamp}</div>'
    html += f'<h1><span class="rank-badge">Rank #{rank}</span> V-TRAC Analysis for {state_name} - Index {index}</h1>'
    
    # Detailed analysis stats at the bottom
    html += '<div class="stats">'
    html += '<h2>Detailed Analysis Statistics</h2>'
    html += (
        "<p><strong>Statistics contract:</strong> Midday, Evening, and Combined "
        "are reported separately. R2/R4/R6/R8 pattern rows and draw_data rows "
        "are separate populations. Occurrences and unique locations are separate "
        "denominators. All-variant totals are descriptive sums, not independent "
        "support or stability.</p>"
    )

    html += "<h3>Variant and Population Summary</h3>"
    html += (
        "<table><tr><th>Variant</th><th>Population</th><th>Rows</th>"
        "<th>Occurrences</th><th>Unique Pattern/Cell Locations</th>"
        "<th>Pattern Identities Present</th></tr>"
    )
    for variant in _REPORT_VARIANTS:
        for population in ("r_pattern", "draw_data"):
            stats = report_statistics["variants"][variant][population]
            html += (
                f"<tr><td>{variant}</td><td>{population}</td>"
                f"<td>{stats['row_count']}</td>"
                f"<td>{stats['pattern_occurrence_total']}</td>"
                f"<td>{stats['pattern_unique_location_total']}</td>"
                f"<td>{len(stats['unique_pattern_identities_present'])}</td></tr>"
            )
    html += "</table>"

    html += "<h3>Ordered Three-Position VTRAC Lane</h3>"
    if ordered_lane_report["status"] == "AVAILABLE":
        html += (
            f"<p>Winner <strong>{ordered_lane_report['winner_literal']}</strong> "
            f"maps to <strong>{ordered_lane_report['ordered_vcode']}</strong> "
            f"(boxed index {ordered_lane_report['boxed_vtrac_index']}). "
            f"Lane members: {' '.join(ordered_lane_report['lane_members'])}.</p>"
        )
        html += (
            "<table><tr><th>Variant</th><th>Population</th>"
            "<th>Lane Occurrences</th><th>Unique Locations</th></tr>"
        )
        for variant in _REPORT_VARIANTS:
            for population in ("r_pattern", "draw_data"):
                lane_stats = ordered_lane_report["variants"][variant][population]
                html += (
                    f"<tr><td>{variant}</td><td>{population}</td>"
                    f"<td>{lane_stats['occurrence_total']}</td>"
                    f"<td>{lane_stats['unique_location_total']}</td></tr>"
                )
        html += "</table>"
    else:
        html += "<p>Ordered lane unavailable: winner is not an exact Pick-3 literal.</p>"
    legacy_marker = ordered_lane_report["legacy_marker"]
    html += (
        "<p><strong>Legacy two-value marker:</strong> "
        f"{legacy_marker['status']}. This preserved marker is not the modern "
        "ordered three-position lane.</p>"
    )

    html += "<h3>Legacy Combined/All-Row Statistics (Compatibility)</h3>"
    html += (
        "<p>These legacy values use the Combined variant only and mix "
        "R-pattern with draw_data rows. Use the variant/population summary and "
        "JSON v2 fields for analytical interpretation.</p>"
    )
    
    # 1. Pattern occurrence counts
    html += "<h4>Pattern Occurrence Counts</h4>"
    html += "<table><tr><th>Pattern</th><th>Occurrences</th></tr>"
    for pattern, count in sorted(
        legacy_stats["pattern_occurrence"].items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        html += f"<tr><td>{pattern}</td><td>{count}</td></tr>"
    html += "</table>"
    
    # 2. Pattern persistence scores
    html += "<h4>Pattern Persistence Scores</h4>"
    html += "<table><tr><th>Pattern</th><th>Persistence Score</th></tr>"
    for pattern, stat_score in sorted(
        legacy_stats["pattern_persistence"].items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        html += f"<tr><td>{pattern}</td><td>{stat_score}</td></tr>"
    html += "</table>"
    
    # 3. Pattern stability scores
    html += "<h4>Pattern Stability Scores</h4>"
    html += "<table><tr><th>Pattern</th><th>Stability Score</th></tr>"
    for pattern, stat_score in sorted(
        legacy_stats["pattern_stability"].items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        html += f"<tr><td>{pattern}</td><td>{stat_score}</td></tr>"
    html += "</table>"
    
    # 4. Straight combinations
    html += "<h4>Straight Combination Occurrences</h4>"
    html += "<table><tr><th>Pattern</th><th>Straight Occurrences</th></tr>"
    for pattern, count in sorted(
        legacy_stats["straight_counts"].items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        html += f"<tr><td>{pattern}</td><td>{count}</td></tr>"
    html += "</table>"
    
    html += '</div>'  # stats
    html += '</body></html>'
    
    return html


def generate_index_json_report(state_name, index, patterns, tables, score, rank, timestamp=None, winner_combo: str | None = None):
    """
    Produce a structured JSON representation of the winners report (tables + legend tags + stats),
    mirroring the HTML highlights without scraping.
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    targets = build_winner_targets(winner_combo or "", patterns)
    evidence_grid = build_evidence_grid(tables).evaluate(targets)
    report_statistics = build_report_statistics(tables, patterns)
    ordered_lane_report = build_ordered_lane_report(
        winner_combo, tables, legacy_vt_pair=targets.vt_pair
    )

    header_cols = ['Set', 'Draw', 'RowType', '7', '6', '5', '4', '3', '2', '1']
    legend = {
        "hit-winner": "Winner",
        "hit-winner-gap": "Winner (gap)",
        "hit-vt-straight": "V-TRAC straight",
        "hit-vt-straight-gap": "V-TRAC straight (value)",
        "hit-family": "Index family",
        "hit-family-gap": "Family (gap)",
        "ls-box": "Long-string (DR) box",
        "ls-box-edge": "Long-string (DR) box edge",
    }

    def serialize_table(df, table_key, variant_label):
        if df is None or df.empty:
            return []
        rows_out = []
        table_key = str(table_key or "").lower()
        for _, row in df.iterrows():
            row_out = {
                "Set": str(row.get("Set", "")),
                "Draw": str(row.get("Draw", "")),
                "RowType": str(row.get("RowType", "")),
                "cells": {},
            }
            set_name = row_out["Set"]
            draw_name = row_out["Draw"]
            row_type = row_out["RowType"]
            for col in header_cols:
                if col not in df.columns:
                    continue
                raw_value = str(row[col])
                tags: list[str] = []
                if col.isdigit() and any(ch.isdigit() for ch in raw_value):
                    col_idx = int(col)
                    box_key = EvidenceBoxKey(
                        variant=variant_label,
                        set_name=set_name,
                        draw=draw_name,
                        column=col_idx,
                    )
                    box = evidence_grid.boxes.get(box_key)
                    if box:
                        cell = box.cells.get(row_type)
                        if cell and cell.spans:
                            for cat, spans in cell.spans.items():
                                if spans:
                                    cls = HIGHLIGHT_CLASS.get(cat)
                                    if cls:
                                        tags.append(cls)
                    if _is_long_string_cell(table_key, set_name, draw_name, row_type, col_idx):
                        tags.extend(["ls-box", "ls-box-edge"])
                row_out["cells"][col] = {
                    "text": raw_value,
                    "tags": sorted(set(tags)),
                }
            rows_out.append(row_out)
        return rows_out

    data = {
        "report_schema_version": "winner_report_semantics_v2",
        "state": state_name,
        "index": index,
        "winner_combo": winner_combo,
        "score": score,
        "rank": rank,
        "timestamp": timestamp,
        "patterns": list(patterns),
        "legend": legend,
        "tables": {
            "Midday": serialize_table(tables.get("Midday_combined"), "midday", "Midday"),
            "Evening": serialize_table(tables.get("Evening_combined"), "evening", "Evening"),
            "Combined": serialize_table(tables.get("Combined_combined"), "combined", "Combined"),
        },
        "statistics_contract": report_statistics["contract"],
        "stats": report_statistics["legacy_combined_all_rows"],
        "stats_by_variant": {
            "variants": report_statistics["variants"],
            "all_variant": report_statistics["all_variant"],
        },
        "ordered_vtrac_lane": ordered_lane_report,
    }
    return data

def generate_top_reports(state_name, results, top_n=3):
    """Generate HTML reports for top N ranked indexes"""
    if not results or len(results) == 0:
        return []
    
    tables = load_state_data(state_name)
    if not tables:
        return []
    
    reports = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for i, result in enumerate(results[:top_n]):
        rank = i + 1
        html = generate_index_html_report(
            state_name,
            result["index"],
            result["patterns"],
            tables,
            result["score"],
            rank,
            timestamp,
            winner_combo=None
        )
        
        filename = f"{state_name}_vtrac_rank{rank}_index{result['index']}_v{timestamp}.html"
        output_dir = ROOT / "data" / "outputs" / "analysis"
        output_dir.mkdir(parents=True, exist_ok=True)
        filepath = output_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        
        reports.append({
            "rank": rank,
            "index": result["index"],
            "score": result["score"],
            "filename": filename,
            "filepath": str(filepath),  # Convert Path to string for compatibility
            "html": html
        })
    
    return reports

def generate_summary_chart(results, top_n=10):
    """Generate a summary chart of top indexes"""
    if not results or len(results) == 0:
        return None
    
    top_results = results[:min(top_n, len(results))]
    indices = [str(r["index"]) for r in top_results]
    scores = [r["score"] for r in top_results]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(indices, scores, color='purple', alpha=0.7)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2.,
            height + 5,
            f'{height:.0f}',
            ha='center',
            va='bottom'
        )
    
    plt.title('Top V-TRAC Indexes by Score', fontsize=16)
    plt.xlabel('V-TRAC Index', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    
    return f"data:image/png;base64,{image_base64}"

def get_combined_table(state_name, time_period):
    """Load combined table for state and time period"""
    tables_dir = get_tables_output_dir()
    date_folders = sorted(
        [d for d in os.listdir(tables_dir) if os.path.isdir(os.path.join(tables_dir, d))],
        reverse=True
    )
    if not date_folders:
        return None
    
    state_dir = os.path.join(tables_dir, date_folders[0], state_name)
    if not os.path.exists(state_dir):
        return None
    
    filename = f"{state_name}_{time_period}_combined.csv"
    filepath = os.path.join(state_dir, filename)
    
    if os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    
    return None

def get_r2_table(state_name, time_period):
    """Load R2-only table for state and time period"""
    tables_dir = get_tables_output_dir()
    date_folders = sorted(
        [d for d in os.listdir(tables_dir) if os.path.isdir(os.path.join(tables_dir, d))],
        reverse=True
    )
    if not date_folders:
        return None
    
    state_dir = os.path.join(tables_dir, date_folders[0], state_name)
    if not os.path.exists(state_dir):
        return None
    
    filename = f"{state_name}_{time_period}_R2_only.csv"
    filepath = os.path.join(state_dir, filename)
    
    if os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    
    return None

def get_patterns_for_index(index):
    """Get all pattern combinations for a specific V-TRAC index"""
    vtrac_entry = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == index), None)
    if vtrac_entry:
        patterns = set()
        patterns.update(vtrac_entry.get("Singles", []))
        patterns.update(vtrac_entry.get("Doubles", []))
        return patterns
    return set()

def get_winners_output_dir():
    """Get the directory for winner outputs"""
    output_dir = os.path.join("data", "outputs", "winners")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def highlight_winners_in_table(tables, midday_winners, evening_winners):
    """
    Highlight winning numbers in tables and save highlighted versions
    
    Args:
        tables (dict): Dictionary of table DataFrames
        midday_winners (list): List of midday winning number strings
        evening_winners (list): List of evening winning number strings
        
    Returns:
        dict: Dictionary of highlighted DataFrames
    """
    highlighted_tables = {}
    
    def highlight_winner(row):
        styles = pd.Series([''] * len(row), index=row.index)
        
        highlight_nums = []
        if 'Midday' in row.get('Category', ''):
            highlight_nums = midday_winners
        elif 'Evening' in row.get('Category', ''):
            highlight_nums = evening_winners
        else:
            # For combined tables, highlight both
            highlight_nums = midday_winners + evening_winners
        
        for num_col in ['Num1', 'Num2', 'Num3']:
            if num_col in row and str(row[num_col]) in highlight_nums:
                styles[num_col] = 'background-color: yellow; font-weight: bold'
        
        if 'Number' in row and str(row['Number']) in highlight_nums:
            styles['Number'] = 'background-color: yellow; font-weight: bold'
            
        return styles
    
    for key, df in tables.items():
        if df is None or df.empty:
            highlighted_tables[key] = df
            continue
        
        highlighted_df = df.copy()
        try:
            styled_df = highlighted_df.style.apply(highlight_winner, axis=1)
            highlighted_tables[key] = styled_df
        except Exception as e:
            st.warning(f"Could not highlight winners in {key}: {str(e)}")
            highlighted_tables[key] = highlighted_df
    
    return highlighted_tables

# ------------------------------------------------------------------------------
# COMBINED MAIN APP
# ------------------------------------------------------------------------------

def main():
    """Main application layout and execution"""
    st.sidebar.title("Alpha Analytical Tool")
    st.sidebar.image("https://img.icons8.com/fluency/96/lottery.png", width=80)
    st.sidebar.markdown("---")
    
    st.title("Alpha Analytical Tool")
    
    tabs = st.tabs([
        "Process Data", 
        "View Results", 
        "Log Winners", 
        "V-TRAC Analyzer"
    ])
    
    with tabs[0]:
        process_data_tab()
    with tabs[1]:
        view_results_tab()
    with tabs[2]:
        log_winners_tab()
    with tabs[3]:
        vtrac_analyzer_tab()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.text(f"Last Updated: {now}")

def process_data_tab():
    """The Process Data tab"""
    st.title("Data Processing")
    st.markdown("Process raw data files to generate cleaned datasets and analysis tables.")
    
    excel_path, excel_exists = check_excel_file()
    
    if not excel_exists:
        st.error(f"Excel file not found at {excel_path}")
        st.warning("Please place the 'Pick3StatsC4.xlsm' file in the data/original directory.")
        return
    
    st.success(f"Found Excel file: {os.path.basename(excel_path)}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        clean_data = st.checkbox("Clean Data", value=True)
    with col2:
        extract_data = st.checkbox("Extract Data", value=True)
    with col3:
        generate_tables_option = st.checkbox("Generate Tables", value=True)
    
    selected_states = st.multiselect(
        "Select States to Process (leave empty for all states)",
        options=STATES,
        default=[]
    )
    states_to_process = selected_states if selected_states else STATES
    
    if st.button("Process Data"):
        progress_bar = st.progress(0)
        status = st.empty()
        results = st.empty()
        
        create_output_directories()
        
        summary = {
            "cleaned_states": [],
            "failed_clean": [],
            "extracted_states": [],
            "tables_generated": []
        }
        
        with st.spinner("Processing data..."):
            # 1) Clean
            if clean_data:
                status.info("Step 1/3: Cleaning data...")
                start_time = datetime.now()
                
                cleaning_results = clean_all_states(
                    states_to_process,
                    excel_path,
                    get_cleaned_data_dir()
                )
                
                summary["cleaned_states"] = cleaning_results["success"]
                summary["failed_clean"] = cleaning_results["failed"]
                
                progress_bar.progress(33)
                duration = (datetime.now() - start_time).total_seconds()
                status.success(f"Data cleaning completed in {format_time(duration)}")
            else:
                progress_bar.progress(33)
                status.info("Skipping data cleaning step")
            
            # 2) Extract
            extracted_data = {}
            if extract_data:
                status.info("Step 2/3: Extracting data...")
                start_time = datetime.now()
                
                extracted_data = extract_all_states(
                    states_to_process,
                    get_cleaned_data_dir()
                )
                
                summary["extracted_states"] = list(extracted_data.keys())
                
                progress_bar.progress(66)
                duration = (datetime.now() - start_time).total_seconds()
                status.success(f"Data extraction completed in {format_time(duration)}")
            else:
                progress_bar.progress(66)
                status.info("Skipping data extraction step")
            
            # 3) Generate tables
            if generate_tables_option and extracted_data:
                status.info("Step 3/3: Generating tables...")
                start_time = datetime.now()
                
                for state_name, state_data in extracted_data.items():
                    generate_tables(
                        state_data,
                        state_name,
                        os.path.join(get_tables_output_dir(), state_name)
                    )
                    summary["tables_generated"].append(state_name)
                
                progress_bar.progress(100)
                duration = (datetime.now() - start_time).total_seconds()
                status.success(f"Table generation completed in {format_time(duration)}")
            else:
                progress_bar.progress(100)
                status.info("Skipping table generation step")
        
        results.markdown("### Processing Summary")
        st.write(f"**States Processed:** {len(states_to_process)}")
        
        if clean_data:
            st.write(f"**Successfully Cleaned:** {len(summary['cleaned_states'])}")
            if summary["failed_clean"]:
                st.warning(f"**Failed to Clean:** {', '.join(summary['failed_clean'])}")
        
        if extract_data:
            st.write(f"**Successfully Extracted:** {len(summary['extracted_states'])}")
        
        if generate_tables_option:
            st.write(f"**Tables Generated:** {len(summary['tables_generated'])}")
        
        st.success("Processing completed!")

def view_results_tab():
    """The View Results tab"""
    st.title("View Results")
    st.markdown("View the generated tables and analysis results.")
    
    output_dir = get_tables_output_dir()
    if not os.path.exists(output_dir):
        st.error(f"Output directory not found: {output_dir}")
        st.info("Please process data first.")
        return
    
    if len(os.listdir(output_dir)) == 0:
        st.error("No output data found.")
        st.info("Please process data first.")
        return
    
    # List top-level directories (states) in get_tables_output_dir()
    available_states = sorted([
        d for d in os.listdir(output_dir)
        if os.path.isdir(os.path.join(output_dir, d))
    ])
    
    if not available_states:
        st.error("No state data found.")
        st.info("Please process data first.")
        return
    
    selected_state = st.selectbox("Select state:", available_states)
    state_dir = os.path.join(output_dir, selected_state)
    available_tables = sorted([f for f in os.listdir(state_dir) if f.endswith(".csv")])
    
    if not available_tables:
        st.error(f"No tables found for state: {selected_state}")
        return
    
    table_options = [
        f"{selected_state}_Midday_combined.csv",
        f"{selected_state}_Evening_combined.csv",
        f"{selected_state}_Combined_combined.csv",
        f"{selected_state}_Midday_R2_only.csv",
        f"{selected_state}_Evening_R2_only.csv",
        f"{selected_state}_Combined_R2_only.csv"
    ]
    
    available_options = [opt for opt in table_options if opt in available_tables]
    if not available_options:
        available_options = available_tables
    
    selected_table = st.selectbox("Select table type:", available_options)
    
    table_path = os.path.join(state_dir, selected_table)
    if os.path.exists(table_path):
        try:
            df = pd.read_csv(table_path)
            
            def highlight_sets(s):
                if s.name != 'Set':
                    return [''] * len(s)
                
                return [
                    'background-color: rgba(31, 119, 180, 0.1)' if x == 'Set3'
                    else 'background-color: rgba(44, 160, 44, 0.1)' if x == 'Set2'
                    else 'background-color: rgba(255, 127, 14, 0.1)' if x == 'Set1'
                    else ''
                    for x in s
                ]
            
            st.dataframe(
                df.style.apply(highlight_sets, axis=0).set_properties(**{
                    'text-align': 'center',
                    'font-family': 'monospace',
                    'white-space': 'nowrap'
                }),
                use_container_width=True
            )
            
            csv = df.to_csv(index=False)
            st.download_button(
                "Download Table as CSV",
                csv,
                file_name=selected_table,
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"Error loading table: {str(e)}")
    else:
        st.error(f"Table file not found: {table_path}")

def _winner_html(df, patterns):
    def cell_fmt(val):
        val = str(val)
        for p in patterns:
            if p in val:
                val = val.replace(p, f'<span class="highlight">{p}</span>')
        return val
    cols = [c for c in ['Set','Draw','RowType','7','6','5','4','3','2','1'] if c in df.columns]
    rows = ["<tr>"+"".join(f"<th>{c}</th>" for c in cols)+"</tr>"]
    for _, row in df.iterrows():
        rows.append("<tr>"+ "".join(f"<td>{cell_fmt(row[c])}</td>" for c in cols) +"</tr>")
    return (
        "<html><head><style> "
        ".highlight{color:#800080;font-weight:800} table{border-collapse:collapse}"
        "th,td{border:1px solid #000;padding:4px 6px;text-align:center}"
        "</style></head><body><table>"
        + "\n".join(rows) + "</table></body></html>"
    )

def get_top_prediction_index(state: str, date_str: str):
    """
    Look at data/outputs/predictions/<state>_<date>_predictions.json
    and return the index with rank 1. None if the file isn't there.
    """
    pred_path = Path("data/outputs/predictions") / f"{state}_{date_str}_predictions.json"
    if not pred_path.exists():
        return None

    with open(pred_path, "r") as f:
        preds = json.load(f)

    # file format: { "predictions": [ { "rank": 1, "index": ... }, ... ] }
    for entry in preds.get("predictions", []):
        if entry.get("rank") == 1:
            return entry.get("index")
    return None

def log_winners_tab():
    """Enhanced Log Winners Tab with JSON Export"""
    st.header("Log & Highlight Winners")
    st.markdown("Enter winning numbers to highlight them in tables and save for AI training.")
    
    # Choose input method
    input_method = st.radio(
        "Choose input method:",
        ["Individual Entry", "Bulk Paste (Multiple States)"],
        key="winner_input_method"
    )
    
    if input_method == "Individual Entry":
        # Original individual entry form
        with st.form("winners_form_individual"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Midday Winners")
                midday_winners = st.text_input(
                    "Enter Midday winning numbers (separated by spaces)",
                    placeholder="e.g. 123 456 789"
                )
            
            with col2:
                st.subheader("Evening Winners")
                evening_winners = st.text_input(
                    "Enter Evening winning numbers (separated by spaces)",
                    placeholder="e.g. 123 456 789"
                )
            
            selected_states = st.multiselect(
                "Select States to Process (leave empty for all)",
                options=STATES,
                default=[],
                key="log_winners_states_individual"
            )
            
            # Add date input for historical data
            winner_date = st.date_input(
                "Winner Date",
                value=datetime.now().date(),
                key="winner_date_individual"
            )
            
            submit_button = st.form_submit_button("Log Winners & Highlight", type="primary")
        
        if submit_button:
            if not midday_winners and not evening_winners:
                st.warning("Please enter at least one winning number")
                return
            
            midday_list = [w.strip() for w in midday_winners.split() if w.strip()]
            evening_list = [w.strip() for w in evening_winners.split() if w.strip()]
            
            states_to_process = selected_states if selected_states else STATES
            date_str = winner_date.strftime("%Y-%m-%d")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            progress_bar = st.progress(0)
            status = st.empty()
            json_files_saved = []
            
            for i, state_name in enumerate(states_to_process):
                status.info(f"Processing {state_name}...")
                
                # Save winners as JSON
                if midday_list or evening_list:
                    midday_winner = midday_list[0] if midday_list else ""
                    evening_winner = evening_list[0] if evening_list else ""
                    
                    json_filepath = save_winners_as_json(
                        state_name, 
                        midday_winner, 
                        evening_winner,
                        date_str
                    )
                    if json_filepath:
                        json_files_saved.append(json_filepath)
                
                # Original highlighting logic
                tables = load_state_data(state_name)
                if not tables:
                    st.warning(f"No tables found for {state_name}")
                    continue
                
                # First check if tables exist and are not empty
                valid_tables = {}
                for section_key, df in tables.items():
                    if df is not None and not df.empty:
                        valid_tables[section_key] = df
                
                if valid_tables:
                    # Now apply highlighting to valid tables
                    highlighted_tables = highlight_winners_in_table(
                        valid_tables,
                        midday_list,
                        evening_list
                    )
                    
                    output_dir = os.path.join(get_winners_output_dir(), state_name)
                    os.makedirs(output_dir, exist_ok=True)
                    
                    # Create winners directory for HTML files
                    winners_dir = Path("data/outputs/winners")
                    winners_dir.mkdir(parents=True, exist_ok=True)
                    
                    for section_key, styled_df in highlighted_tables.items():
                        if styled_df is not None:
                            winners_suffix = ""
                            if "Midday" in section_key and midday_list:
                                winners_suffix = f"_win{'_'.join(midday_list)}"
                            elif "Evening" in section_key and evening_list:
                                winners_suffix = f"_win{'_'.join(evening_list)}"
                            elif "Combined" in section_key and (midday_list or evening_list):
                                winners_suffix = "_winners"
                            
                            # Save CSV
                            output_file = os.path.join(
                                output_dir,
                                f"{state_name}_{section_key}{winners_suffix}.csv"
                            )
                            valid_tables[section_key].to_csv(output_file, index=False)
                            
                            # Get top prediction index for this state/date
                            top_index = get_top_prediction_index(state_name, date_str)
                            patterns = get_patterns_for_index(top_index) if top_index is not None else []
                            html_str = _winner_html(valid_tables[section_key], patterns)
                            html_path = winners_dir / f"{state_name}_{section_key}{winners_suffix}_{timestamp}.html"
                            with open(html_path, "w", encoding="utf-8") as f:
                                f.write(html_str)
                            
                            # Show quick link in UI
                            st.markdown(f"[OK] **HTML saved** -> `{html_path}`")
                    
                    # Create bundle
                    pred_json_path = Path("data/outputs/predictions") / f"{state_name}_{date_str}_predictions.json"
                    winners_json_path = Path("data/outputs/winners_json") / f"{state_name}_{date_str}_winners.json"
                    if pred_json_path.exists() and winners_json_path.exists():
                        bundle_path = bundle_day(state_name, date_str, pred_json_path, winners_json_path)
                        st.success(f"Bundle saved -> {bundle_path}")
                
                progress = (i + 1) / len(states_to_process)
                progress_bar.progress(progress)
            
            status.success("Winner logging completed!")
            
            if json_files_saved:
                st.success(f"Saved {len(json_files_saved)} winner JSON files for AI training")
                with st.expander("View saved JSON files"):
                    for filepath in json_files_saved[:5]:  # Show first 5
                        st.text(filepath)
                    if len(json_files_saved) > 5:
                        st.text(f"... and {len(json_files_saved) - 5} more files")
    
    else:  # Bulk Paste method
        st.markdown("""
        ### Bulk Paste Format
        Paste winners in this format (tab or space separated):
        ```
        Connecticut    042    838
        Delaware       058    478
        Florida        610    975
        ```
        First column: State name
        Second column: Midday winner (or empty)
        Third column: Evening winner (or empty)
        """)
        
        with st.form("winners_form_bulk"):
            winners_text = st.text_area(
                "Paste winners data here:",
                height=300,
                placeholder="Connecticut\t042\t838\nDelaware\t058\t478\nFlorida\t610\t975"
            )
            
            winner_date_bulk = st.date_input(
                "Winner Date",
                value=datetime.now().date(),
                key="winner_date_bulk"
            )
            
            submit_bulk = st.form_submit_button("Process Bulk Winners", type="primary")
        
        if submit_bulk and winners_text:
            # Parse the bulk input
            winners_dict = parse_winners_input(winners_text)
            
            if not winners_dict:
                st.error("No valid winner data found. Please check the format.")
                return
            
            st.write(f"Found winner data for {len(winners_dict)} states")
            
            progress_bar = st.progress(0)
            status = st.empty()
            json_files_saved = []
            date_str = winner_date_bulk.strftime("%Y-%m-%d")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Map state names to match STATES list
            state_mapping = {
                "Connecticut": "Connecticut4",
                "Delaware": "Delaware4",
                "Florida": "Florida4",
                "Indiana": "Indiana4",
                "Michigan": "Michigan4",
                "New Jersey": "NewJersey4",
                "New York": "NewYork4",
                "North Carolina": "NorthCarolina4",
                "Ohio": "Ohio4",
                "Ontario": "OntarioCanada4",
                "Pennsylvania": "Pennsylvania4",
                "Puerto Rico": "PuertoRico4",
                "South Carolina": "SouthCarolina4",
                "Virginia": "Virginia4"
            }
            
            processed_count = 0
            for state_input, (midday, evening) in winners_dict.items():
                # Try to match state name
                state_name = None
                for full_name in STATES:
                    if state_input.lower() in full_name.lower():
                        state_name = full_name
                        break
                
                # Also check mapping
                if not state_name and state_input in state_mapping:
                    state_name = state_mapping[state_input]
                
                if not state_name:
                    st.warning(f"Could not match state: {state_input}")
                    continue
                
                status.info(f"Processing {state_name}...")
                
                # Save winners as JSON
                json_filepath = save_winners_as_json(
                    state_name,
                    midday,
                    evening,
                    date_str
                )
                if json_filepath:
                    json_files_saved.append(json_filepath)
                
                # Highlight in tables if numbers exist
                if midday or evening:
                    tables = load_state_data(state_name)
                    if tables:
                        midday_list = [midday] if midday else []
                        evening_list = [evening] if evening else []
                        
                        # First check if tables exist and are not empty
                        valid_tables = {}
                        for section_key, df in tables.items():
                            if df is not None and not df.empty:
                                valid_tables[section_key] = df
                        
                        if valid_tables:
                            # Now apply highlighting to valid tables
                            highlighted_tables = highlight_winners_in_table(
                                valid_tables,
                                midday_list,
                                evening_list
                            )
                            
                            output_dir = os.path.join(get_winners_output_dir(), state_name)
                            os.makedirs(output_dir, exist_ok=True)
                            
                            # Create winners directory for HTML files
                            winners_dir = Path("data/outputs/winners")
                            winners_dir.mkdir(parents=True, exist_ok=True)
                            
                            for section_key, styled_df in highlighted_tables.items():
                                if styled_df is not None:
                                    # Save CSV
                                    output_file = os.path.join(
                                        output_dir,
                                        f"{state_name}_{section_key}_winners_{date_str}.csv"
                                    )
                                    valid_tables[section_key].to_csv(output_file, index=False)
                                    
                                    # Get top prediction index for this state/date
                                    top_index = get_top_prediction_index(state_name, date_str)
                                    patterns = get_patterns_for_index(top_index) if top_index is not None else []
                                    html_str = _winner_html(valid_tables[section_key], patterns)
                                    html_path = winners_dir / f"{state_name}_{section_key}_winners_{timestamp}.html"
                                    with open(html_path, "w", encoding="utf-8") as f:
                                        f.write(html_str)
                                    
                                    # Show quick link in UI
                                    st.markdown(f"[OK] **HTML saved** -> `{html_path}`")
                    
                            # Create bundle
                            bundle_day(state_name, date_str)
                
                processed_count += 1
                progress_bar.progress(processed_count / len(winners_dict))
            
            status.success(f"Processed {processed_count} states!")
            
            if json_files_saved:
                st.success(f"Saved {len(json_files_saved)} winner JSON files")
                
                # Show summary
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("States Processed", processed_count)
                    st.metric("JSON Files Saved", len(json_files_saved))
                
                with col2:
                    predictions_dir = get_predictions_output_dir()
                    winners_dir = get_winners_json_output_dir()
                    st.info(f"Predictions saved to:\n`{predictions_dir}`")
                    st.info(f"Winners saved to:\n`{winners_dir}`")
    
    # Add section to view saved data
    st.markdown("---")
    st.subheader("View Saved Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("View Recent Predictions"):
            predictions_dir = get_predictions_output_dir()
            if os.path.exists(predictions_dir):
                files = sorted(os.listdir(predictions_dir))[-10:]  # Last 10 files
                if files:
                    st.write("Recent prediction files:")
                    for f in files:
                        st.text(f"- {f}")
                else:
                    st.info("No prediction files found yet")
    
    with col2:
        if st.button("View Recent Winners"):
            winners_dir = get_winners_json_output_dir()
            if os.path.exists(winners_dir):
                files = sorted(os.listdir(winners_dir))[-10:]  # Last 10 files
                if files:
                    st.write("Recent winner files:")
                    for f in files:
                        st.text(f"- {f}")
                else:
                    st.info("No winner files found yet")

def vtrac_analyzer_tab():
    """Enhanced V-TRAC Analyzer Tab Content"""
    st.header("Enhanced V-TRAC Pattern Analyzer")
    st.markdown("""
    This tool analyzes V-TRAC indexes for your selected dataset(s). Use the dropdown 
    to view results for each state.
    """)
    st.info("Analysis may take longer for large datasets or when running all states.")
    
    state_options = ["All States"] + STATES
    selected_option = st.selectbox("Select Dataset(s) to Analyze", state_options, key="vtrac_state_select")
    
    # Hardcode to top 3 instead of using sliders
    top_n_indexes = 3
    top_n_reports = 3
    
    if st.button("Run V-TRAC Analysis", type="primary", key="vtrac_analyzer_run_button"):
        with st.spinner("Running V-TRAC Analysis..."):
            if selected_option == "All States":
                states_to_run = STATES
            else:
                states_to_run = [selected_option]
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            total_start = time.time()
            
            for i, state_name in enumerate(states_to_run):
                print(f"[V-TRAC] Starting analysis for {state_name}...")
                state_start = time.time()
                status_text.info(f"Analyzing {state_name}...")
                
                if 'vtrac_results' not in st.session_state:
                    st.session_state.vtrac_results = {}
                if 'vtrac_reports' not in st.session_state:
                    st.session_state.vtrac_reports = {}
                if 'last_analysis_time' not in st.session_state:
                    st.session_state.last_analysis_time = {}
                
                current_time = time.time()
                cached_results_exist = (
                    state_name in st.session_state.vtrac_results and
                    state_name in st.session_state.last_analysis_time and
                    current_time - st.session_state.last_analysis_time.get(state_name, 0) < 300
                )
                
                if not cached_results_exist:
                    tables = load_state_data(state_name)
                    if not tables:
                        print(f"[V-TRAC] No tables found for {state_name}, skipping.")
                        st.warning(f"No tables found for {state_name}")
                        progress_bar.progress((i + 1) / len(states_to_run))
                        continue
                    
                    results = analyze_all_indexes(state_name)
                    if not results:
                        print(f"[V-TRAC] No analyzable data for {state_name}, skipping.")
                        st.warning(f"No analyzable data found for {state_name}")
                        progress_bar.progress((i + 1) / len(states_to_run))
                        continue
                    
                    st.session_state.vtrac_results[state_name] = results
                    st.session_state.last_analysis_time[state_name] = current_time
                    
                    # Save predictions as JSON for AI training
                    json_filepath = save_predictions_as_json(state_name, results, top_n_reports)
                    if json_filepath:
                        print(f"[V-TRAC] Saved predictions to: {json_filepath}")
                    
                    reports = generate_top_reports(state_name, results, top_n_reports)
                    st.session_state.vtrac_reports[state_name] = reports
                else:
                    print(f"[V-TRAC] Using cached results for {state_name}")
                
                state_end = time.time()
                print(f"[V-TRAC] Finished {state_name} in {state_end - state_start:.2f} seconds.")
                
                progress_bar.progress((i + 1) / len(states_to_run))
            
            total_end = time.time()
            print(f"[V-TRAC] All selected analyses complete in {total_end - total_start:.2f} seconds.")
            status_text.success("Analysis completed!")
    
    # Check if we have analysis results
    has_results = False
    if 'vtrac_results' in st.session_state:
        for s in STATES:
            if s in st.session_state.vtrac_results:
                has_results = True
                break
        if not has_results and selected_option in st.session_state.vtrac_results:
            has_results = True
    
    if has_results:
        st.markdown("## Analysis Results")
        
        available_states = [s for s in STATES if s in st.session_state.vtrac_results]
        
        if len(available_states) > 1:
            if selected_option == "All States" and len(available_states) == 1:
                selected_state = available_states[0]
            else:
                selected_state = st.selectbox("Select State to View Results", available_states, key="vtrac_state_dropdown")
        elif len(available_states) == 1:
            selected_state = available_states[0]
        elif selected_option in st.session_state.vtrac_results:
            selected_state = selected_option
        else:
            st.error("No results found matching the criteria.")
            return
        
        results = st.session_state.vtrac_results[selected_state]
        reports = st.session_state.vtrac_reports.get(selected_state, [])
        
        if selected_state in st.session_state.last_analysis_time:
            last_t = datetime.fromtimestamp(st.session_state.last_analysis_time[selected_state])
            st.info(f"Analysis for {selected_state} was last run on {last_t.strftime('%Y-%m-%d at %H:%M:%S')}")
        
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {selected_state}")
        
        # Display top indexes in a table
        if results:
            top_results = results[:top_n_indexes]
            data = {
                "Rank": [r["rank"] for r in top_results],
                "Index": [r["index"] for r in top_results],
                "Score": [f"{r['score']:.2f}" for r in top_results]
            }
            st.dataframe(pd.DataFrame(data))
        
        # Detailed HTML reports
        if reports and top_n_reports > 0:
            st.subheader("Detailed Analysis Reports")
            report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:top_n_reports]])
            for tab, report in zip(report_tabs, reports[:top_n_reports]):
                with tab:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"V-TRAC Index: {report['index']} | Score: {report['score']:.2f}")
                    with col2:
                        st.download_button(
                            label=f"Download HTML (Rank #{report['rank']})",
                            data=report['html'],
                            file_name=report['filename'],
                            mime="text/html",
                            key=f"dl_html_rank{report['rank']}"
                        )
                        if st.button(
                            f"Open in Browser (Rank #{report['rank']})",
                            key=f"open_browser_{selected_state}_{report['rank']}"
                        ):
                            webbrowser.open(f"file://{os.path.abspath(report['filepath'])}")
                    
                    expand_view = st.checkbox("Expand View", key=f"expand_{selected_state}_{report['rank']}")
                    if expand_view:
                        st.components.v1.html(report['html'], height=4000, scrolling=True)
                    else:
                        st.components.v1.html(report['html'], height=3000, scrolling=True)
        elif top_n_reports > 0:
            st.info("No HTML reports were generated. Analysis might not have produced enough results.")
    else:
        st.info("No analysis results found. Please run an analysis first.")

def render(state: str) -> None:
    """Render the V-TRAC analyzer for the integrated app."""
    _ensure_vtrac_session_state()

    state_slug = _normalize_state_slug(state)
    st.title(f"V-TRAC Analyzer - {state_slug}")
    st.caption("Uses the combined tables produced by the data pipeline.")

    tables_root = Path(get_tables_output_dir())
    slug_candidates = []
    for name in [state_slug, state_slug[:-1] if state_slug.endswith("4") else None, state]:
        if name and name not in slug_candidates:
            slug_candidates.append(name)

    resolved_dir = None
    for name in slug_candidates:
        candidate = (tables_root / name).resolve()
        if candidate.exists() and candidate.is_dir():
            resolved_dir = candidate
            break
    if resolved_dir is None:
        resolved_dir = (tables_root / state_slug).resolve()

    combined_paths = []
    if resolved_dir.exists():
        combined_paths = sorted(path for path in resolved_dir.glob("*_combined.csv"))

    statuses = [
        ("Tables root", tables_root.exists(), str(tables_root)),
        (f"State directory ({resolved_dir.name})", resolved_dir.exists(), str(resolved_dir)),
        ("Combined tables", bool(combined_paths), ", ".join(p.name for p in combined_paths) if combined_paths else "(none)"),
    ]

    st.subheader("Preflight Checks")
    for label, ok, detail in statuses:
        icon = "[OK]" if ok else "[WARN]"
        st.write(f"{icon} {label}: {detail}")

    try:
        show_dev = st.sidebar.checkbox("Show Dev Health (V-TRAC)", value=False, key=f"dev_health_vtrac_{state_slug}")
    except Exception:
        show_dev = False

    if show_dev:
        with st.expander("System Health (V-TRAC)", expanded=False):
            st.caption(f"tables_root: {tables_root} (exists={tables_root.exists()})")
            st.caption(f"state_dir: {resolved_dir} (exists={resolved_dir.exists()})")
            if combined_paths:
                st.caption("Combined tables:")
                for path in combined_paths:
                    try:
                        size = path.stat().st_size
                    except OSError:
                        size = 0
                    st.caption(f"- {path.name} ({size:,} bytes)")
            else:
                st.caption("Combined tables: none found")

    if st.button("Rescan tables & clear cache", key=f"vtrac_rescan_{state_slug}"):
        _clear_vtrac_cache(state_slug)
        st.info("Cache cleared. Re-run analysis to refresh results.")

    if not combined_paths:
        st.warning("No combined tables found. Run the tables pipeline for this state before analyzing V-TRAC.")

    run_disabled = not combined_paths
    if st.button("Run V-TRAC Analysis", type="primary", key=f"vtrac_run_{state_slug}", disabled=run_disabled):
        with st.spinner(f"Running V-TRAC analysis for {state_slug}..."):
            _clear_vtrac_cache(state_slug)
            tables = load_state_data(state_slug)
            if not tables:
                st.warning(f"No tables available for {state_slug}. Run the tables pipeline first.")
            else:
                results = analyze_all_indexes(state_slug)
                if not results:
                    st.warning(f"No analyzable V-TRAC data found for {state_slug}.")
                else:
                    json_path = save_predictions_as_json(state_slug, results, top_n=3)
                    reports = generate_top_reports(state_slug, results, top_n=3)
                    _ensure_vtrac_session_state()
                    st.session_state.vtrac_results[state_slug] = results
                    st.session_state.vtrac_reports[state_slug] = reports
                    st.session_state.last_analysis_time[state_slug] = time.time()
                    st.success(f"V-TRAC analysis complete for {state_slug}.")
                    if json_path:
                        st.caption(f"Predictions JSON saved to {json_path}.")

    _ensure_vtrac_session_state()
    results = st.session_state.get('vtrac_results', {}).get(state_slug)
    if not results:
        return

    top_limit = min(3, len(results))
    st.subheader(f"Top {top_limit} V-TRAC indexes for {state_slug}")

    df = pd.DataFrame({
        "Rank": [r["rank"] for r in results[:top_limit]],
        "Index": [r["index"] for r in results[:top_limit]],
        "Score": [f"{r['score']:.2f}" for r in results[:top_limit]],
    })
    st.dataframe(df, use_container_width=True)

    last_ts = st.session_state.get('last_analysis_time', {}).get(state_slug)
    if last_ts:
        last_dt = datetime.fromtimestamp(last_ts)
        st.caption(f"Last analyzed on {last_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    reports = st.session_state.get('vtrac_reports', {}).get(state_slug, [])
    if not reports:
        return

    st.subheader("Detailed Analysis Reports")
    tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:3]])
    for tab, report in zip(tabs, reports[:3]):
        with tab:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"V-TRAC Index: {report['index']} | Score: {report['score']:.2f}")
            with col2:
                st.download_button(
                    label=f"Download HTML (Rank #{report['rank']})",
                    data=report['html'],
                    file_name=report['filename'],
                    mime="text/html",
                    key=f"dl_html_{state_slug}_{report['rank']}"
                )
                if st.button(
                    f"Open in Browser (Rank #{report['rank']})",
                    key=f"open_browser_{state_slug}_{report['rank']}"
                ):
                    webbrowser.open(f"file://{os.path.abspath(report['filepath'])}")
            expand_key = f"expand_{state_slug}_{report['rank']}"
            expand_view = st.checkbox("Expand View", key=expand_key)
            height = 4000 if expand_view else 3000
            st.components.v1.html(report['html'], height=height, scrolling=True)


if __name__ == "__main__":
    main()

