# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Ohio4 | 27 | 172 | 12:009 | 009 066 113 118 | 3:002 009 559 | 3(6) | idx[16]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 235 | 12:022 | 022 033 088 199 | 3:022 033 225 | 10(6) | idx[16]:3,4,6,7…(36) |
| SouthCarolina4 | 27 | 193 | 11:115 | 115 155 224 233 | 3:115 224 566 | 6(6) | idx[16]:1,2,3,5…(36) |
| NewYork4 | 27 | 196 | 11:001 | 001 007 011 066 | 3:001 011 066 | 6(6) | idx[16]:1,2,3,4…(36) |
| Delaware4 | 27 | 202 | 11:009 | 009 088 223 228 | 4:004 009 088 | 5(6) | idx[16]:4,5,6,13…(36) |
| Florida4 | 27 | 170 | 10:003 | 003 009 011 077 | 2:003 136 | 24(8) | idx[16]:4,5,6,9…(36) |
| Pennsylvania4 | 27 | 203 | 10:007 | 007 066 228 255 | 3:007 059 557 | 3(6) | idx[16]:1,2,3,5…(36) |
| Michigan4 | 27 | 159 | 9:112 | 112 119 155 199 | 2:112 119 | 18(6) | idx[16]:2,5,6,8…(36) |
| NewJersey4 | 27 | 174 | 9:022 | 022 114 155 339 | 3:022 077 114 | 27(6) | idx[16]:2,5,10,11…(36) |
| NorthCarolina4 | 27 | 189 | 9:001 | 001 009 044 225 | 3:001 044 244 | 12(8) | idx[16]:1,2,5,6…(36) |
| Connecticut4 | 27 | 196 | 9:088 | 088 099 223 228 | 2:088 228 | 30(8) | idx[16]:5,10,12,13…(36) |
| Virginia4 | 27 | 215 | 9:004 | 004 177 199 377 | 2:004 377 | 14(8) | idx[16]:4,5,14,15…(36) |
| OntarioCanada4 | 27 | 226 | 9:004 | 004 044 144 244 | 3:004 044 244 | 9(8) | idx[16]:1,2,5,6…(36) |
| Indiana4 | 27 | 232 | 9:002 | 002 022 177 226 | 2:002 177 | 6(6) | idx[16]:2,3,5,6…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

