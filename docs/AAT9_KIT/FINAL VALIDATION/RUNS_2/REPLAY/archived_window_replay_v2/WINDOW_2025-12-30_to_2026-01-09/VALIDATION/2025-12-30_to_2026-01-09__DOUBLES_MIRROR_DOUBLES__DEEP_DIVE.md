# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-04-22T05:52:13.417558+00:00`
- Rows: `149`

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
| double | 82 | 60 | 17 | 33 | 82 | 7.91 | 1.39 | 2.12 | 0.91 |
| triple | 3 | 0 | 0 | 0 | 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| mirror_double | 64 | 45 | 17 | 32 | 63 | 9.14 | 1.30 | 2.17 | 0.61 |

## Per-event evidence pointers

### 2025-12-30 — Connecticut4 — Midday — 095 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Connecticut4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Florida4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Michigan4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__NewYork4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__NorthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Ohio4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Ohio4.md`
- Winners lens dir: `sharepacks/2025-12-30/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2025-12-30/Ohio4/winners/Ohio4/Ohio4_vtrac32_winner_338_20260105_051209.json` (index `32`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — OntarioCanada4 — Evening — 372 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac27_winner_372_20260105_051211.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — OntarioCanada4 — Midday — 409 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__OntarioCanada4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-30/Virginia4/winners/Virginia4/Virginia4_vtrac2_winner_100_20260105_051221.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-30 — Virginia4 — Midday — 888 (triple)

- Winner canonical: `888`
- Mirror pairs: `` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Virginia4.md`
- Winners lens dir: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2025-12-30/Virginia4/winners/Virginia4/Virginia4_vtracNone_winner_888_20260105_051221.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — Connecticut4 — Evening — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Connecticut4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Florida4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Michigan4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Michigan4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__NewYork4.md`
- Winners lens dir: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2025-12-31/NewYork4/winners/NewYork4/NewYork4_vtrac16_winner_116_20260105_052157.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — NewYork4 — Midday — 419 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__NewYork4.md`
- Winners lens dir: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2025-12-31/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_419_20260105_052156.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — NorthCarolina4 — Evening — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__NorthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac15_winner_044_20260105_052214.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2025-12-31 — Virginia4 — Evening — 636 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Virginia4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-31__Virginia4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Connecticut4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__NewYork4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__NorthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__NorthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-01/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-01/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_416_20260105_053418.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-01 — Pennsylvania4 — Evening — 328 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-01__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__NewYork4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac32_winner_383_20260105_070917.json` (index `32`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-02 — NorthCarolina4 — Midday — 033 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__NorthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__Ohio4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__Ohio4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__OntarioCanada4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__OntarioCanada4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__PuertoRico4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-02__SouthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_181_20260105_054534.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Connecticut4 — Midday — 533 (double)

- Winner canonical: `335`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Connecticut4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-03/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-03/Florida4/winners/Florida4/Florida4_vtrac16_winner_611_20260105_054538.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Indiana4 — Evening — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-03/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-03/Indiana4/winners/Indiana4/Indiana4_vtrac10_winner_527_20260105_054539.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Michigan4 — Evening — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-03/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-03/Michigan4/winners/Michigan4/Michigan4_vtrac31_winner_479_20260105_054542.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Ohio4 — Evening — 411 (double)

- Winner canonical: `114`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-03/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-03/Ohio4/winners/Ohio4/Ohio4_vtrac19_winner_411_20260105_054556.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-03 — Pennsylvania4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Pennsylvania4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__SouthCarolina4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_311_20260105_055125.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-04 — Delaware4 — Midday — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Delaware4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Florida4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Indiana4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__NewJersey4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__NewYork4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac29_winner_887_20260105_055144.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-04 — Ohio4 — Evening — 492 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Ohio4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__OntarioCanada4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Virginia4.md`
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
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-04__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-04/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-04/Virginia4/winners/Virginia4/Virginia4_vtrac3_winner_200_20260105_055156.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`20` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 552377** [hit-family,hit-family-gap] | Draw4:R2 col2 552243377** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col1 255377** [hit-family,hit-family-gap] | Draw4:R4 col2 225533477** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col1 775532** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 775533224** [hit-family,hit-family-gap,hit-vt-straight,hit-vt-straight-gap]`

### 2026-01-05 — Connecticut4 — Evening — 660 (double)

- Winner canonical: `066`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_660_20260128_160503.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-05 — Delaware4 — Evening — 267 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-05/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-05/Delaware4/winners/Delaware4/Delaware4_vtrac20_winner_267_20260128_160505.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col2 52244118** [hit-vt-straight-gap] | Draw2:R6 col2 81152244** [hit-family-gap] | Draw2:R8 col2 11822445** [hit-family-gap] | Draw3:R8 col2 011822445** [hit-family-gap] | Draw4:R8 col2 0118822445** [hit-vt-straight-gap] | Draw5:R8 col2 011886224455** [hit-family,hit-family-gap]`

### 2026-01-05 — Florida4 — Evening — 994 (double)

- Winner canonical: `499`
- Mirror pairs: `4/9` | vtrac_group_family: `4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-05/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-05/Florida4/winners/Florida4/Florida4_vtrac35_winner_994_20260128_160507.json` (index `35`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-05 — Florida4 — Midday — 080 (double)

- Winner canonical: `008`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-05/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-05/Florida4/winners/Florida4/Florida4_vtrac4_winner_080_20260128_160506.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw6:R4 col1 259063344* [hit-family-gap] | Draw6:R4 col2 25906334471 [hit-family-gap] | Draw6:R6 col1 605933244* [hit-family-gap] | Draw6:R6 col2 61705933244 [hit-family-gap] | Draw7:R6 col1 60559933244 [hit-vt-straight-gap]`

### 2026-01-05 — Michigan4 — Evening — 772 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-05/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-05/Michigan4/winners/Michigan4/Michigan4_vtrac26_winner_772_20260128_160513.json` (index `26`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-05 — NewJersey4 — Evening — 694 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-05/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-05/NewJersey4/winners/NewJersey4/NewJersey4_vtrac25_winner_694_20260128_160515.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-05 — NewYork4 — Midday — 080 (double)

- Winner canonical: `008`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-05/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-05/NewYork4/winners/NewYork4/NewYork4_vtrac4_winner_080_20260128_160515.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`17` hit-winner-cells=`8` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`2` family_recentest_draw=`3` winner_recentest_draw=`5`
- Winners lens samples: `Draw3:R2 col1 50866** [hit-family,hit-family-gap] | Draw3:R2 col2 508667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R6 col1 66805** [hit-family,hit-family-gap] | Draw3:R6 col2 668705** [hit-family-gap] | Draw4:R2 col1 520866** [hit-family-gap] | Draw4:R2 col2 52038667** [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-05 — NorthCarolina4 — Midday — 553 (double)

- Winner canonical: `355`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_553_20260128_160518.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw5:R6 col2 810559922** [hit-family-gap] | Draw6:R6 col1 680559922* [hit-family,hit-family-gap] | Draw7:R6 col1 668105599224 [hit-family-gap]`

### 2026-01-05 — Ohio4 — Evening — 711 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-05/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-05/Ohio4/winners/Ohio4/Ohio4_vtrac17_winner_711_20260128_160522.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 559200886677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw7:R4 col1 255900668877 [hit-vt-straight-gap] | Draw7:R6 col1 668877005592 [hit-vt-straight-gap] | Draw7:R8 col1 770098866255 [hit-family,hit-family-gap]`

### 2026-01-05 — Ohio4 — Midday — 651 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-05/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-05/Ohio4/winners/Ohio4/Ohio4_vtrac6_winner_651_20260128_160521.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`0` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 599220118** [hit-family,hit-family-gap] | Draw4:R2 col2 599220118** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 225990811** [hit-family-gap] | Draw4:R4 col2 225990811** [hit-family-gap] | Draw4:R6 col1 811059922** [hit-family,hit-family-gap] | Draw4:R6 col2 811059922** [hit-family,hit-family-gap]`

### 2026-01-05 — OntarioCanada4 — Evening — 797 (double)

- Winner canonical: `779`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac28_winner_797_20260128_160522.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R4 col1 5904771** [hit-family,hit-family-gap] | Draw5:R4 col2 59084771** [hit-family,hit-family-gap] | Draw6:R4 col1 59904771* [hit-family,hit-family-gap] | Draw6:R4 col2 25990834771 [hit-family,hit-family-gap] | Draw7:R4 col1 55990644771 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-05 — OntarioCanada4 — Midday — 555 (triple)

- Winner canonical: `555`
- Mirror pairs: `` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_555_20260128_160522.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-05 — Pennsylvania4 — Evening — 600 (double)

- Winner canonical: `006`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_600_20260128_160525.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R4 col1 556447** [hit-family,hit-family-gap] | Draw4:R4 col2 5568447** [hit-family,hit-family-gap] | Draw4:R6 col1 675544** [hit-family-gap] | Draw5:R4 col1 55644771** [hit-family,hit-family-gap] | Draw5:R4 col2 556844771** [hit-family,hit-family-gap] | Draw6:R4 col1 2556447711* [hit-family,hit-family-gap]`

### 2026-01-05 — PuertoRico4 — Evening — 972 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_972_20260128_160527.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 2240086** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 52240086** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col1 6800224** [hit-family,hit-family-gap] | Draw5:R6 col2 68005224** [hit-family,hit-family-gap] | Draw5:R8 col1 0086224** [hit-family,hit-family-gap] | Draw5:R8 col2 00862245** [hit-family,hit-family-gap]`

### 2026-01-05 — PuertoRico4 — Midday — 732 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac27_winner_732_20260128_160526.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 220366** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R6 col2 660322** [hit-family,hit-family-gap] | Draw5:R2 col2 922033667** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col1 6670332** [hit-family-gap,hit-winner-gap] | Draw5:R6 col2 667093322** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R8 col2 709336622** [hit-vt-straight-gap]`

### 2026-01-05 — SouthCarolina4 — Evening — 712 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac20_winner_712_20260128_160529.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`12` hit-winner-cells=`0` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 59936677** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R2 col2 5992336677** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R4 col1 59966377** [hit-family-gap] | Draw5:R4 col2 2599663377** [hit-vt-straight-gap] | Draw5:R6 col1 66775993** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col2 6677599332** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-05 — SouthCarolina4 — Midday — 171 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac17_winner_171_20260128_160528.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 921867** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col2 296871** [hit-family-gap] | Draw4:R6 col2 681792** [hit-family-gap] | Draw5:R2 col2 92241867** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R6 col2 68179224** [hit-family-gap] | Draw6:R2 col2 59224418677 [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-05 — Virginia4 — Evening — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-05/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-05/Virginia4/winners/Virginia4/Virginia4_vtrac4_winner_585_20260128_160531.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 92400188** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 9224001188** [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw5:R4 col1 29008841** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 2290088411** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R6 col1 88100924** [hit-family-gap] | Draw5:R6 col2 8811009224** [hit-vt-straight-gap]`

### 2026-01-06 — Connecticut4 — Evening — 737 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_737_20260107_052253.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`21` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 922487** [hit-family-gap] | Draw2:R2 col2 922487** [hit-family-gap] | Draw2:R4 col1 229847** [hit-family-gap] | Draw2:R4 col2 229847** [hit-family-gap] | Draw2:R6 col1 879224** [hit-family-gap] | Draw2:R6 col2 879224** [hit-family-gap]`

### 2026-01-06 — Delaware4 — Midday — 165 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-06/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-06/Delaware4/winners/Delaware4/Delaware4_vtrac6_winner_165_20260107_052254.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw6:R6 col1 681059334* [hit-family-gap,hit-winner-gap] | Draw7:R2 col1 59401133866 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R4 col1 59066833411 [hit-family,hit-family-gap] | Draw7:R6 col1 66811059334 [hit-family,hit-family-gap] | Draw7:R8 col1 01198336645 [hit-family,hit-family-gap]`

### 2026-01-06 — Florida4 — Evening — 160 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-06/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-06/Florida4/winners/Florida4/Florida4_vtrac6_winner_160_20260107_052258.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-06 — Indiana4 — Evening — 961 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-06/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-06/Indiana4/winners/Indiana4/Indiana4_vtrac19_winner_961_20260107_052301.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw3:R4 col2 206688447** [hit-vt-straight-gap] | Draw3:R8 col2 708866244** [hit-family-gap] | Draw4:R4 col2 2206688447** [hit-vt-straight-gap] | Draw4:R8 col2 7088662244** [hit-vt-straight-gap] | Draw5:R8 col2 70883662244** [hit-vt-straight-gap] | Draw6:R8 col2 700883662244 [hit-vt-straight-gap]`

### 2026-01-06 — Michigan4 — Midday — 618 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`9` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-06/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-06/Michigan4/winners/Michigan4/Michigan4_vtrac18_winner_618_20260107_052302.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`14` hit-winner-cells=`4` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`2` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col1 441187** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 44011867** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R6 col1 811744** [hit-family,hit-family-gap] | Draw5:R6 col2 68117044** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R8 col1 711844** [hit-family,hit-family-gap] | Draw5:R8 col2 70118644** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-06 — NewJersey4 — Evening — 942 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4/NewJersey4_vtrac31_winner_942_20260107_052306.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`6` hit-winner-cells=`4` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`2` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col2 592408877** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R6 col2 887705924** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R2 col2 559244008877 [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw6:R4 col2 255900884477 [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R6 col2 887700559244 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R8 col2 770098824455 [hit-family,hit-family-gap]`

### 2026-01-06 — NewYork4 — Midday — 181 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-06/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac18_winner_181_20260107_052307.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`24` hit-winner-cells=`5` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`2` family_recentest_draw=`2` winner_recentest_draw=`6`
- Winners lens samples: `Draw2:R2 col2 50866** [hit-family,hit-family-gap] | Draw2:R4 col2 50668** [hit-family,hit-family-gap] | Draw2:R6 col2 66805** [hit-family,hit-family-gap] | Draw2:R8 col2 08665** [hit-family,hit-family-gap] | Draw3:R2 col2 520866** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col2 250668** [hit-family,hit-family-gap]`

### 2026-01-06 — NorthCarolina4 — Midday — 552 (double)

- Winner canonical: `255`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_552_20260107_052309.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`5` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`3` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col2 5599220** [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw4:R4 col2 2255990** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw4:R6 col2 0559922** [hit-vt-straight-gap] | Draw4:R8 col2 0992255** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw5:R2 col2 559922086** [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw5:R4 col2 225599068** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap]`

### 2026-01-06 — OntarioCanada4 — Evening — 433 (double)

- Winner canonical: `334`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac33_winner_433_20260107_052315.json` (index `33`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-06 — OntarioCanada4 — Midday — 111 (triple)

- Winner canonical: `111`
- Mirror pairs: `` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_111_20260107_052315.json` (index `None`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-06 — Pennsylvania4 — Evening — 757 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-06__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac10_winner_757_20260107_052318.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`13` hit-winner-cells=`7` hit-vt-straight-cells=`13` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`4` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R4 col1 5544771** [hit-vt-straight-gap] | Draw4:R6 col1 1775544** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw4:R6 col2 61775544** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw5:R4 col1 255447711** [hit-vt-straight-gap] | Draw5:R6 col1 117755244** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap] | Draw5:R6 col2 6117755244** [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap]`

### 2026-01-07 — Connecticut4 — Evening — 553 (double)

- Winner canonical: `355`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac4_winner_553_20260110_033411.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R6 col1 805992244** [hit-family,hit-family-gap] | Draw6:R6 col1 8055992244* [hit-family,hit-family-gap] | Draw7:R6 col1 88055992244 [hit-family,hit-family-gap]`

### 2026-01-07 — Connecticut4 — Midday — 156 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_156_20260110_033410.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-07 — Delaware4 — Evening — 922 (double)

- Winner canonical: `229`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-07/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-07/Delaware4/winners/Delaware4/Delaware4_vtrac28_winner_922_20260110_033414.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-07 — Florida4 — Midday — 434 (double)

- Winner canonical: `344`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-07/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac34_winner_434_20260110_033415.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`22` hit-winner-cells=`16` hit-vt-straight-cells=`20` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`4` family_recentest_draw=`1` winner_recentest_draw=`4`
- Winners lens samples: `Draw1:R2 col2 9436** [hit-family,hit-family-gap] | Draw1:R4 col2 9634** [hit-family-gap] | Draw1:R6 col2 6934** [hit-family,hit-family-gap] | Draw1:R8 col2 9364** [hit-family-gap] | Draw2:R2 col2 592436** [hit-family-gap] | Draw2:R4 col2 259634** [hit-family-gap]`

### 2026-01-07 — Indiana4 — Midday — 823 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-07/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-07/Indiana4/winners/Indiana4/Indiana4_vtrac29_winner_823_20260110_033417.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-07 — Michigan4 — Evening — 616 (double)

- Winner canonical: `166`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-07/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 901866** [hit-family-gap,hit-winner-gap] | Draw2:R4 col1 906681** [hit-family-gap,hit-winner-gap] | Draw2:R6 col1 668109** [hit-family-gap,hit-winner-gap] | Draw3:R2 col1 9011866** [hit-family-gap,hit-winner-gap] | Draw3:R4 col1 9066811** [hit-family-gap,hit-winner-gap] | Draw3:R6 col1 6681109** [hit-family-gap,hit-winner-gap]`

### 2026-01-07 — NewJersey4 — Midday — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4/NewJersey4_vtrac18_winner_361_20260110_033422.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`18` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 94118** [hit-family,hit-family-gap] | Draw3:R2 col2 5941188** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw3:R4 col1 98411** [hit-family-gap] | Draw3:R4 col2 5988411** [hit-family-gap] | Draw3:R6 col1 81194** [hit-family,hit-family-gap] | Draw3:R6 col2 8811594** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-07 — NewYork4 — Midday — 916 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-07/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-07/NewYork4/winners/NewYork4/NewYork4_vtrac19_winner_916_20260110_033425.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 552466** [hit-family,hit-family-gap] | Draw4:R2 col2 552466** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 255664** [hit-family,hit-family-gap] | Draw4:R4 col2 255664** [hit-family,hit-family-gap] | Draw4:R8 col1 662455** [hit-family-gap] | Draw4:R8 col2 662455** [hit-family-gap]`

### 2026-01-07 — NorthCarolina4 — Evening — 202 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac10_winner_202_20260110_033430.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw4:R4 col2 229066441** [hit-family-gap,hit-winner-gap] | Draw4:R6 col2 661092244** [hit-family-gap,hit-winner-gap] | Draw5:R2 col2 59224400166** [hit-family-gap,hit-vt-straight-gap,ls-box,ls-box-edge] | Draw5:R4 col2 22590066441** [hit-family,hit-family-gap] | Draw5:R6 col2 66100592244** [hit-family-gap] | Draw6:R2 col2 5922440013366 [hit-family-gap,hit-vt-straight-gap,ls-box,ls-box-edge]`

### 2026-01-07 — Ohio4 — Midday — 737 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-07/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-07/Ohio4/winners/Ohio4/Ohio4_vtrac27_winner_737_20260110_033431.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R8 col2 0199822** [hit-family,hit-family-gap] | Draw3:R8 col2 01998822** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 8810099322** [hit-family,hit-family-gap] | Draw4:R8 col2 0019988322** [hit-family,hit-family-gap] | Draw5:R6 col2 8810099322** [hit-family,hit-family-gap] | Draw5:R8 col2 0019988322** [hit-family,hit-family-gap]`

### 2026-01-07 — Pennsylvania4 — Midday — 060 (double)

- Winner canonical: `006`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_060_20260110_033438.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`30` hit-winner-cells=`3` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`3` family_recentest_draw=`3` winner_recentest_draw=`4`
- Winners lens samples: `Draw3:R2 col1 9001** [hit-family,hit-family-gap] | Draw3:R2 col2 9001** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 9001** [hit-family,hit-family-gap] | Draw3:R4 col2 9001** [hit-family,hit-family-gap] | Draw3:R6 col1 1009** [hit-family,hit-family-gap] | Draw3:R6 col2 1009** [hit-family,hit-family-gap]`

### 2026-01-07 — PuertoRico4 — Evening — 969 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`9` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_969_20260110_033443.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`4` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw5:R4 col2 2500668844** [hit-vt-straight-gap] | Draw5:R8 col2 0088662445** [hit-family-gap] | Draw6:R4 col2 250066883441 [hit-family,hit-family-gap] | Draw6:R8 col2 001883662445 [hit-family-gap]`

### 2026-01-07 — SouthCarolina4 — Evening — 336 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac23_winner_336_20260110_033446.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`18` hit-winner-cells=`0` hit-vt-straight-cells=`9` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 59938667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 59938667** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 59966837** [hit-family,hit-family-gap] | Draw5:R4 col2 59966837** [hit-family,hit-family-gap] | Draw5:R8 col1 79983665** [hit-family,hit-family-gap] | Draw5:R8 col2 79983665** [hit-family,hit-family-gap]`

### 2026-01-07 — SouthCarolina4 — Midday — 288 (double)

- Winner canonical: `288`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`2` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac29_winner_288_20260110_033445.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 592244003367 [hit-family-gap,ls-box,ls-box-edge] | Draw7:R6 col1 670059332244 [hit-family,hit-family-gap,hit-vt-straight] | Draw7:R8 col1 700933622445 [hit-family-gap]`

### 2026-01-07 — Virginia4 — Evening — 990 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-07/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-07/Virginia4/winners/Virginia4/Virginia4_vtrac15_winner_990_20260110_033448.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col2 9240018** [hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col2 2900841** [hit-family-gap] | Draw3:R6 col2 8100924** [hit-family-gap] | Draw4:R2 col2 92400138** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col1 24400133** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R2 col2 9244001338** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-07 — Virginia4 — Midday — 275 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-07__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-07/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-07/Virginia4/winners/Virginia4/Virginia4_vtrac10_winner_275_20260110_033447.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — Connecticut4 — Evening — 331 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac23_winner_331_20260110_034415.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 559922401388 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R4 col1 225599088341 [hit-family-gap] | Draw7:R6 col1 881055993224 [hit-family,hit-family-gap]`

### 2026-01-08 — Connecticut4 — Midday — 106 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_106_20260110_034414.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — Florida4 — Midday — 429 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-08/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-08/Florida4/winners/Florida4/Florida4_vtrac31_winner_429_20260110_034419.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`17` hit-winner-cells=`5` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`3` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col1 59244336** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R2 col2 5592443366** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R6 col1 65933244** [hit-family,hit-family-gap] | Draw5:R6 col2 6655933244** [hit-family,hit-family-gap] | Draw5:R8 col1 93362445** [hit-family,hit-family-gap] | Draw5:R8 col2 9336624455** [hit-family,hit-family-gap]`

### 2026-01-08 — Indiana4 — Evening — 242 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-08/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-08/Indiana4/winners/Indiana4/Indiana4_vtrac28_winner_242_20260110_034424.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw2:R6 col2 8870244** [hit-family-gap] | Draw7:R4 col1 550883344771 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-08 — NewJersey4 — Evening — 055 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-08/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-08/NewJersey4/winners/NewJersey4/NewJersey4_vtrac1_winner_055_20260110_034430.json` (index `1`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`20` hit-winner-cells=`20` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`4` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 550087** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R2 col2 55008877** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw4:R4 col1 550087** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R4 col2 55008877** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col1 870055** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col2 88770055** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-08 — NewYork4 — Evening — 732 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`7` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-08/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-08/NewYork4/winners/NewYork4/NewYork4_vtrac27_winner_732_20260110_034431.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — NewYork4 — Midday — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-08/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-08/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_199_20260110_034431.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col2 55924667** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col2 25596647** [hit-family-gap] | Draw5:R8 col2 79662455** [hit-family-gap] | Draw6:R2 col1 552244367* [hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 55922443667 [hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 225563447* [hit-family-gap]`

### 2026-01-08 — Ohio4 — Evening — 580 (mirror_double)

- Winner canonical: `058`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-08/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-08/Ohio4/winners/Ohio4/Ohio4_vtrac4_winner_580_20260110_034437.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`5` hit-vt-straight-cells=`10` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`2` family_recentest_draw=`1` winner_recentest_draw=`1`
- Winners lens samples: `Draw1:R2 col1 5588** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R2 col2 55088** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R4 col1 5588** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col2 55088** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R6 col1 8855** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col2 88055** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-08 — Ohio4 — Midday — 681 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-08/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-08/Ohio4/winners/Ohio4/Ohio4_vtrac18_winner_681_20260110_034436.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — OntarioCanada4 — Evening — 498 (mirror_double)

- Winner canonical: `489`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_498_20260110_034440.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — OntarioCanada4 — Midday — 022 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac10_winner_022_20260110_034438.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`14` hit-winner-cells=`4` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`2` family_recentest_draw=`2` winner_recentest_draw=`4`
- Winners lens samples: `Draw2:R6 col1 670324** [hit-family-gap] | Draw2:R6 col2 67703244** [hit-family,hit-family-gap] | Draw2:R8 col2 77036244** [hit-family,hit-family-gap] | Draw3:R6 col1 670324** [hit-family-gap] | Draw3:R6 col2 67703244** [hit-family,hit-family-gap] | Draw3:R8 col2 77036244** [hit-family,hit-family-gap]`

### 2026-01-08 — Pennsylvania4 — Midday — 750 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac3_winner_750_20260110_034441.json` (index `3`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`7` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col2 9220013** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw4:R4 col2 2290031** [hit-family-gap] | Draw5:R2 col2 9220011387** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R4 col2 2290083711** [hit-family-gap] | Draw5:R6 col2 8117009322** [hit-family,hit-family-gap] | Draw5:R8 col2 7001198322** [hit-family,hit-family-gap]`

### 2026-01-08 — PuertoRico4 — Evening — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_479_20260110_034446.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`0` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-08 — SouthCarolina4 — Midday — 277 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac26_winner_277_20260110_034447.json` (index `26`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R6 col2 72244** [hit-family,hit-family-gap] | Draw3:R8 col2 72244** [hit-family,hit-family-gap]`

### 2026-01-09 — Delaware4 — Evening — 681 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-09/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-09/Delaware4/winners/Delaware4/Delaware4_vtrac18_winner_681_20260110_035036.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`22` hit-winner-cells=`3` hit-vt-straight-cells=`4` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`2` family_recentest_draw=`1` winner_recentest_draw=`6`
- Winners lens samples: `Draw1:R2 col2 5440118** [hit-family,hit-family-gap] | Draw1:R6 col2 8110544** [hit-family,hit-family-gap] | Draw1:R8 col2 0118445** [hit-family,hit-family-gap] | Draw2:R2 col2 54401138** [hit-family,hit-family-gap] | Draw2:R6 col2 81105344** [hit-family,hit-family-gap] | Draw2:R8 col2 01183445** [hit-family,hit-family-gap]`

### 2026-01-09 — Delaware4 — Midday — 843 (mirror_double)

- Winner canonical: `348`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-09/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-09/Delaware4/winners/Delaware4/Delaware4_vtrac33_winner_843_20260110_035035.json` (index `33`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`28` hit-winner-cells=`0` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 9433** [hit-family,hit-family-gap] | Draw3:R2 col2 940338** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw3:R4 col1 9334** [hit-family,hit-family-gap] | Draw3:R4 col2 908334** [hit-family,hit-family-gap,hit-winner-gap] | Draw3:R6 col1 9334** [hit-family,hit-family-gap] | Draw3:R6 col2 809334** [hit-family,hit-family-gap]`

### 2026-01-09 — Indiana4 — Evening — 377 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-09/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-09/Indiana4/winners/Indiana4/Indiana4_vtrac27_winner_377_20260110_035042.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 55401338877* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R2 col2 554401338877 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R4 col1 55088334771* [hit-family-gap,hit-winner-gap] | Draw6:R4 col2 550883344771 [hit-vt-straight-gap] | Draw6:R6 col1 88177055334* [hit-family-gap] | Draw6:R6 col2 881770553344 [hit-family-gap]`

### 2026-01-09 — Michigan4 — Evening — 273 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-09/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-09/Michigan4/winners/Michigan4/Michigan4_vtrac27_winner_273_20260110_035045.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R6 col1 810099332244 [hit-family,hit-family-gap,hit-vt-straight] | Draw7:R8 col1 001998332244 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-09 — NewJersey4 — Midday — 287 (mirror_double)

- Winner canonical: `278`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4/NewJersey4_vtrac27_winner_287_20260110_035046.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw5:R4 col1 293471** [hit-family-gap] | Draw5:R6 col1 179324** [hit-family-gap] | Draw6:R2 col1 592241377* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 599224013877 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 225934771* [hit-family-gap] | Draw6:R4 col2 225990834771 [hit-family-gap]`

### 2026-01-09 — NewYork4 — Evening — 835 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`8` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-09/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-09/NewYork4/winners/NewYork4/NewYork4_vtrac13_winner_835_20260110_035050.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-09 — NewYork4 — Midday — 989 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-09/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-09/NewYork4/winners/NewYork4/NewYork4_vtrac34_winner_989_20260110_035049.json` (index `34`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`9` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 552244367** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 552244367** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 225563447** [hit-family,hit-family-gap] | Draw5:R4 col2 225563447** [hit-family,hit-family-gap] | Draw6:R2 col1 55224433677* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R2 col2 559224433677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-09 — NorthCarolina4 — Midday — 177 (double)

- Winner canonical: `177`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac20_winner_177_20260110_035051.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`2` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`1` family_recentest_draw=`6` winner_recentest_draw=`6`
- Winners lens samples: `Draw6:R2 col1 9940086677* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R2 col2 9924001386677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R4 col2 2990066834771 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw6:R6 col1 6687700994* [hit-family-gap] | Draw6:R6 col2 6681770099324 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R2 col1 99400386677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-09 — Ohio4 — Evening — 090 (double)

- Winner canonical: `009`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-09/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-09/Ohio4/winners/Ohio4/Ohio4_vtrac5_winner_090_20260110_035056.json` (index `5`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`0` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col2 559887** [hit-family,hit-family-gap] | Draw2:R4 col2 559887** [hit-family,hit-family-gap] | Draw2:R6 col2 887559** [hit-family,hit-family-gap] | Draw3:R2 col2 5598867** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col2 5596887** [hit-family,hit-family-gap] | Draw3:R6 col2 6887559** [hit-family,hit-family-gap]`

### 2026-01-09 — OntarioCanada4 — Midday — 772 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac26_winner_772_20260110_035057.json` (index `26`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-09 — Pennsylvania4 — Midday — 811 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_811_20260110_035059.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`15` hit-winner-cells=`7` hit-vt-straight-cells=`3` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`4` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 9221138** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R2 col2 92211387** [hit-family,hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw4:R4 col1 2298311** [hit-family,hit-family-gap,hit-winner-gap] | Draw4:R4 col2 22983711** [hit-family-gap] | Draw4:R6 col1 8119322** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R6 col2 81179322** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-09 — PuertoRico4 — Evening — 225 (double)

- Winner canonical: `225`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac10_winner_225_20260110_035103.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-09 — PuertoRico4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac17_winner_126_20260110_035102.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R4 col2 590068834711 [hit-family,hit-family-gap] | Draw6:R6 col2 688117005934 [hit-family,hit-family-gap]`

### 2026-01-09 — Virginia4 — Evening — 262 (double)

- Winner canonical: `226`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-09/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-09/Virginia4/winners/Virginia4/Virginia4_vtrac20_winner_262_20260110_035109.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`1` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`1` family_recentest_draw=`6` winner_recentest_draw=`6`
- Winners lens samples: `Draw6:R2 col1 24401336677* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R2 col2 2244011336677 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R4 col1 20663344771* [hit-family,hit-family-gap] | Draw6:R4 col2 2206633447711 [hit-family,hit-family-gap,hit-vt-straight,hit-winner-gap] | Draw6:R6 col1 66177033244* [hit-family,hit-family-gap] | Draw6:R6 col2 6611770332244 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-09 — Virginia4 — Midday — 380 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-09__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-09/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-09/Virginia4/winners/Virginia4/Virginia4_vtrac13_winner_380_20260110_035108.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 599063344711 [hit-family-gap]`
