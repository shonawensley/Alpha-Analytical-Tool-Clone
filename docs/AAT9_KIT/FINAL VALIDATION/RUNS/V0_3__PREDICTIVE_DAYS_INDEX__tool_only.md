# v0.3 Predictive Days Index (tool_only, stable10)

Purpose: give you a single list of the **predictive days currently available** in `sharepacks/_predictive/`, with the matching RUNS portfolio pages and posted results.

## Windows (how we talk about evaluation)

- **OOS window** (“out-of-sample” guardrail): `2026-01-01 → 2026-01-09`
  - Used as a *holdout* to reduce “we tuned it on this same data” bias.
- **Jan window** (gold / primary deep-dive window): `2026-01-15 → 2026-01-22` (no `2026-01-19` in predictive sharepacks)

## How to use this index (fast)

1) Open a baseline portfolio for a date.
2) Open the same date’s dc1 portfolio (B36-only conversion policy variant) to compare.
3) Compare either/both to `data/results/<D>.txt` (Midday + Evening results for that date).

## Predictive days available

| Date | Baseline portfolio | dc1 portfolio (B36 closure v2) | Posted results |
|---|---|---|---|
| 2026-01-01 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-01.txt` |
| 2026-01-02 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-02.txt` |
| 2026-01-03 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-03.txt` |
| 2026-01-04 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-04.txt` |
| 2026-01-05 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-05.txt` |
| 2026-01-06 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-06.txt` |
| 2026-01-07 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-07.txt` |
| 2026-01-08 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-08.txt` |
| 2026-01-09 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-09.txt` |
| 2026-01-15 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-15.txt` |
| 2026-01-16 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-16.txt` |
| 2026-01-17 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-17.txt` |
| 2026-01-18 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-18.txt` |
| 2026-01-20 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-20.txt` |
| 2026-01-21 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-21.txt` |
| 2026-01-22 | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__PREDICTIVE_PORTFOLIO__tool_only.md` | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md` | `data/results/2026-01-22.txt` |

## Reminder: where the “real” evidence lives

The portfolio pages are an index/printout. The frozen evidence is always:

- Predictive sharepack root: `sharepacks/_predictive/<D>/`
  - Candidate Universe: `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json`
  - Play Card (baseline + dc1 strategy bundle): `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json`
  - Human-readable Play Card: `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.md`
- Posted results: `data/results/<D>.txt`

