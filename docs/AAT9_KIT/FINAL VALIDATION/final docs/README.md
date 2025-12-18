# Final Validation — “Final Docs” Portal (SSOT)

This folder is the **one place to start** for the Final Validation workflow.

## Core docs (keep in sync)
- Master template (questions only): `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- Workflow changelog (“fix later” capture): `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
- Control Center / Brain 2 reference (keep for later): `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPC.md`

## Run reports (filled answers live here)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

Generate a run report scaffold:
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

## Operational guides
- Entry (contracts + semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- Preflight / drift guards: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Preflight.md`
- Workflow architecture map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`

## Key references
- Lean outputs index: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- VTRAC permutations + VSTRAIGHTS reference: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
