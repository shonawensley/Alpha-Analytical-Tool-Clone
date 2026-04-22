# Analysis Arena Control Center Daily Run Report — D=2026-01-08 (H=2026-01-07)

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
- Results date `D`: `2026-01-08`
- History date `H`: `2026-01-07`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/control_center`
- Truth Control Center dir: `sharepacks/2026-01-08/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,229,448` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:224:PERM,HP7 | Combined:0/5-4/9 | 012,018,019 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`033,334,003` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:2/7-3/8 | 016,025,034 | Prog:27|Hidden | tail:33|ev:13|2d:12|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,346,335` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:334:PERM,HP4 | Combined:3/8-4/9 | 023,068,158 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,066,669` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:344:PERM,HP4 | Combined:1/6-2/7 | 015,017,025 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,019,144` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:344:PERM,HP4 | Combined:1/6-2/7 | 015,016,025 | Prog:27|Hidden | tail:44|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,189,089` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:778:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:03|ev:1|2d:1|trial|moderate`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,008,256` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:005:HOT,CONS | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:05|ev:3|2d:3|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,244,559` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:244:PERM,HP6 | Combined:0/5-4/9 | 027,036,126 | Prog:27|Hidden | -`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=2,OFF=25,WATCH=15`, `top_alert=Ohio4:Combined:3:589 679 013; Virginia4:Midday:3:138 156 489`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewJersey4:10:3/8-4/9; Indiana4:8:1/6-2/7; NewYork4:3:0/5-1/6; Connecticut4:2:0/5-4/9; OntarioCanada4:2:0/5-4/9; Ohio4:1:1/6-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=59`, `top_alerts=NewYork4:Combined:A11:005:BOX; Connecticut4:Combined:A05:224:STR8_3; Delaware4:Midday:A05:033:STR8_3; Delaware4:Midday:A09:-:STR8_8; Florida4:Combined:A05:334:STR8_3; Indiana4:Evening:A05:344:STR8_3; Michigan4:Midday:A05:344:STR8_3; NewJersey4:Combined:A10:556:STR8_3`
- Profit compound events: `rows=12`, `top_events=NewYork4:Combined:ENGINE_GOV:P85; NorthCarolina4:Evening:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; Virginia4:Evening:CARRY_PERM:P70; Delaware4:Midday:DBL_BA:P45; Florida4:Combined:CLAMP_4:P25; Michigan4:Combined:CLAMP_4:P25; NewJersey4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-08/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-08/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=70`, `hit_decay=2`, `hit_any_decay=2`
- Merged summary: `rows=49`, `hit_decay=2`, `hit_any_decay=2`, `top_hits=NewJersey4:Midday:A12:; NewJersey4:Midday:A04:`

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
