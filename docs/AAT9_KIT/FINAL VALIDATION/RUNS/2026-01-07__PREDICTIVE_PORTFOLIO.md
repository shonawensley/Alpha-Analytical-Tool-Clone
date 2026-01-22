# Predictive Portfolio — D=2026-01-07

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `mixed` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe.json`
- Play Card file(s): `play_card*.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---:|---:|---|---|---|---|---|
| Virginia4 | 6 | 13 | Combined:A11:BOX:134(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:019(6) | 38 | 174 | 11:004 | 004 177 199 377 | 2:004 009 | - | - |
| Delaware4 | 6 | 12 | Combined:A05:STR8_3:334(3); Midday:A01:BOX:038(6); Midday:A07:BOX:035(6) | 38 | 208 | 11:009 | 009 088 223 228 | 3:004 009 334 | - | - |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 37 | 179 | 10:007 | 007 066 228 255 | 3:000 001 007 | - | - |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:012(8); Midday:A12:STR8_4of8:448(4) | 36 | 195 | 9:088 | 088 099 223 228 | 1:088 | - | - |
| Indiana4 | 4 | 10 | Evening:A05:STR8_3:244(3); Combined:A10:STR8_3:002(3); Combined:A12:STR8_4of8:004(4) | 36 | 213 | 10:002 | 002 022 177 226 | 2:002 244 | - | - |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 35 | 164 | 9:022 | 022 114 155 339 | 3:022 189 778 | - | - |
| SouthCarolina4 | 3 | 11 | Midday:A05:STR8_3:224(3); Midday:A01:BOX:079(6); Combined:A04:BOX:369(6) | 35 | 184 | 9:115 | 115 155 224 233 | 3:115 224 369 | - | - |
| PuertoRico4 | 3 | 11 | Midday:A05:STR8_3:003(3); Evening:A04:BOX:068(6); Midday:A12:STR8_4of8:066(4) | 35 | 203 | 14:022 | 022 033 199 299 | 2:003 022 | - | - |
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:001(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 35 | 156 | 15:001 | 001 007 011 066 | 1:001 | - | - |
| Florida4 | 3 | 10 | Evening:A05:STR8_3:033(3); Evening:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 35 | 165 | 9:003 | 003 009 011 077 | 2:003 033 | - | - |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:001(4); Evening:A04:BOX:016(6) | 35 | 169 | 10:112 | 112 119 155 199 | 3:112 119 344 | - | - |
| NorthCarolina4 | 3 | 10 | Evening:A05:STR8_3:244(3); Combined:A12:STR8_4of8:066(4); Evening:A04:BOX:246(6) | 35 | 178 | 9:001 | 001 009 044 225 | 2:001 244 | - | - |
| Ohio4 | 2 | 7 | Evening:A05:STR8_3:559(3); Combined:A04:BOX:089(6) | 34 | 175 | 9:009 | 009 066 113 118 | 3:009 089 559 | - | - |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 34 | 191 | 10:004 | 004 044 144 228 | 2:004 244 | - | - |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **Virginia4**: `040 090 004 400 009 900 559 554 024 042 204 240`
- **Delaware4**: `009 090 900 334 343 433 035 530 004 040 400 011`
- **Pennsylvania4**: `070 007 700 000 015 001 009 010 090 100 544 599`
- **Connecticut4**: `844 224 088 808 880 894 024 042 240 420 849 242`
- **Indiana4**: `002 020 200 244 762 424 442 004 267 276 672 237`
- **NewJersey4**: `778 022 202 220 189 198 819 918 787 877 891 981`
- **SouthCarolina4**: `224 242 422 115 151 511 369 396 639 693 936 963`
- **PuertoRico4**: `022 220 202 016 061 806 086 068 216 003 030 300`
- **NewYork4**: `001 010 100 058 008 508 507 805 060 506 011 066`
- **Florida4**: `334 436 384 033 303 330 003 030 300 346 364 634`
- **Michigan4**: `112 121 211 191 344 434 443 001 156 119 911 016`
- **NorthCarolina4**: `244 424 442 001 010 100 940 964 440 600 066 469`
- **Ohio4**: `559 595 955 009 090 900 089 098 809 890 908 980`
- **OntarioCanada4**: `004 040 400 244 247 501 224 015 274 424 442 724`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.


## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-07/<STATE>/play_card*.json` (budgeted cuts)
