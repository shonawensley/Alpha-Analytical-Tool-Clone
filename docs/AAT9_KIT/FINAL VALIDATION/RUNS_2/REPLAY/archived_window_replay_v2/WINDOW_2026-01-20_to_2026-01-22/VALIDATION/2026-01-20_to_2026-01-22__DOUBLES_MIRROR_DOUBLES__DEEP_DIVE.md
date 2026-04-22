# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-04-22T06:29:57.846272+00:00`
- Rows: `40`

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
| double | 23 | 16 | 9 | 12 | 23 | 12.70 | 3.13 | 2.22 | 1.17 |
| mirror_double | 17 | 10 | 1 | 5 | 17 | 4.59 | 0.12 | 1.76 | 0.29 |

## Per-event evidence pointers

### 2026-01-20 — Connecticut4 — Evening — 961 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-20/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-20/Connecticut4/winners/Connecticut4/Connecticut4_vtrac19_winner_961_20260127_020426.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-20 — Delaware4 — Evening — 106 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-20/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-20/Delaware4/winners/Delaware4/Delaware4_vtrac6_winner_106_20260127_020428.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw2:R4 col2 259671** [hit-family-gap] | Draw2:R6 col2 617592** [hit-family-gap] | Draw2:R8 col2 719625** [hit-family-gap] | Draw3:R4 col2 2259671** [hit-family-gap] | Draw3:R6 col2 6175922** [hit-family-gap] | Draw4:R4 col2 225966471** [hit-family-gap]`

### 2026-01-20 — Delaware4 — Midday — 099 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-20/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-20/Delaware4/winners/Delaware4/Delaware4_vtrac15_winner_099_20260127_020427.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 55924013386 [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-20 — Michigan4 — Evening — 881 (double)

