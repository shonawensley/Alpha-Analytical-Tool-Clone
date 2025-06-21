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
import os

############################
# HOT ZONE SETTINGS (for Set1)
############################
hotzone_counts = {
    1: 5,  # For Draw1, star the last 5 items
    2: 4,  # For Draw2, star the last 4 items
    3: 3,  # For Draw3, star the last 3 items
    4: 2,  # For Draw4, star the last 2 items
    5: 2,  # For Draw5, star the last 2 items
    6: 1,  # For Draw6, star the last 1 item
    # Draw7 not included in hot zones
}

# Super hot zone settings (subset of hot zones)
super_hotzone_counts = {
    1: 3,  # Last 3 of the 5 hot items in Draw1 are super hot
    2: 2,  # Last 2 of the 4 hot items in Draw2 are super hot
    3: 2,  # Last 2 of the 3 hot items in Draw3 are super hot
    4: 2,  # Both hot items in Draw4 are super hot
    5: 2,  # Both hot items in Draw5 are super hot
}

############################
# HOT ZONE FUNCTION
############################
def mark_hot_zones(set_label, draw_label, row_type, vals):
    """
    For Set1 rows of type R2, R4, R6, or R8, mark items with:
    - Single * for hot zone items
    - Double ** for super hot zone items (subset of hot zone)
    For Set2/Set3 Draw1, mark the last 4 items with *.
    
    Draw number is parsed from draw_label (e.g., "Draw1" => 1).
    """
    if (set_label == "Set1" and row_type in ["R2", "R4", "R6", "R8"]) or \
       (set_label in ["Set2", "Set3"] and draw_label == "Draw1" and row_type in ["R2", "R4", "R6", "R8"]):
        try:
            draw_num = int(draw_label.replace("Draw", ""))
            
            # Determine hot zone count
            if set_label in ["Set2", "Set3"] and draw_label == "Draw1":
                hot_count = 4  # For Set2/Set3 Draw1, mark last 4 items
                super_hot_count = 0  # No super hot for Set2/Set3
            else:
                hot_count = hotzone_counts.get(draw_num, 0)
                super_hot_count = super_hotzone_counts.get(draw_num, 0)
            
            n = len(vals)
            
            # Mark hot zones from right to left
            for i in range(hot_count):
                idx = n - 1 - i  # start from the end
                if idx < 0:
                    break
                
                # Check if this position should be super hot
                if i < super_hot_count:
                    vals[idx] = vals[idx] + "**" if vals[idx] else "**"
                else:
                    vals[idx] = vals[idx] + "*" if vals[idx] else "*"
                    
        except:
            return vals  # parsing error: do nothing
    return vals

############################
# COMBINED TABLE
############################
def build_section_table(section_data, section):
    """Build a table for a specific section (Midday/Evening/Combined)"""
    results = {}
    
    # Build combined table
    combined_df = build_combined_table(section_data)
    results[f"{section}_combined"] = combined_df
    
    return results

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
        combined_df = build_section_table(section_data, section)
        results.update(combined_df)
        
        # Build R2-only table - DISABLED as per new unified flow
        # r2_df = build_r2_only_table(section_data)
        # results[f"{section}_r2"] = r2_df
        
        # Save tables if output_dir is provided
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
            for table_name, df in results.items():
                if df is not None and not df.empty:
                    csv_path = os.path.join(output_dir, f"{state_name}_{table_name}.csv")
                    df.to_csv(csv_path, index=False)
                    print(f"Saved {csv_path}")
            
            print(f"  Saved tables to {output_dir}")
    
    return results

