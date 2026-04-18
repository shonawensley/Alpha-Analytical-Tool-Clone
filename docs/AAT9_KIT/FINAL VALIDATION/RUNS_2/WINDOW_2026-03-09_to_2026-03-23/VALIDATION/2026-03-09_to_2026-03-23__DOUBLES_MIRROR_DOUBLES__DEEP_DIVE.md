# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)

- Generated: `2026-04-16T23:39:06.691002+00:00`
- Rows: `223`

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

## Per-event evidence pointers

### 2026-03-09 — Delaware4 — Midday — 884 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Delaware4.md`
- Winners lens dir: ``

### 2026-03-09 — Florida4 — Evening — 941 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Florida4.md`
- Winners lens dir: ``

### 2026-03-09 — Florida4 — Midday — 383 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Florida4.md`
- Winners lens dir: ``

### 2026-03-09 — Michigan4 — Evening — 116 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Michigan4.md`
- Winners lens dir: ``

### 2026-03-09 — Michigan4 — Midday — 373 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Michigan4.md`
- Winners lens dir: ``

### 2026-03-09 — NewJersey4 — Midday — 617 (mirror_double)

- Winner canonical: `167`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-09 — NewYork4 — Midday — 900 (double)

- Winner canonical: `009`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NewYork4.md`
- Winners lens dir: ``

### 2026-03-09 — NorthCarolina4 — Evening — 000 (triple)

- Winner canonical: `000`
- Mirror pairs: `` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-09 — NorthCarolina4 — Midday — 855 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-09 — Ohio4 — Evening — 664 (double)

- Winner canonical: `466`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Ohio4.md`
- Winners lens dir: ``

### 2026-03-09 — Ohio4 — Midday — 848 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Ohio4.md`
- Winners lens dir: ``

### 2026-03-09 — OntarioCanada4 — Evening — 559 (double)

- Winner canonical: `559`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-09 — Pennsylvania4 — Evening — 966 (double)

- Winner canonical: `669`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-09 — Pennsylvania4 — Midday — 040 (double)

- Winner canonical: `004`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-09 — PuertoRico4 — Evening — 419 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-09 — PuertoRico4 — Midday — 887 (double)

- Winner canonical: `788`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-09 — SouthCarolina4 — Evening — 505 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-09 — SouthCarolina4 — Midday — 455 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-09 — Virginia4 — Evening — 188 (double)

- Winner canonical: `188`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Virginia4.md`
- Winners lens dir: ``

### 2026-03-10 — Connecticut4 — Evening — 556 (double)

- Winner canonical: `556`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-10 — Delaware4 — Midday — 350 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Delaware4.md`
- Winners lens dir: ``

### 2026-03-10 — Florida4 — Evening — 863 (mirror_double)

- Winner canonical: `368`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Florida4.md`
- Winners lens dir: ``

### 2026-03-10 — Florida4 — Midday — 558 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Florida4.md`
- Winners lens dir: ``

### 2026-03-10 — Indiana4 — Evening — 070 (double)

- Winner canonical: `007`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Indiana4.md`
- Winners lens dir: ``

### 2026-03-10 — Michigan4 — Evening — 233 (double)

- Winner canonical: `233`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Michigan4.md`
- Winners lens dir: ``

### 2026-03-10 — NewJersey4 — Midday — 990 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-10 — NewYork4 — Midday — 119 (double)

- Winner canonical: `119`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__NewYork4.md`
- Winners lens dir: ``

### 2026-03-10 — NorthCarolina4 — Midday — 782 (mirror_double)

- Winner canonical: `278`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-10 — Ohio4 — Evening — 570 (mirror_double)

- Winner canonical: `057`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Ohio4.md`
- Winners lens dir: ``

### 2026-03-10 — Ohio4 — Midday — 792 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Ohio4.md`
- Winners lens dir: ``

