# Predictive Portfolio — D=2026-01-21

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-21/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| OntarioCanada4 | 27 | 185 | 11:004 | 004 044 144 228 | 4:004 044 144 | 5(6) | idx[20]:2,3,5,9…(36) |
| Connecticut4 | 27 | 200 | 11:088 | 088 099 223 228 | 2:088 588 | 2(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | 27 | 201 | 11:009 | 009 066 113 118 | 4:004 009 499 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | 27 | 205 | 10:004 | 004 177 199 334 | 4:003 004 009 | 14(8) | idx[20]:2,3,4,5…(36) |
| Delaware4 | 27 | 224 | 10:009 | 009 088 117 223 | 3:009 223 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 234 | 10:022 | 022 033 088 112 | 2:022 033 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | 27 | 180 | 9:066 | 066 112 119 155 | 2:066 155 | 28(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | 27 | 186 | 9:003 | 003 009 011 077 | 2:003 355 | 29(6) | idx[20]:1,3,4,5…(36) |
| SouthCarolina4 | 27 | 199 | 9:114 | 114 115 155 233 | 2:114 233 | 8(8) | idx[20]:1,2,3,4…(36) |
| NewYork4 | 27 | 202 | 9:001 | 001 007 011 066 | 1:001 | 27(6) | idx[20]:2,3,6,8…(36) |
| NewJersey4 | 27 | 204 | 9:022 | 022 114 155 339 | 3:001 022 077 | 2(6) | idx[20]:1,2,3,5…(36) |
| Pennsylvania4 | 27 | 210 | 9:007 | 007 066 228 255 | 3:007 033 168 | 23(6) | idx[20]:1,3,4,6…(36) |
| NorthCarolina4 | 27 | 225 | 9:001 | 001 009 044 225 | 3:001 225 228 | 27(6) | idx[20]:2,5,7,8…(36) |
| Indiana4 | 27 | 240 | 9:002 | 002 022 177 226 | 2:002 007 | 6(6) | idx[20]:2,3,4,5…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **OntarioCanada4**: `004 040 400 044 404 440 144 414 441 455 545 554`
- **Connecticut4**: `088 808 880 238 588 822 858 885 006 283 328 382`
- **Ohio4**: `009 090 900 499 949 994 004 040 400 559 595 955`
- **Virginia4**: `004 040 400 334 343 433 009 090 900 003 030 300`
- **Delaware4**: `009 090 900 559 595 955 223 232 322 655 255 259`
- **PuertoRico4**: `022 202 220 605 186 681 033 303 330 808 168 618`
- **Michigan4**: `066 606 660 155 515 551 247 121 277 150 250 245`
- **Florida4**: `003 030 300 638 368 238 355 535 553 838 008 080`
- **SouthCarolina4**: `114 141 411 233 323 332 005 093 683 903 603 670`
- **NewYork4**: `001 010 100 377 138 183 238 283 318 328 378 381`
- **NewJersey4**: `022 202 220 001 077 707 770 017 010 100 794 101`
- **Pennsylvania4**: `007 070 700 168 186 618 681 816 861 033 303 330`
- **NorthCarolina4**: `001 010 100 228 282 822 225 252 522 327 287 782`
- **Indiana4**: `002 020 200 017 610 071 007 070 700 177 226 262`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **OntarioCanada4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-21/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,9…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 349 489 344 399 249 024 348 236 238 846 246 088 368 001 456 449 228 224 025 825` (src: `sharepacks/_predictive/2026-01-21/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-21/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`038 358 033 088 335 588 015 056 001 006 155 556 049 459 044 099 035 058 003 008 238 699 559 822 068 348 249 489 005 688 007 016 166 466 224 142` (src: `sharepacks/_predictive/2026-01-21/Connecticut4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-21/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 249 479 244 299 447 799 049 459 044 099 027 257 022 077 499 097 788 448 007 113 149 389 138 224 084 008 078 066 109 556` (src: `sharepacks/_predictive/2026-01-21/Ohio4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-21/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 034 039 048 089 345 359 348 389 334 339 127 267 122 177 062 702 003 105 705 244 011 344 099 013 133 148 199 033 224 347` (src: `sharepacks/_predictive/2026-01-21/Virginia4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-21/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 038 358 033 088 049 459 044 099 259 655 336 334 399 244 223 149 037 034 224 003 055 338 615 214` (src: `sharepacks/_predictive/2026-01-21/Delaware4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-21/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`136 168 113 118 366 668 038 358 033 088 335 588 027 257 022 077 035 058 003 008 011 386 605 806 238 028 388 148 112 244 002 114 334 344 505 227` (src: `sharepacks/_predictive/2026-01-21/PuertoRico4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=28(6)` pack=`247 279 224 229 477 779` (src: `sharepacks/_predictive/2026-01-21/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`016 156 011 066 115 566 247 279 224 229 477 779 126 167 112 117 015 056 001 006 250 174 244 245 277 077 119 177 559 778 788 599 449 338 166 120` (src: `sharepacks/_predictive/2026-01-21/Michigan4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=29(6)` pack=`238 378 233 288 337 788` (src: `sharepacks/_predictive/2026-01-21/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`035 058 003 008 355 558 023 028 037 078 235 258 238 378 233 288 138 368 133 188 025 178 278 038 009 838 259 589 077 011 055 599 224 177 046 889` (src: `sharepacks/_predictive/2026-01-21/Florida4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=8(8)` pack=`013 018 036 068 135 158 356 568` (src: `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`013 018 036 068 135 158 146 169 114 119 466 669 238 378 233 288 034 039 048 089 683 167 136 339 005 002 009 670 115 155 033 599 467 003 677 166` (src: `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-21/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,6,8…(36)` pack=`237 278 223 228 377 778 127 267 122 177 226 677 238 378 233 288 015 056 001 006 138 113 353 013 225 011 388 137 007 339 347 357 117 224 044 449` (src: `sharepacks/_predictive/2026-01-21/NewYork4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-21/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`027 257 022 077 225 577 015 056 001 006 155 556 012 017 026 067 249 479 244 299 559 057 599 339 019 133 149 037 038 005 101 114 177 233 714 304` (src: `sharepacks/_predictive/2026-01-21/NewJersey4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-21/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,6…(36)` pack=`138 368 133 188 336 688 238 378 233 288 337 788 025 057 002 007 038 358 033 088 168 034 334 003 028 178 146 344 338 005 228 066 224 177 103 194` (src: `sharepacks/_predictive/2026-01-21/Pennsylvania4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-21/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,7,8…(36)` pack=`237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 238 378 233 288 136 127 344 009 012 368 621 036 024 388 044 227 321 119 166 144` (src: `sharepacks/_predictive/2026-01-21/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-21/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`025 057 002 007 255 557 016 156 011 066 115 566 012 017 026 067 027 257 022 077 177 617 001 641 559 037 244 133 223 014 147 193 166 137 003 593` (src: `sharepacks/_predictive/2026-01-21/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **OntarioCanada4**: `045 059 004 009 455 559 044 144 449 249 844 846 246 001 024 029 074 245 254 452 542 228 282 822`
- **Connecticut4**: `015 056 001 006 155 556 088 238 588 822 166 005 688 068 699 594 945 249 850 065 051 099 223 228`
- **Ohio4**: `045 059 004 009 455 559 499 077 097 449 007 099 084 149 479 497 794 974 940 042 047 079 790 970`
- **Virginia4**: `034 039 048 089 345 359 458 589 004 009 334 003 062 438 105 702 705 706 084 093 390 930 177 199`
- **Delaware4**: `045 059 004 009 455 559 255 655 259 223 055 034 336 338 020 025 075 520 570 088 117 171 711 808`
- **PuertoRico4**: `027 257 022 077 225 577 186 605 028 808 033 388 338 806 386 683 836 118 668 238 283 382 832 805`
- **Michigan4**: `247 279 224 229 477 779 155 277 066 174 121 245 227 150 250 241 124 129 147 471 741 112 119 191`
- **Florida4**: `238 378 233 288 337 788 087 838 003 638 532 355 008 025 278 035 832 038 032 037 009 011 077 090`
- **SouthCarolina4**: `013 018 036 068 135 158 356 568 005 114 093 233 009 055 670 683 167 115 151 155 511 515 551 119`
- **NewYork4**: `237 278 223 228 377 778 001 323 353 113 668 138 238 378 177 717 737 771 773 127 327 347 137 173`
- **NewJersey4**: `015 056 001 006 155 556 017 022 077 101 559 711 019 009 005 050 500 794 012 062 114 141 339 393`
- **Pennsylvania4**: `138 368 133 188 336 688 007 028 224 338 005 168 033 034 093 183 318 381 403 813 831 903 003 818`
- **NorthCarolina4**: `237 278 223 228 377 778 001 006 225 136 168 227 277 388 621 012 017 062 009 044 090 404 440 900`
- **Indiana4**: `016 156 011 066 115 566 017 002 166 007 177 226 001 037 193 601 703 077 606 660 127 172 271 721`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **OntarioCanada4**: `045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 349 489 344 399 249 024 348 236 238 846 246 088 368 001 456 449 228 224 025 825`
- **Connecticut4**: `038 358 033 088 335 588 015 056 001 006 155 556 049 459 044 099 035 058 003 008 238 699 559 822 068 348 249 489 005 688 007 016 166 466 224 142`
- **Ohio4**: `045 059 004 009 455 559 249 479 244 299 447 799 049 459 044 099 027 257 022 077 499 097 788 448 007 113 149 389 138 224 084 008 078 066 109 556`
- **Virginia4**: `045 059 004 009 455 559 034 039 048 089 345 359 348 389 334 339 127 267 122 177 062 702 003 105 705 244 011 344 099 013 133 148 199 033 224 347`
- **Delaware4**: `045 059 004 009 455 559 025 057 002 007 255 557 038 358 033 088 049 459 044 099 259 655 336 334 399 244 223 149 037 034 224 003 055 338 615 214`
- **PuertoRico4**: `136 168 113 118 366 668 038 358 033 088 335 588 027 257 022 077 035 058 003 008 011 386 605 806 238 028 388 148 112 244 002 114 334 344 505 227`
- **Michigan4**: `016 156 011 066 115 566 247 279 224 229 477 779 126 167 112 117 015 056 001 006 250 174 244 245 277 077 119 177 559 778 788 599 449 338 166 120`
- **Florida4**: `035 058 003 008 355 558 023 028 037 078 235 258 238 378 233 288 138 368 133 188 025 178 278 038 009 838 259 589 077 011 055 599 224 177 046 889`
- **SouthCarolina4**: `013 018 036 068 135 158 146 169 114 119 466 669 238 378 233 288 034 039 048 089 683 167 136 339 005 002 009 670 115 155 033 599 467 003 677 166`
- **NewYork4**: `237 278 223 228 377 778 127 267 122 177 226 677 238 378 233 288 015 056 001 006 138 113 353 013 225 011 388 137 007 339 347 357 117 224 044 449`
- **NewJersey4**: `027 257 022 077 225 577 015 056 001 006 155 556 012 017 026 067 249 479 244 299 559 057 599 339 019 133 149 037 038 005 101 114 177 233 714 304`
- **Pennsylvania4**: `138 368 133 188 336 688 238 378 233 288 337 788 025 057 002 007 038 358 033 088 168 034 334 003 028 178 146 344 338 005 228 066 224 177 103 194`
- **NorthCarolina4**: `237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 238 378 233 288 136 127 344 009 012 368 621 036 024 388 044 227 321 119 166 144`
- **Indiana4**: `025 057 002 007 255 557 016 156 011 066 115 566 012 017 026 067 027 257 022 077 177 617 001 641 559 037 244 133 223 014 147 193 166 137 003 593`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-21/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-21/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-21/<STATE>/play_card__tool_only*.json` (budgeted cuts)
