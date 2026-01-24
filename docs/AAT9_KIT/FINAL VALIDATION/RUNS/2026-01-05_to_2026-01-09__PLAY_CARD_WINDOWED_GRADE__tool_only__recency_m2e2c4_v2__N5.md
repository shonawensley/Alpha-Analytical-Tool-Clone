# Play Card Windowed Grade

- sharepacks_root: `sharepacks/_predictive`
- profile: `tool_only`
- experiment_tag: `recency_m2e2c4_v2`
- date_range: `2026-01-05` → `2026-01-09`
- window_draws: `5` (Midday/Evening slots)
- rows: `4410`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `analysis_prefix` | B24 | 70 | 0.1429 | 0.2143 | 0.6000 | 0.0000 | 0.0000 | 0.6000 |
| `analysis_prefix` | B36 | 70 | 0.1571 | 0.2143 | 0.7286 | 0.0000 | 0.0000 | 0.7286 |
| `convergence_box_first` | B12 | 70 | 0.0571 | 0.0714 | 0.2429 | 0.0000 | 0.0000 | 0.2429 |
| `convergence_box_first` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `convergence_box_first` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 | 0.0000 | 0.0000 | 0.5143 |
| `conversion_box_first` | B12 | 70 | 0.0857 | 0.1000 | 0.3714 | 0.0000 | 0.0000 | 0.3714 |
| `conversion_box_first` | B24 | 70 | 0.1286 | 0.1857 | 0.5571 | 0.0000 | 0.0000 | 0.5571 |
| `conversion_box_first` | B36 | 70 | 0.1857 | 0.2286 | 0.6143 | 0.0000 | 0.0000 | 0.6143 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 70 | 0.0857 | 0.1286 | 0.2429 | 0.0000 | 0.0000 | 0.2429 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 | 0.0000 | 0.0000 | 0.5143 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 70 | 0.0857 | 0.1286 | 0.2429 | 0.0000 | 0.0000 | 0.2429 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 | 0.0000 | 0.0000 | 0.5143 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 70 | 0.0857 | 0.1143 | 0.2714 | 0.0000 | 0.0000 | 0.2714 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 | 0.0000 | 0.0000 | 0.5143 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 70 | 0.0857 | 0.1143 | 0.2571 | 0.0000 | 0.0000 | 0.2571 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 | 0.0000 | 0.0000 | 0.5143 |
| `play_box_first` | B12 | 70 | 0.0857 | 0.0857 | 0.2286 | 0.0000 | 0.0000 | 0.2286 |
| `play_box_first` | B24 | 70 | 0.1286 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `play_box_first` | B36 | 70 | 0.2000 | 0.2000 | 0.6000 | 0.0000 | 0.0000 | 0.6000 |
| `v0_2_default` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_b12pack_lenient` | B12 | 70 | 0.1000 | 0.1714 | 0.2714 | 0.1143 | 0.0143 | 0.2571 |
| `v0_2_default_b12pack_lenient` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_b12pack_lenient` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_b12pack_strict` | B12 | 70 | 0.0857 | 0.1571 | 0.2714 | 0.1000 | 0.0000 | 0.2714 |
| `v0_2_default_b12pack_strict` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_b12pack_strict` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_blackapple_reserve_conditional_lenient` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_blackapple_reserve_conditional_strict` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_blackapple_reserve_lenient` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_blackapple_reserve_lenient` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_blackapple_reserve_lenient` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_blackapple_reserve_strict` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_blackapple_reserve_strict` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_blackapple_reserve_strict` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_recency_lenient` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_recency_lenient` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_recency_lenient` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `v0_2_default_recency_strict` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 | 0.0000 | 0.0000 | 0.4429 |
| `v0_2_default_recency_strict` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `v0_2_default_recency_strict` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `vtrac_pack_boxed_first` | B12 | 70 | 0.0714 | 0.2000 | 0.4286 | 0.1143 | 0.0286 | 0.4000 |
| `vtrac_pack_boxed_first` | B24 | 70 | 0.0714 | 0.3143 | 0.7286 | 0.1143 | 0.0286 | 0.7000 |
| `vtrac_pack_boxed_first` | B36 | 70 | 0.1143 | 0.3571 | 0.8000 | 0.1143 | 0.0286 | 0.7714 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B12 | 70 | 0.0857 | 0.2429 | 0.4286 | 0.1286 | 0.0571 | 0.3714 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B24 | 70 | 0.1000 | 0.3429 | 0.7143 | 0.1286 | 0.0286 | 0.6857 |
| `vtrac_pack_boxed_first_laneonly_presetB` | B36 | 70 | 0.1429 | 0.3857 | 0.8000 | 0.1286 | 0.0286 | 0.7714 |
| `vtrac_pack_boxed_only` | B12 | 70 | 0.1000 | 0.1714 | 0.2714 | 0.1143 | 0.0143 | 0.2571 |
| `vtrac_pack_boxed_only` | B24 | 70 | 0.1571 | 0.2714 | 0.5571 | 0.1143 | 0.0143 | 0.5429 |
| `vtrac_pack_boxed_only` | B36 | 70 | 0.1714 | 0.2714 | 0.6857 | 0.1143 | 0.0000 | 0.6857 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B12 | 70 | 0.1143 | 0.2143 | 0.3000 | 0.1286 | 0.0429 | 0.2571 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B24 | 70 | 0.1714 | 0.3000 | 0.5286 | 0.1286 | 0.0143 | 0.5143 |
| `vtrac_pack_boxed_only_laneonly_presetB` | B36 | 70 | 0.1857 | 0.3143 | 0.6714 | 0.1286 | 0.0000 | 0.6714 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PLAY_CARD_WINDOWED_GRADE__tool_only__recency_m2e2c4_v2__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__recency_m2e2c4_v2__N5__2026-01-05_to_2026-01-09.csv`
