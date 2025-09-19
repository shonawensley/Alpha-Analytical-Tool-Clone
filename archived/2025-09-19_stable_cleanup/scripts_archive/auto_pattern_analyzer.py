#!/usr/bin/env python
"""
Automatic Pattern Analyzer - Extracts and highlights significant patterns in lottery data
"""

import json
import os
import sys
from table_formatter import TableFormatter
from pattern_mapper import PatternMapper
from collections import defaultdict, Counter

class AutoPatternAnalyzer:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.formatter = TableFormatter(json_data)
        self.mapper = PatternMapper(json_data)
        
    def find_all_significant_patterns(self, min_cluster_size=2, min_frequency=3):
        """
        Automatically find all significant patterns across the data
        
        Args:
            min_cluster_size (int): Minimum number of rows to be considered a cluster
            min_frequency (int): Minimum frequency for a pattern to be considered significant
            
        Returns:
            dict: Significant patterns with their locations and scores
        """
        # Store all patterns found
        all_patterns = defaultdict(list)
        
        # Step 1: Find all clusters (vertical analysis)
        for section in ["Midday", "Evening", "Combined"]:
            for set_name in ["Set1", "Set2", "Set3"]:
                try:
                    # Skip if this section/set doesn't exist
                    if set_name not in self.data["sections"][section]["sets"]:
                        continue
                        
                    # Analyze each draw within this section/set
                    for draw_num in range(1, 8):
                        draw_name = f"Draw{draw_num}"
                        
                        # Skip if this draw doesn't exist
                        if draw_name not in self.data["sections"][section]["sets"][set_name]["draws"]:
                            continue
                            
                        # Check each valid column for this draw (staircase structure)
                        column_count = 8 - draw_num  # Draw1 has 7 columns, Draw7 has 1 column
                        
                        for col in range(1, column_count + 1):
                            # Get the box/cell
                            box = self.mapper.get_box(section, set_name, draw_name, col)
                            if not box:
                                continue
                                
                            # Extract significant patterns
                            self._extract_patterns_from_box(
                                box, section, set_name, draw_name, col, 
                                all_patterns, min_cluster_size
                            )
                except (KeyError, TypeError) as e:
                    # Skip if we encounter errors
                    continue
        
        # Step 2: Analyze pattern frequency and score each pattern
        scored_patterns = self._score_patterns(all_patterns, min_frequency)
        
        return scored_patterns
        
    def _extract_patterns_from_box(self, box, section, set_name, draw_name, column, 
                                  all_patterns, min_cluster_size):
        """
        Extract significant patterns from a box (cell in the table)
        """
        # Step 1: Find all 3+ digit sequences in the patterns
        digit_sequences = {}
        
        for row_type in ["R2", "R4", "R6", "R8"]:
            if row_type not in box:
                continue
                
            pattern = box[row_type]
            
            # Find all substrings of 3+ digits
            for i in range(len(pattern) - 2):
                for j in range(i + 3, min(i + 7, len(pattern) + 1)):
                    seq = pattern[i:j]
                    
                    # Track which rows this sequence appears in
                    if seq not in digit_sequences:
                        digit_sequences[seq] = set()
                    digit_sequences[seq].add(row_type)
        
        # Step 2: Filter for sequences that appear in multiple rows (clusters)
        for seq, rows in digit_sequences.items():
            if len(rows) >= min_cluster_size:
                # This is a significant pattern (appears in multiple rows)
                location = {
                    "section": section,
                    "set": set_name,
                    "draw": draw_name,
                    "column": column,
                    "rows": list(rows),
                    "is_hot_zone": box["metadata"].get("is_hot_zone", False),
                    "hot_zone_count": box["metadata"].get("hot_zone_count", 0)
                }
                
                all_patterns[seq].append(location)
    
    def _score_patterns(self, all_patterns, min_frequency):
        """
        Score the patterns based on frequency, hot zones, and other factors
        
        Args:
            all_patterns (dict): Dictionary mapping patterns to lists of locations
            min_frequency (int): Minimum frequency to be considered significant
            
        Returns:
            dict: Dictionary of patterns, scores, and summary information
        """
        scored_patterns = {}
        
        for pattern, locations in all_patterns.items():
            # Skip patterns that don't appear enough times
            if len(locations) < min_frequency:
                continue
                
            # Base score is the number of occurrences
            base_score = len(locations)
            
            # Extra points for hot zones
            hot_zone_bonus = sum(1 for loc in locations if loc["is_hot_zone"])
            
            # Extra points for larger clusters (more rows)
            cluster_size_bonus = sum(len(loc["rows"]) for loc in locations)
            
            # Extra points for appearing in different sections
            sections = set(loc["section"] for loc in locations)
            section_bonus = len(sections) * 2
            
            # Calculate total score
            total_score = base_score + hot_zone_bonus + cluster_size_bonus + section_bonus
            
            # Store the scored pattern
            scored_patterns[pattern] = {
                "score": total_score,
                "frequency": base_score,
                "hot_zone_count": hot_zone_bonus,
                "cluster_size_total": cluster_size_bonus,
                "section_count": len(sections),
                "locations": locations
            }
        
        return scored_patterns
    
    def get_top_patterns(self, count=10):
        """
        Get the top N highest-scoring patterns
        
        Args:
            count (int): Number of top patterns to return
            
        Returns:
            list: List of (pattern, score_info) tuples
        """
        scored_patterns = self.find_all_significant_patterns()
        
        # Sort by total score (descending)
        sorted_patterns = sorted(
            scored_patterns.items(), 
            key=lambda x: x[1]["score"], 
            reverse=True
        )
        
        return sorted_patterns[:count]
    
    def highlight_pattern_in_table(self, section, set_name, pattern, style="ascii"):
        """
        Generate a table with a specific pattern highlighted
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            pattern (str): Pattern to highlight
            style (str): "ascii" or "markdown"
            
        Returns:
            str: Formatted table with the pattern highlighted
        """
        return self.formatter.display_table(
            section, set_name, style=style, highlight_pattern=pattern
        )
    
    def display_top_patterns_summary(self, top_patterns):
        """
        Display a summary of the top patterns
        
        Args:
            top_patterns (list): List of (pattern, score_info) tuples
            
        Returns:
            str: Formatted summary table
        """
        rows = []
        
        header = "+----------+-------+------------+-----------+----------------+----------------+"
        rows.append(header)
        rows.append("| Pattern  | Score | Frequency | Hot Zones | Sections       | Example        |")
        rows.append(header)
        
        for pattern, info in top_patterns:
            # Get sections where this pattern appears
            sections = set(loc["section"] for loc in info["locations"])
            sections_str = ", ".join(sorted(sections))
            if len(sections_str) > 14:
                sections_str = sections_str[:11] + "..."
                
            # Get an example location
            example_loc = info["locations"][0]
            example = f"{example_loc['section']}:{example_loc['draw']}:{example_loc['column']}"
            if len(example) > 14:
                example = example[:11] + "..."
            
            row = f"| {pattern:<8} | {info['score']:<5} | {info['frequency']:<10} | {info['hot_zone_count']:<9} | {sections_str:<14} | {example:<14} |"
            rows.append(row)
        
        rows.append(header)
        return "\n".join(rows)
    
    def display_pattern_details(self, pattern, score_info):
        """
        Display detailed information about a specific pattern
        
        Args:
            pattern (str): The pattern
            score_info (dict): Score information for the pattern
            
        Returns:
            str: Formatted details
        """
        rows = []
        
        rows.append(f"Pattern: {pattern}")
        rows.append(f"Total Score: {score_info['score']}")
        rows.append(f"Frequency: {score_info['frequency']}")
        rows.append(f"Hot Zone Count: {score_info['hot_zone_count']}")
        rows.append(f"Cluster Size Total: {score_info['cluster_size_total']}")
        rows.append(f"Appears in {score_info['section_count']} sections")
        rows.append("")
        rows.append("Locations:")
        
        for i, loc in enumerate(score_info["locations"], 1):
            rows.append(f"{i}. {loc['section']}:{loc['set']}:{loc['draw']}:Column{loc['column']}")
            rows.append(f"   Rows: {', '.join(loc['rows'])}")
            rows.append(f"   Hot Zone: {'Yes' if loc['is_hot_zone'] else 'No'}")
        
        return "\n".join(rows)
        
    def generate_reports(self, output_dir="./outputs"):
        """
        Generate reports for the top patterns
        
        Args:
            output_dir (str): Directory to save the reports
            
        Returns:
            None
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Get top patterns
        top_patterns = self.get_top_patterns(count=20)
        
        # Generate summary report
        summary_path = os.path.join(output_dir, "top_patterns_summary.txt")
        with open(summary_path, "w") as f:
            f.write(self.display_top_patterns_summary(top_patterns))
        
        # Generate detailed reports for each top pattern
        for pattern, score_info in top_patterns[:10]:  # Top 10 only
            # Generate pattern details
            details = self.display_pattern_details(pattern, score_info)
            
            # Save to file
            pattern_path = os.path.join(output_dir, f"pattern_{pattern}_details.txt")
            with open(pattern_path, "w") as f:
                f.write(details)
                f.write("\n\n")
                
                # Include example tables
                if score_info["locations"]:
                    loc = score_info["locations"][0]
                    table = self.highlight_pattern_in_table(
                        loc["section"], loc["set"], pattern
                    )
                    f.write(f"Example Table ({loc['section']}:{loc['set']}) with {pattern} highlighted:\n\n")
                    f.write(table)

def main():
    """
    Main function to demonstrate auto pattern analyzer
    """
    # Check if JSON file path is provided
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        # Default path if no arguments provided
        json_file = os.path.join('data', 'ai_exports', 'OntarioCanada4_ai_format_20250403_030615.json')
    
    if not os.path.exists(json_file):
        print(f"Error: JSON file not found: {json_file}")
        print("Usage: python auto_pattern_analyzer.py [path/to/json_file]")
        return
    
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Create AutoPatternAnalyzer
    analyzer = AutoPatternAnalyzer(json_data)
    
    # Get top patterns
    print("\nAnalyzing patterns...\n")
    top_patterns = analyzer.get_top_patterns(count=10)
    
    # Display top patterns summary
    print("\nTOP PATTERNS SUMMARY:\n")
    summary = analyzer.display_top_patterns_summary(top_patterns)
    print(summary)
    
    # Display details for the top pattern
    if top_patterns:
        top_pattern, score_info = top_patterns[0]
        print(f"\nDETAILS FOR TOP PATTERN: {top_pattern}\n")
        details = analyzer.display_pattern_details(top_pattern, score_info)
        print(details)
        
        # Display an example table with the pattern highlighted
        if score_info["locations"]:
            loc = score_info["locations"][0]
            print(f"\nEXAMPLE TABLE ({loc['section']}:{loc['set']}) WITH {top_pattern} HIGHLIGHTED:\n")
            table = analyzer.highlight_pattern_in_table(loc["section"], loc["set"], top_pattern)
            print(table)
    
    # Generate reports
    print("\nGenerating reports...")
    analyzer.generate_reports()
    print("Reports generated in ./outputs directory")

if __name__ == "__main__":
    main() 