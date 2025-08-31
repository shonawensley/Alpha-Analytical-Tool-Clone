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
    .circle {
        border: 2px solid #444;
        padding: 2px 3px;
        border-radius: 6px;
    }
    .shape-red-circle { border: 2px solid red; border-radius: 8px; padding: 1px 3px; }
    .shape-blue-square { border: 2px solid blue; padding: 1px 3px; }
    .row-green { background-color: rgba(0, 200, 0, 0.08); display: block; padding: 2px 4px; min-height: 1.2em; }
    .row-red { background-color: rgba(255, 0, 0, 0.08); display: block; padding: 2px 4px; min-height: 1.2em; }
    .rank-badge { font-size: 0.8em; float: right; opacity: 0.7; }
    .digit { padding: 0 1px; font-weight: 600; }
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

def _severity(cls: str) -> int:
    # Higher number = higher severity (blue > red > purple > none)
    return {"blue": 3, "red": 2, "purple": 1}.get(cls or "", 0)


def _color_digit_pairs(combo: str, pair_status: Dict[str, str]) -> str:
    """Return HTML for a 3-digit combo with per-digit coloring based on due pairs."""
    if len(combo) != 3:
        return combo
    d1, d2, d3 = combo[0], combo[1], combo[2]
    p12 = ''.join(sorted(d1 + d2))
    p23 = ''.join(sorted(d2 + d3))
    p13 = ''.join(sorted(d1 + d3))
    # Determine color per digit by taking the highest severity among pairs containing it
    c1 = pair_status.get(p12, "")
    if _severity(pair_status.get(p13, "")) > _severity(c1):
        c1 = pair_status.get(p13, "")
    c2 = pair_status.get(p12, "")
    if _severity(pair_status.get(p23, "")) > _severity(c2):
        c2 = pair_status.get(p23, "")
    c3 = pair_status.get(p13, "")
    if _severity(pair_status.get(p23, "")) > _severity(c3):
        c3 = pair_status.get(p23, "")
    # Build HTML with digit spans; use same color class names (.red/.blue/.purple)
    s1 = f'<span class="digit {c1}">{d1}</span>' if c1 else f'<span class="digit">{d1}</span>'
    s2 = f'<span class="digit {c2}">{d2}</span>' if c2 else f'<span class="digit">{d2}</span>'
    s3 = f'<span class="digit {c3}">{d3}</span>' if c3 else f'<span class="digit">{d3}</span>'
    return s1 + s2 + s3


def format_combo(combo: str, status_dict: Dict[str, Any], appeared: bool, pair_status: Optional[Dict[str, str]] = None) -> str:
    """Format a combination string with shapes and per-digit coloring for due pairs."""
    if combo not in status_dict:
        # Fallback: plain or per-digit if pair_status is available
        return _color_digit_pairs(combo, pair_status) if pair_status else combo
    
    combo_status = status_dict[combo]
    
    # Determine CSS classes
    classes = []
    # Only add combination threshold shapes (no full-text color here)
    if combo_status.get("shape_red_circle"):
        classes.append("shape-red-circle")
    elif combo_status.get("shape_blue_square"):
        classes.append("shape-blue-square")
    
    inner_html = _color_digit_pairs(combo, pair_status) if pair_status else combo
    if not classes:
        return inner_html
    
    # Join classes and format HTML
    class_str = " ".join(classes)
    return f'<span class="{class_str}">{inner_html}</span>'

