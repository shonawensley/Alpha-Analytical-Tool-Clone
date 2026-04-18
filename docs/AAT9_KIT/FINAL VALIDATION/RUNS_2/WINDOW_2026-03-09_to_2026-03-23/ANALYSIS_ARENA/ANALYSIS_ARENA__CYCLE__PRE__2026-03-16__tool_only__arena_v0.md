# Analysis Arena cycle — PRE — D=2026-03-16

## Metadata
- generated_at: `2026-04-16T23:01:27.326899+00:00`
- git_sha: `7611cd4fe7de60d5a31e15c63f2a8201ae9e82c7`
- history_date(H): `2026-03-15`
- history_file: `- `
- results_date(D): `2026-03-16`
- sharepacks_root: `sharepacks/_predictive`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- board_name: `analysis_arena_day_review`
- top_n_stable: `10 `
- runs_subdir: `WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA`
- states: `ALL`
- force: `True`
- dry_run: `False`

## Operating Picture
- Primary runtime branch: `Brain 1 -> Brain 2 -> shadow DPL`
- Downstream control arm retained: `Candidate Universe -> Play Card -> Portfolio`
- B12/B24/B36 remain comparative/baseline outputs, not the definition of arena truth.

## Expected Arena-Era Outputs
- board overlay: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- board scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__BOARD_SCOREBOARD__analysis_arena_day_review.md`
- shadow DPL: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__SHADOW_DECISION_POLICY__analysis_arena_day_review.md`
- board review bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md`
- translation sandbox manifest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md`
- state-local translation sandbox seeds: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.md`

## Commands

- `python3 scripts/tools/run_predictive_day.py --history-date 2026-03-15 --results-date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --force`
- `python3 scripts/tools/create_day_arena_board_review.py --date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --board-name analysis_arena_day_review --arena-top-items 12 --board-top-items 8 --out-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA --history-date 2026-03-15`
- `python3 scripts/tools/create_candidate_universe.py --date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --profile tool_only --top-n-dr 0 --top-n-stable 10 --experiment-tag arena_v0 --write-signals-bundle --write-evidence --force`
- `python3 scripts/tools/create_play_card.py --date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --write-md --force`
- `python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --profile tool_only --rank-by tool_first --prefer-experiment-tags arena_v0,,vtracpack_v1 --force`
- `python3 scripts/tools/create_translation_sandbox_seed.py --date 2026-03-16 --sharepacks-root /home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --board-name analysis_arena_day_review --runs-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA --overlay-json /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json --scoreboard-json /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__BOARD_SCOREBOARD__analysis_arena_day_review.json --decision-policy-json /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-16__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`
