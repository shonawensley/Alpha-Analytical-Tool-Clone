# Analysis Arena Control Center Daily Run Report — D=2026-03-23 (H=2026-03-22)

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
- Results date `D`: `2026-03-23`
- History date `H`: `2026-03-22`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-23/control_center`
- Truth Control Center dir: `sharepacks/2026-03-23/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`113,025,117` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:113:PERM,HP7 | Combined:0/5-4/9 | 015,016,027 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`011,001,038` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:001:PERM,HP6 | Combined:0/5-3/8 | 019,037,127 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,066,114` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP4 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:02|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,259,004` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:005:PERM,HP2 | Combined:0/5-4/9 | 027,057,127 | Prog:27|Hidden | tail:04|ev:7|2d:7|xvar|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,445,055` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:055:PERM,HP2 | Combined:0/5-1/6 | 127,136,019 | Prog:27|Hidden | tail:55|ev:7|2d:7|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,344,001` hints=`P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:344:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,667,006` hints=`P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:006:HOT,CONS | Combined:0/5-1/6 | 049,238,247 | Prog:27|Hidden | tail:66|ev:10|2d:10|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,889,599` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:499:HOT,CONS | Combined:0/5-4/9 | 013,049,067 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:44|ev:6|2d:6|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=23,WATCH=14`, `top_alert=Michigan4:Combined:4:127 136 019; Connecticut4:Evening:3:056 146 038; NewYork4:Combined:3:049 238 247; Pennsylvania4:Combined:3:059 149 014; SouthCarolina4:Evening:3:057 138 156`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Pennsylvania4:11:0/5-4/9; SouthCarolina4:9:0/5-1/6; Virginia4:5:0/5-4/9; Ohio4:4:1/6-4/9; NewJersey4:3:3/8-4/9; Michigan4:2:0/5-1/6`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=68`, `top_alerts=NewYork4:Combined:A11:006:BOX; NorthCarolina4:Combined:A11:499:BOX; Connecticut4:Evening:A05:113:STR8_3; Connecticut4:Evening:A08:-:OVERLAY; Delaware4:Evening:A05:001:STR8_3; Florida4:Evening:A05:224:STR8_3; Indiana4:Evening:A05:005:STR8_3; Michigan4:Combined:A08:-:OVERLAY`
- Profit compound events: `rows=13`, `top_events=NorthCarolina4:Combined:STRAIGHT_GATE:P80; Indiana4:Evening:CARRY_PERM:P70; NewJersey4:Evening:CARRY_PERM:P70; Virginia4:Evening:CARRY_PERM:P70; NewYork4:Combined:DBL_BA:P45; Delaware4:Midday:CLAMP_4:P25; NewJersey4:Midday:CLAMP_4:P25; NewYork4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-23/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-23/control_center/profit_alerts_eval_merged.csv` (missing)
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
