# 2026-03-13 - DR Super Harness Seed Findings - Round 1

Scope:

- `SEED-A` `2026-01-09 / NewJersey4 / Evening / 028`
- `SEED-C` `2026-01-07 / Florida4 / Evening / 963`
- `SEED-E` `2026-01-08 / OntarioCanada4 / Evening / 498`

Purpose: record the first durable findings from the initial DR super-harness passes before the rest of the seed set is filled.

## 1. Main Result

The first three cases already reinforce the same macro conclusion:

**DR is strongest as a structured evidence tool, not as a narrow literal caller surface.**

What changes from case to case is the *type* of truth it is preserving:

- `NewJersey4 028`: strong buried-but-present trace truth
- `Florida4 963`: pure VTRAC-gateway truth
- `OntarioCanada4 498`: empty-lens / negative-control truth

That is exactly why the super-harness structure is useful.

## 2. Findings That Now Look Durable

### 2.1 `trace strong, caller weak` is a real DR class

`NewJersey4 028` shows that:

- the winner can be deeply present in DR traces
- the winner family can be strongly present
- reduction can still support that family
- while the top-candidate surface remains too weak to use directly

This should become an explicit DR arena/evaluation class rather than an anecdote.

### 2.2 `lane-only confidence` is also a real DR class

`Florida4 963` shows a different case:

- `exact_any=0`
- `vtrac_any=90/90`

So DR can be "perfectly right on lane" while being literally wrong.

That means the arena needs an object that can preserve:

- lane truth
- without exact truth
- and without forcing that lane to compete directly with strong repeated-value literals.

### 2.3 `empty lens` must be preserved, not ignored

`OntarioCanada4 498` is just as important as the positive cases:

- `items_total=0`
- no exact / VTRAC / drop / family support

This means:

- DR sometimes truly does not see the evening winner environment
- or the current mapping does not reach it

Either way, this must be a first-class negative/control state in the harness and later arena.

### 2.4 Group 1 is immediately proving useful

In both positive seed cases so far, the strongest early truth showed up in:

- the upper long-string band
- especially `LS1` style rows

That does not prove the full box map yet, but it does support keeping the group-lens structure.

### 2.5 It is still too early to delete disputed boxes

Nothing from the first three seed cases justifies broad mapping removal.

Current posture still looks right:

- `Set1 Draw3 Col6` can remain a likely dead/N/A candidate
- `Set2 Draw1 Col3` should still be treated as disputed until more seed cases are filled

## 3. First Likely DR Arena Objects

The first three cases suggest these are worth preserving explicitly in `DR Arena v1`:

1. `dr_trace_strength`
- high when the winner family is broadly present in trace even if no final exact survives

2. `dr_lane_only_confidence`
- high when literal exact support is absent but VTRAC-lane support is dominant

3. `dr_competing_literal_pressure`
- when repeated-value caller objects dominate the rank surface but do not align to the winning lane

4. `dr_empty_lens`
- explicit no-signal / control classification

## 4. Immediate Tool/Arena Implications

These look justified already:

- add a DR tracker for `trace strong, caller weak`
- add a DR tracker for `lane-only truth`
- add a DR negative-control tracker for `empty lens`
- preserve `competing literal pressure` separately from winner-family truth

These do **not** look justified yet:

- broad mapped-box deletion
- weight retuning
- direct combo expansion from fourth-variable ideas

## 5. What The Next Two Seed Cases Should Clarify

The remaining high-priority seed cases now have a cleaner job:

- `Florida4 / Midday / 434`
  - pressure-test doubles / mirror-double handling

- `NorthCarolina4 / Midday / 033`
  - pressure-test row-downward repetition and the likely fourth-variable concept

If those two cases behave the way the corpus suggests, then the super-harness will already be yielding a coherent first batch of DR edits rather than a vague brainstorm.
