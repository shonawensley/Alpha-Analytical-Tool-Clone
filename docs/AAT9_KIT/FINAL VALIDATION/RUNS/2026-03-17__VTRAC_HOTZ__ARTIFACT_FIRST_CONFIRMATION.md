# VTRAC + Hot Zones Artifact-First Confirmation

Date: `2026-03-17`

## Purpose

Re-run the `winner-artifact-first` method on `VTRAC Analyzer` and `Hot Zones`
before freezing their arena contribution, and verify whether the earlier closeout
compressed the tool contracts too aggressively.

This pass was **not** a scorer-rewrite pass.

It was a bounded confirmation pass answering:

1. are the current handoff conclusions directionally right?
2. did we preserve enough of the concrete evidence the tools already expose?
3. should the next move be tool-local tuning or contract broadening?

## Scope

Artifacts reviewed directly:

- `sharepacks/2025-06-21/Virginia4/...`
- `sharepacks/2025-12-31/.../vtrac_compact_report.{json,csv}`
- `sharepacks/2026-01-03/Florida4/...`

Primary anchor pairs:

- `Virginia4` `2025-06-21`
  - VTRAC winner `473` / index `30`
  - Hot Zones winners `473` and `016`
- `Florida4` `2026-01-03`
  - VTRAC winner `611` / index `16`
  - Hot Zones winners `708` and `611`

Additional compact-report confirmation:

- `Connecticut4`
- `Virginia4`
- `Florida4`

## Method

Used the locked review method in:

- `2026-03-16__TOOL_REVIEW_METHOD__WINNER_ARTIFACT_FIRST.md`

Meaning:

1. inspect winner artifacts first
2. inspect current predictive outputs second
3. classify the gap
4. update the arena contract only if the artifacts prove the tool already carries more useful semantics than the current contract preserves

## Executive Read

The previous handoff was directionally correct, but it was compressed.

The right updated conclusion is:

- `VTRAC Analyzer` does **not** need another broad scorer loop
- `Hot Zones` does **not** need another guard/weight loop
- both tools **do** need a broader arena contract than the `2026-03-16` version captured

The gap is now primarily:

- `arena_contract_gap`

not:

- `tool_rewrite_gap`

## VTRAC Findings

## 1. The current VTRAC direction was right

The prior handoff was correct that VTRAC is strongest as:

- a lane/index lens
- a straight-neighborhood lens
- a cross-section corroboration feed

The artifact-first review did **not** suggest another top-caller tuning cycle.

## 2. The current contract was too abstract

The current contract named the right semantic areas:

- `cross_variant_lane_strength`
- `straight_lane_quality`
- `vt_only_lane_confidence`
- `lane_dominance`
- `section_lead_profile`
- `mask_drop_lane_reveal`
- `mirror_double_lane_support`

But the anchor review showed that this contract is missing too many of the
concrete evidence families already present in the live artifacts.

### Concrete families confirmed as valuable

From `vtrac_compact_report.csv`:

- `overlap`
- `stable_cols_count`
- `stable_cols`
- `consensus_col1`
- `consensus_col2`
- `cross_section_echo`
- `hot_count`
- `superhot_count`
- `mask_drop`
- `mirror_supported`
- `double_hits`
- `confidence_score`
- `tier`
- `flags`
- `top_tokens`
- `recommended_tokens`
- `top_straights`
- `section_prior`
- `state_prior`
- `why`
- `source`

From enhanced JSON:

- `indices_ranked[].index`
- `indices_ranked[].score`
- `indices_ranked[].evidence`
- `indices_ranked[].straights`
- `straights_ranked[].straight`
- `straights_ranked[].index`
- `straights_ranked[].score`
- `straights_ranked[].reasons`
- `top_straights`
- `section_summaries.<section>.hot_count`
- `section_summaries.<section>.superhot_count`
- `section_summaries.<section>.consensus_col1`
- `section_summaries.<section>.consensus_col2`
- `section_summaries.<section>.stable_columns`
- `section_summaries.<section>.top_box_signatures`
- `section_summaries.<section>.ring_votes`
- `section_summaries.<section>.analyzer_metrics.indices_considered`
- `section_summaries.<section>.analyzer_metrics.mask_drop_count`
- `section_summaries.<section>.analyzer_metrics.reduction_hits`
- `section_summaries.<section>.analyzer_metrics.mirror_supported`
- `section_summaries.<section>.analyzer_metrics.double_hits`
- `section_summaries.<section>.analyzer_metrics.top_straights`
- `telemetry.weights`
- `telemetry.mask_digits`

From winners HTML / JSON:

- `pattern_occurrence`
- `pattern_persistence`
- `pattern_stability`
- `straight_counts`

The winners-layer stats remain audit-only, but they strongly justify preserving
the predictive-side signals that correspond to them.

## 3. The artifacts showed why the broader contract matters

### Virginia4 `473`

The winner HTML / JSON for index `30` showed:

- strong pattern occurrence/persistence/stability concentration inside the winning index
- same-index neighborhood structure like `437`, `734`, `847`
- this is exactly the kind of lane-neighborhood truth the predictive contract should preserve

