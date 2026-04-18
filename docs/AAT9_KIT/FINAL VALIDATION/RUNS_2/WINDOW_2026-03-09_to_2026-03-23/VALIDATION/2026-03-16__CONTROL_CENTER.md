# Analysis Arena Control Center Daily Run Report — D=2026-03-16 (H=2026-03-15)

Purpose
- Review the full-day Control Center tables for the Analysis Arena branch from both the predictive-day snapshot and the post-results evaluation side.
- Surface how Control Center state trackers carried into Brain 2 board posture and translation-sandbox state receipts.
- This is an arena-native daily report, not the older standalone board shell.

Template / SSOT anchors
- Control Center daily template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`
- Brain 2 operating template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Context-tool arena feed: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Aux / Control Center arena contract: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md`
- Aux / Control Center handoff: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__HANDOFF.md`
- Aux / Control Center export slice: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__EXPORT_SLICE.md`

## 0) Provenance
- Results date `D`: `2026-03-16`
- History date `H`: `2026-03-15`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-16/control_center`
- Truth Control Center dir: `sharepacks/2026-03-16/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,344,044` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP6 | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:01|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,559,059` hints=`P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)) | A09::VTRAC,REP | Combined:0/5-3/8 | 469,019,127 | Prog:27|Hidden | tail:3|ev:6|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,006,669` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:669:PERM,HP5 | Combined:0/5-4/9 | 038,056,128 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,224,559` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:224:PERM,HP3 | Combined:0/5-4/9 | 027,279,378 | Prog:27|Hidden | tail:05|ev:3|2d:3|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`044,067,677` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 019,028,127 | Prog:27|Hidden | tail:44|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,099,179` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:099:PERM,HP4 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:99|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,003,559` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:035:CONS,3V | Combined:0/5-1/6 | 067,256,346 | Prog:27|Hidden | tail:03|ev:8|2d:8|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`138,378,366` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:003:PERM,HP7 | Combined:0/5-4/9 | 013,058,139 | Prog:27|Hidden | tail:03|ev:2|2d:1|trial|moderate`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=1,OFF=22,WATCH=19`, `top_alert=Ohio4:Midday:3:013 049 148`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewYork4:11:0/5-1/6; Delaware4:2:0/5-3/8; Ohio4:2:1/6-4/9; SouthCarolina4:2:0/5-1/6; Florida4:1:0/5-4/9; NewJersey4:1:3/8-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=59`, `top_alerts=Connecticut4:Midday:A05:559:STR8_3; Delaware4:Midday:A05:399:STR8_3; Delaware4:Midday:A09:-:STR8_8; Florida4:Midday:A05:669:STR8_3; Indiana4:Evening:A05:224:STR8_3; Michigan4:Evening:A05:044:STR8_3; Michigan4:Midday:A09:-:STR8_8; NewJersey4:Combined:A05:099:STR8_3`
- Profit compound events: `rows=8`, `top_events=Connecticut4:Midday:CARRY_PERM:P70; NewYork4:Evening:CARRY_PERM:P70; Indiana4:Combined:CLAMP_4:P25; Michigan4:Evening:CLAMP_4:P25; Ohio4:Evening:CLAMP_4:P25; Pennsylvania4:Evening:CLAMP_4:P25; PuertoRico4:Midday:CLAMP_4:P25; Virginia4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-16/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-16/control_center/profit_alerts_eval_merged.csv` (missing)
- Eval summary: `Eval rows missing.`
- Merged summary: `Merged rows missing.`

## 4) Cross-State Synthesis

- Strongest board-level Control Center carry-through: `...`
- Strongest tracker-rich state that Brain 2 elevated correctly: `...`
- Strongest tracker-rich state that still feels underused or overused: `...`
- How profit alerts / compound events aligned with board posture: `...`
- Due doubles / mirror-double family notes: `...`

## 5) Fix-Now Vs Fix-Later

- Fix-now: `...`
- Fix-later: `...`
- Next run / next window watch item: `...`
