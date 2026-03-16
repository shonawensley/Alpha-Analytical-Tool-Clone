# VTRAC + Hot Zones Arena Contract

Date: `2026-03-16`

## Purpose

Define what `VTRAC Analyzer` and `Hot Zones` should contribute to the analysis arena after their final review phase.

This is a tool-to-arena contract, not a play-card contract.

## Shared Principle

These tools should feed the arena as:

- structured evidence
- lane and pressure descriptors
- cross-variant context

They should **not** be forced to act like tiny direct-caller oracles.

## VTRAC Analyzer Contract

## Primary predictive-side ingest

Preferred evidence sources:

- enhanced analyzer bundle JSON
- compact report when present

Primary fields to preserve:

- ranked indices / lane summaries
- ranked straights
- per-straight reasons
- hot/superhot support
- recency / first-column pressure
- cross-section echo
- section profile / section strengths

## VTRAC arena objects to preserve

- `cross_variant_lane_strength`
- `right_column_lane_stability`
- `vt_only_lane_confidence`
- `straight_lane_quality`
- `lane_dominance`
- `section_lead_profile`
- `mask_drop_lane_reveal`
- `mirror_double_lane_support`

## VTRAC winners lens

Keep outside predictive mode:

- winners HTML / winners JSON / winner placement diagnostics

These remain the audit lens, not the predictive feed.

## VTRAC non-goal

Do not optimize VTRAC toward:

- “top-8 straight should directly win often”

That is not the right contract.

## Hot Zones Contract

## Primary predictive-side ingest

Preferred evidence sources:

- `*_hot_zones_top_lanes.csv`
- `*_hot_zones_meta.json`

Transitional compatibility source:

- predictive `*_hot_zones_winner_map.json`

Forensic only:

- `*_hot_zones_per_lane.csv`

## Hot Zones arena objects to preserve

- `late_tail_pressure_strength`
- `superhot_echo_strength`
- `vertical_repeat_strength`
- `rowtype_span_support`
- `precol1_funnel_strength`
- `col1_arrival_strength`
- `vt_only_lane_pressure`
- `repeat_3value_score`
- `consensus_column_signal`
- `set1_funnel_density`

## Hot Zones digest requirement

The most useful bounded finish for Hot Zones is likely:

- `hot_zones_summary_digest.csv`
- `hot_zones_ledger_all.csv`
- schema/manifest contract

This reduces the need to reopen heavy raw artifacts during arena review and validation.

## Hot Zones non-goal

Do not optimize Hot Zones toward:

- “top triads should behave like a small standalone straight oracle”

That is not the right contract.

## Shared Arena Interpretation

In the final arena:

- `VTRAC` should answer:
  - what lane / family / straight neighborhood is alive?
- `Hot Zones` should answer:
  - where is pressure surviving and tightening?

Together they describe:

- the active winner corridor
- its lane correctness
- its pressure / survivorship profile
- its cross-variant confirmation

## Freeze Criteria

Freeze each tool for this phase when:

- the arena contract is explicit
- the predictive ingest files are clear
- one bounded final validator/contract pass is complete
- no strong new reusable tool-local rule remains

At that point, any further major lift should be sought in the aggregated analysis arena, not by reopening the individual analyzer loops.
