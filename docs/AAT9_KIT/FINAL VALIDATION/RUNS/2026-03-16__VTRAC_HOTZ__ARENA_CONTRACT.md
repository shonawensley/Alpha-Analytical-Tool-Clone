# VTRAC + Hot Zones Arena Contract

Date: `2026-03-16`

## Purpose

Define what `VTRAC Analyzer` and `Hot Zones` should contribute to the analysis arena after their final review phase.

This is a tool-to-arena contract, not a play-card contract.

## Shared Principle

These tools should feed the arena as:

- structured evidence
- lane and pressure descriptors
- cross-variant context

They should **not** be forced to act like tiny direct-caller oracles.

Important guardrail after the `2026-03-17` artifact-first confirmation:

- the semantic arena objects below should be treated as **rollups over concrete payload families**
- they should **not** replace the raw count/tag/descriptor fields that already exist in the live artifacts

So for both tools the arena should preserve:

- high-level semantic meaning
- plus the concrete fields that make those meanings inspectable and scoreable later

## VTRAC Analyzer Contract

## Primary predictive-side ingest

Preferred evidence sources:

- enhanced analyzer bundle JSON
- compact report when present

Primary fields to preserve:

- ranked indices / lane summaries
- ranked straights
- per-straight reasons
- hot/superhot support
- recency / first-column pressure
- cross-section echo
- section profile / section strengths

### Concrete payload families to preserve

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

From compact report:

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

## VTRAC arena objects to preserve

- `cross_variant_lane_strength`
- `right_column_lane_stability`
- `vt_only_lane_confidence`
- `straight_lane_quality`
- `lane_dominance`
- `section_lead_profile`
- `mask_drop_lane_reveal`
- `mirror_double_lane_support`

These semantic objects should be backed by the concrete payload families above,
not substituted for them.

## VTRAC winners lens

Keep outside predictive mode:

- winners HTML / winners JSON / winner placement diagnostics

Useful audit-only families confirmed by the winner artifacts:

- `pattern_occurrence`
- `pattern_persistence`
- `pattern_stability`
- `straight_counts`

These remain the audit lens, not the predictive feed.

## VTRAC non-goal

Do not optimize VTRAC toward:

- “top-8 straight should directly win often”

That is not the right contract.

## Hot Zones Contract

## Primary predictive-side ingest

Preferred evidence sources:

- `*_hot_zones_top_lanes.csv`
- `*_hot_zones_meta.json`

Transitional compatibility source:

- predictive `*_hot_zones_winner_map.json`

Secondary deep-drill layer to keep reachable:

- `*_hot_zones_per_lane.csv`

### Concrete payload families to preserve

From `top_lanes.csv`:

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

From `per_lane.csv` (secondary/deep-drill, not the lightweight primary ingest):

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

From `meta.json`:

- `date`
- `guard_triads_top20`
- `guard_triads_total`
- `json_source`
- `per_item_rows`
- `top_rows`
- `state`

## Hot Zones arena objects to preserve

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

These semantic objects should be backed by the concrete count/span/tag families
above, not substituted for them.

## Hot Zones digest requirement

The most useful bounded finish for Hot Zones is likely:

- `hot_zones_summary_digest.csv`
- `hot_zones_ledger_all.csv`
- schema/manifest contract

This reduces the need to reopen heavy raw artifacts during arena review and validation.

## Hot Zones non-goal

Do not optimize Hot Zones toward:

- “top triads should behave like a small standalone straight oracle”

That is not the right contract.

## Shared Arena Interpretation

In the final arena:

- `VTRAC` should answer:
  - what lane / family / straight neighborhood is alive?
- `Hot Zones` should answer:
  - where is pressure surviving and tightening?

Together they describe:

- the active winner corridor
- its lane correctness
- its pressure / survivorship profile
- its cross-variant confirmation

Important refinement after artifact-first confirmation:

- `VTRAC` should carry both the semantic lane objects and the concrete lane descriptors that produced them
- `Hot Zones` should carry both the semantic pressure objects and the concrete count/span/tag descriptors that produced them

## Freeze Criteria

Freeze each tool for this phase when:

- the arena contract is explicit
- the predictive ingest files are clear
- one bounded final validator/contract pass is complete
- no strong new reusable tool-local rule remains

At that point, any further major lift should be sought in the aggregated analysis arena, not by reopening the individual analyzer loops.
