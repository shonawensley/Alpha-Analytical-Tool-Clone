# Research Pack — Profit Alerts Postmortem (v0.2) — Manifest

This manifest defines the intended scope for a Profit Alerts postmortem audit. Everything listed is either:
- SSOT workflow docs (`final docs/`),
- committed evidence (`RUNS/`),
- or the wiring surfaces in code (`scripts/tools/`).

## 1) SSOT workflow + Profit Alerts contracts

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`

## 2) v0.2 posture + rationale

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

## 3) Evidence (RUNS)

Profit Alerts rollups:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP_MERGED.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP_MERGED.csv`

Control Center rollups (context for board behavior):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONTROL_CENTER_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONTROL_CENTER_ROLLUP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONTROL_CENTER_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONTROL_CENTER_ROLLUP.csv`

Profit-only baselines (how Profit Alerts behave in isolation):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.csv`

## 4) Wiring surfaces (code)

- `scripts/tools/export_control_center_sharepack.py` (builds `profit_alerts.csv/.md`)
- `scripts/tools/evaluate_profit_alerts.py` (writes `profit_alerts_eval.csv/.md` + `profit_alerts_eval_merged.csv`)
- `scripts/tools/rollup_profit_alerts_corpus.py` (window rollups to RUNS)
- `scripts/tools/create_candidate_universe.py` (parses Control Center `profit_alerts.csv` into packs when profile includes it)
- `scripts/tools/create_play_card.py` (how profit_alerts packs are treated in budget cuts)
- `scripts/tools/create_predictive_portfolio_report.py` (profit_alerts-ranked portfolio for profit_only/mixed)
- `scripts/tools/export_chatgpt_research_pack.py` (optional upload pack generator; supports `--include-profit-alerts` and `--include-tables`)

## 5) Local evidence (gitignored; optional, for deep “wiring parity” checks)

If you are reviewing a local repo copy that includes `sharepacks/`, these are the key raw artifacts:
- `sharepacks/<D>/control_center/profit_alerts.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`
- `sharepacks/<D>/<STATE>/winners/<STATE>/*.json` (environment lens; includes string-table context)
- `sharepacks/<D>/<STATE>/json/<STATE>_tables.json` and `sharepacks/<D>/<STATE>/tables/*.csv` (full string tables snapshot)

