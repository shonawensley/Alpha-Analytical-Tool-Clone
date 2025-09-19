#!/usr/bin/env python
"""
vtrac_test_app.py - Standalone Streamlit app for testing V-TRAC pattern matching

This test app allows:
1. Selecting a V-TRAC index from dropdown OR entering a winning number
2. Visualizing the V-TRAC pattern clusters (red and blue highlighting)
3. Testing the highlighting on sample data tables with proper formatting
"""

import os
import sys
import pandas as pd
import streamlit as st
from itertools import permutations

# Add script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import V-TRAC utilities
from utils.vtrac_utils import BOXED_VTRAC_REFERENCE
from vtrac.winner_highlighter import (
    get_all_permutations,
    get_vtrac_combinations,
    highlight_winners
)

# Set page config
st.set_page_config(
    page_title="V-TRAC Pattern Tester",
    page_icon="🎯",
    layout="wide"
)

# Page title
st.title("V-TRAC Pattern Matching Test Tool")
st.markdown("This tool helps visualize how V-TRAC pattern matching works for winner highlighting.")

# Create tabs
tabs = st.tabs(["Pattern Explorer", "Table Highlighting Test"])

# Create example data for testing - Combined tables like real outputs
def create_sample_tables():
    """Create sample tables with proper structure like real output tables"""
    # Combined table with all sets and draws
    combined_table = pd.DataFrame([
        # Set 1
        {"Set": "Set1", "Draw": "Draw1", "RowType": "R2", "7": "123456", "6": "12345", "5": "1234", "4": "123", "3": "12", "2": "1", "1": "0"},
        {"Set": "Set1", "Draw": "Draw1", "RowType": "Total", "7": "456123", "6": "45123", "5": "4123", "4": "413", "3": "41", "2": "4", "1": "0"},
        {"Set": "Set1", "Draw": "Draw2", "RowType": "R2", "7": "234567", "6": "23456", "5": "2345", "4": "234", "3": "23", "2": "2", "1": "1"},
        {"Set": "Set1", "Draw": "Draw2", "RowType": "Total", "7": "567234", "6": "56234", "5": "5234", "4": "524", "3": "52", "2": "5", "1": "2"},
        {"Set": "Set1", "Draw": "Draw3", "RowType": "R2", "7": "345678", "6": "34567", "5": "3456", "4": "345", "3": "34", "2": "3", "1": "1"},
        {"Set": "Set1", "Draw": "Draw3", "RowType": "Total", "7": "678345", "6": "67345", "5": "6345", "4": "635", "3": "63", "2": "6", "1": "1"},
        
        # Set 2
        {"Set": "Set2", "Draw": "Draw1", "RowType": "R2", "7": "456789", "6": "45678", "5": "4567", "4": "456", "3": "45", "2": "4", "1": "4"},
        {"Set": "Set2", "Draw": "Draw1", "RowType": "Total", "7": "789456", "6": "78456", "5": "7456", "4": "746", "3": "74", "2": "7", "1": "6"},
        {"Set": "Set2", "Draw": "Draw2", "RowType": "R2", "7": "567890", "6": "56789", "5": "5678", "4": "567", "3": "56", "2": "5", "1": "5"},
        {"Set": "Set2", "Draw": "Draw2", "RowType": "Total", "7": "890567", "6": "89567", "5": "8567", "4": "857", "3": "85", "2": "8", "1": "8"},
        
        # Set 3
        {"Set": "Set3", "Draw": "Draw1", "RowType": "R2", "7": "678901", "6": "67890", "5": "6789", "4": "678", "3": "67", "2": "6", "1": "5"},
        {"Set": "Set3", "Draw": "Draw1", "RowType": "Total", "7": "901678", "6": "90678", "5": "9678", "4": "968", "3": "96", "2": "9", "1": "9"},
    ])
    
    # Midday table (subset of combined)
    midday_table = combined_table.copy()
    
    # Evening table (subset of combined)
    evening_table = combined_table.copy()
    
    # R2-only tables
    r2_combined = combined_table[combined_table["RowType"] == "R2"].copy()
    r2_midday = midday_table[midday_table["RowType"] == "R2"].copy()
    r2_evening = evening_table[evening_table["RowType"] == "R2"].copy()
    
    return {
        "Combined": combined_table,
        "Midday": midday_table,
        "Evening": evening_table,
        "R2_Combined": r2_combined,
        "R2_Midday": r2_midday,
        "R2_Evening": r2_evening
    }

