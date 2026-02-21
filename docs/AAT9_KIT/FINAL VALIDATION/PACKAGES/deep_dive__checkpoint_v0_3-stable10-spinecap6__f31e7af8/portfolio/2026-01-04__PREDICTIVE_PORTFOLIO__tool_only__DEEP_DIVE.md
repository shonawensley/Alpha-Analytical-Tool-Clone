# Predictive Portfolio — D=2026-01-04

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-04/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 27 | 227 | 13:022 | 022 033 088 199 | 4:022 033 088 | 10(6) | idx[20]:3,4,7,8…(36) |
| Pennsylvania4 | 27 | 200 | 12:007 | 007 066 228 255 | 2:007 255 | 3(6) | idx[22]:1,2,3,5…(36) |
| Florida4 | 27 | 178 | 11:003 | 003 008 009 011 | 3:003 008 033 | 14(8) | idx[20]:4,5,6,7…(36) |
| Delaware4 | 27 | 186 | 11:009 | 009 088 223 228 | 3:004 009 559 | 5(6) | idx[22]:1,2,4,5…(36) |
| OntarioCanada4 | 27 | 214 | 11:004 | 004 044 144 244 | 3:004 167 244 | 5(6) | idx[20]:3,5,6,8…(36) |
| Ohio4 | 27 | 153 | 10:009 | 009 066 113 118 | 1:009 | 3(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | 27 | 236 | 10:001 | 001 007 011 066 | 3:001 006 066 | 6(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | 27 | 154 | 9:112 | 112 119 155 199 | 1:112 | 18(6) | idx[20]:2,4,5,6…(36) |
| NewJersey4 | 27 | 187 | 9:022 | 022 114 155 339 | 3:022 077 889 | 27(6) | idx[20]:2,5,10,11…(36) |
| NorthCarolina4 | 27 | 192 | 9:001 | 001 009 044 225 | 4:001 009 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| Virginia4 | 27 | 209 | 9:004 | 004 177 199 377 | 4:004 177 377 | 27(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | 27 | 220 | 9:115 | 115 155 224 233 | 3:115 224 233 | 21(8) | idx[20]:2,3,4,5…(36) |
| Indiana4 | 27 | 223 | 9:002 | 002 022 177 226 | 2:002 177 | 18(6) | idx[20]:2,3,5,6…(36) |
| Connecticut4 | 27 | 241 | 9:088 | 088 099 223 228 | 1:088 | 9(8) | idx[20]:1,2,5,9…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **PuertoRico4**: `022 202 220 225 252 522 033 088 303 330 808 880`
- **Pennsylvania4**: `007 070 700 552 055 057 059 255 525 557 095 597`
- **Florida4**: `030 003 300 033 008 080 800 467 303 330 334 343`
- **Delaware4**: `090 009 900 040 595 004 400 559 955 114 088 808`
- **OntarioCanada4**: `040 004 400 167 617 671 716 244 424 442 176 761`
- **Ohio4**: `090 009 900 590 850 508 805 075 059 095 950 025`
- **NewYork4**: `001 010 100 066 705 660 008 606 006 060 600 700`
- **Michigan4**: `112 121 211 168 186 681 368 016 618 861 119 191`
- **NewJersey4**: `022 202 220 889 077 707 770 282 279 898 988 982`
- **NorthCarolina4**: `001 010 100 044 404 440 522 009 090 225 252 900`
- **Virginia4**: `004 040 400 377 177 717 771 737 773 455 545 554`
- **SouthCarolina4**: `115 151 511 238 283 832 233 323 332 224 242 422`
- **Indiana4**: `002 020 200 066 626 668 177 717 771 386 683 836`
- **Connecticut4**: `088 808 880 546 564 654 614 744 645 004 368 099`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-04/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,7,8…(36)` pack=`027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 012 017 026 067 113 033 036 226 233 216 268 134 336 002 003 199 599 227 334 259` (src: `sharepacks/_predictive/2026-01-04/PuertoRico4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-04/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,5…(36)` pack=`025 057 002 007 255 557 045 059 004 009 455 559 005 055 024 029 047 079 066 138 416 015 599 167 678 399 578 038 359 389 228 299 415 224 499 227` (src: `sharepacks/_predictive/2026-01-04/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-04/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:4,5,6,7…(36)` pack=`035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 034 039 048 089 386 599 434 338 467 136 009 364 244 567 011 224 677 227 159 377` (src: `sharepacks/_predictive/2026-01-04/Florida4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-04/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,4,5…(36)` pack=`045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 449 499 011 058 249 001 144 223 334 126 088 055 388 087 811 224 854 344 201 851` (src: `sharepacks/_predictive/2026-01-04/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-04/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,5,6,8…(36)` pack=`045 059 004 009 455 559 126 167 112 117 266 667 146 169 114 119 136 168 113 118 344 244 044 267 047 188 788 180 678 189 007 348 077 224 011 023` (src: `sharepacks/_predictive/2026-01-04/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-04/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 027 257 022 077 035 058 003 008 592 224 113 278 050 599 299 088 066 688 889 116 449 114 338 060` (src: `sharepacks/_predictive/2026-01-04/Ohio4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-04/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 035 058 003 008 706 668 027 348 899 038 368 278 249 500 018 224 559 388 124 599` (src: `sharepacks/_predictive/2026-01-04/NewYork4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-04/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,4,5,6…(36)` pack=`136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 138 368 133 188 112 199 918 335 161 449 388 155 339 244 355 559 599 227 477 108` (src: `sharepacks/_predictive/2026-01-04/Michigan4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-04/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,10,11…(36)` pack=`237 278 223 228 377 778 348 389 334 339 488 889 027 257 022 077 247 279 224 229 079 882 299 982 188 127 599 258 089 155 114 989 227 559 129 199` (src: `sharepacks/_predictive/2026-01-04/NewJersey4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-04/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`024 029 047 079 245 259 049 459 044 099 445 599 027 257 022 077 249 479 244 299 001 199 009 242 344 035 500 449 226 223 227 502 093 932 338 541` (src: `sharepacks/_predictive/2026-01-04/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-04/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`045 059 004 009 455 559 247 279 224 229 477 779 237 278 223 228 024 029 047 079 399 002 334 561 177 015 167 169 148 133 028 233 227 599 593 347` (src: `sharepacks/_predictive/2026-01-04/Virginia4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=21(8)` pack=`123 128 137 178 236 268 367 678` (src: `sharepacks/_predictive/2026-01-04/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`238 378 233 288 337 788 123 128 137 178 236 268 247 279 224 229 015 056 001 006 115 244 235 295 267 389 349 336 003 239 559 002 118 359 227 667` (src: `sharepacks/_predictive/2026-01-04/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-04/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`136 168 113 118 366 668 016 156 011 066 115 566 126 167 112 117 012 017 026 067 386 002 224 177 015 559 146 447 069 144 338 038 246 022 028 616` (src: `sharepacks/_predictive/2026-01-04/Indiana4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,5,9…(36)` pack=`014 019 046 069 145 159 038 358 033 088 335 588 045 059 004 009 247 279 224 229 614 127 024 048 223 694 667 368 744 468 099 248 678 001 227 055` (src: `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **PuertoRico4**: `027 257 022 077 225 577 206 232 237 073 033 088 226 268 278 286 287 327 723 728 782 827 872 223`
- **Pennsylvania4**: `025 057 002 007 255 557 055 059 597 559 599 455 099 138 015 416 075 507 570 750 052 066 228 282`
- **Florida4**: `034 039 048 089 345 359 458 589 030 033 467 338 008 388 434 364 634 303 330 334 343 433 386 647`
- **Delaware4**: `045 059 004 009 455 559 449 114 088 499 144 224 055 388 249 294 429 492 924 942 011 101 110 141`
- **OntarioCanada4**: `045 059 004 009 455 559 167 047 244 344 114 180 181 189 267 074 470 740 484 164 416 168 095 540`
- **Ohio4**: `025 057 002 007 255 557 090 590 850 592 559 027 257 077 088 577 707 757 770 775 225 252 522 058`
- **NewYork4**: `016 156 011 066 115 566 001 008 705 006 700 668 168 500 706 038 052 062 206 250 506 520 005 067`
- **Michigan4**: `136 168 113 118 366 668 112 368 016 119 449 916 388 138 133 313 331 336 363 633 161 918 181 189`
- **NewJersey4**: `237 278 223 228 377 778 022 889 982 279 989 299 227 277 077 707 770 898 988 924 928 229 289 298`
- **NorthCarolina4**: `024 029 047 079 245 259 457 579 044 522 001 035 244 242 229 009 090 225 252 900 199 699 919 969`
- **Virginia4**: `237 278 223 228 377 778 004 097 455 559 177 599 229 399 297 148 227 272 722 561 547 597 042 047`
- **SouthCarolina4**: `123 128 137 178 236 268 367 678 115 238 235 233 224 295 003 015 253 352 371 532 731 387 783 837`
- **Indiana4**: `136 168 113 118 366 668 386 002 066 138 626 026 616 177 688 868 886 183 188 224 242 318 381 422`
- **Connecticut4**: `014 019 046 069 145 159 456 569 088 388 744 004 368 048 468 694 614 041 096 099 223 228 232 282`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **PuertoRico4**: `027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 012 017 026 067 113 033 036 226 233 216 268 134 336 002 003 199 599 227 334 259`
- **Pennsylvania4**: `025 057 002 007 255 557 045 059 004 009 455 559 005 055 024 029 047 079 066 138 416 015 599 167 678 399 578 038 359 389 228 299 415 224 499 227`
- **Florida4**: `035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 034 039 048 089 386 599 434 338 467 136 009 364 244 567 011 224 677 227 159 377`
- **Delaware4**: `045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 449 499 011 058 249 001 144 223 334 126 088 055 388 087 811 224 854 344 201 851`
- **OntarioCanada4**: `045 059 004 009 455 559 126 167 112 117 266 667 146 169 114 119 136 168 113 118 344 244 044 267 047 188 788 180 678 189 007 348 077 224 011 023`
- **Ohio4**: `045 059 004 009 455 559 025 057 002 007 255 557 027 257 022 077 035 058 003 008 592 224 113 278 050 599 299 088 066 688 889 116 449 114 338 060`
- **NewYork4**: `015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 035 058 003 008 706 668 027 348 899 038 368 278 249 500 018 224 559 388 124 599`
- **Michigan4**: `136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 138 368 133 188 112 199 918 335 161 449 388 155 339 244 355 559 599 227 477 108`
- **NewJersey4**: `237 278 223 228 377 778 348 389 334 339 488 889 027 257 022 077 247 279 224 229 079 882 299 982 188 127 599 258 089 155 114 989 227 559 129 199`
- **NorthCarolina4**: `024 029 047 079 245 259 049 459 044 099 445 599 027 257 022 077 249 479 244 299 001 199 009 242 344 035 500 449 226 223 227 502 093 932 338 541`
- **Virginia4**: `045 059 004 009 455 559 247 279 224 229 477 779 237 278 223 228 024 029 047 079 399 002 334 561 177 015 167 169 148 133 028 233 227 599 593 347`
- **SouthCarolina4**: `238 378 233 288 337 788 123 128 137 178 236 268 247 279 224 229 015 056 001 006 115 244 235 295 267 389 349 336 003 239 559 002 118 359 227 667`
- **Indiana4**: `136 168 113 118 366 668 016 156 011 066 115 566 126 167 112 117 012 017 026 067 386 002 224 177 015 559 146 447 069 144 338 038 246 022 028 616`
- **Connecticut4**: `014 019 046 069 145 159 038 358 033 088 335 588 045 059 004 009 247 279 224 229 614 127 024 048 223 694 667 368 744 468 099 248 678 001 227 055`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-04/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-04/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-04/<STATE>/play_card__tool_only*.json` (budgeted cuts)
