# Analysis Arena Frontier Negative-Control Study

## 1. Scope

- Windows reviewed: `5`
- Frontier cases reviewed: `1043`
- Enriched case roster: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_CASES.csv`
- Feature lift table: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_LIFTS.csv`

## 2. Cohort Inventory

- `strict_box`: `74` (`7.1%`)
- `straight`: `138` (`13.2%`)
- `box_gap`: `46` (`4.4%`)
- `vt_only`: `375` (`36.0%`)
- `no_conversion`: `349` (`33.5%`)
- `low_conviction_control`: `724` (`69.4%`)

## 3. Cohort Score Averages

| Cohort | Strength | Hidden | Feeder | VTRAC | Family | Literal | Double |
|---|---:|---:|---:|---:|---:|---:|---:|
| strict_box | 62.74 | 0.638 | 0.567 | 0.348 | 0.338 | 0.127 | 0.568 |
| straight | 61.69 | 0.576 | 0.585 | 0.338 | 0.318 | 0.091 | 0.531 |
| box_gap | 63.60 | 0.698 | 0.565 | 0.332 | 0.357 | 0.106 | 0.505 |
| vt_only | 55.48 | 0.481 | 0.539 | 0.314 | 0.200 | 0.027 | 0.381 |
| no_conversion | 50.88 | 0.416 | 0.511 | 0.305 | 0.137 | 0.025 | 0.222 |
| low_conviction_control | 53.26 | 0.450 | 0.525 | 0.310 | 0.170 | 0.026 | 0.304 |

## 4. Signature Mix

- `strict_box`: `FAMILY_FRONTIER` x4, `FEEDER_TO_FRONTIER` x14, `HIDDEN_COMPRESSED_FRONTIER` x44, `LITERAL_FRONTIER` x2, `VTRAC_FRONTIER` x10
- `straight`: `FAMILY_FRONTIER` x15, `FEEDER_TO_FRONTIER` x35, `HIDDEN_COMPRESSED_FRONTIER` x67, `LITERAL_FRONTIER` x3, `VTRAC_FRONTIER` x18
- `box_gap`: `FAMILY_FRONTIER` x6, `FEEDER_TO_FRONTIER` x4, `HIDDEN_COMPRESSED_FRONTIER` x28, `LITERAL_FRONTIER` x1, `VTRAC_FRONTIER` x7
- `vt_only`: `FAMILY_FRONTIER` x15, `FEEDER_TO_FRONTIER` x114, `HIDDEN_COMPRESSED_FRONTIER` x133, `VTRAC_FRONTIER` x113
- `no_conversion`: `FAMILY_FRONTIER` x2, `FEEDER_TO_FRONTIER` x114, `HIDDEN_COMPRESSED_FRONTIER` x122, `VTRAC_FRONTIER` x111

## 5. Discriminative Frontier Features

### Strict box vs no-conversion

- `Score threshold: literal_frontier_score >= 0.20` cohort=`24.3%` control=`0.0%` lift=`999.00x` delta=`24.3%`
- `Test: literal_frontier_v1` cohort=`21.6%` control=`0.0%` lift=`999.00x` delta=`21.6%`
- `Score threshold: frontier_strength_score >= 70` cohort=`23.0%` control=`0.3%` lift=`80.18x` delta=`22.7%`
- `Score threshold: vtrac_frontier_score >= 0.35` cohort=`33.8%` control=`4.0%` lift=`8.42x` delta=`29.8%`
- `Score threshold: double_anchor_score >= 0.55` cohort=`47.3%` control=`6.0%` lift=`7.86x` delta=`41.3%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`43.2%` control=`6.6%` lift=`6.56x` delta=`36.7%`

### Straight vs no-conversion

- `Score threshold: literal_frontier_score >= 0.20` cohort=`15.2%` control=`0.0%` lift=`999.00x` delta=`15.2%`
- `Test: literal_frontier_v1` cohort=`13.8%` control=`0.0%` lift=`999.00x` delta=`13.8%`
- `Score threshold: frontier_strength_score >= 70` cohort=`19.6%` control=`0.3%` lift=`68.28x` delta=`19.3%`
- `Signature: FAMILY_FRONTIER` cohort=`10.9%` control=`0.6%` lift=`18.97x` delta=`10.3%`
- `Score threshold: double_anchor_score >= 0.55` cohort=`42.8%` control=`6.0%` lift=`7.11x` delta=`36.7%`
- `Score threshold: vtrac_frontier_score >= 0.35` cohort=`26.1%` control=`4.0%` lift=`6.50x` delta=`22.1%`

### Box-gap vs no-conversion

- `Test: literal_frontier_v1` cohort=`17.4%` control=`0.0%` lift=`999.00x` delta=`17.4%`
- `Score threshold: literal_frontier_score >= 0.20` cohort=`17.4%` control=`0.0%` lift=`999.00x` delta=`17.4%`
- `Score threshold: frontier_strength_score >= 70` cohort=`21.7%` control=`0.3%` lift=`75.87x` delta=`21.5%`
- `Signature: FAMILY_FRONTIER` cohort=`13.0%` control=`0.6%` lift=`22.76x` delta=`12.5%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`54.3%` control=`6.6%` lift=`8.25x` delta=`47.8%`
- `Score threshold: double_anchor_score >= 0.55` cohort=`45.7%` control=`6.0%` lift=`7.59x` delta=`39.6%`

### VT-only vs no-conversion

- `Score threshold: double_anchor_score >= 0.55` cohort=`26.1%` control=`6.0%` lift=`4.34x` delta=`20.1%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`19.5%` control=`6.6%` lift=`2.95x` delta=`12.9%`
- `Test: cross_variant_echo_v1` cohort=`21.3%` control=`7.4%` lift=`2.86x` delta=`13.9%`
- `Score threshold: cross_variant_echo_score >= 0.45` cohort=`21.3%` control=`7.4%` lift=`2.86x` delta=`13.9%`
- `Test: family_frontier_v1` cohort=`40.3%` control=`18.9%` lift=`2.13x` delta=`21.4%`
- `Test: double_anchor_v1` cohort=`34.7%` control=`23.5%` lift=`1.48x` delta=`11.2%`

## 6. Ambient / Non-Discriminative Frontier Features

- `Test: vtrac_frontier_v1` control=`100.0%` strict-box lift=`1.00x` box-gap lift=`1.00x`
- `Test: feeder_progression_v1` control=`83.7%` strict-box lift=`1.11x` box-gap lift=`1.09x`
- `Score threshold: feeder_progression_score >= 0.45` control=`74.5%` strict-box lift=`1.16x` box-gap lift=`1.17x`
