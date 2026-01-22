# ChatGPT Pro — Deep Research Prompt (v0.2 Closeout: VTRAC Packs + Windowed Grading)

## Mission

Review the v0.2 closeout work that aligned the system with training semantics:
- the distinction between lane visibility vs closure vs straight hits,
- windowed grading (hit within N draw-slots; N=5),
- and the VTRAC boxed-member pack play-card strategies that produce a repeatable lift at B24/B36.

Deliver an evidence-linked recommendation for what to lock as v0.3 defaults and what to keep as research-only knobs (especially anything involving B12 conversion policies).

Important constraints:
- Do not recommend analyzer changes (Stable/DR/VTRAC/HZ) unless there is a clear artifact-contract violation.
- Treat predictive sharepacks as winners-free evidence; grading outputs live in RUNS.

## Read first (strict order)

1) Navigation + decisions:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

2) Evidence (windowed rollups, N=5):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2026-01-05_to_2026-01-09.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2026-01-05_to_2026-01-09.md`

3) Implementation surfaces (for semantics + diagnostics):
- `scripts/tools/create_play_card.py`
- `scripts/tools/grade_play_card.py`
- `scripts/tools/grade_play_card_windowed.py`
- `scripts/tools/create_predictive_portfolio_report.py`
- `scripts/tools/run_v0_3_cycle.py`

4) VTRAC definition reference (for pack meaning):
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
- `modules/vtrac_reference.py`

## Deliverables

1) **Confirm the semantics are correct**
- Are the metrics names and meanings consistent with the training framing?
  - `hit_any_inclusive` / `canon_hit_any_perm` / `box_hit` / `straight_hit`

2) **Default policy recommendation (v0.3 posture)**
- Should we keep the budget split?
  - B12: conservative (analysis-prefix / diagnostic)
  - B24/B36: conversion-friendly (VTRAC pack-first)

3) **B12 plan (bounded, testable)**
- Propose one or two conditional conversion policies for B12 that can be tested without widening the playset:
  - exact conditions to fire,
  - reserved lines,
  - acceptance criteria (primary + guardrails).

4) **Next two experiments**
- Two small, high-leverage experiments that can be run and graded via the existing harnesses without analyzer edits.

