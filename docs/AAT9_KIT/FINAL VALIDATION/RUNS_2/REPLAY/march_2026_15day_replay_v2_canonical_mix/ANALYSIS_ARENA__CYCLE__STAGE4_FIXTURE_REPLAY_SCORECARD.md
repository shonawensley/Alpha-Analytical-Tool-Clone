# Analysis Arena Stage 4 Fixture Replay Scorecard

Purpose: replay the Stage-3 queue against completed fixture windows before any scoring, translator, candidate, or budget rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- fixture_windows: `4`
- stage3_replay_rows: `1170`
- fixture_ledger_rows: `4680`
- replay_decision_rows: `1170`

## Guardrails
- Stage 4 is read-only. It does not alter live scoring, candidate generation, budgeting, or legacy pipelines.
- `survived_as_boxed_translator_candidate` means future translator-design evidence, not live-play permission.
- VTRAC/territory rows remain watch/decay only unless bounded boxed or exact replay evidence survives.
- Shared-lineage rows cannot be counted as independent multi-source proof.
- Legacy method names are locators; `future_primitive` is the architecture-facing label.

## Decision Counts

- `blocked_by_state_concentration`: `369`
- `survived_as_support_gate`: `363`
- `low_denominator_watchlist`: `172`
- `fixture_only_low_denominator`: `123`
- `survived_with_lineage_guardrail`: `71`
- `watch_decay_only`: `40`
- `diagnostic_fixture_only`: `21`
- `survived_as_boxed_translator_candidate`: `9`
- `needs_replay_refinement`: `2`

## Queue Counts

- `P2_support_gate_replay`: `584`
- `P4_low_denominator_fixture_replay`: `441`
- `P1_boxed_translator_replay`: `84`
- `P3_vtrac_decay_watch_replay`: `40`
- `P4_diagnostic_replay`: `21`

## Mechanism Families

- `old_play_card_expression_spine`: `422`
- `positional_spine`: `187`
- `mirror_pair_closure_spine`: `118`
- `vtrac_enhanced_secondary_spine`: `113`
- `r_perm_spine`: `112`
- `profit_alert_related_boxed_overlap`: `82`
- `misc_stage3_replay`: `58`
- `blackapple_related_boxed_overlap`: `45`
- `due_doubles_support_spine`: `17`
- `vtrac_decay_watch_spine`: `16`

## Shared Lineage Risk

- `high`: `638`
- `medium`: `448`
- `low`: `84`

## Top Boxed Translator Survivors

| entity | primitive | windows | pool | positive/100 ASD | support/100 ASD | lineage | decision |
|---|---:|---:|---:|---:|---:|---:|---|
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:top_canonicals` | `bounded_mirror_pair_box_overlap` | 4 | 1.507 | 1.866 | 3.358 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:top_canonicals` | `bounded_mirror_pair_box_overlap` | 4 | 1.507 | 1.866 | 3.358 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `bounded_mirror_pair_box_overlap` | 4 | 1.314 | 1.786 | 4.286 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` | `bounded_mirror_pair_box_overlap` | 4 | 1.671 | 1.780 | 3.858 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `bounded_mirror_pair_box_overlap` | 4 | 1.671 | 1.780 | 3.858 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `bounded_mirror_pair_box_overlap` | 4 | 1.671 | 1.780 | 3.858 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `bounded_mirror_pair_box_overlap` | 4 | 1.671 | 1.780 | 3.858 | high | survived_with_lineage_guardrail |
| `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` | `bounded_mirror_pair_box_overlap` | 4 | 1.671 | 1.780 | 3.858 | high | survived_with_lineage_guardrail |

## Top Support Gates

| entity | primitive | windows | support/100 ASD | wrong-lane | decision |
|---|---:|---:|---:|---:|---|
| `translation_sandbox:diagnostic_straight_seed` | `misc_bounded_replay_fixture` | 4 | 55.252 | 0 | survived_as_support_gate |
| `old_candidate_universe:pack:aux_positional` | `bounded_positional_box_overlap` | 4 | 53.005 | 0 | survived_as_support_gate |
| `old_play_card:strategy:conversion_box_first:B36:combos` | `legacy_budget_expression_locator` | 4 | 47.899 | 0 | survived_as_support_gate |
| `blackapple:recommended_canonicals` | `blackapple_support_gate_or_restraint` | 4 | 44.748 | 0 | survived_as_support_gate |
| `positional:positional_combo` | `bounded_positional_box_overlap` | 4 | 43.697 | 0 | survived_as_support_gate |
| `old_play_card:strategy:analysis_prefix:B24:combos` | `legacy_budget_expression_locator` | 4 | 43.277 | 0 | survived_as_support_gate |
| `old_play_card:strategy:conversion_box_first:B24:combos` | `legacy_budget_expression_locator` | 4 | 40.756 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B36:combos` | `legacy_budget_expression_locator` | 4 | 37.395 | 0 | survived_as_support_gate |
| `old_play_card:ranked_candidate_combo` | `legacy_budget_expression_locator` | 4 | 31.513 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B24:boxed_canonicals` | `legacy_budget_expression_locator` | 4 | 28.571 | 0 | survived_as_support_gate |
| `old_play_card:strategy:play_box_first:B24:combos` | `legacy_budget_expression_locator` | 4 | 28.571 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:convergence_box_first:B24` | `legacy_budget_expression_locator` | 4 | 27.731 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `legacy_budget_expression_locator` | 4 | 27.731 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `legacy_budget_expression_locator` | 4 | 27.731 | 0 | survived_as_support_gate |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `legacy_budget_expression_locator` | 4 | 27.731 | 0 | survived_as_support_gate |

