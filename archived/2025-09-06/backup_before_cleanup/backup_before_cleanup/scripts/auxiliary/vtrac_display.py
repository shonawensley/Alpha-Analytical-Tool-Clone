"""
vtrac_display.py

Renders a "Boxed V-Trac" table with:
- color coding for each combo based on pair status
- underline if combo not in the last 1000 draws
"""

from typing import Set, Dict, List, Any
import sys
import os

# Add project root to path if needed
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import vtrac_utils from the correct location
try:
    from utils.vtrac_utils import BOXED_VTRAC_REFERENCE
except ImportError:
    # Fallback to direct implementation if import fails
    BOXED_VTRAC_REFERENCE = [
        {"Index": 1, "Singles": [], "Doubles": ["005", "055"]},
        {"Index": 2, "Singles": ["015", "056"], "Doubles": ["001", "006", "155", "556"]},
        {"Index": 3, "Singles": ["025", "057"], "Doubles": ["002", "007", "255", "557"]},
        {"Index": 4, "Singles": ["035", "058"], "Doubles": ["003", "008", "355", "558"]},
        {"Index": 5, "Singles": ["045", "059"], "Doubles": ["004", "009", "455", "559"]},
        {"Index": 6, "Singles": ["016", "156"], "Doubles": ["011", "066", "115", "566"]},
        {"Index": 7, "Singles": ["012", "017", "026", "067", "125", "157", "256", "567"], "Doubles": []},
        {"Index": 8, "Singles": ["013", "018", "036", "068", "135", "158", "356", "568"], "Doubles": []},
        {"Index": 9, "Singles": ["014", "019", "046", "069", "145", "159", "456", "569"], "Doubles": []},
        {"Index": 10, "Singles": ["027", "257"], "Doubles": ["022", "077", "225", "577"]},
        {"Index": 11, "Singles": ["023", "028", "037", "078", "235", "258", "357", "578"], "Doubles": []},
        {"Index": 12, "Singles": ["024", "029", "047", "079", "245", "259", "457", "579"], "Doubles": []},
        {"Index": 13, "Singles": ["038", "358"], "Doubles": ["033", "088", "335", "588"]},
        {"Index": 14, "Singles": ["034", "039", "048", "089", "345", "359", "458", "589"], "Doubles": []},
        {"Index": 15, "Singles": ["049", "459"], "Doubles": ["044", "099", "445", "599"]},
        {"Index": 16, "Singles": [], "Doubles": ["116", "166"]},
        {"Index": 17, "Singles": ["126", "167"], "Doubles": ["112", "117", "266", "667"]},
        {"Index": 18, "Singles": ["136", "168"], "Doubles": ["113", "118", "366", "668"]},
        {"Index": 19, "Singles": ["146", "169"], "Doubles": ["114", "119", "466", "669"]},
        {"Index": 20, "Singles": ["127", "267"], "Doubles": ["122", "177", "226", "677"]},
        {"Index": 21, "Singles": ["123", "128", "137", "178", "236", "268", "367", "678"], "Doubles": []},
        {"Index": 22, "Singles": ["124", "129", "147", "179", "246", "269", "467", "679"], "Doubles": []},
        {"Index": 23, "Singles": ["138", "368"], "Doubles": ["133", "188", "336", "688"]},
        {"Index": 24, "Singles": ["134", "139", "148", "189", "346", "369", "468", "689"], "Doubles": []},
        {"Index": 25, "Singles": ["149", "469"], "Doubles": ["144", "199", "446", "699"]},
        {"Index": 26, "Singles": [], "Doubles": ["227", "277"]},
        {"Index": 27, "Singles": ["237", "278"], "Doubles": ["223", "228", "377", "778"]},
        {"Index": 28, "Singles": ["247", "279"], "Doubles": ["224", "229", "477", "779"]},
        {"Index": 29, "Singles": ["238", "378"], "Doubles": ["233", "288", "337", "788"]},
        {"Index": 30, "Singles": ["234", "239", "248", "289", "347", "379", "478", "789"], "Doubles": []},
        {"Index": 31, "Singles": ["249", "479"], "Doubles": ["244", "299", "447", "799"]},
        {"Index": 32, "Singles": [], "Doubles": ["338", "388"]},
        {"Index": 33, "Singles": ["348", "389"], "Doubles": ["334", "339", "488", "889"]},
        {"Index": 34, "Singles": ["349", "489"], "Doubles": ["344", "399", "448", "899"]},
        {"Index": 35, "Singles": [], "Doubles": ["449", "499"]}
    ]

