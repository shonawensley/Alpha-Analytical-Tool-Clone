# DR Promotion Batch 2

Date: `2026-03-15`

## Change

Added a second bounded predictive-side DR promotion surface:

- `dr_vtrac_cluster_strength`

Location:
- [dr_arena.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/dr_arena.py)

Purpose:
- aggregate DR trace, lane, corridor, gateway, double, row-repeat, and fourth-variable evidence by `VTRAC index`
- test whether a richer cluster object can promote the eventual winner lane better than the simpler `dr_vtrac_lane_gateway` slice

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
- cluster: `22 / 244` (`9.0%`)

Holdout matched rows:
- trace: `8 / 110` (`7.3%`)
- corridor: `8 / 110` (`7.3%`)
- gateway: `9 / 110` (`8.2%`)
- cluster: `9 / 110` (`8.2%`)

### Top-5 winner VTRAC rank

Development matched rows:
- trace: `29 / 244` (`11.9%`)
- corridor: `30 / 244` (`12.3%`)
- gateway: `33 / 244` (`13.5%`)
- cluster: `36 / 244` (`14.8%`)

Holdout matched rows:
- trace: `11 / 110` (`10.0%`)
- corridor: `11 / 110` (`10.0%`)
- gateway: `11 / 110` (`10.0%`)
- cluster: `13 / 110` (`11.8%`)

### Coverage of identifiable winner-lane ranks

Development matched rows with an identifiable winner-lane rank:
- trace: `46`
- corridor: `46`
- gateway: `51`
- cluster: `55`

Holdout matched rows with an identifiable winner-lane rank:
- trace: `17`
- corridor: `17`
- gateway: `19`
- cluster: `21`

### Unique lifts beyond trace / corridor / gateway

Cluster gave new `top-3` VTRAC captures on development rows where the other promotion surfaces did not:
- `2025-06-21 / Indiana4 / Midday / 565`
- `2025-06-23 / NewJersey4 / Midday / 106`

Cluster gave new `top-5` VTRAC captures on holdout rows where the other promotion surfaces did not:
- `2026-01-07 / Pennsylvania4 / Midday / 060`
- `2026-01-09 / Florida4 / Midday / 860`

## Interpretation

`dr_vtrac_cluster_strength` is a **keeper**.

Compared with `dr_vtrac_lane_gateway`, it:
- improves development `top-3` winner-lane promotion
- improves development and holdout `top-5` winner-lane promotion
- increases the number of matched rows where the winner lane is rankable at all

But it still does **not** close the main gap.

The gold-day audits still show:
- DR sees the right eventual winner lane often
- the promotion surfaces only rescue a small fraction of those rows into `top-3`
- the next bottleneck is still how to reward the right lane when assigned-box signal and corridor evidence are already structurally strong

## Recommended Next Step

Keep both:
- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`

Then do the next bounded batch around:

1. promotion weighting that explicitly rewards:
   - assigned-box winner-family signal
   - strong corridor currentness
   - cross-surface agreement between trace, corridor, gateway, and cluster
2. richer permutation-family support inside the same `VTRAC` neighborhood
3. re-run the same frozen dev + holdout windows before any consumer-side DR change
