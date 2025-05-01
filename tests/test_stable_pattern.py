import os
import sys
import unittest

# Add project root to sys.path to allow importing from scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

try:
    from scripts.core.stable_pattern_extractor_full import run_stable_pattern_extraction
except ImportError:
    print("ERROR: Cannot import run_stable_pattern_extraction. Ensure script exists and path is correct.")
    run_stable_pattern_extraction = None # Define as None to avoid NameError later

class TestStablePatternExtractor(unittest.TestCase):

    def test_basic_pattern_extraction(self):
        """Tests if a known simple pattern is extracted and scored."""
        if run_stable_pattern_extraction is None:
            self.skipTest("Skipping test because stable pattern extractor could not be imported.")

        # Minimal JSON structure similar to what convert_csv_to_json_structure produces
        # Using a known pattern '123' in R2, column 1
        test_data = {
            "sections": {
                "Combined": {
                    "sets": {
                        "Set1": {
                            "draws": {
                                "Draw1": {
                                    "pattern_variations": {
                                        "R2": ["", "", "", "", "", "", "5123"], # Pattern in col 1
                                        "R4": ["", "", "", "", "", "", ""],
                                        "R6": ["", "", "", "", "", "", ""],
                                        "R8": ["", "", "", "", "", "", ""]
                                    },
                                    "metadata": {}
                                }
                            }
                        }
                    }
                }
            }
        }

        results = run_stable_pattern_extraction(test_data)

        # Check basic structure of results
        self.assertIn("Combined", results)
        self.assertIn("Set1", results["Combined"])
        self.assertTrue(len(results["Combined"]["Set1"]) > 0, "No draws processed for Set1")
        self.assertTrue(len(results["Combined"]["Set1"][0]) > 0, "No columns processed for Draw1")

        # Check if the specific pattern '123' was found in the expected column (column 1 => index 6)
        col_1_patterns = results["Combined"]["Set1"][0][6] # Draw1 (index 0), Column 1 (index 6)
        self.assertIn("123", col_1_patterns, "Pattern '123' not found in Column 1 results")

        # Check if the found pattern has a score > 0 (basic scoring check)
        self.assertIn("score", col_1_patterns["123"])
        self.assertGreater(col_1_patterns["123"]["score"], 0, "Pattern '123' score is not greater than 0")

if __name__ == '__main__':
    unittest.main() 