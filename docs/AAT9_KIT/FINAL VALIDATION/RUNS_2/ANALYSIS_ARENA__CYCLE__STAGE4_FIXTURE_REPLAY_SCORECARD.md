# Analysis Arena Stage 4 Fixture Replay Scorecard

Purpose: replay the Stage-3 queue against completed fixture windows before any scoring, translator, candidate, or budget rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- fixture_windows: `5`
- stage3_replay_rows: `1135`
- fixture_ledger_rows: `5675`
- replay_decision_rows: `1135`

## Guardrails
- Stage 4 is read-only. It does not alter live scoring, candidate generation, budgeting, or legacy pipelines.
- `survived_as_boxed_translator_candidate` means future translator-design evidence, not live-play permission.
- VTRAC/territory rows remain watch/decay only unless bounded boxed or exact replay evidence survives.
- Shared-lineage rows cannot be counted as independent multi-source proof.
- Legacy method names are locators; `future_primitive` is the architecture-facing label.

## Decision Counts

- `survived_as_support_gate`: `508`
- `blocked_by_state_concentration`: `217`
- `survived_with_lineage_guardrail`: `127`
- `low_denominator_watchlist`: `118`
- `diagnostic_fixture_only`: `58`
- `watch_decay_only`: `40`
- `fixture_only_low_denominator`: `33`
- `survived_as_boxed_translator_candidate`: `32`
- `needs_replay_refinement`: `2`

## Queue Counts

- `P2_support_gate_replay`: `562`
- `P4_low_denominator_fixture_replay`: `303`
- `P1_boxed_translator_replay`: `164`
- `P4_diagnostic_replay`: `66`
- `P3_vtrac_decay_watch_replay`: `40`

## Mechanism Families

- `old_play_card_expression_spine`: `387`
- `positional_spine`: `191`
- `mirror_pair_closure_spine`: `126`
- `vtrac_enhanced_secondary_spine`: `114`
- `r_perm_spine`: `106`
- `profit_alert_related_boxed_overlap`: `95`
- `misc_stage3_replay`: `51`
- `blackapple_related_boxed_overlap`: `46`
- `vtrac_decay_watch_spine`: `16`
- `due_doubles_support_spine`: `3`

## Shared Lineage Risk

- `high`: `575`
- `medium`: `474`
- `low`: `86`

## Top Boxed Translator Survivors

| entity | primitive | windows | pool | positive/100 ASD | support/100 ASD | lineage | decision |
|---|---:|---:|---:|---:|---:|---:|---|
| `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` | `bounded_mirror_pair_box_overlap` | 5 | 1.320 | 2.062 | 5.155 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` | `bounded_mirror_pair_box_overlap` | 5 | 1.320 | 2.062 | 5.155 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` | `bounded_mirror_pair_box_overlap` | 5 | 1.320 | 2.062 | 5.155 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` | `bounded_mirror_pair_box_overlap` | 5 | 1.320 | 2.062 | 5.155 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:aux_positional:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` | `bounded_positional_box_overlap` | 5 | 1.530 | 1.709 | 5.128 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:top_canonicals` | `bounded_mirror_pair_box_overlap` | 5 | 1.502 | 1.672 | 3.679 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:top_canonicals` | `bounded_mirror_pair_box_overlap` | 5 | 1.502 | 1.672 | 3.679 | high | survived_with_lineage_guardrail |
| `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:aux_positional` | `bounded_vtrac_enhanced_box_overlap` | 5 | 1.475 | 1.639 | 4.098 | medium | survived_as_boxed_translator_candidate |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `bounded_mirror_pair_box_overlap` | 5 | 1.323 | 1.597 | 5.112 | high | survived_with_lineage_guardrail |

## Top Support Gates

