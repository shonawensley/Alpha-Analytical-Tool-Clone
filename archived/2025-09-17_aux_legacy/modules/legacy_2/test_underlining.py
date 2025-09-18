"""
Test script to verify VTRAC combo underlining logic.
"""
import sys
import os
import time

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import modules
from modules.vtrac_reference import BOXED_LABEL_LOOKUP, VTRAC_DISPLAY
from modules.analyze_pairs import combos_appeared_in_1000, get_vtrac_statuses

def test_underlining():
    """Test the underlining logic with sample data."""
    print("\n=== Testing VTRAC Underlining Logic ===\n")
    
    # Create sample draw history with specific combos
    # We'll include some combos from VTRAC index 2 and 3
    sample_draws = [
        "015",  # Single from index 2
        "501",  # Permutation of 015
        "051",  # Another permutation of 015
        "006",  # Double from index 2
        "060",  # Permutation of 006
        "025",  # Single from index 3
        "057",  # Single from index 3
        "002",  # Double from index 3
        "255"   # Double from index 3
    ]
    
    # First test the combos_appeared_in_1000 function
    found_boxed_combos = combos_appeared_in_1000(sample_draws)
    print(f"\nFound {len(found_boxed_combos)} unique boxed combos from sample draws")
    print(f"Found boxed combos: {sorted(list(found_boxed_combos))}")
    
    # Now get all unique combos from VTRAC_DISPLAY
    all_combos = set()
    for entry in VTRAC_DISPLAY:
        singles = entry["Singles"].split() if entry["Singles"] else []
        doubles = entry["Doubles"].split() if entry["Doubles"] else []
        all_combos.update(singles)
        all_combos.update(doubles)
    
    # Calculate which combos should be underlined (not found in sample draws)
    underline_combos = set()
    for combo in all_combos:
        if combo not in found_boxed_combos:
            underline_combos.add(combo)
    
    print(f"\nTotal combos in VTRAC display: {len(all_combos)}")
    print(f"Combos NOT found (should be underlined): {len(underline_combos)}")
    
    # Test the vtrac_statuses function
    vtrac_statuses = get_vtrac_statuses(sample_draws, sample_draws)
    
    # Check index 2 (should have 015 and 006 without underline, but 056, 001, 155, 556 with underline)
    status_index_2 = vtrac_statuses.get(2, {})
    
    print("\nChecking VTRAC Index 2:")
    print(f"  Appeared: {status_index_2.get('appeared', False)}")
    
    print("\n  Singles Status:")
    singles_status = status_index_2.get("singles_status", {})
    for combo, status in singles_status.items():
        underline = status.get("underline", False)
        print(f"    {combo}: underline={underline}")
    
    print("\n  Doubles Status:")
    doubles_status = status_index_2.get("doubles_status", {})
    for combo, status in doubles_status.items():
        underline = status.get("underline", False)
        print(f"    {combo}: underline={underline}")
    
    # Check index 3 (should have 025, 057, 002, 255 without underline, but 007, 557 with underline)
    status_index_3 = vtrac_statuses.get(3, {})
    
    print("\nChecking VTRAC Index 3:")
    print(f"  Appeared: {status_index_3.get('appeared', False)}")
    
    print("\n  Singles Status:")
    singles_status = status_index_3.get("singles_status", {})
    for combo, status in singles_status.items():
        underline = status.get("underline", False)
        print(f"    {combo}: underline={underline}")
    
    print("\n  Doubles Status:")
    doubles_status = status_index_3.get("doubles_status", {})
    for combo, status in doubles_status.items():
        underline = status.get("underline", False)
        print(f"    {combo}: underline={underline}")

if __name__ == "__main__":
    test_underlining() 