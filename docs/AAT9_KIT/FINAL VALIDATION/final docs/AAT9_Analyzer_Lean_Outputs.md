# AAT9 — Analyzer Lean Output Spec

## Purpose
Document the lean (analysis-only) artifacts for each analyzer so we can run heroes fast, compare examples across states, and wire the final aggregator without wading through duplicative winners bundles. Digit Reduction is already lean; this spec captures that final layout and records the current raw outputs for Stable and V-TRAC so we can repeat the clean-up when ready.

---

## Digit Reduction (Current State)

### 1. Brain Bundle (per state, per run)
- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/`
  - `<STATE>_analyzer_v2_per_item.csv` — core features (earliest/persistence per detection class, box density, drop metadata, cross-column/variant/method echoes, recency flag, `vt_only_lane`, `funnel_precol1`, `ls_col_42`, `ls2_lane`, `score`, `score_raw`, `score_v2`, `lockscore_v2`, `final_linear`, `final_prob`, `lockscore_prob`, `lock_decision`, `match_types`, `dr.win_*` flags, `reasons_json`).
  - `<STATE>_analyzer_v2_top_candidates.csv` — aggregated families with `score_v2`, support counts, `evidence_tags`, `steps_summary`, and the same match-type taxonomy (`exact`, `vtrac`, `family_vtrac`, `drop_vtrac`).
  - `<STATE>_analyzer_v2_meta.json` — config hash, git SHA, diagnostics flags, file list.
  - `stacked_<variant>.html` for Midday/Evening/Combined — pre-draw human preview.

### 2. Diagnostics (default ON for steps; OFF for overlays)
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`
  - Tidy step trace (Set/Draw/Col/Method/Mode; value/length/unique/is_3value + sequence_meta).
- `training/<STATE>_digit_reduction_logs.json` — compact training log (canonical analyzer input; required).
- `_digit_reduction_log.json` (verbose) — retired by default.
- Per-tool winners output (all `winner_*.json/csv/html`) — gated off; only generated when `diagnostics.write_overlay: true`.

### 3. Central Winner Artifacts
- Control Center batch is the only writer of:
  - `YYYYMMDD_<Variant>_winner_map.json`
  - `YYYYMMDD_<Variant>_winner_flags.csv`
  - Winners HTML (3-table view) when diagnostics enabled.
- Combined variant still available here; analyzer bundles only carry Midday/Evening results.

  Each `winner_flags.csv` now includes `dr_win_vt_boxed` and `dr_win_vt_straight` columns, and the companion `winner_hits.csv` mirrors them so downstream scripts can classify exact straight/boxed vs VT boxed/straight winners using the same taxonomy as Stable.

### 4. Extended ladder + progression (current defaults)
- Extended Set1 ladder (Draw2–Draw7 cols 6→1) is ON by default (`AAT9_DR_EXTENDED_SET1` kill-switch only).
- LS2/VT-only telemetry is preserved; keep weights to avoid burying near-core evidence.
- Progression feature (`ls2_progress`) is emitted in per_item/top; light global weights are set in config (`weight_near=0.02`, `weight_far=0.01`) and can be tuned if needed.
- `scoring_v2` includes a small, config-gated guard (`drop_only_multiplier`, default 1.0, currently 0.9) that gently down-weights **pure** drop-vtrac hits (no exact/VT/family VT) without changing how VT/family VT/exact evidence is scored.

---

## Stable Pattern Extractor — Lean Contract (v1.0)
Packet‑2 landed + literal winner logging. The files below are the contract the Analyzer/Winners module can depend on.

### 1. Brain bundle (per state, per date) — Analyzer inputs
- `data/outputs/analysis/patterns/<STATE>/`
  - `<STATE>_stable_patterns_scores.csv` — full row matrix (`section`, `Set`, `Draw`, `Column`, canonical, `score_*` parts, persistence, VT-straight, double-mirror, etc.).
  - `<STATE>_stable_patterns_families.csv` — family aggregates (`family_score`, `best_compound_score`, `hot1_count`, `hot2_count`, `consensus_hits`, etc.).
  - `<STATE>_stable_patterns_compound.csv` — canonical roll-up with Packet‑2 columns (`compound_score`, `set_chain_depth`, `draw_chain_depth`, `funnel_precol1`, `vt_only_lane`, `compound_why`).
  - `<STATE>_metrics.json` — winners array plus `winner_family_best_rank`, `best_compound_rank`, `winner_hits` (`exact_straight`, `exact_boxed`, `vtrac_boxed` lists), schema versions, and `signals.{hot2_bias,consensus_of_consensus}`.
