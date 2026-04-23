# AAT9 Analysis Arena - Replay Plan Guardrail Check

## Verdict

- status: `pass`
- stage8_permission: `blocked`
- checks: `14/14` passed
- failed: `0`
- csv: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK.csv`

## Evidence Boundary

- Same-window replay remains regression/reproducibility evidence only.
- Canonical replacement-cycle comparison is mandatory for same-window replay.
- Fresh-window confirmation is still required before Stage8 or downstream scoring/candidate/budget rewrite work.

## Replacement Cycle

- `WINDOW_2025-12-30_to_2026-01-04`
- `WINDOW_2026-01-05_to_2026-01-09`
- `WINDOW_2026-01-15_to_2026-01-22`
- `WINDOW_2026-03-09_to_2026-03-23`

## Checks

| Check | Status | Detail |
|---|---:|---|
| `G01_replacement_windows_exact` | `pass` | Candidate replacement cycle must use the canonical non-overlap evidence set. |
| `G02_no_superseded_or_snapshot_windows` | `pass` | Snapshots and superseded overlapping windows must not enter replacement-cycle promotion evidence. |
| `G03_baseline_window_replaced` | `pass` | The candidate cycle must replace the replayed baseline window rather than appending duplicate March evidence. |
| `G04_no_unexpected_execution_prep_blockers` | `pass` | Completed Run2 artifacts may block rerun-in-place; other blockers indicate prep drift. |
| `G05_stage8_blocked_in_prep` | `pass` | Same-window replay planning must never grant Stage8/live downstream permission. |
| `G06_stage2b_canonical_replacement_command` | `pass` | Stage2B must build the candidate cycle from explicit canonical windows. |
| `G07_stage3_explicit_window_roots` | `pass` | stage3-decision-workbench must receive explicit replacement-cycle window roots. |
| `G08_stage4_explicit_window_roots` | `pass` | stage4-fixture-replay must receive explicit replacement-cycle window roots. |
| `G09_stage5_explicit_window_roots` | `pass` | stage5-shadow-evaluator must receive explicit replacement-cycle window roots. |
| `G10_comparison_uses_canonical_mix` | `pass` | Final comparison must point at the canonical mix candidate cycle and require candidate completeness. |
| `G11_comparison_complete_clean` | `pass` | March Run2 should remain deterministic replay confirmation, not a changed-evidence signal. |
| `G12_comparison_no_fresh_unlock` | `pass` | Same-window replay can support regression confidence only, not fresh confirmation or Stage8 unlock. |
| `G13_fresh_window_readiness_boundary` | `pass` | System may proceed to fresh-window evidence collection while keeping Stage8 blocked. |
| `G14_stage7b_read_only_ready` | `pass` | Stage7B can guide confirmation replay but cannot authorize scoring rewrite. |
