# Stage 3 March Casebook

Purpose: convert priority March examples into reusable translator, replay, restraint, and decay lessons.

## Guardrail

- These cases are teaching fixtures, not live scoring changes.
- Positive cases protect future translator changes from regression.
- Gap and wrong-lane cases define what the future expression layer should promote or restrain.

## Cohort Mix

- `gap_teacher`: `23`
- `positive_conversion`: `12`
- `wrong_lane_vtrac`: `12`
- `decay_teacher`: `10`
- `not_promoted_probe`: `10`

## Highest-Value Cases

- `2026-03-09` `Connecticut4` `Evening` winner=`091` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`1` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-09` `Pennsylvania4` `Midday` winner=`040` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`11` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-10` `Indiana4` `Evening` winner=`070` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`4` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-11` `Florida4` `Midday` winner=`700` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`3` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-11` `NewJersey4` `Evening` winner=`388` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`6` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-12` `NewYork4` `Evening` winner=`865` cohort=`gap_teacher` outcome=`EXACT_GAP` rank=`7` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-12` `NorthCarolina4` `Midday` winner=`314` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`8` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-12` `OntarioCanada4` `Evening` winner=`401` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`10` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-12` `SouthCarolina4` `Evening` winner=`266` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`13` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-14` `Indiana4` `Midday` winner=`080` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`4` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-14` `Michigan4` `Evening` winner=`855` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`5` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-14` `OntarioCanada4` `Midday` winner=`290` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`10` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-14` `SouthCarolina4` `Midday` winner=`202` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`13` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-15` `Michigan4` `Midday` winner=`840` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`5` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-17` `Indiana4` `Evening` winner=`108` cohort=`gap_teacher` outcome=`EXACT_GAP` rank=`4` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-20` `Virginia4` `Evening` winner=`259` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`14` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-20` `Virginia4` `Midday` winner=`776` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`14` sharp=`1` lesson=`translator_gap_teacher`
- `2026-03-21` `Pennsylvania4` `Evening` winner=`107` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`11` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-21` `PuertoRico4` `Midday` winner=`992` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`12` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-23` `Florida4` `Midday` winner=`196` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`3` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-23` `Indiana4` `Evening` winner=`420` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`4` sharp=`2` lesson=`translator_gap_teacher`
- `2026-03-23` `Ohio4` `Midday` winner=`766` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`9` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-23` `SouthCarolina4` `Evening` winner=`005` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`13` sharp=`3` lesson=`translator_gap_teacher`
- `2026-03-09` `OntarioCanada4` `Evening` winner=`559` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`10` sharp=`3` lesson=`positive_regression_anchor`
- `2026-03-10` `SouthCarolina4` `Evening` winner=`690` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`13` sharp=`5` lesson=`positive_regression_anchor`
- `2026-03-12` `Virginia4` `Evening` winner=`400` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`14` sharp=`4` lesson=`positive_regression_anchor`
- `2026-03-16` `OntarioCanada4` `Evening` winner=`041` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`10` sharp=`3` lesson=`positive_regression_anchor`
- `2026-03-16` `SouthCarolina4` `Midday` winner=`077` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`13` sharp=`5` lesson=`positive_regression_anchor`
- `2026-03-17` `NorthCarolina4` `Evening` winner=`383` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`8` sharp=`3` lesson=`positive_regression_anchor`
- `2026-03-18` `PuertoRico4` `Evening` winner=`707` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`12` sharp=`2` lesson=`positive_regression_anchor`
- `2026-03-19` `NewYork4` `Midday` winner=`303` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`7` sharp=`4` lesson=`positive_regression_anchor`
- `2026-03-19` `NorthCarolina4` `Midday` winner=`611` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`8` sharp=`4` lesson=`positive_regression_anchor`
- `2026-03-20` `Indiana4` `Midday` winner=`515` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`4` sharp=`3` lesson=`positive_regression_anchor`
- `2026-03-21` `NewJersey4` `Evening` winner=`950` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`6` sharp=`2` lesson=`positive_regression_anchor`
- `2026-03-22` `NewYork4` `Evening` winner=`618` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`7` sharp=`3` lesson=`positive_regression_anchor`
- `2026-03-09` `Indiana4` `Midday` winner=`203` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`4` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-03-09` `NewYork4` `Midday` winner=`900` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`7` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-03-09` `SouthCarolina4` `Midday` winner=`455` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`13` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-03-13` `OntarioCanada4` `Midday` winner=`879` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`10` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-03-16` `Indiana4` `Midday` winner=`279` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`4` sharp=`0` lesson=`wrong_lane_restraint_teacher`

## Generated Files

- Casebook CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__STAGE3_CASEBOOK.csv`
