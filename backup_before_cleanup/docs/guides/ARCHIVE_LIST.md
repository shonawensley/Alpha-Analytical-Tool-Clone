# Archive Candidate List

This document lists scripts that can be safely moved to the archive directory. These scripts are either:
- Experimental versions replaced by better implementations
- Debugging/test scripts
- Obsolete functionality
- Temporary files

## Scripts to Archive

These scripts can be moved to `scripts/archive/`:

1. `scripts/Untitled-2.py.bak` - Backup/temporary file
2. `scripts/clustering_app_2.py` - Older version of clustering app
3. `scripts/clustering_app_2_new.py` - Partial implementation 
4. `scripts/vtrac_analyzer.py` - Replaced by enhanced_analyzer_final.py
5. `scripts/advanced_vtrac_analyzer.py` - Replaced by enhanced_analyzer_final.py
6. `scripts/test_vtrac.py` - Test file
7. `scripts/vtrac_test_app.py` - Test app
8. `scripts/run_simple_pattern_analyzer.bat` - Obsolete batch file
9. `scripts/simple_pattern_highlighter.py` - Replaced by enhanced features
10. `scripts/vtrac_html_test.py` - HTML test implementation
11. `scripts/test_vtrac_streamlit.py` - Test file
12. `scripts/generate_sample.py` - Sample data generator
13. `scripts/test_vtrac_interactive.py` - Interactive test
14. `scripts/test_components.py` - Component testing

## Batch Files to Archive

These batch files in the root directory can be moved to `batch/archive/`:

1. `run_clustering_app_2.bat` - Older version
2. `run_vtrac_test.bat` - Test file
3. `run_simple_pattern_analyzer.bat` - Obsolete
4. `run_pattern_highlighter.bat` - Replaced
5. `run_stable_pattern_test.bat` - Test file
6. `run_streamlit_auto_analyzer.bat` - Obsolete
7. `run_auto_pattern_analyzer.bat` - Obsolete
8. `run_table_formatter.bat` - Obsolete

## Keep These Core Scripts

These scripts should NOT be archived as they are part of the working core process:

1. `scripts/enhanced_analyzer_final.py` - Main V-TRAC analyzer
2. `scripts/streamlit_app_with_analyzer.py` - Integrated app
3. `scripts/run_process.py` - Core process script
4. All files in `scripts/utils/` - Core utilities

## How to Archive

To move a script to the archive:

```powershell
# For scripts
Move-Item "scripts\script_name.py" "scripts\archive\"

# For batch files
Move-Item "batch_file.bat" "batch\archive\"
```

Before archiving, ensure:
1. You've already copied the working scripts to `scripts/core/`
2. You're not removing any essential functionality
3. You've documented any significant code that might be referenced later 