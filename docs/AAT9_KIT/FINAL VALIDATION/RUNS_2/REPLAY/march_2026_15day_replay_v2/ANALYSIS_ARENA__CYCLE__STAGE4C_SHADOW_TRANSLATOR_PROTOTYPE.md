# Analysis Arena Stage 4C Shadow Translator Prototype

Purpose: convert Stage 4B primitive clusters into a read-only shadow translator design package with strict lane separation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- prototype_rule_rows: `32`
- lane_matrix_rows: `1`
- support_gate_effect_rows: `0`
- restraint_audit_rows: `43`
- holdout_scorecard_rows: `1`
- casebook_rows: `16`

## Non-Negotiable Guardrails
- Stage 4C is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Clean candidate lanes are aggregate shadow expressions only; they are not deployable candidate lists.
- Lineage-guarded lanes require duplicate-credit removal before any future scoring prototype.
- Support gates cannot stand alone. They can only provide context beside sharper bounded evidence.
- VTRAC/decay lanes stay in carryforward/watch territory and cannot become boxed spend permission.
- Concentration and negative-control pressure become restraint/retest surfaces, not promotion surfaces.
- Old-system source names remain locators; `future_primitive` labels are the architecture-facing vocabulary.

## Prototype Lane Counts

- `decay_watch_only`: `32`

## Shadow Permission Counts

- `shadow_decay_watch_only`: `32`

## Restraint Pressure Counts

- `high`: `32`

## Lane Separation Matrix

| lane | rules | holdout | avg pos/100 ASD | avg support/100 ASD | pressure mix | guardrail |
|---|---:|---:|---:|---:|---|---|
| `decay_watch_only` | 32 | 0.0% | 16.671 | 39.933 | `high:32` | decay_or_vtrac_watch_never_boxed_spend_permission |

## Holdout Mode Summary

- `decay_watch_context`: holdout `0/0` confirmed (`0.0%`)

## Top Candidate-Expression Clusters

| cluster | lane | holdout | pos/100 ASD | support/100 ASD | pressure | permission |
|---|---:|---:|---:|---:|---:|---|

## Support / Restraint Read
- support_gate_rows: `0`
- paired_support_context_rows: `0`
- restraint_audit_rows: `43`
- Support context should be treated as a confidence modifier only after a candidate lane already exists.
- High negative-control or concentration pressure should become future penalty/veto/retest material before any promotion discussion.

## Interpretation
- Stage 4C gives us a clean vocabulary for future translator design, not a scoring rewrite.
- The most useful immediate output is lane separation: candidate expression, lineage deduplication, support context, decay watch, restraint, and low-denominator watchlist are now separated instead of blended.
- The next safe engineering step after reviewing Stage 4C is a fixture-backed prototype evaluation harness, still read-only, that checks candidate-expression modes before any live scoring rewrite.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.json`
- rule_registry_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv`
- lane_matrix_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_LANE_SEPARATION_MATRIX.csv`
- support_effects_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv`
- restraint_audit_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv`
- holdout_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_HOLDOUT_PROTOTYPE_SCORECARD.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.md`
