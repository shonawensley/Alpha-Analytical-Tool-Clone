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
- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`
- Goal metric: preserve strict `hit_any` as an **OOS guardrail**, while lifting `hit_any_inclusive` by widening lane coverage (ranked index tail) through a tighter spine allocation.
- This is taper6644 geometry with a **split** index chooser:
  - spine indices by `methods_first`
  - tail indices by `score_total_first`
- Jan gold window (known winners, stable10):
  - strict `hit_any` **4.7%**
  - `hit_any_inclusive` **59.1%**
  - `pack_any_correct` **59.1%**
  - `CU_LANE_BUT_PLAY_MISS` **17.6%**
  - `CU_EXACT_BUT_PLAY_MISS` **2.1%**

- OOS window (stable10):
  - strict `hit_any` **4.1%**
  - `hit_any_inclusive` **53.1%**
  - `pack_any_correct` **53.1%**
  - `CU_LANE_BUT_PLAY_MISS` **14.7%**
  - `CU_EXACT_BUT_PLAY_MISS` **3.3%**

Reference:
- Promotion brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_PROMOTION__2026-02-18.md:1`
- Split chooser scoreboards (Jan + OOS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md:1`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md:1`
- Ladder (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first__stable10.md:1`
- Casebook (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first__stable10__B36.md:1`

Recent B36 levers (evaluated; not promoted):
- Taper6643 (free +1 tail lane) failed OOS strict guardrail: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6643_SPLIT_EVAL__2026-02-18.md:1`
- Within-spine canon-ranked (keep split chooser + taper6644; change `spine_pick_mode` only) failed Jan precheck: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINE_CANON_PRECHECK__2026-02-18.md:1`
- Tail score-first (keep split chooser + taper6644; change `tail_pick_mode` only) failed Jan precheck: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_SCORE_FIRST_SPLIT_PRECHECK__2026-02-18.md:1`
- Tail rank5 depth2 (keep split chooser + taper6644; buy 1 extra tail depth line) failed Jan precheck: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_RANK5_DEPTH2_PRECHECK__2026-02-18.md:1`

**Optional: strict-max baseline (research-only)**
- Strategy: `convergence_box_first`
- This maximizes strict hits, but sacrifices lane/pack semantics (everything is effectively “filler coverage”).

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__convergence_box_first__stable10.md`

---

## Crossroads promotion gates (B36; stable10; selection-layer only)

These gates exist to prevent “pretty in-sample stories” from becoming default without surviving OOS.

**Locked invariants (do not change in this phase)**
- Posture: `profile=tool_only`, `experiment_tag=stable10`, budget `B36`
- Analyzers: unchanged (**no analyzer edits**)
- Geometry: `taper6644` (spine ranks 1–4 must allocate at least **6/6/4/4** lines)
- Baseline strategy (current default): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

**Global safety rules (no footguns)**
- Do not overwrite outputs: always pass an explicit unique `--out` and/or `--label` when running sweeps/reports.
- Build date rosters from what exists: derive window date lists from directories under the chosen sharepacks root (`sharepacks/_predictive/` or `sharepacks/`) and skip missing days automatically.

**Material regression threshold**
- Unless stated otherwise: “material regress” means worse by more than **0.5pp absolute** on a rate.

**Robustness strict gate (FEB17 onward)**
- For robustness windows only (i.e., not the OOS hard-gate window), strict `hit_any` uses a **count-based** material-regress check to avoid small‑N false vetoes:
  - Let `n = outcomes_n` (after filtering `winner_missing=1`).
  - Let `allowed_drop_hits = max(1, ceil(0.005 * n))`.
  - Strict `hit_any` is considered a material regress only if the candidate has **more than** `allowed_drop_hits` fewer strict hits than baseline on that window.
- OOS strict remains a **hard** gate (`>= baseline`) and is not count-relaxed.

**Hard gates (must pass)**
- OOS strict guardrail: OOS `hit_any` must be **≥ baseline**.
- OOS coverage guardrail: OOS `hit_any_inclusive` must be **≥ baseline**.
- Robustness (all other windows): `hit_any_inclusive` must not materially regress vs baseline for that window, and strict `hit_any` must not materially regress under the **count-based** rule above.

**Semi-hard gates (in-sample / Jan)**
- Must improve at least one isolation metric vs baseline:
  - Jan `CU_LANE_BUT_PLAY_MISS` improves (lower), or
  - Jan `hit_any_inclusive` improves (higher).
- Neither of those two should materially regress.

**Soft gate (watch exact-miss tradeoffs)**
- OOS `CU_EXACT_BUT_PLAY_MISS` may worsen by **≤ +0.5pp** only if:
  - OOS `hit_any_inclusive` improves by **≥ +0.5pp**, or
  - OOS strict `hit_any` improves by **≥ +0.2pp**.

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
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
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
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
6) Check lane *depth* (this ends “we retained the lane but why didn’t strict lift?” arguments):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
7) Open the casebook buckets (concrete examples to debug policy, not analyzers):
   - Coverage (B24): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__vtrac_pack_boxed_first_laneonly_presetB__stable10__B24.md`
   - Conversion (B36): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36.md:1`

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
  --strategy v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

---

## Lane allocation report (new)

Use this when you want to quantify “how many lanes did we touch?” and “how many lines did the winner lane get?”

```bash
python3 scripts/tools/create_lane_allocation_report.py \
  --date-from 2026-01-15 --date-to 2026-01-22 \
  --profile tool_only \
  --experiment-tag stable10 \
  --strategy v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first \
  --budget B36 --label TAPER6644_SCORE_TOTAL_FIRST
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

---

## Taper depth experiments (B36; not promoted)

These test “more breadth” by tapering spine ranks 3–4 below the promoted `...spine_taper_6644` posture.

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633`: lifts inclusive and reduces lane/exact misses, but **regresses OOS strict** (`4.1% → 3.7%`), so it fails the guardrail.
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6633_EVAL__2026-02-15.md:1`
  - Jan/OOS scoreboards: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1` and `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643`: milder taper (free +1 tail line) still **regresses OOS strict** (`4.1% → 3.7%`), so it fails the guardrail.
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6643_EVAL__2026-02-15.md:1`
  - Jan/OOS scoreboards: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1` and `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

---

## Tail-depth experiments (B36; not promoted)

These are kept for research/provenance. Defaults remain `...spine_taper_6644` (see B36 section above).

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_canon2`: regresses lane retention (touches ~10 indices vs ~15), so inclusive drops.
  - Scoreboard (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL_CANON2.md`
  - Scoreboard (OOS): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL_CANON2.md`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_canonvote`: no measurable difference vs the baseline tail selection in current windows.
  - Scoreboard (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL_CANONVOTE.md`
  - Scoreboard (OOS): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL_CANONVOTE.md`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first`: tail 1-line/index representative chosen by score-first ordering (vs convergence ordering).
  - Result: not promoted (no in-sample lift; OOS strict +1 hit is not robust enough alone).
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md:1`
  - Scoreboard (Jan + OOS, side-by-side): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1` and `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_shoulder_depth`: “shoulder depth” (ranks 5–8 get 2 lines, ranks 9–16 get 1) regresses lane retention without lifting strict in current windows.
  - Scoreboard (Jan + OOS, side-by-side): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SHOULDER_DEPTH.md`
  - Lane allocation (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SHOULDER_DEPTH.md`
  - Lane allocation (OOS): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SHOULDER_DEPTH.md`

---

## Split chooser (B36; promoted)

This is an index-chooser lever on top of the promoted taper6644 baseline:
- Candidate strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`
- Meaning: choose top-4 spine indices by `methods_first`, but choose remaining tail indices by `score_total_first`.

Reference:
- Robustness baselines: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__ROBUSTNESS_WINDOWS__2026-02-16.md:1`
- Prior eval brief (rejected under old robustness strict): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_EVAL__2026-02-16.md:1`
- Promotion brief (under count-based robustness strict): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_PROMOTION__2026-02-18.md:1`

---

## Constraint chooser experiment (B36; not promoted)

This is an index-chooser lever on top of the promoted taper6644 baseline:
- Candidate strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first`
- Meaning: keep `score_total_first` ordering, but constrain the **top‑4 spine indices** to lanes with corroboration (`methods_count>=2 OR variants_non_unknown>=1`), falling back to the unconstrained ranking if needed.

Result: **not promoted** (no measurable lift under the Crossroads gates).
- Jan/OOS/robustness metrics are unchanged vs baseline; the lever is mostly a no‑op in practice under `score_total_first`.

Reference:
- Eval brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_CONSTRAINT_CHOOSER_EVAL__2026-02-17.md:1`
- Scoreboards (Jan/OOS/holdouts):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`

---

## Round-robin mix chooser experiment (B36; not promoted)

This is an index-chooser lever on top of the promoted taper6644 baseline:
- Candidate strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total`
- Meaning: keep taper6644 geometry + display-only spine membership, but choose the ranked index list by a deterministic round-robin mix of three lenses:
  - `methods_first`
  - `packs_first`
  - `score_total_first` (with backstop fill to reach rank_count)

Result: **not promoted** (fails the Jan precheck; strict regresses and lane miss worsens without lifting inclusive).

Reference:
- Eval brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_RRMIX_CHOOSER_EVAL__2026-02-18.md:1`
- Geometry precheck (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__RRMIX_PRECHECK.md:1`
- Scoreboard precheck (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__RRMIX_PRECHECK.md:1`

---

## Tail-only rrmix experiment (B36; not promoted)

This is a constrained follow-up to the full rrmix chooser:
- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_rrmix_methods_packs_score_total`
- Meaning: keep the promoted split chooser spine (`methods_first`), but apply rrmix ordering only to the tail.

Result: **not promoted** (fails Jan precheck; inclusive regresses and lane miss worsens).

Reference:
- Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_RRMIX_PRECHECK__2026-02-18.md:1`

---

## Tail packs-first experiment (B36; not promoted)

This is a tail-only variant on top of the promoted split chooser spine:
- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first`
- Meaning: keep spine indices by `methods_first`, but choose tail indices by `packs_first`.

Result: **not promoted** (fails Jan precheck; inclusive regresses and lane miss worsens).

Reference:
- Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_PACKS_PRECHECK__2026-02-18.md:1`

---

## Spine packs-first experiment (B36; not promoted)

This is a spine index-chooser lever on top of taper6644:
- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first`
- Meaning: choose the top-4 spine indices by `packs_first` ordering, keep tail indices by `score_total_first`.

Result: **not promoted** (fails the OOS strict guardrail).

Reference:
- Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPINE_PACKS_PRECHECK__2026-02-18.md:1`

---

## Spine chooser experiments (B36; not promoted)

These test “within-lane conversion” levers on top of the pre-taper baseline `...spinecap6` by changing how the **6 spine lines per index** are selected.

Note: since the current B36 default is `...spine_taper_6644`, any future within-lane chooser iteration should be re-run on top of taper (these results are still useful provenance, but not directly promotable now).

Current result: **not promoted** (no clean win vs baseline under the Crossroads promotion gates).

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence`: OOS strict lifts, but coverage regresses; Jan strict regresses.
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked`: no measurable change vs baseline in current windows.
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked`: canonical-aware display ranking; no measurable change vs baseline, and changes fewer lines than `...spine_display_ranked` in current windows.
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2`: constrained hybrid (min 4 display + max 2 evidence inside the spine) still regresses OOS coverage/bridge and Jan strict.

Where to inspect:
- Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md:1`
- Hybrid brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_HYBRID_SPINECHOOSER__2026-02-15.md:1`
- Canon-ranked brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md:1`
- Jan sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md`
- Jan hybrid sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md`
- Jan canon-ranked sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md`
- OOS sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md`
- OOS hybrid sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md`
- OOS canon-ranked sweep: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md`

Also tested on top of taper6644 (same geometry; different spine display ordering):
- Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md:1`
- Result: not promoted (no measurable change OOS; Jan strict regressed).
