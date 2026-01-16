# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---|---|
| PuertoRico4 | 27 | 178 | 15:022 | 022 033 199 299 | 3:022 027 077 |
| NewYork4 | 27 | 138 | 13:001 | 001 007 011 066 | 4:001 005 006 |
| NewJersey4 | 27 | 155 | 11:022 | 022 114 155 339 | 3:022 077 168 |
| Delaware4 | 27 | 163 | 11:009 | 009 088 223 228 | 4:004 009 011 |
| Michigan4 | 27 | 150 | 10:112 | 112 119 155 199 | 4:112 114 119 |
| Pennsylvania4 | 27 | 165 | 10:007 | 007 066 228 255 | 4:002 007 112 |
| Florida4 | 27 | 133 | 9:003 | 003 009 011 077 | 4:003 033 335 |
| Connecticut4 | 27 | 147 | 9:088 | 088 099 223 228 | 4:088 244 448 |
| SouthCarolina4 | 27 | 156 | 9:115 | 115 155 224 233 | 4:115 224 566 |
| Ohio4 | 27 | 161 | 9:009 | 009 066 113 118 | 4:009 299 559 |
| NorthCarolina4 | 27 | 170 | 9:001 | 001 009 044 225 | 4:001 006 044 |
| Virginia4 | 27 | 175 | 9:004 | 004 177 199 377 | 3:004 177 349 |
| OntarioCanada4 | 27 | 180 | 9:004 | 004 044 144 228 | 4:004 022 044 |
| Indiana4 | 27 | 192 | 9:002 | 002 022 177 226 | 4:002 066 667 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 077 707 770 027 072 207 270 702 720`
- **NewYork4**: `001 010 100 006 060 600 005 050 500 011 101 110`
- **NewJersey4**: `022 202 220 077 707 770 168 186 618 681 816 861`
- **Delaware4**: `009 090 900 011 101 110 004 040 400 559 595 955`
- **Michigan4**: `112 121 211 119 191 911 155 515 551 114 141 411`
- **Pennsylvania4**: `007 070 700 112 121 211 002 020 200 255 525 552`
- **Florida4**: `003 030 300 338 383 833 335 353 533 033 303 330`
- **Connecticut4**: `088 808 880 244 424 442 448 484 844 449 494 944`
- **SouthCarolina4**: `115 151 511 224 242 422 566 656 665 599 959 995`
- **Ohio4**: `009 090 900 889 898 988 559 595 955 299 929 992`
- **NorthCarolina4**: `001 010 100 244 424 442 044 404 440 006 060 600`
- **Virginia4**: `004 040 400 349 394 439 493 934 943 177 717 771`
- **OntarioCanada4**: `004 040 400 224 242 422 044 404 440 022 202 220`
- **Indiana4**: `002 020 200 066 606 660 667 676 766 669 696 966`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only.json` (budgeted cuts)
