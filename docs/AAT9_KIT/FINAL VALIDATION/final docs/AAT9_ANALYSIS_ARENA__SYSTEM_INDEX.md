# AAT9 Analysis Arena System Index

Purpose:

- define the active Analysis Arena package as one coherent system
- make sure important additions do not live only in chat memory
- show what runs, what it outputs, what it feeds, and where learning is preserved

Use this as the compact registry for the active branch.

## 1. Memory Model

An important addition is only durable when it leaves these traces:

1. process hook
2. named artifact
3. doc anchor
4. learning destination

Git checkpoints are the implementation trail that proves the above really landed.

## 2. Scope

Active Analysis Arena branch means:

- arena-native predictive runtime
- arena-native post-results validation
- arena-native window-close learning stack
- old downstream Candidate Universe / Play Card infrastructure kept only as control arm / baseline

Active arena-era work lives mainly under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`
- `sharepacks/_predictive/<D>/...`

Legacy / control / archive lives mainly under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

## 3. Core Runtime Flow

Primary operator wrapper:

- `scripts/tools/run_analysis_arena_cycle.py`

Main phases:

1. `pre`
2. `post`
3. `window-close`
4. `window-decay-close`
5. `cross-window-rollup`
6. `tuneup-diagnostics`
7. `frontier-negative-control`
8. `fresh-window-readiness`
9. post-run audit Stage 1 / Stage 2 / Stage 2B / Stage 3 decision workbench / Stage 4 fixture replay / Stage 4B replay readback / Stage 4C shadow translator prototype

Per-window lock inputs that should be set before any fresh or backtest window:

1. window start / end dates
2. `decay-upload-days-total` horizon
3. whether full tail results exist or the decay companion should expect `right_censored` rows

## 3A. Results Truth Sidecars

### Bonus-Ball Truth Lane
- raw sidecar source:
  - `data/results_bonus/<D>.txt`
- builder:
  - `scripts/tools/create_bonus_ball_truth_report.py`
- outputs:
  - `reports/stable/bonus_ball_by_date/<D>/bonus_ball_truth.json`
  - `reports/stable/bonus_ball_by_date/<D>/bonus_ball_truth.csv`
  - `reports/stable/bonus_ball_by_date/<D>/bonus_ball_parity_audit.md`
- rules:
  - `data/results/<D>.txt` stays authoritative for winners HTML and existing Pick 3 grading
  - the sidecar parses the full structured source but only keeps the supported active bonus-ball states
  - bonus digits are accepted only when the sidecar Pick 3 draw parity-matches the core results draw for the same state and slot
  - bonus-ball truth remains a separate research lane and is not yet blended into standard straight / box metrics

## 4. Window-Close Artifact Registry

### Performance Gap
- script:
  - `scripts/tools/create_window_performance_gap_report.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP.json`
  - `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- feeds:
  - deep hit analysis
  - pure finalist scorecard
  - translator-learning ledger
  - deep window analysis

### Deep Hit Analysis
- script:
  - `scripts/tools/create_window_deep_hit_analysis_report.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json`
  - `WINDOW_<...>__ANALYSIS_ARENA__HIT_ROSTER.csv`
- feeds:
  - pure finalist scorecard
  - translator-learning ledger
  - later ranking / doubles studies

### C1/C2 Frontier Harness
- script:
  - `scripts/tools/create_window_c1_c2_frontier_harness_report.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json`
  - `WINDOW_<...>__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv`
- feeds:
  - pure finalist scorecard
  - translator-learning ledger
  - later frontier control study

### Pure Finalist Scorecard
- script:
  - `scripts/tools/create_window_pure_arena_finalist_scorecard.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json`
- feeds:
  - deep window analysis
  - cross-window rollup
  - future translator work

### Translator-Learning Ledger
- script:
  - `scripts/tools/create_window_translator_learning_ledger.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json`
  - `WINDOW_<...>__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`
- feeds:
  - deep window analysis
  - cross-window rollup
  - later translator prototype

### Decay / Carryover Scorecard
- script:
  - `scripts/tools/create_window_decay_carryover_scorecard.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.json`
  - `WINDOW_<...>__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`
- posture:
  - companion layer, not a replacement for same-day window-close metrics
  - primary horizon measured in total upload days, same-day included
  - draw offsets preserved as companion accounting because Midday/Evening crossover matters
- feeds:
  - deep window analysis
  - later cross-window decay study
  - later translator / packaging research

### Deep Window Codex Analysis
- script:
  - `scripts/tools/create_window_deep_analysis_report.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json`
- feeds:
  - macro findings log
  - cross-window interpretation

### Same-Window Legacy Comparison
- script:
  - `scripts/tools/create_arena_vs_legacy_window_comparison_report.py`
- outputs:
  - `WINDOW_<...>__ANALYSIS_ARENA__VS_LEGACY_COMPARISON.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__VS_LEGACY_COMPARISON.json`

## 5. Daily / State Review Registry

