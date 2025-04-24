#!/usr/bin/env python
"""
Table Formatter - Helper class to visualize lottery data in a tabular format
"""

from pattern_mapper import PatternMapper
import re

class TableFormatter:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.mapper = PatternMapper(json_data)
        
    def display_table(self, section, set_name, style="ascii", highlight_pattern=None):
        """
        Display a formatted table for a section
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            style (str): "ascii" or "markdown"
            highlight_pattern (str, optional): Pattern to highlight
            
        Returns:
            str: Formatted table
        """
        if style == "ascii":
            return self._generate_ascii_table(section, set_name, highlight_pattern)
        else:
            return self._generate_markdown_table(section, set_name, highlight_pattern)
            
    def _generate_ascii_table(self, section, set_name, highlight_pattern):
        """Generate ASCII formatted table"""
        # Header
        header = "+" + "-"*9 + "+"
        for i in range(7):
            header += "-"*8 + "+"
        
        column_header = "| Draw    |"
        for i in range(7, 0, -1):
            column_header += f" Col {i}  |"
        
        divider = "+" + "-"*9 + "+"
        for i in range(7):
            divider += "-"*8 + "+"
            
        rows = [header, column_header, divider]
        
        # For each draw (1-7)
        for draw_num in range(1, 8):
            draw_name = f"Draw{draw_num}"
            
            # Staircase structure: each draw has 8-draw_num columns
            column_count = 8 - draw_num
            
            # Draw header
            draw_row = f"| {draw_name:<7} |"
            for i in range(7):
                draw_row += "        |"
            rows.append(draw_row)
            
            # For each row type (R2, R4, R6, R8)
            for row_type in ["R2", "R4", "R6", "R8"]:
                try:
                    # Get patterns
                    draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
                    patterns = draw_data["pattern_variations"][row_type]
                    
                    # Row start
                    row = f"| {row_type:<7} |"
                    
                    # Empty spaces for staircasing
                    for i in range(7 - column_count):
                        row += "        |"
                        
                    # Add patterns
                    for i in range(column_count):
                        # Get pattern at reverse index (last element is column 1)
                        pattern_idx = column_count - i - 1
                        pattern = patterns[pattern_idx]
                        
                        # Only show first 6 chars
                        pattern_display = pattern[:6]
                        
                        # Mark hot zones
                        is_hot = False
                        if "is_hot_zone" in draw_data["metadata"] and draw_data["metadata"]["is_hot_zone"]:
                            if "hot_zone_indicators" in draw_data["metadata"]:
                                indicators = draw_data["metadata"]["hot_zone_indicators"][row_type]
                                if pattern_idx < len(indicators) and indicators[pattern_idx]:
                                    is_hot = True
                        
                        # Highlight pattern
                        if highlight_pattern and highlight_pattern in pattern:
                            pattern_display = f"!{pattern_display}!"
                            
                        if is_hot:
                            pattern_display = f"*{pattern_display}*"
                            
                        row += f" {pattern_display:<6} |"
                    
                    rows.append(row)
                except KeyError:
                    # Fallback if data is missing
                    row = f"| {row_type:<7} |"
                    for i in range(7):
                        row += "   N/A  |"
                    rows.append(row)
            
            rows.append(divider)
        
        return "\n".join(rows)
            
    def _generate_markdown_table(self, section, set_name, highlight_pattern):
        """Generate Markdown formatted table"""
        # Header
        header = "| Draw | "
        for i in range(7, 0, -1):
            header += f"Col {i} | "
        
        divider = "|------|"
        for i in range(7):
            divider += "------|"
            
        rows = [header, divider]
        
        # Generate rows similar to ASCII but with markdown formatting
        for draw_num in range(1, 8):
            draw_name = f"Draw{draw_num}"
            column_count = 8 - draw_num
            
            # Draw header
            draw_row = f"| **{draw_name}** |"
            for i in range(7):
                draw_row += " |"
            rows.append(draw_row)
            
            # Row types
            for row_type in ["R2", "R4", "R6", "R8"]:
                try:
                    # Get patterns
                    draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
                    patterns = draw_data["pattern_variations"][row_type]
                    
                    # Row start
                    row = f"| {row_type} |"
                    
                    # Empty spaces for staircasing
                    for i in range(7 - column_count):
                        row += " |"
                        
                    # Add patterns
                    for i in range(column_count):
                        pattern_idx = column_count - i - 1
                        pattern = patterns[pattern_idx]
                        
                        # Only show first 6 chars
                        pattern_display = pattern[:6]
                        
                        # Mark hot zones
                        is_hot = False
                        if "is_hot_zone" in draw_data["metadata"] and draw_data["metadata"]["is_hot_zone"]:
                            if "hot_zone_indicators" in draw_data["metadata"]:
                                indicators = draw_data["metadata"]["hot_zone_indicators"][row_type]
                                if pattern_idx < len(indicators) and indicators[pattern_idx]:
                                    is_hot = True
                        
                        # Highlight pattern
                        if highlight_pattern and highlight_pattern in pattern:
                            pattern_display = f"**{pattern_display}**"
                            
                        if is_hot:
                            pattern_display = f"*{pattern_display}*"
                            
                        row += f" {pattern_display} |"
                    
                    rows.append(row)
                except KeyError:
                    # Fallback if data is missing
                    row = f"| {row_type} |"
                    for i in range(7):
                        row += " N/A |"
                    rows.append(row)
        
        return "\n".join(rows)
    
    def find_clusters(self, section, set_name, pattern_fragment, min_cluster=2):
        """
        Find clusters of patterns containing the given fragment
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            pattern_fragment (str): Pattern to search for
            min_cluster (int): Minimum number to be considered a cluster
            
        Returns:
            dict: Clusters by location
        """
        clusters = {}
        
        # Check each draw
        for draw_num in range(1, 8):
            draw_name = f"Draw{draw_num}"
            
            try:
                # Make sure the draw exists
                if draw_name not in self.data["sections"][section]["sets"][set_name]["draws"]:
                    continue
                    
                # Check each valid column for this draw
                for col in range(1, 8 - draw_num + 1):
                    # Get the box
                    box = self.mapper.get_box(section, set_name, draw_name, col)
                    if not box:
                        continue
                    
                    # Count patterns containing fragment
                    matching_patterns = []
                    for row_type in ["R2", "R4", "R6", "R8"]:
                        if row_type in box and pattern_fragment in box[row_type]:
                            matching_patterns.append({
                                "row_type": row_type,
                                "pattern": box[row_type]
                            })
                    
                    # If we found a cluster
                    if len(matching_patterns) >= min_cluster:
                        location = f"{section}:{set_name}:{draw_name}:Column{col}"
                        clusters[location] = {
                            "matching_patterns": matching_patterns,
                            "count": len(matching_patterns),
                            "is_hot_zone": box["metadata"].get("is_hot_zone", False),
                            "metadata": box["metadata"]
                        }
            except (KeyError, TypeError):
                # Skip if we encounter any errors with this draw
                continue
        
        return clusters
    
    def display_clusters(self, clusters, style="ascii"):
        """
        Display clusters in a formatted table
        
        Args:
            clusters (dict): Output from find_clusters
            style (str): ascii or markdown
            
        Returns:
            str: Formatted table of clusters
        """
        if not clusters:
            return "No clusters found"
            
        if style == "ascii":
            rows = []
            header = "+--------------------------------+--------+------------------+---------------+"
            rows.append(header)
            rows.append("| Location                        | Count  | Patterns          | Hot Zone       |")
            rows.append(header)
            
            for location, data in clusters.items():
                patterns_str = ", ".join([f"{p['row_type']}:{p['pattern'][:4]}" for p in data["matching_patterns"]])
                hot_zone = "Yes" if data["is_hot_zone"] else "No"
                if len(patterns_str) > 16:
                    patterns_str = patterns_str[:13] + "..."
                
                row = f"| {location:<30} | {data['count']:<6} | {patterns_str:<16} | {hot_zone:<13} |"
                rows.append(row)
            
            rows.append(header)
            return "\n".join(rows)
        else:
            rows = []
            rows.append("| Location | Count | Patterns | Hot Zone |")
            rows.append("|----------|-------|----------|----------|")
            
            for location, data in clusters.items():
                patterns_str = ", ".join([f"{p['row_type']}:{p['pattern'][:4]}" for p in data["matching_patterns"]])
                hot_zone = "✓" if data["is_hot_zone"] else ""
                
                row = f"| {location} | {data['count']} | {patterns_str} | {hot_zone} |"
                rows.append(row)
            
            return "\n".join(rows) 