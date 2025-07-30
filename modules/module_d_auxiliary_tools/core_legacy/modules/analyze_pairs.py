"""
Module for analyzing pairs and identifying overdue combinations.
"""

import os
from typing import Dict, List, Tuple, Set, Optional
import pandas as pd
import numpy as np
from modules.vtrac_reference import get_vtrac_index, VTRAC_DISPLAY, BOXED_VTRAC_REFERENCE, BOXED_LABEL_LOOKUP

# Thresholds for different overdue categories
THRESHOLD_LATE_NONREPEATING = 37  # Red for non-repeating pairs
THRESHOLD_LATE_REPEATING = 71     # Red for repeating pairs (doubles)
THRESHOLD_VERY_LATE_NONREPEATING = 56  # Blue for non-repeating pairs
THRESHOLD_VERY_LATE_REPEATING = 107    # Blue for repeating pairs
THRESHOLD_PENDING_LATE = 25       # Purple for any pairs

# Color codes for styling
COLOR_LATE = 'red'
COLOR_VERY_LATE = 'blue'
COLOR_PENDING = 'purple'


def extract_pairs(draw: str) -> Tuple[List[str], List[str]]:
    """
    Extracts pairs from a 3-digit draw, ensuring pairs are in canonical form (sorted).
    
    Args:
        draw: A 3-digit draw string (e.g., '123')
        
    Returns:
        Tuple of (non_repeating_pairs, repeating_pairs)
    """
    if len(draw) != 3:
        raise ValueError(f"Invalid draw value: {draw}. Expected 3 digits.")
    
    digit1, digit2, digit3 = draw[0], draw[1], draw[2]
    
    non_repeating_pairs = []
    repeating_pairs = []
    
    # Get the three pairs: (digit1,digit2), (digit2,digit3), (digit1,digit3)
    raw_pairs = [
        digit1 + digit2,
        digit2 + digit3,
        digit1 + digit3
    ]
    
    # Create canonical pairs (sorted digits) and categorize as non-repeating or repeating
    for raw_pair in raw_pairs:
        # Create canonical form by sorting digits
        pair = ''.join(sorted(raw_pair))
        
        if pair[0] == pair[1]:
            repeating_pairs.append(pair)
        else:
            non_repeating_pairs.append(pair)
    
    # Remove duplicates
    non_repeating_pairs = list(set(non_repeating_pairs))
    repeating_pairs = list(set(repeating_pairs))
    
    return non_repeating_pairs, repeating_pairs


