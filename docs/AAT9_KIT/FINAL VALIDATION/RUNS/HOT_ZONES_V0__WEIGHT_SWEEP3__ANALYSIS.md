# Hot Zones — HOTZ‑003 Weight Sweep v3 (adds VTRAC index gateway metrics) — Analysis Notes

Purpose: interpret the Hot Zones weight sweep results using the same “gateway” language used throughout Master Validation (exact vs boxed vs VTRAC family), without changing analyzer defaults prematurely.

This v3 sweep is the same harness as v2, but with one key measurement upgrade:

- In addition to “winner canonical in top‑K”, it now reports **VTRAC index hit** in top‑K:
  - `vtrac_index_hit_top8/top12/top20`
  - `vtrac_index_hit_only_topK` (index hit, but canonical not present in top‑K)

Why this matters: Hot Zones is intended to be a **lane/index lens** more than a strict “top‑8 straight oracle”. Index‑hit metrics align evaluation with that design intent.

---

## What was swept (v3)

Harness:
- `scripts/tools/hot_zones_weight_sweep.py`

Inputs:
- Frozen JSON tables (all 3 variants embedded as sections): `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`
- Official winners: `data/results/<D>.txt`

Note:
- Hot Zones scanning is **global across sections** (Midday/Evening/Combined); the tool encodes cross‑variant echo via `variant_span/variant_echo` and `w_cross_variant_echo`.
- The harness grades both outcomes (Midday + Evening) against the same ranked `tops` list (per state/day/weights).

Sweep parameters:
- `w_vt_only_lane_bonus`: `0.8, 0.9, 1.0, 1.1` (baseline is `0.8`)
- `w_col1_arrival`: `2.1, 2.4, 2.7, 3.0` (baseline is `2.4`)

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-06-21_to_2025-06-23.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-12-30_to_2026-01-04.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2026-01-05_to_2026-01-09.md` (and `.csv`)

---

## Baseline snapshot (v0 windows; baseline weights only)

Baseline weights:
- `vt_only=0.8,col1=2.4`

Interpretation reminder:
- `winner_in_topK` means the winner **canonical** appears in top‑K.
- `vtrac_index_hit_topK` means *any* triad in top‑K shares the winner’s `vtrac_index`.
- `vtrac_index_hit_only_topK` means index is present, but the winner canonical is not in top‑K (classic “lane correct, box miss” situation).

### Window: `2025-06-21 → 2025-06-23` (rows=81)

- Canonical hit: Top8 `3/81` (0.037), Top12 `5/81` (0.062), Top20 `11/81` (0.136)
- Index hit: Top8 `20/81` (0.247), Top12 `23/81` (0.284), Top20 `33/81` (0.407)
- Index‑hit only: Top8 `17/81` (0.210), Top12 `18/81` (0.222), Top20 `22/81` (0.272)

### Window: `2025-12-30 → 2026-01-04` (rows=163)

- Canonical hit: Top8 `6/163` (0.037), Top12 `14/163` (0.086), Top20 `18/163` (0.110)
- Index hit: Top8 `46/163` (0.282), Top12 `61/163` (0.374), Top20 `75/163` (0.460)
- Index‑hit only: Top8 `40/163` (0.245), Top12 `47/163` (0.288), Top20 `57/163` (0.350)

### Window: `2026-01-05 → 2026-01-09` (rows=138)

- Canonical hit: Top8 `6/138` (0.043), Top12 `9/138` (0.065), Top20 `13/138` (0.094)
- Index hit: Top8 `21/138` (0.152), Top12 `39/138` (0.283), Top20 `55/138` (0.399)
- Index‑hit only: Top8 `15/138` (0.109), Top12 `30/138` (0.217), Top20 `42/138` (0.304)

---

## What v3 changes about our conclusions

### 1) “Hot Zones is weak at top‑K canonical” is still true

Even after adding `w_col1_arrival` to the sweep space, canonical Top8/Top12/Top20 rates do not show stable lift across windows.

### 2) “Hot Zones is useful as an index/lane lens” is now measured directly

Index hit rates are materially higher than canonical hit rates across windows, and a large fraction is **index-hit-only**.

This matches the intended “gateway” behavior:
- Hot Zones can be “right about the rail” (index neighborhood) while missing the exact canonical permutation.

### 3) HOTZ‑003 weight tuning is still not a high-leverage lever (so far)

Across v3, the best-performing weight points for index-hit differ slightly by window (often nudged by `w_col1_arrival=2.1`), but:
- improvements are small,
- inconsistent across windows,
- and do not justify changing default Hot Zones weights in v0.2.

So: v0.2 keeps the current weights; HOTZ‑003 remains a measured v0.3 backlog item.

---

## Next “high-confidence” leverage (aligned with the 4-criteria / gateway philosophy)

Because v3 shows a real **index signal**, the next lever is a selection-layer conversion experiment:

1) Preserve Hot Zones as a low-cost STRAIGHT triad contributor (current v0.2 posture).
2) Add an **optional, additive** conversion pack for experiments (not default):
   - Convert top index votes into a bounded closure set that can turn “index-hit-only” into “box hit”.

This is explicitly “conversion policy” work, not analyzer tuning.

