# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-01-11T21:18:04.737902+00:00`
- Rows: `190`

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
| 2026-01-05 | Florida4 | Evening | 994 | double | True | union |  | False | False |
| 2026-01-05 | Florida4 | Midday | 080 | double | True | due_doubles_mirror_single | 6 | True | True |
| 2026-01-05 | Michigan4 | Evening | 772 | double | True | union |  | False | False |
| 2026-01-05 | NewYork4 | Midday | 080 | double | True | consensus_double_9 | 9 | True | True |
| 2026-01-05 | PuertoRico4 | Midday | 732 | mirror_double | True | union |  | False | True |
| 2026-01-06 | NewYork4 | Midday | 181 | double | True | union |  | False | False |
| 2026-01-07 | Pennsylvania4 | Midday | 060 | double | True | union |  | False | True |
| 2026-01-08 | Indiana4 | Evening | 242 | double | True | union |  | False | False |
| 2026-01-08 | NewJersey4 | Evening | 055 | double | True | union |  | True | True |
| 2026-01-08 | Ohio4 | Evening | 580 | mirror_double | True | union |  | False | False |
| 2026-01-08 | OntarioCanada4 | Evening | 498 | mirror_double | True | union |  | False | False |
| 2026-01-08 | OntarioCanada4 | Midday | 022 | double | True | consensus_double_9 | 9 | True | True |
| 2026-01-08 | Pennsylvania4 | Midday | 750 | mirror_double | True | union |  | False | True |
| 2026-01-08 | SouthCarolina4 | Midday | 277 | double | True | union |  | False | False |
| 2026-01-09 | Ohio4 | Evening | 090 | double | True | due_doubles_mirror_double | 6 | True | True |
| 2026-01-09 | PuertoRico4 | Evening | 225 | double | True | due_doubles_mirror_single | 6 | True | True |

## Per-event evidence pointers

### 2025-06-21 — Connecticut4 — Evening — 155 (double)

- Winner canonical: `155`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Connecticut4.md`
- Winners lens: `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4`

### 2025-06-21 — Connecticut4 — Midday — 950 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Connecticut4.md`
- Winners lens: `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4`

### 2025-06-21 — Delaware4 — Evening — 989 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Delaware4.md`
- Winners lens: `sharepacks/2025-06-21/Delaware4/winners/Delaware4`

### 2025-06-21 — Florida4 — Midday — 927 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Florida4.md`
- Winners lens: `sharepacks/2025-06-21/Florida4/winners/Florida4`

### 2025-06-21 — Indiana4 — Midday — 565 (double)

- Winner canonical: `556`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Indiana4.md`
- Winners lens: `sharepacks/2025-06-21/Indiana4/winners/Indiana4`

### 2025-06-21 — NewJersey4 — Evening — 554 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewJersey4.md`
- Winners lens: `sharepacks/2025-06-21/NewJersey4/winners/NewJersey4`

### 2025-06-21 — NorthCarolina4 — Midday — 427 (mirror_double)

- Winner canonical: `247`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NorthCarolina4.md`
- Winners lens: `sharepacks/2025-06-21/NorthCarolina4/winners/NorthCarolina4`

### 2025-06-21 — Ohio4 — Evening — 868 (double)

- Winner canonical: `688`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Ohio4.md`
- Winners lens: `sharepacks/2025-06-21/Ohio4/winners/Ohio4`

### 2025-06-21 — Pennsylvania4 — Midday — 667 (double)

- Winner canonical: `667`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4`

### 2025-06-21 — PuertoRico4 — Evening — 551 (double)

- Winner canonical: `155`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md`
- Winners lens: `sharepacks/2025-06-21/PuertoRico4/winners/PuertoRico4`

### 2025-06-21 — Virginia4 — Evening — 016 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-21/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Virginia4.md`
- Winners lens: `sharepacks/2025-06-21/Virginia4/winners/Virginia4`

### 2025-06-22 — Connecticut4 — Evening — 835 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Connecticut4.md`
- Winners lens: `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4`

### 2025-06-22 — Delaware4 — Evening — 127 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Delaware4.md`
- Winners lens: `sharepacks/2025-06-22/Delaware4/winners/Delaware4`

### 2025-06-22 — Delaware4 — Midday — 979 (double)

- Winner canonical: `799`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Delaware4.md`
- Winners lens: `sharepacks/2025-06-22/Delaware4/winners/Delaware4`

### 2025-06-22 — Florida4 — Evening — 924 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Florida4.md`
- Winners lens: `sharepacks/2025-06-22/Florida4/winners/Florida4`

