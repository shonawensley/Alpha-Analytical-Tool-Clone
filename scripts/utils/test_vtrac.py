#!/usr/bin/env python
"""
test_vtrac.py - Standalone test script for V-TRAC functionality

This script allows testing V-TRAC features without modifying the main Streamlit app.
It provides simple command-line testing of:
1. V-TRAC index lookup
2. Finding winning permutations
3. Finding related combinations
"""

import os
import sys

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_root)

from vtrac_utils import find_vtrac_index_and_combos

def test_vtrac_lookup(numbers_to_test):
    """Test V-TRAC index lookup and pattern matching"""
    print("\n=== Testing V-TRAC Lookup ===")
    print("Testing numbers:", numbers_to_test)
    print("-" * 50)
    
    for num in numbers_to_test:
        print(f"\nTesting number: {num}")
        vtrac_index, winning_perms, related = find_vtrac_index_and_combos(num)
        print(f"V-TRAC Index: {vtrac_index}")
        print(f"Winning permutations: {sorted(winning_perms)}")
        print(f"Related combinations: {sorted(related)}")
        print("-" * 30)

def main():
    # Test cases
    test_numbers = [
        "123",  # Simple ascending
        "321",  # Simple descending
        "111",  # All same digits
        "147",  # Mixed digits
        "258",  # Another pattern
        "369"   # Another pattern
    ]
    
    test_vtrac_lookup(test_numbers)
    
    # Allow interactive testing
    while True:
        print("\nEnter a 3-digit number to test (or 'q' to quit):")
        user_input = input().strip()
        
        if user_input.lower() == 'q':
            break
            
        if len(user_input) != 3 or not user_input.isdigit():
            print("Please enter exactly 3 digits")
            continue
            
        test_vtrac_lookup([user_input])

if __name__ == "__main__":
    main() 