#!/usr/bin/env python
"""
Integrated Alpha Analytical Tool with V-TRAC Analysis
"""
import streamlit as st

# THIS MUST BE THE VERY FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Alpha Analytical Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import webbrowser
import base64
import io
from collections import Counter

# Add project root to path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

# Import utility modules
from utils.vtrac_utils import BOXED_VTRAC_REFERENCE
from utils.path_handler import (
    get_excel_path,
    create_output_directories,
    get_cleaned_data_dir,
    get_tables_output_dir
)
from utils.state_utils import STATES
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables

# Functions from vtrac_analyzer.py
def load_state_tables(state_name):
    """Load all tables for a specific state from the most recent date folder"""
    tables_root = os.path.join(project_root, "data", "outputs", "tables")
    if not os.path.exists(tables_root):
        st.error(f"Tables root directory not found: {tables_root}")
        return {}

    date_folders = sorted(
        [d for d in os.listdir(tables_root) if os.path.isdir(os.path.join(tables_root, d))],
        reverse=True
    )

    for date_folder in date_folders:
        state_tables_dir = os.path.join(tables_root, date_folder, state_name)
        if os.path.exists(state_tables_dir) and os.listdir(state_tables_dir):
            result = {}
            for filename in os.listdir(state_tables_dir):
                if filename.endswith(".csv"):
                    filepath = os.path.join(state_tables_dir, filename)
                    key = os.path.splitext(filename)[0].replace(f"{state_name}_", "")
                    try:
                        df = pd.read_csv(filepath)
                        result[key] = df
                        st.write(f"[INFO] Loaded table: {key}")
                    except Exception as e:
                        st.error(f"Error loading {filename}: {e}")
            if result:
                st.success(f"Loaded tables for {state_name}")
                return result
    st.error(f"No tables found for {state_name}")
    return {}

def analyze_vtrac_patterns(state_name, tables):
    """Analyze V-TRAC patterns in the tables"""
    results = []
    
    # Get all valid V-TRAC indexes
    vtrac_indices = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
    
    for index in vtrac_indices:
        # Get patterns for this index
        vtrac_entry = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == index), None)
        if not vtrac_entry:
            continue
            
        patterns = set()
        patterns.update(vtrac_entry.get("Singles", []))
        patterns.update(vtrac_entry.get("Doubles", []))
        
        if not patterns:
            continue
            
        # Calculate score based on pattern occurrences and clustering
        score = calculate_index_score(tables, patterns)
        
        results.append({
            "index": index,
            "patterns": patterns,
            "score": score
        })
    
    # Sort by score and add ranks
    results.sort(key=lambda x: x["score"], reverse=True)
    for i, result in enumerate(results):
        result["rank"] = i + 1
        
    return results

def calculate_index_score(tables, patterns):
    """Calculate score for a V-TRAC index based on pattern clustering"""
    overall_score = 0
    
    # Weight different aspects of pattern analysis
    weights = {
        "occurrence": 0.35,
        "persistence": 0.30,
        "stability": 0.25,
        "straight": 0.10
    }
    
    for table_type in ["Combined_combined", "Midday_combined", "Evening_combined"]:
        if table_type not in tables:
            continue
            
        df = tables[table_type]
        
        # Count pattern occurrences
        pattern_counts = count_patterns_in_table(df, patterns)
        occurrence_score = sum(pattern_counts.values())
        
        # Analyze persistence across columns
        persistence_score = analyze_pattern_persistence(df, patterns)
        
        # Analyze stability within row types
        stability_score = analyze_pattern_stability(df, patterns)
        
        # Count straight combinations
        straight_score = sum(detect_straight_combinations(df, pattern) for pattern in patterns)
        
        # Calculate weighted score for this table
        table_score = (
            occurrence_score * weights["occurrence"] +
            persistence_score * weights["persistence"] +
            stability_score * weights["stability"] +
            straight_score * weights["straight"]
        )
        
        overall_score += table_score
        
    return overall_score

