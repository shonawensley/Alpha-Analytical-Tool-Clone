# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 30 | 181 | 15:022 | 022 033 088 199 | 2:022 088 | 10(6) | 10(6) |
| NewYork4 | 30 | 152 | 13:001 | 001 007 011 066 | 3:001 005 006 | 2(6) | 2(6) |
| Florida4 | 30 | 141 | 11:003 | 003 009 011 077 | 2:003 077 | 4(6) | 4(6) |
| Delaware4 | 30 | 174 | 11:009 | 009 088 117 223 | 3:004 009 445 | 5(6) | 5(6) |
| OntarioCanada4 | 30 | 176 | 11:004 | 004 044 144 228 | 2:004 224 | 5(6) | 5(6) |
| Michigan4 | 30 | 167 | 10:112 | 112 119 155 199 | 2:112 119 | 22(8) | 22(8) |
| Pennsylvania4 | 30 | 174 | 10:007 | 007 066 228 255 | 2:007 112 | 3(6) | 3(6) |
| Virginia4 | 30 | 184 | 10:004 | 004 177 199 377 | 1:004 | 5(6) | 5(6) |
| SouthCarolina4 | 30 | 141 | 9:115 | 115 155 224 233 | 2:115 499 | 15(6) | 15(6) |
| Connecticut4 | 30 | 147 | 9:088 | 088 099 223 228 | 3:088 244 448 | 30(8) | 30(8) |
| NewJersey4 | 30 | 166 | 9:022 | 022 114 155 339 | 1:022 | 10(6) | 10(6) |
| Ohio4 | 30 | 179 | 9:009 | 009 066 113 118 | 3:009 559 889 | 5(6) | 5(6) |
| NorthCarolina4 | 30 | 181 | 9:001 | 001 009 044 225 | 3:001 044 446 | 25(6) | 25(6) |
| Indiana4 | 30 | 234 | 9:002 | 002 022 177 226 | 3:002 066 166 | 19(6) | 19(6) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **PuertoRico4**: `220 022 202 088 808 880 077 207 027 072 572 522`
- **NewYork4**: `010 001 100 060 006 600 065 560 005 050 500 507`
- **Florida4**: `030 003 300 077 707 770 752 757 045 080 355 535`
- **Delaware4**: `090 009 900 040 494 004 400 595 445 454 544 404`
- **OntarioCanada4**: `040 004 400 224 242 422 270 274 279 090 455 545`
- **Michigan4**: `112 121 211 119 191 911 155 051 141 059 590 174`
- **Pennsylvania4**: `070 007 700 445 019 112 121 211 020 416 255 525`
- **Virginia4**: `004 040 400 349 394 493 943 361 136 169 364 439`
- **SouthCarolina4**: `115 151 511 599 499 949 994 059 095 509 590 905`
- **Connecticut4**: `088 808 880 244 844 294 894 984 424 442 448 484`
- **NewJersey4**: `022 202 220 127 126 110 112 037 703 014 089 172`
- **Ohio4**: `009 090 900 559 595 955 889 898 988 849 538 835`
- **NorthCarolina4**: `001 010 100 644 044 404 440 446 464 940 646 690`
- **Indiana4**: `002 020 200 066 606 660 166 616 661 022 177 202`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-09/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **Michigan4**: `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=15(6)` pack=`049 459 044 099 445 599` (src: `sharepacks/_predictive/2026-01-09/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=30(8)` pack=`234 239 248 289 347 379 478 789` (src: `sharepacks/_predictive/2026-01-09/Connecticut4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=25(6)` pack=`149 469 144 199 446 699` (src: `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-09/Indiana4/play_card__tool_only__vtracpack_v1.json`)

### B24 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 068 088 800 188 018 205 278 280 033 199 303 330 919 991 008 080 757 775`
- **NewYork4**: `015 056 001 006 155 556 000 256 005 504 118 507 508 007 011 066 070 101 110 606 660 700 449 494`
- **Florida4**: `035 058 003 008 355 558 536 077 727 364 752 757 045 057 347 357 085 530 580 009 011 090 101 110`
- **Delaware4**: `045 059 004 009 455 559 494 444 434 445 313 414 413 404 156 049 094 459 490 495 594 940 954 088`
- **OntarioCanada4**: `045 059 004 009 455 559 224 055 260 634 111 349 489 015 270 274 279 049 094 490 940 540 950 044`
- **Michigan4**: `124 129 147 179 246 269 467 679 112 119 155 019 093 277 051 141 059 590 192 291 921 199 515 551`
- **Pennsylvania4**: `025 057 002 007 255 557 059 445 019 138 112 416 066 228 227 272 277 338 383 388 722 727 772 833`
- **Virginia4**: `045 059 004 009 455 559 349 364 039 361 169 341 049 034 084 093 390 930 177 199 377 717 737 771`
- **SouthCarolina4**: `049 459 044 099 445 599 499 115 059 645 195 665 595 694 894 495 594 954 695 140 145 159 591 951`
- **Connecticut4**: `234 239 248 289 347 379 478 789 294 244 088 844 894 242 494 438 834 489 498 243 099 223 228 232`
- **NewJersey4**: `027 257 022 077 225 577 127 017 278 037 014 089 055 078 126 110 112 172 271 721 120 012 062 071`
- **Ohio4**: `045 059 004 009 455 559 938 889 878 929 058 849 538 088 010 015 065 510 560 066 113 118 131 181`
- **NorthCarolina4**: `149 469 144 199 446 699 001 940 690 044 646 349 244 299 920 194 049 094 490 640 041 046 069 960`
- **Indiana4**: `146 169 114 119 466 669 002 062 166 069 066 596 045 012 017 026 260 620 022 177 202 220 226 262`

### B36 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 068 088 800 188 018 205 278 280 033 199 006 066 688 111 268 286 628 666 682 801 826 862 004 009 040 045 054 059 090 095`
- **NewYork4**: `015 056 001 006 155 556 000 256 005 504 118 507 508 007 011 066 449 499 555 227 277 722 727 772 004 008 040 045 054 080 224 242 244 255 400 405`
- **Florida4**: `035 058 003 008 355 558 536 077 727 364 752 757 045 057 347 357 009 011 333 227 338 383 388 722 772 833 838 883 559 595 955 033 055 224 242 255`
- **Delaware4**: `045 059 004 009 455 559 494 444 434 445 313 414 413 404 156 049 459 088 117 223 499 949 994 003 030 033 133 144 300 303 330 331 334 339 343 393`
- **OntarioCanada4**: `045 059 004 009 455 559 224 055 260 634 111 349 489 015 270 274 279 049 044 144 228 282 404 414 440 441 822 900 005 050 500 006 033 056 060 065`
- **Michigan4**: `124 129 147 179 246 269 467 679 112 119 155 019 093 277 051 141 059 199 117 266 449 499 944 949 994 001 010 100 338 383 388 833 838 883 044 091`
- **Pennsylvania4**: `025 057 002 007 255 557 059 445 019 138 112 416 066 228 227 277 338 388 001 009 113 114 119 131 141 190 191 244 311 411 424 442 454 544 900 901`
- **Virginia4**: `045 059 004 009 455 559 349 364 039 361 169 341 049 034 084 177 199 377 449 499 024 033 042 095 113 131 204 240 303 311 330 336 363 402 420 509`
- **SouthCarolina4**: `049 459 044 099 445 599 499 115 059 645 195 665 595 694 894 695 140 145 155 224 233 242 323 332 422 515 551 011 101 110 566 656 449 494 944 555`
- **Connecticut4**: `234 239 248 289 347 379 478 789 294 244 088 844 894 242 494 438 099 223 228 033 588 116 161 166 611 616 661 229 292 922 847 144 149 194 199 227`
- **NewJersey4**: `027 257 022 077 225 577 127 017 278 037 014 089 055 078 126 110 112 120 062 114 155 339 393 411 515 551 933 252 522 707 770 227 272 277 722 727`
- **Ohio4**: `045 059 004 009 455 559 938 889 878 929 058 849 538 088 010 015 065 066 113 118 116 161 166 611 616 661 599 959 995 999 022 027 072 077 202 207`
- **NorthCarolina4**: `149 469 144 199 446 699 001 940 690 044 646 349 244 299 920 640 041 009 225 006 155 515 551 600 227 272 277 722 727 772 466 664 444 066 099 229`
- **Indiana4**: `146 169 114 119 466 669 002 062 166 069 066 596 045 012 017 022 177 226 007 255 116 161 611 666 004 040 057 075 244 344 388 400 424 434 442 443`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card__tool_only*.json` (budgeted cuts)
