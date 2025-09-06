#!/usr/bin/env python
"""
stable_pattern_extractor_full.py

A single, comprehensive Python file for extracting advanced "stable patterns"
from your "combined table" JSON data (R2/R4/R6/R8 structures),
scoring them with a variety of bonuses (3-value check, V-Trac,
hot zones, mirror, consensus, horizontal & lingering coverage,
order-persistence across consecutive draws), PLUS these new upgrades:

 1) Consensus Digit Bonus: If a column has a consensus digit(s),
    any stable pattern containing those digit(s) gets extra points.
 2) Remaining 3-Value Indicator: If the column has exactly one stable pattern,
    it gets a special bonus.
 3) Multi-Row Straight Enhancement: If a pattern is repeated identically
    in all 4 row types (R2,R4,R6,R8), extra bonus.
 4) Nested Cluster Bonus: If the cluster itself contains smaller sub-clusters
    that are also 3-value, add a small extra bonus.
 5) Dynamic Hot Zone + Consensus Synergy: If a pattern is in a hot zone,
    AND there's a consensus, we give an additional synergy bonus.
 6) Explicit Logging: We attach sub-bonus details in "debug_info" for
    clarity/future ML reference.

Usage:
   python stable_pattern_extractor_full.py path/to/lottery_data.json
"""

import sys
import os
import json
import re
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

# Define MAX_COL constant as requested
MAX_COL = 7

########################################################################
# PART A: HELPER FUNCTIONS
########################################################################

# V-Trac mapping
VTRAC_MAP = {
    '0':'1','5':'1',
    '1':'2','6':'2',
    '2':'3','7':'3',
    '3':'4','8':'4',
    '4':'5','9':'5'
}

def to_vtrac(num_str):
    """Convert digit string to its V-Trac representation (0->1 or 5->1, etc.)."""
    return "".join(VTRAC_MAP.get(ch,'') for ch in num_str)

def is_3value_pattern(cluster):
    """
    Return True if cluster has <=3 unique digits in actual
    OR <=3 unique digits in V-Trac.
    """
    actual_unique = set(cluster)
    if len(actual_unique) <= 3:
        return True
    vtrac_unique = set(to_vtrac(cluster))
    return len(vtrac_unique) <= 3

def canonical_form(pattern_str):
    """
    Return sorted version of the digit string (e.g. '731' -> '137').
    Helps unify permutations as the same "box" form.
    """
    return ''.join(sorted(pattern_str))

def has_mirror_digits(pattern_str):
    """
    Check if pattern has any mirror pair: (0,5), (1,6), (2,7), (3,8), (4,9).
    e.g. '105' => True, because it has '0' and '5'.
    """
    mirror_pairs = [('0','5'),('1','6'),('2','7'),('3','8'),('4','9')]
    for a,b in mirror_pairs:
        if a in pattern_str and b in pattern_str:
            return True
    return False

def long_cluster_bonus(cluster_str):
    """
    Extra bonus for stable clusters ≥5 digits
    (e.g. length=5 => +2, length=6 => +4, etc.).
    """
    length = len(cluster_str)
    return max(0, (length - 4)*2) if length >=5 else 0

def detect_consensus(r2_str, r4_str, r6_str, r8_str):
    """
    Check if R2/R4/R6/R8 share the same 1-2 digit substring => "consensus".
    Return that substring if found, else None.
    Example: if r2_str='88', r4_str='88', r6_str='88', r8_str='88' => '88'
    Must be 1 or 2 digits, and all must match exactly.
    """
    def strip_stars(s): return re.sub(r'\*+','', s or '')
    s2 = strip_stars(r2_str)
    s4 = strip_stars(r4_str)
    s6 = strip_stars(r6_str)
    s8 = strip_stars(r8_str)
    if (1 <= len(s2) <= 2) and (s2==s4==s6==s8):
        return s2
    return None

def nested_cluster_bonus(cluster_str):
    """
    Bonus for containing nested 3-value patterns.
    We'll do a small pass checking sub-substrings
    that are also 3-value. Each found => +1
    """
    bonus = 0
    L = len(cluster_str)
    for start in range(L):
        for end in range(start+3, L+1):
            subc = cluster_str[start:end]
            if is_3value_pattern(subc):
                bonus += 1
    # We might reduce it if it's too large, e.g. for very big strings
    return bonus

