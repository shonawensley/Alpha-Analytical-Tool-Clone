#!/usr/bin/env python
"""
test_analysis.py - Enhanced test script for analyzing lottery pattern variations

This script analyzes lottery patterns (R2/R4/R6/R8) using the AI-friendly JSON format
that's already structured with all pattern variations and metadata.

PATTERN STRUCTURE LEGEND:
-------------------------
1. Combined Table Structure:
   - Each section (Midday/Evening/Combined) contains:
     * Set3 Draw1: Previous 2 days' patterns
     * Set2 Draw1: Previous day's patterns
     * Set1 Draw1-7: Current day patterns with progressive reduction

2. Hot Zone Indicators:
   - In CSV/Excel format:
     * Single * = Hot zone item
     * Double ** = Super hot zone item (subset of hot zone)
   
   - Hot Zone Distribution (Set1):
     * Draw1: Last 5 items are hot (last 3 are super hot)
     * Draw2: Last 4 items are hot (last 2 are super hot)
     * Draw3: Last 3 items are hot (last 2 are super hot)
     * Draw4: Last 2 items are hot (both are super hot)
     * Draw5: Last 2 items are hot (both are super hot)

3. Pattern Box Structure:
   Each Set/Draw contains 4 pattern types in this order:
   - R2 (top row)
   - R4 (second row)
   - R6 (third row)
   - R8 (bottom row)

4. Column Structure:
   - 7 columns for full patterns (right to left)
   - Fewer columns in later draws (Draw7 has only 1 column)
   - Right-aligned with 'N/A' padding on left

Example usage with ChatGPT:
```python
from test_analysis import LotteryAnalyzer

# Just paste this JSON data into ChatGPT along with this code
json_data = {
    "state_name": "OntarioCanada4",
    "sections": {
        "Midday": {
            "sets": {
                "Set1": {
                    "draws": {
                        "Draw1": {
                            "pattern_variations": {
                                "R2": ["559244133877", "5924133877", "9241338"],
                                "R4": ["255983344771", "2598334771", "2983341"],
                                "R6": ["817755933244", "8177593324", "8193324"],
                                "R8": ["771983324455", "7719833245", "1983324"]
                            },
                            "metadata": {
                                "is_hot_zone": true,
                                "hot_zone_count": 5,
                                "hot_zone_indicators": {
                                    "R2": ["", "", "*", "**", "**", "**"],  # Last 5 items, last 3 super hot
                                    "R4": ["", "", "*", "**", "**", "**"],
                                    "R6": ["", "", "*", "**", "**", "**"],
                                    "R8": ["", "", "*", "**", "**", "**"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Create analyzer with your JSON data
analyzer = LotteryAnalyzer(json_data)

# Analyze patterns with hot zone information
patterns = analyzer.get_all_patterns("Set1", "Draw1", "Midday")
print("Patterns found:", patterns)

# Get hot zone patterns with indicators
hot = analyzer.get_hot_zone_patterns("Midday")
print("Hot zone patterns:", hot)
```
"""

import json
from collections import defaultdict

