# Predictive Portfolio — D=2026-01-07

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| NewYork4 | 27 | 174 | 14:001 | 001 007 011 066 | 3:001 011 066 | 2(6) | idx[16]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 243 | 12:022 | 022 033 199 299 | 3:022 033 225 | 10(6) | idx[16]:3,6,8,10…(36) |
| NewJersey4 | 27 | 186 | 11:022 | 022 114 155 339 | 3:022 077 114 | 10(6) | idx[16]:8,9,10,11…(36) |
| SouthCarolina4 | 27 | 191 | 11:115 | 115 155 224 233 | 3:115 224 566 | 6(6) | idx[16]:1,2,3,5…(36) |
| Ohio4 | 27 | 198 | 10:009 | 009 066 113 118 | 4:009 088 559 | 4(6) | idx[16]:1,4,5,6…(36) |
| NorthCarolina4 | 27 | 201 | 10:001 | 001 009 044 225 | 2:001 044 | 31(6) | idx[16]:1,2,4,5…(36) |
| Delaware4 | 27 | 220 | 10:009 | 009 088 223 228 | 3:004 009 559 | 5(6) | idx[16]:4,5,6,8…(36) |
| OntarioCanada4 | 27 | 241 | 10:004 | 004 044 144 228 | 3:004 044 224 | 28(6) | idx[16]:1,2,5,6…(36) |
| Florida4 | 27 | 163 | 9:003 | 003 009 011 077 | 3:003 033 334 | 33(6) | idx[16]:4,5,6,11…(36) |
| Michigan4 | 27 | 179 | 9:112 | 112 119 155 199 | 2:112 119 | 19(6) | idx[16]:2,5,6,8…(36) |
| Connecticut4 | 27 | 189 | 9:088 | 088 099 223 228 | 3:088 223 228 | 30(8) | idx[16]:5,12,13,15…(36) |
| Virginia4 | 27 | 200 | 9:004 | 004 177 199 377 | 3:004 199 377 | 34(6) | idx[16]:2,3,4,5…(36) |
| Pennsylvania4 | 27 | 219 | 9:007 | 007 066 228 255 | 3:007 112 557 | 7(8) | idx[16]:1,2,3,4…(36) |
| Indiana4 | 27 | 240 | 9:002 | 002 022 177 226 | 3:002 066 266 | 12(8) | idx[16]:3,6,7,9…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

