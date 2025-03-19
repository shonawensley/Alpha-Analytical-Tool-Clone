#!/usr/bin/env python
"""
test_vtrac.py - Test script for V-TRAC pattern extraction
"""

import os
import sys
from vtrac_utils import find_vtrac_index_and_combos, highlight_winners_in_table

def test_pattern_extraction():
    """Test V-TRAC pattern extraction with sample numbers"""
    test_cases = [
        "468",  # Sample from your data
        "684",  # Permutation
        "992",  # Another sample
        "025"   # From VTRAC reference
    ]
    
    print("\nTesting V-TRAC Pattern Extraction:")
    print("=" * 50)
    
    for number in test_cases:
        print(f"\nTesting number: {number}")
        try:
            vtrac_index, winning_perms, related = find_vtrac_index_and_combos(number)
            print(f"V-TRAC Index: {vtrac_index}")
            print("Winning Permutations:", winning_perms)
            print("Related Patterns:", related)
        except Exception as e:
            print(f"Error processing {number}: {str(e)}")

def test_with_sample_data():
    """Test pattern matching with sample R2/R4/R6/R8 strings"""
    sample_data = {
        "R2": ["992244138667", "992243667", "9923667"],
        "R4": ["229966834471", "229966347", "2996637"],
        "R6": ["668179932244", "667993224", "6679932"],
        "R8": ["719983662244", "799366224", "7993662"]
    }
    
    print("\nTesting Pattern Matching in Strings:")
    print("=" * 50)
    
    # Test with a winning number
    test_number = "468"
    vtrac_index, winning_perms, related = find_vtrac_index_and_combos(test_number)
    
    print(f"\nSearching for patterns from number: {test_number}")
    print(f"V-TRAC Index: {vtrac_index}")
    
    for row_type, strings in sample_data.items():
        print(f"\n{row_type} Strings:")
        for s in strings:
            matches = []
            for perm in winning_perms:
                if perm in s:
                    matches.append(perm)
            if matches:
                print(f"  {s} => Found patterns: {matches}")
            else:
                print(f"  {s} => No matches")

if __name__ == "__main__":
    test_pattern_extraction()
    test_with_sample_data() 