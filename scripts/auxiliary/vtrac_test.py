#!/usr/bin/env python3
"""
vtrac_test.py

A minimal test app to verify that the V-TRAC table displays correctly without freezing.
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

# Import necessary functions - use the correct paths that worked before
from scripts.auxiliary.vtrac_display import generate_vtrac_display, format_pairs_display
from scripts.auxiliary.pair_analysis import calculate_overdue_pairs, combos_in_last_1000

# Add scripts to path to ensure imports work correctly
scripts_dir = os.path.join(project_root, "scripts")
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)

# Set page config
st.set_page_config(
    page_title="V-TRAC Display Test",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Use direct file access approach that worked before
def find_excel_file(directory):
    """Find the Excel file in the directory"""
    for filename in os.listdir(directory):
        if filename.endswith(".xlsm") and "Pick3StatsC4" in filename:
            return os.path.join(directory, filename)
    return None

def extract_state_draws(excel_path, state_name):
    """Extract draws for a state from the Excel file"""
    import pandas as pd
    
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path, sheet_name=state_name)
        
        # Extract date and draw columns
        date_col = df.columns[0]  # First column is usually date
        draw_col = df.columns[1]  # Second column is usually draw
        
        # Create list of (date, draw) tuples
        draws = []
        for _, row in df.iterrows():
            date = row[date_col]
            draw = str(row[draw_col]).zfill(3)  # Ensure 3 digits
            if pd.notna(date) and pd.notna(draw):
                draws.append((date, draw))
        
        return draws
    except Exception as e:
        print(f"Error extracting data for {state_name}: {e}")
        return []

@st.cache_data(ttl=3600)
def get_excel_path():
    """Get the path to the Excel file"""
    # Check for Excel file in the correct location
    data_dir = os.path.join(project_root, "data", "original")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        return None
    
    excel_path = find_excel_file(data_dir)
    if not excel_path:
        return None
    
    return excel_path

@st.cache_data(ttl=3600, show_spinner=False)
def get_draws_for_state(state_name):
    """Get the draws for a state using caching to improve performance"""
    excel_path = get_excel_path()
    if not excel_path:
        return None, "Excel file not found"
    
    try:
        draws = extract_state_draws(excel_path, state_name)
        if not draws:
            return None, f"No draws found for {state_name}"
        return draws, None
    except Exception as e:
        return None, f"Error: {str(e)}"

@st.cache_data(ttl=3600, show_spinner=False)
def generate_vtrac_display_cached(draws_list):
    """Generate the V-TRAC display with caching to improve performance"""
    try:
        html = generate_vtrac_display(draws_list)
        return html, None
    except Exception as e:
        return None, f"Error generating V-TRAC display: {str(e)}"

@st.cache_data(ttl=3600, show_spinner=False)
def generate_pairs_display_cached(draws_list):
    """Generate the pairs display with caching to improve performance"""
    try:
        non_repeating, repeating, pair_status = calculate_overdue_pairs(draws_list)
        html = format_pairs_display(non_repeating, repeating, pair_status)
        return html, None
    except Exception as e:
        return None, f"Error generating pairs display: {str(e)}"

def main():
    """Main function for the test app"""
    st.title("V-TRAC Display Test")
    st.markdown("""
    This is a simplified test application to verify that the V-TRAC table displays correctly without freezing.
    """)
    
    # Check for Excel file
    excel_path = get_excel_path()
    if not excel_path:
        st.error("Excel file not found. Please ensure 'Pick3StatsC4.xlsm' is in the data/original folder.")
        return
    
    st.success(f"Found Excel file: {os.path.basename(excel_path)}")
    
    # Select state
    state_options = [
        "Pennsylvania3", "NewJersey3", "NewYork3", "Delaware3", "Connecticut3",
        "Florida3", "Illinois3", "Maryland3", "Michigan3", "NorthCarolina3",
        "Ohio3", "Virginia3", "SouthCarolina3", "Washington3",
        "Pennsylvania4", "NewJersey4", "NewYork4", "Delaware4", "Connecticut4",
        "Florida4", "Illinois4", "Maryland4", "Michigan4", "NorthCarolina4",
        "Ohio4", "Virginia4", "SouthCarolina4", "Washington4", "PuertoRico4"
    ]
    
    selected_state = st.selectbox("Select a state to analyze", state_options)
    
    # Create tabs
    tabs = st.tabs(["V-TRAC Table", "Pair Analysis", "About"])
    
    with tabs[0]:
        st.subheader("V-TRAC Table Display")
        st.markdown("""
        This table shows all V-TRAC pattern combinations with:
        - **Underlining**: Combinations not seen in the last 1000 draws
        - **Color coding**: Based on pair status (RED = late, BLUE = very late, PURPLE = pending)
        """)
        
        if st.button("Generate V-TRAC Table"):
            with st.spinner("Loading draws..."):
                draws, error = get_draws_for_state(selected_state)
                
                if error:
                    st.error(error)
                elif not draws:
                    st.warning(f"No draws found for {selected_state}")
                else:
                    st.success(f"Loaded {len(draws)} draws for {selected_state}")
                    
                    with st.spinner("Generating V-TRAC table..."):
                        html, error = generate_vtrac_display_cached(draws)
                        
                        if error:
                            st.error(error)
                        else:
                            st.components.v1.html(html, height=600, scrolling=True)
    
    with tabs[1]:
        st.subheader("Pair Analysis")
        st.markdown("""
        This analysis shows pairs that are overdue:
        - **RED**: Late pairs
        - **BLUE**: Very late pairs 
        - **PURPLE**: Pending pairs
        """)
        
        if st.button("Generate Pair Analysis"):
            with st.spinner("Loading draws..."):
                draws, error = get_draws_for_state(selected_state)
                
                if error:
                    st.error(error)
                elif not draws:
                    st.warning(f"No draws found for {selected_state}")
                else:
                    st.success(f"Loaded {len(draws)} draws for {selected_state}")
                    
                    with st.spinner("Generating pair analysis..."):
                        html, error = generate_pairs_display_cached(draws)
                        
                        if error:
                            st.error(error)
                        else:
                            st.components.v1.html(html, height=600, scrolling=True)
    
    with tabs[2]:
        st.subheader("About this Test App")
        st.markdown("""
        This test application was created to verify that the V-TRAC table displays correctly without freezing.
        
        It includes:
        - Streamlit caching to improve performance
        - Error handling to prevent crashes
        - Simplified HTML generation for better performance
        - Limited display options to focus on key functionality
        
        The V-TRAC table shows all possible boxed combinations organized by index. Each combination is:
        - Colored according to the status of its digit pairs
        - Underlined if it hasn't appeared in the last 1000 draws
        """)

if __name__ == "__main__":
    main() 