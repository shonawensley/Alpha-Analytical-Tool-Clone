# Conversion Scoreboard — 2026-01-01..2026-01-09

Source: conversion ladder CSVs (grade-output driven).

## Candidate Universe (CU) recall (per outcome)
- outcomes: `245`
- CU union hit_any: `25.7%`
- CU union vtrac_index_hit: `71.0%`

## B36

| strategy | rows | hit_any | hit_any_inclusive | pack_any_correct | pack_box_hit | pack_straight_hit | pack_correct | pack_share(inclusive) | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first` | 245 | 4.1% | 53.1% | 53.1% | 15.1% | 4.1% | 2.9% | 100.0% | 14.7% | 3.3% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first` | 245 | 4.1% | 53.1% | 53.1% | 13.9% | 4.1% | 3.3% | 100.0% | 14.7% | 3.3% |

## Notes
- `hit_any_inclusive` is the coverage contract (lane retained or better).
- `hit_any` is the strict contract (exact membership in the budgeted list).
- `pack_any_correct` is the key bridge metric for multi-pack strategies.
- `pack_box_hit` / `pack_straight_hit` are pack-only VTRAC hits (boxed/straight).