def track_pairs(draws: List[str]) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Tracks the most recent appearance of each pair in the draw history.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        
    Returns:
        Tuple of (non_repeating_last_seen, repeating_last_seen) dicts mapping pairs to indices
    """
    # Initialize tracking dictionaries
    non_repeating_last_seen = {}
    repeating_last_seen = {}
    
    # Process draws from newest to oldest
    for i, draw in enumerate(draws):
        # Extract pairs from this draw
        non_repeating, repeating = extract_pairs(draw)
        
        # Update last seen indices for non-repeating pairs
        for pair in non_repeating:
            if pair not in non_repeating_last_seen:
                non_repeating_last_seen[pair] = i
        
        # Update last seen indices for repeating pairs
        for pair in repeating:
            if pair not in repeating_last_seen:
                repeating_last_seen[pair] = i
    
    return non_repeating_last_seen, repeating_last_seen


def calculate_overdue_pairs(draws: List[str]) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, str]]:
    """
    Calculates how many draws it's been since each pair was last seen.
    Properly handles all possible pairs and applies correct thresholds.
    
    Args:
        draws: List of 3-digit draw strings, most recent first (last 100 draws)
        
    Returns:
        Tuple of (non_repeating_overdue, repeating_overdue, pair_status)
    """
    # Initialize last_seen dictionary for all possible pairs with high default value
    last_seen = {}
    times_drawn = {}
    
    # Process draws from newest to oldest (draws[0] is newest)
    for i, draw in enumerate(draws):
        if len(draw) != 3:
            continue
            
        d1, d2, d3 = draw[0], draw[1], draw[2]
        raw_pairs = [d1+d2, d2+d3, d1+d3]
        
        for raw_pair in raw_pairs:
            # Create canonical form (sorted digits)
            pair = ''.join(sorted(raw_pair))
            
            # Count how many times each pair appears
            times_drawn[pair] = times_drawn.get(pair, 0) + 1
            
            # Track first occurrence (lowest index = most recent)
            if pair not in last_seen:
                last_seen[pair] = i
    
    # Generate all possible digit pairs (00-99 in canonical form)
    non_repeating_overdue = {}
    repeating_overdue = {}
    pair_status = {}
    
    # Debug counters
    red_count = 0
    blue_count = 0
    purple_count = 0
    
    for p in range(10):
        for q in range(p, 10):  # Start from p to avoid duplicates
            pair = f"{p}{q}"
            
            # If the pair was found in the draws, use its index
            # Otherwise, treat it as if it's max_draws overdue
            overdue_count = last_seen.get(pair, len(draws))
            times_seen = times_drawn.get(pair, 0)
            
            # Separate repeating and non-repeating pairs
            is_repeating = (pair[0] == pair[1])
            
            if is_repeating:
                repeating_overdue[pair] = overdue_count
                
                # Apply thresholds for repeating pairs
                if overdue_count >= THRESHOLD_VERY_LATE_REPEATING:
                    pair_status[pair] = COLOR_VERY_LATE
                    blue_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Repeating pair {pair} is BLUE (very late) with {overdue_count} draws overdue, seen {times_seen} times")
                elif overdue_count >= THRESHOLD_LATE_REPEATING:
                    pair_status[pair] = COLOR_LATE
                    red_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Repeating pair {pair} is RED (late) with {overdue_count} draws overdue, seen {times_seen} times")
                elif overdue_count >= THRESHOLD_PENDING_LATE:
                    pair_status[pair] = COLOR_PENDING
                    purple_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Repeating pair {pair} is PURPLE (pending) with {overdue_count} draws overdue, seen {times_seen} times")
            else:
                non_repeating_overdue[pair] = overdue_count
                
                # Apply thresholds for non-repeating pairs
                if overdue_count >= THRESHOLD_VERY_LATE_NONREPEATING:
                    pair_status[pair] = COLOR_VERY_LATE
                    blue_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Non-repeating pair {pair} is BLUE (very late) with {overdue_count} draws overdue, seen {times_seen} times")
                elif overdue_count >= THRESHOLD_LATE_NONREPEATING:
                    pair_status[pair] = COLOR_LATE
                    red_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Non-repeating pair {pair} is RED (late) with {overdue_count} draws overdue, seen {times_seen} times")
                elif overdue_count >= THRESHOLD_PENDING_LATE:
                    pair_status[pair] = COLOR_PENDING
                    purple_count += 1
                    # Debug output for verification
                    print(f"DEBUG: Non-repeating pair {pair} is PURPLE (pending) with {overdue_count} draws overdue, seen {times_seen} times")
    
    # Summary output
    print(f"DEBUG: Found {red_count} RED pairs, {blue_count} BLUE pairs, and {purple_count} PURPLE pairs")
    
    return non_repeating_overdue, repeating_overdue, pair_status


def get_top_overdue_repeating_pairs(draws: List[str], n: int = 5) -> List[Tuple[str, int]]:
    """
    Gets the top N most overdue repeating pairs.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        n: Number of top pairs to return
        
    Returns:
        List of tuples (pair, overdue_count) sorted by most overdue first
    """
    # Initialize tracking for all repeating pairs (00-99)
    last_seen = {}
    
    # Process draws from newest to oldest
    for i, draw in enumerate(draws):
        if len(draw) != 3:
            continue
            
        d1, d2, d3 = draw[0], draw[1], draw[2]
        raw_pairs = [d1+d2, d2+d3, d1+d3]
        
        for raw_pair in raw_pairs:
            # Create canonical form (sorted digits)
            pair = ''.join(sorted(raw_pair))
            
            # Only track repeating pairs
            if pair[0] == pair[1] and pair not in last_seen:
                last_seen[pair] = i
    
    # Create a list of all repeating pairs with their overdue counts
    repeating_pairs = []
    for digit in range(10):
        pair = f"{digit}{digit}"
        overdue_count = last_seen.get(pair, len(draws))
        repeating_pairs.append((pair, overdue_count))
    
    # Sort by overdue count (descending)
    repeating_pairs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N
    return repeating_pairs[:n]


def analyze_vtrac_hits(draws: List[str]) -> Dict[int, bool]:
    """
    Analyzes which V-Trac indices have appeared in the draw history.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        
    Returns:
        Dict mapping V-Trac indices to whether they've appeared
    """
    # Initialize with all indices as False (not appeared)
    vtrac_appeared = {i+1: False for i in range(35)}
    
    # Check each draw
    for draw in draws:
        # Skip triples
        if len(set(draw)) == 1:
            continue
            
        # Get V-Trac index
        index = get_vtrac_index(draw)
        if index is not None:
            vtrac_appeared[index] = True
    
    return vtrac_appeared


def combos_appeared_in_1000(draws_1000: List[str]) -> Set[str]:
    """
    Return a set of combos that appear in the last 1000 draws.
    
    Args:
        draws_1000: List of 3-digit draw strings, most recent first (up to 1000 draws)
        
    Returns:
        Set of unique 3-digit combos that have appeared
    """
    from modules.vtrac_reference import BOXED_LABEL_LOOKUP
    
    found_combos = set()
    
    # Get total unique boxed combo labels by checking length of unique values
    total_unique_labels = len(set(BOXED_LABEL_LOOKUP.values()))
    print(f"DEBUG: Total unique combos in VTRAC reference: {total_unique_labels}")
    print(f"DEBUG: Processing {len(draws_1000)} draws for combo appearance tracking")
    
    # Track skipped draws for diagnostics, but don't print each one
    skipped_triples = 0
    draws_without_label = 0
    
    # Check each draw in the history
    for draw in draws_1000:
        if len(draw) != 3:
            # Skip invalid draws without logging each one
            continue
        
        # Skip triples
        if len(set(draw)) == 1:
            skipped_triples += 1
            continue
        
        # Check if we have a direct match in BOXED_LABEL_LOOKUP
        if draw in BOXED_LABEL_LOOKUP:
            # ONLY add the specific boxed label for this draw
            found_combos.add(BOXED_LABEL_LOOKUP[draw])
        else:
            draws_without_label += 1
            # Only log occasionally to reduce output
            if draws_without_label % 100 == 1:
                print(f"DEBUG: Draw {draw} has no boxed label (total so far: {draws_without_label})")
    
    print(f"DEBUG: Skipped {skipped_triples} triples and {draws_without_label} draws without boxed label")
    print(f"DEBUG: Found {len(found_combos)} specific combos that appeared in the draw history")
    
    # Report how many combos were NOT found and should be underlined
    total_boxed_combos = total_unique_labels
    not_found = total_boxed_combos - len(found_combos)
    print(f"DEBUG: {not_found} combos were NOT found and should be underlined")
    
    if len(found_combos) < 10:
        print(f"DEBUG: WARNING - Very few combos found: {found_combos}")
    
    return found_combos


def get_combo_color(combo: str, pair_status: Dict[str, str]) -> str:
    """
    Determine the color for a combo based on its pairs' statuses.
    
    Args:
        combo: A 3-digit combo string
        pair_status: Dict mapping canonical pairs to their status color
        
    Returns:
        The highest priority color ('blue', 'red', 'purple', or '')
    """
    if len(combo) != 3:
        return ""
    
    d1, d2, d3 = combo[0], combo[1], combo[2]
    raw_pairs = [d1+d2, d2+d3, d1+d3]
    
    colors = set()
    for raw_pair in raw_pairs:
        # Create canonical form (sorted digits)
        pair = ''.join(sorted(raw_pair))
        color = pair_status.get(pair, '')
        if color:
            colors.add(color)
    
    # Return the highest priority color
    if COLOR_VERY_LATE in colors:
        return COLOR_VERY_LATE
    elif COLOR_LATE in colors:
        return COLOR_LATE
    elif COLOR_PENDING in colors:
        return COLOR_PENDING
    
    return ""


def get_vtrac_statuses(draws_100: List[str], draws_1000: Optional[List[str]] = None) -> Dict[int, Dict]:
    """
    Gets the status for each V-Trac index and its components.
    
    Args:
        draws_100: List of 3-digit draw strings, most recent first (last 100 draws)
        draws_1000: Optional list of draws for 1000-draw history check (for underlining)
        
    Returns:
        Dict mapping V-Trac indices to their status information
    """
    # Calculate overdue pairs from last 100 draws
    _, _, pair_status = calculate_overdue_pairs(draws_100)
    
    # Analyze V-Trac hits
    vtrac_appeared = analyze_vtrac_hits(draws_100)
    
    # Get combos that have appeared in the last 1000 draws (for underlining)
    if draws_1000 is None:
        draws_1000 = draws_100  # Use the same 100 draws if 1000 not provided
    
    appeared_combos = combos_appeared_in_1000(draws_1000)
    print(f"DEBUG: Found {len(appeared_combos)} specific combos that appeared in the draw history")
    
    # Get all unique combos from VTRAC_DISPLAY for reference
    all_combos = set()
    for entry in VTRAC_DISPLAY:
        singles = entry["Singles"].split() if entry["Singles"] else []
        doubles = entry["Doubles"].split() if entry["Doubles"] else []
        all_combos.update(singles)
        all_combos.update(doubles)
    
    # Calculate which combos should be underlined (not found in 1000 draws)
    underline_combos = []
    for combo in all_combos:
        if combo not in appeared_combos:
            underline_combos.append(combo)
    
    print(f"DEBUG: {len(underline_combos)} combos were NOT found and should be underlined: {underline_combos}")
    
    # Initialize results
    vtrac_statuses = {}
    
    # Process each V-Trac index
    for vtrac_entry in VTRAC_DISPLAY:
        index = vtrac_entry["Index"]
        singles = vtrac_entry["Singles"].split() if vtrac_entry["Singles"] else []
        doubles = vtrac_entry["Doubles"].split() if vtrac_entry["Doubles"] else []
        
        # Initialize status for this index
        vtrac_statuses[index] = {
            "appeared": vtrac_appeared[index],
            "singles_status": {},
            "doubles_status": {}
        }
        
        # Process singles
        for combo in singles:
            combo_status = {}
            
            # Get color based on the "worst" pair in this combo
            color = get_combo_color(combo, pair_status)
            if color:
                combo_status["color"] = color
            
            # Only underline combos that haven't appeared in 1000 draws
            if combo not in appeared_combos:
                combo_status["underline"] = True
            
            # Add combo status if we have any attributes
            if combo_status:
                vtrac_statuses[index]["singles_status"][combo] = combo_status
        
        # Process doubles
        for combo in doubles:
            combo_status = {}
            
            # Get color based on the "worst" pair in this combo
            color = get_combo_color(combo, pair_status)
            if color:
                combo_status["color"] = color
            
            # Only underline combos that haven't appeared in 1000 draws
            if combo not in appeared_combos:
                combo_status["underline"] = True
            
            # Add combo status if we have any attributes
            if combo_status:
                vtrac_statuses[index]["doubles_status"][combo] = combo_status
    
    return vtrac_statuses


def get_doubles_history(state_draws: Dict[str, List[str]]) -> Dict[str, int]:
    """
    Gets the number of draws since the last double for each state.
    
    Args:
        state_draws: Dict mapping state names to their draw histories
        
    Returns:
        Dict mapping state names to draws since last double
    """
    # Safety check - if no data, return empty dict
    if not state_draws:
        return {}
    
    results = {}
    
    for state, draws in state_draws.items():
        # Skip if no draws for this state
        if not draws:
            results[state] = 0
            continue
            
        print(f"DEBUG: Analyzing doubles for {state} with {len(draws)} draws")    
        
        # Initialize counter
        draws_since_double = 0
        found_double = False
        
        # Scan through draws until we find a double
        for i, draw in enumerate(draws):
            # Skip invalid draws
            if not draw or len(draw) != 3:
                continue
                
            # Is this a double? (has exactly 2 unique digits)
            if len(set(draw)) == 2:
                found_double = True
                # Log the position where we found the double
                print(f"DEBUG: Found double {draw} at position {i} for {state}")
                break
            draws_since_double += 1
        
        # If we didn't find a double in the entire history, set to a very high number
        if not found_double:
            draws_since_double = len(draws)
            print(f"DEBUG: State {state} has no doubles in the entire history ({draws_since_double} draws)")
        else:
            print(f"DEBUG: State {state} has {draws_since_double} draws since last double")
        
        results[state] = draws_since_double
    
    return results


def get_colored_pairs(draws: List[str]) -> Dict[str, List[str]]:
    """
    Returns a dictionary mapping each color (red, blue, purple) to a list of canonical pairs
    that have that overdue status based on the provided draws.
    
    Args:
        draws: List of 3-digit draw strings, most recent first
        
    Returns:
        Dict mapping color status to lists of pairs with that status
    """
    _, _, pair_status = calculate_overdue_pairs(draws)
    
    # Initialize result with empty lists
    colored_pairs = {
        COLOR_LATE: [],      # Red
        COLOR_VERY_LATE: [], # Blue
        COLOR_PENDING: []    # Purple
    }
    
    # Group pairs by their color status
    for pair, color in pair_status.items():
        colored_pairs[color].append(pair)
    
    # Sort each list for consistent output
    for color in colored_pairs:
        colored_pairs[color].sort()
    
    # Print debug info about colored pairs
    print(f"DEBUG: Found {len(colored_pairs[COLOR_LATE])} RED (late) pairs")
    print(f"DEBUG: Found {len(colored_pairs[COLOR_VERY_LATE])} BLUE (very late) pairs")
    print(f"DEBUG: Found {len(colored_pairs[COLOR_PENDING])} PURPLE (pending) pairs")
    
    # Print the specific pairs for verification
    print(f"DEBUG: RED pairs: {colored_pairs[COLOR_LATE]}")
    print(f"DEBUG: BLUE pairs: {colored_pairs[COLOR_VERY_LATE]}")
    print(f"DEBUG: PURPLE pairs: {colored_pairs[COLOR_PENDING]}")
    
    return colored_pairs 