| entity | primitive | windows | support/100 ASD | wrong-lane | decision |
|---|---:|---:|---:|---:|---|
| `translation_sandbox:diagnostic_straight_seed` | `misc_bounded_replay_fixture` | 5 | 55.827 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack:aux_positional` | `bounded_positional_box_overlap` | 5 | 52.535 | 0 | survived_as_support_gate |
| `old_play_card:strategy:conversion_box_first:B36:combos` | `legacy_budget_expression_locator` | 5 | 47.180 | 0 | survived_as_support_gate |
| `blackapple:recommended_canonicals` | `blackapple_support_gate_or_restraint` | 5 | 45.113 | 0 | survived_as_support_gate |
| `positional:positional_combo` | `bounded_positional_box_overlap` | 5 | 44.737 | 0 | survived_as_support_gate |
| `old_play_card:strategy:analysis_prefix:B24:combos` | `legacy_budget_expression_locator` | 5 | 43.233 | 0 | survived_as_support_gate |
| `old_play_card:strategy:conversion_box_first:B24:combos` | `legacy_budget_expression_locator` | 5 | 40.226 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B36:combos` | `legacy_budget_expression_locator` | 5 | 37.406 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:convergence_box_first:B36` | `legacy_budget_expression_locator` | 5 | 35.902 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `legacy_budget_expression_locator` | 5 | 35.902 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `legacy_budget_expression_locator` | 5 | 35.902 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `legacy_budget_expression_locator` | 5 | 35.902 | 0 | survived_as_support_gate |
| `old_play_card:ranked_candidate_canonical` | `legacy_budget_expression_locator` | 5 | 31.579 | 0 | survived_as_support_gate |
| `old_play_card:ranked_candidate_combo` | `legacy_budget_expression_locator` | 5 | 31.579 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B24:boxed_canonicals` | `legacy_budget_expression_locator` | 5 | 28.195 | 0 | survived_as_support_gate |

## Restraint / Blocked Examples

| entity | primitive | reason | top-state share | fp rate |
|---|---:|---|---:|---:|
| `box_overlap::old_play_card:strategy_card:convergence_box_first:B24 + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.0% |
| `box_overlap::old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24 + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.0% |
| `box_overlap::old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24 + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.0% |
| `box_overlap::old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24 + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.0% |
| `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + translation_sandbox:diagnostic_boxed_seed` | `misc_bounded_replay_fixture` | Replay support is too concentrated in one state to promote. | 100.0% | 99.0% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy_card:analysis_prefix:B24` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy_card:convergence_box_first:B24` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 80.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 80.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 80.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 80.0% | 98.9% |
| `box_overlap::board_scoreboard:top_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` | `legacy_budget_expression_locator` | Replay support is too concentrated in one state to promote. | 75.0% | 98.9% |

## Negative-Control Mechanism Summary

| mechanism | primitive | controls | avg fp rate | use |
|---|---:|---:|---:|---|
| `old_play_card_expression_spine` | `legacy_budget_expression_locator` | 2080 | 99.1% | candidate penalty/veto library; do not promote directly |
| `due_doubles_support_spine` | `due_doubles_support_gate` | 351 | 99.6% | candidate penalty/veto library; do not promote directly |
| `positional_spine` | `bounded_positional_box_overlap` | 266 | 98.9% | candidate penalty/veto library; do not promote directly |
| `misc_stage3_replay` | `misc_bounded_replay_fixture` | 233 | 99.2% | candidate penalty/veto library; do not promote directly |
| `profit_alert_related_boxed_overlap` | `tracker_boxed_support_gate` | 151 | 99.1% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `bounded_vtrac_enhanced_box_overlap` | 97 | 99.0% | candidate penalty/veto library; do not promote directly |
| `r_perm_spine` | `bounded_r_perm_box_overlap` | 85 | 98.8% | candidate penalty/veto library; do not promote directly |
| `blackapple_related_boxed_overlap` | `blackapple_support_gate_or_restraint` | 49 | 99.2% | candidate penalty/veto library; do not promote directly |
| `mirror_pair_closure_spine` | `bounded_mirror_pair_box_overlap` | 43 | 98.6% | candidate penalty/veto library; do not promote directly |
| `vtrac_decay_watch_spine` | `territory_decay_watch_overlap` | 4 | 99.5% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `territory_vtrac_watch_overlap` | 1 | 100.0% | candidate penalty/veto library; do not promote directly |

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.json`
- ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
- mechanism_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
- ab_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
- yield_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
- lineage_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
- decision_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
- negative_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
