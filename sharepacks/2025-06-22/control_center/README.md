# Control Center Sharepack Export — 2025-06-22

Evaluating Pick3StatsC4 `D-1=? -> D=2025-06-22`

This folder is the **Brain-2 / Control Center** export for the frozen day sharepack.

## Inputs (frozen, drift-proof)
- Results file: `data/results/2025-06-22.txt`
- History workbook: `data/history/Pick3StatsC4_2025-06-21.xlsm`
- Per-state Aux summaries: `sharepacks/<D>/<STATE>/aux/<STATE>/summary.json`
- Per-state Aux draw snapshots: `sharepacks/<D>/<STATE>/aux/draws/*_draws.csv`

## Outputs
- `blackapple_alerts.csv` / `.md`
- `due_doubles.csv` / `.md`
- `vtrac_repeat_watch.csv` / `.md`
- `control_center_report.md`
- `meta.json`

## Regenerate
```bash
python3 scripts/tools/export_control_center_sharepack.py --date 2025-06-22
```
