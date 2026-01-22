# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 30 | 191 | 15:022 | 022 033 199 299 | 1:022 | 10(6) | 10(6) |
| NewYork4 | 30 | 153 | 13:001 | 001 007 011 066 | 3:001 011 066 | 2(6) | 2(6) |
| NewJersey4 | 30 | 164 | 11:022 | 022 114 155 339 | 1:022 | 10(6) | 10(6) |
| Delaware4 | 30 | 182 | 11:009 | 009 088 223 228 | 3:004 009 011 | 5(6) | 5(6) |
| Michigan4 | 30 | 159 | 10:112 | 112 119 155 199 | 3:112 119 155 | 22(8) | 22(8) |
| Pennsylvania4 | 30 | 177 | 10:007 | 007 066 228 255 | 4:002 007 112 | 3(6) | 3(6) |
| Florida4 | 30 | 143 | 9:003 | 003 009 011 077 | 3:003 033 338 | 13(6) | 13(6) |
| Connecticut4 | 30 | 156 | 9:088 | 088 099 223 228 | 3:088 244 448 | 34(6) | 34(6) |
| SouthCarolina4 | 30 | 168 | 9:115 | 115 155 224 233 | 3:115 224 599 | 6(6) | 6(6) |
| Ohio4 | 30 | 173 | 9:009 | 009 066 113 118 | 3:009 559 889 | 33(6) | 33(6) |
| NorthCarolina4 | 30 | 180 | 9:001 | 001 009 044 225 | 3:001 006 044 | 25(6) | 25(6) |
| OntarioCanada4 | 30 | 189 | 9:004 | 004 044 144 228 | 3:004 044 224 | 5(6) | 5(6) |
| Virginia4 | 30 | 194 | 9:004 | 004 177 199 377 | 1:004 | 5(6) | 5(6) |
| Indiana4 | 30 | 205 | 9:002 | 002 022 177 226 | 2:002 066 | 20(6) | 20(6) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **PuertoRico4**: `220 022 202 077 207 027 072 280 522 770 270 720`
- **NewYork4**: `010 001 100 060 005 011 101 110 066 606 660 006`
- **NewJersey4**: `022 220 202 077 186 089 138 183 126 522 770 114`
- **Delaware4**: `090 009 900 011 040 004 400 595 101 110 811 559`
- **Michigan4**: `112 121 211 119 191 911 155 051 141 199 515 551`
- **Pennsylvania4**: `070 007 700 112 121 211 020 255 525 552 002 200`
- **Florida4**: `003 030 300 338 383 833 335 033 303 330 316 343`
- **Connecticut4**: `088 808 880 424 484 448 894 984 244 442 844 494`
- **SouthCarolina4**: `115 151 511 224 242 422 665 599 959 995 059 155`
- **Ohio4**: `009 090 900 889 559 595 955 898 988 893 929 938`
- **NorthCarolina4**: `001 010 100 244 044 404 440 940 964 006 060 600`
- **OntarioCanada4**: `004 040 400 224 044 404 440 242 422 270 274 279`
- **Virginia4**: `004 040 400 349 361 341 042 146 169 394 439 493`
- **Indiana4**: `002 020 200 066 606 660 766 054 247 274 427 472`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **Michigan4**: `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=13(6)` pack=`038 358 033 088 335 588` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=25(6)` pack=`149 469 144 199 446 699` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__vtracpack_v1.json`)

