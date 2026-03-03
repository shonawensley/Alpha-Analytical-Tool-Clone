# Control Center Daily Run Report Template (Brain-2, sharepack-aligned)

Purpose: create **one** “Brain-2” Control Center report per results date **D**, so cross-state boards (Blackapple, Due Doubles, VTRAC Repeat Watch, Profit Alerts A01-A12) are evaluated with the same discipline as the per-state Master Validation run reports.

This is evaluation-only:
- Do not change analyzers (Stable/DR/VTRAC/Hot Zones) here.
- Prefer reading from `sharepacks/<D>/...` only (immutable day snapshot).

Definitions:
- **D** = results/winners date (sharepack folder name under `sharepacks/`)
- **H** = history workbook date (tables/draws world snapshot date, usually D-1)
- **Outcomes** = `Midday` and `Evening` only (real winning draws)
- **Combined** = a lens (not a third outcome stream)

Related SSOT docs:
- Control Center export overview: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
- Profit Alerts evaluation rules: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Profit Alerts grading matrix (per A-ID "what is a hit"): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- 12 Trackers interpretation guide: `docs/AAT9_KIT/FINAL VALIDATION/AAT9_12_TRACKERS_ANALYSIS_HELP.MD`

---

## 0) Provenance (fill every time)

- Results date (D): `YYYY-MM-DD`
- History date (H): `YYYY-MM-DD`
- History workbook path: `data/history/Pick3StatsC4_YYYY_MM_DD.xlsm`
- Results file: `data/results/YYYY-MM-DD.txt`
- Sharepack root: `sharepacks/YYYY-MM-DD/`
- Control Center bundle: `sharepacks/YYYY-MM-DD/control_center/`
- States in scope: `N`

Primary artifacts (links):
- `sharepacks/<D>/control_center/control_center_report.md`
- `sharepacks/<D>/control_center/meta.json`

---

## 1) Boards snapshot (what the Control Center is "seeing" today)

Goal: capture what fired, where, and whether there are immediate (D-only) winner overlaps.

### 1.1 Blackapple (BA) board

Artifacts:
- `sharepacks/<D>/control_center/blackapple_alerts.md`
- `sharepacks/<D>/control_center/blackapple_alerts.csv`

Fill:
- Rows fired (total): ``
- States in `ALERT`: ``
- States in `WATCH`: ``
- Any obvious D-only overlaps (Boxed/VTRAC tags present in the board output): ``

Notes (important):
- BA board hits are diagnostic unless you also evaluate them as episodes with a defined window.

### 1.2 Due Doubles board

Artifacts:
- `sharepacks/<D>/control_center/due_doubles.md`
- `sharepacks/<D>/control_center/due_doubles.csv`

Fill:
- Top due-doubles rows to pay attention to (Top-3 or Top-5): ``
- Any Midday/Evening winner-in-family flags set to `True`: ``
- Any "double event" visible in winners (if relevant to your tracker semantics): ``

### 1.3 VTRAC Repeat Watch board

Artifacts:
- `sharepacks/<D>/control_center/vtrac_repeat_watch.md`
- `sharepacks/<D>/control_center/vtrac_repeat_watch.csv`

Fill:
- Rows fired (total): ``
- Any rows where `Current==WinnerVTRAC` is true: ``
- Any high streak/hazard rows worth logging as "watch": ``

---

## 2) Profit Alerts (A01-A12) daily evaluation (the main Brain-2 scoring layer)

Artifacts:
- Board:
  - `sharepacks/<D>/control_center/profit_alerts.md`
  - `sharepacks/<D>/control_center/profit_alerts.csv`
- Shadow-only derived triage:
  - `sharepacks/<D>/control_center/profit_compound_events.md`
  - `sharepacks/<D>/control_center/profit_compound_events.csv`
- Evaluation (windowed episodes):
  - `sharepacks/<D>/control_center/profit_alerts_eval.md`
  - `sharepacks/<D>/control_center/profit_alerts_eval.csv`
  - `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv` (deduped play-sets)

Fill:
- Fired rows (total): ``
- Candidate rows vs promoters (A03/A08 are promoters): ``
- Variant-faithful scorecard headline (HIT(decay) totals): ``
- Any-outcome (cross-variant) headline (HIT_any(decay) totals): ``
- Diagnostic timeframe headlines (<=7 / <=14):
  - Variant-faithful: `HIT<=7=` `HIT<=14=`
  - Any-outcome: `HIT_any<=7=` `HIT_any<=14=`
- Merged-episode headline:
  - merged_rows_total: ``
  - merged HIT(decay): ``
  - merged HIT_any(decay): ``
  - merged diagnostics: `HIT<=7=` `HIT<=14=` `HIT_any<=7=` `HIT_any<=14=`

Top episodes (what to actually inspect):
- List 3-10 merged episodes with the highest Strength and/or first HIT:
  - `StateKey / Variant / implied_set_size / alert_ids / promoters / status / t_hit / hit_when / hit_type`

Interpretation notes:
- Do not interpret "many rows fired" as "many bets". Use the merged play-set view.
- Combined is a lens, not an outcome; evaluation must grade against real outcomes only (Midday/Evening).

---

## 3) Profitability framing (simple, unitless, non-invasive)

Goal: connect hit timing to cost pressure without building a wagering engine.

Record:
- Default unit assumption (fill one):
  - `1 unit = 1 line played for 1 draw-step`
- For merged episodes, define (v0):
  - `episode_cost_units = implied_set_size * DecayMax`

Fill:
- Median time-to-hit (merged HIT episodes only): ``
- Cost units of HIT episodes (range): ``
- Cost units of EXPIRED episodes (range): ``

Optional (only if you supply payout assumptions separately):
- Break-even hit-rate estimate for a set of size S over W steps:
  - `break_even_hit_rate = (S * W) / payout_units`

---

## 4) Cross-state synthesis (tie Brain-2 back to Brain-1 run reports)

Link to the per-day cross-state synthesis (Brain-1 summaries):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md`

Fill:
- Day environment class (examples: "high convergence", "dominant-lane miss", "noisy heat"): ``
- What CC signaled that Brain-1 agreed with: ``
- What CC signaled that Brain-1 contradicted: ``

---

## 5) Fix-now vs fix-later (do not lose these)

- Fix-now (pipeline correctness / drift / missing artifacts): ``
- Fix-later (tuning / hypothesis tests / new evaluation lenses): ``
- Next run (what to watch for on the next day): ``
