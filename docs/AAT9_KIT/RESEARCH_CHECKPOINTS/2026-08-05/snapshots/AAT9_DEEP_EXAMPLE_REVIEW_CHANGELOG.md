# AAT9 Deep Example Review Changelog

Purpose
- Record system fixes and semantic clarifications discovered during Master Deep Example Review work.
- Separate runtime fixes from review-template notes and from artifacts that require regeneration.
- Preserve the reason each change was made so final-system development does not lose the review context.

## 2026-07-08 - VTRAC Semantics Stabilization

Trigger
- Connecticut4 `2026-03-09` VTRAC review exposed confusion between boxed VTRAC index, full index corridor, ordered VSTRAIGHTS lane, literal permutations, and renderer tags.
- The specific failure mode was `091` being routed through boxed index `9` to representative `v125` in an ordered-lane context.

Runtime Changes
- Added ordered VSTRAIGHTS helpers in `modules/vtrac_straight_map.py`.
- Patched `scripts/tools/export_control_center_sharepack.py` so A05/A12 ordered straight lanes use literal order directly.
- Reclassified A09 VTRAC repeat risk as `VT_INDEX_CORRIDOR` when only boxed-index evidence exists.
- Patched `scripts/tools/create_candidate_universe.py` so `ImpliedSet` accepts only exact Pick-3 literals from external candidate arrays.
- Patched `scripts/tools/cc_sanity_snapshot.py` so it no longer passes boxed index into `get_index_straights`.
- Tightened `scripts/tools/validate_profit_alerts_contract.py` so any present `ImpliedSet` member must be Pick-3.

Regression Coverage
- Added `tests/test_vtrac_straight_semantics.py`.
- Locked examples:
  - `091 -> v152 -> 041,046,091,096,541,546,591,596`
  - `019 -> v125 -> 014,019,064,069,514,519,564,569`
  - `901/906 -> v512 -> 401,406,451,456,901,906,951,956`
  - `168 -> v224 -> 113,118,163,168,613,618,663,668`
  - `v125` rejected from playable candidate arrays
  - boxed index `9` remains valid for `091,019,591,906,901,096`

Artifact Interpretation
- Existing March sharepack artifacts are historical outputs. They do not change until regenerated.
- Future Control Center exports will no longer use a boxed-index representative as an ordered VSTRAIGHTS lane.
- Existing winner HTML/JSON `hit-vt-straight` remains a legacy narrow renderer tag and should not be treated as full VTRAC corridor evidence.
- Existing VTRAC Enhanced JSON remains the primary VTRAC Analyzer evidence source; compact reports remain secondary/global feed artifacts.

Not Fixed In This Pass
- Winner HTML/JSON does not yet expose a full VTRAC corridor summary.
- Analysis Arena still preserves a bounded top slice of VTRAC Enhanced output rather than full corridor diagnostics.
- VTRAC Enhanced straight scoring still depends on `order_counts` extracted from exact indexed literals found in its predictive scan.
- No scoring weights were changed.
- Stable, Digit Reduction, Hot Zones, and VTRAC Enhanced engine scoring were not rewritten.

Next Review/Fix Candidates
- Add a full VTRAC corridor summary for winner-lens and deep-review use.
- Add explicit fields for:
  - boxed index corridor exposure
  - ordered VSTRAIGHTS lane exposure
  - literal permutation exposure
  - strongest straight witnesses by variant/set/column zone
- Decide whether Analysis Arena should preserve this corridor summary as a first-class VTRAC object.
- Clarify or rename legacy `hit-vt-straight` renderer tags as pair-run/two-VTRAC markers.

## 2026-07-08 - VTRAC Corridor Summary Diagnostic

Trigger
- The Section A Method 3 conversion needed a reliable way to distinguish ordered VSTRAIGHTS evidence from broader boxed-index VTRAC corridor evidence.
- The Connecticut4 `091` case showed strong human-visible VTRAC corridor evidence while legacy `hit-vt-straight` tags remained absent.

Review-Only Additions
- Added `scripts/tools/create_vtrac_corridor_summary.py`.
- Added `tests/test_vtrac_corridor_summary.py`.
- Generated review-only Connecticut4 `091` artifacts:
  - `docs/AAT9_KIT/FINAL VALIDATION/DEEP_EXAMPLE_REVIEW_PREP/VTRAC_CORRIDOR_SUMMARIES/2026-03-09__Connecticut4__091__VTRAC_CORRIDOR_SUMMARY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/DEEP_EXAMPLE_REVIEW_PREP/VTRAC_CORRIDOR_SUMMARIES/2026-03-09__Connecticut4__091__VTRAC_CORRIDOR_SUMMARY.json`

