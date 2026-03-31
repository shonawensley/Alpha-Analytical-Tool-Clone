# Analysis Arena Control Center Daily Run Report — D=2026-01-19 (H=2026-01-18)

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
- Results date `D`: `2026-01-19`
- History date `H`: `2026-01-18`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-01-19/control_center`
- Truth Control Center dir: `sharepacks/2026-01-19/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,058,559` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP3 | Combined:0/5-4/9 | 029,038,047 | Prog:27|Hidden | tail:06|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,259,007` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP3 | Combined:2/7-3/8 | 059,158,257 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`388,255,378` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:889:PERM,HP6 | Combined:0/5-4/9 | 013,017,018 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`077,007,038` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:007:HOT,CONS | Combined:1/6-2/7 | 012,013,014 | LR:4|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,011,017` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP3 | Combined:1/6-2/7 | 012,014,017 | Prog:27|Hidden | tail:11|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`004,014,019` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:000:HOT,CONS | Combined:3/8-4/9 | 569,047,056 | Prog:27|Hidden | tail:04|ev:13|2d:13|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`377,337,177` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:339:PERM,HP4 | Combined:0/5-1/6 | 149,167,257 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,244,225` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:244:PERM,HP7 | Combined:0/5-4/9 | 167,059,068 | Prog:27|Hidden | tail:04|ev:5|2d:5|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=21,WATCH=16`, `top_alert=NewJersey4:Combined:3:569 047 056; NewYork4:Combined:3:149 167 257; Ohio4:Evening:3:012 013 014; Pennsylvania4:Evening:3:057 237 012; PuertoRico4:Combined:3:049 139 148`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewYork4:11:0/5-1/6; Pennsylvania4:8:3/8-4/9; SouthCarolina4:4:0/5-1/6; Indiana4:3:1/6-2/7; Connecticut4:2:0/5-4/9; Delaware4:2:2/7-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=65`, `top_alerts=Indiana4:Combined:A11:007:BOX; NewJersey4:Combined:A11:000:BOX; Pennsylvania4:Combined:A11:004:BOX; Connecticut4:Evening:A05:224:STR8_3; Delaware4:Combined:A05:559:STR8_3; Florida4:Combined:A05:889:STR8_3; Indiana4:Combined:A01:017:BOX; Indiana4:Combined:A05:007:STR8_3`
- Profit compound events: `rows=13`, `top_events=Indiana4:Combined:ENGINE_GOV:P85; Pennsylvania4:Combined:ENGINE_GOV:P85; Michigan4:Evening:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; OntarioCanada4:Combined:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; PuertoRico4:Evening:CARRY_PERM:P70; NewJersey4:Midday:IDX_ECHO_BASE:P60`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-19/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-01-19/control_center/profit_alerts_eval_merged.csv` (missing)
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
