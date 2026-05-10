# Final Validation Workflow — Changelog (Master Validation)

Purpose: log **workflow-level** changes, “bumpy items”, and follow-ups discovered while running the Master Validation templates (Parts 1–5). This is the place to capture “fix later” items so they don’t get lost across Codex context resets.

Scope: docs, sharepack helpers (summarizers/validators/run-report generator), and workflow contracts. Avoid changing core analyzers/scorers unless explicitly approved.

---

## 2026-05-10

### Analysis Arena: Stage 7C / Stage 8A dossier freeze pass

- Froze the dossier package as a governing pre-Stage-8 control artifact:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__APPENDIX.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__MECHANISM_APPENDIX.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__FREEZE_RECEIPT.md`
- Locked package status from review posture to `frozen_governing_artifact`.
- Added explicit acceptance checks covering:
  - controlled permission vocabulary
  - bounded fixture bank
  - per-fixture blocker / `allowed_next_use` / fresh-window question coverage
  - mechanism appendix non-authorizing status
- Guardrail: the package remains non-runtime and does not authorize live
  scoring, candidate generation, boxed/straight runtime expression, or budget
  policy changes.

## 2026-04-29

### Analysis Arena: Stage 7C / Stage 8A entry dossier package

- Added the bounded pre-Stage-8 dossier package:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__APPENDIX.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__MECHANISM_APPENDIX.md`
- The dossier locks the pre-Stage-8 decision boundary:
  - executive verdict and evidence hierarchy
  - evidence permission matrix
  - primary restrained lane review
  - blocker register
  - Stage 8A shadow candidate-object schema
  - compact fixture bank
  - fresh-window confirmation charter
  - non-goals and forbidden conclusions
- The machine appendix turns the dossier into a machine-usable contract for:
  - lane permissions
  - blocker definitions
  - shadow-object fields
  - canonical fixtures
  - fresh-window pass/fail questions
  - forbidden conclusions
- The mechanism appendix preserves a bounded backlog of mechanism ideas without
  granting runtime permission.
- Guardrail: this package is evidence synthesis and boundary control only. It
  does not authorize live scoring, candidate generation, boxed/straight runtime
  expression, budget policy, or legacy-infrastructure replacement.

### Analysis Arena: final-doc registry updates for the dossier package

- Updated the final-doc portal and system index to include the Stage 7C /
  Stage 8A dossier package.
- Updated the system index archived replication SSOT pointer to the current
  June-inclusive canonical root:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v5_canonical_with_june2025/`
- Guardrail: registry updates are documentation-only and do not change runtime
  behavior.

## 2026-04-22

### Analysis Arena: March-vs-archived replay decision memo

- Added the read-only March-vs-archived replay decision memo:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__SCENARIO_COMPARISON.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__REQUIREMENT_COMPARISON.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__LANE_COMPARISON.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__BLOCKER_COMPARISON.csv`
- Compared canonical March Run 2 Stage 6B-through-Stage 7B evidence against the archived replay v2 Stage 6B-through-Stage 7B evidence.
- Recorded the March same-window replay caveat: `REPLAY/march_2026_15day_replay_v2` currently has zeroed core Stage 6B candidate-lane metrics and should be repaired or regenerated before serving as an official same-window metric baseline.
- Decision posture:
  - archived replay weakens the March primary-lane promotion case
  - support context, decay/watch, source overlap, restraint, and concentration guardrails remain necessary
  - Stage 8A remains design-ready but evidence-blocked
  - the next true decision gate remains a fresh-window Stage 6B-through-Stage 7B comparison
- Guardrail: this memo is comparison/readback only. It does not change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

### Analysis Arena: March replay Stage 6B comparability audit

- Added the read-only comparability audit:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_REPLAY_STAGE6B_COMPARABILITY_AUDIT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_REPLAY_STAGE6B_COMPARABILITY_AUDIT.json`
- Diagnosed the March same-window replay Stage 6B zero-lane caveat:
  - the replay root is isolated to one window
  - Stage 3 cross-window gates therefore label most rows as `needs_more_windows`
  - Stage 4C/Stage 5/Stage 6B boxed candidate and broad support lanes are zero because no cross-window candidate/support lanes are promoted
- Updated the decision memo interpretation: this is a comparability mismatch, not random corruption.
- Guardrail: no scoring, candidate generation, translator, budget, or legacy behavior changed.

### Analysis Arena: archived-window replay v2 evidence package

- Built the archived-window replication package under:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/`
- Completed three clean replay windows:
  - `WINDOW_2025-12-30_to_2026-01-09`
  - `WINDOW_2026-01-15_to_2026-01-18`
  - `WINDOW_2026-01-20_to_2026-01-22`
- Deliberately split the January 15-22 historical material around the missing `2026-01-19` truth sharepack so the replay corpus does not silently mix complete and incomplete validation days.
- Regenerated the replay readiness report after the user supplied missing standard and bonus result files.
- Ran each clean replay window through pre-range generation, control-arm grading, post-range validation, window-close analysis, decay companion scoring, Stage 1 evidence utilization, Stage 2 signal exposure, and Stage 2B signal-stack analysis.
- Ran the archived replay root through the cross-window Stage 2B rollup and Stage 3 through Stage 7B readback chain.
- Key generated root artifacts:
  - `ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_ROLLUP.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.md`
  - `ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.md`
- Readback posture:
  - cross-window replay has enough evidence to carry forward a disciplined fixture queue and fresh-window preflight
  - primary restrained candidate expression remains the strongest current shadow-design seed
  - broad support, decay/watch, VTRAC territory, duplicate-credit overlap, and hard restraint/veto remain blocked or companion-only
  - live translator/scoring/candidate/budget rewrite remains blocked until future/fresh confirmation clears the Stage 7A/7B gates

---

## 2026-04-21

### Analysis Arena: window replay comparison harness and March replay runbook

- Added a read-only baseline-vs-candidate replay comparison generator:
  - `scripts/tools/create_analysis_arena_window_replay_comparison_report.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare --force`
