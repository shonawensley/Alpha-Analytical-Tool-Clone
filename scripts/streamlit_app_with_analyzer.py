#!/usr/bin/env python
"""
Alpha Analytical Tool with V-TRAC Analysis
Provides data processing, table generation, and pattern analysis for numerical datasets
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
from PIL import Image
import time

# Add the project root to the Python path
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
    highlight_winners_in_table,
    highlight_string_with_matches
)

# Set page config
st.set_page_config(
    page_title="Alpha Analytical Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

#------------------------------------------------------------------------------
# MAIN APP FUNCTIONS (from streamlit_app.py)
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

def load_state_data(state_name):
    """Load generated tables for a specific state"""
    tables_dir = os.path.join(get_tables_output_dir(), state_name)
    result = {}
    
    if os.path.exists(tables_dir):
        for filename in os.listdir(tables_dir):
            if filename.endswith(".csv"):
                filepath = os.path.join(tables_dir, filename)
                key = os.path.splitext(filename)[0].replace(f"{state_name}_", "")
                try:
                    df = pd.read_csv(filepath)
                    result[key] = df
                except Exception as e:
                    st.error(f"Error loading {filename}: {e}")
    
    return result

#------------------------------------------------------------------------------
# V-TRAC ANALYZER FUNCTIONS (from vtrac_analyzer.py)
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
    """
    Calculate an overall score for a V-TRAC index based on pattern occurrence frequency.
    Analyzes patterns across all combined tables (Midday, Evening, Combined).
    """
    if not tables or not patterns:
        return 0
        
    # Check for required tables
    required_tables = ["Midday_combined", "Evening_combined", "Combined_combined"]
    if not all(table in tables for table in required_tables):
        print(f"[ERROR] Missing required tables. Found: {list(tables.keys())}")
        return 0
    
    total_score = 0
    
    # Analyze each combined table
    for table_name in required_tables:
        df = tables[table_name]
        if df is not None and not df.empty:
            # Get pattern counts for this table
            pattern_counts, _ = count_patterns_in_table(df, patterns)
            # Add to total score
            total_score += sum(pattern_counts.values())
    
    # Multiply by 10 for final score
    return total_score * 10

def analyze_all_indexes(state_name):
    """Analyze all V-TRAC indexes for a state and rank them"""
    # Load tables for the state
    tables = load_state_data(state_name)
    
    # Check for required tables
    required_tables = ["Midday_combined", "Evening_combined", "Combined_combined"]
    if not tables or not all(table in tables for table in required_tables):
        print(f"[ERROR] Missing required tables for {state_name}. Found: {list(tables.keys() if tables else [])}")
        return None
    
    # Analyze each V-TRAC index
    results = []
    
    # Get all valid V-TRAC indexes from reference
    for entry in BOXED_VTRAC_REFERENCE:
        index = entry["Index"]
        # Get all patterns for this index
        patterns = set()
        patterns.update(entry.get("Singles", []))
        patterns.update(entry.get("Doubles", []))
        
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
    
    return results

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
    
    # Function to generate table HTML
    def generate_table_html(df, title):
        # Check if dataframe is None or empty
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
    
    # START IMMEDIATELY with tables at the very top
    html += '<style>.horizontal-layout{display:flex; flex-direction:row; justify-content:space-between; width:100%; margin:0; padding:0;} .section{flex:1; margin:0 2px;}</style>'
    
    # Display all three sections horizontally side-by-side without any header
    html += '<div class="horizontal-layout">'
    
    # Midday section
    html += '<div class="section">'
    html += '<h2>Midday Data</h2>'
    if "Midday_combined" in tables:
        html += generate_table_html(tables["Midday_combined"], f"{state_name} Midday Combined Table")
    if "Midday_r2" in tables:
        html += generate_table_html(tables["Midday_r2"], f"{state_name} Midday R2-only Table")
    html += '</div>'
    
    # Evening section
    html += '<div class="section">'
    html += '<h2>Evening Data</h2>'
    if "Evening_combined" in tables:
        html += generate_table_html(tables["Evening_combined"], f"{state_name} Evening Combined Table")
    if "Evening_r2" in tables:
        html += generate_table_html(tables["Evening_r2"], f"{state_name} Evening R2-only Table")
    html += '</div>'
    
    # Combined section
    html += '<div class="section">'
    html += '<h2>Combined Data</h2>'
    if "Combined_combined" in tables:
        html += generate_table_html(tables["Combined_combined"], f"{state_name} Combined Combined Table")
    if "Combined_r2" in tables:
        html += generate_table_html(tables["Combined_r2"], f"{state_name} Combined R2-only Table")
    html += '</div>'
    
    # Close horizontal layout
    html += '</div>'
    
    # V-TRAC info (below tables)
    html += f'<div class="version">Version: v{timestamp}</div>'
    html += f'<h1><span class="rank-badge">Rank #{rank}</span> V-TRAC Analysis for {state_name} - Index {index}</h1>'
    
    # Statistics section at the bottom
    html += '<div class="stats">'
    html += '<h2>Detailed Analysis Statistics</h2>'
    
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
    html += '</div>'
    
    # Close HTML
    html += '</body></html>'
    
    return html

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
        rank = i + 1  # Calculate rank position
        
        # Generate HTML
        html = generate_index_html_report(
            state_name, 
            result["index"], 
            result["patterns"], 
            tables, 
            result["score"], 
            rank,
            timestamp
        )
        
        # Generate filename
        filename = f"{state_name}_vtrac_rank{rank}_index{result['index']}_v{timestamp}.html"
        
        # Define save path
        output_dir = os.path.join(os.path.dirname(script_dir), "outputs", "analysis")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        
        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        
        # Add to reports
        reports.append({
            "rank": rank,
            "index": result["index"],
            "score": result["score"],
            "filename": filename,
            "filepath": filepath,
            "html": html
        })
    
    return reports

def generate_summary_chart(results, top_n=10):
    """Generate a summary chart of top indexes"""
    if not results or len(results) == 0:
        return None
    
    # Limit to top N results
    top_results = results[:min(top_n, len(results))]
    
    # Extract data for chart
    indices = [str(r["index"]) for r in top_results]
    scores = [r["score"] for r in top_results]
    
    # Create chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(indices, scores, color='purple', alpha=0.7)
    
    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'{height:.0f}',
                 ha='center', va='bottom')
    
    # Add chart details
    plt.title('Top V-TRAC Indexes by Score', fontsize=16)
    plt.xlabel('V-TRAC Index', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Convert to base64 for embedding in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    
    return f"data:image/png;base64,{image_base64}"

def get_combined_table(state_name, time_period):
    """Load combined table for state and time period"""
    tables_dir = get_tables_output_dir()  
    # Get most recent date folder
    date_folders = sorted([d for d in os.listdir(tables_dir) if os.path.isdir(os.path.join(tables_dir, d))], reverse=True)
    if not date_folders:
        return None
    
    # Use most recent date
    state_dir = os.path.join(tables_dir, date_folders[0], state_name)
    if not os.path.exists(state_dir):
        return None
    
    # Look for the combined table file
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
    # Get most recent date folder
    date_folders = sorted([d for d in os.listdir(tables_dir) if os.path.isdir(os.path.join(tables_dir, d))], reverse=True)
    if not date_folders:
        return None
    
    # Use most recent date
    state_dir = os.path.join(tables_dir, date_folders[0], state_name)
    if not os.path.exists(state_dir):
        return None
    
    # Look for the R2-only table file
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
    """Highlight winning numbers in tables and save highlighted versions
    
    Args:
        tables (dict): Dictionary of table DataFrames
        midday_winners (list): List of midday winning number strings
        evening_winners (list): List of evening winning number strings
        
    Returns:
        dict: Dictionary of highlighted DataFrames
    """
    highlighted_tables = {}
    
    # Function to apply highlight style
    def highlight_winner(row):
        # Create a styling DataFrame with same dimensions as row
        styles = pd.Series([''] * len(row), index=row.index)
        
        # Check which numbers to highlight
        highlight_nums = []
        if 'Midday' in row.get('Category', ''):
            highlight_nums = midday_winners
        elif 'Evening' in row.get('Category', ''):
            highlight_nums = evening_winners
        else:
            # For combined tables, highlight both
            highlight_nums = midday_winners + evening_winners
        
        # Apply highlight style
        for num_col in ['Num1', 'Num2', 'Num3']:
            if num_col in row and str(row[num_col]) in highlight_nums:
                styles[num_col] = 'background-color: yellow; font-weight: bold'
        
        # Check combined number
        if 'Number' in row and str(row['Number']) in highlight_nums:
            styles['Number'] = 'background-color: yellow; font-weight: bold'
            
        return styles
    
    # Process each table
    for key, df in tables.items():
        if df is None or df.empty:
            highlighted_tables[key] = df
            continue
            
        # Copy the DataFrame to avoid modifying the original
        highlighted_df = df.copy()
        
        # Apply styling
        try:
            styled_df = highlighted_df.style.apply(highlight_winner, axis=1)
            highlighted_tables[key] = styled_df
        except Exception as e:
            st.warning(f"Could not highlight winners in {key}: {str(e)}")
            highlighted_tables[key] = highlighted_df
    
    return highlighted_tables

#------------------------------------------------------------------------------
# COMBINED MAIN APP
#------------------------------------------------------------------------------

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

def process_data_tab():
    """The Process Data tab"""
    st.title("Data Processing")
    st.markdown("Process raw data files to generate cleaned datasets and analysis tables.")
    
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
        default=[]
    )
    
    # Use all states if none selected
    states_to_process = selected_states if selected_states else STATES
    
    # Process button
    if st.button("Process Data"):
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
            
            # Step 2: Extract data
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
            
            # Step 3: Generate tables
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
    """The View Results tab"""
    st.title("View Results")
    st.markdown("View the generated tables and analysis results.")
    
    # Find the most recent date folder
    output_dir = get_tables_output_dir()
    if not os.path.exists(output_dir):
        st.error(f"Output directory not found: {output_dir}")
        st.info("Please process data first.")
        return
    
    # Check if there are any files/directories in the output directory
    if len(os.listdir(output_dir)) == 0:
        st.error("No output data found.")
        st.info("Please process data first.")
        return
    
    # List state directories directly instead of assuming date folders
    available_states = sorted([d for d in os.listdir(output_dir) 
                              if os.path.isdir(os.path.join(output_dir, d))])
    
    if not available_states:
        st.error("No state data found.")
        st.info("Please process data first.")
        return
    
    # Select state
    selected_state = st.selectbox("Select state:", available_states)
    
    # Get tables for the selected state
    state_dir = os.path.join(output_dir, selected_state)
    available_tables = sorted([f for f in os.listdir(state_dir) if f.endswith(".csv")])
    
    if not available_tables:
        st.error(f"No tables found for state: {selected_state}")
        return
    
    # Select table type
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
        available_options = available_tables  # Fallback to all tables if expected ones aren't found
        
    selected_table = st.selectbox("Select table type:", available_options)
    
    # Display the selected table
    table_path = os.path.join(state_dir, selected_table)
    if os.path.exists(table_path):
        try:
        df = pd.read_csv(table_path)
        
        # Apply background colors to different sets
        def highlight_sets(s):
            if s.name != 'Set':
                return [''] * len(s)
            
            return ['background-color: rgba(31, 119, 180, 0.1)' if x == 'Set3'
                   else 'background-color: rgba(44, 160, 44, 0.1)' if x == 'Set2'
                   else 'background-color: rgba(255, 127, 14, 0.1)' if (x == 'Set1')
                   else '' for x in s]
        
        # Display styled table
        st.dataframe(
            df.style.apply(highlight_sets, axis=0).set_properties(**{
                'text-align': 'center',
                'font-family': 'monospace',
                'white-space': 'nowrap'
            }),
            use_container_width=True
        )
        
        # Download button
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
    """Enhanced V-TRAC Analyzer Tab Content with optimized performance and improved layout from clustering_app_3"""
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
                
                # Initialize session state for this state if needed
                if 'vtrac_results' not in st.session_state:
                    st.session_state.vtrac_results = {}
                if 'vtrac_reports' not in st.session_state:
                    st.session_state.vtrac_reports = {}
                if 'last_analysis_time' not in st.session_state:
                    st.session_state.last_analysis_time = {}
                
                # Check if we already have recent results (< 5 minutes old)
                current_time = time.time()
                cached_results_exist = (
                    state_name in st.session_state.vtrac_results and
                    state_name in st.session_state.last_analysis_time and
                    current_time - st.session_state.last_analysis_time.get(state_name, 0) < 300  # 5 minutes
                )
                
                if not cached_results_exist:
                    # Load tables using the efficient load_state_data function
                    tables = load_state_data(state_name)
                    if not tables:
                        print(f"[V-TRAC] No tables found for {state_name}, skipping.")
                        st.warning(f"No tables found for {state_name}")
                        progress_bar.progress((i+1)/len(states_to_run))
                        continue
                    
                    results = analyze_all_indexes(state_name)
                    if not results:
                        print(f"[V-TRAC] No analyzable data for {state_name}, skipping.")
                        st.warning(f"No analyzable data found for {state_name}")
                        progress_bar.progress((i+1)/len(states_to_run))
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
                
                progress_bar.progress((i+1)/len(states_to_run))
            
            total_end = time.time()
            print(f"[V-TRAC] All selected analyses complete in {total_end - total_start:.2f} seconds.")
            
            status_text.success("Analysis completed!")
    
    # Always display results if we have them, regardless of whether button was pressed
    # This allows results to persist across UI interactions
    
    # Check if we have any analysis results
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
            last_t = datetime.fromtimestamp(st.session_state.last_analysis_time[selected_state])
            st.info(f"Analysis for {selected_state} was last run on {last_t.strftime('%Y-%m-%d at %H:%M:%S')}")
        
        # Display summary
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {selected_state}")
        
        # Display table with results
        top_results_df = pd.DataFrame([
            {
                "Rank": i + 1,  # Calculate rank position directly
                "Index": r["index"],
                "Score": f"{r['score']:.2f}",
                "Patterns": len(r["patterns"]),
                "Top Patterns": ", ".join(sorted(list(r["patterns"]))[:5]) + "..." if len(r["patterns"]) > 5 else ", ".join(sorted(r["patterns"]))
            }
            for i, r in enumerate(results[:top_n_indexes])
        ])
        st.dataframe(top_results_df, use_container_width=True)
        
        # Show the #1 rank table set in three columns (from clustering_app_3)
        if results:
            best_result = results[0]  # rank #1
            st.subheader(f"Top Ranked Index Tables (Index #{best_result['index']})")
            st.write("Midday, Evening, and Combined data for the highest-scoring index.")
            
            # Get tables for this state (using our efficient table loading)
            st_tbls = load_state_data(selected_state)
            col1, col2, col3 = st.columns(3)
                    
                    with col1:
                st.markdown("**Midday Combined Table**")
                if "Midday_combined" in st_tbls:
                    st.dataframe(st_tbls["Midday_combined"], use_container_width=True, height=400)
                    csv = st_tbls["Midday_combined"].to_csv(index=False)
                    st.download_button(
                        "Download Midday Combined Table",
                        data=csv,
                        file_name=f"{selected_state}_Midday_combined.csv",
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
                        file_name=f"{selected_state}_Evening_combined.csv",
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
                        file_name=f"{selected_state}_Combined_combined.csv",
                        mime="text/csv",
                        key="dl_top_combined_combined"
                    )
                else:
                    st.info("No Combined table available")
        
        # Display HTML reports in tabs
        if reports and top_n_reports > 0:
            st.subheader("Detailed Analysis Reports")
            # Add rank to reports if needed
            for i, report in enumerate(reports):
                if 'rank' not in report:
                    report['rank'] = i + 1
                    
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
                        if st.button(f"Open in Browser (Rank #{report['rank']})", 
                                     key=f"open_browser_{selected_state}_{report['rank']}"):
                            webbrowser.open(f"file://{os.path.abspath(report['filepath'])}")
                    
                    # Add toggle for expanding the view
                    expand_view = st.checkbox("Expand View", key=f"expand_{selected_state}_{report['rank']}")
        
                    # Show HTML report with different heights based on expand state
                    if expand_view:
                        st.components.v1.html(report['html'], height=4000, scrolling=True)
                    else:
                        st.components.v1.html(report['html'], height=3000, scrolling=True)
        elif top_n_reports > 0:
            st.info("No HTML reports were generated. Analysis might not have produced enough results.")
    else:
        st.info("No analysis results found. Please run an analysis first.")

if __name__ == "__main__":
    main() 