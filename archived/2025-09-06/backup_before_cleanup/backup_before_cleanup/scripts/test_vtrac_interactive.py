#!/usr/bin/env python
"""
Interactive V-TRAC Testing Program
"""

import os
import sys
import pandas as pd
from pathlib import Path

# Add scripts directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from utils.vtrac_utils import find_vtrac_index_and_combos
from vtrac.winner_highlighter import highlight_winners

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print program header"""
    print("\n" + "="*60)
    print("V-TRAC Pattern Testing Program")
    print("="*60)

def create_sample_data():
    """Create sample data for testing"""
    return pd.DataFrame({
        'Set': ['Set1', 'Set1', 'Set1', 'Set1', 'Set1'],
        'Draw': ['Draw1', 'Draw2', 'Draw3', 'Draw4', 'Draw5'],
        'RowType': ['R2', 'R2', 'R2', 'R2', 'R2'],
        '7': ['123456', '234567', '345678', '456789', '567890'],
        '6': ['12345', '23456', '34567', '45678', '56789'],
        '5': ['1234', '2345', '3456', '4567', '5678'],
        '4': ['123', '234', '345', '456', '567'],
        '3': ['12', '23', '34', '45', '56'],
        '2': ['1', '2', '3', '4', '5'],
        '1': ['0', '1', '2', '3', '4']
    })

def show_vtrac_info(number):
    """Show V-TRAC information for a number"""
    print(f"\nAnalyzing number: {number}")
    print("-" * 40)
    
    index, winning_perms, related_combos = find_vtrac_index_and_combos(number)
    
    if index is not None:
        print(f"V-TRAC Index: {index}")
        print("\nWinning Permutations:")
        print(", ".join(sorted(winning_perms)))
        print("\nRelated Combinations:")
        # Print related combinations in rows of 10
        combos = sorted(related_combos)
        for i in range(0, len(combos), 10):
            print(", ".join(combos[i:i+10]))
    else:
        print("Number not found in V-TRAC reference")

def main():
    """Main interactive loop"""
    clear_screen()
    print_header()
    
    # Load sample data
    df = create_sample_data()
    print("\nSample data loaded successfully!")
    print(f"Table shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    while True:
        print("\n" + "="*60)
        print("\nOptions:")
        print("1. Enter a number to test")
        print("2. Show current data")
        print("3. Clear screen")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            number = input("\nEnter a 3-digit number to test: ").strip()
            if not (number.isdigit() and len(number) == 3):
                print("\n❌ Please enter a valid 3-digit number")
                continue
            
            # Show V-TRAC information
            show_vtrac_info(number)
            
            # Show highlighted table
            print("\nHighlighted Table:")
            print("-" * 40)
            highlighted = highlight_winners(df, number)
            print(highlighted)
            
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\nCurrent Data:")
            print("-" * 40)
            print(df)
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            clear_screen()
            print_header()
            
        elif choice == '4':
            print("\nGoodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 