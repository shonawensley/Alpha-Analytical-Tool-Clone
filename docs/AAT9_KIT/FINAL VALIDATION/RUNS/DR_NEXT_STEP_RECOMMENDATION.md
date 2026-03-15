# Digit Reduction - Next Step Recommendation

Context:
- 11 fully filled DR super-harness cases
- `DR Arena v1` implemented
- parity audit completed
- broader 25-case screened validation completed

Purpose: define the next best DR move without guessing.

---

## Decision

The next best move is **not**:

- DR weight retuning
- broad mapped-box deletion
- immediate Analyzer V3 rewrite
- automatic fourth-variable combo generation

The next best move is:

1. a small final deep-fill set from Batch 3,
2. then a narrow `DR Arena v1.1` calibration pass,
3. then the first consumer-side DR change.

---

## Why

### 1. `DR Arena v1` is already good enough to learn from

Parity result:
- `9/11` cases aligned well enough
- major positive surfaces are stable

That means the arena bridge is working.

### 2. The main weakness is now localized

The broader screen showed one clear issue:

- `dr_empty_lens` is too permissive

This is much better than the earlier state of DR, where the tool itself looked confused.

Now the problem is narrower:
- the arena needs better negative-control discrimination

### 3. We still do not have evidence that extraction is the problem

Nothing in the current parity + screen results forces:
- a DR extractor rewrite
- or immediate `V3`

The pressure is still mainly on:
- evidence interpretation
- sparse-control logic
- later consumer logic

---

## Recommended immediate sequence

### Step 1 - fill 4-5 Batch 3 cases deeply

Recommended set:

1. `2025-06-21 / Virginia4 / Midday / 473`
2. `2025-12-31 / Delaware4 / Evening / 337`
3. `2025-12-31 / NewYork4 / Evening / 116`
4. `2026-01-03 / Florida4 / Evening / 611`
5. `2025-06-23 / Indiana4 / Midday / 110`

Why these:
- one false-empty / buried-positive challenge
- one strong buried positive
- one false-active control
- one double-trace case with moderate pressure
- one clean older-window positive

That set is the best small final batch before an arena refinement pass.

### Step 2 - calibrate `DR Arena v1.1`

The first likely calibration target is:
- `dr_empty_lens`

Goal:
- distinguish:
  - `true empty / control`
  - `active but low-trust`
  - `positive buried trace`

Virginia `473` is now the anchor example for the second bucket. It should no longer be treated as a clean no-signal control.

This should be an arena-layer calibration, not a DR extractor rewrite.

### Step 3 - make the first DR consumer-side change

Only after the `v1.1` sparse-control calibration should we make the first real consumer change.

Most likely first consumer move:
- use `dr_competing_literal_pressure`
- plus `dr_lane_only_confidence`
- plus `dr_row_repeat_and_final_survival`

to improve how DR contributes to later decision layers,
without reviving DR top-candidates as a primary caller.

---

## V2 vs V3 read

Current recommendation:

- keep `Analyzer V2` as the extractor for now
- keep improving the arena/consumption layer first
- revisit `V3` only after:
  - the control logic is better,
  - and we know which evidence objects are still awkward or impossible to express through current V2 outputs

So the present sequence remains:

- `V2 extraction`
- `DR Arena v1`
- `DR Arena v1.1`
- first consumer changes
- then `V3` decision if still needed

---

## Bottom line

The overnight work clarified the DR path substantially.

We are no longer stuck asking:
- “is DR good or bad?”

We are now at:
- DR is useful,
- DR Arena v1 is useful,
- the next issue is specific,
- and the next move is controlled.

That is a strong place to be.
