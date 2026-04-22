# Analysis Arena cycle — WINDOW REPLAY EXECUTION PLAN

## Metadata
- generated_at: `2026-04-21T23:05:18.831114+00:00`
- git_sha: `40a4c6ede96112baf2e6e017f5ace8831661d14e`
- run_label: `march_2026_15day_replay_v2`
- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- baseline_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- candidate_sharepacks_root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_window_replay_execution_plan.py --run-label march_2026_15day_replay_v2 --baseline-window-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23 --baseline-cycle-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --runs2-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --candidate-sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive_replay/march_2026_15day_replay_v2 --force`

## Guardrail

- Window replay plan generation is read-only and does not run the March replay.
- The generated plan must keep Run 2 artifacts isolated from the preserved March baseline.
- Same-window replay cannot unlock Stage 8A or live scoring/budget changes.
