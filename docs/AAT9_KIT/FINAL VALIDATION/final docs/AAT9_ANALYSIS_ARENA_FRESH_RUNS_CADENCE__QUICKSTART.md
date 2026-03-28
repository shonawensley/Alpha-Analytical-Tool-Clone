# AAT9 Analysis Arena Fresh-Runs Cadence — Quickstart

Purpose: define the current arena-era predictive cadence clearly enough that a fresh
Pick3StatsC4 run can be executed and reviewed without relying on chat memory.

This is the renamed operator shell for the newer branch architecture.

Use this when the goal is:

- generate the predictive sharepack
- rebuild Brain 1
- rebuild Brain 2
- emit the shadow Decision Policy Layer
- retain Candidate Universe / Play Card as the downstream control arm
- capture translation-learning seeds without activating live translator logic

## Naming / Layering

The branch now has two different cadence ideas:

- `analysis-arena cycle`
  - the current arena-era predictive runtime
  - Brain 1 -> Brain 2 -> shadow DPL -> Translation Sandbox
  - plus the control arm

- `v0.3 cycle`
  - the older wrapper that still grades Candidate Universe / Play Card
  - useful for post-results control-arm grading
  - not the full expression of arena truth

That means:

- `run_analysis_arena_cycle.py` is the current pre-results operator wrapper
- `run_analysis_arena_cycle.py post` is the current post-results operator wrapper
- `run_v0_3_cycle.py` still runs inside that post flow for control-arm grading only

## Operator Checklist

Before running:

1. Confirm the history workbook date `H`
2. Confirm repo root and git status
3. Decide the profile and experiment tag
4. Decide whether you want all states or a subset
5. Run the arena cycle
6. Review the emitted board bundle + translation sandbox before interpreting the control arm too literally

## Recommended Fast Path

From repo root:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre --history-date <H> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --write-audit-evidence --play-card-write-md --force
```

Example:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre --history-date 2026-01-19 --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --write-audit-evidence --play-card-write-md --force
```

## What This Produces

### Predictive sharepack

- `sharepacks/_predictive/<D>/...`

### Arena runtime receipts

Under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`

You will get:

- board spillover overlay
- board scoreboard
- shadow decision policy
- board review bundle
- translation sandbox day manifest
- an arena-cycle receipt

### State-local learning surfaces

Under:

- `sharepacks/_predictive/<D>/<STATE>/analysis/`

You will get:

- aggregated analysis arena
- translation sandbox seed

### Control-arm outputs

Under each predictive state folder:

- `candidate_universe__*.json`
- `play_card__*.json`
- optional markdown/evidence surfaces

These remain:

- baseline comparison targets
- not the definition of arena truth

## Range Runs

```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre-range --start-history-date <H0> --end-history-date <H1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --force
```

## Practical Reading Order After A Run

1. board review bundle
2. board scoreboard
3. shadow DPL
4. per-state aggregated arena
5. per-state translation sandbox seed
6. Candidate Universe / Play Card as the downstream control arm

This order matters because the branch now preserves truth first and compression second.

Companion references:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PORTAL.md`

## Post-Results Note

Use the aligned post-results wrapper:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py post --date <D> --sharepacks-root sharepacks/_predictive --truth-sharepacks-root sharepacks --profile tool_only --experiment-tag arena_v0 --analysis-runs-subdir ANALYSIS_ARENA --runs-subdir VALIDATION --force
```

This now does both:

- control-arm grading through the retained baseline wrapper
- arena-native post-results outputs under `RUNS_2/VALIDATION/`

So the branch is now:

- pre-results arena-native
- post-results arena-native at the reporting/validation layer
- still using the control arm only as baseline comparison inside that post flow

## Window Closeout

After a completed window under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<...>/`

generate the full end-of-window closeout set:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-close --window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_<...> --runs-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --force
```

These produce:

- quantitative `arena truth vs control-arm realization vs opportunity gap`
- deep hit analysis + machine-readable hit roster
- pure arena finalist / candidate scorecard
- C1/C2 vertical-frontier harness analysis + machine-readable frontier cases
- broader Codex-style window synthesis

Use them after:

1. `pre-range`
2. `post-range`
3. validation shells are generated
