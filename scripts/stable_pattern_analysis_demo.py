#!/usr/bin/env python
import json
import re
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import os
import sys

###############################################################################
# 1) STABLE PATTERN EXTRACTOR (Parts 1 & 2, plus Box vs. Straight & Long Clusters)
###############################################################################

# -----------------------------
#    HELPER FUNCTIONS
# -----------------------------
def canonical_form(pattern_str):
    """Return sorted version of pattern (for boxed equivalence)."""
    return ''.join(sorted(pattern_str))

def to_vtrac(num_str):
    """Map digits to their V-Trac equivalents (0/5 ->1, 1/6->2, etc.)."""
    vtrac_map = {
        '0': '1', '5': '1',
        '1': '2', '6': '2',
        '2': '3', '7': '3',
        '3': '4', '8': '4',
        '4': '5', '9': '5'
    }
    return ''.join(vtrac_map[d] for d in num_str if d in vtrac_map)

def is_three_value_pattern(cluster_str):
    """Check if cluster has at most 3 unique V-Trac digits."""
    vtrac_cluster = to_vtrac(cluster_str)
    return len(set(vtrac_cluster)) <= 3

def has_mirror_digits(pattern_str):
    """Check if pattern contains any mirror pairs (0-5,1-6,2-7,3-8,4-9)."""
    mirror_pairs = [('0','5'), ('1','6'), ('2','7'), ('3','8'), ('4','9')]
    for a, b in mirror_pairs:
        if a in pattern_str and b in pattern_str:
            return True
    return False

def long_cluster_bonus(cluster_str):
    """Extra points for longer clusters (≥5 digits)."""
    length = len(cluster_str)
    if length >= 5:
        return (length - 4) * 2  # start bonus from length=5
    return 0

def evaluate_boxed_vs_straight(pattern_info):
    """
    Returns (straight_bonus, boxed_permutation_bonus).
    - straight_bonus: bonus if exact same string (straight order) appears multiple times
    - boxed_permutation_bonus: bonus for multiple distinct permutations (boxed).
    """
    # Pattern info is a dict like {'R2': '6611888', 'R4': '...', ...}
    # We'll check exactly how many unique 'straight' forms appear
    straight_map = Counter(pattern_info.values())       # e.g. '6611888' : count
    boxed_map    = Counter(canonical_form(x) for x in pattern_info.values())

    # If the exact same straight pattern shows up multiple times
    straight_bonus = 0
    for s, count in straight_map.items():
        if count > 1:
            # Each repetition is valuable
            straight_bonus += count * 3

    # Number of different boxed permutations
    # For example, if we see '618' and '186' => same box (168).
    # The more distinct box forms appear, the more we add.
    boxed_permutation_bonus = len(boxed_map)

    return straight_bonus, boxed_permutation_bonus

