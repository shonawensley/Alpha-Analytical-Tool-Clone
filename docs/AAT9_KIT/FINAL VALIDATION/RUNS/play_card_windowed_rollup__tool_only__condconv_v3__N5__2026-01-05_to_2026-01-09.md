# Play Card Windowed Grade

- sharepacks_root: `sharepacks/_predictive`
- profile: `tool_only`
- experiment_tag: `condconv_v3`
- date_range: `2026-01-05` → `2026-01-09`
- window_draws: `5` (Midday/Evening slots)
- rows: `1680`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive |
|---|---|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 70 | 0.0714 | 0.1714 | 0.4571 |
| `analysis_prefix` | B24 | 70 | 0.1286 | 0.1857 | 0.6286 |
| `analysis_prefix` | B36 | 70 | 0.1286 | 0.2143 | 0.7143 |
| `convergence_box_first` | B12 | 70 | 0.0714 | 0.0714 | 0.2143 |
| `convergence_box_first` | B24 | 70 | 0.1286 | 0.1571 | 0.3571 |
| `convergence_box_first` | B36 | 70 | 0.1286 | 0.1571 | 0.5000 |
| `conversion_box_first` | B12 | 70 | 0.0857 | 0.1000 | 0.3429 |
| `conversion_box_first` | B24 | 70 | 0.1143 | 0.1714 | 0.5571 |
| `conversion_box_first` | B36 | 70 | 0.1714 | 0.2000 | 0.6286 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 70 | 0.1000 | 0.1714 | 0.2857 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 70 | 0.1429 | 0.1571 | 0.4571 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 70 | 0.1286 | 0.2143 | 0.5571 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 70 | 0.1000 | 0.1714 | 0.2714 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 70 | 0.1429 | 0.2000 | 0.4429 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 70 | 0.1286 | 0.2286 | 0.5571 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 70 | 0.0857 | 0.1143 | 0.3000 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 70 | 0.1286 | 0.1857 | 0.5143 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 70 | 0.1286 | 0.1714 | 0.5000 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 70 | 0.0857 | 0.1571 | 0.2714 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 70 | 0.1286 | 0.1857 | 0.5286 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 70 | 0.1286 | 0.2143 | 0.5571 |
| `play_box_first` | B12 | 70 | 0.1000 | 0.1000 | 0.2571 |
| `play_box_first` | B24 | 70 | 0.1714 | 0.1714 | 0.4286 |
| `play_box_first` | B36 | 70 | 0.1714 | 0.1714 | 0.5429 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v3__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__condconv_v3__N5__2026-01-05_to_2026-01-09.csv`
