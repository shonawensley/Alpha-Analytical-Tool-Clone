# Digit Reduction Analyzer V2 — Spec Lock

## Overview
- Analyzer V2 consumes reducer training logs and emits per-item features, scored candidates, and winners overlay artifacts.
- All processing runs from the repo root and respects the Combined baseline (Midday/Evening additive).
- Config-driven design: tuning is isolated to `alpha_analytical/digit_reduction/analyzer_v2/config.yml`.

## Core Pipelines
1. **Feature Extraction (`features.py`)**
   - Scans each item (R2/R4/R6/R8 ladder) for detection classes:
     - `exact`, `vtrac`, `drop_exact`, `drop_vtrac`, `family_exact`, `family_vtrac`.
   - Produces earliest step, persistence, final match flags per class.
   - Captures extended cluster stats (3–12 digit windows), drop metadata (digit/run length), box family density, duplicate bonus, and residual purity.
   - Serialises run details to `features_json` for diagnostics.

2. **Aggregations (`pipeline._aggregate_metrics`)**
   - Computes cross-column/variant/method echoes with a configurable step ceiling.
   - Derives `cols_hit`, `variants_hit`, `method_consensus`, `cluster_echo_count`, `variant_echo_count`, `set_echo_count`, `recency_carryover`, `box_pair_agree`.

3. **Scoring (`score.py`)**
   - Config weights (`w_*`) applied to detection strength, density, drop quality, and echo metrics.
   - Supports drop-length shaping, Set2→Set1 carryover, and optional bonuses (early multi-column Drop-VTRAC).
   - Outputs tanh-clamped score, lock decision, and raw contribution.

4. **Winners Overlay (`winners_overlay.py`)**
   - Optional batch runner fed by config `overlay.winners`.
   - Generates map/hits/flags/stamp artifacts under `analyzer_v2/winners/`.
   - Provides flag map for pipeline join so UI/CSV stay in sync.

5. **Writers (`writers.py`)**
   - Always writes per-item CSV, top-candidates CSV, meta JSON.
   - Optional diagnostics (feature detail JSON, overlay manifest) controlled by config.
   - Overlay file list recorded in meta.

## Outputs
- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/`
  - `<STATE>_analyzer_v2_per_item.csv`
  - `<STATE>_analyzer_v2_top_candidates.csv`
  - `<STATE>_analyzer_v2_meta.json`
  - `winners/<STAMP>_<VAR>_winner_{flags,map,hits}.csv/json` (+ HTML/manifest when enabled)
- Config hash + git SHA stored in meta for reproducibility.

## Config Highlights (`config.yml`)
- `features.cluster_scan` bounds (3–12), `variants_step_ceiling`, `box_pair_agree_pairs`.
- Weight hierarchy: `Exact > VTRAC > Drop > Family` plus density, duplicates, echo, drop quality, recency.
- Caps for density/dup bonus, gating thresholds (`early_lock`, `early_unlock`, `tanh_scale`).
- Policy: `combined_auto_run`, `write_own_vs_combined_delta` (diagnostic default).
- Overlay toggles (`write_flags`, `write_detailed_hits_csv`, `write_html`, `near_miss_hint`).
- Diagnostics toggles (feature distributions, overlay manifest).

## Test Coverage
- `tests/test_digit_reduction_features_v2.py`
  - Validates drop metadata, density/duplicate computation, aggregation metrics (columns/variants/methods/recency), and scoring shape.
- `tests/test_digit_reduction_overlay.py`
  - Ensures helper utilities and `_load_winner_flags` operate with new pipeline interface.

## Notes
- Overlay generation requires `overlay.winners` mapping; absent winners → graceful no-op with empty flag map.
- Aggregations treat `variants_step_ceiling` as the authoritative bound for early detection.
- Method consensus counts include Method `T`.
