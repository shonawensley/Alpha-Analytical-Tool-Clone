#!/usr/bin/env python
"""
vtrac_analyzer_standalone.py

Standalone Streamlit interface for V-TRAC analysis ONLY.
This version loads pre-generated tables and does not include data processing tabs.

Key differences from older versions:
1) Only loads 3 core tables (Midday_combined, Evening_combined, Combined_combined).
2) We removed references to R2-only tables in the UI (optional).
3) Restores the import block that had been accidentally removed.
"""

import os
import sys
import time
import json
import base64
import webbrowser
import traceback
from datetime import datetime
from collections import Counter
from functools import lru_cache

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Adjust path (script_dir -> project_root)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
sys.path.append(project_root)

# ------------------------------------------------------------------
# Project-level helpers and constants
# ------------------------------------------------------------------
try:
    from scripts.utils.path_handler import (
        get_tables_output_dir,
        # If you want to save winners highlight, you can keep:
        get_winners_output_dir
    )
    from scripts.utils.state_utils import STATES
    from scripts.utils.vtrac_utils import (
        BOXED_VTRAC_REFERENCE,
        highlight_winners_in_table,  # Optional if needed
    )
except ImportError as e:
    print(f"[IMPORT-ERROR] {e}")
    sys.exit(1)

#####################################################################
# Basic LRU-based CSV loader
#####################################################################
@lru_cache(maxsize=32)
def load_csv_cached(path: str) -> pd.DataFrame:
    """Load a CSV file as strings, fill NaNs with 'N/A' (cached)."""
    df = pd.read_csv(path, dtype=str).fillna("N/A")
    return df

# Debug line to see the LRU behavior
print("[DEBUG] load_csv_cached:", load_csv_cached.cache_info())


