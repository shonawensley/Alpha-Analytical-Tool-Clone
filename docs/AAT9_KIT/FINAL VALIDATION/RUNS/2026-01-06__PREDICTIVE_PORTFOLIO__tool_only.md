# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---|---|
| PuertoRico4 | 27 | 184 | 14:022 | 022 033 088 199 | 3:022 027 077 |
| Ohio4 | 27 | 161 | 12:009 | 009 066 113 118 | 3:002 009 025 |
| NewJersey4 | 27 | 135 | 11:022 | 022 114 155 339 | 4:022 077 788 |
| NewYork4 | 27 | 144 | 11:001 | 001 007 011 066 | 4:001 008 011 |
| Delaware4 | 27 | 163 | 11:009 | 009 088 223 228 | 4:004 009 011 |
| Michigan4 | 27 | 142 | 10:112 | 112 119 155 199 | 4:112 117 118 |
| Pennsylvania4 | 27 | 157 | 10:007 | 007 066 228 255 | 3:007 059 557 |
| Florida4 | 27 | 144 | 9:003 | 003 009 011 077 | 3:003 346 366 |
| SouthCarolina4 | 27 | 159 | 9:115 | 115 155 224 233 | 4:005 115 224 |
| Connecticut4 | 27 | 167 | 9:088 | 088 099 223 228 | 3:088 247 277 |
| NorthCarolina4 | 27 | 167 | 9:001 | 001 009 044 225 | 3:001 044 049 |
| Virginia4 | 27 | 170 | 9:004 | 004 177 199 377 | 3:004 009 489 |
| OntarioCanada4 | 27 | 173 | 9:004 | 004 044 144 244 | 3:004 015 144 |
| Indiana4 | 27 | 180 | 9:002 | 002 022 177 226 | 3:002 016 066 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 077 707 770 027 072 207 270 702 720`
- **Ohio4**: `009 090 900 025 052 205 250 502 520 002 020 200`
- **NewJersey4**: `022 202 220 077 707 770 788 878 887 889 898 988`
- **NewYork4**: `001 010 100 011 101 110 066 606 660 008 080 800`
- **Delaware4**: `009 090 900 004 040 400 559 595 955 011 101 110`
- **Michigan4**: `112 121 211 119 191 911 118 181 811 117 171 711`
- **Pennsylvania4**: `007 070 700 557 575 755 059 095 509 590 905 950`
- **Florida4**: `003 030 300 346 364 436 463 634 643 366 636 663`
- **SouthCarolina4**: `115 151 511 224 242 422 005 050 500 669 696 966`
- **Connecticut4**: `088 808 880 277 727 772 247 274 427 472 724 742`
- **NorthCarolina4**: `001 010 100 044 404 440 049 094 409 490 904 940`
- **Virginia4**: `004 040 400 489 498 849 894 948 984 009 090 900`
- **OntarioCanada4**: `004 040 400 015 051 105 150 501 510 144 414 441`
- **Indiana4**: `002 020 200 066 606 660 016 061 106 160 601 610`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card__tool_only.json` (budgeted cuts)
