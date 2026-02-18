# Conversion Ladder — 2026-01-01..2026-01-09

Purpose: make the break explicit across the predictive substrate:
- Candidate Universe (`__UNION__` row) = what the system *could* play (unbounded).
- Play Card = what we *would* play under a fixed budget (B12/B24/B36).

Notes (critical):
- Always filter out `winner_missing=1` rows when interpreting hit rates.
- This report is grade-output driven; it does not read sharepacks directly.

## Coverage
- Requested range: `2026-01-01..2026-01-09`
- Included dates (grade files present): `2026-01-01, 2026-01-02, 2026-01-03, 2026-01-04, 2026-01-05, 2026-01-06, 2026-01-07, 2026-01-08, 2026-01-09`

## Summary (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first`)
- Rows in CSV: `252` (known winners: `245`; censored: `7`)

### Candidate Universe (`__UNION__`) recall (per outcome)
- outcomes: `245`
- CU union hit_any: `25.7%`
- CU union box_hit: `25.7%`
- CU union straight_hit: `20.4%`
- CU union vtrac_index_hit: `71.0%`

### Play Card conversion (per budget; `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first`)
| Budget | rows | hit_any | hit_any_inclusive | box_hit | straight_hit | vtrac_index_hit | pack_box_hit | pack_straight_hit | pack_correct | pack_any_correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B36 | 245 | 3.7% | 55.5% | 0.0% | 3.7% | 55.5% | 12.2% | 3.7% | 3.3% | 55.5% |

### Conditional conversion (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first`)
- `P(play_hit_any_inclusive | CU_vtrac_index_hit)` answers: when CU touches the winner lane, how often does the budgeted card retain it?
- `P(play_hit_any_inclusive | CU_hit_any)` answers: when CU contains the exact winner (box/straight), how often does the budgeted card keep it?

| Budget | P(play_hit_any_inclusive) | P(play_hit_any_inclusive \| CU_vtrac_index_hit) | P(play_hit_any_inclusive \| CU_hit_any) |
|---|---:|---:|---:|
| B36 | 55.5% | 78.2% | 92.1% |

### Inclusive hit attribution (pack vs filler)
- `pack_hit_any_inclusive` / `filler_hit_any_inclusive` are already emitted by the play-card grader.
- If most inclusive hits come from `filler`, the chosen VTRAC pack is not doing the work we think it is.

| Budget | pack_hit_any_inclusive | filler_hit_any_inclusive | among inclusive hits: pack share | among inclusive hits: filler share |
|---|---:|---:|---:|---:|
| B36 | 55.5% | 0.0% | 100.0% | 0.0% |

### Break buckets (per budget)
Bucket definitions (winner present only): `HIT_INCLUSIVE`, `CU_EXACT_BUT_PLAY_MISS`, `CU_LANE_BUT_PLAY_MISS`, `CU_MISS`, `NO_CU_JOIN`.

| Budget | HIT_INCLUSIVE | CU_EXACT_BUT_PLAY_MISS | CU_LANE_BUT_PLAY_MISS | CU_MISS | NO_CU_JOIN |
|---|---:|---:|---:|---:|---:|
| B36 | 136 (55.5%) | 5 (2.0%) | 33 (13.5%) | 71 (29.0%) | 0 (0.0%) |

## Output CSV
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first__stable10.csv`
