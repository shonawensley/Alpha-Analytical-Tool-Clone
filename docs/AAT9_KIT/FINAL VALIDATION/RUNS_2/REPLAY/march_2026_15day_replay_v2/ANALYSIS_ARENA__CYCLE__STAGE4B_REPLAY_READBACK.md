# Analysis Arena Stage 4B Replay Readback

Purpose: turn Stage 4 fixture replay into primitive-level decision intelligence before any scoring or translator rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- stage4_decision_rows: `104`
- primitive_clusters: `60`
- holdout_rows: `104`
- translator_queue_rows: `32`
- negative_control_families: `11`

## Guardrails
- Stage 4B is read-only and cannot change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Primitive clusters collapse aliases and old-system locator names; they are not live rules.
- Holdout confirmation is a research filter, not live-play permission.
- Support gates, VTRAC/decay rows, concentration-blocked rows, and negative controls must stay in their lanes.

## Stage 4 Decision Baseline

- `needs_more_fixture_coverage`: `64`
- `watch_decay_only`: `40`

## Primitive Cluster Uses

- `decay_or_vtrac_watch_cluster`: `32`
- `diagnostic_fixture_cluster`: `28`

## Leave-One-Window-Out Outcomes

- `train_did_not_survive`: `104`

## Translator Queue Next Actions

- `keep_in_decay_watch_not_boxed_spend`: `32`

## Top Translator Candidate Clusters

| cluster | use | holdout confirm | pos/100 ASD | support/100 ASD | representative |
|---|---:|---:|---:|---:|---|

## Interpretation
- The cleanest future translator material is the cluster set marked `translator_candidate_cluster`.
- `translator_candidate_with_duplicate_credit_guardrail` is valuable but must be de-duplicated before any scoring prototype.
- `support_gate_cluster` should help later ranking/translator confidence only when paired with sharper bounded evidence.
- `state_concentration_retest_or_restraint` rows are warning signs until broader state confirmation appears.
- Negative-control families remain restraint/penalty/veto assets.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.json`
- cluster_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
- holdout_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
- translator_queue_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
