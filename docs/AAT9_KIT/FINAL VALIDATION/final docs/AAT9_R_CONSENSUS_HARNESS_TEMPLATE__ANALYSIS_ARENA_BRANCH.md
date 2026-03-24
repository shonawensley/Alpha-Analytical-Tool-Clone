# AAT9 R-Consensus Harness Template — Analysis Arena Branch

Date: `2026-03-24`

## Purpose

This document is the worksheet template for deep reverse-engineer harness testing of
the `R-Consensus` string-table event.

Use it when reviewing any consensus event/example across gold days or other
high-value corpora.

This template is intentionally:

- research-first
- winner-truth-aware
- reverse-engineer oriented
- detailed enough to capture later integration value

This template is **not**:

- a production play policy
- a final combination-forming engine
- a budget or staking sheet

## Naming Lock

Do not use `consensus` loosely in this harness.

Use:

- `R-Consensus`
  - string-table tail-box event
  - Columns `1–2` only
  - `R2 / R4 / R6 / R8` share the same `1–2` digit tail
- `XVAR-Cons`
  - positional cross-variant alignment concept
- `convergence`
  - any broader generic agreement language

## Template Operating Rules

1. Lock the exact event first.
2. Read the full mini string table that contains the event, not only the consensus box.
3. Evaluate the surrounding structure:
   - mini table above
   - mini table below
   - hot zone boxes / near-column-1 influence
4. Measure both:
   - classic consensus doubles-method behavior
   - broader pattern-cluster amplification behavior
5. Use all four result criteria whenever possible:
   - exact straight
   - exact boxed
   - VTRAC straight
   - VTRAC boxed
6. Record same-day and decay behavior separately.
7. Perform a second-pass review after the worksheet is filled out.

---

## Worksheet

### 1. Event Identity

- Event ID:
- Results date:
- State:
- Draw under review:
- Gold-day / cohort label:
- Primary source files:
  - winners HTML:
  - winners JSON:
  - stable scores / excerpt:
  - aux / control-center sharepack:

### 2. R-Consensus Lock

- Variant:
- Section:
- Set:
- Draw:
- Column:
- Raw tail values:
  - `R2`:
  - `R4`:
  - `R6`:
  - `R8`:
- Star-stripped tail value:
- Tail length:
- Event class:
  - `single-digit`
  - `two-digit`
- Stable-style flags present:
  - `cons_full`:
  - `cons_3v`:
  - `cons_stub`:

### 3. Board Multiplicity

- Total R-Consensus count across all variants:
- Same-variant multiple consensus?:
- Same-day multiple consensus?:
- Cross-variant multiplicity?:
- Multiplicity notes:

### 4. Local Mini-Table Read

- Full mini string table identity:
- Strongest exact patterns in the mini table:
- Strongest boxed families / canonicals:
- Strongest VTRAC-related patterns:
- Persistence / progression clues:
- Permutation clues:
- Survivor / lingering clues:
- Does winner appear directly in the mini table?:
- Does winner VTRAC appear directly in the mini table?:

### 5. Nearby Key Extraction

- Nearby key digits:
  - key 1:
  - key 2:
  - key 3:
- How keys were selected:
- Nearby support VTRAC digits:
- Consensus doubles shortlist generated:
- Related mirror-double shortlist:

### 6. Consensus Method Evaluation

- Doubles shortlist exact-straight result:
- Doubles shortlist exact-boxed result:
- Doubles shortlist VTRAC-straight result:
- Doubles shortlist VTRAC-boxed result:
- Pair-right but 3rd-digit-missed?:
- Did the full related boxed VTRAC index look stronger than the narrow list?:

### 7. Local Pattern-Cluster Evaluation

- Highest-value exact cluster:
- Highest-value boxed family cluster:
- Highest-value VTRAC lane cluster:
- Double / mirror-double pressure:
- Hidden-family or hidden-terminal clues:
- Best direct pattern support for the eventual hit:

### 8. Surrounding Structure Read

- Mini table above:
  - carry-in clues:
- Mini table below:
  - carry-forward clues:
- Hot zone / near-column-1 influence:
- Repeating into nearby boxes:
- Cross-box persistence / progression:
- Nearby VTRAC relation:

### 9. Cross-Variant Read

- Survivor relation with other variants:
- Column `1–2` cluster relation with other variants:
- Family / lane echo with other variants:
- `XVAR-Cons` positional reinforcement:
- Cross-variant depth / accumulation notes:

### 10. Trace Analysis

- Winner trace through the consensus mini table:
- Winner-VTRAC trace through the consensus mini table:
- Best explanation of why the converting list or cluster worked:
  - `consensus digit only`
  - `consensus + nearby key`
  - `strong local pattern presence`
  - `strong local VTRAC presence`
  - `surrounding / hot-zone reinforcement`
  - `cross-variant reinforcement`
  - `compound mix`
- Notes:

### 11. Profit / Aux / Control Center Context

- Profit alerts fired:
- Consensus-adjacent alert relation:
- Due doubles relation:
- Positional / `XVAR-Cons` relation:
- Pairs relation:
- Sums relation:
- VTRAC index relation:
- Blackapple relation:
- Other Aux context:

### 12. Same-Day And Decay Window

- Variant where event was present:
- Draw where conversion happened:
- Same-day conversion?:
- Midday / Evening crossover?:
- `4-day` decay conversion window findings:

### 13. Event Verdict

- Primary function of this event:
  - `doubles trigger`
  - `pattern-cluster amplifier`
  - `VTRAC-index amplifier`
  - `cross-variant amplifier`
  - `carryover / decay signal`
  - `mixed`
- Strength class:
  - `high`
  - `medium`
  - `weak / noisy`

### 14. Integration Notes

- What should be preserved upstream:
- What should be scored later:
- What should remain research-only for now:
- Candidate later translator implication:

### 15. Second-Pass Review

- Second-pass interpretation:
- What was easy to miss on first pass:
- Strongest measurable feature:
- Strongest integration lesson:

## Per-Example Deliverables

Each reviewed example should produce:

- one filled worksheet in `md`
- one structured twin in `json` if generated later
- one supporting artifact bundle list
- one short final verdict paragraph
