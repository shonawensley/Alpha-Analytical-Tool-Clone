# AAT9 - Quickstart Cheat Sheet

## Preflight (before launch)
- Command: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Confirms:
  - CWD is repo root
  - Python path
  - Import sources for `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
  - Draw inventory lines for `data/cleaned/draws` (should be non-zero) and selected state resolution

## Launch the App
- `run_app.bat` (runs `streamlit run src\app.py` from repo root)
- Dev tip: keep the in-app "System Health" expander available to debug path drift.

## Data Sources by Page
- Aux / Blackapple: `data/cleaned/draws/*_draws.csv` (draws-only; Combined/Midday/Evening all live here)
- Variant support: Combined / Midday / Evening. Use `modules.aux_loaders.load_state_draws(state, variant)`; Control Center and the Aux page surface all available variants.
- V-TRAC / Stable / Digit Reduction: combined tables via `utils.path_handler` under `tables/` or `data/outputs/tables/<STATE>/`

**Policy:** Combined is the **baseline** dataset. Midday/Evening are **additive** variants that never replace Combined.
**Contracts:** Aux/Blackapple read only `data/cleaned/*_draws.csv` (newest-first strings). V-TRAC / Stable / Digit Reduction read combined tables from `tables/<STATE>/` (or `data/outputs/tables/<STATE>/`) via `utils.path_handler`.


## Combined Tables Pipeline (if needed)
1) `generate_tables_pipeline.bat`
2) Verify: `tables/<STATE>/` exists (or `data/outputs/tables/<STATE>/`)

### Swapping Pick3StatsC4 workbooks (critical when running historical dates)
Whenever you copy a dated workbook (e.g., `Pick3StatsC4_2025-06-24.xlsm`) into `data/original/`, you **must** regenerate the tables before running Stable/V-TRAC:

1. Select the workbook  
   `python3 scripts/tools/select_pick3_history.py --file Pick3StatsC4_2025-06-24.xlsm`
2. Rebuild draws + tables for all states (mirrors the Control Center batch)  
   ```bash
   python3 - <<'PY'
   from src.core.pipeline_runner import run_pipeline_from_original_path
   from utils import path_handler as ph
   run_pipeline_from_original_path(ph.get_excel_path())
   PY
   ```
3. Sanity-check the tables: open `data/outputs/tables/Connecticut4/Combined_Combined.csv`, grab `Set1/Draw1/RowType=draw_data`, and confirm the last two columns match the previous day’s Midday/Evening draws recorded in `data/results/results_checkCT.txt`. This confirms the tables truly came from the intended workbook.

Skipping these steps leaves the old tables in place, so every analysis would unknowingly point at the wrong date.

## Common Checks
- If a page shows "missing data": ensure the expected directory exists (per above contracts).
- If BA shows import issues: verify `modules/blackapple.py` path in System Health.
- If Aux state draws empty: verify `data/cleaned/draws/<State>_draws.csv` (preflight lists inventory) and rerun `scripts/tools/validate_aux_all.ps1`.
- After any draws refresh or CSV edit, run `scripts/tools/validate_aux_all.ps1` from repo root; it fails fast if the Aux loaders drift from the canonical directory.
- Commits automatically run the Aux guard (`python scripts/hooks/validate_aux_draws.py`). Only bypass in emergencies via `AAT9_SKIP_AUX_GUARD=1` before `git commit`.

## Useful Paths & Helpers
- `utils.path_handler` - canonical path helpers for outputs/analysis/tables
- `modules.aux_loaders.load_state_draws(state)` - robust draws CSV resolver
- `alpha_analytical/stable` - YAML-weighted stable extractor (`feature_config.yml`)

\n\n## Control Center Batch Workflow\n- Paste the Pick3StatsC4 winners list into the Control Center batch expander.\n- Use the toggles to run the winners logger, Stable Pattern extractor (with optional bundle), and the Digit Reduction pipeline (reducer refresh, Analyzer V2 overlays, optional Digit Reduction bundle).\n- Set the bundle stamp before enabling Stable or Digit Reduction bundle options so artifacts land under the desired `data/outputs/analysis/.../<STAMP>/` folder.\n- Ensure combined tables exist for every tracked state you refresh; the expander writes Digit Reduction outputs under `data/outputs/analysis/digit_reduction/<STATE>/`.
- Digit Reduction training bundles copy Midday + Evening winner artifacts by default (10 files). Use the `include_combined` flag/checkbox when you need the Combined artifacts as well.\n\n## Auxiliary Tools Highlights
- Positional Pressure (Aux page) renders Combined/Midday/Evening side-by-side (P1/P2/P3 columns, top-3 digits) with a fixed 360-draw window and Top-3 ranks; hard-due cells are highlighted in red.
- Consensus, mirror, and double-pressure tags appear beside each position along with a ranked positional shortlist.
- Control Center adds a positional heat badge per state/variant using the same draws-only engine.

## Stable Pattern extras
- After running the Stable page you should see the HTML/CSV under `data/outputs/analysis/patterns/<STATE>/`.
- A new winners field accepts comma-separated 3-digit numbers; when supplied, the run produces `<STATE>_winner_family_spotlight_raw.csv` and `<STATE>_winner_family_spotlight_families.csv` alongside `<STATE>_stable_patterns_families.csv`.
- Use Dev Health (Stable) to confirm the engine path, YAML path, and the generated file locations.
- Batch runs write `<STATE>_metrics.json` (stable evidence schema) and manifest entries so Control Center can display per-state metrics and download links after successful runs.
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


