# Aux Badge Pressure Harness — 2025-06-21 → 2025-06-23

- Generated: `2026-01-21T09:04:02.282906+00:00`
- Sharepacks root: `sharepacks`
- Rank-by: `pressure_density` (colors: red=3 blue=2 purple=1; shapes: RC=2 BS=1)
- K: `5`
- Event CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-06-21_to_2025-06-23.csv`
- Index contract CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2025-06-21_to_2025-06-23.csv`

## Summary (evaluable events = winner has a vtrac_index)

- Midday events: 40 (evaluable=40)
  - Overlay topK hit: 2 / 40 (rate=0.0500)
  - Pressure topK hit: 4 / 40 (rate=0.1000)
  - Cross-variant pressure intersection hit: 1 / 40 (rate=0.0250)
- Evening events: 41 (evaluable=41)
  - Overlay topK hit: 6 / 41 (rate=0.1463)
  - Pressure topK hit: 11 / 41 (rate=0.2683)
  - Cross-variant pressure intersection hit: 1 / 41 (rate=0.0244)

Notes:
- Combined is treated as a lens only; event evaluation uses Midday→midday and Evening→evening.
- The cross-variant intersection is computed as (topK pressure Midday) ∩ (topK pressure Evening) for the same state/day.
