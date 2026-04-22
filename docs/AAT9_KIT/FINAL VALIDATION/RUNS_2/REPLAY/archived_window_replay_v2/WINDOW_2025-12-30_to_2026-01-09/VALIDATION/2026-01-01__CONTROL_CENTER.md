# Analysis Arena Control Center Daily Run Report — D=2026-01-01 (H=2025-12-31)

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
- Results date `D`: `2026-01-01`
- History date `H`: `2025-12-31`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/control_center`
- Truth Control Center dir: `sharepacks/2026-01-01/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`011,388,368` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:008:HOT,CONS | Combined:0/5-4/9 | 038,058,138 | Prog:27|Hidden | tail:11|ev:16|2d:13|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,014,144` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP6 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | tail:9|ev:10|2d:4|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,138,559` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:077:PERM,HP5 | Combined:0/5-3/8 | 059,068,149 | Prog:27|Hidden | tail:77|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,244,668` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:677:PERM,HP6 | Combined:1/6-2/7 | 037,127,379 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,133,599` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:006:HOT,CONS | Combined:1/6-2/7 | 016,049,056 | Prog:27|Hidden | tail:06|ev:6|2d:6|xvar|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`299,778,118` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:778:PERM,HP7 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:4|ev:2|trial|moderate`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`778,677,678` hints=`P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:778:PERM,HP6 | Combined:0/5-1/6 | 027,038,057 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,003,223` hints=`P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:224:PERM,HP5 | Combined:0/5-4/9 | 012,013,023 | Prog:27|Hidden | tail:03|ev:9|2d:7|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=30,WATCH=8`, `top_alert=NorthCarolina4:Evening:4:025 034 124; NewYork4:Evening:3:349 358 016; NewYork4:Midday:3:016 027 056; NorthCarolina4:Combined:3:012 013 023`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=PuertoRico4:12:1/6-4/9; OntarioCanada4:5:0/5-4/9; Connecticut4:4:0/5-4/9; Indiana4:3:1/6-2/7; NorthCarolina4:3:0/5-4/9; Ohio4:3:1/6-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=63`, `top_alerts=Connecticut4:Combined:A11:008:BOX; Michigan4:Combined:A11:006:BOX; Ohio4:Combined:A11:055:BOX; Connecticut4:Evening:A02:011:STR8_3; Connecticut4:Evening:A05:011:STR8_3; Delaware4:Combined:A05:244:STR8_3; Florida4:Evening:A05:077:STR8_3; Indiana4:Combined:A05:677:STR8_3`
- Profit compound events: `rows=10`, `top_events=Michigan4:Combined:ENGINE_GOV:P85; Connecticut4:Combined:STRAIGHT_GATE:P80; Ohio4:Combined:STRAIGHT_GATE:P80; NorthCarolina4:Midday:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; SouthCarolina4:Midday:CARRY_PERM:P70; PuertoRico4:Evening:IDX_ECHO_CLAMP:P65; Florida4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-01/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-01/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=70`, `hit_decay=0`, `hit_any_decay=0`
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
