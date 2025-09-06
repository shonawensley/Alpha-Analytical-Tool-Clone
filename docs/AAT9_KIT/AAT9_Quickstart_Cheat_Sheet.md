# AAT9 — Quickstart Cheat Sheet

## Preflight (before launch)
- Command: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Confirms:
  - CWD is repo root
  - Python path
  - Import sources for `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
  - `data/cleaned/*_draws.csv` inventory and selected state resolution

## Launch the App
- `run_app.bat` (runs `streamlit run src\app.py` from repo root)
- Dev tip: keep the in‑app “System Health” expander available to debug path drift.

## Data Sources by Page
- Aux / Blackapple: `data/cleaned/*_draws.csv` (draws‑only)
- V‑TRAC / Stable / Digit Reduction: combined tables via `utils.path_handler` under `tables/` or `data/outputs/tables/<STATE>/`

## Combined Tables Pipeline (if needed)
1) `generate_tables_pipeline.bat`
2) Verify: `tables/<STATE>/` exists (or `data/outputs/tables/<STATE>/`)

## Common Checks
- If a page shows "missing data": ensure the expected directory exists (per above contracts).
- If BA shows import issues: verify `modules/blackapple.py` path in System Health.
- If Aux state draws empty: verify `data/cleaned/<State>_draws.csv` (preflight lists inventory).

## Useful Paths & Helpers
- `utils.path_handler` — canonical path helpers for outputs/analysis/tables
- `modules.aux_loaders.load_state_draws(state)` — robust draws CSV resolver
- `alpha_analytical/stable` — YAML‑weighted stable extractor (`feature_config.yml`)