Diagnostic Findings
- `091` maps to ordered lane `v152` and boxed VTRAC index `9`.
- Ordered lane `v152` members: `041,046,091,096,541,546,591,596`.
- Boxed index `9` has six ordered lanes and a full corridor of `48` playable literals.
- Winner JSON exposure:
  - literal permutations: `63` strict cells
  - ordered lane: `16` strict cells
  - boxed-index corridor: `134` strict cells
- Top ordered-lane witnesses: `591` x14, `096` x2.
- Top same-index witnesses: `906` x38, `019` x30, `901` x24, `591` x14, `401` x10, `109` x9.
- `renderer_gap=True`: full corridor evidence exists, but legacy `hit-vt-straight` tags total `0`.
- `analyzer_gap=True`: VTRAC Enhanced preserved boxed index `9` but did not carry positive order-counts for exact ordered lane `v152`.

Template Updates
- Updated `tasks/MASTER_DEEP_REVIEW_SECTION_A_METHOD_CONVERSION__2026-03-09__CONNECTICUT4__091.md`.
- Updated `tasks/MASTER_DEEP_EXAMPLE_REVIEW__SECTION_A_BRAINSTORM_NOTES.md`.
- Future Section A Method 3 must explicitly extract:
  - `ordered_vcode`
  - `ordered_lane_8`
  - `boxed_corridor_48`
  - `top_ordered_lane_witnesses`
  - `top_same_index_witnesses`
  - `renderer_gap_flag`
  - `analyzer_gap_flag`

Not Changed
- No VTRAC Enhanced scoring rewrite.
- No winner HTML renderer rewrite.
- No predictive Arena JSON mutation.
- No March window regeneration.

## 2026-07-08 - VTRAC Follow-Up Scope Clarification

Trigger
- While comparing Section A winner-lens analysis with Section B VTRAC Analyzer outputs, the CT4 `091` case exposed two separate issues:
  - old winner-lens VTRAC statistics can include `draw_data` rows,
  - VTRAC Enhanced preserves useful index and straight-candidate evidence but does not yet expose full ordered-lane / corridor metrics as first-class fields.

Clarification
- `draw_data` rows are raw draw context, not R2/R4/R6/R8 pattern-progression rows.
- Future winner-lens and corridor metrics should default to `pattern_rows_only` for predictive scoring and optionally report `draw_data` as support/context.
- VTRAC Enhanced remains useful: it ranked index `9` at rank `5` for CT4 `091` and preserved cross-section, set, column, streak, hot/superhot, mask-drop, and straight-candidate evidence.
- The gap is not “VTRAC Enhanced is useless.” The gap is that it does not yet expose Section A style ordered VSTRAIGHTS lane/corridor analysis in a complete, first-class way.

New Ledger Entries
- Added `VTRAC-006 - Winner-Lens VTRAC Statistics Should Exclude draw_data`.
- Added `VTRAC-007 - Enhanced VTRAC Should Add First-Class Corridor / Ordered-Lane Metrics`.

Development Implication
- The Master Deep Review is functioning as intended: Section A identifies high-value winner-extraction structure, Section B checks whether the current system/tooling captured it, and gaps become fix/enhancement candidates for the final Arena-native analysis layer.

## 2026-07-09 - VTRAC Corridor Objects Added To Arena Preservation

Trigger
- Section A / Section B comparison showed that VTRAC Enhanced preserved useful index and straight evidence, but the Aggregated Arena did not expose ordered VSTRAIGHTS lanes or boxed VTRAC corridors as first-class review objects.
- ChatGPT Pro review agreed with the bounded path: improve observability/preservation first; do not retune scoring or regenerate March artifacts yet.

Runtime / Review Changes
- Extended `scripts/tools/create_vtrac_corridor_summary.py` with row-scope breakout:
  - `pattern_rows_only`
  - `draw_data_only`
  - `all_rows_inclusive`
- Added row-scope flags for `pattern_row_corridor_present`, `ordered_lane_pattern_row_present`, `draw_data_corridor_support`, and `draw_data_inflation_warning`.
- Extended `scripts/tools/build_aggregated_analysis_arena.py` so `string_tools.vtrac_analyzer.arena_objects` now preserves:
  - `ordered_lane_corridors`
  - `boxed_index_corridors`
  - `semantic_guardrails`
