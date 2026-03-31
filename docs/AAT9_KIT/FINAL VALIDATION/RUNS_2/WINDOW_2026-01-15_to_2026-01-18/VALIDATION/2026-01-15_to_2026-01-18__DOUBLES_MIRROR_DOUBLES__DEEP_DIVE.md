# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-03-28T10:04:04.303251+00:00`
- Rows: `64`

## Interpretation notes (so we don’t contaminate)

- This report is **post-results** analysis. It links to winners lens + Master Validation RUNS and also to pre-results predictive grades when available.
- `aux_ds_since_double` and `cc_due_doubles_ds` are computed from the **pre-results** Aux snapshot (history workbook H = D-1), i.e. the state of the world before results date D posted.
- `Type=mirror_double` means the winner contains a full VTRAC mirror pair (0/5,1/6,2/7,3/8,4/9) but is not itself a double/triple.

## High-priority audit: CC vs Aux DS

Rows where `cc_minus_aux_ds_delta != 0` (should be rare; investigate if recurring):

| Date | State | Period | Winner | Type | CC DS | Aux DS | Delta | Aux CSV |
|---|---|---|---:|---|---:|---:|---:|---|
| *(none)* | | | | | | | | |

## Predictive coverage (when available)

Rows where Candidate Universe or Play Card achieved a **BOX hit** (useful for learning which method_ids convert lane/index pressure into box coverage):

| Date | State | Period | Winner | Type | CU Box | CU Best (non-union) | CU Cost | Play Box | Play Index |
|---|---|---|---:|---|---:|---|---:|---:|---:|
| *(none)* | | | | | | | | | |

## Winners lens quick stats (Set1 col1/2 ladder)

Computed from the winners JSON lens for the same event (focus variant = period).

| Type | Rows | Any hit-family | Any hit-winner | Any hit-vt-straight | Any ls-box | Avg family cells | Avg winner cells | Avg xvar family | Avg xvar winner |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| double | 27 | 21 | 10 | 13 | 27 | 7.00 | 1.19 | 2.22 | 0.78 |
| triple | 2 | 0 | 0 | 0 | 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| mirror_double | 35 | 27 | 8 | 15 | 35 | 7.29 | 0.49 | 2.26 | 0.57 |

## Per-event evidence pointers

### 2026-01-15 — Connecticut4 — Evening — 617 (mirror_double)

- Winner canonical: `167`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`6` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-15/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-15/Connecticut4/winners/Connecticut4/Connecticut4_vtrac17_winner_617_20260127_014826.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-15 — Connecticut4 — Midday — 495 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-15/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-15/Connecticut4/winners/Connecticut4/Connecticut4_vtrac15_winner_495_20260127_014825.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`28` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 5998** [hit-family,hit-family-gap] | Draw3:R2 col2 59987** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 5998** [hit-family,hit-family-gap] | Draw3:R4 col2 59987** [hit-family,hit-family-gap] | Draw3:R6 col1 8599** [hit-family,hit-family-gap] | Draw3:R6 col2 87599** [hit-family,hit-family-gap]`

### 2026-01-15 — Delaware4 — Midday — 288 (double)

- Winner canonical: `288`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-15/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-15/Delaware4/winners/Delaware4/Delaware4_vtrac29_winner_288_20260127_014827.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 9400387** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 592400387** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 9008347** [hit-family-gap] | Draw5:R4 col2 259008347** [hit-family-gap] | Draw5:R8 col2 700983245** [hit-family,hit-family-gap] | Draw6:R2 col1 940038867* [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-15 — Florida4 — Midday — 404 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-15/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-15/Florida4/winners/Florida4/Florida4_vtrac15_winner_404_20260127_014830.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 5941377** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col2 5934771** [hit-family-gap] | Draw4:R6 col2 1775934** [hit-family-gap] | Draw4:R8 col2 7719345** [hit-family-gap] | Draw5:R2 col2 594138677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col2 681775934** [hit-family-gap]`