### 2025-06-22 — Florida4 — Midday — 330 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Florida4.md`
- Winners lens: `sharepacks/2025-06-22/Florida4/winners/Florida4`

### 2025-06-22 — Indiana4 — Evening — 702 (mirror_double)

- Winner canonical: `027`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Indiana4.md`
- Winners lens: `sharepacks/2025-06-22/Indiana4/winners/Indiana4`

### 2025-06-22 — Michigan4 — Evening — 700 (double)

- Winner canonical: `007`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Michigan4.md`
- Winners lens: `sharepacks/2025-06-22/Michigan4/winners/Michigan4`

### 2025-06-22 — NewJersey4 — Evening — 887 (double)

- Winner canonical: `788`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewJersey4.md`
- Winners lens: `sharepacks/2025-06-22/NewJersey4/winners/NewJersey4`

### 2025-06-22 — NewYork4 — Midday — 202 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewYork4.md`
- Winners lens: `sharepacks/2025-06-22/NewYork4/winners/NewYork4`

### 2025-06-22 — Ohio4 — Evening — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Ohio4.md`
- Winners lens: `sharepacks/2025-06-22/Ohio4/winners/Ohio4`

### 2025-06-22 — OntarioCanada4 — Evening — 616 (double)

- Winner canonical: `166`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__OntarioCanada4.md`
- Winners lens: `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4`

### 2025-06-22 — Pennsylvania4 — Evening — 570 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4`

### 2025-06-22 — Pennsylvania4 — Midday — 398 (mirror_double)

- Winner canonical: `389`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4`

### 2025-06-22 — Virginia4 — Evening — 938 (mirror_double)

- Winner canonical: `389`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-22/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Virginia4.md`
- Winners lens: `sharepacks/2025-06-22/Virginia4/winners/Virginia4`

### 2025-06-23 — Connecticut4 — Evening — 938 (mirror_double)

- Winner canonical: `389`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Connecticut4.md`
- Winners lens: `sharepacks/2025-06-23/Connecticut4/winners/Connecticut4`

### 2025-06-23 — Delaware4 — Evening — 919 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Delaware4.md`
- Winners lens: `sharepacks/2025-06-23/Delaware4/winners/Delaware4`

### 2025-06-23 — Delaware4 — Midday — 669 (double)

- Winner canonical: `669`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Delaware4.md`
- Winners lens: `sharepacks/2025-06-23/Delaware4/winners/Delaware4`

### 2025-06-23 — Florida4 — Midday — 665 (double)

- Winner canonical: `566`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Florida4.md`
- Winners lens: `sharepacks/2025-06-23/Florida4/winners/Florida4`

### 2025-06-23 — Indiana4 — Midday — 110 (double)

- Winner canonical: `011`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Indiana4.md`
- Winners lens: `sharepacks/2025-06-23/Indiana4/winners/Indiana4`

### 2025-06-23 — Michigan4 — Evening — 964 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Michigan4.md`
- Winners lens: `sharepacks/2025-06-23/Michigan4/winners/Michigan4`

### 2025-06-23 — NewJersey4 — Midday — 106 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewJersey4.md`
- Winners lens: `sharepacks/2025-06-23/NewJersey4/winners/NewJersey4`

### 2025-06-23 — NewYork4 — Evening — 767 (double)

- Winner canonical: `677`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`15` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`15` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewYork4.md`
- Winners lens: `sharepacks/2025-06-23/NewYork4/winners/NewYork4`

### 2025-06-23 — NewYork4 — Midday — 638 (mirror_double)

- Winner canonical: `368`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewYork4.md`
- Winners lens: `sharepacks/2025-06-23/NewYork4/winners/NewYork4`

### 2025-06-23 — Ohio4 — Evening — 368 (mirror_double)

- Winner canonical: `368`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Ohio4.md`
- Winners lens: `sharepacks/2025-06-23/Ohio4/winners/Ohio4`

### 2025-06-23 — OntarioCanada4 — Evening — 438 (mirror_double)

- Winner canonical: `348`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__OntarioCanada4.md`
- Winners lens: `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4`

### 2025-06-23 — Pennsylvania4 — Evening — 040 (double)

- Winner canonical: `004`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4`

### 2025-06-23 — Pennsylvania4 — Midday — 164 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4`

### 2025-06-23 — PuertoRico4 — Evening — 454 (double)

