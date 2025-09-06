# AAT9 — KIT (Curated, Up‑To‑Date) Documentation

Purpose: A single, current source for AAT9 usage, structure, workflow, and update practices. Use this KIT first; older documents remain in `docs/AAT9_DOCS` for history.

## Contents\\n- AAT9_Workflow_Standard.md � The step-by-step workflow and required doc updates\\n- AAT9_Task_Template.md � Copy-paste template for new tasks
- AAT9_Quickstart_Cheat_Sheet.md — Preflight → launch → data checks → common CLI
- AAT9_AI_Contributor_Guide.md — How to build safely, add tools, and update docs
- AAT9_Unified_Changelog.md — Rolling log of meaningful changes
- AAT9_Preflight_Reference.md — Expected outputs and quick triage
- AAT9_Diagrams_Guide.md — Mermaid usage and update workflow
- Canonical Architecture & Flow (referenced)
  - docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md
  - docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md

## Canonical Setup (Quick)
- Launch: `run_app.bat` → `streamlit run src\app.py` (from repo root)
- Imports resolve to in‑repo files:
  - `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
- Data contracts:
  - Aux/Blackapple → `data/cleaned/*_draws.csv`
  - V‑TRAC / Stable / Digit Reduction → combined tables under `tables/` or `data/outputs/tables/<STATE>/` via `utils.path_handler`
- Preflight: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

