# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-03-30T08:33:00.391674+00:00`
- Rows: `75`

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
| double | 41 | 29 | 6 | 13 | 41 | 8.80 | 0.88 | 2.20 | 0.95 |
| triple | 1 | 0 | 0 | 0 | 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| mirror_double | 33 | 27 | 12 | 21 | 33 | 11.15 | 1.88 | 2.39 | 0.82 |

## Per-event evidence pointers

### 2025-12-30 — Connecticut4 — Midday — 095 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Connecticut4.md`
- Winners lens dir: `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_095_20260105_051145.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`26` hit-winner-cells=`8` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`2` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 590386** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R2 col2 590386** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw4:R4 col1 590683** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R4 col2 590683** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col1 680593** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col2 680593** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2025-12-30 — Florida4 — Midday — 377 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Florida4.md`
- Winners lens dir: `sharepacks/2025-12-30/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2025-12-30/Florida4/winners/Florida4/Florida4_vtrac27_winner_377_20260105_051152.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`6` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`3` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 013388677** [hit-family-gap] | Draw4:R2 col2 013388677** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 068833771** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw4:R4 col2 068833771** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw4:R6 col1 688177033** [hit-family-gap,hit-winner-gap] | Draw4:R6 col2 688177033** [hit-family-gap,hit-winner-gap]`

### 2025-12-30 — Indiana4 — Midday — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Indiana4.md`
- Winners lens dir: `sharepacks/2025-12-30/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2025-12-30/Indiana4/winners/Indiana4/Indiana4_vtrac4_winner_585_20260105_051154.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 508866** [hit-family,hit-family-gap] | Draw2:R2 col2 508866** [hit-family,hit-family-gap] | Draw2:R6 col1 668805** [hit-family,hit-family-gap] | Draw2:R6 col2 668805** [hit-family,hit-family-gap] | Draw3:R2 col1 5088667** [hit-family,hit-family-gap] | Draw3:R2 col2 5088667** [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2025-12-30 — Michigan4 — Midday — 250 (mirror_double)

- Winner canonical: `025`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Michigan4.md`
- Winners lens dir: `sharepacks/2025-12-30/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2025-12-30/Michigan4/winners/Michigan4/Michigan4_vtrac3_winner_250_20260105_051157.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`16` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`4` family_recentest_draw=`1` winner_recentest_draw=`3`
- Winners lens samples: `Draw1:R2 col1 002** [hit-family,hit-family-gap] | Draw1:R4 col1 002** [hit-family,hit-family-gap] | Draw1:R6 col1 002** [hit-family,hit-family-gap] | Draw1:R8 col1 002** [hit-family,hit-family-gap] | Draw3:R2 col1 520036** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw3:R2 col2 52001336** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge]`

### 2025-12-30 — NewYork4 — Midday — 051 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__NewYork4.md`
- Winners lens dir: `sharepacks/2025-12-30/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2025-12-30/NewYork4/winners/NewYork4/NewYork4_vtrac2_winner_051_20260105_051203.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`23` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 520016** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R2 col2 52200116** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col1 250061** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R4 col2 22500611** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R6 col1 610052** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R6 col2 61100522** [hit-family,hit-family-gap,hit-vt-straight,hit-winner-gap]`

### 2025-12-30 — NorthCarolina4 — Midday — 455 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac5_winner_455_20260105_051206.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`34` hit-winner-cells=`0` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 22400** [hit-family,hit-family-gap] | Draw2:R2 col2 224006** [hit-family,hit-family-gap] | Draw2:R4 col1 22004** [hit-family,hit-family-gap] | Draw2:R4 col2 220064** [hit-family-gap] | Draw3:R2 col1 9224003** [hit-family,hit-family-gap] | Draw3:R2 col2 92240036** [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2025-12-30 — Ohio4 — Evening — 327 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Ohio4.md`
- Winners lens dir: `sharepacks/2025-12-30/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2025-12-30/Ohio4/winners/Ohio4/Ohio4_vtrac27_winner_327_20260105_051209.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 59038677** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 59068377** [hit-family,hit-family-gap] | Draw5:R4 col2 5990668377** [hit-family,hit-family-gap] | Draw5:R6 col1 68770593** [hit-family,hit-family-gap] | Draw5:R6 col2 6687705993** [hit-family,hit-family-gap] | Draw6:R2 col1 5903388677* [hit-family-gap,ls-box,ls-box-edge]`