# -----------------------------
#    CORE EXTRACTION (PART 1)
# -----------------------------
def extract_patterns_per_column(r2_str, r4_str, r6_str, r8_str, hot_zone_indicators=None):
    """
    Extract stable patterns from a single column of data (R2/R4/R6/R8).
    r2_str, r4_str, etc. are the digit strings from that column.
    hot_zone_indicators (dict) -> e.g. {'R2': '**', 'R4': '*', 'R6': None, 'R8': None}
    Returns dict of {canonical_pattern: {...scoring details...}, ...}
    """

    # We'll gather all discovered clusters from these 4 row strings
    row_data = {
        "R2": r2_str if r2_str else "",
        "R4": r4_str if r4_str else "",
        "R6": r6_str if r6_str else "",
        "R8": r8_str if r8_str else ""
    }
    patterns_in_col = defaultdict(lambda: {"rows": {}})  # canonical -> {"rows": {"R2": "xxx", ...}}

    # Extract 3+ digit clusters from each row
    # If it meets "is_three_value_pattern", store it
    for row_type, row_str in row_data.items():
        # Remove any '*' from the string to avoid confusion
        # (assuming your data sometimes includes '*' inline)
        cleaned_row = re.sub(r'\*', '', row_str)

        # Find all digit clusters of length >= 3
        for match in re.finditer(r'(\d{3,})', cleaned_row):
            cluster = match.group(1)
            if is_three_value_pattern(cluster):
                can_form = canonical_form(cluster)
                patterns_in_col[can_form]["rows"][row_type] = cluster

    # Build the result dict with scores
    result_for_column = {}
    for can_form, info in patterns_in_col.items():
        row_patterns = info["rows"]

        # Basic vertical coverage = how many R-rows
        vertical_coverage = len(row_patterns)
        # Count how many unique strings appear among them
        permutation_strength = len(set(row_patterns.values()))
        # Vtrac strength
        vtrac_score = 2 if len(set(to_vtrac(can_form))) <= 2 else 1

        # Evaluate hot zone bonus if present
        hot_zone_bonus = 0
        if hot_zone_indicators:
            # If any row has '*' or '**', we add extra
            for row_type, cluster_str in row_patterns.items():
                indicator = hot_zone_indicators.get(row_type)
                if indicator == '**':
                    hot_zone_bonus += 3
                elif indicator == '*':
                    hot_zone_bonus += 2

        # Check consensus endings across R2/R4/R6/R8
        # (If all row patterns share same last digit or 2 digits)
        consensus_bonus = 0
        endings = []
        for rt, cluster_str in row_patterns.items():
            # For 2-digit check:
            last2 = cluster_str[-2:] if len(cluster_str) >= 2 else cluster_str
            endings.append(last2)
        if endings and len(set(endings)) == 1:
            # all have same 2-digit ending
            consensus_bonus = 3

        # Mirror digit bonus
        mirror_bonus = 2 if has_mirror_digits(can_form) else 0

        # Box vs. straight bonus
        straight_bonus, box_bonus = evaluate_boxed_vs_straight(row_patterns)
        # long cluster bonus
        length_bonus = 0
        # If there are multiple row_type strings, pick the longest for a bigger bonus
        longest_str = max(row_patterns.values(), key=len)
        length_bonus = long_cluster_bonus(longest_str)

        # base coverage
        coverage_score = vertical_coverage * 2
        # sum them up
        total_score = (coverage_score + permutation_strength + vtrac_score
                       + hot_zone_bonus + consensus_bonus + mirror_bonus
                       + straight_bonus + box_bonus + length_bonus)

        result_for_column[can_form] = {
            "raw_clusters": row_patterns,      # each row's raw cluster
            "vertical_coverage": vertical_coverage,
            "permutation_strength": permutation_strength,
            "vtrac_score": vtrac_score,
            "hot_zone_bonus": hot_zone_bonus,
            "consensus_bonus": consensus_bonus,
            "mirror_digit_bonus": mirror_bonus,
            "straight_bonus": straight_bonus,
            "box_permutation_bonus": box_bonus,
            "length_bonus": length_bonus,
            "total_score": total_score
        }

    return result_for_column

# -----------------------------
#    ADVANCED (PART 2)
# -----------------------------
def evaluate_horizontal_persistence(all_cols_patterns):
    """
    Given a list of pattern dicts for consecutive columns, see how many patterns persist horizontally
    from one column to the next. We'll add a 'horizontal_persistence_score' to each pattern's dict.
    
    all_cols_patterns is a list of {canonical: {...}} for columns left->right.
    """
    # We'll track how many times a pattern repeats from col i to col i+1
    # Then add a small bonus for each repeat
    if len(all_cols_patterns) < 2:
        return

    for col_idx in range(len(all_cols_patterns) - 1):
        current_col = all_cols_patterns[col_idx]
        next_col    = all_cols_patterns[col_idx + 1]
        # Check which patterns overlap
        overlap = set(current_col.keys()).intersection(set(next_col.keys()))
        for pat in overlap:
            # add 2 points to each occurrence for persisting horizontally
            current_col[pat].setdefault("horizontal_persistence_score", 0)
            current_col[pat]["horizontal_persistence_score"] += 2
            current_col[pat]["total_score"] += 2