- New comparison outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__WINDOW_REPLAY_COMPARE.md`
- Added the March same-window replay runbook:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
- The comparison report currently runs in candidate-pending mode, preserving the March baseline target ledger until a rerun package exists.
- Guardrail: this is comparison/reporting only. It does not run a window, change scoring, create candidate objects, alter translator or budget logic, or unlock Stage 8A.

### Analysis Arena: window replay readiness report and comparison design

- Added a read-only replay-readiness generator:
  - `scripts/tools/create_analysis_arena_window_replay_readiness_report.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- New readiness outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__WINDOW_REPLAY_READINESS.md`
- Added a docs-only comparison design stub:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- The readiness report now records source coverage, per-window readiness, Stage 6B-through-Stage 7B artifact status, baseline artifact paths/hashes, and the strongest same-window / archived replication candidates.
- Guardrail: the command is report-only. It does not run a replay, change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

### Analysis Arena: window replay and replication protocol

- Added a docs-only operating protocol:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- The protocol separates available-window usage into three evidence tiers:
  - `same_window_replay`
  - `archived_window_replication`
  - `true_fresh_confirmation`
- Added a read-only available-window inventory:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
- The current strongest same-window replay candidate is `WINDOW_2026-03-09_to_2026-03-23`; the strongest archived replication candidate is `WINDOW_2025-12-30_to_2026-01-04`.
- Same-window replay can support regression, traceability, and before/after comparison, but it cannot unlock Stage 8A by itself.
- Archived-window replication can stress-test March findings on older historical windows, but it cannot replace true fresh-window confirmation.
- Updated the final-doc portal, system index, fresh-window reading guide, and Stage 8 readiness brief so reruns are labeled before interpretation.

### Analysis Arena: Stage 8 downstream rebuild readiness guardrail

- Added a docs-only Stage 8 readiness brief:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
- The brief preserves the future downstream rebuild path:
  - Stage 8A Arena-native candidate object specification
  - Stage 8B boxed / straight shadow expression simulator
  - Stage 8C budget policy sandbox
- Guardrail: this is not implementation permission. Stage 8A remains blocked until a fresh window reruns Stage 6B through Stage 7B and March-vs-fresh Stage 7B comparison separates repeated lanes from weakened, contradicted, blocked, and research-only lanes.
- Updated the final-doc portal, system index, and fresh-window reading guide so the Stage 8 path is durable but remains downstream of fresh-window confirmation.

### Analysis Arena: Stage 7B fixture replay/readiness harness

- Added a read-only pre-flight replay harness:
  - `scripts/tools/create_analysis_arena_stage7b_fixture_replay_harness.py`
- Added cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage7b-fixture-replay-harness --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 7B replays the Stage 6F carry-forward queue against Stage 7A confirmation requirements, active blocker rechecks, and priority casebook traceability.
- New cycle-level outputs include:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_QUEUE_REPLAY_STATUS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_REQUIREMENT_COVERAGE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_BLOCKER_RECHECK.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_CASEBOOK_TRACEABILITY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7B_READY_FOR_FRESH_WINDOW.md`
- Guardrail: Stage 7B is fresh-window replay readiness only. `ready_for_fresh_confirmation` and `ready_but_watch` are testability labels, not live scoring, candidate generation, translator, budget, hard-veto, broad-support, or deployment permission.

## 2026-04-20

### Analysis Arena: Stage 6F decision atlas and Stage 7A fresh confirmation scaffold

- Added a read-only integrated decision atlas and priority casebook:
  - `scripts/tools/create_analysis_arena_stage6f_integrated_decision_atlas.py`
- Added a read-only fresh-window confirmation scaffold:
  - `scripts/tools/create_analysis_arena_stage7a_fresh_confirmation_scaffold.py`
- Added cycle-wrapper commands:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6f-decision-atlas --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage7a-fresh-confirmation-scaffold --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 6F integrates Stage 6B readback, Stage 6C confirmation contracts, Stage 6D restraint calibration, Stage 6E support narrowing, and Stage 5 value-level examples into lane decisions, blockers, carry-forward queue, macro disposition, and a priority bucket casebook.
- Stage 7A converts the Stage 6C/6F package into pending future-window confirmation requirements, March seed benchmarks, future-window evaluation template rows, and a run checklist.
- New cycle-level outputs include:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_LANE_DECISION_ATLAS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_ACTIVE_BLOCKERS_AND_CLEARANCE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv`
- Guardrail: Stage 6F and Stage 7A are synthesis/scaffold layers only. They do not create live scoring, candidate generation, translator logic, hard vetoes, broad support promotion, macro confirmation, or budget behavior.

### Analysis Arena: Stage 6C/6D/6E post-readback confirmation workbenches

- Added three read-only post-Stage-6B research layers:
  - `scripts/tools/create_analysis_arena_stage6c_confirmation_protocol.py`
  - `scripts/tools/create_analysis_arena_stage6d_restraint_calibration_workbench.py`
  - `scripts/tools/create_analysis_arena_stage6e_support_modifier_narrowing_workbench.py`
- Added cycle-wrapper commands:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6c-confirmation-protocol --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6d-restraint-calibration --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6e-support-narrowing --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 6C converts Stage 6B readback into future/fresh-window confirmation tests, threshold contracts, fresh-window queue items, rewrite blockers, and macro-review gates.
- Stage 6D decomposes restraint pressure into bucket scorecards, high-pressure rescue/downweight candidates, soft-penalty policy hypotheses, and next actions.
- Stage 6E decomposes support context into paired support-on/support-off buckets, narrow support candidates, support failure modes, and next actions. It now requires meaningful support-off peer denominators before labeling support-on as a candidate.
- New cycle-level outputs include:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_CONFIRMATION_TEST_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6C_REWRITE_BLOCKERS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NARROWING_CANDIDATES.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_FAILURE_MODES.csv`
- Guardrail: Stage 6C/6D/6E outputs are confirmation and research gates only. They do not create live scoring, candidate generation, translator logic, hard vetoes, broad support promotion, or budget behavior.

### Analysis Arena: Stage 6B readback decision memo

- Added a read-only Stage 6B readback decision layer for Stage 6B simulator outputs:
  - `scripts/tools/create_analysis_arena_stage6b_readback_decision_memo.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6b-readback --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 6B readback converts simulator evidence into scenario decisions, Stage 6A requirement results, guardrail verdicts, next actions, and macro-findings candidates before future/fresh confirmation or any rewrite specification is considered.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_GUARDRAIL_VERDICT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_NEXT_ACTION_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_MACRO_FINDINGS_CANDIDATES.csv`