- Winner canonical: `188`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-20/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-20/Michigan4/winners/Michigan4/Michigan4_vtrac23_winner_881_20260127_020436.json` (index `23`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`12` hit-winner-cells=`0` hit-vt-straight-cells=`4` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`6` winner_recentest_draw=``
- Winners lens samples: `Draw6:R2 col1 92488677* [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 92244088677 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw6:R4 col1 29688477* [hit-family,hit-family-gap] | Draw6:R4 col2 22906884477 [hit-family,hit-family-gap] | Draw6:R6 col1 68877924* [hit-family,hit-family-gap] | Draw6:R6 col2 68877092244 [hit-family,hit-family-gap]`

### 2026-01-20 — Michigan4 — Midday — 616 (double)

- Winner canonical: `166`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-20/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-20/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260127_020436.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`3` hit-winner-cells=`3` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R2 col1 52244016677 [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R6 col1 66177052244 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R8 col1 77016622445 [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-20 — NewJersey4 — Midday — 866 (double)

- Winner canonical: `668`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__NewJersey4.md`
- Winners lens dir: `sharepacks/2026-01-20/NewJersey4/winners/NewJersey4`
- Winners lens JSON: `sharepacks/2026-01-20/NewJersey4/winners/NewJersey4/NewJersey4_vtrac18_winner_866_20260127_020437.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-20 — NewYork4 — Midday — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`6` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-20/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-20/NewYork4/winners/NewYork4/NewYork4_vtrac31_winner_479_20260127_020439.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-20 — Ohio4 — Evening — 843 (mirror_double)

- Winner canonical: `348`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-20/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-20/Ohio4/winners/Ohio4/Ohio4_vtrac33_winner_843_20260127_020446.json` (index `33`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`2` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`1` family_recentest_draw=`5` winner_recentest_draw=`5`
- Winners lens samples: `Draw5:R2 col1 524038877** [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R4 col1 250883477** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R4 col2 2500883477** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw5:R8 col1 770883245** [hit-family-gap,hit-winner-gap] | Draw5:R8 col2 7700883245** [hit-family-gap,hit-winner-gap] | Draw6:R2 col1 55240338877* [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge]`

### 2026-01-20 — Ohio4 — Midday — 556 (double)

- Winner canonical: `556`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-20/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-20/Ohio4/winners/Ohio4/Ohio4_vtrac2_winner_556_20260127_020445.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`5` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 994400867** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 9924400867** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 990068447** [hit-family,hit-family-gap] | Draw5:R4 col2 2990068447** [hit-family,hit-family-gap] | Draw6:R2 col1 9924400867* [hit-family-gap,ls-box,ls-box-edge] | Draw6:R2 col2 99224400867 [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-20 — OntarioCanada4 — Evening — 038 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-20/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-20/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac13_winner_038_20260127_020448.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw4:R4 col2 25683447** [hit-family-gap] | Draw4:R6 col2 68753244** [hit-family-gap] | Draw5:R4 col1 5568344** [hit-family-gap] | Draw5:R4 col2 2556883447** [hit-family-gap] | Draw5:R6 col1 6855344** [hit-family-gap] | Draw5:R6 col2 6887553244** [hit-family-gap]`

### 2026-01-20 — OntarioCanada4 — Midday — 561 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-20/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-20/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac6_winner_561_20260127_020447.json` (index `6`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`38` hit-winner-cells=`0` hit-vt-straight-cells=`28` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 440016** [hit-family,hit-family-gap] | Draw2:R2 col2 440016** [hit-family,hit-family-gap] | Draw2:R6 col1 610044** [hit-family,hit-family-gap] | Draw2:R6 col2 610044** [hit-family,hit-family-gap] | Draw2:R8 col1 001644** [hit-family,hit-family-gap] | Draw2:R8 col2 001644** [hit-family,hit-family-gap]`

### 2026-01-20 — Pennsylvania4 — Evening — 242 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-20/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-20/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac28_winner_242_20260127_020450.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`3` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R2 col1 55922418877 [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R4 col1 22559884771 [hit-family,hit-family-gap] | Draw7:R6 col1 88177559224 [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw7:R8 col1 77198822455 [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-20 — PuertoRico4 — Midday — 742 (mirror_double)

- Winner canonical: `247`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-20/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-20/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_742_20260127_020451.json` (index `28`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-20 — SouthCarolina4 — Evening — 328 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-20/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-20__SouthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-20/SouthCarolina4/winners/SouthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-20/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac29_winner_328_20260127_020456.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R2 col1 9003367** [hit-family-gap] | Draw4:R2 col2 994003367** [hit-family-gap,ls-box,ls-box-edge] | Draw4:R4 col1 9006337** [hit-family,hit-family-gap] | Draw4:R4 col2 990063347** [hit-family-gap] | Draw5:R2 col1 92003367** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 9924003367** [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-21 — Connecticut4 — Evening — 141 (double)

- Winner canonical: `114`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-21/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac19_winner_141_20260127_020823.json` (index `19`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-21 — Florida4 — Midday — 350 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-21/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-21/Florida4/winners/Florida4/Florida4_vtrac4_winner_350_20260127_020827.json` (index `4`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`10` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`3` winner_recentest_draw=``
- Winners lens samples: `Draw3:R2 col1 5208** [hit-family-gap] | Draw3:R2 col2 52087** [hit-family-gap,ls-box,ls-box-edge] | Draw3:R4 col1 2508** [hit-family,hit-family-gap] | Draw3:R4 col2 25087** [hit-family,hit-family-gap] | Draw3:R6 col1 8052** [hit-family,hit-family-gap] | Draw3:R6 col2 87052** [hit-family-gap]`

### 2026-01-21 — Indiana4 — Evening — 612 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`11` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`11` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-21/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-21/Indiana4/winners/Indiana4/Indiana4_vtrac17_winner_612_20260127_020831.json` (index `17`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw6:R6 col1 681793244* [hit-family-gap] | Draw7:R2 col1 59244138667 [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw7:R6 col1 66817593244 [hit-family-gap] | Draw7:R8 col1 71983662445 [hit-family,hit-family-gap]`

### 2026-01-21 — Michigan4 — Evening — 221 (double)

- Winner canonical: `122`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-21/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-21/Michigan4/winners/Michigan4/Michigan4_vtrac20_winner_221_20260127_020833.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`5` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 924677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 92488677** [hit-family,hit-family-gap,ls-box,ls-box-edge] | Draw5:R4 col1 296477** [hit-family-gap] | Draw5:R6 col1 677924** [hit-family,hit-family-gap] | Draw5:R8 col1 779624** [hit-family-gap] | Draw6:R2 col1 924336677* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-21 — Michigan4 — Midday — 220 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Michigan4.md`
- Winners lens dir: `sharepacks/2026-01-21/Michigan4/winners/Michigan4`
- Winners lens JSON: `sharepacks/2026-01-21/Michigan4/winners/Michigan4/Michigan4_vtrac10_winner_220_20260127_020832.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`46` hit-winner-cells=`3` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`3` family_recentest_draw=`1` winner_recentest_draw=`4`
- Winners lens samples: `Draw1:R2 col1 52247** [hit-family,hit-family-gap] | Draw1:R2 col2 522417** [hit-family,hit-family-gap] | Draw1:R4 col1 22547** [hit-family,hit-family-gap] | Draw1:R4 col2 225471** [hit-family,hit-family-gap] | Draw1:R6 col1 75224** [hit-family,hit-family-gap] | Draw1:R6 col2 175224** [hit-family,hit-family-gap]`

### 2026-01-21 — NewYork4 — Evening — 233 (double)

- Winner canonical: `233`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-21/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-21/NewYork4/winners/NewYork4/NewYork4_vtrac29_winner_233_20260127_020838.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`34` hit-winner-cells=`10` hit-vt-straight-cells=`24` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`4` family_recentest_draw=`1` winner_recentest_draw=`4`
- Winners lens samples: `Draw1:R2 col1 13377** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R2 col2 13377** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col1 33771** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col2 33771** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col1 17733** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col2 17733** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-21 — NewYork4 — Midday — 616 (double)

- Winner canonical: `166`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`7` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-21/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-21/NewYork4/winners/NewYork4/NewYork4_vtrac16_winner_616_20260127_020837.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-21 — NorthCarolina4 — Evening — 577 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-21/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-21/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac10_winner_577_20260127_020839.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-21 — NorthCarolina4 — Midday — 767 (double)

- Winner canonical: `677`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NorthCarolina4.md`
- Winners lens dir: `sharepacks/2026-01-21/NorthCarolina4/winners/NorthCarolina4`
- Winners lens JSON: `sharepacks/2026-01-21/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac20_winner_767_20260127_020839.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`17` hit-winner-cells=`7` hit-vt-straight-cells=`6` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`4` family_recentest_draw=`4` winner_recentest_draw=`4`
- Winners lens samples: `Draw4:R2 col1 2388677** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw4:R2 col2 22388677** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw4:R4 col2 22688377** [hit-family,hit-family-gap] | Draw4:R8 col2 77883622** [hit-family,hit-family-gap] | Draw5:R2 col1 20388677** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge] | Draw5:R2 col2 220388677** [hit-family,hit-family-gap,hit-winner,hit-winner-gap,ls-box,ls-box-edge]`

### 2026-01-21 — Ohio4 — Midday — 649 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-21/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-21/Ohio4/winners/Ohio4/Ohio4_vtrac25_winner_649_20260127_020840.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`4` winner_recentest_draw=``
- Winners lens samples: `Draw4:R4 col2 990068447** [hit-family-gap] | Draw4:R8 col2 700998644** [hit-family,hit-family-gap,hit-winner-gap] | Draw5:R4 col2 2990068447** [hit-family-gap] | Draw5:R8 col2 7009986244** [hit-family-gap,hit-winner-gap] | Draw6:R8 col2 700998862445 [hit-family-gap] | Draw7:R4 col1 299006884471 [hit-family-gap]`

### 2026-01-21 — OntarioCanada4 — Evening — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-21/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac25_winner_199_20260127_020845.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`18` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`5` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col1 5446** [hit-family,hit-family-gap] | Draw2:R2 col2 54436** [hit-family-gap] | Draw2:R4 col1 5644** [hit-family,hit-family-gap] | Draw2:R4 col2 56344** [hit-family-gap] | Draw2:R6 col1 6544** [hit-family-gap] | Draw2:R8 col1 6445** [hit-family,hit-family-gap]`

### 2026-01-21 — Pennsylvania4 — Evening — 816 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-21/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_816_20260127_020846.json` (index `18`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R2 col1 55991388677 [hit-family-gap,hit-winner-gap,ls-box,ls-box-edge] | Draw7:R6 col1 68817755993 [hit-family-gap,hit-winner-gap]`

### 2026-01-21 — Pennsylvania4 — Midday — 848 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`8` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Pennsylvania4.md`
- Winners lens dir: `sharepacks/2026-01-21/Pennsylvania4/winners/Pennsylvania4`
- Winners lens JSON: `sharepacks/2026-01-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac33_winner_848_20260127_020845.json` (index `33`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`29` hit-winner-cells=`0` hit-vt-straight-cells=`10` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`6` winner_draws=`0` family_recentest_draw=`2` winner_recentest_draw=``
- Winners lens samples: `Draw2:R2 col2 94038** [hit-family-gap] | Draw2:R4 col2 90834** [hit-family,hit-family-gap] | Draw2:R6 col2 80934** [hit-family-gap] | Draw2:R8 col2 09834** [hit-family,hit-family-gap] | Draw3:R2 col1 94033** [hit-family-gap] | Draw3:R2 col2 940338** [hit-family-gap,ls-box,ls-box-edge]`

### 2026-01-21 — PuertoRico4 — Evening — 257 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-21/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-21/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac10_winner_257_20260127_020848.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-21 — PuertoRico4 — Midday — 328 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-21/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-21/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac29_winner_328_20260127_020847.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-21 — Virginia4 — Evening — 469 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-21/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-21/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-21/Virginia4/winners/Virginia4/Virginia4_vtrac25_winner_469_20260127_020854.json` (index `25`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`8` hit-winner-cells=`0` hit-vt-straight-cells=`8` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R2 col1 554411388** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R2 col2 5544113388** [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw5:R4 col1 558834411** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R4 col2 5588334411** [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R2 col1 554411388* [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge] | Draw6:R2 col2 55441133887 [hit-family,hit-family-gap,hit-vt-straight,ls-box,ls-box-edge]`

### 2026-01-22 — Connecticut4 — Midday — 556 (double)

- Winner canonical: `556`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`1` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Connecticut4.md`
- Winners lens dir: `sharepacks/2026-01-22/Connecticut4/winners/Connecticut4`
- Winners lens JSON: `sharepacks/2026-01-22/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_556_20260128_032316.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`48` hit-winner-cells=`0` hit-vt-straight-cells=`20` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`0` family_recentest_draw=`1` winner_recentest_draw=``
- Winners lens samples: `Draw1:R2 col2 006** [hit-family,hit-family-gap] | Draw1:R4 col2 006** [hit-family,hit-family-gap] | Draw1:R6 col2 060** [hit-family,hit-family-gap] | Draw1:R8 col2 006** [hit-family,hit-family-gap] | Draw2:R2 col1 0016** [hit-family,hit-family-gap] | Draw2:R2 col2 00166** [hit-family,hit-family-gap]`

### 2026-01-22 — Delaware4 — Midday — 288 (double)

- Winner canonical: `288`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`1` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Delaware4.md`
- Winners lens dir: `sharepacks/2026-01-22/Delaware4/winners/Delaware4`
- Winners lens JSON: `sharepacks/2026-01-22/Delaware4/winners/Delaware4/Delaware4_vtrac29_winner_288_20260128_032319.json` (index `29`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`4` hit-winner-cells=`0` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`3` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw5:R6 col2 681553324** [hit-family,hit-family-gap] | Draw5:R8 col2 183362455** [hit-family-gap] | Draw6:R6 col1 66811553324* [hit-family,hit-family-gap] | Draw6:R6 col2 668115533224 [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R8 col2 118336622455 [hit-vt-straight-gap] | Draw7:R6 col1 668115533244 [hit-family,hit-family-gap]`

### 2026-01-22 — Florida4 — Evening — 116 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`1` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Florida4.md`
- Winners lens dir: `sharepacks/2026-01-22/Florida4/winners/Florida4`
- Winners lens JSON: `sharepacks/2026-01-22/Florida4/winners/Florida4/Florida4_vtrac16_winner_116_20260128_032323.json` (index `16`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`0` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``
- Winners lens samples: `Draw7:R6 col1 68117705932 [hit-family-gap,hit-winner-gap]`

### 2026-01-22 — Indiana4 — Evening — 757 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`12` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Indiana4.md`
- Winners lens dir: `sharepacks/2026-01-22/Indiana4/winners/Indiana4`
- Winners lens JSON: `sharepacks/2026-01-22/Indiana4/winners/Indiana4/Indiana4_vtrac10_winner_757_20260128_032325.json` (index `10`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`1` hit-winner-cells=`1` hit-vt-straight-cells=`1` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`1`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`1` family_recentest_draw=`7` winner_recentest_draw=`7`
- Winners lens samples: `Draw7:R6 col1 68775593344 [hit-family,hit-family-gap,hit-vt-straight,hit-winner,hit-winner-gap]`

### 2026-01-22 — NewYork4 — Evening — 787 (double)

- Winner canonical: `778`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`0` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__NewYork4.md`
- Winners lens dir: `sharepacks/2026-01-22/NewYork4/winners/NewYork4`
- Winners lens JSON: `sharepacks/2026-01-22/NewYork4/winners/NewYork4/NewYork4_vtrac27_winner_787_20260128_032335.json` (index `27`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`16` hit-winner-cells=`6` hit-vt-straight-cells=`12` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`4` family_recentest_draw=`1` winner_recentest_draw=`4`
- Winners lens samples: `Draw1:R2 col2 513377** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R4 col2 533771** [hit-family,hit-family-gap,hit-vt-straight] | Draw1:R6 col2 177533** [hit-family-gap] | Draw1:R8 col2 771335** [hit-family-gap] | Draw2:R2 col2 5113377** [hit-family,hit-family-gap,hit-vt-straight] | Draw2:R4 col2 5337711** [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-22 — Ohio4 — Midday — 217 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`1` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Ohio4.md`
- Winners lens dir: `sharepacks/2026-01-22/Ohio4/winners/Ohio4`
- Winners lens JSON: `sharepacks/2026-01-22/Ohio4/winners/Ohio4/Ohio4_vtrac20_winner_217_20260128_032339.json` (index `20`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`1` winner_draws=`0` family_recentest_draw=`7` winner_recentest_draw=``
- Winners lens samples: `Draw7:R4 col1 290088347711 [hit-family,hit-family-gap,hit-vt-straight] | Draw7:R6 col1 881177009324 [hit-family,hit-family-gap,hit-vt-straight] | Draw7:R8 col1 770011988324 [hit-vt-straight-gap]`

### 2026-01-22 — OntarioCanada4 — Evening — 544 (double)

- Winner canonical: `445`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`0` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__OntarioCanada4.md`
- Winners lens dir: `sharepacks/2026-01-22/OntarioCanada4/winners/OntarioCanada4`
- Winners lens JSON: `sharepacks/2026-01-22/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac15_winner_544_20260128_032343.json` (index `15`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`34` hit-winner-cells=`30` hit-vt-straight-cells=`18` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`3`
- Set1 col1/2 draw recency: family_draws=`7` winner_draws=`7` family_recentest_draw=`1` winner_recentest_draw=`1`
- Winners lens samples: `Draw1:R2 col1 5446** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R2 col2 5446** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R4 col1 5644** [hit-family-gap,hit-winner-gap] | Draw1:R4 col2 5644** [hit-family-gap,hit-winner-gap] | Draw1:R6 col1 6544** [hit-family,hit-family-gap,hit-winner,hit-winner-gap] | Draw1:R6 col2 6544** [hit-family,hit-family-gap,hit-winner,hit-winner-gap]`

### 2026-01-22 — PuertoRico4 — Evening — 992 (double)

- Winner canonical: `299`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`3` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-22/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-22/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_992_20260128_032348.json` (index `31`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`0` hit-winner-cells=`0` hit-vt-straight-cells=`0` ls-box-cells=`7` xvar-family-variants=`1` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`0` winner_draws=`0` family_recentest_draw=`` winner_recentest_draw=``

### 2026-01-22 — PuertoRico4 — Midday — 583 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`3` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__PuertoRico4.md`
- Winners lens dir: `sharepacks/2026-01-22/PuertoRico4/winners/PuertoRico4`
- Winners lens JSON: `sharepacks/2026-01-22/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac13_winner_583_20260128_032347.json` (index `13`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`2` hit-winner-cells=`0` hit-vt-straight-cells=`2` ls-box-cells=`7` xvar-family-variants=`2` xvar-winner-variants=`0`
- Set1 col1/2 draw recency: family_draws=`2` winner_draws=`0` family_recentest_draw=`5` winner_recentest_draw=``
- Winners lens samples: `Draw3:R4 col2 0688411** [hit-family-gap] | Draw5:R6 col2 668811055334** [hit-family,hit-family-gap,hit-vt-straight] | Draw6:R6 col2 668811055334 [hit-family,hit-family-gap,hit-vt-straight]`

### 2026-01-22 — Virginia4 — Evening — 100 (double)

- Winner canonical: `001`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`4` delta(cc-aux)=`` draws=`sharepacks/2026-01-22/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-22__Virginia4.md`
- Winners lens dir: `sharepacks/2026-01-22/Virginia4/winners/Virginia4`
- Winners lens JSON: `sharepacks/2026-01-22/Virginia4/winners/Virginia4/Virginia4_vtrac2_winner_100_20260128_032354.json` (index `2`)
- Winners lens Set1 col1/2 (focus variant = period): hit-family-cells=`13` hit-winner-cells=`9` hit-vt-straight-cells=`13` ls-box-cells=`7` xvar-family-variants=`3` xvar-winner-variants=`2`
- Set1 col1/2 draw recency: family_draws=`4` winner_draws=`2` family_recentest_draw=`4` winner_recentest_draw=`6`
- Winners lens samples: `Draw4:R2 col1 55411388** [hit-family-gap] | Draw4:R2 col2 554411388** [hit-vt-straight-gap,ls-box,ls-box-edge] | Draw4:R6 col1 88115534** [hit-family,hit-family-gap,hit-vt-straight] | Draw4:R6 col2 881155344** [hit-family,hit-family-gap,hit-vt-straight] | Draw5:R2 col1 55411388** [hit-family-gap,ls-box,ls-box-edge] | Draw5:R2 col2 554411388** [hit-vt-straight-gap,ls-box,ls-box-edge]`