def detect_lingering_patterns_in_draw(all_cols_patterns):
    """
    If a pattern appears in multiple columns of a single draw,
    we add a lingering bonus proportional to frequency.
    """
    pattern_count = Counter()
    for col_dict in all_cols_patterns:
        for pat in col_dict.keys():
            pattern_count[pat] += 1

    for col_dict in all_cols_patterns:
        for pat, details in col_dict.items():
            freq = pattern_count[pat]
            if freq >= 2:
                # add 1 point per repeated appearance
                # e.g., if freq=3 => +3
                lingering_bonus = freq
                details["lingering_pattern_bonus"] = lingering_bonus
                details["total_score"] += lingering_bonus

###############################################################################
# 2) FUNCTION TO SCAN YOUR FULL JSON AND EXTRACT PATTERNS FOR ALL SETS/DRAWS
###############################################################################
def run_stable_extraction_on_json(json_data):
    """
    Iterates over your entire JSON structure:
      sections -> sets -> draws -> columns
    Extracts stable patterns for each column using above logic.
    Scores patterns with advanced modules.
    Returns a nested result dict:
      result[section][set_name][draw_name]["columns"][col_number] = {canonical_pattern: {scoring details}}
    """
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

    # Go through each section (Midday, Evening, Combined)
    for section_name, section_obj in json_data["sections"].items():
        # each set (Set1, Set2, Set3, etc.)
        for set_name, set_obj in section_obj["sets"].items():
            # each draw (Draw1, Draw2, ...)
            for draw_name, draw_obj in set_obj["draws"].items():

                # how many columns are there for R2, R4, R6, R8?
                # For example, R2 might have N items, R4 might have M items,
                # but we generally expect them to have the same length for the columns
                # in pattern_variations.
                pattern_variations = draw_obj["pattern_variations"]
                # R2, R4, R6, R8 might be lists
                # We'll assume they are all the same length (the "column count" for that draw).
                max_columns = 0
                # could check min or max across R2,R4,R6,R8
                for row_type in ["R2", "R4", "R6", "R8"]:
                    if row_type in pattern_variations:
                        length = len(pattern_variations[row_type])
                        if length > max_columns:
                            max_columns = length

                # We'll store all columns in a list
                columns_data = []

                # We'll gather the "hot zone indicators" if exist
                # e.g. draw_obj["metadata"]["hot_zone_indicators"] -> { "R2": [...], "R4": [...], ... }
                hot_zone_indicators = draw_obj["metadata"].get("hot_zone_indicators", None)

                for col_index in range(max_columns):
                    # Build single column data
                    r2_val = pattern_variations["R2"][col_index] if ("R2" in pattern_variations and col_index < len(pattern_variations["R2"])) else None
                    r4_val = pattern_variations["R4"][col_index] if ("R4" in pattern_variations and col_index < len(pattern_variations["R4"])) else None
                    r6_val = pattern_variations["R6"][col_index] if ("R6" in pattern_variations and col_index < len(pattern_variations["R6"])) else None
                    r8_val = pattern_variations["R8"][col_index] if ("R8" in pattern_variations and col_index < len(pattern_variations["R8"])) else None

                    # relevant zone indicators for this column
                    indicators_for_col = {}
                    if hot_zone_indicators:
                        for rt in ["R2", "R4", "R6", "R8"]:
                            if rt in hot_zone_indicators and col_index < len(hot_zone_indicators[rt]):
                                indicators_for_col[rt] = hot_zone_indicators[rt][col_index]

                    col_patterns = extract_patterns_per_column(r2_val, r4_val, r6_val, r8_val, hot_zone_indicators=indicators_for_col)
                    columns_data.append(col_patterns)

                # Now run advanced horizontal/lingering analysis
                evaluate_horizontal_persistence(columns_data)
                detect_lingering_patterns_in_draw(columns_data)

                # Save the data in the result
                # We want to label columns from left to right or right to left?
                # Let's just store them in the same index order as the array (0-based).
                result[section_name][set_name][draw_name]["columns"] = columns_data

    return result

