# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-06

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `3cc9b8a0b0e36f76`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 244, 468, 478, 044, 229, 248 | 28, 31, 30, 15, 12, 34, 24, 18 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 2 | Delaware4 | 334, 003, 118, 445, 004, 559, 144, 449 | 5, 15, 33, 4, 13, 18, 1, 32 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 334, 033, 346, 344, 445, 336, 224, 244 | 24, 33, 13, 15, 23, 34, 31, 10 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 4 | Indiana4 | 244, 366, 066, 006, 138, 014, 003, 225 | 31, 18, 6, 23, 12, 8, 10, 9 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 118, 144, 668, 156, 135, 013, 011, 066 | 18, 6, 25, 8, 2, 17, 35, 23 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 6 | NewJersey4 | 778, 088, 788, 889, 188, 189, 148, 078 | 27, 13, 24, 33, 4, 11, 23, 29 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 008, 005, 025, 066, 056, 001, 255, 224 | 6, 3, 4, 2, 1, 18, 17, 33 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 224, 229, 299, 044, 019, 244, 029 | 28, 31, 15, 9, 12, 25, 5, 26 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 088, 008, 559, 009, 229, 299, 029 | 5, 13, 10, 12, 4, 28, 1, 3 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 014, 015, 177, 459, 244, 477, 124 | 20, 28, 15, 9, 2, 22, 31, 5 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 059, 559, 455, 000, 012, 009, 177, 001 | 5, 15, 2, 9, 3, 20, 7, 23 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 068, 003, 006, 268, 688, 244 | 4, 31, 21, 8, 12, 23, 2, 10 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 13 | SouthCarolina4 | 007, 599, 667, 005, 669, 566, 677, 399 | 17, 20, 3, 28, 6, 15, 5, 1 | - | - | shared_host | Midday:ALERT/3, Evening:WATCH/2, Combined:OFF/1 |
| 14 | Virginia4 | 224, 559, 189, 008, 009, 377, 024, 229 | 5, 28, 12, 27, 24, 23, 4, 33 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 255 | 31 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 313 | 39 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 241 | 29 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 265 | 32 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 228 | 26 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 233 | 29 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 292 | 36 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 276 | 35 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 299 | 37 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 257 | 30 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 006, 011, 014, 017, 066, 168, 668 | 7 | 12 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 014, 017, 024, 244, 299, 447 | 6 | 11 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 003, 006, 011, 244, 299, 447 | 6 | 11 | False | True |
| Indiana4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 18, 2, 20, 23, 31, 9 | - | 7 | 11 | False | True |
| NewYork4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 12, 17, 18, 23, 3, 6 | - | 7 | 11 | False | True |
| Pennsylvania4 | Delaware4 | alert_implied_echo | lane/family | primary | 5 | 009, 045, 455, 559 | 4 | 10 | False | True |
| Pennsylvania4 | Ohio4 | alert_implied_echo | lane/family | primary | 1, 5 | 005, 009, 059, 559 | 4 | 10 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 044, 224, 229, 244, 299 | 5 | 10 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 009, 011, 014, 559 | 5 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 008, 011 | 5 | 10 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 006, 007, 566 | 5 | 10 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 224, 229 | 5 | 10 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 006, 008, 088, 299 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 059, 599 | 5 | 10 | False | True |
| Connecticut4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 31 | - | 6 | 10 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 13, 15, 23, 24, 31, 33 | - | 6 | 10 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 6 | - | 6 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 31 | - | 6 | 10 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 20, 23, 6 | - | 6 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 4 | - | 6 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 28, 31, 9 | - | 6 | 10 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 2, 20, 23, 9 | - | 6 | 10 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 15, 18, 20, 23, 28 | - | 6 | 10 | False | True |
| NewYork4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 4, 1 | 003, 005, 008 | 3 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 1, 5 | 005, 009, 059 | 3 | 9 | False | True |
| PuertoRico4 | Indiana4 | alert_implied_echo | lane/family | primary | 4, 6 | 003, 011, 066 | 3 | 9 | False | True |
| PuertoRico4 | NewYork4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 014, 017, 224, 244 | 4 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 024, 224, 229 | 4 | 9 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 014, 044, 118 | 4 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 009, 445, 455, 559 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 244 | 4 | 9 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 066 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017 | 4 | 9 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 008, 011 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 229, 299 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 559 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 009, 059 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 008, 009, 229, 559 | 4 | 9 | False | True |
| Connecticut4 | Florida4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 31 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `NewYork4 ↔ PuertoRico4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ PuertoRico4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ OntarioCanada4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ NorthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
