# Master Validation — OntarioCanada4 — 2025-06-21 (AAT9 live final runs)

Purpose: single reference for the 2025-06-21 OntarioCanada4 run (history 2025-06-20 → results 2025-06-21) with all final outputs gathered in `sharepacks/2025-06-21/OntarioCanada4/`.

## Inputs
- History workbook: `data/history/Pick3StatsC4_2025_06_20.xlsm` (activated via `run_tables_with_guard.py`)
- Results file (day-ahead): `data/results/2025-06-21.txt` (Ontario winners Midday 678, Evening 517)

## Commands (summary)
- Tables/JSON: `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_2025_06_20.xlsm`
- Winners: `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/2025-06-21.txt --out-dir reports/stable/winners_by_date/2025-06-21/`
- Digit Reduction batch: `PYTHONPATH=.:src AAT9_DR_EXTENDED_SET1=1 python3 - <<'PY' ... run_digit_reduction_workflow(...) ... PY`
- Stable: `PYTHONPATH=.:src python3 scripts/tools/run_stable_from_results.py --state OntarioCanada4 --results-file data/results/2025-06-21.txt --results-label Ontario --min-occ 1 --write-bundle`
- VTRAC enhanced: `python3 TOOLS/vtrac_enhanced_cli.py --state OntarioCanada4`
- VTRAC validator: `python3 TOOLS/vtrac_validate.py --state OntarioCanada4`
- VTRAC bundle: `python3 TOOLS/run_vtrac_share_bundle.py`
- Hot Zones: `PYTHONPATH=.:src python3 scripts/hot_zones/run_hot_zones_cli.py --state OntarioCanada4 --date 2025-06-21 --json data/outputs/json_tables/OntarioCanada4_tables.json --out-dir data/outputs/analysis/hot_zones/OntarioCanada4`

## Collected artifacts (see `sharepacks/2025-06-21/OntarioCanada4/`)
- `tables/`: Combined_Combined.csv, Midday_Combined.csv, Evening_Combined.csv
- `json/`: OntarioCanada4_tables.json
- `winners/`: HTML/JSON for 678 (Midday) and 517 (Evening)
- `digit_reduction/`: reducer report/scores, analyzer_v2 per_item/top/meta, overlays (maps/flags/hits), training log/steps
- `stable/`: scores, families, compound, metrics.json, winner spotlight raw/families, report HTML, training_sets
- `vtrac/`: enhanced analyzer bundle + validation report for OntarioCanada4
- `hot_zones/`: per_lane, top_lanes, meta, 2025-06-21_hot_zones_winner_map.json
- Global VTRAC summaries: `sharepacks/2025-06-21/{summary.md,summary.csv,vtrac_compact_report.{json,csv}}`

## Notes
- Stable initially returned zero patterns because the extractor globbed `<STATE>_*_combined.csv`; adding lowercase state-prefixed copies restored output.
- VTRAC bundle needed the enhanced analyzer + validator to populate `data/outputs/analysis/vtrac_validation/`; once run, the compact report and summaries were generated.
