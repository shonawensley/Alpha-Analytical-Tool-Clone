# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Michigan4 | 30 | 128 | 12:112 | 112 119 155 199 | 2:112 119 | 17(6) | 17(6) |
| PuertoRico4 | 30 | 193 | 12:022 | 022 033 088 199 | 2:022 033 | 10(6) | 10(6) |
| NewYork4 | 30 | 151 | 11:001 | 001 007 011 066 | 3:001 006 066 | 2(6) | 2(6) |
| Pennsylvania4 | 30 | 161 | 11:007 | 007 066 228 255 | 2:007 059 | 3(6) | 3(6) |
| Ohio4 | 30 | 163 | 11:009 | 009 066 113 118 | 2:009 559 | 5(6) | 5(6) |
| NewJersey4 | 30 | 170 | 11:022 | 022 114 155 339 | 1:022 | 10(6) | 10(6) |
| Delaware4 | 30 | 172 | 11:009 | 009 088 223 228 | 3:004 009 559 | 5(6) | 5(6) |
| OntarioCanada4 | 30 | 178 | 11:004 | 004 044 144 244 | 2:004 244 | 5(6) | 5(6) |
| Florida4 | 30 | 155 | 9:003 | 003 008 009 011 | 3:003 008 344 | 34(6) | 34(6) |
| SouthCarolina4 | 30 | 174 | 9:115 | 115 155 224 233 | 3:115 224 599 | 28(6) | 28(6) |
| Virginia4 | 30 | 181 | 9:004 | 004 177 199 377 | 4:004 377 455 | 5(6) | 5(6) |
| Indiana4 | 30 | 187 | 9:002 | 002 022 177 226 | 2:002 066 | 18(6) | 18(6) |
| NorthCarolina4 | 30 | 191 | 9:001 | 001 009 044 225 | 2:001 044 | 31(6) | 31(6) |
| Connecticut4 | 30 | 200 | 9:088 | 088 099 223 228 | 2:088 277 | 12(8) | 12(8) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **Michigan4**: `121 112 211 168 160 165 186 681 156 119 191 911`
- **PuertoRico4**: `022 202 220 033 303 330 206 232 237 273 372 732`
- **NewYork4**: `001 010 100 066 660 800 606 006 060 600 011 008`
- **Pennsylvania4**: `070 007 700 059 095 590 015 075 570 509 905 950`
- **Ohio4**: `090 009 900 059 559 595 955 590 058 850 050 010`
- **NewJersey4**: `022 220 202 297 792 279 077 882 889 522 770 229`
- **Delaware4**: `090 009 900 040 004 400 594 595 511 984 559 955`
- **OntarioCanada4**: `040 004 400 244 424 442 164 194 774 090 455 545`
- **Florida4**: `003 030 300 434 008 080 800 344 443 084 033 594`
- **SouthCarolina4**: `115 151 511 224 242 422 599 959 995 275 297 267`
- **Virginia4**: `004 040 400 377 737 773 455 545 554 559 595 955`
- **Indiana4**: `002 020 200 066 606 660 076 626 676 686 636 026`
- **NorthCarolina4**: `001 010 100 044 404 440 522 294 242 244 224 049`
- **Connecticut4**: `088 808 880 727 724 747 744 024 277 772 099 223`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **Michigan4**: `idx(size)=17(6)` pack=`126 167 112 117 266 667` (src: `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-05/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-05/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-05/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=28(6)` pack=`247 279 224 229 477 779` (src: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-05/Connecticut4/play_card__tool_only__vtracpack_v1.json`)

### B24 (vtrac_pack_boxed_first)

- **Michigan4**: `126 167 112 117 266 667 160 168 165 119 661 668 169 161 138 386 831 176 621 671 155 199 515 551`
- **PuertoRico4**: `027 257 022 077 225 577 206 276 232 268 237 073 033 226 278 287 327 723 728 782 827 872 223 322`
- **NewYork4**: `015 056 001 006 155 556 066 011 800 805 250 168 500 808 667 065 560 605 650 067 016 061 561 007`
- **Pennsylvania4**: `025 057 002 007 255 557 059 015 005 055 167 056 066 228 599 959 995 777 227 272 277 338 383 388`
- **Ohio4**: `045 059 004 009 455 559 058 010 080 088 225 038 050 060 015 065 510 560 066 113 118 131 181 311`
- **NewJersey4**: `027 257 022 077 225 577 297 229 299 778 418 984 882 889 114 141 155 339 393 411 515 551 933 252`
- **Delaware4**: `045 059 004 009 455 559 594 449 499 058 388 814 511 984 149 459 495 954 088 223 228 232 282 322`
- **OntarioCanada4**: `045 059 004 009 455 559 244 774 174 459 161 267 164 194 247 540 950 044 144 404 414 440 441 900`
- **Florida4**: `349 489 344 399 448 899 034 084 003 594 008 033 054 136 038 083 348 380 384 483 830 843 734 039`
- **SouthCarolina4**: `247 279 224 229 477 779 115 275 599 003 015 227 277 135 267 762 123 128 173 155 233 323 332 515`
- **Virginia4**: `045 059 004 009 455 559 377 597 097 888 489 599 055 561 092 592 042 047 079 790 970 177 199 717`
- **Indiana4**: `136 168 113 118 366 668 076 002 066 026 188 224 244 447 666 138 386 683 813 831 836 626 676 267`
- **NorthCarolina4**: `249 479 244 299 447 799 029 044 001 522 242 540 500 192 264 291 941 049 094 490 492 940 942 240`
- **Connecticut4**: `024 029 047 079 245 259 457 579 088 727 744 644 694 028 724 747 074 099 223 228 232 282 322 822`

### B36 (vtrac_pack_boxed_first)

- **Michigan4**: `126 167 112 117 266 667 160 168 165 119 661 668 169 161 138 386 155 199 449 499 338 383 388 833 838 883 011 101 110 118 166 181 244 424 442 616`
- **PuertoRico4**: `027 257 022 077 225 577 206 276 232 268 237 073 033 226 278 216 230 028 088 199 002 003 020 030 200 224 242 262 300 344 422 434 443 622 688 868`
- **NewYork4**: `015 056 001 006 155 556 066 011 800 805 250 168 500 808 667 067 016 561 007 449 499 944 949 994 113 118 131 136 163 181 311 316 361 366 613 618`
- **Pennsylvania4**: `025 057 002 007 255 557 059 015 005 055 167 056 066 228 599 777 227 277 338 388 455 545 554 126 162 216 261 578 579 587 597 612 621 758 759 785`
- **Ohio4**: `045 059 004 009 455 559 058 010 080 088 225 038 050 060 015 065 066 113 118 116 166 611 616 661 800 808 880 022 027 072 077 202 207 220 257 270`
- **NewJersey4**: `027 257 022 077 225 577 297 229 299 778 418 984 882 889 114 155 339 227 277 449 499 944 949 994 008 011 080 088 101 110 244 292 424 442 488 559`
- **Delaware4**: `045 059 004 009 455 559 594 449 499 058 388 814 511 984 149 088 223 228 888 003 244 300 334 343 389 398 424 433 442 588 839 858 885 893 938 983`
- **OntarioCanada4**: `045 059 004 009 455 559 244 774 174 459 161 267 164 194 247 044 144 005 055 177 224 242 422 549 599 717 771 945 955 959 995 047 074 111 147 158`
- **Florida4**: `349 489 344 399 448 899 034 084 003 594 008 033 054 136 038 348 734 039 009 011 355 535 553 338 383 388 833 838 883 227 272 277 722 727 772 138`
- **SouthCarolina4**: `247 279 224 229 477 779 115 275 599 003 015 227 277 135 267 123 128 173 155 233 011 101 110 566 656 665 777 338 383 388 449 494 499 833 838 883`
- **Virginia4**: `045 059 004 009 455 559 377 597 097 888 489 599 055 561 092 592 042 047 177 199 449 494 499 944 949 994 002 008 020 080 200 224 242 248 284 334`
- **Indiana4**: `136 168 113 118 366 668 076 002 066 026 188 224 244 447 666 138 386 626 676 267 021 067 670 760 022 177 202 220 226 262 622 717 771 007 070 255`
- **NorthCarolina4**: `249 479 244 299 447 799 029 044 001 522 242 540 500 192 264 941 049 240 542 074 009 090 225 252 900 006 060 155 515 551 600 422 227 272 277 722`
- **Connecticut4**: `024 029 047 079 245 259 457 579 088 727 744 644 694 028 724 747 099 223 228 033 588 116 161 166 611 616 661 224 242 422 777 001 004 010 040 100`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card__tool_only*.json` (budgeted cuts)
