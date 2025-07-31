"""
Indicators and compound scoring for auxiliary tools.

This module provides overdue pairs tracking, doubles analysis, and placeholder
functionality for future compound scoring indicators.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Tuple, Optional
import logging
import sys
import os

# Add the legacy modules to path for imports
legacy_path = os.path.join(os.path.dirname(__file__), '..', 'core_legacy', 'legacy_modules_backup')
if legacy_path not in sys.path:
    sys.path.insert(0, legacy_path)

try:
    from analyze_pairs import (
        extract_pairs, calculate_overdue_pairs, get_top_overdue_repeating_pairs,
        get_doubles_history, COLOR_LATE, COLOR_VERY_LATE, COLOR_PENDING,
        THRESHOLD_LATE_NONREPEATING, THRESHOLD_LATE_REPEATING,
        THRESHOLD_VERY_LATE_NONREPEATING, THRESHOLD_VERY_LATE_REPEATING,
        THRESHOLD_PENDING_LATE
    )
except ImportError as e:
    logging.error(f"Failed to import legacy analyze_pairs module: {e}")
    # Define fallbacks
    COLOR_LATE = 'red'
    COLOR_VERY_LATE = 'blue'  
    COLOR_PENDING = 'purple'

logger = logging.getLogger(__name__)


def get_overdue_pairs_analysis(draws: List[str], top_n: int = 10) -> pd.DataFrame:
    """
    Analyze overdue pairs and return a DataFrame with color coding.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        top_n: Number of top overdue pairs to return
        
    Returns:
        DataFrame with pair, overdue_count, and color information
    """
    if not draws:
        logger.warning("No draws provided for overdue pairs analysis")
        return pd.DataFrame(columns=['Pair', 'Draws_Overdue', 'Color', 'Type'])
    
    try:
        # Calculate overdue pairs
        non_repeating_overdue, repeating_overdue, colored_pairs = calculate_overdue_pairs(draws)
        
        # Get top overdue repeating pairs specifically
        top_pairs = get_top_overdue_repeating_pairs(draws, top_n)
        
        # Combine all overdue pairs
        all_pairs = []
        
        # Add repeating pairs
        for pair, overdue_count in repeating_overdue.items():
            color = determine_pair_color(pair, overdue_count, is_repeating=True)
            all_pairs.append({
                'Pair': pair,
                'Draws_Overdue': overdue_count,
                'Color': color,
                'Type': 'Repeating'
            })
        
        # Add non-repeating pairs
        for pair, overdue_count in non_repeating_overdue.items():
            color = determine_pair_color(pair, overdue_count, is_repeating=False)
            all_pairs.append({
                'Pair': pair,
                'Draws_Overdue': overdue_count,
                'Color': color,
                'Type': 'Non-Repeating'
            })
        
        # Create DataFrame and sort by overdue count
        df = pd.DataFrame(all_pairs)
        if not df.empty:
            df = df.sort_values('Draws_Overdue', ascending=False).head(top_n)
        
        return df
        
    except Exception as e:
        logger.error(f"Error in overdue pairs analysis: {e}")
        return pd.DataFrame(columns=['Pair', 'Draws_Overdue', 'Color', 'Type'])


def get_doubles_tracker_analysis(draws: List[str]) -> pd.DataFrame:
    """
    Track doubles (repeating pairs) and their patterns.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        
    Returns:
        DataFrame with doubles analysis
    """
    if not draws:
        logger.warning("No draws provided for doubles analysis")
        return pd.DataFrame(columns=['Double', 'Last_Seen', 'Frequency', 'Draws_Since'])
    
    try:
        # Get doubles history
        doubles_data = get_doubles_history(draws)
        
        # Process the doubles data
        doubles_analysis = []
        
        for double, info in doubles_data.items():
            last_seen = info.get('last_seen', len(draws))
            frequency = info.get('frequency', 0)
            draws_since = info.get('draws_since', len(draws))
            
            doubles_analysis.append({
                'Double': double,
                'Last_Seen': last_seen,
                'Frequency': frequency,
                'Draws_Since': draws_since
            })
        
        # Create DataFrame and sort by draws since last appearance
        df = pd.DataFrame(doubles_analysis)
        if not df.empty:
            df = df.sort_values('Draws_Since', ascending=False)
        
        return df
        
    except Exception as e:
        logger.error(f"Error in doubles analysis: {e}")
        # Return basic doubles analysis as fallback
        return get_basic_doubles_analysis(draws)


def get_basic_doubles_analysis(draws: List[str]) -> pd.DataFrame:
    """
    Basic doubles analysis fallback when legacy modules are not available.
    
    Args:
        draws: List of 3-digit draw strings
        
    Returns:
        DataFrame with basic doubles information
    """
    doubles_count = {}
    doubles_last_seen = {}
    
    for i, draw in enumerate(draws):
        if len(draw) == 3:
            # Check for doubles in the draw
            if draw[0] == draw[1]:
                double = draw[0] + draw[1]
                doubles_count[double] = doubles_count.get(double, 0) + 1
                if double not in doubles_last_seen:
                    doubles_last_seen[double] = i
            
            if draw[1] == draw[2]:
                double = draw[1] + draw[2]
                doubles_count[double] = doubles_count.get(double, 0) + 1
                if double not in doubles_last_seen:
                    doubles_last_seen[double] = i
            
            if draw[0] == draw[2]:
                double = draw[0] + draw[2]
                doubles_count[double] = doubles_count.get(double, 0) + 1
                if double not in doubles_last_seen:
                    doubles_last_seen[double] = i
    
    # Create analysis data
    analysis_data = []
    for double in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']:
        last_seen = doubles_last_seen.get(double, len(draws))
        frequency = doubles_count.get(double, 0)
        draws_since = last_seen
        
        analysis_data.append({
            'Double': double,
            'Last_Seen': last_seen,
            'Frequency': frequency,
            'Draws_Since': draws_since
        })
    
    return pd.DataFrame(analysis_data).sort_values('Draws_Since', ascending=False)


def determine_pair_color(pair: str, overdue_count: int, is_repeating: bool) -> str:
    """
    Determine the color coding for a pair based on how overdue it is.
    
    Args:
        pair: The pair string
        overdue_count: Number of draws since last seen
        is_repeating: Whether this is a repeating pair (double)
        
    Returns:
        Color string ('red', 'blue', 'purple', or '')
    """
    if is_repeating:
        if overdue_count >= THRESHOLD_VERY_LATE_REPEATING:
            return COLOR_VERY_LATE  # blue
        elif overdue_count >= THRESHOLD_LATE_REPEATING:
            return COLOR_LATE  # red
        elif overdue_count >= THRESHOLD_PENDING_LATE:
            return COLOR_PENDING  # purple
    else:
        if overdue_count >= THRESHOLD_VERY_LATE_NONREPEATING:
            return COLOR_VERY_LATE  # blue
        elif overdue_count >= THRESHOLD_LATE_NONREPEATING:
            return COLOR_LATE  # red
        elif overdue_count >= THRESHOLD_PENDING_LATE:
            return COLOR_PENDING  # purple
    
    return ''  # No special color


def get_compound_scoring_placeholder(draws: List[str]) -> pd.DataFrame:
    """
    Placeholder for future compound scoring logic.
    
    Args:
        draws: List of 3-digit draw strings
        
    Returns:
        DataFrame with placeholder compound scoring data
    """
    logger.info("Compound scoring is not yet implemented - returning placeholder")
    
    # Return placeholder DataFrame
    return pd.DataFrame({
        'Indicator': ['Pattern_Stability', 'Frequency_Score', 'Overdue_Weight', 'Combined_Score'],
        'Value': [0.0, 0.0, 0.0, 0.0],
        'Status': ['Placeholder'] * 4,
        'Description': [
            'Pattern stability indicator (not implemented)',
            'Frequency-based scoring (not implemented)', 
            'Overdue weighting factor (not implemented)',
            'Combined compound score (not implemented)'
        ]
    })


def format_overdue_pairs_for_display(df: pd.DataFrame) -> str:
    """
    Format overdue pairs DataFrame for HTML display with color styling.
    
    Args:
        df: Overdue pairs DataFrame
        
    Returns:
        HTML formatted string
    """
    if df.empty:
        return "<p>No overdue pairs data available.</p>"
    
    html_rows = []
    
    for _, row in df.iterrows():
        pair = row['Pair']
        overdue = row['Draws_Overdue']
        color = row.get('Color', '')
        pair_type = row.get('Type', '')
        
        if color:
            html_rows.append(
                f'<span class="{color}">{pair} - {overdue} draws overdue ({pair_type})</span>'
            )
        else:
            html_rows.append(f'{pair} - {overdue} draws overdue ({pair_type})')
    
    return '<br>'.join(html_rows)


def get_indicators_summary(overdue_df: pd.DataFrame, doubles_df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate summary statistics for the indicators.
    
    Args:
        overdue_df: Overdue pairs DataFrame
        doubles_df: Doubles analysis DataFrame
        
    Returns:
        Dictionary with summary statistics
    """
    try:
        summary = {
            'total_overdue_pairs': len(overdue_df),
            'red_overdue_pairs': len(overdue_df[overdue_df['Color'] == 'red']) if not overdue_df.empty else 0,
            'blue_overdue_pairs': len(overdue_df[overdue_df['Color'] == 'blue']) if not overdue_df.empty else 0,
            'purple_pending_pairs': len(overdue_df[overdue_df['Color'] == 'purple']) if not overdue_df.empty else 0,
            'total_doubles_tracked': len(doubles_df),
            'most_overdue_pair': overdue_df.iloc[0]['Pair'] if not overdue_df.empty else 'None',
            'most_overdue_count': overdue_df.iloc[0]['Draws_Overdue'] if not overdue_df.empty else 0
        }
        
        return summary
        
    except Exception as e:
        logger.error(f"Error generating indicators summary: {e}")
        return {
            'total_overdue_pairs': 0,
            'red_overdue_pairs': 0,
            'blue_overdue_pairs': 0,
            'purple_pending_pairs': 0,
            'total_doubles_tracked': 0,
            'most_overdue_pair': 'None',
            'most_overdue_count': 0
        }