# VTRAC Analyzer Handoff

Date: `2026-03-16`

## Current Role

`VTRAC Analyzer` should now be treated as:

- a lane / family / straight evidence feed
- a cross-section corroboration feed
- a winners-lens audit partner

It should **not** be treated as a tiny top-k direct-caller oracle.

## Predictive-Side Artifacts To Feed The Arena

Primary:

- enhanced analyzer bundle JSON
  - `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`

Preferred global compact layer when present:

- `vtrac_compact_report.json`
- `vtrac_compact_report.csv`

Key evidence to preserve:

- `indices_ranked`
- `straights_ranked`
- `top_straights`
- `section_summaries`
- `telemetry`
- `top_indices_by_state` from the compact layer when available

## Audit-Only Winners Lens

Keep outside predictive mode:

- winners HTML
- winners JSON
- winner index placement diagnostics
- validation reports

These remain the truth layer for review, not the predictive feed.

## Most Valuable Arena Contribution

VTRAC’s best arena contribution is:

- `cross_variant_lane_strength`
- `straight_lane_quality`
- `vt_only_lane_confidence`
- `lane_dominance`
- `section_lead_profile`
- `mask_drop_lane_reveal`
- `mirror_double_lane_support`

## One Bounded Finish Still Worth Doing

If any final slice is taken, it should be:

- contract/lean-output finalization
- compact-report smoke validation

Not:

- another broad scorer rescue cycle

## Validation Closeout

The compact-report smoke validator already exists:

- `scripts/tools/validate_vtrac_compact_report.py`

It was smoke-run successfully on representative gold-day dates:

- `2025-06-21`
- `2025-12-31`

Observed result:

- compact report present
- non-empty `states`
- non-empty `sections`
- `scorer_version=0.4.0`

That means the bounded closeout is now a documentation/contract problem, not a missing-validator problem.

## Freeze Criteria

Freeze `VTRAC Analyzer` for this phase when:

1. the predictive-side ingest artifacts are explicit
2. the winners lens is clearly marked audit-only
3. the compact-report contract is validated
4. no new bounded lane-lift hypothesis is clearly better than the current handoff

## Recommended Next Step After Freeze

Move VTRAC into the aggregated analysis arena as a lane-semantics feed and judge any remaining gap there before reopening the analyzer.
