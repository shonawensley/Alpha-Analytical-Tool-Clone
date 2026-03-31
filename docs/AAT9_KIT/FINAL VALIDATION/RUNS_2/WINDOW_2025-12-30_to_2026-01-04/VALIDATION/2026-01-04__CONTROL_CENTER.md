# Analysis Arena Control Center Daily Run Report — D=2026-01-04 (H=2026-01-03)

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
- Results date `D`: `2026-01-04`
- History date `H`: `2026-01-03`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-01-04/control_center`
- Truth Control Center dir: `sharepacks/2026-01-04/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,456,024` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:004:PERM,HP2 | Combined:0/5-4/9 | 012,014,023 | Prog:27|Hidden | tail:06|ev:4|2d:4|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,559,004` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:2/7-3/8 | 015,018,025 | Prog:27|Hidden | tail:04|ev:10|2d:9|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,334,033` hints=`P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:346:PERSIST,BA | Combined:0/5-3/8 | 149,014,023 | Prog:27|Hidden | tail:33|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,668,138` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP7 | Combined:1/6-2/7 | 016,018,026 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`168,668,156` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:446:PERM,HP4 | Combined:1/6-2/7 | 013,049,058 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`599,299,229` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:778:PERM,HP6 | Combined:3/8-4/9 | 017,018,027 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`038,005,025` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:889:PERM,HP6 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`229,299,044` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:044:PERM,HP7 | Combined:0/5-4/9 | 012,016,019 | Prog:27|Hidden | tail:44|ev:4|2d:4|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=1,OFF=27,WATCH=14`, `top_alert=Florida4:Combined:3:149 014 023`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=OntarioCanada4:11:0/5-4/9; Michigan4:6:1/6-2/7; SouthCarolina4:6:0/5-1/6; Virginia4:6:1/6-4/9; NewYork4:3:0/5-1/6; PuertoRico4:3:1/6-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=58`, `top_alerts=OntarioCanada4:Combined:A11:007:BOX; SouthCarolina4:Combined:A11:002:BOX; Connecticut4:Combined:A05:004:STR8_3; Delaware4:Combined:A09:-:STR8_8; Delaware4:Midday:A05:004:STR8_3; Florida4:Combined:A04:346:BOX; Florida4:Combined:A05:033:STR8_3; Florida4:Combined:A08:-:OVERLAY`
- Profit compound events: `rows=8`, `top_events=OntarioCanada4:Combined:ENGINE_GOV:P85; SouthCarolina4:Combined:STRAIGHT_GATE:P80; Florida4:Combined:CARRY_PERM:P70; Delaware4:Combined:IDX_ECHO_BASE:P60; Delaware4:Evening:CLAMP_4:P25; NewYork4:Evening:CLAMP_4:P25; Ohio4:Evening:CLAMP_4:P25; Pennsylvania4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-04/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-04/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=67`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=49`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
