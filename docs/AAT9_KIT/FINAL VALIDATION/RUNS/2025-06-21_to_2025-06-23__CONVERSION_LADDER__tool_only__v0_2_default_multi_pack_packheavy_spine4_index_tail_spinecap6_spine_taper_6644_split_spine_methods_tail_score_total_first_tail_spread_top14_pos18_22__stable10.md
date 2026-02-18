# Conversion Ladder — 2025-06-21..2025-06-23

Purpose: make the break explicit across the predictive substrate:
- Candidate Universe (`__UNION__` row) = what the system *could* play (unbounded).
- Play Card = what we *would* play under a fixed budget (B12/B24/B36).

Notes (critical):
- Always filter out `winner_missing=1` rows when interpreting hit rates.
- This report is grade-output driven; it does not read sharepacks directly.

## Coverage
- Requested range: `2025-06-21..2025-06-23`
- Included dates (grade files present): `2025-06-21, 2025-06-22, 2025-06-23`

## Summary (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`)
- Rows in CSV: `84` (known winners: `81`; censored: `3`)

### Candidate Universe (`__UNION__`) recall (per outcome)
- outcomes: `81`
- CU union hit_any: `28.4%`
- CU union box_hit: `28.4%`
- CU union straight_hit: `21.0%`
- CU union vtrac_index_hit: `65.4%`

### Play Card conversion (per budget; `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`)
| Budget | rows | hit_any | hit_any_inclusive | box_hit | straight_hit | vtrac_index_hit | pack_box_hit | pack_straight_hit | pack_correct | pack_any_correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B36 | 81 | 2.5% | 54.3% | 0.0% | 2.5% | 54.3% | 12.3% | 2.5% | 1.2% | 54.3% |

### Conditional conversion (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`)
- `P(play_hit_any_inclusive | CU_vtrac_index_hit)` answers: when CU touches the winner lane, how often does the budgeted card retain it?
- `P(play_hit_any_inclusive | CU_hit_any)` answers: when CU contains the exact winner (box/straight), how often does the budgeted card keep it?

| Budget | P(play_hit_any_inclusive) | P(play_hit_any_inclusive \| CU_vtrac_index_hit) | P(play_hit_any_inclusive \| CU_hit_any) |
|---|---:|---:|---:|
| B36 | 54.3% | 83.0% | 95.7% |

### Inclusive hit attribution (pack vs filler)
- `pack_hit_any_inclusive` / `filler_hit_any_inclusive` are already emitted by the play-card grader.
- If most inclusive hits come from `filler`, the chosen VTRAC pack is not doing the work we think it is.

| Budget | pack_hit_any_inclusive | filler_hit_any_inclusive | among inclusive hits: pack share | among inclusive hits: filler share |
|---|---:|---:|---:|---:|
| B36 | 54.3% | 0.0% | 100.0% | 0.0% |

### Break buckets (per budget)
Bucket definitions (winner present only): `HIT_INCLUSIVE`, `CU_EXACT_BUT_PLAY_MISS`, `CU_LANE_BUT_PLAY_MISS`, `CU_MISS`, `NO_CU_JOIN`.

| Budget | HIT_INCLUSIVE | CU_EXACT_BUT_PLAY_MISS | CU_LANE_BUT_PLAY_MISS | CU_MISS | NO_CU_JOIN |
|---|---:|---:|---:|---:|---:|
| B36 | 44 (54.3%) | 1 (1.2%) | 8 (9.9%) | 28 (34.6%) | 0 (0.0%) |

## Output CSV
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22__stable10.csv`
