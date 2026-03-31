# Analysis Arena Control Center Daily Run Report — D=2026-01-07 (H=2026-01-06)

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
- Results date `D`: `2026-01-07`
- History date `H`: `2026-01-06`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-01-07/control_center`
- Truth Control Center dir: `sharepacks/2026-01-07/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,244,229` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A09::VTRAC,REP | Combined:0/5-4/9 | 012,014,018 | Prog:27|Hidden | tail:24|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,003,044` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:038:CONS,3V | Combined:2/7-3/8 | 016,025,034 | Prog:27|Hidden | tail:03|ev:6|2d:6|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,346,336` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:033:PERM,HP4 | Combined:3/8-4/9 | 059,257,023 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,066,004` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP5 | Combined:1/6-2/7 | 015,016,025 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,011,001` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:344:PERM,HP3 | Combined:1/6-2/7 | 049,139,589 | Prog:27|Hidden | tail:44|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,189,088` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:778:PERM,HP7 | Combined:3/8-4/9 | 027,035,038 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`008,001,667` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:001:PERM,HP5 | Combined:0/5-1/6 | 016,169,268 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,244,229` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:244:PERM,HP7 | Combined:0/5-4/9 | 018,027,036 | Prog:27|Hidden | -`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=22,WATCH=17`, `top_alert=Florida4:Combined:3:059 257 023; PuertoRico4:Combined:3:059 149 167; PuertoRico4:Evening:3:057 138 489`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewJersey4:8:3/8-4/9; Delaware4:6:2/7-3/8; Indiana4:6:1/6-2/7; PuertoRico4:5:1/6-4/9; SouthCarolina4:3:0/5-1/6; Florida4:2:3/8-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=65`, `top_alerts=Virginia4:Combined:A11:001:BOX; Connecticut4:Combined:A05:224:STR8_3; Connecticut4:Midday:A09:-:STR8_8; Delaware4:Combined:A05:334:STR8_3; Delaware4:Midday:A01:038:BOX; Delaware4:Midday:A07:038:BOX; Delaware4:Midday:A07:035:BOX; Florida4:Combined:A08:-:OVERLAY`
- Profit compound events: `rows=13`, `top_events=Virginia4:Combined:ENGINE_GOV:P85; Delaware4:Combined:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; Connecticut4:Midday:CLAMP_4:P25; Florida4:Evening:CLAMP_4:P25; Indiana4:Combined:CLAMP_4:P25; Michigan4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-07/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-07/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=76`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=56`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
