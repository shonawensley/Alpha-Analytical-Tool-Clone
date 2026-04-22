# Stage 3 March Casebook

Purpose: convert priority March examples into reusable translator, replay, restraint, and decay lessons.

## Guardrail

- These cases are teaching fixtures, not live scoring changes.
- Positive cases protect future translator changes from regression.
- Gap and wrong-lane cases define what the future expression layer should promote or restrain.

## Cohort Mix

- `positive_conversion`: `12`
- `wrong_lane_vtrac`: `12`
- `decay_teacher`: `10`
- `not_promoted_probe`: `10`
- `gap_teacher`: `2`

## Highest-Value Cases

- `2026-01-21` `NorthCarolina4` `Evening` winner=`577` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`8` sharp=`2` lesson=`translator_gap_teacher`
- `2026-01-22` `Virginia4` `Evening` winner=`100` cohort=`gap_teacher` outcome=`BOX_GAP` rank=`14` sharp=`3` lesson=`translator_gap_teacher`
- `2026-01-20` `Michigan4` `Evening` winner=`881` cohort=`positive_conversion` outcome=`BOX_ANY` rank=`5` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-20` `Pennsylvania4` `Midday` winner=`218` cohort=`positive_conversion` outcome=`BOX_ANY` rank=`11` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-20` `Virginia4` `Midday` winner=`260` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`14` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-21` `Florida4` `Midday` winner=`350` cohort=`positive_conversion` outcome=`BOX_ANY` rank=`3` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-21` `Michigan4` `Midday` winner=`220` cohort=`positive_conversion` outcome=`BOX_ANY` rank=`5` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-21` `NewYork4` `Evening` winner=`233` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`7` sharp=`2` lesson=`positive_regression_anchor`
- `2026-01-21` `Ohio4` `Evening` winner=`740` cohort=`positive_conversion` outcome=`BOX_ANY` rank=`9` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-21` `OntarioCanada4` `Evening` winner=`199` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`10` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-21` `Pennsylvania4` `Evening` winner=`816` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`11` sharp=`2` lesson=`positive_regression_anchor`
- `2026-01-21` `PuertoRico4` `Midday` winner=`328` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`12` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-22` `Ohio4` `Evening` winner=`048` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`9` sharp=`0` lesson=`positive_regression_anchor`
- `2026-01-22` `OntarioCanada4` `Evening` winner=`544` cohort=`positive_conversion` outcome=`STRAIGHT` rank=`10` sharp=`3` lesson=`positive_regression_anchor`
- `2026-01-20` `Indiana4` `Evening` winner=`208` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`4` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-20` `NewYork4` `Evening` winner=`406` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`7` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-20` `NorthCarolina4` `Midday` winner=`254` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`8` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-20` `Ohio4` `Evening` winner=`843` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`9` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-20` `SouthCarolina4` `Midday` winner=`786` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`13` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-21` `NorthCarolina4` `Midday` winner=`767` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`8` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-21` `OntarioCanada4` `Midday` winner=`197` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`10` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-21` `Pennsylvania4` `Midday` winner=`848` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`11` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-21` `Virginia4` `Midday` winner=`314` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`14` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-22` `Connecticut4` `Midday` winner=`556` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`1` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-22` `Indiana4` `Midday` winner=`286` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`4` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-22` `Michigan4` `Evening` winner=`652` cohort=`wrong_lane_vtrac` outcome=`VTRAC_ONLY` rank=`5` sharp=`0` lesson=`wrong_lane_restraint_teacher`
- `2026-01-20` `Connecticut4` `Evening` winner=`961` cohort=`decay_teacher` outcome=`NO_CONVERSION` rank=`1` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `Connecticut4` `Midday` winner=`587` cohort=`decay_teacher` outcome=`VTRAC_ONLY` rank=`1` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `Florida4` `Midday` winner=`743` cohort=`decay_teacher` outcome=`NO_CONVERSION` rank=`3` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `Michigan4` `Midday` winner=`616` cohort=`decay_teacher` outcome=`NO_CONVERSION` rank=`5` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `PuertoRico4` `Evening` winner=`182` cohort=`decay_teacher` outcome=`NO_CONVERSION` rank=`12` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `PuertoRico4` `Midday` winner=`742` cohort=`decay_teacher` outcome=`VTRAC_ONLY` rank=`12` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-21` `Ohio4` `Midday` winner=`649` cohort=`decay_teacher` outcome=`VTRAC_ONLY` rank=`9` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-22` `NewYork4` `Evening` winner=`787` cohort=`decay_teacher` outcome=`BOX_ANY` rank=`7` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-22` `NewYork4` `Midday` winner=`981` cohort=`decay_teacher` outcome=`NO_CONVERSION` rank=`7` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-22` `PuertoRico4` `Midday` winner=`583` cohort=`decay_teacher` outcome=`BOX_ANY` rank=`12` sharp=`0` lesson=`carryforward_teacher`
- `2026-01-20` `NewJersey4` `Evening` winner=`689` cohort=`not_promoted_probe` outcome=`NO_CONVERSION` rank=`6` sharp=`0` lesson=`hypothesis_probe`
- `2026-01-20` `NewJersey4` `Midday` winner=`866` cohort=`not_promoted_probe` outcome=`NO_CONVERSION` rank=`6` sharp=`0` lesson=`hypothesis_probe`
- `2026-01-20` `NewYork4` `Midday` winner=`479` cohort=`not_promoted_probe` outcome=`NO_CONVERSION` rank=`7` sharp=`0` lesson=`hypothesis_probe`
- `2026-01-20` `Ohio4` `Midday` winner=`556` cohort=`not_promoted_probe` outcome=`VTRAC_ONLY` rank=`9` sharp=`0` lesson=`hypothesis_probe`

## Generated Files

- Casebook CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__STAGE3_CASEBOOK.csv`
