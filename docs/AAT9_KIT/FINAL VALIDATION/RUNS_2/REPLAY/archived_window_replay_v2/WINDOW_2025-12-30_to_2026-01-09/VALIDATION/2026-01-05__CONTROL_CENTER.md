# Analysis Arena Control Center Daily Run Report — D=2026-01-05 (H=2026-01-04)

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
- Results date `D`: `2026-01-05`
- History date `H`: `2026-01-04`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-05/control_center`
- Truth Control Center dir: `sharepacks/2026-01-05/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,447,024` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:024:PERM,HP2 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,244,004` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:449:PERM,HP7 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | tail:04|ev:7|2d:7|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,033,334` hints=`P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:033:PERM,HP7 | Combined:0/5-3/8 | 014,023,149 | Prog:27|Hidden | tail:33|ev:4|2d:4|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,668,066` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP6 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`168,118,668` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP3 | Combined:1/6-2/7 | 013,049,058 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,008,599` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:008:HOT,CONS | Combined:3/8-4/9 | 015,016,025 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`025,008,005` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 015,016,025 | Prog:27|Hidden | tail:08|ev:2|2d:2|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`229,224,299` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:044:PERM,HP7 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:44|ev:4|2d:4|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=26,WATCH=13`, `top_alert=NewYork4:Evening:3:016 025 349; OntarioCanada4:Combined:3:127 469 037; Virginia4:Evening:3:038 056 389`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=OntarioCanada4:13:0/5-4/9; Michigan4:8:1/6-2/7; SouthCarolina4:7:0/5-1/6; NewYork4:5:0/5-1/6; NewJersey4:4:3/8-4/9; PuertoRico4:3:1/6-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=62`, `top_alerts=NewJersey4:Combined:A11:008:BOX; SouthCarolina4:Combined:A11:677:BOX; Virginia4:Combined:A11:008:BOX; Connecticut4:Evening:A05:024:STR8_8; Connecticut4:Evening:A09:-:STR8_8; Delaware4:Evening:A05:449:STR8_3; Florida4:Combined:A05:033:STR8_3; Indiana4:Evening:A05:244:STR8_3`
- Profit compound events: `rows=9`, `top_events=NewJersey4:Combined:ENGINE_GOV:P85; Virginia4:Combined:ENGINE_GOV:P85; SouthCarolina4:Combined:STRAIGHT_GATE:P80; Connecticut4:Evening:CARRY_PERM:P70; Michigan4:Combined:CARRY_PERM:P70; NewYork4:Midday:CARRY_PERM:P70; Florida4:Combined:CLAMP_4:P25; Indiana4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-05/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-05/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=12`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=7`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
