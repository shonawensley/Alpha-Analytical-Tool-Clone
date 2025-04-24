#!/usr/bin/env python
"""
vtrac_html_test.py - Generate HTML files with V-TRAC pattern highlighting

This script:
1. Creates sample data tables that match the real data format
2. Applies V-TRAC pattern highlighting (red for winners, blue for related)
3. Generates HTML with the exact 3-column layout from the examples
4. Preserves the complete dataset structure without manipulation
"""

import os
import sys
import pandas as pd
import streamlit as st
from itertools import permutations
from datetime import datetime
import time
import tempfile
import webbrowser
from pathlib import Path

# Add script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import V-TRAC utilities
from utils.vtrac_utils import BOXED_VTRAC_REFERENCE

# Set page config
st.set_page_config(
    page_title="V-TRAC Pattern HTML Generator",
    page_icon="🎯",
    layout="wide"
)

# Function to get all permutations of a number
def get_all_permutations(number):
    """Get all permutations of a 3-digit number"""
    number = str(number).zfill(3)
    digits = list(number)
    return set(''.join(p) for p in permutations(digits))

# Function to get V-TRAC combinations
def get_vtrac_combinations(number):
    """Get winner and related pattern sets from V-TRAC reference"""
    number = str(number).zfill(3)
    winning_perms = get_all_permutations(number)
    related_combos = set()
    
    for vtrac_entry in BOXED_VTRAC_REFERENCE:
        all_combos = set()
        all_combos.update(vtrac_entry.get("Singles", []))
        all_combos.update(vtrac_entry.get("Doubles", []))
        
        if number in all_combos:
            related_combos = set(all_combos) - winning_perms
            break
            
    return winning_perms, related_combos

# Generate HTML template that matches the example files
def generate_html_template(state_name, winning_number, timestamp=None):
    """Generate HTML template with header, styling, and layout"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Get V-TRAC patterns
    winning_patterns, related_patterns = get_vtrac_combinations(winning_number)
    
    # Format winning and related patterns for display
    winning_patterns_str = ', '.join(sorted(winning_patterns))
    related_patterns_str = ', '.join(sorted(related_patterns))
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Pattern Analysis</title>
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
        .winning {{
            color: #ff0000;
            font-weight: 800;
        }}
        .pattern {{
            color: #0000ff;
            font-weight: 800;
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
    </style>
</head>
<body>
<div class="version">Version: v{timestamp}</div>
<div class="three-column-layout">
"""
    return html, winning_patterns, related_patterns

