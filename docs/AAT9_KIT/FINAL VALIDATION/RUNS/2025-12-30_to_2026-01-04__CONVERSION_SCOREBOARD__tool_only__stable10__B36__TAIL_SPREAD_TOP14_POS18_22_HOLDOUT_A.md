# Conversion Scoreboard — 2025-12-30..2026-01-04

Source: conversion ladder CSVs (grade-output driven).

## Candidate Universe (CU) recall (per outcome)
- outcomes: `163`
- CU union hit_any: `23.9%`
- CU union vtrac_index_hit: `74.8%`

## B36

| strategy | rows | hit_any | hit_any_inclusive | pack_any_correct | pack_box_hit | pack_straight_hit | pack_correct | pack_share(inclusive) | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first` | 163 | 4.3% | 56.4% | 56.4% | 12.9% | 4.3% | 3.7% | 100.0% | 14.7% | 3.7% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22` | 163 | 4.9% | 56.4% | 56.4% | 13.5% | 4.9% | 3.7% | 100.0% | 16.0% | 2.5% |

## Notes
- `hit_any_inclusive` is the coverage contract (lane retained or better).
- `hit_any` is the strict contract (exact membership in the budgeted list).
- `pack_any_correct` is the key bridge metric for multi-pack strategies.
- `pack_box_hit` / `pack_straight_hit` are pack-only VTRAC hits (boxed/straight).
