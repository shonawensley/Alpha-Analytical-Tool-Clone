# Analysis Arena Control Center Daily Run Report — D=2026-03-18 (H=2026-03-17)

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
- Results date `D`: `2026-03-18`
- History date `H`: `2026-03-17`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-18/control_center`
- Truth Control Center dir: `sharepacks/2026-03-18/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,559,244` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP3 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:99|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`099,399,599` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:399:PERM,HP7 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:3|ev:6|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,224,114` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A09::VTRAC,REP | Combined:0/5-4/9 | 012,017,023 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,599,224` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:559:PERM,HP5 | Combined:0/5-4/9 | 014,015,024 | Prog:27|Hidden | tail:24|ev:2|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,559,044` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:055:PERM,HP4 | Combined:0/5-1/6 | 019,028,037 | Prog:27|Hidden | tail:55|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,118,038` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A09::VTRAC,REP | Combined:3/8-4/9 | 015,019,025 | Prog:27|Hidden | tail:99|ev:6|2d:6|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`035,667,036` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:667:PERM,HP4 | Combined:0/5-1/6 | 013,067,139 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`112,117,177` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:138:PERSIST,BA | Combined:0/5-4/9 | 049,238,247 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=23,WATCH=15`, `top_alert=NorthCarolina4:Combined:3:049 238 247; NorthCarolina4:Evening:3:238 247 013; Ohio4:Combined:3:368 026 035; Ohio4:Midday:3:058 238 589`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Ohio4:6:1/6-4/9; NewJersey4:5:3/8-4/9; Indiana4:4:0/5-4/9; PuertoRico4:4:1/6-4/9; Virginia4:3:0/5-4/9; Delaware4:2:0/5-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=56`, `top_alerts=Pennsylvania4:Combined:A11:077:BOX; Connecticut4:Evening:A05:244:STR8_3; Delaware4:Midday:A05:399:STR8_3; Florida4:Combined:A05:224:STR8_3; Florida4:Combined:A09:-:STR8_8; Indiana4:Midday:A05:559:STR8_3; Michigan4:Midday:A05:055:STR8_3; NewJersey4:Evening:A05:499:STR8_3`
- Profit compound events: `rows=10`, `top_events=Pennsylvania4:Combined:STRAIGHT_GATE:P80; Indiana4:Midday:CARRY_PERM:P70; PuertoRico4:Combined:CARRY_PERM:P70; Connecticut4:Combined:CLAMP_4:P25; Florida4:Evening:CLAMP_4:P25; Michigan4:Evening:CLAMP_4:P25; NewYork4:Midday:CLAMP_4:P25; Ohio4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-18/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-18/control_center/profit_alerts_eval_merged.csv` (missing)
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
