# Analysis Arena cycle — WINDOW REPLAY READINESS

## Metadata
- generated_at: `2026-04-21T05:57:09.879133+00:00`
- git_sha: `ca587a341a809f5cd0959c3199736e5a572997fd`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- explicit_windows: `0`
- history_root: `data/history`
- results_root: `data/results`
- bonus_results_root: `data/results_bonus`
- predictive_sharepacks_root: `sharepacks/_predictive`
- truth_sharepacks_root: `sharepacks`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_window_replay_readiness_report.py --runs2-root /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --history-root /home/ser/code/Alpha-Analytical-Tool-Clone/data/history --results-root /home/ser/code/Alpha-Analytical-Tool-Clone/data/results --bonus-results-root /home/ser/code/Alpha-Analytical-Tool-Clone/data/results_bonus --predictive-sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --truth-sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks --force`

## Guardrail

- Window replay readiness is a read-only inventory and baseline-manifest layer.
- It does not run a same-window replay, alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Same-window replay is restricted to bugfix/regression evidence; archived-window reuse is replication evidence only.
