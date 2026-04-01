# Analysis Arena Frontier Negative-Control Study

## 1. Scope

- Windows reviewed: `4`
- Frontier cases reviewed: `629`
- Enriched case roster: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_CASES.csv`
- Feature lift table: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_LIFTS.csv`

## 2. Cohort Inventory

- `strict_box`: `45` (`7.2%`)
- `straight`: `84` (`13.4%`)
- `box_gap`: `25` (`4.0%`)
- `vt_only`: `228` (`36.2%`)
- `no_conversion`: `211` (`33.5%`)
- `low_conviction_control`: `439` (`69.8%`)

## 3. Cohort Score Averages

| Cohort | Strength | Hidden | Feeder | VTRAC | Family | Literal | Double |
|---|---:|---:|---:|---:|---:|---:|---:|
| strict_box | 63.62 | 0.648 | 0.566 | 0.353 | 0.351 | 0.126 | 0.532 |
| straight | 62.31 | 0.601 | 0.592 | 0.338 | 0.332 | 0.089 | 0.470 |
| box_gap | 63.50 | 0.738 | 0.570 | 0.326 | 0.337 | 0.106 | 0.467 |
| vt_only | 55.36 | 0.484 | 0.542 | 0.313 | 0.200 | 0.028 | 0.363 |
| no_conversion | 51.11 | 0.419 | 0.514 | 0.306 | 0.138 | 0.027 | 0.231 |
| low_conviction_control | 53.31 | 0.452 | 0.529 | 0.310 | 0.170 | 0.027 | 0.299 |

## 4. Signature Mix

- `strict_box`: `FAMILY_FRONTIER` x2, `FEEDER_TO_FRONTIER` x6, `HIDDEN_COMPRESSED_FRONTIER` x28, `LITERAL_FRONTIER` x1, `VTRAC_FRONTIER` x8
- `straight`: `FAMILY_FRONTIER` x12, `FEEDER_TO_FRONTIER` x15, `HIDDEN_COMPRESSED_FRONTIER` x43, `LITERAL_FRONTIER` x1, `VTRAC_FRONTIER` x13
- `box_gap`: `FAMILY_FRONTIER` x5, `FEEDER_TO_FRONTIER` x3, `HIDDEN_COMPRESSED_FRONTIER` x17
- `vt_only`: `FAMILY_FRONTIER` x7, `FEEDER_TO_FRONTIER` x70, `HIDDEN_COMPRESSED_FRONTIER` x81, `VTRAC_FRONTIER` x70
- `no_conversion`: `FAMILY_FRONTIER` x1, `FEEDER_TO_FRONTIER` x70, `HIDDEN_COMPRESSED_FRONTIER` x75, `VTRAC_FRONTIER` x65

## 5. Discriminative Frontier Features

### Strict box vs no-conversion

- `Score threshold: literal_frontier_score >= 0.20` cohort=`24.4%` control=`0.0%` lift=`999.00x` delta=`24.4%`
- `Test: literal_frontier_v1` cohort=`20.0%` control=`0.0%` lift=`999.00x` delta=`20.0%`
- `Score threshold: frontier_strength_score >= 70` cohort=`26.7%` control=`0.5%` lift=`56.27x` delta=`26.2%`
- `Score threshold: vtrac_frontier_score >= 0.35` cohort=`37.8%` control=`4.3%` lift=`8.86x` delta=`33.5%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`48.9%` control=`7.1%` lift=`6.88x` delta=`41.8%`
- `Score threshold: double_anchor_score >= 0.55` cohort=`40.0%` control=`6.2%` lift=`6.49x` delta=`33.8%`

### Straight vs no-conversion

- `Score threshold: literal_frontier_score >= 0.20` cohort=`15.5%` control=`0.0%` lift=`999.00x` delta=`15.5%`
- `Test: literal_frontier_v1` cohort=`13.1%` control=`0.0%` lift=`999.00x` delta=`13.1%`
- `Score threshold: frontier_strength_score >= 70` cohort=`22.6%` control=`0.5%` lift=`47.73x` delta=`22.1%`
- `Signature: FAMILY_FRONTIER` cohort=`14.3%` control=`0.5%` lift=`30.14x` delta=`13.8%`
- `Score threshold: vtrac_frontier_score >= 0.35` cohort=`27.4%` control=`4.3%` lift=`6.42x` delta=`23.1%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`45.2%` control=`7.1%` lift=`6.36x` delta=`38.1%`

### Box-gap vs no-conversion

- `Test: literal_frontier_v1` cohort=`16.0%` control=`0.0%` lift=`999.00x` delta=`16.0%`
- `Score threshold: literal_frontier_score >= 0.20` cohort=`16.0%` control=`0.0%` lift=`999.00x` delta=`16.0%`
- `Signature: FAMILY_FRONTIER` cohort=`20.0%` control=`0.5%` lift=`42.20x` delta=`19.5%`
- `Score threshold: frontier_strength_score >= 70` cohort=`16.0%` control=`0.5%` lift=`33.76x` delta=`15.5%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`48.0%` control=`7.1%` lift=`6.75x` delta=`40.9%`
- `Score threshold: double_anchor_score >= 0.55` cohort=`40.0%` control=`6.2%` lift=`6.49x` delta=`33.8%`

### VT-only vs no-conversion

- `Score threshold: double_anchor_score >= 0.55` cohort=`23.2%` control=`6.2%` lift=`3.77x` delta=`17.1%`
- `Score threshold: family_frontier_score >= 0.30` cohort=`20.6%` control=`7.1%` lift=`2.90x` delta=`13.5%`
- `Test: cross_variant_echo_v1` cohort=`22.4%` control=`8.1%` lift=`2.78x` delta=`14.3%`
- `Score threshold: cross_variant_echo_score >= 0.45` cohort=`22.4%` control=`8.1%` lift=`2.78x` delta=`14.3%`
- `Test: family_frontier_v1` cohort=`39.5%` control=`19.4%` lift=`2.03x` delta=`20.0%`
- `Test: double_anchor_v1` cohort=`33.8%` control=`25.6%` lift=`1.32x` delta=`8.2%`

## 6. Ambient / Non-Discriminative Frontier Features

- `Test: vtrac_frontier_v1` control=`100.0%` strict-box lift=`1.00x` box-gap lift=`1.00x`
- `Test: feeder_progression_v1` control=`84.8%` strict-box lift=`1.10x` box-gap lift=`1.08x`
- `Score threshold: feeder_progression_score >= 0.45` control=`78.2%` strict-box lift=`1.11x` box-gap lift=`1.18x`
