# AAT9 Analysis Arena - March Run 2 Execution Prep

## 1. Verdict

- run_label: `march_2026_15day_replay_v2`
- evidence_tier: `same_window_replay`
- status: `blocked_until_prep_items_resolved`
- stage8_permission: `blocked`
- command_count: `59`
- command_csv: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_RUN2_EXECUTION_PREP.csv`

Operational read:

- March 09-23 is approved here only as a controlled same-window Run 2 replay target.
- This prep does not execute the replay.
- The actual run should be executed only after reviewing this plan and approving the command sequence.

## 2. Namespaces

- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_replay_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- candidate_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- candidate_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_sharepacks_root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- candidate_control_arm_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/CONTROL_ARM`

Important routing choice:

- The Run 2 window keeps the exact folder name `WINDOW_2026-03-09_to_2026-03-23` inside a nested replay root.
- This is intentional because Stage 3/4 fixture tools discover exact `WINDOW_<start>_to_<end>` names and would ignore a suffixed `__RUN2` folder.
- Stage 2B through Stage 7B run in the separate candidate replacement-cycle root so the candidate March window is compared inside the same multi-window context as the baseline.

Replacement-cycle window set:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`

## 3. Source Coverage

- history_missing: `none`
- results_missing: `none`
- tail_results_missing: `none`
- bonus_results_missing: `none`
- source_ready: `true`

## 4. Namespace Safety

- baseline_window_exists: `true`
- baseline_cycle_exists: `true`
- candidate_replay_root_exists: `true`
- candidate_cycle_root_exists: `true`
- candidate_window_root_exists: `true`
- candidate_sharepacks_root_exists: `true`
- candidate_control_arm_exists: `true`
- candidate_window_equals_baseline_window: `false`
- candidate_window_inside_baseline_window: `false`
- baseline_window_inside_candidate_window: `false`
- candidate_replay_path_has_run_label: `true`
- candidate_cycle_path_has_run_label: `true`
- candidate_window_path_has_run_label: `true`
- candidate_sharepacks_path_has_run_label: `true`
- candidate_sharepacks_is_production_predictive: `false`
- safe_to_create_candidate_namespace: `false`
- baseline_cycle_window_count: `4`
- replacement_cycle_window_count: `4`
- baseline_window_replaced_in_candidate_cycle: `true`
- planned_write_paths_inside_baseline_window: `[]`

## 5. Baseline Manifest

- markdown: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_RUN2_BASELINE_MANIFEST.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_RUN2_BASELINE_MANIFEST.json`
- csv: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_RUN2_BASELINE_MANIFEST.csv`
- created_by_first_preflight_command: `true`

## 6. Command Phases

- `preflight`: `3` commands
- `namespace_setup`: `1` commands
- `pre`: `1` commands
- `control_arm_grading`: `31` commands
- `post`: `1` commands
- `window_close`: `1` commands
- `post_run_audit`: `4` commands
- `canonical_replacement_cycle`: `1` commands
- `stage3_to_7b_canonical_cycle`: `15` commands
- `comparison`: `1` commands

The full executable command list is in the CSV. The major order is:

1. baseline manifest freeze, replay readiness, and pending comparison preflight
2. isolated pre-range into Run 2 sharepacks and Run 2 Analysis Arena folder
3. isolated control-arm grading into Run 2 `CONTROL_ARM`
4. isolated post-range into Run 2 `VALIDATION`
5. window close plus decay
6. post-run audit on the candidate window
7. canonical replacement-cycle Stage 2B using baseline peer windows plus Run 2
8. Stage 3 through Stage 7B regeneration inside the canonical replacement-cycle root
9. candidate-complete baseline-vs-Run-2 comparison using the replacement-cycle root

## 7. Blockers

- candidate window root already exists; archive or choose a new run label before execution
- candidate sharepacks root already exists; archive or choose a new run label before execution
- candidate replacement-cycle root already exists; archive or choose a new run label before execution

## 8. Guardrails

- Do not write into the preserved baseline window root.
- Do not write Run 2 predictive sharepacks into sharepacks/_predictive.
- Run 2 is same-window replay evidence only.
- Stage 2B through Stage 7B must run in the canonical replacement-cycle root, not the one-window replay root.
- Same-window replay cannot unlock Stage 8A or live scoring/candidate/budget changes.
- Review degraded or contradicted comparison rows before using Run 2 as development evidence.

## 9. Run-Ready Meaning

If blockers are `none`, the system is ready for a separately approved March Run 2 execution.
That still means same-window replay only. It can measure regression, reproducibility, traceability improvements, and changed Stage 6B-7B posture, but it cannot substitute for true fresh-window confirmation.
