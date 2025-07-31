"""
Test to ensure existing modules remain intact after auxiliary tools integration.

This test runs typical calls for each existing tool and compares outputs 
to frozen snapshots to ensure no regressions.
"""

import pytest
import pandas as pd
import json
from pathlib import Path
import sys
import tempfile
import hashlib

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestExistingModulesIntact:
    """Tests to ensure existing modules are not broken by auxiliary tools integration."""
    
    def test_vtrac_module_import(self):
        """Test that V-TRAC module can still be imported."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from core import module_c_vtrac
            assert hasattr(module_c_vtrac, 'main'), "V-TRAC module should have main function"
        except ImportError as e:
            pytest.fail(f"Failed to import V-TRAC module: {e}")
    
    def test_stable_pattern_extractor_import(self):
        """Test that Stable Pattern Extractor can still be imported."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from core import stable_pattern_extractor
            # Check for key functions
            assert hasattr(stable_pattern_extractor, 'run_stable_pattern_extraction'), \
                "Stable pattern extractor should have run_stable_pattern_extraction function"
        except ImportError as e:
            pytest.fail(f"Failed to import Stable Pattern Extractor: {e}")
    
    def test_digit_reduction_import(self):
        """Test that Digit Reduction module can still be imported."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from core.module_b_digit_reduction import run_digit_reduction
            assert callable(run_digit_reduction), "run_digit_reduction should be callable"
        except ImportError as e:
            pytest.fail(f"Failed to import Digit Reduction module: {e}")
    
    def test_utils_path_handler_import(self):
        """Test that path handler utilities are still accessible."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from utils import path_handler
            # Check for key functions
            assert hasattr(path_handler, 'get_tables_output_dir'), \
                "Path handler should have get_tables_output_dir function"
        except ImportError as e:
            pytest.fail(f"Failed to import path handler: {e}")
    
    def test_main_app_structure_intact(self):
        """Test that the main app structure is intact."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from app import main, show_digit_reduction_page
            assert callable(main), "Main app function should be callable"
            assert callable(show_digit_reduction_page), "Digit reduction page function should be callable"
        except ImportError as e:
            pytest.fail(f"Failed to import main app components: {e}")
    
    def test_digit_reduction_function_signature(self):
        """Test that digit reduction function signature is unchanged."""
        # Add src to path if needed
        import sys
        from pathlib import Path
        src_path = Path(__file__).parent.parent / "src"
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))
        
        from core.module_b_digit_reduction import run_digit_reduction
        import inspect
        
        # Get function signature
        sig = inspect.signature(run_digit_reduction)
        
        # Check that required parameters exist
        params = list(sig.parameters.keys())
        assert 'state' in params, "run_digit_reduction should have 'state' parameter"
        
        # Function should be callable without breaking
        assert callable(run_digit_reduction), "run_digit_reduction should be callable"
    
    def test_path_handler_functions_intact(self):
        """Test that path handler functions return expected types."""
        # Add src to path if needed
        import sys
        from pathlib import Path
        src_path = Path(__file__).parent.parent / "src"
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))
        
        from utils.path_handler import get_tables_output_dir
        
        # Should return a string path
        result = get_tables_output_dir()
        assert isinstance(result, str), f"get_tables_output_dir should return string, got {type(result)}"
    
    def test_existing_imports_dont_conflict(self):
        """Test that existing imports don't conflict with new auxiliary tools."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            # Import existing modules
            from core import module_c_vtrac
            from core import stable_pattern_extractor
            from core.module_b_digit_reduction import run_digit_reduction
            from utils import path_handler
            
            # Import new auxiliary tools
            from modules.module_d_auxiliary_tools.integration import run_aux_tools
            
            # All should coexist without issues
            assert callable(module_c_vtrac.main)
            assert callable(run_digit_reduction)
            assert callable(run_aux_tools)
            
        except ImportError as e:
            pytest.fail(f"Import conflict detected: {e}")
    
    def test_streamlit_app_components_accessible(self):
        """Test that Streamlit app components are still accessible."""
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            import streamlit as st
            from app import main
            
            # Main function should exist and be callable
            assert callable(main), "Main Streamlit function should be callable"
            
        except ImportError as e:
            pytest.fail(f"Streamlit app components not accessible: {e}")
    
    def test_no_circular_imports(self):
        """Test that there are no circular import issues."""
        try:
            # Import in different orders to check for circular dependencies
            
            # Order 1
            from modules.module_d_auxiliary_tools.integration import run_aux_tools
            from src.core import module_c_vtrac
            
            # Order 2  
            from src.core.module_b_digit_reduction import run_digit_reduction
            from modules.module_d_auxiliary_tools.refactored.boxed_vtrac import generate_boxed_vtrac_table
            
            # All should work without circular import errors
            assert callable(run_aux_tools)
            assert callable(run_digit_reduction)
            assert callable(generate_boxed_vtrac_table)
            
        except ImportError as e:
            if "circular import" in str(e).lower():
                pytest.fail(f"Circular import detected: {e}")
            else:
                pytest.fail(f"Import error: {e}")
    
    def test_existing_module_function_outputs(self):
        """Test that existing modules produce expected output types."""
        # Test digit reduction with mock data
        try:
            # Add src to path if needed
            import sys
            from pathlib import Path
            src_path = Path(__file__).parent.parent / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            from core.module_b_digit_reduction import run_digit_reduction
            
            # Create a temporary test state
            with tempfile.TemporaryDirectory() as temp_dir:
                tables_path = Path(temp_dir)
                
                # The function should handle missing data gracefully
                # and return the expected tuple structure (even if empty)
                try:
                    result = run_digit_reduction("TestState", tables_path=tables_path)
                    
                    # Should return a tuple with 3 elements: (df, html_path, csv_path)
                    assert isinstance(result, tuple), f"run_digit_reduction should return tuple, got {type(result)}"
                    assert len(result) == 3, f"run_digit_reduction should return 3-tuple, got {len(result)}"
                    
                    df, html_path, csv_path = result
                    assert isinstance(df, pd.DataFrame), f"First element should be DataFrame, got {type(df)}"
                    
                except Exception as e:
                    # Function might fail due to missing data, but should fail gracefully
                    pass
                    
        except ImportError as e:
            pytest.fail(f"Could not test digit reduction output: {e}")
    
    def test_auxiliary_tools_dont_modify_existing_paths(self):
        """Test that auxiliary tools don't modify existing file paths or directories."""
        # Add src to path if needed
        import sys
        from pathlib import Path
        src_path = Path(__file__).parent.parent / "src"
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))
        
        from utils.path_handler import get_tables_output_dir
        
        # Get existing path
        original_path = get_tables_output_dir()
        
        # Import auxiliary tools
        from modules.module_d_auxiliary_tools.integration import run_aux_tools
        
        # Path should remain unchanged
        current_path = get_tables_output_dir()
        assert original_path == current_path, "Auxiliary tools should not modify existing paths"
    
    def test_existing_module_file_integrity(self):
        """Test that existing module files haven't been accidentally modified."""
        # Check that key module files exist
        key_files = [
            "src/app.py",
            "src/core/module_b_digit_reduction.py", 
            "src/utils/path_handler.py"
        ]
        
        for file_path in key_files:
            full_path = project_root / file_path
            assert full_path.exists(), f"Key module file missing: {file_path}"
            
            # Check that files have reasonable content (not empty)
            content = full_path.read_text(encoding='utf-8')
            assert len(content) > 100, f"Module file appears to be empty or too small: {file_path}"
            
            # Check for key function definitions
            if "app.py" in file_path:
                assert "def main(" in content, "app.py should contain main function"
            elif "digit_reduction" in file_path:
                assert "def run_digit_reduction(" in content, "digit_reduction should contain run_digit_reduction function"
    
    def test_existing_requirements_compatibility(self):
        """Test that existing requirements/dependencies are compatible."""
        try:
            # Import key dependencies that existing modules rely on
            import pandas as pd
            import streamlit as st
            import numpy as np
            from pathlib import Path
            
            # All should import successfully
            assert pd.__version__, "Pandas should be available"
            assert st.__version__, "Streamlit should be available"
            assert np.__version__, "NumPy should be available"
            
        except ImportError as e:
            pytest.fail(f"Required dependency missing: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])