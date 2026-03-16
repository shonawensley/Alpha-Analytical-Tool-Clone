# DR Arena v1.1 - Lock-In

Purpose: freeze the Digit Reduction `v1.1` additions that were explicitly carried forward from:

- Virginia4 Midday `473`
- Indiana4 Midday `110`
- Delaware4 Evening `337`
- NewYork4 Evening `116`
- Florida4 Evening `611`

This note defines what landed now, what was intentionally folded into a cleaner corridor/structural model, and what remains deferred.

---

## Landed now

### 1. `dr_empty_lens` calibration

`dr_empty_lens` is no longer just a sparse/not-sparse flag.

It now preserves:

- `classification`
  - `true_empty`
  - `active_low_trust`
  - `positive_trace`
- `confidence`
- `positive_signal_score`
- `cold_ratio`
- `raw_exposure_count`
- `path_summary_count`

This is the direct answer to the Virginia `473` false-empty problem.

### 2. Corridor model

Instead of exploding the schema into many case-specific corridor fields, the predictive writer now preserves:

- `dr_corridor_strength`
- `corridor_scope`
  - `exact_corridor`
  - `family_neighborhood`
  - `compact_double_corridor`
  - `vtrac_corridor`
- `corridor_band`
  - `set1_current_day`
  - `7_6_5_band`
  - `mixed`
- `raw_exposure_count`
- `path_summary_count`
- `neighbor_box_support`
- `consecutive_box_progression`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`

This is the clean predictive-side home for:

- Indiana `110` current-day corridor
- Delaware `337` family-neighborhood saturation
- Florida `611` compact corridor-inside-family

### 3. Structural signals

The predictive writer now exposes section-level structural signals:

- `pre_reduction_cluster_strength`
- `reveal_purity`
- `early_activation_strength`
- `consecutive_box_progression`
- `neighbor_box_support`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`
- `core_vs_clutter_transit_score`
- explicit `raw_exposure_count` vs `path_summary_count`

This is the main predictive-side absorption of the Batch 3 example reviews.

---

## Folded in rather than added as separate top-level fields

These ideas are preserved through the new corridor / structural model instead of becoming standalone top-level arena objects:

- `dr_set1_exact_corridor`
- `dr_current_day_corridor_strength`
- `double_family_corridor_strength`
- `exact_vtrac_corridor_strength`
- `cross_variant_corridor_strength`

The reason is schema discipline.

The underlying concepts are valuable.
The separate field explosion is not.

---

## Deferred on purpose

These items remain valid, but they were not forced into the predictive writer in this pass:

### 1. Winner-aware `overlay_summary_mismatch`

This needs winner overlays / stamp context.
The predictive writer now carries an explicit placeholder:

- `overlay_summary_mismatch.available = false`

That keeps the requirement visible without pretending the predictive build can evaluate it fully.

### 2. Rich permutation-neighborhood scoring

Virginia `473` still argues for stronger permutation-neighborhood treatment.
The current pass only absorbs part of that through:

- corridor grouping
- family saturation
- progression signals

A fuller winner-aware permutation scorer is still a later pass.

### 3. Richer VTRAC-cluster scoring inside stable rows

Partially represented through:

- `corridor_scope = vtrac_corridor`
- lane confidence
- structural saturation

But not yet as a dedicated winner-aware VTRAC-cluster audit.

### 4. Guarded `protected_core_reduction_candidate`

Still valid.
Still explicitly approved.
Still intentionally deferred from default predictive logic.

---

## Why this is the right boundary

This pass was meant to improve the predictive-side DR evidence writer without:

- rewriting Analyzer V2
- retuning DR weights
- reviving top-candidates as the main caller surface
- forcing winner-only audit logic into predictive generation

So the `v1.1` lock-in is:

- stronger empty-lens discrimination
- stronger corridor modeling
- stronger structural signals
- clearer raw-vs-path accounting

That is the right next layer before any future consumer changes or `V2` vs `V3` decision.
