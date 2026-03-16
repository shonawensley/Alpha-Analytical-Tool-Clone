# DR Winner Promotion Lab Plan

Date: `2026-03-15`

## Purpose

Switch the current DR tuning loop from:

- aggregate-first promotion experiments

to:

- winner-artifact-first scoring engineering

without losing the frozen gold-day benchmark discipline.

## Why This Shift Is Needed

The frozen gold-day audits already established:

1. DR often sees the eventual winner `VTRAC` lane.
2. Winner-family / winner-`VTRAC` corridors are usually present in the assigned long-string boxes.
3. The remaining bottleneck is usually promotion:
   - the right lane is present
   - a compact attractor family still wins the visible surfaces

That means the best next hypotheses should come from direct winner-vs-attractor comparison against the winner HTML / JSON / overlay artifacts, then be tested back on the same frozen windows.

## Guardrail Against Artificial Narrowing

The audit instrumentation is widened to a `top20` view for:

- trace
- lane
- competing
- double
- gateway
- cluster

This is intentional and audit-only.

The live predictive writer is unchanged.

The lab must distinguish:

- not visible at all
- visible but under-promoted
- strong top-band promotion

So success is not judged by `top3` alone.

## Core Questions

For each anchor case:

1. What did the winning corridor have that the losing attractor lacked?
2. Was the winner lane:
   - cross-variant stronger?
   - broader across assigned boxes?
   - more stable across `R2/R4/R6/R8`?
   - more current?
   - more supported by row-repeat / fourth-variable / corridor structure?
3. Was the attractor only winning because it was:
   - denser
   - more compact
   - or easier for the current score geometry to reward?

## Anchor Set

Use 3 groups:

1. **Missed-present anchors**
   - winner lane present
   - `vtrac_any > 0`
   - assigned-box signal strong
   - still under-promoted or buried

2. **Success anchors**
   - winner lane promoted strongly enough to be practically useful

3. **Controls**
   - true-empty / active-low-trust cases
   - ensure any scoring change does not flood weak environments

Primary source docs:

- [2026-03-15__DR_PROMOTION_GAP_CASEPACK.md](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_PROMOTION_GAP_CASEPACK.md)
- [2026-03-15__DR_PROMOTION_GAP_ANCHORS.md](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_PROMOTION_GAP_ANCHORS.md)

## Comparison Traits

For each winner corridor vs attractor corridor comparison, score or note:

- assigned-box breadth
- consecutive-box progression
- cross-variant convergence (`Combined / Midday / Evening`)
- row stability / survival across `R2/R4/R6/R8`
- currentness / early activation
- family neighborhood saturation
- family asymmetry inside the corridor
- raw exposure count vs path-summary count
- row-repeat / final-survival support
- fourth-variable support
- compactness of the attractor
- cross-surface corroboration of the attractor
- score gap between top visible attractor and winner lane

## Primary Metrics

The lab should report all of these, not just `top3`:

- `gateway winner VTRAC rank <= 3/5/8/10/20`
- `cluster winner VTRAC rank <= 3/5/8/10/20`
- `best surface winner VTRAC rank <= 3/5/8/10/20`
- identifiable winner-lane coverage
- cluster/gateway score-gap when the winner lane is visible
- holdout stability

## Implementation Style

Keep batches bounded:

1. derive one hypothesis from winner-vs-attractor comparisons
2. implement one small scoring or suppression change
3. rerun the same frozen dev + holdout audits
4. keep only if it improves broader rank-band visibility without flooding controls

## Stop Condition

Stop the DR-local loop when:

- the next change does not improve the frozen benchmark enough
- or the remaining hypotheses become too case-specific

At that point, the next bottleneck should be treated as:

- arena synthesis
- or later conversion

not more blind DR-local tinkering.