### 2026-01-15 — Indiana4 — Evening — 094 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`5` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-15/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-15/Indiana4/winners/Indiana4/Indiana4_vtrac15_winner_094_20260127_014833.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`27` hit-winner-cells=`3` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`2` family_recentest_draw=`3` winner_recentest_draw=`6`
- Winners lens samples: `Draw3:R2 col1 59901366** [hit-family,hit-family-gap] | Draw3:R2 col2 599013866** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 59906631** [hit-family,hit-family-gap] | Draw3:R4 col2 599066831** [hit-family,hit-family-gap] | Draw3:R6 col1 66105993** [hit-family,hit-family-gap] | Draw3:R6 col2 668105993** [hit-family,hit-family-gap]`

### 2026-01-15 — Indiana4 — Midday — 311 (double)

- Winner canonical: `113`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-15/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-15/Indiana4/winners/Indiana4/Indiana4_vtrac18_winner_311_20260127_014832.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`26` hit-winner-cells=`1` hit-vt-straight-cells=`17` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`1` family_recentest_draw=`1` winner_recentest_draw=`7`
- Winners lens samples: `Draw1:R2 col2 086677** [hit-family,hit-family-gap] | Draw1:R4 col2 066877** [hit-family,hit-family-gap] | Draw1:R6 col2 668770** [hit-family,hit-family-gap] | Draw1:R8 col2 770866** [hit-family,hit-family-gap] | Draw2:R2 col2 0086677** [hit-family,hit-family-gap] | Draw2:R4 col2 0066877** [hit-family,hit-family-gap]`

### 2026-01-15 — Michigan4 — Evening — 664 (double)

- Winner canonical: `466`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-15/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-15/Michigan4/winners/Michigan4/Michigan4_vtrac19_winner_664_20260127_014835.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`17` hit-winner-cells=`5` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`2` family_recentest_draw=`3` winner_recentest_draw=`4`
- Winners lens samples: `Draw3:R2 col1 4116** [hit-family,hit-family-gap] | Draw3:R2 col2 4411386** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw3:R4 col1 6411** [hit-family,hit-family-gap] | Draw3:R4 col2 6834411** [hit-family,hit-family-gap,hit-vt-straight] | Draw3:R6 col1 6114** [hit-family,hit-family-gap] | Draw3:R6 col2 6811344** [hit-family-gap]`

### 2026-01-15 — Michigan4 — Midday — 386 (mirror_double)

- Winner canonical: `368`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`18` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`18` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-15/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-15/Michigan4/winners/Michigan4/Michigan4_vtrac23_winner_386_20260127_014834.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-15 — NewJersey4 — Evening — 466 (double)

- Winner canonical: `466`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`6` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-15/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-15/NewJersey4/winners/NewJersey4/NewJersey4_vtrac19_winner_466_20260127_014837.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`5` hit-vt-straight-cells=`4` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`5` family_recentest_draw=`2` winner_recentest_draw=`2`
- Winners lens samples: `Draw2:R2 col1 416** [hit-family,hit-family-gap] | Draw2:R2 col2 41366** [hit-family-gap] | Draw2:R4 col1 641** [hit-family,hit-family-gap] | Draw2:R4 col2 66341** [hit-family-gap,hit-winner-gap] | Draw2:R6 col1 614** [hit-family,hit-family-gap] | Draw2:R6 col2 66134** [hit-family-gap]`

### 2026-01-15 — NewJersey4 — Midday — 419 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-15/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-15/NewJersey4/winners/NewJersey4/NewJersey4_vtrac25_winner_419_20260127_014836.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`0` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 99011** [hit-family-gap] | Draw4:R2 col2 9901137** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 99011** [hit-family-gap] | Draw4:R6 col1 11099** [hit-family-gap] | Draw4:R8 col1 01199** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R8 col2 7011993** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-15 — NorthCarolina4 — Midday — 045 (mirror_double)

- Winner canonical: `045`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-15/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-15/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac5_winner_045_20260127_014841.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 55248** [hit-family-gap] | Draw3:R2 col2 552408** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw3:R4 col1 25584** [hit-family-gap] | Draw3:R4 col2 255084** [hit-family-gap,hit-winner-gap] | Draw3:R6 col1 85524** [hit-family-gap] | Draw3:R6 col2 805524** [hit-family-gap,hit-winner-gap]`

### 2026-01-15 — Pennsylvania4 — Evening — 385 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac13_winner_385_20260127_014851.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-15 — Pennsylvania4 — Midday — 612 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_612_20260127_014850.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col2 59244001367 [hit-family-gap,ls-box,ls-box-edge] | Draw6:R6 col2 61700593244 [hit-family,hit-family-gap] | Draw7:R2 col1 92244003667 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R6 col1 66700932244 [hit-family,hit-family-gap] | Draw7:R8 col1 70093662244 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-15 — SouthCarolina4 — Evening — 118 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac18_winner_118_20260127_014857.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`12` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 924486677* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 559224486677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 296684477* [hit-family,hit-family-gap] | Draw6:R4 col2 225596684477 [hit-family,hit-family-gap] | Draw6:R6 col1 668779244* [hit-family,hit-family-gap] | Draw6:R6 col2 668775592244 [hit-family,hit-family-gap]`

