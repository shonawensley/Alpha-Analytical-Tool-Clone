#!/usr/bin/env python
"""
Demo script for TableFormatter
Displays lottery data in tabular format
"""

import json
import os
import sys
from table_formatter import TableFormatter

def main():
    """
    Main function to demonstrate table formatter
    """
    # Check if JSON file path is provided
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        # Default path if no arguments provided
        json_file = os.path.join('data', 'ai_exports', 'OntarioCanada4_ai_format_20250403_030615.json')
    
    if not os.path.exists(json_file):
        print(f"Error: JSON file not found: {json_file}")
        print("Usage: python table_formatter_demo.py [path/to/json_file]")
        return
    
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Create TableFormatter
    formatter = TableFormatter(json_data)
    
    # Display tables for each section and Set1
    for section in ["Midday", "Evening", "Combined"]:
        print(f"\n\n{'='*80}")
        print(f"SECTION: {section}, SET: Set1")
        print(f"{'='*80}\n")
        
        # Display the table
        table = formatter.display_table(section, "Set1", style="ascii")
        print(table)
        
        # Find clusters for "455" as an example
        print(f"\n\nClusters containing '455' pattern in {section}:Set1\n")
        clusters = formatter.find_clusters(section, "Set1", "455", min_cluster=2)
        cluster_table = formatter.display_clusters(clusters, style="ascii")
        print(cluster_table)
    
    # Example for highlighting a pattern
    highlight_pattern = "455"
    print(f"\n\n{'='*80}")
    print(f"HIGHLIGHTING PATTERN: '{highlight_pattern}' in COMBINED:Set1")
    print(f"{'='*80}\n")
    
    # Display the table with highlighted pattern
    table = formatter.display_table("Combined", "Set1", style="ascii", highlight_pattern=highlight_pattern)
    print(table)

if __name__ == "__main__":
    main() 