#!/usr/bin/env python
"""
vtrac_analyzer_standalone.py

Standalone Streamlit interface for V-TRAC analysis ONLY.
This version loads pre-generated tables and does not include data processing tabs.
It is based on enhanced_analyzer_final.py.
"""

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
import time
from functools import lru_cache

# Add script directory to path for imports
# Adjust path assuming this script is in scripts/core
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir)) # Go up two levels
sys.path.append(project_root)


# Import utility modules
try:
    from scripts.utils.path_handler import (
        get_tables_output_dir,
        # Note: Removed get_excel_path, create_output_directories, get_cleaned_data_dir
        get_winners_output_dir # Keep if winner highlighting is needed
    )
    from scripts.utils.state_utils import STATES
    # Note: Removed clean_data, extract_data, table_generator imports related to processing
    from scripts.utils.vtrac_utils import (
        BOXED_VTRAC_REFERENCE,
        find_vtrac_index_and_combos,
        highlight_winners_in_table # Keep if winner highlighting is needed
    )
except ImportError as e:
    print(f"Error importing utility modules: {e}")
    print("Please ensure the script is run from the project root or relevant paths are set.")
    sys.exit(1)


# ---------------------------------------------------------------------------------
# STREAMLIT PAGE CONFIG
# ---------------------------------------------------------------------------------

