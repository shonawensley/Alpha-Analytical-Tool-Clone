"""
combined_view.py

Provides a dryness ranking: how many draws since last double for each state
"""

from typing import Dict, List, Tuple, Set
import itertools

def get_doubles_history(all_states_draws):
    """
    Calculate how many draws since the last double for each state
    
    Args:
        all_states_draws: dict of state_name -> list of (date, draw) tuples
            Each list is ordered with newest draws first (index 0)
            
    Returns:
        dict: state_name -> dryness_count
    """
    dryness = {}
    for state, draws_list in all_states_draws.items():
        # Extract just the draws (not dates)
        draws = [draw for _, draw in draws_list]
        
        # Default to total length if no double is found
        dryness_count = len(draws)
        
        # Check each draw for a double (repeated digit)
        for i, draw in enumerate(draws):
            # Check if it's a double (any two digits match)
            if draw[0] == draw[1] or draw[1] == draw[2] or draw[0] == draw[2]:
                dryness_count = i  # i = 0 means current draw has a double
                break
                
        dryness[state] = dryness_count
        
    return dryness

def get_latest_double(all_states_draws):
    """
    Get the latest double for each state
    
    Args:
        all_states_draws: dict of state_name -> list of (date, draw) tuples
            
    Returns:
        dict: state_name -> latest double (or None if no double found)
    """
    latest_doubles = {}
    
    for state, draws_list in all_states_draws.items():
        draws = [draw for _, draw in draws_list]
        
        # Check each draw for a double
        for draw in draws:
            if draw[0] == draw[1] or draw[1] == draw[2] or draw[0] == draw[2]:
                latest_doubles[state] = draw
                break
        else:
            # No double found
            latest_doubles[state] = None
    
    return latest_doubles

