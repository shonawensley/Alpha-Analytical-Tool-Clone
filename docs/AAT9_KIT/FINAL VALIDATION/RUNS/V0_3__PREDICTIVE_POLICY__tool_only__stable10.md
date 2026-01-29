# v0.3 Predictive Policy (tool_only, stable10)

This document is the **single source of truth** for how we interpret and use the pipeline when you ask:

> “Are we actually predicting anything / why do the strict hit rates look bad?”

Core mental model:
- **Evidence (tools) ≠ Selection (what we would play).**
- Our current system shows **very strong lane/placement signal**, but conversion to a **budgeted selection** is where performance collapses.

This policy locks a default “coverage vs conversion” posture per budget so we stop oscillating between incompatible goals.

---

## Definitions (do not mix these up)

**Candidate Universe (CU)** (unbounded):
- “What the system *could* play.” Think: recall.
- The CU `__UNION__` row is the cleanest “could we have hit at all?” surface.

**Play Card** (budgeted selection):
- “What we *would* play” under a fixed spend (B12/B24/B36).
- This is the surface you should call “predictions”.

**Strict vs Lane vs Inclusive**
- `hit_any` / `straight_hit` / `box_hit`: strict winner membership in the budgeted list.
- `vtrac_index_hit`: we touched the winner’s **VTRAC index/group** (lane signal).
- `hit_any_inclusive`: budgeted card retained the winner **lane** (or better). This is the “coverage” contract.

**Pack correctness (the missing bridge)**
- `pack_correct`: chosen `vtrac_pack_index == winner_vtrac_index` (selection correctness).
- `pack_any_correct`: winner index is in `vtrac_pack_indices` (multi-pack correctness).

---

## Locked default posture (stable10)

### Candidate Universe
Lock: **Stable10** (stable recall posture).

Why: in the Jan gold window, CU union recall is strong:
- CU union `vtrac_index_hit`: **78.8%**
- CU union `hit_any`: **27.5%**
- CU union `straight_hit`: **20.7%**

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__tool_only__stable10.md`

If the stable10 rollups are missing, generate them:

```bash
python3 scripts/tools/rollup_candidate_universe_corpus.py --profile tool_only --experiment-tag stable10
python3 scripts/tools/rollup_play_card_corpus.py --profile tool_only --experiment-tag stable10
```

### Play Card defaults by budget

We do **not** try to optimize “strict hits” and “lane coverage” with the same budget posture.

**B24 = Coverage mode**
- Strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- Goal metric: maximize `hit_any_inclusive`
- Jan gold window (known winners, stable10): `hit_any_inclusive` **32.6%**

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__vtrac_pack_boxed_first_laneonly_presetB__stable10.md`
- Casebook (debug examples): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__vtrac_pack_boxed_first_laneonly_presetB__stable10__B24.md`

**B36 = Conversion mode**
- Strategy: `v0_2_default_multi_pack_packheavy_lane_diverse_filler`
- Goal metric: lift strict `hit_any` while keeping `pack_any_correct` measurable and improving
- Jan gold window (known winners, stable10):
  - `hit_any` **5.7%**
  - `hit_any_inclusive` **35.2%**
  - `pack_any_correct` **15.0%**

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_lane_diverse_filler__stable10.md`
- Casebook (debug examples): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_lane_diverse_filler__stable10__B36.md`

**Optional: strict-max baseline (research-only)**
- Strategy: `convergence_box_first`
- This maximizes strict hits, but sacrifices lane/pack semantics (everything is effectively “filler coverage”).

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__convergence_box_first__stable10.md`

---

## “If the tools are strong, why is prediction still bad?”

Because “tools strong” is usually **lane signal** (placement/coverage), not “winner in a tiny Top‑K list”.

The ladder reports make the break explicit:
- CU can often touch the winner lane (`vtrac_index_hit` high),
- but the Play Card frequently chooses the wrong pack index (`pack_correct` low),
- and strict hits stay low at fixed budget.

This is not an analyzer failure; it is a **conversion policy failure**.

---

## Spiral breaker (read order)

If you feel “we’re broken / nothing converts”, stop and do this in order:

0) Open the single scoreboard (side-by-side truth page):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10.md`
1) Results coverage (do we have enough future results to grade what we’re claiming?):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__RESULTS_HORIZON.md`
2) Always filter `winner_missing=1` (censored ≠ miss).
3) Separate semantics:
   - strict: `hit_any`, `box_hit`, `straight_hit`
   - lane: `vtrac_index_hit`
   - coverage: `hit_any_inclusive`
4) Check the bridge metrics:
   - `pack_correct` (single-pack selection correctness)
   - `pack_any_correct` (multi-pack correctness)
5) Check lane ranking vs selection (this ends “is it lane ranking or pack conversion?” arguments):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36.md`
6) Open the casebook buckets (concrete examples to debug policy, not analyzers):
   - Coverage (B24): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__vtrac_pack_boxed_first_laneonly_presetB__stable10__B24.md`
   - Conversion (B36): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy__stable10__B36.md`

---

## Regenerate the ladder (one command per strategy)

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-15 --date-to 2026-01-22 \
  --profile tool_only \
  --experiment-tag stable10 \
  --strategy vtrac_pack_boxed_first_laneonly_presetB \
  --write-casebook --casebook-budget B24 --casebook-n 5
```

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-15 --date-to 2026-01-22 \
  --profile tool_only \
  --experiment-tag stable10 \
  --strategy v0_2_default_multi_pack_packheavy \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

---

## Results coverage (avoid “censored” confusion)

Before reading any rates, confirm horizon coverage:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__RESULTS_HORIZON.md`

---

## MoP (Mixture-of-Policies) status (experimental)

We experimented with a MoP B36 strategy:
- `v0_2_default_multi_pack_mop_24_12`

Current result: **not promoted** (does not beat the B36 default cleanly across both harness windows).

Where to inspect:
- In-sample (Jan gold window): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__MOP.md`
- OOS window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__MOP.md`
