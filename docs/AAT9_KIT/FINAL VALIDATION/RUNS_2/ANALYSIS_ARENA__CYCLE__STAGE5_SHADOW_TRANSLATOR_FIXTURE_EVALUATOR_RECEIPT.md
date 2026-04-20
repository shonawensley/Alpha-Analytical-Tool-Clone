# Analysis Arena cycle — STAGE 5 SHADOW TRANSLATOR FIXTURE EVALUATOR

## Metadata
- generated_at: `2026-04-20T05:17:12.708316+00:00`
- git_sha: `b4e24348447f8740cea74185fbca335ea2e3633c`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- casebook_limit: `120`
- max_value_rows: `all`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage5_shadow_translator_fixture_evaluator.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --casebook-limit 120 --force`

## Guardrail

- Stage 5 is a read-only fixture-backed shadow translator evaluator; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Stage 5 evaluates Stage 4C lanes by state-day fixture behavior, sample completeness, support context, restraint pressure, and source A / source B / overlap ablations.
- Stage 5 output is evidence for future design review only; it does not create deployable candidate lists or scoring weights.