def apply_styling_to_table(df):
    """Apply section background colors to tables"""
    styled = df.style.apply(lambda x: [
        'background-color: rgba(31, 119, 180, 0.1)' if x['Set'] == 'Set3'
        else 'background-color: rgba(44, 160, 44, 0.1)' if x['Set'] == 'Set2'
        else 'background-color: rgba(255, 127, 14, 0.1)' if (x['Set'] == 'Set1' and x['Draw'] == 'Draw1')
        else '' for _ in range(len(x))
    ], axis=1)
    
    return styled.set_properties(**{
        'text-align': 'center',
        'font-family': 'monospace',
        'white-space': 'nowrap',
        'padding': '8px'
    })

# Tab 1: Pattern Explorer
with tabs[0]:
    st.header("Explore V-TRAC Pattern Clusters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Input options
        st.subheader("Input Options")
        
        input_method = st.radio(
            "Select Input Method",
            ["Enter Winning Number", "Select V-TRAC Index"]
        )
        
        selected_index = None
        winning_number = None
        
        if input_method == "Enter Winning Number":
            winning_number = st.text_input(
                "Enter 3-digit Winning Number",
                value="123",
                max_chars=3
            )
        else:
            vtrac_indices = [entry["Index"] for entry in BOXED_VTRAC_REFERENCE]
            selected_index = st.selectbox(
                "Select V-TRAC Index",
                options=vtrac_indices
            )
    
    # Get pattern data based on input
    pattern_data = None
    exact_matches = set()
    related_combos = set()
    
    if winning_number and len(winning_number) == 3 and winning_number.isdigit():
        exact_matches, related_combos = get_vtrac_combinations(winning_number)
        
        # Find the V-TRAC index for display
        for vtrac_entry in BOXED_VTRAC_REFERENCE:
            all_combos = set()
            all_combos.update(vtrac_entry.get("Singles", []))
            all_combos.update(vtrac_entry.get("Doubles", []))
            
            if winning_number in all_combos:
                pattern_data = vtrac_entry
                break
    
    elif selected_index is not None:
        # Get data from selected index
        pattern_data = next((item for item in BOXED_VTRAC_REFERENCE if item["Index"] == selected_index), None)
        
        if pattern_data:
            # Use first pattern as sample winning number if available
            all_patterns = pattern_data.get("Singles", []) + pattern_data.get("Doubles", [])
            if all_patterns:
                sample_winner = all_patterns[0]
                exact_matches, related_combos = get_vtrac_combinations(sample_winner)
    
    # Display the pattern data
    with col2:
        if pattern_data:
            st.subheader(f"V-TRAC Index {pattern_data['Index']}")
            
            # Show the index patterns
            st.markdown("**Singles Patterns:**")
            singles = pattern_data.get("Singles", [])
            if singles:
                singles_chunks = [singles[i:i+6] for i in range(0, len(singles), 6)]
                for chunk in singles_chunks:
                    st.write(' '.join(chunk))
            else:
                st.write("No singles patterns in this index")
                
            st.markdown("**Doubles Patterns:**")
            doubles = pattern_data.get("Doubles", [])
            if doubles:
                doubles_chunks = [doubles[i:i+6] for i in range(0, len(doubles), 6)]
                for chunk in doubles_chunks:
                    st.write(' '.join(chunk))
            else:
                st.write("No doubles patterns in this index")
    
    # Display highlighted combinations
    st.markdown("---")
    st.subheader("Highlighted Combinations")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**Winning Combinations (RED):**")
        st.markdown('<div style="color: red; font-weight: bold">' + 
                    ' '.join(sorted(exact_matches)) + 
                    '</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown("**Related Combinations (BLUE):**")
        st.markdown('<div style="color: blue">' + 
                    ' '.join(sorted(related_combos)) + 
                    '</div>', unsafe_allow_html=True)
        
    # Display pattern summary
    st.markdown("---")
    st.markdown(f"**Total Patterns:** {len(exact_matches) + len(related_combos)}")
    st.markdown(f"**Winners (RED):** {len(exact_matches)}")
    st.markdown(f"**Related (BLUE):** {len(related_combos)}")

# Tab 2: Table Highlighting Test
with tabs[1]:
    st.header("Test Highlighting on Sample Tables")
    
    # Input for winning number(s)
    col1, col2 = st.columns(2)
    
    with col1:
        midday_winner = st.text_input(
            "Enter Midday Winning Number",
            value="123",
            max_chars=3,
            help="3-digit number for midday highlighting"
        )
    
    with col2:
        evening_winner = st.text_input(
            "Enter Evening Winning Number",
            value="456",
            max_chars=3,
            help="3-digit number for evening highlighting"
        )
    
    # Create sample tables
    sample_tables = create_sample_tables()
    
    # Apply highlighting if valid input
    highlighted_tables = {}
    
    if (midday_winner and len(midday_winner) == 3 and midday_winner.isdigit()) or \
       (evening_winner and len(evening_winner) == 3 and evening_winner.isdigit()):
        
        # Show winning patterns
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("**Midday Winning Patterns:**")
            if midday_winner and len(midday_winner) == 3 and midday_winner.isdigit():
                exact_midday, related_midday = get_vtrac_combinations(midday_winner)
                st.markdown('<div style="color: red; font-weight: bold">RED: ' + 
                            ' '.join(sorted(exact_midday)) + 
                            '</div>', unsafe_allow_html=True)
                st.markdown('<div style="color: blue">BLUE: ' + 
                            ' '.join(sorted(list(related_midday)[:10])) + 
                            f'... ({len(related_midday)} total)</div>', unsafe_allow_html=True)
            else:
                st.write("No midday winner specified")
        
        with col4:
            st.markdown("**Evening Winning Patterns:**")
            if evening_winner and len(evening_winner) == 3 and evening_winner.isdigit():
                exact_evening, related_evening = get_vtrac_combinations(evening_winner)
                st.markdown('<div style="color: red; font-weight: bold">RED: ' + 
                            ' '.join(sorted(exact_evening)) + 
                            '</div>', unsafe_allow_html=True)
                st.markdown('<div style="color: blue">BLUE: ' + 
                            ' '.join(sorted(list(related_evening)[:10])) + 
                            f'... ({len(related_evening)} total)</div>', unsafe_allow_html=True)
            else:
                st.write("No evening winner specified")
        
        # Apply highlighting to each table
        for table_name, table_df in sample_tables.items():
            highlighted_df = table_df.copy()
            
            # Apply styling based on table type
            if "Midday" in table_name and midday_winner:
                highlighted_df = highlight_winners(highlighted_df, midday_winner)
            elif "Evening" in table_name and evening_winner:
                highlighted_df = highlight_winners(highlighted_df, evening_winner)
            elif "Combined" in table_name:
                # For combined tables, apply both highlights
                if midday_winner:
                    highlighted_df = highlight_winners(highlighted_df, midday_winner)
                if evening_winner:
                    # Second pass with evening winner
                    highlighted_df = highlight_winners(highlighted_df, evening_winner)
            
            highlighted_tables[table_name] = highlighted_df
    
    # Table viewer with sections for Combined, R2, Midday and Evening
    st.markdown("---")
    main_tabs = st.tabs(["Combined Tables", "R2-Only Tables", "Midday Tables", "Evening Tables"])
    
    # Tab 1: Combined Tables
    with main_tabs[0]:
        if "Combined" in highlighted_tables:
            st.subheader("Combined Table (All Sets, All Draws)")
            st.write(highlighted_tables["Combined"].to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.write("Enter valid winning numbers to see highlighted combined table")
    
    # Tab 2: R2-Only Tables
    with main_tabs[1]:
        if "R2_Combined" in highlighted_tables:
            st.subheader("R2-Only Combined Table")
            st.write(highlighted_tables["R2_Combined"].to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.write("Enter valid winning numbers to see highlighted R2-only table")
    
    # Tab 3: Midday Tables
    with main_tabs[2]:
        if "Midday" in highlighted_tables:
            st.subheader("Midday Table")
            st.write(highlighted_tables["Midday"].to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.write("Enter valid winning numbers to see highlighted midday table")
    
    # Tab 4: Evening Tables
    with main_tabs[3]:
        if "Evening" in highlighted_tables:
            st.subheader("Evening Table")
            st.write(highlighted_tables["Evening"].to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.write("Enter valid winning numbers to see highlighted evening table")
    
    # Explanation of highlighting
    st.markdown("---")
    st.info("""
    **Highlighting Logic:**
    - RED: Exact matches of the winning number and its permutations
    - BLUE: Related combinations from the same V-TRAC index
    
    This follows the same V-TRAC pattern matching system used in the main application.
    """)

# Footer
st.markdown("---")
st.markdown("**V-TRAC Pattern Matching Test Tool** - *This is a separate testing environment that doesn't affect the main application*") 