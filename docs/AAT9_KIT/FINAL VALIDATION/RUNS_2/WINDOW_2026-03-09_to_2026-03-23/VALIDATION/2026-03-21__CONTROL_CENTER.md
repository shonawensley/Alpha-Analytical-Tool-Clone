# Analysis Arena Control Center Daily Run Report — D=2026-03-21 (H=2026-03-20)

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
- Results date `D`: `2026-03-21`
- History date `H`: `2026-03-20`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-21/control_center`
- Truth Control Center dir: `sharepacks/2026-03-21/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,224,355` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,599,016` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:599:PERM,HP6 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:3|ev:1|light`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,246,114` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP3 | Combined:0/5-4/9 | 014,016,024 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,455,002` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:022:HOT,CONS | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:02|ev:7|2d:6|xvar|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`567,001,599` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:445:HOT,CONS | Combined:0/5-1/6 | 046,136,145 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`455,559,499` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:003:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:03|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,667,013` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:066:HOT,CONS | Combined:0/5-1/6 | 058,238,049 | Prog:27|Hidden | tail:66|ev:6|2d:6|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,117,889` hints=`P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:499:HOT,CONS | Combined:0/5-4/9 | 049,139,148 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:94|ev:14|2d:9|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=22,WATCH=15`, `top_alert=NewYork4:Combined:3:058 238 049; Ohio4:Combined:3:134 017 035; Ohio4:Midday:3:013 589 058; SouthCarolina4:Combined:3:035 278 368; SouthCarolina4:Evening:3:057 138 156`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Michigan4:8:0/5-1/6; Pennsylvania4:7:0/5-4/9; SouthCarolina4:6:0/5-1/6; Connecticut4:3:0/5-4/9; NorthCarolina4:3:0/5-4/9; OntarioCanada4:2:2/7-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=77`, `top_alerts=Indiana4:Combined:A11:022:BOX; Michigan4:Combined:A11:445:BOX; NewYork4:Combined:A11:066:BOX; NorthCarolina4:Combined:A11:499:BOX; Ohio4:Midday:A01:024:BOX; Virginia4:Combined:A11:022:BOX; Connecticut4:Evening:A05:113:STR8_3; Connecticut4:Evening:A09:-:STR8_8`
- Profit compound events: `rows=14`, `top_events=NorthCarolina4:Combined:ENGINE_GOV:P85; Indiana4:Combined:STRAIGHT_GATE:P80; Michigan4:Combined:STRAIGHT_GATE:P80; NewYork4:Combined:STRAIGHT_GATE:P80; Virginia4:Combined:STRAIGHT_GATE:P80; Connecticut4:Evening:CARRY_PERM:P70; Pennsylvania4:Combined:IDX_ECHO_BASE:P60; Connecticut4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-21/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-21/control_center/profit_alerts_eval_merged.csv` (missing)
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