## Restraint / Blocked Examples

| entity | primitive | reason | top-state share | fp rate |
|---|---:|---|---:|---:|
| `box_overlap::old_candidate_universe:candidate_universe_union_combo + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.4% |
| `box_overlap::brain1:context_reinforced_canonicals + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.4% |
| `box_overlap::old_candidate_universe:pack_method:stable_top:canonical + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::old_play_card:strategy:v0_2_default:B36:combos + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::brain1:context_reinforced_canonicals + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::profit_alerts:top_profit_alerts + shadow_policy:primary_cluster_context` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::brain1:dominant_canonicals + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::old_candidate_universe:pack:stable_top + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::old_play_card:strategy:v0_2_default:B36:combos + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.3% |
| `box_overlap::old_candidate_universe:pack:stable_top + profit_alerts:top_profit_alerts` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.2% |
| `box_overlap::brain1:dominant_canonicals + profit_alerts:implied_canonicals` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.2% |
| `box_overlap::profit_alerts:implied_canonicals + shadow_policy:primary_cluster_context` | `tracker_boxed_support_gate` | Replay support is too concentrated in one state to promote. | 71.4% | 99.2% |

## Negative-Control Mechanism Summary

| mechanism | primitive | controls | avg fp rate | use |
|---|---:|---:|---:|---|
| `old_play_card_expression_spine` | `legacy_budget_expression_locator` | 2080 | 99.2% | candidate penalty/veto library; do not promote directly |
| `due_doubles_support_spine` | `due_doubles_support_gate` | 351 | 99.5% | candidate penalty/veto library; do not promote directly |
| `positional_spine` | `bounded_positional_box_overlap` | 301 | 99.0% | candidate penalty/veto library; do not promote directly |
| `misc_stage3_replay` | `misc_bounded_replay_fixture` | 236 | 99.2% | candidate penalty/veto library; do not promote directly |
| `profit_alert_related_boxed_overlap` | `tracker_boxed_support_gate` | 154 | 99.2% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `bounded_vtrac_enhanced_box_overlap` | 116 | 99.0% | candidate penalty/veto library; do not promote directly |
| `mirror_pair_closure_spine` | `bounded_mirror_pair_box_overlap` | 103 | 98.4% | candidate penalty/veto library; do not promote directly |
| `r_perm_spine` | `bounded_r_perm_box_overlap` | 83 | 98.8% | candidate penalty/veto library; do not promote directly |
| `blackapple_related_boxed_overlap` | `blackapple_support_gate_or_restraint` | 60 | 99.1% | candidate penalty/veto library; do not promote directly |
| `vtrac_decay_watch_spine` | `territory_decay_watch_overlap` | 4 | 99.6% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `territory_vtrac_watch_overlap` | 1 | 100.0% | candidate penalty/veto library; do not promote directly |

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.json`
- ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
- mechanism_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
- ab_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
- yield_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
- lineage_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
- decision_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
- negative_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
