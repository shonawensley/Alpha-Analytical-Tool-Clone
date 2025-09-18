#!/usr/bin/env python3
"""
A minimal test app that shows the V-TRAC table with only the known working states.
"""

import os
import sys
import streamlit as st
import pandas as pd
from pathlib import Path

# Add project root to path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, "../.."))
sys.path.append(project_root)

# Import necessary functions
from scripts.auxiliary.vtrac_display import generate_vtrac_display, format_pairs_display
from scripts.auxiliary.pair_analysis import calculate_overdue_pairs, combos_in_last_1000

# Set page config
st.set_page_config(
    page_title="V-TRAC Simple Test",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define a list of KNOWN working states (correct sheet names)
WORKING_STATES = ["PuertoRico4", "Pennsylvania4", "Florida4", "NorthCarolina4"]

# Find Excel file
def find_excel_file(directory):
    """Find the Excel file in the directory"""
    for filename in os.listdir(directory):
        if filename.endswith(".xlsm") and "Pick3StatsC4" in filename:
            return os.path.join(directory, filename)
    return None

# Extract draws function using pandas
def extract_state_draws(excel_path, state_name):
    """Extract draws for a state directly from the Excel file"""
    try:
        # Read the Excel sheet
        df = pd.read_excel(excel_path, sheet_name=state_name)
        
        # Get the first two columns (usually date and draw)
        # This is the part that works with the actual Excel structure
        date_col = df.columns[0]
        draw_col = df.columns[1]
        
        # Create a list of (date, draw) tuples
        draws = []
        for _, row in df.iterrows():
            date_val = row[date_col]
            draw_val = row[draw_col]
            
            # Ensure draw is 3 digits
            if pd.notna(date_val) and pd.notna(draw_val):
                draw_str = str(int(draw_val)).zfill(3)
                draws.append((date_val, draw_str))
        
        return draws
    except Exception as e:
        st.error(f"Error extracting data for {state_name}: {str(e)}")
        return []

# Run the app
def main():
    st.title("V-TRAC Simple Test")
    st.subheader("Shows the V-TRAC table for states known to work")
    
    # Check for Excel file
    data_dir = os.path.join(project_root, "data", "original")
    excel_path = find_excel_file(data_dir)
    
    if not excel_path:
        st.error("Excel file not found. Please ensure 'Pick3StatsC4.xlsm' is in the data/original folder.")
        return
    
    st.success(f"Found Excel file: {os.path.basename(excel_path)}")
    
    # Select state from only the working ones
    selected_state = st.selectbox("Select a state to analyze", WORKING_STATES)
    
    # Simple tabbed interface
    tabs = st.tabs(["V-TRAC Table", "Pair Analysis"])
    
    with tabs[0]:
        st.write("Click the button below to generate the V-TRAC table for the selected state.")
        
        if st.button("Generate V-TRAC Table"):
            # Load draws for the selected state
            with st.spinner(f"Loading draws for {selected_state}..."):
                draws = extract_state_draws(excel_path, selected_state)
                
                if not draws:
                    st.warning(f"No draws found for {selected_state}.")
                else:
                    st.success(f"Loaded {len(draws)} draws.")
                    
                    # Generate and display the V-TRAC table
                    with st.spinner("Generating V-TRAC table..."):
                        html = generate_vtrac_display(draws)
                        st.components.v1.html(html, height=600, scrolling=True)
    
    with tabs[1]:
        st.write("Click the button below to analyze pair frequencies.")
        
        if st.button("Analyze Pairs"):
            # Load draws for the selected state
            with st.spinner(f"Loading draws for {selected_state}..."):
                draws = extract_state_draws(excel_path, selected_state)
                
                if not draws:
                    st.warning(f"No draws found for {selected_state}.")
                else:
                    st.success(f"Loaded {len(draws)} draws.")
                    
                    # Generate and display the pair analysis
                    with st.spinner("Analyzing pairs..."):
                        non_repeating, repeating, pair_status = calculate_overdue_pairs(draws)
                        html = format_pairs_display(non_repeating, repeating, pair_status)
                        st.components.v1.html(html, height=600, scrolling=True)

if __name__ == "__main__":
    main() 