# Analysis Arena Control Center Daily Run Report — D=2026-03-14 (H=2026-03-13)

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
- Results date `D`: `2026-03-14`
- History date `H`: `2026-03-13`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-14/control_center`
- Truth Control Center dir: `sharepacks/2026-03-14/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,368,689` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP4 | Combined:0/5-4/9 | 059,068,158 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,049,007` hints=`P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:049:HOT,CONS | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:94|ev:13|2d:13|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,226,499` hints=`P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:499:PERM,HP6 | Combined:0/5-4/9 | 012,016,023 | Prog:27|Hidden | tail:99|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`599,788,005` hints=`P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)) | A01:015:CONS,3V | Combined:0/5-4/9 | 027,279,378 | Prog:27|Hidden | tail:05|ev:3|2d:3|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`008,688,455` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 019,028,037 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`004,244,224` hints=`P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:004:HOT,CONS | Combined:3/8-4/9 | 049,139,238 | Prog:27|Hidden | tail:04|ev:14|2d:14|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,006,039` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:006:HOT,CONS | Combined:0/5-1/6 | 012,023,024 | Prog:27|Hidden | tail:06|ev:11|2d:11|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`388,368,009` hints=`P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:003:PERM,HP7 | Combined:0/5-4/9 | 058,067,148 | Prog:27|Hidden | tail:3|ev:5|2d:2|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=8,OFF=16,WATCH=18`, `top_alert=Florida4:Midday:3:056 146 389; Indiana4:Combined:3:027 279 378; Indiana4:Evening:3:027 045 126; NewJersey4:Combined:3:049 139 238; NewJersey4:Evening:3:049 247 058`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Ohio4:8:1/6-4/9; NewYork4:7:0/5-1/6; PuertoRico4:7:1/6-4/9; OntarioCanada4:5:2/7-3/8; NewJersey4:4:3/8-4/9; Pennsylvania4:4:0/5-2/7`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=78`, `top_alerts=Delaware4:Combined:A11:049:BOX; NewJersey4:Combined:A11:004:BOX; NewYork4:Combined:A11:006:BOX; Connecticut4:Combined:A05:559:STR8_3; Delaware4:Combined:A01:049:BOX; Delaware4:Combined:A01:049:BOX; Delaware4:Evening:A09:-:STR8_8; Delaware4:Midday:A01:047:BOX`
- Profit compound events: `rows=13`, `top_events=Delaware4:Combined:ENGINE_GOV:P85; NewJersey4:Combined:STRAIGHT_GATE:P80; Michigan4:Combined:CARRY_PERM:P70; NewYork4:Evening:CARRY_PERM:P70; OntarioCanada4:Midday:CARRY_PERM:P70; Delaware4:Evening:IDX_ECHO_BASE:P60; Pennsylvania4:Combined:IDX_ECHO_BASE:P60; Virginia4:Midday:IDX_ECHO_BASE:P60`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-14/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-14/control_center/profit_alerts_eval_merged.csv` (missing)
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
