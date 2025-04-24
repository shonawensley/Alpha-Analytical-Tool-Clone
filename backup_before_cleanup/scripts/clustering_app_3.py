#!/usr/bin/env python
"""
clustering_app_3.py - Enhanced Streamlit interface with V-TRAC analyzer
Based on the working Enhanced Analyzer (streamlit_app_with_analyzer.py)
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
import subprocess
import re
import seaborn as sns
from PIL import Image
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
from utils.state_utils import STATES, get_state_display_name, get_state_file_name
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables
from utils.vtrac_utils import (
    BOXED_VTRAC_REFERENCE,
    find_vtrac_index_and_combos,
    highlight_winners_in_table
)

# Set page config
st.set_page_config(
    page_title="Clustering App 3",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for storing analysis results
if 'state_tables' not in st.session_state:
    st.session_state.state_tables = {}
if 'vtrac_results' not in st.session_state:
    st.session_state.vtrac_results = {}
if 'vtrac_reports' not in st.session_state:
    st.session_state.vtrac_reports = {}
if 'last_analysis_time' not in st.session_state:
    st.session_state.last_analysis_time = {}

# Custom CSS
st.markdown("""
<style>
    .main .block-container {padding-top: 2rem;}
    .stTabs [data-baseweb="tab-list"] {gap: 8px;}
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e6f3ff;
        font-weight: bold;
    }
    .stButton button {
        width: 100%;
        border-radius: 4px;
        height: 2.5rem;
    }
    .highlight {
        background-color: yellow;
        padding: 1px 4px;
        border-radius: 3px;
        font-weight: bold;
    }
    .stAlert {margin-top: 1rem; margin-bottom: 1rem;}
    .stProgress > div > div {height: 10px;}
    .stDownloadButton button {width: auto;}
