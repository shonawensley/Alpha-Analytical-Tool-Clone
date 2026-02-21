# V0.3 — Profit Alerts Revamp (Quarantined) — Stage 2 Report

Timestamp (UTC): `2026-02-21`

Scope:
- Profit Alerts (A01–A12) only (quarantined; **does not** touch `tool_only` selection/analyzers).
- Goal is **truth-layer + auditability**, not tuning.

Hard invariants:
- No analyzer edits (Stable/DR/Hot Zones/VTRAC unchanged).
- No overwrite footguns: all window outputs are label-suffixed.
- Windows are driven by existing `sharepacks/<D>/...` artifacts.

## What Stage 2 produced

For each window:
- Rollup (performance lenses + hit typing):
  - `<A>_to_<B>__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21.md`
  - `<A>_to_<B>__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_ROWS.csv`
  - `<A>_to_<B>__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_MERGED.csv`
- Integrity report (coverage + wiring sanity):
  - `V0_3__PROFIT_ALERTS__INTEGRITY__<A>_to_<B>__2026-02-21__revamp_2026-02-21_v2.md`
- Manual audit casebook package:
  - `PACKAGES/profit_alerts_revamp__<A>_to_<B>__2026-02-21__revamp_2026-02-21/CASEBOOK.md`
  - `PACKAGES/profit_alerts_revamp__<A>_to_<B>__2026-02-21__revamp_2026-02-21/MANIFEST.md`

## Windows evaluated

- “Known-good mini corpus”: `2025-06-21..2025-06-23`
- “Reported-bad window”: `2025-12-30..2026-01-09`

Rosters (sharepack coverage):
- `RUNS/V0_3__PROFIT_ALERTS__ROSTER__2025-06-21_to_2025-06-23__2026-02-21.csv`
- `RUNS/V0_3__PROFIT_ALERTS__ROSTER__2025-12-30_to_2026-01-09__2026-02-21.csv`

## Key results (high level)

### 1) Integrity: “wiring” is not the problem

Both windows show:
- `evidence_ok=N`: **0**
- Evidence errors: **none**
- Canonical-required alerts: **0 canonical invalid**
- Candidate implied-set size mismatches vs expected: **0**

So the earlier “Profit Alerts are broken” suspicion does **not** reproduce as an integrity failure in the current exporter + evaluator.

References:
- `RUNS/V0_3__PROFIT_ALERTS__INTEGRITY__2025-06-21_to_2025-06-23__2026-02-21__revamp_2026-02-21_v2.md`
- `RUNS/V0_3__PROFIT_ALERTS__INTEGRITY__2025-12-30_to_2026-01-09__2026-02-21__revamp_2026-02-21_v2.md`

### 2) Performance: hit rates are low but coherent with the intended semantics

Profit Alerts are *episode signals*; strict same-day is diagnostic, not the primary lens.

Known-good (`2025-06-21..2025-06-23`):
- Rows: 257 (candidates 182; promoters 55)
- Row HIT: 3/257
- Candidate strict_hit (D-only): 0/177
- Candidate hit_decay (episode): 3/182
- Merged set HIT: 2/157

Reported-bad (`2025-12-30..2026-01-09`):
- Rows: 721 (candidates 543; promoters 139)
- Row HIT: 4/721
- Candidate strict_hit (D-only): 4/522
- Candidate hit_decay (episode): 4/426 (117 unknown due to censoring)
- Merged set HIT: 4/494 (94 censored)

References:
- `RUNS/2025-06-21_to_2025-06-23__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21.md`
- `RUNS/2025-12-30_to_2026-01-09__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21.md`

### 3) Manual audit is now feasible (fast, deterministic)

The casebooks give you a bounded set of examples with direct pointers to:
- the exact `profit_alerts_eval.csv` row,
- the matching `profit_alerts.md` board row,
- the winners digest + HTML/JSON,
- Stable scored rows,
- and the JSON tables snapshot.

References:
- `PACKAGES/profit_alerts_revamp__2025-06-21_to_2025-06-23__2026-02-21__revamp_2026-02-21/CASEBOOK.md`
- `PACKAGES/profit_alerts_revamp__2025-12-30_to_2026-01-09__2026-02-21__revamp_2026-02-21/CASEBOOK.md`

## Interpretation (what Stage 2 means)

- Profit Alerts are **not failing due to mis-mapped features** (at least within these two windows).
- The “low %” that triggered quarantine is most consistent with **expectation mismatch**:
  - treating episode-style alerts as “next-day strict callers”, and/or
  - grading overlays/promoters as if they were candidate sets.
- With the current truth-layer, we can now safely move to Stage 3 (fix/upgrade) **only if** the casebooks show real conceptual misalignment (e.g., the board fires for patterns that don’t exist in the underlying tables).

## Recommended next steps (Stage 3 options)

Pick one (do not stack):

1) **Provenance/locator upgrade (best for your manual audit workflow)**
   - Add minimal locators to `profit_alerts.csv` rows (e.g., stable source filename + row index, or set/col pointers) so you can jump from alert → raw table evidence without searching.
   - Keeps the alerts quarantined; does not change the analyzers; mostly exporter metadata.

2) **Corpus expansion (best for reducing small-N confusion)**
   - Run the same Stage 2 suite on a larger, recent window (more outcomes) to stabilize hit rates and reveal which alert IDs actually have signal.

3) **Tuning (only after 1+2)**
   - Adjust thresholds only if:
     - the integrity + manual audit pass says wiring is correct, and
     - we can demonstrate the tweak improves episode conversion without exploding implied set sizes.

