"""
Streamlit application for the Lottery Data Analysis Tool.
"""

import os
import sys
import json
import pandas as pd
import streamlit as st
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import modules
from modules.parse_excel import process_excel_file
from modules.analyze_pairs import (
    calculate_overdue_pairs,
    get_top_overdue_repeating_pairs,
    get_vtrac_statuses,
    get_doubles_history,
    get_colored_pairs,
    COLOR_LATE,
    COLOR_VERY_LATE,
    COLOR_PENDING
)
from modules.vtrac_reference import VTRAC_DISPLAY

# Set page configuration
st.set_page_config(
    page_title="Lottery Analysis Tool",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
THRESHOLD_LATE_NONREPEATING = 37  # Red for non-repeating pairs
THRESHOLD_LATE_REPEATING = 71     # Red for repeating pairs (doubles)
THRESHOLD_VERY_LATE_NONREPEATING = 56  # Blue for non-repeating pairs
THRESHOLD_VERY_LATE_REPEATING = 107    # Blue for repeating pairs
THRESHOLD_PENDING_LATE = 25       # Purple for any pairs

# Styling
st.markdown("""
<style>
    .red { color: red; font-weight: bold; }
    .blue { color: blue; font-weight: bold; }
    .purple { color: purple; font-weight: bold; }
    .underline { text-decoration: underline; }
    .red.underline { color: red; font-weight: bold; text-decoration: underline; }
    .blue.underline { color: blue; font-weight: bold; text-decoration: underline; }
    .purple.underline { color: purple; font-weight: bold; text-decoration: underline; }
    .header-container { display: flex; align-items: center; justify-content: space-between; }
    .header-title { font-size: 2rem; }
    .header-date { font-size: 1.2rem; color: #666; }
    .state-header { font-size: 1.8rem; color: #333; margin-bottom: 1rem; }
    .top-pairs-header { font-size: 1.4rem; color: #444; margin-top: 1rem; margin-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None
if 'last_upload_time' not in st.session_state:
    st.session_state.last_upload_time = None
if 'current_state' not in st.session_state:
    st.session_state.current_state = None

def process_file(uploaded_file):
    """Process the uploaded Excel file."""
    try:
        # Create directories if they don't exist
        os.makedirs("data/original", exist_ok=True)
        os.makedirs("data/cleaned", exist_ok=True)
        os.makedirs("data/outputs", exist_ok=True)
        
        # Save the uploaded file temporarily
        temp_file = os.path.normpath(os.path.join("data", "original", uploaded_file.name))
        
        with open(temp_file, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.info(f"Saved uploaded file to {temp_file}")
        
        # Get the analysis window size from session state or use default
        analysis_draws = st.session_state.get("analysis_draws", 100)
        
        # Process the file
        from run_process import run_process
        results = run_process(temp_file, max_draws=1000, analysis_draws=analysis_draws)
        
        # Store results in session state
        st.session_state.results = results
        st.session_state.last_upload_time = datetime.now()
        
        return True
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return False

def format_combo(combo: str, status_dict: Dict[str, Any], appeared: bool) -> str:
    """Format a combination string with appropriate styling."""
    if combo not in status_dict:
        return combo
    
    combo_status = status_dict[combo]
    
    # Determine CSS classes
    classes = []
    
    # Add color class if overdue
    if "color" in combo_status:
        classes.append(combo_status["color"])
    
    # Add underline if specified (hasn't appeared in 1000 draws)
    if "underline" in combo_status and combo_status["underline"]:
        classes.append("underline")
    
    # If no classes, return as-is
    if not classes:
        return combo
    
    # Join classes and format HTML
    class_str = " ".join(classes)
    return f'<span class="{class_str}">{combo}</span>'

def display_vtrac_table(state_data: Dict[str, Any]):
    """Display the V-Trac table for a state."""
    vtrac_statuses = state_data["vtrac_statuses"]
    
    # Create a DataFrame to display the table
    table_data = []
    
    for entry in VTRAC_DISPLAY:
        index = entry["Index"]
        status = vtrac_statuses.get(index, {})
        appeared = status.get("appeared", False)
        singles_status = status.get("singles_status", {})
        doubles_status = status.get("doubles_status", {})
        
        # Format singles
        singles = entry["Singles"]
        if singles:
            formatted_singles = " ".join([
                format_combo(combo, singles_status, appeared) 
                for combo in singles.split()
            ])
        else:
            formatted_singles = ""
        
        # Format doubles
        doubles = entry["Doubles"]
        if doubles:
            formatted_doubles = " ".join([
                format_combo(combo, doubles_status, appeared)
                for combo in doubles.split()
            ])
        else:
            formatted_doubles = ""
        
        # Add to table data
        table_data.append({
            "Index": index,
            "Singles": formatted_singles,
            "Doubles": formatted_doubles
        })
    
    # Convert to DataFrame and display
    df = pd.DataFrame(table_data)
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

def display_top_overdue_pairs(state_data: Dict[str, Any]):
    """Display the top 5 most overdue repeating pairs."""
    top_pairs = state_data["top_overdue_pairs"]
    
    st.markdown('<div class="top-pairs-header">Top 5 Most Overdue Repeating Pairs</div>', unsafe_allow_html=True)
    
    # Display each pair
    for pair, overdue in top_pairs:
        # Determine color
        if overdue >= THRESHOLD_VERY_LATE_REPEATING:
            color = "blue"
        elif overdue >= THRESHOLD_LATE_REPEATING:
            color = "red"
        elif overdue >= THRESHOLD_PENDING_LATE:
            color = "purple"
        else:
            color = ""
        
        # Format output
        if color:
            st.markdown(f'<span class="{color}">{pair} - {overdue} draws overdue</span>', unsafe_allow_html=True)
        else:
            st.write(f"{pair} - {overdue} draws overdue")

def display_state_page(state: str):
    """Display the analysis page for a specific state."""
    results = st.session_state.results
    
    if not results or state not in results:
        st.warning(f"No data available for {state}. Please upload an Excel file.")
        return
    
    state_data = results[state]
    
    # Display state header
    st.markdown(f'<div class="state-header">{state} Analysis</div>', unsafe_allow_html=True)
    
    # Display latest draws
    st.subheader("Latest Draws")
    if state_data["draws"]:
        latest_draws = state_data["draws"][:5]  # Show top 5
        df = pd.DataFrame({"Draw": latest_draws})
        st.dataframe(df)
    
    # Display colored pairs analysis
    st.subheader("Overdue Pairs Analysis")
    
    # Get the raw overdue data to separate repeating from non-repeating
    draws_100 = state_data["draws"][:100] if len(state_data["draws"]) >= 100 else state_data["draws"]
    non_repeating_overdue, repeating_overdue, pair_status = calculate_overdue_pairs(draws_100)
    
    # Separate repeating and non-repeating pairs with their colors
    repeating_red = []
    repeating_blue = []
    repeating_purple = []
    non_repeating_red = []
    non_repeating_blue = []
    non_repeating_purple = []
    
    for pair, overdue in repeating_overdue.items():
        if overdue >= THRESHOLD_VERY_LATE_REPEATING:
            repeating_blue.append(pair)
        elif overdue >= THRESHOLD_LATE_REPEATING:
            repeating_red.append(pair)
        elif overdue >= THRESHOLD_PENDING_LATE:
            repeating_purple.append(pair)
    
    for pair, overdue in non_repeating_overdue.items():
        if overdue >= THRESHOLD_VERY_LATE_NONREPEATING:
            non_repeating_blue.append(pair)
        elif overdue >= THRESHOLD_LATE_NONREPEATING:
            non_repeating_red.append(pair)
        elif overdue >= THRESHOLD_PENDING_LATE:
            non_repeating_purple.append(pair)
    
    # Sort all lists
    repeating_red.sort()
    repeating_blue.sort()
    repeating_purple.sort()
    non_repeating_red.sort()
    non_repeating_blue.sort()
    non_repeating_purple.sort()
    
    # First show threshold information
    st.info(f"""
    **Overdue Thresholds:**
    - Repeating pairs (00, 11, etc): RED={THRESHOLD_LATE_REPEATING}+, BLUE={THRESHOLD_VERY_LATE_REPEATING}+, PURPLE={THRESHOLD_PENDING_LATE}+
    - Non-repeating pairs (01, 23, etc): RED={THRESHOLD_LATE_NONREPEATING}+, BLUE={THRESHOLD_VERY_LATE_NONREPEATING}+, PURPLE={THRESHOLD_PENDING_LATE}+
    """)
    
    # Display header for repeating pairs
    st.markdown("<b>Repeating Pairs (Doubles)</b>", unsafe_allow_html=True)
    
    # Create columns for repeating pairs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'<div style="color: red; font-weight: bold;">RED (Late) Pairs (≥{THRESHOLD_LATE_REPEATING}):</div>', unsafe_allow_html=True)
        if repeating_red:
            st.write(", ".join(repeating_red))
        else:
            st.write("None")
    
    with col2:
        st.markdown(f'<div style="color: blue; font-weight: bold;">BLUE (Very Late) Pairs (≥{THRESHOLD_VERY_LATE_REPEATING}):</div>', unsafe_allow_html=True)
        if repeating_blue:
            st.write(", ".join(repeating_blue))
        else:
            st.write("None")
    
    with col3:
        st.markdown(f'<div style="color: purple; font-weight: bold;">PURPLE (Pending) Pairs (≥{THRESHOLD_PENDING_LATE}):</div>', unsafe_allow_html=True)
        if repeating_purple:
            st.write(", ".join(repeating_purple))
        else:
            st.write("None")
    
    # Display header for non-repeating pairs
    st.markdown("<b>Non-Repeating Pairs</b>", unsafe_allow_html=True)
    
    # Create columns for non-repeating pairs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'<div style="color: red; font-weight: bold;">RED (Late) Pairs (≥{THRESHOLD_LATE_NONREPEATING}):</div>', unsafe_allow_html=True)
        if non_repeating_red:
            st.write(", ".join(non_repeating_red))
        else:
            st.write("None")
    
    with col2:
        st.markdown(f'<div style="color: blue; font-weight: bold;">BLUE (Very Late) Pairs (≥{THRESHOLD_VERY_LATE_NONREPEATING}):</div>', unsafe_allow_html=True)
        if non_repeating_blue:
            st.write(", ".join(non_repeating_blue))
        else:
            st.write("None")
    
    with col3:
        st.markdown(f'<div style="color: purple; font-weight: bold;">PURPLE (Pending) Pairs (≥{THRESHOLD_PENDING_LATE}):</div>', unsafe_allow_html=True)
        if non_repeating_purple:
            st.write(", ".join(non_repeating_purple))
        else:
            st.write("None")
    
    # Create detailed pairs analysis table (like official Ontario data)
    st.subheader("Pairs Analysis Results")
    
    # Calculate times drawn for each pair
    times_drawn = {}
    last_seen_date = {}
    
    # Process draws for both times drawn and last seen date
    for i, draw in enumerate(state_data["draws"][:150]):  # Use 150 draws like official stats
        if len(draw) != 3:
            continue
        
        # Extract date information from state_data if available
        draw_date = datetime.now()  # Default to today if no date available
        if "dates" in state_data and i < len(state_data["dates"]):
            try:
                draw_date = datetime.strptime(state_data["dates"][i], "%Y-%m-%d")
            except:
                pass  # Use default date if parsing fails
        
        d1, d2, d3 = draw[0], draw[1], draw[2]
        raw_pairs = [d1+d2, d2+d3, d1+d3]
        
        for raw_pair in raw_pairs:
            # Create canonical form (sorted digits)
            pair = ''.join(sorted(raw_pair))
            
            # Count times drawn
            times_drawn[pair] = times_drawn.get(pair, 0) + 1
            
            # Track last seen date (only for first occurrence)
            if pair not in last_seen_date:
                last_seen_date[pair] = draw_date
    
    # Combine all pairs and their metrics
    all_pairs = list(set(list(non_repeating_overdue.keys()) + list(repeating_overdue.keys())))
    all_pairs.sort()  # Sort numerically
    
    # Create table data
    pair_data = []
    
    for pair in all_pairs:
        # Skip pairs we haven't seen in our window
        if pair not in times_drawn:
            continue
            
        is_repeating = (pair[0] == pair[1])
        overdue = repeating_overdue.get(pair, 0) if is_repeating else non_repeating_overdue.get(pair, 0)
        
        pair_data.append({
            "Pair": pair,
            "Times Drawn": times_drawn.get(pair, 0),
            "Last Seen": last_seen_date.get(pair, "").strftime("%b %d, %Y") if pair in last_seen_date else "",
            "Draws Since": overdue
        })
    
    # Sort by draws since (descending)
    pair_data.sort(key=lambda x: x["Draws Since"], reverse=True)
    
    # Create DataFrame and display
    df_pairs = pd.DataFrame(pair_data)
    st.dataframe(df_pairs)
    
    # Display V-Trac Table
    st.subheader("V-Trac Analysis")
    display_vtrac_table(state_data)
    
    # Display Top Overdue Pairs
    display_top_overdue_pairs(state_data)

def display_combined_page():
    """Display the combined analysis page with all states ranked by draws since last double."""
    results = st.session_state.results
    
    if not results:
        st.warning("No data available. Please upload an Excel file.")
        return
    
    combined_data = results.get("combined")
    if not combined_data:
        st.warning("No combined analysis data available.")
        return
    
    # Get doubles history with safety check
    doubles_history = combined_data.get("doubles_history")
    if not doubles_history:
        st.warning("No doubles history data available.")
        return
    
    # Create enhanced display information
    display_data = []
    for state, draws_since in doubles_history.items():
        # Get total draws for this state for context
        total_draws = len(results.get(state, {}).get("draws", []))
        
        # Check if this state has no doubles found
        no_doubles_found = draws_since >= total_draws - 1  # Account for zero-based indexing
        
        # Get the latest double if there is one
        latest_double = "None"
        if not no_doubles_found and total_draws > 0:
            state_draws = results.get(state, {}).get("draws", [])
            if draws_since < len(state_draws):
                # The double is at position 'draws_since'
                latest_double = state_draws[draws_since]
                
        display_data.append({
            "State": state,
            "Draws Since Last Double": "No doubles found" if no_doubles_found else draws_since,
            "Latest Double": latest_double if not no_doubles_found else "None",
            "Total Draws": total_draws,
            "Numerical Value": total_draws + 1000 if no_doubles_found else draws_since  # For sorting
        })
    
    # Convert to DataFrame and sort
    df = pd.DataFrame(display_data)
    df = df.sort_values("Numerical Value", ascending=False)
    
    # Display only the relevant columns
    display_df = df[["State", "Draws Since Last Double", "Latest Double", "Total Draws"]]
    
    # Display as table
    st.subheader("States Ranked by Draws Since Last Double")
    st.dataframe(display_df)

# Sidebar
st.sidebar.title("Lottery Analysis Tool")

# Analysis settings
st.sidebar.header("Analysis Settings")
if "analysis_draws" not in st.session_state:
    st.session_state.analysis_draws = 100

analysis_draws = st.sidebar.slider(
    "Analysis Window Size (Draws)", 
    min_value=50, 
    max_value=500, 
    value=st.session_state.analysis_draws,
    step=50,
    help="Number of draws to use for calculating overdue pairs. Smaller windows will show more overdue pairs."
)
st.session_state.analysis_draws = analysis_draws

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload Pick3StatsC4 Excel File", type=["xlsx", "xlsm"])
if uploaded_file:
    if st.sidebar.button("Process File"):
        with st.spinner("Processing file..."):
            success = process_file(uploaded_file)
            if success:
                st.sidebar.success("File processed successfully!")
                # Set the first state as current if none selected
                if not st.session_state.current_state and st.session_state.results:
                    valid_states = [s for s in st.session_state.results.keys() if s != "combined"]
                    if valid_states:
                        st.session_state.current_state = valid_states[0]

# Display last upload time
if st.session_state.last_upload_time:
    st.sidebar.info(f"Last upload: {st.session_state.last_upload_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Navigation
st.sidebar.header("Navigation")

# Only show navigation options if results are available
if st.session_state.results:
    # Get valid states (exclude "combined")
    valid_states = [s for s in st.session_state.results.keys() if s != "combined"]
    
    # Add "Combined View" at the top
    view_options = ["Combined View"] + valid_states
    selected_view = st.sidebar.selectbox("Select View", view_options)
    
    # Update current state
    st.session_state.current_state = selected_view if selected_view != "Combined View" else None
    
    # Display selected view
    if selected_view == "Combined View":
        st.title("Combined Analysis")
        display_combined_page()
    else:
        st.title(f"{selected_view} Analysis")
        display_state_page(selected_view)
else:
    # Display welcome message
    st.title("Welcome to the Lottery Analysis Tool")
    st.write("Please upload a Pick3StatsC4 Excel file to begin analysis.")
    
    # Show example image or description
    st.markdown("""
    ### How to Use This Tool
    
    1. **Upload File**: Use the sidebar to upload your Pick3StatsC4 Excel file
    2. **Process Data**: Click "Process File" to analyze the data
    3. **Navigate States**: Use the sidebar to select different states or the combined view
    
    ### Features
    
    - V-Trac analysis for each state
    - Color-coded overdue pairs:
        - Red: Late pairs (non-repeating: 37+ draws, repeating: 71+ draws)
        - Blue: Very late pairs (non-repeating: 56+ draws, repeating: 107+ draws)
        - Purple: Pending late pairs (25+ draws)
    - Underlined combinations that haven't appeared in 1,000 draws
    - Top 5 most overdue repeating pairs for each state
    - Combined ranking of states by draws since last double
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2023 Lottery Analysis Tool") 