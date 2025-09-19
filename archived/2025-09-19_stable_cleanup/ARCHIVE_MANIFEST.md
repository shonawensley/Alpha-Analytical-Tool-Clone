# Archive Manifest - 2025-09-19 Stable Pattern Cleanup

Items moved here were legacy Stable Pattern runners, demos, outputs, or tests that are no longer part of the integrated app flow. The canonical path remains src/app.py ? src/core/stable_pattern_extractor.py ? alpha_analytical/stable/__init__.py.

## Files
- run_stable_pattern_extractor.bat (root launcher)

## Directories
- scripts_archive/ (legacy Streamlit/demos + helpers)
- utils_old/ (superseded helper utilities)
- data_outputs/stable_patterns/ (historical exports from legacy scripts)
- scripts/run_stable_pattern_test.bat (batch helper for legacy demo)
- tests/test_stable_pattern.py (unit test targeting archived module_a_stable_patterns)
- legacy_scripts/stable_pattern_analyzer_standalone.py (standalone demo entrypoint)

These are preserved for reference; new work should rely on the canonical extractor and outputs under data/outputs/analysis/patterns/.
