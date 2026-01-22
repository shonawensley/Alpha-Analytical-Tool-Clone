# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `vtracpack_v2`
- date_range: `2025-06-21` → `2025-06-23`
- window_draws: `5` (Midday/Evening slots)
- rows: `1512`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 42 | 0.1190 | 0.1429 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `analysis_prefix` | B24 | 42 | 0.1667 | 0.1905 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `analysis_prefix` | B36 | 42 | 0.1905 | 0.2381 | 0.6667 | 0.0000 | 0.0000 | 0.6667 |
| `convergence_box_first` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 | 0.0000 | 0.0000 | 0.2381 |
| `convergence_box_first` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `convergence_box_first` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first` | B12 | 42 | 0.0952 | 0.1429 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `conversion_box_first` | B24 | 42 | 0.1429 | 0.2143 | 0.5714 | 0.0000 | 0.0000 | 0.5714 |
| `conversion_box_first` | B36 | 42 | 0.2381 | 0.2619 | 0.6905 | 0.0000 | 0.0000 | 0.6905 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 | 0.0000 | 0.0000 | 0.2381 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 | 0.0000 | 0.0000 | 0.2381 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 | 0.0000 | 0.0000 | 0.2381 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 42 | 0.0714 | 0.0714 | 0.2381 | 0.0000 | 0.0000 | 0.2381 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 42 | 0.2381 | 0.2381 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `play_box_first` | B12 | 42 | 0.0714 | 0.0714 | 0.2619 | 0.0000 | 0.0000 | 0.2619 |
| `play_box_first` | B24 | 42 | 0.1429 | 0.1429 | 0.4286 | 0.0000 | 0.0000 | 0.4286 |
| `play_box_first` | B36 | 42 | 0.1905 | 0.1905 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `vtrac_pack_boxed_first` | B12 | 42 | 0.0238 | 0.1667 | 0.4048 | 0.0238 | 0.0238 | 0.3810 |
| `vtrac_pack_boxed_first` | B24 | 42 | 0.1429 | 0.2857 | 0.7381 | 0.0238 | 0.0000 | 0.7381 |
| `vtrac_pack_boxed_first` | B36 | 42 | 0.1905 | 0.4286 | 0.8810 | 0.0238 | 0.0000 | 0.8810 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B12 | 42 | 0.0952 | 0.2619 | 0.4048 | 0.0952 | 0.0952 | 0.3095 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B24 | 42 | 0.1429 | 0.3571 | 0.7381 | 0.0952 | 0.0476 | 0.6905 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B36 | 42 | 0.1905 | 0.5000 | 0.8810 | 0.0952 | 0.0476 | 0.8333 |
| `vtrac_pack_boxed_only` | B12 | 42 | 0.0952 | 0.0952 | 0.3333 | 0.0238 | 0.0000 | 0.3333 |
| `vtrac_pack_boxed_only` | B24 | 42 | 0.1190 | 0.1429 | 0.5238 | 0.0238 | 0.0000 | 0.5238 |
| `vtrac_pack_boxed_only` | B36 | 42 | 0.1667 | 0.2143 | 0.5952 | 0.0238 | 0.0000 | 0.5952 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B12 | 42 | 0.0476 | 0.1667 | 0.3095 | 0.0952 | 0.0476 | 0.2619 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B24 | 42 | 0.1429 | 0.2381 | 0.5238 | 0.0952 | 0.0000 | 0.5238 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B36 | 42 | 0.1667 | 0.2857 | 0.5952 | 0.0952 | 0.0000 | 0.5952 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_WINDOWED_GRADE__tool_only__vtracpack_v2__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v2__N5__2025-06-21_to_2025-06-23.csv`
