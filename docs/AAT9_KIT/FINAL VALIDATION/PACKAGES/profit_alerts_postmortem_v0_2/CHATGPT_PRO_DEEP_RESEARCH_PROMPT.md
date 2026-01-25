# ChatGPT Pro — Deep Research Prompt (Profit Alerts Postmortem v0.2)

## Mission

Perform a **wiring + semantics audit** of Profit Alerts (A01–A12):
- Are the Profit Alerts boards built correctly (state mapping, variant mapping, date alignment)?
- Are the evaluation rules correct (decay windows, strict vs hit_any, censored handling)?
- If performance is poor, is it because of (a) wiring/contract defects, (b) overly broad triggers, or (c) the concept not adding value?

This is a **research-only** project. Do not recommend enabling Profit Alerts in defaults unless evidence is strong and stable.

## Required reading order (strict)

1) Workflow timeline + Control Center:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`

2) Profit Alerts semantics:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`

3) v0.2 posture / quarantine context:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

4) Evidence rollups (what happened):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.md`

5) Wiring surfaces (code):
- Build board: `scripts/tools/export_control_center_sharepack.py` (see `_build_profit_alerts_df(...)`)
- Evaluate episodes: `scripts/tools/evaluate_profit_alerts.py`
- Rollups: `scripts/tools/rollup_profit_alerts_corpus.py`
- Consumption in Candidate Universe: `scripts/tools/create_candidate_universe.py` (`_parse_profit_alerts(...)`)
- Portfolio ranking: `scripts/tools/create_predictive_portfolio_report.py` (profit_alerts ranking mode)

## Optional raw-evidence audit (only if sharepacks are available)

If `sharepacks/<D>/...` is available (local repo or exported pack), audit a small sample:
- Pick 2–4 HIT rows from `sharepacks/<D>/control_center/profit_alerts_eval.csv` and confirm:
  - `state_key` matches the folder naming used elsewhere (`<STATE>4` style keys)
  - `variant` semantics match the charter (Combined uses Midday→Evening→… sequencing)
  - `canonical` / `suggested` are interpreted consistently (boxed vs straight group kinds)
  - (Optional) open winners lens + tables snapshots for the same state/day:
    - `sharepacks/<D>/<STATE>/winners/<STATE>/*.json`
    - `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`

## Deliverables (write as sections)

1) **Wiring verdict**
- PASS/FAIL with exact reason(s) and file/line references.

2) **Semantics verdict**
- Are the evaluation windows and hit criteria consistent with the charter?
- Any “CENSORED” or “unknown results coverage” artifacts that could artificially depress rates?

3) **Failure mode taxonomy**
Propose 3–6 reasons the system produces many EXPIRED rows:
- trigger too broad
- implied playset too large
- variant mismatch
- horizon mismatch
- etc.

4) **Salvage plan (if any)**
Only if you see a credible path:
- 1–3 minimal experiments to try later (default-off), with acceptance criteria.
Otherwise recommend deletion/retirement.

## Constraints

- Do not recommend analyzer edits or touching string-table extraction.
- Treat defaults as quarantined; this is a postmortem / research output only.
- Prefer rollups for global conclusions; use raw sharepacks only for parity checks.

