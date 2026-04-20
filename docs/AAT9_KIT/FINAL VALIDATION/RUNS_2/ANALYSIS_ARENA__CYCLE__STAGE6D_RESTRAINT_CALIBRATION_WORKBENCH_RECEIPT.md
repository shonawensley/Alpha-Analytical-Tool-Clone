# Analysis Arena cycle — STAGE 6D RESTRAINT CALIBRATION WORKBENCH

## Metadata
- generated_at: `2026-04-20T06:44:59.283664+00:00`
- git_sha: `f4bd0f7530e5dce2aa17b5dc4bf2078813cebf86`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage6d_restraint_calibration_workbench.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --force`

## Guardrail

- Stage 6D is a read-only restraint calibration workbench; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Stage 6D converts Stage 6B restraint evidence into pressure buckets, high-pressure rescue review, and soft-penalty research hypotheses.
- Stage 6D output is penalty research only; hard vetoes and live candidate permissions remain forbidden.
