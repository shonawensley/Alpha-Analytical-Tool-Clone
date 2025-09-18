"""
pair_analysis.py

Implements:
1) Overdue pair detection (non-repeating & repeating)
2) Color-coded thresholds (RED, BLUE, PURPLE)
3) Top 5 overdue repeating pairs
4) combos_in_last_1000(...) for the underline logic
"""

import itertools
from typing import Dict, List, Tuple, Set

# Overdue thresholds
OVERDUE_THRESHOLDS = {
    'non_repeating': {'RED': 37, 'BLUE': 56, 'PURPLE': 25},
    'repeating':     {'RED': 71, 'BLUE': 107, 'PURPLE': 25},
}

def calculate_overdue_pairs(draws_list):
    """
    Args:
      draws_list: list of (date, draw) tuples, newest first
    Returns:
      (nonrep, rep, pair_status) tuple:
        nonrep => { "RED":[pairs], "BLUE":[pairs], "PURPLE":[pairs] }
        rep => same structure
        pair_status => { pair: { 'draws_since': X, 'color': 'RED'/'BLUE'/'PURPLE' } }
    """
    # Extract only the draw strings (ignore dates)
    draws = [draw for _, draw in draws_list]
    
    total_draws = len(draws)
    # pair -> index of last seen (0=newest)
    pair_last_seen = {}

    # We'll iterate from oldest to newest so final index=0 is the newest
    for i in range(total_draws-1, -1, -1):
        d = draws[i]
        # create 2-digit pairs in sorted form
        p1 = ''.join(sorted(d[0:2]))
        p2 = ''.join(sorted(d[1:3]))
        p3 = ''.join(sorted([d[0], d[2]]))
        for p in (p1, p2, p3):
            pair_last_seen[p] = i

    pair_status = {}
    for p, last_seen_i in pair_last_seen.items():
        skip = last_seen_i  # if last_seen_i=0 => skip=0 => pair found in newest
        repeating = (p[0] == p[1])
        if repeating:
            thr = OVERDUE_THRESHOLDS['repeating']
        else:
            thr = OVERDUE_THRESHOLDS['non_repeating']

        color = None
        if skip >= thr['BLUE']:
            color = "BLUE"
        elif skip >= thr['RED']:
            color = "RED"
        elif skip >= thr['PURPLE']:
            color = "PURPLE"

        pair_status[p] = {"draws_since": skip, "color": color}

    nonrep = {"RED": [], "BLUE": [], "PURPLE": []}
    rep    = {"RED": [], "BLUE": [], "PURPLE": []}

    for p, st in pair_status.items():
        c = st["color"]
        if c:
            if p[0] == p[1]:
                rep[c].append(p)
            else:
                nonrep[c].append(p)

    return nonrep, rep, pair_status

def get_top_overdue_repeating_pairs(draws_list, top_n=5):
    """
    Returns list of (pair, skip) sorted by skip desc, up to top_n, only repeating pairs.
    
    Args:
        draws_list: list of (date, draw) tuples, newest first
        top_n: Number of top pairs to return
        
    Returns:
        List of (pair, draws_since) tuples
    """
    _, rep, all_info = calculate_overdue_pairs(draws_list)
    # gather repeating pairs from all_info
    repeating_pairs = []
    for p, st in all_info.items():
        if p[0] == p[1]:
            repeating_pairs.append((p, st["draws_since"]))
    # sort
    repeating_pairs.sort(key=lambda x: x[1], reverse=True)
    return repeating_pairs[:top_n]

def combos_in_last_1000(draws_list):
    """
    Return a set of all permutations from up to last 1000 draws (newest is index 0).
    This helps with 'underline' logic for combos not in the last 1000 draws.
    
    Args:
        draws_list: list of (date, draw) tuples, newest first
        
    Returns:
        Set of strings representing all 3-digit permutations from draws
    """
    # Extract just the draw strings (ignore dates)
    draws = [draw for _, draw in draws_list]
    
    # Take up to 1000 draws
    subset = draws[:1000]  
    appeared = set()
    
    for draw_str in subset:
        perms = set(itertools.permutations(draw_str, 3))
        for perm in perms:
            appeared.add("".join(perm))
    
    return appeared

def extract_pairs_from_draw(draw):
    """
    Extract all 2-digit pairs from a 3-digit draw in canonical (sorted) form.
    
    Args:
        draw (str): A 3-digit string (e.g., '123')
        
    Returns:
        list: List of sorted 2-digit pairs (e.g., ['12', '13', '23'])
    """
    if not isinstance(draw, str) or len(draw) != 3:
        return []
        
    # Extract digits
    digits = list(draw)
    
    # Create sorted pairs
    pair1 = ''.join(sorted([digits[0], digits[1]]))
    pair2 = ''.join(sorted([digits[1], digits[2]]))
    pair3 = ''.join(sorted([digits[0], digits[2]]))
    
    return [pair1, pair2, pair3]

def build_pairs_table(draws, analysis_window=100):
    """
    Build a table of draws since each pair was last seen.
    
    Args:
        draws (list): List of 3-digit draw strings, newest first
        analysis_window (int): Number of recent draws to analyze
        
    Returns:
        list: List of dicts with 'Pair' and 'Draws Since' keys
    """
    _, _, pair_status = calculate_overdue_pairs(draws)
    
    # Create table data
    table = []
    for pair, info in pair_status.items():
        table.append({
            'Pair': pair,
            'Draws Since': info['draws_since'],
            'Color': info['color'],
            'Is Repeating': pair[0] == pair[1]
        })
    
    # Sort by draws_since (descending)
    table.sort(key=lambda x: x['Draws Since'], reverse=True)
    
    return table

def get_overdue_stats(draws, analysis_window=100):
    """
    Get summary statistics about overdue pairs.
    
    Args:
        draws (list): List of 3-digit draw strings, newest first
        analysis_window (int): Number of recent draws to analyze
        
    Returns:
        dict: Dictionary with summary statistics
    """
    non_repeating, repeating, _ = calculate_overdue_pairs(draws)
    
    # Count pairs in each category
    stats = {
        'non_repeating': {
            'RED': len(non_repeating['RED']),
            'BLUE': len(non_repeating['BLUE']),
            'PURPLE': len(non_repeating['PURPLE']),
            'total': len(non_repeating['RED']) + len(non_repeating['BLUE']) + len(non_repeating['PURPLE'])
        },
        'repeating': {
            'RED': len(repeating['RED']),
            'BLUE': len(repeating['BLUE']),
            'PURPLE': len(repeating['PURPLE']),
            'total': len(repeating['RED']) + len(repeating['BLUE']) + len(repeating['PURPLE'])
        }
    }
    
    return stats

# Example usage
if __name__ == "__main__":
    # Get sample draw data
    from draw_extractor import get_state_draws
    
    # Get data for Connecticut
    draws = get_state_draws("Connecticut4", max_draws=100)
    
    # Calculate overdue pairs
    non_repeating, repeating, pair_status = calculate_overdue_pairs(draws)
    
    # Print summary
    print("\nOverdue Non-Repeating Pairs:")
    for color, pairs in non_repeating.items():
        if pairs:
            print(f"{color}: {', '.join(pairs)}")
    
    print("\nOverdue Repeating Pairs:")
    for color, pairs in repeating.items():
        if pairs:
            print(f"{color}: {', '.join(pairs)}")
    
    # Get top 5 overdue repeating pairs
    top5 = get_top_overdue_repeating_pairs(draws)
    print("\nTop 5 Most Overdue Repeating Pairs:")
    for pair, draws_since in top5:
        print(f"{pair}: {draws_since} draws ago") 