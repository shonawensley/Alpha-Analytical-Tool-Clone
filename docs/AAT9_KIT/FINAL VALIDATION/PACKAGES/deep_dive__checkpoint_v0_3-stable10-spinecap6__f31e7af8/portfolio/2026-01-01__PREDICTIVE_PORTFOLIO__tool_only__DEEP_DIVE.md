# Predictive Portfolio — D=2026-01-01

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-01/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Ohio4 | 27 | 183 | 12:009 | 009 066 113 114 | 1:009 | 3(6) | idx[20]:1,2,3,5…(36) |
| NorthCarolina4 | 27 | 212 | 11:001 | 001 009 044 225 | 4:001 009 044 | 11(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 273 | 11:022 | 022 033 088 199 | 3:022 224 225 | 10(6) | idx[20]:2,7,10,11…(36) |
| NewJersey4 | 27 | 165 | 10:022 | 022 114 155 339 | 2:022 225 | 28(6) | idx[20]:1,2,10,15…(36) |
| Connecticut4 | 27 | 211 | 10:088 | 088 099 223 228 | 4:001 003 008 | 4(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | 27 | 217 | 10:009 | 009 088 223 228 | 1:009 | 9(8) | idx[20]:1,2,5,6…(36) |
| SouthCarolina4 | 27 | 173 | 9:115 | 115 155 224 288 | 3:011 115 224 | 2(6) | idx[20]:1,2,3,4…(36) |
| Virginia4 | 27 | 190 | 9:004 | 004 177 199 377 | 3:004 177 339 | 22(8) | idx[20]:2,3,4,5…(36) |
| Florida4 | 27 | 199 | 9:003 | 003 008 009 011 | 4:003 008 011 | 11(8) | idx[24]:3,4,5,6…(36) |
| Michigan4 | 27 | 203 | 9:112 | 112 119 155 199 | 3:112 155 559 | 18(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | 27 | 208 | 9:004 | 004 044 144 244 | 2:004 244 | 19(6) | idx[20]:5,6,7,9…(36) |
| Indiana4 | 27 | 221 | 9:002 | 002 022 177 226 | 3:002 007 177 | 7(8) | idx[20]:2,3,4,6…(36) |
| NewYork4 | 27 | 221 | 9:001 | 001 007 011 066 | 3:001 006 066 | 6(6) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | 27 | 226 | 9:007 | 007 228 255 277 | 2:007 138 | 23(6) | idx[20]:3,4,5,11…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Ohio4**: `090 009 900 570 059 075 057 077 095 590 707 750`
- **NorthCarolina4**: `001 010 100 044 404 440 344 434 443 009 090 900`
- **PuertoRico4**: `022 202 220 224 225 252 522 242 422 144 199 919`
- **NewJersey4**: `202 022 220 297 792 225 252 522 279 972 929 989`
- **Connecticut4**: `088 808 880 001 008 003 010 030 080 100 300 800`
- **Delaware4**: `009 090 900 141 191 114 014 194 168 186 618 681`
- **SouthCarolina4**: `115 151 511 138 011 183 831 224 242 422 101 110`
- **Virginia4**: `004 040 400 177 717 771 377 197 339 393 933 334`
- **Florida4**: `003 030 300 008 080 800 011 101 110 077 707 770`
- **Michigan4**: `112 121 211 155 515 551 559 595 955 105 368 565`
- **OntarioCanada4**: `004 040 400 114 181 118 244 424 442 168 186 618`
- **Indiana4**: `002 020 200 066 676 056 177 717 771 007 070 700`
- **NewYork4**: `001 010 100 066 660 677 606 011 006 060 600 077`
- **Pennsylvania4**: `007 070 700 138 183 318 381 813 831 357 378 387`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-01/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 027 257 022 077 247 279 224 229 259 056 244 368 099 068 066 113 114 055 699 388 677 116 178 449` (src: `sharepacks/_predictive/2026-01-01/Ohio4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`247 279 224 229 477 779 015 056 001 006 155 556 034 039 048 089 023 028 037 078 044 225 344 244 003 009 144 243 005 007 240 232 011 033 667 233` (src: `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-01/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,7,10,11…(36)` pack=`027 257 022 077 225 577 149 469 144 199 446 699 247 279 224 229 023 028 037 078 136 223 236 233 134 226 344 244 033 624 445 026 234 334 001 116` (src: `sharepacks/_predictive/2026-01-01/PuertoRico4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=28(6)` pack=`247 279 224 229 477 779` (src: `sharepacks/_predictive/2026-01-01/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,10,15…(36)` pack=`027 257 022 077 225 577 247 279 224 229 477 779 249 479 244 299 237 278 223 228 339 289 238 118 127 138 182 599 155 114 989 272 199 449 005 189` (src: `sharepacks/_predictive/2026-01-01/NewJersey4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-01/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`038 358 033 088 335 588 035 058 003 008 355 558 013 018 036 068 237 278 223 228 025 386 144 224 388 702 093 099 687 001 559 334 189 116 117 704` (src: `sharepacks/_predictive/2026-01-01/Connecticut4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-01/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,5,6…(36)` pack=`149 469 144 199 446 699 146 169 114 119 466 669 014 019 046 069 045 059 004 009 244 344 168 171 001 599 499 223 017 018 088 011 224 005 134 338` (src: `sharepacks/_predictive/2026-01-01/Delaware4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-01/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 138 368 133 188 013 018 036 068 181 938 038 119 338 198 224 009 288 008 599 007 244 449 005 227` (src: `sharepacks/_predictive/2026-01-01/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-01/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`124 129 147 179 246 269 127 267 122 177 226 677 045 059 004 009 136 168 113 118 399 337 133 339 224 015 057 035 358 199 377 244 117 599 517 397` (src: `sharepacks/_predictive/2026-01-01/Virginia4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-01/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[24]:3,4,5,6…(36)` pack=`023 028 037 078 235 258 338 388 016 156 011 066 035 058 003 008 138 114 077 767 778 113 167 279 769 009 337 057 116 088 449 790 244 599 699 399` (src: `sharepacks/_predictive/2026-01-01/Florida4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-01/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 136 168 113 118 366 668 138 368 133 188 126 167 112 117 013 019 335 355 016 346 559 119 244 338 199 002 224 599 166 055` (src: `sharepacks/_predictive/2026-01-01/Michigan4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-01/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:5,6,7,9…(36)` pack=`136 168 113 118 366 668 146 169 114 119 466 669 138 368 133 188 045 059 004 009 884 115 718 484 014 244 157 022 449 144 044 189 161 224 226 824` (src: `sharepacks/_predictive/2026-01-01/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-01/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,6…(36)` pack=`025 057 002 007 255 557 012 017 026 067 125 157 127 267 122 177 016 156 011 066 676 386 056 224 022 146 668 144 244 033 079 116 445 377 558 788` (src: `sharepacks/_predictive/2026-01-01/Indiana4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-01/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`016 156 011 066 115 566 015 056 001 006 155 556 136 168 113 118 247 279 224 229 607 045 077 984 007 677 244 687 334 987 667 116 599 778 149 688` (src: `sharepacks/_predictive/2026-01-01/NewYork4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,11…(36)` pack=`025 057 002 007 255 557 138 368 133 188 336 688 127 267 122 177 035 058 003 008 357 228 378 334 038 079 338 559 277 379 359 113 117 317 399 468` (src: `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Ohio4**: `025 057 002 007 255 557 090 059 077 559 099 224 027 056 257 270 275 279 297 506 527 572 605 702`
- **NorthCarolina4**: `023 028 037 078 235 258 357 578 001 344 034 240 044 244 242 003 224 009 090 900 006 060 600 232`
- **PuertoRico4**: `027 257 022 077 225 577 224 144 199 136 226 236 334 134 469 496 624 649 694 946 964 223 232 322`
- **NewJersey4**: `247 279 224 229 477 779 202 929 989 272 225 182 282 289 924 928 982 118 249 294 492 942 278 742`
- **Connecticut4**: `035 058 003 008 355 558 088 001 018 116 388 386 338 788 093 687 867 903 011 068 508 702 720 728`
- **Delaware4**: `014 019 046 069 145 159 456 569 009 499 141 191 194 004 559 449 494 944 949 994 119 411 911 144`
- **SouthCarolina4**: `015 056 001 006 155 556 138 011 115 180 224 181 198 338 388 838 883 168 186 618 681 816 861 188`
- **Virginia4**: `124 129 147 179 246 269 467 679 177 004 377 117 399 339 349 334 337 343 373 433 733 311 113 366`
- **Florida4**: `023 028 037 078 235 258 357 578 338 388 003 008 011 077 778 767 769 138 183 813 831 188 688 377`
- **Michigan4**: `136 168 113 118 366 668 155 112 559 006 338 133 335 355 105 368 565 506 605 358 131 186 681 119`
- **OntarioCanada4**: `146 169 114 119 466 669 004 181 244 188 168 884 718 161 484 449 494 944 164 183 813 189 184 841`
- **Indiana4**: `012 017 026 067 125 157 256 567 386 002 066 676 056 177 007 116 161 611 368 638 863 606 660 667`
- **NewYork4**: `016 156 011 066 115 566 001 677 668 006 077 778 607 977 687 116 067 076 160 610 670 760 984 987`
- **Pennsylvania4**: `138 368 133 188 336 688 007 338 357 277 388 378 717 037 057 073 075 370 375 570 573 730 750 753`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Ohio4**: `045 059 004 009 455 559 025 057 002 007 255 557 027 257 022 077 247 279 224 229 259 056 244 368 099 068 066 113 114 055 699 388 677 116 178 449`
- **NorthCarolina4**: `247 279 224 229 477 779 015 056 001 006 155 556 034 039 048 089 023 028 037 078 044 225 344 244 003 009 144 243 005 007 240 232 011 033 667 233`
- **PuertoRico4**: `027 257 022 077 225 577 149 469 144 199 446 699 247 279 224 229 023 028 037 078 136 223 236 233 134 226 344 244 033 624 445 026 234 334 001 116`
- **NewJersey4**: `027 257 022 077 225 577 247 279 224 229 477 779 249 479 244 299 237 278 223 228 339 289 238 118 127 138 182 599 155 114 989 272 199 449 005 189`
- **Connecticut4**: `038 358 033 088 335 588 035 058 003 008 355 558 013 018 036 068 237 278 223 228 025 386 144 224 388 702 093 099 687 001 559 334 189 116 117 704`
- **Delaware4**: `149 469 144 199 446 699 146 169 114 119 466 669 014 019 046 069 045 059 004 009 244 344 168 171 001 599 499 223 017 018 088 011 224 005 134 338`
- **SouthCarolina4**: `015 056 001 006 155 556 016 156 011 066 115 566 138 368 133 188 013 018 036 068 181 938 038 119 338 198 224 009 288 008 599 007 244 449 005 227`
- **Virginia4**: `124 129 147 179 246 269 127 267 122 177 226 677 045 059 004 009 136 168 113 118 399 337 133 339 224 015 057 035 358 199 377 244 117 599 517 397`
- **Florida4**: `023 028 037 078 235 258 338 388 016 156 011 066 035 058 003 008 138 114 077 767 778 113 167 279 769 009 337 057 116 088 449 790 244 599 699 399`
- **Michigan4**: `015 056 001 006 155 556 136 168 113 118 366 668 138 368 133 188 126 167 112 117 013 019 335 355 016 346 559 119 244 338 199 002 224 599 166 055`
- **OntarioCanada4**: `136 168 113 118 366 668 146 169 114 119 466 669 138 368 133 188 045 059 004 009 884 115 718 484 014 244 157 022 449 144 044 189 161 224 226 824`
- **Indiana4**: `025 057 002 007 255 557 012 017 026 067 125 157 127 267 122 177 016 156 011 066 676 386 056 224 022 146 668 144 244 033 079 116 445 377 558 788`
- **NewYork4**: `016 156 011 066 115 566 015 056 001 006 155 556 136 168 113 118 247 279 224 229 607 045 077 984 007 677 244 687 334 987 667 116 599 778 149 688`
- **Pennsylvania4**: `025 057 002 007 255 557 138 368 133 188 336 688 127 267 122 177 035 058 003 008 357 228 378 334 038 079 338 559 277 379 359 113 117 317 399 468`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-01/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-01/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-01/<STATE>/play_card__tool_only*.json` (budgeted cuts)