st.set_page_config(
    page_title="Standalone V-TRAC Analyzer", # Changed Title
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------------------
# SESSION STATE (MATCHING CLUSTERING_APP_3)
# ---------------------------------------------------------------------------------

if 'state_tables' not in st.session_state:
    st.session_state.state_tables = {}
if 'vtrac_results' not in st.session_state:
    st.session_state.vtrac_results = {}
if 'vtrac_reports' not in st.session_state:
    st.session_state.vtrac_reports = {}
if 'last_analysis_time' not in st.session_state:
    st.session_state.last_analysis_time = {}

# ---------------------------------------------------------------------------------
# HELPER FUNCTIONS (Keep necessary ones)
# ---------------------------------------------------------------------------------

def format_time(seconds):
    """Format time in seconds to human-readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    else:
        minutes = int(seconds // 60)
        sec = seconds % 60
        return f"{minutes} min {sec:.2f} sec"

# Removed check_excel_file as it's not needed for standalone analyzer

@lru_cache(maxsize=32)
def load_state_data_cached(state_name):
    """
    Cached loader for a state's CSV tables from the output/tables folder.
    Looks for the newest date folder first.
    THIS IS THE CORE DATA LOADING FUNCTION FOR THE ANALYZER.
    """
    tables_root = get_tables_output_dir()

    if not os.path.exists(tables_root):
        print(f"[ERROR] Tables root directory not found: {tables_root}")
        st.error(f"Required directory not found: {tables_root}. Please generate tables first.")
        return {}

    # Find the state directory directly under tables_root
    # Simplified: Assumes tables are in data/outputs/tables/[STATE_NAME]/
    state_tables_dir = os.path.join(tables_root, state_name)

    if os.path.exists(state_tables_dir) and os.listdir(state_tables_dir):
        print(f"Loading tables for {state_name} from: {state_tables_dir}")
        result = {}
        required_files_found = 0
        required_filenames = [
            f"{state_name}_Midday_combined.csv", f"{state_name}_Evening_combined.csv", f"{state_name}_Combined_combined.csv",
            f"{state_name}_Midday_R2_only.csv", f"{state_name}_Evening_R2_only.csv", f"{state_name}_Combined_R2_only.csv"
        ]

        for filename in os.listdir(state_tables_dir):
            if filename.endswith(".csv"):
                filepath = os.path.join(state_tables_dir, filename)
                # Key uses filename without state prefix and extension
                key_parts = os.path.splitext(filename)[0].split(f"{state_name}_")
                key = key_parts[1] if len(key_parts) > 1 else os.path.splitext(filename)[0]
                try:
                    df = pd.read_csv(filepath)
                    result[key] = df
                    if filename in required_filenames:
                        required_files_found += 1
                except Exception as e:
                    print(f"[ERROR] Error loading {filename}: {e}")
                    st.warning(f"Could not load table: {filename}")
        if result:
             # Warn if not all 6 standard tables were found
            if required_files_found < 6:
                print(f"[WARNING] Found {required_files_found}/6 standard tables for {state_name}.")
                # st.warning(f"Found {required_files_found}/6 standard tables for {state_name}. Analysis might be incomplete.")
            return result

    print(f"[ERROR] No tables found for {state_name} in {state_tables_dir}")
    st.error(f"No CSV tables found in {state_tables_dir}. Please run the table generation pipeline first.")
    return {}

def load_state_data(state_name):
    """
    Load generated tables for a specific state using session-state caching
    so we don't re-read from disk every time.
    """
    # If we already loaded this state's data in session_state, just use it
    if state_name in st.session_state.state_tables:
        return st.session_state.state_tables[state_name]

    tables = load_state_data_cached(state_name)
    if tables:
        st.session_state.state_tables[state_name] = tables
    return tables

# ---------------------------------------------------------------------------------
# V-TRAC ANALYSIS FUNCTIONS (Copied from enhanced_analyzer_final.py - NO CHANGES NEEDED HERE)
# ---------------------------------------------------------------------------------

def get_all_combinations_for_index(index):
    """Get all pattern combinations for a specific V-TRAC index from BOXED_VTRAC_REFERENCE."""
    vtrac_entry = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == index), None)
    if vtrac_entry:
        combos = set()
        combos.update(vtrac_entry.get("Singles", []))
        combos.update(vtrac_entry.get("Doubles", []))
        return combos
    return set()

def count_patterns_in_table(df, patterns):
    """Count occurrences of each pattern in columns ['7','6','5','4','3','2','1']."""
    pattern_counts = {p: 0 for p in patterns}
    total_matches = 0
    if df is None or df.empty:
        return pattern_counts, total_matches

    columns = [c for c in ['7','6','5','4','3','2','1'] if c in df.columns]
    for col in columns:
        # Ensure column is treated as string, handle potential NaN/float values gracefully
        try:
            series_str = df[col].astype(str)
        except Exception:
            series_str = df[col].fillna('').astype(str) # Fallback for mixed types

        for cell_val in series_str:
            for p in patterns:
                # Ensure pattern `p` is also a string for comparison
                p_str = str(p)
                c = cell_val.count(p_str)
                if c > 0:
                    pattern_counts[p] += c
                    total_matches += c
    return pattern_counts, total_matches

def analyze_pattern_persistence(df, patterns):
    """Check how long patterns persist across consecutive columns (7->1)."""
    scores = {p: 0 for p in patterns}
    if df is None or df.empty:
        return scores

    columns = [c for c in ['7','6','5','4','3','2','1'] if c in df.columns]
    for p in patterns:
        p_str = str(p) # Ensure pattern is string
        for _, row in df.iterrows():
            consecutive = 0
            max_consecutive = 0
            for col in columns:
                val = str(row[col])
                if p_str in val:
                    consecutive += 1
                else:
                    max_consecutive = max(max_consecutive, consecutive)
                    consecutive = 0
            # End of row check
            max_consecutive = max(max_consecutive, consecutive)
            # Weighted by squares
            scores[p] += max_consecutive**2
    return scores

def analyze_pattern_stability(df, patterns):
    """Check if patterns appear across multiple row types (R2, R4, R6, R8)."""
    scores = {p: 0 for p in patterns}
    if df is None or df.empty or 'RowType' not in df.columns or 'Set' not in df.columns or 'Draw' not in df.columns:
        return scores # Cannot perform stability without these columns

    grouped = df.groupby(['Set','Draw'])
    for _, group in grouped:
        rowtypes = group['RowType'].unique()
        # If there's only 1 row type in the group, skip
        if len(rowtypes) < 2:
            continue
        for p in patterns:
            p_str = str(p)
            rowtype_count = 0
            for rt in ['R2','R4','R6','R8']:
                sub = group[group['RowType'] == rt]
                if sub.empty:
                    continue
                # If pattern appears in any col
                found = False
                for col in ['7','6','5','4','3','2','1']:
                    if col not in sub.columns:
                        continue
                    # Ensure column is string before checking `any`
                    try:
                        col_str = sub[col].astype(str)
                    except Exception:
                        col_str = sub[col].fillna('').astype(str)

                    if any(p_str in str(v) for v in col_str):
                        found = True
                        break
                if found:
                    rowtype_count += 1
            scores[p] += rowtype_count**2
    return scores

def detect_straight_combinations(df, pattern):
    """
    If a pattern appears more than once in the same row (across columns),
    we count that as multiple straight occurrences.
    """
    if df is None or df.empty:
        return 0
    columns = [c for c in ['7','6','5','4','3','2','1'] if c in df.columns]
    straight_count = 0
    p_str = str(pattern) # Ensure pattern is string
    for _, row in df.iterrows():
        occurrences = 0
        for col in columns:
            val = str(row[col])
            if p_str in val:
                # Count how many times pattern appears in this cell
                 occurrences += val.count(p_str)
        # Sum occurrences across the row for this pattern
        straight_count += occurrences

    return straight_count

def calculate_index_score(tables, patterns):
    """
    Weighted scoring across 'Midday_combined', 'Evening_combined', 'Combined_combined',
    plus optional R2 tables if available. Summarizes occurrence, persistence, stability,
    and 'straight' combos into a single numeric score.
    """
    if not tables or not patterns:
        st.warning("Cannot calculate score: No tables or patterns provided.")
        return 0

    # Weighted table references (Using keys consistent with load_state_data_cached)
    tables_to_score = {
        "Combined_combined": 3.0,  # highest weight
        "Midday_combined": 1.5,
        "Evening_combined": 1.5,
        "Combined_R2_only": 2.0, # Adjusted key
        "Midday_R2_only": 1.0,   # Adjusted key
        "Evening_R2_only": 1.0   # Adjusted key
    }

    occurrence_score = 0
    persistence_score = 0
    stability_score = 0
    straight_score = 0
    tables_found_count = 0

    for tname, weight in tables_to_score.items():
        df = tables.get(tname)
        if df is None or df.empty:
            # print(f"[Debug] Table '{tname}' not found or empty for scoring.")
            continue # Skip missing tables

        tables_found_count += 1
        # print(f"[Debug] Scoring table: {tname} with weight {weight}")

        # Occurrence
        _, match_count = count_patterns_in_table(df, patterns)
        occurrence_score += (match_count * weight)

        # Persistence
        pers = analyze_pattern_persistence(df, patterns)
        persistence_score += (sum(pers.values()) * weight)

        # Stability only if table has RowType
        if 'RowType' in df.columns:
            stab = analyze_pattern_stability(df, patterns)
            stability_score += (sum(stab.values()) * weight)
        # else:
            # print(f"[Debug] Skipping stability for {tname} (no RowType column)")

        # Straight combos
        for p in patterns:
            scount = detect_straight_combinations(df, p)
            straight_score += (scount * weight)

    if tables_found_count == 0:
        st.warning("No standard tables found for scoring. Please ensure tables are generated.")
        return 0

    # Weighted combination
    overall_score = (
        occurrence_score * 0.35 +
        persistence_score * 0.30 +
        stability_score * 0.25 +
        straight_score * 0.10
    )
    # print(f"[Debug] Calculated score: {overall_score:.2f} (Occ: {occurrence_score:.1f}, Pers: {persistence_score:.1f}, Stab: {stability_score:.1f}, Str: {straight_score:.1f})")
    return overall_score

def analyze_all_indexes(state_name):
    """Analyze all known V-TRAC indexes for the given state, computing a ranking."""
    print(f"Analyzing all indexes for: {state_name}")
    tables = load_state_data(state_name)
    if not tables:
        st.error(f"Failed to load tables for {state_name}. Cannot perform analysis.")
        return None # Return None if tables fail to load

    vtrac_indices = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()

    total_indices = len(vtrac_indices)
    for i, idx in enumerate(vtrac_indices):
        status_text.info(f"Analyzing Index {idx}/{total_indices}...")
        patterns = get_all_combinations_for_index(idx)
        if not patterns:
            continue
        score = calculate_index_score(tables, patterns)
        results.append({
            "index": idx,
            "patterns": patterns,
            "score": score
        })
        progress_bar.progress((i + 1) / total_indices)

    status_text.success("Index analysis complete.")
    progress_bar.empty() # Clear progress bar

    # Sort descending by score
    results.sort(key=lambda x: x["score"], reverse=True)
    # Assign rank after sorting
    for i, r in enumerate(results):
        r["rank"] = i + 1

    print(f"Analysis complete for {state_name}. Top score: {results[0]['score']:.2f} (Index {results[0]['index']})")
    return results

def generate_index_html_report(state_name, index, patterns, tables, score, rank, timestamp=None):
    """
    Produce an HTML snippet (including <table> with highlighting)
    that shows midday/evening/combined plus pattern stats (occurrence, persistence, etc.).
    """
    from datetime import datetime
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def highlight_table_html(df, title):
        if df is None or df.empty:
            # Return a placeholder if data is missing
            return f'<div class="table-container"><h2>{title}</h2><p style="color: grey;">No data available for this table.</p></div>'

        # Ensure required columns exist, add if missing with default value like 'N/A'
        required_cols = ['Set','Draw','RowType','7','6','5','4','3','2','1']
        for col in required_cols:
            if col not in df.columns:
                df[col] = 'N/A' # Add missing column

        # Reorder columns to standard order
        df = df[required_cols]

        html_out = [f'<div class="table-container"><h2>{title}</h2><table>']
        # Table header
        html_out.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in df.columns) + "</tr></thead>")
        # Table body
        html_out.append("<tbody>")
        for _, row in df.iterrows():
            html_out.append("<tr>")
            for c in df.columns:
                # Safely convert cell value to string, handling potential NaN or other types
                try:
                    val = str(row[c]) if pd.notna(row[c]) else ''
                except Exception:
                    val = '' # Fallback for unexpected types

                # Highlight patterns (ensure pattern `p` is string)
                highlighted_val = val
                for p in patterns:
                    p_str = str(p)
                    if p_str in highlighted_val:
                        # Use a placeholder to avoid nested spans if pattern contains span tag itself (unlikely but safe)
                        placeholder = f"__HIGHLIGHT__{p_str}__ENDHIGHLIGHT__"
                        highlighted_val = highlighted_val.replace(p_str, placeholder)

                # Replace placeholders with actual span tags
                highlighted_val = highlighted_val.replace("__HIGHLIGHT__", '<span class="highlight">').replace("__ENDHIGHLIGHT__", '</span>')

                html_out.append(f"<td>{highlighted_val}</td>")
            html_out.append("</tr>")
        html_out.append("</tbody></table></div>")
        return "\n".join(html_out)

    # Build main HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>V-TRAC Analysis - Index {index}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 15px;
            background-color: #f9f9f9;
            color: #333;
        }}
        h1, h2, h3 {{
            color: #800080; /* Purple theme */
        }}
        h1 {{
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }}
        h2 {{
            margin-top: 25px;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }}
        table {{
            border-collapse: collapse;
            margin: 15px 0;
            width: 100%;
            font-size: 0.9em; /* Slightly smaller table font */
            background-color: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 10px; /* Adjusted padding */
            text-align: center;
            white-space: nowrap; /* Prevent wrapping */
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: 600; /* Slightly less bold */
            color: #555;
        }}
        tbody tr:nth-child(even) {{ background-color: #fdfdfd; }}
        .version {{
            color: #999;
            font-size: 0.85em;
            margin-bottom: 10px;
            text-align: right;
        }}
        .highlight {{
            color: #800080; /* Purple */
            font-weight: 700;
            background-color: rgba(128, 0, 128, 0.08); /* Subtle highlight bg */
            padding: 1px 2px;
            border-radius: 3px;
        }}
        .stats {{
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #eee;
        }}
        .stats h2, .stats h3 {{
            margin-top: 0;
            color: #800080;
        }}
        .stats h3 {{
            font-size: 1.1em;
            margin-bottom: 10px;
        }}
        .stats table {{
            width: auto; /* Allow stats tables to shrink */
            min-width: 300px;
            margin-left: 10px;
        }}
        .three-column-layout {{
            display: flex;
            flex-wrap: nowrap; /* Prevent wrapping to ensure columns */
            justify-content: space-between;
            width: 100%;
            gap: 15px; /* Add gap between columns */
            margin-bottom: 20px;
            overflow-x: auto; /* Allow horizontal scroll on small screens */
        }}
        .column {{
            flex: 1; /* Each column takes equal width */
            min-width: 300px; /* Minimum width before scroll */
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #eee;
        }}
        .column h2 {{
            margin-top: 0;
            font-size: 1.2em;
        }}
        /* Responsive adjustments if needed */
        @media (max-width: 1200px) {{ /* Adjust breakpoint as needed */
             .three-column-layout {{
                flex-wrap: wrap; /* Allow wrapping on smaller screens */
             }}
             .column {{
                 flex: 1 1 100%; /* Full width on smaller screens */
                 margin-bottom: 15px;
             }}
        }}
        .rank-badge {{
            display: inline-block;
            background-color: #800080;
            color: white;
            font-weight: bold;
            padding: 6px 12px;
            font-size: 0.9em;
            border-radius: 20px;
            margin-right: 15px;
        }}
        .pattern-list {{
            font-size: 0.9em;
            color: #555;
            word-break: break-all; /* Break long pattern lists */
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
<div class="version">Generated: {timestamp}</div>
<h1><span class="rank-badge">Rank #{rank}</span> V-TRAC Analysis: {state_name} - Index {index}</h1>

<div class="three-column-layout">
    <div class="column">
"""
    # Midday Table Data
    # Use .get() with default to handle potentially missing tables gracefully
    html += highlight_table_html(tables.get("Midday_combined"), "Midday Combined")
    html += highlight_table_html(tables.get("Midday_R2_only"), "Midday R2-only")
    html += "</div><div class=\"column\">"

    # Evening Table Data
    html += highlight_table_html(tables.get("Evening_combined"), "Evening Combined")
    html += highlight_table_html(tables.get("Evening_R2_only"), "Evening R2-only")
    html += "</div><div class=\"column\">"

    # Combined Table Data
    html += highlight_table_html(tables.get("Combined_combined"), "Combined Combined")
    html += highlight_table_html(tables.get("Combined_R2_only"), "Combined R2-only")
    html += "</div></div>"

    # Analysis stats section
    html += f"""
<div class="stats">
    <h2>Analysis Statistics</h2>
    <p><strong>Index Score:</strong> {score:.2f}</p>
    <p><strong>Total Unique Patterns for Index {index}:</strong> {len(patterns)}</p>
    <p class="pattern-list"><strong>Patterns:</strong> {', '.join(sorted(list(patterns)))}</p>
"""

    # Create sub-sections for detailed stats
    html += '<div style="display: flex; flex-wrap: wrap; gap: 20px;">' # Flex container for stats tables

    # 1) Pattern occurrence counts
    html += '<div><h3>Occurrence Counts</h3><table><thead><tr><th>Pattern</th><th>Occurrences</th></tr></thead><tbody>'
    # Use Combined_combined as the primary source for stats, check if exists
    combined_table_for_stats = tables.get("Combined_combined")
    if combined_table_for_stats is not None and not combined_table_for_stats.empty:
        pc, _ = count_patterns_in_table(combined_table_for_stats, patterns)
        for p, cnt in sorted(pc.items(), key=lambda x:x[1], reverse=True):
             if cnt > 0: # Only show patterns that occurred
                 html += f"<tr><td>{p}</td><td>{cnt}</td></tr>"
    else:
        html += '<tr><td colspan="2" style="color: grey;">Combined table missing</td></tr>'
    html += "</tbody></table></div>"

    # 2) Persistence
    html += "<div><h3>Persistence Scores</h3><table><thead><tr><th>Pattern</th><th>Score</th></tr></thead><tbody>"
    if combined_table_for_stats is not None and not combined_table_for_stats.empty:
        pers = analyze_pattern_persistence(combined_table_for_stats, patterns)
        for p, val in sorted(pers.items(), key=lambda x:x[1], reverse=True):
             if val > 0:
                 html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    else:
        html += '<tr><td colspan="2" style="color: grey;">Combined table missing</td></tr>'
    html += "</tbody></table></div>"

    # 3) Stability
    html += "<div><h3>Stability Scores</h3><table><thead><tr><th>Pattern</th><th>Score</th></tr></thead><tbody>"
    if combined_table_for_stats is not None and not combined_table_for_stats.empty and 'RowType' in combined_table_for_stats.columns:
        stab = analyze_pattern_stability(combined_table_for_stats, patterns)
        for p, val in sorted(stab.items(), key=lambda x:x[1], reverse=True):
             if val > 0:
                 html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    else:
        html += '<tr><td colspan="2" style="color: grey;">Combined table missing or lacks RowType</td></tr>'
    html += "</tbody></table></div>"

    # 4) Straight combos
    html += "<div><h3>Straight Occurrences</h3><table><thead><tr><th>Pattern</th><th>Occurrences</th></tr></thead><tbody>"
    if combined_table_for_stats is not None and not combined_table_for_stats.empty:
        scounts = {p: detect_straight_combinations(combined_table_for_stats, p) for p in patterns}
        for p, val in sorted(scounts.items(), key=lambda x: x[1], reverse=True):
             if val > 0:
                 html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    else:
        html += '<tr><td colspan="2" style="color: grey;">Combined table missing</td></tr>'
    html += "</tbody></table></div>"

    html += '</div>' # Close flex container for stats
    html += "</div></body></html>"
    return html

def generate_top_reports(state_name, results, top_n=3):
    """
    Generate HTML reports for the top-N indexes of a single state.
    Returns a list of {rank, index, score, filename, filepath, html}.
    """
    if not results:
        st.warning(f"No analysis results provided for {state_name} to generate reports.")
        return []

    print(f"Generating top {top_n} reports for {state_name}...")
    tables = load_state_data(state_name)
    if not tables:
        st.error(f"Failed to load tables for {state_name}. Cannot generate reports.")
        return []

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports = []
    # Define output directory for analysis reports
    # Assumes script is in scripts/core, so go up two levels for project root
    analysis_dir = os.path.join(project_root, "data", "outputs", "analysis")
    os.makedirs(analysis_dir, exist_ok=True)

    # Ensure results list has ranks
    if results and 'rank' not in results[0]:
         for i, r in enumerate(results):
             r['rank'] = i + 1

    for r in results[:top_n]:
        # Check if all required keys exist in the result dictionary
        required_keys = ["index", "score", "patterns", "rank"]
        if not all(key in r for key in required_keys):
            print(f"[WARNING] Skipping report generation for a result due to missing keys: {r}")
            continue

        idx = r["index"]
        sc = r["score"]
        pats = r["patterns"]
        rank = r["rank"]
        print(f"  Generating report for Rank {rank}, Index {idx}...")
        try:
            html = generate_index_html_report(state_name, idx, pats, tables, sc, rank, timestamp)
            filename = f"{state_name}_vtrac_rank{rank}_index{idx}_{timestamp}.html"
            filepath = os.path.join(analysis_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            reports.append({
                "rank": rank,
                "index": idx,
                "score": sc,
                "filename": filename,
                "filepath": filepath,
                "html": html
            })
        except Exception as e:
            print(f"[ERROR] Failed to generate report for Index {idx}: {e}")
            st.error(f"Error generating report for Index {idx}: {e}")

    print(f"Generated {len(reports)} reports for {state_name}.")
    return reports

# ---------------------------------------------------------------------------------
# REMOVED TABS: process_data_tab, view_results_tab, log_winners_tab
# ---------------------------------------------------------------------------------

# The process_data_tab() function definition is removed.
# The view_results_tab() function definition is removed.
# The log_winners_tab() function definition is removed.

# ---------------------------------------------------------------------------------
# KEPT AND RENAMED: vtrac_analyzer_tab() becomes the main content
# ---------------------------------------------------------------------------------

def vtrac_analyzer_main_content(): # Renamed function
    """
    Main content area for V-TRAC analysis.
    Loads existing tables and performs analysis.
    """
    st.header("Standalone V-TRAC Pattern Analyzer")
    st.markdown("""
    This tool analyzes V-TRAC indexes using pre-generated tables. Select a state to begin.
    Ensure tables have been generated using the `generate_tables_pipeline.bat` script first.
    """)
    # Removed info message about long run times as processing is separate

    # State selection - crucial for loading data
    selected_state = st.selectbox("Select State to Analyze", STATES, key="vtrac_state_select_standalone")
    if not selected_state:
        st.warning("Please select a state.")
        return # Cannot proceed without a state

    top_n_indexes = st.slider("Number of Top Indexes to Display", 1, 35, 10, key="standalone_slider_indexes")
    top_n_reports = st.slider("Number of HTML Reports to Generate", 0, 10, 3, key="standalone_slider_reports")

    # Analysis Button
    if st.button("Run V-TRAC Analysis", type="primary", key="vtrac_standalone_run_button"):
        # Clear previous results for this state before running new analysis
        if selected_state in st.session_state.vtrac_results:
            del st.session_state.vtrac_results[selected_state]
        if selected_state in st.session_state.vtrac_reports:
            del st.session_state.vtrac_reports[selected_state]
        if selected_state in st.session_state.last_analysis_time:
             del st.session_state.last_analysis_time[selected_state]

        with st.spinner(f"Running V-TRAC Analysis for {selected_state}..."):
            total_start = time.time()

            # Load data - This now uses the function that reads from disk
            tables = load_state_data(selected_state)
            if not tables:
                # Error messages are handled within load_state_data
                st.error(f"Could not load necessary tables for {selected_state}. Analysis aborted.")
                return # Stop if tables aren't loaded

            # Run analysis
            results = analyze_all_indexes(selected_state)

            # Check if analysis returned results
            if not results:
                st.warning(f"Analysis for {selected_state} did not produce results. Check table data.")
                # Clear session state just in case partial data was stored
                if selected_state in st.session_state.vtrac_results: del st.session_state.vtrac_results[selected_state]
                if selected_state in st.session_state.vtrac_reports: del st.session_state.vtrac_reports[selected_state]
                return # Stop if analysis failed

            # Store results and reports in session state
            st.session_state.vtrac_results[selected_state] = results
            st.session_state.last_analysis_time[selected_state] = time.time()
            reports = generate_top_reports(selected_state, results, top_n_reports)
            st.session_state.vtrac_reports[selected_state] = reports

            total_end = time.time()
            st.success(f"Analysis for {selected_state} completed in {format_time(total_end - total_start)}!")

    # --- Display Results Area --- (This part runs always if results exist) --- 
    if selected_state and selected_state in st.session_state.vtrac_results:
        st.markdown("--- ") # Separator
        st.markdown("## Analysis Results")

        results = st.session_state.vtrac_results[selected_state]
        reports = st.session_state.vtrac_reports.get(selected_state, [])

        # Display last analysis time
        if selected_state in st.session_state.last_analysis_time:
            last_t = datetime.fromtimestamp(st.session_state.last_analysis_time[selected_state])
            st.info(f"Analysis results generated on: {last_t.strftime('%Y-%m-%d at %H:%M:%S')}")

        if not results:
             st.warning(f"No analysis results available for {selected_state}.")
             return # Exit display if no results

        # Display Top Indexes Table
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {selected_state}")
        top_df = pd.DataFrame([
            {
                "Rank": r["rank"],
                "Index": r["index"],
                "Score": f"{r['score']:.2f}",
                "Patterns": len(r["patterns"]),
                # Safer way to get top patterns
                "Top Patterns": ", ".join(sorted(list(r.get("patterns", set()))))[:80] + ("..." if len(r.get("patterns", set())) > 5 else "")
            }
            for r in results[:top_n_indexes]
        ])
        # Use st.table for simpler layout, or st.dataframe
        st.dataframe(top_df, use_container_width=True)

        # Display Top Ranked Index Tables (Midday/Evening/Combined) in columns
        if results:
            best_result = results[0] # Rank #1
            st.subheader(f"Tables for Top Ranked Index (#{best_result['rank']} - Index {best_result['index']})")
            # st.write("Displays Midday, Evening, and Combined tables loaded for this state.")

            st_tbls = load_state_data(selected_state) # Reload or use cached tables
            if not st_tbls:
                st.warning("Could not load tables to display top rank details.")
            else:
                col1, col2, col3 = st.columns(3)
                table_keys = {
                    col1: ["Midday_combined", "Midday_R2_only"],
                    col2: ["Evening_combined", "Evening_R2_only"],
                    col3: ["Combined_combined", "Combined_R2_only"]
                }
                column_titles = {col1: "Midday", col2: "Evening", col3: "Combined"}

                for col, keys in table_keys.items():
                    with col:
                        st.markdown(f"**{column_titles[col]} Data**")
                        table_found_in_col = False
                        for key in keys:
                            if key in st_tbls and not st_tbls[key].empty:
                                table_found_in_col = True
                                # Display table title based on key
                                title = key.replace("_", " ").replace("combined", "Combined").replace("R2 only", "R2-only").replace(selected_state, "").strip()
                                st.markdown(f"*{title} Table*", unsafe_allow_html=True)
                                st.dataframe(st_tbls[key], use_container_width=True, height=300)
                                # Add download button for this specific table
                                csv_data = st_tbls[key].to_csv(index=False)
                                st.download_button(
                                    label=f"Download {title}",
                                    data=csv_data,
                                    file_name=f"{selected_state}_{key}.csv",
                                    mime="text/csv",
                                    key=f"dl_top_{key}"
                                )
                                st.markdown("&nbsp;", unsafe_allow_html=True) # Add space
                        if not table_found_in_col:
                             st.info(f"No {column_titles[col]} tables available.")

        # Display Detailed HTML Reports in Tabs
        if reports and top_n_reports > 0:
            st.subheader("Detailed Analysis Reports")
            # Make sure reports have ranks
            for i, rep in enumerate(reports): rep['rank'] = i + 1

            report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:top_n_reports]])
            for tab, rep in zip(report_tabs, reports[:top_n_reports]):
                with tab:
                    col1, col2 = st.columns([3,1]) # Adjust column ratio
                    with col1:
                        st.write(f"**V-TRAC Index:** {rep['index']} | **Score:** {rep['score']:.2f}")
                    with col2:
                        st.download_button(
                            label=f"Download HTML",
                            data=rep["html"],
                            file_name=rep["filename"],
                            mime="text/html",
                            key=f"dl_html_rank{rep['rank']}_standalone"
                        )
                        # Optional: Add 'Open in Browser' button
                        # if st.button(f"Open HTML", key=f"open_browser_{selected_state}_{rep['rank']}_standalone"):
                        #     try: webbrowser.open(f"file://{os.path.abspath(rep['filepath'])}")
                        #     except Exception as e: st.error(f"Could not open file: {e}")

                    st.markdown("--- ") # Separator
                    # IFrame embedding for HTML report
                    st.components.v1.html(rep["html"], height=800, scrolling=True)
        elif top_n_reports > 0:
            st.info("No HTML reports were generated for this analysis run.")
    elif st.session_state.get('vtrac_results') is not None: # Check if analysis was run but failed
         st.warning("No results available for the selected state. Please run analysis.")

# ---------------------------------------------------------------------------------
# MAIN APP LAYOUT FOR STANDALONE
# ---------------------------------------------------------------------------------

def main():
    st.sidebar.title("Standalone V-TRAC Analyzer")
    # You can add a different icon or image if desired
    st.sidebar.image("https://img.icons8.com/fluency/96/target-spotlight.png", width=80)
    st.sidebar.markdown("---")
    st.sidebar.info("This tool analyzes pre-generated CSV tables.")
    st.sidebar.markdown("Run `generate_tables_pipeline.bat` first if tables are missing or outdated.")

    # Main content area - directly call the analyzer content function
    vtrac_analyzer_main_content()

    st.sidebar.markdown("---")
    st.sidebar.text(f"App Loaded: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 