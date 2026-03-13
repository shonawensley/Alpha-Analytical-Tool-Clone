# DR Super-Harness - Batch 3 Plan

Purpose: expand the DR review from the 11 fully filled harness cases into a broader, behavior-balanced validation batch before any DR redesign decisions.

Batch 3 is intentionally larger than Batch 2, but still structured.

The goal is not “read everything.”
The goal is:

- more data than the seed/batch2 phase,
- still behavior-led,
- still useful for design,
- and large enough to support the first post-parity DR decision layer.

---

## Why Batch 3 exists

After:
- 11 filled DR harness cases
- `DR Arena v1` implementation
- and the first parity audit

the next question is no longer:
- “what should DR preserve?”

It is:
- “do those preserved evidence classes still hold up across a much larger inventory?”

That is what Batch 3 is for.

---

## Batch 3 target size

Recommended total evidence base before the next DR decision:

- `11` fully filled harness cases
- plus `14` screened validation cases
- for a total working inventory of `25` cases

That is large enough to:
- confirm recurring DR evidence classes,
- detect obvious weak surfaces,
- and avoid overfitting to a small January-only set.

---

## Batch 3 candidate set

### A. Buried-trace / lane-heavy positives

| Case | Why it belongs |
|---|---|
| `2025-12-31 / Delaware4 / Evening / 337` | strong buried-trace positive from a different window |
| `2026-01-07 / Delaware4 / Evening / 922` | lane-heavy January positive |
| `2025-06-23 / Indiana4 / Midday / 110` | older-window positive with strong exact trace |
| `2026-01-02 / SouthCarolina4 / Midday / 308` | buried-trace positive outside the existing state mix |
| `2025-06-23 / NewJersey4 / Midday / 106` | positive NJ case that helps compare against the stronger evening NJ traces |

### B. Doubles / mirror-double positives

| Case | Why it belongs |
|---|---|
| `2025-12-31 / Virginia4 / Midday / 686` | double-heavy positive in a different state family |
| `2026-01-02 / PuertoRico4 / Midday / 144` | compact double-positive with strong exact trace |
| `2025-06-23 / NewYork4 / Evening / 767` | repeated-value / mirror-double pressure case |
| `2026-01-03 / Florida4 / Evening / 611` | another January double-heavy case outside the first Florida pair |

### C. Empty-lens / negative controls

| Case | Why it belongs |
|---|---|
| `2025-06-21 / Virginia4 / Midday / 473` | older-window control with very low DR activity |
| `2025-06-22 / OntarioCanada4 / Evening / 616` | second Ontario control to compare against `ON 498` |
| `2025-12-31 / NewYork4 / Evening / 116` | New York control to compare against the positive NY buried-trace cases |
| `2026-01-02 / Indiana4 / Evening / 359` | another empty control from a different state shape |
| `2026-01-05 / NewJersey4 / Evening / 694` | NJ control to challenge the otherwise strong NJ-positive story |

---

## What Batch 3 should answer

1. Does `dr_trace_strength` stay useful across more states and older windows?
2. Does `dr_lane_only_confidence` hold up outside the strongest seed cases?
3. Does `dr_competing_literal_pressure` keep explaining why DR is often close but caller-wrong?
4. Do doubles / mirror-double cases keep reinforcing `dr_double_pressure` as a real regime?
5. Does `dr_empty_lens` remain the weakest arena surface once we pressure it on more controls?
6. Are the first 11 cases enough to trust the current arena schema, or does a bigger batch expose missing evidence classes?

---

## Batch 3 method

This is not a full deep-fill pass for all 14 cases.

The Batch 3 method is:

1. run `DR Arena v1` against the selected cases,
2. compare the arena surfaces against:
   - corpus metrics,
   - winner stamps/flags,
   - known case labels,
3. record a lighter-weight screen for each case,
4. only then choose which Batch 3 cases deserve a full manual harness fill.

This keeps the overnight batch efficient while still evidence-led.

---

## Desired outcome

By the end of Batch 3, we should be able to say with confidence:

- whether the current DR arena schema is basically correct,
- whether `dr_empty_lens` needs a v1.1 recalibration,
- whether more full harness fills are still needed before consumer changes,
- and whether the next move is:
  - DR arena v1.1 calibration,
  - first DR consumer change,
  - or rising pressure toward a future `Analyzer V3`.
