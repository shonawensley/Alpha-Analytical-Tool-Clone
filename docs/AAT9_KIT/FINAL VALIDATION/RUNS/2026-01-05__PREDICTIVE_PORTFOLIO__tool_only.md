# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| PuertoRico4 | 4 | 12 | Midday:A05:STR8_3:003(3); Midday:A01:BOX:036(6); Midday:A01:BOX:036(6) | 30 | 187 | 13:022 | 022 033 088 199 | 4:022 033 223 |
| Michigan4 | 3 | 10 | Combined:A05:STR8_3:011(3); Combined:A10:STR8_3:566(3); Combined:A04:BOX:168(6) | 30 | 128 | 12:112 | 112 119 155 199 | 3:112 119 168 |
| NewJersey4 | 5 | 13 | Combined:A11:BOX:028(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:028(6) | 30 | 144 | 11:022 | 022 114 155 339 | 3:022 077 279 |
| Pennsylvania4 | 3 | 11 | Combined:A05:STR8_3:055(3); Combined:A09:STR8_8:034(8); Midday:A04:BOX:059(6) | 30 | 144 | 11:007 | 007 066 228 255 | 3:002 007 059 |
| NewYork4 | 3 | 11 | Midday:A05:STR8_3:066(3); Midday:A09:STR8_8:234(8); Midday:A04:BOX:056(6) | 30 | 146 | 11:001 | 001 007 011 066 | 4:001 005 008 |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:599(3); Combined:A12:STR8_4of8:088(4); Combined:A04:BOX:259(6) | 30 | 147 | 11:009 | 009 066 113 118 | 3:009 059 559 |
| Virginia4 | 4 | 13 | Combined:A11:BOX:089(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:089(6) | 30 | 155 | 11:004 | 004 177 199 377 | 4:004 377 455 |
| OntarioCanada4 | 3 | 11 | Combined:A10:STR8_3:255(3); Midday:A05:STR8_3:244(3); Evening:A04:BOX:459(6) | 30 | 159 | 11:004 | 004 044 144 244 | 4:004 244 455 |
| Delaware4 | 2 | 7 | Evening:A05:STR8_3:449(3); Combined:A04:BOX:058(6) | 30 | 167 | 11:009 | 009 088 223 228 | 3:004 009 459 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:467(6) | 30 | 145 | 9:003 | 003 008 009 011 | 4:003 008 033 |
| SouthCarolina4 | 5 | 12 | Combined:A11:BOX:259(6); Midday:A05:STR8_3:007(3); Combined:A10:STR8_3:115(3) | 30 | 165 | 9:115 | 115 155 224 233 | 4:003 115 224 |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 30 | 175 | 9:001 | 001 009 044 225 | 4:001 044 224 |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:244(3); Midday:A12:STR8_4of8:066(4); Midday:A04:BOX:368(6) | 30 | 176 | 9:002 | 002 022 177 226 | 4:002 022 066 |
| Connecticut4 | 3 | 11 | Evening:A05:STR8_8:024(8); Evening:A09:STR8_8:113(8); Evening:A04:BOX:024(6) | 30 | 187 | 9:088 | 088 099 223 228 | 3:088 247 277 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 033 303 330 225 252 522 223 232 322`
- **Michigan4**: `112 121 211 168 186 618 681 816 861 119 191 911`
- **NewJersey4**: `022 202 220 279 297 729 792 927 972 077 707 770`
- **Pennsylvania4**: `007 070 700 059 095 509 590 905 950 002 020 200`
- **NewYork4**: `001 010 100 066 606 660 008 080 800 005 050 500`
- **Ohio4**: `009 090 900 059 095 509 590 905 950 559 595 955`
- **Virginia4**: `004 040 400 377 737 773 559 595 955 455 545 554`
- **OntarioCanada4**: `004 040 400 244 424 442 455 545 554 477 747 774`
- **Delaware4**: `009 090 900 004 040 400 459 495 549 594 945 954`
- **Florida4**: `003 030 300 344 434 443 008 080 800 033 303 330`
- **SouthCarolina4**: `115 151 511 224 242 422 599 959 995 003 030 300`
- **NorthCarolina4**: `001 010 100 044 404 440 225 252 522 224 242 422`
- **Indiana4**: `002 020 200 066 606 660 244 424 442 022 202 220`
- **Connecticut4**: `088 808 880 277 727 772 247 274 427 472 724 742`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card__tool_only.json` (budgeted cuts)