- Stage 6B readback remains a decision gate only. It does not create deployable candidate lists, scoring weights, translator logic, or budget behavior.

### Analysis Arena: Stage 6B shadow replay simulator

- Added a read-only Stage 6B shadow replay simulator for Stage 6A and Stage 5 outputs:
  - `scripts/tools/create_analysis_arena_stage6b_shadow_replay_simulator.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6b-shadow-replay --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 6B replays the Stage 6A lane contract against the Stage 5 value-level ledger as separated scenarios before any Stage 6B readback, translator rewrite, scoring rewrite, or budget work is considered.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_REPLAY_SCENARIO_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_LANE_INCREMENT_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SUPPORT_MODIFIER_ABLATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_RESTRAINT_CALIBRATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_CONCENTRATION_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_GUARDRAIL_COMPLIANCE.csv`
- Stage 6B keeps candidate-expression, support modifier, decay/watch companion, low-denominator watchlist, and restraint calibration lanes separated. It does not create deployable candidate lists, scoring weights, translator logic, or budget behavior.

### Analysis Arena: Stage 6A shadow translator specification

- Added a read-only Stage 6A shadow translator specification layer for Stage 5 readback outputs:
  - `scripts/tools/create_analysis_arena_stage6a_shadow_translator_specification.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage6a-shadow-spec --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 6A turns Stage 5 readback decisions into a formal shadow translator contract before any Stage 6B replay simulator or scoring rewrite is considered.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_LANE_CONTRACT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_GUARDRAIL_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SIMULATION_REQUIREMENTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_ACCEPTANCE_CHECKLIST.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_SPEC_QUEUE.csv`
- Stage 6A remains a specification gate only. It does not create deployable candidate lists, scoring weights, translator logic, or budget behavior.

### Analysis Arena: Stage 5 readback decision memo

- Added a read-only Stage 5 readback layer for Stage 5 evaluator outputs:
  - `scripts/tools/create_analysis_arena_stage5_readback_decision_memo.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage5-readback --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 5 readback converts evaluator outputs into explicit shadow-spec, support, restraint, watchlist, and documentation gates before any translator/scoring rewrite is considered.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO_RECEIPT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_MODE_DECISIONS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_NEXT_ACTION_QUEUE.csv`
- Formalized the Analysis Arena documentation memory rules in the system index:
  - changelog = what was built or changed
  - system index = what is part of the active package
  - macro findings log = evidence-led lessons after review
  - RUNS/RUNS_2 reports and receipts = exact run ledger
  - Git commits = implementation checkpoints
- Stage 5 readback remains an interpretation gate only. It does not create deployable candidate lists, scoring weights, translator logic, or budget behavior.

## 2026-04-18

### Analysis Arena: Stage 4 fixture replay harness

- Added a read-only Stage 4 fixture replay layer for the Stage 3 replay queue:
  - `scripts/tools/create_analysis_arena_stage4_fixture_replay_harness.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage4-fixture-replay --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- The harness tests Stage 3 candidates against completed Stage 2B fixture windows without changing live scoring, candidate generation, translator logic, budgeting, or legacy infrastructure.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_SCORECARD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_REPLAY_DECISION_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_MECHANISM_FAMILY_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_YIELD_AND_CONCENTRATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_SHARED_LINEAGE_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv`
- Stage 4 adds the approved `PRO_96` controls: mechanism-family replay, future primitive aliasing, source A / source B / overlap comparison, shared-lineage de-duplication, yield/concentration diagnostics, and negative-control restraint summaries.
- Updated the Analysis Arena system index, post-run audit protocol, and fresh-window reading guide so Stage 4 is part of the durable cadence package.

### Analysis Arena: Stage 4B replay readback

- Added a read-only Stage 4B readback layer for Stage 4 outputs:
  - `scripts/tools/create_analysis_arena_stage4b_replay_readback.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage4b-replay-readback --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 4B collapses Stage 4 rows into primitive clusters, survivor/support/restraint examples, leave-one-window-out outcomes, and a future translator design queue without changing scoring or pipeline behavior.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
- Stage 4B keeps the same guardrail as Stage 4: holdout confirmation and prototype queue membership are research filters, not live scoring permission.

### Analysis Arena: Stage 4C shadow translator prototype

- Added a read-only Stage 4C shadow translator design layer for Stage 4B outputs:
  - `scripts/tools/create_analysis_arena_stage4c_shadow_translator_prototype.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage4c-shadow-translator --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 4C converts the Stage 4B translator design queue into strict lanes without changing scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.json`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_LANE_SEPARATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_HOLDOUT_PROTOTYPE_SCORECARD.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.csv`
- Stage 4C separates clean boxed candidate expressions, lineage-guarded candidate expressions, support gates, decay/watch rows, concentration/retest rows, low-denominator watchlists, and restraint surfaces so future prototype work does not blend incompatible evidence lanes.

### Analysis Arena: Stage 5 shadow translator fixture evaluator

- Added a read-only Stage 5 fixture-backed evaluator for Stage 4C prototype lanes:
  - `scripts/tools/create_analysis_arena_stage5_shadow_translator_fixture_evaluator.py`
- Added the cycle-wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py stage5-shadow-evaluator --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force`
- Stage 5 replays Stage 4C lanes against completed Stage 2B state-day pairing fixtures and keeps sample completeness, support context, restraint pressure, source A / source B / overlap ablations, window/state stratification, and `PRO_44` compliance explicit.
- New cycle-level outputs:
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
- Stage 5 remains a pre-rewrite evidence layer. It does not create deployable candidate lists, scoring weights, translator logic, or budget behavior.

### Analysis Arena: Stage 3 decision workbench

- Added a read-only Stage 3 decision layer for completed post-run audit artifacts:
  - `scripts/tools/create_analysis_arena_stage3_decision_workbench.py`
- The workbench converts Stage 2 / Stage 2B evidence into replay and restraint artifacts without changing live scoring, candidate formation, budgeting, or legacy infrastructure.
- New cycle-level outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`
- New focus-window casebook outputs for the March 9-23 window:
  - `WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__STAGE3_CASEBOOK.md`
  - `WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__STAGE3_CASEBOOK.csv`
