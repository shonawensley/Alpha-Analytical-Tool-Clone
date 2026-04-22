# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-15

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `07dc79d634a44104`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 899, 599, 559, 089, 359, 589, 299 | 34, 14, 15, 5, 31, 33, 30, 25 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 2 | Delaware4 | 059, 249, 299, 009, 599, 559, 013, 079 | 5, 31, 15, 12, 9, 1, 8, 3 | - | - | shared_host | Evening:ALERT/3, Combined:OFF/1, Midday:OFF/0 |
| 3 | Florida4 | 177, 577, 224, 225, 255, 178, 778 | 10, 20, 27, 28, 3, 11, 21, 33 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 4 | Indiana4 | 599, 339, 667, 368, 038, 336, 338, 066 | 15, 23, 33, 6, 17, 18, 5, 13 | - | - | shared_host | Combined:ALERT/4, Evening:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 114, 344, 014, 055, 015, 559, 144, 113 | 9, 2, 19, 1, 5, 34, 15, 6 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 6 | NewJersey4 | 001, 136, 179, 449, 119, 016, 499, 019 | 18, 2, 35, 25, 6, 22, 9, 34 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 7 | NewYork4 | 677, 377, 337, 336, 001, 334, 009, 017 | 23, 20, 29, 27, 12, 28, 2, 15 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 224, 344, 255, 000, 225, 445, 004, 025 | 5, 28, 3, 34, 15, 31, 25, 27 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 599, 039, 559, 334, 368, 009, 459 | 15, 5, 14, 33, 23, 34, 13, 10 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 225, 039, 049, 022, 003, 559, 002, 255 | 10, 15, 14, 5, 3, 7, 4, 6 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:OFF/1 |
| 11 | Pennsylvania4 | 244, 446, 234, 239, 388, 688, 889, 224 | 31, 30, 25, 33, 32, 23, 34, 28 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 088, 004, 034, 003, 334, 033, 013, 138 | 13, 23, 33, 8, 4, 5, 14, 12 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 13 | SouthCarolina4 | 449, 678, 004, 344, 499, 467, 068, 014 | 35, 5, 15, 8, 21, 28, 17, 18 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 14 | Virginia4 | 449, 599, 459, 033, 005, 559, 335, 059 | 15, 35, 13, 5, 25, 1, 31, 11 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 211 | 26 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 331 | 41 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 107 | 12 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 254 | 30 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 259 | 29 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 273 | 33 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 299 | 38 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 310 | 39 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 292 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 334 | 38 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 013, 014, 059, 559, 599 | 6 | 11 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 007, 009, 336, 368 | 6 | 11 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 099, 368, 459, 599 | 6 | 11 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 009, 225, 255, 445, 559 | 6 | 11 | False | True |
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 009, 039, 049, 459, 559 | 6 | 11 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 14, 15, 18, 23, 33, 4, 5 | - | 7 | 11 | False | True |
| Delaware4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045, 059 | 4 | 10 | False | True |
| SouthCarolina4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045, 059 | 4 | 10 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 559, 599 | 5 | 10 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 244, 249, 299 | 5 | 10 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017, 449 | 5 | 10 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 059, 344, 455, 559 | 5 | 10 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 059, 449, 499, 559 | 5 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 15, 18, 23, 3, 5 | - | 6 | 10 | False | True |
| Delaware4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 15 | 004, 009, 599 | 3 | 9 | False | True |
| Michigan4 | NewJersey4 | alert_implied_echo | lane/family | primary | 8, 9 | 013, 014, 018 | 3 | 9 | False | True |
| NewJersey4 | Michigan4 | alert_implied_echo | lane/family | primary | 2 | 001, 015, 056 | 3 | 9 | False | True |
| NewJersey4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 2, 1 | 001, 005, 006 | 3 | 9 | False | True |
| NewYork4 | Indiana4 | alert_implied_echo | lane/family | primary | 2, 5 | 001, 006, 009 | 3 | 9 | False | True |
| NewYork4 | Michigan4 | alert_implied_echo | lane/family | primary | 2 | 001, 015, 056 | 3 | 9 | False | True |
| SouthCarolina4 | Delaware4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| SouthCarolina4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 15 | 004, 009, 049 | 3 | 9 | False | True |
| SouthCarolina4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 5, 15 | 004, 009, 049 | 3 | 9 | False | True |
| Virginia4 | Delaware4 | alert_implied_echo | lane/family | primary | 1, 5, 15 | 005, 059, 599 | 3 | 9 | False | True |
| Virginia4 | Ohio4 | alert_implied_echo | lane/family | primary | 1, 15 | 005, 459, 599 | 3 | 9 | False | True |
| Delaware4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 059, 559 | 4 | 9 | False | True |
| Delaware4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 559 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 014, 059, 559 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 688 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 011, 044, 559 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 014, 044, 344, 559 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 334, 368 | 4 | 9 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 006, 138, 334 | 4 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 334 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 049, 559 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 459, 559, 599 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 044, 049, 559 | 4 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 445, 459, 559 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 044 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 14, 15, 23, 33, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `NorthCarolina4 ↔ SouthCarolina4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewJersey4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ OntarioCanada4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ OntarioCanada4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ SouthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NorthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
