#!/usr/bin/env python
"""
test_vtrac_terminal.py - Interactive terminal testing for V-TRAC pattern highlighting
"""

import os
import sys
from vtrac_utils import (
    find_vtrac_index_and_combos,
    find_all_patterns_in_string,
    find_patterns_in_row
)

def print_colored(text, color):
    """Print colored text in terminal"""
    colors = {
        'red': '\033[91m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'reset': '\033[0m',
        'bold': '\033[1m'
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def highlight_patterns_in_string(string, patterns, color='red'):
    """Highlight patterns in a string with colored brackets"""
    colors = {
        'red': '\033[91m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'reset': '\033[0m',
        'bold': '\033[1m'
    }
    result = string
    # Sort patterns by length (longest first) to avoid overlapping matches
    sorted_patterns = sorted(patterns, key=len, reverse=True)
    
    for pattern in sorted_patterns:
        start = 0
        while True:
            pos = string.find(pattern, start)
            if pos == -1:
                break
            # Replace the pattern with colored version
            result = result[:pos] + f"{colors[color]}[{pattern}]{colors['reset']}" + result[pos + len(pattern):]
            start = pos + len(pattern)
    
    return result

def test_pattern_highlighting(vtrac_index):
    """Test pattern highlighting in combined table strings"""
    print("\n" + "=" * 80)
    print_colored(f"Testing pattern highlighting for V-TRAC Index: {vtrac_index}", 'green')
    print("=" * 80)
    
    # Sample combined table data (from your actual data)
    combined_data = {
        "R2": ['552240088677', '55224008867', '552400886', '52400886', '540086', '540086', '5086'],
        "R4": ['225500688477', '22550068847', '255006884', '25006884', '500684', '500684', '5068'],
        "R6": ['688770055224', '68870055224', '688005524', '68800524', '680054', '680054', '6805'],
        "R8": ['770088622455', '70088622455', '008862455', '00886245', '008645', '008645', '0865']
    }
    
    # Get patterns for this V-TRAC index
    _, winning_patterns, related_patterns = find_vtrac_index_and_combos(str(vtrac_index))
    
    print("\nWinning Patterns to Highlight:")
    print_colored(str(winning_patterns), 'red')
    print("\nRelated Patterns to Highlight:")
    print_colored(str(related_patterns), 'blue')
    
    print("\nHighlighting in Combined Table Strings:")
    print("-" * 80)
    
    for row_type, strings in combined_data.items():
        print(f"\n{row_type} Strings:")
        for i, string in enumerate(strings):
            # Highlight winning patterns in red
            highlighted = highlight_patterns_in_string(string, winning_patterns, 'red')
            # Highlight related patterns in blue
            highlighted = highlight_patterns_in_string(highlighted, related_patterns, 'blue')
            print(f"String {i+1}: {highlighted}")

def interactive_test():
    """Interactive testing mode"""
    while True:
        print("\n" + "=" * 80)
        print("Interactive V-TRAC Pattern Highlighting Test")
        print("=" * 80)
        print("\nOptions:")
        print("1. Test with V-TRAC index")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            try:
                index = int(input("\nEnter V-TRAC index to test: "))
                test_pattern_highlighting(index)
            except ValueError:
                print("\nPlease enter a valid number")
        
        elif choice == "2":
            print("\nExiting...")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If index provided as argument, run direct test
        try:
            index = int(sys.argv[1])
            test_pattern_highlighting(index)
        except ValueError:
            print("Please provide a valid V-TRAC index number")
    else:
        # Otherwise run interactive mode
        interactive_test() 