- Updated the Analysis Arena system index, post-run audit protocol, and fresh-window reading guide so Stage 3 is durable cadence memory rather than a one-off artifact.

---

## 2026-01-16

### Tool-first predictive defaults (Profit Alerts quarantined by default)

- Updated the prediction-layer helpers so “doing the obvious thing” produces tool-first artifacts by default:
  - Default `--profile` is now `tool_only` for:
    - `scripts/tools/create_candidate_universe.py`
    - `scripts/tools/create_play_card.py`
    - `scripts/tools/create_predictive_portfolio_report.py`
    - `scripts/tools/grade_candidate_universe.py`
    - `scripts/tools/grade_play_card.py`
    - `scripts/tools/create_predictive_run_report.py` (references the profiled `candidate_universe{__profile}.json`)
    - `scripts/tools/rollup_candidate_universe_corpus.py`
    - `scripts/tools/rollup_play_card_corpus.py`
  - Default `--top-n-dr` is now `0` for `create_candidate_universe.py` (DR “top candidates” demoted in v0.2 posture).
- Reminder: file naming remains profile-based:
  - `mixed` uses unsuffixed filenames (e.g., `candidate_universe.json`, `RUNS/*__CANDIDATE_UNIVERSE_GRADE.md`).
  - Non-`mixed` profiles are suffix-named (e.g., `candidate_universe__tool_only.json`, `RUNS/*__CANDIDATE_UNIVERSE_GRADE__tool_only.md`).
- Added a new Play Card strategy to support “rail conversion” experiments under tight budgets:
  - `conversion_box_first` (box-first + small reserved lane-closure slot; selection-layer only).

## 2026-01-13

### Candidate Universe: experimental mirror-pair closure (due-doubles seeded)

- Added an **optional**, bounded Candidate Universe pack to improve mirror-double conversion (index-hit → box-hit) by seeding mirror-pair selection from the Control Center Due Doubles families:
  - `method_id=mirror_pair_closure_due_doubles` (disabled by default; enabled via CLI flags)
  - Flags:
    - `create_candidate_universe.py --mirror-pair-closure-due-doubles-pairs <N>`
    - `create_candidate_universe.py --top-n-mirror-pair-closure-due-doubles <M>`
- Play Card selection recognizes the new method when present (still derived from Candidate Universe; does not change analyzers).

### Profit Alerts quarantine (ablation profiles; additive)

- Added `--profile {mixed,tool_only,profit_only}` support across the predictive “playset → selection → grading” layer so we can measure Profit Alerts without deleting them:
  - Candidate Universe: `scripts/tools/create_candidate_universe.py`
  - Play Cards: `scripts/tools/create_play_card.py`
  - Graders: `scripts/tools/grade_candidate_universe.py`, `scripts/tools/grade_play_card.py`
  - Rollups: `scripts/tools/rollup_candidate_universe_corpus.py`, `scripts/tools/rollup_play_card_corpus.py`
  - Predictive portfolio triage: `scripts/tools/create_predictive_portfolio_report.py`
- Output files are suffix-named (e.g., `candidate_universe__tool_only.json`, `RUNS/*__PLAY_CARD_GRADE__profit_only.*`) so they do not overwrite the mixed view.

## 2026-01-08

### Candidate Universe (pre-results): playset contract + generator + grader

- Added a first-class, gradeable predictions artifact (“Candidate Universe / Playset”) to bridge predictive snapshots → measurable performance:
  - Contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
  - Output (predictive SSOT): `sharepacks/_predictive/<D>/<STATE>/candidate_universe{__profile}.json`
- Added Candidate Universe generator (reads sharepacks only; deterministic; anti-leakage gate for predictive roots):
  - Command: `python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive`
  - File: `scripts/tools/create_candidate_universe.py`
- Candidate Universe now also ingests the Control Center “Due Doubles” board as a bounded, gradeable BOX pack:
  - Evidence: `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
  - Packs: `method_id=due_doubles` (`due_doubles:Combined|Midday|Evening`)
- Candidate Universe also supports bounded “mirror double” expansions seeded from the due-doubles top canonical (COMBINATION_FORMING3 primitive):
  - `method_id=due_doubles_mirror_single`
  - `method_id=due_doubles_mirror_double`
- Added Candidate Universe grader (reads results + candidate_universe.json; writes only to RUNS to keep predictive sharepacks immutable):
  - Command: `python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive`
  - Outputs: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.*`
  - File: `scripts/tools/grade_candidate_universe.py`
- Added a predictive run report scaffold to capture pre-results analysis alongside the Candidate Universe:
  - Command: `python3 scripts/tools/create_predictive_run_report.py --date <D> --state <STATE> --sharepacks-root sharepacks/_predictive`
  - Output: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE.md`
  - File: `scripts/tools/create_predictive_run_report.py`
- Added an optional cross-state predictive portfolio triage report (fast “where to focus” view):
  - Command: `python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive`
  - Output: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO.md`
  - File: `scripts/tools/create_predictive_portfolio_report.py`
- Added deterministic budgeted “Play Cards” (e.g., 12/24/36 combo cuts) derived from Candidate Universe (useful for live-style competitions + controlled selection experiments):
  - Command: `python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --budgets 12,24,36`
  - Output: `sharepacks/_predictive/<D>/<STATE>/play_card{__profile}.json`
  - File: `scripts/tools/create_play_card.py`
  - Built-in strategies: `play_box_first`, `analysis_prefix`, `convergence_box_first`
- Added Play Card grader (writes only to RUNS):
  - Command: `python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive`
  - Outputs: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE.*`
  - File: `scripts/tools/grade_play_card.py`
- Candidate Universe generator adds two additional bounded, gradeable pack sources:
  - Aux VTRAC overdue index closures: `method_id=aux_vtrac_index_overdue`
  - COMBINATION_FORMING3 consensus double pack: `method_id=consensus_double_9`
- Added corpus rollups (RUNS-only) to summarize grades across days (no horizon/carryover semantics; same-day grading only):
  - `python3 scripts/tools/rollup_candidate_universe_corpus.py` → `RUNS/candidate_universe_rollup.*`
  - `python3 scripts/tools/rollup_play_card_corpus.py` → `RUNS/play_card_rollup.*`
- Added “superbrain primitives” ledger (taxonomy layer mapping evidence → transforms → packs → grading):
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`

