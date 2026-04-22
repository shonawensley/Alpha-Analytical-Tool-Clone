# Analysis Arena Control Center Daily Run Report — D=2025-12-31 (H=2025-12-30)

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
- Results date `D`: `2025-12-31`
- History date `H`: `2025-12-30`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/control_center`
- Truth Control Center dir: `sharepacks/2025-12-31/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011,559,003` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP5 | Combined:0/5-4/9 | 013,018,023 | Prog:27|Hidden | tail:3|ev:12|2d:8|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,144,499` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP4 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | tail:9|ev:5|2d:1|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,116,077` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-3/8 | 014,059,068 | Prog:27|Hidden | tail:77|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,244,668` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP4 | Combined:1/6-2/7 | 037,127,136 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`136,244,599` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:335:PERM,HP5 | Combined:1/6-2/7 | 016,056,126 | Prog:27|Hidden | tail:02|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,224,118` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:224:PERM,HP6 | Combined:3/8-4/9 | 017,018,019 | Prog:27|Hidden | tail:4|ev:6|2d:1|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,677,116` hints=`P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:677:PERM,HP3 | Combined:0/5-1/6 | 014,016,017 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`003,224,034` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:003:PERM,HP5 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:03|ev:12|2d:10|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=26,WATCH=12`, `top_alert=Connecticut4:Midday:3:138 237 489; NorthCarolina4:Evening:3:034 124 016; Ohio4:Midday:3:035 278 026; OntarioCanada4:Combined:3:127 136 019`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=PuertoRico4:10:1/6-4/9; SouthCarolina4:8:0/5-1/6; Michigan4:6:1/6-2/7; Delaware4:4:2/7-3/8; NewYork4:4:0/5-1/6; Pennsylvania4:4:3/8-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=58`, `top_alerts=Connecticut4:Evening:A05:011:STR8_3; Connecticut4:Midday:A08:-:OVERLAY; Delaware4:Combined:A05:244:STR8_3; Florida4:Evening:A05:077:STR8_3; Florida4:Evening:A09:-:STR8_8; Indiana4:Evening:A05:244:STR8_3; Michigan4:Evening:A05:335:STR8_3; NewJersey4:Combined:A05:224:STR8_3`
- Profit compound events: `rows=12`, `top_events=NewJersey4:Combined:CARRY_PERM:P70; NewYork4:Midday:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; Ohio4:Midday:CARRY_PERM:P70; SouthCarolina4:Midday:CARRY_PERM:P70; OntarioCanada4:Midday:DBL_BA:P45; Connecticut4:Evening:CLAMP_4:P25; Indiana4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2025-12-31/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2025-12-31/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=69`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=48`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