def get_combo_color(combo: str, pair_status: Dict[str, Dict]) -> str:
    """
    Determine the color for a combo based on its pairs' statuses.
    
    Args:
        combo: A 3-digit combo string
        pair_status: Dict mapping canonical pairs to their status info
        
    Returns:
        The highest priority color ('BLUE', 'RED', 'PURPLE', or None)
    """
    if len(combo) != 3:
        return None
    
    # Extract all possible pairs from this combo
    d1, d2, d3 = combo[0], combo[1], combo[2]
    raw_pairs = [d1+d2, d2+d3, d1+d3]
    
    colors = set()
    for raw_pair in raw_pairs:
        # Create canonical form (sorted digits)
        pair = ''.join(sorted(raw_pair))
        if pair in pair_status and pair_status[pair]["color"]:
            colors.add(pair_status[pair]["color"])
    
    # Return the highest priority color
    if "BLUE" in colors:
        return "BLUE"
    elif "RED" in colors:
        return "RED"
    elif "PURPLE" in colors:
        return "PURPLE"
    
    return None

def build_vtrac_table_html_simple(last_1000_set: Set[str], pair_status: Dict[str, Dict]) -> str:
    """
    A simplified and performance-optimized version of the V-TRAC table HTML builder
    
    Args:
        last_1000_set: Set of combos that appeared in the last 1000 draws
        pair_status: Dict of pair status info from calculate_overdue_pairs
        
    Returns:
        HTML string for the V-TRAC table
    """
    # Precompute color styles
    color_styles = {
        "RED": "color: red;",
        "BLUE": "color: blue;",
        "PURPLE": "color: purple;"
    }
    
    # Start with basic table structure
    html = [
        '<table border="1" style="border-collapse: collapse; width: 100%;">',
        '<tr style="background-color: #f2f2f2;">',
        '<th style="padding: 8px; text-align: center;">Index</th>',
        '<th style="padding: 8px; text-align: center;">Singles</th>',
        '<th style="padding: 8px; text-align: center;">Doubles</th>',
        '</tr>'
    ]
    
    # Process all entries in one go
    for entry in BOXED_VTRAC_REFERENCE:
        idx = entry["Index"]
        singles_list = entry.get("Singles", [])
        doubles_list = entry.get("Doubles", [])
        
        # Process singles
        single_strs = []
        for combo in singles_list:
            color = get_combo_color(combo, pair_status)
            style = color_styles.get(color, "")
            
            if combo not in last_1000_set:
                if style:
                    single_strs.append(f'<span style="{style}"><u>{combo}</u></span>')
                else:
                    single_strs.append(f'<u>{combo}</u>')
            else:
                if style:
                    single_strs.append(f'<span style="{style}">{combo}</span>')
                else:
                    single_strs.append(f'{combo}')
        
        # Process doubles
        double_strs = []
        for combo in doubles_list:
            color = get_combo_color(combo, pair_status)
            style = color_styles.get(color, "")
            
            if combo not in last_1000_set:
                if style:
                    double_strs.append(f'<span style="{style}"><u>{combo}</u></span>')
                else:
                    double_strs.append(f'<u>{combo}</u>')
            else:
                if style:
                    double_strs.append(f'<span style="{style}">{combo}</span>')
                else:
                    double_strs.append(f'{combo}')
        
        # Format cell content
        singles_content = '' if not single_strs else ' '.join(single_strs)
        doubles_content = '' if not double_strs else ' '.join(double_strs)
        
        # Add row to table
        html.append(f'<tr>')
        html.append(f'<td style="padding: 8px; text-align: center;">{idx}</td>')
        html.append(f'<td style="padding: 8px; text-align: left;">{singles_content}</td>')
        html.append(f'<td style="padding: 8px; text-align: left;">{doubles_content}</td>')
        html.append('</tr>')
    
    html.append('</table>')
    return "\n".join(html)