## 2026-01-07

### Predictive day (no results yet): isolated sharepacks + CC export

- Added a predictive-day orchestrator that builds a “no results yet” snapshot from a history workbook:
  - Command: `PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date <H>`
  - Output root: `sharepacks/_predictive/<D>/...` (kept separate from SSOT `sharepacks/<D>/`)
  - Notes:
    - No winners lens is generated (no `winners/`), and Profit Alerts evaluation is not run (requires future `data/results/*.txt`).
    - Control Center export is produced using a tab-header placeholder results file written into the predictive sharepack.
  - Files:
    - `scripts/tools/run_predictive_day.py`
    - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`
- Freezer now supports alternate sharepack roots and can skip winners-dependent VTRAC validation bundles (prevents stale `validation_report.*` from leaking into predictive packs):
  - `scripts/tools/freeze_sharepack_day.py` (`--sharepacks-root`, `--skip-global-vtrac`, `--skip-winners`)
- Aux sharepack summarizer supports alternate sharepack roots:
  - `scripts/tools/aux_sharepack_summary.py` (`--sharepacks-root`)
- SSOT pointers updated:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
  - `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`

## 2026-01-05

### Fix-Now: results parsing + DR overlays (Québec / Combined mismatch)

- Fixed results parsing to be **tab-aware + diacritic-robust** (prevents “Québec” / continuation lines contaminating the next state).
  - `alpha_analytical/control_center/batch_runner.py`
- Removed unsafe Digit Reduction `Combined` winner inference from “extra digits” on the results line (Combined winner is now driven only by the actual results mapping + sharepack convention).
  - `alpha_analytical/control_center/batch_runner.py`
- DR sharepack summarizer now loads winners from `data/results/<D>.txt` and **skips missing periods/states** (one-winner days, missing PR line) instead of emitting misleading “unknown” winners.
  - `scripts/tools/dr_sharepack_summary.py`
- DR winner validator now skips cleanly when a state has no line in `data/results/<D>.txt` (expected on some days; prevents false “missing winners/overlays” failures).
  - `scripts/tools/validate_dr_winners.py`
- Regenerated DR overlays + summaries in sharepacks (no full reruns):
  - `sharepacks/2025-06-21/PuertoRico4/digit_reduction/PuertoRico4/` (Combined winner now 910)
  - `sharepacks/2025-06-22/Pennsylvania4/digit_reduction/Pennsylvania4/` (Combined winner now 398)
  - `sharepacks/2025-06-23/PuertoRico4/digit_reduction/PuertoRico4/` (Combined winner now 858)
  - `sharepacks/2025-06-22/SouthCarolina4/digit_reduction/SouthCarolina4/` (Midday skipped; Evening/Combined winner 675)

### Fix-Now: one-winner day semantics (Midday blank)

- Stable/Hot Zones summarizers + validators now preserve Midday vs Evening using the tab-structured results mapping (no “Evening unknown” / false Midday labeling on one-winner days).
  - `scripts/tools/stable_sharepack_summary.py`
  - `scripts/tools/validate_stable_winners.py`
  - `scripts/tools/hot_zones_sharepack_summary.py`
  - `scripts/tools/validate_hot_zones_winners.py`

### Fix (future): table hygiene (`nan**`)

- Future table generation treats NaN as empty and avoids applying `*`/`**` markers to empty cells (prevents confusing `nan**` artifacts).
  - `src/utils/table_generator.py`

### Run reports + corpus refresh

- Updated run reports to remove now-fixed DR Combined mismatch narratives and reflect corrected one-winner handling:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Pennsylvania4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__SouthCarolina4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__PuertoRico4.md`
- Refreshed corpus exports after fixes:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`

### New corpus days: Dec/Jan block (2025‑12‑30 → 2026‑01‑04)

- Added new history workbooks + results files and built sharepacks for:
  - `sharepacks/2025-12-30/` (H=2025-12-29)
  - `sharepacks/2025-12-31/` (H=2025-12-30)
  - `sharepacks/2026-01-01/` (H=2025-12-31)
  - `sharepacks/2026-01-02/` (H=2026-01-01)
  - `sharepacks/2026-01-03/` (H=2026-01-02)
  - `sharepacks/2026-01-04/` (H=2026-01-03)
- Corpus audit passes for the full 6-day block:
  - `reports/audit/sharepacks_audit_20260105_125553.md` (PASS=825 WARN=3 FAIL=0 SKIP=6)
  - WARN/SKIP can be expected when a state/day has no results line (e.g., Puerto Rico on some days); treat FAIL as “fix-now”.
- Filled per-state run reports (Parts A–5) using sharepack summaries + results mapping (no analyzer reruns):
  - `scripts/tools/fill_master_validation_run_report.py`
- Normalized Part 5 formatting in run reports so corpus export can parse Pack/Drivers/Fix‑Later blocks deterministically:
  - `python3 scripts/tools/fill_master_validation_run_report.py --date <D> --state <STATE> --normalize-part5`
- Generated day synthesis stubs (Brain‑1 cross‑state summaries):
  - `python3 scripts/tools/create_day_synthesis_run_report.py --date <D>`
  - Outputs: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md`
- Added a 6‑day corpus synthesis pointer doc:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
- Added a pointer-only research pack for external review / ChatGPT Pro:
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-12-30_to_2026-01-04/README.md`

## 2026-01-03

### Brain-2: Control Center daily run report template + generator

- Added a fillable per-day Control Center report template (Brain-2, sharepack-aligned):
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`
- Added a generator that scaffolds one Control Center run report per results date `D` using only frozen sharepack artifacts:
  - `python3 scripts/tools/create_control_center_daily_run_report.py --date <D>`
  - Output: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