def table_to_json_schema():
    """
    Returns a JSON schema representation of our table structures
    """
    return {
        "combined_table": {
            "columns": ["Set", "Draw", "RowType", "7", "6", "5", "4", "3", "2", "1"],
            "structure": {
                "Set": {"type": "string", "values": ["Set1", "Set2", "Set3"]},
                "Draw": {"type": "string", "pattern": "Draw[1-7]"},
                "RowType": {"type": "string", "values": ["DRAW_DATA", "R2", "R4", "R6", "R8"]},
                "7,6,5,4,3,2,1": {"type": "string", "format": "right-aligned with N/A padding"}
            },
            "ordering": [
                "Set3 -> Draw1 (all row types)",
                "Set2 -> Draw1 (all row types)",
                "Set1 -> Draw1-7 (all row types)"
            ]
        },
        "r2_only_table": {
            "columns": ["Set", "Draw", "7", "6", "5", "4", "3", "2", "1"],
            "structure": {
                "Set": {"type": "string", "values": ["Set1", "Set2", "Set3"]},
                "Draw": {"type": "string", "pattern": "Draw[1-7]"},
                "7,6,5,4,3,2,1": {"type": "string", "format": "right-aligned with N/A padding"}
            },
            "slicing_rules": {
                "Set3/Set2 Draw1": "First 3 items",
                "Set1 Draw1": "First 3 items",
                "Set1 Draw2": "First 2 items",
                "Set1 Draw3-7": "First 1 item"
            }
        },
        "hot_zones": {
            "Set1": {
                "Draw1": "Last 5 items",
                "Draw2": "Last 5 items",
                "Draw3": "Last 5 items",
                "Draw4": "Last 4 items",
                "Draw5": "Last 2 items"
            }
        }
    }

def data_to_json(section_data):
    """
    Converts section data to a JSON representation
    """
    return {
        "section_type": list(section_data.keys())[0],  # Midday/Evening/Combined
        "sets": {
            set_name: {
                draw_name: {
                    "draw_data": data.get("draw_data", []),
                    "R2": data.get("R2", []),
                    "R4": data.get("R4", []),
                    "R6": data.get("R6", []),
                    "R8": data.get("R8", [])
                }
                for draw_name, data in set_data.items()
            }
            for set_name, set_data in section_data.items()
        }
    }

# ---------------------------------------------------------------------------
#  deterministic combined-table builder (preserves order & hot-zones)        
# ---------------------------------------------------------------------------
SET_ORDER      = ["Set3", "Set2", "Set1"]             # visual top ➜ bottom
DRAW_ORDER     = [f"Draw{i}" for i in range(1, 8)]      # Draw1 … Draw7
ROWTYPE_ORDER  = ["draw_data", "R2", "R4", "R6", "R8"]

def build_combined_table(section_data):
    """Return DataFrame with rows ordered Set3→Set2→Set1 / Draw1→Draw7 / row-types."""
    rows = []
    if not section_data:
        return pd.DataFrame()

    for set_name in SET_ORDER:
        if set_name not in section_data:
            continue
        draw_map = section_data[set_name]

        for draw_name in DRAW_ORDER:
            if draw_name not in draw_map:
                continue
            rowtypes = draw_map[draw_name]

            for rtype in ROWTYPE_ORDER:
                if rtype not in rowtypes:
                    continue
                digits = rowtypes[rtype]

                # 1️⃣ canonicalise to zero-padded strings (keep leading zeros)
                vals = []
                for x in digits:
                    if x in (None, ""):
                        vals.append("")
                    else:
                        s = str(x).split(".")[0]  # drop trailing .0 if present
                        if s.isdigit() and len(s) <= 3:
                            s = s.zfill(3)
                        vals.append(s)

                # 2️⃣ apply hot-/super-hot markers
                vals = mark_hot_zones(set_name, draw_name, rtype, vals)

                # 3️⃣ right-align to 7 cells
                vals = (["N/A"] * (7 - len(vals)) + vals)[-7:]

                # 4️⃣ append row
                rows.append({
                    "Set": set_name,
                    "Draw": draw_name,
                    "RowType": rtype,
                    "7": vals[0], "6": vals[1], "5": vals[2],
                    "4": vals[3], "3": vals[4], "2": vals[5], "1": vals[6]
                })

    cols = ["Set", "Draw", "RowType", "7", "6", "5", "4", "3", "2", "1"]
    return pd.DataFrame(rows, columns=cols)

if __name__ == "__main__":
    # Demo with sample data
    print("This module is designed to be imported, not run directly.")
    print("For testing, import and use the functions with sample data.") 