# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-22

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `8e3443a77946021f`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 113, 224, 003, 225, 355, 255, 123, 011 | 18, 4, 28, 19, 10, 23, 3, 21 | - | - | shared_host | Midday:ALERT/3, Evening:ALERT/3, Combined:WATCH/2 |
| 2 | Delaware4 | 001, 599, 006, 116, 038, 011 | 2, 15, 16, 6, 13, 5, 12, 35 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/0 |
| 3 | Florida4 | 118, 024, 224, 066, 244, 229, 114, 026 | 12, 28, 31, 18, 19, 24, 6, 17 | - | - | shared_host | Midday:OFF/1, Combined:OFF/0, Evening:OFF/0 |
| 4 | Indiana4 | 559, 002, 259, 025, 005, 155, 455, 004 | 5, 3, 12, 2, 1, 6, 14, 26 | - | - | shared_host | Combined:OFF/0, Evening:OFF/0, Midday:OFF/0 |
| 5 | Michigan4 | 445, 344, 244, 012, 455, 677, 567, 001 | 15, 7, 5, 35, 1, 31, 2, 25 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 445, 344, 455, 001, 559, 005, 003, 499 | 5, 15, 1, 34, 2, 35, 4, 25 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 7 | NewYork4 | 066, 668, 667, 366, 136, 466, 156, 013 | 18, 6, 17, 23, 7, 32, 15, 19 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 8 | NorthCarolina4 | 499, 599, 088, 299, 889, 122, 119, 116 | 35, 31, 15, 33, 34, 13, 17, 10 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 002, 168, 669, 224, 128, 699, 667 | 3, 31, 18, 19, 21, 17, 28, 25 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 559, 055, 599, 368, 579, 399, 077, 057 | 5, 1, 12, 15, 8, 18, 23, 4 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 448, 449, 468, 048, 688, 044, 489, 447 | 34, 35, 25, 14, 31, 24, 23, 9 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 12 | PuertoRico4 | 338, 224, 244, 007, 368, 788 | 32, 28, 23, 31, 3, 29, 21, 13 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 559, 155, 455, 055, 255, 668, 577 | 5, 2, 3, 1, 8, 4, 18, 23 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 14 | Virginia4 | 225, 559, 003, 255, 259, 224, 038 | 10, 4, 3, 5, 32, 7, 28, 17 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 250 | 30 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 249 | 34 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 278 | 36 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 303 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 305 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 277 | 33 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 234 | 30 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 211 | 25 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 248 | 30 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 262 | 33 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 005, 014, 017, 055, 059, 455, 559 | 7 | 12 | False | True |
| Indiana4 | NewJersey4 | alert_implied_echo | lane/family | primary | 1, 5 | 005, 045, 059, 455, 559 | 5 | 11 | False | True |
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 113, 136, 366, 668 | 6 | 11 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 007, 118, 255, 668 | 6 | 11 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 055, 155, 455, 559 | 6 | 11 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 005, 045, 455, 559 | 6 | 11 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 33, 34, 35 | - | 7 | 11 | False | True |
| Indiana4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 1, 5 | 005, 059, 455, 559 | 4 | 10 | False | True |
| Indiana4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 1, 5 | 005, 045, 455, 559 | 4 | 10 | False | True |
| Pennsylvania4 | Michigan4 | alert_implied_echo | lane/family | primary | 7 | 012, 017, 256, 567 | 4 | 10 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 014, 024, 224 | 5 | 10 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 005, 059, 455, 559 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 344, 445, 455 | 5 | 10 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 013, 014, 017, 455, 599 | 5 | 10 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 055, 455, 559, 568 | 5 | 10 | False | True |
| Connecticut4 | PuertoRico4 | shared_lane | lane/family | primary | 10, 15, 18, 23, 28, 3 | - | 6 | 10 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 10, 18, 23, 28, 3, 4 | - | 6 | 10 | False | True |
| Florida4 | Ohio4 | shared_lane | lane/family | primary | 12, 18, 19, 23, 28, 31 | - | 6 | 10 | False | True |
| Michigan4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 18, 20, 31, 34, 35 | - | 6 | 10 | False | True |
| Michigan4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 24, 31, 34, 35 | - | 6 | 10 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 10, 18, 23, 28, 3, 32 | - | 6 | 10 | False | True |
| NewJersey4 | Michigan4 | alert_implied_echo | lane/family | primary | 15 | 445, 459, 599 | 3 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 003, 004, 011 | 4 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 003, 004, 007, 224 | 4 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_box_family | lane/family | primary | - | 003, 224, 225, 255 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 011 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 005, 006, 011 | 4 | 9 | False | True |
| Florida4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 009, 014, 244 | 4 | 9 | False | True |
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 224, 229, 244 | 4 | 9 | False | True |
| Florida4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 024, 224, 259 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 014, 017, 044, 344 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 005, 059, 455, 559 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 024, 224, 255 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 18, 19, 23, 28, 3 | - | 5 | 9 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 17, 18, 19, 23, 6 | - | 5 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 18, 2, 3, 5 | - | 5 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_lane | lane/family | primary | 1, 15, 23, 34, 5 | - | 5 | 9 | False | True |
| NewJersey4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 15, 2, 23, 5 | - | 5 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_lane | lane/family | primary | 18, 23, 28, 3, 31 | - | 5 | 9 | False | True |
| Ohio4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 28, 3 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ SouthCarolina4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewJersey4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
