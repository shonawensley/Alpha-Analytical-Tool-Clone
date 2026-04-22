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

### Documentation Update Rules

- `WORKFLOW_CHANGELOG.md` records what was built or changed: new scripts, commands, workflow stages, outputs, and cadence behavior.
- `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md` records what is now part of the active Analysis Arena package, what it outputs, and what it feeds.
- `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md` records evidence-led lessons after review, especially repeated findings, confirmed behavior, contradicted assumptions, and explicitly provisional conclusions.
- RUNS/RUNS_2 reports and receipts record exact run outputs and should be treated as the run ledger.
- Git commits record exact implementation checkpoints and should not be the only human-readable memory layer.

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
9. `window-replay-readiness`
10. post-run audit Stage 1 / Stage 2 / Stage 2B / Stage 3 decision workbench / Stage 4 fixture replay / Stage 4B replay readback / Stage 4C shadow translator prototype / Stage 5 shadow translator fixture evaluator / Stage 5 readback decision memo / Stage 6A shadow translator specification / Stage 6B shadow replay simulator / Stage 6B readback decision memo / Stage 6C confirmation protocol / Stage 6D restraint calibration / Stage 6E support narrowing / Stage 6F integrated decision atlas / Stage 7A fresh confirmation scaffold / Stage 7B fixture replay harness

Planned downstream rebuild guardrail:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
- status: docs-only / design-brief-only until a fresh window reruns Stage 6B through Stage 7B and is compared against March

Window replay / replication protocol:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
- status: operating protocol for evidence-tier labeling
- evidence tiers:
  - `same_window_replay`
  - `archived_window_replication`
  - `true_fresh_confirmation`
- current archived-window replication package:
  - root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/`
  - predictive sharepacks: `sharepacks/_predictive_replay/archived_window_replay_v2/<D>/`
  - completed clean windows:
    - `WINDOW_2025-12-30_to_2026-01-09`
    - `WINDOW_2026-01-15_to_2026-01-18`
    - `WINDOW_2026-01-20_to_2026-01-22`
  - deliberate gap handling:
    - `2026-01-19` is excluded because the truth sharepack is missing; the surrounding January material is split into clean subwindows instead of being treated as one complete validation span
  - root readback chain:
    - Stage 2B cross-window rollup
    - Stage 3 decision workbench
    - Stage 4 fixture replay
    - Stage 4B replay readback
    - Stage 4C shadow translator prototype
    - Stage 5 shadow evaluator and readback
    - Stage 6A through Stage 6F shadow/restriction/confirmation layers
    - Stage 7A fresh-confirmation scaffold
    - Stage 7B fixture replay harness
  - March-vs-archived decision memo:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO.md`
    - compares canonical March Run 2 against archived replay v2 at Stage 6B-through-Stage 7B level
    - records that the `REPLAY/march_2026_15day_replay_v2` Stage 6B candidate-lane metrics are currently not a safe official metric baseline because the isolated replay root does not satisfy cross-window promotion gates
  - March replay Stage 6B comparability audit:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_REPLAY_STAGE6B_COMPARABILITY_AUDIT.md`
    - explains why isolated single-window replay zeroes candidate/support/restraint lanes at Stage 6B
    - recommended handling: use isolated replay for window-close traceability; use a corpus-mirrored replay root if official root-level Stage 6B same-window comparison is required
  - evidence posture:
    - archived replication and fixture replay only
    - useful for regression, traceability, lane separation, and fresh-window preflight
    - weakens the March primary-lane promotion case rather than confirming it
    - not sufficient by itself to unlock Stage 8A or any live translator/scoring/candidate/budget rewrite

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

### Stage 8 Downstream Rebuild Readiness
- doc:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
- posture:
  - design brief only
  - no runtime command
  - no scoring, candidate-generation, translator, budget, or legacy replacement permission
- purpose:
  - preserves the future Arena-native candidate object / boxed-straight expression / budget sandbox path
  - blocks implementation until a fresh window reruns Stage 6B through Stage 7B and is compared against March

### Window Replay And Replication Protocol
- doc:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
- script:
  - `scripts/tools/create_analysis_arena_window_replay_readiness_report.py`
  - `scripts/tools/create_analysis_arena_window_replay_comparison_report.py`
- command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
  - `python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare --force`
- outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__WINDOW_REPLAY_READINESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__WINDOW_REPLAY_COMPARE.md`
- posture:
  - operating protocol
  - read-only inventory / readiness / comparison layer
  - runtime commands are report-only
  - no fresh-confirmation substitution
