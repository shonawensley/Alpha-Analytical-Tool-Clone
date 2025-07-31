"""
Smoke test for auxiliary tools module.

This test ensures that run_aux_tools returns the expected dictionary structure
with the required keys for all configured states.
"""

import pytest
import pandas as pd
from pathlib import Path
import sys
import os

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.module_d_auxiliary_tools.integration import run_aux_tools, get_available_states


class TestAuxiliaryToolsSmoke:
    """Smoke tests for auxiliary tools functionality."""
    
    def test_run_aux_tools_returns_expected_keys(self):
        """Test that run_aux_tools returns a dict with the mandatory keys."""
        # Use a mock state for testing if no real data is available
        state = "Connecticut4"
        
        # Run the auxiliary tools
        result = run_aux_tools(state)
        
        # Check that result is a dictionary
        assert isinstance(result, dict), "run_aux_tools should return a dictionary"
        
        # Check for mandatory keys
        expected_keys = {"boxed_vtrac", "overdue_pairs", "doubles_tracker"}
        actual_keys = set(result.keys())
        
        assert expected_keys.issubset(actual_keys), f"Missing required keys. Expected {expected_keys}, got {actual_keys}"
    
    def test_all_results_are_dataframes(self):
        """Test that all returned values are pandas DataFrames."""
        state = "Connecticut4"
        result = run_aux_tools(state)
        
        for key, value in result.items():
            assert isinstance(value, pd.DataFrame), f"Value for key '{key}' should be a pandas DataFrame, got {type(value)}"
    
    def test_boxed_vtrac_has_correct_columns(self):
        """Test that boxed_vtrac DataFrame has the expected columns."""
        state = "Connecticut4"
        result = run_aux_tools(state)
        
        boxed_vtrac = result["boxed_vtrac"]
        expected_columns = ['Index', 'Singles', 'Doubles']
        
        assert list(boxed_vtrac.columns) == expected_columns, f"boxed_vtrac should have columns {expected_columns}, got {list(boxed_vtrac.columns)}"
    
    def test_overdue_pairs_has_correct_columns(self):
        """Test that overdue_pairs DataFrame has the expected columns."""
        state = "Connecticut4"
        result = run_aux_tools(state)
        
        overdue_pairs = result["overdue_pairs"]
        expected_columns = ['Pair', 'Draws_Overdue', 'Color', 'Type']
        
        assert list(overdue_pairs.columns) == expected_columns, f"overdue_pairs should have columns {expected_columns}, got {list(overdue_pairs.columns)}"
    
    def test_doubles_tracker_has_correct_columns(self):
        """Test that doubles_tracker DataFrame has the expected columns."""
        state = "Connecticut4"
        result = run_aux_tools(state)
        
        doubles_tracker = result["doubles_tracker"]
        expected_columns = ['Double', 'Last_Seen', 'Frequency', 'Draws_Since']
        
        assert list(doubles_tracker.columns) == expected_columns, f"doubles_tracker should have columns {expected_columns}, got {list(doubles_tracker.columns)}"
    
    def test_empty_results_structure(self):
        """Test that empty results still have the correct structure."""
        # Test with a non-existent state to trigger empty results
        state = "NonExistentState99"
        result = run_aux_tools(state)
        
        # Should still return the expected keys with empty DataFrames
        expected_keys = {"boxed_vtrac", "overdue_pairs", "doubles_tracker"}
        assert expected_keys.issubset(set(result.keys())), "Empty results should still have required keys"
        
        # All values should be DataFrames (even if empty)
        for key, value in result.items():
            if key in expected_keys:
                assert isinstance(value, pd.DataFrame), f"Empty result for '{key}' should still be a DataFrame"
    
    @pytest.mark.parametrize("state", [
        "Connecticut4", "Delaware4", "Florida4", "Georgia4", "Indiana4",
        "Michigan4", "NewJersey4", "Ohio4", "Pennsylvania4", "Texas4"
    ])
    def test_multiple_states_return_valid_structure(self, state):
        """Test that multiple states return valid results structure."""
        result = run_aux_tools(state)
        
        # Check basic structure
        assert isinstance(result, dict), f"Result for {state} should be a dictionary"
        
        required_keys = {"boxed_vtrac", "overdue_pairs", "doubles_tracker"}
        assert required_keys.issubset(set(result.keys())), f"Missing required keys for {state}"
        
        # Check all required results are DataFrames
        for key in required_keys:
            assert isinstance(result[key], pd.DataFrame), f"{key} for {state} should be a DataFrame"
    
    def test_get_available_states_returns_list(self):
        """Test that get_available_states returns a list."""
        states = get_available_states()
        assert isinstance(states, list), "get_available_states should return a list"
        
        # All states should be strings
        for state in states:
            assert isinstance(state, str), f"State name should be string, got {type(state)}"
    
    def test_function_handles_missing_data_gracefully(self):
        """Test that functions handle missing data without crashing."""
        # Test with non-existent data directory
        from pathlib import Path
        non_existent_dir = Path("/nonexistent/directory")
        
        try:
            result = run_aux_tools("Connecticut4", data_dir=non_existent_dir)
            # Should not crash, should return empty results
            assert isinstance(result, dict), "Should return dict even with missing data"
            
            required_keys = {"boxed_vtrac", "overdue_pairs", "doubles_tracker"}
            assert required_keys.issubset(set(result.keys())), "Should have required keys even with missing data"
            
        except Exception as e:
            pytest.fail(f"Function should handle missing data gracefully, but raised: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])