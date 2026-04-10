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

### Planned Next Research Layers
- new canonical fresh-window intake
- later cross-window decay / carryover rollup once fresh windows accumulate
- later shadow translator prototype fed by the translator-learning ledger and the frontier control study

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