- The Arena object is predictive-safe: it is derived from VTRAC Enhanced inputs only and does not use winner artifacts.

Guardrails
- VTRAC Enhanced scoring was not rewritten.
- Winner HTML rendering was not rewritten.
- No scoring weights were changed.
- Existing March sharepacks and generated predictive artifacts were not regenerated.
- Candidate lists still treat `v###` labels as metadata, not playable Pick-3 literals.

Regression Coverage
- Extended `tests/test_vtrac_corridor_summary.py`.
- Extended `tests/test_aggregated_analysis_arena.py`.
- Confirmed focused VTRAC/Arena tests passed.

## 2026-07-27 - Classic Due-Doubles Review Surface And Source Guards

Trigger
- Deep Review needed the original human-readable relationship between top due
  repeated pairs and their red boxed combinations without replacing the
  existing advanced family-pressure table.

Review / UI Additions
- Added `src/core/classic_due_doubles.py` as a pure calculation layer.
- Added `Doubles Table #2` beneath the current Control Center family table.
- Ranks four repeated pairs from Combined 360-draw history.
- Lists red-only canonical boxes from complete 1,000-draw C/M/E histories.
- Preserves source labels and groups multi-variant boxes into green convergence
  tokens such as `244 C-M-E`.
- Adds a 12-box Top-4 due-pair closure and a complete draw-source manifest.
- Added a three-state inspection preview at
  `.codex/doubles_table_2_three_state_preview.html`.

Data-Integrity / Rendering Fixes
- Replaced fuzzy draw-source substring matching with exact normalized-state
  matching in `modules/aux_loaders.py`.
- Preserved the established `OntarioCanada -> Ontario` alias.
- Missing West Virginia Midday now remains missing instead of borrowing
  `Virginia_Midday_draws.csv`.
- Made the Control Center path-handler import unconditional so the page no
  longer falls into the rescue screen before rendering its tables.

Regression Coverage
- Added `tests/test_classic_due_doubles.py`.
- Extended `tests/test_aux_loaders_variants.py` with West Virginia isolation and
  Ontario alias cases.
- Independently reconciled Connecticut, Florida, and Ontario red boxes against
  raw CSV histories.
- Confirmed those results match the existing advanced family ranker.
- Confirmed all 18 current state rows build and Control Center executes through
  Streamlit AppTest.

Scope Guardrails
- Existing family-pressure calculations were not changed.
- Existing `due_doubles.csv`, Candidate Universe, Play Card, Arena, cadence,
  tool scoring, and prediction infrastructure were not changed.
- Green is a visual multi-variant convergence label, not a new analytical
  score or predictive credit.
- The 12-box closure remains a review hypothesis until denominator and holdout
  evidence support downstream promotion.

## 2026-07-27 - Connecticut Semantic Calibration v1.1

Repair Scope
- Added an immutable, additive semantic-calibration layer for the Connecticut4
  Evening 091 completion.
- Preserved all 44 baseline files and changed no runtime, Arena, Brain 2,
  scoring, route member, or predictive artifact.
- Added explicit contracts, output schemas, deterministic generation, and
  adversarial validation under
  `phase1_execution/new_analysis_v1/semantic_calibration_v1_1`.

Calibrated Outputs
- Frozen 37 substantive analysis units before prose rendering.
- Mapped all 337 responsibilities once and answered all 153 authority
  questions explicitly.
- Split lineage into independent roots, tool views, transformations, Arena
  restatements, downstream descendants, context, and post-result diagnostics.
- Versioned and separated structural-pathway, system-influence,
  candidate-route, and failure/action ledgers.
- Added candidate burdens, true source widths, route objective grading, and
  responsibility/question/conclusion-level semantic diffs.
- Kept B36 canonical-box success separate from exact 091 absence and kept
  portfolio-default, selection, and funding as independent statuses.

Validation
- Semantic calibration: 20 checks passed, zero failures.
- New adversarial suite: 17 tests passed.
- Existing semantic-boundary suite: 20 tests passed.
- Generated output manifest: 38 records, zero hash mismatches.
- Protected baseline: 44 files, zero hash mismatches.
- Deterministic package fingerprint:
  `3a873207d4ce14fbe685d794c4d39c8b82067dfff9565dfa9cd9b27af7befdf1`.

Acceptance Boundary
- Codex recommendation: `READY_FOR_PRO_REVIEW`.
- Human analytical acceptance remains `PENDING_PRO_REVIEW`.
- No second case or runtime change is authorized until Connecticut human
  review, exact-positive control, and predeclared negative control are complete.
