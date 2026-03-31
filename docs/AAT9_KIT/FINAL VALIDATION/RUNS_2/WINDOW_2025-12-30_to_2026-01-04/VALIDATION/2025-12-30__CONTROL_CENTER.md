# Analysis Arena Control Center Daily Run Report — D=2025-12-30 (H=2025-12-29)

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
- Results date `D`: `2025-12-30`
- History date `H`: `2025-12-29`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2025-12-30/control_center`
- Truth Control Center dir: `sharepacks/2025-12-30/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,011,000` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP7 | Combined:0/5-4/9 | 167,059,068 | Prog:27|Hidden | tail:3|ev:14|2d:8|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,113,244` hints=`P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:113:PERM,HP7 | Combined:2/7-3/8 | 015,016,045 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,177,677` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:077:PERM,HP5 | Combined:0/5-3/8 | 014,068,149 | Prog:27|Hidden | tail:77|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,116,068` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:256:PERSIST,BA | Combined:1/6-2/7 | 127,028,037 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,244,136` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:244:PERM,HP3 | Combined:1/6-2/7 | 014,024,034 | Prog:27|Hidden | tail:02|ev:2|2d:2|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,118,299` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:224:HOT,CONS | Combined:3/8-4/9 | 012,014,017 | Prog:27|Hidden | tail:44|ev:11|2d:9|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`016,778,677` hints=`P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:778:PERM,HP6 | Combined:0/5-1/6 | 016,017,026 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,003,005` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:003:PERM,HP5 | Combined:0/5-4/9 | 059,149,257 | Prog:27|Hidden | tail:03|ev:4|2d:4|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=23,WATCH=15`, `top_alert=NorthCarolina4:Evening:4:016 025 034; Indiana4:Combined:3:127 028 037; NorthCarolina4:Combined:3:059 149 257; Ohio4:Combined:3:057 138 156`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=PuertoRico4:8:1/6-4/9; SouthCarolina4:6:0/5-1/6; Michigan4:4:1/6-2/7; Ohio4:3:1/6-4/9; Delaware4:2:2/7-3/8; NewYork4:2:0/5-1/6`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=55`, `top_alerts=NewJersey4:Combined:A11:224:BOX; Connecticut4:Evening:A05:011:STR8_3; Delaware4:Evening:A05:113:STR8_3; Florida4:Evening:A05:077:STR8_3; Indiana4:Combined:A04:256:BOX; Indiana4:Combined:A05:066:STR8_3; Indiana4:Combined:A08:-:OVERLAY; Michigan4:Evening:A05:244:STR8_3`
- Profit compound events: `rows=9`, `top_events=NewJersey4:Combined:STRAIGHT_GATE:P80; Connecticut4:Evening:CARRY_PERM:P70; Indiana4:Combined:CARRY_PERM:P70; SouthCarolina4:Combined:CARRY_PERM:P70; Virginia4:Evening:CARRY_PERM:P70; Delaware4:Evening:CLAMP_4:P25; Pennsylvania4:Evening:CLAMP_4:P25; PuertoRico4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2025-12-30/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2025-12-30/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=72`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=44`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