### 2026-03-10 — OntarioCanada4 — Midday — 712 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-10 — PuertoRico4 — Midday — 322 (double)

- Winner canonical: `223`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-10 — SouthCarolina4 — Midday — 783 (mirror_double)

- Winner canonical: `378`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-10 — Virginia4 — Midday — 316 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-10__Virginia4.md`
- Winners lens dir: ``

### 2026-03-11 — Connecticut4 — Evening — 922 (double)

- Winner canonical: `229`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-11 — Florida4 — Evening — 194 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Florida4.md`
- Winners lens dir: ``

### 2026-03-11 — Florida4 — Midday — 700 (double)

- Winner canonical: `007`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Florida4.md`
- Winners lens dir: ``

### 2026-03-11 — Indiana4 — Evening — 015 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Indiana4.md`
- Winners lens dir: ``

### 2026-03-11 — Michigan4 — Midday — 729 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Michigan4.md`
- Winners lens dir: ``

### 2026-03-11 — NewJersey4 — Evening — 388 (double)

- Winner canonical: `388`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-11 — NorthCarolina4 — Evening — 405 (mirror_double)

- Winner canonical: `045`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-11 — Ohio4 — Evening — 615 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Ohio4.md`
- Winners lens dir: ``

### 2026-03-11 — OntarioCanada4 — Midday — 577 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-11 — Pennsylvania4 — Evening — 757 (double)

- Winner canonical: `577`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-11 — SouthCarolina4 — Evening — 388 (double)

- Winner canonical: `388`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-11 — SouthCarolina4 — Midday — 441 (double)

- Winner canonical: `144`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-11 — Virginia4 — Evening — 331 (double)

- Winner canonical: `133`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-11__Virginia4.md`
- Winners lens dir: ``

### 2026-03-12 — Indiana4 — Evening — 636 (double)

- Winner canonical: `366`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Indiana4.md`
- Winners lens dir: ``

### 2026-03-12 — Michigan4 — Midday — 212 (double)

- Winner canonical: `122`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Michigan4.md`
- Winners lens dir: ``

### 2026-03-12 — NewJersey4 — Evening — 725 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-12 — NewJersey4 — Midday — 165 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-12 — NorthCarolina4 — Evening — 996 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-12 — Ohio4 — Evening — 721 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Ohio4.md`
- Winners lens dir: ``

### 2026-03-12 — Ohio4 — Midday — 385 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Ohio4.md`
- Winners lens dir: ``

### 2026-03-12 — Pennsylvania4 — Evening — 052 (mirror_double)

- Winner canonical: `025`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-12 — Pennsylvania4 — Midday — 732 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-12 — PuertoRico4 — Evening — 964 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-12 — SouthCarolina4 — Evening — 266 (double)

- Winner canonical: `266`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-12 — Virginia4 — Evening — 400 (double)

- Winner canonical: `004`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Virginia4.md`
- Winners lens dir: ``

### 2026-03-13 — Connecticut4 — Evening — 377 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-13 — Connecticut4 — Midday — 404 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-13 — Delaware4 — Midday — 266 (double)

- Winner canonical: `266`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Delaware4.md`
- Winners lens dir: ``

### 2026-03-13 — Florida4 — Evening — 334 (double)

- Winner canonical: `334`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Florida4.md`
- Winners lens dir: ``

### 2026-03-13 — Florida4 — Midday — 450 (mirror_double)

- Winner canonical: `045`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Florida4.md`
- Winners lens dir: ``

### 2026-03-13 — Indiana4 — Evening — 831 (mirror_double)

- Winner canonical: `138`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Indiana4.md`
- Winners lens dir: ``

### 2026-03-13 — NewJersey4 — Evening — 056 (mirror_double)

- Winner canonical: `056`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-13 — NorthCarolina4 — Midday — 950 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-13 — Ohio4 — Evening — 257 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Ohio4.md`
- Winners lens dir: ``

