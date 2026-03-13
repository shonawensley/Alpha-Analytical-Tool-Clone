# DR Super-Harness — Batch 2 Findings

Purpose: synthesize the broader pre-arena conclusions after expanding from the 5-case seed set to an 11-case targeted set.

Batch scope:
- Seed set (`5`)
- Batch 2 expansion (`6`)

Total filled cases: `11`

---

## What changed after Batch 2

The seed round was enough to prove that the template worked and that DR needed to be treated as multiple evidence classes instead of one caller surface.

Batch 2 did something more important:

- it confirmed those evidence classes across a wider mix of states and windows,
- it separated `lane-only truth` from `buried exact truth`,
- it confirmed `double-pressure` as a recurring DR strength,
- it confirmed `empty-lens` as a real category rather than a one-off anomaly,
- and it made `competing literal pressure` impossible to ignore as a first-class DR phenomenon.

The biggest new result is:

**DR is often not wrong about the environment.  
It is often wrong about which literal family should represent that environment.**

That is a different failure mode than “the tool saw nothing.”

---

## Case coverage summary

### Seed set (`5`)

- `NewJersey4 / 2026-01-09 / Evening / 028`
  - `trace strong / caller weak`
- `Florida4 / 2026-01-07 / Evening / 963`
  - `lane-only / VTRAC-gateway truth`
- `OntarioCanada4 / 2026-01-08 / Evening / 498`
  - `empty-lens / negative control`
- `Florida4 / 2026-01-07 / Midday / 434`
  - `doubles / repeated-value pressure`
- `NorthCarolina4 / 2026-01-02 / Midday / 033`
  - `row-repeat / final-survival truth`

### Batch 2 (`6`)

- `NewYork4 / 2025-06-23 / Midday / 638`
  - `buried exact truth + competing literal pressure`
- `NewJersey4 / 2026-01-06 / Evening / 942`
  - `lane-only truth + competing literal pressure`
- `OntarioCanada4 / 2026-01-09 / Evening / 104`
  - `buried exact truth + competing literal pressure`
- `Michigan4 / 2026-01-07 / Evening / 616`
  - `double pressure + final-survival truth`
- `Pennsylvania4 / 2025-06-21 / Midday / 667`
  - `double pressure + competing literal pressure`
- `NewYork4 / 2026-01-08 / Midday / 199`
  - `empty-lens / negative control`

---

## DR evidence classes now confirmed

These are no longer just seed-round ideas. They now look stable enough to formalize.

### 1. `dr_trace_strength`

Definition:
- DR has strong exact and/or VTRAC presence in the trace, even if the winner never becomes a top candidate.

Confirmed by:
- `NJ 028`
- `NY 638`
- `ON 104`
- `PA 667`

Interpretation:
- this is the “winner is in the DR world” class
- but the caller surface is too narrow or too easily distracted

### 2. `dr_lane_only_confidence`

Definition:
- the winner lane/family is extremely strong in VTRAC/family space even though exact literal support is weak or secondary.

Confirmed by:
- `FL 963`
- `NJ 942`

Interpretation:
- this is not a literal caller object
- this is a gateway / lane object that should feed the arena as such

### 3. `dr_competing_literal_pressure`

Definition:
- the winner lane/truth is alive,
- but a different compact repeated motif steals the caller surface.

Confirmed by:
- `NJ 028` (`992/922`)
- `NY 638` (`994/559/554/...`)
- `NJ 942` (`992/599`)
- `ON 104` (`552/501/559`)
- `PA 667` (`922/228/992`)

Interpretation:
- this is now one of the most important DR failure modes
- it explains why strong winner truth can coexist with bad top-candidate output

### 4. `dr_double_pressure`

Definition:
- repeated-value / double / mirror-double structure is one of DR’s strongest and most recurring positive regimes.

Confirmed by:
- `FL 434`
- `MI 616`
- `PA 667`

Interpretation:
- this aligns strongly with the competition observations and with the broader system behavior
- it should become a first-class DR arena surface

