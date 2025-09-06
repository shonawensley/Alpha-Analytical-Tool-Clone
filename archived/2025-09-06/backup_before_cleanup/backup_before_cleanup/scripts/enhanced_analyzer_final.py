#!/usr/bin/env python
"""
enhanced_analyzer_final.py - Enhanced Streamlit interface with V-TRAC analyzer
Based on the original Enhanced Analyzer with exact processing and scoring logic,
restoring the three-column clustering layout and HTML reports seen in clustering_app_3.py.
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
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

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
from utils.state_utils import STATES
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables
from utils.vtrac_utils import (
    BOXED_VTRAC_REFERENCE,
    find_vtrac_index_and_combos,
    highlight_winners_in_table
)

# ---------------------------------------------------------------------------------
# STREAMLIT PAGE CONFIG
# ---------------------------------------------------------------------------------

st.set_page_config(
    page_title="Enhanced V-TRAC Analyzer FINAL",
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
# HELPER FUNCTIONS
# ---------------------------------------------------------------------------------

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

@lru_cache(maxsize=32)
def load_state_data_cached(state_name):
    """
    Cached loader for a state's CSV tables from the output/tables folder.
    Looks directly in the tables/state_name directory.
    """
    print(f"[V-TRAC] Looking for tables for {state_name}...")
    
    # Use direct path like in the working version
    tables_dir = os.path.join(get_tables_output_dir(), state_name)
    result = {}
    
    if not os.path.exists(tables_dir):
        print(f"[ERROR] Tables directory not found: {tables_dir}")
        return {}
    
    print(f"[V-TRAC] Found tables directory for {state_name}")
    
    # Load all CSV files
    for filename in os.listdir(tables_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(tables_dir, filename)
            # Extract table key (remove state prefix)
            key = os.path.splitext(filename)[0].replace(f"{state_name}_", "")
            try:
                df = pd.read_csv(filepath)
                result[key] = df
                print(f"[V-TRAC] Loaded table: {key}")
            except Exception as e:
                print(f"[ERROR] Error loading {filename}: {e}")
    
    if result:
        return result
    else:
        print(f"[ERROR] No tables found for {state_name} in {tables_dir}")
        return {}

def load_state_data(state_name):
    """
    Load generated tables for a specific state using session-state caching
    so we don't re-read from disk every time.
    """
    # If we already loaded this state's data in session_state, just use it
    if state_name in st.session_state.state_tables:
        print(f"[V-TRAC] Using tables from session state for {state_name}")
        return st.session_state.state_tables[state_name]
    
    # Not in session state, load from disk
    print(f"[V-TRAC] Loading tables from disk for {state_name}")
    tables = load_state_data_cached(state_name)
    if tables:
        st.session_state.state_tables[state_name] = tables
    return tables

# ---------------------------------------------------------------------------------
# V-TRAC ANALYSIS FUNCTIONS
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
        for cell_val in df[col].astype(str):
            for p in patterns:
                c = cell_val.count(p)
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
        for _, row in df.iterrows():
            consecutive = 0
            max_consecutive = 0
            for col in columns:
                val = str(row[col])
                if p in val:
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
    if df is None or df.empty:
        return scores

    grouped = df.groupby(['Set','Draw'])
    for _, group in grouped:
        rowtypes = group['RowType'].unique()
        # If there's only 1 row type in the group, skip
        if len(rowtypes) < 2:
            continue
        for p in patterns:
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
                    if any(p in str(v) for v in sub[col]):
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
    for _, row in df.iterrows():
        occurrences = 0
        for col in columns:
            val = str(row[col])
            if pattern in val:
                occurrences += 1
        if occurrences > 1:
            straight_count += occurrences
    return straight_count

def calculate_index_score(tables, patterns):
    """
    Weighted scoring across 'Midday_combined', 'Evening_combined', 'Combined_combined',
    plus optional R2 tables if available. Summarizes occurrence, persistence, stability,
    and 'straight' combos into a single numeric score.
    """
    if not tables or not patterns:
        return 0

    # Weighted table references
    tables_to_score = {
        "Combined_combined": 3.0,  # highest weight
        "Midday_combined": 1.5,
        "Evening_combined": 1.5,
        "Combined_r2": 2.0,
        "Midday_r2": 1.0,
        "Evening_r2": 1.0
    }

    occurrence_score = 0
    persistence_score = 0
    stability_score = 0
    straight_score = 0

    for tname, weight in tables_to_score.items():
        df = tables.get(tname, pd.DataFrame())
        if df.empty:
            continue

        # occurrence
        _, match_count = count_patterns_in_table(df, patterns)
        occurrence_score += (match_count * weight)

        # persistence
        pers = analyze_pattern_persistence(df, patterns)
        persistence_score += (sum(pers.values()) * weight)

        # stability only if table has RowType
        if 'RowType' in df.columns:
            stab = analyze_pattern_stability(df, patterns)
            stability_score += (sum(stab.values()) * weight)

        # straight combos
        for p in patterns:
            scount = detect_straight_combinations(df, p)
            straight_score += (scount * weight)

    # Weighted combination
    overall_score = (
        occurrence_score * 0.35 +
        persistence_score * 0.30 +
        stability_score * 0.25 +
        straight_score * 0.10
    )
    return overall_score

def analyze_all_indexes(state_name):
    """Analyze all known V-TRAC indexes for the given state, computing a ranking."""
    # First, check if we already have analysis results for this state
    if state_name in st.session_state.vtrac_results:
        print(f"[V-TRAC] Using cached analysis results for {state_name}")
        return st.session_state.vtrac_results[state_name]
    
    # If not in cache, load tables and perform analysis
    print(f"[V-TRAC] No cached results found, analyzing {state_name}...")
    tables = load_state_data(state_name)
    if not tables:
        return None

    vtrac_indices = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
    results = []

    for idx in vtrac_indices:
        patterns = get_all_combinations_for_index(idx)
        if not patterns:
            continue
        score = calculate_index_score(tables, patterns)
        results.append({
            "index": idx,
            "patterns": patterns,
            "score": score
        })

    # Sort descending by score
    results.sort(key=lambda x: x["score"], reverse=True)
    for i, r in enumerate(results):
        r["rank"] = i + 1
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
            return f"<h2>{title}</h2><p>No data available</p>"

        html_out = [f"<h2>{title}</h2><table>"]
        cols = ['Set','Draw','RowType','7','6','5','4','3','2','1']
        # table header
        html_out.append("<tr>" + "".join(f"<th>{c}</th>" for c in cols if c in df.columns) + "</tr>")
        # table rows
        for _, row in df.iterrows():
            html_out.append("<tr>")
            for c in cols:
                if c not in df.columns:
                    continue
                val = str(row[c])
                # highlight patterns
                for p in patterns:
                    if p in val:
                        val = val.replace(p, f'<span class="highlight">{p}</span>')
                html_out.append(f"<td>{val}</td>")
            html_out.append("</tr>")
        html_out.append("</table>")
        return "\n".join(html_out)

    # Build main HTML
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
            margin: 20px 0;
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
            margin-bottom: 20px;
        }}
        .three-column-layout {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            width: 100%;
        }}
        .column {{
            flex: 0 0 32%;
            margin-bottom: 20px;
            min-width: 30%;
        }}
        @media (max-width: 1500px) {{
            .column {{
                flex: 0 0 100%;
                min-width: 100%;
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
    </style>
</head>
<body>
<div class="version">Version: v{timestamp}</div>
<h1><span class="rank-badge">Rank #{rank}</span> V-TRAC Analysis for {state_name} - Index {index}</h1>

<div class="three-column-layout">
    <div class="column"><h2>Midday Data</h2>
"""
    # Midday
    if "Midday_combined" in tables:
        html += highlight_table_html(tables["Midday_combined"], f"{state_name} Midday Combined Table")
    if "Midday_r2" in tables:
        html += highlight_table_html(tables["Midday_r2"], f"{state_name} Midday R2-only Table")
    html += "</div><div class=\"column\"><h2>Evening Data</h2>"

    # Evening
    if "Evening_combined" in tables:
        html += highlight_table_html(tables["Evening_combined"], f"{state_name} Evening Combined Table")
    if "Evening_r2" in tables:
        html += highlight_table_html(tables["Evening_r2"], f"{state_name} Evening R2-only Table")
    html += "</div><div class=\"column\"><h2>Combined Data</h2>"

    # Combined
    if "Combined_combined" in tables:
        html += highlight_table_html(tables["Combined_combined"], f"{state_name} Combined Combined Table")
    if "Combined_r2" in tables:
        html += highlight_table_html(tables["Combined_r2"], f"{state_name} Combined R2-only Table")
    html += "</div></div>"

    # Analysis stats
    html += f"""
<div class="stats">
    <h2>Analysis Statistics</h2>
    <p><strong>Index Score:</strong> {score:.2f}</p>
    <p><strong>Total Patterns:</strong> {len(patterns)}</p>
    <p><strong>Pattern List:</strong> {', '.join(sorted(patterns))}</p>
"""

    # 1) Pattern occurrence counts
    html += "<h3>Pattern Occurrence Counts</h3><table><tr><th>Pattern</th><th>Occurrences</th></tr>"
    if "Combined_combined" in tables:
        pc, _ = count_patterns_in_table(tables["Combined_combined"], patterns)
        for p, cnt in sorted(pc.items(), key=lambda x:x[1], reverse=True):
            html += f"<tr><td>{p}</td><td>{cnt}</td></tr>"
    html += "</table>"

    # 2) Persistence
    html += "<h3>Pattern Persistence Scores</h3><table><tr><th>Pattern</th><th>Score</th></tr>"
    if "Combined_combined" in tables:
        pers = analyze_pattern_persistence(tables["Combined_combined"], patterns)
        for p, val in sorted(pers.items(), key=lambda x:x[1], reverse=True):
            html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    html += "</table>"

    # 3) Stability
    html += "<h3>Pattern Stability Scores</h3><table><tr><th>Pattern</th><th>Score</th></tr>"
    if "Combined_combined" in tables:
        stab = analyze_pattern_stability(tables["Combined_combined"], patterns)
        for p, val in sorted(stab.items(), key=lambda x:x[1], reverse=True):
            html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    html += "</table>"

    # 4) Straight combos
    html += "<h3>Straight Combination Occurrences</h3><table><tr><th>Pattern</th><th>Occurrences</th></tr>"
    if "Combined_combined" in tables:
        scounts = {p: detect_straight_combinations(tables["Combined_combined"], p) for p in patterns}
        for p, val in sorted(scounts.items(), key=lambda x: x[1], reverse=True):
            html += f"<tr><td>{p}</td><td>{val}</td></tr>"
    html += "</table>"

    html += "</div></body></html>"
    return html

