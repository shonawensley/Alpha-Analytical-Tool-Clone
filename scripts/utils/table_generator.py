#!/usr/bin/env python
"""
table_generator.py - Generate formatted lottery data tables

This script:
1. Builds Combined Tables with all sets and row types
2. Builds R2-only Tables with custom slicing rules
3. Applies right-alignment with "N/A" padding
4. Marks hot zones in Set1 rows with "*" suffix
5. Provides ASCII table printing for terminal output
"""
import pandas as pd

############################
# HOT ZONE SETTINGS (for Set1)
############################
hotzone_counts = {
    1: 5,  # For Draw1, star the last 5 items
    2: 5,  # For Draw2, star the last 5 items
    3: 5,  # For Draw3, star the last 5 items
    4: 4,  # For Draw4, star the last 4 items
    5: 2,  # For Draw5, star the last 2 items
    # Draw6 and Draw7 not included in hot zones
}

############################
# HOT ZONE FUNCTION
############################
def mark_hot_zones(set_label, draw_label, row_type, vals):
    """
    For Set1 rows of type R2, R4, R6, or R8, mark the last hotzone_counts[draw_num] items 
    by appending a '*' to them.
    
    Draw number is parsed from draw_label (e.g., "Draw1" => 1).
    """
    if set_label == "Set1" and row_type in ["R2", "R4", "R6", "R8"]:
        try:
            draw_num = int(draw_label.replace("Draw", ""))
        except:
            return vals  # parsing error: do nothing
        if draw_num in hotzone_counts:
            count_needed = hotzone_counts[draw_num]
            n = len(vals)
            for i in range(count_needed):
                idx = n - 1 - i  # start from the end
                if idx < 0:
                    break
                vals[idx] = vals[idx] + "*" if vals[idx] else "*"
    return vals

############################
# COMBINED TABLE
############################
def build_section_table(section_data):
    """
    Build a combined table DataFrame with columns:
        [Set, Draw, RowType, 7, 6, 5, 4, 3, 2, 1]
    
    • For each row, if there are fewer than 7 items, we right-align the data by 
      prepending "N/A" placeholders (so the actual data appears in the rightmost columns).
    • For Set1 rows (R2, R4, R6, R8), the hot zone marking is applied (stars are appended).
    • Processes Set3 and Set2 (Draw1 only) and Set1 (Draw1 to Draw7)
    """
    columns = ["Set", "Draw", "RowType", "7", "6", "5", "4", "3", "2", "1"]
    records = []

    def add_row(set_label, draw_label, row_type, values):
        # Convert to list and mark hot zones if applicable.
        vals = list(values)
        vals = mark_hot_zones(set_label, draw_label, row_type, vals)
        
        # Right-align: if fewer than 7 items, prepend "N/A" so that real data becomes right-aligned.
        if len(vals) < 7:
            needed = 7 - len(vals)
            vals = ["N/A"] * needed + vals
        elif len(vals) > 7:
            vals = vals[:7]
            
        rec = {
            "Set": set_label,
            "Draw": draw_label,
            "RowType": row_type,
            "7": vals[0],
            "6": vals[1],
            "5": vals[2],
            "4": vals[3],
            "3": vals[4],
            "2": vals[5],
            "1": vals[6]
        }
        records.append(rec)

    # Process Set3 -> Draw1 (include DRAW_DATA and R2, R4, R6, R8 rows)
    if "Set3" in section_data and "Draw1" in section_data["Set3"]:
        d = section_data["Set3"]["Draw1"]
        if "draw_data" in d:
            add_row("Set3", "Draw1", "DRAW_DATA", d["draw_data"])
        for rt in ["R2", "R4", "R6", "R8"]:
            if rt in d:
                add_row("Set3", "Draw1", rt, d[rt])

    # Process Set2 -> Draw1 (include DRAW_DATA and R2, R4, R6, R8 rows)
    if "Set2" in section_data and "Draw1" in section_data["Set2"]:
        d = section_data["Set2"]["Draw1"]
        if "draw_data" in d:
            add_row("Set2", "Draw1", "DRAW_DATA", d["draw_data"])
        for rt in ["R2", "R4", "R6", "R8"]:
            if rt in d:
                add_row("Set2", "Draw1", rt, d[rt])

    # Process Set1 -> Draw1 to Draw7
    if "Set1" in section_data:
        for draw_num in range(1, 8):
            dk = f"Draw{draw_num}"
            if dk in section_data["Set1"]:
                d = section_data["Set1"][dk]
                if draw_num == 1 and "draw_data" in d:
                    add_row("Set1", dk, "DRAW_DATA", d["draw_data"])
                for rt in ["R2", "R4", "R6", "R8"]:
                    if rt in d:
                        add_row("Set1", dk, rt, d[rt])

    df = pd.DataFrame(records, columns=columns)
    return df

