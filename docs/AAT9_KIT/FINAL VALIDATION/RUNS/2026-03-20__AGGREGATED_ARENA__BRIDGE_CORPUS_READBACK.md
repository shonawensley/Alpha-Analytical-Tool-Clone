# Aggregated Arena Bridge Corpus Readback

- Purpose: combine bridge-study rows across measured windows, then split one repeated cohort into same-day, decay-only, and miss cases before any promotion decision.
- Rule analyzed: `top4_perm`
- Focus source mix: `aux_overdue+aux_badge`
- summary_csv: `/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_SUMMARY.csv`
- focus_csv: `/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_FOCUS_ROWS.csv`
- gated_focus_csv: `/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_GATED_FOCUS_ROWS.csv`
- total selected rows: `14`
- focus rows: `8`
- gated focus rows: `6`

## Source Mix Summary

| source_mix | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| aux_overdue+aux_badge | 8 | 3/8 | 2/8 | 3/8 |
| due_doubles | 2 | 2/2 | 0/2 | 0/2 |
| due_doubles+aux_overdue+aux_badge | 4 | 0/4 | 0/4 | 4/4 |

## Focus Cohort Split By Window

| window | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| 2025-06-21_to_2025-06-24 | 2 | 0/2 | 1/2 | 1/2 |
| 2025-12-30_to_2026-01-04 | 3 | 1/3 | 1/3 | 1/3 |
| 2026-01-05_to_2026-01-09 | 3 | 2/3 | 0/3 | 1/3 |

## Focus Cohort Split By Gap Detail

| gap_detail | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| family_alive_literal_missing_front5 | 2 | 0/2 | 1/2 | 1/2 |
| lane_alive_literal_missing_front3 | 5 | 2/5 | 1/5 | 2/5 |
| lane_alive_literal_missing_front5 | 1 | 1/1 | 0/1 | 0/1 |

## Focus Cohort Split By VTRAC Rank Band

| arena_vtrac_rank_band | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| front3 | 5 | 2/5 | 1/5 | 2/5 |
| front5 | 1 | 1/1 | 0/1 | 0/1 |
| wider | 2 | 0/2 | 1/2 | 1/2 |

## Focus Cohort Split By Watchlist Band

| watchlist_band | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| large | 3 | 1/3 | 1/3 | 1/3 |
| medium | 4 | 1/4 | 1/4 | 2/4 |
| small | 1 | 1/1 | 0/1 | 0/1 |

## Focus Cohort Rows

| window | date | state_key | outcome | winner | gap_detail | arena_vtrac_rank | arena_vtrac_rank_band | watchlist_canonical_count | watchlist_band | same_day_box_hit | within_3d_box_hit | first_box_event | outcome_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-06-21_to_2025-06-24 | 2025-06-21 | NewJersey4 | Evening | 554 | family_alive_literal_missing_front5 | 15 | wider | 12 | medium | 0 | 1 | 2025-06-22 Evening 887 | decay_only |
| 2025-06-21_to_2025-06-24 | 2025-06-23 | Connecticut4 | Evening | 938 | family_alive_literal_missing_front5 | 10 | wider | 14 | large | 0 | 0 |  | miss |
| 2025-12-30_to_2026-01-04 | 2025-12-30 | Florida4 | Midday | 377 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | 0 | 0 |  | miss |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Evening | 636 | lane_alive_literal_missing_front3 | 3 | front3 | 16 | large | 1 | 1 | 2025-12-31 Evening 636 | same_day |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Midday | 686 | lane_alive_literal_missing_front3 | 3 | front3 | 16 | large | 0 | 1 | 2025-12-31 Evening 636 | decay_only |
| 2026-01-05_to_2026-01-09 | 2026-01-08 | NewJersey4 | Evening | 055 | lane_alive_literal_missing_front3 | 3 | front3 | 9 | small | 1 | 1 | 2026-01-08 Midday 089 | same_day |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | Delaware4 | Midday | 843 | lane_alive_literal_missing_front5 | 4 | front5 | 13 | medium | 1 | 1 | 2026-01-09 Midday 843 | same_day |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | NewJersey4 | Midday | 287 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | 0 | 0 |  | miss |

## Gated Focus Cohort

- gap_details: `lane_alive_literal_missing_front3, lane_alive_literal_missing_front5 `
- max_vtrac_rank: `5`

| window | rows | same_day | decay_only | miss |
|---|---|---|---|---|
| 2025-12-30_to_2026-01-04 | 3 | 1/3 | 1/3 | 1/3 |
| 2026-01-05_to_2026-01-09 | 3 | 2/3 | 0/3 | 1/3 |

## Gated Focus Rows

| window | date | state_key | outcome | winner | gap_detail | arena_vtrac_rank | arena_vtrac_rank_band | watchlist_canonical_count | watchlist_band | same_day_box_hit | within_3d_box_hit | first_box_event | outcome_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-12-30_to_2026-01-04 | 2025-12-30 | Florida4 | Midday | 377 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | 0 | 0 |  | miss |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Evening | 636 | lane_alive_literal_missing_front3 | 3 | front3 | 16 | large | 1 | 1 | 2025-12-31 Evening 636 | same_day |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Midday | 686 | lane_alive_literal_missing_front3 | 3 | front3 | 16 | large | 0 | 1 | 2025-12-31 Evening 636 | decay_only |
| 2026-01-05_to_2026-01-09 | 2026-01-08 | NewJersey4 | Evening | 055 | lane_alive_literal_missing_front3 | 3 | front3 | 9 | small | 1 | 1 | 2026-01-08 Midday 089 | same_day |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | Delaware4 | Midday | 843 | lane_alive_literal_missing_front5 | 4 | front5 | 13 | medium | 1 | 1 | 2026-01-09 Midday 843 | same_day |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | NewJersey4 | Midday | 287 | lane_alive_literal_missing_front3 | 3 | front3 | 11 | medium | 0 | 0 |  | miss |

## Notes

- `same_day` means the bridge candidate set already boxed or hit the reviewed winner on the same outcome row.
- `decay_only` means the same frozen bridge candidate set did not close same-day but did resolve within the next 3 days.
- `miss` means no bridge closure within the measured horizon.