### 2025-12-30 — Ohio4 — Midday — 338 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Ohio4.md`
- Winners lens dir: `sharepacks/2025-12-30/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2025-12-30/Ohio4/winners/Ohio4/Ohio4_vtrac32_winner_338_20260105_051209.json` (index `32`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — OntarioCanada4 — Evening — 372 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac27_winner_372_20260105_051211.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — OntarioCanada4 — Midday — 409 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac15_winner_409_20260105_051210.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 552244188677 [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw7:R6 col1 688177552244 [hit-vt-straight-gap] | Draw7:R8 col1 771886224455 [hit-family,hit-family-gap,hit-vt-straight]`

### 2025-12-30 — Pennsylvania4 — Midday — 186 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`9` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_186_20260105_051212.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 591388677* [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R6 col1 688177593* [hit-family-gap,hit-winner-gap] | Draw6:R6 col2 68817759933 [hit-family-gap,hit-winner-gap] | Draw7:R2 col1 594011388677 [hit-family,hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R6 col1 688117705934 [hit-family,hit-family-gap,hit-vt-straight,hit-winner-gap] | Draw7:R8 col1 770119883645 [hit-family-gap]`

### 2025-12-30 — Virginia4 — Evening — 100 (double)

- Winner canonical: `001`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-30/Virginia4/winners/Virginia4/Virginia4_vtrac2_winner_100_20260105_051221.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — Virginia4 — Midday — 888 (triple)

- Winner canonical: `888`
- Mirror pairs: `` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-30/Virginia4/winners/Virginia4/Virginia4_vtracNone_winner_888_20260105_051221.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — Connecticut4 — Evening — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Connecticut4.md`
- Winners lens dir: `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_361_20260105_052142.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 921186** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 924118667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 296811** [hit-family,hit-family-gap] | Draw5:R4 col2 296684711** [hit-family,hit-family-gap] | Draw5:R6 col1 681192** [hit-family,hit-family-gap] | Draw5:R6 col2 668117924** [hit-family,hit-family-gap]`

### 2025-12-31 — Delaware4 — Evening — 337 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Delaware4.md`
- Winners lens dir: `sharepacks/2025-12-31/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2025-12-31/Delaware4/winners/Delaware4/Delaware4_vtrac29_winner_337_20260105_052144.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col2 559944113877 [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2025-12-31 — Florida4 — Evening — 211 (double)

- Winner canonical: `112`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Florida4.md`
- Winners lens dir: `sharepacks/2025-12-31/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2025-12-31/Florida4/winners/Florida4/Florida4_vtrac17_winner_211_20260105_052147.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`24` hit-winner-cells=`0` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 5924167** [hit-family,hit-family-gap] | Draw4:R2 col2 59241677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 2596471** [hit-family-gap] | Draw4:R4 col2 25964771** [hit-family-gap] | Draw4:R6 col1 6175924** [hit-family,hit-family-gap] | Draw4:R6 col2 61775924** [hit-family,hit-family-gap]`

### 2025-12-31 — Michigan4 — Evening — 477 (double)

- Winner canonical: `477`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Michigan4.md`
- Winners lens dir: `sharepacks/2025-12-31/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2025-12-31/Michigan4/winners/Michigan4/Michigan4_vtrac28_winner_477_20260105_052152.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`1` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R4 col1 25506334771 [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2025-12-31 — Michigan4 — Midday — 583 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Michigan4.md`
- Winners lens dir: `sharepacks/2025-12-31/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2025-12-31/Michigan4/winners/Michigan4/Michigan4_vtrac13_winner_583_20260105_052151.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 013866** [hit-family-gap] | Draw4:R2 col2 520013866** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R6 col1 668103** [hit-family-gap] | Draw4:R8 col1 018366** [hit-family-gap] | Draw4:R8 col2 001836625** [hit-family-gap] | Draw5:R2 col1 013866** [hit-family-gap,ls-box,ls-box-edge]`

### 2025-12-31 — NewJersey4 — Midday — 366 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__NewJersey4.md`
- Winners lens dir: `sharepacks/2025-12-31/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2025-12-31/NewJersey4/winners/NewJersey4/NewJersey4_vtrac18_winner_366_20260105_052153.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`19` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col2 22118** [hit-family,hit-family-gap] | Draw1:R4 col2 22811** [hit-family,hit-family-gap] | Draw1:R6 col2 81122** [hit-family,hit-family-gap] | Draw1:R8 col2 11822** [hit-family,hit-family-gap] | Draw2:R2 col2 22118** [hit-family,hit-family-gap] | Draw2:R4 col2 22811** [hit-family,hit-family-gap]`

### 2025-12-31 — NewYork4 — Evening — 116 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__NewYork4.md`
- Winners lens dir: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2025-12-31/NewYork4/winners/NewYork4/NewYork4_vtrac16_winner_116_20260105_052157.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — NewYork4 — Midday — 419 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__NewYork4.md`
- Winners lens dir: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2025-12-31/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_419_20260105_052156.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — NorthCarolina4 — Evening — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_057_20260105_052159.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`26` hit-winner-cells=`0` hit-vt-straight-cells=`12` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col2 55007** [hit-family,hit-family-gap,hit-winner-gap] | Draw2:R4 col2 55007** [hit-family,hit-family-gap,hit-winner-gap] | Draw2:R6 col2 70055** [hit-family,hit-family-gap,hit-winner-gap] | Draw2:R8 col2 70055** [hit-family,hit-family-gap,hit-winner-gap] | Draw3:R6 col2 8700553** [hit-family,hit-family-gap,hit-winner-gap] | Draw3:R8 col2 7008355** [hit-family,hit-family-gap]`

### 2025-12-31 — Pennsylvania4 — Evening — 221 (double)

- Winner canonical: `122`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac20_winner_221_20260105_052208.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R4 col2 8337711** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 8117733** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R8 col2 7711833** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 588337711** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col2 881177533** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R8 col2 771188335** [hit-family,hit-family-gap,hit-vt-straight]`

### 2025-12-31 — SouthCarolina4 — Evening — 044 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`11` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`11` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac15_winner_044_20260105_052214.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — Virginia4 — Evening — 636 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-31/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-31/Virginia4/winners/Virginia4/Virginia4_vtrac18_winner_636_20260105_052216.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 59411877** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R6 col2 81177594** [hit-family,hit-family-gap] | Draw4:R8 col2 77119845** [hit-family-gap] | Draw5:R2 col2 5922411877** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col2 8117759224** [hit-family,hit-family-gap] | Draw5:R8 col2 7711982245** [hit-family-gap]`

### 2025-12-31 — Virginia4 — Midday — 686 (double)

- Winner canonical: `668`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-31__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-31/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-31/Virginia4/winners/Virginia4/Virginia4_vtrac18_winner_686_20260105_052215.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`41` hit-winner-cells=`0` hit-vt-straight-cells=`41` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col1 113366** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R2 col2 113366** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col1 663311** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col2 663311** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col1 661133** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col2 661133** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-01 — Connecticut4 — Midday — 228 (double)

- Winner canonical: `228`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_228_20260105_053356.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`0` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 54388677** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 5943388677** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 56883477** [hit-family-gap] | Draw5:R4 col2 5968833477** [hit-family-gap] | Draw5:R6 col1 68877534** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col2 6887759334** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-01 — Delaware4 — Midday — 149 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-01/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-01/Delaware4/winners/Delaware4/Delaware4_vtrac25_winner_149_20260105_053359.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`28` hit-winner-cells=`0` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 441** [hit-family,hit-family-gap] | Draw2:R2 col2 441** [hit-family,hit-family-gap] | Draw2:R4 col1 441** [hit-family,hit-family-gap] | Draw2:R4 col2 441** [hit-family,hit-family-gap] | Draw2:R6 col1 144** [hit-family,hit-family-gap] | Draw2:R6 col2 144** [hit-family,hit-family-gap]`

### 2026-01-01 — Indiana4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-01/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-01/Indiana4/winners/Indiana4/Indiana4_vtrac15_winner_909_20260105_053406.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 2440138677* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 24401338677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R2 col1 924401388677 [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-01 — Indiana4 — Midday — 474 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-01/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-01/Indiana4/winners/Indiana4/Indiana4_vtrac31_winner_474_20260105_053405.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 992013386677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R4 col1 299066833771 [hit-family,hit-family-gap] | Draw7:R6 col1 668177099332 [hit-family-gap]`

### 2026-01-01 — NewJersey4 — Evening — 504 (mirror_double)

- Winner canonical: `045`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4/NewJersey4_vtrac5_winner_504_20260105_053411.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`11` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 59922400877* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 5992244008877 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R4 col1 22599008477* [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R4 col2 2259900884477 [hit-family,hit-family-gap,hit-vt-straight,hit-vt-straight-gap] | Draw6:R6 col1 87700599224* [hit-family,hit-family-gap] | Draw6:R6 col2 8877005992244 [hit-family,hit-family-gap]`

### 2026-01-01 — NewJersey4 — Midday — 770 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4/NewJersey4_vtrac10_winner_770_20260105_053410.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`2` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R6 col1 881770599324 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R8 col1 770199883245 [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-01 — NewYork4 — Midday — 117 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-01/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-01/NewYork4/winners/NewYork4/NewYork4_vtrac17_winner_117_20260105_053412.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`13` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 5206677** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R2 col2 52406677** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R4 col1 2506677** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 25066477** [hit-family-gap] | Draw5:R6 col1 6677052** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col2 66770524** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-01 — NorthCarolina4 — Evening — 053 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_053_20260105_053415.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`28` hit-winner-cells=`11` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`5` family_recentest_draw=`2` winner_recentest_draw=`2`
- Winners lens samples: `Draw2:R2 col1 503** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw2:R2 col2 55003** [hit-family,hit-family-gap,hit-winner-gap] | Draw2:R4 col1 503** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw2:R4 col2 55003** [hit-family,hit-family-gap,hit-winner-gap] | Draw2:R6 col1 053** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw2:R6 col2 00553** [hit-family,hit-family-gap,hit-winner-gap]`

### 2026-01-01 — NorthCarolina4 — Midday — 416 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac19_winner_416_20260105_053414.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R4 col1 2290033411** [hit-family,hit-family-gap] | Draw5:R4 col2 2290033411** [hit-family,hit-family-gap] | Draw5:R8 col1 0011933224** [hit-family,hit-family-gap] | Draw5:R8 col2 0011933224** [hit-family,hit-family-gap] | Draw6:R4 col1 22990033411* [hit-family,hit-family-gap] | Draw6:R4 col2 229900334711 [hit-family-gap]`

### 2026-01-01 — Ohio4 — Evening — 416 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-01/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-01/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_416_20260105_053418.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-01 — Pennsylvania4 — Evening — 328 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac29_winner_328_20260105_053423.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 387** [hit-family,hit-family-gap] | Draw3:R2 col2 1387** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 837** [hit-family,hit-family-gap] | Draw3:R4 col2 8371** [hit-family,hit-family-gap] | Draw3:R6 col1 873** [hit-family,hit-family-gap] | Draw3:R6 col2 8173** [hit-family-gap]`

### 2026-01-01 — Pennsylvania4 — Midday — 322 (double)

- Winner canonical: `223`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`11` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`11` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac27_winner_322_20260105_053422.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 59377** [hit-family,hit-family-gap] | Draw4:R2 col2 593877** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 59377** [hit-family,hit-family-gap] | Draw4:R4 col2 598377** [hit-family,hit-family-gap] | Draw4:R6 col2 877593** [hit-family,hit-family-gap] | Draw4:R8 col1 77935** [hit-family-gap]`

### 2026-01-02 — Delaware4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-02/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`3` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 2416** [hit-family-gap,hit-winner-gap] | Draw4:R4 col1 2641** [hit-family-gap,hit-winner-gap] | Draw4:R6 col1 6124** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col2 611244** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R8 col1 1624** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R8 col2 116244** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-02 — Indiana4 — Midday — 974 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-02/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-02/Indiana4/winners/Indiana4/Indiana4_vtrac31_winner_974_20260105_070905.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 99201338667* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 992013386677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 29906683371* [hit-family,hit-family-gap] | Draw6:R4 col2 299066833771 [hit-family,hit-family-gap] | Draw6:R6 col1 66817099332* [hit-family-gap] | Draw6:R6 col2 668177099332 [hit-family-gap]`

### 2026-01-02 — NewJersey4 — Evening — 331 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4/NewJersey4_vtrac23_winner_331_20260105_070912.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 99220138677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R4 col1 22990683771 [hit-family,hit-family-gap] | Draw7:R8 col1 77019983622 [hit-family,hit-family-gap]`

### 2026-01-02 — NewJersey4 — Midday — 633 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4/NewJersey4_vtrac23_winner_633_20260105_070911.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 9924188** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 992418877** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 2998841** [hit-family-gap] | Draw5:R6 col1 8819924** [hit-family,hit-family-gap] | Draw5:R6 col2 881779924** [hit-family,hit-family-gap] | Draw6:R2 col1 599241388* [hit-family,hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-02 — NewYork4 — Midday — 998 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-02/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-02/NewYork4/winners/NewYork4/NewYork4_vtrac34_winner_998_20260105_070913.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 59240388667* [hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 592403886677 [hit-family-gap,ls-box,ls-box-edge] | Draw6:R6 col1 66887059324* [hit-family-gap] | Draw6:R6 col2 668877059324 [hit-family-gap]`

### 2026-01-02 — NorthCarolina4 — Evening — 383 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac32_winner_383_20260105_070917.json` (index `32`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-02 — NorthCarolina4 — Midday — 033 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`7` hit-vt-straight-cells=`7` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`3` family_recentest_draw=`3` winner_recentest_draw=`3`
- Winners lens samples: `Draw3:R2 col1 9220033** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw3:R2 col2 922400133** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw3:R4 col1 2290033** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw3:R4 col2 229003341** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw3:R6 col1 0093322** [hit-family-gap,hit-winner-gap] | Draw3:R6 col2 100933224** [hit-family-gap,hit-winner-gap]`

### 2026-01-02 — Ohio4 — Evening — 133 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-02/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-02/Ohio4/winners/Ohio4/Ohio4_vtrac23_winner_133_20260105_070918.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`20` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col2 503886** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col2 506883** [hit-family,hit-family-gap] | Draw3:R6 col2 688053** [hit-family,hit-family-gap] | Draw3:R8 col2 088365** [hit-family,hit-family-gap] | Draw4:R2 col2 55003886** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col2 55006883** [hit-family,hit-family-gap]`

### 2026-01-02 — Ohio4 — Midday — 747 (double)

- Winner canonical: `477`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-02/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-02/Ohio4/winners/Ohio4/Ohio4_vtrac28_winner_747_20260105_070917.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`24` hit-winner-cells=`0` hit-vt-straight-cells=`14` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col2 5522417** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R6 col2 1755224** [hit-family,hit-family-gap] | Draw3:R8 col2 7122455** [hit-family,hit-family-gap] | Draw4:R2 col1 552241** [hit-family,hit-family-gap] | Draw4:R2 col2 552244167** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R6 col1 155224** [hit-family,hit-family-gap]`

### 2026-01-02 — OntarioCanada4 — Evening — 816 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac18_winner_816_20260105_070920.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`44` hit-winner-cells=`0` hit-vt-straight-cells=`44` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col1 1188** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R2 col2 541188** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col1 8811** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col2 588411** [hit-family-gap] | Draw1:R6 col1 8811** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col2 881154** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-02 — OntarioCanada4 — Midday — 053 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac4_winner_053_20260105_070919.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`1` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`1` family_recentest_draw=`6` winner_recentest_draw=`7`
- Winners lens samples: `Draw2:R4 col2 2255687** [hit-family-gap] | Draw2:R6 col2 6875522** [hit-family-gap] | Draw3:R4 col2 2255687** [hit-family-gap] | Draw3:R6 col2 6875522** [hit-family-gap] | Draw4:R4 col2 225568477** [hit-family-gap] | Draw5:R4 col2 225568477** [hit-family-gap]`

### 2026-01-02 — PuertoRico4 — Midday — 144 (double)

- Winner canonical: `144`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`10` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`10` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_144_20260105_070924.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`10` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`6` family_recentest_draw=`1` winner_recentest_draw=`1`
- Winners lens samples: `Draw1:R2 col2 54413** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R4 col2 53441** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R8 col2 13445** [hit-family-gap,hit-winner-gap] | Draw2:R2 col2 544113** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw2:R4 col2 534411** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw2:R8 col2 113445** [hit-family-gap,hit-winner-gap]`

### 2026-01-02 — SouthCarolina4 — Midday — 308 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-02__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac13_winner_308_20260105_070926.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`4` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`2` family_recentest_draw=`3` winner_recentest_draw=`3`
- Winners lens samples: `Draw3:R2 col1 90387** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw3:R2 col2 99001387** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw3:R4 col1 90837** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw3:R4 col2 99008371** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw3:R6 col1 87093** [hit-family-gap,hit-winner-gap] | Draw3:R8 col1 70983** [hit-family-gap,hit-winner-gap]`

### 2026-01-03 — Connecticut4 — Evening — 181 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_181_20260105_054534.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Connecticut4 — Midday — 533 (double)

- Winner canonical: `335`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac13_winner_533_20260105_054533.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 54386** [hit-family-gap] | Draw2:R2 col2 54386** [hit-family-gap] | Draw2:R4 col1 56834** [hit-family-gap] | Draw2:R4 col2 56834** [hit-family-gap] | Draw2:R6 col1 68534** [hit-family,hit-family-gap] | Draw2:R6 col2 68534** [hit-family,hit-family-gap]`

### 2026-01-03 — Delaware4 — Evening — 797 (double)

- Winner canonical: `779`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-03/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-03/Delaware4/winners/Delaware4/Delaware4_vtrac28_winner_797_20260105_054536.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`0` hit-vt-straight-cells=`21` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 592244118** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R2 col2 5922440118** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col1 225984411** [hit-family-gap] | Draw4:R4 col2 2259084411** [hit-family-gap] | Draw4:R6 col1 811592244** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 8110592244** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-03 — Delaware4 — Midday — 422 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`5` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-03/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-03/Delaware4/winners/Delaware4/Delaware4_vtrac28_winner_422_20260105_054535.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 55906833477 [hit-family,hit-family-gap] | Draw7:R8 col1 77098336455 [hit-family-gap]`

### 2026-01-03 — Florida4 — Evening — 611 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-03/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-03/Florida4/winners/Florida4/Florida4_vtrac16_winner_611_20260105_054538.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Indiana4 — Evening — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-03/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-03/Indiana4/winners/Indiana4/Indiana4_vtrac25_winner_199_20260105_054540.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`16` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col1 244167** [hit-family,hit-family-gap] | Draw1:R2 col2 244167** [hit-family,hit-family-gap] | Draw1:R4 col1 264471** [hit-family,hit-family-gap] | Draw1:R4 col2 264471** [hit-family,hit-family-gap] | Draw1:R8 col1 716244** [hit-family-gap] | Draw1:R8 col2 716244** [hit-family-gap]`

### 2026-01-03 — Indiana4 — Midday — 527 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-03/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-03/Indiana4/winners/Indiana4/Indiana4_vtrac10_winner_527_20260105_054539.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Michigan4 — Evening — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-03/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-03/Michigan4/winners/Michigan4/Michigan4_vtrac31_winner_479_20260105_054542.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Ohio4 — Evening — 411 (double)

- Winner canonical: `114`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-03/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-03/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_411_20260105_054556.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Pennsylvania4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac15_winner_909_20260105_054601.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`32` hit-winner-cells=`10` hit-vt-straight-cells=`24` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`4` family_recentest_draw=`3` winner_recentest_draw=`4`
- Winners lens samples: `Draw3:R2 col1 59987** [hit-family,hit-family-gap] | Draw3:R2 col2 59987** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 59987** [hit-family,hit-family-gap] | Draw3:R4 col2 59987** [hit-family,hit-family-gap] | Draw3:R6 col1 87599** [hit-family,hit-family-gap] | Draw3:R6 col2 87599** [hit-family,hit-family-gap]`

### 2026-01-03 — Pennsylvania4 — Midday — 744 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac31_winner_744_20260105_054600.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 59407** [hit-family-gap] | Draw4:R4 col1 59047** [hit-family-gap] | Draw4:R4 col2 5904771** [hit-family-gap] | Draw4:R8 col1 70945** [hit-family-gap]`

### 2026-01-03 — SouthCarolina4 — Evening — 051 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-03__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac2_winner_051_20260105_054608.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`10` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`1` winner_recentest_draw=`1`
- Winners lens samples: `Draw1:R2 col1 051** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R2 col2 051** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R4 col1 051** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R4 col2 051** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R6 col1 015** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R6 col2 015** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-04 — Connecticut4 — Evening — 311 (double)

- Winner canonical: `113`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_311_20260105_055125.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-04 — Delaware4 — Midday — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-04/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-04/Delaware4/winners/Delaware4/Delaware4_vtrac3_winner_057_20260105_055126.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`2` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`1` family_recentest_draw=`5` winner_recentest_draw=`6`
- Winners lens samples: `Draw5:R6 col1 8755933** [hit-family,hit-family-gap] | Draw5:R6 col2 87559334** [hit-family,hit-family-gap] | Draw6:R6 col1 6877055933* [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R6 col2 68770559334 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R6 col1 688770055933 [hit-family,hit-family-gap,hit-vt-straight,hit-winner-gap] | Draw7:R8 col1 770098833655 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-04 — Florida4 — Midday — 171 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-04/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-04/Florida4/winners/Florida4/Florida4_vtrac17_winner_171_20260105_055129.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 5924136** [hit-family-gap,ls-box,ls-box-edge] | Draw6:R6 col2 68170593324 [hit-family-gap] | Draw7:R6 col1 61705933244 [hit-family,hit-family-gap]`

### 2026-01-04 — Indiana4 — Midday — 813 (mirror_double)

- Winner canonical: `138`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-04/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-04/Indiana4/winners/Indiana4/Indiana4_vtrac23_winner_813_20260105_055131.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`42` hit-winner-cells=`2` hit-vt-straight-cells=`22` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`1` family_recentest_draw=`1` winner_recentest_draw=`3`
- Winners lens samples: `Draw1:R2 col1 03866** [hit-family,hit-family-gap] | Draw1:R2 col2 203866** [hit-family,hit-family-gap] | Draw1:R4 col1 06683** [hit-family,hit-family-gap] | Draw1:R4 col2 206683** [hit-family,hit-family-gap] | Draw1:R6 col1 66803** [hit-family-gap] | Draw1:R6 col2 668032** [hit-family-gap]`

### 2026-01-04 — NewJersey4 — Evening — 261 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4/NewJersey4_vtrac17_winner_261_20260105_055139.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col2 59922086677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R4 col2 22599066877 [hit-family-gap] | Draw6:R6 col2 66877059922 [hit-family-gap] | Draw6:R8 col2 77099866225 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-04 — NewJersey4 — Midday — 275 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4/NewJersey4_vtrac10_winner_275_20260105_055138.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col2 5599224401188 [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw6:R4 col2 2255990884411 [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R6 col2 8811055992244 [hit-vt-straight-gap] | Draw6:R8 col2 0119988224455 [hit-vt-straight-gap]`

### 2026-01-04 — NewYork4 — Evening — 489 (mirror_double)

- Winner canonical: `489`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-04/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-04/NewYork4/winners/NewYork4/NewYork4_vtrac34_winner_489_20260105_055141.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`1` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`1` family_recentest_draw=`2` winner_recentest_draw=`2`
- Winners lens samples: `Draw2:R2 col2 94887** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw2:R4 col2 98847** [hit-family-gap,hit-winner-gap] | Draw2:R6 col2 88794** [hit-family-gap,hit-winner-gap] | Draw2:R8 col2 79884** [hit-family-gap,hit-winner-gap] | Draw3:R8 col2 7009884** [hit-family-gap,hit-winner-gap] | Draw4:R6 col2 88700934** [hit-family,hit-family-gap]`

### 2026-01-04 — NorthCarolina4 — Evening — 887 (double)

- Winner canonical: `788`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac29_winner_887_20260105_055144.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-04 — Ohio4 — Evening — 492 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-04/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-04/Ohio4/winners/Ohio4/Ohio4_vtrac31_winner_492_20260105_055147.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`2` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`1` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col2 5592400886** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R6 col2 6880055924** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R2 col2 559224008867 [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R6 col2 688700559224 [hit-family-gap,hit-winner-gap] | Draw7:R2 col1 5599220088677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw7:R4 col1 2255990068877 [hit-vt-straight-gap]`

### 2026-01-04 — OntarioCanada4 — Evening — 382 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`7` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac29_winner_382_20260105_055149.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`2` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`6` winner_recentest_draw=`6`
- Winners lens samples: `Draw6:R2 col2 59240013877 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col2 25900834771 [hit-family-gap] | Draw6:R8 col2 77001983245 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R2 col1 59924013877 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R4 col1 25990834771 [hit-family-gap] | Draw7:R8 col1 77019983245 [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-04 — Virginia4 — Evening — 217 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-04/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-04/Virginia4/winners/Virginia4/Virginia4_vtrac20_winner_217_20260105_055157.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col1 2218** [hit-family,hit-family-gap] | Draw1:R2 col2 922187** [hit-family,hit-family-gap,hit-winner-gap] | Draw1:R4 col1 2281** [hit-family-gap] | Draw1:R6 col1 8122** [hit-family,hit-family-gap] | Draw1:R6 col2 817922** [hit-family-gap,hit-winner-gap] | Draw1:R8 col1 1822** [hit-family-gap]`

### 2026-01-04 — Virginia4 — Midday — 200 (double)

- Winner canonical: `002`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-04/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-04/Virginia4/winners/Virginia4/Virginia4_vtrac3_winner_200_20260105_055156.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`20` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 552377** [hit-family,hit-family-gap] | Draw4:R2 col2 552243377** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col1 255377** [hit-family,hit-family-gap] | Draw4:R4 col2 225533477** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col1 775532** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 775533224** [hit-family,hit-family-gap,hit-vt-straight,hit-vt-straight-gap]`

