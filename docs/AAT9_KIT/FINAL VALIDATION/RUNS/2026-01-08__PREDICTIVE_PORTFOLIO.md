# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Starts from Control Center Profit Alerts (bet-ready) and annotates with Candidate Universe size.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|
| NewYork4 | 6 | 13 | Combined:A11:BOX:459(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:057(6) | 34 | 127 | 001 007 011 066 | 4:001 005 006 |
| Virginia4 | 5 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 33 | 152 | 004 177 199 377 | 3:004 024 559 |
| Delaware4 | 5 | 11 | Midday:A05:STR8_3:033(3); Midday:A09:STR8_8:011(8); Midday:A02:STR8_3:033(3) | 33 | 160 | 009 088 223 228 | 4:009 011 033 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:009(3); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 33 | 138 | 007 066 228 255 | 4:007 009 445 |
| NewJersey4 | 4 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A12:STR8_4of8:089(4) | 32 | 134 | 022 114 155 339 | 3:022 089 778 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:334(3); Combined:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 31 | 110 | 003 009 011 077 | 3:003 334 346 |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:004(4); Evening:A04:BOX:019(6) | 31 | 122 | 112 119 155 199 | 4:004 112 119 |
| OntarioCanada4 | 3 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Evening:A04:BOX:015(6) | 31 | 150 | 004 044 144 228 | 3:004 015 224 |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:344(3); Combined:A10:STR8_3:002(3); Midday:A04:BOX:069(6) | 31 | 174 | 002 022 177 226 | 3:002 069 344 |
| Ohio4 | 2 | 8 | Evening:A05:STR8_3:889(3); Combined:A04:BOX:359(6) | 30 | 133 | 009 066 113 118 | 4:009 299 559 |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:248(6) | 30 | 122 | 088 099 223 228 | 3:088 224 248 |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:369(6) | 30 | 125 | 115 155 224 233 | 4:115 224 244 |
| NorthCarolina4 | 2 | 7 | Evening:A05:STR8_3:244(3); Evening:A04:BOX:016(6) | 30 | 154 | 001 009 044 225 | 4:001 006 044 |
| PuertoRico4 | 1 | 3 | Evening:A04:BOX:068(6) | 29 | 157 | 022 033 199 299 | 3:022 068 077 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **NewYork4**: `001 010 100 005 050 500 006 060 600 011 101 110`
- **Virginia4**: `004 040 400 024 042 204 240 402 420 559 595 955`
- **Delaware4**: `011 101 110 009 090 900 033 303 330 118 181 811`
- **Pennsylvania4**: `007 070 700 599 959 995 009 090 900 445 454 544`
- **NewJersey4**: `022 202 220 089 098 809 890 908 980 778 787 877`
- **Florida4**: `334 343 433 003 030 300 346 364 436 463 634 643`
- **Michigan4**: `112 121 211 344 434 443 004 040 400 119 191 911`
- **OntarioCanada4**: `224 242 422 004 040 400 015 051 105 150 501 510`
- **Indiana4**: `002 020 200 344 434 443 069 096 609 690 906 960`
- **Ohio4**: `889 898 988 009 090 900 559 595 955 299 929 992`
- **Connecticut4**: `224 242 422 088 808 880 248 284 428 482 824 842`
- **SouthCarolina4**: `115 151 511 244 424 442 599 959 995 224 242 422`
- **NorthCarolina4**: `244 424 442 001 010 100 044 404 440 006 060 600`
- **PuertoRico4**: `022 202 220 068 086 608 680 806 860 077 707 770`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical “what to play” remains:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card.json` (budgeted cuts)
