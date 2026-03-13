# DR Arena v1 — Integration Plan

Purpose: convert the super-harness learning phase into a concrete structured output target for Digit Reduction.

This is the bridge between:
- manual DR case review (`truth lens + canvas + action ledger`)
and
- future DR system outputs that preserve the same evidence types automatically.

This is **not** a caller-redesign document.
It is an **evidence contract** document.

---

## 1. Why DR Arena v1 exists

After the 11-case DR super-harness pass, the main conclusion is stable:

**Digit Reduction is strongest as a structured evidence tool, not as a narrow top-candidate caller.**

The current `analyzer_v2_top_candidates.csv` surface is too compressed to represent the actual DR truth space.

So the right next step is:
- do not tune caller weights yet
- do not jump straight to `Analyzer V3`
- first preserve the right DR evidence objects in a reusable structured form

That structured form is `DR Arena v1`.

---

## 2. Design goals

`DR Arena v1` should:

1. preserve what DR is actually good at
2. separate winner-support truth from competing literal pressure
3. preserve both pre-reduction and post-reduction evidence
4. stay predictive-side and winners-free
5. be inspectable in both JSON and compact markdown form
6. remain compatible with later:
   - arena comparison across tools
   - bounded projection logic
   - eventual `Analyzer V2` extension or `Analyzer V3` redesign

---

## 3. Inputs

The first version should consume existing DR outputs, not rewrite DR extraction first.

Primary predictive inputs:
- `analyzer_v2_per_item.csv`
- `analyzer_v2_top_candidates.csv`
- reducer score / metadata artifacts already written by DR

Primary truth-side learning references:
- winners HTML / JSON
- winner overlay
- winner stamp / flags / hits
- master validation reports

Important rule:
- truth-side winner artifacts are for **learning and validation**
- predictive-side DR Arena outputs must remain **winners-free**

---

## 4. Core DR Arena v1 evidence surfaces

These are the first evidence surfaces justified by the 11 reviewed cases.

### 4.1 `dr_trace_strength`

Question answered:
- how strongly is the candidate family/literal environment alive in the DR trace?

Preserve:
- variant
- section
- best boxes / rows
- exact-like support
- VTRAC-like support
- family support
- breadth across mapped boxes
- breadth across methods
- breadth across sets

Primary use:
- capture buried-but-present cases without forcing a literal top candidate

### 4.2 `dr_lane_only_confidence`

Question answered:
- is DR strongly right on the winner lane/VTRAC family even when exact literal support is weak?

Preserve:
- strongest family / VTRAC lane
- VTRAC breadth
- family-VTRAC breadth
- literal exact weakness
- lane confidence class

Primary use:
- represent cases like `FL 963` and `NJ 942`

### 4.3 `dr_competing_literal_pressure`

Question answered:
- what rival motif family is stealing the caller surface away from the stronger winner lane?

Preserve:
- strongest competing literal family
- best competing patterns
- where they repeat
- repeated-value depth
- whether they dominate current-band boxes
- whether they are stronger in literal terms than the actual lane truth

Primary use:
- explain the main DR failure mode seen across multiple positive cases

### 4.4 `dr_double_pressure`

Question answered:
- how strong is the repeated-value / double / mirror-double environment?

Preserve:
- repeated-value anchors
- mirror pair / mirror-double cues
- duplicate depth
- compact repeated families
- repeated boxes and row depth

Primary use:
- capture one of DR’s strongest recurring predictive regimes

### 4.5 `dr_row_repeat_and_final_survival`

Question answered:
- what repeats downward through rows and what survives late/final?

Preserve:
- row-downward repeat leaders
- late-row survivors
- final-survival count/strength
- method persistence
- whether final rows support exact / VTRAC / family

Primary use:
- encode the DR counterpart to the “late string / repeat / survivor” logic

### 4.6 `dr_empty_lens`

Question answered:
- is DR genuinely cold on the winner environment?

Preserve:
- zero-or-near-zero trace state
- what competing motifs were active instead
- whether the case is empty, weak, or wrong-world

Primary use:
- protect the system from over-crediting any active DR day

---

