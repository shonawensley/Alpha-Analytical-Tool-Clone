# AAT9 - Macro Roadmap

## Vision Snapshot
- **Brain 1 - Per-State Optimization:** each state runs its full tool stack (Stable Pattern, Digit Reduction, V-TRAC, Aux features, future Hot Zones) to isolate winning pattern candidates, manage historical timelines, and tune wagering thresholds locally.
- **Brain 2 - Aggregate Control Center:** the integrated app aggregates state insights (Due Doubles, Black Apple, VT repeat watch, Aux compound scores, overall analysis ranks) to decide which states are favourable for play and to manage profitability across the portfolio.
- Goal: optimise self-contained tools first, then combine insights into aggregate scoring, profitability tracking, and eventually predictive AI while preserving guardrails.

## Module Status Checklist
| Module | Current state | Next focus |
| --- | --- | --- |
| Stable Pattern Extractor | Integrated; needs enhanced analysis outputs & three-value handling | Train on real examples, add winners logging & training bundles |
| Digit Reduction Analyzer V2 | Rebuilt overlay + scoring + winners map | Continue optimisation and tie into aggregate scoring |
| V-TRAC Analyzer | Restored with winner/family/VT-straight highlights | Feed overlays into Aux scoring & Control Center rankings |
| Auxiliary Features | SSOT windows, repeat watch baselines | Build compound scoring, expose JSON evidence |
| Hot Zones (planned) | Not yet implemented | Design complementary features aligned with Stable extractor |
| Winners Logging | Compact + analyzer-style reports with downloads | Expand metadata for profitability & ML |
| Combination Former | Pending | Generate actionable play slips from ranked candidates |
| Profitability Logging | Pending | Record wagers, cost, ROI, state history |
| ML On-Ramp | JSON tags seeded; no models yet | Define training rows, compare rules vs ML |

## Daily Run Lifecycle
1. **Data ingest:** refresh `Pick3StatsC4`, run pipeline builders (tables, draws, Aux).
2. **Module execution:** run Stable, Digit Reduction, V-TRAC, Aux (and future Hot Zones) on combined + variant data.
3. **Analysis outputs:** persist HTML/CSV/JSON to `data/outputs/analysis/<module>/<STATE>/...` with timestamps.
4. **Winners logging:** generate compact + analyzer reports, metadata JSON, training overlays.
5. **Training bundle update:** drop artefacts into `analysis/<module>/<STATE>/training/` for offline review.
6. **Profitability tracking (future):** append wager logs once scoring thresholds dictate plays.

## Optimisation Phases
1. Self-contained tool mastery Ã¢â€ â€™ optimise each module against real winners, capture insights + JSON tags.
2. Aggregated analysis Ã¢â€ â€™ combine module outputs to form compound scores & state rankings.
3. Profitability instrumentation Ã¢â€ â€™ log outcomes, build dashboards, enforce wagering gates.
4. Predictive enhancement Ã¢â€ â€™ introduce ML gradually, comparing against rule baselines while guardrails remain rule-driven.

## Data & Artefact Guidelines
- Tables: `data/outputs/tables/<STATE>/` (Combined/Midday/Evening).
- Analysis outputs: `data/outputs/analysis/<module>/<STATE>/...`.
- Training bundles: mirror analysis folders for reproducibility.
- Winners logs: `data/outputs/analysis/winners/<STATE>/...` with metadata JSON.

## Training & Evaluation Strategy
- Ensure each module produces analysis output + winners log + training artefact.
- Derive features from winners JSON (winner/family/VT-straight hits, Aux evidence) for weekly reviews.
- Maintain per-state regression fixtures for manual audits and automated tests.

## Pending Major Tasks
- Stable Pattern analysis helper for three-value normalization and highlight outputs.
- Combination Former to convert ranked candidates into suggested plays (boxed/straight).
- Hot Zones design, delivering complementary pressure indicators.
- Aux compound scoring weights, synergy rules, UI evidence panels.
- Profitability dashboard capturing ROI and state prioritisation.
- Machine learning harness combining module outputs + Aux + profitability labels.

## Scoring & Wagering Philosophy
- Scores must be evidence-driven: play only when combined conditions exceed thresholds.
- Compound scores = string evidence + Aux confirmations; Aux never overrides base patterns.
- Control Center (Brain 2) manages loss tolerance by focusing on favourable states.

## Machine Learning On-Ramp
- Assemble training rows from module outputs, Aux features, profitability labels.
- Start with interpretable models (RandomForest, XGBoost) and compare against rules-only baselines.
- Keep guardrails ahead of ML; models refine ranking thresholds rather than replacing them.
- Document retraining cadence and feature provenance once established.

## Key References
- `docs/AAT9_KIT/AAT9_Analysis_Insights.md` Ã¢â‚¬â€ analytical signals.
- `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md` Ã¢â‚¬â€ module routing.
- `docs/AAT9_KIT/AAT9_Testing_Roadmap.md` Ã¢â‚¬â€ test coverage.
- `briefings/CODEX_READ_FIRST_AAT9.md` Ã¢â‚¬â€ session protocol & preflight.

## Update Log
- 2025-10-08 Ã¢â‚¬â€ Initial roadmap capturing Brain 1/Brain 2 strategy, module status, daily lifecycle, and pending profitability/ML work.
