# Control Center Sharepack Export — 2026-01-04

Evaluating Pick3StatsC4 `D-1=2026-01-03 -> D=2026-01-04`

This folder is the **Brain-2 / Control Center** export for the frozen day sharepack.

## Inputs (frozen, drift-proof)
- Results file: `data/results/2026-01-04.txt`
- History workbook: `data/history/Pick3StatsC4_2026-01-03.xlsm`
- Per-state Aux summaries: `sharepacks/<D>/<STATE>/aux/<STATE>/summary.json`
- Per-state Aux draw snapshots: `sharepacks/<D>/<STATE>/aux/draws/*_draws.csv`

## Outputs
- `blackapple_alerts.csv` / `.md`
- `due_doubles.csv` / `.md`
- `vtrac_repeat_watch.csv` / `.md`
- `profit_alerts.csv` / `.md`
- `profit_compound_events.csv` / `.md` (shadow; compound co-fire watchlist)
- `profit_alerts_eval.csv` / `.md` (optional; windowed evaluation harness)
- `profit_alerts_eval_merged.csv` (optional; deduped play-sets)
- `control_center_report.md`
- `meta.json`

## Regenerate
```bash
python3 scripts/tools/export_control_center_sharepack.py --date 2026-01-04
```

## Evaluate (optional; windowed)
```bash
python3 scripts/tools/evaluate_profit_alerts.py --date 2026-01-04
```
