# AAT9 — Live Wiring & Data Paths

Purpose: Map each page to its engines/modules and the exact input/output directories.

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
  - Outputs: `data/outputs/analysis/digit_reduction/<STATE>/`

- Auxiliary Tools (working parity logic)
  - Engines: staged/working `modules.analyze_pairs`, `modules.vtrac_reference`; sums optional under `modules/module_d_auxiliary_tools/refactored`
  - Inputs: `data/cleaned/*_draws.csv` (draws‑only; newest‑first)
  - Outputs: rendered in‑page (tables/captions); no writes to code folders

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

## Winners Logger (V‑Trac Winner Report)
- Entry: Control Center → “Winners Logger (V‑Trac winner report)”
- Inputs: State (single), winning number (3 digits)
- Behavior: renders index panels (Midday/Evening/Combined) using V‑Trac mapping
  - Purple: stable‑pattern combos for the winner’s index
  - Green: straight permutations of the winner (order‑specific)
- Outputs: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Notes: table‑agnostic (does not require state tables); safe to use for states still missing string‑tables

## Inventories & Preflight
- Draws (Aux/BA): `data/cleaned/*_draws.csv` (preflight lists inventory)
- Cleaned Excel: `data/cleaned/*_cleaned.xlsx` (preflight lists inventory)
- Combined tables: `data/outputs/tables/<STATE>/` (preflight `-CheckTables` validates root and a state dir)

## Canonical Helpers
- Path SSOT: `utils/path_handler.py` (do not import from `src/utils`)
- BA/Aux: `modules/blackapple.py`, `modules/aux_loaders.py`
- Stable: `alpha_analytical/stable/{__init__.py, feature_config.yml}`

## Winners Logger (Analyzer-style Full Report)
- Entry: Control Center + “Winners Logger (Analyzer-style full report)”
- Inputs (read-only): `data/outputs/tables/<STATE>/<STATE>_{Midday,Evening,Combined}_combined.csv`
- Logic: compute index via `modules.vtrac_reference.get_vtrac_index(winner)`; purple coverage via `get_index_set(index)`; green overlay via `get_index_straights(winner)`; render analyzer-style 3 panes
- Outputs (HTML): `data/outputs/analysis/winners/<STATE>/<STATE>_<Draw>_<YYYY-MM-DD>_winner_<NNN>_analyzer.html`
- Notes: compact Winners tile remains as fallback when tables are missing

- Legacy dependency: Aux loads boxed VTRAC data via the staged package listed in docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md.
