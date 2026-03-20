# Aggregated Arena Bridge Family Casepack

- Purpose: inspect bridge families as concrete state/day rows instead of only aggregate scoreboards.
- Rule analyzed: `top4_perm`
- Families: `aux_overdue+aux_badge, due_doubles+aux_badge, profit_alert+aux_badge`

## `aux_overdue+aux_badge`

- Rows: `8`
- Resolution profile: `3` direct, `1` same-day precursor+same-day, `1` carry-forward, `0` future-day decay, `3` miss

| window | date | state | outcome | gap_detail | vt_rank | box_profile | first_box_event | watch_items | watch_canonicals | baseline_literal |
|---|---|---|---|---|---:|---|---|---:|---:|---:|
| 2025-12-30_to_2026-01-04 | 2025-12-30 | Florida4 | Midday | lane_alive_literal_missing_front3 | 3 | miss | - | 4 | 11 | 0 |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Evening | lane_alive_literal_missing_front3 | 3 | direct_same_outcome | 2025-12-31 Evening 636 | 4 | 16 | 0 |
| 2025-12-30_to_2026-01-04 | 2025-12-31 | Virginia4 | Midday | lane_alive_literal_missing_front3 | 3 | same_day_carryforward | 2025-12-31 Evening 636 | 4 | 16 | 0 |
| 2026-01-05_to_2026-01-09 | 2026-01-08 | NewJersey4 | Evening | lane_alive_literal_missing_front3 | 3 | same_day_precursor_plus_same_day | 2026-01-08 Midday 089 | 4 | 9 | 0 |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | Delaware4 | Midday | lane_alive_literal_missing_front5 | 4 | direct_same_outcome | 2026-01-09 Midday 843 | 4 | 13 | 0 |
| 2026-01-05_to_2026-01-09 | 2026-01-09 | NewJersey4 | Midday | lane_alive_literal_missing_front3 | 3 | miss | - | 4 | 11 | 0 |
| 2026-01-18_to_2026-01-20 | 2026-01-18 | Delaware4 | Midday | lane_alive_literal_missing_front3 | 3 | direct_same_outcome | 2026-01-18 Midday 490 | 4 | 17 | 0 |
| 2026-01-21_to_2026-01-22 | 2026-01-22 | Indiana4 | Midday | lane_alive_literal_missing_front3 | 1 | miss | - | 4 | 8 | 0 |

## `due_doubles+aux_badge`

- Rows: `2`
- Resolution profile: `1` direct, `0` same-day precursor+same-day, `0` carry-forward, `1` future-day decay, `0` miss

| window | date | state | outcome | gap_detail | vt_rank | box_profile | first_box_event | watch_items | watch_canonicals | baseline_literal |
|---|---|---|---|---|---:|---|---|---:|---:|---:|
| 2026-01-15_to_2026-01-17 | 2026-01-15 | Indiana4 | Evening | lane_alive_literal_missing_front3 | 1 | future_day_decay | 2026-01-16 Midday 954 | 4 | 14 | 0 |
| 2026-01-15_to_2026-01-17 | 2026-01-15 | Michigan4 | Evening | lane_alive_literal_missing_front3 | 3 | direct_same_outcome | 2026-01-15 Evening 664 | 4 | 11 | 0 |

## `profit_alert+aux_badge`

- Rows: `3`
- Resolution profile: `1` direct, `0` same-day precursor+same-day, `0` carry-forward, `1` future-day decay, `1` miss

| window | date | state | outcome | gap_detail | vt_rank | box_profile | first_box_event | watch_items | watch_canonicals | baseline_literal |
|---|---|---|---|---|---:|---|---|---:|---:|---:|
| 2026-01-15_to_2026-01-17 | 2026-01-15 | OntarioCanada4 | Midday | lane_alive_literal_missing_front3 | 3 | future_day_decay | 2026-01-16 Evening 390 | 4 | 15 | 0 |
| 2026-01-15_to_2026-01-17 | 2026-01-16 | Florida4 | Midday | lane_alive_literal_missing_front3 | 2 | direct_same_outcome | 2026-01-16 Midday 273 | 4 | 15 | 0 |
| 2026-01-21_to_2026-01-22 | 2026-01-21 | Delaware4 | Midday | lane_alive_literal_missing_front5 | 5 | miss | - | 4 | 11 | 0 |

