# Analysis Arena cycle — WINDOW REPLAY COMPARE

## Metadata
- generated_at: `2026-04-22T00:21:06.728332+00:00`
- git_sha: `40a4c6ede96112baf2e6e017f5ace8831661d14e`
- run_label: `march_2026_15day_replay_v2`
- evidence_tier: `same_window_replay`
- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`
- baseline_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- candidate_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- require_candidate_complete: `True`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_window_replay_comparison_report.py --baseline-window-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23 --baseline-cycle-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --evidence-tier same_window_replay --run-label march_2026_15day_replay_v2 --candidate-window-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23 --candidate-cycle-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2 --require-candidate-complete --force`

## Guardrail

- Window replay comparison is read-only and does not run a window.
- Candidate roots are optional so this can preserve the baseline before a rerun exists.
- Same-window replay and archived-window replication cannot unlock Stage 8A or live scoring/budget changes.
