# Conversion Scoreboard — 2026-01-15..2026-01-22

Source: conversion ladder CSVs (grade-output driven).

## Candidate Universe (CU) recall (per outcome)
- outcomes: `193`
- CU union hit_any: `27.5%`
- CU union vtrac_index_hit: `78.8%`

## B36

| strategy | rows | hit_any | hit_any_inclusive | pack_any_correct | pack_box_hit | pack_straight_hit | pack_correct | pack_share(inclusive) | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22` | 193 | 4.7% | 62.2% | 62.2% | 21.8% | 4.7% | 1.6% | 100.0% | 15.0% | 1.6% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top12_pos16_20` | 193 | 4.7% | 61.1% | 61.1% | 20.7% | 4.7% | 1.6% | 100.0% | 15.0% | 2.6% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos16_20` | 193 | 4.7% | 61.1% | 61.1% | 20.7% | 4.7% | 1.6% | 100.0% | 15.0% | 2.6% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_24` | 193 | 4.7% | 61.7% | 61.7% | 21.8% | 4.7% | 1.6% | 100.0% | 15.5% | 1.6% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos20_26` | 193 | 4.7% | 60.1% | 60.1% | 21.2% | 4.7% | 1.6% | 100.0% | 16.6% | 2.1% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top16_pos18_24` | 193 | 4.7% | 59.6% | 59.6% | 21.2% | 4.7% | 1.6% | 100.0% | 17.1% | 2.1% |

## Notes
- `hit_any_inclusive` is the coverage contract (lane retained or better).
- `hit_any` is the strict contract (exact membership in the budgeted list).
- `pack_any_correct` is the key bridge metric for multi-pack strategies.
- `pack_box_hit` / `pack_straight_hit` are pack-only VTRAC hits (boxed/straight).
