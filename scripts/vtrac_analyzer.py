#!/usr/bin/env python
"""
vtrac_analyzer.py - Analytical tool for V-TRAC pattern prediction

This tool:
1. Analyzes all 35 V-TRAC indexes across state datasets
2. Scores and ranks indexes by pattern clustering strength
3. Generates HTML reports for the top indexes
4. Provides statistical analysis of pattern persistence
"""

import os
import sys
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
import webbrowser
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
import io
import base64

# Add script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import utility modules
from utils.vtrac_utils import BOXED_VTRAC_REFERENCE
from utils.path_handler import get_tables_output_dir, get_project_root
from utils.state_utils import STATES

# Function to load tables for a specific state
def load_state_tables(state_name):
    """
    Load all tables for a specific state from the most recent non-empty date folder.
    This will fix the issue where the analyzer can't find the combined tables.
    """
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

# Function to get all combinations from a V-TRAC index
def get_all_combinations_for_index(index):
    """Get all pattern combinations for a specific V-TRAC index"""
    vtrac_entry = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == index), None)
    
    if vtrac_entry:
        combinations = set()
        combinations.update(vtrac_entry.get("Singles", []))
        combinations.update(vtrac_entry.get("Doubles", []))
        return combinations
    
    return set()

# Function to count pattern occurrences in a table
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

# Function to analyze persistence of patterns across columns
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

# Function to analyze pattern stability within row types
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

# Function to detect straight combinations (same order)
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

# Function to calculate an overall score for a V-TRAC index
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

# Function to generate HTML report for a V-TRAC index
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
        }}
        .column {{
            flex: 0 0 32%;
            margin-bottom: 20px;
        }}
        @media (max-width: 1200px) {{
            .column {{
                flex: 0 0 100%;
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
<div class="stats">
    <h2>Analysis Statistics</h2>
    <p><strong>Index Score:</strong> {score:.2f}</p>
    <p><strong>Total Patterns:</strong> {len(patterns)}</p>
    <p><strong>Pattern List:</strong> {', '.join(sorted(patterns))}</p>
"""

    # Add statistics tables
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
    
    # Close stats div
    html += "</div>"
    
    # Start three-column layout
    html += '<div class="three-column-layout">'
    
    # Function to generate table HTML
    def generate_table_html(df, title):
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
    
    # Close layout and HTML
    html += '</div></body></html>'
    
    return html

# Function to analyze all V-TRAC indexes for a state
def analyze_all_indexes(state_name):
    """Analyze all V-TRAC indexes for a state and rank them"""
    # Load tables for the state
    tables = load_state_tables(state_name)
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

# Function to generate HTML reports for top indexes
def generate_top_reports(state_name, results, top_n=3):
    """Generate HTML reports for top N ranked indexes"""
    if not results or len(results) == 0:
        return []
    
    # Load tables for the state
    tables = load_state_tables(state_name)
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

# Function to generate a summary chart for visualization
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

# --- ADD BACK STREAMLIT UI CODE (ensure error check is clear) ---
def main():
    st.set_page_config(
        page_title="V-TRAC Pattern Analyzer",
        page_icon="📊",
        layout="wide"
    )
    st.title("V-TRAC Pattern Analyzer")
    st.markdown("Analyze state data for optimal V-TRAC indexes and pattern predictions")
    
    # Select state
    # Use a default from STATES or ensure STATES is not empty
    default_state = STATES[0] if STATES else None 
    state = st.selectbox("Select State", STATES, index=STATES.index(default_state) if default_state in STATES else 0)
    
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
        tables = load_state_tables(state)
        if not tables:
            # More specific error message
            st.error(f"No table data loaded for {state}. Ensure data has been processed successfully via the main app (check 'data/outputs/tables/YYYY-MM-DD/{state}/').")
            return
        progress_bar.progress(25)
        
        status.info("Step 2/4: Analyzing all V-TRAC indexes...")
        results = analyze_all_indexes(state) # This function uses load_state_tables internally
        if not results:
            # Updated error message
            st.error(f"Analysis complete, but no V-TRAC indexes met the scoring criteria based on the loaded data for {state}. Try processing more historical data or checking the table generation.")
            return
        progress_bar.progress(50)
        
        status.info("Step 3/4: Generating HTML reports...")
        if top_n_reports > 0:
            reports = generate_top_reports(state, results, top_n_reports)
        else:
            reports = []
            st.info("HTML report generation skipped as requested.")
        progress_bar.progress(75)
        
        status.info("Step 4/4: Preparing visualization...")
        chart_image = generate_summary_chart(results, top_n_indexes)
        progress_bar.progress(100)
        
        status.success("Analysis complete!")
        
        if chart_image:
            st.subheader("V-TRAC Index Ranking")
            st.image(chart_image)
        
        st.subheader(f"Top {min(top_n_indexes, len(results))} V-TRAC Indexes for {state}")
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
        
        if reports:
            st.subheader(f"Top {len(reports)} HTML Reports")
            report_tabs = st.tabs([f"Rank #{r['rank']} (Index {r['index']})" for r in reports])
            for i, (tab, report) in enumerate(zip(report_tabs, reports)):
                with tab:
                    st.markdown(f"**V-TRAC Index: {report['index']}** - Score: {report['score']:.2f}")
                    col1_rep, col2_rep = st.columns(2)
                    with col1_rep:
                        report_file_path = Path(report['filepath']).resolve()
                        report_uri = report_file_path.as_uri()
                        if st.button(f"Open Report (Rank #{report['rank']})", key=f"open_{report['rank']}"):
                            webbrowser.open(report_uri)
                    with col2_rep:
                        st.download_button(
                            f"Download Report (Rank #{report['rank']})",
                            report['html'],
                            file_name=report['filename'],
                            mime="text/html",
                            key=f"download_{report['rank']}"
                        )
                    with st.expander(f"Preview Report (Rank #{report['rank']})", expanded=False):
                        st.components.v1.html(report['html'], height=600, scrolling=True)
        elif top_n_reports > 0:
            st.info("No HTML reports were generated (analysis might not have produced enough results).")

# --- ADD BACK ENTRY POINT ---
if __name__ == "__main__":
    main() 