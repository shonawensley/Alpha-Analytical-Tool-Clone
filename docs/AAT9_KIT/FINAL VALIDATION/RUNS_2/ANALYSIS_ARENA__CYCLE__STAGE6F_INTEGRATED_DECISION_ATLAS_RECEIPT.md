# Analysis Arena cycle — STAGE 6F INTEGRATED DECISION ATLAS

## Metadata
- generated_at: `2026-04-20T07:33:30.560407+00:00`
- git_sha: `df133258f6b4710b4c59f51f0e9422bde8002f19`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- casebook_limit_per_bucket: `8`
- max_ledger_rows: `0`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage6f_integrated_decision_atlas.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --casebook-limit-per-bucket 8 --force`

## Guardrail

- Stage 6F is a read-only integrated decision atlas; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Stage 6F combines Stage 6B readback, Stage 6C contracts, Stage 6D restraint calibration, Stage 6E support narrowing, and Stage 5 value-ledger examples.
- Stage 6F output is decision/casebook evidence only; it does not create deployable candidate lists or scoring weights.
