# Play Card Rollup

- Grade files: `14`
- Rows scanned: `9408`
- experiment_tag: `condconv_v2`
- Dates covered: `14`
- Date range: `2025-06-21` → `2026-01-09`

## By strategy + budget (winner_label)

| winner_label | strategy | budget | rows | hit_any | perm_hit | closure_hit | straight_hit | vtrac_hit |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Evening | `play_box_first` | B36 | 192 | 0.0312 | 0.0312 | 0.0312 | 0.0312 | 0.1354 |
| Evening | `analysis_prefix` | B24 | 192 | 0.0208 | 0.0365 | 0.0156 | 0.0208 | 0.1615 |
| Evening | `analysis_prefix` | B36 | 192 | 0.0208 | 0.0417 | 0.0156 | 0.0208 | 0.2031 |
| Evening | `convergence_box_first` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1042 |
| Evening | `convergence_box_first` | B36 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1406 |
| Evening | `conversion_box_first` | B36 | 192 | 0.0208 | 0.0312 | 0.0208 | 0.0208 | 0.1667 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1042 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B36 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1406 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1042 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B36 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1406 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1042 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B36 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1406 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1042 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B36 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.1406 |
| Evening | `play_box_first` | B24 | 192 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 0.0990 |
| Evening | `convergence_box_first` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first` | B24 | 192 | 0.0156 | 0.0208 | 0.0156 | 0.0156 | 0.1354 |
| Evening | `conversion_box_first_conditional_lenient_presetA` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first_conditional_lenient_presetB` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first_conditional_strict_presetA` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `conversion_box_first_conditional_strict_presetB` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0573 |
| Evening | `play_box_first` | B12 | 192 | 0.0156 | 0.0156 | 0.0156 | 0.0156 | 0.0521 |
| Evening | `analysis_prefix` | B12 | 192 | 0.0104 | 0.0260 | 0.0104 | 0.0104 | 0.1042 |
| Evening | `conversion_box_first` | B12 | 192 | 0.0052 | 0.0104 | 0.0052 | 0.0052 | 0.1094 |
| Midday | `conversion_box_first` | B36 | 190 | 0.0526 | 0.0632 | 0.0474 | 0.0526 | 0.2421 |
| Midday | `play_box_first` | B36 | 190 | 0.0474 | 0.0474 | 0.0474 | 0.0474 | 0.2105 |
| Midday | `analysis_prefix` | B36 | 190 | 0.0421 | 0.0632 | 0.0316 | 0.0421 | 0.2684 |
| Midday | `play_box_first` | B24 | 190 | 0.0421 | 0.0421 | 0.0421 | 0.0421 | 0.1737 |
| Midday | `analysis_prefix` | B24 | 190 | 0.0368 | 0.0526 | 0.0211 | 0.0368 | 0.2263 |
| Midday | `convergence_box_first` | B24 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.1474 |
| Midday | `convergence_box_first` | B36 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.2053 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B24 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.1474 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B36 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.2053 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B24 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.1474 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B36 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.2053 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B24 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.1474 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B36 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.2053 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B24 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.1474 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B36 | 190 | 0.0368 | 0.0368 | 0.0368 | 0.0368 | 0.2053 |
| Midday | `conversion_box_first` | B24 | 190 | 0.0316 | 0.0579 | 0.0316 | 0.0316 | 0.2211 |
| Midday | `analysis_prefix` | B12 | 190 | 0.0263 | 0.0368 | 0.0105 | 0.0263 | 0.1684 |
| Midday | `play_box_first` | B12 | 190 | 0.0263 | 0.0263 | 0.0263 | 0.0263 | 0.1158 |
| Midday | `convergence_box_first` | B12 | 190 | 0.0211 | 0.0211 | 0.0211 | 0.0211 | 0.0842 |
| Midday | `conversion_box_first` | B12 | 190 | 0.0211 | 0.0368 | 0.0211 | 0.0211 | 0.1263 |
| Midday | `conversion_box_first_conditional_lenient_presetA` | B12 | 190 | 0.0211 | 0.0211 | 0.0211 | 0.0211 | 0.0842 |
| Midday | `conversion_box_first_conditional_lenient_presetB` | B12 | 190 | 0.0211 | 0.0211 | 0.0211 | 0.0211 | 0.0842 |
| Midday | `conversion_box_first_conditional_strict_presetA` | B12 | 190 | 0.0211 | 0.0211 | 0.0211 | 0.0211 | 0.0842 |
| Midday | `conversion_box_first_conditional_strict_presetB` | B12 | 190 | 0.0211 | 0.0211 | 0.0211 | 0.0211 | 0.0842 |

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__condconv_v2.csv`
