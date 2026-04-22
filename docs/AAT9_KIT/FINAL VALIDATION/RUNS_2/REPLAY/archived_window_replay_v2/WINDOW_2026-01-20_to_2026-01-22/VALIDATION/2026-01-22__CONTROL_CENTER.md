# Analysis Arena Control Center Daily Run Report — D=2026-01-22 (H=2026-01-21)

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
- Results date `D`: `2026-01-22`
- History date `H`: `2026-01-21`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-22/control_center`
- Truth Control Center dir: `sharepacks/2026-01-22/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,006,255` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,255,336` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:133:PERM,HP6 | Combined:0/5-4/9 | 059,068,158 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`007,259,224` hints=`P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:007:HOT,CONS | Combined:0/5-2/7 | 012,013,014 | Prog:27|Hidden | tail:07|ev:4|2d:4|xvar|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`077,001,003` hints=`P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)) | A01:014:CONS,3V | Combined:1/6-2/7 | 057,138,237 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:01|ev:8|2d:8|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,477,559` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:027:CONS,3V | Combined:1/6-2/7 | 013,015,017 | Prog:27|Hidden | tail:07|ev:5|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`017,299,009` hints=`P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:299:PERM,HP4 | Combined:3/8-4/9 | 012,013,023 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`238,337,133` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:337:PERM,HP6 | Combined:0/5-1/6 | 059,068,158 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,778,011` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:006:PERM,HP2 | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=6,OFF=23,WATCH=13`, `top_alert=Ohio4:Midday:4:013 049 058; Indiana4:Combined:3:057 138 237; PuertoRico4:Combined:3:035 368 017; PuertoRico4:Evening:3:057 138 156; Virginia4:Combined:3:045 378 459`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=SouthCarolina4:10:0/5-1/6; Indiana4:9:1/6-2/7; Virginia4:8:1/6-4/9; Florida4:7:0/5-2/7; PuertoRico4:6:1/6-4/9; Delaware4:3:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=62`, `top_alerts=Florida4:Combined:A11:007:BOX; OntarioCanada4:Combined:A11:044:BOX; Virginia4:Evening:A02:033:STR8_3; Virginia4:Evening:A02:339:STR8_3; Connecticut4:Combined:A05:003:STR8_3; Connecticut4:Evening:A09:-:STR8_8; Delaware4:Midday:A05:133:STR8_3; Florida4:Combined:A05:007:STR8_3`
- Profit compound events: `rows=8`, `top_events=Florida4:Combined:STRAIGHT_GATE:P80; OntarioCanada4:Combined:STRAIGHT_GATE:P80; Connecticut4:Evening:IDX_ECHO_BASE:P60; Virginia4:Evening:DBL_BA:P45; NorthCarolina4:Combined:CLAMP_4:P25; OntarioCanada4:Midday:CLAMP_4:P25; Pennsylvania4:Midday:CLAMP_4:P25; Virginia4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-22/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-01-22/control_center/profit_alerts_eval_merged.csv` (missing)
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
