# DR Promotion Batch 1

Date: `2026-03-15`

## Change

Added a new predictive-side DR surface:

- `dr_vtrac_lane_gateway`

Location:
- [dr_arena.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/dr_arena.py)

Purpose:
- aggregate existing DR family, corridor, pattern, and top-candidate evidence by `VTRAC index`
- test whether a bounded promotion-oriented surface can lift the eventual winner lane without changing extractor behavior

This was evaluated with:
- [audit_dr_gold_day.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/audit_dr_gold_day.py)
- [DEV gold-day audit](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__DEV__V1_1.md)
- [HOLDOUT gold-day audit](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__HOLDOUT__V1_1.md)

## Result

### Top-3 winner VTRAC rank

Development matched rows:
- trace: `20 / 244` (`8.2%`)
- corridor: `19 / 244` (`7.8%`)
- gateway: `19 / 244` (`7.8%`)

Holdout matched rows:
- trace: `8 / 110` (`7.3%`)
- corridor: `8 / 110` (`7.3%`)
- gateway: `9 / 110` (`8.2%`)

### Coverage of identifiable winner-lane ranks

Development matched rows with an identifiable winner-lane rank:
- trace: `46`
- corridor: `46`
- gateway: `51`

Holdout matched rows with an identifiable winner-lane rank:
- trace: `17`
- corridor: `17`
- gateway: `19`

### Top-5 winner VTRAC rank

Development:
- trace: `29`
- corridor: `30`
- gateway: `33`

Holdout:
- trace: `11`
- corridor: `11`
- gateway: `11`

## Interpretation

`dr_vtrac_lane_gateway` is **worth keeping**, but it does **not** solve the promotion problem by itself.

What it did:
- broadened measurable winner-lane visibility
- modestly improved holdout top-3 VTRAC alignment
- improved development-window top-5 VTRAC alignment

What it did **not** do:
- materially close the top-3 promotion gap
- convert the high `vtrac_any` rate into a strong top-surface lift

So this batch supports the broader gold-day audit conclusion:

- DR already sees the eventual winner lane often
- promotion / packaging is still the bottleneck
- a simple index-level aggregation is helpful, but not enough

## Recommended Next Step

Do **not** remove `dr_vtrac_lane_gateway`.

Instead, use it as a base for the next bounded batch:

1. richer standalone `VTRAC cluster` scoring
2. stronger promotion logic when:
   - assigned-box winner-family signal is historically strong
   - lane-only / corridor / gateway all point into the same index neighborhood
3. keep re-running the same dev + holdout gold-day audits after each batch
