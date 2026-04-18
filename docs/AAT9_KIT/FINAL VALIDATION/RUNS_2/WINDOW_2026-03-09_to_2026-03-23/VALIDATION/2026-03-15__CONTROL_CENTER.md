# Analysis Arena Control Center Daily Run Report — D=2026-03-15 (H=2026-03-14)

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
- Results date `D`: `2026-03-15`
- History date `H`: `2026-03-14`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-15/control_center`
- Truth Control Center dir: `sharepacks/2026-03-15/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,689,346` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP4 | Combined:0/5-4/9 | 014,059,149 | Prog:27|Hidden | tail:01|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,049,599` hints=`P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:049:HOT,CONS | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:94|ev:12|2d:10|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`699,224,668` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A04:469:PERSIST,BA | Combined:0/5-4/9 | 015,016,038 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,224,669` hints=`P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)) | A01:056:CONS,3V | Combined:0/5-4/9 | 027,189,279 | Prog:27|Hidden | tail:99|ev:7|2d:7|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`455,044,008` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:008:PERM,HP7 | Combined:0/5-1/6 | 037,127,379 | Prog:27|Hidden | tail:44|ev:2|2d:2|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,099,004` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:099:HOT,CONS | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:44|ev:9|2d:9|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`668,039,012` hints=`P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)) | A01:039:CONS,3V | Combined:0/5-1/6 | 015,016,126 | Prog:27|Hidden | tail:03|ev:10|2d:10|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`388,138,368` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:003:PERM,HP7 | Combined:0/5-4/9 | 013,139,238 | Prog:27|Hidden | tail:3|ev:4|2d:2|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=24,WATCH=14`, `top_alert=Florida4:Midday:3:038 056 146; NewYork4:Midday:3:058 238 247; Ohio4:Midday:3:049 247 013; SouthCarolina4:Evening:3:049 058 247`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewYork4:9:0/5-1/6; OntarioCanada4:7:2/7-3/8; NewJersey4:6:3/8-4/9; Connecticut4:2:0/5-4/9; Florida4:2:0/5-4/9; Indiana4:1:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=60`, `top_alerts=Delaware4:Combined:A11:049:BOX; NewJersey4:Combined:A11:099:BOX; Connecticut4:Combined:A05:559:STR8_3; Delaware4:Combined:A01:049:BOX; Delaware4:Combined:A01:049:BOX; Delaware4:Midday:A01:017:BOX; Delaware4:Midday:A01:047:BOX; Delaware4:Midday:A05:007:STR8_3`
- Profit compound events: `rows=11`, `top_events=Delaware4:Combined:ENGINE_GOV:P85; NewJersey4:Combined:STRAIGHT_GATE:P80; Florida4:Midday:CARRY_PERM:P70; Michigan4:Combined:CARRY_PERM:P70; OntarioCanada4:Midday:CARRY_PERM:P70; Delaware4:Evening:CLAMP_4:P25; Indiana4:Combined:CLAMP_4:P25; Michigan4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-15/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-15/control_center/profit_alerts_eval_merged.csv` (missing)
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
