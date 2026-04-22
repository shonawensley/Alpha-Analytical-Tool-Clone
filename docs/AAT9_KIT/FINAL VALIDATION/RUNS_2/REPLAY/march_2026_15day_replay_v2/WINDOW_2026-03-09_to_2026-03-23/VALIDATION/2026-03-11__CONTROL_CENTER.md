# Analysis Arena Control Center Daily Run Report — D=2026-03-11 (H=2026-03-10)

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
- Results date `D`: `2026-03-11`
- History date `H`: `2026-03-10`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-11/control_center`
- Truth Control Center dir: `sharepacks/2026-03-11/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,168,338` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:068:CONS,3V | Combined:0/5-4/9 | 023,239,347 | Prog:27|Hidden | tail:06|ev:4|2d:4|xvar|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,117,499` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:599:PERM,HP2 | Combined:0/5-3/8 | 012,039,057 | Prog:27|Hidden | tail:99|ev:4|2d:4|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,077,066` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP4 | Combined:0/5-4/9 | 015,016,025 | Prog:27|Hidden | tail:24|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`255,788,113` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A09::VTRAC,REP | Combined:0/5-4/9 | 014,018,024 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`559,599,455` hints=`P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:244:PERM,HP4 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`177,009,244` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:006:PERM,HP4 | Combined:0/5-1/6 | 058,148,238 | Prog:27|Hidden | tail:06|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368,224,559` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP3 | Combined:0/5-1/6 | 023,689,014 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,388,003` hints=`P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:003:PERM,HP5 | Combined:0/5-4/9 | 013,049,067 | Prog:27|Hidden | tail:03|ev:1|2d:1|trial|moderate`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=19,WATCH=19`, `top_alert=NewYork4:Combined:3:023 689 014; Ohio4:Midday:3:013 049 058; SouthCarolina4:Midday:3:049 238 247; Virginia4:Midday:3:237 489 012`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Delaware4:3:0/5-3/8; NorthCarolina4:2:0/5-4/9; Ohio4:2:1/6-4/9; OntarioCanada4:2:0/5-4/9; Pennsylvania4:2:0/5-2/7; SouthCarolina4:2:0/5-1/6`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=60`, `top_alerts=Connecticut4:Evening:A05:066:STR8_3; Connecticut4:Midday:A01:068:BOX; Delaware4:Combined:A10:557:STR8_3; Delaware4:Evening:A05:599:STR8_3; Florida4:Evening:A05:224:STR8_3; Indiana4:Combined:A05:007:STR8_3; Indiana4:Midday:A09:-:STR8_8; Michigan4:Evening:A05:244:STR8_3`
- Profit compound events: `rows=9`, `top_events=Delaware4:Evening:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; SouthCarolina4:Combined:CARRY_PERM:P70; Virginia4:Midday:CARRY_PERM:P70; Ohio4:Combined:CLAMP_4:P25; OntarioCanada4:Combined:CLAMP_4:P25; PuertoRico4:Combined:CLAMP_4:P25; SouthCarolina4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-11/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-11/control_center/profit_alerts_eval_merged.csv` (missing)
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
