# Analysis Arena Control Center Daily Run Report — D=2026-01-09 (H=2026-01-08)

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
- Results date `D`: `2026-01-09`
- History date `H`: `2026-01-08`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-09/control_center`
- Truth Control Center dir: `sharepacks/2026-01-09/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,448,229` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A09::VTRAC,REP | Combined:0/5-4/9 | 012,014,018 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,033,445` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:033:PERM,HP6 | Combined:2/7-3/8 | 034,124,349 | Prog:27|Hidden | tail:33|ev:7|2d:7|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`255,559,224` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:224:PERM,HP4 | Combined:3/8-4/9 | 068,158,167 | Prog:27|Hidden | tail:55|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,669,004` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:004:PERM,HP2 | Combined:1/6-2/7 | 017,027,037 | Prog:27|Hidden | tail:04|ev:2|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,019,059` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:334:PERM,HP3 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:44|ev:2|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,137,014` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:003:PERM,HP2 | Combined:3/8-4/9 | 015,016,025 | Prog:27|Hidden | tail:03|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,001,255` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:005:HOT,CONS | Combined:0/5-1/6 | 015,016,025 | Prog:27|Hidden | tail:05|ev:7|2d:7|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,066,446` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:066:PERM,HP6 | Combined:0/5-4/9 | 036,126,369 | Prog:27|Hidden | -`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=24,WATCH=13`, `top_alert=Florida4:Midday:3:058 049 067; Pennsylvania4:Midday:3:012 013 014; PuertoRico4:Combined:3:059 149 167; PuertoRico4:Evening:3:057 138 489; SouthCarolina4:Midday:3:035 368 017`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Florida4:3:3/8-4/9; Ohio4:3:1/6-3/8; Pennsylvania4:3:3/8-4/9; Delaware4:2:2/7-3/8; Michigan4:2:1/6-2/7; NorthCarolina4:2:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=65`, `top_alerts=NewYork4:Combined:A11:005:BOX; Connecticut4:Combined:A05:224:STR8_3; Connecticut4:Midday:A09:-:STR8_8; Delaware4:Midday:A05:033:STR8_3; Florida4:Combined:A10:077:STR8_3; Florida4:Evening:A05:224:STR8_3; Indiana4:Combined:A05:004:STR8_3; Michigan4:Combined:A05:334:STR8_3`
- Profit compound events: `rows=13`, `top_events=NewYork4:Combined:ENGINE_GOV:P85; Florida4:Evening:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; Ohio4:Combined:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; PuertoRico4:Midday:CARRY_PERM:P70; Delaware4:Midday:DBL_BA:P45; NewYork4:Evening:DBL_BA:P45`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-09/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-09/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=83`, `hit_decay=1`, `hit_any_decay=1`
- Merged summary: `rows=52`, `hit_decay=1`, `hit_any_decay=1`, `top_hits=NewJersey4:Evening:A12:A08`

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