def generate_top_reports(state_name, results, top_n=3):
    """
    Generate HTML reports for the top-N indexes of a single state. 
    Returns a list of {rank, index, score, filename, filepath, html}.
    """
    if not results:
        return []
    tables = load_state_data(state_name)
    if not tables:
        return []

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports = []
    # Directory for these analyses
    # We'll put them in data/outputs/analysis for consistency
    analysis_dir = os.path.join(
        os.path.dirname(os.path.dirname(script_dir)), 
        "data",
        "outputs",
        "analysis"
    )
    os.makedirs(analysis_dir, exist_ok=True)

    for i, r in enumerate(results[:top_n], start=1):
        idx = r["index"]
        sc = r["score"]
        pats = r["patterns"]
        rank = r["rank"]
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
    return reports

# ---------------------------------------------------------------------------------
# MAIN TABS
# ---------------------------------------------------------------------------------

def process_data_tab():
    st.header("Process Lottery Data")

    # File uploader for the Excel macro workbook
    uploaded_file = st.file_uploader("Upload Pick3StatsC4.xlsm (required each day)", type=["xlsm"], key="pick3_upload")
    if uploaded_file:
        save_path = os.path.join("data", "original", "Pick3StatsC4.xlsm")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("File uploaded and saved. Please process data below.")

    excel_path, excel_exists = check_excel_file()
    if not excel_exists:
        st.error(f"Excel file not found at {excel_path}")
        st.warning("Please place 'Pick3StatsC4.xlsm' in data/original.")
        return
    else:
        st.success(f"Found Excel file: {os.path.basename(excel_path)}")

    col1, col2, col3 = st.columns(3)
    with col1:
        do_clean = st.checkbox("Clean Data", value=True)
    with col2:
        do_extract = st.checkbox("Extract Data", value=True)
    with col3:
        do_tables = st.checkbox("Generate Tables", value=True)

    selected_states = st.multiselect("Select States (empty = all)",
                                     options=STATES,
                                     default=[],
                                     key="process_data_states")
    states_to_process = selected_states if selected_states else STATES

    if st.button("Process Data", type="primary"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        results_placeholder = st.empty()

        create_output_directories()

        summary = {
            "cleaned_states": [],
            "failed_clean": [],
            "extracted_states": [],
            "tables_generated": []
        }
        with st.spinner("Processing data..."):
            # 1) Clean
            if do_clean:
                status_text.info("Step 1/3: Cleaning data...")
                start_time = time.time()
                try:
                    res = clean_all_states(states_to_process, excel_path, get_cleaned_data_dir())
                    summary["cleaned_states"] = res["success"]
                    summary["failed_clean"] = res["failed"]
                except Exception as e:
                    st.error(f"Error cleaning data: {e}")
                progress_bar.progress(33)
                status_text.success(f"Done cleaning in {format_time(time.time()-start_time)}")
            else:
                progress_bar.progress(33)
                status_text.info("Skipping clean data")

            # 2) Extract
            extracted_data = {}
            if do_extract:
                status_text.info("Step 2/3: Extracting data...")
                start_time = time.time()
                try:
                    extracted_data = extract_all_states(states_to_process, get_cleaned_data_dir())
                    summary["extracted_states"] = list(extracted_data.keys())
                except Exception as e:
                    st.error(f"Error extracting data: {e}")
                progress_bar.progress(66)
                status_text.success(f"Done extracting in {format_time(time.time()-start_time)}")
            else:
                progress_bar.progress(66)
                status_text.info("Skipping extract data")

            # 3) Generate tables
            if do_tables and extracted_data:
                status_text.info("Step 3/3: Generating tables...")
                start_time = time.time()
                for st_name, st_data in extracted_data.items():
                    try:
                        generate_tables(st_data, st_name, os.path.join(get_tables_output_dir(), st_name))
                        summary["tables_generated"].append(st_name)
                    except Exception as e:
                        st.error(f"Error generating tables for {st_name}: {e}")
                progress_bar.progress(100)
                status_text.success(f"Done generating tables in {format_time(time.time()-start_time)}")
            else:
                progress_bar.progress(100)
                status_text.info("Skipping generate tables")

        # Summary
        results_placeholder.markdown("### Processing Summary")
        st.write(f"**States Processed:** {len(states_to_process)}")
        if do_clean:
            st.write(f"**Successfully Cleaned:** {len(summary['cleaned_states'])}")
            if summary["failed_clean"]:
                st.warning("**Failed to Clean:** " + ", ".join(summary["failed_clean"]))
        if do_extract:
            st.write(f"**Successfully Extracted:** {len(summary['extracted_states'])}")
        if do_tables:
            st.write(f"**Tables Generated:** {len(summary['tables_generated'])}")
        st.success("Processing completed!")

def view_results_tab():
    st.header("View Results")

    state_name = st.selectbox("Select State", STATES, key="view_results_state_select")
    tables = load_state_data(state_name)
    if not tables:
        st.warning(f"No data found for {state_name}. Please process data first.")
        return

    tab_midday, tab_evening, tab_combined = st.tabs(["Midday", "Evening", "Combined"])
    with tab_midday:
        st.subheader("Midday - Combined Table")
        ckey = "Midday_combined"
        if ckey in tables:
            st.dataframe(tables[ckey], use_container_width=True, height=400)
            csv = tables[ckey].to_csv(index=False)
            st.download_button(
                label="Download Midday Combined Table",
                data=csv,
                file_name=f"{state_name}_Midday_combined.csv",
                mime="text/csv",
                key="dl_midday_combined"
            )
        else:
            st.info("No Midday combined table available")

        r2key = "Midday_r2"
        st.subheader("Midday - R2 Table")
        if r2key in tables:
            st.dataframe(tables[r2key], use_container_width=True, height=250)
            csv = tables[r2key].to_csv(index=False)
            st.download_button(
                label="Download Midday R2 Table",
                data=csv,
                file_name=f"{state_name}_Midday_r2.csv",
                mime="text/csv",
                key="dl_midday_r2"
            )
        else:
            st.info("No Midday R2 table available")

    with tab_evening:
        st.subheader("Evening - Combined Table")
        ckey = "Evening_combined"
        if ckey in tables:
            st.dataframe(tables[ckey], use_container_width=True, height=400)
            csv = tables[ckey].to_csv(index=False)
            st.download_button(
                label="Download Evening Combined Table",
                data=csv,
                file_name=f"{state_name}_Evening_combined.csv",
                mime="text/csv",
                key="dl_evening_combined"
            )
        else:
            st.info("No Evening combined table available")

        r2key = "Evening_r2"
        st.subheader("Evening - R2 Table")
        if r2key in tables:
            st.dataframe(tables[r2key], use_container_width=True, height=250)
            csv = tables[r2key].to_csv(index=False)
            st.download_button(
                label="Download Evening R2 Table",
                data=csv,
                file_name=f"{state_name}_Evening_r2.csv",
                mime="text/csv",
                key="dl_evening_r2"
            )
        else:
            st.info("No Evening R2 table available")

    with tab_combined:
        st.subheader("Combined - Combined Table")
        ckey = "Combined_combined"
        if ckey in tables:
            st.dataframe(tables[ckey], use_container_width=True, height=400)
            csv = tables[ckey].to_csv(index=False)
            st.download_button(
                label="Download Combined Table",
                data=csv,
                file_name=f"{state_name}_Combined_combined.csv",
                mime="text/csv",
                key="dl_combined_combined"
            )
        else:
            st.info("No 'Combined' table available")

        r2key = "Combined_r2"
        st.subheader("Combined - R2 Table")
        if r2key in tables:
            st.dataframe(tables[r2key], use_container_width=True, height=250)
            csv = tables[r2key].to_csv(index=False)
            st.download_button(
                label="Download Combined R2 Table",
                data=csv,
                file_name=f"{state_name}_Combined_r2.csv",
                mime="text/csv",
                key="dl_combined_r2"
            )
        else:
            st.info("No 'Combined_r2' table available")

def log_winners_tab():
    st.header("Log & Highlight Winners")

    with st.form("winners_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Midday Winners")
            midday_winners_in = st.text_input(
                "Enter Midday winning numbers (space-separated)",
                placeholder="e.g. 123 456 789"
            )
        with col2:
            st.subheader("Evening Winners")
            evening_winners_in = st.text_input(
                "Enter Evening winning numbers (space-separated)",
                placeholder="e.g. 123 456 789"
            )
        chosen_states = st.multiselect(
            "Select States to Process (empty = all)",
            options=STATES,
            default=[]
        )
        submit_btn = st.form_submit_button("Highlight Winners", type="primary")

    if submit_btn:
        if not midday_winners_in and not evening_winners_in:
            st.warning("Please enter at least one winning number")
            return

        midday_winners = [w.strip() for w in midday_winners_in.split() if w.strip()]
        evening_winners = [w.strip() for w in evening_winners_in.split() if w.strip()]

        if midday_winners:
            st.write("Midday Winners:", ", ".join(midday_winners))
        if evening_winners:
            st.write("Evening Winners:", ", ".join(evening_winners))

        states_to_process = chosen_states if chosen_states else STATES
        st.write(f"Processing {len(states_to_process)} states...")

        progress_bar = st.progress(0)
        status = st.empty()

        for i, st_name in enumerate(states_to_process):
            status.info(f"Processing {st_name}...")
            tables = load_state_data(st_name)
            if not tables:
                st.warning(f"No tables found for {st_name}")
                continue

            highlighted = highlight_winners_in_table(
                tables,
                midday_winners=midday_winners,
                evening_winners=evening_winners
            )
            # Save them
            out_dir = os.path.join(get_winners_output_dir(), st_name)
            os.makedirs(out_dir, exist_ok=True)
            for tkey, df in highlighted.items():
                if df is not None and not df.empty:
                    out_file = os.path.join(out_dir, f"{st_name}_{tkey}.csv")
                    df.to_csv(out_file, index=False)

            progress_bar.progress((i + 1) / len(states_to_process))

        status.success("Winner highlighting completed!")

        # Show sample from first state
        if states_to_process:
            st.subheader("Sample Results (First State)")
            first_st = states_to_process[0]
            st_data = load_state_data(first_st)
            if "Midday_combined" in st_data and midday_winners:
                st.write("Midday Combined Table (with winners):")
                dfh = highlight_winners_in_table(
                    {"Midday_combined": st_data["Midday_combined"]},
                    midday_winners=midday_winners,
                    evening_winners=[]
                )
                st.dataframe(dfh["Midday_combined"], use_container_width=True)

            if "Evening_combined" in st_data and evening_winners:
                st.write("Evening Combined Table (with winners):")
                dfh = highlight_winners_in_table(
                    {"Evening_combined": st_data["Evening_combined"]},
                    midday_winners=[],
                    evening_winners=evening_winners
                )
                st.dataframe(dfh["Evening_combined"], use_container_width=True)

# ---------------------------------------------------------------------------------
# REPLACED vtrac_analyzer_tab() WITH CLUSTERING_APP_3 LAYOUT
# ---------------------------------------------------------------------------------

def vtrac_analyzer_tab():
    """
    Matches the logic from clustering_app_3.py so we get the same
    three-column layout for the top rank and detailed HTML report tabs.
    """
    st.header("Enhanced V-TRAC Pattern Analyzer")
    st.markdown("""
    This tool analyzes V-TRAC indexes for your selected dataset(s). 
    Use the dropdown to view results for each state.
    """)
    st.info("Analysis may take longer for large datasets or when running all states.")

    # "All states" or a single state
    state_options = ["All States"] + STATES
    selected_option = st.selectbox("Select Dataset(s) to Analyze", state_options, key="vtrac_state_select")

    top_n_indexes = st.slider("Number of Top Indexes to Display", 1, 35, 10)
    top_n_reports = st.slider("Number of HTML Reports to Generate", 0, 10, 3)

    if st.button("Run V-TRAC Analysis for Selected Dataset(s)", type="primary", key="vtrac_analyzer_run_button"):
        with st.spinner("Running V-TRAC Analysis..."):
            if selected_option == "All States":
                states_to_run = STATES
            else:
                states_to_run = [selected_option]

            progress_bar = st.progress(0)
            status_text = st.empty()
            total_start = time.time()

            for i, state_name in enumerate(states_to_run):
                status_text.info(f"Analyzing {state_name}...")
                t0 = time.time()

                # Check if session state has tables first
                if state_name not in st.session_state.state_tables:
                    print(f"[V-TRAC] Loading tables for {state_name} from disk...")
                    # Load from disk only if not in session state
                    tbls = load_state_data_cached(state_name)
                    if not tbls:
                        st.warning(f"No tables found for {state_name}")
                        progress_bar.progress((i+1)/len(states_to_run))
                        continue
                    st.session_state.state_tables[state_name] = tbls
                else:
                    print(f"[V-TRAC] Using cached tables for {state_name}")
                
                # Now run analysis - analyze_all_indexes will check for cached results
                results = analyze_all_indexes(state_name)
                if not results:
                    st.warning(f"No analyzable data for {state_name}")
                    progress_bar.progress((i+1)/len(states_to_run))
                    continue
                
                # Store results
                st.session_state.vtrac_results[state_name] = results
                st.session_state.last_analysis_time[state_name] = time.time()
                
                # Generate reports only if needed
                if (state_name not in st.session_state.vtrac_reports or 
                    len(st.session_state.vtrac_reports.get(state_name, [])) < top_n_reports):
                    print(f"[V-TRAC] Generating reports for {state_name}...")
                    reports = generate_top_reports(state_name, results, top_n_reports)
                    st.session_state.vtrac_reports[state_name] = reports

                t1 = time.time()
                print(f"[V-TRAC] Finished {state_name} in {t1 - t0:.2f} sec.")
                progress_bar.progress((i+1)/len(states_to_run))

            total_end = time.time()
            status_text.success("Analysis completed!")
            print(f"[V-TRAC] All done in {total_end - total_start:.2f} sec.")

    # Show analysis results if we have them
    has_results = False
    # Which states do we actually have results for?
    if 'vtrac_results' in st.session_state:
        for s in STATES:
            if s in st.session_state.vtrac_results:
                has_results = True
                break

    if has_results:
        st.markdown("## Analysis Results")
        # Let user pick which state's results to see
        available_states = [s for s in STATES if s in st.session_state.vtrac_results]
        if not available_states:
            st.warning("No states have analysis results yet.")
            return

        if len(available_states) > 1:
            if selected_option == "All States" and len(available_states) == 1:
                chosen_state = available_states[0]
            else:
                chosen_state = st.selectbox("Select State to View Results", available_states, key="vtrac_state_dropdown")
        else:
            chosen_state = available_states[0]

        # Grab results + reports
        results = st.session_state.vtrac_results.get(chosen_state, [])
        reports = st.session_state.vtrac_reports.get(chosen_state, [])

        # Last analysis time
        if chosen_state in st.session_state.last_analysis_time:
            last_t = datetime.fromtimestamp(st.session_state.last_analysis_time[chosen_state])
            st.info(f"Analysis last run on {last_t.strftime('%Y-%m-%d at %H:%M:%S')}")

        if results:
            st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {chosen_state}")
            top_df = pd.DataFrame([
                {
                    "Rank": r["rank"],
                    "Index": r["index"],
                    "Score": f"{r['score']:.2f}",
                    "Number of Patterns": len(r["patterns"]),
                    "Top Patterns": (", ".join(sorted(list(r["patterns"]))[:5]) + "...")
                        if len(r["patterns"])>5 else ", ".join(sorted(r["patterns"]))
                }
                for r in results[:top_n_indexes]
            ])
            st.dataframe(top_df, use_container_width=True)

            # Show the #1 rank table set (Midday/Evening/Combined) in columns, just like clustering_app_3
            best_result = results[0]  # rank #1
            st.subheader(f"Top Ranked Index Tables (Rank #{best_result['rank']})")
            st.write("Midday, Evening, and Combined data for the highest-scoring index. (Same layout as clustering_app_3.)")

            # We'll just show all midday/evening/combined from the loaded tables
            st_tbls = load_state_data(chosen_state)
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("**Midday Combined Table**")
                if "Midday_combined" in st_tbls:
                    st.dataframe(st_tbls["Midday_combined"], use_container_width=True, height=400)
                    csv = st_tbls["Midday_combined"].to_csv(index=False)
                    st.download_button(
                        "Download Midday Combined Table",
                        data=csv,
                        file_name=f"{chosen_state}_Midday_combined.csv",
                        mime="text/csv",
                        key="dl_top_midday_combined"
                    )
                else:
                    st.info("No Midday combined table available")

            with col2:
                st.markdown("**Evening Combined Table**")
                if "Evening_combined" in st_tbls:
                    st.dataframe(st_tbls["Evening_combined"], use_container_width=True, height=400)
                    csv = st_tbls["Evening_combined"].to_csv(index=False)
                    st.download_button(
                        "Download Evening Combined Table",
                        data=csv,
                        file_name=f"{chosen_state}_Evening_combined.csv",
                        mime="text/csv",
                        key="dl_top_evening_combined"
                    )
                else:
                    st.info("No Evening combined table available")

            with col3:
                st.markdown("**Combined Table**")
                if "Combined_combined" in st_tbls:
                    st.dataframe(st_tbls["Combined_combined"], use_container_width=True, height=400)
                    csv = st_tbls["Combined_combined"].to_csv(index=False)
                    st.download_button(
                        "Download Combined Table",
                        data=csv,
                        file_name=f"{chosen_state}_Combined_combined.csv",
                        mime="text/csv",
                        key="dl_top_combined_combined"
                    )
                else:
                    st.info("No Combined table available")

            # Detailed HTML reports
            if reports and top_n_reports > 0:
                st.subheader("Detailed Analysis Reports")
                report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:top_n_reports]])
                for tab, rep in zip(report_tabs, reports[:top_n_reports]):
                    with tab:
                        c1, c2 = st.columns(2)
                        with c1:
                            st.write(f"V-TRAC Index: {rep['index']} | Score: {rep['score']:.2f}")
                        with c2:
                            st.download_button(
                                label=f"Download HTML (Rank #{rep['rank']})",
                                data=rep["html"],
                                file_name=rep["filename"],
                                mime="text/html",
                                key=f"dl_html_rank{rep['rank']}"
                            )
                            if st.button(f"Open in Browser (Rank #{rep['rank']})",
                                         key=f"open_browser_{chosen_state}_{rep['rank']}"):
                                webbrowser.open(f"file://{os.path.abspath(rep['filepath'])}")

                        expand_view = st.checkbox("Expand View", key=f"expand_{chosen_state}_{rep['rank']}")
                        if expand_view:
                            st.components.v1.html(rep["html"], height=4000, scrolling=True)
                        else:
                            st.components.v1.html(rep["html"], height=3000, scrolling=True)
            elif top_n_reports > 0:
                st.info("No HTML reports were generated for this analysis yet.")
        else:
            st.warning("No results to display. Please run the analysis first.")
    else:
        st.info("No analysis results found. Please run an analysis above.")

# ---------------------------------------------------------------------------------
# MAIN APP
# ---------------------------------------------------------------------------------

def main():
    st.sidebar.title("Alpha Analytical Tool")
    st.sidebar.image("https://img.icons8.com/fluency/96/lottery.png", width=80)
    st.sidebar.markdown("---")

    st.title("Enhanced V-TRAC Analyzer FINAL")

    # Main tabs
    tabs = st.tabs([
        "📊 Process Data",
        "👁 View Results",
        "🏆 Log Winners",
        "📈 V-TRAC Analyzer"
    ])

    with tabs[0]:
        process_data_tab()
    with tabs[1]:
        view_results_tab()
    with tabs[2]:
        log_winners_tab()
    with tabs[3]:
        vtrac_analyzer_tab()

    st.sidebar.markdown("---")
    st.sidebar.text(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 