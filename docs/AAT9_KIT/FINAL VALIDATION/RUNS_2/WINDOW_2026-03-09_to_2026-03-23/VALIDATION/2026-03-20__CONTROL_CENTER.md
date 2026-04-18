# Analysis Arena Control Center Daily Run Report — D=2026-03-20 (H=2026-03-19)

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
- Results date `D`: `2026-03-20`
- History date `H`: `2026-03-19`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-20/control_center`
- Truth Control Center dir: `sharepacks/2026-03-20/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,113,133` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP6 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,099,399` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:399:PERM,HP7 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:93|ev:3|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`244,114,246` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP4 | Combined:0/5-4/9 | 013,014,016 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,455,155` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP2 | Combined:0/5-4/9 | 012,015,023 | Prog:27|Hidden | tail:55|ev:3|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,001,677` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:055:PERM,HP4 | Combined:0/5-1/6 | 046,145,469 | Prog:27|Hidden | tail:05|ev:7|2d:7|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,499,334` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:049:CONS,3V | Combined:3/8-4/9 | 013,014,015 | Prog:27|Hidden | tail:94|ev:6|2d:6|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`066,035,667` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:066:HOT,CONS | Combined:0/5-1/6 | 013,067,139 | Prog:27|Hidden | tail:66|ev:6|2d:6|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`299,117,088` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:348:PERSIST,BA | Combined:0/5-4/9 | 049,058,139 | Prog:27|Hidden | tail:4|ev:8|2d:4|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=24,WATCH=15`, `top_alert=Florida4:Midday:3:146 479 038; NorthCarolina4:Midday:3:049 058 238; Ohio4:Midday:3:013 589 058`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Indiana4:8:0/5-4/9; Michigan4:6:0/5-1/6; Pennsylvania4:5:0/5-4/9; SouthCarolina4:4:0/5-1/6; Delaware4:3:0/5-3/8; Virginia4:3:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=66`, `top_alerts=NewYork4:Combined:A11:066:BOX; Ohio4:Combined:A11:006:BOX; Connecticut4:Combined:A05:224:STR8_3; Delaware4:Midday:A05:399:STR8_3; Florida4:Combined:A05:244:STR8_3; Florida4:Midday:A08:-:OVERLAY; Indiana4:Combined:A10:002:STR8_3; Indiana4:Evening:A05:559:STR8_3`
- Profit compound events: `rows=12`, `top_events=Ohio4:Combined:ENGINE_GOV:P85; NewYork4:Combined:STRAIGHT_GATE:P80; Florida4:Combined:CARRY_PERM:P70; Indiana4:Evening:CARRY_PERM:P70; Michigan4:Midday:CARRY_PERM:P70; NorthCarolina4:Midday:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; PuertoRico4:Evening:CARRY_PERM:P70`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-20/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-20/control_center/profit_alerts_eval_merged.csv` (missing)
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
