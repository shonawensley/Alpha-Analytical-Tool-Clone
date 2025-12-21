# AAT9 Master Validation Preflight (Pipeline + Batch)

Use this as a quick-start for new sessions before running any validation/batch
work. The goal is to guarantee the correct history workbook is active, tables +
JSON are rebuilt, and winners/batch outputs come from the intended day-ahead
results file.

## One-shot command (recommended)

Run the wrapper to enforce the day-ahead rule and basic checks for CT/FL:

```bash
PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-date YYYY-MM-DD --regen-aux-draws
# or
PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm --regen-aux-draws
```

Notes:
- `--history-date` accepts a date and will auto-detect `data/history/Pick3StatsC4_YYYY-MM-DD.xlsm` or `data/history/Pick3StatsC4_YYYY_MM_DD.xlsm` when present.
- If you pass `--history-file`, use the exact filename under `data/history/` (either hyphen or underscore naming).

This will:
- Activate `data/history/Pick3StatsC4_YYYY-MM-DD.xlsm` into `data/original/Pick3StatsC4.xlsm`.
- Rebuild tables + JSON (via `run_tables_with_guard.py`).
- Regenerate Aux draw CSVs for sentinel states (CT/FL) from the activated workbook (avoids Aux/table drift).
- Validate that CT/FL tables and Aux draws describe the same newest draws (guards against stale Aux draw CSVs).
- Generate winners using `data/results/(YYYY-MM-DD + 1).txt` into `reports/stable/winners_by_date/<RESULTS_DATE>/`.
- Validate that CT/FL winners HTML exists for the expected triads and that the Set1/Draw1 sequence from the Combined tables appears inside the HTML (guards against stale tables).
- Write a summary JSON to `reports/stable/validation_logs/validation_<RESULTS_DATE>.json`.

## Manual checklist (if you need to do it step-by-step)

1) Activate history workbook and rebuild tables/JSON  
```
PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm
```
- Confirm `data/outputs/tables/tables_manifest.json` points to the correct history workbook (path/mtime/size).
- Verify per-state tables and JSON exist under:
  - `data/outputs/tables/<STATE>/Combined_Combined.csv`
  - `data/outputs/json_tables/<STATE>_tables.json`
- Optional quick check: read CT/FL Set1/Draw1 row in the Combined CSV to see col1/col2 digits.

1b) Regenerate Aux draw CSVs (CT/FL) and validate alignment (recommended)
```
python3 scripts/auxiliary/generate_draws_csv.py --states Connecticut Florida --max-draws 1000
python3 scripts/tools/validate_tables_aux_alignment.py --state Connecticut4
python3 scripts/tools/validate_tables_aux_alignment.py --state Florida4
```

2) Generate winners for the day-ahead results (history date + 1)  
```
PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py \
  --results-file data/results/<RESULTS_DATE>.txt \
  --out-dir reports/stable/winners_by_date/<RESULTS_DATE>/
```

3) Verify winners vs results  
- Parse `data/results/<RESULTS_DATE>.txt` and ensure the CT/FL triads (Midday/Evening) have matching `_winner_<TRIAD>_` HTML files under `reports/stable/winners_by_date/<RESULTS_DATE>/<STATE>/`.

4) Verify winners vs tables (no stale tables)  
- Open `data/outputs/tables/Connecticut4/Combined_Combined.csv` and `.../Florida4/...` and note the Set1/Draw1 sequence (columns 7→1).  
- Confirm that sequence appears inside at least one winners HTML file for the state/date. This proves the HTML was generated from the current tables, not an old environment.

## Where to look
- Winners HTML: `reports/stable/winners_by_date/<RESULTS_DATE>/<STATE>/`
- Tables: `data/outputs/tables/<STATE>/Combined_Combined.csv`
- JSON mirrors: `data/outputs/json_tables/<STATE>_tables.json`
- Validation log: `reports/stable/validation_logs/validation_<RESULTS_DATE>.json`
- Full SOP log (per run): `docs/AAT9_KIT/AAT9_String_Table_Testing.md`

## Notes
- The results file is always the day after the history workbook date (history D → results D+1).
- Streamlit cache warnings during CLI runs are per-process; nothing persists across runs.
- For quick manual confidence, pick a run, open the winners directory, verify triads match the official results, and spot-check the Set1 sequence in both the CSV and an HTML file.
