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
├── cleaned/              # Cleaned state data
├── archive/              # Excel exports of state tables
└── historical_files/     # Historical Pick3StatsC4 files
docs/
└── VTRAC_SYSTEM.md       # V-TRAC documentation
```

## Recent Updates

### Excel Export Feature (NEW)
- Export all tables (Midday, Evening, Combined) for a state to a single Excel file
- Tables are arranged side by side in the same layout as Streamlit
- Files are saved to `data/archive` with state name and timestamp
- Access via "Log All [State] Tables to Excel" button in the app

### Historical Files Management (NEW)
- Added `data/historical_files` directory for storing multiple Pick3StatsC4 files
- Allows tracking of historical data without disrupting current system
- Date selection feature coming soon to specify which file to process

### V-TRAC System
- Pattern matching system for identifying winning combinations
- See `docs/VTRAC_SYSTEM.md` for detailed documentation
- Currently under review for improvements

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
3. V-TRAC pattern highlighting needs improvement
4. Date selection for historical files pending

## Testing V-TRAC
To test V-TRAC functionality without affecting the main app:
1. Run `python scripts/utils/test_vtrac.py`
2. Use the interactive mode to test specific numbers
3. Check V-TRAC index and related combinations

## Future Improvements
1. Optimize state processing to cache results
2. Add date selection for historical files
3. Improve V-TRAC pattern highlighting
4. Add automated tests 