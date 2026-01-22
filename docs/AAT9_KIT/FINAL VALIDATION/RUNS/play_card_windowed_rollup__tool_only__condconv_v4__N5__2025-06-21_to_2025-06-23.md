# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `condconv_v4`
- date_range: `2025-06-21` → `2025-06-23`
- window_draws: `5` (Midday/Evening slots)
- rows: `1008`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive |
|---|---|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 42 | 0.1190 | 0.1429 | 0.4286 |
| `analysis_prefix` | B24 | 42 | 0.1667 | 0.1905 | 0.5476 |
| `analysis_prefix` | B36 | 42 | 0.1905 | 0.2381 | 0.6667 |
| `convergence_box_first` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 |
| `convergence_box_first` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 |
| `convergence_box_first` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 |
| `conversion_box_first` | B12 | 42 | 0.0952 | 0.1429 | 0.4048 |
| `conversion_box_first` | B24 | 42 | 0.1429 | 0.2143 | 0.5714 |
| `conversion_box_first` | B36 | 42 | 0.2381 | 0.2619 | 0.6905 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 |
| `play_box_first` | B12 | 42 | 0.0714 | 0.0714 | 0.2619 |
| `play_box_first` | B24 | 42 | 0.1429 | 0.1429 | 0.4286 |
| `play_box_first` | B36 | 42 | 0.1905 | 0.1905 | 0.5476 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v4__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__condconv_v4__N5__2025-06-21_to_2025-06-23.csv`