def count_patterns_in_table(df, patterns):
    """Count occurrences of patterns in a table"""
    pattern_counts = Counter()
    
    for col in ['7', '6', '5', '4', '3', '2', '1']:
        if col in df.columns:
            for value in df[col].astype(str):
                for pattern in patterns:
                    pattern_counts[pattern] += value.count(pattern)
                    
    return pattern_counts

def analyze_pattern_persistence(df, patterns):
    """Calculate persistence score based on patterns appearing in consecutive columns"""
    total_score = 0
    columns = ['7', '6', '5', '4', '3', '2', '1']
    
    for pattern in patterns:
        for _, row in df.iterrows():
            consecutive = 0
            max_consecutive = 0
            
            for col in columns:
                if col in df.columns and pattern in str(row[col]):
                    consecutive += 1
                else:
                    max_consecutive = max(max_consecutive, consecutive)
                    consecutive = 0
                    
            max_consecutive = max(max_consecutive, consecutive)
            total_score += max_consecutive ** 2
            
    return total_score

def analyze_pattern_stability(df, patterns):
    """Calculate stability score based on patterns appearing across different row types"""
    total_score = 0
    
    for pattern in patterns:
        for _, group in df.groupby(['Set', 'Draw']):
            row_types_with_pattern = set()
            
            for row_type in ['R2', 'R4', 'R6', 'R8']:
                type_rows = group[group['RowType'] == row_type]
                if type_rows.empty:
                    continue
                    
                pattern_found = False
                for col in ['7', '6', '5', '4', '3', '2', '1']:
                    if col in df.columns:
                        for value in type_rows[col].astype(str):
                            if pattern in value:
                                pattern_found = True
                                break
                    if pattern_found:
                        row_types_with_pattern.add(row_type)
                        break
                        
            total_score += len(row_types_with_pattern) ** 2
            
    return total_score

def detect_straight_combinations(df, pattern):
    """Count instances of patterns appearing in straight combinations"""
    straight_count = 0
    columns = ['7', '6', '5', '4', '3', '2', '1']
    
    for _, row in df.iterrows():
        occurrences = sum(
            1 for col in columns 
            if col in df.columns and pattern in str(row[col])
        )
        if occurrences > 1:
            straight_count += occurrences
            
    return straight_count

