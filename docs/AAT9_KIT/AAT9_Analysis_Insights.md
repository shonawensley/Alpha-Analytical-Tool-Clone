[*] DO NOT REMOVE EXISTING ENTRIES — APPEND NEW INSIGHTS ONLY

# AAT9 Analysis Insights
## Stable Pattern Extractor

_No entries yet — append new insights here._


## Long String / Digit Reduction

### 2025-11-02 — Analyzer V2 DIGIT06 rollout (Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, Ohio4)
- Harness checks confirm every state produces 396 analyzer rows; mean scores sit ~0.74–0.82 with max ~0.92–0.95. Locked candidates cluster around Set3/Set2 ladders where the June17 winners lived (e.g., CT Set3 col7 994, DE Set3 col6 016, FL Set2 col7 116, IN Set3 col7 338, MI Set3 col6 667, NJ Set3 col7 667, NY Set3 col7 441, OH Set3 col7 550/552).
- Density and dup_bonus metrics behave as intended: all locked rows show dup_bonus=1.0 and density ≥0.6; variance across states still reflects different ladder tightness (e.g., Delaware′ density mean 0.64 vs. Michigan 0.70).
- No overlay artifacts yet (config overlay.winners blank), but analyzer writes full per-item/top candidates/meta bundles for each state; future runs can populate overlay inputs once aggregated winners are ready.
- Next: use the June17 winners list to feed Control Center bulk logger, generate winners overlays, then retune `config.yml` weights so the expected winners score >0.9 and non-winners fall below lock. Document final weight choices and capture Control Center workflow notes for repeatability.

### 2025-11-07 — VTRAC-aware validator + extended-cluster boosts (June17 states)
- What changed:
  - Validator now accepts `--match-mode {exact,box,vtrac,any}` and normalizes each winner/candidate into exact, sorted box, and VTRAC-family codes. Reports now include `hit_at_1_vtrac`, `hit_at_3_vtrac`, `match_channel`, and `top_vtrac_family`, so family-only wins aren’t lost when the literal triple isn’t rank 1.
  - Added `extended_cluster_bonus`, `vtrac_family_rescue`, and `min_drop_run_len` guards to `scoring_v2`/`lockscore`, allowing long-run evidence (e.g., 661111188) and confirmed family hits to influence ranking without touching reducers or winners writers.
  - Ran the full loop for Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, Ohio4: `20250617_V_BASE` (literal), `_V_SV2` (scoring_v2 on), `_V_S01…S09` (sweep), `_V_LSCR` (lockscore as ranker). All artifacts plus the current config live in `reports_20250617_V_bundle.zip` (repo root).
- Results:
  - Literal-only baseline still shows Hit@3=0.0, MRR≈0.016; when VTRAC families are credited (`--match-mode any`) and the new bonuses are enabled, Hit@3 rises to ~6.2% with MRR≈0.056, and the top-miss CSVs clearly indicate which states hit via `match_channel=vtrac`.
  - Grid sweep across `extended_cluster_bonus ∈ {0.15,0.25,0.35}` and `min_drop_run_len ∈ {4,5,6}` ties around the same aggregate metrics, but provides ready-made YAML overrides for future tuning; `_V_S01` currently serves as the “best” config snapshot.
  - Lockscore-as-top did not yet outperform score_v2; we left `lockscore.use_for_top=false` after capturing `_V_LSCR` for reference.
- Next:
  - Share the bundle + summaries with ChatGPT Pro to decide which YAML combo to ship (likely `_V_S01`) and gather guidance on literal coverage gaps.
  - Once a final config is chosen, update `config.yml` and add a short postmortem here describing the winning weights; then resume weight work or collect a fresh stamp using the same validator workflow.

### 2025-11-07 — Pick3 workbook history + Stable Pattern baseline
- Added `data/history/` (dated `Pick3StatsC4_YYYY-MM-DD.xlsm`) and `data/results/<date>.txt` so we can replay any day’s tables/results without renaming files; `utils.path_handler.get_pick3_workbook_path()` (plus optional `scripts/tools/select_pick3_history.py`) auto-detects the active workbook and supports `PICK3_WORKBOOK=/abs/path`.
- Stable Pattern extractor now reads Midday, Evening, and Combined tables in a single run (per-state), tags each row’s `section`, and writes the usual HTML/CSV outputs—so future scoring work starts with full-variant coverage instead of Combined-only.
- Process reminder: each dated workbook represents the tables as of that day (predicting the next day’s results). Pick a file from `data/history/`, point the Control Center or CLI at it, run the tools, and compare against the paired `data/results/<date>.txt` file when reverse-engineering.