- Updated the generator + template to summarize not just HIT(decay), but also <=7 and <=14 diagnostic windows (variant-faithful + any-outcome).
- Generated Control Center run reports for the gold days:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__CONTROL_CENTER.md`
- Added an SSOT “Analysis Navigator” so day review follows a deterministic order (CC daily → day synthesis → state runs → sharepack evidence) and context resets can resume without re-explaining the workflow:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- Added a curated “research pack” entry point (pointer-only) so external reviews can load the corpus without repo spelunking or duplicating sharepacks:
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-06-21_to_2025-06-23/README.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-06-21_to_2025-06-23/MANIFEST.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-06-21_to_2025-06-23/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`

## 2026-01-01

### Run report progress tracking + day close (D=2025-06-21)

- Added a simple progress index so context resets don’t cause “where are we?” loops:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Closed out the last missing 2025-06-21 run reports (filled end-to-end, Parts A–5):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__SouthCarolina4.md`
- Fix-later (workflow hygiene): PuertoRico4 Digit Reduction “Combined” winner stamp appears inconsistent with Puerto Rico winners on `D=2025-06-21` (captured in the run report; do not treat as sharepack drift).

## 2025-12-31

### Sharepacks corpus audit (confidence + drift guard)

- Added a deterministic corpus audit that scans one or more frozen days and reports:
  - required artifacts present per state/tool,
  - day mapping + winners availability,
  - basic “freshness fingerprints” (so obvious cross-day copy mistakes are caught quickly).
- Command:
  - `python3 scripts/tools/audit_sharepacks_corpus.py --dates 2025-06-21 2025-06-22 2025-06-23`
- Output:
  - a timestamped markdown report under `reports/audit/sharepacks_audit_<timestamp>.md` (read-only; intended for humans).
- Notes:
  - WARN/SKIP can be expected for states/periods with no draws or missing winners lines (e.g., Puerto Rico on certain days); treat FAIL as “fix-now”.
- Files:
  - `scripts/tools/audit_sharepacks_corpus.py`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`

## 2025-12-13

### Digit Reduction: clarify “any vs final” semantics (SSOT = winner stamp JSON)

- Problem observed: `winner_hits.csv` was misread as if the “winner” must appear in `final_value`. In reality:
  - “Any” matches (e.g., `exact_any`, `vtrac_any`) are reflected in `winner_flags.csv` (`dr_win_*`) and in `*_winner_stamp.json` `counts`.
  - “Final” matches (e.g., `exact_final`, `vtrac_final`) are reflected in `winner_hits.csv` `final_*_match` columns and in `*_winner_stamp.json` `counts`.
  - It is valid for an example to have strong `*_any` counts but **zero** `*_final` counts.
- Impact: Part 2 DR summaries/validators can look “broken” unless the semantics are explicit.
- Fix: update DR summarizer + validator to use `*_winner_stamp.json` as the semantic anchor and to report totals correctly (no `final_value == winner` filtering).
- Files:
  - `scripts/tools/dr_sharepack_summary.py`
  - `scripts/tools/validate_dr_winners.py`

### VTRAC: guard against empty compact report

- Problem observed: `sharepacks/<DATE>/vtrac_compact_report.json` can exist but contain empty `states=[]` and `sections=[]`, which silently breaks aggregator-style reads.
- Fix: add a validator to flag “missing or empty compact report” early in the workflow.
- Files:
  - `scripts/tools/validate_vtrac_compact_report.py`

### Workflow contract clarity

- Clarify that `sharepacks/<DATE>/...` uses the **results/winners date (D)** and the history workbook is typically **D-1**.
- Add “Contract Truth Table” + “Known bumpy semantics” to the entry doc so future sessions don’t have to rediscover these rules.
- Files:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

### Part 3: Aux evidence dump + prompts

- Added a formal Part 3 section to the master template (Aux signals across Combined/Midday/Evening + convergence + expense/mode question).
- Added an Aux sharepack summarizer that snapshots draw CSVs into the sharepack and emits `summary.md`/`summary.json` for paste-ready evidence (no screenshots required).
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
  - `scripts/tools/aux_sharepack_summary.py`

### Drift guards: tables↔aux alignment (why sentinel checks exist)

- Problem observed: it is possible for **tables** (`data/outputs/tables/...`) and **aux draws** (`data/cleaned/draws/...`) to describe different “world snapshots” after workbook swaps/rebuilds. This can silently invalidate analysis runs.
- Fix: add a fast validator that compares “newest draws” in tables vs aux draws and fails fast on mismatch.
- Files:
  - `scripts/tools/validate_tables_aux_alignment.py`
- How it’s used (two modes):
  - **Live workspace guard** (mutable outputs): `python3 scripts/tools/validate_tables_aux_alignment.py --state <STATE>`
  - **Master Validation guard** (sharepack snapshots): `python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict`
- Why we default to “check a couple states” in preflight:
  - Preflight should be **fast enough that you actually run it**, so it uses sentinel states (CT/FL) to catch systemic drift.
  - This catches global “wrong workbook / stale tables / stale aux draws” problems, but it does **not** guarantee every state is healthy (state-specific issues can still exist).
  - Recommended escalation:
    - Quick: CT/FL sentinel checks (default).
    - Targeted: run alignment for the specific state you are analyzing that day.
    - Full sweep (optional): iterate all tracked states when debugging or before a large batch.

### Run report safety + Part 3 wiring

- Run report generator now includes Part 3 scaffolding and Aux sharepack pointers.
- It refuses to overwrite an existing filled run report unless `--force` is provided (prevents accidental loss of answers).
- Files:
  - `scripts/tools/create_master_validation_run_report.py`

### Blackapple robustness (Aux dependency)

- Fix: prevent a crash when draw streams contain `"000"` placeholders (e.g., missing values normalized by loaders) by allowing root-sum `0` in the internal root tracking map.
- File:
  - `modules/blackapple.py`

---

## 2025-12-17

### Part 4–5: add the “translation layer” + final summary to the master template

- Problem observed: after completing Parts 1–3, there was no canonical way to:
  - freeze a small “candidate universe” per draw (Midday/Evening),
  - map candidates to coverage modes (perm-only vs boxed vs VT-boxed vs VT-straight), and
  - end runs with a consistent “what matters” wrap-up.
- Fix: add **Part 4** (candidate universe + evidence vectors + coverage mapping + pack decision) and **Part 5** (summary + fix-now vs fix-later + next run) to the master template.
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

