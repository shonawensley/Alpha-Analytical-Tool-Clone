# Play Card Windowed Grade

- sharepacks_root: `sharepacks`
- profile: `tool_only`
- experiment_tag: `recency_m2e2c4_v1`
- date_range: `2025-12-30` → `2026-01-04`
- window_draws: `5` (Midday/Evening slots)
- rows: `5292`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `analysis_prefix` | B24 | 84 | 0.1905 | 0.2619 | 0.7024 | 0.0000 | 0.0000 | 0.7024 |
| `analysis_prefix` | B36 | 84 | 0.2143 | 0.2976 | 0.7976 | 0.0000 | 0.0000 | 0.7976 |
| `convergence_box_first` | B12 | 84 | 0.0833 | 0.0952 | 0.3571 | 0.0000 | 0.0000 | 0.3571 |
| `convergence_box_first` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `convergence_box_first` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `conversion_box_first` | B12 | 84 | 0.0595 | 0.1310 | 0.5000 | 0.0000 | 0.0000 | 0.5000 |
| `conversion_box_first` | B24 | 84 | 0.1429 | 0.2024 | 0.6667 | 0.0000 | 0.0000 | 0.6667 |
| `conversion_box_first` | B36 | 84 | 0.1905 | 0.2500 | 0.7262 | 0.0000 | 0.0000 | 0.7262 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 84 | 0.0595 | 0.1071 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 84 | 0.0595 | 0.0952 | 0.3690 | 0.0000 | 0.0000 | 0.3690 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 84 | 0.1667 | 0.1667 | 0.5476 | 0.0000 | 0.0000 | 0.5476 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 84 | 0.2143 | 0.2143 | 0.6429 | 0.0000 | 0.0000 | 0.6429 |
| `play_box_first` | B12 | 84 | 0.0833 | 0.0833 | 0.3571 | 0.0000 | 0.0000 | 0.3571 |
| `play_box_first` | B24 | 84 | 0.1667 | 0.1667 | 0.5238 | 0.0000 | 0.0000 | 0.5238 |
| `play_box_first` | B36 | 84 | 0.2262 | 0.2381 | 0.6905 | 0.0000 | 0.0000 | 0.6905 |
| `v0_2_default` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_b12pack_lenient` | B12 | 84 | 0.0476 | 0.2024 | 0.3810 | 0.1190 | 0.0238 | 0.3571 |
| `v0_2_default_b12pack_lenient` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_b12pack_lenient` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_b12pack_strict` | B12 | 84 | 0.0357 | 0.1905 | 0.4167 | 0.0833 | 0.0119 | 0.4048 |
| `v0_2_default_b12pack_strict` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_b12pack_strict` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_blackapple_reserve_lenient` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_lenient` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_blackapple_reserve_lenient` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_blackapple_reserve_strict` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_blackapple_reserve_strict` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_blackapple_reserve_strict` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_recency_lenient` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_recency_lenient` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_recency_lenient` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `v0_2_default_recency_strict` | B12 | 84 | 0.0595 | 0.1429 | 0.4762 | 0.0000 | 0.0000 | 0.4762 |
| `v0_2_default_recency_strict` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `v0_2_default_recency_strict` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `vtrac_pack_boxed_first` | B12 | 84 | 0.0476 | 0.2143 | 0.5119 | 0.1310 | 0.0952 | 0.4167 |
| `vtrac_pack_boxed_first` | B24 | 84 | 0.1190 | 0.4048 | 0.7976 | 0.1310 | 0.0119 | 0.7857 |
| `vtrac_pack_boxed_first` | B36 | 84 | 0.1786 | 0.4643 | 0.8810 | 0.1310 | 0.0238 | 0.8571 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B12 | 84 | 0.0357 | 0.2024 | 0.4524 | 0.1310 | 0.0952 | 0.3571 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B24 | 84 | 0.1190 | 0.3929 | 0.7619 | 0.1310 | 0.0238 | 0.7381 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B36 | 84 | 0.1548 | 0.4643 | 0.8810 | 0.1310 | 0.0119 | 0.8690 |
| `vtrac_pack_boxed_only` | B12 | 84 | 0.0476 | 0.2143 | 0.3810 | 0.1310 | 0.0357 | 0.3452 |
| `vtrac_pack_boxed_only` | B24 | 84 | 0.1786 | 0.2976 | 0.6190 | 0.1310 | 0.0000 | 0.6190 |
| `vtrac_pack_boxed_only` | B36 | 84 | 0.2143 | 0.3333 | 0.7619 | 0.1310 | 0.0000 | 0.7619 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B12 | 84 | 0.0238 | 0.1905 | 0.3810 | 0.1310 | 0.0357 | 0.3452 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B24 | 84 | 0.1548 | 0.3095 | 0.6310 | 0.1310 | 0.0000 | 0.6310 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B36 | 84 | 0.2143 | 0.3452 | 0.7500 | 0.1310 | 0.0000 | 0.7500 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_WINDOWED_GRADE__tool_only__recency_m2e2c4_v1__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__recency_m2e2c4_v1__N5__2025-12-30_to_2026-01-04.csv`