</style>
""", unsafe_allow_html=True)

#------------------------------------------------------------------------------
# MAIN APP FUNCTIONS
#------------------------------------------------------------------------------

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
    """Cached version of load_state_data to avoid repeated disk reads"""
    # Find the parent directory containing all date folders
    tables_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "outputs", "tables")
    if not os.path.exists(tables_root):
        print(f"[ERROR] Tables root directory not found: {tables_root}")
        return {}

    # Find all date folders, sorted newest first
    date_folders = sorted(
        [d for d in os.listdir(tables_root) if os.path.isdir(os.path.join(tables_root, d))],
        reverse=True
    )

    for date_folder in date_folders:
        state_tables_dir = os.path.join(tables_root, date_folder, state_name)
        if os.path.exists(state_tables_dir) and os.listdir(state_tables_dir):
            # Found a non-empty folder for this state
            result = {}
            for filename in os.listdir(state_tables_dir):
                if filename.endswith(".csv"):
                    filepath = os.path.join(state_tables_dir, filename)
                    key = os.path.splitext(filename)[0].replace(f"{state_name}_", "")
                    try:
                        df = pd.read_csv(filepath)
                        result[key] = df
                        print(f"[INFO] Loaded table: {key} from {filename}")
                    except Exception as e:
                        print(f"[ERROR] Error loading {filename}: {e}")
            if result:
                print(f"[INFO] Loaded tables for {state_name} from {state_tables_dir}")
                return result  # Return immediately after finding and loading tables
            
    print(f"[ERROR] No tables found for {state_name} in any date folder under {tables_root}")
    return {} 

def load_state_data(state_name):
    """Load generated tables for a specific state with session state caching"""
    # Check if we already have this state's data in session state
    if state_name in st.session_state.state_tables:
        print(f"[INFO] Using cached tables for {state_name}")
        return st.session_state.state_tables[state_name]
    
    # Otherwise load from disk and cache
    tables = load_state_data_cached(state_name)
    if tables:
        st.session_state.state_tables[state_name] = tables
    
    return tables

#------------------------------------------------------------------------------
# V-TRAC ANALYZER FUNCTIONS
#------------------------------------------------------------------------------

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
        # Check each row
        for _, row in df.iterrows():
            # Count consecutive columns containing the pattern
            consecutive_count = 0
            max_consecutive = 0
            
            for col in valid_columns:
                if pattern in str(row[col]):
                    consecutive_count += 1
                else:
                    # Update max_consecutive if current streak is better
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
    
    # For each group, check pattern presence across row types
    for _, group in grouped:
        # Skip groups without all row types
        row_types = group['RowType'].unique()
        if len(row_types) < 2:  # Need at least 2 row types to measure stability
            continue
            
        # Check each pattern
        for pattern in patterns:
            # Count row types containing the pattern
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
    
    # Define columns to check
    columns = ['7', '6', '5', '4', '3', '2', '1']
    valid_columns = [col for col in columns if col in df.columns]
    
    # Check each row
    for _, row in df.iterrows():
        # Count occurrences in this row
        occurrences = 0
        for col in valid_columns:
            if pattern in str(row[col]):
                occurrences += 1
        
        # If pattern appears multiple times in the same row, count as straight
        if occurrences > 1:
            straight_count += occurrences
    
    return straight_count

def calculate_index_score(tables, patterns):
    """Calculate an overall score for a V-TRAC index based on multiple metrics"""
    
    overall_score = 0
    combined_table = tables.get("Combined_combined", pd.DataFrame())
    midday_table = tables.get("Midday_combined", pd.DataFrame())
    evening_table = tables.get("Evening_combined", pd.DataFrame())
    
    # Skip if no data
    if combined_table.empty and midday_table.empty and evening_table.empty:
        return 0
    
    # 1. Total pattern occurrence score (weighted by importance of table)
    tables_to_score = {
        "Combined_combined": 3.0,  # Highest weight
        "Midday_combined": 1.5,
        "Evening_combined": 1.5,
        "Combined_r2": 2.0,
        "Midday_r2": 1.0,
        "Evening_r2": 1.0
    }
    
    occurrence_score = 0
    for table_name, weight in tables_to_score.items():
        if table_name in tables:
            _, match_count = count_patterns_in_table(tables[table_name], patterns)
            occurrence_score += match_count * weight
    
    # 2. Pattern persistence score
    persistence_score = 0
    for table_name, weight in tables_to_score.items():
        if table_name in tables:
            persistence_results = analyze_pattern_persistence(tables[table_name], patterns)
            persistence_score += sum(persistence_results.values()) * weight
    
    # 3. Pattern stability score
    stability_score = 0
    for table_name, weight in tables_to_score.items():
        if table_name in tables and "_combined" in table_name:  # Only combined tables have row types
            stability_results = analyze_pattern_stability(tables[table_name], patterns)
            stability_score += sum(stability_results.values()) * weight
    
    # 4. Straight combinations score
    straight_score = 0
    for table_name, weight in tables_to_score.items():
        if table_name in tables:
            for pattern in patterns:
                straight_score += detect_straight_combinations(tables[table_name], pattern) * weight
    
    # Combine all scores with appropriate weighting
    overall_score = (
        occurrence_score * 0.35 +  # 35% weight
        persistence_score * 0.30 +  # 30% weight
        stability_score * 0.25 +    # 25% weight
        straight_score * 0.10       # 10% weight
    )
    
    return overall_score 

def generate_index_html_report(state_name, index, patterns, tables, score, rank, timestamp=None):
    """Generate an HTML report for a specific V-TRAC index"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create HTML header
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
            min-width: 30%;  /* Ensure columns have a minimum width */
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
"""

    # First show the tables (three-column layout)
    html += '<div class="three-column-layout">'
    
    # Function to generate table HTML
    def generate_table_html(df, title):
        if df is None or df.empty:
            return f"<h2>{title}</h2><p>No data available</p>"
            
        table_html = f"<h2>{title}</h2><table>"
        
        # Table header
        header_cols = ['Set', 'Draw', 'RowType', '7', '6', '5', '4', '3', '2', '1']
        table_html += "<tr>" + "".join([f"<th>{col}</th>" for col in header_cols if col in df.columns]) + "</tr>"
        
        # Table rows
        for _, row in df.iterrows():
            table_html += "<tr>"
            for col in header_cols:
                if col in df.columns:
                    value = str(row[col])
                    # Apply highlighting
                    for pattern in patterns:
                        if pattern in value:
                            value = value.replace(pattern, f'<span class="highlight">{pattern}</span>')
                    table_html += f"<td>{value}</td>"
            table_html += "</tr>"
        
        table_html += "</table>"
        return table_html
    
    # Midday column
    html += '<div class="column"><h2>Midday Data</h2>'
    if "Midday_combined" in tables:
        html += generate_table_html(tables["Midday_combined"], f"{state_name} Midday Combined Table")
    if "Midday_r2" in tables:
        html += generate_table_html(tables["Midday_r2"], f"{state_name} Midday R2-only Table")
    html += '</div>'
    
    # Evening column
    html += '<div class="column"><h2>Evening Data</h2>'
    if "Evening_combined" in tables:
        html += generate_table_html(tables["Evening_combined"], f"{state_name} Evening Combined Table")
    if "Evening_r2" in tables:
        html += generate_table_html(tables["Evening_r2"], f"{state_name} Evening R2-only Table")
    html += '</div>'
    
    # Combined column
    html += '<div class="column"><h2>Combined Data</h2>'
    if "Combined_combined" in tables:
        html += generate_table_html(tables["Combined_combined"], f"{state_name} Combined Combined Table")
    if "Combined_r2" in tables:
        html += generate_table_html(tables["Combined_r2"], f"{state_name} Combined R2-only Table")
    html += '</div>'
    
    # Close tables layout
    html += '</div>'
    
    # Then add the stats section
    html += '<div class="stats">'
    html += "<h2>Analysis Statistics</h2>"
    html += f"<p><strong>Index Score:</strong> {score:.2f}</p>"
    html += f"<p><strong>Total Patterns:</strong> {len(patterns)}</p>"
    html += f"<p><strong>Pattern List:</strong> {', '.join(sorted(patterns))}</p>"

    # 1. Pattern occurrence counts
    html += "<h3>Pattern Occurrence Counts</h3>"
    html += "<table><tr><th>Pattern</th><th>Occurrences</th></tr>"
    
    # Get pattern counts from combined table
    if "Combined_combined" in tables:
        pattern_counts, _ = count_patterns_in_table(tables["Combined_combined"], patterns)
        for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
            html += f"<tr><td>{pattern}</td><td>{count}</td></tr>"
    
    html += "</table>"
    
    # 2. Pattern persistence scores
    html += "<h3>Pattern Persistence Scores</h3>"
    html += "<table><tr><th>Pattern</th><th>Persistence Score</th></tr>"
    
    # Get persistence scores from combined table
    if "Combined_combined" in tables:
        persistence_scores = analyze_pattern_persistence(tables["Combined_combined"], patterns)
        for pattern, score in sorted(persistence_scores.items(), key=lambda x: x[1], reverse=True):
            html += f"<tr><td>{pattern}</td><td>{score}</td></tr>"
    
    html += "</table>"
    
    # 3. Pattern stability scores
    html += "<h3>Pattern Stability Scores</h3>"
    html += "<table><tr><th>Pattern</th><th>Stability Score</th></tr>"
    
    # Get stability scores from combined table
    if "Combined_combined" in tables:
        stability_scores = analyze_pattern_stability(tables["Combined_combined"], patterns)
        for pattern, score in sorted(stability_scores.items(), key=lambda x: x[1], reverse=True):
            html += f"<tr><td>{pattern}</td><td>{score}</td></tr>"
    
    html += "</table>"
    
    # 4. Straight combinations
    html += "<h3>Straight Combination Occurrences</h3>"
    html += "<table><tr><th>Pattern</th><th>Straight Occurrences</th></tr>"
    
    # Get straight counts from combined table
    if "Combined_combined" in tables:
        straight_counts = {pattern: detect_straight_combinations(tables["Combined_combined"], pattern) for pattern in patterns}
        for pattern, count in sorted(straight_counts.items(), key=lambda x: x[1], reverse=True):
            html += f"<tr><td>{pattern}</td><td>{count}</td></tr>"
    
    html += "</table>"
    
    # Close stats div and HTML
    html += '</div></body></html>'
    
    return html

def analyze_all_indexes(state_name):
    """Analyze all V-TRAC indexes for a state and rank them"""
    # Load tables for the state
    tables = load_state_data(state_name)
    if not tables:
        return None
    
    # Analyze each V-TRAC index
    results = []
    
    # Get all valid V-TRAC indexes
    vtrac_indices = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
    
    for index in vtrac_indices:
        # Get all patterns for this index
        patterns = get_all_combinations_for_index(index)
        
        # Skip indexes with no patterns
        if not patterns:
            continue
        
        # Calculate score for this index
        score = calculate_index_score(tables, patterns)
        
        # Store result
        results.append({
            "index": index,
            "patterns": patterns,
            "score": score
        })
    
    # Sort results by score (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)
    
    # Add ranks
    for i, result in enumerate(results):
        result["rank"] = i + 1
    
    return results

def generate_top_reports(state_name, results, top_n=3):
    """Generate HTML reports for top N ranked indexes"""
    if not results or len(results) == 0:
        return []
    
    # Load tables for the state
    tables = load_state_data(state_name)
    if not tables:
        return []
    
    # Generate reports for top N results
    reports = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for i, result in enumerate(results[:top_n]):
        # Generate HTML
        html = generate_index_html_report(
            state_name, 
            result["index"], 
            result["patterns"], 
            tables, 
            result["score"], 
            result["rank"],
            timestamp
        )
        
        # Generate filename
        filename = f"{state_name}_vtrac_rank{i+1}_index{result['index']}_v{timestamp}.html"
        
        # Define save path
        output_dir = os.path.join(os.path.dirname(script_dir), "outputs", "analysis")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        
        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        
        # Add to reports
        reports.append({
            "rank": i + 1,
            "index": result["index"],
            "score": result["score"],
            "filename": filename,
            "filepath": filepath,
            "html": html
        })
    
    return reports 

#------------------------------------------------------------------------------
# TAB CONTENT FUNCTIONS
#------------------------------------------------------------------------------

def process_data_tab():
    """Process Data Tab Content"""
    st.header("Process Lottery Data")
    
    # File uploader for Pick3StatsC4.xlsm
    uploaded_file = st.file_uploader("Upload Pick3StatsC4.xlsm (required each day)", type=["xlsm"], key="pick3_upload")
    if uploaded_file:
        save_path = os.path.join("data", "original", "Pick3StatsC4.xlsm")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("File uploaded and saved. Please process data below.")
    
    # Check if Excel file exists
    excel_path, excel_exists = check_excel_file()
    
    if not excel_exists:
        st.error(f"Excel file not found at {excel_path}")
        st.warning("Please place the 'Pick3StatsC4.xlsm' file in the data/original directory.")
        return
    
    st.success(f"Found Excel file: {os.path.basename(excel_path)}")
    
    # Create columns for processing options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        clean_data = st.checkbox("Clean Data", value=True)
    with col2:
        extract_data = st.checkbox("Extract Data", value=True)
    with col3:
        generate_tables_option = st.checkbox("Generate Tables", value=True)
    
    # Add multi-select for states
    selected_states = st.multiselect(
        "Select States to Process (leave empty for all states)",
        options=STATES,
        default=[],
        key="process_data_states"
    )
    
    # Use all states if none selected
    states_to_process = selected_states if selected_states else STATES
    
    # Process button
    if st.button("Process Data", type="primary"):
        # Create progress bar and status
        progress_bar = st.progress(0)
        status = st.empty()
        results = st.empty()
        
        # Create output directories
        create_output_directories()
        
        # Initialize processing summary
        summary = {
            "cleaned_states": [],
            "failed_clean": [],
            "extracted_states": [],
            "tables_generated": []
        }
        
        with st.spinner("Processing data..."):
            # Step 1: Clean data
            if clean_data:
                status.info("Step 1/3: Cleaning data...")
                start_time = time.time()
                
                cleaning_results = clean_all_states(
                    states_to_process, 
                    excel_path, 
                    get_cleaned_data_dir()
                )
                
                summary["cleaned_states"] = cleaning_results["success"]
                summary["failed_clean"] = cleaning_results["failed"]
                
                progress_bar.progress(33)
                duration = time.time() - start_time
                status.success(f"Data cleaning completed in {format_time(duration)}")
            else:
                progress_bar.progress(33)
                status.info("Skipping data cleaning step")
            
            # Step 2: Extract data
            extracted_data = {}
            if extract_data:
                status.info("Step 2/3: Extracting data...")
                start_time = time.time()
                
                extracted_data = extract_all_states(
                    states_to_process,
                    get_cleaned_data_dir()
                )
                
                summary["extracted_states"] = list(extracted_data.keys())
                
                progress_bar.progress(66)
                duration = time.time() - start_time
                status.success(f"Data extraction completed in {format_time(duration)}")
            else:
                progress_bar.progress(66)
                status.info("Skipping data extraction step")
            
            # Step 3: Generate tables
            if generate_tables_option and extracted_data:
                status.info("Step 3/3: Generating tables...")
                start_time = time.time()
                
                for state_name, state_data in extracted_data.items():
                    generate_tables(
                        state_data,
                        state_name,
                        os.path.join(get_tables_output_dir(), state_name)
                    )
                    summary["tables_generated"].append(state_name)
                
                progress_bar.progress(100)
                duration = time.time() - start_time
                status.success(f"Table generation completed in {format_time(duration)}")
            else:
                progress_bar.progress(100)
                status.info("Skipping table generation step")
        
        # Show processing summary
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
    """View Results Tab Content"""
    st.header("View Results")
    
    # Select state
    state = st.selectbox("Select State", STATES, key="view_results_state_select")
    
    # Load data for selected state
    state_data = load_state_data(state)
    
    if not state_data:
        st.warning(f"No data found for {state}. Please process data first.")
        return
    
    # Create tabs for different sections
    tables_tabs = st.tabs(["Midday", "Evening", "Combined"])
    
    for i, section in enumerate(["Midday", "Evening", "Combined"]):
        with tables_tabs[i]:
            # Combined table
            combined_key = f"{section}_combined"
            r2_key = f"{section}_r2"
            
            st.subheader(f"{section} - Combined Table")
            if combined_key in state_data:
                st.dataframe(
                    state_data[combined_key], 
                    use_container_width=True,
                    height=400
                )
                
                # Download option
                csv = state_data[combined_key].to_csv(index=False)
                st.download_button(
                    f"Download {section} Combined Table",
                    data=csv,
                    file_name=f"{state}_{section}_combined.csv",
                    mime="text/csv",
                )
            else:
                st.info(f"No {section} combined table available")
            
            # R2 table
            st.subheader(f"{section} - R2 Table")
            if r2_key in state_data:
                st.dataframe(
                    state_data[r2_key],
                    use_container_width=True,
                    height=250
                )
                
                # Download option
                csv = state_data[r2_key].to_csv(index=False)
                st.download_button(
                    f"Download {section} R2 Table",
                    data=csv,
                    file_name=f"{state}_{section}_r2.csv",
                    mime="text/csv",
                )
            else:
                st.info(f"No {section} R2 table available")

def log_winners_tab():
    """Log Winners Tab Content"""
    st.header("Log & Highlight Winners")
    
    # Form for winner inputs
    with st.form("winners_form"):
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
        
        # Select states to process
        selected_states = st.multiselect(
            "Select States to Process (leave empty for all)",
            options=STATES,
            default=[],
            key="log_winners_states"
        )
        
        submit_button = st.form_submit_button("Highlight Winners", type="primary")
    
    # Process winners when submitted
    if submit_button:
        if not midday_winners and not evening_winners:
            st.warning("Please enter at least one winning number")
            return
        
        # Parse winners
        midday_list = [w.strip() for w in midday_winners.split() if w.strip()]
        evening_list = [w.strip() for w in evening_winners.split() if w.strip()]
        
        # Preview winners
        if midday_list:
            st.write("Midday Winners:", ", ".join(midday_list))
        if evening_list:
            st.write("Evening Winners:", ", ".join(evening_list))
        
        # States to process
        states_to_process = selected_states if selected_states else STATES
        st.write(f"Processing {len(states_to_process)} states...")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status = st.empty()
        
        # Process each state
        for i, state_name in enumerate(states_to_process):
            status.info(f"Processing {state_name}...")
            
            # Load tables for this state
            tables = load_state_data(state_name)
            
            if not tables:
                st.warning(f"No tables found for {state_name}")
                continue
            
            # Highlight winners
            highlighted_tables = highlight_winners_in_table(
                tables,
                midday_list,
                evening_list
            )
            
            # Save highlighted tables
            output_dir = os.path.join(get_winners_output_dir(), state_name)
            os.makedirs(output_dir, exist_ok=True)
            
            for section_key, df in highlighted_tables.items():
                if df is not None and not df.empty:
                    # Create winner-specific filename
                    winners_suffix = ""
                    if "Midday" in section_key and midday_list:
                        winners_suffix = f"_win{'_'.join(midday_list)}"
                    elif "Evening" in section_key and evening_list:
                        winners_suffix = f"_win{'_'.join(evening_list)}"
                    elif "Combined" in section_key and (midday_list or evening_list):
                        winners_suffix = "_winners"
                    
                    output_file = os.path.join(
                        output_dir, 
                        f"{state_name}_{section_key}{winners_suffix}.csv"
                    )
                    df.to_csv(output_file, index=False)
            
            # Update progress
            progress = (i + 1) / len(states_to_process)
            progress_bar.progress(progress)
        
        # Complete
        status.success("Winner highlighting completed!")
        
        # Show sample results
        if states_to_process:
            st.subheader("Sample Results (First State)")
            first_state = states_to_process[0]
            sample_tables = load_state_data(first_state)
            
            if "Midday_combined" in sample_tables and midday_list:
                st.write("Midday Combined Table (with winners):")
                highlighted = highlight_winners_in_table(
                    {"Midday_combined": sample_tables["Midday_combined"]},
                    midday_list,
                    []
                )
                st.dataframe(highlighted["Midday_combined"], use_container_width=True)
            
            if "Evening_combined" in sample_tables and evening_list:
                st.write("Evening Combined Table (with winners):")
                highlighted = highlight_winners_in_table(
                    {"Evening_combined": sample_tables["Evening_combined"]},
                    [],
                    evening_list
                )
                st.dataframe(highlighted["Evening_combined"], use_container_width=True)

def vtrac_analyzer_tab():
    """Enhanced V-TRAC Analyzer Tab Content with optimized performance"""
    st.header("Enhanced V-TRAC Pattern Analyzer")
    st.markdown("""
    This tool analyzes V-TRAC indexes for your selected dataset(s). Use the dropdown to view results for each state.
    """)
    st.info("Analysis may take longer for large datasets or when running all states.")
    
    # Dropdown for single state or all states
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
                print(f"[V-TRAC] Starting analysis for {state_name}...")
                state_start = time.time()
                status_text.info(f"Analyzing {state_name}...")
                
                # Check if we already have recent results (< 5 minutes old)
                current_time = time.time()
                cached_results_exist = (
                    state_name in st.session_state.vtrac_results and
                    state_name in st.session_state.last_analysis_time and
                    current_time - st.session_state.last_analysis_time.get(state_name, 0) < 300  # 5 minutes
                )
                
                if not cached_results_exist:
                    # Load tables (using cached function to avoid disk reads)
                    tables = load_state_data(state_name)
                    if not tables:
                        print(f"[V-TRAC] No tables found for {state_name}, skipping.")
                        st.warning(f"No tables found for {state_name}")
                        continue
                    
                    results = analyze_all_indexes(state_name)
                    if not results:
                        print(f"[V-TRAC] No analyzable data for {state_name}, skipping.")
                        st.warning(f"No analyzable data found for {state_name}")
                        continue
                    
                    # Store in session state
                    st.session_state.vtrac_results[state_name] = results
                    st.session_state.last_analysis_time[state_name] = current_time
                    
                    # Generate reports
                    reports = generate_top_reports(state_name, results, top_n_reports)
                    st.session_state.vtrac_reports[state_name] = reports
                else:
                    print(f"[V-TRAC] Using cached results for {state_name}")
                
                state_end = time.time()
                print(f"[V-TRAC] Finished {state_name} in {state_end - state_start:.2f} seconds.")
                
                progress = (i + 1) / len(states_to_run)
                progress_bar.progress(progress)
            
            total_end = time.time()
            print(f"[V-TRAC] All selected analyses complete in {total_end - total_start:.2f} seconds.")
            
            progress_bar.progress(1.0)
            status_text.success("Analysis completed!")
    
    # Always display results if we have them, regardless of whether button was pressed
    # This allows results to persist across UI interactions
    
    # Check if we have any analysis results
    has_results = False
    for state_name in (states_to_run if 'states_to_run' in locals() else STATES):
        if state_name in st.session_state.vtrac_results:
            has_results = True
            break
    
    if not has_results and selected_option in st.session_state.vtrac_results:
        has_results = True
    
    if has_results:
        st.markdown("## Analysis Results")
        
        # Dropdown to select which state's results to view
        available_states = [s for s in STATES if s in st.session_state.vtrac_results]
        
        if len(available_states) > 1:
            # If All States was selected but we only have one state's results, select it directly
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
        
        # Display when this analysis was performed
        if selected_state in st.session_state.last_analysis_time:
            last_time = datetime.fromtimestamp(st.session_state.last_analysis_time[selected_state])
            st.info(f"Analysis for {selected_state} was last run on {last_time.strftime('%Y-%m-%d at %H:%M:%S')}")
        
        # Display summary
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {selected_state}")
        
        # Display table with results
        top_results_df = pd.DataFrame([
            {
                "Rank": r["rank"],
                "Index": r["index"],
                "Score": f"{r['score']:.2f}",
                "Patterns": len(r["patterns"]),
                "Top Patterns": ", ".join(sorted(list(r["patterns"]))[:5]) + "..." if len(r["patterns"]) > 5 else ", ".join(sorted(r["patterns"]))
            }
            for r in results[:top_n_indexes]
        ])
        st.dataframe(top_results_df)
        
        # Display HTML reports
        if reports:
            st.subheader("Detailed Analysis Reports")
            report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:top_n_reports]])
            for tab, report in zip(report_tabs, reports[:top_n_reports]):
                with tab:
                    col1, col2, col3 = st.columns([1, 1, 1])
                    with col1:
                        st.write(f"V-TRAC Index: {report['index']} | Score: {report['score']:.2f}")
                    with col2:
                        st.download_button(
                            label=f"Download HTML (Rank #{report['rank']})",
                            data=report['html'],
                            file_name=report['filename'],
                            mime="text/html"
                        )
                    with col3:
                        if st.button(f"Open in Browser (Rank #{report['rank']})", key=f"open_browser_{selected_state}_{report['rank']}"):
                            webbrowser.open(f"file://{os.path.abspath(report['filepath'])}")
                    
                    # Add toggle for expanding the view
                    expand_view = st.checkbox("Expand View", key=f"expand_{selected_state}_{report['rank']}")
                    
                    # Show only the clustering HTML report (no raw tables)
                    if expand_view:
                        # Full width with more height when expanded
                        st.components.v1.html(report['html'], height=4000, scrolling=True)
                    else:
                        # Normal height when not expanded
                        st.components.v1.html(report['html'], height=3000, scrolling=True)
        elif top_n_reports > 0:
            st.info("No HTML reports were generated. Analysis might not have produced enough results.")

def highlight_winners_in_table(tables, midday_winners=None, evening_winners=None):
    """
    Highlights winning numbers in tables by adding color columns
    
    Args:
        tables: Dictionary of tables
        midday_winners: List of midday winning numbers
        evening_winners: List of evening winning numbers
        
    Returns:
        Dictionary of tables with highlighted winners
    """
    if not midday_winners and not evening_winners:
        return tables
    
    # Create copies to avoid modifying originals
    highlighted_tables = {}
    
    # Process each table
    for key, df in tables.items():
        if df is None or df.empty:
            highlighted_tables[key] = df
            continue
        
        # Create a copy
        highlighted_df = df.copy()
        
        # Add color columns based on winning numbers
        if "Midday" in key and midday_winners:
            for winner in midday_winners:
                # Check if any digit columns contain the winning number
                columns_to_check = [col for col in highlighted_df.columns if col.startswith('D') and col[1:].isdigit()]
                
                for col in columns_to_check:
                    # Create color column name
                    color_col = f"Color_{col}"
                    
                    # Initialize color column if it doesn't exist
                    if color_col not in highlighted_df.columns:
                        highlighted_df[color_col] = ""
                    
                    # Set color for matching cells
                    highlighted_df.loc[highlighted_df[col] == winner, color_col] = "yellow"
        
        if "Evening" in key and evening_winners:
            for winner in evening_winners:
                # Check if any digit columns contain the winning number
                columns_to_check = [col for col in highlighted_df.columns if col.startswith('D') and col[1:].isdigit()]
                
                for col in columns_to_check:
                    # Create color column name
                    color_col = f"Color_{col}"
                    
                    # Initialize color column if it doesn't exist
                    if color_col not in highlighted_df.columns:
                        highlighted_df[color_col] = ""
                    
                    # Set color for matching cells
                    highlighted_df.loc[highlighted_df[col] == winner, color_col] = "yellow"
        
        # Store the highlighted dataframe
        highlighted_tables[key] = highlighted_df
    
    return highlighted_tables

def create_output_directories():
    """Create all necessary output directories for the application"""
    # Create main data directories
    os.makedirs("data/original", exist_ok=True)
    os.makedirs("data/cleaned", exist_ok=True)
    
    # Create outputs directory structure
    outputs_dir = "data/outputs"
    os.makedirs(outputs_dir, exist_ok=True)
    
    # Create date-based directory
    today = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(outputs_dir, today)
    os.makedirs(date_dir, exist_ok=True)
    
    # Create tables directory
    tables_dir = os.path.join(date_dir, "tables")
    os.makedirs(tables_dir, exist_ok=True)
    
    # Create winners directory
    winners_dir = os.path.join(date_dir, "winners")
    os.makedirs(winners_dir, exist_ok=True)
    
    # Create vtrac directory
    vtrac_dir = os.path.join(date_dir, "vtrac")
    os.makedirs(vtrac_dir, exist_ok=True)
    
    # Create state directories in each
    for state in STATES:
        os.makedirs(os.path.join(tables_dir, state), exist_ok=True)
        os.makedirs(os.path.join(winners_dir, state), exist_ok=True)
        os.makedirs(os.path.join(vtrac_dir, state), exist_ok=True)
    
    return {
        "base": outputs_dir,
        "date": date_dir,
        "tables": tables_dir,
        "winners": winners_dir,
        "vtrac": vtrac_dir
    }

def get_tables_output_dir():
    """Get the current tables output directory"""
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("data", "outputs", today, "tables")

def get_winners_output_dir():
    """Get the current winners output directory"""
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("data", "outputs", today, "winners")

def get_vtrac_output_dir():
    """Get the current vtrac output directory"""
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("data", "outputs", today, "vtrac")

def get_cleaned_data_dir():
    """Get the cleaned data directory"""
    return os.path.join("data", "cleaned")

def main():
    """Main application layout and execution"""
    # Set sidebar
    st.sidebar.title("Alpha Analytical Tool")
    st.sidebar.image("https://img.icons8.com/fluency/96/lottery.png", width=80)
    st.sidebar.markdown("---")
    
    # Page title
    st.title("Alpha Analytical Tool")
    
    # Create tabs
    tabs = st.tabs([
        "📊 Process Data", 
        "👁 View Results", 
        "🏆 Log Winners", 
        "📈 V-TRAC Analyzer"
    ])
    
    # Process Data tab
    with tabs[0]:
        process_data_tab()
    
    # View Results tab
    with tabs[1]:
        view_results_tab()
    
    # Log Winners tab
    with tabs[2]:
        log_winners_tab()
    
    # V-TRAC Analyzer tab
    with tabs[3]:
        vtrac_analyzer_tab()
    
    # Display date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.text(f"Last Updated: {now}")

if __name__ == "__main__":
    main() 