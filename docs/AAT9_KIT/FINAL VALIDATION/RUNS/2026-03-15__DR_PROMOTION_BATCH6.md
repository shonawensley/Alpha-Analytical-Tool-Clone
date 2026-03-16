# DR Promotion Batch 6

Date: `2026-03-15`

## Purpose

Attack the `buried` DR regime directly, without another generic reranker.

The winner-promotion lab showed that many rows were not merely under-promoted. They were completely absent from:

- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `candidate` preview

even though the winners HTML / JSON kept showing strong assigned-box corridor truth.

## Hypothesis

The buried winner lane is often present inside raw assigned-box strings, but not as the row's headline family/pattern.

So instead of asking DR families to recover that lane indirectly, add a new predictive-side surface that scores `VTRAC` lanes directly from:

- `box_id`
- bounded `final_value`

using 3-digit windows from the raw analyzer rows.

## Change

New arena surface in:

- [dr_arena.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/dr_arena.py)

New surface:

- `dr_assigned_box_vtrac_strength`

Behavior:

1. scan 3-digit windows inside raw assigned-box strings (`box_id`)
2. add bounded support from `final_value`
3. convert those windows to `VTRAC index`
4. score each lane using:
   - currentness
   - cluster/variant echo
   - box pair agree
   - box family density
   - row count / box count / column spread

Important:

- this is still predictive-side evidence only
- no winner-aware inputs are used
- no budget / pack / combo logic is touched

The audit was extended in:

- [audit_dr_gold_day.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/audit_dr_gold_day.py)

so the new surface is measured directly and included in `best_surface`.

## Result

Frozen reruns on the same dev / holdout windows:

Development rows: `245`

- `cluster top3`: `23`
- `assigned-box top3`: `24`
- `assigned-box top5`: `41`
- `assigned-box top10`: `84`
- `assigned-box top20`: `149`
- `best-surface top3`: `45`
- `best-surface top5`: `66`
- `best-surface top10`: `108`
- `best-surface top20`: `154`

Holdout rows: `138`

- `cluster top3`: `11`
- `assigned-box top3`: `15`
- `assigned-box top5`: `22`
- `assigned-box top10`: `44`
- `assigned-box top20`: `82`
- `best-surface top3`: `24`
- `best-surface top5`: `34`
- `best-surface top10`: `55`
- `best-surface top20`: `85`

## What This Proved

This is the first strong keeper for the buried regime.

It rescued many previously buried winner lanes into the visible band, including examples like:

- `2026-01-04 / Indiana4 / Midday / 813 / VT 23`
- `2025-12-31 / Virginia4 / Evening / 636 / VT 18`
- `2026-01-06 / Michigan4 / Midday / 618 / VT 18`
- `2025-06-23 / Ohio4 / Evening / 368 / VT 23`
- `2026-01-09 / Pennsylvania4 / Midday / 811 / VT 18`

That is exactly the kind of assigned-box winner-corridor recovery the gold-day lab was trying to find.

## Interpretation

The buried regime is not mainly:

- a generic compact-attractor problem
- or a missing candidate-preview problem

It is largely an:

- assigned-box lane-isolation problem

where the correct lane is living inside box windows, but not being preserved by the family-led DR surfaces.

## Next Step

Do **not** immediately force this surface into cluster fusion.

Next:

1. keep `dr_assigned_box_vtrac_strength` as its own arena surface
2. review rescued buried anchors against winners HTML / overlays
3. only then test one bounded fusion rule:
   - when assigned-box lane and cluster/gateway agree, promote that lane more strongly
   - but do not flatten the open arena into one merged score too early
