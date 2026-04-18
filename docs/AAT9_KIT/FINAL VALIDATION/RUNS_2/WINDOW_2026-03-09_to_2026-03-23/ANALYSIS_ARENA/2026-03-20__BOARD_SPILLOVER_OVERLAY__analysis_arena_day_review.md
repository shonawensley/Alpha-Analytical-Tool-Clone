# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-20

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `49402ade9a7937da`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 113, 133, 355, 144, 255, 244, 114 | 18, 28, 23, 4, 34, 25, 24, 29 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 2 | Delaware4 | 001, 099, 399, 599, 559, 019, 069 | 2, 15, 5, 34, 9, 14, 6, 35 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 244, 114, 246, 006, 224, 249, 066, 124 | 31, 22, 28, 19, 6, 17, 2, 3 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 559, 455, 155, 259, 599, 249, 055, 255 | 5, 12, 15, 2, 31, 9, 1, 3 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 5 | Michigan4 | 559, 001, 677, 229, 556, 044, 005, 009 | 5, 2, 1, 31, 3, 15, 7, 20 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 6 | NewJersey4 | 559, 499, 334, 455, 003, 149, 013, 344 | 5, 35, 15, 25, 33, 4, 34, 14 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 066, 035, 667, 013, 259, 366, 033, 559 | 6, 17, 4, 18, 5, 8, 12, 13 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 8 | NorthCarolina4 | 299, 117, 088, 889, 599, 177 | 31, 17, 15, 13, 20, 29, 33, 28 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 069, 699, 006, 559, 099, 019, 002, 299 | 9, 5, 3, 25, 15, 2, 31, 12 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 559, 368, 599, 138, 378, 355, 239, 168 | 23, 5, 30, 18, 27, 24, 3, 15 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 11 | Pennsylvania4 | 067, 244, 467, 044, 088, 446, 046, 677 | 31, 7, 9, 25, 22, 23, 24, 13 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 244, 006, 224, 144, 388, 017, 246, 445 | 31, 25, 22, 2, 28, 15, 10, 16 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 559, 455, 344, 155, 055, 003, 355 | 5, 4, 34, 1, 2, 3, 31, 10 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 14 | Virginia4 | 225, 255, 559, 268, 259, 022, 224, 229 | 10, 3, 21, 28, 5, 12, 1, 18 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 218 | 26 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 254 | 29 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 216 | 27 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 312 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 288 | 34 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 248 | 28 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 276 | 34 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 174 | 20 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 309 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 279 | 33 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 224, 244, 246, 249, 299, 447, 479 | 8 | 13 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 045, 059, 155, 455, 559 | 8 | 13 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 019, 069, 099, 559 | 7 | 12 | False | True |
| SouthCarolina4 | Michigan4 | alert_implied_echo | lane/family | primary | 5, 1 | 045, 055, 059, 455, 559 | 5 | 11 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 007, 045, 059, 455, 559 | 6 | 11 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 007, 045, 055, 059, 455, 559 | 6 | 11 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 005, 013, 014, 455, 559 | 6 | 11 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 22, 23, 25, 31, 7 | - | 7 | 11 | False | True |
| PuertoRico4 | Florida4 | alert_implied_echo | lane/family | primary | 2, 28, 22 | 001, 006, 224, 246 | 4 | 10 | False | True |
| SouthCarolina4 | Indiana4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 044, 559 | 5 | 10 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 455, 559 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 014, 017, 244, 249, 447 | 5 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 31, 5 | - | 6 | 10 | False | True |
| Michigan4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 2, 23, 28, 31, 5 | - | 6 | 10 | False | True |
| Ohio4 | Delaware4 | alert_implied_echo | lane/family | primary | 2, 9, 15 | 006, 069, 099 | 3 | 9 | False | True |
| PuertoRico4 | Delaware4 | alert_implied_echo | lane/family | primary | 2 | 001, 006, 015 | 3 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 014, 144, 224 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 001, 155, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 559 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 013, 559 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 005, 455, 559 | 4 | 9 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 004, 024, 559 | 4 | 9 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 455, 559 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 013, 014, 455, 559 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 18, 23, 25, 33, 4 | - | 5 | 9 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 5 | - | 5 | 9 | False | True |
| Delaware4 | Ohio4 | shared_lane | lane/family | primary | 15, 2, 23, 5, 9 | - | 5 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 5 | - | 5 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 2, 23, 34, 5 | - | 5 | 9 | False | True |
| Florida4 | PuertoRico4 | shared_lane | lane/family | primary | 2, 22, 23, 28, 31 | - | 5 | 9 | False | True |
| Indiana4 | Michigan4 | shared_lane | lane/family | primary | 15, 2, 23, 31, 5 | - | 5 | 9 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 5 | - | 5 | 9 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 5 | - | 5 | 9 | False | True |
| Michigan4 | Ohio4 | shared_lane | lane/family | primary | 15, 2, 23, 3, 5 | - | 5 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 15, 2, 23, 5 | - | 5 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_lane | lane/family | primary | 15, 18, 23, 4, 5 | - | 5 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 4, 5 | - | 5 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 25, 5 | - | 5 | 9 | False | True |
| NewYork4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 17, 23, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Florida4 ↔ PuertoRico4` score=`40` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ SouthCarolina4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Ohio4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ PuertoRico4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ PuertoRico4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
