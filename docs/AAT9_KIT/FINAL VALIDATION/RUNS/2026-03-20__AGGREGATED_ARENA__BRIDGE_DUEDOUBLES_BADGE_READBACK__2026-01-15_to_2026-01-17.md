# Aggregated Arena Bridge Corpus Readback

- Purpose: combine bridge-study rows across measured windows, then split one repeated cohort into same-day, decay-only, and miss cases before any promotion decision.
- Rule analyzed: `top4_perm`
- Focus source mix: `due_doubles+aux_badge`
- summary_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_DUEDOUBLES_BADGE_SUMMARY__2026-01-15_to_2026-01-17.csv`
- focus_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_DUEDOUBLES_BADGE_FOCUS__2026-01-15_to_2026-01-17.csv`
- gated_focus_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_DUEDOUBLES_BADGE_GATED__2026-01-15_to_2026-01-17.csv`
- total selected rows: `6`
- focus rows: `2`
- gated focus rows: `2`

## Source Mix Summary

| source_mix | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| due_doubles+aux_badge | 2 | 1/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | 2 | 1/2 | 1/2 | 0/2 |
| profit_alert+due_doubles+aux_overdue+aux_badge | 2 | 0/2 | 1/2 | 1/2 |

## Focus Cohort Split By Window

| window | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2 | 1/2 | 1/2 | 0/2 |

## Focus Cohort Split By Reviewed Outcome

| outcome | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| Evening | 2 | 1/2 | 1/2 | 0/2 |

## Focus Cohort Split By Gap Detail

| gap_detail | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| lane_alive_literal_missing_front3 | 2 | 1/2 | 1/2 | 0/2 |

## Focus Cohort Split By VTRAC Rank Band

| arena_vtrac_rank_band | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| front3 | 2 | 1/2 | 1/2 | 0/2 |

## Focus Cohort Split By Watchlist Band

| watchlist_band | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| large | 1 | 0/1 | 1/1 | 0/1 |
| medium | 1 | 1/1 | 0/1 | 0/1 |

## Focus Cohort Split By Box Resolution Profile

| box_resolution_profile | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| direct_same_outcome | 1 | 1/1 | 0/1 | 0/1 |
| future_day_decay | 1 | 0/1 | 1/1 | 0/1 |

## Focus Cohort Rows

| window | date | state_key | outcome | winner | gap_detail | arena_vtrac_rank | arena_vtrac_rank_band | watchlist_canonical_count | watchlist_band | box_resolution_profile | same_day_box_hit | within_3d_box_hit | first_box_event | outcome_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2026-01-15 | Indiana4 | Evening | 094 | lane_alive_literal_missing_front3 | 1 | front3 | 14 | large | future_day_decay | 0 | 1 | 2026-01-16 Midday 954 | decay_only |
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2026-01-15 | Michigan4 | Evening | 664 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | direct_same_outcome | 1 | 1 | 2026-01-15 Evening 664 | same_day |

## Gated Focus Cohort

- gap_details: `lane_alive_literal_missing_front3, lane_alive_literal_missing_front5 `
- max_vtrac_rank: `5`

| window | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2 | 1/2 | 1/2 | 0/2 |

## Gated Focus Rows

| window | date | state_key | outcome | winner | gap_detail | arena_vtrac_rank | arena_vtrac_rank_band | watchlist_canonical_count | watchlist_band | box_resolution_profile | same_day_box_hit | within_3d_box_hit | first_box_event | outcome_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2026-01-15 | Indiana4 | Evening | 094 | lane_alive_literal_missing_front3 | 1 | front3 | 14 | large | future_day_decay | 0 | 1 | 2026-01-16 Midday 954 | decay_only |
| 2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS | 2026-01-15 | Michigan4 | Evening | 664 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | direct_same_outcome | 1 | 1 | 2026-01-15 Evening 664 | same_day |

## Notes

- `same_day` means the bridge candidate set already boxed or hit the reviewed winner on the same outcome row.
- `decay_only` means the same frozen bridge candidate set did not close same-day but did resolve within the next 3 days.
- `miss` means no bridge closure within the measured horizon.