- Training bundles (`training_sets/<STAMP>/...`) are generated via `scripts/tools/run_stable_from_results.py --write-bundle` and copy the same four files above for reproducibility.

### 2. Stable winners lens (per state, per date)
- `<STATE>_winner_family_spotlight_raw.csv`
- `<STATE>_winner_family_spotlight_families.csv`

Both spotlight CSVs now include `winner_literal_midday`, `winner_literal_evening`, and the boolean flags (`is_exact_straight`, `is_exact_boxed`, `is_vtrac_boxed`). These feed the future centralized Winners module while remaining small enough for quick inspection.

### 3. Human QA (optional but shipped in sharepacks)
- `<STATE>_stable_patterns_report.html` — Combined/Midday/Evening Top‑30 view + compound leaderboard.
- `sharepacks/YYYY-MM-DD/<STATE>/compound_top5.txt` — Midday/Evening/Combined Top‑5 summary (`compound_score`, chain depths, hot counts).
- `sharepacks/YYYY-MM-DD/<STATE>/headers.txt` — column snapshots for scores/families/compound CSVs (helpful during deep-review sessions).

### Tooling / guardrails
- Workbook swap: `scripts/tools/select_pick3_history.py --file Pick3StatsC4_YYYY-MM-DD.xlsm` followed by `pipeline_runner.run_pipeline_from_original_path(...)` (documented in AAT9 Quickstart).
- Stable runs per state via `scripts/tools/run_stable_from_results.py --state <STATE> --results-file data/results/<DATE>.txt` (wrap in bash loop for bulk runs).
- Winners HTML regeneration: `scripts/tools/generate_winners_from_results.py --results-file ... --out-dir reports/stable/winners_by_date/<DATE>`.
- Guardrails: `scripts/checks/validate_stable_schema.py` (columns + metrics + literal winners + Combined coverage), `scripts/tools/compound_top5.py`, `scripts/checks/print_stable_header.py`.

→ **Current status:** Contract is locked; sharepacks mirror this layout. Future clean-up (once the centralized Winners module is in place) can demote the optional HTML/spotlight copies, but the Analyzer can rely on the brain bundle + winner lens files today.

---

## V-TRAC Analyzer — Lean Contract (phase-close target)

### 1. Brain bundle (per state/date) — Analyzer inputs
- `data/outputs/analysis/vtrac/<STATE>/`
  - Enhanced analyzer bundle JSON (`<STATE>_vtrac_enhanced_<STAMP>.json`) with:
    - `indices_ranked`
    - `straights_ranked`
    - `top_straights`
    - `section_summaries`
    - `telemetry`
  - Legacy CSV/JSON per variant may still exist, but the enhanced JSON is the SSOT for the predictive-side analyzer feed.
- Validation artifacts (parity vs winners HTML):
  - `data/outputs/analysis/vtrac_validation/<STATE>/validation_report.{json,md}`
  - Batch summaries: `data/outputs/analysis/vtrac_validation/summary.{md,csv}`
- Aggregator feed (global per date):
  - `vtrac_compact_report.{json,csv}` produced by `TOOLS/vtrac_score_and_export.py` / `TOOLS/run_vtrac_share_bundle.py`.

Primary predictive-side arena meaning:

- `indices_ranked` = lane/index evidence
- `straights_ranked` = bounded straight witnesses inside those lanes
- `section_summaries` + `telemetry` = section profile / hot-right-column context

The intended role is:

- lane semantics
- cross-section corroboration
- bounded straight-lane explanation

Not:

- a tiny direct-caller oracle

### 2. Winners lens (post‑results audit)
V‑TRAC winners artifacts are generated by the **centralized Winners Logger**, not by the analyzer run:
- Analyzer‑style 3‑variant winners overlays (Midday/Evening/Combined):
  - `data/outputs/analysis/winners/<STATE>/*_winner_*_analyzer.html`
- Compact V‑TRAC winner report (table‑agnostic):
  - `data/outputs/winners/<YYYY-MM-DD>/vtrac_reports/<STATE>/*.html`
- Sharepacks mirror these under `sharepacks/<DATE>/<STATE>/winners/<STATE>/`.

→ **Lean target**: keep winners HTML/JSON as the audit lens, not the predictive feed. The predictive feed should standardize on:

- enhanced JSON
- compact report
- centralized winners artifacts only for post-results review

Current closeout posture:

- finish the contract / lean-output clarity
- do not reopen broad scorer tuning by default

## Hot Zones — Lean Contract (phase-close target)

