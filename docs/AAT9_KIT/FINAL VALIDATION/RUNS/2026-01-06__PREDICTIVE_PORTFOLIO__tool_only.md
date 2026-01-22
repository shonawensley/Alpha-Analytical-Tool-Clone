# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 30 | 193 | 14:022 | 022 033 088 199 | 1:022 | 10(6) | 10(6) |
| Ohio4 | 30 | 175 | 12:009 | 009 066 113 118 | 1:009 | 5(6) | 5(6) |
| NewJersey4 | 30 | 147 | 11:022 | 022 114 155 339 | 3:022 077 788 | 10(6) | 10(6) |
| NewYork4 | 30 | 164 | 11:001 | 001 007 011 066 | 3:001 011 066 | 2(6) | 2(6) |
| Delaware4 | 30 | 184 | 11:009 | 009 088 223 228 | 3:004 009 011 | 5(6) | 5(6) |
| Michigan4 | 30 | 145 | 10:112 | 112 119 155 199 | 3:112 117 119 | 17(6) | 17(6) |
| Pennsylvania4 | 30 | 165 | 10:007 | 007 066 228 255 | 2:007 557 | 3(6) | 3(6) |
| Florida4 | 30 | 159 | 9:003 | 003 009 011 077 | 1:003 | 18(6) | 18(6) |
| SouthCarolina4 | 30 | 172 | 9:115 | 115 155 224 233 | 2:115 224 | 20(6) | 20(6) |
| Connecticut4 | 30 | 178 | 9:088 | 088 099 223 228 | 1:088 | 31(6) | 31(6) |
| Virginia4 | 30 | 180 | 9:004 | 004 177 199 377 | 2:004 009 | 5(6) | 5(6) |
| NorthCarolina4 | 30 | 186 | 9:001 | 001 009 044 225 | 3:001 044 244 | 15(6) | 15(6) |
| OntarioCanada4 | 30 | 193 | 9:004 | 004 044 144 244 | 3:004 144 244 | 5(6) | 5(6) |
| Indiana4 | 30 | 194 | 9:002 | 002 022 177 226 | 2:002 066 | 6(6) | 6(6) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **PuertoRico4**: `022 220 202 077 027 072 522 770 270 720 216 806`
- **Ohio4**: `090 009 900 025 020 080 249 066 113 118 131 181`
- **NewJersey4**: `022 220 202 077 887 770 889 707 088 788 808 878`
- **NewYork4**: `001 010 100 011 066 110 660 008 101 606 006 060`
- **Delaware4**: `090 009 900 040 004 400 595 011 101 110 894 811`
- **Michigan4**: `112 121 211 191 118 156 119 911 117 171 711 165`
- **Pennsylvania4**: `070 007 700 575 059 557 755 020 015 416 255 525`
- **Florida4**: `003 030 300 436 636 646 008 136 433 613 631 364`
- **SouthCarolina4**: `115 151 511 224 242 422 005 297 267 696 762 007`
- **Connecticut4**: `088 808 880 727 724 794 747 024 486 684 864 224`
- **Virginia4**: `004 040 400 849 009 090 900 377 891 042 198 489`
- **NorthCarolina4**: `001 010 100 044 404 440 940 942 244 424 442 242`
- **OntarioCanada4**: `004 040 400 015 144 244 414 424 441 442 051 164`
- **Indiana4**: `002 020 200 066 606 660 061 076 766 138 244 366`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-06/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-06/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-06/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **Michigan4**: `idx(size)=17(6)` pack=`126 167 112 117 266 667` (src: `sharepacks/_predictive/2026-01-06/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-06/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-06/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-06/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-06/Connecticut4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=15(6)` pack=`049 459 044 099 445 599` (src: `sharepacks/_predictive/2026-01-06/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-06/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__vtracpack_v1.json`)

### B24 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 806 286 866 688 216 278 033 088 199 303 330 808 880 919 991 666 725 757`
- **Ohio4**: `045 059 004 009 455 559 080 022 058 098 125 025 020 249 029 092 290 920 012 017 062 066 113 118`
- **NewJersey4**: `027 257 022 077 225 577 887 889 278 088 189 188 778 829 882 087 028 072 572 114 141 155 339 393`
- **NewYork4**: `015 056 001 006 155 556 011 066 008 168 808 005 566 502 507 085 508 506 016 061 561 007 070 700`
- **Delaware4**: `045 059 004 009 455 559 449 338 011 811 854 538 894 459 088 223 228 232 282 322 808 822 880 499`
- **Michigan4**: `126 167 112 117 266 667 156 191 118 168 169 135 277 138 198 268 123 128 178 155 199 515 551 919`
- **Pennsylvania4**: `025 057 002 007 255 557 561 000 059 015 416 066 228 001 777 227 272 277 338 383 388 722 727 772`
- **Florida4**: `136 168 113 118 366 668 436 003 008 433 034 646 023 028 073 009 011 077 090 101 110 707 770 900`
- **SouthCarolina4**: `127 267 122 177 226 677 115 005 224 696 007 567 297 015 012 017 062 125 152 251 521 155 233 323`
- **Connecticut4**: `249 479 244 299 447 799 088 248 727 024 224 486 784 724 747 029 074 099 223 228 232 282 322 822`
- **Virginia4**: `045 059 004 009 455 559 849 891 042 097 377 499 399 899 047 079 790 970 177 199 717 737 771 773`
- **NorthCarolina4**: `049 459 044 099 445 599 092 001 942 242 292 244 469 240 074 009 090 225 252 522 900 006 060 155`
- **OntarioCanada4**: `045 059 004 009 455 559 015 247 014 144 244 174 164 019 064 145 154 451 541 044 404 440 090 545`
- **Indiana4**: `016 156 011 066 115 566 076 002 138 244 224 366 447 036 386 683 836 061 766 021 026 067 670 760`

### B36 (vtrac_pack_boxed_first)

- **PuertoRico4**: `027 257 022 077 225 577 806 286 866 688 216 278 033 088 199 666 003 006 066 224 244 300 422 424 442 600 606 660 668 686 868 886 145 154 415 451`
- **Ohio4**: `045 059 004 009 455 559 080 022 058 098 125 025 020 249 029 012 017 062 066 113 118 131 181 311 606 660 811 040 400 595 955 116 161 166 611 616`
- **NewJersey4**: `027 257 022 077 225 577 887 889 278 088 189 188 778 829 882 087 028 114 155 339 888 227 272 277 722 727 772 449 494 499 944 949 994 008 080 198`
- **NewYork4**: `015 056 001 006 155 556 011 066 008 168 808 005 566 502 507 085 016 561 007 449 499 944 949 994 666 113 118 131 136 163 181 311 316 361 366 613`
- **Delaware4**: `045 059 004 009 455 559 449 338 011 811 854 538 894 459 088 223 228 499 003 334 335 343 344 353 433 434 443 533 058 085 145 154 333 358 385 415`
- **Michigan4**: `126 167 112 117 266 667 156 191 118 168 169 135 277 138 198 268 123 128 178 155 199 515 551 919 991 626 662 449 494 499 944 949 994 688 868 886`
- **Pennsylvania4**: `025 057 002 007 255 557 561 000 059 015 416 066 228 001 777 227 277 338 388 009 122 212 221 224 242 422 445 454 455 544 545 554 900 222 789 798`
- **Florida4**: `136 168 113 118 366 668 436 003 008 433 034 646 023 028 073 009 011 077 355 227 277 338 383 388 722 727 772 833 838 883 224 242 336 363 422 633`
- **SouthCarolina4**: `127 267 122 177 226 677 115 005 224 696 007 567 297 015 012 017 062 125 155 233 011 101 110 566 656 665 555 338 383 388 449 494 499 833 838 883`
- **Connecticut4**: `249 479 244 299 447 799 088 248 727 024 224 486 784 724 747 029 074 099 223 228 033 303 330 588 858 885 242 422 424 442 116 161 166 611 616 661`
- **Virginia4**: `045 059 004 009 455 559 849 891 042 097 377 499 399 899 047 177 199 449 007 008 224 242 244 402 422 424 442 557 575 595 700 755 800 955 111 279`
- **NorthCarolina4**: `049 459 044 099 445 599 092 001 942 242 292 244 469 240 074 009 225 006 155 227 277 722 727 772 422 922 126 162 216 246 261 264 426 462 612 621`
- **OntarioCanada4**: `045 059 004 009 455 559 015 247 014 144 244 174 164 019 064 145 044 005 055 177 111 105 401 459 477 495 501 549 594 595 747 774 945 954 955 147`
- **Indiana4**: `016 156 011 066 115 566 076 002 138 244 224 366 447 036 386 766 021 026 022 177 226 262 622 717 771 007 070 255 525 552 700 116 161 166 611 616`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card__tool_only*.json` (budgeted cuts)
