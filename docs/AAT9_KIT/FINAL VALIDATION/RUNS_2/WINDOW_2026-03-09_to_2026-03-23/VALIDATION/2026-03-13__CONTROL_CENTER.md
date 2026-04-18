# Analysis Arena Control Center Daily Run Report — D=2026-03-13 (H=2026-03-12)

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
- Results date `D`: `2026-03-13`
- History date `H`: `2026-03-12`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-13/control_center`
- Truth Control Center dir: `sharepacks/2026-03-13/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,668,336` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:066:PERM,HP6 | Combined:0/5-4/9 | 014,149,248 | Prog:27|Hidden | tail:06|ev:3|2d:3|xvar|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,559,005` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:005:PERM,HP2 | Combined:0/5-3/8 | 012,039,048 | Prog:27|Hidden | tail:07|ev:7|2d:6|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,499,226` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:499:PERM,HP6 | Combined:0/5-4/9 | 012,015,023 | Prog:27|Hidden | tail:99|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,788,005` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:005:PERM,HP2 | Combined:0/5-4/9 | 018,019,028 | Prog:27|Hidden | tail:05|ev:2|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`688,455,559` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:008:PERM,HP5 | Combined:0/5-1/6 | 019,028,037 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`244,004,167` hints=`P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:004:HOT,CONS | Combined:3/8-4/9 | 049,247,058 | Prog:27|Hidden | tail:44|ev:10|2d:10|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,039,006` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:006:HOT,CONS | Combined:0/5-1/6 | 059,149,239 | Prog:27|Hidden | tail:93|ev:7|2d:7|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009,388,366` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:003:PERM,HP6 | Combined:0/5-4/9 | 058,148,238 | Prog:27|Hidden | tail:3|ev:4|2d:1|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=21,WATCH=18`, `top_alert=NewJersey4:Combined:3:049 247 058; NewJersey4:Evening:3:049 058 067; Ohio4:Midday:3:049 058 013`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Delaware4:7:0/5-3/8; Ohio4:6:1/6-4/9; NewYork4:5:0/5-1/6; PuertoRico4:5:1/6-4/9; Florida4:3:0/5-4/9; OntarioCanada4:3:2/7-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=70`, `top_alerts=NewJersey4:Combined:A11:004:BOX; NewYork4:Combined:A11:006:BOX; Ohio4:Combined:A11:033:BOX; Pennsylvania4:Combined:A11:003:BOX; Connecticut4:Evening:A05:066:STR8_3; Delaware4:Combined:A10:557:STR8_3; Delaware4:Evening:A05:005:STR8_3; Florida4:Midday:A05:499:STR8_3`
- Profit compound events: `rows=11`, `top_events=Ohio4:Combined:ENGINE_GOV:P85; Pennsylvania4:Combined:ENGINE_GOV:P85; NewJersey4:Combined:STRAIGHT_GATE:P80; NewJersey4:Midday:CARRY_PERM:P70; NewYork4:Midday:CARRY_PERM:P70; OntarioCanada4:Midday:CARRY_PERM:P70; OntarioCanada4:Evening:IDX_ECHO_BASE:P60; Ohio4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-13/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-13/control_center/profit_alerts_eval_merged.csv` (missing)
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
