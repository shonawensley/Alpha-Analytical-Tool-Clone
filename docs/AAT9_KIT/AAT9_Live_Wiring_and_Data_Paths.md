# AAT9 — Live Wiring & Data Paths

Purpose: Map each page to its engines/modules and the exact input/output directories.

**Dataset interpretation:** Combined is the baseline dataset; Midday/Evening are additive variants surfaced alongside Combined. Aux/Blackapple read `data/cleaned/*_draws.csv` (draws-only). V-TRAC / Stable / Digit Reduction read combined tables under `tables/<STATE>/` (or `data/outputs/tables/<STATE>/`) via `utils.path_handler`.


## Pages → Engines → Inputs/Outputs
- V‑TRAC Analyzer
  - Engine: `core/module_c_vtrac.py` (internal helpers under `src/utils/*` as needed)
  - Inputs: combined tables under `data/outputs/tables/<STATE>/`
  - Outputs: optional analysis under `data/outputs/analysis/vtrac/<STATE>/` (when applicable)

- Stable Pattern Extractor
  - Engine: `src/core/stable_pattern_extractor.py` → `alpha_analytical/stable` (post-pass families + spotlight helpers)
  - Inputs: combined tables under `data/outputs/tables/<STATE>/`
  - Outputs: `data/outputs/analysis/patterns/<STATE>/`
    - Always writes `<STATE>_stable_patterns_scores.csv` + HTML report
    - Emits `<STATE>_stable_patterns_families.csv` via post-pass aggregation
    - Winners text box (optional) adds `<STATE>_winner_family_spotlight_{raw,families}.csv`
  - Dev Health: confirms engine/YAML paths and displays new file paths after a run

- Digit Reduction
  - Engine: `src/core/module_b_digit_reduction.py`
  - Inputs: combined tables under `data/outputs/tables/<STATE>/`
  - Outputs:
    - Reducer: `data/outputs/analysis/digit_reduction/<STATE>/` (tabbed + stacked HTML, summary CSV, training steps CSV).
    - Analyzer V2: `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/` (lean bundle — `per_item.csv`, `top_candidates.csv`, `meta.json`, stacked HTML per variant; diagnostics: `_steps.csv` when enabled).
    - Training bundles: `data/outputs/analysis/digit_reduction/<STATE>/training_sets/<STAMP>/` (copies the lean bundle + steps when enabled; no winners by default).
    - Winners map/flags/HTML are generated centrally via the Control Center batch and stored under the shared winners directory (see Control Center section).

- Auxiliary Tools (working parity logic)
    - Engines: staged/working `modules.analyze_pairs`, `modules.vtrac_reference`; positional pressure via `modules/module_d_auxiliary_tools/refactored/positional_tool.py`; sums optional under `modules/module_d_auxiliary_tools/refactored`
  - Inputs: `data/cleaned/*_draws.csv` (draws‑only; newest‑first)
    - Outputs: rendered in-page (tables/captions) plus positional shortlist/heat badges; no writes to code folders

- Control Center (cross‑state doubles + BA summary)
  - Logic: scans `data/cleaned/*_draws.csv` to build a doubles table; renders BA summary across states
  - Optional: “Tables Pipeline” panel to regenerate combined tables from Excel

## String‑Table Pipeline (from Excel)
- Source Excel: `data/original/Pick3StatsC4.xlsm`
- Cleaned Excel sheets: `data/cleaned/<State>_cleaned.xlsx`
- Combined tables: `data/outputs/tables/<STATE>/` (Midday/Evening/Combined CSVs)
  - Filenames: `Midday_Combined.csv`, `Evening_Combined.csv`, `Combined_Combined.csv`
- Runner: `src/core/pipeline_runner.py` (pure functions)
  - App entry: Control Center → “Tables Pipeline (optional)”
  - CLI (optional): can be wired via a small script in `scripts/pipeline/`

## Winners Logger (V-Trac Winner Report)
- Entry: Control Center -> "Winners Logger (V-Trac winner report)"
- Inputs: State (single), winning number (3 digits)
- Behavior: renders index panels (Midday/Evening/Combined) using V-Trac mapping with green / blue / purple overlays.
  - Green: winner permutations (strict + gap-1).
  - Blue: V-Trac straights (AABB/BBAA) including value-block runs.
  - Purple: index-family combos aligned to the winner's index.
- Outputs: data/outputs/winners/<YYYY-MM-DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html
- UI: Control Center surfaces an 'Open report (HTML)' download button (no Streamlit /pages routing).
- Notes: table-agnostic (does not require state tables); safe for states still missing string-tables.

## Inventories & Preflight
- Draws (Aux/BA): `data/cleaned/*_draws.csv` (preflight lists inventory)
- Cleaned Excel: `data/cleaned/*_cleaned.xlsx` (preflight lists inventory)
- Combined tables: `data/outputs/tables/<STATE>/` (preflight `-CheckTables` validates root and a state dir)

## Canonical Helpers
- Path SSOT: `utils/path_handler.py` (do not import from `src/utils`)
- BA/Aux: `modules/blackapple.py`, `modules/aux_loaders.py`
- Stable: `alpha_analytical/stable/{__init__.py, feature_config.yml}`

## Winners Logger (Analyzer-style Full Report)
- Entry: Control Center -> "Winners Logger (Analyzer-style full report)"
- Inputs (read-only): data/outputs/tables/<STATE>/<STATE>_{Midday,Evening,Combined}_combined.csv
- Logic: compute index via modules.vtrac_reference.get_vtrac_index(winner); apply green (winner), blue (VT-straight), purple (family) overlays via modules.vtrac_matchers.collect_spans; render analyzer-style 3 panes.
- Outputs (HTML): data/outputs/analysis/winners/<STATE>/<STATE>_<Draw>_<YYYY-MM-DD>_winner_<NNN>_analyzer.html
- UI: download button mirrors the compact tile (no /pages routing).
- Notes: compact Winners tile remains as fallback when tables are missing.


- Legacy dependency: Aux loads boxed VTRAC data via the staged package listed in docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md.
