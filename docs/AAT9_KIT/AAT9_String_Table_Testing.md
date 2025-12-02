# AAT9 String Table Testing SOP

Use this log to document each “clean” string-table regeneration run. The goal is
to prove that a specific Pick3StatsC4 workbook was activated, all per-state CSV
tables and JSON mirrors were rebuilt, and the Set1 guard columns match the
intended results day before any batch/analysis work begins.

## Stage 0 – Environment Reset

- `data/outputs/tables/` – empty before Stage 1? ✅ / ☐
- `data/outputs/json_tables/` – empty before Stage 1? ✅ / ☐
- `data/outputs/analysis/` – empty before Stage 1? ✅ / ☐
- `reports/stable/winners_by_date/` – empty before Stage 1? ✅ / ☐
- Notes:

## Stage 1 – Workbook Activation & Table Build

| Run ID | History Workbook | Command | Manifest path | Notes |
| ------ | ---------------- | ------- | ------------- | ----- |
| A | `Pick3StatsC4_2025_06_20.xlsm` | `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_2025_06_20.xlsm` | `data/outputs/tables/tables_manifest.json` | Manifest workbook mtime/size matches the June 20 file; tables already up to date. |
| B | `Pick3StatsC4_2025-06-21.xlsm` | `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_2025-06-21.xlsm` | `data/outputs/tables/tables_manifest.json` | Regenerated tables/JSON for 21 Jun workbook (new checksums logged). |
| C | `Pick3StatsC4_2025-06-22.xlsm` | `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_2025-06-22.xlsm` | `data/outputs/tables/tables_manifest.json` | Regenerated tables/JSON for 22 Jun workbook (new checksums logged). |

For each run:
1. Activate the workbook:  
   `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm`
2. Record the manifest snapshot (`data/outputs/tables/tables_manifest.json`).
3. List the regenerated tables + JSON mirrors (see Stage 2/3 below).

## Stage 2 – CSV Inventory & Guard Columns

| Run ID | State | Combined CSV path | Set1 col1 | Set1 col2 | Matches results? |
| ------ | ----- | ----------------- | --------- | --------- | ---------------- |
| A | Connecticut4 | `data/outputs/tables/Connecticut4/Combined_Combined.csv` | 763 | 913 | Pending (results start at 2025-06-21) |
| A | Florida4 | `data/outputs/tables/Florida4/Combined_Combined.csv` | 927 | 510 | Pending (results start at 2025-06-21) |
| B | Connecticut4 | `data/outputs/tables/Connecticut4/Combined_Combined.csv` | 155 | 950 | Pending (results=2025-06-22 used in Stage 2) |
| B | Florida4 | `data/outputs/tables/Florida4/Combined_Combined.csv` | 120 | 927 | Pending (results=2025-06-22 used in Stage 2) |
| C | Connecticut4 | `data/outputs/tables/Connecticut4/Combined_Combined.csv` | 835 | 281 | Pending (results=2025-06-23 used in Stage 2) |
| C | Florida4 | `data/outputs/tables/Florida4/Combined_Combined.csv` | 924 | 330 | Pending (results=2025-06-23 used in Stage 2) |

Checklist per run:
- `ls data/outputs/tables/` – confirm each state directory exists.
- `head data/outputs/tables/<STATE>/Combined_Combined.csv` (optional spot check).
- Capture Set1/Draw1/RowType=`draw_data` for Connecticut4 & Florida4 (minimum).
- If the corresponding results file exists, compare Set1 col1 with the expected winner and note pass/fail.

## Stage 3 – JSON Inventory

| Run ID | JSON path | Exists? |
| ------ | --------- | ------- |
| A | `data/outputs/json_tables/Connecticut4_tables.json` | ✅ |
| A | `data/outputs/json_tables/Florida4_tables.json` | ✅ |
| B | `data/outputs/json_tables/Connecticut4_tables.json` | ✅ |
| B | `data/outputs/json_tables/Florida4_tables.json` | ✅ |
| C | `data/outputs/json_tables/Connecticut4_tables.json` | ✅ |
| C | `data/outputs/json_tables/Florida4_tables.json` | ✅ |

