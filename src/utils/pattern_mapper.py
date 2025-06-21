"""
Pattern Mapper - Helper class for lottery pattern analysis and location mapping.
"""

class PatternMapper:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.sections = ["Midday", "Evening", "Combined"]
        self.sets = ["Set3", "Set2", "Set1"]
        self.draws = [f"Draw{i}" for i in range(1, 8)]
        self.row_types = ["R2", "R4", "R6", "R8"]
        
    def get_box(self, section, set_name, draw_name, column):
        """
        Get all patterns in a specific box (vertical R2/R4/R6/R8 alignment)
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            draw_name (str): Draw1-Draw7
            column (int): Column number (1-7)
            
        Returns:
            dict: Patterns for each row type and metadata
        """
        try:
            draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
            patterns = {}
            
            # Get pattern for each row type
            for row_type in self.row_types:
                pattern_list = draw_data["pattern_variations"][row_type]
                # Adjust column index (7→1 to 0-based index)
                col_idx = len(pattern_list) - column
                if 0 <= col_idx < len(pattern_list):
                    patterns[row_type] = pattern_list[col_idx]
                    
            # Add metadata
            patterns["metadata"] = {
                "is_hot_zone": draw_data["metadata"]["is_hot_zone"],
                "hot_zone_count": draw_data["metadata"]["hot_zone_count"],
                "indicators": self._get_indicators(draw_data, column) if draw_data["metadata"]["is_hot_zone"] else None
            }
            
            return patterns
        except KeyError:
            return None
            
    def _get_indicators(self, draw_data, column):
        """Get hot zone indicators for a specific column"""
        indicators = {}
        if "hot_zone_indicators" in draw_data["metadata"]:
            for row_type in self.row_types:
                ind_list = draw_data["metadata"]["hot_zone_indicators"][row_type]
                # Adjust column index
                col_idx = len(ind_list) - column
                if 0 <= col_idx < len(ind_list):
                    indicators[row_type] = ind_list[col_idx]
        return indicators
        
    def get_hot_zones(self, section, set_name=None, draw_name=None):
        """
        Get all hot zone patterns
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str, optional): Filter by set
            draw_name (str, optional): Filter by draw
            
        Returns:
            dict: Hot zone patterns and their indicators
        """
        hot_zones = {}
        sets_to_check = [set_name] if set_name else self.sets
        
        for set_n in sets_to_check:
            if set_n not in self.data["sections"][section]["sets"]:
                continue
                
            draws_to_check = [draw_name] if draw_name else self.draws
            for draw_n in draws_to_check:
                if draw_n not in self.data["sections"][section]["sets"][set_n]["draws"]:
                    continue
                    
                draw_data = self.data["sections"][section]["sets"][set_n]["draws"][draw_n]
                if draw_data["metadata"]["is_hot_zone"]:
                    hot_zones[f"{set_n}:{draw_n}"] = {
                        "patterns": draw_data["pattern_variations"],
                        "hot_zone_count": draw_data["metadata"]["hot_zone_count"],
                        "indicators": draw_data["metadata"]["hot_zone_indicators"]
                    }
                    
        return hot_zones
        
    def track_pattern(self, pattern, section, set_name, analysis_type="horizontal"):
        """
        Track a pattern across columns or sections
        
        Args:
            pattern (str): Pattern to track
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            analysis_type (str): horizontal/vertical/cross_section
            
        Returns:
            dict: Pattern occurrences and their locations
        """
        occurrences = {}
        
        if analysis_type == "horizontal":
            # Track across columns in each draw
            for draw_name in self.draws:
                if draw_name not in self.data["sections"][section]["sets"][set_name]["draws"]:
                    continue
                    
                draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
                for row_type in self.row_types:
                    pattern_list = draw_data["pattern_variations"][row_type]
                    for i, p in enumerate(pattern_list):
                        if pattern in p:
                            col_num = len(pattern_list) - i
                            loc = f"{draw_name}:Column{col_num}:{row_type}"
                            occurrences[loc] = {
                                "full_pattern": p,
                                "is_hot_zone": draw_data["metadata"]["is_hot_zone"],
                                "indicator": self._get_indicators(draw_data, col_num)[row_type] if draw_data["metadata"]["is_hot_zone"] else None
                            }
                            
        return occurrences
        
    def check_consensus(self, section, set_name, draw_name, column):
        """
        Check if a box has consensus (same ending digits across R2/R4/R6/R8)
        
        Args:
            section (str): Midday/Evening/Combined
            set_name (str): Set1/Set2/Set3
            draw_name (str): Draw1-Draw7
            column (int): Column number (1-7)
            
        Returns:
            dict: Consensus information if found
        """
        box = self.get_box(section, set_name, draw_name, column)
        if not box:
            return None
            
        # Get last 1-2 digits from each row
        endings = {}
        for row_type in self.row_types:
            if row_type in box:
                pattern = box[row_type]
                # Take last 1-2 digits
                ending = pattern[-2:] if len(pattern) >= 2 else pattern[-1:]
                endings[row_type] = ending
                
        # Check if all endings are the same
        if len(set(endings.values())) == 1:
            return {
                "consensus": list(endings.values())[0],
                "location": f"{section}:{set_name}:{draw_name}:Column{column}",
                "is_hot_zone": box["metadata"]["is_hot_zone"],
                "indicators": box["metadata"]["indicators"]
            }
            
        return None

def demo():
    """Demo usage with sample data"""
    import json
    
    # Load sample data
    with open("data/ai_exports/Indiana4_ai_format_20250331_025625.json", "r") as f:
        data = json.load(f)
        
    # Create mapper
    mapper = PatternMapper(data)
    
    print("\n=== Pattern Mapper Demo ===")
    
    # 1. Get a specific box
    print("\n1. Box Analysis (Midday:Set1:Draw1:Column2):")
    box = mapper.get_box("Midday", "Set1", "Draw1", 2)
    for row_type, pattern in box.items():
        if row_type != "metadata":
            print(f"{row_type}: {pattern}")
    print("Metadata:", box["metadata"])
    
    # 2. Get hot zones
    print("\n2. Hot Zones (Midday:Set1):")
    hot_zones = mapper.get_hot_zones("Midday", "Set1")
    for location, data in hot_zones.items():
        print(f"\n{location}:")
        print(f"Hot zone count: {data['hot_zone_count']}")
        print("Indicators:", data['indicators'])
        
    # 3. Track a pattern
    print("\n3. Pattern Tracking ('224' in Midday:Set1):")
    occurrences = mapper.track_pattern("224", "Midday", "Set1")
    for location, data in occurrences.items():
        print(f"\n{location}:")
        print(f"Full pattern: {data['full_pattern']}")
        if data["indicator"]:
            print(f"Hot zone indicator: {data['indicator']}")
            
    # 4. Check consensus
    print("\n4. Consensus Check (Midday:Set1:Draw1:Column1):")
    consensus = mapper.check_consensus("Midday", "Set1", "Draw1", 1)
    if consensus:
        print(f"Found consensus: {consensus['consensus']}")
        print(f"Location: {consensus['location']}")
        if consensus["is_hot_zone"]:
            print("In hot zone with indicators:", consensus["indicators"])

if __name__ == "__main__":
    demo() 