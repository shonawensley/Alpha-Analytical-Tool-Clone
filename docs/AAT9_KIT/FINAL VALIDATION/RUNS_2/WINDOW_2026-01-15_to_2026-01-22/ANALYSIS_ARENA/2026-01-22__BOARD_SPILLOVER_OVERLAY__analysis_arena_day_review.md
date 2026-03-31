# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-22

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `7075fb84658a4d95`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 005, 006, 255, 055, 001, 355, 058, 003 | 1, 2, 4, 3, 15, 13, 8, 6 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 2 | Delaware4 | 559, 255, 336, 259, 355, 133, 055, 599 | 5, 12, 23, 3, 4, 11, 31, 1 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 007, 259, 224, 178, 025, 678, 257, 278 | 3, 10, 21, 12, 27, 29, 23, 7 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 077, 001, 003, 137, 037, 334, 347, 014 | 11, 10, 21, 33, 15, 5, 2, 6 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 224, 477, 559, 077, 017, 007, 778, 779 | 28, 10, 12, 17, 15, 5, 3, 7 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 017, 299, 009, 133, 001, 059, 044, 229 | 5, 7, 31, 12, 33, 2, 23, 21 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 238, 337, 133, 177, 559, 115, 377, 255 | 29, 23, 13, 10, 5, 6, 32, 27 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 8 | NorthCarolina4 | 113, 778, 011, 244, 006, 119, 288, 012 | 18, 27, 31, 2, 23, 6, 29, 12 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 9 | Ohio4 | 007, 078, 008, 077, 088, 559, 057, 255 | 3, 5, 4, 11, 10, 35, 13, 34 | - | - | shared_host | Midday:ALERT/4, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 044, 244, 445, 004, 006, 456, 446 | 15, 31, 5, 9, 12, 25, 2, 21 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 11 | Pennsylvania4 | 559, 599, 399, 007, 039, 224, 339 | 5, 14, 15, 34, 33, 3, 28, 18 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 366, 011, 334, 168, 455, 015, 033, 136 | 18, 6, 23, 33, 5, 2, 13, 19 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:WATCH/2 |
| 13 | SouthCarolina4 | 009, 599, 005, 007, 029, 039, 299 | 5, 3, 1, 2, 15, 12, 31, 14 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 559, 026, 016, 339, 033, 002, 255, 188 | 7, 6, 13, 8, 5, 3, 23, 33 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 253 | 30 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 249 | 31 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 250 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 298 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 242 | 30 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 278 | 32 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 250 | 30 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 215 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 245 | 28 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 218 | 25 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 039, 059, 559, 599 | 8 | 13 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 007, 025, 057, 224, 255 | 6 | 11 | False | True |
| NewJersey4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 33, 5, 7 | - | 7 | 11 | False | True |
| NorthCarolina4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 2, 18 | 006, 118, 136, 168 | 4 | 10 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 017, 059, 133, 455, 559 | 5 | 10 | False | True |
| Florida4 | Michigan4 | shared_box_family | lane/family | primary | - | 007, 017, 057, 224, 225 | 5 | 10 | False | True |
| Florida4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 002, 005, 007, 255, 259 | 5 | 10 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 007, 057, 077, 224, 559 | 5 | 10 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 017, 133, 559 | 5 | 10 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 011, 115, 559 | 5 | 10 | False | True |
| NorthCarolina4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 011, 136, 168, 366 | 5 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 224, 559 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 255, 559 | 5 | 10 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 002, 005, 006, 115, 559 | 5 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 12, 15, 2, 23, 3 | - | 6 | 10 | False | True |
| Indiana4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 18, 2, 23, 33 | - | 6 | 10 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 10, 11, 12, 15, 21, 4 | - | 6 | 10 | False | True |
| NewJersey4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 31, 5 | - | 6 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 33, 5 | - | 6 | 10 | False | True |
| NewYork4 | Virginia4 | shared_lane | lane/family | primary | 12, 13, 18, 23, 5, 6 | - | 6 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_lane | lane/family | primary | 15, 18, 23, 3, 33, 5 | - | 6 | 10 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 15, 18, 23, 33, 5, 6 | - | 6 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 013, 055, 255, 355 | 4 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 255 | 4 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 015 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_box_family | lane/family | primary | - | 014, 017, 133, 559 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 059, 255, 259, 559 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 007, 011, 017, 077 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 011, 017, 137 | 4 | 9 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 014, 017 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 011, 455 | 4 | 9 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 011, 012, 559 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 029, 115, 559 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 4 | - | 5 | 9 | False | True |
| Delaware4 | NewYork4 | shared_lane | lane/family | primary | 12, 18, 20, 23, 5 | - | 5 | 9 | False | True |
| Delaware4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 3, 5 | - | 5 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 14, 15, 18, 23, 33 | - | 5 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 33 | - | 5 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 14, 15, 2, 23 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 33 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Pennsylvania4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ PuertoRico4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