### B12 (`analysis_prefix`)
- **Ohio4**: `090 009 900 020 050 025 002 200 559 595 955 070`
- **PuertoRico4**: `022 202 220 286 225 252 522 033 088 303 330 808`
- **SouthCarolina4**: `151 115 511 566 656 665 224 242 422 695 599 959`
- **NewYork4**: `001 010 100 011 066 110 660 008 101 606 506 006`
- **Delaware4**: `090 009 900 040 004 400 595 559 955 088 808 880`
- **Florida4**: `003 030 300 136 613 631 436 163 316 361 368 386`
- **Pennsylvania4**: `070 007 700 059 095 590 575 557 755 509 905 950`
- **Michigan4**: `191 112 121 211 118 119 911 138 168 156 186 618`
- **NewJersey4**: `022 202 220 889 887 077 114 141 411 778 707 770`
- **NorthCarolina4**: `001 010 100 044 404 440 940 942 244 424 442 242`
- **Connecticut4**: `088 808 880 228 282 822 248 727 298 284 724 794`
- **Virginia4**: `004 040 400 377 098 737 773 849 089 899 009 090`
- **OntarioCanada4**: `004 040 400 015 244 424 442 044 144 404 414 440`
- **Indiana4**: `002 020 200 066 177 717 771 386 683 836 266 606`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-06/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 024 029 047 079 245 259 035 058 003 008 355 558 050 249 066 599 088 060 022 224 113 116 388 449` (src: `sharepacks/_predictive/2026-01-06/Ohio4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-06/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,4,6,7…(36)` pack=`027 257 022 077 225 577 012 017 026 067 125 157 013 018 036 068 135 158 123 128 137 178 236 268 866 226 278 199 033 066 688 245 224 007 216 003` (src: `sharepacks/_predictive/2026-01-06/PuertoRico4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-06/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`016 156 011 066 115 566 247 279 224 229 477 779 127 267 122 177 226 677 049 459 044 099 445 599 667 695 005 369 696 595 155 244 225 295 007 296` (src: `sharepacks/_predictive/2026-01-06/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 035 058 003 008 355 558 025 057 002 007 255 557 668 005 808 788 706 801 802 449 226 224 245 266` (src: `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-06/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,13…(36)` pack=`045 059 004 009 455 559 038 358 033 088 335 588 016 156 011 066 115 566 146 169 114 119 466 669 894 811 449 834 445 224 244 338 144 003 336 854` (src: `sharepacks/_predictive/2026-01-06/Delaware4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=24(8)` pack=`134 139 148 189 346 369 468 689` (src: `sharepacks/_predictive/2026-01-06/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,9…(36)` pack=`035 058 003 008 355 558 136 168 113 118 366 668 348 389 334 339 488 889 134 139 148 189 346 369 344 023 646 368 011 009 233 599 167 437 456 236` (src: `sharepacks/_predictive/2026-01-06/Florida4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-06/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`025 057 002 007 255 557 015 056 001 006 155 556 045 059 004 009 455 559 016 156 011 066 115 566 019 599 228 117 717 244 368 359 005 416 017 227` (src: `sharepacks/_predictive/2026-01-06/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-06/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,5,6,8…(36)` pack=`136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 115 566 126 167 112 117 266 667 199 138 155 277 244 198 108 449 559 338 599 344` (src: `sharepacks/_predictive/2026-01-06/Michigan4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,5,10,11…(36)` pack=`237 278 223 228 377 778 348 389 334 339 488 889 027 257 022 077 225 577 238 378 233 288 337 788 279 188 189 087 114 829 127 227 155 449 244 559` (src: `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-06/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,5,6…(36)` pack=`049 459 044 099 445 599 249 479 244 299 447 799 024 029 047 079 245 259 247 279 224 229 477 779 202 144 001 009 019 232 344 227 226 005 066 166` (src: `sharepacks/_predictive/2026-01-06/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=30(8)` pack=`234 239 248 289 347 379 478 789` (src: `sharepacks/_predictive/2026-01-06/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,10,12,13…(36)` pack=`234 239 248 289 347 379 247 279 224 229 477 779 249 479 244 299 447 799 038 358 033 088 335 588 099 228 727 448 388 024 486 668 144 027 116 559` (src: `sharepacks/_predictive/2026-01-06/Connecticut4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,14,15…(36)` pack=`034 039 048 089 345 359 349 489 344 399 448 899 045 059 004 009 455 559 049 459 044 099 445 599 377 891 499 199 177 898 008 248 244 821 224 188` (src: `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-06/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,5,6…(36)` pack=`045 059 004 009 455 559 014 019 046 069 145 159 015 056 001 006 155 556 249 479 244 299 447 799 144 247 124 164 044 177 011 277 116 126 005 118` (src: `sharepacks/_predictive/2026-01-06/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,5,6…(36)` pack=`016 156 011 066 115 566 012 017 026 067 125 157 025 057 002 007 255 557 127 267 122 177 226 677 386 266 366 246 244 022 046 224 006 678 116 059` (src: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Ohio4**: `025 057 002 007 255 557 090 050 559 080 022 225 060 259 249 052 059 095 250 590 950 029 092 290`
- **PuertoRico4**: `027 257 022 077 225 577 286 260 068 033 088 688 866 216 226 021 076 199 919 991 006 060 066 244`
- **SouthCarolina4**: `016 156 011 066 115 566 695 005 599 595 224 295 696 007 297 267 762 106 601 651 155 233 323 332`
- **NewYork4**: `016 156 011 066 115 566 001 008 506 006 668 005 168 808 706 056 502 507 085 508 061 561 007 070`
- **Delaware4**: `045 059 004 009 455 559 088 449 499 011 114 224 244 338 388 838 883 811 834 538 583 835 853 054`
- **Florida4**: `134 139 148 189 346 369 468 689 003 136 008 433 344 368 636 646 023 028 073 009 011 077 090 101`
- **Pennsylvania4**: `025 057 002 007 255 557 059 368 717 000 359 005 015 416 561 520 750 066 228 282 606 660 822 599`
- **Michigan4**: `136 168 113 118 366 668 191 112 138 156 117 368 016 277 169 196 691 961 198 698 163 155 199 515`
- **NewJersey4**: `237 278 223 228 377 778 889 077 022 887 114 188 189 087 882 279 287 297 728 782 792 872 972 822`
- **NorthCarolina4**: `024 029 047 079 245 259 457 579 044 001 940 942 244 242 292 144 414 441 446 464 644 699 969 996`
- **Connecticut4**: `234 239 248 289 347 379 478 789 088 727 224 244 228 388 744 486 684 824 864 277 772 482 842 144`
- **Virginia4**: `034 039 048 089 345 359 458 589 377 004 849 899 499 009 891 898 908 948 989 998 593 399 043 177`
- **OntarioCanada4**: `014 019 046 069 145 159 456 569 015 004 247 244 044 144 011 124 724 277 150 510 116 161 611 164`
- **Indiana4**: `016 156 011 066 115 566 076 002 386 138 244 177 266 366 224 242 422 368 638 863 046 776 447 688`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`)

- **Ohio4**: `045 059 004 009 455 559 025 057 002 007 255 557 024 029 047 079 245 259 035 058 003 008 355 558 050 249 066 599 088 060 022 224 113 116 388 449`
- **PuertoRico4**: `027 257 022 077 225 577 012 017 026 067 125 157 013 018 036 068 135 158 123 128 137 178 236 268 866 226 278 199 033 066 688 245 224 007 216 003`
- **SouthCarolina4**: `016 156 011 066 115 566 247 279 224 229 477 779 127 267 122 177 226 677 049 459 044 099 445 599 667 695 005 369 696 595 155 244 225 295 007 296`
- **NewYork4**: `015 056 001 006 155 556 016 156 011 066 115 566 035 058 003 008 355 558 025 057 002 007 255 557 668 005 808 788 706 801 802 449 226 224 245 266`
- **Delaware4**: `045 059 004 009 455 559 038 358 033 088 335 588 016 156 011 066 115 566 146 169 114 119 466 669 894 811 449 834 445 224 244 338 144 003 336 854`
- **Florida4**: `035 058 003 008 355 558 136 168 113 118 366 668 348 389 334 339 488 889 134 139 148 189 346 369 344 023 646 368 011 009 233 599 167 437 456 236`
- **Pennsylvania4**: `025 057 002 007 255 557 015 056 001 006 155 556 045 059 004 009 455 559 016 156 011 066 115 566 019 599 228 117 717 244 368 359 005 416 017 227`
- **Michigan4**: `136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 115 566 126 167 112 117 266 667 199 138 155 277 244 198 108 449 559 338 599 344`
- **NewJersey4**: `237 278 223 228 377 778 348 389 334 339 488 889 027 257 022 077 225 577 238 378 233 288 337 788 279 188 189 087 114 829 127 227 155 449 244 559`
- **NorthCarolina4**: `049 459 044 099 445 599 249 479 244 299 447 799 024 029 047 079 245 259 247 279 224 229 477 779 202 144 001 009 019 232 344 227 226 005 066 166`
- **Connecticut4**: `234 239 248 289 347 379 247 279 224 229 477 779 249 479 244 299 447 799 038 358 033 088 335 588 099 228 727 448 388 024 486 668 144 027 116 559`
- **Virginia4**: `034 039 048 089 345 359 349 489 344 399 448 899 045 059 004 009 455 559 049 459 044 099 445 599 377 891 499 199 177 898 008 248 244 821 224 188`
- **OntarioCanada4**: `045 059 004 009 455 559 014 019 046 069 145 159 015 056 001 006 155 556 249 479 244 299 447 799 144 247 124 164 044 177 011 277 116 126 005 118`
- **Indiana4**: `016 156 011 066 115 566 012 017 026 067 125 157 025 057 002 007 255 557 127 267 122 177 226 677 386 266 366 246 244 022 046 224 006 678 116 059`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card__tool_only*.json` (budgeted cuts)
