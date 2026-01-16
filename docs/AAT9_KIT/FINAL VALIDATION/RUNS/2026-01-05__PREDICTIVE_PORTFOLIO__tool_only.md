# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---|---|
| Michigan4 | 27 | 125 | 12:112 | 112 119 155 199 | 3:112 119 168 |
| PuertoRico4 | 27 | 185 | 12:022 | 022 033 088 199 | 3:022 026 033 |
| Pennsylvania4 | 27 | 142 | 11:007 | 007 066 228 255 | 3:002 007 059 |
| NewJersey4 | 27 | 143 | 11:022 | 022 114 155 339 | 3:022 077 279 |
| NewYork4 | 27 | 144 | 11:001 | 001 007 011 066 | 4:001 006 008 |
| Ohio4 | 27 | 145 | 11:009 | 009 066 113 118 | 3:009 059 559 |
| OntarioCanada4 | 27 | 158 | 11:004 | 004 044 144 244 | 3:004 146 244 |
| Delaware4 | 27 | 164 | 11:009 | 009 088 223 228 | 3:004 009 459 |
| Florida4 | 27 | 142 | 9:003 | 003 008 009 011 | 4:003 008 033 |
| SouthCarolina4 | 27 | 160 | 9:115 | 115 155 224 233 | 4:003 115 224 |
| Virginia4 | 27 | 168 | 9:004 | 004 177 199 377 | 4:004 377 455 |
| Indiana4 | 27 | 173 | 9:002 | 002 022 177 226 | 4:002 066 266 |
| NorthCarolina4 | 27 | 173 | 9:001 | 001 009 044 225 | 4:001 044 224 |
| Connecticut4 | 27 | 184 | 9:088 | 088 099 223 228 | 3:088 247 277 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **Michigan4**: `112 121 211 168 186 618 681 816 861 119 191 911`
- **PuertoRico4**: `022 202 220 033 303 330 026 062 206 260 602 620`
- **Pennsylvania4**: `007 070 700 059 095 509 590 905 950 002 020 200`
- **NewJersey4**: `022 202 220 279 297 729 792 927 972 077 707 770`
- **NewYork4**: `001 010 100 066 606 660 008 080 800 006 060 600`
- **Ohio4**: `009 090 900 059 095 509 590 905 950 559 595 955`
- **OntarioCanada4**: `004 040 400 244 424 442 146 164 416 461 614 641`
- **Delaware4**: `009 090 900 004 040 400 459 495 549 594 945 954`
- **Florida4**: `003 030 300 344 434 443 008 080 800 033 303 330`
- **SouthCarolina4**: `115 151 511 224 242 422 599 959 995 003 030 300`
- **Virginia4**: `004 040 400 377 737 773 455 545 554 559 595 955`
- **Indiana4**: `002 020 200 066 606 660 266 626 662 667 676 766`
- **NorthCarolina4**: `001 010 100 044 404 440 225 252 522 224 242 422`
- **Connecticut4**: `088 808 880 277 727 772 247 274 427 472 724 742`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card__tool_only.json` (budgeted cuts)
