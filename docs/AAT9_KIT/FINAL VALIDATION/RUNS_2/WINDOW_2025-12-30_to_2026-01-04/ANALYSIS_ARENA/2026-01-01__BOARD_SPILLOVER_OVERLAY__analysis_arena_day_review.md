# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-01

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `6fcec45d5ae2a060`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 011, 388, 368, 001, 008, 559, 249, 003 | 4, 23, 32, 5, 14, 31, 6, 15 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 244, 014, 144, 449, 499, 114, 117 | 35, 31, 25, 9, 19, 15, 28, 17 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 599, 138, 559, 778, 077, 368, 133, 466 | 23, 15, 10, 32, 5, 19, 18, 27 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 677, 244, 668, 368, 144, 056, 017 | 20, 18, 23, 31, 16, 6, 25, 21 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 006, 133, 599, 025, 244, 299, 002 | 2, 23, 3, 9, 8, 31, 15, 17 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 6 | NewJersey4 | 299, 778, 118, 599, 899, 289, 128 | 31, 30, 18, 27, 28, 15, 34, 21 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 7 | NewYork4 | 778, 677, 678, 478, 667, 789, 016 | 30, 27, 31, 6, 17, 18, 20, 10 | - | - | shared_host | Midday:ALERT/3, Evening:ALERT/3, Combined:WATCH/2 |
| 8 | NorthCarolina4 | 224, 003, 223, 005, 229, 055, 004 | 28, 4, 1, 5, 27, 12, 14, 3 | - | - | shared_host | Evening:ALERT/4, Combined:ALERT/3, Midday:OFF/1 |
| 9 | Ohio4 | 055, 559, 068, 009, 224, 255, 007, 099 | 1, 5, 3, 8, 2, 15, 28, 31 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 10 | OntarioCanada4 | 114, 022, 255, 188, 118, 225, 224, 148 | 10, 19, 21, 3, 18, 23, 27, 4 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 359, 339, 138, 113, 599, 133 | 5, 23, 18, 33, 14, 15, 29, 21 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 344, 113, 224, 002, 001, 226, 134, 244 | 24, 34, 18, 31, 28, 10, 12, 3 | - | - | shared_host | Evening:OFF/1, Combined:OFF/0, Midday:OFF/0 |
| 13 | SouthCarolina4 | 118, 011, 138, 189, 068, 008, 006 | 18, 23, 6, 8, 4, 24, 5, 2 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 224, 177, 133, 137, 113, 477, 244, 334 | 28, 20, 23, 18, 31, 22, 7, 33 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 280 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 229 | 27 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 292 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 236 | 30 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 281 | 35 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 245 | 28 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 241 | 31 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 197 | 25 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 224 | 28 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 165 | 20 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 011, 017, 113, 133, 138, 336, 559, 599 | 8 | 13 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 006, 009, 058, 355 | 6 | 11 | False | True |
| Virginia4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 18 | 113, 118, 168, 366 | 4 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 006, 008, 009, 011 | 5 | 10 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 017, 044, 249, 299 | 5 | 10 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 006, 009, 055, 224 | 5 | 10 | False | True |
| Michigan4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 3, 8 | - | 6 | 10 | False | True |
| Michigan4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 3, 31 | - | 6 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 31, 34 | - | 6 | 10 | False | True |
| NewYork4 | Virginia4 | shared_lane | lane/family | primary | 17, 18, 20, 21, 28, 31 | - | 6 | 10 | False | True |
| Ohio4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 28, 3 | - | 6 | 10 | False | True |
| SouthCarolina4 | Connecticut4 | alert_implied_echo | lane/family | primary | 4 | 003, 008, 058 | 3 | 9 | False | True |
| SouthCarolina4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 4 | 003, 035, 058 | 3 | 9 | False | True |
| Virginia4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 18, 28 | 113, 136, 224 | 3 | 9 | False | True |
| Connecticut4 | Florida4 | shared_box_family | lane/family | primary | - | 011, 368, 559, 688 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 017, 144, 244 | 4 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 044 | 4 | 9 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 017, 599, 778 | 4 | 9 | False | True |
| Florida4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 011, 113, 138, 188 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 006, 013, 056, 244 | 4 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 248, 249, 478, 778 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 009, 057, 059, 559 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 068 | 4 | 9 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 113 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 009, 011, 113, 138 | 4 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_lane | lane/family | primary | 14, 18, 23, 33, 5 | - | 5 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 20, 23, 5 | - | 5 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 18, 2, 20, 23, 31 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 17, 18, 20, 23, 31 | - | 5 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_lane | lane/family | primary | 18, 27, 28, 30, 31 | - | 5 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_lane | lane/family | primary | 1, 15, 23, 28, 5 | - | 5 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_lane | lane/family | primary | 17, 18, 19, 21, 23 | - | 5 | 9 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 18, 20, 23, 28, 31 | - | 5 | 9 | False | True |
| Connecticut4 | Delaware4 | alert_implied_echo | lane/family | primary | 6, 31 | 011, 249 | 2 | 8 | False | True |
| Connecticut4 | Florida4 | alert_implied_echo | lane/family | primary | 6, 23 | 011, 368 | 2 | 8 | False | True |
| Connecticut4 | Indiana4 | alert_implied_echo | lane/family | primary | 6, 23 | 011, 368 | 2 | 8 | False | True |
| Connecticut4 | NewJersey4 | alert_implied_echo | lane/family | primary | 6, 31 | 011, 249 | 2 | 8 | False | True |
| Connecticut4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 4, 6 | 008, 011 | 2 | 8 | False | True |
| Michigan4 | Connecticut4 | alert_implied_echo | lane/family | primary | 2 | 001, 006 | 2 | 8 | False | True |
| Michigan4 | Indiana4 | alert_implied_echo | lane/family | primary | 2 | 006, 056 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ NewYork4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Florida4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Pennsylvania4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ SouthCarolina4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
