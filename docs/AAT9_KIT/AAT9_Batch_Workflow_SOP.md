# AAT9 — Control Center Batch Workflow SOP

This captures the “swap workbook → regenerate inputs → run batches → collect outputs” loop so every session follows the same playbook without guesswork.

## 0. Swap workbook & regenerate tables/draws

1. Pick the history file you want to analyze (e.g., `Pick3StatsC4_2025-06-24.xlsm`).
2. Activate it and rebuild tables/JSON with the guard:
   ```bash
   python scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_2025-06-24.xlsm
   ```
   - This purges per-state CSVs under `data/outputs/tables/<STATE>/`, rebuilds them, emits JSON mirrors under `data/outputs/json_tables/`, and rewrites `data/outputs/tables/tables_manifest.json`.
3. Spot-check `data/outputs/tables/Connecticut4/Combined_Combined.csv` (Set1/Draw1/RowType=draw_data) against `data/results/results_checkCT.txt` to confirm the tables came from the intended workbook.
4. (Optional) Run `.codex/preflight.ps1 -CheckTables -State "<STATE>"` to display the manifest info before proceeding.

Draws for Aux/Blackapple are regenerated via the Control Center “Aux Draws Pipeline” expander when needed; it mirrors the same “pushd → regenerate” behavior.

## 1. Prepare results input

- For the workbook dated `YYYY-MM-DD`, use the next day’s results file (`data/results/YYYY-MM-DD+1.txt`) as the target when reverse-engineering winners.
- Keep a single source list (e.g., the winners sheet pasted into Control Center, or the `data/results/*.txt` files) so every tool is evaluating the same draws.

## 2. Run Control Center batches

Inside the Control Center app (or using the equivalent CLI scripts), follow this pattern:

1. **Paste winners** into the batch expander.
2. Toggle the tools you want to run:
   - Winners logger (V-TRAC analyzer-style HTML).
   - Stable Pattern extractor (optionally with training bundle + winners spotlight).
   - Digit Reduction pipeline (reducers + Analyzer V2 overlays, bundle toggle).
   - Aux draw refresh or other Aux features if the workbook brought new draws.
3. Provide/verify the bundle stamp so artifacts land under `data/outputs/analysis/<tool>/<STATE>/<STAMP>/`.
4. Run the batch; Control Center writes all lean outputs + winners logs in one pass.

Equivalent CLI commands (for headless operation):

- Stable rerun per state: `python scripts/tools/run_stable_from_results.py --state <STATE> --results-file data/results/2025-06-24.txt`
- Winners HTML regeneration: `python scripts/tools/generate_winners_from_results.py --results-file data/results/2025-06-24.txt --out-dir reports/stable/winners_by_date/2025-06-24/`
- V-TRAC enhanced analyzer + validator + compact reports: `python TOOLS/run_vtrac_share_bundle.py`
- Hot Zones brain bundle (JSON mirror required): `python scripts/hot_zones/run_hot_zones_cli.py --state <STATE> --date 2025-06-24`

## 3. Collect lean outputs (per tool)

Refer to `docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md` for canonical artifact lists:

- **Digit Reduction**: `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/{per_item,top_candidates,meta}.csv/json` (plus optional stacked HTML/training sets).
- **Stable Pattern**: `data/outputs/analysis/patterns/<STATE>/{stable_patterns_scores.csv, stable_patterns_families.csv, stable_patterns_compound.csv, metrics.json, winner_family_spotlight_*.csv}`.
- **V-TRAC**: `data/outputs/analysis/vtrac/<STATE>/...` for analyzer bundles, and `data/outputs/analysis/vtrac_validation/` for compact reports / share bundles.
- **Winners logger**: `reports/stable/winners_by_date/YYYY-MM-DD/<STATE>/...html` (analyzer-style) plus the Control Center compact index panel.
- **Aux**: draws CSVs under `data/cleaned/draws/`, positional CSV/HTML in their respective analysis folders.

Every tool’s outputs live under `data/outputs/analysis/<tool>/<STATE>/…`, making it easy for the Aggregator to ingest them later.

## 4. Logging & validation

After each batch:

- Update `docs/AAT9_KIT/AAT9_Checkpoint_Log.md` (or your task log) with the workbook date, results file, commands run, bundle stamp, and any anomalies.
- Optional smoke validations:
  - `python scripts/checks/validate_stable_schema.py`
  - `python scripts/checks/smoke_aux_vtrac.py`
  - `python scripts/checks/smoke_project_loader.py`
  - `python TOOLS/run_vtrac_share_bundle.py` (already run above) to ensure compact reports refresh cleanly.

## 5. How this maps to the future “aggregated” flow

The Control Center batch mimics the final production workflow:

- Inputs: one Excel workbook (tables) + one results file (targets).
- Tools: each analyzer runs, writes its lean bundle, and optionally produces winners artifacts.
- Outputs: all data lands in tool-specific folders under `data/outputs/analysis/…`, ready for the upcoming Aggregator to read and score in one pass.

By following this SOP, you can run historical validations, capture share bundles, and build Hot Zones or Aggregator logic without re-inventing the process every session.