############################
# CUSTOM R2 SLICING
############################
def custom_r2_slice(set_label, draw_label, r2_list):
    """
    Custom slice for R2 data:
      - For Set3/Set2 and Draw1: first 3 items.
      - For Set1:
          * Draw1: first 3 items.
          * Draw2: first 2 items.
          * Draw3 - Draw7: first 1 item.
    """
    vals = list(r2_list)
    if set_label in ["Set3", "Set2"] and draw_label == "Draw1":
        return vals[:3]
    if set_label == "Set1":
        try:
            dnum = int(draw_label.replace("Draw", ""))
        except:
            dnum = 0
        if dnum == 1:
            return vals[:3]
        elif dnum == 2:
            return vals[:2]
        else:
            return vals[:1]
    return vals

############################
# R2-ONLY TABLE
############################
def build_r2_only_table(section_data):
    """
    Build an R2-only table with columns:
        [Set, Draw, 7, 6, 5, 4, 3, 2, 1]
    Uses custom_r2_slice() to get the correct number of items for each Set/Draw.
    """
    columns = ["Set", "Draw", "7", "6", "5", "4", "3", "2", "1"]
    records = []

    def add_r2_row(slabel, dlabel, r2_values):
        # First apply the custom slice
        sliced = custom_r2_slice(slabel, dlabel, r2_values)
        # Then right-align by prepending "N/A"
        if len(sliced) > 7:
            sliced = sliced[:7]
        elif len(sliced) < 7:
            needed = 7 - len(sliced)
            sliced = ["N/A"] * needed + sliced
        
        rec = {
            "Set": slabel,
            "Draw": dlabel,
            "7": sliced[0],
            "6": sliced[1],
            "5": sliced[2],
            "4": sliced[3],
            "3": sliced[4],
            "2": sliced[5],
            "1": sliced[6]
        }
        records.append(rec)

    # Process Set3 -> Draw1
    if "Set3" in section_data and "Draw1" in section_data["Set3"]:
        d = section_data["Set3"]["Draw1"]
        if "R2" in d:
            add_r2_row("Set3", "Draw1", d["R2"])
    
    # Process Set2 -> Draw1
    if "Set2" in section_data and "Draw1" in section_data["Set2"]:
        d = section_data["Set2"]["Draw1"]
        if "R2" in d:
            add_r2_row("Set2", "Draw1", d["R2"])
    
    # Process Set1 -> Draw1 through Draw7
    if "Set1" in section_data:
        for draw_num in range(1, 8):
            dk = f"Draw{draw_num}"
            if dk in section_data["Set1"]:
                d = section_data["Set1"][dk]
                if "R2" in d:
                    add_r2_row("Set1", dk, d["R2"])

    df = pd.DataFrame(records, columns=columns)
    return df

############################
# ASCII PRINT
############################
def print_ascii_table(df, title=""):
    """
    Print the DataFrame as a nicely formatted ASCII table in the terminal.
    """
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)
    if df.empty:
        print("No data.")
        return
    try:
        print(df.to_markdown(tablefmt="grid", index=False))
    except Exception as e:
        print("Error printing table:", e)
        print(df)

############################
# GENERATE ALL TABLES FOR A STATE
############################
def generate_tables(state_data, state_name, output_dir=None):
    """
    Generate and optionally save all tables for a state
    
    Args:
        state_data: The extracted data dictionary for the state
        state_name: Name of the state
        output_dir: Optional directory to save CSV files
    
    Returns:
        Dictionary with all generated DataFrames
    """
    results = {}
    
    for section in ["Midday", "Evening", "Combined"]:
        if section not in state_data:
            print(f"Skipping {section} for {state_name} - not found")
            continue
            
        print(f"Generating tables for {state_name} {section}...")
        section_data = state_data[section]
        
        # Build combined table
        combined_df = build_section_table(section_data)
        results[f"{section}_combined"] = combined_df
        
        # Build R2-only table
        r2_df = build_r2_only_table(section_data)
        results[f"{section}_r2"] = r2_df
        
        # Save tables if output_dir is provided
        if output_dir:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            combined_path = os.path.join(output_dir, f"{state_name}_{section}_combined.csv")
            r2_path = os.path.join(output_dir, f"{state_name}_{section}_r2.csv")
            
            combined_df.to_csv(combined_path, index=False)
            r2_df.to_csv(r2_path, index=False)
            
            print(f"  Saved tables to {output_dir}")
    
    return results

if __name__ == "__main__":
    # Demo with sample data
    print("This module is designed to be imported, not run directly.")
    print("For testing, import and use the functions with sample data.") 