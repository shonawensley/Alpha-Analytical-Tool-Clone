# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `ba_pack_v1`
- date_range: `2025-12-30` → `2026-01-04`
- window_draws: `5` (Midday/Evening slots)
- rows: `4284`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 84 | 0.0952 | 0.1310 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `analysis_prefix` | B24 | 84 | 0.1548 | 0.2262 | 0.6905 | 0.0000 | 0.0000 | 0.6905 |
| `analysis_prefix` | B36 | 84 | 0.1667 | 0.2738 | 0.7976 | 0.0000 | 0.0000 | 0.7976 |
| `convergence_box_first` | B12 | 84 | 0.0714 | 0.0714 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `convergence_box_first` | B24 | 84 | 0.1190 | 0.1190 | 0.5119 | 0.0000 | 0.0000 | 0.5119 |
| `convergence_box_first` | B36 | 84 | 0.1905 | 0.1905 | 0.6548 | 0.0000 | 0.0000 | 0.6548 |
| `conversion_box_first` | B12 | 84 | 0.0595 | 0.1667 | 0.5357 | 0.0000 | 0.0000 | 0.5357 |
| `conversion_box_first` | B24 | 84 | 0.1190 | 0.1905 | 0.6905 | 0.0000 | 0.0000 | 0.6905 |
| `conversion_box_first` | B36 | 84 | 0.1667 | 0.2262 | 0.7857 | 0.0000 | 0.0000 | 0.7857 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 84 | 0.0595 | 0.0833 | 0.3810 | 0.0000 | 0.0000 | 0.3810 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 84 | 0.1190 | 0.1190 | 0.5119 | 0.0000 | 0.0000 | 0.5119 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 84 | 0.1905 | 0.1905 | 0.6548 | 0.0000 | 0.0000 | 0.6548 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 84 | 0.0595 | 0.0833 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 84 | 0.1190 | 0.1190 | 0.5119 | 0.0000 | 0.0000 | 0.5119 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 84 | 0.1905 | 0.1905 | 0.6548 | 0.0000 | 0.0000 | 0.6548 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 84 | 0.0595 | 0.0833 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 84 | 0.1190 | 0.1190 | 0.5119 | 0.0000 | 0.0000 | 0.5119 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 84 | 0.1905 | 0.1905 | 0.6548 | 0.0000 | 0.0000 | 0.6548 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 84 | 0.0595 | 0.0833 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 84 | 0.1190 | 0.1190 | 0.5119 | 0.0000 | 0.0000 | 0.5119 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 84 | 0.1905 | 0.1905 | 0.6548 | 0.0000 | 0.0000 | 0.6548 |
| `play_box_first` | B12 | 84 | 0.0714 | 0.0714 | 0.3452 | 0.0000 | 0.0000 | 0.3452 |
| `play_box_first` | B24 | 84 | 0.1429 | 0.1429 | 0.5357 | 0.0000 | 0.0000 | 0.5357 |
| `play_box_first` | B36 | 84 | 0.2024 | 0.2024 | 0.6786 | 0.0000 | 0.0000 | 0.6786 |
| `v0_2_default` | B12 | 84 | 0.0952 | 0.1310 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `v0_2_default` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `v0_2_default_b12pack_lenient` | B12 | 84 | 0.0357 | 0.1548 | 0.3214 | 0.0952 | 0.0000 | 0.3214 |
| `v0_2_default_b12pack_lenient` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `v0_2_default_b12pack_lenient` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `v0_2_default_b12pack_strict` | B12 | 84 | 0.0238 | 0.1548 | 0.3810 | 0.0714 | 0.0000 | 0.3810 |
| `v0_2_default_b12pack_strict` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `v0_2_default_b12pack_strict` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `v0_2_default_blackapple_reserve_lenient` | B12 | 84 | 0.0952 | 0.1310 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_lenient` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `v0_2_default_blackapple_reserve_lenient` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `v0_2_default_blackapple_reserve_strict` | B12 | 84 | 0.0952 | 0.1310 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_strict` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `v0_2_default_blackapple_reserve_strict` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `vtrac_pack_boxed_first` | B12 | 84 | 0.0476 | 0.2024 | 0.4762 | 0.1190 | 0.0714 | 0.4048 |
| `vtrac_pack_boxed_first` | B24 | 84 | 0.1310 | 0.3929 | 0.7738 | 0.1190 | 0.0119 | 0.7619 |
| `vtrac_pack_boxed_first` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1190 | 0.0357 | 0.7976 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B12 | 84 | 0.0476 | 0.2143 | 0.4405 | 0.1429 | 0.0833 | 0.3571 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B24 | 84 | 0.1310 | 0.3929 | 0.7619 | 0.1429 | 0.0119 | 0.7500 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B36 | 84 | 0.1548 | 0.4405 | 0.8333 | 0.1429 | 0.0357 | 0.7976 |
| `vtrac_pack_boxed_only` | B12 | 84 | 0.0238 | 0.1667 | 0.3214 | 0.1190 | 0.0238 | 0.2976 |
| `vtrac_pack_boxed_only` | B24 | 84 | 0.1429 | 0.3095 | 0.6548 | 0.1190 | 0.0119 | 0.6429 |
| `vtrac_pack_boxed_only` | B36 | 84 | 0.1667 | 0.3333 | 0.7619 | 0.1190 | 0.0119 | 0.7500 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B12 | 84 | 0.0119 | 0.1667 | 0.3452 | 0.1429 | 0.0595 | 0.2857 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B24 | 84 | 0.1429 | 0.3214 | 0.6548 | 0.1429 | 0.0119 | 0.6429 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B36 | 84 | 0.1667 | 0.3452 | 0.7381 | 0.1429 | 0.0119 | 0.7262 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_WINDOWED_GRADE__tool_only__ba_pack_v1__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__ba_pack_v1__N5__2025-12-30_to_2026-01-04.csv`