###############################################################################
# 3) SIMPLE DEMO: PARSE THE PROVIDED DATA, EXTRACT PATTERNS, SHOW ASCII + A CHART
###############################################################################

def demo_stable_pattern_extraction(json_filepath=None):
    """
    1) Load your big JSON data
    2) Run stable pattern extraction
    3) Print top patterns in ASCII table
    4) Plot a quick bar chart for top patterns
    """
    if not json_filepath:
        print("Please provide a valid JSON file path to demo.")
        return

    # Load data
    with open(json_filepath, "r", encoding="utf-8") as f:
        lottery_data = json.load(f)

    # Run extraction
    full_analysis = run_stable_extraction_on_json(lottery_data)

    # Collect all patterns across entire dataset
    all_patterns = []
    for section_name, sets_dict in full_analysis.items():
        for set_name, draws_dict in sets_dict.items():
            for draw_name, draw_data in draws_dict.items():
                col_list = draw_data["columns"]  # list of dicts
                for col_idx, col_dict in enumerate(col_list):
                    for can_pat, details in col_dict.items():
                        # We'll gather into a single list
                        # We'll keep track of location & total_score
                        row_info = {
                            "section": section_name,
                            "set": set_name,
                            "draw": draw_name,
                            "column_index": col_idx,
                            "pattern": can_pat,
                            "score": details["total_score"]
                        }
                        all_patterns.append(row_info)

    # Sort them by descending total_score
    all_patterns_sorted = sorted(all_patterns, key=lambda x: x["score"], reverse=True)

    # Print out top N in an ASCII table for demonstration
    TOP_N = 15
    print("\n=== TOP {} STABLE PATTERNS (By Total Score) ===".format(TOP_N))
    print("+---------------------------------------------------------------------------------------+")
    print("|{:<5}|{:<10}|{:<10}|{:<8}|{:<6}|{:<10}|{:<8}|".format(
        "Rank", "Section", "Set", "Draw", "Column", "Pattern", "Score"
    ))
    print("+---------------------------------------------------------------------------------------+")

    for i, row in enumerate(all_patterns_sorted[:TOP_N], start=1):
        print("|{:<5}|{:<10}|{:<10}|{:<8}|{:<6}|{:<10}|{:<8}|".format(
            i,
            row["section"],
            row["set"],
            row["draw"],
            row["column_index"],
            row["pattern"],
            int(row["score"])
        ))
    print("+---------------------------------------------------------------------------------------+\n")

    # --- Quick Bar Chart of top scoring patterns ---
    top_for_chart = all_patterns_sorted[:10]  # top 10
    patterns = [f"{r['pattern']}@{r['draw']}" for r in top_for_chart]
    scores = [r["score"] for r in top_for_chart]

    plt.figure(figsize=(10, 5))
    plt.barh(patterns, scores, color='skyblue')
    plt.gca().invert_yaxis()  # highest at the top
    plt.title("Top 10 Stable Patterns by Score")
    plt.xlabel("Score")
    plt.ylabel("Pattern@Draw")
    plt.tight_layout()
    
    # Save the plot to a file instead of showing it (for terminal environment)
    plot_path = os.path.join(os.path.dirname(json_filepath), 'stable_patterns_chart.png')
    plt.savefig(plot_path)
    print(f"Chart saved to: {plot_path}")

###############################################################################
# 4) MAIN GUARD
###############################################################################
if __name__ == "__main__":
    """
    Usage:
      python stable_pattern_analysis_demo.py path/to/your_data.json
    """
    if len(sys.argv) > 1:
        path = sys.argv[1]
        demo_stable_pattern_extraction(path)
    else:
        # Default path if no arguments provided
        default_path = os.path.join('data', 'ai_exports', 'OntarioCanada4_ai_format_20250403_030615.json')
        if os.path.exists(default_path):
            print(f"Using default JSON file path: {default_path}")
            demo_stable_pattern_extraction(default_path)
        else:
            print("Please run with: python stable_pattern_analysis_demo.py path/to/lottery_data.json")
            print(f"Default path '{default_path}' was not found.") 