def display_vtrac_table(state_data: Dict[str, Any], pair_status: Optional[Dict[str, str]] = None):
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
        index_style = status.get("index_style", {})
        
        # Format singles (per-digit pair coloring)
        singles = entry["Singles"]
        if singles:
            formatted_singles = " ".join([
                format_combo(combo, singles_status, appeared, pair_status) 
                for combo in singles.split()
            ])
        else:
            formatted_singles = ""
        
        # Format doubles (per-digit pair coloring)
        doubles = entry["Doubles"]
        if doubles:
            formatted_doubles = " ".join([
                format_combo(combo, doubles_status, appeared, pair_status)
                for combo in doubles.split()
            ])
        else:
            formatted_doubles = ""
        
        # Add badge if ranked
        badge = ""
        if index_style.get("rank"):
            badge = f'<sup class="rank-badge">{index_style["rank"]}</sup>'

        # Row class for tinting
        row_class = ""
        if index_style.get("bg") == "green":
            row_class = "row-green"
        elif index_style.get("bg") == "red":
            row_class = "row-red"

        # Ensure non-empty content so tint spans even when no combos present
        singles_content = formatted_singles if formatted_singles else "&nbsp;"
        doubles_content = formatted_doubles if formatted_doubles else "&nbsp;"

        # Wrap cells with row class and badge
        index_cell = f'<div class="{row_class}">{index}{badge}</div>' if row_class else f'{index}{badge}'
        singles_cell = f'<div class="{row_class}">{singles_content}{badge}</div>' if row_class else f'{formatted_singles}{badge}'
        doubles_cell = f'<div class="{row_class}">{doubles_content}{badge}</div>' if row_class else f'{formatted_doubles}{badge}'

        table_data.append({
            "Index": index_cell,
            "Singles": singles_cell,
            "Doubles": doubles_cell
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
    
    # Prepare latest draws for multi-column layout
    df_latest = pd.DataFrame({"Draw": state_data["draws"][:5]}) if state_data["draws"] else pd.DataFrame({"Draw": []})
    
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
    
    # Create DataFrame (render later in row)
    df_pairs = pd.DataFrame(pair_data)
    
    # Build Combinations Analysis data (render later in row)
    dfc = pd.DataFrame()
    try:
        combo_ds = state_data["vtrac_statuses"].get(0, {})
        singles_ds = combo_ds.get("singles_ds", {})
        doubles_ds = combo_ds.get("doubles_ds", {})
        if singles_ds or doubles_ds:
            rows = []
            S_RED, S_BLUE, D_RED, D_BLUE = 501, 334, 1000, 667
            for base, ds in singles_ds.items():
                rows.append({"Combo": base, "Type": "Single", "Draws Since": ds})
            for base, ds in doubles_ds.items():
                rows.append({"Combo": base, "Type": "Double", "Draws Since": ds})
            if rows:
                rows.sort(key=lambda x: x["Draws Since"], reverse=True)
                dfc = pd.DataFrame(rows)
    except Exception:
        dfc = pd.DataFrame()
    
    # Display V-Trac Table with shapes
    st.subheader("V-Trac Analysis")
    display_vtrac_table(state_data, pair_status)

    # Four panels row: Latest Draws | Pairs Analysis | Combinations | Top 5 Doubles
    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        st.subheader("Latest Draws")
        st.dataframe(df_latest, use_container_width=True)
    with c2:
        st.subheader("Pairs Analysis Results")
        st.dataframe(df_pairs, use_container_width=True)
    with c3:
        st.subheader("Combinations Analysis (Draws Since)")
        if not dfc.empty:
            # Render combo column with the same digit-level coloring and shapes
            safe_rows = []
            combo_ds = state_data["vtrac_statuses"].get(0, {})
            singles_ds = combo_ds.get("singles_ds", {})
            doubles_ds = combo_ds.get("doubles_ds", {})
            S_RED, S_BLUE, D_RED, D_BLUE = 501, 334, 1000, 667
            # Build a tiny status mapping to reuse format_combo shapes
            for _, r in dfc.iterrows():
                combo = str(r["Combo"]).zfill(3)
                typ = r["Type"]
                ds = int(r["Draws Since"]) if pd.notna(r["Draws Since"]) else 0
                status = {}
                if typ == "Single":
                    if ds >= S_RED:
                        status[combo] = {"shape_red_circle": True}
                    elif ds >= S_BLUE:
                        status[combo] = {"shape_blue_square": True}
                else:
                    if ds >= D_RED:
                        status[combo] = {"shape_red_circle": True}
                    elif ds >= D_BLUE:
                        status[combo] = {"shape_blue_square": True}
                html_combo = format_combo(combo, status, True, pair_status)
                safe_rows.append({"Combo": html_combo, "Type": typ, "Draws Since": ds})
            dfc_html = pd.DataFrame(safe_rows)
            # Make scrollable container like before
            from io import StringIO
            html_table = dfc_html.to_html(escape=False, index=False)
            st.markdown(f'<div style="max-height: 420px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_table}</div>', unsafe_allow_html=True)
        else:
            st.write("No data")
    with c4:
        st.subheader("Top 5 Most Overdue Repeating Pairs")
        display_top_overdue_pairs(state_data)

    # Legend
    with st.expander("Legend / Feature Guide"):
        st.markdown("""
        - V‑Trac index row tints: light green = last 5 hit (rank 1..5), light red = 5 most overdue (rank 1..5).
        - Combination shapes:
          - Red circle: Singles ≥ 501 draws since; Doubles ≥ 1000
          - Blue square: Singles ≥ 334; Doubles ≥ 667
          - Boxed combos: permutations are treated as the same combo
        - Pairs colors (analysis window based):
          - Red (Late): non‑repeating ≥ 37, repeating ≥ 71
          - Blue (Very Late): non‑repeating ≥ 56, repeating ≥ 107
          - Purple (Pending): ≥ 25
        """)

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

# --- NEW: Local File Processor ---
st.sidebar.header("Data Source")
local_excel_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")

if os.path.exists(local_excel_path):
    st.sidebar.success(f"Found local file: {os.path.basename(local_excel_path)}")
    if st.sidebar.button("Process Local File"):
        with st.spinner("Processing local file..."):
            try:
                from run_process import run_process
                analysis_draws = st.session_state.get("analysis_draws", 100)
                results = run_process(local_excel_path, max_draws=1000, analysis_draws=analysis_draws)
                
                st.session_state.results = results
                st.session_state.last_upload_time = datetime.now()
                st.sidebar.success("File processed successfully!")

                if not st.session_state.current_state and st.session_state.results:
                   valid_states = [s for s in st.session_state.results.keys() if s != "combined"]
                   if valid_states:
                       st.session_state.current_state = valid_states[0]
                # Trigger a rerun to update the main page
                st.rerun()

            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
                import traceback
                st.error(traceback.format_exc())
else:
    st.sidebar.warning("No local Pick3StatsC4.xlsm file found in data/original. Please upload a file below.")

st.sidebar.markdown("---")

# File uploader
st.sidebar.subheader("Or Upload a Different File")
uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx", "xlsm"])
if uploaded_file:
    if st.sidebar.button("Process Uploaded File"):
        with st.spinner("Processing uploaded file..."):
            success = process_file(uploaded_file)
            if success:
                st.sidebar.success("File processed successfully!")
                # Set the first state as current if none selected
                if not st.session_state.current_state and st.session_state.results:
                    valid_states = [s for s in st.session_state.results.keys() if s != "combined"]
                    if valid_states:
                        st.session_state.current_state = valid_states[0]
                st.rerun()

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