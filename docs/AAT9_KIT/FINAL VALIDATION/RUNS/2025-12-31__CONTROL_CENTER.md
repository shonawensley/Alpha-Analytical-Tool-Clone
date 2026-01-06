# Control Center Daily Run Report — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/`
- Control Center bundle: `sharepacks/2025-12-31/control_center/`
- Control Center report: `sharepacks/2025-12-31/control_center/control_center_report.md`
- Meta (provenance): `sharepacks/2025-12-31/control_center/meta.json`

Cross-state Brain-1 synthesis (same day):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__DAY_SYNTHESIS.md`

## 0) Provenance
- Results date (D): `2025-12-31`
- History date (H): `2025-12-30`
- History workbook: `data/history/Pick3StatsC4_2025_12_30.xlsm`
- Results file: `data/results/2025-12-31.txt`
- States in scope: `14`

## 1) Boards snapshot

### 1.1 Blackapple
- Artifacts: `sharepacks/2025-12-31/control_center/blackapple_alerts.csv`, `sharepacks/2025-12-31/control_center/blackapple_alerts.md`
- Rows: `42`
- Status counts: `ALERT=4, OFF=26, WATCH=12`
- States in ALERT: `4`
- States in WATCH: `10`
- Rows with Midday hits (D-only diagnostic): `5`
- Rows with Evening hits (D-only diagnostic): `5`

### 1.2 Due Doubles
- Artifacts: `sharepacks/2025-12-31/control_center/due_doubles.csv`, `sharepacks/2025-12-31/control_center/due_doubles.md`
- Rows: `42`
- Midday winner-in-family True rows: `3`
- Evening winner-in-family True rows: `3`
- Top due rows by Draws Since Double:
  - `SouthCarolina4` `Evening`: `11`
  - `Pennsylvania4` `Midday`: `10`
  - `PuertoRico4` `Combined`: `10`
  - `PuertoRico4` `Midday`: `9`
  - `SouthCarolina4` `Combined`: `8`

### 1.3 VTRAC Repeat Watch
- Artifacts: `sharepacks/2025-12-31/control_center/vtrac_repeat_watch.csv`, `sharepacks/2025-12-31/control_center/vtrac_repeat_watch.md`
- Rows: `42`
- Rows where Current==WinnerVTRAC: `1`
- Hit rows:
  - `PuertoRico4` `Evening`: idx `24` == winnerVT `24`

## 2) Profit Alerts (A01-A12) daily evaluation

Artifacts:
- Board: `sharepacks/2025-12-31/control_center/profit_alerts.csv`, `sharepacks/2025-12-31/control_center/profit_alerts.md`
- Eval: `sharepacks/2025-12-31/control_center/profit_alerts_eval.csv`, `sharepacks/2025-12-31/control_center/profit_alerts_eval.md`
- Merged: `sharepacks/2025-12-31/control_center/profit_alerts_eval_merged.csv`

Auto-summary (from eval CSV):
- Rows fired: `69`
- HIT(decay) rows (variant-faithful): `0`
- HIT_any(decay) rows (any-outcome diagnostic): `0`
- HIT<=7 rows (variant-faithful diagnostic): `0`
- HIT<=14 rows (variant-faithful diagnostic): `0`
- HIT_any<=7 rows (any-outcome diagnostic): `2`
- HIT_any<=14 rows (any-outcome diagnostic): `2`
- CENSORED rows (insufficient future results files): `0`
- By AlertId (fired / hit_decay / hit_any_decay):
  - `A01`: `5` / `0` / `0`
  - `A02`: `8` / `0` / `0`
  - `A04`: `14` / `0` / `0`
  - `A05`: `14` / `0` / `0`
  - `A08`: `14` / `0` / `0`
  - `A09`: `2` / `0` / `0`
  - `A10`: `3` / `0` / `0`
  - `A11`: `2` / `0` / `0`
  - `A12`: `7` / `0` / `0`
- By AlertId (hit_14 / hit_any_14):
  - `A01`: `0` / `0`
  - `A02`: `0` / `0`
  - `A04`: `0` / `0`
  - `A05`: `0` / `0`
  - `A08`: `0` / `0`
  - `A09`: `0` / `1`
  - `A10`: `0` / `0`
  - `A11`: `0` / `0`
  - `A12`: `0` / `1`

Merged-episode summary:
- Merged rows (deduped play-sets): `48`
- HIT(decay) merged episodes: `0`
- HIT_any(decay) merged episodes: `0`
- HIT<=7 merged episodes (diagnostic): `0`
- HIT<=14 merged episodes (diagnostic): `0`
- HIT_any<=7 merged episodes (diagnostic): `1`
- HIT_any<=14 merged episodes (diagnostic): `1`
- Episode cost units (implied_set_size * decay_max): min/median/max = `6` / `8` / `18`

Top HIT merged episodes:
- (no HIT(decay) merged episodes; showing `HIT<=14 (diagnostic)` rows instead)
- `SouthCarolina4` `Midday` (S=3, set=4, decay=2): `A12` + promoters `A08` hit_any<=14 (timing not recorded in merged CSV)

## 3) Profitability framing (unitless, evaluation-only)

Working definitions (v0):
- `1 unit = 1 line played for 1 draw-step`
- `episode_cost_units = implied_set_size * decay_max` (merged view)

Notes:
- Do not interpret this as ROI until you attach payout assumptions per venue/state.
- Use it to compare relative cost pressure across alert types and windows.

## 4) Cross-state synthesis (Brain-2 vs Brain-1)

Fill:
- Day environment class (short label): `...`
- What Control Center signaled that Brain-1 agreed with: `...`
- What Control Center signaled that Brain-1 contradicted: `...`

## 5) Fix-now vs fix-later

- Fix-now (pipeline correctness / drift / missing artifacts): `...`
- Fix-later (tuning / hypothesis tests / evaluation lens changes): `...`
- Next run: `...`