# Function to create sample data that matches real data structure
def create_sample_data(state_name="SampleState4"):
    """Create sample data tables that match the real format"""
    # Sample DRAW_DATA
    sample_draws = {
        "Midday": [
            {"Set": "Set3", "Draw": "Draw1", "row": ["912", "437", "894", "258", "663", "502", "643"]},
            {"Set": "Set2", "Draw": "Draw1", "row": ["437", "894", "258", "663", "502", "643", "064"]},
            {"Set": "Set1", "Draw": "Draw1", "row": ["894", "258", "663", "502", "643", "064", "058"]}
        ],
        "Evening": [
            {"Set": "Set3", "Draw": "Draw1", "row": ["585", "325", "339", "076", "845", "020", "270"]},
            {"Set": "Set2", "Draw": "Draw1", "row": ["325", "339", "076", "845", "020", "270", "074"]},
            {"Set": "Set1", "Draw": "Draw1", "row": ["339", "076", "845", "020", "270", "074", "478"]}
        ]
    }
    
    # Create full tables with R2, R4, R6, R8 rows
    tables = {section: [] for section in ["Midday", "Evening", "Combined"]}
    
    # Generate the Midday and Evening tables
    for section, draw_data in sample_draws.items():
        for draw in draw_data:
            # DRAW_DATA row
            tables[section].append({
                "Set": draw["Set"],
                "Draw": draw["Draw"],
                "RowType": "DRAW_DATA",
                "7": draw["row"][0],
                "6": draw["row"][1],
                "5": draw["row"][2],
                "4": draw["row"][3],
                "3": draw["row"][4],
                "2": draw["row"][5],
                "1": draw["row"][6]
            })
            
            # R2 row
            tables[section].append({
                "Set": draw["Set"],
                "Draw": draw["Draw"],
                "RowType": "R2",
                "7": f"55240388{generate_three_digits()}",
                "6": f"55208{generate_three_digits()}",
                "5": f"5520{generate_three_digits()}",
                "4": f"50{generate_three_digits()}",
                "3": f"{generate_three_digits()}",
                "2": f"{generate_one_digit()}",
                "1": f"{generate_one_digit()}"
            })
            
            # R4 row
            tables[section].append({
                "Set": draw["Set"],
                "Draw": draw["Draw"],
                "RowType": "R4",
                "7": f"2{generate_three_digits()}6{generate_three_digits()}",
                "6": f"2{generate_three_digits()}6{generate_three_digits()}",
                "5": f"{generate_three_digits()}6{generate_three_digits()}",
                "4": f"{generate_three_digits()}{generate_one_digit()}",
                "3": f"{generate_three_digits()}",
                "2": f"{generate_one_digit()}",
                "1": f"{generate_one_digit()}"
            })
            
            # R6 row
            tables[section].append({
                "Set": draw["Set"],
                "Draw": draw["Draw"],
                "RowType": "R6",
                "7": f"{generate_three_digits()}{generate_three_digits()}24",
                "6": f"{generate_three_digits()}{generate_three_digits()}{generate_one_digit()}",
                "5": f"{generate_three_digits()}0{generate_three_digits()}{generate_one_digit()}",
                "4": f"{generate_three_digits()}0{generate_one_digit()}",
                "3": f"{generate_three_digits()}",
                "2": f"{generate_one_digit()}",
                "1": f"{generate_one_digit()}"
            })
            
            # R8 row
            tables[section].append({
                "Set": draw["Set"],
                "Draw": draw["Draw"],
                "RowType": "R8",
                "7": f"{generate_three_digits()}{generate_three_digits()}{generate_three_digits()}",
                "6": f"{generate_three_digits()}{generate_three_digits()}{generate_three_digits()}",
                "5": f"{generate_three_digits()}{generate_three_digits()}{generate_one_digit()}",
                "4": f"{generate_three_digits()}{generate_one_digit()}{generate_one_digit()}",
                "3": f"{generate_three_digits()}",
                "2": f"{generate_one_digit()}",
                "1": f"{generate_one_digit()}"
            })
    
    # Generate the Combined table (simplified version for sample)
    tables["Combined"] = [
        # Set 3
        {"Set": "Set3", "Draw": "Draw1", "RowType": "DRAW_DATA", "7": "845", "6": "502", "5": "020", "4": "643", "3": "270", "2": "064", "1": "074"},
        {"Set": "Set3", "Draw": "Draw1", "RowType": "R2", "7": f"599224011387", "6": f"992411387", "5": f"99411387", "4": f"991187", "3": f"99118", "2": f"99118", "1": f"99118"},
        {"Set": "Set3", "Draw": "Draw1", "RowType": "R4", "7": f"225990834711", "6": f"299834711", "5": f"99834711", "4": f"998711", "3": f"99811", "2": f"99811", "1": f"99811"},
        {"Set": "Set3", "Draw": "Draw1", "RowType": "R6", "7": f"8117059932", "6": f"81179932", "5": f"8117993", "4": f"811799", "3": f"81199", "2": f"81199", "1": f"81199"},
        {"Set": "Set3", "Draw": "Draw1", "RowType": "R8", "7": f"70119983245", "6": f"71199832", "5": f"7119983", "4": f"711998", "3": f"11998", "2": f"11998", "1": f"11998"},
        
        # Set 2
        {"Set": "Set2", "Draw": "Draw1", "RowType": "DRAW_DATA", "7": "502", "6": "020", "5": "643", "4": "270", "3": "064", "2": "074", "1": "058"},
        {"Set": "Set2", "Draw": "Draw1", "RowType": "R2", "7": f"99240113877", "6": f"994113877", "5": f"9911877", "4": f"991187", "3": f"991187", "2": f"99118", "1": f"9911"},
        {"Set": "Set2", "Draw": "Draw1", "RowType": "R4", "7": f"29908347711", "6": f"998347711", "5": f"9987711", "4": f"998711", "3": f"998711", "2": f"99811", "1": f"9911"},
        {"Set": "Set2", "Draw": "Draw1", "RowType": "R6", "7": f"8117709932", "6": f"8117793", "5": f"811779", "4": f"81179", "3": f"8117", "2": f"8119", "1": f"119"},
        {"Set": "Set2", "Draw": "Draw1", "RowType": "R8", "7": f"770119983", "6": f"7711998", "5": f"771199", "4": f"71199", "3": f"7119", "2": f"1198", "1": f"119"},
        
        # Set 1
        {"Set": "Set1", "Draw": "Draw1", "RowType": "DRAW_DATA", "7": "020", "6": "643", "5": "270", "4": "064", "3": "074", "2": "058", "1": "478"},
        {"Set": "Set1", "Draw": "Draw1", "RowType": "R2", "7": f"994113386677", "6": f"991138677", "5": f"9911386", "4": f"991138", "3": f"99113", "2": f"9911", "1": f"991"},
        {"Set": "Set1", "Draw": "Draw1", "RowType": "R4", "7": f"9966833471", "6": f"996837711", "5": f"9968371", "4": f"998371", "3": f"99831", "2": f"9931", "1": f"993"},
        {"Set": "Set1", "Draw": "Draw1", "RowType": "R6", "7": f"668117799", "6": f"6811779", "5": f"681179", "4": f"81179", "3": f"8119", "2": f"119", "1": f"19"},
        {"Set": "Set1", "Draw": "Draw1", "RowType": "R8", "7": f"7711998366", "6": f"771199836", "5": f"7119983", "4": f"711998", "3": f"11998", "2": f"1199", "1": f"119"}
    ]
    
    # Convert to pandas DataFrames
    for section in tables:
        tables[section] = pd.DataFrame(tables[section])
    
    # Create R2-only tables
    r2_tables = {
        section: tables[section][tables[section]["RowType"] == "R2"] 
        for section in tables
    }
        
    return {
        "tables": tables,
        "r2_tables": r2_tables
    }