### Run report generator: scaffold Parts 4–5

- Fix: extend the run report generator to scaffold Part 4 + Part 5 so new sessions don’t have to manually add those sections.
- Files:
  - `scripts/tools/create_master_validation_run_report.py`

---

## 2025-12-20

### Brain‑2: export Control Center into sharepacks (drift-proof)

- Added a sharepack-aligned Control Center exporter so Brain‑2 artifacts are frozen alongside Brain‑1 under `sharepacks/<D>/...`.
- Command: `python3 scripts/tools/export_control_center_sharepack.py --date <D>`
- Outputs: `sharepacks/<D>/control_center/` (Blackapple, Due Doubles, VTRAC Repeat Watch, Profit Alerts A01–A12 + README/meta/report).
- Files:
  - `scripts/tools/export_control_center_sharepack.py`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`

---

## 2025-12-23

### Evaluation layer: leading-zero false negatives + correct Stable/Hot Zones semantics

- Problem: evaluation scripts were vulnerable to pandas dtype inference (e.g., `033 → 33`), creating false “missing winner” alarms in Stable + Hot Zones summaries/validators.
- Problem: `validate_stable_winners.py` was validating the wrong criterion (treating “no exact Stable hit” as “pipeline failure”).
- Fix: force string dtype for ID-like columns (Canonical/triad and winner-literal cols) + normalize Pick‑3 literals as 3-digit strings in sharepack summarizers/validators.
- Fix: Stable validator now matches the real contract:
  - validates winner-family presence via `winner_family_ids` + spotlight `family_id`
  - only requires exact-canonical rows when metrics indicates `exact_*`
  - prints `NOTE` for “no exact hit” (tool outcome) instead of failing
- Files:
  - `scripts/tools/stable_sharepack_summary.py`
  - `scripts/tools/validate_stable_winners.py`
  - `scripts/tools/hot_zones_sharepack_summary.py`
  - `scripts/tools/validate_hot_zones_winners.py`
  - `scripts/tools/build_winners_log.py`
  - `scripts/tools/dr_sharepack_summary.py` (tolerate missing winners overlays)

### Sharepack determinism: multi-day-safe freezer (winners hygiene)

- Problem: sharepack “winners” folders could accumulate multiple timestamped reruns copied from live outputs, undermining snapshot clarity.
- Fix: `freeze_sharepack_day.py` now copies only the newest `.html`/`.json` per winner artifact key (no deletions in live cache).
- Files:
  - `scripts/tools/freeze_sharepack_day.py`

### Docs: “Pipeline vs tool outcome” callout (prevents panic loops)

- Added explicit guidance that “tool miss” ≠ “pipeline broke”, plus a note about leading zeros / dtype inference.
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

### Sharepack evidence refresh (no reruns)

- Regenerated paste-ready `summary.md`/`summary.json` blocks using the updated scripts:
  - `sharepacks/2025-06-22/*/stable/*/summary.*` and `sharepacks/2025-06-22/*/hot_zones/*/summary.*`
  - Fixed straggler Stable/Hot Zones summaries for: `sharepacks/2025-06-21/SouthCarolina4/...` and `sharepacks/2025-06-21/Virginia4/...`

### Build-from-scratch gate: full day sharepacks/2025-06-23 (H=2025-06-22 → D=2025-06-23)

- Built a full-day frozen snapshot for `D=2025-06-23` using history workbook `H=2025-06-22`:
  - Brain‑1 frozen under `sharepacks/2025-06-23/<STATE>/...`
  - Aux snapshots generated (history‑aligned) and alignment validated (strict)
  - Brain‑2 Control Center export frozen under `sharepacks/2025-06-23/control_center/`
  - Run report scaffolds generated under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__*.md`
- Note: there was an older legacy/partial `sharepacks/2025-06-23` snapshot in repo history; it was replaced by the modern schema so `sharepacks/<D>/` remains the canonical “day folder”.

### VTRAC validation: use date-scoped winners lens (prevents empty compact reports)

- Updated the build-from-scratch quickstart to ensure `TOOLS/vtrac_validate.py` validates against:
  - `reports/stable/winners_by_date/<D>/<STATE>/`
- The legacy `data/outputs/winners/` cache can be stale and may yield empty/invalid `vtrac_compact_report.*` if used accidentally.

### Sharepack usability: freezer writes README.md if missing

- `scripts/tools/freeze_sharepack_day.py` now writes:
  - `sharepacks/<D>/README.md` (history/results mapping, contents)
  - `sharepacks/<D>/<STATE>/README.md` (what should be inside per state)

---

## 2025-12-24

### Sharepack summaries: add cross-tool comparability metrics (rank + magnitude)

- Problem observed: cross-tool comparisons were hard when summaries only included raw rank. Also, some “winner present” checks were overly literal (doubles like `330` vs canonical `033`).
- Fix: enhance sharepack summarizers to emit standardized “rank + magnitude” fields (names vary slightly by tool), e.g.:
  - `rows_total`, `winner_best_rank`, `winner_rank_fraction`
  - `top_score_*`, `winner_score_*`, `winner_score_ratio_to_top`, `winner_score_delta_from_top`
- Files:
  - `scripts/tools/stable_sharepack_summary.py`
  - `scripts/tools/dr_sharepack_summary.py`
  - `scripts/tools/hot_zones_sharepack_summary.py`
  - `scripts/tools/vtrac_sharepack_summary.py`

### Digit Reduction: canonical/permutation-aware winner presence in top candidates

- Fix: treat the winner as present in DR top candidates if **any permutation** of the canonical triad is present (prevents false negatives for doubles like `330`).
- File:
  - `scripts/tools/dr_sharepack_summary.py`

### Digit Reduction validation: results-aware missing-period handling

- Problem observed: some states/days can have only one winner in `data/results/<D>.txt` (e.g., Midday blank but Evening present). In that case, strict Midday+Evening stamp expectations can produce false failures.
- Fix: `validate_dr_winners.py` now:
  - skips validating periods with no winner in the results file, and
  - allows a single-winner day to be stored under the other period bucket (prints `NOTE`) while still validating stamp↔flags↔hits consistency.
