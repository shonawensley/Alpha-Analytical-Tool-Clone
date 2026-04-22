# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-18

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `155988cc845ad604`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 344, 559, 244, 346, 399, 144, 113, 355 | 34, 5, 18, 24, 31, 23, 25, 15 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 2 | Delaware4 | 099, 399, 599, 559, 229, 039, 001, 389 | 15, 34, 5, 28, 14, 33, 2, 35 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 006, 224, 114, 255, 124, 246, 066, 025 | 19, 28, 2, 22, 3, 18, 31, 7 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 4 | Indiana4 | 559, 599, 224, 249, 569, 455, 024, 579 | 5, 15, 12, 31, 9, 28, 30, 6 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 5 | Michigan4 | 001, 559, 044, 055, 677, 167, 267, 127 | 20, 5, 2, 1, 15, 3, 17, 35 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 6 | NewJersey4 | 499, 118, 038, 599, 199, 023, 224, 158 | 35, 25, 18, 13, 15, 8, 3, 11 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 035, 667, 036, 006, 559, 366, 007, 013 | 4, 2, 8, 3, 17, 18, 14, 33 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/0 |
| 8 | NorthCarolina4 | 112, 117, 177, 122, 299 | 17, 20, 18, 31, 21, 29, 23, 16 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 9 | Ohio4 | 559, 069, 006, 099, 299, 026, 224, 009 | 5, 7, 9, 15, 2, 31, 35, 4 | - | - | shared_host | Combined:ALERT/3, Midday:ALERT/3, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 223, 138, 148, 168, 113, 368, 349, 114 | 18, 27, 23, 24, 21, 33, 34, 8 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 077, 067, 034, 259, 477, 677, 133, 033 | 10, 28, 12, 7, 23, 14, 24, 32 | - | - | shared_host | Combined:OFF/1, Midday:OFF/0, Evening:OFF/0 |
| 12 | PuertoRico4 | 244, 006, 144, 024, 224, 677, 256, 559 | 31, 2, 28, 20, 25, 7, 12, 5 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 344, 455, 003, 355, 244, 559, 447 | 5, 34, 4, 31, 15, 2, 33, 3 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 14 | Virginia4 | 559, 255, 225, 235, 668, 256, 055, 268 | 3, 5, 10, 1, 11, 7, 18, 8 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 285 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 257 | 30 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 248 | 32 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 315 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 267 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 269 | 35 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 275 | 32 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 134 | 16 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 271 | 32 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 206 | 25 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Florida4 | NewYork4 | alert_implied_echo | lane/family | primary | 2, 8 | 006, 013, 015, 036, 056 | 5 | 11 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 013, 244, 344, 349, 559 | 6 | 11 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31, 5, 9 | - | 7 | 11 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 011, 013, 349, 399, 559 | 5 | 10 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 011, 013, 599, 899 | 5 | 10 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 005, 013, 559 | 5 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 113, 118, 133, 138, 366 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 007, 077, 224, 677 | 5 | 10 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 31, 5 | - | 6 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_lane | lane/family | primary | 10, 12, 18, 23, 33, 7 | - | 6 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 31, 34 | 244, 344, 349 | 3 | 9 | False | True |
| Florida4 | Virginia4 | alert_implied_echo | lane/family | primary | 8, 2, 3 | 013, 015, 025 | 3 | 9 | False | True |
| Michigan4 | NewYork4 | alert_implied_echo | lane/family | primary | 2 | 006, 015, 056 | 3 | 9 | False | True |
| OntarioCanada4 | Connecticut4 | alert_implied_echo | lane/family | primary | 34 | 344, 349, 399 | 3 | 9 | False | True |
| OntarioCanada4 | Delaware4 | alert_implied_echo | lane/family | primary | 34 | 349, 399, 899 | 3 | 9 | False | True |
| PuertoRico4 | NewYork4 | alert_implied_echo | lane/family | primary | 2 | 006, 015, 056 | 3 | 9 | False | True |
| SouthCarolina4 | Connecticut4 | alert_implied_echo | lane/family | primary | 34 | 344, 349, 399 | 3 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 004, 059, 559, 569 | 4 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 113, 349 | 4 | 9 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 009, 099, 559 | 4 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 224, 477 | 4 | 9 | False | True |
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 224 | 4 | 9 | False | True |
| Florida4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 025, 255, 668 | 4 | 9 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 004, 455, 559 | 4 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 024, 224, 249 | 4 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 455, 559 | 4 | 9 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 559 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 044, 559 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 118 | 4 | 9 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 003, 004, 006, 017 | 4 | 9 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 013, 015, 559 | 4 | 9 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 007, 244 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 013, 455, 559 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 15, 18, 33, 34, 5 | - | 5 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 23, 25, 34 | - | 5 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 5 | - | 5 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 23, 31, 34, 5 | - | 5 | 9 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 12, 17, 2, 23, 3 | - | 5 | 9 | False | True |
| NewYork4 | Ohio4 | shared_lane | lane/family | primary | 12, 18, 2, 23, 5 | - | 5 | 9 | False | True |
| NewYork4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 3, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ SouthCarolina4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ OntarioCanada4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ PuertoRico4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ PuertoRico4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Ohio4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ PuertoRico4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