## 5. Supporting surfaces

These should also be preserved in v1.

### 5.1 `dr_precluster_ledger`

For each important mapped zone:
- strongest clusters before reduction
- boxes involved
- variants involved
- repeated-value notes
- family / VTRAC notes

### 5.2 `dr_reduction_reveal_ledger`

For each important reveal:
- method
- own vs combined vs transit
- before/after pattern
- purity gain
- “only remaining” / near-pure state

### 5.3 `dr_box_validity_ledger`

For each mapped box/window:
- current label:
  - core
  - supportive
  - experimental
  - disputed
  - likely dead/N/A
- supporting case count
- contradictory case count

This allows map cleanup later without ad hoc deletions.

### 5.4 `dr_fourth_variable_candidates`

This should exist in v1, but as an evidence panel rather than as pack generation.

Preserve:
- core anchor
- anchor type
- lingering extra digit
- lingering extra VTRAC digit
- support count
- repeated-value depth
- candidate closure neighborhood
- confidence

Important:
- v1 stores the evidence
- it does not yet generate broad closure packs from it

---

## 6. Recommended object shape

High-level top-level JSON structure:

```json
{
  "tool": "digit_reduction_arena",
  "version": "v1",
  "state": "ExampleState4",
  "date": "2026-01-09",
  "profile": "tool_only",
  "variants": {
    "Midday": {},
    "Evening": {},
    "Combined": {}
  },
  "box_validity_ledger": [],
  "notes": []
}
```

Per variant:

```json
{
  "trace_strength": [],
  "lane_only_confidence": [],
  "competing_literal_pressure": [],
  "double_pressure": [],
  "row_repeat_and_final_survival": [],
  "empty_lens": {},
  "precluster_ledger": [],
  "reduction_reveal_ledger": [],
  "fourth_variable_candidates": []
}
```

This is enough for v1.

---

## 7. What should **not** happen in v1

Do **not** do these yet:

- no DR weight retuning
- no broad mapped-box deletion
- no new DR candidate packs
- no automated fourth-variable combo expansion
- no attempt to replace `Analyzer V2` caller logic immediately

v1 is an evidence-preservation step, not a caller redesign step.

---

## 8. Implementation strategy

### Phase 1 — Build the arena writer

Add a DR arena builder that reads current predictive DR outputs and writes:
- `analysis/dr_arena__tool_only__<tag>.json`
- `analysis/dr_arena__tool_only__<tag>.md`

This should be analogous in spirit to the Stable arena path:
- additive
- default-off at first
- baseline preserved

### Phase 2 — Preserve the first 6 evidence surfaces

Minimum first target:
- `dr_trace_strength`
- `dr_lane_only_confidence`
- `dr_competing_literal_pressure`
- `dr_double_pressure`
- `dr_row_repeat_and_final_survival`
- `dr_empty_lens`

### Phase 3 — Add the supporting ledgers

Then add:
- precluster ledger
- reduction reveal ledger
- box validity ledger
- fourth-variable candidates

### Phase 4 — Validate against the 11 harness cases

The first validation of `DR Arena v1` should be:
- can it reproduce the evidence classes we already learned manually?
- can it distinguish:
  - positive trace cases
  - lane-only cases
  - double-pressure cases
  - final-survival cases
  - empty-lens cases

Only after that should we consider code-level analyzer redesign.

---

## 9. What this means for V2 vs V3

Current recommendation:

- treat `Analyzer V2` as a still-usable extractor
- treat `DR Arena v1` as the first proper structured consumption layer
- then decide if the cleanest future path is:
  - extend `V2` outputs, or
  - design `V3`

Current leaning:
- extraction still looks salvageable in `V2`
- the redesign pressure is mainly:
  - evidence model
  - output schema
  - consumption model

So the likely sequence is:
- `V2 extractor -> DR Arena v1 -> later V3 decision`

---

## 10. Immediate next step

The next optimal development task is:

**implement `DR Arena v1` as an additive predictive-side evidence writer using the 11-case harness findings as the schema source of truth.**

That is the cleanest way to turn the DR harness work into system progress without guessing or over-retuning.
