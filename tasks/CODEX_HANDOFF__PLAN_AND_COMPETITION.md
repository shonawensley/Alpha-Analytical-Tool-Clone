# CODEX HANDOFF — Plan + Competition Mode (AAT9)

Purpose:
- Preserve the approved “Candidate Universe / Playset” plan across chat/context resets.
- Provide a safe “competition/live predicting” mode that won’t contaminate measurements.

Repo root (WSL canonical): `/home/ser/code/Alpha-Analytical-Tool-Clone`

---

## 0) Non‑negotiables (safety)

- Do all commands from repo root (`pwd` must show the path above).
- Do not change analyzers (Stable/DR/VTRAC/Hot Zones) unless explicitly approved.
- Do not touch combined-table extraction/readers unless explicitly approved.
- Treat `sharepacks/<D>/` as immutable “after” snapshots.
- Treat `sharepacks/_predictive/<D>/` as immutable “before” snapshots.
- Biggest risk is **time contamination** (winners-dependent artifacts in predictive packs).

---

## 1) Terminology locks (prevents drift)

### 1.1 “Mirror” (required)

Default mirror scheme is **VTRAC-pair** mapping (NOT “sum-to-9”):
- `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`

In any new artifacts, store:
- `mirror_scheme: "vtrac_pair"`

### 1.2 “VTRAC” disambiguation (required)

Always distinguish:
- `vtrac_index` = boxed family index (`get_vtrac_index` style)
- `vstraight_vcode` / `vstraight_lane` = the 8-combo positional lane (STR8_8 style)

---

## 2) Competition Mode (live predicting, safe)

Goal: run “live-style” prediction work without breaking the development plan or contaminating evidence.

Rules:
- Prefer **existing frozen sharepacks** and templates.
- Do not regenerate analyzers while competing unless explicitly intended.

### Option A (recommended): Predictive snapshot is the “before”

1) Ensure the day’s predictive snapshot exists:
   - `sharepacks/_predictive/<D>/...`
2) Use that snapshot as the evidence base for picks.
3) Do **not** grade it until results exist for `<D>` (avoid hindsight).

Fast “open one file” triage (recommended):
- Generate/update:
  - `python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --force`
- Then open:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO.md` (includes PlayCard B12 list when present).

### Option B: Evaluate-only from post-results sharepacks (not predictive performance)

If you’re reviewing an already-built full-day sharepack (`sharepacks/<D>/`):
- That’s reverse-engineering / analysis, not “predictive hit rate”.

---

## 3) Approved development plan (Candidate Universe / Playset)

High-level outcome:
- Add a pre-results, gradeable “Candidate Universe” artifact per state/day.
- Later grade it against results honestly (with censored handling).
- Keep analyzers frozen; iterate in reporting/aggregation until enough sample size exists.

### Phase 0 — Hygiene / checkpoint prep

- Keep the working tree sane; avoid accidental commits of bulk artifacts.
- Restore any accidentally deleted SSOT docs (done in this workspace).

### Phase 1 — SSOT contract (doc-only)

Deliver:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`

Defines:
- schema fields
- mirror_scheme / vtrac disambiguation
- output locations
- anti-leakage rules

### Phase 2 — Candidate Universe generator (tooling only)

Deliver:
- `scripts/tools/create_candidate_universe.py`

Writes (per state/day):
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json` (+ optional `.md`)

Must include (minimum):
- `digit_pool` / envelope (when applicable)
- `derived_triads`
- `derived_vtrac_indices` and/or `vstraight_lane`
- `why_tags`
- `cost_units`
- `transform_chain` per pack

### Phase 3 — Grader (post-results)

Deliver:
- `scripts/tools/grade_candidate_universe.py`

Outputs:
- `candidate_universe_grade.csv` + `candidate_universe_grade.md`

### Phase 3b — Play Cards (budgeted cuts; discovery mode)

Deliver:
- `scripts/tools/create_play_card.py` → `sharepacks/_predictive/<D>/<STATE>/play_card.json`
- `scripts/tools/grade_play_card.py` → `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE.*`

### Phase 4 — Predictive run report scaffold

Deliver:
- `scripts/tools/create_predictive_run_report.py`
  - emits: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE.md`

### Phase 5 — Superbrain primitives ledger (research memory)

Deliver:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`

---

## 4) Resume checklist (after competition)

1) Print-only sanity:
```bash
pwd
git status -sb
git branch -vv
```

2) Re-open SSOT portals:
- `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`

3) Continue from Phase 1.
