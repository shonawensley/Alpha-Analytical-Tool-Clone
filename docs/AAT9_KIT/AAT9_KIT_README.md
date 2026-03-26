# AAT9 - KIT (Curated, Up-To-Date) Documentation

Purpose: A single, current source for AAT9 usage, structure, workflow, and update practices. Use this KIT first; older documents remain in `docs/AAT9_DOCS` for history.

## Contents
- AAT9_Onboarding_Compass.md - start here for session flow, doc order, and validation checklist
- AAT9_Workflow_Standard.md - step-by-step workflow and required doc updates
- AAT9_Task_Template.md - copy-paste template for new tasks
- AAT9_Quickstart_Cheat_Sheet.md - preflight, launch, data checks, common CLI
- AAT9_AI_Contributor_Guide.md - how to build safely, add tools, and update docs
- AAT9_Unified_Changelog.md - rolling log of meaningful changes
- AAT9_Preflight_Reference.md - expected outputs and quick triage
- AAT9_Diagrams_Guide.md - Mermaid usage and update workflow
- AAT9_Digit_Reduction_Training_Exports.md - stacked view plus training CSV/JSON
- AAT9_Winners_VTrac_Report.md - per-winner V-Trac index panels (training export)
- AAT9_Stable_Analysis_Log.md - reverse-engineered Stable runs + insights/follow-ups
- Canonical architecture and flow (referenced)
  - docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md
  - docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md

## Analysis Arena Current Path

When the task is about the rebuilt Analysis Arena branch or fresh-run Final Validation, use these as the current-path references:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PORTAL.md`

Treat `docs/AAT9_KIT/FINAL VALIDATION/RUNS/` as the historical/control-arm comparison layer unless a doc explicitly says otherwise.

## Canonical Setup (Quick)
- Launch: `run_app.bat` -> `streamlit run src\app.py` (from repo root)
- Imports resolve to in-repo files:
  - `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
- Data contracts:
  - Aux or Blackapple -> `data/cleaned/*_draws.csv`
  - V-TRAC / Stable / Digit Reduction -> combined tables under `tables/` or `data/outputs/tables/<STATE>/` via `utils.path_handler`
- Preflight: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

## Dev Health Cheat Sheet (fast diagnostics)
- Control Center: shows bindings for `utils.path_handler`, `modules.vtrac_reference`, `modules.winner_report_full`, `modules.blackapple`, `modules.aux_loaders`, `core.pipeline_runner`, and tables root inventory.
- Winners Full tile: shows actual `modules` binding, `modules.vtrac_reference` path, builder presence, and per-state combined tables existence.
- V-TRAC Analyzer and Stable pages: show module bindings and tables roots for their flows.

Tip: use these before running pipelines or generating reports to confirm environment, imports, and data availability.
