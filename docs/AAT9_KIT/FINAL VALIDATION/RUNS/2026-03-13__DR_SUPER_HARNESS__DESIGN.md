# 2026-03-13 — Digit Reduction Super Harness Design

Purpose: define a state-of-the-art, evidence-first harness for Digit Reduction (DR) that:

- recovers what DR is actually seeing in the strings,
- preserves that evidence in an arena-compatible structure,
- compares it against the current Analyzer V2 surface,
- and converts repeated findings into concrete tool / arena / policy / test work.

This is not a generic regression harness.
It is a DR-specific analysis-and-design harness.

Related:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_DEEP_EXAMPLE_REVIEW_ANALYSIS.md`
- `tasks/RECENT_DISCUSSION8.txt`
- `tasks/BRAINSTORM_DIGIT_SUPERHARNESS.txt`

---

## 1. Design Intent

The super harness exists because DR was historically strongest at:

- buried-but-present winner structure,
- VTRAC family / lane visibility,
- lingering long-string clusters,
- reduction-reveal behavior,
- repeats across boxes, sets, variants, and reduction rows,
- doubles / mirror-doubles / duplicate depth,
- and likely the "fourth variable" phenomenon.

But DR was repeatedly judged through the wrong surface:

- small top-candidate caller lists,
- compressed `best_pattern` outputs,
- and direct-pick expectations.

So this harness is designed to evaluate DR at the right layer:

- `truth` layer first,
- `arena/evidence` layer second,
- `action/integration` layer third.

---

## 2. What This Harness Is For

The harness should help answer:

- What does the winners lens show in the mapped DR areas?
- What was already visible before reduction?
- What became clearer because of reduction?
- Which repeats / VTRAC relations / doubles / extra digits were present?
- Which of those are already represented in Analyzer V2?
- Which are represented weakly or compressed incorrectly?
- Which are missing and deserve new arena fields, features, or later projection logic?

The harness should also help define:

- what DR should feed into the analysis arena,
- how DR evidence should be scored there,
- and which bounded closure ideas are justified later.

---

## 3. Non-Goals

This harness is not for:

- reviving DR as a blind top-3 straight caller,
- doing freeform narrative reviews with no structured outputs,
- letting Aux / Control Center replace the truth read,
- or immediately widening into large prediction packs.

DR remains:

- evidence-first by default,
- bounded-promotion only by experiment later,
- and arena-fed before policy-fed.

---

## 4. Core Principles

### 4.1 DR has two evidence channels

Every case must distinguish:

- `pre-reduction cluster evidence`
- `post-reduction reveal evidence`

This is the main discipline that prevents future circles.

### 4.2 Group boxes for clarity, not dogma

Use the two-group box model as a template lens:

- `Group 1`: upper long-string band, especially `7/6/5` style boxes across `Set3 -> Set2 -> Set1`
- `Group 2`: staircase / current-day ladder moving toward the most current long-string endpoint

This grouping is for structured reading and later quantification.
It is not immediate hard scoring logic.

### 4.3 Row 1 / Row 2 matter specially

The harness should explicitly rate:

- first reduction row influence,
- second reduction row influence,
- and how often those rows already isolate or strongly clarify the winner family.

### 4.4 Transit-digit reveal quality matters

The harness should explicitly record when:

- elimination of recent digits,
- especially as exact / VTRAC occurrence,
- leaves a pattern "only remaining in box" or nearly so.

### 4.5 Repeats must be split by type

Do not treat "repeat" as one vague thing.
The harness should distinguish:

- across-box repeats,
- across-set repeats,
- across-variant repeats,
- and row-downward repeats inside the reduction trace.

### 4.6 Doubles / mirror-doubles / duplicate depth are first-class

The harness must explicitly preserve:

- repeated-value anchors,
- mirror-double corridors,
- longer residual depth,
- and cases where extra copies imply stronger holding power.

### 4.7 Fourth-variable evidence starts as evidence, not expansion

The "4th variable" idea should first be captured as:

- a structured evidence object,
- not a direct combo generator.

Later bounded closure logic can be built from it.

---

## 5. The Three-Layer Harness Model

### Layer A — Truth Lens

This is the post-results ground truth layer.

Inputs:

- winners HTML / JSON
- winners overlay
- winner flags / hits
- mapped box view

Questions:

- Where was the winner family visible?
- Was it visible pre-reduction, post-reduction, or both?
- Which boxes and rows mattered most?
- Was the winner more exact, boxed, VTRAC-boxed, or VTRAC-straight in character?

### Layer B — DR Arena / Canvas

This is the open evidence layer.

It preserves:

- pre-reduction clusters,
- reveal events,
- repeats,
- VTRAC convergence,
- duplicate depth,
- fourth-variable candidates,
- frontier/currentness,
- decay / short-window behavior,
- and corroboration from Aux / Control Center.

This is not yet the prediction layer.

### Layer C — Action Ledger

This converts findings into system changes.

For every important phenomenon, the harness should decide whether it is:

- already represented well in V2,
- represented but compressed poorly,
- missing entirely,
- better as an arena field,
- better as a tool feature,
- better as a tracker/test,
- or better left observational for now.

---

## 6. Required Evidence Objects

The harness should build or emulate these DR evidence objects:

### 6.1 `dr_precluster_evidence`

What was already alive before reduction:

- literal cluster
- canonical / family / VTRAC identity
- source boxes
- source section(s)
- cluster depth / unique digits
- stability / structure notes

### 6.2 `dr_reduction_reveal`

What reduction clarified:

- own vs combined source
- exact vs VTRAC elimination mode
- all-occurrence vs as-is / one-at-a-time
- row index
- purity gain
- reveal quality
- "only remaining in box" / near-pure status

### 6.3 `dr_repeat_signal`

Repeat classes:

- across boxes
- across sets
- across variants
- down reduction rows

### 6.4 `dr_vtrac_gateway`

How the same family/lane appears:

- across variants,
- across methods,
- across boxes,
- and across reduction stages.

### 6.5 `dr_double_pressure`

Repeated-value emphasis:

- duplicate depth
- doubles / mirror-doubles
- repeated-value anchors
- pair-centered stability

### 6.6 `dr_fourth_variable_candidate`

Structured bounded-closure precursor:

- `core_anchor`
- `anchor_type`
- `core_vtrac_index`
- `lingering_digit`
- `lingering_vtrac_digit`
- `survival_count`
- `dup_depth`
- `currentness`
- `closure_neighborhood`
- `incremental_cost`
- `why_tags`

---

## 7. Template Requirements

The harness template must capture all of these in a reusable way:

- truth receipts
- grouped box reading
- pre-reduction evidence
- post-reduction reveals
- row-downward repeats
- cross-box / cross-set / cross-variant convergence
- fourth-variable candidates
- Aux / Control Center corroboration
- V2 salvage comparison
- box validity ledger
- short-window decay register
- integration decisions

The template should be structured, not freeform.

---

## 8. Box Validity Sub-Study

The harness must explicitly classify mapped boxes as:

- `core`
- `supportive`
- `experimental`
- `disputed`
- `dead_or_na`

Current guidance:

- `Set1 / Draw3 / Col6` may be treated as a likely `dead_or_na` candidate if confirmed empty/no-data.
- `Set2 / Draw1 / Col3` should be treated as `disputed`, not deleted casually, because the historical evidence ledger says it was previously added as an evidence-led residual hotspot.

This sub-study exists to stop repeated mapping anxiety and make window edits evidence-led.

---

## 9. Aux / Control Center Role

Aux and Control Center should be included, but only after the DR truth layer is read.

Use them as:

- corroboration,
- compound scoring support,
- badge pressure,
- due doubles / mirror-double support,
- positional overlap,
- VTRAC overlay support,
- and possible conversion helpers.

Do not let them define the truth read of the DR case.

---

## 10. Analyzer V2 Comparison Is Mandatory

Every harness case should answer:

- What did Analyzer V2 already capture?
- What did it capture but compress too aggressively?
- What did it capture in the wrong scoring shape?
- What did it miss?
- What should be salvaged?

This is necessary so the harness improves the real tool instead of becoming a parallel interpretation layer with no implementation path.

---

## 11. Decay / Short-Window Register

The harness should track notable DR indicators over:

- same draw
- next 2 draws
- next 3 days

using:

- exact straight
- exact boxed
- VTRAC boxed
- VTRAC straight

Purpose:

- capture the "2–5 draws" behavior you described,
- test whether some DR objects are short-window indicators rather than same-draw-only indicators,
- and keep future profitability logic evidence-based.

---

## 12. Recommended Execution Cadence

### Stage 1 — Build the template

Do this before broad testing.

### Stage 2 — Run a seed set

Recommended seed mix:

- 1 buried-but-present winner case
- 1 strong VTRAC-lane case
- 1 doubles / mirror-double case
- 1 noisy case
- 1 fourth-variable-looking case

### Stage 3 — Review and tighten the template

Make sure the template:

- captures the right evidence,
- is not too cluttered,
- and can compare with V2 cleanly.

### Stage 4 — Run a broader gold-window round

Then move to larger windows.

### Stage 5 — Convert findings into tool / arena changes

Prefer:

- batched edits after a coherent round,
- with live edits only for obvious correctness defects.

---

## 13. Immediate Deliverables

The first concrete deliverables should be:

1. this design spec
2. the fillable DR super-harness template
3. a small seed-set case list
4. queue entries for:
   - DR two-channel evidence rule
   - DR box validity ledger
   - DR super-harness workflow
   - DR Arena v1 schema split

---

## 14. Acceptance Criteria

The super-harness is successful if it:

- makes DR examples easier to understand, not harder,
- captures buried-but-present winner structure more cleanly than current top-candidate surfaces,
- identifies what V2 already does versus where it compresses too early,
- gives the fourth-variable idea a measurable home,
- resolves disputed box questions with evidence,
- and produces concrete, reusable integration decisions.

---

## 15. Bottom Line

The optimal way forward is not:

- retune DR caller weights first,
- or rebuild DR blindly.

The optimal way forward is:

- build a DR-specific super-harness,
- preserve DR evidence in a structured canvas,
- compare it against truth and V2,
- and use that to drive the next arena/tool changes deliberately.
