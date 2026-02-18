# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| NewYork4 | 27 | 172 | 13:001 | 001 007 011 066 | 2:001 011 | 2(6) | idx[22]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 253 | 13:022 | 022 033 199 299 | 3:022 033 225 | 10(6) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | 27 | 183 | 11:022 | 022 114 155 339 | 3:022 077 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | 27 | 186 | 11:115 | 115 155 224 233 | 2:115 224 | 6(6) | idx[20]:1,2,3,5…(36) |
| Delaware4 | 27 | 212 | 10:009 | 009 088 223 228 | 3:009 011 559 | 5(6) | idx[20]:1,2,4,5…(36) |
| OntarioCanada4 | 27 | 230 | 10:004 | 004 044 144 228 | 4:004 044 224 | 12(8) | idx[20]:1,2,3,4…(36) |
| Florida4 | 27 | 157 | 9:003 | 003 009 011 077 | 2:003 334 | 33(6) | idx[20]:4,5,6,10…(36) |
| Connecticut4 | 27 | 175 | 9:088 | 088 099 223 228 | 2:088 228 | 34(6) | idx[20]:5,7,10,13…(36) |
| NorthCarolina4 | 27 | 193 | 9:001 | 001 009 044 225 | 3:001 009 044 | 31(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | 27 | 198 | 9:112 | 112 119 155 199 | 3:112 117 119 | 9(8) | idx[20]:2,3,5,6…(36) |
| Ohio4 | 27 | 201 | 9:009 | 009 066 113 118 | 4:009 088 559 | 4(6) | idx[20]:1,3,4,5…(36) |
| Pennsylvania4 | 27 | 217 | 9:007 | 007 066 228 255 | 2:007 557 | 5(6) | idx[20]:2,3,5,6…(36) |
| Virginia4 | 27 | 231 | 9:004 | 004 177 199 377 | 2:004 136 | 9(8) | idx[20]:2,3,5,6…(36) |
| Indiana4 | 27 | 246 | 9:002 | 002 022 177 226 | 3:002 066 266 | 12(8) | idx[20]:3,5,6,9…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

### B12 (`analysis_prefix`)
- **NewYork4**: `010 001 100 507 060 005 011 101 110 007 066 070`
- **PuertoRico4**: `220 022 202 225 252 522 028 280 033 303 330 207`
- **NewJersey4**: `022 220 202 077 770 189 707 088 788 808 878 880`
- **SouthCarolina4**: `151 115 511 059 224 242 422 665 095 509 590 905`
- **Delaware4**: `009 090 900 559 595 955 011 034 101 110 114 141`
- **OntarioCanada4**: `004 040 400 224 044 404 440 455 545 554 242 422`
- **Florida4**: `003 030 300 343 334 436 335 433 033 233 303 323`
- **Connecticut4**: `088 808 880 424 484 448 228 282 822 824 248 894`
- **NorthCarolina4**: `001 010 100 044 404 440 244 009 090 900 940 964`
- **Michigan4**: `112 121 211 119 191 911 155 117 171 711 051 141`
- **Ohio4**: `009 090 900 889 559 595 955 898 988 088 808 880`
- **Pennsylvania4**: `007 070 700 112 557 575 755 059 095 509 590 905`
- **Virginia4**: `004 040 400 361 349 059 136 163 316 613 631 114`
- **Indiana4**: `002 020 200 066 606 660 266 626 662 636 054 093`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **NewYork4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 005 055 808 668 008 256 599 378 559 245 224 667 244 449 227 802 804 169 234 489` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 025 057 002 007 068 688 278 668 006 238 236 004 800 299 245 127 388 199 224 066` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`027 257 022 077 225 577 146 169 114 119 466 669 134 139 148 189 348 389 334 339 788 138 078 007 186 126 155 014 089 088 008 017 287 005 559 224` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`016 156 011 066 115 566 014 019 046 069 145 159 045 059 004 009 134 139 148 189 699 599 002 244 155 233 224 336 024 399 499 005 669 667 339 338` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,4,5…(36)` pack=`045 059 004 009 455 559 034 039 048 089 345 359 016 156 011 066 136 168 113 118 044 088 114 344 105 414 223 338 053 133 334 814 224 244 449 005` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 024 029 047 079 044 244 263 344 015 401 677 011 036 055 228 144 002 003 033 668` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:4,5,6,10…(36)` pack=`348 389 334 339 488 889 038 358 033 088 335 588 138 368 133 188 016 156 011 066 003 436 023 034 316 009 234 146 233 338 077 224 599 244 344 227` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:5,7,10,13…(36)` pack=`349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 049 459 044 099 224 088 228 144 468 388 494 889 559 225 668 188 116 227 017 854` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`049 459 044 099 445 599 249 479 244 299 447 799 149 469 144 199 015 056 001 006 009 899 920 025 466 224 225 066 944 003 166 366 334 227 005 648` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`126 167 112 117 266 667 014 019 046 069 145 159 015 056 001 006 146 169 114 119 559 151 194 344 181 599 471 057 244 334 089 277 185 688 449 338` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`045 059 004 009 455 559 348 389 334 339 488 889 035 058 003 008 038 358 033 088 899 022 929 098 788 599 113 005 388 188 224 066 255 199 116 449` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 237 278 223 228 059 114 818 012 112 339 445 019 113 414 132 224 244 122 899 227` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 014 019 046 069 149 349 361 341 061 244 234 224 117 007 013 024 359 177 377 001` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,5,6,9…(36)` pack=`146 169 114 119 466 669 126 167 112 117 266 667 024 029 047 079 127 267 122 177 054 224 002 688 636 609 237 093 447 448 066 044 234 022 788 476` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **NewYork4**: `015 056 001 006 155 556 005 507 011 007 066 256 668 808 008 118 508 561 510 224 242 422 449 494`
- **PuertoRico4**: `027 257 022 077 225 577 028 033 388 200 800 068 238 205 023 073 199 299 919 929 991 992 244 424`
- **NewJersey4**: `027 257 022 077 225 577 189 088 788 078 005 089 119 186 138 183 126 287 782 072 572 114 141 155`
- **SouthCarolina4**: `016 156 011 066 115 566 059 599 595 224 499 699 906 936 336 369 005 050 500 695 596 106 601 651`
- **Delaware4**: `045 059 004 009 455 559 034 011 044 334 338 114 414 811 105 054 450 540 053 039 084 345 354 453`
- **OntarioCanada4**: `024 029 047 079 245 259 457 579 004 224 044 455 055 225 263 367 401 015 677 270 274 279 220 074`
- **Florida4**: `348 389 334 339 488 889 003 436 335 336 338 033 233 034 234 243 340 342 430 432 316 023 028 073`
- **Connecticut4**: `349 489 344 399 448 899 248 298 424 088 224 228 388 229 144 414 441 494 249 294 492 498 942 243`
- **NorthCarolina4**: `249 479 244 299 447 799 044 001 964 940 920 009 006 466 144 414 441 446 464 644 899 989 998 469`
- **Michigan4**: `014 019 046 069 145 159 456 569 112 119 155 117 181 471 668 277 051 141 151 154 194 941 591 951`
- **Ohio4**: `035 058 003 008 355 558 889 009 559 899 022 088 929 005 055 080 800 893 938 588 098 053 066 113`
- **Pennsylvania4**: `045 059 004 009 455 559 007 112 557 414 445 818 015 012 017 062 125 152 251 521 066 228 255 282`
- **Virginia4**: `014 019 046 069 145 159 456 569 004 361 349 059 114 061 341 344 146 169 149 194 491 941 041 049`
- **Indiana4**: `024 029 047 079 245 259 457 579 002 066 224 266 636 054 093 247 274 427 472 609 724 742 906 447`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`)

