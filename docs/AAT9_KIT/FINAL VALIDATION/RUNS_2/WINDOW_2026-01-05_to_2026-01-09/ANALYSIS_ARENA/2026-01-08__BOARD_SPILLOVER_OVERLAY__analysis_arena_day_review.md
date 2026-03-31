# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-08

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `c73ad7ebad9fad66`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 229, 448, 248, 244, 289 | 28, 34, 30, 15, 25, 31, 24, 12 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 2 | Delaware4 | 033, 334, 003, 044, 011, 344, 034, 118 | 13, 15, 33, 4, 31, 34, 6, 14 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 3 | Florida4 | 334, 346, 335, 336, 033, 345, 134 | 33, 24, 13, 5, 23, 31, 34, 14 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 4 | Indiana4 | 244, 066, 669, 344, 045, 455, 004, 069 | 5, 31, 6, 9, 19, 34, 18, 15 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 344, 019, 144, 059, 001, 044, 015, 599 | 5, 34, 15, 9, 8, 2, 25, 35 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 6 | NewJersey4 | 778, 189, 089, 078, 007, 889, 178, 008 | 27, 4, 3, 1, 33, 24, 14, 5 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 7 | NewYork4 | 005, 008, 256, 001, 245, 255, 011, 559 | 3, 7, 6, 1, 5, 4, 2, 12 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 8 | NorthCarolina4 | 299, 244, 559, 446, 146, 006, 016 | 31, 5, 25, 19, 15, 2, 6, 28 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 9 | Ohio4 | 889, 559, 599, 299, 788, 899, 199, 088 | 33, 5, 15, 13, 14, 31, 1, 4 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 224, 015, 006, 559, 066, 014, 367, 236 | 2, 28, 21, 5, 20, 6, 9, 30 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 599, 009, 445, 113, 000, 001, 559, 244 | 15, 5, 21, 18, 9, 31, 20, 3 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 068, 006, 244, 028, 224 | 8, 31, 18, 2, 4, 5, 10, 12 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 13 | SouthCarolina4 | 599, 244, 005, 559, 059, 099, 007, 224 | 15, 5, 31, 9, 28, 35, 1, 14 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 559, 024, 244, 134, 059, 224, 229, 189 | 5, 24, 12, 31, 18, 28, 19, 23 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 226 | 29 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 306 | 36 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 196 | 24 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 285 | 34 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 359 | 42 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 237 | 28 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 290 | 36 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 305 | 36 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 244 | 32 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 306 | 38 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 099, 559, 599 | 7 | 12 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 004, 011, 014, 015, 044, 344 | 6 | 11 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 011, 059, 559 | 6 | 11 | False | True |
| Michigan4 | Indiana4 | alert_implied_echo | lane/family | primary | 5, 34 | 004, 045, 059, 344 | 4 | 10 | False | True |
| Virginia4 | Indiana4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 003, 014, 033, 044, 334 | 5 | 10 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 007, 008 | 5 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007, 008 | 5 | 10 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 244, 559 | 5 | 10 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 34, 6 | - | 6 | 10 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 14, 15, 23, 24, 33, 5 | - | 6 | 10 | False | True |
| Florida4 | Ohio4 | shared_lane | lane/family | primary | 13, 14, 15, 31, 33, 5 | - | 6 | 10 | False | True |
| Indiana4 | Michigan4 | shared_lane | lane/family | primary | 15, 18, 23, 34, 5, 9 | - | 6 | 10 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 5, 9 | - | 6 | 10 | False | True |
| Michigan4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 5, 9 | - | 6 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 12, 14, 15, 3, 33, 5 | - | 6 | 10 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 2, 21, 5, 9 | - | 6 | 10 | False | True |
| SouthCarolina4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 28, 31, 5 | - | 6 | 10 | False | True |
| Michigan4 | Virginia4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| NewYork4 | Michigan4 | alert_implied_echo | lane/family | primary | 2, 1 | 001, 005, 015 | 3 | 9 | False | True |
| Pennsylvania4 | Michigan4 | alert_implied_echo | lane/family | primary | 2, 5, 9 | 001, 009, 019 | 3 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 5, 15 | 009, 445, 599 | 3 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 224, 229 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 004, 059, 344, 559 | 4 | 9 | False | True |
| Indiana4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 244, 559 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 006, 017, 066, 559 | 4 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 013, 244 | 4 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 059, 244, 559 | 4 | 9 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 059, 244, 559 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 559 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 015, 559 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 009, 019, 559 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 559 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 008 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 299, 559 | 4 | 9 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 244, 559 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 009, 445, 559, 599 | 4 | 9 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 244 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 009, 059, 244, 559 | 4 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 13, 15, 23, 31, 33 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ Michigan4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Pennsylvania4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Florida4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
