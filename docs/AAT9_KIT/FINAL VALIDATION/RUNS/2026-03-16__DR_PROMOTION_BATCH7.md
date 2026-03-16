# DR Promotion Batch 7

Date: `2026-03-16`

## Purpose

Test one bounded fusion layer after the assigned-box breakthrough from Batch 6.

The goal was not to replace:

- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`

The goal was to answer a narrower question:

- when assigned-box lane truth agrees with cluster/gateway, or when assigned-box is strongly alive while cluster/gateway stay dead, can one small predictive-side fusion surface improve visible winner-lane promotion without flattening the open arena?

## Change

New predictive-side surface in:

- [dr_arena.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/dr_arena.py)

New surface:

- `dr_vtrac_fusion_strength`

Inputs:

- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`
- bounded structural guards from `dr_structural_signals`

Two fusion regimes only:

1. `agreement`
   - assigned-box and cluster/gateway are both visibly alive on the same `VTRAC` lane
2. `rescue`
   - assigned-box is strong enough to matter
   - cluster/gateway are still dead
   - row / box / echo structure is strong enough that rescue is not just noise

Important:

- this remains predictive-side evidence only
- no winner-aware inputs are used
- no budget / pack / combo logic is touched
- assigned-box remains its own independent arena object

## Result

Frozen reruns on the same dev / holdout windows:

Development matched rows: `244`

- `cluster top3`: `23`
- `assigned-box top3`: `24`
- `fusion top3`: `25`
- `fusion top5`: `39`
- `fusion top8`: `57`
- `best-surface top3`: `46 / 245`
- `best-surface top5`: `66 / 245`

Holdout matched rows: `110`

- `cluster top3`: `9`
- `assigned-box top3`: `11`
- `fusion top3`: `8`
- `fusion top5`: `17`
- `fusion top8`: `28`
- `best-surface top3`: `25 / 138`
- `best-surface top5`: `35 / 138`

## What This Proved

This is a keeper, but a modest one.

What it does well:

- helps some visible-under-promoted rows where assigned-box and cluster/gateway agree
- helps some buried rows become more visibly rankable without inventing another generic promotion surface
- improves the combined `best-surface` view on the frozen benchmark

What it does **not** do:

- replace assigned-box as the main buried-lane discovery surface
- solve the whole promotion problem
- justify another broad round of DR-only scoring invention

## Rejected Variant

One stronger rescue version was tested during this batch.

It boosted some box-only rescues more aggressively, but it slightly weakened the broader `best-surface` benchmark.

So that version was rejected and removed.

The keeper is the first, smaller fusion pass only.

## Interpretation

The DR keeper stack is now:

- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`
- `dr_vtrac_fusion_strength`

That is a much stronger arena feed than the old DR path:

- visible lane surface
- richer cluster/corridor surface
- buried assigned-box surface
- bounded agreement/rescue fusion surface

## Next Step

Do **not** continue inventing generic DR surfaces from here.

The next high-value move is:

1. treat this 4-surface DR package as the keeper baseline
2. review remaining missed anchors against winners HTML / overlays
3. decide whether the next lift is still truly DR-local
4. if not, move toward the aggregated analysis-arena phase