# Helper function to generate random 3-digit numbers (for sample data)
def generate_three_digits():
    import random
    return f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

# Helper function to generate random 1-digit numbers (for sample data)
def generate_one_digit():
    import random
    return f"{random.randint(0, 9)}"

# Apply highlighting to a value
def highlight_value(value, winning_patterns, related_patterns):
    """Apply HTML highlighting to a value based on pattern matches"""
    if not isinstance(value, str):
        return str(value)
    
    # Check for winning patterns
    for pattern in winning_patterns:
        if pattern in value:
            value = value.replace(pattern, f'<span class="winning">{pattern}</span>')
    
    # Check for related patterns
    for pattern in related_patterns:
        if pattern in value and f'<span class="winning">{pattern}</span>' not in value:
            value = value.replace(pattern, f'<span class="pattern">{pattern}</span>')
    
    return value

# Generate table HTML
def generate_table_html(df, title, winning_patterns, related_patterns):
    """Generate HTML for a table with pattern highlighting"""
    html = f"""
        <style>
            table {{
                border-collapse: collapse;
                margin: 20px 0;
                font-family: Arial, sans-serif;
                font-size: 14px;
                width: 100%;
                max-width: 1200px;
            }}
            th {{
                background-color: #f2f2f2;
                padding: 8px;
                font-weight: bold;
                text-align: center;
                border: 1px solid #000;
            }}
            td {{
                padding: 6px;
                border: 1px solid #000;
                text-align: center;
                font-weight: 400;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            .winning {{
                color: #ff0000;
                font-weight: 800;
            }}
            .pattern {{
                color: #0000ff;
                font-weight: 800;
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
        </style>
        <h2>{title}</h2>
<table>
<tr><th>Set</th><th>Draw</th><th>RowType</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th></tr>
"""
    
    for _, row in df.iterrows():
        html += "<tr>"
        for col in ["Set", "Draw", "RowType"]:
            html += f"<td>{row[col]}</td>"
        
        for col in ["7", "6", "5", "4", "3", "2", "1"]:
            highlighted_value = highlight_value(row[col], winning_patterns, related_patterns)
            html += f"<td>{highlighted_value}</td>"
        
        html += "</tr>\n"
    
    html += "</table>\n<br>\n"
    return html