#####################################################################
# Streamlit Page Config
#####################################################################
st.set_page_config(
    page_title="Standalone V-TRAC Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

#####################################################################
# Session States
#####################################################################
if 'state_tables' not in st.session_state:
    st.session_state.state_tables = {}
if 'vtrac_results' not in st.session_state:
    st.session_state.vtrac_results = {}
if 'vtrac_reports' not in st.session_state:
    st.session_state.vtrac_reports = {}
if 'last_analysis_time' not in st.session_state:
    st.session_state.last_analysis_time = {}


#####################################################################
# Formatting Helper
#####################################################################
def format_time(seconds: float) -> str:
    """Convert 'seconds' to a short human-readable string."""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = int(seconds // 60)
    sec = seconds % 60
    return f"{minutes} min {sec:.2f} sec"


#####################################################################
# Load State Data (3 combined tables)
#####################################################################
@lru_cache(maxsize=32)
def load_state_data_cached(state_name: str) -> dict:
    """
    Loads only the 3 "combined" tables from data/outputs/tables/[STATE_NAME]/.
    Returns a dict: { 'Midday_combined': df, 'Evening_combined': df, 'Combined_combined': df }
    """
    tables_root = get_tables_output_dir()
    if not os.path.exists(tables_root):
        print(f"[ERROR] Tables root dir not found: {tables_root}")
        st.error("Please generate tables first.")
        return {}

    state_dir = os.path.join(tables_root, state_name)
    if not os.path.exists(state_dir) or not os.listdir(state_dir):
        print(f"[ERROR] No CSV found for {state_name} in {state_dir}")
        st.error(f"No CSV found for {state_name}. Check table generation.")
        return {}

    # We only want these
    required_filenames = [
        f"{state_name}_Midday_combined.csv",
        f"{state_name}_Evening_combined.csv",
        f"{state_name}_Combined_combined.csv",
    ]

    found_count = 0
    result = {}
    for filename in os.listdir(state_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(state_dir, filename)
            # Derive the table key from the filename
            key_parts = os.path.splitext(filename)[0].split(f"{state_name}_")
            table_key = key_parts[1] if len(key_parts) > 1 else None
            if table_key and filename in required_filenames:
                try:
                    df = load_csv_cached(filepath)
                    result[table_key] = df
                    found_count += 1
                except Exception as e:
                    print(f"[ERROR] Loading {filename}: {e}")

    if found_count < 1:
        st.error("No combined tables found (midday/evening/combined).")
    return result


def load_state_data(state_name: str) -> dict:
    """
    Loads the 3 combined tables for a state using session state + the above cached function.
    """
    if state_name in st.session_state.state_tables:
        return st.session_state.state_tables[state_name]

    data = load_state_data_cached(state_name)
    if data:
        st.session_state.state_tables[state_name] = data
    return data


#####################################################################
# Analysis Logic (imported from older script)
#####################################################################

def get_all_combinations_for_index(index: str) -> set:
    """Get all pattern combos for the given V-TRAC index."""
    entry = next((x for x in BOXED_VTRAC_REFERENCE if x["Index"] == index), None)
    if not entry:
        return set()
    combos = set(entry.get("Singles", [])) | set(entry.get("Doubles", []))
    return combos


def count_patterns_in_table(df: pd.DataFrame, patterns: set) -> (dict, int):
    """Count total occurrences in columns 7..1."""
    pattern_counts = {p: 0 for p in patterns}
    total_matches = 0
    if df is None or df.empty:
        return pattern_counts, total_matches

    columns = [c for c in ["7","6","5","4","3","2","1"] if c in df.columns]
    for col in columns:
        ser = df[col].astype(str)
        for cell in ser:
            for p in patterns:
                c = cell.count(p)
                if c > 0:
                    pattern_counts[p] += c
                    total_matches += c
    return pattern_counts, total_matches


def analyze_pattern_persistence(df: pd.DataFrame, patterns: set) -> dict:
    """Check how long patterns persist in consecutive columns (7->1)."""
    scores = {p: 0 for p in patterns}
    if df is None or df.empty:
        return scores
    columns = [c for c in ["7","6","5","4","3","2","1"] if c in df.columns]

    for p in patterns:
        p_str = str(p)
        for _, row in df.iterrows():
            consecutive = 0
            max_c = 0
            for col in columns:
                val = str(row[col])
                if p_str in val:
                    consecutive += 1
                else:
                    max_c = max(max_c, consecutive)
                    consecutive = 0
            max_c = max(max_c, consecutive)
            scores[p] += (max_c**2)
    return scores


def analyze_pattern_stability(df: pd.DataFrame, patterns: set) -> dict:
    """Check if patterns appear across multiple row types (R2,R4,R6,R8)."""
    scores = {p: 0 for p in patterns}
    if df is None or df.empty or "RowType" not in df.columns:
        return scores

    grouped = df.groupby(["Set","Draw"])
    for _, g in grouped:
        rowtypes = g["RowType"].unique()
        if len(rowtypes) < 2:
            continue
        for p in patterns:
            found_types = 0
            for rt in ["R2","R4","R6","R8"]:
                sub = g[g["RowType"]==rt]
                if sub.empty:
                    continue
                # if any col 7..1 has p:
                if any(str(v).find(p) >= 0 for col in ["7","6","5","4","3","2","1"] if col in sub.columns for v in sub[col]):
                    found_types += 1
            scores[p] += (found_types**2)
    return scores


def detect_straight_combinations(df: pd.DataFrame, pattern: str) -> int:
    """Count multiple occurrences within the same row as extra straight combos."""
    if df is None or df.empty:
        return 0
    columns = [c for c in ["7","6","5","4","3","2","1"] if c in df.columns]
    total_straight = 0
    for _, row in df.iterrows():
        occurrences = 0
        for col in columns:
            val = str(row[col])
            occurrences += val.count(pattern)
        total_straight += occurrences
    return total_straight


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


def analyze_all_indexes(state_name: str) -> list:
    """Loop all VTRAC indices, compute score, produce final sorted list of results."""
    st.info(f"Loading tables for {state_name}...")
    tables = load_state_data(state_name)
    if not tables:
        st.error("No tables loaded. Aborting.")
        return []

    idx_list = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
    results = []
    progress_bar = st.progress(0)
    status_txt = st.empty()

    total_idx = len(idx_list)
    for i, idx in enumerate(idx_list):
        status_txt.info(f"Index {idx} ({i+1}/{total_idx})...")
        combos = get_all_combinations_for_index(idx)
        if not combos:
            continue
        sc = calculate_index_score(tables, combos)
        results.append({
            "index": idx,
            "score": sc,
            "patterns": combos
        })
        progress_bar.progress((i+1)/total_idx)

    status_txt.success("Done analyzing all indexes.")
    progress_bar.empty()

    # sort
    results.sort(key=lambda x: x["score"], reverse=True)
    # rank
    for i, r in enumerate(results):
        r["rank"] = i+1
    return results


#####################################################################
# The HTML Report
#####################################################################
def generate_index_html_report(state_name: str, index: str, patterns: set, tables: dict, score: float, rank: int, timestamp=None) -> str:
    """
    A simple static HTML generator to show the combined tables + highlight patterns.
    """
    from datetime import datetime
    if not timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def highlight_table(df: pd.DataFrame, title: str) -> str:
        """Produce an HTML table with pattern highlights."""
        if df is None or df.empty:
            return f'<div><h3>{title}</h3><p style="color:gray;">No data</p></div>'

        # Ensure columns exist
        needed_cols = ["Set","Draw","RowType","7","6","5","4","3","2","1"]
        for c in needed_cols:
            if c not in df.columns:
                df[c] = "N/A"
        df = df[needed_cols]

        out = [f"<div><h3>{title}</h3><table>"]
        # header
        out.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in df.columns) + "</tr></thead>")
        # body
        out.append("<tbody>")
        for _, row in df.iterrows():
            out.append("<tr>")
            for c in df.columns:
                val = str(row[c])
                for pat in patterns:
                    pat_str = str(pat)
                    if pat_str in val:
                        placeholder = f"__H__{pat_str}__E__"
                        val = val.replace(pat_str, placeholder)
                val = val.replace("__H__", "<span style='color:#800080;font-weight:bold;background:#f6edf8;'>")
                val = val.replace("__E__", "</span>")
                out.append(f"<td>{val}</td>")
            out.append("</tr>")
        out.append("</tbody></table></div>")
        return "".join(out)

    html = f"""
<html>
<head>
<meta charset="UTF-8"/>
<title>VTRAC Index {index} - {state_name}</title>
<style>
body {{
  font-family: Arial, sans-serif; margin: 0; padding: 15px; background:#fdfdfd; color:#333;
}}
h1,h2,h3 {{
  color:#800080;
}}
span.highlight {{
  background-color:#f6edf8; color:#800080; font-weight:bold;
}}
table {{
  border-collapse:collapse; margin:15px 0; min-width:600px; width:100%;
}}
th,td {{
  border:1px solid #ccc; padding:5px 8px; text-align:center;
}}
</style>
</head>
<body>
<h1>VTRAC Index {index} (Rank #{rank})</h1>
<p>Analysis for state <strong>{state_name}</strong> at {timestamp}. Score: {score:.2f}<br/>
Patterns Found: {len(patterns)}</p>
<div style="display:flex; gap:20px;">
<div style="flex:1;">"""

    # Midday
    midday_df = tables.get("Midday_combined")
    html += highlight_table(midday_df, "Midday Combined")

    html += "</div><div style='flex:1;'>"
    # Evening
    evening_df = tables.get("Evening_combined")
    html += highlight_table(evening_df, "Evening Combined")

    html += "</div><div style='flex:1;'>"
    # Combined
    combo_df = tables.get("Combined_combined")
    html += highlight_table(combo_df, "Overall Combined")

    html += "</div></div></body></html>"
    return html


#####################################################################
# Main Streamlit UI
#####################################################################
def main():
    st.sidebar.title("Standalone V-TRAC Analyzer")
    st.sidebar.image("https://img.icons8.com/fluency/96/target-spotlight.png", width=80)
    st.sidebar.markdown("---")
    st.sidebar.info("This tool loads the 3 combined tables for a state and performs VTRAC analysis.")
    st.sidebar.markdown("Run `generate_tables_pipeline.bat` first if tables are missing.")

    st.title("Standalone V-TRAC Analyzer")
    st.write("This version focuses on the 3 combined tables only (Midday, Evening, and Combined).")

    selected_state = st.sidebar.selectbox("Choose State", STATES)
    top_n = st.sidebar.slider("Number of top indexes to show", 1, 35, 10)

    if st.sidebar.button("Run Analysis"):
        # Clear old results
        if selected_state in st.session_state.vtrac_results:
            del st.session_state.vtrac_results[selected_state]
        if selected_state in st.session_state.vtrac_reports:
            del st.session_state.vtrac_reports[selected_state]
        if selected_state in st.session_state.last_analysis_time:
             del st.session_state.last_analysis_time[selected_state]

        with st.spinner(f"Analyzing {selected_state}..."):
            start_t = time.time()
            results = analyze_all_indexes(selected_state)
            if not results:
                st.warning("No results. Possibly no data or no patterns found.")
                return
            st.session_state.vtrac_results[selected_state] = results
            st.session_state.last_analysis_time[selected_state] = time.time()
            end_t = time.time()
            st.success(f"Done. Time: {format_time(end_t - start_t)}")

    st.markdown("---")

    if selected_state in st.session_state.vtrac_results:
        st.subheader(f"Results for {selected_state}")

        results = st.session_state.vtrac_results[selected_state]
        if not results:
            st.info("No data in results.")
            return

        # Show top indexes
        top_results = results[:top_n]
        df_show = pd.DataFrame([
            {
                "Rank": r["rank"],
                "Index": r["index"],
                "Score": f"{r['score']:.2f}",
                "Num Patterns": len(r["patterns"]),
            }
            for r in top_results
        ])
        st.dataframe(df_show, use_container_width=True)

        # Show best index details
        best = top_results[0]
        st.markdown(f"### Best Index: {best['index']} (Score: {best['score']:.2f})")
        st.write(f"Patterns found: {len(best['patterns'])}")

        # Load tables again to pass to HTML generator
        tables = load_state_data(selected_state)
        html_rep = generate_index_html_report(selected_state, best["index"], best["patterns"], tables, best["score"], best["rank"])
        st.markdown("#### Inline HTML Report")
        st.components.v1.html(html_rep, height=700, scrolling=True)

        # Download
        st.download_button(
            label="Download HTML",
            data=html_rep.encode("utf-8"),
            file_name=f"{selected_state}_rank1_index_{best['index']}.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()