### 2026-03-13 — PuertoRico4 — Evening — 835 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-13 — SouthCarolina4 — Evening — 911 (double)

- Winner canonical: `119`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-13 — SouthCarolina4 — Midday — 969 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-13 — Virginia4 — Evening — 621 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Virginia4.md`
- Winners lens dir: ``

### 2026-03-14 — Connecticut4 — Midday — 762 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-14 — Delaware4 — Evening — 474 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Delaware4.md`
- Winners lens dir: ``

### 2026-03-14 — Florida4 — Evening — 273 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Florida4.md`
- Winners lens dir: ``

### 2026-03-14 — Florida4 — Midday — 270 (mirror_double)

- Winner canonical: `027`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Florida4.md`
- Winners lens dir: ``

### 2026-03-14 — Indiana4 — Midday — 080 (double)

- Winner canonical: `008`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Indiana4.md`
- Winners lens dir: ``

### 2026-03-14 — Michigan4 — Evening — 855 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Michigan4.md`
- Winners lens dir: ``

### 2026-03-14 — NewJersey4 — Midday — 274 (mirror_double)

- Winner canonical: `247`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-14 — NewYork4 — Evening — 723 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__NewYork4.md`
- Winners lens dir: ``

### 2026-03-14 — NewYork4 — Midday — 495 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__NewYork4.md`
- Winners lens dir: ``

### 2026-03-14 — NorthCarolina4 — Evening — 989 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-14 — NorthCarolina4 — Midday — 172 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-14 — Ohio4 — Evening — 844 (double)

- Winner canonical: `448`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Ohio4.md`
- Winners lens dir: ``

### 2026-03-14 — Ohio4 — Midday — 601 (mirror_double)

- Winner canonical: `016`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Ohio4.md`
- Winners lens dir: ``

### 2026-03-14 — OntarioCanada4 — Evening — 964 (mirror_double)

- Winner canonical: `469`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-14 — Pennsylvania4 — Evening — 969 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-14 — Pennsylvania4 — Midday — 511 (double)

- Winner canonical: `115`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-14 — PuertoRico4 — Evening — 181 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-14 — SouthCarolina4 — Evening — 136 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-14 — SouthCarolina4 — Midday — 202 (double)

- Winner canonical: `022`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-14 — Virginia4 — Midday — 707 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-14__Virginia4.md`
- Winners lens dir: ``

### 2026-03-15 — Connecticut4 — Evening — 558 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-15 — Delaware4 — Evening — 873 (mirror_double)

- Winner canonical: `378`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Delaware4.md`
- Winners lens dir: ``

### 2026-03-15 — Florida4 — Midday — 595 (double)

- Winner canonical: `559`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Florida4.md`
- Winners lens dir: ``

### 2026-03-15 — Indiana4 — Evening — 339 (double)

- Winner canonical: `339`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Indiana4.md`
- Winners lens dir: ``

### 2026-03-15 — Michigan4 — Evening — 337 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Michigan4.md`
- Winners lens dir: ``

### 2026-03-15 — NewJersey4 — Midday — 997 (double)

- Winner canonical: `799`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-15 — NorthCarolina4 — Evening — 404 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-15 — NorthCarolina4 — Midday — 020 (double)

- Winner canonical: `002`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-15 — Ohio4 — Evening — 831 (mirror_double)

- Winner canonical: `138`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Ohio4.md`
- Winners lens dir: ``

### 2026-03-15 — OntarioCanada4 — Evening — 538 (mirror_double)

- Winner canonical: `358`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-15 — OntarioCanada4 — Midday — 252 (double)

- Winner canonical: `225`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-15 — Pennsylvania4 — Midday — 336 (double)

- Winner canonical: `336`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-15 — Virginia4 — Evening — 747 (double)

- Winner canonical: `477`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Virginia4.md`
- Winners lens dir: ``

### 2026-03-15 — Virginia4 — Midday — 489 (mirror_double)