- **NewYork4**: `015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 005 055 808 668 008 256 599 378 559 245 224 667 244 449 227 802 804 169 234 489`
- **PuertoRico4**: `027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 025 057 002 007 068 688 278 668 006 238 236 004 800 299 245 127 388 199 224 066`
- **NewJersey4**: `027 257 022 077 225 577 146 169 114 119 466 669 134 139 148 189 348 389 334 339 788 138 078 007 186 126 155 014 089 088 008 017 287 005 559 224`
- **SouthCarolina4**: `016 156 011 066 115 566 014 019 046 069 145 159 045 059 004 009 134 139 148 189 699 599 002 244 155 233 224 336 024 399 499 005 669 667 339 338`
- **Delaware4**: `045 059 004 009 455 559 034 039 048 089 345 359 016 156 011 066 136 168 113 118 044 088 114 344 105 414 223 338 053 133 334 814 224 244 449 005`
- **OntarioCanada4**: `045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 024 029 047 079 044 244 263 344 015 401 677 011 036 055 228 144 002 003 033 668`
- **Florida4**: `348 389 334 339 488 889 038 358 033 088 335 588 138 368 133 188 016 156 011 066 003 436 023 034 316 009 234 146 233 338 077 224 599 244 344 227`
- **Connecticut4**: `349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 049 459 044 099 224 088 228 144 468 388 494 889 559 225 668 188 116 227 017 854`
- **NorthCarolina4**: `049 459 044 099 445 599 249 479 244 299 447 799 149 469 144 199 015 056 001 006 009 899 920 025 466 224 225 066 944 003 166 366 334 227 005 648`
- **Michigan4**: `126 167 112 117 266 667 014 019 046 069 145 159 015 056 001 006 146 169 114 119 559 151 194 344 181 599 471 057 244 334 089 277 185 688 449 338`
- **Ohio4**: `045 059 004 009 455 559 348 389 334 339 488 889 035 058 003 008 038 358 033 088 899 022 929 098 788 599 113 005 388 188 224 066 255 199 116 449`
- **Pennsylvania4**: `025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 237 278 223 228 059 114 818 012 112 339 445 019 113 414 132 224 244 122 899 227`
- **Virginia4**: `045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 014 019 046 069 149 349 361 341 061 244 234 224 117 007 013 024 359 177 377 001`
- **Indiana4**: `146 169 114 119 466 669 126 167 112 117 266 667 024 029 047 079 127 267 122 177 054 224 002 688 636 609 237 093 447 448 066 044 234 022 788 476`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only*.json` (budgeted cuts)