def dynamic_hot_consensus_bonus(hot_zone_points, consensus_val):
    """
    If there's a hot zone (hot_zone_points > 0) AND we have consensus_val,
    we add synergy.
    e.g. synergy = +2 if only one present, +4 if both present strongly
    For simplicity:
      if both => +4
      else => 0
    """
    if hot_zone_points>0 and consensus_val:
        return 4
    return 0

def evaluate_boxed_vs_straight(rows_map):
    """
    rows_map: dict of row_type-> cluster_str
    Return (straight_bonus, box_bonus).

    We also incorporate 'multi-row-straight' if all 4 are identical.
    """
    if not rows_map:
        return 0, 0
    row_vals = list(rows_map.values())
    # Count exact duplicates
    c_straight = Counter(row_vals)
    # normal "straight repeat" bonus
    straight_bonus = 0
    for s, count in c_straight.items():
        if count > 1:
            # each extra repeat => +3
            straight_bonus += (count-1)*3

    # multi-row straight => if any pattern is repeated EXACTLY in all 4 rows => +5
    if len(c_straight) == 1 and len(row_vals)==4:
        # means all row_vals are identical
        # Check if the single pattern count is 4
        most_common = c_straight.most_common(1)
        if most_common and most_common[0][1] == 4:
            straight_bonus += 5

    # Distinct box forms
    c_box = Counter(canonical_form(x) for x in row_vals)
    box_bonus = len(c_box)
    return straight_bonus, box_bonus


########################################################################
# PART B: ADVANCED STABLE-PATTERN EXTRACTOR
########################################################################

def extract_column_patterns(r2_str, r4_str, r6_str, r8_str,
                            hot_indicators=None, check_consensus=True):
    """
    Extract stable patterns (3-value) from one "column" of R2/R4/R6/R8 strings.
    Return dict { canonical_pattern: { "rows":..., "score":..., "debug_info":{...} } }

    We'll:
      1) Identify all 3-value digit substrings (≥3 length).
      2) Score them by coverage, vtrac strength, mirror, length, box/straight,
         nested sub-clusters, consensus digit presence, hot zone synergy, etc.
    """
    def remove_stars(s):
        return re.sub(r'\*+','', s or '')
    row_data = {
        "R2": r2_str or "",
        "R4": r4_str or "",
        "R6": r6_str or "",
        "R8": r8_str or ""
    }
    row_clean = {rt: remove_stars(val) for rt,val in row_data.items()}

    # check if there's a consensus substring
    consensus_val = None
    if check_consensus:
        consensus_val = detect_consensus(r2_str, r4_str, r6_str, r8_str)

    # pass 1: find all clusters
    patterns_in_col = defaultdict(lambda: {"rows":{}})
    for rt,clean_str in row_clean.items():
        L = len(clean_str)
        for start in range(L):
            for end in range(start+3, L+1):
                sub = clean_str[start:end]
                if is_3value_pattern(sub):
                    cpat = canonical_form(sub)
                    patterns_in_col[cpat]["rows"][rt] = sub

    result_for_col = {}

    # pass 2: compute coverage-based, etc.
    # (We'll see below if there's exactly 1 pattern => "remaining_3value")

    for can_pat, info in patterns_in_col.items():
        row_map = info["rows"]
        coverage = len(row_map)  # vertical coverage
        coverage_score = coverage*2
        perm_strength = len(set(row_map.values()))
        vtrac_strength = 2 if len(set(to_vtrac(can_pat)))<=2 else 1
        mirror_b = 2 if has_mirror_digits(can_pat) else 0
        sb, bb = evaluate_boxed_vs_straight(row_map)
        longest_sub = ""
        if row_map: # Check if row_map is not empty
            longest_sub = max(row_map.values(), key=len)

        length_b = long_cluster_bonus(longest_sub)
        # hot zone
        hot_b = 0
        if hot_indicators:
            for rt,subval in row_map.items():
                if rt in hot_indicators and hot_indicators[rt]:
                    if hot_indicators[rt]=='**':
                        hot_b+=3
                    else:
                        hot_b+=2

        # nested clusters
        nest_b = nested_cluster_bonus(longest_sub)

        # consensus digit bonus => check if can_pat includes any digit from consensus_val
        cons_digit_bonus = 0
        if consensus_val:
            # we interpret consensus_val as the substring => e.g. '88'
            # if any digit in that substring is also in can_pat => +3
            set_cons = set(consensus_val)
            set_pat = set(can_pat)  # canonical form = sorted digits
            if set_cons & set_pat:
                cons_digit_bonus += 3

        # synergy hot zone + consensus
        synergy_b = dynamic_hot_consensus_bonus(hot_b, consensus_val)

        # sum
        base_score = coverage_score + perm_strength + vtrac_strength + mirror_b + sb + bb + length_b + hot_b
        total_score = base_score + nest_b + cons_digit_bonus + synergy_b

        # store debug info
        debug_info = {
            "vertical_coverage": coverage,
            "permutation_strength": perm_strength,
            "vtrac_strength": vtrac_strength,
            "mirror_bonus": mirror_b,
            "straight_bonus": sb,
            "box_bonus": bb,
            "length_bonus": length_b,
            "hot_zone_points": hot_b,
            "nested_cluster_bonus": nest_b,
            "consensus_digit_bonus": cons_digit_bonus,
            "hot_zone_consensus_synergy": synergy_b
        }

        result_for_col[can_pat] = {
            "rows": row_map,
            "score": total_score,
            "debug_info": debug_info
        }

    # pass 3: if exactly 1 pattern => "remaining 3-value" => +4
    if len(result_for_col)==1:
        only_pat = next(iter(result_for_col))
        result_for_col[only_pat]["score"] += 4
        result_for_col[only_pat]["debug_info"]["remaining_3value_bonus"] = 4

    return result_for_col