- Winner canonical: `489`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-15__Virginia4.md`
- Winners lens dir: ``

### 2026-03-16 — Connecticut4 — Evening — 700 (double)

- Winner canonical: `007`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-16 — Connecticut4 — Midday — 766 (double)

- Winner canonical: `667`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-16 — Delaware4 — Evening — 545 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Delaware4.md`
- Winners lens dir: ``

### 2026-03-16 — Delaware4 — Midday — 722 (double)

- Winner canonical: `227`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Delaware4.md`
- Winners lens dir: ``

### 2026-03-16 — Florida4 — Evening — 884 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Florida4.md`
- Winners lens dir: ``

### 2026-03-16 — Indiana4 — Evening — 276 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Indiana4.md`
- Winners lens dir: ``

### 2026-03-16 — Indiana4 — Midday — 279 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Indiana4.md`
- Winners lens dir: ``

### 2026-03-16 — Michigan4 — Evening — 454 (double)

- Winner canonical: `445`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Michigan4.md`
- Winners lens dir: ``

### 2026-03-16 — Michigan4 — Midday — 818 (double)

- Winner canonical: `188`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Michigan4.md`
- Winners lens dir: ``

### 2026-03-16 — NewYork4 — Evening — 797 (double)

- Winner canonical: `779`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__NewYork4.md`
- Winners lens dir: ``

### 2026-03-16 — NorthCarolina4 — Evening — 005 (double)

- Winner canonical: `005`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-16 — OntarioCanada4 — Midday — 207 (mirror_double)

- Winner canonical: `027`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-16 — Pennsylvania4 — Evening — 381 (mirror_double)

- Winner canonical: `138`
- Mirror pairs: `3/8` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-16 — SouthCarolina4 — Midday — 077 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-16 — Virginia4 — Evening — 961 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Virginia4.md`
- Winners lens dir: ``

### 2026-03-16 — Virginia4 — Midday — 440 (double)

- Winner canonical: `044`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Virginia4.md`
- Winners lens dir: ``

### 2026-03-17 — Connecticut4 — Evening — 077 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-17 — Connecticut4 — Midday — 991 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-17 — Indiana4 — Midday — 832 (mirror_double)

- Winner canonical: `238`
- Mirror pairs: `3/8` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Indiana4.md`
- Winners lens dir: ``

### 2026-03-17 — NewYork4 — Evening — 744 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__NewYork4.md`
- Winners lens dir: ``

### 2026-03-17 — NorthCarolina4 — Evening — 383 (double)

- Winner canonical: `338`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-17 — Ohio4 — Evening — 150 (mirror_double)

- Winner canonical: `015`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Ohio4.md`
- Winners lens dir: ``

### 2026-03-17 — Ohio4 — Midday — 327 (mirror_double)

- Winner canonical: `237`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Ohio4.md`
- Winners lens dir: ``

### 2026-03-17 — OntarioCanada4 — Evening — 868 (double)

- Winner canonical: `688`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-17 — Pennsylvania4 — Midday — 255 (double)

- Winner canonical: `255`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-17 — PuertoRico4 — Midday — 305 (mirror_double)

- Winner canonical: `035`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-17 — SouthCarolina4 — Evening — 922 (double)

- Winner canonical: `229`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-17 — SouthCarolina4 — Midday — 671 (mirror_double)

- Winner canonical: `167`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-18 — Connecticut4 — Midday — 848 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-18 — Delaware4 — Evening — 483 (mirror_double)

- Winner canonical: `348`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Delaware4.md`
- Winners lens dir: ``

### 2026-03-18 — Delaware4 — Midday — 773 (double)

- Winner canonical: `377`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Delaware4.md`
- Winners lens dir: ``

### 2026-03-18 — Florida4 — Evening — 585 (double)