### 2025-11-08 — Stable Pattern persistence & VTRAC straight cues
- Added set/draw persistence tracking to the row scorer (`persistence_set_count`, `persistence_draw_run`, and corresponding score columns). Patterns that survive from Set3→Set2→Set1 or span multiple Draws now pick up explicit bonuses and `why` tags (`set_chainX`, `draw_chainY`).
- Introduced `score_vtrac_straight` (config weight) for straight candidates showing up in late columns; reasons ledger now calls out `vtrac_straight` when the bonus fires.
- CSV schema updated and covered by `tests/test_stable_multi_variant.py`; next steps: exploit these persistence signals in the upcoming family/post-pass aggregation and hot-zone module.


## V-TRAC Analyzer

## 2025-10-17 - Enhanced V-TRAC Parity Sweep
- Added `tools/vtrac_validate.py` to compare Winners Logger HTML against the enhanced analyzer JSON bundles. The validator now parses Set1/Draw1 tables (Midday/Evening/Combined), recomputes 3-value V-TRAC signatures, hot/super-hot counts, consensus flags, and reports overlap against analyzer exports.
- Extended `modules.vtrac_enhanced.write_prediction_bundle` so every bundle includes `section_summaries` (hot/super-hot counts, consensus flags, stable columns, top signatures, ring votes) plus `top_straights`. Existing CLI/Streamlit hooks pass the engine input so summaries mirror the rendered tables.
- Validation snapshots (new JSON + Markdown under `data/outputs/analysis/vtrac_validation/`):
  - **Delaware4** - Combined consensus column 1 (`True`) and top signatures `V5x3_2x2_3x1`, `V5x2_2x1_3x1`, `V2x1_3x1_5x1` match analyzer exports (3/3 overlap). Midday/Evening signatures also line up (1/1 and 2/2 overlaps).
  - **Michigan4** - Wide stability across columns (`stable_columns`: `4,3,2,1`) with analyzer overlap for all reported signatures in each section (Midday 3/3, Evening 2/2, Combined 2/2).
  - **Florida4** - Midday consensus column 1 (`True`) confirmed; analyzer echoes the Midday and Evening signatures while Combined shows no 3-value clusters (expected given the table).
  - **NewJersey4** - Combined grid highlights five stable columns and analyzer surfaces the same four dominant signatures; Midday (`V2x2_1x1` family) and Evening (`V1x2_2x1`) also align.
  - **Virginia4** - Strong Midday stability (`V1x3` family) and Combined `V1x2_3x1_5x1` signature replicated in analyzer output, verifying the high-score doubles bias.
- Florida4 Combined re-check: Combined Set1/Draw1 cells collapse to two-digit strings (`03**`, `033**`, etc.), so no valid 3-value signatures exist; analyzer’s empty Combined set is expected, while Midday/Evening retain full overlap.
- Remaining watch: Combined coverage can legitimately be empty when reductions collapse to two digits (Florida4 confirmed); keep an eye on future runs for unexpected gaps.
- Next steps: (1) Promote fixtures for two states into `tests/` to regression-test `section_summaries`; (2) Evaluate precision@K hooks once legacy vs enhanced A/B harness is ready.


## 2025-10-18 - Data hand-off & aggregation strategy
- Documented the validation loop in `AAT9_Data_Validation_Workflow.md`: generate enhanced bundles, run the validator, produce batch summaries (`matrix.csv`, `findings.md`), and choose a sharing strategy (commit/push vs. zip vs. targeted upload).
- Confirmed that the enhanced analyzer and Winners Logger share the same straight families; validator straight overlap remains zero until the logger flags upcoming straights with non-zero counts.
- Sharing best practices:
  - Commit & push summaries to GitHub so ChatGPT Pro (or agents) can read `raw.githubusercontent` URLs without upload limits.
  - Alternatively, zip `data/outputs/analysis/vtrac_validation` or upload key state reports (`validation_report.md/json` + bundle JSON) for focused reviews.