### 2026-01-15 — SouthCarolina4 — Midday — 441 (double)

- Winner canonical: `144`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac25_winner_441_20260127_014856.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-15 — Virginia4 — Midday — 493 (mirror_double)

- Winner canonical: `349`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-15/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-15/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-15/Virginia4/winners/Virginia4/Virginia4_vtrac34_winner_493_20260127_014857.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 225599068441 [hit-family,hit-family-gap] | Draw7:R8 col1 019986224455 [hit-family,hit-family-gap]`

### 2026-01-16 — Florida4 — Evening — 100 (double)

- Winner canonical: `001`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-16/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-16/Florida4/winners/Florida4/Florida4_vtrac2_winner_100_20260127_015240.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`6` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`2` family_recentest_draw=`5` winner_recentest_draw=`6`
- Winners lens samples: `Draw3:R6 col1 8175522** [hit-family-gap] | Draw4:R6 col1 81755322** [hit-family-gap] | Draw5:R4 col2 22550683771** [hit-family,hit-family-gap] | Draw5:R6 col1 817055322** [hit-family-gap] | Draw6:R2 col1 55220013887* [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R2 col2 5522001388677 [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge]`

### 2026-01-16 — Florida4 — Midday — 273 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-16/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-16/Florida4/winners/Florida4/Florida4_vtrac27_winner_273_20260127_015239.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`30` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 5377** [hit-family,hit-family-gap] | Draw2:R2 col2 5377** [hit-family,hit-family-gap] | Draw2:R4 col1 5377** [hit-family,hit-family-gap] | Draw2:R4 col2 5377** [hit-family,hit-family-gap] | Draw2:R6 col1 7753** [hit-family-gap] | Draw2:R6 col2 7753** [hit-family-gap]`

### 2026-01-16 — Indiana4 — Evening — 836 (mirror_double)

- Winner canonical: `368`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-16/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-16/Indiana4/winners/Indiana4/Indiana4_vtrac23_winner_836_20260127_015241.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`2` hit-vt-straight-cells=`21` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`1` family_recentest_draw=`4` winner_recentest_draw=`7`
- Winners lens samples: `Draw4:R2 col1 5913366** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R2 col2 599013366** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col1 5966331** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R4 col2 599066331** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R8 col1 1933665** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R8 col2 019933665** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-16 — Indiana4 — Midday — 954 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-16/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-16/Indiana4/winners/Indiana4/Indiana4_vtrac15_winner_954_20260127_015241.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`1` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`1` family_recentest_draw=`5` winner_recentest_draw=`7`
- Winners lens samples: `Draw5:R2 col1 940388677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 94013388677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col1 688770934** [hit-family-gap] | Draw6:R2 col1 9440388677* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 9440113388677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R6 col1 6887709344* [hit-family-gap]`

### 2026-01-16 — Michigan4 — Evening — 633 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-16/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-16/Michigan4/winners/Michigan4/Michigan4_vtrac23_winner_633_20260127_015243.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 59220113877 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R8 col1 77011983225 [hit-family-gap]`

### 2026-01-16 — Michigan4 — Midday — 946 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`19` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`19` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-16/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-16/Michigan4/winners/Michigan4/Michigan4_vtrac25_winner_946_20260127_015242.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 55224411** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R2 col2 55224411** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R4 col1 22554411** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 22554411** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R8 col1 11224455** [hit-vt-straight-gap] | Draw5:R8 col2 11224455** [hit-vt-straight-gap]`

### 2026-01-16 — NewJersey4 — Midday — 877 (double)

- Winner canonical: `778`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-16/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-16/NewJersey4/winners/NewJersey4/NewJersey4_vtrac27_winner_877_20260127_015244.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-16 — NewYork4 — Evening — 496 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`15` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`15` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-16/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-16/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_496_20260127_015248.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 599213377* [hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 59924133677 [hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col2 25996334771 [hit-family,hit-family-gap] | Draw6:R8 col1 771993325* [hit-family,hit-family-gap] | Draw6:R8 col2 77199336245 [hit-family,hit-family-gap] | Draw7:R2 col1 55992133677 [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-16 — NorthCarolina4 — Evening — 083 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`8` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-16/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-16/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_083_20260127_015250.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`11` hit-winner-cells=`1` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`1` family_recentest_draw=`3` winner_recentest_draw=`7`
- Winners lens samples: `Draw3:R4 col1 258344** [hit-family,hit-family-gap] | Draw3:R4 col2 22583441** [hit-family,hit-family-gap] | Draw3:R6 col1 853244** [hit-family,hit-family-gap] | Draw3:R6 col2 81532244** [hit-family-gap] | Draw4:R4 col1 258344** [hit-family,hit-family-gap] | Draw4:R4 col2 22583441** [hit-family,hit-family-gap]`

### 2026-01-16 — NorthCarolina4 — Midday — 169 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-16/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-16/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac19_winner_169_20260127_015249.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 592241188677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R8 col1 771198862245 [hit-family,hit-family-gap]`

### 2026-01-16 — Ohio4 — Evening — 646 (double)

- Winner canonical: `466`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-16/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-16/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_646_20260127_015252.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`1` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R4 col1 599006634477 [hit-family-gap,hit-vt-straight-gap,hit-winner-gap] | Draw7:R8 col1 770099366445 [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap]`

### 2026-01-16 — Ohio4 — Midday — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-16/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-16/Ohio4/winners/Ohio4/Ohio4_vtrac4_winner_585_20260127_015251.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col2 94003** [hit-family,hit-family-gap] | Draw1:R4 col2 90034** [hit-family,hit-family-gap] | Draw1:R6 col2 00934** [hit-family-gap] | Draw1:R8 col2 00934** [hit-family-gap] | Draw2:R2 col1 94003** [hit-family,hit-family-gap] | Draw2:R2 col2 940033** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-16 — OntarioCanada4 — Midday — 998 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`6` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-16/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-16/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_998_20260127_015253.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`12` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R4 col1 003441** [hit-family,hit-family-gap] | Draw5:R4 col2 59003441** [hit-family,hit-family-gap] | Draw5:R6 col1 100344** [hit-family,hit-family-gap] | Draw5:R6 col2 10059344** [hit-family,hit-family-gap] | Draw5:R8 col1 001344** [hit-family,hit-family-gap] | Draw5:R8 col2 00193445** [hit-family,hit-family-gap]`

### 2026-01-16 — Pennsylvania4 — Evening — 439 (mirror_double)

- Winner canonical: `349`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-16/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-16/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac34_winner_439_20260127_015257.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`13` hit-winner-cells=`4` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`3` family_recentest_draw=`3` winner_recentest_draw=`3`
- Winners lens samples: `Draw3:R2 col1 94866** [hit-family,hit-family-gap] | Draw3:R2 col2 9438866** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw3:R6 col1 66894** [hit-family,hit-family-gap] | Draw3:R6 col2 6688934** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R2 col1 9441866** [hit-family-gap] | Draw4:R2 col2 944138866** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge]`

### 2026-01-16 — PuertoRico4 — Evening — 222 (triple)

- Winner canonical: `222`
- Mirror pairs: `` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-16/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-16/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtracNone_winner_222_20260127_015259.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-16 — PuertoRico4 — Midday — 729 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-16/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-16/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_729_20260127_015258.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`12` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 9224001186* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 922400113867 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 2290068411* [hit-family,hit-family-gap] | Draw6:R4 col2 229006834711 [hit-family,hit-family-gap] | Draw6:R6 col1 6811009224* [hit-family,hit-family-gap] | Draw6:R6 col2 681170093224 [hit-family,hit-family-gap]`

### 2026-01-16 — SouthCarolina4 — Midday — 884 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-16/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-16/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac33_winner_884_20260127_015259.json` (index `33`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`6` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`4` family_recentest_draw=`3` winner_recentest_draw=`3`
- Winners lens samples: `Draw3:R4 col2 508841** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw3:R8 col2 018845** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R4 col2 508841** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R8 col2 018845** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R4 col2 500688471** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R8 col2 700188645** [hit-family-gap,hit-winner-gap]`

### 2026-01-16 — Virginia4 — Evening — 627 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`6` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-16/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-16__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-16/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-16/Virginia4/winners/Virginia4/Virginia4_vtrac20_winner_627_20260127_015303.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R8 col1 099336622* [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R8 col2 09933662245 [hit-family,hit-family-gap,hit-vt-straight] | Draw7:R8 col1 700199336622 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-17 — Connecticut4 — Evening — 969 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`8` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-17/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-17/Connecticut4/winners/Connecticut4/Connecticut4_vtrac25_winner_969_20260127_015626.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 225599068834 [hit-family-gap,hit-winner-gap]`

### 2026-01-17 — Delaware4 — Evening — 888 (triple)

- Winner canonical: `888`
- Mirror pairs: `` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-17/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-17/Delaware4/winners/Delaware4/Delaware4_vtracNone_winner_888_20260127_015628.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-17 — Delaware4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-17/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-17/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260127_015627.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`11` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 40133667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 9400133667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col1 66170334** [hit-family,hit-family-gap] | Draw5:R6 col2 6617009334** [hit-family,hit-family-gap] | Draw6:R2 col1 940133667* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 99400133667 [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-17 — Indiana4 — Evening — 065 (mirror_double)

- Winner canonical: `056`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`7` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-17/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-17/Indiana4/winners/Indiana4/Indiana4_vtrac2_winner_065_20260127_015632.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 5591136** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 559113366** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 5596311** [hit-family-gap] | Draw5:R4 col2 559663311** [hit-family-gap] | Draw5:R6 col1 6115593** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col2 661155933** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-17 — Indiana4 — Midday — 922 (double)

- Winner canonical: `229`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-17/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-17/Indiana4/winners/Indiana4/Indiana4_vtrac28_winner_922_20260127_015631.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw3:R6 col2 68877093** [hit-family-gap] | Draw3:R8 col2 77098836** [hit-family-gap] | Draw4:R4 col2 906883477** [hit-family,hit-family-gap] | Draw4:R6 col2 688770934** [hit-family-gap] | Draw4:R8 col2 770988364** [hit-family-gap] | Draw5:R4 col1 06883477** [hit-family,hit-family-gap]`

### 2026-01-17 — Michigan4 — Evening — 501 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-17/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-17/Michigan4/winners/Michigan4/Michigan4_vtrac2_winner_501_20260127_015634.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 520117** [hit-family-gap,hit-winner-gap] | Draw4:R2 col2 5201137** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw4:R4 col1 250711** [hit-family-gap,hit-winner-gap] | Draw4:R6 col1 117052** [hit-family-gap,hit-winner-gap] | Draw4:R6 col2 1170532** [hit-family-gap,hit-winner-gap] | Draw4:R8 col1 701125** [hit-family-gap,hit-winner-gap]`

### 2026-01-17 — Michigan4 — Midday — 995 (double)

- Winner canonical: `599`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`20` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`20` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-17/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-17/Michigan4/winners/Michigan4/Michigan4_vtrac15_winner_995_20260127_015633.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`3` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`1` family_recentest_draw=`4` winner_recentest_draw=`6`
- Winners lens samples: `Draw4:R2 col2 55224411** [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw4:R4 col2 22554411** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 11552244** [hit-vt-straight-gap] | Draw4:R8 col2 11224455** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 2255944711** [hit-family,hit-family-gap] | Draw5:R8 col2 7119224455** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-17 — NewJersey4 — Midday — 873 (mirror_double)

- Winner canonical: `378`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-17/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-17/NewJersey4/winners/NewJersey4/NewJersey4_vtrac29_winner_873_20260127_015635.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`2` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col2 920013867** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R4 col2 290068371** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R8 col2 700198362** [hit-family-gap] | Draw6:R2 col2 59200138867 [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R4 col2 25900688371 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R6 col2 68817005932 [hit-family-gap]`

### 2026-01-17 — NewYork4 — Midday — 904 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-17/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-17/NewYork4/winners/NewYork4/NewYork4_vtrac15_winner_904_20260127_015637.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R8 col2 7788336622445 [hit-family,hit-family-gap] | Draw7:R2 col1 224403886677 [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-17 — NorthCarolina4 — Evening — 594 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`9` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-17/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-17/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac15_winner_594_20260127_015641.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`16` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 5244** [hit-family-gap] | Draw2:R2 col2 524438** [hit-family-gap] | Draw2:R4 col1 2544** [hit-family,hit-family-gap] | Draw2:R6 col1 5244** [hit-family-gap] | Draw2:R8 col1 2445** [hit-family,hit-family-gap] | Draw2:R8 col2 832445** [hit-family,hit-family-gap]`

### 2026-01-17 — NorthCarolina4 — Midday — 414 (double)

- Winner canonical: `144`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-17/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-17/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac25_winner_414_20260127_015640.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-17 — Ohio4 — Evening — 992 (double)

- Winner canonical: `299`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-17/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-17/Ohio4/winners/Ohio4/Ohio4_vtrac31_winner_992_20260127_015643.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`1` hit-vt-straight-cells=`4` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`1` family_recentest_draw=`1` winner_recentest_draw=`7`
- Winners lens samples: `Draw1:R2 col2 94677** [hit-family-gap] | Draw1:R4 col2 96477** [hit-family-gap] | Draw1:R6 col2 67794** [hit-family,hit-family-gap] | Draw1:R8 col2 77964** [hit-family-gap] | Draw2:R2 col2 94677** [hit-family-gap] | Draw2:R4 col2 96477** [hit-family-gap]`

### 2026-01-17 — Ohio4 — Midday — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-17/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-17/Ohio4/winners/Ohio4/Ohio4_vtrac18_winner_361_20260127_015642.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 994400138677 [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R6 col1 681770099344 [hit-family,hit-family-gap]`

### 2026-01-17 — Pennsylvania4 — Midday — 207 (mirror_double)

- Winner canonical: `027`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-17/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-17/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac10_winner_207_20260127_015647.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-17 — PuertoRico4 — Evening — 799 (double)

- Winner canonical: `799`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-17/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-17/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_799_20260127_015650.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 552440336** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R6 col2 605533244** [hit-family,hit-family-gap] | Draw4:R8 col2 033624455** [hit-family,hit-family-gap] | Draw5:R2 col2 5524401336** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col2 6105533244** [hit-family,hit-family-gap] | Draw5:R8 col2 0133624455** [hit-family,hit-family-gap]`

### 2026-01-17 — PuertoRico4 — Midday — 799 (double)

- Winner canonical: `799`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-17/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-17/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_799_20260127_015650.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col2 9224001186** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col2 6811009224** [hit-family-gap] | Draw6:R2 col1 244001186* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 92244001186 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R6 col1 681100244* [hit-family,hit-family-gap] | Draw6:R6 col2 68110092244 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-17 — SouthCarolina4 — Midday — 716 (mirror_double)

- Winner canonical: `167`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-17/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-17/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac17_winner_716_20260127_015651.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`2` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`6` winner_recentest_draw=`6`
- Winners lens samples: `Draw6:R2 col1 552001367* [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R4 col1 255006371* [hit-family-gap,hit-winner-gap] | Draw6:R6 col1 617005532* [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R8 col1 700136255* [hit-family-gap] | Draw7:R2 col1 559920013677 [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R4 col1 255990063771 [hit-family-gap,hit-winner-gap]`

### 2026-01-17 — Virginia4 — Evening — 020 (double)

- Winner canonical: `002`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`7` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-17/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-17__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-17/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-17/Virginia4/winners/Virginia4/Virginia4_vtrac3_winner_020_20260127_015655.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`3` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`6` winner_recentest_draw=`6`
- Winners lens samples: `Draw6:R2 col1 992001336* [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R2 col2 992200133667 [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R4 col2 229900663371 [hit-vt-straight-gap] | Draw6:R6 col2 661700993322 [hit-family,hit-family-gap] | Draw6:R8 col2 700199336622 [hit-family,hit-family-gap] | Draw7:R2 col1 59920013367 [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge]`

### 2026-01-18 — Connecticut4 — Midday — 238 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-18/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-18/Connecticut4/winners/Connecticut4/Connecticut4_vtrac29_winner_238_20260127_020019.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col2 2886** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col2 2688** [hit-family-gap] | Draw3:R6 col2 6882** [hit-family,hit-family-gap] | Draw3:R8 col2 8862** [hit-family-gap] | Draw4:R2 col1 52886** [hit-family,hit-family-gap] | Draw4:R2 col2 522886** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-18 — Delaware4 — Midday — 490 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-18/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-18/Delaware4/winners/Delaware4/Delaware4_vtrac15_winner_490_20260127_020022.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`2` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`1` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col1 9403367** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R2 col2 940133667** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R2 col1 9440133677* [hit-family,hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R2 col2 944011336677 [hit-family,hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R2 col1 559440133677 [hit-family,hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R8 col1 770193364455 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-18 — Florida4 — Midday — 911 (double)

- Winner canonical: `119`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-18/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-18/Florida4/winners/Florida4/Florida4_vtrac19_winner_911_20260127_020024.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 259906688371 [hit-family-gap]`

### 2026-01-18 — Michigan4 — Midday — 303 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-18/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-18/Michigan4/winners/Michigan4/Michigan4_vtrac13_winner_303_20260127_020030.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 225008347711 [hit-family,hit-family-gap]`

### 2026-01-18 — NewJersey4 — Evening — 955 (double)

- Winner canonical: `559`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-18/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-18/NewJersey4/winners/NewJersey4/NewJersey4_vtrac5_winner_955_20260127_020034.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`19` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col1 004** [hit-family,hit-family-gap] | Draw1:R2 col2 004** [hit-family,hit-family-gap] | Draw1:R4 col1 004** [hit-family,hit-family-gap] | Draw1:R4 col2 004** [hit-family,hit-family-gap] | Draw1:R6 col1 004** [hit-family,hit-family-gap] | Draw1:R6 col2 004** [hit-family,hit-family-gap]`

### 2026-01-18 — NewJersey4 — Midday — 238 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-18/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-18/NewJersey4/winners/NewJersey4/NewJersey4_vtrac29_winner_238_20260127_020033.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw5:R8 col2 001983625** [hit-family-gap,hit-winner-gap]`

### 2026-01-18 — NewYork4 — Evening — 094 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`17` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`17` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-18/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-18/NewYork4/winners/NewYork4/NewYork4_vtrac15_winner_094_20260127_020036.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-18 — NorthCarolina4 — Evening — 772 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`10` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`10` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-18/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-18/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac26_winner_772_20260127_020038.json` (index `26`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`1` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R6 col1 67724** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col2 6775244** [hit-family-gap,hit-winner-gap] | Draw4:R8 col1 77624** [hit-family-gap,hit-winner-gap] | Draw4:R8 col2 7762445** [hit-family-gap,hit-winner-gap] | Draw5:R6 col1 677324** [hit-family-gap,hit-winner-gap]`

### 2026-01-18 — NorthCarolina4 — Midday — 094 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-18/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-18/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac15_winner_094_20260127_020037.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-18 — Ohio4 — Evening — 961 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-18/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-18/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_961_20260127_020040.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-18 — OntarioCanada4 — Evening — 119 (double)

- Winner canonical: `119`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`7` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-18/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-18/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac19_winner_119_20260127_020043.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 5224366** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col2 2256634** [hit-family-gap] | Draw5:R2 col2 52244366** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col2 22566344** [hit-family-gap] | Draw5:R8 col2 36622445** [hit-vt-straight-gap] | Draw6:R8 col2 70836622445 [hit-vt-straight-gap]`

### 2026-01-18 — Pennsylvania4 — Evening — 461 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-18/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-18/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-18/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac19_winner_461_20260127_020046.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 4186** [hit-family-gap,hit-winner-gap] | Draw2:R2 col2 41866** [hit-family-gap,hit-winner-gap] | Draw2:R4 col1 6841** [hit-family-gap,hit-winner-gap] | Draw2:R4 col2 66841** [hit-family-gap,hit-winner-gap] | Draw2:R6 col1 6814** [hit-family-gap,hit-winner-gap] | Draw2:R6 col2 66814** [hit-family-gap,hit-winner-gap]`

