# Analysis Arena Control Center Daily Run Report — D=2026-03-22 (H=2026-03-21)

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
- Results date `D`: `2026-03-22`
- History date `H`: `2026-03-21`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-22/control_center`
- Truth Control Center dir: `sharepacks/2026-03-22/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`113,224,003` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:136:PERSIST,BA | Combined:0/5-4/9 | 015,016,025 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,599,006` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:001:PERM,HP5 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:3|ev:1|light`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`118,024,224` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP3 | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,002,259` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:023:CONS,3V | Combined:0/5-4/9 | 016,026,036 | Prog:27|Hidden | tail:02|ev:8|2d:8|xvar|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`445,344,244` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:009:PERM,HP4 | Combined:0/5-1/6 | 046,145,469 | Prog:27|Hidden | tail:55|ev:5|2d:5|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`445,344,455` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:003:PERM,HP5 | Combined:3/8-4/9 | 015,016,045 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`066,668,667` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:066:HOT,CONS | Combined:0/5-1/6 | 013,067,139 | Prog:27|Hidden | tail:66|ev:7|2d:7|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`499,599,088` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:499:HOT,CONS | Combined:0/5-4/9 | 013,049,139 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:44|ev:12|2d:11|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=22,WATCH=17`, `top_alert=Connecticut4:Evening:3:056 146 038; Connecticut4:Midday:3:059 167 257; NorthCarolina4:Midday:3:049 058 238`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Pennsylvania4:9:0/5-4/9; SouthCarolina4:8:0/5-1/6; Connecticut4:5:0/5-4/9; OntarioCanada4:4:2/7-3/8; Virginia4:3:0/5-4/9; Indiana4:2:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=70`, `top_alerts=NewYork4:Combined:A11:066:BOX; NorthCarolina4:Combined:A11:499:BOX; Connecticut4:Evening:A04:136:BOX; Connecticut4:Evening:A05:113:STR8_3; Connecticut4:Evening:A08:-:OVERLAY; Connecticut4:Midday:A08:-:OVERLAY; Delaware4:Evening:A05:001:STR8_3; Florida4:Evening:A05:224:STR8_3`
- Profit compound events: `rows=11`, `top_events=NorthCarolina4:Combined:STRAIGHT_GATE:P80; Connecticut4:Evening:CARRY_PERM:P70; Indiana4:Evening:CARRY_PERM:P70; OntarioCanada4:Evening:CARRY_PERM:P70; NewYork4:Combined:DBL_BA:P45; NewYork4:Midday:DBL_BA:P45; Connecticut4:Midday:CLAMP_4:P25; Michigan4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-22/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-22/control_center/profit_alerts_eval_merged.csv` (missing)
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