- Winner canonical: `558`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Florida4.md`
- Winners lens dir: ``

### 2026-03-18 — NewJersey4 — Evening — 927 (mirror_double)

- Winner canonical: `279`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-18 — NewYork4 — Evening — 299 (double)

- Winner canonical: `299`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__NewYork4.md`
- Winners lens dir: ``

### 2026-03-18 — NorthCarolina4 — Evening — 038 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-18 — NorthCarolina4 — Midday — 077 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-18 — Pennsylvania4 — Evening — 083 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-18 — PuertoRico4 — Evening — 707 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-18 — PuertoRico4 — Midday — 464 (double)

- Winner canonical: `446`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-18 — SouthCarolina4 — Midday — 027 (mirror_double)

- Winner canonical: `027`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-18 — Virginia4 — Midday — 303 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-18__Virginia4.md`
- Winners lens dir: ``

### 2026-03-19 — Connecticut4 — Midday — 699 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-19 — Florida4 — Midday — 752 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Florida4.md`
- Winners lens dir: ``

### 2026-03-19 — Michigan4 — Midday — 398 (mirror_double)

- Winner canonical: `389`
- Mirror pairs: `3/8` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Michigan4.md`
- Winners lens dir: ``

### 2026-03-19 — NewJersey4 — Evening — 686 (double)

- Winner canonical: `668`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-19 — NewJersey4 — Midday — 822 (double)

- Winner canonical: `228`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-19 — NewYork4 — Midday — 303 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NewYork4.md`
- Winners lens dir: ``

### 2026-03-19 — NorthCarolina4 — Midday — 611 (double)

- Winner canonical: `116`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-19 — Ohio4 — Midday — 484 (double)

- Winner canonical: `448`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Ohio4.md`
- Winners lens dir: ``

### 2026-03-19 — OntarioCanada4 — Evening — 118 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-19 — PuertoRico4 — Evening — 909 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-19 — Virginia4 — Evening — 905 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Virginia4.md`
- Winners lens dir: ``

### 2026-03-20 — Delaware4 — Midday — 799 (double)

- Winner canonical: `799`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Delaware4.md`
- Winners lens dir: ``

### 2026-03-20 — Florida4 — Midday — 033 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Florida4.md`
- Winners lens dir: ``

### 2026-03-20 — Indiana4 — Evening — 884 (double)

- Winner canonical: `488`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Indiana4.md`
- Winners lens dir: ``

### 2026-03-20 — Indiana4 — Midday — 515 (double)

- Winner canonical: `155`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Indiana4.md`
- Winners lens dir: ``

### 2026-03-20 — NewJersey4 — Evening — 688 (double)

- Winner canonical: `688`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-20 — NewJersey4 — Midday — 337 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-20 — NewYork4 — Evening — 055 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NewYork4.md`
- Winners lens dir: ``

### 2026-03-20 — Ohio4 — Evening — 055 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Ohio4.md`
- Winners lens dir: ``

### 2026-03-20 — OntarioCanada4 — Evening — 163 (mirror_double)

- Winner canonical: `136`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-20 — OntarioCanada4 — Midday — 941 (mirror_double)

- Winner canonical: `149`
- Mirror pairs: `4/9` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-20 — PuertoRico4 — Evening — 118 (double)

- Winner canonical: `118`
- Mirror pairs: `` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-20 — SouthCarolina4 — Evening — 490 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-20 — Virginia4 — Midday — 776 (double)

- Winner canonical: `677`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Virginia4.md`
- Winners lens dir: ``

### 2026-03-21 — Connecticut4 — Evening — 394 (mirror_double)

- Winner canonical: `349`
- Mirror pairs: `4/9` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-21 — Connecticut4 — Midday — 954 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-21 — Delaware4 — Evening — 888 (triple)

- Winner canonical: `888`
- Mirror pairs: `` | vtrac_group_family: `3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Delaware4.md`
- Winners lens dir: ``

### 2026-03-21 — Florida4 — Midday — 466 (double)

- Winner canonical: `466`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Florida4.md`
- Winners lens dir: ``