def horizontal_persistence_scoring(col_list):
    """
    If the same pattern canonical appears in consecutive columns,
    add +2 each time it persists. Affects the score of the earlier column.
    """
    for i in range(len(col_list)-1):
        curr_dict = col_list[i]
        next_dict = col_list[i+1]
        overlap = set(curr_dict.keys()).intersection(set(next_dict.keys()))
        for pat in overlap:
            # Check if 'score' exists before incrementing
            if pat in curr_dict and 'score' in curr_dict[pat]:
                curr_dict[pat].setdefault("debug_info",{})
                curr_dict[pat]["debug_info"].setdefault("horizontal_persistence",0)
                curr_dict[pat]["debug_info"]["horizontal_persistence"] += 2
                curr_dict[pat]["score"] += 2
            else:
                 # Handle case where pattern might be missing score (shouldn't happen with current logic)
                 print(f"[Warning] Pattern {pat} missing score in horizontal persistence check.")


def detect_lingering(col_list):
    """
    If a pattern appears in multiple columns of the same draw,
    add a lingering bonus = freq of columns. E.g. if it appears in 3 columns => +3.
    """
    freq_count = Counter()
    for cdict in col_list:
        for pat in cdict.keys():
            freq_count[pat]+=1
    for cdict in col_list:
        for pat, details in cdict.items():
             # Ensure 'score' exists before adding bonus
            if 'score' in details:
                details.setdefault("debug_info", {})
                freq = freq_count[pat]
                if freq>=2:
                    details["debug_info"].setdefault("lingering_bonus",0)
                    details["debug_info"]["lingering_bonus"] += freq
                    details["score"] += freq
            else:
                 print(f"[Warning] Pattern {pat} missing score in lingering bonus check.")


def order_persistence_indicator(draw_list):
    """
    We unify each draw's patterns, compare consecutive draws.
    If rowmaps match exactly, +3 to the patterns in the *current* draw.
    """
    # unify patterns for each draw
    draws_patterns = []
    for col_list in draw_list:
        big_map = {}
        for col_dict in col_list:
            for pat, details in col_dict.items():
                # Store a reference to the actual details dict in the col_list
                big_map.setdefault(pat, {"details_ref": details, "rows": details.get("rows",{})})
        draws_patterns.append(big_map)

    for i in range(len(draw_list)-1):
        prev_big = draws_patterns[i]
        curr_big = draws_patterns[i+1]

        for pat, prev_info in prev_big.items():
            if pat in curr_big:
                curr_info = curr_big[pat]
                # Compare the 'rows' part
                if curr_info.get("rows", {}) == prev_info.get("rows", {}):
                    # apply +3 to current draw's pattern details
                    det = curr_info.get("details_ref")
                    if det and 'score' in det: # Check score exists
                        det.setdefault("debug_info",{})
                        det["debug_info"].setdefault("order_persistence",0)
                        det["debug_info"]["order_persistence"] += 3
                        det["score"] += 3
                    # else:
                    #      print(f"[Warning] Pattern {pat} missing score/details_ref in order persistence.")

