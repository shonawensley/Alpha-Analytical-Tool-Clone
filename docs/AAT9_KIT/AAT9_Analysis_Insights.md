[*] DO NOT REMOVE EXISTING ENTRIES — APPEND NEW INSIGHTS ONLY

# AAT9 Analysis Insights
## Stable Pattern Extractor

_No entries yet — append new insights here._


## Long String / Digit Reduction

_No entries yet — append new insights here._


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


## Hotzones (Future Module)

_No entries yet — append new insights here._


## Cross-Tool Aggregator / Analysis Module

_No entries yet — append new insights here._


## General Notes

_No entries yet — append new insights here._
