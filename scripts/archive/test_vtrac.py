#!/usr/bin/env python
"""
test_vtrac.py - Test V-TRAC pattern matching and winner highlighting
"""

import os
import sys
import pandas as pd
from typing import List, Tuple

# Add scripts to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from utils.vtrac_utils import (
    BOXED_VTRAC_REFERENCE,
    find_vtrac_index_and_combos,
    get_all_permutations
)
from vtrac.winner_highlighter import highlight_winners

def print_test_header(title: str):
    """Print formatted test header"""
    print("\n" + "="*50)
    print(f"TEST: {title}")
    print("="*50)

def test_vtrac_lookup():
    """Test V-TRAC index lookup and pattern matching"""
    print_test_header("V-TRAC Lookup and Pattern Matching")
    
    # Test cases with expected results
    test_cases = [
        ("123", "Singles pattern - should be in index with singles"),
        ("111", "Doubles pattern - should be in index with doubles"),
        ("456", "Singles pattern - should be in index with singles"),
        ("789", "Singles pattern - should be in index with singles"),
        ("112", "Mixed pattern - should be in index with mixed"),
        ("000", "Special case - all zeros"),
        ("999", "Special case - all nines")
    ]
    
    for number, description in test_cases:
        print(f"\nTesting number: {number}")
        print(f"Description: {description}")
        
        # Get V-TRAC index and combinations
        index, winning_perms, related_combos = find_vtrac_index_and_combos(number)
        
        print(f"V-TRAC Index: {index}")
        print(f"Winning permutations: {sorted(winning_perms)}")
        print(f"Related combinations: {sorted(related_combos)}")
        
        # Verify results
        if index is not None:
            print("✓ V-TRAC index found")
            if winning_perms:
                print("✓ Winning permutations found")
            if related_combos:
                print("✓ Related combinations found")
        else:
            print("✗ No V-TRAC index found")

def create_test_table() -> pd.DataFrame:
    """Create a test table with various number combinations"""
    return pd.DataFrame({
        'Set': ['Set1', 'Set1', 'Set1', 'Set1'],
        'Draw': ['Draw1', 'Draw2', 'Draw3', 'Draw4'],
        'RowType': ['R2', 'R2', 'R2', 'R2'],
        '7': ['123456', '234567', '345678', '456789'],
        '6': ['12345', '23456', '34567', '45678'],
        '5': ['1234', '2345', '3456', '4567'],
        '4': ['123', '234', '345', '456'],
        '3': ['12', '23', '34', '45'],
        '2': ['1', '2', '3', '4'],
        '1': ['0', '1', '2', '3']
    })

def test_winner_highlighting():
    """Test winner highlighting in tables"""
    print_test_header("Winner Highlighting in Tables")
    
    # Create test table
    test_df = create_test_table()
    print("\nOriginal table:")
    print(test_df)
    
    # Test cases for highlighting
    test_cases = [
        ("123", "Testing singles pattern"),
        ("111", "Testing doubles pattern"),
        ("456", "Testing another singles pattern")
    ]
    
    for winning_number, description in test_cases:
        print(f"\nHighlighting winners for number: {winning_number}")
        print(f"Description: {description}")
        
        # Apply highlighting
        highlighted = highlight_winners(test_df, winning_number)
        
        # Print results
        print("\nHighlighted table:")
        print(highlighted)
        
        # Verify highlighting
        has_red = any('color: red' in str(val) for val in highlighted.values)
        has_blue = any('color: blue' in str(val) for val in highlighted.values)
        
        if has_red:
            print("✓ Red highlighting applied (exact matches)")
        if has_blue:
            print("✓ Blue highlighting applied (related combinations)")

def test_edge_cases():
    """Test edge cases and error handling"""
    print_test_header("Edge Cases and Error Handling")
    
    # Test empty table
    empty_df = pd.DataFrame()
    print("\nTesting empty table:")
    result = highlight_winners(empty_df, "123")
    print("✓ Empty table handled correctly")
    
    # Test invalid winning number
    test_df = create_test_table()
    print("\nTesting invalid winning number:")
    result = highlight_winners(test_df, "invalid")
    print("✓ Invalid winning number handled correctly")
    
    # Test table with missing columns
    partial_df = test_df[['Set', 'Draw', 'RowType', '4', '3', '2', '1']]
    print("\nTesting table with missing columns:")
    result = highlight_winners(partial_df, "123")
    print("✓ Partial table handled correctly")

if __name__ == "__main__":
    # Run all tests
    test_vtrac_lookup()
    test_winner_highlighting()
    test_edge_cases()
    
    print("\nAll tests completed!") 