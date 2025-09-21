# AAT9 – Aux Staging Manifest

These files and directories must remain available for the Auxiliary Tools feature. They hold the legacy boxed V-TRAC reference and analysis helpers that the staged Aux package imports during runtime.

## Required Legacy Assets
- `modules/module_d_auxiliary_tools/core_legacy/legacy_modules_backup/analyze_pairs.py`
- `modules/module_d_auxiliary_tools/core_legacy/legacy_modules_backup/modules/vtrac_reference.py`
- `modules/module_d_auxiliary_tools/core_legacy/legacy_modules_backup/parse_excel.py`
- `modules/module_d_auxiliary_tools/core_legacy/legacy_modules_backup/vtrac_generator.py`

(Keep the entire `legacy_modules_backup` directory intact; the staged package expects both the root files and the `modules/` subpackage.)

## Why They Matter
- `modules.vtrac_reference` (legacy) exposes `VTRAC_DISPLAY`, `BOXED_VTRAC_REFERENCE`, and `BOXED_LABEL_LOOKUP`, which drive the boxed V-TRAC grid and pair analysis in Aux.
- `analyze_pairs.py` contains the overdue calculations and doubles tracker used by both Aux and the refactored helpers.
- `parse_excel.py` and `vtrac_generator.py` support the one-time draw extraction fallback if CSVs are missing.

If these files are moved or archived, update `modules/module_d_auxiliary_tools/refactored/bootstrap_imports.py` to point to the new location and re-run the Aux smoke script (`scripts/checks/smoke_aux_vtrac.py`).
