# Superbrain Config Harness — 2025-12-30 to 2026-01-04

Provenance
- Generated: `2026-01-21T10:00:21.364711+00:00`
- Predictive sharepacks root: `sharepacks`
- Profile: `tool_only`
- Top N states per day: `4`
- Play Card strategy/budget: `play_box_first` / `B12`
- Aux pressure index stats: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2025-12-30_to_2026-01-04.csv`

## Summary (slot-rate over top-N states)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.250 | 0.250 | 0.042 | 0.167 | 0.167 | 0.000 |
| `pressure_tiebreak` | 0.208 | 0.208 | 0.042 | 0.167 | 0.167 | 0.000 |

## Summary (day-rate: at least one hit in top-N)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.667 | 0.667 | 0.167 | 0.667 | 0.667 | 0.000 |
| `pressure_tiebreak` | 0.333 | 0.333 | 0.167 | 0.667 | 0.667 | 0.000 |

## Notes

- This is a triage/ranking harness (Brain‑2), not an analyzer benchmark.
- `CU box_hit` measures whether the winning **canonical** is present anywhere in Candidate Universe canonicals (lane visibility).
- `CU hit_any` (MIXED) is `straight_hit OR box_hit` for the union pack, matching grade semantics.
