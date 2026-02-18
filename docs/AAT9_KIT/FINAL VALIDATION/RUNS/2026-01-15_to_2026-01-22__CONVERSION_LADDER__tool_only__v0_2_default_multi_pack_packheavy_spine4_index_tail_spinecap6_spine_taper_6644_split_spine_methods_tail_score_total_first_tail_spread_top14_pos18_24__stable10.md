# Conversion Ladder — 2026-01-15..2026-01-22

Purpose: make the break explicit across the predictive substrate:
- Candidate Universe (`__UNION__` row) = what the system *could* play (unbounded).
- Play Card = what we *would* play under a fixed budget (B12/B24/B36).

Notes (critical):
- Always filter out `winner_missing=1` rows when interpreting hit rates.
- This report is grade-output driven; it does not read sharepacks directly.

## Coverage
- Requested range: `2026-01-15..2026-01-22`
- Included dates (grade files present): `2026-01-15, 2026-01-16, 2026-01-17, 2026-01-18, 2026-01-20, 2026-01-21, 2026-01-22`
- Excluded dates (missing grades): `2026-01-19`

## Summary (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_24`)
- Rows in CSV: `196` (known winners: `193`; censored: `3`)

### Candidate Universe (`__UNION__`) recall (per outcome)
- outcomes: `193`
- CU union hit_any: `27.5%`
- CU union box_hit: `27.5%`
- CU union straight_hit: `20.7%`
- CU union vtrac_index_hit: `78.8%`

### Play Card conversion (per budget; `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_24`)
| Budget | rows | hit_any | hit_any_inclusive | box_hit | straight_hit | vtrac_index_hit | pack_box_hit | pack_straight_hit | pack_correct | pack_any_correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B36 | 193 | 4.7% | 61.7% | 0.0% | 4.7% | 61.7% | 21.8% | 4.7% | 1.6% | 61.7% |

### Conditional conversion (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_24`)
- `P(play_hit_any_inclusive | CU_vtrac_index_hit)` answers: when CU touches the winner lane, how often does the budgeted card retain it?
- `P(play_hit_any_inclusive | CU_hit_any)` answers: when CU contains the exact winner (box/straight), how often does the budgeted card keep it?

| Budget | P(play_hit_any_inclusive) | P(play_hit_any_inclusive \| CU_vtrac_index_hit) | P(play_hit_any_inclusive \| CU_hit_any) |
|---|---:|---:|---:|
| B36 | 61.7% | 78.3% | 94.3% |

### Inclusive hit attribution (pack vs filler)
- `pack_hit_any_inclusive` / `filler_hit_any_inclusive` are already emitted by the play-card grader.
- If most inclusive hits come from `filler`, the chosen VTRAC pack is not doing the work we think it is.

| Budget | pack_hit_any_inclusive | filler_hit_any_inclusive | among inclusive hits: pack share | among inclusive hits: filler share |
|---|---:|---:|---:|---:|
| B36 | 61.7% | 0.5% | 100.0% | 0.8% |

### Break buckets (per budget)
Bucket definitions (winner present only): `HIT_INCLUSIVE`, `CU_EXACT_BUT_PLAY_MISS`, `CU_LANE_BUT_PLAY_MISS`, `CU_MISS`, `NO_CU_JOIN`.

| Budget | HIT_INCLUSIVE | CU_EXACT_BUT_PLAY_MISS | CU_LANE_BUT_PLAY_MISS | CU_MISS | NO_CU_JOIN |
|---|---:|---:|---:|---:|---:|
| B36 | 119 (61.7%) | 3 (1.6%) | 30 (15.5%) | 41 (21.2%) | 0 (0.0%) |

## Output CSV
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_24__stable10.csv`
