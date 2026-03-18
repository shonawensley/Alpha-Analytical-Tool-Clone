# AAT9 Aggregated Analysis Arena Contract v0

Purpose: define the first real runtime arena object that sits between tool outputs and downstream conversion / play-card packaging.

This contract is intentionally:
- predictive-safe
- budget-blind
- broad enough for example review
- narrow enough to be implemented as one concrete per-state artifact

This document does not replace the existing feed contracts.
It consumes them.

Authoritative source contracts:
- `AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `AAT9_Analyzer_Lean_Outputs.md`

Related workflow shell:
- `AAT9_Master_Validation_Analysis_Navigator.md`
- `2026-03-16__TOOL_REVIEW_METHOD__WINNER_ARTIFACT_FIRST.md`

## Role In The System

The aggregated arena is the missing inner analysis layer:

1. tools emit evidence
2. the aggregated arena preserves that evidence in one object
3. arena review compares that object against winners / results
4. later layers decide conversion and combination-forming

It is not:
- Candidate Universe
- Play Card
- B12/B24/B36 packaging
- budget policy

Those remain downstream consumers / controls until arena-native replacements are proven.

## Runtime Artifact

Per-state output:

- `sharepacks/<ROOT>/<D>/<STATE>/analysis/aggregated_analysis_arena__<PROFILE>__<EXPERIMENT>.json`
- optional markdown twin:
  - `sharepacks/<ROOT>/<D>/<STATE>/analysis/aggregated_analysis_arena__<PROFILE>__<EXPERIMENT>.md`

Example:
- `sharepacks/_predictive/2026-03-15/NorthCarolina4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`

## Required Top-Level Namespaces

The v0 object must contain:

1. `schema_version`
2. `metadata`
3. `provenance`
4. `string_tools`
5. `context_tools`
6. `cross_tool_relations`
7. `arena_synthesis`
8. `downstream_handoff`
9. `review_links`

## Metadata

`metadata` carries the runtime identity of the arena snapshot:
- `generated_at`
- `results_date`
- `history_date`
- `profile`
- `experiment_tag`
- `state_key`
- `sharepack_root`
- `sharepack_state_dir`
- `contains_winners_artifacts`

## Provenance

`provenance` must make the artifact auditable:
- `inputs_hash`
- `evidence_paths`
- `source_status`
- `contract_refs`

`source_status` should show, per tool/context layer:
- `available`
- `source_mode`
  - `rebuilt_from_raw`
  - `loaded_prebuilt`
  - `raw`
  - `missing`
- `source_path` or `source_paths`

## String Tools

`string_tools` preserves the main structural evidence layers:

- `stable`
- `digit_reduction`
- `vtrac_analyzer`
- `hot_zones`

The arena should preserve the strongest tool-specific structures rather than collapsing them to a tiny top-N board.

Expected v0 preservation posture:
- Stable: sectioned row / compound / family / frontier evidence
- Digit Reduction: sectioned trace / lane / empty-lens / gateway / cluster / assigned-box / fusion evidence when available
- VTRAC: ranked indices, ranked straights, section summaries, telemetry hints, optional day compact-report context
- Hot Zones: top lanes, per-lane drill rows, meta counts, evidence tags, VT/literal lane context

## Context Tools

`context_tools` preserves reinforcement / corroboration layers without letting them manufacture string truth.

Expected v0 namespace:
- `aux_control_center`

That wrapper should preserve the already-defined Aux / Control Center arena objects, including:
- positional pressure
- VTRAC pressure
- badge pressure
- pair / combo context
- due doubles
- repeat watch
- sums
- Blackapple
- profit alerts
- compound events
- tracker context

## Cross-Tool Relations

This namespace is where the aggregated arena becomes more than a raw bundle.

The first v0 relations should be review-oriented, not final policy:
- `canonical_consensus_top`
- `vtrac_index_consensus_top`
- `family_consensus_top`
- `regime_flags`
- `contradiction_flags`

These relations should answer:
- where multiple tools point to the same canonical / family / VTRAC lane
- where context reinforces string truth
- where the environment is split, diluted, or double-heavy

They should not yet decide budget or final pack geometry.

## Arena Synthesis

This namespace is the review surface for Brain 1.

Expected v0 contents:
- `dominant_canonicals`
- `dominant_vtrac_indices`
- `dominant_families`
- `context_reinforced_canonicals`
- `context_only_pressure`
- `state_regime`
- `review_prompts`

These are hypothesis-driving summaries for example review, not final play-card outputs.

## Downstream Handoff

This namespace is intentionally narrow.

It exists to compare the arena with downstream baseline consumers:
- `candidate_universe`
- `play_card`

The handoff may include:
- file paths
- schema version
- counts
- preview rows
- strategy names

It must not let current downstream packaging redefine the arena object.

## Review Links

This namespace is for fast review navigation:
- winners paths when present
- signals bundle path when present
- tool root dirs
- control-center meta path

The purpose is to make arena-vs-winner review operational without re-spelunking the sharepack.

## Predictive-Safe Boundary

When the sharepack root is predictive:
- the arena must not depend on winners artifacts
- `contains_winners_artifacts` must be `false`
- winners links may be empty

When the sharepack root is results/frozen:
- winners links may be populated for review
- the evidence surfaces must still remain predictive-side in meaning

## Non-Goals For v0

v0 does not:
- redesign analyzers
- redesign Candidate Universe
- redesign play-card geometry
- redesign budget policy
- finalize arena-native conversion logic

v0 only establishes the real runtime arena object and enough synthesis to review it coherently.

## Pilot Success Criteria

The first pilot is successful if:
- a per-state aggregated arena object exists
- it preserves the intended tool/context evidence families
- a reviewer can compare it against winners without reopening every raw folder first
- it becomes possible to classify gaps as:
  - arena missing
  - arena present but underweighted
  - conversion gap
  - budget / packaging gap