- Winner canonical: `445`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__PuertoRico4.md`
- Winners lens: `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4`

### 2025-06-23 — PuertoRico4 — Midday — 858 (double)

- Winner canonical: `588`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__PuertoRico4.md`
- Winners lens: `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4`

### 2025-06-23 — Virginia4 — Evening — 385 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-06-23/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Virginia4.md`
- Winners lens: `sharepacks/2025-06-23/Virginia4/winners/Virginia4`

### 2025-12-30 — Connecticut4 — Midday — 095 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Connecticut4.md`
- Winners lens: `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4`

### 2025-12-30 — Florida4 — Midday — 377 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Florida4.md`
- Winners lens: `sharepacks/2025-12-30/Florida4/winners/Florida4`

### 2025-12-30 — Indiana4 — Midday — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Indiana4.md`
- Winners lens: `sharepacks/2025-12-30/Indiana4/winners/Indiana4`

### 2025-12-30 — Michigan4 — Midday — 250 (mirror_double)

- Winner canonical: `025`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Michigan4.md`
- Winners lens: `sharepacks/2025-12-30/Michigan4/winners/Michigan4`

### 2025-12-30 — NewYork4 — Midday — 051 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NewYork4.md`
- Winners lens: `sharepacks/2025-12-30/NewYork4/winners/NewYork4`

### 2025-12-30 — NorthCarolina4 — Midday — 455 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NorthCarolina4.md`
- Winners lens: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4`

### 2025-12-30 — Ohio4 — Evening — 327 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Ohio4.md`
- Winners lens: `sharepacks/2025-12-30/Ohio4/winners/Ohio4`

### 2025-12-30 — Ohio4 — Midday — 338 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Ohio4.md`
- Winners lens: `sharepacks/2025-12-30/Ohio4/winners/Ohio4`

### 2025-12-30 — OntarioCanada4 — Evening — 372 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__OntarioCanada4.md`
- Winners lens: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4`

### 2025-12-30 — OntarioCanada4 — Midday — 409 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__OntarioCanada4.md`
- Winners lens: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4`

### 2025-12-30 — Pennsylvania4 — Midday — 186 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`9` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4`

### 2025-12-30 — Virginia4 — Evening — 100 (double)

- Winner canonical: `001`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Virginia4.md`
- Winners lens: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`

### 2025-12-30 — Virginia4 — Midday — 888 (triple)

- Winner canonical: `888`
- Mirror pairs: `` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Virginia4.md`
- Winners lens: `sharepacks/2025-12-30/Virginia4/winners/Virginia4`

### 2025-12-31 — Connecticut4 — Evening — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Connecticut4.md`
- Winners lens: `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4`

### 2025-12-31 — Delaware4 — Evening — 337 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Delaware4.md`
- Winners lens: `sharepacks/2025-12-31/Delaware4/winners/Delaware4`

### 2025-12-31 — Florida4 — Evening — 211 (double)

- Winner canonical: `112`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Florida4.md`
- Winners lens: `sharepacks/2025-12-31/Florida4/winners/Florida4`

### 2025-12-31 — Michigan4 — Evening — 477 (double)

- Winner canonical: `477`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Michigan4.md`
- Winners lens: `sharepacks/2025-12-31/Michigan4/winners/Michigan4`

### 2025-12-31 — Michigan4 — Midday — 583 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Michigan4.md`
- Winners lens: `sharepacks/2025-12-31/Michigan4/winners/Michigan4`

### 2025-12-31 — NewJersey4 — Midday — 366 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NewJersey4.md`
- Winners lens: `sharepacks/2025-12-31/NewJersey4/winners/NewJersey4`

### 2025-12-31 — NewYork4 — Evening — 116 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NewYork4.md`
- Winners lens: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`

### 2025-12-31 — NewYork4 — Midday — 419 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NewYork4.md`
- Winners lens: `sharepacks/2025-12-31/NewYork4/winners/NewYork4`

### 2025-12-31 — NorthCarolina4 — Evening — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NorthCarolina4.md`
- Winners lens: `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4`

### 2025-12-31 — Pennsylvania4 — Evening — 221 (double)

- Winner canonical: `122`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Pennsylvania4.md`
- Winners lens: `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4`

### 2025-12-31 — SouthCarolina4 — Evening — 044 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`11` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`11` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__SouthCarolina4.md`
- Winners lens: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4`

### 2025-12-31 — Virginia4 — Evening — 636 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Virginia4.md`
- Winners lens: `sharepacks/2025-12-31/Virginia4/winners/Virginia4`

### 2025-12-31 — Virginia4 — Midday — 686 (double)