- Brain bundle lives under `data/outputs/analysis/hot_zones/<STATE>/` and mirrors the Digit Reduction / Stable structure:
  - `<STATE>_hot_zones_per_lane.csv` — per-item evidence with late-column flags (vt_only_lane, funnel_precol1, col1_arrival, ls2_lane, etc.).
  - `<STATE>_hot_zones_top_lanes.csv` — aggregated triads with support counts, variant/set spans, and score mean/max.
  - `<STATE>_hot_zones_meta.json` — run metadata (state, date stamp, JSON source, row counts, weights).
- Winners lens:
  - `YYYYMMDD_hot_zones_winner_map.{json,csv}` under the same folder (or a shared winners directory). Captures the top triads for that date, ready for the Aggregator to join with other tools.
- Run via CLI today:
  ```bash
  python scripts/hot_zones/run_hot_zones_cli.py \
      --state Connecticut4 \
      --date 2025-06-24 \
      --json data/outputs/json_tables/Connecticut4_tables.json \
      --out-dir data/outputs/analysis/hot_zones/Connecticut4
  ```
  (The default paths resolve via `utils.path_handler`, so only `--state` and `--date` are required in most runs.)

Primary predictive-side ingest for the arena should be:

- `<STATE>_hot_zones_top_lanes.csv`
- `<STATE>_hot_zones_meta.json`

Forensic / debug only:

- `<STATE>_hot_zones_per_lane.csv`

Transitional compatibility:

- `YYYYMMDD_hot_zones_winner_map.{json,csv}` can still act as a compact triad list, but the more complete arena-facing contract should prefer `top_lanes + meta`.

Primary arena meaning:

- late-tail pressure
- superhot/funnel pressure
- vertical support
- VT-only lane pressure
- col1 / pre-col1 tightening

The intended role is:

- pressure / location / survivorship semantics
- lane/index corroboration

Not:

- a tiny direct-caller oracle

Recommended final validator/digest additions:

- `hot_zones_summary_digest.csv`
- `hot_zones_ledger_all.csv`
- schema/manifest export

These belong to the validation/consumption layer, not to another guard or weight loop.

Current repo note:

- `scripts/tools/validate_vtrac_compact_report.py` already covers the VTRAC compact-report smoke check.
- `scripts/tools/hot_zones_sharepack_summary.py` already provides a practical Hot Zones validation summary from `top_lanes + per_lane + winner_map`.

So the phase-close expectation is to formalize and reuse those validator paths before inventing any new analyzer-side outputs.

## Aux / Control Center Context — Lean Contract (phase-close target)

The current predictive selection usage is intentionally narrow.

That narrowness should be understood as:

- a bounded candidate-universe / conversion choice

not:

- the final analysis-arena contract for `Aux / Control Center`

### Primary predictive-side ingest

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`
- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

### Arena meaning

Primary arena objects should preserve:

- `aux_positional_pressure`
- `aux_vtrac_pressure`
- `aux_badge_pressure`
- `aux_pair_band_context`
- `aux_due_doubles_family_pressure`
- `aux_repeat_watch_context`
- `aux_sums_context`
- `aux_blackapple_context`
- `cc_profit_alert_context`
- `cc_compound_event_context`
- `cc_tracker_context`

### Heavy truth layers

The arena should preserve structured summaries while keeping drill-down paths to:

- full boxed VTRAC badge tables
- raw badge rows by pair / combo / variant
- full pair-status tables
- Blackapple candidate ledgers
- detailed profit-alert evidence JSON

### Non-goal

Do not define `Aux / Control Center` by only the current narrow predictive methods:

- `aux_positional`
- `aux_vtrac_index_overdue`
- `mirror_pair_closure`
- `due_doubles`

Those remain bounded conversion surfaces, not the full tool-to-arena contract.

### Finish stance

The correct phase-close for `Aux / Control Center` is:

- broader structured arena preservation from existing summary/control-center artifacts
- not a new broad scorer rewrite
- not another attempt to turn the context layer into a tiny direct-caller oracle

---

## Applying the Lean Template to Stable / V-TRAC / Hot Zones

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

By keeping the evidence layout consistent, the eventual Aggregator module (the “master brain”) can ingest all tools’ per_item/top/meta files without juggling bespoke directories.

Current finish stance for these tools:

- `Stable` — wrapped for this phase
- `Digit Reduction` — wrapped for this phase
- `V-TRAC Analyzer` — finish contract/lean closeout, not broad tuning
- `Hot Zones` — finish validator/digest closeout, not broad tuning
