# Aux / Control Center Parity Audit

- Purpose: verify that selected frozen gold-day Aux / Control Center artifacts can be regenerated from the recorded workbook snapshot without drift.
- Samples audited: `3`
- Overall PASS: `3/3`

## 2025-12-30 / Florida4
- Workbook snapshot: `data/history/Pick3StatsC4_2025-12-29.xlsm`
- Aux summary: `sharepacks/2025-12-30/Florida4/aux/Florida4/summary.json`
- Aux draws: `sharepacks/2025-12-30/Florida4/aux/draws`
- Inferred top-list limit: `10`
- Draw parity: `PASS`
  - Combined: `PASS` counts `1000==1000`
  - Midday: `PASS` counts `1000==1000`
  - Evening: `PASS` counts `1000==1000`
- Summary parity: `PASS`
- Control Center parity: `PASS`
  - blackapple_alerts: `PASS` rows `3==3` file `sharepacks/2025-12-30/control_center/blackapple_alerts.csv`
  - due_doubles: `PASS` rows `3==3` file `sharepacks/2025-12-30/control_center/due_doubles.csv`
  - vtrac_repeat_watch: `PASS` rows `3==3` file `sharepacks/2025-12-30/control_center/vtrac_repeat_watch.csv`
  - profit_alerts: `PASS` rows `4==4` file `sharepacks/2025-12-30/control_center/profit_alerts.csv`
- Overall: `PASS`

## 2025-12-31 / Virginia4
- Workbook snapshot: `data/history/Pick3StatsC4_2025_12_30.xlsm`
- Aux summary: `sharepacks/2025-12-31/Virginia4/aux/Virginia4/summary.json`
- Aux draws: `sharepacks/2025-12-31/Virginia4/aux/draws`
- Inferred top-list limit: `10`
- Draw parity: `PASS`
  - Combined: `PASS` counts `1000==1000`
  - Midday: `PASS` counts `1000==1000`
  - Evening: `PASS` counts `1000==1000`
- Summary parity: `PASS`
- Control Center parity: `PASS`
  - blackapple_alerts: `PASS` rows `3==3` file `sharepacks/2025-12-31/control_center/blackapple_alerts.csv`
  - due_doubles: `PASS` rows `3==3` file `sharepacks/2025-12-31/control_center/due_doubles.csv`
  - vtrac_repeat_watch: `PASS` rows `3==3` file `sharepacks/2025-12-31/control_center/vtrac_repeat_watch.csv`
  - profit_alerts: `PASS` rows `4==4` file `sharepacks/2025-12-31/control_center/profit_alerts.csv`
- Overall: `PASS`

## 2026-01-09 / Delaware4
- Workbook snapshot: `data/history/Pick3StatsC4_2026-01-08.xlsm`
- Aux summary: `sharepacks/2026-01-09/Delaware4/aux/Delaware4/summary.json`
- Aux draws: `sharepacks/2026-01-09/Delaware4/aux/draws`
- Inferred top-list limit: `10`
- Draw parity: `PASS`
  - Combined: `PASS` counts `1000==1000`
  - Midday: `PASS` counts `1000==1000`
  - Evening: `PASS` counts `1000==1000`
- Summary parity: `PASS`
- Control Center parity: `PASS`
  - blackapple_alerts: `PASS` rows `3==3` file `sharepacks/2026-01-09/control_center/blackapple_alerts.csv`
  - due_doubles: `PASS` rows `3==3` file `sharepacks/2026-01-09/control_center/due_doubles.csv`
  - vtrac_repeat_watch: `PASS` rows `3==3` file `sharepacks/2026-01-09/control_center/vtrac_repeat_watch.csv`
  - profit_alerts: `PASS` rows `6==6` file `sharepacks/2026-01-09/control_center/profit_alerts.csv`
- Overall: `PASS`
