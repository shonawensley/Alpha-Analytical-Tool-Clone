# Analysis Arena cycle — STAGE 6B SHADOW REPLAY SIMULATOR

## Metadata
- generated_at: `2026-04-20T06:08:48.655304+00:00`
- git_sha: `e3223c8193bae799907e266b291acaf0dbfdd7d6`
- runs2_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- output_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- force: `True`
- dry_run: `False`

## Command

- `python3 scripts/tools/create_analysis_arena_stage6b_shadow_replay_simulator.py --runs2-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --output-dir /home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS_2 --force`

## Guardrail

- Stage 6B is a read-only shadow replay simulator; it does not alter live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.
- Stage 6B converts the Stage 6A lane contract into scenario scorecards, support/restraint ablations, concentration audit, and guardrail compliance.
- Stage 6B output is evidence for Stage 6B readback only; it does not create deployable candidate lists or scoring weights.
