# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `condconv_v4`
- date_range: `2025-12-30` → `2026-01-04`
- window_draws: `5` (Midday/Evening slots)
- rows: `2016`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive |
|---|---|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 |
| `analysis_prefix` | B24 | 84 | 0.1905 | 0.2619 | 0.7024 |
| `analysis_prefix` | B36 | 84 | 0.2143 | 0.2976 | 0.7976 |
| `convergence_box_first` | B12 | 84 | 0.0833 | 0.0952 | 0.3571 |
| `convergence_box_first` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 |
| `convergence_box_first` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 |
| `conversion_box_first` | B12 | 84 | 0.0595 | 0.1310 | 0.5000 |
| `conversion_box_first` | B24 | 84 | 0.1429 | 0.2024 | 0.6667 |
| `conversion_box_first` | B36 | 84 | 0.1905 | 0.2500 | 0.7262 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 84 | 0.0595 | 0.1071 | 0.3690 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 |
| `play_box_first` | B12 | 84 | 0.0833 | 0.0833 | 0.3571 |
| `play_box_first` | B24 | 84 | 0.1667 | 0.1667 | 0.5238 |
| `play_box_first` | B36 | 84 | 0.2262 | 0.2381 | 0.6905 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v4__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__condconv_v4__N5__2025-12-30_to_2026-01-04.csv`