- Winner canonical: `668`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Virginia4.md`
- Winners lens: `sharepacks/2025-12-31/Virginia4/winners/Virginia4`

### 2026-01-01 — Connecticut4 — Midday — 228 (double)

- Winner canonical: `228`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4`

### 2026-01-01 — Delaware4 — Midday — 149 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Delaware4.md`
- Winners lens: `sharepacks/2026-01-01/Delaware4/winners/Delaware4`

### 2026-01-01 — Indiana4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Indiana4.md`
- Winners lens: `sharepacks/2026-01-01/Indiana4/winners/Indiana4`

### 2026-01-01 — Indiana4 — Midday — 474 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Indiana4.md`
- Winners lens: `sharepacks/2026-01-01/Indiana4/winners/Indiana4`

### 2026-01-01 — NewJersey4 — Evening — 504 (mirror_double)

- Winner canonical: `045`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4`

### 2026-01-01 — NewJersey4 — Midday — 770 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-01/NewJersey4/winners/NewJersey4`

### 2026-01-01 — NewYork4 — Midday — 117 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NewYork4.md`
- Winners lens: `sharepacks/2026-01-01/NewYork4/winners/NewYork4`

### 2026-01-01 — NorthCarolina4 — Evening — 053 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4`

### 2026-01-01 — NorthCarolina4 — Midday — 416 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4`

### 2026-01-01 — Ohio4 — Evening — 416 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Ohio4.md`
- Winners lens: `sharepacks/2026-01-01/Ohio4/winners/Ohio4`

### 2026-01-01 — Pennsylvania4 — Evening — 328 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4`

### 2026-01-01 — Pennsylvania4 — Midday — 322 (double)

- Winner canonical: `223`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`11` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`11` delta(cc-aux)=`0` draws=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4`

### 2026-01-02 — Delaware4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Delaware4.md`
- Winners lens: `sharepacks/2026-01-02/Delaware4/winners/Delaware4`

### 2026-01-02 — Indiana4 — Midday — 974 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Indiana4.md`
- Winners lens: `sharepacks/2026-01-02/Indiana4/winners/Indiana4`

### 2026-01-02 — NewJersey4 — Evening — 331 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4`

### 2026-01-02 — NewJersey4 — Midday — 633 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-02/NewJersey4/winners/NewJersey4`

### 2026-01-02 — NewYork4 — Midday — 998 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NewYork4/aux/draws/New_York_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NewYork4.md`
- Winners lens: `sharepacks/2026-01-02/NewYork4/winners/NewYork4`

### 2026-01-02 — NorthCarolina4 — Evening — 383 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4`

### 2026-01-02 — NorthCarolina4 — Midday — 033 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4`

### 2026-01-02 — Ohio4 — Evening — 133 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Ohio4.md`
- Winners lens: `sharepacks/2026-01-02/Ohio4/winners/Ohio4`

### 2026-01-02 — Ohio4 — Midday — 747 (double)

- Winner canonical: `477`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Ohio4.md`
- Winners lens: `sharepacks/2026-01-02/Ohio4/winners/Ohio4`

### 2026-01-02 — OntarioCanada4 — Evening — 816 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4`

### 2026-01-02 — OntarioCanada4 — Midday — 053 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4`

### 2026-01-02 — PuertoRico4 — Midday — 144 (double)

- Winner canonical: `144`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`10` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`10` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4`

### 2026-01-02 — SouthCarolina4 — Midday — 308 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4`

### 2026-01-03 — Connecticut4 — Evening — 181 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4`

### 2026-01-03 — Connecticut4 — Midday — 533 (double)

- Winner canonical: `335`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4`

### 2026-01-03 — Delaware4 — Evening — 797 (double)

- Winner canonical: `779`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Delaware4.md`
- Winners lens: `sharepacks/2026-01-03/Delaware4/winners/Delaware4`

### 2026-01-03 — Delaware4 — Midday — 422 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`5` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Delaware4.md`
- Winners lens: `sharepacks/2026-01-03/Delaware4/winners/Delaware4`

### 2026-01-03 — Florida4 — Evening — 611 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Florida4/aux/draws/Florida_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Florida4.md`
- Winners lens: `sharepacks/2026-01-03/Florida4/winners/Florida4`

### 2026-01-03 — Indiana4 — Evening — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Indiana4.md`
- Winners lens: `sharepacks/2026-01-03/Indiana4/winners/Indiana4`

### 2026-01-03 — Indiana4 — Midday — 527 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Indiana4.md`
- Winners lens: `sharepacks/2026-01-03/Indiana4/winners/Indiana4`