class LotteryAnalyzer:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.state = json_data["state_name"]
        
    def get_all_patterns(self, set_name, draw_name, section="Midday"):
        """
        Get all pattern variations (R2/R4/R6/R8) for a specific set/draw
        
        Args:
            set_name: 'Set1', 'Set2', or 'Set3'
            draw_name: 'Draw1' through 'Draw7'
            section: 'Midday', 'Evening', or 'Combined'
            
        Returns:
            Dictionary with pattern variations and hot zone indicators
        """
        try:
            draw_data = self.data["sections"][section]["sets"][set_name]["draws"][draw_name]
            result = {
                "patterns": draw_data["pattern_variations"],
                "metadata": draw_data["metadata"]
            }
            
            # Add hot zone explanation if it's a hot zone
            if draw_data["metadata"]["is_hot_zone"]:
                result["hot_zone_info"] = self._get_hot_zone_explanation(draw_name)
            
            return result
        except KeyError:
            return {}
            
    def _get_hot_zone_explanation(self, draw_name):
        """Get explanation of hot zone structure for a draw"""
        hot_zone_info = {
            "Draw1": {
                "total_hot": 5,
                "super_hot": 3,
                "explanation": "Last 5 items are hot, last 3 are super hot"
            },
            "Draw2": {
                "total_hot": 4,
                "super_hot": 2,
                "explanation": "Last 4 items are hot, last 2 are super hot"
            },
            "Draw3": {
                "total_hot": 3,
                "super_hot": 2,
                "explanation": "Last 3 items are hot, last 2 are super hot"
            },
            "Draw4": {
                "total_hot": 2,
                "super_hot": 2,
                "explanation": "Last 2 items are hot, both are super hot"
            },
            "Draw5": {
                "total_hot": 2,
                "super_hot": 2,
                "explanation": "Last 2 items are hot, both are super hot"
            }
        }
        return hot_zone_info.get(draw_name, {})
        
    def get_hot_zone_patterns(self, section="Midday"):
        """
        Get patterns from hot zones in Set1 with detailed hot zone information
        
        Returns:
            Dictionary mapping draw numbers to hot zone patterns with indicators
        """
        hot_zones = {}
        set1_draws = self.data["sections"][section]["sets"]["Set1"]["draws"]
        
        for draw_name, draw_data in set1_draws.items():
            if draw_data["metadata"]["is_hot_zone"]:
                hot_count = draw_data["metadata"]["hot_zone_count"]
                patterns = {}
                indicators = {}
                
                # Get patterns and their hot zone indicators
                for ptype, strings in draw_data["pattern_variations"].items():
                    patterns[ptype] = strings[-hot_count:] if len(strings) >= hot_count else strings
                    indicators[ptype] = self._generate_hot_indicators(draw_name, len(strings))
                    
                hot_zones[draw_name] = {
                    "patterns": patterns,
                    "hot_zone_count": hot_count,
                    "indicators": indicators,
                    "explanation": self._get_hot_zone_explanation(draw_name)
                }
                
        return hot_zones
        
    def _generate_hot_indicators(self, draw_name, total_length):
        """Generate hot zone indicators for a pattern"""
        indicators = [""] * total_length  # Initialize with no indicators
        
        hot_info = self._get_hot_zone_explanation(draw_name)
        if not hot_info:
            return indicators
            
        # Add indicators from right to left
        total_hot = hot_info["total_hot"]
        super_hot = hot_info["super_hot"]
        
        # Add regular hot indicators
        for i in range(total_hot):
            if i < len(indicators):
                indicators[-(i+1)] = "*"
                
        # Override with super hot indicators
        for i in range(super_hot):
            if i < len(indicators):
                indicators[-(i+1)] = "**"
                
        return indicators
        
    def analyze_pattern_relationships(self, patterns):
        """
        Analyze relationships between R2/R4/R6/R8 patterns
        
        Args:
            patterns: Dictionary with R2/R4/R6/R8 pattern lists
            
        Returns:
            Dictionary with pattern analysis
        """
        analysis = {
            'pattern_lengths': {},
            'common_endings': defaultdict(list),
            'pattern_persistence': {},
            'cross_pattern_matches': defaultdict(list)
        }
        
        # Analyze pattern lengths
        for ptype, strings in patterns.items():
            analysis['pattern_lengths'][ptype] = [len(s) for s in strings]
            
        # Find common endings (last 3 digits)
        for ptype, strings in patterns.items():
            for s in strings:
                if len(s) >= 3:
                    ending = s[-3:]
                    analysis['common_endings'][ptype].append(ending)
                    
        # Check pattern persistence
        for ptype, strings in patterns.items():
            repeats = defaultdict(int)
            for s in strings:
                repeats[s] += 1
            analysis['pattern_persistence'][ptype] = {
                k: v for k, v in repeats.items() if v > 1
            }
            
        # Look for matches across pattern types
        all_endings = set()
        for strings in patterns.values():
            for s in strings:
                if len(s) >= 3:
                    all_endings.add(s[-3:])
                    
        for ending in all_endings:
            matches = []
            for ptype, strings in patterns.items():
                if any(s.endswith(ending) for s in strings):
                    matches.append(ptype)
            if len(matches) > 1:
                analysis['cross_pattern_matches'][ending] = matches
                
        return dict(analysis)
        
    def find_stable_patterns(self, section='Midday'):
        """
        Find patterns that remain stable across draws
        
        Args:
            section: 'Midday', 'Evening', or 'Combined'
            
        Returns:
            Dictionary of stable patterns
        """
        stable = defaultdict(list)
        set1_draws = self.data["sections"][section]["sets"]["Set1"]["draws"]
        
        # Check all draws
        for draw_name, draw_data in set1_draws.items():
            # Track patterns that appear in multiple positions
            for ptype, strings in draw_data["pattern_variations"].items():
                for s in strings:
                    if len(s) >= 3:  # Only consider patterns of length 3+
                        stable[f"{ptype}_{s}"].append(draw_name)
                        
        # Filter for patterns that appear multiple times
        return {k: v for k, v in stable.items() if len(v) > 1}
        
    def analyze_cross_section_patterns(self):
        """
        Analyze patterns across Midday/Evening/Combined sections
        
        Returns:
            Dictionary of patterns that appear in multiple sections
        """
        section_patterns = {}
        cross_matches = defaultdict(list)
        
        # Collect patterns from each section's Set1/Draw1
        for section in ["Midday", "Evening", "Combined"]:
            patterns = self.get_all_patterns("Set1", "Draw1", section)
            section_patterns[section] = patterns
            
            # Track all unique patterns
            for ptype, strings in patterns.items():
                for s in strings:
                    if len(s) >= 3:  # Only consider patterns of length 3+
                        cross_matches[s].append(section)
                        
        # Filter for patterns that appear in multiple sections
        return {
            "cross_section_matches": {
                k: v for k, v in cross_matches.items() if len(v) > 1
            },
            "section_patterns": section_patterns
        }

