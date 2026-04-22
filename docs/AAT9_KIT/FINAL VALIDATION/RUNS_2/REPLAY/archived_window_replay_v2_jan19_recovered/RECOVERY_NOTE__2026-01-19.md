# Jan19 Recovery Note

## Verdict

The January 19, 2026 gap was recoverable. The missing blocker was the frozen truth sharepack at `sharepacks/2026-01-19`, not corrupted results data and not a systemic replay failure.

## What Was Rebuilt

- Rebuilt the predictive Jan19 probe from `Pick3StatsC4_2026-01-18.xlsm` into `sharepacks/_predictive_replay/archived_window_replay_v2_jan19_recovered/2026-01-19`.
- Regenerated Jan19 winners into `reports/stable/winners_by_date/2026-01-19`.
- Ran winner-aware Stable Pattern and Digit Reduction outputs for all 14 active states.
- Ran the Jan19 history/results validation log at `reports/stable/validation_logs/validation_2026-01-19.json`.
- Froze the recovered Jan19 truth package into `sharepacks/2026-01-19`.
- Added Aux summaries and control-center sharepack material for all 14 active states.

## Validation Checks

- `sharepacks/2026-01-19` has all 14 active states.
- Required Jan19 truth components are present: table CSVs, table JSON, winner files, Stable outputs, Digit Reduction outputs, Aux summaries, and control-center files.
- JSON validation found no parse errors and no non-finite values in the checked recovered package.
- Connecticut and Florida sequence checks in `validation_2026-01-19.json` passed with expected winners present.

## Recovered Window

The continuous recovered window is:

`docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2_jan19_recovered/WINDOW_2026-01-15_to_2026-01-22`

Canonical subfolders:

- `ANALYSIS_ARENA`
- `VALIDATION`
- `CONTROL_ARM`

Window-close completed after rebuilding the package in the standard layout. The performance ledger has 221 winner-event rows plus the CSV header. The count is expected from the source results: January 18 has 25 active winner events because Puerto Rico is absent in `data/results/2026-01-18.txt` and South Carolina only has an Evening value.

## Scratch Material

Non-canonical artifacts from the first wrong-layout attempt were preserved, not deleted:

- `_scratch_initial_parent_analysis_arena_20260422`
- `WINDOW_2026-01-15_to_2026-01-22/_scratch_flat_postrange_attempt_20260422`

Use the standard recovered window path above for future evaluation.
