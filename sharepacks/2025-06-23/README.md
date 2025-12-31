# Sharepacks — 2025-06-23

Evaluating Pick3StatsC4 `D-1=2025-06-22 -> D=2025-06-23`

This folder is the frozen day snapshot used for Master Validation.

## Inputs
- History workbook (H): `data/history/Pick3StatsC4_2025-06-22.xlsm`
- Results file (D): `data/results/2025-06-23.txt`

## Contents
- Per-state bundles: `<STATE>/` (Stable, Digit Reduction, VTRAC, Hot Zones, Aux, winners lens, tables/json)
- Global VTRAC day summaries: `summary.md`, `summary.csv`, `vtrac_compact_report.*`
- Brain-2 Control Center export: `control_center/`

## Notes
- Some states may have missing winners in the results file; in that case the winners lens and winner-overlays may be absent (expected).
