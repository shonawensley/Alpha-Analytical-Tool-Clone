# Superbrain Config Harness — 2025-06-21 to 2025-06-23

Provenance
- Generated: `2026-01-21T10:00:20.552257+00:00`
- Predictive sharepacks root: `sharepacks`
- Profile: `tool_only`
- Top N states per day: `4`
- Play Card strategy/budget: `play_box_first` / `B12`
- Aux pressure index stats: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__2025-06-21_to_2025-06-23.csv`

## Summary (slot-rate over top-N states)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.083 | 0.083 | 0.000 | 0.167 | 0.167 | 0.000 |
| `pressure_tiebreak` | 0.083 | 0.083 | 0.000 | 0.250 | 0.250 | 0.000 |

## Summary (day-rate: at least one hit in top-N)

| Config | Midday CU hit_any | Midday CU box_hit | Midday PC hit_any | Evening CU hit_any | Evening CU box_hit | Evening PC hit_any |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_tool_first` | 0.333 | 0.333 | 0.000 | 0.333 | 0.333 | 0.000 |
| `pressure_tiebreak` | 0.333 | 0.333 | 0.000 | 1.000 | 1.000 | 0.000 |

## Notes

- This is a triage/ranking harness (Brain‑2), not an analyzer benchmark.
- `CU box_hit` measures whether the winning **canonical** is present anywhere in Candidate Universe canonicals (lane visibility).
- `CU hit_any` (MIXED) is `straight_hit OR box_hit` for the union pack, matching grade semantics.
