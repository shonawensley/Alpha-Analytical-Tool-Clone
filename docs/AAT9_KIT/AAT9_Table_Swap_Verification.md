# AAT9 Table Swap Verification

This note captures a repeatable checklist for proving that a new Pick3StatsC4
workbook has been activated, tables regenerated, and the matching winners HTML
was produced. Use it whenever you swap Excel history files so future sessions
can audit the guardrails without re-deriving the commands.

## Core Workflow

1. **Activate + rebuild tables**  
   ```
   PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py \
       --history-file Pick3StatsC4_YYYY-MM-DD.xlsm
   ```
   The helper copies `data/history/<file>` into `data/original/Pick3StatsC4.xlsm`
   and runs the full cleaning/extraction/table build, including JSON mirrors and
   the guard manifest.

2. **Confirm the workbook + guard columns**  
   - Inspect `data/outputs/tables/tables_manifest.json` to verify the new
     `workbook.path`, `mtime`, and `size`.  
   - Spot-check `data/outputs/tables/<STATE>/Combined_Combined.csv` for
     `Set1/Draw1/RowType=draw_data` so column `1` (newest draw) and column `2`
     match the expected Set1 guard check (e.g., Connecticut’s `col1` should be
     the latest draw inside the workbook, and `col2` the prior draw).
   - Optional: hash the CSV to prove it changed per workbook.

3. **Generate winners HTML using the “day-after” results file**  
   ```
   PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py \
       --results-file data/results/<YYYY-MM-DD>.txt \
       --out-dir reports/stable/winners_by_date/<YYYY-MM-DD>/
   ```
   The `<YYYY-MM-DD>` here is the results day you are validating (one day after
   the workbook date). The script renders the V‑TRAC HTML under
   `reports/stable/winners_by_date/<DATE>/<STATE>/`.

4. **(Optional) Hot Zones / batch work**  
   Once the tables+results pairing is verified you can safely run the Hot Zones
   CLI or any batch scripts for that environment knowing both the Set1 guard
   manifest and winners HTML are in sync.

## Recent Verification Runs

| Run | History Workbook | Results File | CT Set1 col1 / col2 | FL Set1 col1 / col2 | CT Combined_Combined md5 | Winners Directory |
| --- | ---------------- | ------------ | ------------------- | ------------------- | ------------------------ | ----------------- |
| A | `Pick3StatsC4_2025-06-23.xlsm` | `data/results/2025-06-24.txt` | `938 / 130` | `465 / 665` | `b763f8449d79` | `reports/stable/winners_by_date/2025-06-24/` |
| B | `Pick3StatsC4_2025-06-24.xlsm` | `data/results/2025-06-25.txt` | `858 / 494` | `271 / 733` | `50ade8200cec` | `reports/stable/winners_by_date/2025-06-25/` |
| C | `Pick3StatsC4_2025_06_26.xlsm` | `data/results/2025-06-27.txt` | `612 / 928` | `337 / 100` | `d25b3dff3cf6` | `reports/stable/winners_by_date/2025-06-27/` |

Each line above was produced by:

1. Running `run_tables_with_guard.py` for the stated history file.
2. Reading `data/outputs/tables/Connecticut4/Combined_Combined.csv` and
   `.../Florida4/Combined_Combined.csv` to log the Set1 guard columns.
3. Hashing Connecticut’s Combined table via `md5sum` to capture a fingerprint.
4. Running `generate_winners_from_results.py` for the results date (always
   one day ahead of the workbook) and verifying the per-state HTML exists under
   the winners directory shown.

To audit a run, pick the corresponding row, open the Combined table to confirm
the Set1 values, and visit the winners directory to load the HTML (which shows
the Set1/Draw1 guard draws in context). If the manifest/workbook details or
Set1 digits differ from expectation, rebuild the tables before proceeding with
any validation or batch work.