def demo():
    """Demo usage with sample JSON data including hot zone indicators"""
    # Sample JSON data with hot zone indicators
    sample_data = {
        "state_name": "OntarioCanada4",
        "sections": {
            "Midday": {
                "sets": {
                    "Set1": {
                        "draws": {
                            "Draw1": {
                                "pattern_variations": {
                                    "R2": ["559244133877", "5924133877", "9241338"],
                                    "R4": ["255983344771", "2598334771", "2983341"],
                                    "R6": ["817755933244", "8177593324", "8193324"],
                                    "R8": ["771983324455", "7719833245", "1983324"]
                                },
                                "metadata": {
                                    "is_hot_zone": True,
                                    "hot_zone_count": 5,
                                    "hot_zone_indicators": {
                                        "R2": ["", "", "*", "**", "**", "**"],
                                        "R4": ["", "", "*", "**", "**", "**"],
                                        "R6": ["", "", "*", "**", "**", "**"],
                                        "R8": ["", "", "*", "**", "**", "**"]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    # Create analyzer
    analyzer = LotteryAnalyzer(sample_data)
    
    print("\n=== Pattern Analysis Demo with Hot Zones ===")
    
    # 1. Get all patterns with hot zone information
    print("\n1. Set1/Draw1 Patterns and Hot Zones:")
    result = analyzer.get_all_patterns("Set1", "Draw1", "Midday")
    print("\nPatterns:")
    for ptype, strings in result["patterns"].items():
        print(f"{ptype}: {strings}")
    print("\nHot Zone Info:")
    print(json.dumps(result.get("hot_zone_info", {}), indent=2))
    
    # 2. Get hot zone patterns with indicators
    print("\n2. Hot Zone Patterns with Indicators:")
    hot_patterns = analyzer.get_hot_zone_patterns("Midday")
    for draw, data in hot_patterns.items():
        print(f"\n{draw}:")
        print(f"Hot zone count: {data['hot_zone_count']}")
        print("Explanation:", data['explanation']['explanation'])
        print("\nPatterns with indicators:")
        for ptype in ["R2", "R4", "R6", "R8"]:
            if ptype in data['patterns']:
                print(f"{ptype}:")
                print("  Patterns:", data['patterns'][ptype])
                print("  Indicators:", data['indicators'][ptype])

if __name__ == "__main__":
    demo() 