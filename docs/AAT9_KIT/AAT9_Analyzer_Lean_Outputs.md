# AAT9 — Analyzer Lean Output Spec

## Purpose
Document the lean (analysis-only) artifacts for each analyzer so we can run heroes fast, compare examples across states, and wire the final aggregator without wading through duplicative winners bundles. Digit Reduction is already lean; this spec captures that final layout and records the current raw outputs for Stable and V-TRAC so we can repeat the clean-up when ready.

---

## Digit Reduction (Current State)

### 1. Brain Bundle (per state, per run)
- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/`
  - `<STATE>_analyzer_v2_per_item.csv` — core features (earliest/persistence per detection class, box density, drop metadata, cross-column/variant/method echoes, recency flag, normalized score, lock_decision, reasons_json).
  - `<STATE>_analyzer_v2_top_candidates.csv` — aggregated families with score, support counts, `evidence_tags`, `steps_summary`.
  - `<STATE>_analyzer_v2_meta.json` — config hash, git SHA, diagnostics flags, file list.
  - `stacked_<variant>.html` for Midday/Evening/Combined — pre-draw human preview.

### 2. Diagnostics (default ON for steps; OFF for overlays)
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`
  - Tidy step trace (Set/Draw/Col/Method/Mode; value/length/unique/is_3value + sequence_meta).
- `_digit_reduction_log.json` (verbose) — retired by default.
- Per-tool winners output (all `winner_*.json/csv/html`) — gated off; only generated when `diagnostics.write_overlay: true`.

### 3. Central Winner Artifacts
- Control Center batch is the only writer of:
  - `YYYYMMDD_<Variant>_winner_map.json`
  - `YYYYMMDD_<Variant>_winner_flags.csv`
  - Winners HTML (3-table view) when diagnostics enabled.
- Combined variant still available here; analyzer bundles only carry Midday/Evening results.

---

## Stable Pattern Extractor (Current Outputs)
*Not yet leaned out; listed here for scoping the next pass.*

- `data/outputs/analysis/patterns/<STATE>/`
  - `<STATE>_stable_patterns_<variant>.html` (per variant).
  - `<STATE>_stable_patterns_scores.csv`
  - Companion JSON (families, metrics, winners spotlight) under `analysis/patterns/<STATE>/`.
- `training_sets/<STAMP>/` for Stable currently includes:
  - Metrics JSON (`<STATE>_metrics.json`)
  - `<STATE>_stable_patterns_families.csv`
  - Winners spotlight CSVs if toggled
  - Map/stamp artifacts similar to Digit Reduction (per variant).
  - Zip copy when requested.

→ **Lean target**: Keep per-state metrics JSON, families CSV, top candidates, meta, stacked (if any). Move winner map/flags to the centralized winners module; steps/logs optional. Document the exact file list before trimming.

---

## V-TRAC Analyzer (Current Outputs)
*Also slated for the lean pass.*

- `data/outputs/analysis/vtrac/<STATE>/`
  - Analyzer CSV/JSON per variant (legacy + enhanced engines).
  - Evidence grid JSON (`evidence/*.json`), winners logger HTML, overlay ZIP when sharing.
- Training bundles / share bundles include:
  - `vtrac_compact_report.{csv,json}`
  - `summary.md/csv`, `summary.html`
  - `winner_map.json`, `winner_flags.csv`, overlay HTML zipped.

→ **Lean target**: Standardize on per_item/top/meta (matching the enhanced evidence grid), keep the compact report as the aggregator feed, move map/flags to the centralized winners module.

---

## Applying the Lean Template to Stable / V-TRAC

When ready, follow the same steps used for Digit Reduction:

1. **Inventory current outputs**:
   - List every file produced under `analysis/<tool>/<STATE>/` and `training_sets/<STAMP>/`.
   - Identify which belong to the “brain” (per-item, top candidates, meta, stacked preview) vs diagnostics vs winners.

2. **Update configs**:
   - Add `outputs.write_stacked_html`, `diagnostics.write_steps_csv`, `diagnostics.write_overlay` toggles (matching Digit Reduction).
   - Default to true for stacked, false for overlay; steps CSV on/off per tool.

3. **Adjust pipeline/writers**:
   - Emit only the brain files + stacked; gate everything else behind diagnostics flags.
   - Ensure training bundles copy the same lean files.

4. **Centralize winners**:
   - Remove per-tool winner writers; Control Center remains the only place generating `winner_map.json`, `winner_flags.csv`, and overlays.

5. **Docs + Validation**:
   - Update this document and the Unified Changelog once each tool is converted.
   - Run at least one state per tool to confirm the new structure.

By keeping the evidence layout consistent, the eventual Aggregator module (the “master brain”) can ingest all tools’ per_item/top/meta files without juggling bespoke directories. When the time comes, we’ll update this document with the exact file lists for Stable and V-TRAC after their lean-outs.

