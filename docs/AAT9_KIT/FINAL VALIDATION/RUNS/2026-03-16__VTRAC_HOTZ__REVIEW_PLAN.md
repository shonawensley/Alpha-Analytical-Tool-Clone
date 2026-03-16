# VTRAC + Hot Zones Review Plan

Date: `2026-03-16`

## Purpose

Run the last deep tool-level assessment for:

- `VTRAC Analyzer`
- `Hot Zones`

before the project moves into the aggregated analysis-arena phase.

These two tools should be reviewed together at the truth layer because they describe the same winner environment from different angles:

- `VTRAC Analyzer` = lane / family / straight semantics
- `Hot Zones` = pressure / location / survivorship semantics

## Main Question

What is the most valuable winner-related evidence each tool can still contribute to the analysis arena, and is any final bounded tool-local change still justified before freezing them?

## Shared Truth Layer

Primary truth source:

- winners HTML / winners JSON / overlays

Why:

- shows exact winner path
- shows VTRAC winner path
- shows cross-variant echoes
- shows hot/superhot and late-column behavior
- shows length/progression of pattern clusters

## Frozen Review Windows

Use the same gold-day windows that have already been useful elsewhere:

- `2025-06-21 -> 2025-06-23`
- `2025-12-30 -> 2026-01-04`
- `2026-01-05 -> 2026-01-09`

## Priority Anchor Cases

These are the best starting anchors because they already appear repeatedly in the validation materials:

### Hot Zones anchors

- `Connecticut4 494 / 858` — literal Set1 funnel preservation
- `Florida4 733` — VT family present but literal triad visibility issue
- `Pennsylvania4 014` — direct hit case
- `NewJersey4 089` — near-miss sensitivity case
- `Connecticut4 576`
- `Connecticut4 737`

### VTRAC anchors

- `Connecticut4 919 / 864`
- `Florida4 695`
- `Indiana4 138`
- `Michigan4 199`
- any lane-rescue examples where overlap stayed low but the HTML showed strong lane truth

### Shared bridge anchors

Use cases where both tools clearly touched the same neighborhood:

- `OntarioCanada4` Hot Zones + VTRAC reinforcement example
- `Florida4 695`
- `Connecticut4 494/858`

## Tool-Specific Questions

### VTRAC Analyzer

Ask:

- Is the correct VTRAC lane present?
- Is the lane semantically rich enough in the current bundle/compact outputs?
- Is overlap still suppressing the most valuable low-overlap lane truth?
- Are the strongest cues:
  - recency lane
  - VT-only lane
  - straight-lane quality
  - hot/superhot echoes
  - section profile
  actually making it into arena-ready outputs?

### Hot Zones

Ask:

- Is the pressure path clear in Set1 / col2 -> col1?
- Are hot/superhot survivors properly preserved?
- Are the strongest vertical and multi-row repeats visible in arena-friendly outputs?
- Is the tool preserving literal and VT-only lane distinctions clearly enough?
- Is anything still missing beyond a digest/contract pass?

## Gap Taxonomy

Classify each important miss as one of:

- `tool_gap`
- `arena_feed_gap`
- `conversion_gap`
- `no_action`

This is required before recommending any tool-local change.

## Deliverables

The review should produce:

1. a joint assessment memo
2. a joint arena-contract memo
3. if justified, one or two bounded final tool-local slices only
4. explicit freeze/handoff guidance for each tool

## Stop Condition

Stop tool-local work when:

- the remaining gap is narrow and not worth more broad tuning
- or the next likely lift belongs to the aggregated analysis arena

That is the intended finish state.
