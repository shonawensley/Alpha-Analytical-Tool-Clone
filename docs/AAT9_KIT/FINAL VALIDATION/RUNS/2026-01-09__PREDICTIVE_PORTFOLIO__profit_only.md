# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `profit_only` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__profit_only.json`
- Play Card file(s): `play_card__profit_only*.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---:|---:|---|---|---|---|---|
| NewYork4 | 8 | 13 | Combined:A11:BOX:045(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:045(6) | 8 | 27 | 3:001 | - | 2:005 045 | - | - |
| Delaware4 | 5 | 10 | Midday:A05:STR8_3:033(3); Midday:A02:STR8_3:033(3); Midday:A02:STR8_3:033(3) | 5 | 13 | 3:033 | - | 2:013 033 | - | - |
| Virginia4 | 4 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 4 | 19 | 3:024 | - | 1:024 | - | - |
| PuertoRico4 | 4 | 11 | Midday:A05:STR8_3:006(3); Midday:A01:BOX:068(6); Combined:A12:STR8_4of8:088(4) | 4 | 13 | 2:068 | - | 2:006 068 | - | - |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:011(8); Midday:A12:STR8_4of8:448(4) | 4 | 21 | 1:011 016 066 | - | 1:224 | - | - |
| OntarioCanada4 | 4 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Combined:A06:BOX:015(6) | 4 | 12 | 2:015 | - | 2:015 224 | - | - |
| Florida4 | 3 | 11 | Combined:A10:STR8_3:077(3); Evening:A05:STR8_3:224(3); Evening:A04:BOX:034(6) | 3 | 12 | 1:034 077 224 | - | 3:034 077 224 | - | - |
| Pennsylvania4 | 3 | 11 | Midday:A05:STR8_3:009(3); Midday:A04:BOX:019(6); Combined:A10:STR8_3:066(3) | 3 | 12 | 1:009 019 066 | - | 3:009 019 066 | - | - |
| NewJersey4 | 3 | 10 | Combined:A05:STR8_3:003(3); Evening:A12:STR8_4of8:078(4); Evening:A04:BOX:078(6) | 3 | 12 | 2:078 | - | 2:003 078 | - | - |
| Ohio4 | 3 | 10 | Combined:A05:STR8_3:399(3); Combined:A10:STR8_3:066(3); Combined:A04:BOX:039(6) | 3 | 12 | 1:039 066 399 | - | 3:039 066 399 | - | - |
| Indiana4 | 2 | 7 | Combined:A05:STR8_3:004(3); Midday:A04:BOX:069(6) | 2 | 9 | 1:004 069 | - | 2:004 069 | - | - |
| Michigan4 | 2 | 7 | Combined:A05:STR8_3:334(3); Evening:A04:BOX:019(6) | 2 | 9 | 1:019 334 | - | 2:019 334 | - | - |
| NorthCarolina4 | 2 | 7 | Combined:A05:STR8_3:066(3); Combined:A04:BOX:039(6) | 2 | 9 | 1:039 066 | - | 2:039 066 | - | - |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:059(6) | 2 | 9 | 1:059 244 | - | 2:059 244 | - | - |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **NewYork4**: `045 054 405 450 504 540 005 050 057 075 500 507`
- **Delaware4**: `033 303 330 013 031 103 130 301 310 344 349 394`
- **Virginia4**: `024 042 204 240 402 420 029 074 079 524 529 574`
- **PuertoRico4**: `068 086 608 680 806 860 006 060 600 033 038 083`
- **Connecticut4**: `011 016 061 066 224 242 422 511 516 561 566 289`
- **OntarioCanada4**: `224 242 422 051 015 105 150 501 510 001 006 056`
- **Florida4**: `077 224 242 422 707 770 034 043 304 340 403 430`
- **Pennsylvania4**: `009 019 090 091 109 190 900 901 910 066 606 660`
- **NewJersey4**: `003 030 300 078 023 028 073 087 708 780 807 870`
- **Ohio4**: `399 939 993 039 066 093 309 390 606 660 903 930`
- **Indiana4**: `004 040 400 069 096 609 690 906 960`
- **Michigan4**: `334 343 433 019 091 109 190 901 910`
- **NorthCarolina4**: `066 606 660 039 093 309 390 903 930`
- **SouthCarolina4**: `244 424 442 059 095 509 590 905 950`

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
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe__profit_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card__profit_only*.json` (budgeted cuts)