- purpose:
  - lets existing windows support regression, replay, and historical replication work
  - keeps same-window replay, archived-window replication, and true fresh-window confirmation separated
  - records which existing windows appear best suited for future replay or replication
  - preserves baseline artifact hashes and comparison categories before any same-window rerun
  - compares baseline-vs-candidate artifacts after a rerun without granting Stage 8 permission

### Post-Run Audit, Stage 3 Decision Workbench, Stage 4 Fixture Replay, Stage 4B Readback, Stage 4C Shadow Prototype, Stage 5 Fixture Evaluator, Stage 5 Readback, Stage 6A Shadow Specification, Stage 6B Shadow Replay, Stage 6B Readback, Stage 6C Confirmation, Stage 6D Restraint Calibration, Stage 6E Support Narrowing, Stage 6F Atlas, Stage 7A Scaffold, And Stage 7B Harness
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
- Stage 5 script:
  - `scripts/tools/create_analysis_arena_stage5_shadow_translator_fixture_evaluator.py`
- Stage 5 readback script:
  - `scripts/tools/create_analysis_arena_stage5_readback_decision_memo.py`
- Stage 6A script:
  - `scripts/tools/create_analysis_arena_stage6a_shadow_translator_specification.py`
- Stage 6B script:
  - `scripts/tools/create_analysis_arena_stage6b_shadow_replay_simulator.py`
- Stage 6B readback script:
  - `scripts/tools/create_analysis_arena_stage6b_readback_decision_memo.py`
- Stage 6C script:
  - `scripts/tools/create_analysis_arena_stage6c_confirmation_protocol.py`
- Stage 6D script:
  - `scripts/tools/create_analysis_arena_stage6d_restraint_calibration_workbench.py`
- Stage 6E script:
  - `scripts/tools/create_analysis_arena_stage6e_support_modifier_narrowing_workbench.py`
- Stage 6F script:
  - `scripts/tools/create_analysis_arena_stage6f_integrated_decision_atlas.py`
- Stage 7A script:
  - `scripts/tools/create_analysis_arena_stage7a_fresh_confirmation_scaffold.py`
- Stage 7B script:
  - `scripts/tools/create_analysis_arena_stage7b_fixture_replay_harness.py`
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
- Stage 5 cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_COMPLETENESS_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_REPLAY_LEDGER.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_PROTOTYPE_MODE_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_ABLATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_WINDOW_STRATIFICATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_STATE_STRATIFICATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SUPPORT_GATE_ABLATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_RESTRAINT_EFFECT_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_PRO44_COMPLIANCE_CHECKLIST.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.csv`
- Stage 5 readback outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_MODE_DECISIONS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_NEXT_ACTION_QUEUE.csv`
- Stage 6A cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_LANE_CONTRACT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_GUARDRAIL_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SIMULATION_REQUIREMENTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_ACCEPTANCE_CHECKLIST.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_SPEC_QUEUE.csv`
- Stage 6B cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_REPLAY_SCENARIO_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_LANE_INCREMENT_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SUPPORT_MODIFIER_ABLATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_RESTRAINT_CALIBRATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_CONCENTRATION_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_GUARDRAIL_COMPLIANCE.csv`
- Stage 6B readback outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_GUARDRAIL_VERDICT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_NEXT_ACTION_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_MACRO_FINDINGS_CANDIDATES.csv`
- Stage 6C confirmation outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_CONFIRMATION_TEST_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_THRESHOLD_CONTRACT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_FRESH_WINDOW_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_REWRITE_BLOCKERS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_MACRO_REVIEW_GATE.csv`
- Stage 6D restraint calibration outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_NEXT_ACTIONS.csv`
- Stage 6E support narrowing outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_BUCKET_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NARROWING_CANDIDATES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_FAILURE_MODES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NEXT_ACTIONS.csv`
- Stage 6F integrated decision atlas outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_LANE_DECISION_ATLAS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_ACTIVE_BLOCKERS_AND_CLEARANCE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_MACRO_FINDINGS_DISPOSITION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
- Stage 7A fresh confirmation scaffold outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_RUN_CHECKLIST.csv`
- Stage 7B fixture replay harness outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_QUEUE_REPLAY_STATUS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_REQUIREMENT_COVERAGE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_BLOCKER_RECHECK.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_CASEBOOK_TRACEABILITY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_READY_FOR_FRESH_WINDOW.md`
- feeds:
  - next fresh-window review posture
  - replay queue design
  - future Brain1 / Brain2 / translator redesign
  - future/fresh-window confirmation design
  - future translator/scoring rewrite specification after Stage 5 review, Stage 6A specification, Stage 6B replay, Stage 6B readback, Stage 6C confirmation, Stage 6D restraint calibration, Stage 6E support narrowing, Stage 6F atlas review, Stage 7A scaffold evaluation, Stage 7B replay readiness, and future/fresh repeat evidence
