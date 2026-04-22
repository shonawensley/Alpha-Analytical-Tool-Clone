# Analysis Arena Control Center Daily Run Report — D=2026-01-18 (H=2026-01-17)

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
- Results date `D`: `2026-01-18`
- History date `H`: `2026-01-17`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-18/control_center`
- Truth Control Center dir: `sharepacks/2026-01-18/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`088,559,599` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:088:PERM,HP4 | Combined:0/5-4/9 | 029,038,047 | Prog:27|Hidden | tail:08|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`259,007,559` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:249:PERM,HP5 | Combined:2/7-3/8 | 014,059,149 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225,255,559` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-4/9 | 018,019,028 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`077,368,559` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:005:PERM,HP2 | Combined:1/6-2/7 | 015,123,168 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:3|2d:3|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,177,011` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP3 | Combined:1/6-2/7 | 025,027,038 | Prog:27|Hidden | tail:01|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`019,009,004` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:009:HOT,CONS | Combined:3/8-4/9 | 569,578,029 | Prog:27|Hidden | tail:04|ev:11|2d:11|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`377,339,368` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:339:PERM,HP4 | Combined:0/5-1/6 | 014,149,158 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,778,225` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP7 | Combined:0/5-4/9 | 167,257,059 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=2,OFF=22,WATCH=18`, `top_alert=Indiana4:Combined:4:015 123 168; PuertoRico4:Combined:3:049 139 148`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewYork4:9:0/5-1/6; Pennsylvania4:6:3/8-4/9; NewJersey4:3:3/8-4/9; OntarioCanada4:3:0/5-4/9; SouthCarolina4:3:0/5-1/6; Florida4:2:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=63`, `top_alerts=NewJersey4:Combined:A11:009:BOX; Pennsylvania4:Combined:A11:004:BOX; Connecticut4:Combined:A05:088:STR8_3; Delaware4:Evening:A05:249:STR8_8; Florida4:Combined:A05:599:STR8_3; Florida4:Combined:A09:-:STR8_8; Indiana4:Combined:A05:005:STR8_3; Indiana4:Combined:A08:-:OVERLAY`
- Profit compound events: `rows=10`, `top_events=Pennsylvania4:Combined:ENGINE_GOV:P85; NewJersey4:Combined:STRAIGHT_GATE:P80; Delaware4:Evening:CARRY_PERM:P70; Michigan4:Evening:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; PuertoRico4:Evening:CARRY_PERM:P70; Virginia4:Evening:DBL_BA:P45; Connecticut4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-18/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-18/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=79`, `hit_decay=0`, `hit_any_decay=0`
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