At the predictive side, the enhanced JSON already preserved:

- section-level hot/superhot counts
- stable columns
- ring votes
- top box signatures
- analyzer metrics

So the problem is **not** that VTRAC lacks semantics.
The problem is that the earlier contract described them too loosely.

### Florida4 `611`

The winner HTML / JSON for index `16` showed:

- `611` and `661` dominating the winner index
- `166` and `116` as weaker same-index shoulders
- a clear example of family asymmetry inside a winner index

That means the arena should preserve:

- same-index straight neighborhood structure
- not just a single “lane is alive” boolean

## 4. VTRAC confirmation judgment

The correct VTRAC finish is:

- **no broad scorer retune**
- **yes to a broader arena contract**
- **yes to preserving the concrete supporting descriptors behind the semantic rollups**

## Hot Zones Findings

## 1. The current Hot Zones direction was right

The prior handoff was correct that Hot Zones is strongest as:

- a late-tail pressure extractor
- a vertical-support / survivorship extractor
- a lane/index corroboration feed

The anchor review did **not** justify another weight-sweep loop.

## 2. The current contract was too abstract

The current contract named the right semantic areas:

- `late_tail_pressure_strength`
- `superhot_echo_strength`
- `vertical_repeat_strength`
- `rowtype_span_support`
- `precol1_funnel_strength`
- `col1_arrival_strength`
- `vt_only_lane_pressure`
- `repeat_3value_score`
- `consensus_column_signal`
- `set1_funnel_density`

But the current contract did not preserve enough of the concrete count families
and evidence tags that actually make those semantics inspectable and later
aggregatable.

### Concrete families confirmed as valuable

From `*_hot_zones_top_lanes.csv`:

- `triad`
- `vt_triad`
- `support_count`
- `hot_hits`
- `superhot_hits`
- `vertical_hits`
- `set1_hits`
- `col1_hits`
- `precol1_hits`
- `vt_straight_hits`
- `vt_only_lane_hits`
- `guard_hits`
- `literal_hits`
- `variant_span`
- `set_span`
- `column_span`
- `score_mean`
- `score_max`
- `evidence_tags`

From `*_hot_zones_per_lane.csv`:

- `section`
- `set_name`
- `draw_name`
- `column_index`
- `triad`
- `vt_triad`
- `vertical_support`
- `horizontal_span`
- `set_span`
- `variant_echo`
- `has_straight`
- `has_vt_straight`
- `vt_only_lane`
- `col1_arrival`
- `precol1_funnel`
- `ls_col_42`
- `ls2_lane`
- `is_starred`
- `star_count`
- `is_superhot_slot`
- `is_set1`
- `guard_injected`
- `score`
- `reasons`

From `*_hot_zones_meta.json`:

- `date`
- `guard_triads_top20`
- `guard_triads_total`
- `json_source`
- `per_item_rows`
- `top_rows`
- `state`

From winner-map outputs:

- compact top20+guard snapshot presence
- useful for audit/coverage
- not enough by itself to define the predictive feed

## 3. The artifacts showed why the broader contract matters

### Virginia4 `473`

`347` ranked only `83/208` in `top_lanes`, which is exactly why a top-rank-only
view would under-read Hot Zones.

But the same row also carried:

- `support_count = 51`
- `hot_hits = 51`
- `superhot_hits = 13`
- `vertical_hits = 4`
- `set1_hits = 43`
- `precol1_hits = 9`
- `vt_straight_hits = 12`
- `vt_only_lane_hits = 8`
- `variant_span = 3`
- `set_span = 3`
- `column_span = 7`

That is a strong pressure/survivorship object.
The current abstract contract does not preserve enough of this numeric texture.

### Florida4 `611`

`116` ranked only `31/210`, but still carried:

- `support_count = 16`
- `hot_hits = 16`
- `vertical_hits = 4`
- `set1_hits = 9`
- `vt_straight_hits = 12`
- `vt_only_lane_hits = 4`
- `variant_span = 2`
- `set_span = 3`
- `column_span = 4`

Again, this is meaningful pressure structure even though it is not a top-10 lane.

This is the same lesson as DR:

- top-band rank is not the whole truth
- the arena should preserve the richer object

## 4. Hot Zones confirmation judgment

The correct Hot Zones finish is:

- **no broad guard/weight retune**
- **yes to a broader arena contract**
- **yes to preserving explicit count families, spans, and raw evidence tags**

## Combined Judgment

The artifact-first confirmation supports all of the following:

1. the earlier VTRAC/Hot Zones handoff was directionally right
2. neither tool should be reopened for another broad tuning loop
3. both arena contracts were too compressed
4. the next move should be broader contract preservation, not scorer thrash

## Recommended Action

1. broaden `2026-03-16__VTRAC_HOTZ__ARENA_CONTRACT.md`
2. carry the broadened contract forward into the per-tool master arena-feed document
3. only reopen tool-local tuning later if the aggregated arena proves a specific missing rule

## Stop Condition

After the contract broadening is recorded, both tools can still be treated as
effectively wrapped for this phase.

The result is:

- broader preservation
- higher confidence
- no unnecessary analyzer churn

That is the optimal finish.