### 2026-01-03 — Michigan4 — Evening — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Michigan4.md`
- Winners lens: `sharepacks/2026-01-03/Michigan4/winners/Michigan4`

### 2026-01-03 — Ohio4 — Evening — 411 (double)

- Winner canonical: `114`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Ohio4.md`
- Winners lens: `sharepacks/2026-01-03/Ohio4/winners/Ohio4`

### 2026-01-03 — Pennsylvania4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4`

### 2026-01-03 — Pennsylvania4 — Midday — 744 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4`

### 2026-01-03 — SouthCarolina4 — Evening — 051 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4`

### 2026-01-04 — Connecticut4 — Evening — 311 (double)

- Winner canonical: `113`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4`

### 2026-01-04 — Delaware4 — Midday — 057 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Delaware4.md`
- Winners lens: `sharepacks/2026-01-04/Delaware4/winners/Delaware4`

### 2026-01-04 — Florida4 — Midday — 171 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Florida4/aux/draws/Florida_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Florida4.md`
- Winners lens: `sharepacks/2026-01-04/Florida4/winners/Florida4`

### 2026-01-04 — Indiana4 — Midday — 813 (mirror_double)

- Winner canonical: `138`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Indiana4.md`
- Winners lens: `sharepacks/2026-01-04/Indiana4/winners/Indiana4`

### 2026-01-04 — NewJersey4 — Evening — 261 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4`

### 2026-01-04 — NewJersey4 — Midday — 275 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-04/NewJersey4/winners/NewJersey4`

### 2026-01-04 — NewYork4 — Evening — 489 (mirror_double)

- Winner canonical: `489`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NewYork4/aux/draws/New_York_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NewYork4.md`
- Winners lens: `sharepacks/2026-01-04/NewYork4/winners/NewYork4`

### 2026-01-04 — NorthCarolina4 — Evening — 887 (double)

- Winner canonical: `788`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4`

### 2026-01-04 — Ohio4 — Evening — 492 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Ohio4.md`
- Winners lens: `sharepacks/2026-01-04/Ohio4/winners/Ohio4`

### 2026-01-04 — OntarioCanada4 — Evening — 382 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`7` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4`

### 2026-01-04 — Virginia4 — Evening — 217 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Virginia4.md`
- Winners lens: `sharepacks/2026-01-04/Virginia4/winners/Virginia4`

### 2026-01-04 — Virginia4 — Midday — 200 (double)

- Winner canonical: `002`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Virginia4.md`
- Winners lens: `sharepacks/2026-01-04/Virginia4/winners/Virginia4`

### 2026-01-05 — Connecticut4 — Evening — 660 (double)

- Winner canonical: `066`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Connecticut4/play_card.json`

### 2026-01-05 — Delaware4 — Evening — 267 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Delaware4.md`
- Winners lens: `sharepacks/2026-01-05/Delaware4/winners/Delaware4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Delaware4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Delaware4/play_card.json`

### 2026-01-05 — Florida4 — Evening — 994 (double)

- Winner canonical: `499`
- Mirror pairs: `4/9` | vtrac_group_family: `4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Florida4/aux/draws/Florida_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Florida4.md`
- Winners lens: `sharepacks/2026-01-05/Florida4/winners/Florida4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Florida4/play_card.json`

### 2026-01-05 — Florida4 — Midday — 080 (double)

- Winner canonical: `008`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Florida4/aux/draws/Florida_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=`due_doubles_mirror_single`@`6` box_methods_non_union=`due_doubles,due_doubles_mirror_single`
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Florida4.md`
- Winners lens: `sharepacks/2026-01-05/Florida4/winners/Florida4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Florida4/play_card.json`

### 2026-01-05 — Michigan4 — Evening — 772 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Michigan4.md`
- Winners lens: `sharepacks/2026-01-05/Michigan4/winners/Michigan4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Michigan4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Michigan4/play_card.json`

### 2026-01-05 — NewJersey4 — Evening — 694 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-05/NewJersey4/winners/NewJersey4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/NewJersey4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/NewJersey4/play_card.json`

### 2026-01-05 — NewYork4 — Midday — 080 (double)

- Winner canonical: `008`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/NewYork4/aux/draws/New_York_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=`consensus_double_9`@`9` box_methods_non_union=`consensus_double_9,stable_top`
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`
- Winners lens: `sharepacks/2026-01-05/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/NewYork4/play_card.json`

### 2026-01-05 — NorthCarolina4 — Midday — 553 (double)

- Winner canonical: `355`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/NorthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card.json`

