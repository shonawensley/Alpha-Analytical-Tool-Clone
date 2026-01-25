# Research Pack — Profit Alerts Postmortem (v0.2)

Goal: give a reviewer (ChatGPT Pro / human) a tight scope to audit **why Profit Alerts (A01–A12)** performed poorly and whether:
- they were **wired correctly** (contracts + date/variant alignment),
- the evaluation semantics are correct,
- they should remain quarantined, be redesigned, or be removed.

This pack is **research-only**:
- v0.2 defaults remain `tool_only` (Profit Alerts have zero default influence).
- No analyzer edits are required.

## Start here (recommended order)

1) SSOT workflow + timeline (prevents “date drift” confusion):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`

2) Profit Alerts semantics (what is being evaluated):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`

3) Evidence (what happened in the v0 windows):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP.md`
- Portfolio/corpus baselines:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.md`
- Quarantine posture / rationale:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

4) Wiring surfaces (where Profit Alerts are built + graded):
- Build board (Control Center export): `scripts/tools/export_control_center_sharepack.py`
- Episode evaluation + merged playsets: `scripts/tools/evaluate_profit_alerts.py`
- Roll up across a window: `scripts/tools/rollup_profit_alerts_corpus.py`
- How Profit Alerts become Candidate Universe packs (when profile includes them): `scripts/tools/create_candidate_universe.py`

## Optional: generate an uploadable “slice pack” (includes string tables)

If you want ChatGPT Pro to inspect the **string tables** and the winners lens alongside Profit Alerts:

```bash
python3 scripts/tools/export_chatgpt_research_pack.py \
  --start-date 2025-12-30 --end-date 2026-01-04 \
  --mode curated \
  --max-profit-alerts-cases 50 \
  --include-control-center --include-profit-alerts \
  --include-tables \
  --include-predictive --profile mixed \
  --zip
```

Notes:
- This exports `sharepacks/<D>/control_center/profit_alerts*.csv` and `profit_alerts_eval*.csv` (all states), plus a bounded set of per-state winners/tables evidence for context.
- Output lands under `sharepacks/_scratch/` and is gitignored.
