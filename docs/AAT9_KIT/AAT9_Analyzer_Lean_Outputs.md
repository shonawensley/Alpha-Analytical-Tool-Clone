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
*Packet‑2 schema landed; core outputs now include compound CSV and references to helper scripts for dated runs.*

- `data/outputs/analysis/patterns/<STATE>/`
  - `<STATE>_stable_patterns_report.html` — multi-variant (Combined/Midday/Evening) table with Top‑30 score breakdown + **Compound Leaderboard (Top 30)** per section.
  - `<STATE>_stable_patterns_scores.csv` — per-row evidence (`section`, `Set`, `Draw`, `Column`, canonical, score parts, persistence, hidden-core, double_mirror, etc.).
  - `<STATE>_stable_patterns_compound.csv` — canonical roll-up (compound score, base score, set/draw chain depth, hot1/hot2 counts, consensus/hidden/vtrac/double hits, `compound_why`).
  - `<STATE>_stable_patterns_families.csv` — family aggregation plus Packet‑2 fields (`persistence_set_count`, `hot1_count`, `hot2_count`, `consensus_hits`, `best_compound_score`, ...).
  - `<STATE>_metrics.json` — winners array, `winner_family_best_rank`, new `best_compound_rank`, `compound_schema_version`, and `signals.{hot2_bias,consensus_of_consensus}`.
  - Optional spotlight CSVs (`<STATE>_winner_family_spotlight_{raw,families}.csv`) when winners are supplied.
- `training_sets/<STAMP>/` mirrors the above (scores, families, compound, metrics, spotlight) via `scripts/tools/run_stable_from_results.py` + `alpha_analytical/stable/training_bundle.py`.

### Stable tooling for dated runs
- Rotate workbooks: `scripts/tools/select_pick3_history.py --file Pick3StatsC4_YYYY-MM-DD.xlsm` + pipeline runner.
- Generate draw CSVs for Aux/Blackapple/Control Center: `scripts/auxiliary/generate_draws_csv.py`.
- Run Stable with winners: `scripts/tools/run_stable_from_results.py --state <STATE> --results-file data/results/<DATE>.txt` (call per state or wrap in a loop).
- Produce analyzer-style winners HTML for all states: `scripts/tools/generate_winners_from_results.py --results-file ... --out-dir reports/stable/winners_by_date/<DATE>`.
- Inspect/guard Packet‑2 schema: `scripts/checks/validate_stable_schema.py`, `scripts/checks/print_stable_header.py`, `scripts/tools/compound_top5.py`.

→ **Lean target**: Now that scores/families/compound/metrics are locked, the remaining step is trimming legacy diagnostics (optional stacked HTML, spotlight copies) once the aggregator consumes the new contract.

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
