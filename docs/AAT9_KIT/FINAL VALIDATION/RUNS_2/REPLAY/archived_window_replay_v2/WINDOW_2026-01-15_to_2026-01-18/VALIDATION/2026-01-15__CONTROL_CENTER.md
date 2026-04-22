# Analysis Arena Control Center Daily Run Report — D=2026-01-15 (H=2026-01-14)

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
- Results date `D`: `2026-01-15`
- History date `H`: `2026-01-14`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/control_center`
- Truth Control Center dir: `sharepacks/2026-01-15/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`899,599,559` hints=`P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:899:PERM,HP5 | Combined:0/5-4/9 | 013,015,019 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`059,249,299` hints=`P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)) | A04:059:PERSIST,BA | Combined:2/7-3/8 | 049,059,149 | Prog:27|Hidden | tail:04|ev:2|2d:1|trial|moderate`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`177,577,224` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP6 | Combined:3/8-4/9 | 015,025,027 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`599,339,667` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:339:PERM,HP7 | Combined:1/6-2/7 | 015,123,168 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`114,344,014` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:1/6-2/7 | 015,016,126 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,136,179` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:001:HOT,CONS | Combined:3/8-4/9 | 038,128,389 | Prog:27|Hidden | tail:01|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,377,337` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:009:PERM,HP4 | Combined:0/5-1/6 | 023,167,239 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,344,255` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:245:PERSIST,BA | Combined:0/5-4/9 | 146,479,029 | Prog:27|Hidden | tail:00|ev:4|2d:4|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=6,OFF=24,WATCH=12`, `top_alert=Indiana4:Combined:4:015 123 168; Delaware4:Evening:3:027 126 279; Florida4:Evening:3:059 167 257; NorthCarolina4:Combined:3:146 479 029; OntarioCanada4:Midday:3:469 019 028`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=OntarioCanada4:8:0/5-4/9; NewJersey4:7:3/8-4/9; Michigan4:6:1/6-2/7; Indiana4:5:1/6-2/7; NewYork4:3:0/5-1/6; NorthCarolina4:3:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=69`, `top_alerts=NewJersey4:Combined:A11:001:BOX; OntarioCanada4:Combined:A11:002:BOX; Virginia4:Combined:A11:005:BOX; Connecticut4:Midday:A05:899:STR8_3; Delaware4:Evening:A04:059:BOX; Delaware4:Evening:A05:599:STR8_3; Delaware4:Evening:A08:-:OVERLAY; Florida4:Evening:A05:224:STR8_3`
- Profit compound events: `rows=13`, `top_events=NewJersey4:Combined:ENGINE_GOV:P85; OntarioCanada4:Combined:ENGINE_GOV:P85; Virginia4:Combined:ENGINE_GOV:P85; Delaware4:Evening:CARRY_PERM:P70; Michigan4:Evening:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; PuertoRico4:Combined:CARRY_PERM:P70`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-15/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-15/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=77`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=50`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
