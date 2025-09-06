"""
test_vtrac_app.py

A comprehensive Streamlit app that demonstrates all the V-TRAC analyzer features,
specifically designed to test the implementation before integrating with the main app.
"""

import os
import sys
import pandas as pd
import streamlit as st
from datetime import datetime

# Add parent directory to path to import other modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
project_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(project_dir)

# Import our modules
from auxiliary.draw_extractor import get_state_columns, load_draw_data, extract_state_draws, get_all_state_draws
from auxiliary.pair_analysis import calculate_overdue_pairs, get_top_overdue_repeating_pairs, combos_in_last_1000
from auxiliary.vtrac_display import generate_vtrac_display, format_pairs_display
from auxiliary.combined_view import build_combined_ranking, generate_dryness_html_table

# Page configuration
st.set_page_config(
    page_title="V-TRAC Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get Excel file path
def get_excel_path():
    """Find the Pick3StatsC4.xlsm file in the standard data folder."""
    excel_path = os.path.join(project_dir, "data", "original", "Pick3StatsC4.xlsm")
    if not os.path.exists(excel_path):
        return None
    return excel_path

def main():
    st.title("V-TRAC Analyzer")
    st.write("This app demonstrates the analysis features: overdue pairs, V-TRAC table with sum-root, and state rankings.")
    
    # Excel file selection
    excel_path = get_excel_path()
    if not excel_path:
        st.error("Excel file not found in the standard location. Please check the data/original folder.")
        return
        
    st.sidebar.info(f"Using Excel file: {os.path.basename(excel_path)}")
    
    # Load the dataframe first
    try:
        df = load_draw_data(excel_path)
        if df is None:
            st.error("Failed to load Excel file. Please check that it exists and has the proper format.")
            return
            
        # Get state columns from the mappings
        state_cols = get_state_columns(df)
        available_states = list(state_cols.keys())
        
        if not available_states:
            st.error("No states defined in the state mapping.")
            return
        
        # Create tabs for different analyses
        tab1, tab2, tab3 = st.tabs(["V-TRAC Analysis", "Pair Analysis", "Combined Analysis"])
        
        # Tab 1: V-TRAC Table
        with tab1:
            st.header("V-TRAC Analysis")
            
            selected_state = st.selectbox(
                "Select State to Analyze",
                available_states,
                key="state_selector_1"
            )
            
            max_draws = st.slider(
                "Number of Draws for Analysis",
                min_value=200,
                max_value=1000,
                value=1000,
                step=100,
                key="max_draws_1"
            )
            
            if st.button("Generate V-TRAC Table", key="vtrac_button"):
                with st.spinner("Generating V-TRAC table..."):
                    # Get the draws
                    state_col = state_cols[selected_state]
                    draws = extract_state_draws(df, state_col, max_draws=max_draws)
                    
                    if not draws:
                        st.error(f"No draw data found for {selected_state}")
                        return
                    
                    # Generate the V-TRAC table
                    vtrac_html = generate_vtrac_display(draws)
                    
                    # Display top 5 most overdue repeating pairs first
                    st.subheader("Top 5 Most Overdue Repeating Pairs")
                    top_pairs = get_top_overdue_repeating_pairs(draws, 5)
                    
                    if top_pairs:
                        for i, (pair, draws_since) in enumerate(top_pairs, 1):
                            st.markdown(f"**{i}. {pair} - {draws_since} draws overdue**")
                    else:
                        st.write("No repeating pairs found")
                    
                    # Display HTML
                    st.subheader(f"V-TRAC Table for {selected_state}")
                    st.markdown("""
                    **V-Trac Analysis**  
                    - Combinations with sum-root sum in parentheses: 123(6-6)
                    - <u>Underlined</u> combinations haven't appeared in the draws
                    - Colored combinations contain overdue pairs:
                      - <span style='color: red'>RED</span> (late)
                      - <span style='color: blue'>BLUE</span> (very late)
                      - <span style='color: purple'>PURPLE</span> (pending)
                    """)
                    
                    st.components.v1.html(vtrac_html, height=800, scrolling=True)
                    
                    # Show some stats about the last 1000 draws
                    last_1000 = combos_in_last_1000(draws)
                    st.write(f"Total unique combinations seen in draws: {len(last_1000)}/1000 ({len(last_1000)/10:.1f}%)")
        
        # Tab 2: Overdue Pairs Analysis
        with tab2:
            st.header("Pair Analysis")
            
            selected_state_2 = st.selectbox(
                "Select State to Analyze",
                available_states,
                key="state_selector_2"
            )
            
            max_draws_2 = st.slider(
                "Number of Draws to Analyze",
                min_value=50,
                max_value=500,
                value=200,
                step=50,
                key="max_draws_2"
            )
            
            if st.button("Analyze Pairs", key="analyze_pairs_button"):
                with st.spinner("Analyzing pairs..."):
                    # Get the draws
                    state_col = state_cols[selected_state_2]
                    draws = extract_state_draws(df, state_col, max_draws=max_draws_2)
                    
                    if not draws:
                        st.error(f"No draw data found for {selected_state_2}")
                        return
                    
                    # Show raw draw data sample
                    st.subheader(f"Recent Draws for {selected_state_2}")
                    draws_df = pd.DataFrame(draws[:10], columns=["Date", "Draw"])
                    st.dataframe(draws_df)
                    
                    # Calculate overdue pairs
                    non_repeating, repeating, pair_status = calculate_overdue_pairs(draws)
                    
                    # Display results
                    st.subheader("Pair Analysis Results")
                    
                    # Generate HTML for pair display
                    pairs_html = format_pairs_display(non_repeating, repeating, pair_status)
                    st.components.v1.html(pairs_html, height=600, scrolling=True)
                    
                    # Top 5 most overdue repeating pairs
                    st.subheader("Top 5 Most Overdue Repeating Pairs")
                    top_pairs = get_top_overdue_repeating_pairs(draws, 5)
                    
                    if top_pairs:
                        for i, (pair, draws_since) in enumerate(top_pairs, 1):
                            st.markdown(f"**{i}. {pair} - {draws_since} draws overdue**")
                    else:
                        st.write("No repeating pairs found")
        
        # Tab 3: State Rankings
        with tab3:
            st.header("Combined State Analysis")
            
            max_draws_3 = st.slider(
                "Number of Draws for Analysis",
                min_value=50,
                max_value=500,
                value=200,
                step=50,
                key="max_draws_3"
            )
            
            if st.button("Generate State Rankings", key="rankings_button"):
                with st.spinner("Generating state rankings..."):
                    # Get all state draws
                    all_state_draws = {}
                    
                    for state, col in state_cols.items():
                        draws = extract_state_draws(df, col, max_draws=max_draws_3)
                        if draws:
                            all_state_draws[state] = draws
                    
                    if not all_state_draws:
                        st.error("No draw data found for any state")
                        return
                    
                    # Generate rankings table
                    rankings_html = generate_dryness_html_table(all_state_draws)
                    
                    # Display HTML
                    st.components.v1.html(rankings_html, height=600, scrolling=True)
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main() 