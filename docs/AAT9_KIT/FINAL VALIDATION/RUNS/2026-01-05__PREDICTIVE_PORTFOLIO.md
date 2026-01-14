# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Starts from Control Center Profit Alerts (bet-ready) and annotates with Candidate Universe size.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|
| NewJersey4 | 5 | 13 | Combined:A11:BOX:028(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:028(6) | 37 | 172 | 022 114 155 339 | 3:022 389 889 |
| SouthCarolina4 | 5 | 12 | Combined:A11:BOX:259(6); Midday:A05:STR8_3:007(3); Combined:A10:STR8_3:115(3) | 37 | 185 | 115 155 224 233 | 3:115 224 267 |
| Virginia4 | 4 | 13 | Combined:A11:BOX:089(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:089(6) | 36 | 174 | 004 177 199 377 | 3:004 156 377 |
| PuertoRico4 | 4 | 12 | Midday:A05:STR8_3:003(3); Midday:A01:BOX:036(6); Midday:A01:BOX:036(6) | 36 | 210 | 022 033 088 199 | 3:003 022 026 |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 36 | 191 | 001 009 044 225 | 3:001 044 249 |
| Pennsylvania4 | 3 | 11 | Combined:A05:STR8_3:055(3); Combined:A09:STR8_8:034(8); Midday:A04:BOX:059(6) | 35 | 159 | 007 066 228 255 | 3:007 055 059 |
| NewYork4 | 3 | 11 | Midday:A05:STR8_3:066(3); Midday:A09:STR8_8:234(8); Midday:A04:BOX:056(6) | 35 | 166 | 001 007 011 066 | 3:001 056 066 |
| OntarioCanada4 | 3 | 11 | Combined:A10:STR8_3:255(3); Midday:A05:STR8_3:244(3); Evening:A04:BOX:459(6) | 35 | 170 | 004 044 144 244 | 3:004 244 459 |
| Connecticut4 | 3 | 11 | Evening:A05:STR8_8:024(8); Evening:A09:STR8_8:113(8); Evening:A04:BOX:024(6) | 35 | 214 | 088 099 223 228 | 3:088 247 277 |
| Michigan4 | 3 | 10 | Combined:A05:STR8_3:011(3); Combined:A10:STR8_3:566(3); Combined:A04:BOX:168(6) | 35 | 138 | 112 119 155 199 | 2:016 168 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:467(6) | 35 | 164 | 003 008 009 011 | 3:003 033 348 |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:599(3); Combined:A12:STR8_4of8:088(4); Combined:A04:BOX:259(6) | 35 | 165 | 009 066 113 118 | 4:009 088 559 |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:244(3); Midday:A12:STR8_4of8:066(4); Midday:A04:BOX:368(6) | 35 | 181 | 002 022 177 226 | 4:002 022 066 |
| Delaware4 | 2 | 7 | Evening:A05:STR8_3:449(3); Combined:A04:BOX:058(6) | 34 | 179 | 009 088 223 228 | 4:004 009 449 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **NewJersey4**: `389 398 839 893 938 983 022 202 220 889 898 988`
- **SouthCarolina4**: `115 151 511 224 242 422 267 276 627 672 726 762`
- **Virginia4**: `004 040 400 156 165 516 561 615 651 377 737 773`
- **PuertoRico4**: `022 202 220 026 062 206 260 602 620 003 030 300`
- **NorthCarolina4**: `044 404 440 001 010 100 249 294 429 492 924 942`
- **Pennsylvania4**: `059 095 509 590 905 950 007 070 700 055 505 550`
- **NewYork4**: `001 010 100 066 606 660 056 065 506 560 605 650`
- **OntarioCanada4**: `244 424 442 004 040 400 459 495 549 594 945 954`
- **Connecticut4**: `088 808 880 247 274 427 472 724 742 277 727 772`
- **Michigan4**: `168 186 618 681 816 861 016 061 106 160 601 610`
- **Florida4**: `348 384 438 483 834 843 003 030 300 033 303 330`
- **Ohio4**: `009 090 900 599 959 995 088 808 880 559 595 955`
- **Indiana4**: `066 606 660 244 424 442 002 020 200 022 202 220`
- **Delaware4**: `009 090 900 004 040 400 449 494 944 559 595 955`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical “what to play” remains:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card.json` (budgeted cuts)