### 5. `dr_row_repeat_and_final_survival`

Definition:
- winner structure repeats downward through reduction rows and survives late into the trace/final rows.

Confirmed by:
- `NC 033`
- `MI 616`

Interpretation:
- this is one of the best DR-specific counterparts to the late-string / 3-digit-repeat logic from training

### 6. `dr_empty_lens`

Definition:
- DR does not meaningfully see the winner environment at all.

Confirmed by:
- `ON 498`
- `NY 199`

Interpretation:
- this is critically important because it keeps us honest
- not every active DR day is a useful predictive DR day

---

## The biggest cross-case conclusions

### A. DR is not failing in one way

The old project posture often treated DR as:
- “bad top candidates”

That is too simple.

The fuller picture is:
- sometimes DR is strong on trace and weak on caller
- sometimes DR is strong on lane only
- sometimes DR is strong on doubles/final-survival
- sometimes DR is empty

So the tool must be consumed through multiple evidence channels, not one rank list.

### B. Competing literal pressure is now a major design target

This is the biggest new conclusion from Batch 2.

Across multiple states and windows, DR often:
- contains the winner family strongly,
- but gets attracted to a different repeated-value literal family.

That means `DR Arena v1` cannot just preserve:
- “winner lane strength”

It also needs to preserve:
- “what rival family is stealing the caller surface?”

That is exactly what `dr_competing_literal_pressure` is for.

### C. Double-pressure is not just a side phenomenon

The deeper we go, the clearer it gets:
- doubles / mirror-doubles / repeated-value anchors are one of DR’s natural strengths
- and they line up with the larger competition and portfolio observations

This does **not** mean abandon singles.
It does mean DR should explicitly separate:
- doubles-strength truth
- from generic motif clutter

### D. Final-survival truth deserves its own surface

`MI 616` especially makes this very clear.

There are DR cases where the tool is not merely “kind of right.”
It is extremely right all the way into the final-survival trace.

If the system still misses those cases because top candidates are wrong, that is an output/consumption failure, not an extraction failure.

---

## What this means for `DR Arena v1`

After `11` cases, the first DR arena schema should preserve these sub-surfaces:

- `dr_trace_strength`
- `dr_lane_only_confidence`
- `dr_competing_literal_pressure`
- `dr_double_pressure`
- `dr_row_repeat_and_final_survival`
- `dr_empty_lens`

Those are now the best current candidates for structured DR evidence objects.

### First practical interpretation

`DR Arena v1` should not start by trying to produce top picks.

It should start by preserving:
- what DR sees strongly,
- what kind of truth it is,
- what it is competing against,
- and whether the day is positive, mixed, or empty from a DR perspective.

---

## What this means for V2 vs V3

After `11` cases, my current read is:

- still **do not** rush into DR code tuning
- still **do not** force the current caller surface to carry the whole job
- define `DR Arena v1` first
- then decide whether:
  - `Analyzer V2` can be extended cleanly to emit the right evidence objects
  - or whether the cleaner answer is `Analyzer V3`

Current leaning:
- `V2` still looks salvageable as an extractor
- the main redesign pressure is on:
  - outputs
  - evidence model
  - consumption

That means:
- probably `V2 extraction + DR Arena v1 first`
- then later decide whether the caller/aggregation layer becomes `V3`

---

## Box-validity posture after Batch 2

No broad box deletions yet.

Current state:
- Group 1 remains strongly justified as a harness lens
- `Set2 Draw1 Col3` remains disputed
- `Set1 Draw3 Col6` remains only a likely dead/N/A candidate

Batch 2 did not provide enough new evidence to justify map surgery yet.

---

## Recommended next step

The next optimal move is:

1. checkpoint Batch 2,
2. update the queue with the now-confirmed DR evidence classes,
3. design `DR Arena v1` from this 11-case base,
4. only then decide what the first DR code-facing change should be.

That is the cleanest path out of the “manual review” phase and into structured system redesign.
