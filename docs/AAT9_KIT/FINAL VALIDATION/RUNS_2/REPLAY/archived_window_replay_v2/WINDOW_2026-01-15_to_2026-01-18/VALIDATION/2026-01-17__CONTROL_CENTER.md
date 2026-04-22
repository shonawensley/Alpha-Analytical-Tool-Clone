# Analysis Arena Control Center Daily Run Report — D=2026-01-17 (H=2026-01-16)

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
- Results date `D`: `2026-01-17`
- History date `H`: `2026-01-16`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/control_center`
- Truth Control Center dir: `sharepacks/2026-01-17/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,599,899` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-4/9 | 029,038,128 | Prog:27|Hidden | tail:08|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`167,259,007` hints=`P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:249:PERM,HP4 | Combined:2/7-3/8 | 014,068,149 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`255,225,559` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:255:PERM,HP3 | Combined:0/5-4/9 | 015,018,025 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368,077,559` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:368:PERSIST,BA | Combined:1/6-2/7 | 015,024,123 | Prog:27|Hidden | tail:05|ev:1|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011,559,117` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP3 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:11|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,019,499` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A01:019:CONS,3V | Combined:3/8-4/9 | 029,128,236 | Prog:27|Hidden | tail:01|ev:8|2d:8|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`377,339,368` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:339:PERM,HP3 | Combined:0/5-1/6 | 167,257,059 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,244,225` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:348:PERSIST,BA | Combined:0/5-4/9 | 027,057,127 | Prog:27|Hidden | tail:44|ev:1|2d:1|trial|moderate`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=4,OFF=20,WATCH=18`, `top_alert=Indiana4:Combined:3:015 024 123; Michigan4:Midday:3:058 238 247; NorthCarolina4:Evening:3:027 045 279; Virginia4:Evening:3:059 149 023`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewYork4:7:0/5-1/6; NorthCarolina4:7:0/5-4/9; Connecticut4:5:0/5-4/9; Virginia4:5:1/6-4/9; Pennsylvania4:4:3/8-4/9; Delaware4:3:2/7-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=57`, `top_alerts=Pennsylvania4:Combined:A11:244:BOX; Connecticut4:Combined:A09:-:STR8_8; Connecticut4:Evening:A05:559:STR8_3; Delaware4:Evening:A05:249:STR8_8; Florida4:Combined:A05:255:STR8_3; Indiana4:Combined:A04:368:BOX; Indiana4:Combined:A08:-:OVERLAY; Indiana4:Midday:A05:077:STR8_3`
- Profit compound events: `rows=7`, `top_events=Pennsylvania4:Combined:ENGINE_GOV:P85; Connecticut4:Evening:CARRY_PERM:P70; NewJersey4:Midday:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; SouthCarolina4:Combined:CARRY_PERM:P70; Virginia4:Evening:DBL_BA:P45; Virginia4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-17/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-17/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=71`, `hit_decay=1`, `hit_any_decay=1`
- Merged summary: `rows=42`, `hit_decay=1`, `hit_any_decay=1`, `top_hits=NewJersey4:Combined:A11:A08`

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
