# Research Pack — Play Cards + Budgets + Combo Packs (Selection/Grading)

Goal: give an external reviewer (ChatGPT Pro / human) a tight scope to evaluate:
- how Candidate Universe forms method packs (including combo-forming packs),
- how Play Cards apply budgets and strategies (B12/B24/B36),
- how grading + rollups measure outcomes (same-day + windowed),
- and where design/semantics might unintentionally distort tool outcomes.

This pack is pointer-only (no duplication). Evidence + implementation live in the repo.

## Start here (recommended order)

1) Orientation / SSOTs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

2) Contracts / semantics:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

3) Core code surfaces (selection):
- `scripts/tools/create_candidate_universe.py`
- `scripts/tools/create_play_card.py`
- `scripts/tools/create_predictive_portfolio_report.py`
- `scripts/tools/run_v0_3_cycle.py` (workflow wrapper; receipt-based)

4) Core code surfaces (grading/rollups):
- `scripts/tools/grade_candidate_universe.py`
- `scripts/tools/grade_play_card.py`
- `scripts/tools/grade_play_card_windowed.py`
- `scripts/tools/rollup_candidate_universe_corpus.py`
- `scripts/tools/rollup_play_card_corpus.py`

## Manifest + prompt kit

- File manifest: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/play_cards_budget_system_review/MANIFEST.md`
- ChatGPT Pro prompt (copy/paste): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/play_cards_budget_system_review/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`

