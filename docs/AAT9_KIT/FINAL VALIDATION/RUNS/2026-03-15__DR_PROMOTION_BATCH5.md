# DR Promotion Batch 5

Date: `2026-03-15`

## Purpose

Apply the first winner-artifact-first scoring change from the promotion lab:

- do not treat all misses the same
- only target the `visible_under_promoted` regime
- leave truly buried rows for a later extraction/isolation pass

## Change

A bounded post-process was added to `dr_vtrac_cluster_strength` in:

- [dr_arena.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/dr_arena.py)

The new rule:

1. detects when the raw top cluster is a compact double-driven monopoly:
   - `support_class_count >= 5`
   - `member_family_count <= 1`
   - `member_pattern_count <= 1`
   - `double` support present
2. looks for structurally rich challenger lanes:
   - `support_class_count >= 4`
   - and one of:
     - currentness close to the top lane
     - multiple family members
     - multiple pattern members
3. lightly boosts those challengers and lightly penalizes the monopoly top lane

This is intentionally narrow.

It is **not** a hard-coded family penalty and does **not** blindly suppress `559/259/...` families.

## Why This Batch Was Chosen

The winner-promotion lab showed:

- `23` visible-under-promoted rows were structurally rich
- `10` visible-under-promoted rows were thin / fringe-supported
- `227` rows were still buried

So the best next move was to help the rich near-miss set first.

## Result

Frozen dev / holdout rerun:

- DEV matched rows `244`
  - cluster `top3`: `21 -> 23`
  - cluster `top5`: `34 -> 34`
  - cluster `top8`: `49 -> 50`
  - cluster `top10`: `54 -> 54`
  - cluster `top20`: `63 -> 63`
  - best-surface `top3`: `27 -> 29`

- HOLDOUT matched rows `110`
  - cluster `top3`: `9 -> 9`
  - cluster `top5`: `13 -> 14`
  - cluster `top8`: `21 -> 21`
  - cluster `top10`: `21 -> 21`
  - cluster `top20`: `23 -> 23`
  - best-surface `top5`: `13 -> 14`

Changed rows were small and interpretable:

Improvements included:
- `2026-01-07 / Florida4 / Midday / 434` (`8 -> 7`)
- `2026-01-09 / NewJersey4 / Evening / 028` (`7 -> 5`)
- `2026-01-06 / Michigan4 / Midday / 250` (`2 -> 1`)
- `2025-06-23 / NewJersey4 / Midday / 106` (`4 -> 3`)

Two already-good rows slipped slightly on dev:
- `2025-06-21 / SouthCarolina4 / Midday / 069` (`1 -> 2`)
- `2025-12-30 / Florida4 / Evening / 870` (`9 -> 10`)

That tradeoff was still acceptable because:
- holdout did not worsen
- the gains hit the intended regime
- the batch did not inflate deeper rank bands artificially

## Interpretation

This batch confirms:

1. the `visible_under_promoted` regime is real
2. a challenger-aware rebalance can lift some of those rows
3. the much larger `buried` regime is still a separate problem

So this is a keeper, but not the final answer.

## Next Step

The next bounded batch should focus on the buried regime:

- compare buried anchors vs visible-under-promoted anchors directly against winner artifacts
- identify what isolation trait is still missing before promotion can even matter
