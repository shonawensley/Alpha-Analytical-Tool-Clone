# AAT9 Analysis Arena - Window Replay Comparison Design

Date: `2026-04-21`

Status: `design_stub`

Runtime effect: none

## Purpose

This document defines how to compare an existing Analysis Arena window baseline
against a rerun or archived replication output without confusing that evidence
with true fresh confirmation.

Use this with:

- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`

## Required Inputs

Before comparing two runs, record:

- `baseline_run_label`
- `rerun_run_label`
- `evidence_tier`
- `window_start`
- `window_end`
- `baseline_system_checkpoint`
- `rerun_system_checkpoint`
- `history_source_status`
- `core_results_status`
- `decay_tail_status`
- `bonus_ball_sidecar_status`
- `truth_sharepack_status`
- `expected_allowed_conclusions`
- `expected_blocked_conclusions`

## Baseline Manifest

The replay-readiness report stores key artifact paths and SHA-256 hashes for the
existing window root. Those hashes are not a prediction metric. They are a
preservation and comparison contract.

For same-window replay, keep the old window package intact and write the rerun
to a separate label or namespace before comparing.

For archived-window replication, use the manifest to explain which historical
artifact family was available before the modern rerun.

## Comparison Categories

Every material difference should be classified as one of:

- `unchanged`
- `improved_traceability`
- `newly_exposed`
- `degraded`
- `contradicted`
- `renamed_or_reclassified_only`
- `blocked_by_missing_data`

These categories are deliberately descriptive. They do not grant live scoring,
candidate generation, budget, or Stage 8 permission.

## Stage 6B Through Stage 7B Targets

When comparing March against a rerun or archived replication, prioritize:

- Stage 6B scenario decisions
- Stage 6B lane increment matrix
- Stage 6B support modifier ablation
- Stage 6B restraint calibration
- Stage 6B concentration audit
- Stage 6B guardrail compliance
- Stage 6B readback scenario decisions
- Stage 6B readback requirement results
- Stage 6C confirmation test matrix
- Stage 6C rewrite blockers
- Stage 6D restraint bucket posture
- Stage 6E support narrowing posture
- Stage 6F lane decision atlas
- Stage 6F active blockers and clearance
- Stage 6F fresh-window carry-forward queue
- Stage 7A confirmation requirements
- Stage 7A March seed benchmarks
- Stage 7B queue replay status
- Stage 7B requirement coverage
- Stage 7B blocker recheck

## Interpretation Rules

Same-window replay can prove reproducibility, regression safety, improved
traceability, or changed output behavior on known evidence. It cannot prove a
signal generalizes.

Archived-window replication can show that a March-derived finding appears or
fails under other historical conditions. It still cannot replace true fresh
confirmation.

True fresh confirmation remains the only path that can support Stage 8A
consideration, and only after March Stage 7B is compared against fresh Stage 7B.

## Blocked Uses

Do not use this comparison design to:

- overwrite the March baseline without a preserved copy
- treat same-window replay as fresh confirmation
- treat archived-window replication as Stage 8 permission
- activate new scoring weights
- alter Candidate Universe, Play Card, translator, or budget behavior
- blend bonus-ball sidecar truth into standard straight or boxed metrics
