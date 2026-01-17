# CODEX HANDOFF — Superbrain v0 Synthesis Sprint (Status Log)

Append-only status notes intended to survive chat/context resets.

---

## 2026-01-14

### Start-of-sprint snapshot

- Mode: v0 synthesis sprint (no new runs; no analyzer edits).
- Profit Alerts posture: quarantined via `--profile tool_only` (ablation profiles exist for measurement).
- Gold ledger capture format:
  - Template + stable IDs added in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.
  - Initial entries created: `GOLD-0001` → `GOLD-0003`.
- Next actions:
  1) Mine more entries from `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md` and `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`.
  2) DR deep audit using design docs + winners lens + DR overlays + RUNS Part 2.
  3) Aux boxed-VTRAC badge matrix parity audit (Windows app feature).
  4) Lock `SUPERBRAIN_V0_2__DEFAULTS.md`, then resume new days.

### Queue mining progress (doubles + convergence)

- Doubles/mirror-doubles study queue:
  - Processed rows 1–13 from `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`.
  - Added `GOLD-0004` → `GOLD-0013` into `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.
- Top convergence cases:
  - Processed score=4 cases from `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`.
  - Added `GOLD-0014` → `GOLD-0018` into `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.
- Key v0 takeaway: many “index hit → box miss” cases are actually low-signal lane-hits (winners lens silent in Set1 col1/2); only high-evidence cases should drive v0.2 changes.
- Key action emerging: in high-evidence convergence cases, misses look like **Candidate Universe ingestion / Play Card budget allocation** issues (e.g., not ingesting top boxed canonicals from Stable scores), not analyzer failures.

### v0 sprint status (DR audit + Aux badge-matrix export + v0.2 defaults)

Completed (reporting-only / no analyzer changes):

- DR v0 audit (quant + cases + explicit v0.2 consumption decisions):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
  - Key posture: treat DR as an **envelope/trace lens**, not a default top‑caller (`--top-n-dr 0` in tool‑only baseline).

- Aux boxed VTRAC “badge matrix” parity export (Windows-style surface, reporting-only):
  - Audit/spec: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_VTRAC_BADGE_MATRIX__AUDIT.md`
  - Export script: `scripts/tools/create_aux_vtrac_badge_matrix_report.py`
  - v0 window day exports: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__AUX_VTRAC_BADGE_MATRIX.md` → `2026-01-09__AUX_VTRAC_BADGE_MATRIX.md` (+ `.csv`)
  - Legend + placement: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Aux_Coverage_And_Legend.md`

- v0.2 defaults + tool-first scoring locked:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
  - Predictive portfolio now includes `CU top support` (convergence proxy) and ranks tool-first by:
    - higher top support → smaller union → more due doubles → more packs.

Next actions (v0.2 execution):

1) Resume new days using the v0.2 defaults (tool-first, Profit Alerts quarantined):
   - `python3 scripts/tools/run_predictive_day.py --history-date <H>`
   - `python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --top-n-dr 0`
   - `python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only`
   - `python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --rank-by tool_first`

2) Optional (recommended): mine the badge-matrix exports into more GOLD entries:
   - look for cases where badge density + index pressure compounds across variants but we still miss (or get index_hit_only).

### Tool consumption audits (Stable / Hot Zones / VTRAC) + ledger/portal wiring

Completed (reporting-only / no analyzer changes):

- Stable v0 consumption audit (quant + cases + explicit consumption decisions):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
- Hot Zones v0 consumption audit (quant + cases + explicit consumption decisions):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
- VTRAC enhanced v0 consumption audit (quant + cases + explicit consumption decisions):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`

Ledger/portal updates:

- Added new GOLD entries capturing canonical-only conversion opportunities (lane tools are often “right about the box”): `GOLD-0019` → `GOLD-0021` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.
- Updated RUNS navigation to include the tool audit docs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`

---

## 2026-01-16

### Tool-only defaults (anti-pollution hardening)

- Prediction-layer tooling now defaults to `--profile tool_only` so Profit Alerts have **zero influence** unless explicitly requested:
  - Candidate Universe / Play Cards / predictive portfolio / grading / rollups.
- The v0 sprint doc remains the “how to run ablation”; `mixed` and `profit_only` are still available for measurement, but not the default posture.

### Predictive RUNS completeness (tool_only)

- Generated per-state predictive run reports for the v0 Jan window (all tracked states × `D=2026-01-05` → `2026-01-09`):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE__tool_only.md`

### Selection experiment: conversion slots (negative result)

- Added a Play Card strategy experiment (`conversion_box_first`) intended to convert `vtrac_index_hit_only` into actual hits under a fixed budget.
- Result on v0 Jan window: improved `vtrac_index_hit`, but reduced `hit_any` vs `play_box_first`.
- Logged as a negative-result “gold” entry (research-only; do not promote to default): `GOLD-0028` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.

### FINAL REVIEW SWEEP (RUNS + CODEX_ANALYSIS8)

- Completed an exhaustive scan of `docs/AAT9_KIT/FINAL VALIDATION/RUNS/` plus `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/CODEX_ANALYSIS8.txt` to confirm we didn’t miss any “universal gold”.
- Outcome: no net-new gold actions were discovered; the sweep reinforced that the current v0.2 posture + existing GOLD entries already cover the actionable insights.
- Receipt:
  - RUNS: scanned 544 files (MD/CSV/TXT/etc.).
  - CODEX_ANALYSIS8: scanned 1479 lines.
  - Summary is appended as “FINAL REVIEW SWEEP” in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`.

---

## 2026-01-17

### STABLE-002 (compound aggregation correctness) — closed

- Fix landed (commit): `b7a42db3` (“Fix Stable compound flag parsing and update score contracts”).
- What it fixes: Stable compound aggregation now correctly treats Stable flags as boolean-like and uses `persistence_set_count` / `persistence_draw_run` when available (prevents silent under-crediting in `*_stable_patterns_compound.csv`).
- Regression coverage:
  - `tests/test_stable_compound.py` (boolean flags + persistence fields)
  - `tests/test_stable_contracts.py` updated to reflect the current Stable score contract (row + family parts).
- Note: existing frozen sharepacks already on disk still contain the old `patterns_compound.csv` outputs from before this fix; we do not rewrite historical SSOT snapshots in place. The fix applies to future sharepack builds (or explicit day rebuilds into a new folder).
