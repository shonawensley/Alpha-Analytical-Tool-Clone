#!/usr/bin/env python
"""
winner_highlighter.py - Highlight winning numbers and V-TRAC combinations in lottery tables

This module:
1. Finds exact matches to winning numbers (highlighted in RED)
2. Looks up V-TRAC index for winning numbers
3. Finds all permutations from same V-TRAC index (highlighted in BLUE)
4. Applies styling to DataFrames for display
"""

import os
import sys
import pandas as pd
import numpy as np
from typing import List, Dict, Set, Optional, Tuple
from itertools import permutations

# Add scripts to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.dirname(current_dir)
sys.path.append(scripts_dir)

from utils.vtrac_utils import (
    BOXED_VTRAC_REFERENCE,
    get_all_permutations,
    find_vtrac_index_and_combos,
    highlight_string_with_matches
)

def get_vtrac_combinations(number: str) -> Tuple[Set[str], Set[str]]:
    """
    Get all related combinations for a number from V-TRAC reference.
    
    Args:
        number: 3-digit number to look up
        
    Returns:
        Tuple of (exact_matches, related_combos) where:
            exact_matches: Set of all permutations of the winning number
            related_combos: Set of all other combinations from same V-TRAC index
    """
    number = str(number).zfill(3)
    _, winning_perms, related_combos = find_vtrac_index_and_combos(number)
    return winning_perms, related_combos

def style_cell(val: str, exact_matches: Set[str], related_combos: Set[str]) -> str:
    """
    Apply HTML styling to cell value based on matches.
    
    Args:
        val: Cell value to check
        exact_matches: Set of winning number permutations
        related_combos: Set of related V-TRAC combinations
        
    Returns:
        HTML-styled string
    """
    if val == "N/A" or not val:
        return val
        
    # Clean value (remove any existing styling)
    clean_val = ''.join(c for c in val if c.isdigit() or c.isspace())
    
    # Check for matches
    if any(combo in clean_val for combo in exact_matches):
        return f'<span style="color: red; font-weight: bold">{val}</span>'
    elif any(combo in clean_val for combo in related_combos):
        return f'<span style="color: blue">{val}</span>'
    
    return val

def highlight_winners(df: pd.DataFrame, winning_number: str) -> pd.DataFrame:
    """
    Highlight winning numbers (red) and related combinations (blue) in table.
    
    Args:
        df: DataFrame to process
        winning_number: 3-digit winning number
        
    Returns:
        Styled DataFrame with highlighted values
    """
    if df is None or df.empty or not winning_number:
        return df
    
    # Get exact matches and related combinations
    exact_matches, related_combos = get_vtrac_combinations(winning_number)
    
    # Create copy for modification
    styled_df = df.copy()
    
    # Value columns (7 to 1)
    value_cols = [str(i) for i in range(7, 0, -1)]
    
    # Apply styling to each cell
    for col in value_cols:
        if col in styled_df.columns:
            styled_df[col] = styled_df[col].apply(
                lambda x: style_cell(str(x), exact_matches, related_combos)
            )
    
    return styled_df

def highlight_winners_in_tables(tables_data: Dict, 
                              midday_winner: Optional[str] = None,
                              evening_winner: Optional[str] = None) -> Dict:
    """
    Process all tables and highlight winners.
    
    Args:
        tables_data: Dictionary containing tables
        midday_winner: Optional midday winning number
        evening_winner: Optional evening winning number
        
    Returns:
        Dictionary with highlighted tables
    """
    result = {}
    
    for section_name, section_data in tables_data.items():
        # Determine which winner to use
        winner = None
        if "Midday" in section_name and midday_winner:
            winner = midday_winner
        elif "Evening" in section_name and evening_winner:
            winner = evening_winner
        elif "Combined" in section_name:
            # For combined, check both winners
            if midday_winner:
                section_data = highlight_winners(section_data, midday_winner)
            if evening_winner:
                section_data = highlight_winners(section_data, evening_winner)
            result[section_name] = section_data
            continue
            
        # Process section if we have a winner
        if winner:
            result[section_name] = highlight_winners(section_data, winner)
        else:
            result[section_name] = section_data
            
    return result

def parse_winners_input(winners_text: str) -> List[str]:
    """
    Parse winners input text into list of numbers.
    
    Args:
        winners_text: String containing winning numbers
        
    Returns:
        List of cleaned 3-digit numbers
    """
    if not winners_text:
        return []
        
    # Split on common separators and clean
    numbers = []
    for part in winners_text.replace(',', ' ').split():
        clean = ''.join(c for c in part if c.isdigit())
        if len(clean) >= 3:
            numbers.append(clean[-3:])  # Take last 3 digits
            
    return numbers

# Example usage and testing
if __name__ == "__main__":
    # Sample data for testing
    sample_df = pd.DataFrame({
        'Set': ['Set1', 'Set1'],
        'Draw': ['Draw1', 'Draw2'],
        'RowType': ['R2', 'R2'],
        '7': ['123456', '234567'],
        '6': ['12345', '23456'],
        '5': ['1234', '2345'],
        '4': ['123', '234'],
        '3': ['12', '23'],
        '2': ['1', '2'],
        '1': ['0', '1']
    })
    
    # Test highlighting
    winning_number = "123"
    highlighted = highlight_winners(sample_df, winning_number)
    print("\nHighlighted table for winner", winning_number)
    print(highlighted)
    
    # Test V-TRAC combinations
    exact, related = get_vtrac_combinations("123")
    print("\nV-TRAC combinations for", winning_number)
    print("Exact matches:", exact)
    print("Related combinations:", related) 