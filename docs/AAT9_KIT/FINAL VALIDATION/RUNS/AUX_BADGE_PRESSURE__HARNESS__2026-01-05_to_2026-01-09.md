# Aux Badge Pressure Harness — 2026-01-05 → 2026-01-09

- Generated: `2026-01-21T09:03:38.650173+00:00`
- Sharepacks root: `sharepacks`
- Rank-by: `pressure_density` (colors: red=3 blue=2 purple=1; shapes: RC=2 BS=1)
- K: `5`
- Event CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2026-01-05_to_2026-01-09.csv`
- Index contract CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2026-01-05_to_2026-01-09.csv`

## Summary (evaluable events = winner has a vtrac_index)

- Midday events: 69 (evaluable=67)
  - Overlay topK hit: 6 / 67 (rate=0.0896)
  - Pressure topK hit: 6 / 67 (rate=0.0896)
  - Cross-variant pressure intersection hit: 2 / 67 (rate=0.0299)
- Evening events: 69 (evaluable=69)
  - Overlay topK hit: 7 / 69 (rate=0.1014)
  - Pressure topK hit: 10 / 69 (rate=0.1449)
  - Cross-variant pressure intersection hit: 2 / 69 (rate=0.0290)

Notes:
- Combined is treated as a lens only; event evaluation uses Midday→midday and Evening→evening.
- The cross-variant intersection is computed as (topK pressure Midday) ∩ (topK pressure Evening) for the same state/day.