### 2026-03-21 — Michigan4 — Evening — 699 (double)

- Winner canonical: `699`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Michigan4.md`
- Winners lens dir: ``

### 2026-03-21 — Michigan4 — Midday — 276 (mirror_double)

- Winner canonical: `267`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Michigan4.md`
- Winners lens dir: ``

### 2026-03-21 — NewJersey4 — Evening — 950 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-21 — NewJersey4 — Midday — 992 (double)

- Winner canonical: `299`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-21 — NewYork4 — Evening — 899 (double)

- Winner canonical: `899`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewYork4.md`
- Winners lens dir: ``

### 2026-03-21 — NewYork4 — Midday — 271 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewYork4.md`
- Winners lens dir: ``

### 2026-03-21 — NorthCarolina4 — Midday — 550 (double)

- Winner canonical: `055`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-21 — PuertoRico4 — Evening — 515 (double)

- Winner canonical: `155`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-21 — PuertoRico4 — Midday — 992 (double)

- Winner canonical: `299`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-21 — Virginia4 — Evening — 164 (mirror_double)

- Winner canonical: `146`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Virginia4.md`
- Winners lens dir: ``

### 2026-03-21 — Virginia4 — Midday — 940 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Virginia4.md`
- Winners lens dir: ``

### 2026-03-22 — Connecticut4 — Evening — 500 (double)

- Winner canonical: `005`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-22 — Connecticut4 — Midday — 303 (double)

- Winner canonical: `033`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-22 — Delaware4 — Evening — 844 (double)

- Winner canonical: `448`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Delaware4.md`
- Winners lens dir: ``

### 2026-03-22 — Delaware4 — Midday — 056 (mirror_double)

- Winner canonical: `056`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Delaware4.md`
- Winners lens dir: ``

### 2026-03-22 — Florida4 — Evening — 676 (double)

- Winner canonical: `667`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Florida4.md`
- Winners lens dir: ``

### 2026-03-22 — Indiana4 — Evening — 065 (mirror_double)

- Winner canonical: `056`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Indiana4.md`
- Winners lens dir: ``

### 2026-03-22 — Indiana4 — Midday — 991 (double)

- Winner canonical: `199`
- Mirror pairs: `` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Indiana4.md`
- Winners lens dir: ``

### 2026-03-22 — Michigan4 — Evening — 275 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Michigan4.md`
- Winners lens dir: ``

### 2026-03-22 — NewYork4 — Evening — 618 (mirror_double)

- Winner canonical: `168`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__NewYork4.md`
- Winners lens dir: ``

### 2026-03-22 — NorthCarolina4 — Evening — 242 (double)

- Winner canonical: `224`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-22 — OntarioCanada4 — Evening — 099 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-22 — OntarioCanada4 — Midday — 211 (double)

- Winner canonical: `112`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-22 — Pennsylvania4 — Evening — 580 (mirror_double)

- Winner canonical: `058`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-22 — SouthCarolina4 — Evening — 916 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-22 — Virginia4 — Evening — 742 (mirror_double)

- Winner canonical: `247`
- Mirror pairs: `2/7` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-22__Virginia4.md`
- Winners lens dir: ``

### 2026-03-23 — Connecticut4 — Midday — 000 (triple)

- Winner canonical: `000`
- Mirror pairs: `` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Connecticut4.md`
- Winners lens dir: ``

### 2026-03-23 — Delaware4 — Evening — 059 (mirror_double)

- Winner canonical: `059`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Delaware4.md`
- Winners lens dir: ``

### 2026-03-23 — Delaware4 — Midday — 355 (double)

- Winner canonical: `355`
- Mirror pairs: `` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Delaware4.md`
- Winners lens dir: ``

### 2026-03-23 — Florida4 — Evening — 232 (double)

- Winner canonical: `223`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Florida4.md`
- Winners lens dir: ``

