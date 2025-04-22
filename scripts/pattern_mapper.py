#!/usr/bin/env python
"""
Pattern Mapper - Helper class to navigate the lottery data structure
"""

class PatternMapper:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
    
    def get_box(self, section, set_name, draw_name, column):
        """
        Get data for a specific "box" (intersection of section/set/draw/column)
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            draw_name (str): Draw1/Draw2/etc.
            column (int): Column number (1-based)
            
        Returns:
            dict: Box data containing pattern for each row type
        """
        try:
            # Get the draw data
            draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
            
            # Get pattern variations
            pattern_variations = draw_data["pattern_variations"]
            
            # Create box data
            box = {}
            
            # For each row type, get the pattern at column position
            for row_type in ["R2", "R4", "R6", "R8"]:
                if row_type in pattern_variations:
                    patterns = pattern_variations[row_type]
                    
                    # Column is 1-based, but index is 0-based
                    # Also, we access columns in reverse (column 1 is the rightmost)
                    reversed_idx = len(patterns) - column
                    
                    if 0 <= reversed_idx < len(patterns):
                        box[row_type] = patterns[reversed_idx]
            
            # Add metadata
            box["metadata"] = {
                "is_hot_zone": draw_data["metadata"].get("is_hot_zone", False),
                "hot_zone_count": draw_data["metadata"].get("hot_zone_count", 0)
            }
            
            # Add hot zone indicators if available
            if "hot_zone_indicators" in draw_data["metadata"]:
                box["metadata"]["hot_zone_indicators"] = {}
                for row_type in ["R2", "R4", "R6", "R8"]:
                    if row_type in draw_data["metadata"]["hot_zone_indicators"]:
                        indicators = draw_data["metadata"]["hot_zone_indicators"][row_type]
                        reversed_idx = len(indicators) - column
                        if 0 <= reversed_idx < len(indicators):
                            box["metadata"]["hot_zone_indicators"][row_type] = indicators[reversed_idx]
            
            return box
        except (KeyError, IndexError):
            return None
    
    def get_pattern(self, section, set_name, draw_name, column, row_type):
        """
        Get a specific pattern
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            draw_name (str): Draw1/Draw2/etc.
            column (int): Column number (1-based)
            row_type (str): R2/R4/R6/R8
            
        Returns:
            str: Pattern or None if not found
        """
        box = self.get_box(section, set_name, draw_name, column)
        if box and row_type in box:
            return box[row_type]
        return None
    
    def find_all_patterns(self, pattern_fragment):
        """
        Find all occurrences of a pattern fragment across the data
        
        Args:
            pattern_fragment (str): Pattern to search for
            
        Returns:
            list: All locations where pattern appears
        """
        results = []
        
        for section in self.data["sections"]:
            for set_name in self.data["sections"][section]["sets"]:
                for draw_name in self.data["sections"][section]["sets"][set_name]["draws"]:
                    draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
                    
                    # Calculate max columns for this draw
                    max_columns = 0
                    for row_type in ["R2", "R4", "R6", "R8"]:
                        if row_type in draw_data["pattern_variations"]:
                            max_columns = max(max_columns, len(draw_data["pattern_variations"][row_type]))
                    
                    # Check each column (1-based)
                    for column in range(1, max_columns + 1):
                        box = self.get_box(section, set_name, draw_name, column)
                        if not box:
                            continue
                        
                        for row_type in ["R2", "R4", "R6", "R8"]:
                            if row_type in box and pattern_fragment in box[row_type]:
                                results.append({
                                    "section": section,
                                    "set": set_name,
                                    "draw": draw_name,
                                    "column": column,
                                    "row_type": row_type,
                                    "pattern": box[row_type],
                                    "is_hot_zone": box["metadata"]["is_hot_zone"]
                                })
        
        return results 