### 2026-01-05 — Ohio4 — Evening — 711 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Ohio4.md`
- Winners lens: `sharepacks/2026-01-05/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Ohio4/play_card.json`

### 2026-01-05 — Ohio4 — Midday — 651 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Ohio4.md`
- Winners lens: `sharepacks/2026-01-05/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Ohio4/play_card.json`

### 2026-01-05 — OntarioCanada4 — Evening — 797 (double)

- Winner canonical: `779`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`8` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card.json`

### 2026-01-05 — OntarioCanada4 — Midday — 555 (triple)

- Winner canonical: `555`
- Mirror pairs: `` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`6` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card.json`

### 2026-01-05 — Pennsylvania4 — Evening — 600 (double)

- Winner canonical: `006`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Pennsylvania4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card.json`

### 2026-01-05 — PuertoRico4 — Evening — 972 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`8` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card.json`

### 2026-01-05 — PuertoRico4 — Midday — 732 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card.json`

### 2026-01-05 — SouthCarolina4 — Evening — 712 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/SouthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card.json`

### 2026-01-05 — SouthCarolina4 — Midday — 171 (double)

- Winner canonical: `117`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`7` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/SouthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card.json`

### 2026-01-05 — Virginia4 — Evening — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-05/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Virginia4.md`
- Winners lens: `sharepacks/2026-01-05/Virginia4/winners/Virginia4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-05/Virginia4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-05/Virginia4/play_card.json`

### 2026-01-06 — Connecticut4 — Evening — 737 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Connecticut4/play_card.json`

### 2026-01-06 — Delaware4 — Midday — 165 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`2` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Delaware4.md`
- Winners lens: `sharepacks/2026-01-06/Delaware4/winners/Delaware4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Delaware4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Delaware4/play_card.json`

### 2026-01-06 — Florida4 — Evening — 160 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Florida4/aux/draws/Florida_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Florida4.md`
- Winners lens: `sharepacks/2026-01-06/Florida4/winners/Florida4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Florida4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Florida4/play_card.json`

### 2026-01-06 — Indiana4 — Evening — 961 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Indiana4.md`
- Winners lens: `sharepacks/2026-01-06/Indiana4/winners/Indiana4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Indiana4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Indiana4/play_card.json`

### 2026-01-06 — Michigan4 — Midday — 618 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`9` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Michigan4/aux/draws/Michigan_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Michigan4.md`
- Winners lens: `sharepacks/2026-01-06/Michigan4/winners/Michigan4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Michigan4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Michigan4/play_card.json`

### 2026-01-06 — NewJersey4 — Evening — 942 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/NewJersey4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/NewJersey4/play_card.json`

### 2026-01-06 — NewYork4 — Midday — 181 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NewYork4/aux/draws/New_York_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewYork4.md`
- Winners lens: `sharepacks/2026-01-06/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/NewYork4/play_card.json`

### 2026-01-06 — NorthCarolina4 — Midday — 552 (double)

- Winner canonical: `255`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/NorthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/NorthCarolina4/play_card.json`

### 2026-01-06 — OntarioCanada4 — Evening — 433 (double)

- Winner canonical: `334`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/OntarioCanada4/play_card.json`

### 2026-01-06 — OntarioCanada4 — Midday — 111 (triple)

- Winner canonical: `111`
- Mirror pairs: `` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/OntarioCanada4/play_card.json`

### 2026-01-06 — Pennsylvania4 — Evening — 757 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-06/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/Pennsylvania4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-06/Pennsylvania4/play_card.json`

### 2026-01-07 — Connecticut4 — Evening — 553 (double)

- Winner canonical: `355`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`3` winner_in_family=`True`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card.json`

### 2026-01-07 — Connecticut4 — Midday — 156 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card.json`

### 2026-01-07 — Delaware4 — Evening — 922 (double)

- Winner canonical: `229`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Delaware4.md`
- Winners lens: `sharepacks/2026-01-07/Delaware4/winners/Delaware4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Delaware4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Delaware4/play_card.json`

### 2026-01-07 — Florida4 — Midday — 434 (double)

- Winner canonical: `344`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Florida4/aux/draws/Florida_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
- Winners lens: `sharepacks/2026-01-07/Florida4/winners/Florida4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Florida4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Florida4/play_card.json`

### 2026-01-07 — Indiana4 — Midday — 823 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Indiana4/aux/draws/Indiana_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Indiana4.md`
- Winners lens: `sharepacks/2026-01-07/Indiana4/winners/Indiana4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Indiana4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Indiana4/play_card.json`

