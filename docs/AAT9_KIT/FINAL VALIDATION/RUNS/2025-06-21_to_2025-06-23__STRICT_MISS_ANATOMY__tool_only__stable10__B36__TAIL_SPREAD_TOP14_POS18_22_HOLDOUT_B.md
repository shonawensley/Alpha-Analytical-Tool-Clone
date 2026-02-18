# Strict Miss Anatomy — 2025-06-21..2025-06-23

Source: conversion ladder CSVs (grade-output driven).

Budget: `B36` | Profile: `tool_only` | Experiment tag: `stable10`

Interpretation:
- `lane_retained_rate` answers: “did the B36 Play Card touch the winner lane at all?”
- `strict_given_lane_retained` answers: “once we retained the lane, did we convert to strict?”
- `strict_miss_lane_*_share` answers: “when strict misses happen, are they mostly lane drops or within-lane misses?”

## B36

| strategy | outcomes | strict_hit | strict_miss | lane_retained_rate | strict_given_lane_retained | strict_miss_lane_dropped_share | strict_miss_lane_retained_share |
|---|---:|---:|---:|---:|---:|---:|---:|
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first` | 81 | 2 | 79 | 51.9% | 4.8% | 49.4% | 50.6% |
| `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22` | 81 | 2 | 79 | 54.3% | 4.5% | 46.8% | 53.2% |
