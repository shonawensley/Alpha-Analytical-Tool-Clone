# RUNS/V0_3 (Out-of-Sample Receipts + Grades)

Purpose: keep **new-day (v0.3) run receipts + grading outputs** separate from the historical v0 windows in `RUNS/`.

Notes:
- `sharepacks/` are gitignored frozen snapshots; `RUNS/` is the committed, reviewable evidence layer.
- Nothing in this folder should require editing analyzers; treat it as **measurement + workflow evidence**.

## What goes here
- v0.3 cadence receipts from `scripts/tools/run_v0_3_cycle.py` (PRE + POST).
- Windowed grading outputs (`*__PLAY_CARD_GRADE_WINDOWED__*.md/.csv`) for out-of-sample days/ranges.
- Any small “study queue” markdowns produced from out-of-sample runs (winners-linked, post-results only).

## Recommended usage
- For new days, prefer writing receipts into this folder via:
  - `python3 scripts/tools/run_v0_3_cycle.py pre ... --stable10 --runs-subdir V0_3`
  - `python3 scripts/tools/run_v0_3_cycle.py post ... --stable10 --runs-subdir V0_3`

Recommended policy (how to interpret “signal vs conversion” and which strategies to default to):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

If `--runs-subdir` is unavailable in your current branch, receipts will land in `RUNS/` root; do not manually move them unless you also update all links.
