# Analysis Arena Stage 4 Fixture Replay Scorecard

Purpose: replay the Stage-3 queue against completed fixture windows before any scoring, translator, candidate, or budget rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- fixture_windows: `3`
- stage3_replay_rows: `1097`
- fixture_ledger_rows: `3291`
- replay_decision_rows: `1097`

## Guardrails
- Stage 4 is read-only. It does not alter live scoring, candidate generation, budgeting, or legacy pipelines.
- `survived_as_boxed_translator_candidate` means future translator-design evidence, not live-play permission.
- VTRAC/territory rows remain watch/decay only unless bounded boxed or exact replay evidence survives.
- Shared-lineage rows cannot be counted as independent multi-source proof.
- Legacy method names are locators; `future_primitive` is the architecture-facing label.

## Decision Counts

- `survived_as_support_gate`: `386`
- `low_denominator_watchlist`: `269`
- `blocked_by_state_concentration`: `230`
- `survived_with_lineage_guardrail`: `118`
- `watch_decay_only`: `40`
- `fixture_only_low_denominator`: `24`
- `diagnostic_fixture_only`: `14`
- `survived_as_boxed_translator_candidate`: `14`
- `demote_to_restraint`: `2`

## Queue Counts

- `P4_low_denominator_fixture_replay`: `496`
- `P2_support_gate_replay`: `400`
- `P1_boxed_translator_replay`: `147`
- `P3_vtrac_decay_watch_replay`: `40`
- `P4_diagnostic_replay`: `14`

## Mechanism Families

- `old_play_card_expression_spine`: `445`
- `positional_spine`: `131`
- `mirror_pair_closure_spine`: `126`
- `r_perm_spine`: `120`
- `vtrac_enhanced_secondary_spine`: `91`
- `blackapple_related_boxed_overlap`: `65`
- `misc_stage3_replay`: `53`
- `profit_alert_related_boxed_overlap`: `43`
- `vtrac_decay_watch_spine`: `16`
- `due_doubles_support_spine`: `7`

## Shared Lineage Risk

- `high`: `633`
- `medium`: `407`
- `low`: `57`

## Top Boxed Translator Survivors

| entity | primitive | windows | pool | positive/100 ASD | support/100 ASD | lineage | decision |
|---|---:|---:|---:|---:|---:|---:|---|
| `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` | `bounded_mirror_pair_box_overlap` | 3 | 1.284 | 6.818 | 6.818 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:mirror_pair_closure:canonical` | `bounded_mirror_pair_box_overlap` | 3 | 1.284 | 6.818 | 6.818 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:R-perm-4:canonical` | `bounded_mirror_pair_box_overlap` | 3 | 1.284 | 6.818 | 6.818 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` | `bounded_mirror_pair_box_overlap` | 3 | 1.284 | 6.818 | 6.818 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `bounded_mirror_pair_box_overlap` | 3 | 1.439 | 6.081 | 6.081 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:convergence_box_first:B36` | `legacy_budget_expression_locator` | 3 | 2.246 | 5.263 | 5.263 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `legacy_budget_expression_locator` | 3 | 2.246 | 5.263 | 5.263 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `legacy_budget_expression_locator` | 3 | 2.246 | 5.263 | 5.263 | high | survived_with_lineage_guardrail |

## Top Support Gates

