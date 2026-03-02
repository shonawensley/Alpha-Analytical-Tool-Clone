# Morning Brief — Evidence Extraction (v0.3)

Date: `2026-03-01`

Purpose: give you a **single, low-friction entrypoint** for resuming the deep dive without getting lost in artifacts.

## What changed (doc-only; no sharepacks regenerated)

- SSOT ledger upgraded with:
  - 5‑minute + 20‑minute “how to use” workflows
  - Plain-English executive summary (what we know / bottlenecks / what’s next)
  - Mining status table (proof we “squeezed the orange”)
  - Expanded teaching-case index (so you can learn regimes fast)
  - Profit Alerts quarantine evidence preserved as an appendix (no reintegration)
  - File: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`
- Predictive day navigation is now one-click:
  - File: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_DAYS_INDEX__tool_only.md`
- Portal now links the predictive day index + the dc1 portfolio variant:
  - File: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- Bottleneck dashboard added (lane drop vs within-lane, with exact counts):
  - File: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__BOTTLENECK_DASHBOARD__tool_only__stable10__B36.md`

## 10-minute “broad check” (start here)

1) Predictive days list:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_DAYS_INDEX__tool_only.md`

2) Pick one window report (broad reality check):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
- Optional comparison: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md`

3) If you want “tight vs noisy” posture context:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md`

## 30-minute “one day, two states” drill (broad → specific)

Pick a date you want to audit (example: `2026-01-22`):

- Day synthesis (fast anchor):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__DAY_SYNTHESIS.md`
- Baseline portfolio (triage + printed play cards):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__PREDICTIVE_PORTFOLIO__tool_only.md`
- dc1 portfolio (same day, B36 conversion variant printed):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- Posted results:
  - `data/results/2026-01-22.txt`

Then pick 1–2 states and open the “6 receipts”:
- MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__<STATE>.md`
- Winners HTML/JSON: `sharepacks/2026-01-22/<STATE>/winners/<STATE>/...`
- Predictive CU: `sharepacks/_predictive/2026-01-22/<STATE>/candidate_universe__tool_only__stable10.json`
- Predictive Play Card (baseline + dc1 in same JSON bundle):
  - `sharepacks/_predictive/2026-01-22/<STATE>/play_card__tool_only__stable10.json`

## The 3 best teaching cases to review next (fast learning)

Open these inside the SSOT ledger and follow the “open these files (in order)” lists:
- `C035` — NewYork4 `2026-01-06` Evening (lane drop; dc1 can’t help if lane gets 0 lines)
- `C036` — Delaware4 `2026-01-02` Evening (lane retained but 1-line depth; lane hit → box miss)
- `C031` — Ohio4 `2026-01-22` Evening (strict recovery BASE→dc1 without analyzer edits)

Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`

## If you want a single “why Ohio was ranked #1” reminder

Portfolio rank (`rank_by=tool_first`) is a triage sort:
- higher `CU top support` first (more cross-pack agreement on a top canonical),
- then smaller `CU union`,
- then more `due_doubles` count.

Code receipt: `scripts/tools/create_predictive_portfolio_report.py`
