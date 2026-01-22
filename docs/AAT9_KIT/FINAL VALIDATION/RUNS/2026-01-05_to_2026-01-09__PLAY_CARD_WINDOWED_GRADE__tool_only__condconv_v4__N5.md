# Play Card Windowed Grade

- sharepacks_root: `sharepacks/_predictive`
- profile: `tool_only`
- experiment_tag: `condconv_v4`
- date_range: `2026-01-05` → `2026-01-09`
- window_draws: `5` (Midday/Evening slots)
- rows: `1680`

## Rollup (by strategy + budget)

| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive |
|---|---|---:|---:|---:|---:|
| `analysis_prefix` | B12 | 70 | 0.0714 | 0.1286 | 0.4429 |
| `analysis_prefix` | B24 | 70 | 0.1429 | 0.2143 | 0.6000 |
| `analysis_prefix` | B36 | 70 | 0.1571 | 0.2143 | 0.7286 |
| `convergence_box_first` | B12 | 70 | 0.0571 | 0.0714 | 0.2429 |
| `convergence_box_first` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 |
| `convergence_box_first` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 |
| `conversion_box_first` | B12 | 70 | 0.0857 | 0.1000 | 0.3714 |
| `conversion_box_first` | B24 | 70 | 0.1286 | 0.1857 | 0.5571 |
| `conversion_box_first` | B36 | 70 | 0.1857 | 0.2286 | 0.6143 |
| `conversion_box_first_conditional_lenient_presetA` | B12 | 70 | 0.0857 | 0.1286 | 0.2429 |
| `conversion_box_first_conditional_lenient_presetA` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 |
| `conversion_box_first_conditional_lenient_presetA` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 |
| `conversion_box_first_conditional_lenient_presetB` | B12 | 70 | 0.0857 | 0.1286 | 0.2429 |
| `conversion_box_first_conditional_lenient_presetB` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 |
| `conversion_box_first_conditional_lenient_presetB` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 |
| `conversion_box_first_conditional_strict_presetA` | B12 | 70 | 0.0857 | 0.1143 | 0.2714 |
| `conversion_box_first_conditional_strict_presetA` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 |
| `conversion_box_first_conditional_strict_presetA` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 |
| `conversion_box_first_conditional_strict_presetB` | B12 | 70 | 0.0857 | 0.1143 | 0.2571 |
| `conversion_box_first_conditional_strict_presetB` | B24 | 70 | 0.1429 | 0.1714 | 0.4429 |
| `conversion_box_first_conditional_strict_presetB` | B36 | 70 | 0.1714 | 0.1857 | 0.5143 |
| `play_box_first` | B12 | 70 | 0.0857 | 0.0857 | 0.2286 |
| `play_box_first` | B24 | 70 | 0.1286 | 0.1286 | 0.4429 |
| `play_box_first` | B36 | 70 | 0.2000 | 0.2000 | 0.6000 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v4__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__condconv_v4__N5__2026-01-05_to_2026-01-09.csv`
