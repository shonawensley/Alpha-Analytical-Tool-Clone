# AAT9 R-Consensus Harness Plan — Analysis Arena Branch

Date: `2026-03-24`

## Purpose

This document defines the prep-stage plan for the `R-Consensus` harness.

It exists so the branch can study the string-table consensus event in a
disciplined way before deciding:

- how it should be scored
- how it should be preserved in Analysis Arena
- whether it deserves a dedicated modular surface
- what later translation behavior, if any, is justified

## Core Thesis

`R-Consensus` is too valuable to leave as a thin registration flag, but too
specialized to spray into production combination logic before it is measured
properly.

So the correct order is:

1. inventory the event
2. reverse-engineer the event deeply
3. measure conversion behavior and decay
4. identify the real explanatory features
5. then decide how to integrate it

## Non-Negotiable Questions

The harness must answer:

1. How often does `R-Consensus` occur across gold days?
2. Is it mainly a doubles-trigger, a mini-table amplifier, or both?
3. Are patterns inside the event mini table measurably stronger than usual?
4. Are patterns above, below, and in hot-zone / near-column-1 areas also measurably stronger?
5. Does cross-variant reinforcement materially improve the event?
6. Do multiple same-day `R-Consensus` events make the signal stronger?
7. When the classic consensus doubles list converts, is there a clearer reason than “one of the keys happened to hit”?
8. Which Aux / Control Center signals tend to compound with conversion?
9. Is same-day use enough, or is the event materially decay-driven?
10. What should later be preserved, scored, or translated?

## Naming Lock

Use this naming consistently throughout the harness:

- `R-Consensus`
  - string-table tail-box collapse
- `XVAR-Cons`
  - positional cross-variant alignment
- `convergence`
  - broader generic agreement

Do not use bare `consensus` by itself in conclusions or schema names.

## Discovery Strategy

The initial event inventory should come from Stable-side evidence first.

Primary discovery surfaces:

- Stable score rows with:
  - `cons_full`
  - `cons_stub`
  - `cons_3v`
- Stable excerpts already embedded in profit-alert evidence packs
- winners HTML / JSON review when confirming the event visually

Recommended event key:

- `date/state/variant/set/draw/column/star_stripped_tail_value`

This lets the roster deduplicate cleanly.

## Review Inputs Per Event

Each event review should assemble:

- winners HTML
- winners JSON
- the local mini string table
- the stable score rows / excerpt for the event
- related aux / control-center sharepack outputs
- VTRAC reference material
- the filled worksheet template

## Required Analytical Passes

Each event gets two analytical passes.

### Pass 1

Fill the worksheet:

- lock the event
- extract local patterns
- build the consensus doubles list
- record same-day / decay behavior
- register surrounding and cross-variant structure

### Pass 2

Interpret the completed sheet:

- determine what actually explained conversion
- separate method-hit from structural amplification
- record the real integration lesson

## Cohort Scope

Use as many gold days / comprehensive review days as possible.

Because the event is relatively rare, breadth matters.

The harness should not stop at one window if additional reviewed gold days are
available in:

- filled templates
- winners outputs
- sharepacks
- packaged evidence corpora

## Required Measurements

Every event should measure:

- exact straight
- exact boxed
- VTRAC straight
- VTRAC boxed

And not only for the classic doubles shortlist.

Also measure:

- strongest local mini-table clusters
- strongest surrounding / hot-zone influenced clusters
- strongest related VTRAC lane or full VTRAC-boxed index if doubles/mirror pressure makes that meaningful

## Special Focus Areas

These are mandatory in the harness.

### Classic Doubles Method

Record the shortlist created from:

- consensus digit or digits
- three nearby key digits

Then measure it directly.

### Mini-Table Amplification

Study whether the mini string table containing the event has:

- stronger exact patterns
- stronger boxed families
- stronger VTRAC relations
- stronger persistence / progression

than a normal mini table.

### Surrounding Pressure

Study:

- the mini table above
- the mini table below
- hot-zone / near-column-1 boxes

to test the idea that consensus makes nearby patterns hotter or more pending.

### Cross-Variant Accumulation

Measure:

- survivor relations
- column `1–2` cluster relations
- family / lane echoes
- `XVAR-Cons` positional reinforcement

### Multiplicity

Record total same-day `R-Consensus` count across all variants and ask whether
multiple events are materially stronger than single events.

### Aux / Profit Context

Record:

- profit alerts
- due doubles
- positional signals
- pairs
- sums
- VTRAC index pressure
- Blackapple

This is required because conversion may be compounded, not isolated.

## Deliverables

Prep stage deliverables:

- this plan document
- the per-event worksheet template

Harness stage deliverables later:

- event roster CSV
- one filled worksheet per event
- one cohort rollup
- one naming-audit summary
- one final integration memo

## Likely Output Files Later

Recommended later outputs:

- `R_CONSENSUS_EVENT_ROSTER.csv`
- `R_CONSENSUS_EVENT__<date>__<state>__<eventid>.md`
- `R_CONSENSUS_EVENT__<date>__<state>__<eventid>.json`
- `R_CONSENSUS_HARNESS_ROLLUP.md`
- `R_CONSENSUS_HARNESS_ROLLUP.csv`
- `R_CONSENSUS_NAMING_AUDIT.md`

## Integration Boundary

This harness is prep for learning, not immediate production promotion.

Do not treat completion of the harness as automatic approval to:

- inject consensus combo logic into production
- rewrite Candidate Universe
- rewrite budgeting
- inflate board scoring without evidence

Instead the likely post-harness outcomes are:

- clearer naming
- richer upstream preservation
- better scoring features
- a future bounded translator or modular tool decision