- guardrail:
  - Stage 3 is replay/interpretation permission only; it does not change live scoring, candidate formation, or budget logic.
  - Stage 4 is a controlled fixture replay/audit layer only; it tests Stage 3 decisions by mechanism family, source A / source B / overlap lift, shared lineage, yield, concentration, and negative controls before any future rewrite.
  - Stage 4B is the readback layer that collapses Stage 4 rows into primitive clusters, casebook exemplars, leave-one-window-out outcomes, and a prototype-design queue. It still grants no live scoring permission.
  - Stage 4C is the shadow translator design layer that separates candidate-expression, lineage de-duplication, support context, decay watch, restraint/retest, and low-denominator lanes. It still grants no live scoring or candidate-generation permission.
  - Stage 5 is the fixture-backed evaluator that checks Stage 4C lanes against completed state-day artifacts, sample completeness, support context, restraint pressure, and source A / source B / overlap ablations. It still grants no live scoring or candidate-generation permission.
  - Stage 5 readback converts evaluator outputs into shadow-spec, support, restraint, watchlist, and documentation gates. It still grants no live scoring or candidate-generation permission.
  - Stage 6A converts Stage 5 readback gates into a formal shadow translator lane contract, guardrail matrix, simulation requirements, acceptance checklist, and spec queue. It still grants no live scoring or candidate-generation permission.
  - Stage 6B replays the Stage 6A lane contract as separated read-only scenarios with support/restraint ablations, concentration audit, and guardrail compliance. It still grants no live scoring or candidate-generation permission.
  - Stage 6B readback converts simulator outputs into scenario decisions, requirement results, guardrail verdicts, next actions, and macro-findings candidates. It still grants no live scoring or candidate-generation permission.
  - Stage 6C converts Stage 6B readback into future/fresh-window confirmation tests, threshold contracts, rewrite blockers, and macro-review gates. It still grants no live scoring or candidate-generation permission.
  - Stage 6D calibrates restraint pressure as soft-penalty research, including high-pressure rescue buckets and aggregate penalty hypotheses. It still grants no hard veto, live scoring, or candidate-generation permission.
  - Stage 6E narrows support context through paired support-on/support-off buckets and failure modes. It still grants no broad support-on, standalone support gate, live scoring, or candidate-generation permission.
  - Stage 6F integrates Stage 6B through Stage 6E into one lane decision atlas, active blocker table, future-window carry-forward queue, macro disposition table, and priority bucket casebook. It still grants no live scoring or candidate-generation permission.
  - Stage 7A turns Stage 6C/6F evidence into pending future-window confirmation requirements, March seed benchmarks, evaluation template rows, and a run checklist. It still confirms nothing until a future/fresh window is evaluated.
  - Stage 7B replays Stage 6F decisions against Stage 7A requirements, blocker rechecks, and casebook traceability. It is a fresh-window pre-flight harness only and still grants no live scoring or candidate-generation permission.

### Planned Next Research Layers
- new canonical fresh-window intake
- later cross-window decay / carryover rollup once fresh windows accumulate
- controlled same-window replay / archived-window replication using the window replay protocol when fresh gold days are not ready
- future/fresh execution of the Stage 6C confirmation contract using the Stage 7A scaffold and Stage 7B pre-flight queue
- later translator/scoring rewrite specification only after Stage 5 results, Stage 5 readback, Stage 6A specification, Stage 6B simulator, Stage 6B readback, Stage 6C confirmation, Stage 6D/6E workbench evidence, Stage 6F atlas, Stage 7A future-window evaluation, Stage 7B replay readiness, and future/fresh repeat evidence are reviewed
- Stage 8A Arena-native candidate object specification only after March-vs-fresh Stage 7B comparison separates repeated lanes from weakened, contradicted, blocked, and research-only lanes
- Stage 8B boxed / straight shadow expression simulator only after Stage 8A defines traceable candidate objects
- Stage 8C budget policy sandbox only after Stage 8B produces separated shadow expression outputs

## 7. Promotion Rules

- Do not promote a new scoring feature from one window alone.
- Do not promote frontier features into live scoring before the negative-control study is reviewed.
- Do not rebuild budgeting before the translator-learning layer exists.
- Do not start Stage 8A implementation before a fresh window reruns Stage 6B through Stage 7B and is compared against March.
- Do not treat same-window replay or archived-window replication as true fresh-window confirmation.
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
5. `AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
6. `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
7. `AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
8. `AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
9. `AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
10. `RUNS_2/PORTAL.md`
11. current window artifacts
12. `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md`
