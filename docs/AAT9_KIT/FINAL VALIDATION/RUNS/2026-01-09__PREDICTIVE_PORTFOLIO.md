# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `mixed` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe.json`
- Play Card file(s): `play_card*.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---:|---:|---|---|---|---|---|
| NewYork4 | 8 | 13 | Combined:A11:BOX:045(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:045(6) | 40 | 180 | 14:001 | 001 007 011 066 | 2:001 057 | - | - |
| Delaware4 | 5 | 10 | Midday:A05:STR8_3:033(3); Midday:A02:STR8_3:033(3); Midday:A02:STR8_3:033(3) | 37 | 203 | 10:009 | 009 088 117 223 | 3:009 033 344 | - | - |
| Virginia4 | 4 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 36 | 184 | 10:004 | 004 177 199 377 | 2:004 024 | - | - |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:011(8); Midday:A12:STR8_4of8:448(4) | 36 | 166 | 9:088 | 088 099 223 228 | 1:088 | - | - |
| PuertoRico4 | 4 | 11 | Midday:A05:STR8_3:006(3); Midday:A01:BOX:068(6); Combined:A12:STR8_4of8:088(4) | 36 | 189 | 15:022 | 022 033 088 199 | 1:022 | - | - |
| OntarioCanada4 | 4 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Combined:A06:BOX:015(6) | 36 | 183 | 9:004 | 004 044 144 228 | 2:004 224 | - | - |
| Florida4 | 3 | 11 | Combined:A10:STR8_3:077(3); Evening:A05:STR8_3:224(3); Evening:A04:BOX:034(6) | 35 | 153 | 11:003 | 003 009 011 077 | 3:003 077 224 | - | - |
| Pennsylvania4 | 3 | 11 | Midday:A05:STR8_3:009(3); Midday:A04:BOX:019(6); Combined:A10:STR8_3:066(3) | 35 | 199 | 9:007 | 007 066 228 255 | 2:007 066 | - | - |
| Ohio4 | 3 | 10 | Combined:A05:STR8_3:399(3); Combined:A10:STR8_3:066(3); Combined:A04:BOX:039(6) | 35 | 178 | 9:009 | 009 066 113 118 | 3:009 066 399 | - | - |
| NewJersey4 | 3 | 10 | Combined:A05:STR8_3:003(3); Evening:A12:STR8_4of8:078(4); Evening:A04:BOX:078(6) | 35 | 189 | 9:022 | 022 114 155 339 | 2:003 022 | - | - |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:059(6) | 34 | 153 | 9:115 | 115 155 224 233 | 2:059 115 | - | - |
| Michigan4 | 2 | 7 | Combined:A05:STR8_3:334(3); Evening:A04:BOX:019(6) | 34 | 165 | 10:112 | 112 119 155 199 | 3:019 112 334 | - | - |
| NorthCarolina4 | 2 | 7 | Combined:A05:STR8_3:066(3); Combined:A04:BOX:039(6) | 34 | 183 | 9:001 | 001 009 044 225 | 2:001 066 | - | - |
| Indiana4 | 2 | 7 | Combined:A05:STR8_3:004(3); Midday:A04:BOX:069(6) | 34 | 233 | 9:002 | 002 022 177 226 | 3:002 004 069 | - | - |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **NewYork4**: `001 010 100 507 057 075 005 500 570 705 750 540`
- **Delaware4**: `009 090 900 344 033 303 330 434 544 559 504 443`
- **Virginia4**: `004 040 400 364 634 024 042 204 240 402 420 346`
- **Connecticut4**: `894 844 849 088 808 880 242 298 224 294 892 982`
- **PuertoRico4**: `220 022 202 088 068 086 680 033 038 083 608 806`
- **OntarioCanada4**: `224 242 422 004 040 400 501 270 274 924 051 015`
- **Florida4**: `030 077 707 770 003 300 224 242 422 045 057 075`
- **Pennsylvania4**: `019 007 070 700 066 606 660 009 090 091 109 190`
- **Ohio4**: `009 090 900 066 606 660 849 559 399 939 993 039`
- **NewJersey4**: `022 202 220 003 030 300 078 073 087 708 780 807`
- **SouthCarolina4**: `059 095 509 590 905 950 115 151 511 599 499 949`
- **Michigan4**: `112 121 211 019 334 343 433 091 109 190 901 910`
- **NorthCarolina4**: `001 010 100 940 644 440 066 606 660 049 094 490`
- **Indiana4**: `002 020 200 069 096 609 690 906 960 004 040 400`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.


### B24 (vtrac_pack_boxed_first)

- (not available for this profile/day)

### B36 (vtrac_pack_boxed_first)

- (not available for this profile/day)

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card*.json` (budgeted cuts)
