# Analysis Arena cycle — STAGE 4 FIXTURE REPLAY

## Metadata
- generated_at: `2026-04-22T00:16:37.712048+00:00`
- git_sha: `40a4c6ede96112baf2e6e017f5ace8831661d14e`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- max_replay_rows: `all`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage4_fixture_replay_harness.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2 --force`

## Guardrail

- Stage 4 is a read-only fixture replay/audit layer; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Source A / source B / overlap comparisons and shared-lineage flags are required before any future scoring rewrite.
