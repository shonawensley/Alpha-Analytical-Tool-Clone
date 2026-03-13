# DR Super-Harness — Batch 2 Plan

Purpose: expand from the 5-case seed round to a broader pre-arena evidence base without jumping into an unstructured full-corpus review.

Batch 2 should raise the filled-case total from `5` to `11`. The goal is not raw volume. The goal is to confirm that the seed-round evidence classes remain stable across more states, windows, and winner shapes.

---

## Why a second targeted batch

The seed round already established that DR is not a single evidence type. It broke the tool into multiple recurring truth classes:

- `dr_trace_strength`
- `dr_lane_only_confidence`
- `dr_double_pressure`
- `dr_row_repeat_and_final_survival`
- `dr_empty_lens`

Before defining `DR Arena v1`, we want another bounded batch that:

- repeats each major class at least once more,
- adds stronger buried-but-present coverage,
- adds more doubles / mirror-double pressure,
- adds one more empty-lens sanity check,
- and checks whether the likely fourth-variable idea keeps appearing in the same kinds of cases.

---

## Batch 2 cases

### B2-A — NewYork4 / 2025-06-23 / Midday / 638

- Source class: buried-but-present
- Study queue / audit anchor:
  - buried-but-present list in `DR_V0__STUDY_QUEUE.md`
- Why it matters:
  - aligned on-disk winner artifacts (unlike the drifted `2026-01-05 / NY / Midday` sharepack)
  - strong buried-trace candidate from the June window
  - useful older-window counterpart to `NJ 028`
- Main question:
  - how often does DR contain a strong exact object while the caller surface still routes attention into the wrong motif family?

### B2-B — NewJersey4 / 2026-01-06 / Evening / 942

- Source class: buried-but-present with extreme lane evidence
- Study queue / audit anchor:
  - `DR_V0__AUDIT__CASES.md` Case 5
- Why it matters:
  - `vtrac_any=252/252`, `drop_vtrac_any=240`
  - ideal stress test for “family everywhere, literal nowhere useful”
  - strong candidate for `dr_lane_only_confidence` and `dr_competing_literal_pressure`
- Main question:
  - when the lane is overwhelmingly obvious, what is DR actually competing against at the literal level?

### B2-C — OntarioCanada4 / 2026-01-09 / Evening / 104

- Source class: buried-but-present with very strong trace support
- Study queue anchor:
  - top row in `DR_V0__STUDY_QUEUE.md`
- Why it matters:
  - `items_total=240`
  - `exact_any=204`
  - `vtrac_any=240`
  - complements the seed-round negative Ontario case (`ON 498`) with a strong positive Ontario case
- Main question:
  - does the same state show both empty-lens and rich buried-truth modes cleanly enough to justify distinct DR arena sub-surfaces?

### B2-D — Michigan4 / 2026-01-07 / Evening / 616

- Source class: doubles / mirror-double pressure
- Study queue anchor:
  - buried-but-present list in `DR_V0__STUDY_QUEUE.md`
- Why it matters:
  - compact double-rich case
  - likely to sharpen mirror-pair / repeated-value handling
  - useful comparison point against `FL 434`
- Main question:
  - how should DR distinguish direct double pressure from broader repeated-value clutter?

### B2-E — Pennsylvania4 / 2025-06-21 / Midday / 667

- Source class: doubles / mirror-double pressure with older gold-window coverage
- Study queue anchor:
  - buried-but-present list in `DR_V0__STUDY_QUEUE.md`
- Why it matters:
  - crosses into the June window instead of staying entirely in January
  - strong double/mirror-double candidate
  - useful for checking whether the same evidence classes travel across windows
- Main question:
  - do the seed-round DR classes remain coherent when we step back into the older corpus window?

### B2-F — NewYork4 / 2026-01-08 / Midday / 199

- Source class: empty-lens / negative control
- Study queue anchor:
  - empty-lens list in `DR_V0__STUDY_QUEUE.md`
- Why it matters:
  - second empty-lens case from a different state shape than `ON 498`
  - helps prevent over-crediting every mapped-box environment
  - useful pressure test for box-validity discussions
- Main question:
  - when DR sees nothing, is that because the mapped lens is genuinely cold, or because the current map/analyzer contract is still missing a recurring winner type?

---

## Coverage logic

After Batch 2, the expected behavior coverage is:

- buried-but-present / caller weak: `NJ 028`, `NY 080`, `NJ 942`, `ON 104`
- lane-only / VTRAC gateway: `FL 963`, `NJ 942`
- doubles / mirror-double pressure: `FL 434`, `MI 616`, `PA 667`
- row-repeat / final-survival: `NC 033`
- empty-lens / controls: `ON 498`, `NY 199`

This is enough to support a first serious `DR Arena v1` design pass without pretending we have exhausted the corpus.

---

## Batch 2 completion criteria

Batch 2 is complete when:

1. all 6 cases have filled super-harness docs,
2. a new findings note summarizes what remained stable vs what changed,
3. the DR evidence classes are either confirmed or revised,
4. we can state whether the next step is:
   - `DR Arena v1` schema design,
   - a small intermediate review pass,
   - or direct `V2`/`V3` design exploration.

---

## Guardrails

- No DR code edits during Batch 2 unless an obvious correctness defect appears.
- No mapped-box deletions during Batch 2.
- Hidden / weak cases should be preserved as negatives, not explained away.
- Aux / Control Center remain corroboration layers, not truth layers.