def generate_analysis_report(state_name, results, tables):
    """Generate HTML report for the analysis results"""
    if not results:
        return None
        
    # Get top 3 results
    top_results = results[:3]
    
    # Create summary chart
    plt.figure(figsize=(10, 6))
    indices = [str(r["index"]) for r in top_results]
    scores = [r["score"] for r in top_results]
    
    bars = plt.bar(indices, scores, color='purple', alpha=0.7)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{height:.0f}',
                ha='center', va='bottom')
    
    plt.title('Top V-TRAC Indexes by Score', fontsize=16)
    plt.xlabel('V-TRAC Index', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Convert plot to base64 for embedding
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    
    # Generate HTML report
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            .highlight {{ color: purple; font-weight: bold; }}
            .chart {{ text-align: center; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <h1>V-TRAC Analysis Report for {state_name}</h1>
        <div class="chart">
            <img src="data:image/png;base64,{image_base64}" alt="Top Indexes Chart">
        </div>
        <h2>Top 3 V-TRAC Indexes</h2>
        <table>
            <tr>
                <th>Rank</th>
                <th>Index</th>
                <th>Score</th>
                <th>Patterns</th>
            </tr>
    """
    
    for result in top_results:
        html += f"""
            <tr>
                <td>{result['rank']}</td>
                <td>{result['index']}</td>
                <td>{result['score']:.2f}</td>
                <td>{', '.join(sorted(result['patterns']))}</td>
            </tr>
        """
    
    html += """
        </table>
    </body>
    </html>
    """
    
    return html

def main():
    """Main function to run the integrated app"""
    st.title("Alpha Analytical Tool")
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/150x80?text=Alpha+Analytics", width=150)
        
        mode = st.radio(
            "Select Mode",
            ["Process Data", "V-TRAC Analysis", "About"]
        )
    
    if mode == "Process Data":
        st.header("Process Lottery Data")
        
        # Check for Excel file
        excel_path = get_excel_path()
        if not os.path.exists(excel_path):
            st.error("Excel file not found. Please ensure Pick3StatsC4.xlsm is in the data/original folder.")
            return
            
        if st.button("Process All States"):
            with st.spinner("Processing data..."):
                try:
                    # Create necessary directories
                    create_output_directories()
                    
                    # Get required paths
                    cleaned_dir = get_cleaned_data_dir()
                    tables_dir = get_tables_output_dir()
                    
                    st.info("Step 1: Cleaning data for all states...")
                    # Clean all states data at once
                    clean_all_states(STATES, excel_path, cleaned_dir)
                    
                    st.info("Step 2: Extracting data...")
                    # Extract all states data at once
                    extracted_data = extract_all_states(STATES, cleaned_dir)
                    
                    st.info("Step 3: Generating tables...")
                    # Generate tables for all states
                    for state in STATES:
                        generate_tables(extracted_data[state], state)
                    
                    st.success("Data processing complete!")
                except Exception as e:
                    st.error(f"Error during data processing: {str(e)}")
                    st.info("Please check that all required files and directories are in place.")
                    
    elif mode == "V-TRAC Analysis":
        st.header("V-TRAC Pattern Analysis")
        
        # State selection
        analysis_mode = st.radio("Analysis Mode", ["Single State", "All States"])
        
        if analysis_mode == "Single State":
            state = st.selectbox("Select State", STATES)
            
            if st.button("Run Analysis"):
                with st.spinner("Analyzing patterns..."):
                    # Load tables
                    tables = load_state_tables(state)
                    
                    if tables:
                        # Analyze patterns
                        results = analyze_vtrac_patterns(state, tables)
                        
                        if results:
                            # Generate and display report
                            report = generate_analysis_report(state, results, tables)
                            
                            if report:
                                # Save report
                                report_dir = os.path.join(project_root, "outputs", "analysis")
                                os.makedirs(report_dir, exist_ok=True)
                                
                                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                                filename = f"{state}_vtrac_analysis_{timestamp}.html"
                                filepath = os.path.join(report_dir, filename)
                                
                                with open(filepath, "w", encoding="utf-8") as f:
                                    f.write(report)
                                
                                # Display in Streamlit
                                st.components.v1.html(report, height=800, scrolling=True)
                                
                                # Download button
                                st.download_button(
                                    "Download Report",
                                    report,
                                    file_name=filename,
                                    mime="text/html"
                                )
                            else:
                                st.error("Failed to generate analysis report.")
                        else:
                            st.error("No analysis results found.")
                    else:
                        st.error("Failed to load state tables. Please process data first.")
                        
        else:  # All States
            if st.button("Analyze All States"):
                with st.spinner("Analyzing all states..."):
                    all_results = {}
                    
                    for state in STATES:
                        tables = load_state_tables(state)
                        if tables:
                            results = analyze_vtrac_patterns(state, tables)
                            if results:
                                all_results[state] = results
                    
                    if all_results:
                        st.success("Analysis complete!")
                        
                        # Create tabs for each state
                        state_tabs = st.tabs(list(all_results.keys()))
                        
                        for tab, (state, results) in zip(state_tabs, all_results.items()):
                            with tab:
                                report = generate_analysis_report(state, results, load_state_tables(state))
                                if report:
                                    st.components.v1.html(report, height=800, scrolling=True)
                    else:
                        st.error("No results found. Please process data first.")
                        
    else:  # About
        st.header("About")
        st.markdown("""
        # Alpha Analytical Tool with V-TRAC Analysis
        
        This tool combines lottery data processing with advanced V-TRAC pattern analysis:
        
        1. **Data Processing**
           - Reads and cleans lottery data
           - Generates combined tables
           - Prepares data for analysis
           
        2. **V-TRAC Analysis**
           - Analyzes pattern clustering
           - Identifies strongest V-TRAC indexes
           - Generates detailed reports
           
        3. **Features**
           - Single state or all states analysis
           - Automated pattern detection
           - Statistical scoring
           - Interactive visualizations
        """)

if __name__ == "__main__":
    main() 