# Generate a complete HTML file with all tables
def generate_full_html(state_name, winning_number, timestamp=None):
    """Generate complete HTML with all tables and highlighting"""
    html_template, winning_patterns, related_patterns = generate_html_template(
        state_name, winning_number, timestamp
    )
    
    # Create sample data
    data = create_sample_data(state_name)
    tables = data["tables"]
    r2_tables = data["r2_tables"]
    
    # Start building HTML
    html = html_template
    
    # Midday column
    html += '<div class="column">\n<h2>Midday Draw</h2>\n'
    html += generate_table_html(
        tables["Midday"], 
        f"{state_name} Midday Combined Table", 
        winning_patterns, 
        related_patterns
    )
    html += generate_table_html(
        r2_tables["Midday"], 
        f"{state_name} Midday R2-only Table", 
        winning_patterns, 
        related_patterns
    )
    html += '</div><!-- End column -->\n'
    
    # Evening column
    html += '<div class="column">\n<h2>Evening Draw</h2>\n'
    html += generate_table_html(
        tables["Evening"], 
        f"{state_name} Evening Combined Table", 
        winning_patterns, 
        related_patterns
    )
    html += generate_table_html(
        r2_tables["Evening"], 
        f"{state_name} Evening R2-only Table", 
        winning_patterns, 
        related_patterns
    )
    html += '</div><!-- End column -->\n'
    
    # Combined column
    html += '<div class="column">\n<h2>Combined Draw</h2>\n'
    html += generate_table_html(
        tables["Combined"], 
        f"{state_name} Combined Combined Table", 
        winning_patterns, 
        related_patterns
    )
    html += generate_table_html(
        r2_tables["Combined"], 
        f"{state_name} Combined R2-only Table", 
        winning_patterns, 
        related_patterns
    )
    html += '</div><!-- End column -->\n'
    
    # Close HTML
    html += '</div><!-- End three-column layout -->\n'
    html += '</body></html>'
    
    return html

# Streamlit app for generating the HTML
st.title("V-TRAC Pattern HTML Generator")
st.markdown("Generate HTML files with V-TRAC pattern highlighting that match the example format")

# Input fields
col1, col2 = st.columns(2)

with col1:
    state_name = st.selectbox(
        "Select State",
        ["Connecticut4", "Delaware4", "Florida4", "Indiana4", "Michigan4", 
         "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4", "OntarioCanada4", 
         "Pennsylvania4", "PuertoRico4", "SouthCarolina4", "Virginia4"]
    )

with col2:
    winning_number = st.text_input(
        "Enter 3-digit Winning Number",
        value="123",
        max_chars=3
    )

# Generate button
if st.button("Generate HTML"):
    if winning_number and len(winning_number) == 3 and winning_number.isdigit():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate HTML
        html_content = generate_full_html(state_name, winning_number, timestamp)
        
        # Save to file
        output_dir = os.path.join(os.path.dirname(script_dir), "outputs", "patterns")
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{state_name}_patterns_v{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        st.success(f"HTML file generated: {filepath}")
        
        # Open in browser option
        if st.button("Open in Browser"):
            webbrowser.open(f"file://{filepath}")
        
        # Show preview
        with st.expander("Preview HTML"):
            st.components.v1.html(html_content, height=600, scrolling=True)
    else:
        st.error("Please enter a valid 3-digit number")

# Also provide a test viewer for existing HTML files
st.markdown("---")
st.subheader("View Existing Pattern HTML Files")

# Find existing pattern HTML files
pattern_dir = os.path.join(os.path.dirname(script_dir), "docs", "EX. CLUSTER LOG OLD")
if os.path.exists(pattern_dir):
    pattern_files = [f for f in os.listdir(pattern_dir) if f.endswith(".html")]
    
    if pattern_files:
        selected_file = st.selectbox("Select Pattern File", pattern_files)
        
        if st.button("View Selected File"):
            filepath = os.path.join(pattern_dir, selected_file)
            with open(filepath, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            st.components.v1.html(html_content, height=600, scrolling=True)
    else:
        st.info("No pattern HTML files found in the docs/EX. CLUSTER LOG OLD directory")
else:
    st.info("docs/EX. CLUSTER LOG OLD directory not found") 