# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `ba_pack_control_v1`
- date_range: `2025-06-21` → `2025-06-23`
- window_draws: `5` (Midday/Evening slots)
- rows: `2142`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 42 | 0.1190 | 0.1429 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `analysis_prefix` | B24 | 42 | 0.1667 | 0.1905 | 0.5238 | 0.0000 | 0.0000 | 0.5238 |
| `analysis_prefix` | B36 | 42 | 0.2143 | 0.2619 | 0.6667 | 0.0000 | 0.0000 | 0.6667 |
| `convergence_box_first` | B12 | 42 | 0.0952 | 0.0952 | 0.2619 | 0.0000 | 0.0000 | 0.2619 |
| `convergence_box_first` | B24 | 42 | 0.1667 | 0.1667 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `convergence_box_first` | B36 | 42 | 0.2143 | 0.2143 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first` | B12 | 42 | 0.1190 | 0.1429 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `conversion_box_first` | B24 | 42 | 0.1429 | 0.1905 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first` | B36 | 42 | 0.2619 | 0.2619 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 42 | 0.0952 | 0.0952 | 0.2857 | 0.0000 | 0.0000 | 0.2857 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 42 | 0.2143 | 0.2143 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 42 | 0.0952 | 0.0952 | 0.2857 | 0.0000 | 0.0000 | 0.2857 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 42 | 0.2143 | 0.2143 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 42 | 0.0952 | 0.0952 | 0.2857 | 0.0000 | 0.0000 | 0.2857 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 42 | 0.1667 | 0.1667 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 42 | 0.2143 | 0.2143 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 42 | 0.0952 | 0.0952 | 0.2857 | 0.0000 | 0.0000 | 0.2857 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 42 | 0.1667 | 0.1667 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 42 | 0.2143 | 0.2143 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `play_box_first` | B12 | 42 | 0.0952 | 0.0952 | 0.2857 | 0.0000 | 0.0000 | 0.2857 |
| `play_box_first` | B24 | 42 | 0.1429 | 0.1429 | 0.4048 | 0.0000 | 0.0000 | 0.4048 |
| `play_box_first` | B36 | 42 | 0.1905 | 0.1905 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `v0_2_default` | B12 | 42 | 0.1190 | 0.1429 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `v0_2_default` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `v0_2_default` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `v0_2_default_b12pack_lenient` | B12 | 42 | 0.0952 | 0.0952 | 0.3095 | 0.0476 | 0.0000 | 0.3095 |
| `v0_2_default_b12pack_lenient` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `v0_2_default_b12pack_lenient` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `v0_2_default_b12pack_strict` | B12 | 42 | 0.0952 | 0.0952 | 0.3095 | 0.0238 | 0.0000 | 0.3095 |
| `v0_2_default_b12pack_strict` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `v0_2_default_b12pack_strict` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `v0_2_default_blackapple_reserve_lenient` | B12 | 42 | 0.1190 | 0.1429 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `v0_2_default_blackapple_reserve_lenient` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `v0_2_default_blackapple_reserve_lenient` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `v0_2_default_blackapple_reserve_strict` | B12 | 42 | 0.1190 | 0.1429 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `v0_2_default_blackapple_reserve_strict` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `v0_2_default_blackapple_reserve_strict` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `vtrac_pack_boxed_first` | B12 | 42 | 0.0238 | 0.1905 | 0.4286 | 0.0476 | 0.0000 | 0.4286 |
| `vtrac_pack_boxed_first` | B24 | 42 | 0.1429 | 0.2857 | 0.6667 | 0.0476 | 0.0238 | 0.6429 |
| `vtrac_pack_boxed_first` | B36 | 42 | 0.2143 | 0.4286 | 0.8333 | 0.0476 | 0.0238 | 0.8095 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B12 | 42 | 0.0476 | 0.2619 | 0.4286 | 0.0952 | 0.0714 | 0.3571 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B24 | 42 | 0.1905 | 0.3810 | 0.7143 | 0.0952 | 0.0476 | 0.6667 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B36 | 42 | 0.2143 | 0.5000 | 0.8095 | 0.0952 | 0.0476 | 0.7619 |
| `vtrac_pack_boxed_only` | B12 | 42 | 0.0952 | 0.0952 | 0.3095 | 0.0476 | 0.0000 | 0.3095 |
| `vtrac_pack_boxed_only` | B24 | 42 | 0.1190 | 0.1429 | 0.5238 | 0.0476 | 0.0000 | 0.5238 |
| `vtrac_pack_boxed_only` | B36 | 42 | 0.2143 | 0.2381 | 0.6429 | 0.0476 | 0.0000 | 0.6429 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B12 | 42 | 0.0714 | 0.1667 | 0.3333 | 0.0952 | 0.0476 | 0.2857 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B24 | 42 | 0.1429 | 0.2381 | 0.5238 | 0.0952 | 0.0000 | 0.5238 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B36 | 42 | 0.2143 | 0.3095 | 0.6190 | 0.0952 | 0.0000 | 0.6190 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_WINDOWED_GRADE__tool_only__ba_pack_control_v1__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__ba_pack_control_v1__N5__2025-06-21_to_2025-06-23.csv`
