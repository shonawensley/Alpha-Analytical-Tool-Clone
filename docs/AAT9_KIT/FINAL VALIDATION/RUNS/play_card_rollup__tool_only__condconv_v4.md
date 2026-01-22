# Play Card Rollup

- Grade files: `14`
- Rows scanned: `9408`
- experiment_tag: `condconv_v4`
- Dates covered: `14`
- Date range: `2025-06-21` → `2026-01-09`

## By strategy + budget (winner_label)

| winner_label | strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | perm_hit | closure_hit | straight_hit | vtrac_hit |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Evening | `analysis_prefix` | B36 | 192 | 0.0260 | 0.0521 | 0.1979 | 0.0521 | 0.0156 | 0.0260 | 0.1979 |
| Evening | `conversion_box_first` | B36 | 192 | 0.0260 | 0.0469 | 0.1823 | 0.0469 | 0.0260 | 0.0260 | 0.1823 |
| Evening | `analysis_prefix` | B24 | 192 | 0.0156 | 0.0417 | 0.1510 | 0.0417 | 0.0104 | 0.0156 | 0.1510 |
| Evening | `conversion_box_first` | B24 | 192 | 0.0156 | 0.0312 | 0.1510 | 0.0312 | 0.0156 | 0.0156 | 0.1510 |
| Evening | `play_box_first` | B36 | 192 | 0.0365 | 0.0417 | 0.1510 | 0.0417 | 0.0365 | 0.0365 | 0.1510 |
| Evening | `convergence_box_first` | B36 | 192 | 0.0365 | 0.0365 | 0.1458 | 0.0365 | 0.0365 | 0.0365 | 0.1458 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B36 | 192 | 0.0365 | 0.0365 | 0.1458 | 0.0365 | 0.0365 | 0.0365 | 0.1458 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B36 | 192 | 0.0365 | 0.0365 | 0.1458 | 0.0365 | 0.0365 | 0.0365 | 0.1458 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B36 | 192 | 0.0365 | 0.0365 | 0.1458 | 0.0365 | 0.0365 | 0.0365 | 0.1458 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B36 | 192 | 0.0365 | 0.0365 | 0.1458 | 0.0365 | 0.0365 | 0.0365 | 0.1458 |
| Evening | `convergence_box_first` | B24 | 192 | 0.0312 | 0.0365 | 0.1302 | 0.0365 | 0.0312 | 0.0312 | 0.1302 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B24 | 192 | 0.0312 | 0.0365 | 0.1302 | 0.0365 | 0.0312 | 0.0312 | 0.1302 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B24 | 192 | 0.0312 | 0.0365 | 0.1302 | 0.0365 | 0.0312 | 0.0312 | 0.1302 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B24 | 192 | 0.0312 | 0.0365 | 0.1302 | 0.0365 | 0.0312 | 0.0312 | 0.1302 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B24 | 192 | 0.0312 | 0.0365 | 0.1302 | 0.0365 | 0.0312 | 0.0312 | 0.1302 |
| Evening | `conversion_box_first` | B12 | 192 | 0.0052 | 0.0156 | 0.1094 | 0.0156 | 0.0052 | 0.0052 | 0.1094 |
| Evening | `analysis_prefix` | B12 | 192 | 0.0104 | 0.0208 | 0.1042 | 0.0208 | 0.0052 | 0.0104 | 0.1042 |
| Evening | `play_box_first` | B24 | 192 | 0.0260 | 0.0260 | 0.1042 | 0.0260 | 0.0260 | 0.0260 | 0.1042 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B12 | 192 | 0.0156 | 0.0208 | 0.0625 | 0.0208 | 0.0156 | 0.0156 | 0.0625 |
| Evening | `convergence_box_first` | B12 | 192 | 0.0104 | 0.0104 | 0.0573 | 0.0104 | 0.0104 | 0.0104 | 0.0573 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B12 | 192 | 0.0156 | 0.0156 | 0.0573 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B12 | 192 | 0.0156 | 0.0156 | 0.0573 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B12 | 192 | 0.0156 | 0.0156 | 0.0573 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `play_box_first` | B12 | 192 | 0.0104 | 0.0104 | 0.0469 | 0.0104 | 0.0104 | 0.0104 | 0.0469 |
| Midday | `analysis_prefix` | B36 | 190 | 0.0579 | 0.0684 | 0.2632 | 0.0684 | 0.0474 | 0.0579 | 0.2632 |
| Midday | `conversion_box_first` | B36 | 190 | 0.0632 | 0.0684 | 0.2579 | 0.0684 | 0.0579 | 0.0632 | 0.2579 |
| Midday | `analysis_prefix` | B24 | 190 | 0.0579 | 0.0684 | 0.2316 | 0.0684 | 0.0368 | 0.0579 | 0.2316 |
| Midday | `play_box_first` | B36 | 190 | 0.0632 | 0.0632 | 0.2263 | 0.0632 | 0.0632 | 0.0632 | 0.2263 |
| Midday | `convergence_box_first` | B36 | 190 | 0.0526 | 0.0526 | 0.2158 | 0.0526 | 0.0526 | 0.0526 | 0.2158 |
| Midday | `conversion_box_first` | B24 | 190 | 0.0421 | 0.0632 | 0.2158 | 0.0632 | 0.0316 | 0.0421 | 0.2158 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B36 | 190 | 0.0526 | 0.0526 | 0.2158 | 0.0526 | 0.0526 | 0.0526 | 0.2158 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B36 | 190 | 0.0526 | 0.0526 | 0.2158 | 0.0526 | 0.0526 | 0.0526 | 0.2158 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B36 | 190 | 0.0526 | 0.0526 | 0.2158 | 0.0526 | 0.0526 | 0.0526 | 0.2158 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B36 | 190 | 0.0526 | 0.0526 | 0.2158 | 0.0526 | 0.0526 | 0.0526 | 0.2158 |
| Midday | `play_box_first` | B24 | 190 | 0.0421 | 0.0421 | 0.1789 | 0.0421 | 0.0421 | 0.0421 | 0.1789 |
| Midday | `analysis_prefix` | B12 | 190 | 0.0211 | 0.0421 | 0.1737 | 0.0421 | 0.0105 | 0.0211 | 0.1737 |
| Midday | `convergence_box_first` | B24 | 190 | 0.0474 | 0.0474 | 0.1579 | 0.0474 | 0.0421 | 0.0474 | 0.1579 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B24 | 190 | 0.0474 | 0.0474 | 0.1579 | 0.0474 | 0.0421 | 0.0474 | 0.1579 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B24 | 190 | 0.0474 | 0.0474 | 0.1579 | 0.0474 | 0.0421 | 0.0474 | 0.1579 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B24 | 190 | 0.0474 | 0.0474 | 0.1579 | 0.0474 | 0.0421 | 0.0474 | 0.1579 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B24 | 190 | 0.0474 | 0.0474 | 0.1579 | 0.0474 | 0.0421 | 0.0474 | 0.1579 |
| Midday | `conversion_box_first` | B12 | 190 | 0.0211 | 0.0316 | 0.1421 | 0.0316 | 0.0158 | 0.0211 | 0.1421 |
| Midday | `play_box_first` | B12 | 190 | 0.0263 | 0.0263 | 0.1158 | 0.0263 | 0.0263 | 0.0263 | 0.1158 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B12 | 190 | 0.0158 | 0.0211 | 0.1000 | 0.0211 | 0.0158 | 0.0158 | 0.1000 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B12 | 190 | 0.0158 | 0.0211 | 0.1000 | 0.0211 | 0.0158 | 0.0158 | 0.1000 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B12 | 190 | 0.0158 | 0.0158 | 0.1000 | 0.0158 | 0.0158 | 0.0158 | 0.1000 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B12 | 190 | 0.0158 | 0.0158 | 0.1000 | 0.0158 | 0.0158 | 0.0158 | 0.1000 |
| Midday | `convergence_box_first` | B12 | 190 | 0.0158 | 0.0158 | 0.0947 | 0.0158 | 0.0158 | 0.0158 | 0.0947 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__condconv_v4.csv`
