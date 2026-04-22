# Analysis Arena Control Center Daily Run Report — D=2026-01-02 (H=2026-01-01)

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
- Results date `D`: `2026-01-02`
- History date `H`: `2026-01-01`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-02/control_center`
- Truth Control Center dir: `sharepacks/2026-01-02/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,559,388` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:006:PERM,HP2 | Combined:0/5-4/9 | 015,025,035 | Prog:27|Hidden | tail:01|ev:12|2d:11|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,449,499` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:014:CONS,3V | Combined:2/7-3/8 | 038,056,146 | Prog:27|Hidden | tail:49|ev:12|2d:9|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,466,366` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP3 | Combined:0/5-3/8 | 023,068,167 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,668,367` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP6 | Combined:1/6-2/7 | 028,046,136 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,069,599` hints=`P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:006:HOT,CONS | Combined:1/6-2/7 | 016,019,026 | Prog:27|Hidden | tail:06|ev:6|2d:6|xvar|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,599,899` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:599:PERM,HP2 | Combined:3/8-4/9 | 025,027,049 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`688,788,778` hints=`P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:788:PERM,HP7 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,223,229` hints=`P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:044:PERM,HP5 | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:33|ev:6|2d:6|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=1,OFF=26,WATCH=15`, `top_alert=NorthCarolina4:Evening:4:025 034 124`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=PuertoRico4:12:1/6-4/9; OntarioCanada4:7:0/5-4/9; NorthCarolina4:5:0/5-4/9; Ohio4:5:1/6-4/9; Delaware4:2:2/7-3/8; Florida4:2:0/5-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=64`, `top_alerts=Michigan4:Combined:A11:006:BOX; Ohio4:Combined:A11:055:BOX; Connecticut4:Midday:A05:006:STR8_3; Delaware4:Midday:A01:014:BOX; Delaware4:Midday:A05:004:STR8_3; Florida4:Evening:A05:559:STR8_3; Indiana4:Evening:A05:244:STR8_3; Michigan4:Combined:A01:069:BOX`
- Profit compound events: `rows=12`, `top_events=Michigan4:Combined:CARRY_PERM_HARDLOCK:P95; Ohio4:Combined:STRAIGHT_GATE:P80; Connecticut4:Midday:CARRY_PERM:P70; Florida4:Evening:CARRY_PERM:P70; OntarioCanada4:Midday:CARRY_PERM:P70; SouthCarolina4:Combined:CARRY_PERM:P70; PuertoRico4:Evening:IDX_ECHO_CLAMP:P65; Connecticut4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-02/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-02/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=64`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=40`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
