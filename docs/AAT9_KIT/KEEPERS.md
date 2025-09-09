# AAT9 — KEEPERS (Canonical Choices)

Use these as the single sources of truth to avoid drift.

- Launch: `run_app.bat` → `streamlit run src\app.py` (repo root)
- Path helper: `utils/path_handler.py` (SSOT); do not import from `src/utils`.
- Data contracts:
  - Aux/BA inputs: `data/cleaned/*_draws.csv` only
  - String‑table pipeline: `data/original/Pick3StatsC4.xlsm` → `data/cleaned/<State>_cleaned.xlsx` → `data/outputs/tables/<STATE>/`
- Combined tables consumer pages: Stable, Digit Reduction, V‑TRAC
- BA isolation: absolute‑path loader (do not let `modules` name collisions shadow project code)
- Preflight: `.codex/preflight.ps1` (with optional `-CheckTables`)
- App docs: AAT9 KIT is the living source; older docs are reference only
 - Imports SSOT: App enforces top‑level `utils` binding at entry to prevent `/src/utils` shadowing
