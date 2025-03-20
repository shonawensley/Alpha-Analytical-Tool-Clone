#!/usr/bin/env python
"""
generate_sample.py - Generate sample lottery data and tables for documentation
"""
import json
import os
import sys
import pandas as pd

# Add the project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from scripts.utils.table_generator import (
    build_section_table,
    build_r2_only_table,
    print_ascii_table
)

def generate_sample_data():
    """Generate a sample dataset that demonstrates all key features"""
    return {
        "Midday": {
            "Set3": {
                "Draw1": {
                    "draw_data": ["934", "916", "319", "917", "723", "753", "832"],
                    "R2": ["55924001877", "552400877", "552400877", "55240087", "554008", "54008", "5400"],
                    "R4": ["25590084771", "255008477", "255008477", "25500847", "550084", "50084", "5004"],
                    "R6": ["81770055924", "877005524", "877005524", "87005524", "800554", "80054", "0054"],
                    "R8": ["77001982455", "770082455", "770082455", "70082455", "008455", "00845", "0045"]
                }
            },
            "Set2": {
                "Draw1": {
                    "draw_data": ["827", "705", "130", "246", "640", "008", "390"],
                    "R2": ["992440013866", "99244013866", "99244866", "99486", "998", "99", "9"],
                    "R4": ["299006683441", "29906683441", "29966844", "99684", "998", "99", "9"],
                    "R6": ["668100993244", "66810993244", "66899244", "68994", "899", "99", "9"],
                    "R8": ["001998366244", "01998366244", "99866244", "99864", "998", "99", "9"]
                }
            },
            "Set1": {
                "Draw1": {
                    "draw_data": ["705", "130", "246", "640", "008", "390", "408"],
                    "R2": ["992440133866", "992443866", "994386", "9938", "993", "9", "9"],
                    "R4": ["299066833441", "299668344", "996834", "9983", "993", "9", "9"],
                    "R6": ["668109933244", "668993244", "689934", "8993", "993", "9", "9"],
                    "R8": ["019983366244", "998366244", "998364", "9983", "993", "9", "9"]
                },
                "Draw2": {
                    "R2": ["59924413866", "59941386", "599138", "59913", "591", "591"],
                    "R4": ["25996683441", "59968341", "599831", "59931", "591", "591"],
                    "R6": ["66815993244", "68159934", "815993", "15993", "159", "159"],
                    "R8": ["19983662445", "19983645", "199835", "19935", "195", "195"]
                }
            }
        }
    }

def export_sample(output_dir="sample_output"):
    """Generate and export sample data in multiple formats"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sample data
    data = generate_sample_data()
    
    # 1. Save raw data as JSON
    with open(os.path.join(output_dir, "sample_data.json"), "w") as f:
        json.dump(data, f, indent=2)
    
    # 2. Generate and save tables
    section_data = data["Midday"]
    
    # Combined table
    combined_df = build_section_table(section_data)
    combined_df.to_csv(os.path.join(output_dir, "combined_table.csv"), index=False)
    with open(os.path.join(output_dir, "combined_table.md"), "w") as f:
        f.write(combined_df.to_markdown(tablefmt="pipe", index=False))
    
    # R2-only table
    r2_df = build_r2_only_table(section_data)
    r2_df.to_csv(os.path.join(output_dir, "r2_table.csv"), index=False)
    with open(os.path.join(output_dir, "r2_table.md"), "w") as f:
        f.write(r2_df.to_markdown(tablefmt="pipe", index=False))
    
    # 3. Print ASCII versions to console
    print("\n=== Combined Table ===")
    print_ascii_table(combined_df)
    print("\n=== R2-only Table ===")
    print_ascii_table(r2_df)
    
    print(f"\nFiles exported to {output_dir}/")

if __name__ == "__main__":
    export_sample() 






   