### B12 (`analysis_prefix`)
- **NewYork4**: `010 001 100 060 506 508 011 066 101 110 606 660`
- **PuertoRico4**: `022 202 220 225 252 522 033 303 330 168 186 618`
- **NewJersey4**: `022 220 202 077 770 114 141 411 707 088 788 808`
- **SouthCarolina4**: `151 115 511 665 566 656 224 242 422 059 095 509`
- **Ohio4**: `009 090 900 889 559 595 955 088 808 880 898 988`
- **NorthCarolina4**: `001 010 100 044 404 440 600 244 940 900 964 006`
- **Delaware4**: `009 090 900 559 595 955 004 040 400 011 114 101`
- **OntarioCanada4**: `004 040 400 224 044 404 440 242 422 270 274 247`
- **Florida4**: `003 030 300 433 334 436 343 033 233 303 323 330`
- **Michigan4**: `112 121 211 191 156 141 119 911 155 196 691 117`
- **Connecticut4**: `088 808 880 228 424 844 282 822 223 232 322 824`
- **Virginia4**: `004 040 400 199 919 991 377 737 773 349 399 009`
- **Pennsylvania4**: `007 070 700 112 015 557 575 755 121 211 016 035`
- **Indiana4**: `002 020 200 066 606 660 266 626 662 064 636 762`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **NewYork4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-07/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 035 058 003 008 355 558 016 156 011 066 115 566 025 057 002 007 255 557 808 118 005 018 559 802 449 224 256 227 667 244` (src: `sharepacks/_predictive/2026-01-07/NewYork4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,6,8,10…(36)` pack=`027 257 022 077 225 577 136 168 113 118 366 668 038 358 033 088 335 588 238 378 233 288 337 788 688 806 028 278 199 299 066 224 286 200 245 134` (src: `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:8,9,10,11…(36)` pack=`027 257 022 077 225 577 146 169 114 119 466 669 348 389 334 339 488 889 238 378 233 288 337 788 189 188 018 778 078 088 244 187 126 989 159 227` (src: `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`016 156 011 066 115 566 045 059 004 009 455 559 049 459 044 099 445 599 015 056 001 006 155 556 224 695 244 226 667 002 669 005 469 692 233 369` (src: `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,4,5,6…(36)` pack=`045 059 004 009 455 559 035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 488 889 929 788 089 899 066 599 022 113 116 388 005 224` (src: `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,4,5…(36)` pack=`249 479 244 299 447 799 015 056 001 006 155 556 049 459 044 099 445 599 149 469 144 199 446 699 920 900 642 224 019 466 003 227 225 366 344 005` (src: `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-07/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,8…(36)` pack=`045 059 004 009 455 559 016 156 011 066 115 566 136 168 113 118 366 668 146 169 114 119 466 669 034 414 133 893 088 044 344 338 013 014 003 224` (src: `sharepacks/_predictive/2026-01-07/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=28(6)` pack=`247 279 224 229 477 779` (src: `sharepacks/_predictive/2026-01-07/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,5,6…(36)` pack=`247 279 224 229 477 779 045 059 004 009 455 559 127 267 122 177 226 677 027 257 022 077 225 577 024 264 228 044 015 324 146 005 144 019 244 011` (src: `sharepacks/_predictive/2026-01-07/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,11…(36)` pack=`348 389 334 339 488 889 238 378 233 288 337 788 138 368 133 188 336 688 035 058 003 008 355 558 436 234 023 011 344 009 033 136 167 029 446 227` (src: `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,5,6,8…(36)` pack=`146 169 114 119 466 669 016 156 011 066 115 566 149 469 144 199 446 699 136 168 113 118 366 668 112 155 479 599 013 147 277 161 449 344 338 559` (src: `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=30(8)` pack=`234 239 248 289 347 379 478 789` (src: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,12,13,15…(36)` pack=`234 239 248 289 347 379 249 479 244 299 447 799 349 489 344 399 448 899 237 278 223 228 377 778 099 088 889 224 668 144 494 116 559 024 678 468` (src: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-07/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,4,5…(36)` pack=`149 469 144 199 446 699 045 059 004 009 455 559 349 489 344 399 448 899 134 139 148 189 346 369 099 091 361 499 177 377 669 355 244 224 001 007` (src: `sharepacks/_predictive/2026-01-07/Virginia4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 115 566 045 059 004 009 455 559 012 112 122 019 228 227 013 005 035 599 338 224` (src: `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,6,7,9…(36)` pack=`127 267 122 177 226 677 024 029 047 079 245 259 136 168 113 118 366 668 126 167 112 117 266 667 002 064 066 447 669 788 264 022 224 448 688 706` (src: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **NewYork4**: `015 056 001 006 155 556 118 508 011 066 005 668 808 008 507 605 805 038 016 051 610 510 007 070`
- **PuertoRico4**: `027 257 022 077 225 577 028 033 866 688 788 168 200 286 806 068 138 183 813 831 238 283 382 832`
- **NewJersey4**: `027 257 022 077 225 577 114 088 788 078 119 187 189 188 778 126 072 572 155 339 393 515 551 933`
- **SouthCarolina4**: `016 156 011 066 115 566 599 595 224 059 005 695 155 233 099 244 369 396 424 442 639 667 676 693`
- **Ohio4**: `035 058 003 008 355 558 009 889 059 559 088 022 225 899 929 989 080 089 095 098 590 800 890 950`
- **NorthCarolina4**: `249 479 244 299 447 799 001 044 600 964 940 920 900 224 229 006 060 144 414 441 446 464 644 642`
- **Delaware4**: `045 059 004 009 455 559 011 114 414 338 811 893 034 039 084 345 354 453 543 088 223 228 232 282`
- **OntarioCanada4**: `247 279 224 229 477 779 004 044 177 264 324 015 270 762 024 029 074 245 254 452 542 144 228 282`
- **Florida4**: `348 389 334 339 488 889 003 436 336 033 233 234 023 028 073 009 011 077 090 101 110 707 770 900`
- **Michigan4**: `146 169 114 119 466 669 112 156 155 117 101 016 186 277 161 479 149 164 194 461 491 941 411 199`
- **Connecticut4**: `234 239 248 289 347 379 478 789 228 424 088 844 894 224 223 229 744 847 482 748 842 144 414 441`
- **Virginia4**: `349 489 344 399 448 899 199 004 091 499 377 009 198 341 361 099 149 194 491 941 041 049 014 064`
- **Pennsylvania4**: `012 017 026 067 125 157 256 567 007 112 015 557 227 013 095 000 059 021 120 210 005 050 500 016`
- **Indiana4**: `024 029 047 079 245 259 457 579 002 064 224 066 266 636 906 447 448 788 046 092 254 290 452 460`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`)

- **NewYork4**: `015 056 001 006 155 556 035 058 003 008 355 558 016 156 011 066 115 566 025 057 002 007 255 557 808 118 005 018 559 802 449 224 256 227 667 244`
- **PuertoRico4**: `027 257 022 077 225 577 136 168 113 118 366 668 038 358 033 088 335 588 238 378 233 288 337 788 688 806 028 278 199 299 066 224 286 200 245 134`
- **NewJersey4**: `027 257 022 077 225 577 146 169 114 119 466 669 348 389 334 339 488 889 238 378 233 288 337 788 189 188 018 778 078 088 244 187 126 989 159 227`
- **SouthCarolina4**: `016 156 011 066 115 566 045 059 004 009 455 559 049 459 044 099 445 599 015 056 001 006 155 556 224 695 244 226 667 002 669 005 469 692 233 369`
- **Ohio4**: `045 059 004 009 455 559 035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 488 889 929 788 089 899 066 599 022 113 116 388 005 224`
- **NorthCarolina4**: `249 479 244 299 447 799 015 056 001 006 155 556 049 459 044 099 445 599 149 469 144 199 446 699 920 900 642 224 019 466 003 227 225 366 344 005`
- **Delaware4**: `045 059 004 009 455 559 016 156 011 066 115 566 136 168 113 118 366 668 146 169 114 119 466 669 034 414 133 893 088 044 344 338 013 014 003 224`
- **OntarioCanada4**: `247 279 224 229 477 779 045 059 004 009 455 559 127 267 122 177 226 677 027 257 022 077 225 577 024 264 228 044 015 324 146 005 144 019 244 011`
- **Florida4**: `348 389 334 339 488 889 238 378 233 288 337 788 138 368 133 188 336 688 035 058 003 008 355 558 436 234 023 011 344 009 033 136 167 029 446 227`
- **Michigan4**: `146 169 114 119 466 669 016 156 011 066 115 566 149 469 144 199 446 699 136 168 113 118 366 668 112 155 479 599 013 147 277 161 449 344 338 559`
- **Connecticut4**: `234 239 248 289 347 379 249 479 244 299 447 799 349 489 344 399 448 899 237 278 223 228 377 778 099 088 889 224 668 144 494 116 559 024 678 468`
- **Virginia4**: `149 469 144 199 446 699 045 059 004 009 455 559 349 489 344 399 448 899 134 139 148 189 346 369 099 091 361 499 177 377 669 355 244 224 001 007`
- **Pennsylvania4**: `025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 115 566 045 059 004 009 455 559 012 112 122 019 228 227 013 005 035 599 338 224`
- **Indiana4**: `127 267 122 177 226 677 024 029 047 079 245 259 136 168 113 118 366 668 126 167 112 117 266 667 002 064 066 447 669 788 264 022 224 448 688 706`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-07/<STATE>/play_card__tool_only*.json` (budgeted cuts)
