# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `profit_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__profit_only.json`
- Play Card file: `play_card__profit_only.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| Delaware4 | 5 | 10 | Midday:A05:STR8_3:033(3); Midday:A02:STR8_3:033(3); Midday:A02:STR8_3:033(3) | 5 | 13 | 3:033 | - | 2:013 033 |
| Virginia4 | 4 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 4 | 19 | 3:024 | - | 2:024 346 |
| NewYork4 | 8 | 13 | Combined:A11:BOX:045(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:045(6) | 8 | 27 | 3:001 | - | 3:001 005 045 |
| OntarioCanada4 | 4 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Combined:A06:BOX:015(6) | 4 | 12 | 2:015 | - | 2:015 224 |
| NewJersey4 | 3 | 10 | Combined:A05:STR8_3:003(3); Evening:A12:STR8_4of8:078(4); Evening:A04:BOX:078(6) | 3 | 12 | 2:078 | - | 2:003 078 |
| PuertoRico4 | 4 | 11 | Midday:A05:STR8_3:006(3); Midday:A01:BOX:068(6); Combined:A12:STR8_4of8:088(4) | 4 | 13 | 2:068 | - | 2:006 068 |
| Indiana4 | 2 | 7 | Combined:A05:STR8_3:004(3); Midday:A04:BOX:069(6) | 2 | 9 | 1:004 069 | - | 2:004 069 |
| Michigan4 | 2 | 7 | Combined:A05:STR8_3:334(3); Evening:A04:BOX:019(6) | 2 | 9 | 1:019 334 | - | 2:019 334 |
| NorthCarolina4 | 2 | 7 | Combined:A05:STR8_3:066(3); Combined:A04:BOX:039(6) | 2 | 9 | 1:039 066 | - | 2:039 066 |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:059(6) | 2 | 9 | 1:059 244 | - | 2:059 244 |
| Florida4 | 3 | 11 | Combined:A10:STR8_3:077(3); Evening:A05:STR8_3:224(3); Evening:A04:BOX:034(6) | 3 | 12 | 1:034 077 224 | - | 3:034 077 224 |
| Ohio4 | 3 | 10 | Combined:A05:STR8_3:399(3); Combined:A10:STR8_3:066(3); Combined:A04:BOX:039(6) | 3 | 12 | 1:039 066 399 | - | 3:039 066 399 |
| Pennsylvania4 | 3 | 11 | Midday:A05:STR8_3:009(3); Midday:A04:BOX:019(6); Combined:A10:STR8_3:066(3) | 3 | 12 | 1:009 019 066 | - | 3:009 019 066 |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:011(8); Midday:A12:STR8_4of8:448(4) | 4 | 21 | 1:011 016 066 | - | 2:224 289 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **Delaware4**: `033 303 330 013 031 103 130 301 310 344 349 394`
- **Virginia4**: `024 042 204 240 402 420 346 364 436 463 634 643`
- **NewYork4**: `045 054 405 450 504 540 005 050 500 001 010 100`
- **OntarioCanada4**: `224 242 422 015 051 105 150 501 510 001 006 056`
- **NewJersey4**: `003 030 300 078 087 708 780 807 870 023 028 073`
- **PuertoRico4**: `068 086 608 680 806 860 006 060 600 033 038 083`
- **Indiana4**: `004 040 400 069 096 609 690 906 960`
- **Michigan4**: `334 343 433 019 091 109 190 901 910`
- **NorthCarolina4**: `066 606 660 039 093 309 390 903 930`
- **SouthCarolina4**: `244 424 442 059 095 509 590 905 950`
- **Florida4**: `077 707 770 224 242 422 034 043 304 340 403 430`
- **Ohio4**: `399 939 993 039 093 309 390 903 930 066 606 660`
- **Pennsylvania4**: `009 090 900 019 091 109 190 901 910 066 606 660`
- **Connecticut4**: `224 242 422 289 298 829 892 928 982 011 016 061`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe__profit_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card__profit_only.json` (budgeted cuts)
