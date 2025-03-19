# Lottery Data Analysis Tool

## Project Structure
```
scripts/
├── utils/
│   ├── streamlit_app.py    # Main Streamlit interface
│   ├── table_generator.py  # Table generation functions
│   ├── vtrac_utils.py     # V-TRAC functionality
│   ├── clean_data.py      # Data cleaning functions
│   ├── extract_data.py    # Data extraction logic
│   └── test_vtrac.py      # Standalone V-TRAC tester
data/
├── original/              # Original Excel files
└── cleaned/              # Cleaned state data
```

## Important Notes

### Git Practice
This is a practice change to demonstrate committing and syncing.

### GitHub Integration Test
Repository successfully connected on: [Current Date]
Testing Cursor Git Integration!

### Streamlit App (streamlit_app.py)
- **CRITICAL**: The app currently reprocesses all states when switching between states. This is inefficient and will be optimized in a future update.
- Use the correct function names from table_generator.py:
  - `build_section_table` (not build_section_table_simple)
  - `build_r2_only_table` (not build_r2_only_table_simple)

### Table Generation (table_generator.py)
- Contains logic for both combined and R2-only tables
- Includes hot zone marking functionality
- Uses custom slicing rules for R2 data:
  - Set3/Set2 Draw1: first 3 items
  - Set1 Draw1: first 3 items
  - Set1 Draw2: first 2 items
  - Set1 Draw3-Draw7: first 1 item

### V-TRAC Testing
- Use test_vtrac.py for testing V-TRAC functionality separately
- DO NOT modify V-TRAC implementation in the main app
- Run with: `python scripts/utils/test_vtrac.py`

## Known Issues
1. State reprocessing on state change (performance issue)
2. Path handling needs standardization
3. Excel file processing could be optimized

## Testing V-TRAC
To test V-TRAC functionality without affecting the main app:
1. Run `python scripts/utils/test_vtrac.py`
2. Use the interactive mode to test specific numbers
3. Check V-TRAC index and related combinations

## Future Improvements
1. Optimize state processing to cache results
2. Add proper error handling for Excel files
3. Implement proper GitHub version control
4. Add automated tests 