- File:
  - `scripts/tools/validate_dr_winners.py`

### Hot Zones: winner-map semantics clarity (top-20 snapshot, not exhaustive)

- Fix: Hot Zones sharepack summary now records winner-map scope (`top20+guard_hits`) and treats “not in winner_map” as a note (often expected) rather than a coverage gap.
- File:
  - `scripts/tools/hot_zones_sharepack_summary.py`

### VTRAC: winner index placement included in summary JSON

- Fix: VTRAC sharepack summary JSON now includes a small winners digest + winner index placement metrics (rank fraction + score-vs-top ratio/delta) so templates don’t require raw winners JSON.
- File:
  - `scripts/tools/vtrac_sharepack_summary.py`

### Control Center meta: parse history date from both workbook name styles

- Fix: the Control Center sharepack exporter now parses `Pick3StatsC4_YYYY-MM-DD.xlsm` and `Pick3StatsC4_YYYY_MM_DD.xlsm` so `history_date (D-1)` is populated consistently.
- File:
  - `scripts/tools/export_control_center_sharepack.py`

### Sharepack day README: fill missing Inputs sections

- Fix: `sharepacks/2025-06-21/README.md` and `sharepacks/2025-06-23/README.md` now include Inputs (history workbook + results file) and consistent Notes.
- Files:
  - `sharepacks/2025-06-21/README.md`
  - `sharepacks/2025-06-23/README.md`

### Part A helper: winners JSON digest script

- Added a helper to generate a small Markdown digest from winners JSON (avoids pasting thousands of lines into chat).
- File:
  - `scripts/tools/winners_json_digest.py`

### Template + docs: comparability + digest pointers

- Updated template and SSOT docs to point to the digest script and to explicitly request rank+magnitude fields in per-tool evidence blocks.
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
  - `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`

---

## 2025-12-25

### Brain‑2: Profit Alerts (A01–A12) exported into sharepacks

- Added a sharepack-aligned Profit Alerts board (A01–A12) so Brain‑2 can be evaluated like Brain‑1 without relying on Streamlit UI state.
- Command: `python3 scripts/tools/export_control_center_sharepack.py --date <D>`
- Outputs:
  - `sharepacks/<D>/control_center/profit_alerts.csv`
  - `sharepacks/<D>/control_center/profit_alerts.md`
- Notes:
  - This is detectors + evidence (no wagering engine).
  - Inputs are frozen sharepack artifacts (Stable/DR/Hot Zones/Aux + results file for evaluation).
- Files:
  - `scripts/tools/export_control_center_sharepack.py`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`

---

## 2025-12-26

### Profit Alerts: windowed evaluation harness + charter

- Added SSOT evaluation semantics (variants, draw-steps, decay windows, censored handling):
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Added a deterministic evaluator that grades Profit Alerts against `data/results/*.txt` timelines (primary = hit within per-row `DecayDraws`, secondary = 7/14 draw-steps):
  - Command: `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`
  - Outputs:
    - `sharepacks/<D>/control_center/profit_alerts_eval.md`
    - `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- Tightened Profit Alerts candidate validity (Pick‑3 only): filter out Stable rows where `Canonical` or `orders_modal_value` are not 3-digit (prevents impossible 4-digit candidates in A05/A12 exports):
  - `scripts/tools/export_control_center_sharepack.py`
- Control Center sharepack README now lists the optional evaluation artifacts + command:
  - `sharepacks/<D>/control_center/README.md` (generated by `scripts/tools/export_control_center_sharepack.py`)
- Updated SSOT pointers so zero-context sessions find the charter + evaluator quickly:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`
  - `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`

---

## 2025-12-27

### Profit Alerts: implied_set exports + merged episode scoring (SSOT)

- Added SSOT grading matrix clarifying “pipeline vs tool outcome” and per‑AID hit definitions (prevents the “0 hits” panic loop caused by grading the wrong object):
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- Exporter now emits explicit `ImpliedSet` (JSON list of 3‑digit strings) where required so evaluation never guesses clamp subsets:
  - A06/A07/A11 boxed perms (optional) and A12 STR8_4of8 clamp lane
  - A05/A09/A10 already export implied sets (STR8_8, STR8_3)
  - `scripts/tools/export_control_center_sharepack.py`
- Evaluator now grades set membership when `ImpliedSet` is present (primary), and writes a **merged play‑set** view so co‑firing alerts don’t double count spend:
  - `scripts/tools/evaluate_profit_alerts.py`
  - Outputs:
    - `sharepacks/<D>/control_center/profit_alerts_eval.csv`
    - `sharepacks/<D>/control_center/profit_alerts_eval.md`
    - `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`
- Updated SSOT pointers and docs to reference the grading matrix and merged output:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`

---

## 2026-04-22

### Analysis Arena: canonical replay guardrails and next-run boundary

- Added a replay-plan guardrail check so same-window replay cannot accidentally compare a one-window candidate cycle against the multi-window baseline cycle.
- Added wrapper command:
  - `python3 scripts/tools/run_analysis_arena_cycle.py replay-plan-guardrails --force`
- Hardened readiness discovery so superseded overlap windows and snapshot folders do not re-enter canonical readiness counts.
- Added an evidence boundary / next-run map that separates:
  - `true_fresh_confirmation`
  - `archived_window_replication`
  - `same_window_replay`
- Added a gold-day / window inventory reference so future sessions can see the canonical Pick3StatsC4 input ranges, results windows, decay tails, bonus sidecar coverage, and non-canonical exclusions in one place.
- Current boundary remains:
  - March Run2 canonical mix comparison is clean regression evidence.
  - Stage7B is ready for read-only confirmation replay.
  - Stage8 and downstream scoring / candidate / budget rewrite remain blocked until fresh confirmation.
- Files:
  - `scripts/tools/create_analysis_arena_replay_plan_guardrail_check.py`
  - `scripts/tools/create_analysis_arena_window_replay_readiness_report.py`
  - `scripts/tools/create_analysis_arena_fresh_window_readiness_report.py`
  - `scripts/tools/run_analysis_arena_cycle.py`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__EVIDENCE_BOUNDARY_AND_NEXT_RUN_MAP.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__GOLD_DAY_WINDOW_INVENTORY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