### 2026-03-23 — Florida4 — Midday — 196 (mirror_double)

- Winner canonical: `169`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Florida4.md`
- Winners lens dir: ``

### 2026-03-23 — Indiana4 — Midday — 990 (double)

- Winner canonical: `099`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Indiana4.md`
- Winners lens dir: ``

### 2026-03-23 — Michigan4 — Evening — 455 (double)

- Winner canonical: `455`
- Mirror pairs: `` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Michigan4.md`
- Winners lens dir: ``

### 2026-03-23 — Michigan4 — Midday — 126 (mirror_double)

- Winner canonical: `126`
- Mirror pairs: `1/6` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Michigan4.md`
- Winners lens dir: ``

### 2026-03-23 — NewJersey4 — Evening — 380 (mirror_double)

- Winner canonical: `038`
- Mirror pairs: `3/8` | vtrac_group_family: `0/5-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NewJersey4.md`
- Winners lens dir: ``

### 2026-03-23 — NewYork4 — Evening — 409 (mirror_double)

- Winner canonical: `049`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NewYork4.md`
- Winners lens dir: ``

### 2026-03-23 — NewYork4 — Midday — 939 (double)

- Winner canonical: `399`
- Mirror pairs: `` | vtrac_group_family: `3/8-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NewYork4.md`
- Winners lens dir: ``

### 2026-03-23 — NorthCarolina4 — Evening — 615 (mirror_double)

- Winner canonical: `156`
- Mirror pairs: `1/6` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-23 — NorthCarolina4 — Midday — 794 (mirror_double)

- Winner canonical: `479`
- Mirror pairs: `4/9` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NorthCarolina4.md`
- Winners lens dir: ``

### 2026-03-23 — Ohio4 — Evening — 655 (double)

- Winner canonical: `556`
- Mirror pairs: `` | vtrac_group_family: `0/5-1/6`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Ohio4.md`
- Winners lens dir: ``

### 2026-03-23 — Ohio4 — Midday — 766 (double)

- Winner canonical: `667`
- Mirror pairs: `` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Ohio4.md`
- Winners lens dir: ``

### 2026-03-23 — OntarioCanada4 — Evening — 172 (mirror_double)

- Winner canonical: `127`
- Mirror pairs: `2/7` | vtrac_group_family: `1/6-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__OntarioCanada4.md`
- Winners lens dir: ``

### 2026-03-23 — Pennsylvania4 — Midday — 594 (mirror_double)

- Winner canonical: `459`
- Mirror pairs: `4/9` | vtrac_group_family: `0/5-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Pennsylvania4.md`
- Winners lens dir: ``

### 2026-03-23 — PuertoRico4 — Evening — 752 (mirror_double)

- Winner canonical: `257`
- Mirror pairs: `2/7` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-23 — PuertoRico4 — Midday — 733 (double)

- Winner canonical: `337`
- Mirror pairs: `` | vtrac_group_family: `2/7-3/8`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__PuertoRico4.md`
- Winners lens dir: ``

### 2026-03-23 — SouthCarolina4 — Evening — 005 (double)

- Winner canonical: `005`
- Mirror pairs: `0/5` | vtrac_group_family: `0/5`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-23 — SouthCarolina4 — Midday — 707 (double)

- Winner canonical: `077`
- Mirror pairs: `` | vtrac_group_family: `0/5-2/7`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__SouthCarolina4.md`
- Winners lens dir: ``

### 2026-03-23 — Virginia4 — Evening — 447 (double)

- Winner canonical: `447`
- Mirror pairs: `` | vtrac_group_family: `2/7-4/9`
- Control Center due-doubles: DS=`` family_rank_match=`` winner_in_family=``
- Aux DS audit: DS=`` delta(cc-aux)=`` draws=``
- RUNS report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Virginia4.md`
- Winners lens dir: ``

