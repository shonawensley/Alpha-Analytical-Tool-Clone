# Analysis Arena cycle — WINDOW REPLAY COMPARE

## Metadata
- generated_at: `2026-04-21T07:18:42.353451+00:00`
- git_sha: `c25876e6acc21559a0b461232d307d0be50b35fe`
- run_label: `march_2026_15day_replay_v2_pending`
- evidence_tier: `same_window_replay`
- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_window_root: `not_provided`
- baseline_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- candidate_cycle_root: `not_provided`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_window_replay_comparison_report.py --baseline-window-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23 --baseline-cycle-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --evidence-tier same_window_replay --run-label march_2026_15day_replay_v2_pending --force`

## Guardrail

- Window replay comparison is read-only and does not run a window.
- Candidate roots are optional so this can preserve the baseline before a rerun exists.
- Same-window replay and archived-window replication cannot unlock Stage 8A or live scoring/budget changes.
