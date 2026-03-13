# 2026-03-13 - DR Super Harness Seed Set

Purpose: choose a small, balanced first-pass Digit Reduction (DR) seed set that exercises the new super-harness template before broader window work.

Related:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-13__DR_SUPER_HARNESS__DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_SUPER_HARNESS__TEMPLATE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md`

## Selection Rules

The seed set should cover the main DR behaviors we care about before any code edits:

1. buried-but-present exact/family case
2. strong VTRAC-gateway / lane-only case
3. doubles / mirror-double case
4. likely fourth-variable or lingering-extra-variable case
5. noisy / empty-lens control

The seed set is intentionally small so the template can be tightened quickly before scaling to a full window.

## Chosen Seed Set

| Label | Case | Primary behavior | Why it belongs in the seed set |
|---|---|---|---|
| `SEED-A` | `2026-01-09 / NewJersey4 / Evening / 028` | buried-but-present | Strong exact/VTRAC trace presence, but weak caller promotion. Good first proof that DR sees more than the top-candidate surface admits. |
| `SEED-B` | `2026-01-07 / Florida4 / Midday / 434` | exact trace + double-pressure style case | High exact/VTRAC trace presence, winner absent from top candidates, and the environment is rich in repeated-value / mirror-like behavior. |
| `SEED-C` | `2026-01-07 / Florida4 / Evening / 963` | VTRAC-gateway case | `exact_any=0` but `vtrac_any=90/90`. This is the clearest early example of DR being right on family/lane while wrong on literal caller output. |
| `SEED-D` | `2026-01-02 / NorthCarolina4 / Midday / 033` | likely fourth-variable / row-repeat case | Very strong trace presence, strong boxed VTRAC counts, and a useful case for testing downward repetition plus lingering extra-variable thinking. |
| `SEED-E` | `2026-01-08 / OntarioCanada4 / Evening / 498` | noisy / empty-lens control | `items_total=0`. This is the right control to keep the harness honest and to test the mapped-box validity ledger. |

## Reserve Cases

These are not first-pass fills, but they are strong follow-ups if the first five reveal obvious gaps.

| Case | Why it is reserved |
|---|---|
| `2026-01-05 / NewYork4 / Midday / 080` | Good doubles / mirror-double follow-up if `SEED-B` does not capture that regime strongly enough. |
| `2026-01-06 / NewJersey4 / Evening / 942` | Strong family-lane case where DR appears very VTRAC-aware but still fails caller promotion. |
| `2026-01-09 / OntarioCanada4 / Evening / 104` | Very strong buried-but-present case from the study queue if more high-volume active cases are needed. |

## First Fill Order

The first fill order is not random. It is designed to make the template prove distinct things quickly.

1. `SEED-A` `NewJersey4 / Evening / 028`
Reason:
- clearest buried-but-present case
- good first test of truth vs arena vs caller compression

2. `SEED-C` `Florida4 / Evening / 963`
Reason:
- cleanest VTRAC-gateway case
- forces the template to preserve family/lane truth without exact-literal dependence

3. `SEED-E` `OntarioCanada4 / Evening / 498`
Reason:
- needed early control
- prevents the harness from over-crediting every interesting-looking environment

4. `SEED-B` `Florida4 / Midday / 434`
Reason:
- good doubles / repeated-value pressure case after the first two template passes are stable

5. `SEED-D` `NorthCarolina4 / Midday / 033`
Reason:
- better tackled after the template is already holding row-repeat and fourth-variable notes cleanly

## Early Questions The Seed Set Should Answer

1. Is the split between pre-reduction evidence and post-reduction reveal evidence clear enough?
2. Are the grouped box reads (`Group 1` / `Group 2`) actually helping, or are they still too vague?
3. Is row-downward repetition worth its own ledger?
4. Do we need a stronger explicit ledger for doubles / mirror-doubles?
5. Can the fourth-variable panel stay evidence-first without becoming premature combo generation?
6. Do disputed or dead-box questions become clearer after just a few real cases?

## Immediate Output Goal

The seed round should produce:

- filled case docs for the first seed cases,
- a short running findings summary,
- and the first narrow list of DR-specific edits or arena fields that are truly justified.