| entity | primitive | windows | support/100 ASD | wrong-lane | decision |
|---|---:|---:|---:|---:|---|
| `old_play_card:strategy:v0_2_default:B24:combos` | `legacy_budget_expression_locator` | 3 | 58.333 | 0 | survived_as_support_gate |
| `translation_sandbox:diagnostic_straight_seed` | `misc_bounded_replay_fixture` | 3 | 54.762 | 0 | survived_as_support_gate |
| `old_play_card:strategy:conversion_box_first:B36:combos` | `legacy_budget_expression_locator` | 3 | 49.603 | 0 | survived_as_support_gate |
| `positional:positional_combo` | `bounded_positional_box_overlap` | 3 | 45.238 | 0 | survived_as_support_gate |
| `blackapple:recommended_canonicals` | `blackapple_support_gate_or_restraint` | 3 | 44.444 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B36:combos` | `legacy_budget_expression_locator` | 3 | 41.270 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B24:combos` | `legacy_budget_expression_locator` | 3 | 27.778 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack:R-perm-4` | `bounded_r_perm_box_overlap` | 3 | 24.206 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack_method:R-perm-4:canonical` | `bounded_r_perm_box_overlap` | 3 | 24.206 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B12:combos` | `legacy_budget_expression_locator` | 3 | 17.857 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack_method:PackA_vt8:canonical` | `misc_bounded_replay_fixture` | 3 | 8.730 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` | `misc_bounded_replay_fixture` | 3 | 8.730 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack:PackB_mirror3rd` | `misc_bounded_replay_fixture` | 3 | 7.273 | 0 | survived_as_support_gate |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B24:combos` | `bounded_mirror_pair_box_overlap` | 3 | 6.034 | 0 | survived_as_support_gate |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B24:combos` | `bounded_mirror_pair_box_overlap` | 3 | 6.034 | 0 | survived_as_support_gate |

## Restraint / Blocked Examples

| entity | primitive | reason | top-state share | fp rate |
|---|---:|---|---:|---:|
| `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals` | `blackapple_support_gate_or_restraint` | Blackapple-related replay is broad/no-conversion in fixtures; preserve as restraint material. | 0.0% | 100.0% |
| `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B12` | `blackapple_support_gate_or_restraint` | Blackapple-related replay is broad/no-conversion in fixtures; preserve as restraint material. | 0.0% | 100.0% |
| `box_overlap::old_candidate_universe:pack_method:consensus_double_9:canonical + survivor:survivor_frontier_canonicals` | `misc_bounded_replay_fixture` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_play_card:strategy:conversion_box_first:B12:combos + positional:positional_canonical` | `bounded_positional_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_play_card:strategy:conversion_box_first:B12:combos + positional:positional_combo` | `bounded_positional_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:top_canonicals` | `misc_bounded_replay_fixture` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` | `bounded_r_perm_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first:B24` | `bounded_r_perm_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` | `bounded_r_perm_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:conversion_box_first:B24` | `bounded_r_perm_box_overlap` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:top_canonicals` | `misc_bounded_replay_fixture` | Replay support is too concentrated in one state to promote. | 75.0% | 98.9% |
| `box_overlap::old_candidate_universe:pack_method:due_doubles_mirror_double:canonical + survivor:survivor_frontier_canonicals` | `due_doubles_support_gate` | Replay support is too concentrated in one state to promote. | 100.0% | 98.9% |

## Negative-Control Mechanism Summary

| mechanism | primitive | controls | avg fp rate | use |
|---|---:|---:|---:|---|
| `old_play_card_expression_spine` | `legacy_budget_expression_locator` | 1979 | 99.0% | candidate penalty/veto library; do not promote directly |
| `due_doubles_support_spine` | `due_doubles_support_gate` | 337 | 99.6% | candidate penalty/veto library; do not promote directly |
| `positional_spine` | `bounded_positional_box_overlap` | 269 | 99.2% | candidate penalty/veto library; do not promote directly |
| `misc_stage3_replay` | `misc_bounded_replay_fixture` | 183 | 99.2% | candidate penalty/veto library; do not promote directly |
| `profit_alert_related_boxed_overlap` | `tracker_boxed_support_gate` | 144 | 99.3% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `bounded_vtrac_enhanced_box_overlap` | 97 | 99.2% | candidate penalty/veto library; do not promote directly |
| `r_perm_spine` | `bounded_r_perm_box_overlap` | 43 | 98.6% | candidate penalty/veto library; do not promote directly |
| `blackapple_related_boxed_overlap` | `blackapple_support_gate_or_restraint` | 29 | 99.0% | candidate penalty/veto library; do not promote directly |
| `mirror_pair_closure_spine` | `bounded_mirror_pair_box_overlap` | 25 | 98.8% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `territory_vtrac_watch_overlap` | 4 | 99.2% | candidate penalty/veto library; do not promote directly |
| `vtrac_decay_watch_spine` | `territory_decay_watch_overlap` | 1 | 98.5% | candidate penalty/veto library; do not promote directly |

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.json`
- ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
- mechanism_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
- ab_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
- yield_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
- lineage_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
- decision_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
- negative_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
