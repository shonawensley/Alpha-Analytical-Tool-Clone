# Conversion Scoreboard — 2025-06-21..2025-06-23

Source: conversion ladder CSVs (grade-output driven).

## Candidate Universe (CU) recall (per outcome)
- outcomes: `81`
- CU union hit_any: `28.4%`
- CU union vtrac_index_hit: `65.4%`

## B36

| strategy | rows | hit_any | hit_any_inclusive | pack_any_correct | pack_box_hit | pack_straight_hit | pack_correct | pack_share(inclusive) | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first` | 81 | 2.5% | 51.9% | 51.9% | 12.3% | 2.5% | 1.2% | 100.0% | 12.3% | 1.2% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22` | 81 | 2.5% | 54.3% | 54.3% | 12.3% | 2.5% | 1.2% | 100.0% | 9.9% | 1.2% |

## Notes
- `hit_any_inclusive` is the coverage contract (lane retained or better).
- `hit_any` is the strict contract (exact membership in the budgeted list).
- `pack_any_correct` is the key bridge metric for multi-pack strategies.
- `pack_box_hit` / `pack_straight_hit` are pack-only VTRAC hits (boxed/straight).
