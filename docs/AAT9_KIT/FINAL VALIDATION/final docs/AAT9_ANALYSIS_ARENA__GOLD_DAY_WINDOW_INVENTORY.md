# AAT9 Analysis Arena - Gold-Day Window Inventory

Status: `canonical_reference`

Runtime effect: none

## Purpose

This is the plain-language reference for the finalized Analysis Arena gold-day
and window inventory. Use it when a future session, agent, or analyst needs to
understand which Pick3StatsC4 gold days are part of the active Analysis Arena
evidence package and how those days flow into results, decay, bonus-ball
sidecars, replay, and future development decisions.

This document is intentionally about the Analysis Arena version of the system,
not the older legacy/control-arm window history.

## Date Vocabulary

`Pick3StatsC4 gold day`

- The uploaded history workbook day used to generate predictive artifacts.
- For a results day `D`, the corresponding Pick3StatsC4 input is usually `D - 1`.
- Example: results day `2026-03-09` uses Pick3StatsC4 gold day `2026-03-08`.

`results window`

- The actual evaluated draw-result dates.
- This is the `WINDOW_<start>_to_<end>` range in `RUNS_2`.

`decay tail`

- Extra results coverage after the window end so the decay/carryover companion can score delayed resolution.
- Current default is `5` total upload days, same-day included.
- Therefore full tail coverage means results through `window_end + 4 days`.

`bonus sidecar`

- Optional Fireball / Wild Ball / Superball truth source under `data/results_bonus/<D>.txt`.
- It stays separate from core Pick 3 straight/boxed grading.

## Canonical Window Set

These are the finalized canonical Analysis Arena windows as of the Jan19
recovery and March Run2 canonical replay work.

| Canonical window | Evidence tier | Pick3StatsC4 gold-day range | Results window | Full decay / bonus tail | Role |
|---|---|---|---|---|---|
| `WINDOW_2025-12-30_to_2026-01-04` | `archived_window_replication` | `2025-12-29` to `2026-01-03` | `2025-12-30` to `2026-01-04` | `2025-12-30` to `2026-01-08` | Early-January archived replication window. |
| `WINDOW_2026-01-05_to_2026-01-09` | `archived_window_replication` | `2026-01-04` to `2026-01-08` | `2026-01-05` to `2026-01-09` | `2026-01-05` to `2026-01-13` | Second non-overlap early-January archived replication window. |
| `WINDOW_2026-01-15_to_2026-01-22` | `archived_window_replication` | `2026-01-14` to `2026-01-21` | `2026-01-15` to `2026-01-22` | `2026-01-15` to `2026-01-26` | Recovered January window; supersedes the shorter Jan15-Jan18 split. |
| `WINDOW_2026-03-09_to_2026-03-23` | `same_window_replay` / March reference | `2026-03-08` to `2026-03-22` | `2026-03-09` to `2026-03-23` | `2026-03-09` to `2026-03-27` | Comprehensive March reference window and Run2 replay baseline. |

Current machine reports agree with this set:

- `window-replay-readiness`: `4` scanned windows
- archived replication ready: `3`
- same-window replay candidates: `1`
- `fresh-window-readiness`: `4` canonical completed windows
- replay-plan guardrails: `14/14` checks passing

## Canonical Roots

The canonical window roots live under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`

The March Run2 candidate replay window lives under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`

The March Run2 canonical replacement-cycle root is:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`

## Excluded / Non-Canonical Artifacts

These artifacts may exist on disk, but they must not be treated as additional
independent evidence windows for Analysis Arena cross-window promotion.

| Artifact | Why excluded |
|---|---|
| `WINDOW_2026-01-15_to_2026-01-18` | Superseded by recovered `WINDOW_2026-01-15_to_2026-01-22`; including both double-counts Jan15-Jan18. |
| `WINDOW_2026-01-05_to_2026-01-09__PREALIGN_SNAPSHOT` | Snapshot/reference artifact only, not an independent window. |
| `REPLAY/archived_window_replay_v2_jan19_recovered/_scratch_initial_parent_analysis_arena_20260422` | Scratch recovery artifact from an initial wrong-layout attempt. |
| `REPLAY/archived_window_replay_v2_jan19_recovered/WINDOW_2026-01-15_to_2026-01-22/_scratch_flat_postrange_attempt_20260422` | Scratch recovery artifact from a flat postrange attempt. |
| June 2025 material | Not part of the current canonical Analysis Arena evidence set. It may become future archived replication work only after coverage is rebuilt and explicitly labeled. |

## How These Windows Feed Development

Use the canonical windows for:

- current Analysis Arena cross-window rollups
- Stage2B through Stage7B read-only replay and blocker analysis
- archived-window stress testing
- March Run2 regression/reproducibility comparison
- fresh-window preflight context

Do not use these windows for:

- claiming true fresh confirmation
- unlocking Stage8A
- live scoring rewrite
- live candidate-expression rewrite
- budget policy replacement

## Same-Window Replay Rule

If March is replayed again, do not compare a one-window candidate cycle against
the multi-window baseline cycle.

Correct replacement-cycle set for March same-window replay:

- `WINDOW_2025-12-30_to_2026-01-04`
- `WINDOW_2026-01-05_to_2026-01-09`
- `WINDOW_2026-01-15_to_2026-01-22`
- candidate replay version of `WINDOW_2026-03-09_to_2026-03-23`

Always run:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py replay-plan-guardrails --force
```

## Fresh-Window Boundary

The next unlock-relevant evidence tier is still a true fresh gold-day window.
When that arrives, create a new clearly named window package instead of blending
it into the current canonical historical/replay set.

Before a fresh window starts, lock:

- window start and end dates
- Pick3StatsC4 gold-day coverage
- `decay-upload-days-total`
- tail results coverage through `window_end + 4 days` for full decay scoring
- bonus/fireball sidecar coverage plan

## Current Reference Chain

Read these together:

- `AAT9_ANALYSIS_ARENA__GOLD_DAY_WINDOW_INVENTORY.md`
- `AAT9_ANALYSIS_ARENA__EVIDENCE_BOUNDARY_AND_NEXT_RUN_MAP.md`
- `AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.md`
