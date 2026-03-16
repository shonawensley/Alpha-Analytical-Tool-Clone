# Tool Review Method — Winner Artifact First

Date: `2026-03-16`

## Purpose

Lock in the review method that proved most effective during the late Digit Reduction phase and carry it forward into the remaining tool reviews.

This method is designed to avoid:

- blind weight-thrashing
- top-3 tunnel vision
- confusing tool-local gaps with arena or conversion gaps
- repeating broad optimization loops without a stable truth layer

## Core Principle

Use the richest **winner artifacts** first, then derive bounded scoring or export hypotheses from those artifacts, and only then validate them on frozen windows.

Short version:

1. inspect winner truth
2. inspect current tool output
3. classify the gap
4. derive one bounded hypothesis
5. rerun the same frozen benchmark
6. keep or reject

## Why This Worked Better

The earlier surface-first loop was useful for building structure, but it was too indirect once the remaining problem became:

- “the right lane/corridor exists, but the wrong visible surface still wins”

The winner-artifact-first method improved the work because it:

- used the winners HTML / JSON / overlays as a direct truth microscope
- separated “present but buried” from “actually absent”
- exposed different miss regimes instead of flattening everything into generic misses
- made top-band cutoffs (`top3`) less misleading by tracking broader rank bands too
- created clear keep/reject discipline for bounded changes

## Mandatory Inputs

For every serious tool review phase:

- frozen multi-window gold-day benchmark
- winner HTML / overlay / winner JSON or equivalent truth artifacts
- current predictive tool outputs
- current arena-facing extraction/consumption path

## Review Sequence

### 1. Truth first

Open the winner artifacts before reading the tool output.

Ask:

- what is the actual winner corridor / lane / pattern cluster?
- how does it migrate across `Set3 -> Set2 -> Set1`?
- what survives in late columns (`2 -> 1`)?
- what is cross-variant vs own-variant support?
- is the signal literal, family, VTRAC, VT-straight, masked, or mixed?

### 2. Tool second

Then inspect the tool output and ask:

- is the winner-related pattern present at all?
- is it directly visible or only implied?
- is it strong in the right place?
- what competing attractor/lane beat it?

### 3. Gap classification

Every miss should be classified before any tuning attempt:

- `tool_gap`
  - the important winner-related structure is not meaningfully extracted
- `arena_feed_gap`
  - the structure is extracted, but the arena-facing tool output does not preserve it well enough
- `conversion_gap`
  - the structure is preserved, but later selection/pack conversion would still miss
- `no_action`
  - the current tool already contributes enough; the remaining issue belongs elsewhere

### 4. Broader rank-band view

Never judge the tool only by `top3`.

Track at minimum:

- `top3`
- `top5`
- `top8`
- `top10`
- `top20`
- identifiable rank coverage
- score gap vs dominant rival

This prevents “evaluation narrowing” from being mistaken for a tool failure.

### 5. One bounded hypothesis at a time

Only make one bounded change per batch:

- one export/contract refinement
- one scoring adjustment
- one bounded rescue rule
- one bounded new evidence surface

Then rerun the same frozen windows.

### 6. Keep/reject discipline

Keep the change only if it:

- improves the agreed benchmark or the clarity of the arena feed
- generalizes across the frozen windows
- does not create a broader regression or schema mess

Otherwise reject it and document why.

## Stop Condition

Stop tool-local tuning when either is true:

1. the remaining gap is narrow and no longer worth broad tool work
2. the remaining lift is more likely to come from the aggregated analysis arena than the tool itself

That is the desired handoff point, not a failure condition.

## Current Applicability

This method is now the preferred review path for:

- `VTRAC Analyzer`
- `Hot Zones`
- any later remaining tool slices where the winners artifacts are richer than the current predictive surface

## Expected Deliverables Per Tool Review

- one review plan
- one artifact-first assessment
- one arena-feed contract
- zero or more bounded changes
- one freeze/handoff recommendation

## Non-Negotiables

- no broad rewrites first
- no “make top-8 perfect” goal
- no winner-dependent artifacts leaking into predictive mode
- no reopening a tool once the residual gap is clearly arena-level unless a narrow, reusable hypothesis exists
