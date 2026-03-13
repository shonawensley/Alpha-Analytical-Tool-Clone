# 2026-03-13 - DR Super Harness Seed Findings - Round 2

Scope:

- `SEED-A` `2026-01-09 / NewJersey4 / Evening / 028`
- `SEED-B` `2026-01-07 / Florida4 / Midday / 434`
- `SEED-C` `2026-01-07 / Florida4 / Evening / 963`
- `SEED-D` `2026-01-02 / NorthCarolina4 / Midday / 033`
- `SEED-E` `2026-01-08 / OntarioCanada4 / Evening / 498`

Purpose: summarize the first full seed-set pass and identify the first DR-specific arena surfaces and likely tool directions justified by actual cases.

## 1. Seed Set Verdict

The seed round was worth doing before any DR edits.

It shows five distinct DR truth types:

1. `trace strong / caller weak`
   - `NewJersey4 028`

2. `lane-only / VTRAC-gateway truth`
   - `Florida4 963`

3. `doubles / repeated-value pressure`
   - `Florida4 434`

4. `row-repeat / final-survival truth`
   - `NorthCarolina4 033`

5. `empty-lens / negative control`
   - `OntarioCanada4 498`

That is exactly the kind of coverage the super-harness needed.

## 2. Strongest Overall Conclusion

**DR is not one thing.**

The seed set shows that DR truth must be split into at least five classes:

- buried trace truth
- VTRAC-lane truth
- repeated-value / doubles pressure
- row-downward / final-survival truth
- negative-control / empty-lens truth

That means a single compressed `best_pattern` caller surface is structurally the wrong interface.

## 3. What Looks Most Important For DR Arena v1

The seed round justifies these concrete arena sub-surfaces:

### 3.1 `dr_trace_strength`

For cases like `NewJersey4 028`.

Need:
- strong trace presence
- strong family/VTRAC presence
- caller under-promotion flag

### 3.2 `dr_lane_only_confidence`

For cases like `Florida4 963`.

Need:
- low or zero literal exact presence
- very high VTRAC-family presence
- low reduction dependence

### 3.3 `dr_double_pressure`

For cases like `Florida4 434`.

Need:
- repeated-value anchors
- duplicate depth
- mirror-double / same-family repeated pressure
- whether that pressure supports or competes with the winner core

### 3.4 `dr_row_repeat_and_final_survival`

For cases like `NorthCarolina4 033`.

Need:
- row-downward repetition
- final-survival counts
- guide-corridor vs final-winner distinction

### 3.5 `dr_empty_lens`

For cases like `OntarioCanada4 498`.

Need:
- no-signal classification
- grouped-box emptiness
- negative-control status

## 4. What The Seed Round Suggests About The 4th Variable

The seed round did not yet prove a fully operational fourth-variable rule.

But it did make the design direction clearer.

The most relevant cases were:

- `Florida4 434`
  - repeated-value pressure (`544/559`) clearly sits around the winner-support environment

- `NorthCarolina4 033`
  - a strong guide corridor (`922/992`) surrounds a winner that actually survives to final rows

So the current best design stance is:

- treat fourth-variable logic as an evidence object first
- do not turn it into combo generation yet
- but preserve:
  - core anchor
  - surrounding repeated-value or adjacent-family corridor
  - whether that corridor seems supportive or competing

## 5. Mapped-Box Conclusion So Far

After the first full seed set:

- Group 1 is clearly useful as a harness lens.
- It keeps producing the strongest early receipts.
- It is still too early to remove disputed boxes broadly.

Current practical stance still looks right:

- `Set1 Draw3 Col6` remains a likely dead/N/A candidate
- `Set2 Draw1 Col3` remains disputed and should still be settled by repeated harness evidence, not instinct

## 6. What Now Looks Most Salvageable From Analyzer V2

The seed round supports this salvage posture:

- keep extraction logic for now
- salvage these truths into the arena:
  - trace strength
  - lane-only truth
  - repeated-value pressure
  - final-survival truth
  - empty-lens truth

The seed round does **not** support reviving the current `top_candidates` surface as the main predictive object.

## 7. Most Likely First DR Changes After The Harness

These now look like the first justified next changes:

1. `DR Arena v1` schema
   - preserve the sub-surfaces above explicitly

2. explicit `guide corridor vs winner core` distinction
   - especially for cases like `NC 033`

3. explicit `supportive vs competing duplicate pressure`
   - especially for cases like `FL 434` and `FL 963`

4. explicit `empty-lens` handling
   - so DR silence becomes structured information rather than a quiet failure

What still does **not** look justified yet:

- broad weight retuning
- broad box deletion
- direct fourth-variable combo expansion

## 8. Recommended Immediate Next Step

The next optimal move is not to jump to DR code edits immediately.

The next move should be:

1. sync these seed findings into the queue
2. optionally fill one or two reserve cases if we want more proof around doubles or buried-family variants
3. then design `DR Arena v1` from the seed evidence classes

At this point, there is enough evidence to move from:
- generic DR skepticism
to
- a concrete arena-first DR redesign posture
