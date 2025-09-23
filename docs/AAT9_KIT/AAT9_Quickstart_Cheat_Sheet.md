# AAT9 - Quickstart Cheat Sheet

## Preflight (before launch)
- Command: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Confirms:
  - CWD is repo root
  - Python path
  - Import sources for `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
  - `data/cleaned/*_draws.csv` inventory and selected state resolution

## Launch the App
- `run_app.bat` (runs `streamlit run src\app.py` from repo root)
- Dev tip: keep the in-app "System Health" expander available to debug path drift.

## Data Sources by Page
- Aux / Blackapple: `data/cleaned/*_draws.csv` (draws-only)
- Variant support: Combined / Midday / Evening. Use `modules.aux_loaders.load_state_draws(state, variant)`; Control Center and the Aux page surface all available variants.
- V-TRAC / Stable / Digit Reduction: combined tables via `utils.path_handler` under `tables/` or `data/outputs/tables/<STATE>/`

## Combined Tables Pipeline (if needed)
1) `generate_tables_pipeline.bat`
2) Verify: `tables/<STATE>/` exists (or `data/outputs/tables/<STATE>/`)

## Common Checks
- If a page shows "missing data": ensure the expected directory exists (per above contracts).
- If BA shows import issues: verify `modules/blackapple.py` path in System Health.
- If Aux state draws empty: verify `data/cleaned/<State>_draws.csv` (preflight lists inventory).

## Useful Paths & Helpers
- `utils.path_handler` - canonical path helpers for outputs/analysis/tables
- `modules.aux_loaders.load_state_draws(state)` - robust draws CSV resolver
- `alpha_analytical/stable` - YAML-weighted stable extractor (`feature_config.yml`)



## Stable Pattern extras
- After running the Stable page you should see the HTML/CSV under `data/outputs/analysis/patterns/<STATE>/`.
- A new winners field accepts comma-separated 3-digit numbers; when supplied, the run produces `<STATE>_winner_family_spotlight_raw.csv` and `<STATE>_winner_family_spotlight_families.csv` alongside `<STATE>_stable_patterns_families.csv`.
- Use Dev Health (Stable) to confirm the engine path, YAML path, and the generated file locations.
## Dev Health (fast UI checks)
- Control Center: toggle Dev Health to see key module bindings (path_handler, vtrac_reference, winner_report_full, blackapple, aux_loaders, pipeline_runner) and tables root inventory.
- Winners Full tile: toggle Dev Health to confirm `modules` binding, canonical vtrac_reference path, builder presence, and per-state combined tables existence.
- V-TRAC Analyzer + Stable pages: Dev Health shows module bindings and tables roots for their flows.

## Optional: Codex model preset
- If your Codex client supports model presets, choose `gpt-5-codex` and set reasoning to High for complex tasks (wiring, refactors) or Medium for general work.
- Otherwise, use `gpt-5 high` with dynamic thinking enabled.


## Default model preset (Pro)
- Select gpt-5-codex (High) after launch; switch to Medium only when you need lower latency.
- If Aux shows legacy import errors, run `python scripts/checks/smoke_aux_vtrac.py` and confirm the files listed in `docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md` are present.