- Aggregator outlook:
  - Keep each tool’s validator pass in the tuning loop; once all pages emit reliable summaries, feed those into a draw-level aggregator.
  - Stay rule-driven today; optional ML layers can be explored later when we have durable logs of validation runs.
- Action items captured for future cycles: commit/push artifacts before requesting remote analysis, expand validator parsing if we want to compare HTML legend highlights (vt-straight gap, family gap), and continue logging observations in this file after every sweep.


## 2025-10-26 - Compact scoring bundle + config hand-off
- Added a config-driven scorer (`TOOLS/vtrac_score_and_export.py`) that reads `validation_report.json`, applies overlap/stability/consensus rescues, and emits `vtrac_compact_report.{json,csv}`. Scores now include `section_prior`, `state_prior`, and a compact `why` field (breakdown of overlap/stable/echo/hot/mask/etc.).
- Introduced `configs/vtrac_score_config.json` so weights/column priors/state priors can be tuned without editing code. `TOOLS/run_vtrac_share_bundle.py` now runs the scorer with this config after `make_pro_payload.py`, keeping summaries, compact report, and optional ZIP in sync.
- Unit test `tests/test_vtrac_score_export.py` (with fixture `tests/fixtures/vtrac_validation/DemoState4/validation_report.json`) locks the consensus rescue, analyzer-only echo boosts, config overrides, and recommended token ordering.
- Sharing workflow: run `python TOOLS/run_vtrac_share_bundle.py`, commit `summary.*`, `vtrac_compact_report.*`, and share the raw URLs. Reviewers can read the `why` column to understand score contribution breakdowns immediately.
- Next sweep: generate fresh validation runs, inspect the compact CSV against Winners HTML, and capture findings here before wiring aggregates into the cross-tool scorer.


### 2025-12-07 — Final DR configuration + June history environment pattern
- Configuration locked for AAT9: extended Set1 ladder (Draw2–Draw7 cols 6→1) ON by default behind `AAT9_DR_EXTENDED_SET1`; progression feature `ls2_progress` enabled with light global weights (`near=0.02`, `far=0.01`); scoring surfaces `score_v2`, `lockscore_v2`, `final_prob`, and `lockscore_prob` emitted in `analyzer_v2_per_item/top_candidates`; optional `drop_only_multiplier` guard in `scoring_v2.guards` (default 1.0, currently 0.9) gently de‑emphasises **pure** drop‑vtrac hits without touching VT/family VT/exact evidence.
- Six June workbooks (history 2025‑06‑20/21/22/24/25/26) plus results (21/22/23/25/26/27) show a stable environment pattern: CT/FL/IN/PA/NJ/MI (often NC/VA/ON) repeatedly present rich long-string + VT corridors with LS2 support, while OH (and often NY) remain weak or noisy. Primary/support/skip classifications for each date are captured in `AAT9_Digit_Analysis_Log_Part2.md`.
- Winners HTML/JSON and DR’s VT features are aligned: boxes carrying the key winner VTRAC families across variants (Midday/Evening/Combined) are consistently high-ranked when supported by VT/family VT/exact, and VT-only days are handled cleanly; noisy VT/drop-heavy environments still require thresholds but no longer dominate rankings via drop‑only boxes.
- Aggregator guidance: treat the current DR outputs (per_item/top/meta + winner maps/flags) and the environment classifications in `AAT9_Digit_Analysis_Log_Part2.md` as the “final” Digit Reduction baseline when wiring the master validation and cross-tool scorer; any further VT or environment gating should happen in the Aggregator layer, not by changing DR’s internal features.

## Hotzones (Future Module)

_No entries yet — append new insights here._


## Cross-Tool Aggregator / Analysis Module

_No entries yet — append new insights here._


## General Notes

_No entries yet — append new insights here._
- 2025-11-03 update: Analyzer bundles are now lean (per_item, top_candidates, meta, stacked HTML) with winners JSON/flags produced only by the Control Center module; reducer steps optional.