def generate_vtrac_display(draws_list):
    """
    Generate the V-Trac display with proper formatting.
    
    Args:
        draws_list: List of (date, draw) tuples, newest first
        
    Returns:
        HTML string for the V-Trac table
    """
    try:
        # Use local import to avoid circular imports
        from scripts.auxiliary.pair_analysis import combos_in_last_1000, calculate_overdue_pairs
        
        # Get combos from last 1000 draws
        last_1000 = combos_in_last_1000(draws_list)
        
        # Get pair status info for coloring
        _, _, pair_status = calculate_overdue_pairs(draws_list)
        
        # Use the simplified, optimized HTML builder
        html = build_vtrac_table_html_simple(last_1000, pair_status)
        return html
    except Exception as e:
        # Return error message as HTML
        return f'<div style="color: red; padding: 20px; border: 1px solid red;">Error generating V-TRAC display: {str(e)}</div>'

def format_pairs_display_simple(non_repeating, repeating, pair_status):
    """
    A simplified version of the pairs display to improve performance
    
    Args:
        non_repeating: Dict of non-repeating pairs by color
        repeating: Dict of repeating pairs by color
        pair_status: Dict of pair status info
        
    Returns:
        HTML string for the pairs display
    """
    html = ['<div style="padding: 10px;">']
    
    # Repeating Pairs (Doubles) section with minimal formatting
    html.append('<h3>Repeating Pairs (Doubles)</h3>')
    html.append('<div style="display: flex; flex-wrap: wrap;">')
    
    # RED Pairs
    html.append('<div style="margin-right: 30px;">')
    html.append('<p><strong>RED (Late) Pairs (≥71):</strong></p>')
    if repeating["RED"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in repeating["RED"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20 for performance
            html.append(f'<li style="color: red;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    # BLUE Pairs
    html.append('<div style="margin-right: 30px;">')
    html.append('<p><strong>BLUE (Very Late) Pairs (≥107):</strong></p>')
    if repeating["BLUE"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in repeating["BLUE"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20
            html.append(f'<li style="color: blue;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    # PURPLE Pairs
    html.append('<div>')
    html.append('<p><strong>PURPLE (Pending) Pairs (≥25):</strong></p>')
    if repeating["PURPLE"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in repeating["PURPLE"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20
            html.append(f'<li style="color: purple;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    html.append('</div>')  # Close flex container
    
    # Non-Repeating Pairs section with minimal formatting
    html.append('<h3>Non-Repeating Pairs</h3>')
    html.append('<div style="display: flex; flex-wrap: wrap;">')
    
    # RED Pairs
    html.append('<div style="margin-right: 30px;">')
    html.append('<p><strong>RED (Late) Pairs (≥37):</strong></p>')
    if non_repeating["RED"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in non_repeating["RED"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20
            html.append(f'<li style="color: red;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    # BLUE Pairs
    html.append('<div style="margin-right: 30px;">')
    html.append('<p><strong>BLUE (Very Late) Pairs (≥56):</strong></p>')
    if non_repeating["BLUE"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in non_repeating["BLUE"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20
            html.append(f'<li style="color: blue;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    # PURPLE Pairs
    html.append('<div>')
    html.append('<p><strong>PURPLE (Pending) Pairs (≥25):</strong></p>')
    if non_repeating["PURPLE"]:
        sorted_pairs = sorted([(pair, pair_status[pair]["draws_since"]) for pair in non_repeating["PURPLE"]], 
                              key=lambda x: x[1], reverse=True)
        html.append('<ul style="list-style-type: none; padding-left: 0;">')
        for pair, draws_since in sorted_pairs[:20]:  # Limit to top 20
            html.append(f'<li style="color: purple;">{pair} - {draws_since} draws</li>')
        html.append('</ul>')
    else:
        html.append('<p>None</p>')
    html.append('</div>')
    
    html.append('</div>')  # Close flex container
    html.append('</div>')  # Close outer container
    
    return "\n".join(html)

def format_pairs_display(non_repeating, repeating, pair_status):
    """
    Create a formatted HTML display of overdue pairs.
    
    Args:
        non_repeating: Dict of non-repeating pairs by color
        repeating: Dict of repeating pairs by color
        pair_status: Dict of pair status info
        
    Returns:
        HTML string for the pairs display
    """
    try:
        return format_pairs_display_simple(non_repeating, repeating, pair_status)
    except Exception as e:
        # Return error message as HTML
        return f'<div style="color: red; padding: 20px; border: 1px solid red;">Error generating pairs display: {str(e)}</div>'

# For backward compatibility
build_vtrac_table_html = build_vtrac_table_html_simple 