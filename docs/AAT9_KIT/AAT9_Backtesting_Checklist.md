# AAT9 — Backtesting Checklist

Use this loop whenever you run historical validations so every tool (Stable, Digit Reduction, V‑TRAC, Aux, Hot Zones) reads the correct tables and results.

## 1. Activate the workbook

```bash
python scripts/tools/select_pick3_history.py --file Pick3StatsC4_YYYY-MM-DD.xlsm
```

This copies the dated workbook into `data/original/Pick3StatsC4.xlsm`.

## 2. Rebuild tables with guard

```bash
python scripts/tools/run_tables_with_guard.py
```

- The guard compares the workbook path/mtime against `data/outputs/tables/tables_manifest.json`.
- If the workbook is unchanged, it skips work; otherwise it purges the per-state tables and regenerates them.
- After each successful rebuild the manifest records the workbook identity and per-state checksums.

## 3. Spot-check Set1/Draw1 vs results

For a canonical state (e.g., `Connecticut4`):

1. Open `data/outputs/tables/Connecticut4/Combined_Combined.csv`.
2. Locate the `Set1,Draw1,RowType=draw_data` row (the most recent draws).
3. Confirm the last two columns match the previous day's Midday/Evening numbers in `data/results/results_checkCT.txt` (or the date-specific results file you are targeting).

If they do not match, stop and rerun the pipeline—the tables are stale.

## 4. Run analyzers + batches

After the tables pass the check:

1. Run Stable Pattern, Digit Reduction, V‑TRAC, Aux/Blackapple, and any batch winners logging for the paired results file (`data/results/YYYY-MM-DD.txt`).
2. Use a consistent bundle stamp so per-tool outputs land under `data/outputs/analysis/<tool>/<STATE>/<STAMP>/`.
3. Generate sharepacks / winners map as needed.

## 5. Log the run

Record (in your task log or `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`):

- Workbook filename / date.
- Results file consumed.
- Commands executed (especially table guard + analyzers).
- Bundle stamp / output folders.

This keeps historical analyses reproducible and makes it obvious which workbook produced a given set of artifacts.
