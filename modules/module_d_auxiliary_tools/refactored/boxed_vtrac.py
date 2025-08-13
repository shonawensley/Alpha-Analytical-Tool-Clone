"""
Boxed V-TRAC table generator with color rules.

This module creates the traditional 35x8 V-TRAC table with proper color coding
for overdue patterns based on the legacy auxiliary tools functionality.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Tuple, Optional
import logging
import sys
import os
from .bootstrap_imports import init as _aux_bootstrap_init

# Add the legacy modules to path for imports
legacy_path = os.path.join(os.path.dirname(__file__), '..', 'core_legacy', 'legacy_modules_backup')
if legacy_path not in sys.path:
    sys.path.insert(0, legacy_path)

# --- force-load the rich legacy vtrac_reference as "modules.vtrac_reference" safely ---
# Initialize legacy imports once
_aux_bootstrap_init()

try:
    from vtrac_reference import VTRAC_DISPLAY, get_vtrac_index
    from analyze_pairs import (
        extract_pairs, track_pairs, calculate_overdue_pairs,
        get_vtrac_statuses, get_colored_pairs,
        COLOR_LATE, COLOR_VERY_LATE, COLOR_PENDING,
        THRESHOLD_LATE_NONREPEATING, THRESHOLD_LATE_REPEATING,
        THRESHOLD_VERY_LATE_NONREPEATING, THRESHOLD_VERY_LATE_REPEATING,
        THRESHOLD_PENDING_LATE
    )
except ImportError as e:
    logging.error(f"Failed to import legacy modules: {e}")
    # Define fallbacks
    COLOR_LATE = 'red'
    COLOR_VERY_LATE = 'blue'
    COLOR_PENDING = 'purple'
    VTRAC_DISPLAY = []

# Belt-and-suspenders: provide no-op stubs if legacy functions are missing
if 'calculate_overdue_pairs' not in globals():
    def calculate_overdue_pairs(draws):
        return ({}, {}, {})

if 'get_vtrac_statuses' not in globals():
    def get_vtrac_statuses(draws_100, draws_1000=None):
        return {}

logger = logging.getLogger(__name__)


def generate_boxed_vtrac_table(draws: List[str]) -> pd.DataFrame:
    """
    Generate the 35x8 boxed V-TRAC table with color styling.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        
    Returns:
        pandas.DataFrame with Index, Singles, Doubles columns and styling information
    """
    print(f"[DEBUG] generate_boxed_vtrac_table called with {len(draws)} draws")
    print(f"[DEBUG] VTRAC_DISPLAY available: {len(VTRAC_DISPLAY) if VTRAC_DISPLAY else 'NO'}")
    
    if not draws:
        logger.warning("No draws provided for V-TRAC table generation")
        print("[DEBUG] No draws provided - returning empty DataFrame")
        return pd.DataFrame(columns=['Index', 'Singles', 'Doubles'])
    
    try:
        # Use last 100 draws for overdue logic; last 1000 for underline checks
        draws_100 = draws[:100]
        draws_1000 = draws[:1000]

        # Calculate overdue pairs and get V-TRAC statuses
        non_repeating_overdue, repeating_overdue, colored_pairs = calculate_overdue_pairs(draws_100)
        vtrac_statuses = get_vtrac_statuses(draws_100, draws_1000)
        
        # Build the table data
        table_data = []
        
        for entry in VTRAC_DISPLAY:
            index = entry["Index"]
            status = vtrac_statuses.get(index, {})
            
            # Process singles
            singles_raw = entry.get("Singles", "")
            if singles_raw == "·":
                singles_formatted = "·"
            else:
                singles_list = singles_raw.split() if singles_raw else []
                singles_formatted = format_combinations(singles_list, status.get("singles_status", {}))
            
            # Process doubles
            doubles_raw = entry.get("Doubles", "")
            if doubles_raw == "·":
                doubles_formatted = "·"
            else:
                doubles_list = doubles_raw.split() if doubles_raw else []
                doubles_formatted = format_combinations(doubles_list, status.get("doubles_status", {}))
            
            table_data.append({
                'Index': index,
                'Singles': singles_formatted,
                'Doubles': doubles_formatted
            })
        
        # Create DataFrame
        df = pd.DataFrame(table_data)
        
        # Ensure we have exactly 35 rows
        while len(df) < 35:
            df = pd.concat([df, pd.DataFrame({'Index': [len(df) + 1], 'Singles': [''], 'Doubles': ['']})], 
                          ignore_index=True)
        
        return df.head(35)  # Ensure exactly 35 rows
        
    except Exception as e:
        logger.error(f"Error generating boxed V-TRAC table: {e}")
        # Return empty table with correct structure
        return pd.DataFrame({
            'Index': range(1, 36),
            'Singles': [''] * 35,
            'Doubles': [''] * 35
        })


def format_combinations(combos: List[str], status_dict: Dict[str, Any]) -> str:
    """
    Format a list of combinations with appropriate color styling.
    
    Args:
        combos: List of combination strings
        status_dict: Dictionary with status information for each combo
        
    Returns:
        Formatted string with HTML color coding
    """
    if not combos:
        return ""
    
    formatted_combos = []
    
    for combo in combos:
        if combo not in status_dict:
            formatted_combos.append(combo)
            continue
        
        combo_status = status_dict[combo]
        
        # Determine styling
        classes = []
        
        # Add color class if overdue
        if "color" in combo_status:
            classes.append(combo_status["color"])
        
        # Add underline if specified (hasn't appeared in analysis window)
        if combo_status.get("underline", False):
            classes.append("underline")
        
        # Format with styling if needed
        if classes:
            class_str = " ".join(classes)
            formatted_combos.append(f'<span class="{class_str}">{combo}</span>')
        else:
            formatted_combos.append(combo)
    
    return " ".join(formatted_combos)


def apply_vtrac_styling(df: pd.DataFrame):
    """
    Apply CSS styling to the V-TRAC DataFrame for display.
    
    Args:
        df: V-TRAC DataFrame
        
    Returns:
        Styled DataFrame object with color rules applied
    """
    def style_cell(val):
        """Apply styling to individual cells"""
        if pd.isna(val) or val == '':
            return ''
        
        # Base styling for the table
        base_style = 'font-family: monospace; padding: 4px; border: 1px solid #ddd;'
        
        return base_style
    
    # Apply base styling to all cells
    styler = df.style.applymap(style_cell)
    
    # Add CSS for color classes
    styler = styler.set_table_styles([
        {
            'selector': '.red',
            'props': [('color', 'red'), ('font-weight', 'bold')]
        },
        {
            'selector': '.blue', 
            'props': [('color', 'blue'), ('font-weight', 'bold')]
        },
        {
            'selector': '.purple',
            'props': [('color', 'purple'), ('font-weight', 'bold')]
        },
        {
            'selector': '.underline',
            'props': [('text-decoration', 'underline')]
        },
        {
            'selector': 'table',
            'props': [('border-collapse', 'collapse'), ('margin', '10px 0')]
        },
        {
            'selector': 'th',
            'props': [('background-color', '#f0f0f0'), ('font-weight', 'bold'), 
                     ('text-align', 'center'), ('padding', '8px')]
        },
        {
            'selector': 'td',
            'props': [('text-align', 'center'), ('vertical-align', 'middle')]
        }
    ])
    
    return styler


def render_boxed_vtrac_html(df: pd.DataFrame) -> str:
    """
    Render the boxed V-TRAC DataFrame as HTML with color classes preserved.

    Streamlit's dataframe escapes HTML; for legacy-style colored output we
    return an HTML table string for st.markdown(..., unsafe_allow_html=True).
    """
    if df is None or df.empty:
        return "<p>No V-TRAC data available.</p>"

    css = """
    <style>
      table.vtrac { border-collapse: collapse; width: 100%; }
      table.vtrac th, table.vtrac td { border: 1px solid #ddd; padding: 6px; text-align: center; }
      table.vtrac th { background: #f7f7f7; font-weight: 600; }
      .red { color: red; font-weight: 700; }
      .blue { color: blue; font-weight: 700; }
      .purple { color: purple; font-weight: 700; }
      .underline { text-decoration: underline; }
    </style>
    """

    html = df.to_html(escape=False, index=False, classes=["vtrac"])
    return css + html


def get_boxed_vtrac_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate summary statistics for the boxed V-TRAC table.
    
    Args:
        df: V-TRAC DataFrame
        
    Returns:
        Dictionary with summary statistics
    """
    try:
        total_singles = sum(1 for singles in df['Singles'] if singles and singles != '·')
        total_doubles = sum(1 for doubles in df['Doubles'] if doubles and doubles != '·')
        
        # Count colored entries (approximate by looking for HTML tags)
        red_count = sum(1 for row in df.itertuples() 
                       if 'red' in str(row.Singles) or 'red' in str(row.Doubles))
        blue_count = sum(1 for row in df.itertuples() 
                        if 'blue' in str(row.Singles) or 'blue' in str(row.Doubles))
        purple_count = sum(1 for row in df.itertuples() 
                          if 'purple' in str(row.Singles) or 'purple' in str(row.Doubles))
        
        return {
            'total_indices': len(df),
            'active_singles': total_singles,
            'active_doubles': total_doubles,
            'red_overdue': red_count,
            'blue_overdue': blue_count,
            'purple_pending': purple_count,
            'table_shape': df.shape
        }
        
    except Exception as e:
        logger.error(f"Error generating V-TRAC summary: {e}")
        return {
            'total_indices': len(df) if df is not None else 0,
            'active_singles': 0,
            'active_doubles': 0,
            'red_overdue': 0,
            'blue_overdue': 0,
            'purple_pending': 0,
            'table_shape': df.shape if df is not None else (0, 0)
        }