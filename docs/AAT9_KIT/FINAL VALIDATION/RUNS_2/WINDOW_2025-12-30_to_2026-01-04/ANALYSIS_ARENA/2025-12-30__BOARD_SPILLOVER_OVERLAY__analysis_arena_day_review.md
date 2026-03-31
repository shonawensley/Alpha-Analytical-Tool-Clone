# Board Spillover Overlay — analysis_arena_day_review — D=2025-12-30

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `1ea0bd3c2493e73c`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 559, 011, 000, 039, 006, 117, 005, 001 | 5, 2, 6, 15, 17, 14, 1, 18 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 2 | Delaware4 | 344, 113, 244, 147, 499, 144, 017, 044 | 31, 22, 34, 35, 28, 18, 15, 25 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/0 |
| 3 | Florida4 | 778, 177, 677, 133, 077, 678, 137, 037 | 20, 10, 23, 27, 21, 11, 12, 32 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 4 | Indiana4 | 066, 116, 068, 668, 225, 259, 677 | 6, 16, 18, 20, 8, 10, 19, 9 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 599, 244, 136, 255, 355, 002, 155, 366 | 18, 15, 3, 23, 7, 8, 6, 2 | - | - | shared_host | Evening:WATCH/2, Midday:OFF/1, Combined:OFF/0 |
| 6 | NewJersey4 | 224, 118, 299, 012, 229, 289, 899 | 28, 18, 31, 30, 7, 5, 1, 27 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 016, 778, 677, 116, 224, 229, 277, 338 | 6, 17, 28, 20, 10, 26, 16, 27 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 8 | NorthCarolina4 | 224, 003, 005, 004, 034, 024, 055 | 1, 28, 5, 4, 3, 2, 15, 12 | - | - | shared_host | Evening:ALERT/4, Combined:ALERT/3, Midday:OFF/1 |
| 9 | Ohio4 | 677, 057, 599, 077, 699, 067, 009, 007 | 3, 7, 15, 20, 10, 5, 25, 2 | - | - | shared_host | Combined:ALERT/3, Midday:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 188, 225, 114, 022, 255, 228, 226, 126 | 23, 10, 20, 17, 19, 31, 21, 27 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 11 | Pennsylvania4 | 339, 113, 138, 133, 338, 559 | 23, 33, 18, 32, 29, 21, 13, 5 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 344, 134, 244, 113, 299, 246, 229, 345 | 34, 31, 14, 24, 22, 18, 28, 5 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 13 | SouthCarolina4 | 189, 599, 009, 066, 017, 006, 389, 056 | 24, 5, 15, 6, 2, 33, 23, 21 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 14 | Virginia4 | 399, 133, 177, 117, 113, 119, 136 | 23, 20, 34, 18, 17, 28, 19, 27 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 299 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 298 | 38 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 245 | 31 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 256 | 28 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 281 | 35 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 239 | 31 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 241 | 26 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 145 | 18 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 213 | 27 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 241 | 29 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 014, 044, 113, 244, 299, 344, 447 | 7 | 12 | False | True |
| Connecticut4 | Indiana4 | alert_implied_echo | lane/family | primary | 6, 7 | 011, 016, 017, 066 | 4 | 10 | False | True |
| Delaware4 | Michigan4 | alert_implied_echo | lane/family | primary | 18 | 113, 118, 136, 168 | 4 | 10 | False | True |
| Pennsylvania4 | Michigan4 | alert_implied_echo | lane/family | primary | 18 | 113, 118, 136, 168 | 4 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 011, 017, 455 | 5 | 10 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 017, 113, 244, 299 | 5 | 10 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 007, 677, 778 | 5 | 10 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 007, 017, 077, 677 | 5 | 10 | False | True |
| Florida4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 017, 022, 077, 133, 225 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 011, 113, 118, 244 | 5 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 224, 229 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 017, 057, 599 | 5 | 10 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 12, 15, 17, 18, 23, 6 | - | 6 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 5, 6 | - | 6 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 22, 23, 31, 34 | - | 6 | 10 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 10, 16, 17, 18, 20, 6 | - | 6 | 10 | False | True |
| Indiana4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 12, 17, 18, 20, 23 | - | 6 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 6, 7 | 011, 017, 066 | 3 | 9 | False | True |
| Delaware4 | NewJersey4 | alert_implied_echo | lane/family | primary | 7, 18 | 017, 113, 118 | 3 | 9 | False | True |
| Delaware4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 7, 18 | 017, 113, 118 | 3 | 9 | False | True |
| Virginia4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 23 | 133, 138, 188 | 3 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 004, 006, 011, 017 | 4 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 455 | 4 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 113 | 4 | 9 | False | True |
| Florida4 | Indiana4 | shared_box_family | lane/family | primary | - | 006, 017, 225, 677 | 4 | 9 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 016, 116, 677 | 4 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 011, 017, 066 | 4 | 9 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 005, 006, 566 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 677 | 4 | 9 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 017, 113, 133, 188 | 4 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 12, 14, 15, 23, 5 | - | 5 | 9 | False | True |
| Florida4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 18, 20, 23, 27 | - | 5 | 9 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 10, 12, 15, 20, 23 | - | 5 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_lane | lane/family | primary | 1, 15, 23, 3, 4 | - | 5 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 7 | - | 5 | 9 | False | True |
| NewYork4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 17, 18, 20, 27 | - | 5 | 9 | False | True |
| Ohio4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 12, 20, 23, 3 | - | 5 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_lane | lane/family | primary | 17, 18, 19, 20, 23 | - | 5 | 9 | False | True |
| Connecticut4 | Delaware4 | alert_implied_echo | lane/family | primary | 6, 7 | 011, 017 | 2 | 8 | False | True |
| Connecticut4 | NewJersey4 | alert_implied_echo | lane/family | primary | 6, 7 | 011, 017 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ PuertoRico4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
