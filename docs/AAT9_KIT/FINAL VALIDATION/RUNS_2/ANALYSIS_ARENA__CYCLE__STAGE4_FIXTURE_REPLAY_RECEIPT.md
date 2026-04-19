# Analysis Arena cycle — STAGE 4 FIXTURE REPLAY

## Metadata
- generated_at: `2026-04-19T06:58:05.411003+00:00`
- git_sha: `c9a7bf25c102ada4efe2ebe126a1047e4310f181`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- max_replay_rows: `all`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage4_fixture_replay_harness.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --force`

## Guardrail

- Stage 4 is a read-only fixture replay/audit layer; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Source A / source B / overlap comparisons and shared-lineage flags are required before any future scoring rewrite.