### Per-state Master Validation
- template:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- now includes:
  - explicit Aux badge inventory
  - cross-variant overlaps
  - due-VTRAC overlays by Combined / Midday / Evening
  - optional Part J advanced final questions for unusually informative states
  - companion VTRAC appendix:
    - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__VTRAC_REFERENCE_APPENDIX.md`

### Brain 2 Master Validation
- template:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

### Brain 2 Tracker Ledger
- producer:
  - `scripts/tools/create_brain2_master_validation_run_report.py`
- output:
  - `<D>__BRAIN2_TRACKER_LEDGER.json`

## 6. System-Level Learning Artifacts

### Metric Legend
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md`

### How To Read Fresh-Window Results
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`

### Macro Findings Log
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md`

### Cross-Window Rollup
- script:
  - `scripts/tools/create_analysis_arena_cross_window_rollup.py`
- outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.md`
  - `.json`
  - `.csv`

### Tune-Up Diagnostics
- script:
  - `scripts/tools/create_analysis_arena_tuneup_diagnostics.py`
- outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__BRAIN2_RANKING_DIAGNOSTIC.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TRACKER_LIFT_ROLLUP.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__DOUBLES_SUBTYPE_ROLLUP.csv`

### Frontier Negative-Control Study
- script:
  - `scripts/tools/create_analysis_arena_frontier_negative_control_study.py`
- outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_CASES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_LIFTS.csv`

### Fresh-Window Readiness
- script:
  - `scripts/tools/create_analysis_arena_fresh_window_readiness_report.py`
- outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.json`

### Post-Run Audit, Stage 3 Decision Workbench, Stage 4 Fixture Replay, Stage 4B Readback, And Stage 4C Shadow Prototype
- protocol:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md`
- Stage 1 / interpretation scripts:
  - `scripts/tools/create_window_evidence_utilization_audit.py`
  - `scripts/tools/create_window_audit_interpretation_report.py`
- Stage 2 / Stage 2B scripts:
  - `scripts/tools/create_window_stage2_signal_exposure_audit.py`
  - `scripts/tools/create_window_stage2b_signal_stack_analysis.py`
  - `scripts/tools/create_stage2b_cross_window_stack_rollup.py`
- Stage 3 script:
  - `scripts/tools/create_analysis_arena_stage3_decision_workbench.py`
- Stage 4 script:
  - `scripts/tools/create_analysis_arena_stage4_fixture_replay_harness.py`
- Stage 4B script:
  - `scripts/tools/create_analysis_arena_stage4b_replay_readback.py`
- Stage 4C script:
  - `scripts/tools/create_analysis_arena_stage4c_shadow_translator_prototype.py`
- Stage 3 cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`
- focus-window casebook output:
  - `WINDOW_<...>__ANALYSIS_ARENA__STAGE3_CASEBOOK.md`
  - `WINDOW_<...>__ANALYSIS_ARENA__STAGE3_CASEBOOK.csv`
- Stage 4 cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
- Stage 4B cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
- Stage 4C cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_LANE_SEPARATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_HOLDOUT_PROTOTYPE_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.csv`
- feeds:
  - next fresh-window review posture
  - replay queue design
  - future Brain1 / Brain2 / translator redesign
  - fixture-backed shadow translator evaluation harness
- guardrail:
  - Stage 3 is replay/interpretation permission only; it does not change live scoring, candidate formation, or budget logic.
  - Stage 4 is a controlled fixture replay/audit layer only; it tests Stage 3 decisions by mechanism family, source A / source B / overlap lift, shared lineage, yield, concentration, and negative controls before any future rewrite.
  - Stage 4B is the readback layer that collapses Stage 4 rows into primitive clusters, casebook exemplars, leave-one-window-out outcomes, and a prototype-design queue. It still grants no live scoring permission.
  - Stage 4C is the shadow translator design layer that separates candidate-expression, lineage de-duplication, support context, decay watch, restraint/retest, and low-denominator lanes. It still grants no live scoring or candidate-generation permission.

### Planned Next Research Layers
- new canonical fresh-window intake
- later cross-window decay / carryover rollup once fresh windows accumulate
- later fixture-backed shadow translator evaluation harness fed by Stage 4C prototype lanes and guardrails

## 7. Promotion Rules

- Do not promote a new scoring feature from one window alone.
- Do not promote frontier features into live scoring before the negative-control study is reviewed.
- Do not rebuild budgeting before the translator-learning layer exists.
- Do not use `B12/B24/B36` alone as the main measure of analysis quality.
- Keep arena truth, downstream realization, and opportunity gap as separate evaluation layers.

## 8. Current Known Weak Points

- Brain 2 ranking discrimination
- downstream translator / combo expression
- downstream budgeting / realization
- replay uplift is still mixed across window character

## 9. Active Reading Order

1. `README.md`
2. `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md`
3. `AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md`
4. `AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`
5. `AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
6. `AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
7. `RUNS_2/PORTAL.md`
8. current window artifacts
9. `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md`
