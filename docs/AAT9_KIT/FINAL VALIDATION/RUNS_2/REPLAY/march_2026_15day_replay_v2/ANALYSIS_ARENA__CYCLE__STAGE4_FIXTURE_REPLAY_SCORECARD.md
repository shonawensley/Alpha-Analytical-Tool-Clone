# Analysis Arena Stage 4 Fixture Replay Scorecard

Purpose: replay the Stage-3 queue against completed fixture windows before any scoring, translator, candidate, or budget rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- fixture_windows: `1`
- stage3_replay_rows: `104`
- fixture_ledger_rows: `104`
- replay_decision_rows: `104`

## Guardrails
- Stage 4 is read-only. It does not alter live scoring, candidate generation, budgeting, or legacy pipelines.
- `survived_as_boxed_translator_candidate` means future translator-design evidence, not live-play permission.
- VTRAC/territory rows remain watch/decay only unless bounded boxed or exact replay evidence survives.
- Shared-lineage rows cannot be counted as independent multi-source proof.
- Legacy method names are locators; `future_primitive` is the architecture-facing label.

## Decision Counts

- `needs_more_fixture_coverage`: `64`
- `watch_decay_only`: `40`

## Queue Counts

- `P4_diagnostic_replay`: `64`
- `P3_vtrac_decay_watch_replay`: `40`

## Mechanism Families

- `old_play_card_expression_spine`: `47`
- `vtrac_enhanced_secondary_spine`: `16`
- `vtrac_decay_watch_spine`: `16`
- `misc_stage3_replay`: `13`
- `positional_spine`: `4`
- `blackapple_related_boxed_overlap`: `2`
- `r_perm_spine`: `2`
- `due_doubles_support_spine`: `2`
- `profit_alert_related_boxed_overlap`: `2`

## Shared Lineage Risk

- `low`: `71`
- `medium`: `20`
- `high`: `13`

## Top Boxed Translator Survivors

| entity | primitive | windows | pool | positive/100 ASD | support/100 ASD | lineage | decision |
|---|---:|---:|---:|---:|---:|---:|---|

## Top Support Gates

| entity | primitive | windows | support/100 ASD | wrong-lane | decision |
|---|---:|---:|---:|---:|---|

## Restraint / Blocked Examples

| entity | primitive | reason | top-state share | fp rate |
|---|---:|---|---:|---:|

## Negative-Control Mechanism Summary

| mechanism | primitive | controls | avg fp rate | use |
|---|---:|---:|---:|---|
| `old_play_card_expression_spine` | `legacy_budget_expression_locator` | 1913 | 99.2% | candidate penalty/veto library; do not promote directly |
| `due_doubles_support_spine` | `due_doubles_support_gate` | 326 | 99.6% | candidate penalty/veto library; do not promote directly |
| `positional_spine` | `bounded_positional_box_overlap` | 244 | 99.0% | candidate penalty/veto library; do not promote directly |
| `misc_stage3_replay` | `misc_bounded_replay_fixture` | 188 | 99.2% | candidate penalty/veto library; do not promote directly |
| `profit_alert_related_boxed_overlap` | `tracker_boxed_support_gate` | 145 | 99.3% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `bounded_vtrac_enhanced_box_overlap` | 121 | 98.9% | candidate penalty/veto library; do not promote directly |
| `mirror_pair_closure_spine` | `bounded_mirror_pair_box_overlap` | 105 | 98.8% | candidate penalty/veto library; do not promote directly |
| `r_perm_spine` | `bounded_r_perm_box_overlap` | 93 | 98.8% | candidate penalty/veto library; do not promote directly |
| `blackapple_related_boxed_overlap` | `blackapple_support_gate_or_restraint` | 71 | 99.7% | candidate penalty/veto library; do not promote directly |
| `vtrac_decay_watch_spine` | `territory_decay_watch_overlap` | 18 | 99.6% | candidate penalty/veto library; do not promote directly |
| `vtrac_enhanced_secondary_spine` | `territory_vtrac_watch_overlap` | 11 | 99.2% | candidate penalty/veto library; do not promote directly |

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.json`
- ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
- mechanism_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
- ab_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
- yield_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
- lineage_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
- decision_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
- negative_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
