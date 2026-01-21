# Superbrain Config Harness — 2026-01-05 to 2026-01-09

Provenance
- Generated: `2026-01-21T10:00:22.152877+00:00`
- Predictive sharepacks root: `sharepacks/_predictive`
- Profile: `tool_only`
- Top N states per day: `4`
- Play Card strategy/budget: `play_box_first` / `B12`
- Aux pressure index stats: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2026-01-05_to_2026-01-09.csv`

## Summary (slot-rate over top-N states)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.250 | 0.250 | 0.050 | 0.250 | 0.250 | 0.050 |
| `pressure_tiebreak` | 0.300 | 0.300 | 0.050 | 0.250 | 0.250 | 0.050 |

## Summary (day-rate: at least one hit in top-N)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.600 | 0.600 | 0.200 | 0.600 | 0.600 | 0.200 |
| `pressure_tiebreak` | 0.600 | 0.600 | 0.200 | 0.600 | 0.600 | 0.200 |

## Notes

- This is a triage/ranking harness (Brain‑2), not an analyzer benchmark.
- `CU box_hit` measures whether the winning **canonical** is present anywhere in Candidate Universe canonicals (lane visibility).
- `CU hit_any` (MIXED) is `straight_hit OR box_hit` for the union pack, matching grade semantics.
