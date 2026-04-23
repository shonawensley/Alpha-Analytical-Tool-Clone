# AAT9 Analysis Arena Operating Flow — Fresh Runs

Date: `2026-03-26`

## Purpose

This document explains the current end-to-end operating flow for the rebuilt
Analysis Arena branch.

Use it when you want a broad, flowchart-style understanding of:

- what the new cadence does
- where sharepacks fit
- how Brain 1 and Brain 2 relate
- where shadow DPL and the translation sandbox sit
- what still remains control-arm only
- how daily runs turn into window learning

---

## Core Idea

The branch now works in this order:

1. freeze the predictive day snapshot
2. build Brain 1 per-state truth
3. build Brain 2 board-level comparison
4. emit shadow DPL posture
5. preserve translation-learning signals
6. keep the old downstream pack stack as a control arm
7. once results exist, run per-state and board-level validation
8. roll windows up and do deeper end-of-window analysis

---

## Flow Diagram

```mermaid
flowchart TD
    A[Pick3StatsC4 History Workbook H] --> B[run_analysis_arena_cycle.py pre]
    B --> C[Predictive Sharepack Freeze<br/>sharepacks/_predictive/D]
    C --> D[Brain 1<br/>Aggregated Analysis Arena per state]
    D --> E[Brain 2 Runtime<br/>Board Overlay + Scoreboard + Bundle]
    E --> F[Shadow DPL<br/>PLAY/WATCH/SKIP + mode + cap]
    F --> G[Translation Sandbox Seed<br/>boxed / straight / vt-box learning]
    C --> H[Control Arm<br/>Candidate Universe + Play Card + Portfolio]
    E --> I[RUNS_2/ANALYSIS_ARENA<br/>runtime receipts]
    G --> J[Per-state Translation Learning]
    K[Results / Winners Truth] --> L[Per-state Master Validation]
    I --> M[Brain 2 Master Validation]
    J --> M
    H --> M
    L --> N[Window Learning / Decay / Comparison]
    M --> N
    N --> O[Performance / Opportunity Gap Report]
    N --> P[Deep Hit Analysis / Hit Roster]
    N --> Q[Pure Finalist / Candidate Scorecard]
    N --> R[Translator-Learning Ledger]
    N --> S[C1/C2 Frontier Harness / Frontier Cases]
    N --> T[Window Deep Analysis / Codex Report]
```

---

## Layer Notes

### Frozen Evidence Layer

- `sharepacks/_predictive/<D>/...`
- this is the immutable predictive-day snapshot
- sharepacks remain the evidence substrate for both daily review and later validation

### Brain 1

- per-state aggregated analysis arena
- dominant canonicals
- dominant families
- dominant VTRAC indices
- survivor and `R-Consensus` context
- local context reinforcement

### Brain 2 Runtime

- board review bundle
- board scoreboard
- spillover overlay
- host vs echo vs shared-host logic

### Shadow DPL

- posture
- mode
- cap class
- translator route
- reason codes

This is still shadow/learning mode, not active final policy.

### Translation Sandbox

- captures near-final cluster intelligence
- boxed / straight / vt-box hypotheses
- preserved-not-budgeted clusters
- shortlist carry-through

This is a learning layer, not live combination forming.

### Control Arm

- Candidate Universe
- Play Card
- portfolio outputs

These are still baseline comparison surfaces.

They are not the definition of arena truth.

---

## Output Homes

Current arena-era output homes:

- runtime receipts:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`
- human validation and window learning:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`
- frozen predictive evidence:
  - `sharepacks/_predictive/<D>/...`
- historical / legacy comparison:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

---

## Operational Reading Order

For a fresh day:

1. board review bundle
2. board scoreboard
3. shadow DPL
4. per-state aggregated analysis arena
5. per-state translation sandbox seed
6. Candidate Universe / Play Card

For post-results:

1. winners truth and per-state Master Validation
2. Brain 2 Master Validation
3. control-arm comparison
4. performance / opportunity gap report
5. deep hit analysis / hit roster
6. pure finalist / candidate scorecard
7. translator-learning ledger
8. C1/C2 frontier harness / frontier cases
9. window deep analysis / Codex report

---

## Current Boundary Conditions

What is real now:

- Brain 1
- Brain 2 runtime
- shadow DPL
- translation sandbox
- per-state Master Validation
- Brain 2 Master Validation

What is still deliberately deferred:

- active arena-native translators
- final combination-forming logic
- budgeting / waging redesign

That is intentional.

The branch is designed to let real fresh-run evidence teach those later layers.

When an already-known or archived window is rerun, label the run before
interpretation using:

- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- `AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`

Same-window replay and archived-window replication are useful development and
stress-test evidence, but they do not replace true fresh-window confirmation.

## Window-Close Commands

Once a full window is complete, run:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-close --window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_<...> --runs-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --force
```

That gives the branch six different window-close artifacts:

- one quantitative report for arena quality, control-arm realization, and opportunity gap
- one deep converted-hit report for hit class, rank, cost, and arena-finalist signatures
- one pure arena finalist / candidate scorecard for VTRAC/finalist territory, combo-like candidate traces, and opportunity-gap evidence
- one translator-learning ledger for future translator design and opportunity-gap teaching rows
- one winner-HTML frontier harness for C1/C2 survivor / feeder / compression analysis
- one broader narrative report for repeated structures, carryover, tracker families, and promotions

After multiple completed windows, run the system-level rollup:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py cross-window-rollup --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

And then the tune-up diagnostics package:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py tuneup-diagnostics --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

Then run the frontier negative-control study before promoting frontier features:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py frontier-negative-control --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

For same-window replay or archived-window replication target selection, run:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

Then run the baseline-vs-candidate comparison report. With no candidate root,
this acts as a baseline-preservation checklist:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare --force
```

For same-window replay, Stage 2B through Stage 7B must be regenerated in a
canonical replacement-cycle root, not in the isolated one-window replay root.
The replacement cycle keeps the baseline peer windows and swaps only the
baseline window being replayed for the candidate window. Comparing a one-window
candidate cycle to a multi-window baseline cycle is invalid because cross-window
promotion guardrails can block artificially.

And before starting a new fresh gold-day window, run the readiness preflight:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py fresh-window-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```
