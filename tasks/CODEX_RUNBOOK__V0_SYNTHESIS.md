# CODEX RUNBOOK — Superbrain v0 Synthesis Sprint (Reset‑Proof)

Purpose: keep the v0 synthesis sprint moving even across chat/context resets.

Canonical repo root: `/home/ser/code/Alpha-Analytical-Tool-Clone`

---

## 0) Non‑negotiables (safety + scope)

- Run commands from repo root only.
- Do **not** change analyzers (Stable / Digit Reduction / VTRAC / Hot Zones).
- Do **not** touch combined-table extraction/readers unless explicitly scoped.
- Do **not** generate new sharepacks/runs during v0 synthesis (we are mining + auditing only).
- Profit Alerts stay quarantined during synthesis:
  - Use `--profile tool_only` for any synthesis/triage/grades/rollups unless explicitly testing ablation.

---

## 1) “Resume in 2 minutes” checklist

1) Open these files (in this order):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`

2) Read the latest handoff:
   - `tasks/CODEX_HANDOFF__V0_SYNTHESIS_STATUS.md`

3) Confirm we’re still in synthesis mode (no new runs):
   - `git status -sb`

---

## 2) Current plan (v0 → v0.2)

1) Mine doubles/convergence queues → write `GOLD-####` entries.
2) Digit Reduction deep audit (design intent + quant + cases + decisions).
3) Aux “boxed VTRAC badge matrix” audit (Windows app parity check).
4) Lock v0.2 defaults (profile, budgets, allowed bounded rules) and only then resume runs.

---

## 3) Gold entry protocol (don’t lose insights)

Gold ledger:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`

Last used gold ID:
- `GOLD-0018`

Next ID:
- `GOLD-0019`

Rules:
- Every gold entry must link: deep dive line, run report, predictive CU, predictive play card, winners digest.
- If it’s a pipeline defect, log it to:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md` or
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

---

## 4) Useful regeneration commands (tool-only)

Rollups (do not run unless needed; writes only to RUNS):
```bash
export PYTHONPATH=.:src
python3 scripts/tools/rollup_candidate_universe_corpus.py --profile tool_only
python3 scripts/tools/rollup_play_card_corpus.py --profile tool_only
```

Portfolio (tool-only triage surface):
```bash
export PYTHONPATH=.:src
python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-01-09 --sharepacks-root sharepacks/_predictive --profile tool_only
```

---

## 5) Deliverables to produce during the sprint

- DR audit docs (RUNS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
- Aux badge matrix audit (RUNS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_VTRAC_BADGE_MATRIX__AUDIT.md`
- v0.2 defaults lock (RUNS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