def run_stable_pattern_extraction(json_data):
    """
    Master function:
     - For each (section->set), gather draws in ascending order (Draw1..7).
     - For each draw => columns => col_list => extract_column_patterns
       => apply horizontal_persistence & lingering
     - Then apply order_persistence among consecutive draws.

    returns stable_results[section][set_name] = [col_list_draw1, col_list_draw2, ...]
    """
    stable_results = defaultdict(lambda: defaultdict(list))
    row_types = ["R2","R4","R6","R8"]
    sections_obj = json_data.get("sections", {})
    draw_names = [f"Draw{i}" for i in range(1,MAX_COL+1)] # Use MAX_COL

    for section_name, sect_data in sections_obj.items():
        sets_data = sect_data.get("sets",{})
        for set_name, set_data in sets_data.items():
            all_draws_col_lists = []
            # Sort draw keys numerically if possible (e.g., "Draw1", "Draw10")
            # This handles potential variations in draw naming/order in the input JSON
            try:
                 sorted_draw_keys = sorted(set_data.get("draws", {}).keys(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
            except:
                 sorted_draw_keys = sorted(set_data.get("draws", {}).keys()) # Fallback sort


            for draw_name in sorted_draw_keys:
            # for draw_name in draw_names: # Original way, might miss draws if named differently
                if draw_name not in set_data["draws"]:
                    continue

                draw_info = set_data["draws"][draw_name]
                pattern_vars = draw_info.get("pattern_variations",{})

                # Determine max columns dynamically based on actual data in this draw
                max_cols_in_draw=0
                for rt in row_types:
                    if rt in pattern_vars and isinstance(pattern_vars[rt], list):
                        length = len(pattern_vars[rt])
                        if length>max_cols_in_draw: max_cols_in_draw=length

                hot_zone_ind = draw_info.get("metadata",{}).get("hot_zone_indicators",{})
                col_list=[]

                # Iterate up to max columns found in *this specific draw*
                for col_i in range(max_cols_in_draw):
                    r2_val = pattern_vars["R2"][col_i] if "R2" in pattern_vars and isinstance(pattern_vars["R2"], list) and col_i<len(pattern_vars["R2"]) else ""
                    r4_val = pattern_vars["R4"][col_i] if "R4" in pattern_vars and isinstance(pattern_vars["R4"], list) and col_i<len(pattern_vars["R4"]) else ""
                    r6_val = pattern_vars["R6"][col_i] if "R6" in pattern_vars and isinstance(pattern_vars["R6"], list) and col_i<len(pattern_vars["R6"]) else ""
                    r8_val = pattern_vars["R8"][col_i] if "R8" in pattern_vars and isinstance(pattern_vars["R8"], list) and col_i<len(pattern_vars["R8"]) else ""

                    col_hot = {}
                    # Ensure hot_zone_ind is a dict and rt exists before accessing
                    if isinstance(hot_zone_ind, dict):
                        for rt in row_types:
                             # Check rt key exists and its value is a list/iterable
                            if rt in hot_zone_ind and isinstance(hot_zone_ind[rt], (list, tuple, str)) and col_i<len(hot_zone_ind[rt]):
                                col_hot[rt] = hot_zone_ind[rt][col_i]

                    col_patterns = extract_column_patterns(r2_val, r4_val, r6_val, r8_val,
                                                          hot_indicators=col_hot,
                                                          check_consensus=True)
                    col_list.append(col_patterns)

                horizontal_persistence_scoring(col_list)
                detect_lingering(col_list)
                all_draws_col_lists.append(col_list)

            # order persistence across consecutive draws
            order_persistence_indicator(all_draws_col_lists)

            stable_results[section_name][set_name] = all_draws_col_lists

    return dict(stable_results) # Convert back to regular dict


########################################################################
# PART C: HTML REPORT & DEMO
########################################################################

def build_html_report(stable_results):
    """
    Build an HTML doc listing top patterns + column by column details.
    Now includes sub-bonus debug info for clarity.
    """
    big_global_list = []
    for section_name, setsdict in stable_results.items():
        for set_name, draw_list in setsdict.items():
            # draw_list = [col_list_draw1, col_list_draw2, ...]
            for draw_idx, col_list in enumerate(draw_list, start=1):
                draw_label = f"Draw{draw_idx}" # Assuming draws are ordered 1..N
                for col_i, col_dict in enumerate(col_list):
                    for pat, details in col_dict.items():
                        big_global_list.append({
                            "section": section_name,
                            "set": set_name,
                            "draw": draw_label,
                            "column": col_i+1, # 1-based column index
                            "pattern": pat,
                            "score": details.get("score", 0), # Use .get() for safety
                            "debug_info": details.get("debug_info",{})
                        })

    # sort top patterns
    big_global_list.sort(key=lambda x:x["score"], reverse=True)

    topN = 20
    head_html = f"""<html><head>
    <meta charset="UTF-8"/>
    <title>Stable Patterns Report (Upgraded Version)</title>
    <style>
    body {{
       font-family: Arial, sans-serif;
       margin: 0; padding: 20px;
       background-color: #f9f9f9; color: #333;
    }}
    h1,h2,h3,h4,h5 {{
       color: #800080;
       margin-bottom: 0.4em;
    }}
    table {{
       border-collapse: collapse;
       width: 100%;
       margin-bottom: 20px;
       background-color: #fff;
       font-size: 0.85em; /* Slightly smaller font */
    }}
    th,td {{
       border: 1px solid #ccc;
       padding: 4px 6px; /* Smaller padding */
       text-align: left;
       word-wrap: break-word; /* Allow wrapping long text */
    }}
    th {{ background-color: #f0f0f0; font-weight: bold; }}
    tr:nth-child(even){{background-color:#fefefe}}
    .high-score {{ background-color: #dfd; }}
    .order-persist {{ background-color: #cfc; }}
    .debug-info {{
       font-size: 0.9em; /* Relative size */
       color: #666;
       white-space: pre-wrap; /* Allow wrapping */
    }}
    .pattern-cell {{ max-width: 100px; overflow: hidden; text-overflow: ellipsis; }}
    .debug-cell {{ max-width: 250px; }}
    </style>
    </head><body>
    <h1>Upgraded Stable Pattern Extraction Report</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    """

    # top 20
    top_html = "<h2>Top Stable Patterns (Global)</h2>"
    top_html += "<table><tr><th>Rank</th><th>Section</th><th>Set</th><th>Draw</th><th>Col</th><th>Pattern</th><th>Score</th></tr>"
    for i,row in enumerate(big_global_list[:topN], start=1):
        css = ''
        if row["score"]>=30:
            css = ' class="high-score"'
        top_html += f"<tr{css}>"
        top_html += f"<td>{i}</td><td>{row['section']}</td><td>{row['set']}</td>"
        top_html += f"<td>{row['draw']}</td><td>{row['column']}</td>"
        top_html += f"<td class='pattern-cell'>{row['pattern']}</td><td>{int(row['score'])}</td>"
        top_html += "</tr>"
    top_html += "</table>"

    detail_html = "<h2>Detailed Patterns by Section & Set</h2>"
    for section_name, setsdict in stable_results.items():
        detail_html += f"<h3>Section: {section_name}</h3>"
        for set_name, draw_list in setsdict.items():
            detail_html += f"<h4>Set: {set_name}</h4>"
            for draw_idx, col_list in enumerate(draw_list, start=1):
                draw_label = f"Draw{draw_idx}"
                detail_html += f"<h5>{draw_label}</h5>"
                for col_i, col_dict in enumerate(col_list):
                    detail_html += f"<p><strong>Column {col_i+1}</strong></p>"
                    if not col_dict:
                        detail_html += "<p style='color:gray;'>No stable patterns found.</p>"
                        continue
                    detail_html += "<table><thead><tr><th>Pattern</th><th>Rows</th><th>Score</th><th>Debug Info</th></tr></thead><tbody>"
                    # Sort patterns within the column by score
                    sorted_pats = sorted(col_dict.items(), key=lambda x:x[1].get("score", 0), reverse=True)
                    for pat, det in sorted_pats:
                        sc = det.get("score", 0)
                        dbg = det.get("debug_info", {})
                        # optional color for order_persistence or high score
                        style=''
                        if 'order_persistence' in dbg and dbg['order_persistence'] > 0:
                            style=' class="order-persist"' # Use class instead of inline style
                        elif sc>=30:
                            style=' class="high-score"' # Use class
                        # Safely join row descriptions
                        row_desc = ", ".join([f"{r}={v}" for r,v in det.get("rows", {}).items()])
                        # Format debug info nicely
                        debug_items = []
                        for k, v in dbg.items():
                             # Format numbers nicely if possible
                             if isinstance(v, (int, float)):
                                 debug_items.append(f"{k}: {v:g}") # General format for numbers
                             else:
                                 debug_items.append(f"{k}: {v}")
                        debug_txt = "\n".join(debug_items) # Use newline for pre-wrap

                        detail_html += f"<tr{style}>"
                        detail_html += f"<td class='pattern-cell'>{pat}</td><td>{row_desc}</td><td>{int(sc)}</td>"
                        detail_html += f"<td class='debug-info debug-cell'>{debug_txt}</td>"
                        detail_html += f"</tr>"
                    detail_html += "</tbody></table>"

    closing = "</body></html>"
    return head_html + top_html + detail_html + closing

def demo_main(json_path):
    """
    CLI demonstration:
     1) load the JSON
     2) run run_stable_pattern_extraction
     3) build_html_report
     4) save output_stable_patterns.html
     5) print top 10 patterns in console
    """
    if not os.path.exists(json_path):
        print(f"ERROR: JSON file not found: {json_path}")
        return
    try:
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to decode JSON file: {json_path} - {e}")
        return
    except Exception as e:
        print(f"ERROR: Failed to read file: {json_path} - {e}")
        return

    print(f"Running stable pattern extraction on {json_path}")
    try:
        results = run_stable_pattern_extraction(data)
    except Exception as e:
        print(f"ERROR: Failed during stable pattern extraction: {e}")
        import traceback
        traceback.print_exc() # Print stack trace for debugging
        return

    try:
        html_report = build_html_report(results)
        out_file = "output_stable_patterns.html"
        with open(out_file,"w",encoding="utf-8") as f:
            f.write(html_report)
        print(f"HTML report generated: {out_file}")
    except Exception as e:
        print(f"ERROR: Failed to build or save HTML report: {e}")
        # Continue to print console summary if report fails

    # also do a top-10 console print
    big_list = []
    for sec, setsdict in results.items():
        for st, draw_list in setsdict.items():
            for d_idx, col_list in enumerate(draw_list, start=1):
                draw_label = f"Draw{d_idx}"
                for col_i, cdict in enumerate(col_list):
                    for pat, info in cdict.items():
                        big_list.append({
                          "section": sec,
                          "set": st,
                          "draw": draw_label,
                          "column": col_i+1,
                          "pattern": pat,
                          "score": info.get("score", 0) # Safe access
                        })
    big_list.sort(key=lambda x:x["score"], reverse=True)
    print("\n=== TOP 10 STABLE PATTERNS ===")
    if not big_list:
        print("No stable patterns found.")
    else:
        for i,row in enumerate(big_list[:10], start=1):
            print(f"{i}. {row['section']} - {row['set']} - {row['draw']} col{row['column']} => {row['pattern']} (score={int(row['score'])})")

# ---------------------------------------------------------------------------
# Streamlit UI wrapper (lightweight)                                          
# ---------------------------------------------------------------------------
try:
    import streamlit as st
    import pandas as pd
    from utils.path_handler import get_tables_output_dir
except ModuleNotFoundError:
    st = None  # Allows CLI usage without Streamlit


def _load_tables_csv(state_name):
    """Load *_combined.csv tables for given state into dict[str->DataFrame]."""
    import pandas as pd, os
    out = {}
    base = os.path.join(get_tables_output_dir(), state_name)
    for sec in ["Midday", "Evening", "Combined"]:
        csv_path = os.path.join(base, f"{state_name}_{sec}_combined.csv")
        if os.path.exists(csv_path):
            out[f"{sec}_combined"] = pd.read_csv(csv_path)
    return out


def _tables_to_jsonlike(state_name: str, tbls: dict) -> dict:
    """Convert *_combined.csv DataFrames into nested dict expected by extractor."""
    out = {}
    for sec_key, df in tbls.items():            # e.g. 'Midday_combined'
        section = sec_key.split("_")[0]         # 'Midday'
        for _, row in df.iterrows():
            set_name  = row["Set"]
            draw_name = row["Draw"]
            rtype     = row["RowType"]
            digits = [
                str(val).split(".")[0].zfill(3) if str(val).strip() not in ("", "None", "N/A") else ""
                for val in row[["7","6","5","4","3","2","1"]]
                if str(val).strip() not in ("", "None", "N/A")
            ]
            (out
             .setdefault(section, {})
             .setdefault(set_name, {})
             .setdefault(draw_name, {})
            )[rtype] = digits
    return out


def _results_to_df(results: dict) -> "pd.DataFrame":
    """Flatten nested extractor results dict into a DataFrame suitable for display."""
    import pandas as pd
    rows = []
    for sec, sets in results.items():
        for set_name, draws in sets.items():
            for d_idx, col_list in enumerate(draws, start=1):
                draw_label = f"Draw{d_idx}"
                for col_idx, col_dict in enumerate(col_list):
                    for pat, det in col_dict.items():
                        rows.append({
                            "Section": sec,
                            "Set": set_name,
                            "Draw": draw_label,
                            "Col": col_idx + 1,
                            "Pattern": pat,
                            "Score": det.get("score", 0),
                        })
    return pd.DataFrame(rows).sort_values("Score", ascending=False) if rows else pd.DataFrame()


def _display_results(results: dict, state: str = "unknown"):
    """Flatten results dict and show in Streamlit with download button."""
    if results.empty:
        st.warning("No stable patterns found.")
        return
    df = results
    st.dataframe(df, use_container_width=True)
    
    # Auto-save output for reproducibility
    today = datetime.now().strftime("%Y-%m-%d")
    out_dir = Path("data/outputs/patterns")
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_auto = out_dir / f"{state}_{today}_stable_patterns.csv"
    try:
        df.to_csv(csv_auto, index=False)
        st.success(f"📁 Saved to {csv_auto}")
        csv_bytes = df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv_bytes, file_name="stable_patterns.csv")
    except Exception as exc:
        st.warning(f"⚠️ Failed to auto-save CSV: {exc}")


def main():  # noqa: D401 – Streamlit entry point
    """Streamlit wrapper for the stable-pattern extractor."""
    if st is None:
        print("[Stable Patterns] Streamlit not available – main() skipped.")
        return

    st.header("Stable Pattern Extractor")

    # Offer two modes: using existing CSV tables or uploading a raw JSON bundle
    mode = st.radio("Choose data source:", [
        "Use generated *_combined.csv tables",
        "Upload JSON from AI export",
    ], index=0)

    if mode == "Use generated *_combined.csv tables":
        # Dynamically list states based on folders present
        import os
        table_dir = get_tables_output_dir()
        state_opts = [d for d in os.listdir(table_dir) if d.endswith("4") and os.path.isdir(os.path.join(table_dir, d))]
        if not state_opts:
            st.warning("No processed states found. Run *Process Data* first.")
            st.stop()
        state = st.selectbox("Select state", sorted(state_opts))
        if st.button("Run Stable Pattern Extraction", key="run_stable_csv"):
            with st.spinner("Loading tables & extracting stable patterns …"):
                tbls = _load_tables_csv(state)
                if not tbls:
                    st.error("Could not find combined tables for that state.")
                    st.stop()
                json_like = _tables_to_jsonlike(state, tbls)
                results = run_stable_pattern_extraction(json_like)
            df_scores = _results_to_df(results)
            _display_results(df_scores, state)
    else:
        uploaded = st.file_uploader("Upload *_all_tables_ JSON export", type=["json"])
        if uploaded is not None:
            import json, io
            try:
                data = json.load(io.TextIOWrapper(uploaded, encoding="utf-8"))
            except Exception as e:
                st.error(f"Failed to parse JSON: {e}")
                st.stop()
            with st.spinner("Extracting stable patterns …"):
                results = run_stable_pattern_extraction(data)
            if not results:
                st.warning("No stable patterns found.")
                st.stop()
            st.success("Extraction complete.")
            _display_results(_results_to_df(results), "uploaded")

# Note: existing CLI demo_main() remains functional.

if __name__=="__main__":
    if len(sys.argv)<2:
        print(f"Usage: python {os.path.basename(__file__)} path/to/lottery_data.json")
        sys.exit(1)
    demo_main(sys.argv[1]) 