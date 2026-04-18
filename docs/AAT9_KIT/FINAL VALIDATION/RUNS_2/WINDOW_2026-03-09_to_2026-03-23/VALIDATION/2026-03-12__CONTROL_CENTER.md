# Analysis Arena Control Center Daily Run Report — D=2026-03-12 (H=2026-03-11)

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
- Results date `D`: `2026-03-12`
- History date `H`: `2026-03-11`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-12/control_center`
- Truth Control Center dir: `sharepacks/2026-03-12/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,168,006` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:068:CONS,3V | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:06|ev:4|2d:4|xvar|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`499,599,047` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:499:PERM,HP4 | Combined:0/5-3/8 | 048,147,246 | Prog:27|Hidden | tail:99|ev:4|2d:4|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,077,499` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:499:PERM,HP6 | Combined:0/5-4/9 | 249,267,015 | Prog:27|Hidden | tail:99|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`788,015,688` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:788:PERM,HP6 | Combined:0/5-4/9 | 038,058,138 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`455,688,488` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:488:PERM,HP6 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`177,244,006` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:068:CONS,3V | Combined:0/5-1/6 | 049,247,058 | Prog:27|Hidden | tail:06|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,368,559` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP4 | Combined:0/5-1/6 | 689,014,023 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`009,344,388` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A04:349:PERSIST,BA | Combined:0/5-4/9 | 238,013,049 | Prog:27|Hidden | tail:3|ev:2|2d:1|trial|moderate`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=6,OFF=22,WATCH=14`, `top_alert=Indiana4:Evening:3:027 126 279; NewJersey4:Combined:3:049 247 058; NewJersey4:Evening:3:247 049 058; NewYork4:Combined:3:689 014 023; NorthCarolina4:Combined:3:238 013 049`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Delaware4:5:0/5-3/8; NorthCarolina4:4:0/5-4/9; Ohio4:4:1/6-4/9; NewYork4:3:0/5-1/6; PuertoRico4:3:1/6-4/9; Indiana4:2:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=62`, `top_alerts=NewJersey4:Combined:A01:068:BOX; NewJersey4:Combined:A01:068:BOX; NewJersey4:Combined:A11:006:BOX; Ohio4:Combined:A11:033:BOX; Connecticut4:Evening:A05:006:STR8_3; Connecticut4:Midday:A01:068:BOX; Delaware4:Combined:A05:499:STR8_3; Delaware4:Combined:A10:557:STR8_3`
- Profit compound events: `rows=11`, `top_events=NewJersey4:Combined:ENGINE_GOV:P85; Ohio4:Combined:STRAIGHT_GATE:P80; NewJersey4:Midday:CARRY_PERM:P70; NewYork4:Midday:CARRY_PERM:P70; OntarioCanada4:Midday:CARRY_PERM:P70; SouthCarolina4:Evening:CARRY_PERM:P70; Virginia4:Combined:CARRY_PERM:P70; OntarioCanada4:Evening:IDX_ECHO_BASE:P60`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-12/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-12/control_center/profit_alerts_eval_merged.csv` (missing)
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