### 2026-01-07 — Michigan4 — Evening — 616 (double)

- Winner canonical: `166`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Michigan4.md`
- Winners lens: `sharepacks/2026-01-07/Michigan4/winners/Michigan4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Michigan4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Michigan4/play_card.json`

### 2026-01-07 — NewJersey4 — Midday — 361 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/NewJersey4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/NewJersey4/play_card.json`

### 2026-01-07 — NewYork4 — Midday — 916 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NewYork4/aux/draws/New_York_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewYork4.md`
- Winners lens: `sharepacks/2026-01-07/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/NewYork4/play_card.json`

### 2026-01-07 — NorthCarolina4 — Evening — 202 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/NorthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card.json`

### 2026-01-07 — Ohio4 — Midday — 737 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Ohio4.md`
- Winners lens: `sharepacks/2026-01-07/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Ohio4/play_card.json`

### 2026-01-07 — Pennsylvania4 — Midday — 060 (double)

- Winner canonical: `006`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`3` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Pennsylvania4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card.json`

### 2026-01-07 — PuertoRico4 — Evening — 969 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`9` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`9` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card.json`

### 2026-01-07 — SouthCarolina4 — Evening — 336 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/SouthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card.json`

### 2026-01-07 — SouthCarolina4 — Midday — 288 (double)

- Winner canonical: `288`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`2` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/SouthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card.json`

### 2026-01-07 — Virginia4 — Evening — 990 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Virginia4.md`
- Winners lens: `sharepacks/2026-01-07/Virginia4/winners/Virginia4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Virginia4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Virginia4/play_card.json`

### 2026-01-07 — Virginia4 — Midday — 275 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-07/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Virginia4.md`
- Winners lens: `sharepacks/2026-01-07/Virginia4/winners/Virginia4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-07/Virginia4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-07/Virginia4/play_card.json`

### 2026-01-08 — Connecticut4 — Evening — 331 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card.json`

### 2026-01-08 — Connecticut4 — Midday — 106 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Connecticut4.md`
- Winners lens: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Connecticut4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card.json`

### 2026-01-08 — Florida4 — Midday — 429 (mirror_double)

- Winner canonical: `249`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Florida4/aux/draws/Florida_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Florida4.md`
- Winners lens: `sharepacks/2026-01-08/Florida4/winners/Florida4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Florida4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Florida4/play_card.json`

### 2026-01-08 — Indiana4 — Evening — 242 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`4` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Indiana4.md`
- Winners lens: `sharepacks/2026-01-08/Indiana4/winners/Indiana4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Indiana4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Indiana4/play_card.json`

### 2026-01-08 — NewJersey4 — Evening — 055 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-08/NewJersey4/winners/NewJersey4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/NewJersey4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card.json`

### 2026-01-08 — NewYork4 — Evening — 732 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`7` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`7` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewYork4/aux/draws/New_York_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewYork4.md`
- Winners lens: `sharepacks/2026-01-08/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/NewYork4/play_card.json`

### 2026-01-08 — NewYork4 — Midday — 199 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/NewYork4/aux/draws/New_York_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewYork4.md`
- Winners lens: `sharepacks/2026-01-08/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/NewYork4/play_card.json`

### 2026-01-08 — Ohio4 — Evening — 580 (mirror_double)

- Winner canonical: `058`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Ohio4.md`
- Winners lens: `sharepacks/2026-01-08/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Ohio4/play_card.json`

### 2026-01-08 — Ohio4 — Midday — 681 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`1` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Ohio4/aux/draws/Ohio_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Ohio4.md`
- Winners lens: `sharepacks/2026-01-08/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Ohio4/play_card.json`

### 2026-01-08 — OntarioCanada4 — Evening — 498 (mirror_double)

- Winner canonical: `489`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card.json`

### 2026-01-08 — OntarioCanada4 — Midday — 022 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=`consensus_double_9`@`9` box_methods_non_union=`consensus_double_9`
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card.json`

### 2026-01-08 — Pennsylvania4 — Midday — 750 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/Pennsylvania4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card.json`

### 2026-01-08 — PuertoRico4 — Evening — 479 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`2` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card.json`

### 2026-01-08 — SouthCarolina4 — Midday — 277 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-08/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__SouthCarolina4.md`
- Winners lens: `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-08/SouthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card.json`

### 2026-01-09 — Delaware4 — Evening — 681 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Delaware4/aux/draws/Delaware_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Delaware4.md`
- Winners lens: `sharepacks/2026-01-09/Delaware4/winners/Delaware4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Delaware4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Delaware4/play_card.json`