### B24 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 068 280 058 205 278 033 199 299 244 424 442 000 725 757 775 006 060 066`
- **NewYork4**: `015 056 001 006 155 556 005 011 066 008 256 000 118 507 508 561 510 007 070 700 449 494 499 944`
- **NewJersey4**: `027 257 022 077 225 577 189 000 078 089 186 138 126 114 155 339 393 411 515 551 933 252 707 227`
- **Delaware4**: `045 059 004 009 455 559 011 334 811 034 105 049 088 223 228 232 282 322 808 822 880 033 303 330`
- **Michigan4**: `124 129 147 179 246 269 467 679 112 119 155 000 277 051 141 194 941 192 291 921 199 515 551 919`
- **Pennsylvania4**: `025 057 002 007 255 557 112 059 009 445 818 132 066 228 599 959 995 999 227 272 277 338 383 388`
- **Florida4**: `038 358 033 088 335 588 338 003 087 343 333 536 316 436 032 037 078 780 870 009 011 077 090 101`
- **Connecticut4**: `349 489 344 399 448 899 298 088 424 248 224 229 444 494 249 294 492 498 942 824 284 243 099 223`
- **SouthCarolina4**: `016 156 011 066 115 566 059 224 599 499 936 005 120 125 175 155 233 323 332 515 551 101 110 656`
- **Ohio4**: `348 389 334 339 488 889 009 559 888 022 929 058 010 015 065 510 560 066 113 118 131 181 311 606`
- **NorthCarolina4**: `149 469 144 199 446 699 920 001 244 940 044 006 299 948 944 924 049 094 249 294 490 492 942 024`
- **OntarioCanada4**: `045 059 004 009 455 559 224 015 044 677 270 274 279 220 024 029 074 245 254 452 542 144 228 282`
- **Virginia4**: `045 059 004 009 455 559 361 349 042 097 341 344 597 146 169 049 047 079 790 970 177 199 377 717`
- **Indiana4**: `127 267 122 177 226 677 002 076 066 054 247 669 609 766 021 026 067 670 760 022 202 220 262 622`

### B36 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 068 280 058 205 278 033 199 299 244 000 006 066 668 688 036 063 268 286 306 360 603 628 630 682 826 862 004 009 040 045`
- **NewYork4**: `015 056 001 006 155 556 005 011 066 008 256 000 118 507 508 561 007 449 499 555 227 272 277 722 727 772 080 255 525 552 559 595 667 676 766 800`
- **NewJersey4**: `027 257 022 077 225 577 189 000 078 089 186 138 126 114 155 339 227 277 449 499 003 007 008 030 070 080 098 224 242 300 422 559 595 599 700 778`
- **Delaware4**: `045 059 004 009 455 559 011 334 811 034 105 049 088 223 228 033 444 449 499 003 244 300 344 424 434 442 443 043 124 142 214 241 304 333 340 389`
- **Michigan4**: `124 129 147 179 246 269 467 679 112 119 155 000 277 051 141 194 199 117 266 449 499 244 424 442 058 085 508 580 805 850 338 383 388 833 838 883`
- **Pennsylvania4**: `025 057 002 007 255 557 112 059 009 445 818 132 066 228 599 999 227 277 338 388 000 019 090 091 109 113 131 190 244 311 424 442 454 544 900 901`
- **Florida4**: `038 358 033 088 335 588 338 003 087 343 333 536 316 436 032 037 009 011 077 008 355 535 553 800 433 227 272 277 388 722 727 772 838 883 353 533`
- **Connecticut4**: `349 489 344 399 448 899 298 088 424 248 224 229 444 494 249 243 099 223 228 033 588 858 885 242 422 116 161 166 611 616 661 292 922 829 888 928`
- **SouthCarolina4**: `016 156 011 066 115 566 059 224 599 499 936 005 120 125 175 155 233 338 388 449 007 070 099 244 424 442 699 700 909 969 990 996 396 444 555 579`
- **Ohio4**: `348 389 334 339 488 889 009 559 888 022 929 058 010 015 065 066 113 118 004 116 166 611 616 661 599 959 995 027 072 077 207 225 252 257 270 275`
- **NorthCarolina4**: `149 469 144 199 446 699 920 001 244 940 044 006 299 948 944 924 024 074 009 225 155 515 551 227 272 277 722 727 772 666 003 030 099 224 229 242`
- **OntarioCanada4**: `045 059 004 009 455 559 224 015 044 677 270 274 279 220 024 029 074 245 144 228 005 050 055 500 505 550 000 006 060 066 095 244 424 442 509 590`
- **Virginia4**: `045 059 004 009 455 559 361 349 042 097 341 344 597 146 169 049 047 177 199 377 449 494 499 944 949 994 001 007 010 070 100 113 131 134 143 204`
- **Indiana4**: `127 267 122 177 226 677 002 076 066 054 247 669 609 766 021 026 022 007 255 116 166 611 616 661 666 004 040 045 088 244 344 400 405 424 434 442`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only*.json` (budgeted cuts)