Checklist per run:
- `ls data/outputs/json_tables/*.json` – confirm each state has a mirror file.
- Optional: open one file to ensure schema matches expectations (`state_name`, `sections`, `sets`, etc.).

## Notes / Issues

- Use this space to record any anomalies (e.g., missing results file, guard mismatch, pipeline errors).
- Only proceed to batch/winners work once Stage 2/3 are confirmed for the run.

## Stage 2 – Batch/Winners Verification (Run A: 2025-06-20 → 2025-06-21)

- Active workbook: `data/history/Pick3StatsC4_2025_06_20.xlsm` → copied to `data/original/Pick3StatsC4.xlsm` (manifest mtime/size match).
- Results file used: `data/results/2025-06-21.txt` (CT winners 950/155, FL winners 927/120).
- Winners generation: `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/2025-06-21.txt --out-dir reports/stable/winners_by_date/2025-06-21/`
- HTML presence check:
  - Connecticut4: 950 ✅, 155 ✅
  - Florida4: 927 ✅, 120 ✅
- Table↔HTML consistency:
  - CT Combined Set1 Draw1 sequence (`059,221,070,620,201,913,763`) found in `reports/stable/winners_by_date/2025-06-21/Connecticut4/Connecticut4_vtrac2_winner_155_20251201_233350.html` ✅
- Notes: Results comparisons are day-ahead (history date +1); proceed similarly for 2025-06-21 → 2025-06-22 and 2025-06-22 → 2025-06-23.

## Stage 2 – Batch/Winners Verification (Run B: 2025-06-21 → 2025-06-22)

- Active workbook: `data/history/Pick3StatsC4_2025-06-21.xlsm` → copied to `data/original/Pick3StatsC4.xlsm` (manifest checksums updated).
- Results file used: `data/results/2025-06-22.txt` (CT winners 281/835, FL winners 330/924).
- Winners generation: `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/2025-06-22.txt --out-dir reports/stable/winners_by_date/2025-06-22/`
- HTML presence check:
  - Connecticut4: 281 ✅, 835 ✅
  - Florida4: 330 ✅, 924 ✅
- Table↔HTML consistency:
  - CT Combined Set1 Draw1 sequence (`070,620,201,913,763,950,155`) found in `reports/stable/winners_by_date/2025-06-22/Connecticut4/Connecticut4_vtrac21_winner_281_20251202_010904.html` ✅
- Notes: Continue with the same procedure for 2025-06-22 → 2025-06-23.

## Stage 2 – Batch/Winners Verification (Run C: 2025-06-22 → 2025-06-23)

- Active workbook: `data/history/Pick3StatsC4_2025-06-22.xlsm` → copied to `data/original/Pick3StatsC4.xlsm` (manifest checksums updated).
- Results file used: `data/results/2025-06-23.txt` (CT winners 130/938, FL winners 665/465).
- Winners generation: `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/2025-06-23.txt --out-dir reports/stable/winners_by_date/2025-06-23/`
- HTML presence check:
  - Connecticut4: 130 ✅, 938 ✅
  - Florida4: 665 ✅, 465 ✅
- Table↔HTML consistency:
  - CT Combined Set1 Draw1 sequence (`201,913,763,950,155,281,835`) found in `reports/stable/winners_by_date/2025-06-23/Connecticut4/Connecticut4_vtrac8_winner_130_20251202_012221.html` ✅
  - FL Combined Set1 Draw1 sequence (`262,433,241,927,120,330,924`) found in `reports/stable/winners_by_date/2025-06-23/Florida4/Florida4_vtrac6_winner_665_20251202_012223.html` ✅
- Notes: The day-ahead rule holds across all three runs; winners HTML ties back to the freshly rebuilt tables for each workbook.
