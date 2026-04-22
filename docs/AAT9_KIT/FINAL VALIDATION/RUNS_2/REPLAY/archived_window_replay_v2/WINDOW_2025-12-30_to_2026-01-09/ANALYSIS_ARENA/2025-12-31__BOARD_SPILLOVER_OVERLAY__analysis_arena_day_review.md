# Board Spillover Overlay — analysis_arena_day_review — D=2025-12-31

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `9e1f5e3b339bfab7`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 011, 559, 003, 368, 678, 338, 114, 599 | 6, 24, 23, 5, 32, 4, 15, 18 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/0 |
| 2 | Delaware4 | 244, 144, 499, 014, 117, 114, 449, 447 | 31, 35, 25, 22, 17, 9, 21, 28 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 3 | Florida4 | 677, 116, 077, 778, 259, 013, 114, 133 | 21, 10, 23, 16, 32, 12, 20, 27 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 4 | Indiana4 | 677, 244, 668, 226, 066, 144, 011 | 20, 18, 6, 31, 16, 23, 10, 19 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 136, 244, 599, 335, 255, 559, 355 | 18, 3, 2, 23, 31, 15, 13, 5 | - | - | shared_host | Evening:WATCH/2, Midday:OFF/1, Combined:OFF/0 |
| 6 | NewJersey4 | 299, 224, 118, 128, 289, 599, 899 | 31, 18, 28, 21, 30, 15, 35, 1 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 7 | NewYork4 | 778, 677, 116, 016, 667, 006, 478 | 20, 17, 27, 6, 18, 16, 2, 35 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 8 | NorthCarolina4 | 003, 224, 034, 005, 004, 055, 223 | 4, 28, 1, 5, 12, 14, 15, 9 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 599, 009, 559, 057, 056, 077, 099, 677 | 5, 15, 7, 2, 3, 10, 17, 1 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 188, 022, 114, 225, 255, 118, 258, 488 | 10, 23, 20, 19, 21, 18, 3, 33 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 11 | Pennsylvania4 | 339, 138, 559, 177, 113, 133, 255 | 23, 33, 18, 29, 20, 5, 3, 32 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/0, Evening:OFF/0 |
| 12 | PuertoRico4 | 344, 244, 113, 224, 246, 445, 134, 011 | 31, 34, 18, 28, 22, 15, 24, 19 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 189, 066, 138, 019, 011, 006, 018, 118 | 6, 23, 2, 24, 8, 5, 18, 9 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 14 | Virginia4 | 177, 224, 133, 113, 399, 117, 138 | 20, 23, 18, 28, 34, 17, 31, 7 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 300 | 37 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 254 | 31 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 262 | 29 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 327 | 39 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 237 | 27 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 227 | 29 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 232 | 26 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 187 | 25 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 203 | 26 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 194 | 22 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 014, 044, 114, 244, 299, 447 | 7 | 12 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 005, 006, 127, 226, 267, 668, 677 | 7 | 12 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 011, 017, 056, 066, 368 | 6 | 11 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 044, 113, 224, 244, 299 | 6 | 11 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 113, 133, 138, 177, 336, 368 | 6 | 11 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 011, 189, 368 | 5 | 10 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 007, 116, 677, 778 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 005, 113, 168, 244, 599 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 017, 056 | 5 | 10 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 17, 18, 23, 25, 31 | - | 6 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 22, 23, 31, 34 | - | 6 | 10 | False | True |
| Connecticut4 | Indiana4 | alert_implied_echo | lane/family | primary | 6, 23 | 011, 066, 368 | 3 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 6, 23 | 011, 066, 368 | 3 | 9 | False | True |
| Indiana4 | NewYork4 | alert_implied_echo | lane/family | primary | 20 | 226, 267, 677 | 3 | 9 | False | True |
| NewYork4 | Indiana4 | alert_implied_echo | lane/family | primary | 20 | 226, 267, 677 | 3 | 9 | False | True |
| SouthCarolina4 | Florida4 | alert_implied_echo | lane/family | primary | 2, 3, 12 | 006, 007, 259 | 3 | 9 | False | True |
| SouthCarolina4 | Ohio4 | alert_implied_echo | lane/family | primary | 2, 3 | 006, 007, 056 | 3 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 006, 009 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 017, 144, 244 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 044, 244, 299 | 4 | 9 | False | True |
| Florida4 | Indiana4 | shared_box_family | lane/family | primary | - | 006, 011, 017, 677 | 4 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 007, 017, 077 | 4 | 9 | False | True |
| Florida4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 011, 017 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 005, 006, 244, 668 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 011, 017, 177, 368 | 4 | 9 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 127, 177, 368, 677 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 011, 017, 138, 368 | 4 | 9 | False | True |
| Connecticut4 | Florida4 | shared_lane | lane/family | primary | 12, 18, 21, 23, 32 | - | 5 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 18, 21, 23, 24, 6 | - | 5 | 9 | False | True |
| Delaware4 | Virginia4 | shared_lane | lane/family | primary | 17, 18, 19, 23, 34 | - | 5 | 9 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 10, 16, 18, 20, 27 | - | 5 | 9 | False | True |
| Florida4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 18, 20, 21, 23 | - | 5 | 9 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 16, 17, 18, 20, 6 | - | 5 | 9 | False | True |
| Michigan4 | Ohio4 | shared_lane | lane/family | primary | 15, 2, 23, 3, 5 | - | 5 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 31 | - | 5 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 6, 23 | 011, 368 | 2 | 8 | False | True |
| Indiana4 | Virginia4 | alert_implied_echo | lane/family | primary | 23, 20 | 368, 677 | 2 | 8 | False | True |
| SouthCarolina4 | Connecticut4 | alert_implied_echo | lane/family | primary | 2 | 001, 006 | 2 | 8 | False | True |
| SouthCarolina4 | Indiana4 | alert_implied_echo | lane/family | primary | 2 | 006, 056 | 2 | 8 | False | True |
| SouthCarolina4 | Michigan4 | alert_implied_echo | lane/family | primary | 2 | 001, 006 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ NewYork4` score=`39` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Indiana4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Florida4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ Virginia4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ PuertoRico4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
