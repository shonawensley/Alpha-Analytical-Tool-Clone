# AAT9 — App Flow Addendum (2025-09-06)

This addendum clarifies the canonical launch path, import sources, and data contracts to align existing App Flow docs with the current integrated app.

## Canonical Setup
- Launch: `run_app.bat` → `streamlit run src\app.py` (from repo root)
- Imports resolve to in-repo files:
  - `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
- Data contracts:
  - Aux/Blackapple → `data/cleaned/*_draws.csv`
  - V‑TRAC / Stable / Digit Reduction → combined tables under `tables/` or `data/outputs/tables/<STATE>/` via `utils.path_handler`
- Preflight (recommended): `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

## Directory Quick Reference
See `AAT9_Architecture_Dir_Layout_2025-09-06.md` for the canonical tree, diagrams, and guardrails.

## Notes on Legacy References
- Older references to `scripts/streamlit_app_with_analyzer.py` and stand‑alone streamlit entries are deprecated; use `run_app.bat`.
- Legacy runners and entrypoints were archived under `archived/2025-09-06/` with `ARCHIVE_MANIFEST.md`.
