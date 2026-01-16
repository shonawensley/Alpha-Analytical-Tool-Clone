# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---|---|
| PuertoRico4 | 27 | 169 | 15:022 | 022 033 088 199 | 4:022 077 088 |
| NewYork4 | 27 | 147 | 13:001 | 001 007 011 066 | 3:001 006 056 |
| Florida4 | 27 | 133 | 11:003 | 003 009 011 077 | 3:003 077 257 |
| Delaware4 | 27 | 157 | 11:009 | 009 088 117 223 | 4:004 009 449 |
| OntarioCanada4 | 27 | 164 | 11:004 | 004 044 144 228 | 3:004 027 224 |
| Michigan4 | 27 | 149 | 10:112 | 112 119 155 199 | 4:112 114 119 |
| Pennsylvania4 | 27 | 165 | 10:007 | 007 066 228 255 | 3:007 019 445 |
| Virginia4 | 27 | 174 | 10:004 | 004 177 199 377 | 3:004 177 349 |
| SouthCarolina4 | 27 | 137 | 9:115 | 115 155 224 233 | 4:115 499 566 |
| Connecticut4 | 27 | 144 | 9:088 | 088 099 223 228 | 4:088 244 448 |
| NewJersey4 | 27 | 158 | 9:022 | 022 114 155 339 | 3:011 022 127 |
| Ohio4 | 27 | 166 | 9:009 | 009 066 113 118 | 4:009 299 559 |
| NorthCarolina4 | 27 | 174 | 9:001 | 001 009 044 225 | 4:001 044 446 |
| Indiana4 | 27 | 224 | 9:002 | 002 022 177 226 | 4:002 022 066 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 088 808 880 077 707 770 225 252 522`
- **NewYork4**: `001 010 100 006 060 600 056 065 506 560 605 650`
- **Florida4**: `003 030 300 077 707 770 257 275 527 572 725 752`
- **Delaware4**: `009 090 900 004 040 400 449 494 944 559 595 955`
- **OntarioCanada4**: `004 040 400 224 242 422 027 072 207 270 702 720`
- **Michigan4**: `112 121 211 119 191 911 155 515 551 114 141 411`
- **Pennsylvania4**: `007 070 700 445 454 544 019 091 109 190 901 910`
- **Virginia4**: `004 040 400 349 394 439 493 934 943 177 717 771`
- **SouthCarolina4**: `115 151 511 599 959 995 499 949 994 566 656 665`
- **Connecticut4**: `088 808 880 244 424 442 448 484 844 449 494 944`
- **NewJersey4**: `022 202 220 127 172 217 271 712 721 011 101 110`
- **Ohio4**: `009 090 900 559 595 955 889 898 988 299 929 992`
- **NorthCarolina4**: `001 010 100 446 464 644 044 404 440 466 646 664`
- **Indiana4**: `002 020 200 066 606 660 166 616 661 022 202 220`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card__tool_only.json` (budgeted cuts)
