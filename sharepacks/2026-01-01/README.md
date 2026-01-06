# Sharepacks — 2026-01-01

Evaluating Pick3StatsC4 `D-1=2025-12-31 -> D=2026-01-01`

This folder is the frozen day snapshot used for Master Validation.

## Inputs
- History workbook (H): `data/history/Pick3StatsC4_2025_12_31.xlsm`
- Results file (D): `data/results/2026-01-01.txt`

## Contents
- Per-state bundles: `<STATE>/` (Stable, Digit Reduction, VTRAC, Hot Zones, Aux, winners lens, tables/json)
- Global VTRAC day summaries: `summary.md`, `summary.csv`, `vtrac_compact_report.*`
- Brain-2 Control Center export: `control_center/`

## Notes
- Some states may have missing winners in the results file; in that case the winners lens and winner-overlays may be absent (expected).
