# AAT9 Analysis Insights

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
