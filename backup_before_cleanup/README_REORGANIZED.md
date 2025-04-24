# Alpha Analytical Tool (Reorganized)

This project has been reorganized to create a cleaner structure for ongoing development. The core functionality remains the same, but files are now organized more logically.

## Project Structure

```
Alpha Analytical Tool/
├── batch/                   # Batch files to launch applications
│   ├── run_enhanced_analyzer.bat     # Runs the standalone V-TRAC analyzer
│   └── run_integrated_app.bat        # Runs the full integrated application
├── data/                    # Data storage (unchanged)
│   ├── original/            # Original Excel files
│   ├── cleaned/             # Cleaned CSV files
│   └── outputs/             # Generated output
├── docs/
│   └── guides/              # Detailed documentation
│       ├── CORE_PROCESS_GUIDE.md     # Explains the main data flow
│       └── VTRAC_ANALYZER_GUIDE.md   # Details on the V-TRAC analyzer
├── scripts/
│   ├── core/                # Production-ready scripts
│   │   ├── enhanced_analyzer_final.py      # Standalone V-TRAC analyzer
│   │   └── streamlit_app_with_analyzer.py  # Integrated application
│   ├── utils/               # Core utilities (unchanged)
│   ├── auxiliary/           # Future module development
│   └── archive/             # Deprecated/experimental scripts
```

## Quick Start

Use the batch files in the `batch` directory to run the applications:

1. **For V-TRAC Analysis only:**
   - Double-click `batch/run_enhanced_analyzer.bat`

2. **For the complete integrated application:**
   - Double-click `batch/run_integrated_app.bat`

## Documentation

The documentation has been reorganized and expanded:

1. **Core Process Guide:**
   - `docs/guides/CORE_PROCESS_GUIDE.md`
   - Explains the complete data flow from Excel to analysis
   - Reference for all developers to maintain consistency

2. **V-TRAC Analyzer Guide:**
   - `docs/guides/VTRAC_ANALYZER_GUIDE.md`
   - Detailed explanation of the V-TRAC analysis system
   - How to use and extend the analyzer

## Future Development

When adding new features:

1. Place new production scripts in `scripts/core/`
2. Create new batch files in `batch/`
3. Follow the pattern from the CORE_PROCESS_GUIDE
4. Add documentation for new features

## Original Files

All original files remain in their original locations for compatibility, but the reorganized structure should be used for future development. Eventually, once all development transitions to the new structure, the redundant files can be removed.

---

*This reorganization was done to improve project organization while maintaining compatibility with existing code and workflows.* 