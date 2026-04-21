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
5. If this is a windowed run, lock the evidence tier and per-window inputs before starting
6. Run the arena cycle
7. Review the emitted board bundle + translation sandbox before interpreting the control arm too literally

## Per-Window Lock Inputs

Before starting any fresh or backtest window, explicitly lock:

1. `evidence tier`
   - `same_window_replay`
   - `archived_window_replication`
   - `true_fresh_confirmation`
2. `run label`
   - stable label for comparing baseline vs rerun outputs
3. `window dates`
   - exact window start and window end
4. `decay-upload-days-total`
   - default `5`
   - this means `5` total Pick3StatsC4 upload days including same-day
5. `tail coverage expectation`
   - either results exist through `window_end + 4 days`
   - or the decay companion is expected to contain `right_censored` rows
6. `decay execution posture`
   - run the decay companion as part of closeout for backtest windows
   - or defer it until future results arrive for live-style windows

This lock step matters because same-day grading and decay grading are both official,
but they answer different questions and should not be blended.

Use `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md` before
rerunning any known or archived window. Same-window replay and archived-window
replication can support development, but only `true_fresh_confirmation` can
support fresh-confirmation gates.

Before selecting a known-window rerun target, generate the replay-readiness
matrix:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

Read:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`

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

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
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

## Optional Bonus-Ball Sidecar Truth

If you are also collecting Fireball / Wild Ball / Superball source files, keep them in:

- `data/results_bonus/<D>.txt`

Core results stay authoritative in:

- `data/results/<D>.txt`

Generate the normalized bonus-ball truth companion with:

```bash
python3 scripts/tools/create_bonus_ball_truth_report.py --date <D> --force
```

This sidecar:

- parses the full structured source and filters only the supported active bonus-ball states
- accepts a bonus digit only when the sidecar Pick 3 draw parity-matches the core results draw for the same state and slot
- writes normalized truth under `reports/stable/bonus_ball_by_date/<D>/`
- does not drive winners HTML or replace the standard Pick 3 results path

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
- translator-learning ledger for future translator study
- C1/C2 vertical-frontier harness analysis + machine-readable frontier cases
- broader Codex-style window synthesis

Optional companion decay/carryover closeout:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-decay-close --window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_<...> --results-root data/results --decay-upload-days-total 5 --force
```

Notes:

- `decay-upload-days-total 5` means `5` total Pick3StatsC4 upload days including same-day
- that corresponds to at most `10` total draws
- for a backtest window, results must exist through `window_end + 4 days` for full decay coverage
- if tail coverage is incomplete, the decay scorecard should mark rows as `right_censored`, not `miss`

Use them after:

1. `pre-range`
2. `post-range`
3. validation shells are generated

## Cross-Window Rollup

After `2+` completed windows, generate the system-level rollup:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py cross-window-rollup --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

Then generate the tune-up diagnostics package:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py tuneup-diagnostics --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

And then the frontier negative-control study:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py frontier-negative-control --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

If the next target is a same-window replay or archived-window replication, run
the replay-readiness inventory before choosing the run label:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

Then generate the baseline-vs-candidate comparison report. Before a candidate
rerun exists, this records the preserved baseline and expected comparison
targets:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare --force
```

Before starting a new fresh gold-day window, run the readiness preflight:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py fresh-window-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

When the window is complete, first confirm the evidence tier:

- `same_window_replay`
- `archived_window_replication`
- `true_fresh_confirmation`

Then read it in this order:

1. Arena Truth
2. Brain 2 Prioritization
3. Control Arm Realization
4. Translator Opportunity
5. Decay / Carryover Companion when available

Do not start with `B12/B24/B36` or Play Card and treat them as the branch verdict.
