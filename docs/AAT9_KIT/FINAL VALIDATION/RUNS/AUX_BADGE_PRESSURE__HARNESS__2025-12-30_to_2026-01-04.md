# Aux Badge Pressure Harness — 2025-12-30 → 2026-01-04

- Generated: `2026-01-21T09:04:01.049932+00:00`
- Sharepacks root: `sharepacks`
- Rank-by: `pressure_density` (colors: red=3 blue=2 purple=1; shapes: RC=2 BS=1)
- K: `5`
- Event CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-12-30_to_2026-01-04.csv`
- Index contract CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2025-12-30_to_2026-01-04.csv`

## Summary (evaluable events = winner has a vtrac_index)

- Midday events: 81 (evaluable=80)
  - Overlay topK hit: 5 / 80 (rate=0.0625)
  - Pressure topK hit: 8 / 80 (rate=0.1000)
  - Cross-variant pressure intersection hit: 1 / 80 (rate=0.0125)
- Evening events: 82 (evaluable=82)
  - Overlay topK hit: 7 / 82 (rate=0.0854)
  - Pressure topK hit: 15 / 82 (rate=0.1829)
  - Cross-variant pressure intersection hit: 2 / 82 (rate=0.0244)

Notes:
- Combined is treated as a lens only; event evaluation uses Midday→midday and Evening→evening.
- The cross-variant intersection is computed as (topK pressure Midday) ∩ (topK pressure Evening) for the same state/day.
