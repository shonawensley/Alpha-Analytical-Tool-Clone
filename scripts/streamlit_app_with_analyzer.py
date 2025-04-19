#!/usr/bin/env python
"""
streamlit_app_with_analyzer.py - Enhanced Streamlit interface with V-TRAC analyzer
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

# Set page config
st.set_page_config(
    page_title="Lottery Data Processor with V-TRAC Analyzer",
    page_icon="🎲",
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
        # Generate HTML
        html = generate_index_html_report(
            state_name, 
            result["index"], 
            result["patterns"], 
            tables, 
            result["score"], 
            i + 1,
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

#------------------------------------------------------------------------------
# COMBINED MAIN APP
#------------------------------------------------------------------------------

def main():
    # Sidebar navigation
    st.sidebar.title("Lottery Data Processor")
    st.sidebar.image("https://img.icons8.com/fluency/96/lottery.png", width=80)
    
    # Tabs for different sections
    app_mode = st.sidebar.radio(
        "Select Mode",
        ["Process Data", "View Results", "V-TRAC Analyzer", "About"]
    )
    
    # Process Data tab
    if app_mode == "Process Data":
        st.header("Process Lottery Data")
        
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
    
    # View Results tab
    elif app_mode == "View Results":
        st.header("View Results")
        
        # Select state
        state = st.selectbox("Select State", STATES)
        
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
                        csv,
                        f"{state}_{section}_combined.csv",
                        "text/csv",
                        key=f"dl-combined-{section}"
                    )
                
                st.subheader(f"{section} - R2-only Table")
                if r2_key in state_data:
                    st.dataframe(
                        state_data[r2_key],
                        use_container_width=True,
                        height=400
                    )
                    
                    # Download option
                    csv = state_data[r2_key].to_csv(index=False)
                    st.download_button(
                        f"Download {section} R2-only Table",
                        csv,
                        f"{state}_{section}_r2.csv",
                        "text/csv",
                        key=f"dl-r2-{section}"
                    )
    
    # V-TRAC Analyzer tab
    elif app_mode == "V-TRAC Analyzer":
        vtrac_analyzer_tab()
    
    # About tab
    else:
        st.header("About This Tool")
        st.markdown("""
        ## Lottery Data Processor with V-TRAC Analyzer
        
        This tool combines data processing and analysis features:
        
        1. **Process Data:** Clean, extract, and generate tables from Excel files
        2. **View Results:** View and download generated tables
        3. **V-TRAC Analyzer:** Analyze state data for optimal V-TRAC indexes and pattern predictions
        
        The V-TRAC Analyzer evaluates all 35 pattern indexes to find those with strongest clustering 
        across your data tables. It scores indexes based on:
        
        - Pattern occurrence frequency
        - Pattern persistence across columns
        - Pattern stability within row types
        - Straight combinations
        
        Top-scoring indexes are presented with detailed HTML reports showing pattern highlighting 
        across all data tables.
        """)
        
        # Add notes about file locations and data paths
        st.subheader("Important File Locations")
        st.markdown("""
        - Input Excel: `data/original/Pick3StatsC4.xlsm`
        - Cleaned Data: `data/cleaned/[STATE]_cleaned.xlsx`
        - Generated Tables: `data/outputs/[STATE]/*.csv`
        - Analysis Reports: `data/outputs/analysis/*.html`
        """)

def vtrac_analyzer_tab():
    """V-TRAC Analyzer Interface"""
    st.title("V-TRAC Pattern Analyzer")
    st.markdown("Analyze state data for optimal V-TRAC indexes and pattern predictions")
    
    # Select state
    state_name = st.selectbox("Select State", STATES)
    
    # Analysis options
    st.subheader("Analysis Options")
    col1, col2 = st.columns(2)
    
    with col1:
        top_n_indexes = st.slider("Number of Top Indexes to Display", 1, 35, 10)
    
    with col2:
        top_n_reports = st.slider("Number of HTML Reports to Generate", 0, 10, 3)
    
    # Run analysis button
    if st.button("Run V-TRAC Analysis", type="primary"):
        progress_bar = st.progress(0)
        status = st.empty()
        
        status.info("Step 1/4: Loading state data...")
        tables = load_state_data(state_name)
        if not tables:
            st.error(f"No table data loaded for {state_name}. Please process data first.")
            return
        progress_bar.progress(25)
        
        status.info("Step 2/4: Analyzing all V-TRAC indexes...")
        results = analyze_all_indexes(state_name)
        if not results:
            st.error(f"Analysis failed for {state_name}. Please check the data.")
            return
        progress_bar.progress(50)
        
        status.info("Step 3/4: Generating HTML reports...")
        if top_n_reports > 0:
            reports = generate_top_reports(state_name, results, top_n_reports)
        else:
            reports = []
        progress_bar.progress(75)
        
        status.info("Step 4/4: Preparing visualization...")
        chart_image = generate_summary_chart(results, top_n_indexes)
        progress_bar.progress(100)
        
        status.success("Analysis complete!")
        
        # Display top indexes first
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {state_name}")
        top_results_df = pd.DataFrame([
            {
                "Rank": i + 1,
                "Index": r["index"],
                "Score": f"{r['score']:.2f}",
                "Patterns": len(r["patterns"]),
                "Pattern List": ", ".join(sorted(r["patterns"]))
            }
            for i, r in enumerate(results[:top_n_indexes])
        ])
        st.dataframe(top_results_df, use_container_width=True)
        
        # Show chart if available
        if chart_image:
            st.subheader("Score Distribution")
            st.image(chart_image)
        
        # Display top 3 reports with full tables and statistics
        if reports:
            st.subheader("Detailed Analysis Reports")
            report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports[:3]])
            
            for tab, report in zip(report_tabs, reports[:3]):
                with tab:
                    # File info row
                    col1, col2, col3 = st.columns([1, 1, 1])
                    
                    with col1:
                        st.write(f"V-TRAC Index: {report['index']} | Score: {report['score']:.2f}")
                    
                    with col2:
                        # Download button
                        st.download_button(
                            label=f"Download HTML (Rank #{report['rank']})",
                            data=report['html'],
                            file_name=report['filename'],
                            mime="text/html"
                        )
                    
                    with col3:
                        # Open in browser button
                        if st.button(f"Open in Browser (Rank #{report['rank']})", 
                                   key=f"open_browser_{report['rank']}"):
                            webbrowser.open(f"file://{os.path.abspath(report['filepath'])}")
                    
                    # Preview with maximum height
                    st.components.v1.html(report['html'], height=1800, scrolling=True)
        
        elif top_n_reports > 0:
            st.info("No HTML reports were generated. Analysis might not have produced enough results.")
    else:
        # Show example of what to expect
        st.info("Click 'Run V-TRAC Analysis' to analyze patterns and generate reports.")

if __name__ == "__main__":
    main() 