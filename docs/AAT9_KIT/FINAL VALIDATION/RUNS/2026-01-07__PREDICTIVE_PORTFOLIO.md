# Predictive Portfolio — D=2026-01-07

Purpose
- Cross-state triage for a predictive day (pre-results).
- Starts from Control Center Profit Alerts (bet-ready) and annotates with Candidate Universe size.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|
| Virginia4 | 6 | 13 | Combined:A11:BOX:134(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:019(6) | 34 | 145 | 004 177 199 377 | 4:004 009 455 |
| Delaware4 | 6 | 12 | Combined:A05:STR8_3:334(3); Midday:A01:BOX:038(6); Midday:A07:BOX:035(6) | 34 | 164 | 009 088 223 228 | 3:009 035 334 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 33 | 141 | 007 066 228 255 | 4:000 001 007 |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:012(8); Midday:A12:STR8_4of8:448(4) | 32 | 138 | 088 099 223 228 | 4:088 224 244 |
| Indiana4 | 4 | 10 | Evening:A05:STR8_3:244(3); Combined:A10:STR8_3:002(3); Combined:A12:STR8_4of8:004(4) | 32 | 173 | 002 022 177 226 | 4:002 004 066 |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 31 | 119 | 022 114 155 339 | 3:022 189 778 |
| SouthCarolina4 | 3 | 11 | Midday:A05:STR8_3:224(3); Midday:A01:BOX:079(6); Combined:A04:BOX:369(6) | 31 | 136 | 115 155 224 233 | 3:115 224 369 |
| PuertoRico4 | 3 | 11 | Midday:A05:STR8_3:003(3); Evening:A04:BOX:068(6); Midday:A12:STR8_4of8:066(4) | 31 | 168 | 022 033 199 299 | 3:003 022 068 |
| Florida4 | 3 | 10 | Evening:A05:STR8_3:033(3); Evening:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 31 | 119 | 003 009 011 077 | 3:033 334 346 |
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:001(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 31 | 119 | 001 007 011 066 | 4:001 006 008 |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:001(4); Evening:A04:BOX:016(6) | 31 | 127 | 112 119 155 199 | 4:001 112 119 |
| NorthCarolina4 | 3 | 10 | Evening:A05:STR8_3:244(3); Combined:A12:STR8_4of8:066(4); Evening:A04:BOX:246(6) | 31 | 152 | 001 009 044 225 | 4:001 006 044 |
| Ohio4 | 2 | 7 | Evening:A05:STR8_3:559(3); Combined:A04:BOX:089(6) | 30 | 129 | 009 066 113 118 | 3:009 089 559 |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 30 | 148 | 004 044 144 228 | 3:004 015 244 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **Virginia4**: `004 040 400 009 090 900 559 595 955 455 545 554`
- **Delaware4**: `009 090 900 334 343 433 035 053 305 350 503 530`
- **Pennsylvania4**: `007 070 700 000 001 010 100 009 090 900 544 599`
- **Connecticut4**: `448 484 844 224 242 422 088 808 880 244 424 442`
- **Indiana4**: `002 020 200 244 424 442 004 040 400 066 606 660`
- **NewJersey4**: `778 787 877 022 202 220 189 198 819 891 918 981`
- **SouthCarolina4**: `224 242 422 115 151 511 369 396 639 693 936 963`
- **PuertoRico4**: `022 202 220 068 086 608 680 806 860 003 030 300`
- **Florida4**: `334 343 433 346 364 436 463 634 643 033 303 330`
- **NewYork4**: `001 010 100 008 080 800 006 060 600 011 101 110`
- **Michigan4**: `112 121 211 119 191 911 344 434 443 001 010 100`
- **NorthCarolina4**: `244 424 442 001 010 100 044 404 440 006 060 600`
- **Ohio4**: `559 595 955 009 090 900 089 098 809 890 908 980`
- **OntarioCanada4**: `004 040 400 244 424 442 015 051 105 150 501 510`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical “what to play” remains:
  - `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv` (bet-ready implied sets)
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-07/<STATE>/play_card.json` (budgeted cuts)