### 2026-01-09 — Delaware4 — Midday — 843 (mirror_double)

- Winner canonical: `348`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`5` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`5` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Delaware4/aux/draws/Delaware_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Delaware4.md`
- Winners lens: `sharepacks/2026-01-09/Delaware4/winners/Delaware4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Delaware4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Delaware4/play_card.json`

### 2026-01-09 — Indiana4 — Evening — 377 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Indiana4/aux/draws/Indiana_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Indiana4.md`
- Winners lens: `sharepacks/2026-01-09/Indiana4/winners/Indiana4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Indiana4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Indiana4/play_card.json`

### 2026-01-09 — Michigan4 — Evening — 273 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`3` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Michigan4/aux/draws/Michigan_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Michigan4.md`
- Winners lens: `sharepacks/2026-01-09/Michigan4/winners/Michigan4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Michigan4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Michigan4/play_card.json`

### 2026-01-09 — NewJersey4 — Midday — 287 (mirror_double)

- Winner canonical: `278`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`6` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`6` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md`
- Winners lens: `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/NewJersey4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/NewJersey4/play_card.json`

### 2026-01-09 — NewYork4 — Evening — 835 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`8` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`8` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewYork4/aux/draws/New_York_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewYork4.md`
- Winners lens: `sharepacks/2026-01-09/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/NewYork4/play_card.json`

### 2026-01-09 — NewYork4 — Midday — 989 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NewYork4/aux/draws/New_York_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewYork4.md`
- Winners lens: `sharepacks/2026-01-09/NewYork4/winners/NewYork4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/NewYork4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/NewYork4/play_card.json`

### 2026-01-09 — NorthCarolina4 — Midday — 177 (double)

- Winner canonical: `177`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`2` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`2` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NorthCarolina4.md`
- Winners lens: `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/NorthCarolina4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card.json`

### 2026-01-09 — Ohio4 — Evening — 090 (double)

- Winner canonical: `009`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`3` family_rank_match=`4` winner_in_family=`True`
- Aux DS audit: DS=`3` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Ohio4/aux/draws/Ohio_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=`due_doubles_mirror_double`@`6` box_methods_non_union=`due_doubles,due_doubles_mirror_double,due_doubles_mirror_single`
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Ohio4.md`
- Winners lens: `sharepacks/2026-01-09/Ohio4/winners/Ohio4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Ohio4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Ohio4/play_card.json`

### 2026-01-09 — OntarioCanada4 — Midday — 772 (double)

- Winner canonical: `277`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`0` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`0` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__OntarioCanada4.md`
- Winners lens: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/OntarioCanada4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card.json`

### 2026-01-09 — Pennsylvania4 — Midday — 811 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`1` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Pennsylvania4.md`
- Winners lens: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Pennsylvania4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card.json`

### 2026-01-09 — PuertoRico4 — Evening — 225 (double)

- Winner canonical: `225`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`5` winner_in_family=`True`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv`
- Candidate Universe: box_hit=`True` idx_hit=`True` best_box=`due_doubles_mirror_single`@`6` box_methods_non_union=`due_doubles_mirror_single`
- Play Card: box_hit=`True` idx_hit=`True`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card.json`

### 2026-01-09 — PuertoRico4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`False` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PuertoRico4.md`
- Winners lens: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/PuertoRico4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card.json`

### 2026-01-09 — Virginia4 — Evening — 262 (double)

- Winner canonical: `226`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`1` family_rank_match=`4` winner_in_family=`False`
- Aux DS audit: DS=`1` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Virginia4/aux/draws/Virginia_Evening_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Virginia4.md`
- Winners lens: `sharepacks/2026-01-09/Virginia4/winners/Virginia4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Virginia4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Virginia4/play_card.json`

### 2026-01-09 — Virginia4 — Midday — 380 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`4` family_rank_match=`` winner_in_family=`False`
- Aux DS audit: DS=`4` delta(cc-aux)=`0` draws=`sharepacks/2026-01-09/Virginia4/aux/draws/Virginia_Midday_draws.csv`
- Candidate Universe: box_hit=`False` idx_hit=`True` best_box=``@`` box_methods_non_union=``
- Play Card: box_hit=`False` idx_hit=`False`
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Virginia4.md`
- Winners lens: `sharepacks/2026-01-09/Virginia4/winners/Virginia4`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-09/Virginia4/candidate_universe.json`
- Predictive Play Card: `sharepacks/_predictive/2026-01-09/Virginia4/play_card.json`