def build_combined_ranking(all_states_draws):
    """
    Build a ranking of states by dryness (draws since last double)
    
    Args:
        all_states_draws: dict of state_name -> list of (date, draw) tuples
            
    Returns:
        list: List of (state_name, dryness_count) tuples, sorted by dryness (desc)
    """
    dryness = get_doubles_history(all_states_draws)
    
    # Sort by dryness (descending)
    ranking = sorted(dryness.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

def get_top_pairs_for_all_states(all_states_draws, n=5):
    """
    Get the top N most overdue repeating pairs for each state
    
    Args:
        all_states_draws: dict of state_name -> list of (date, draw) tuples
        n: Number of top pairs to return for each state
        
    Returns:
        dict: state_name -> [(pair, draws_since), ...]
    """
    from auxiliary.pair_analysis import calculate_overdue_pairs
    
    result = {}
    
    for state, draws_list in all_states_draws.items():
        # Need at least some draws to analyze
        if not draws_list:
            result[state] = []
            continue
        
        # Extract just the draws (no dates)
        draws = [draw for _, draw in draws_list]
        
        # Calculate overdue pairs
        _, repeating, pair_status = calculate_overdue_pairs(draws_list)
        
        # Get top repeating pairs
        repeating_pairs = []
        for color in ["RED", "BLUE", "PURPLE"]:
            for pair in repeating.get(color, []):
                repeating_pairs.append((pair, pair_status[pair]["draws_since"]))
        
        # Sort by draws_since (descending)
        repeating_pairs.sort(key=lambda x: x[1], reverse=True)
        
        # Get top N
        result[state] = repeating_pairs[:n]
    
    return result

def find_related_combos(pairs, all_combos):
    """
    Find combinations that contain the given pairs
    
    Args:
        pairs: List of pairs to check
        all_combos: Dictionary of all combinations, boxed by index
        
    Returns:
        Set of combinations that contain at least one of the pairs
    """
    related_combos = set()
    pairs_set = {p for p, _ in pairs}
    
    # Check all indices and their combinations
    for entry in all_combos:
        idx = entry["Index"]
        singles = entry.get("Singles", [])
        doubles = entry.get("Doubles", [])
        
        # Check each combo
        for combo in singles + doubles:
            # Get all pairs from this combo
            d1, d2, d3 = combo[0], combo[1], combo[2]
            combo_pairs = {
                ''.join(sorted(d1+d2)),
                ''.join(sorted(d2+d3)),
                ''.join(sorted(d1+d3))
            }
            
            # If any pair matches our target pairs, add the combo
            if combo_pairs.intersection(pairs_set):
                related_combos.add(combo)
    
    return related_combos

def get_related_combos_for_all_states(all_states_top_pairs, boxed_reference):
    """
    Get combinations related to the top pairs for each state
    
    Args:
        all_states_top_pairs: dict of state_name -> [(pair, draws_since), ...]
        boxed_reference: The BOXED_VTRAC_REFERENCE with all combinations
        
    Returns:
        dict: state_name -> set of related combinations
    """
    result = {}
    
    for state, pairs in all_states_top_pairs.items():
        result[state] = find_related_combos(pairs, boxed_reference)
    
    return result

def generate_dryness_html_table(all_states_draws):
    """
    Generate an HTML table showing the dryness ranking
    
    Args:
        all_states_draws: dict of state_name -> list of (date, draw) tuples
            
    Returns:
        str: HTML string with the ranking table
    """
    from scripts.utils.vtrac_utils import BOXED_VTRAC_REFERENCE
    
    dryness = get_doubles_history(all_states_draws)
    top_pairs_by_state = get_top_pairs_for_all_states(all_states_draws, 5)
    related_combos_by_state = get_related_combos_for_all_states(top_pairs_by_state, BOXED_VTRAC_REFERENCE)
    
    # Sort by dryness (descending)
    ranking = sorted(dryness.items(), key=lambda x: x[1], reverse=True)
    
    html = []
    html.append('<h2>Combined State Analysis</h2>')
    html.append('<table border="1" style="border-collapse: collapse; width: 100%;">')
    html.append('<tr style="background-color: #f2f2f2;">')
    html.append('<th style="padding: 8px; text-align: center;">Rank</th>')
    html.append('<th style="padding: 8px; text-align: center;">State</th>')
    html.append('<th style="padding: 8px; text-align: center;">Draws Since Last Double</th>')
    html.append('<th style="padding: 8px; text-align: center;">Top Overdue Repeating Pairs</th>')
    html.append('<th style="padding: 8px; text-align: center;">Related Combinations</th>')
    html.append('</tr>')
    
    for rank, (state, dryness_count) in enumerate(ranking, 1):
        row_class = ""
        
        if dryness_count >= 50:
            row_class = ' style="background-color: #ffe6e6;"'  # Light red for very dry states
        elif dryness_count >= 25:
            row_class = ' style="background-color: #fff2e6;"'  # Light orange for somewhat dry states
        
        # Format top pairs
        pairs_html = []
        for pair, draws_since in top_pairs_by_state.get(state, []):
            if draws_since >= 107:  # Very Late threshold
                pairs_html.append(f'<span style="color: blue;">{pair} ({draws_since})</span>')
            elif draws_since >= 71:  # Late threshold
                pairs_html.append(f'<span style="color: red;">{pair} ({draws_since})</span>')
            elif draws_since >= 25:  # Pending threshold
                pairs_html.append(f'<span style="color: purple;">{pair} ({draws_since})</span>')
            else:
                pairs_html.append(f'{pair} ({draws_since})')
        
        # Format related combos
        combos_html = []
        for combo in sorted(related_combos_by_state.get(state, []))[:20]:  # Limit to 20 combos
            combos_html.append(combo)
        
        html.append(f'<tr{row_class}>')
        html.append(f'<td style="padding: 8px; text-align: center;">{rank}</td>')
        html.append(f'<td style="padding: 8px; text-align: left;">{state}</td>')
        html.append(f'<td style="padding: 8px; text-align: center;">{dryness_count}</td>')
        html.append(f'<td style="padding: 8px; text-align: left;">{", ".join(pairs_html) if pairs_html else "None"}</td>')
        html.append(f'<td style="padding: 8px; text-align: left;">{" ".join(combos_html) if combos_html else "None"}</td>')
        html.append('</tr>')
    
    html.append('</table>')
    
    # Add note
    html.append('<div style="margin-top: 1em; font-size: 0.9em;">')
    html.append('<p>Note: "Draws Since Last Double" counts how many draws since a draw with at least two identical digits last appeared.</p>')
    html.append('<p>"Related Combinations" are combinations that contain at least one of the top overdue repeating pairs.</p>')
    html.append('</div>')
    
    return "\n".join(html)

# Example usage
if __name__ == "__main__":
    from draw_extractor import get_all_state_draws
    from pair_analysis import get_top_overdue_repeating_pairs
    
    # Get draws for all states
    all_state_draws = get_all_state_draws(max_draws=1000)
    
    # Get top 5 repeating pairs for each state
    top_pairs = {}
    for state, draws in all_state_draws.items():
        top_pairs[state] = get_top_overdue_repeating_pairs(draws, top_n=5)
    
    # Build combined view HTML
    html = generate_dryness_html_table(all_state_draws)
    
    # Write to a file for testing
    import os
    os.makedirs("data/outputs/vtrac", exist_ok=True)
    with open("data/outputs/vtrac/combined_view_test.html", "w") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Combined State View Test</title>
        </head>
        <body>
            <h1>Combined State Analysis</h1>
            {html}
        </body>
        </html>
        """)
    
    print(f"Wrote test HTML to: data/outputs/vtrac/combined_view_test.html") 