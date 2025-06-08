#!/usr/bin/env python
"""
test_vtrac_enhanced.py - Enhanced testing for V-TRAC pattern extraction and string matching
"""

import os
import sys
from vtrac_utils import (
    find_vtrac_index_and_combos,
    find_all_patterns_in_string,
    find_patterns_in_row
)

def test_pattern_extraction():
    """Test V-TRAC pattern extraction with sample numbers"""
    test_cases = [
        "468",  # From NorthCarolina4 patterns
        "025",  # From Ohio4 patterns
        "177",  # From Ohio4 patterns
        "569"   # From Virginia4 patterns
    ]
    
    print("\nTesting V-TRAC Pattern Extraction:")
    print("=" * 50)
    
    for number in test_cases:
        print(f"\nTesting number: {number}")
        try:
            vtrac_index, winning_perms, related = find_vtrac_index_and_combos(number)
            print(f"V-TRAC Index: {vtrac_index}")
            print("Winning Permutations:", sorted(winning_perms))
            print("Related Patterns:", sorted(related))
        except Exception as e:
            print(f"Error processing {number}: {str(e)}")

def test_pattern_matching():
    """Test enhanced pattern matching in R2/R4/R6/R8 strings"""
    # Real sample data from your output
    sample_data = {
        "R2": [
            "992244138667",  # Complex string
            "992243667",     # Medium string
            "9923667",       # Short string
            "9267",          # Very short string
            "926"           # Minimal string
        ],
        "R4": [
            "229966834471",  # Complex string with potential overlaps
            "229966347",     # Medium string
            "2996637",       # Short string
            "2967",          # Very short string
            "296"           # Minimal string
        ],
        "R6": [
            "668179932244",  # Complex string with multiple patterns
            "667993224",     # Medium string
            "6679932",       # Short string
            "6792",          # Very short string
            "692"           # Minimal string
        ],
        "R8": [
            "719983662244",  # Complex string with potential patterns
            "799366224",     # Medium string
            "7993662",       # Short string
            "7962",          # Very short string
            "962"           # Minimal string
        ]
    }
    
    # Test with multiple winning numbers
    test_numbers = ["468", "025"]
    
    print("\nTesting Enhanced Pattern Matching:")
    print("=" * 50)
    
    for number in test_numbers:
        print(f"\nAnalyzing patterns for: {number}")
        vtrac_index, winning_perms, related = find_vtrac_index_and_combos(number)
        
        print(f"V-TRAC Index: {vtrac_index}")
        print("Winning patterns:", sorted(winning_perms))
        
        for row_type, strings in sample_data.items():
            print(f"\n{row_type} Strings Analysis:")
            for s in strings:
                print(f"\nString: {s}")
                matches = find_patterns_in_row(s, winning_perms, related)
                
                if matches['winning']:
                    print("  Winning Matches:")
                    for match in sorted(matches['winning'], key=lambda x: x['position'][0]):
                        start, end = match['position']
                        print(f"    {match['pattern']} at position {start}-{end}")
                        print(f"    Context: {s[:start]}[{s[start:end]}]{s[end:]}")
                
                if matches['related']:
                    print("  Related Matches:")
                    for match in sorted(matches['related'], key=lambda x: x['position'][0]):
                        start, end = match['position']
                        print(f"    {match['pattern']} at position {start}-{end}")
                        print(f"    Context: {s[:start]}[{s[start:end]}]{s[end:]}")
                
                if not matches['winning'] and not matches['related']:
                    print("  No matches found")

def test_overlapping_patterns():
    """Test handling of overlapping patterns"""
    test_strings = [
        "468486",       # Two winning patterns next to each other
        "468468",       # Same winning pattern repeated
        "134468139",    # Related pattern before and after winning
        "468134486"     # Mix of winning and related patterns
    ]
    
    print("\nTesting Overlapping Pattern Handling:")
    print("=" * 50)
    
    number = "468"  # Use this as our test case
    vtrac_index, winning_perms, related = find_vtrac_index_and_combos(number)
    
    print(f"Testing with number: {number}")
    print(f"V-TRAC Index: {vtrac_index}")
    
    for s in test_strings:
        print(f"\nAnalyzing string: {s}")
        matches = find_patterns_in_row(s, winning_perms, related)
        
        if matches['winning']:
            print("  Winning Matches:")
            for match in sorted(matches['winning'], key=lambda x: x['position'][0]):
                start, end = match['position']
                print(f"    {match['pattern']} at position {start}-{end}")
                print(f"    Context: {s[:start]}[{s[start:end]}]{s[end:]}")
        
        if matches['related']:
            print("  Related Matches:")
            for match in sorted(matches['related'], key=lambda x: x['position'][0]):
                start, end = match['position']
                print(f"    {match['pattern']} at position {start}-{end}")
                print(f"    Context: {s[:start]}[{s[start:end]}]{s[end:]}")

if __name__ == "__main__":
    print("Running Enhanced V-TRAC Tests")
    print("=" * 50)
    
    test_pattern_extraction()
    print("\n" + "=" * 50)
    
    test_pattern_matching()
    print("\n" + "=" * 50)
    
    test_overlapping_patterns() 