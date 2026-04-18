# Analysis Arena Control Center Daily Run Report — D=2026-03-09 (H=2026-03-08)

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
- Results date `D`: `2026-03-09`
- History date `H`: `2026-03-08`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-09/control_center`
- Truth Control Center dir: `sharepacks/2026-03-09/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`168,189,006` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:168:PERSIST,BA | Combined:0/5-4/9 | 149,167,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,129,259` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:006:HOT,CONS | Combined:0/5-3/8 | 012,013,014 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,778,889` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP7 | Combined:0/5-4/9 | 036,045,126 | Prog:27|Hidden | tail:24|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011,225,255` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:078:PERSIST,BA | Combined:0/5-4/9 | 016,025,027 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`118,778,188` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:119:PERM,HP3 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,177,007` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:006:HOT,CONS | Combined:0/5-1/6 | 013,049,058 | Prog:27|Hidden | tail:06|ev:7|2d:7|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,368,689` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP4 | Combined:0/5-1/6 | 023,059,149 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`599,003,344` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:035:PERSIST,BA | Combined:0/5-4/9 | 049,058,247 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=9,OFF=20,WATCH=13`, `top_alert=Connecticut4:Combined:3:149 167 014; Connecticut4:Evening:3:038 056 146; Indiana4:Evening:3:027 126 279; NorthCarolina4:Combined:3:049 058 247; NorthCarolina4:Evening:3:049 058 238`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Delaware4:7:0/5-3/8; Pennsylvania4:4:0/5-2/7; Virginia4:4:0/5-4/9; Ohio4:3:1/6-4/9; Indiana4:2:0/5-4/9; Connecticut4:1:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=61`, `top_alerts=Delaware4:Combined:A11:006:BOX; NewJersey4:Combined:A11:006:BOX; Ohio4:Combined:A11:003:BOX; Connecticut4:Combined:A04:168:BOX; Connecticut4:Evening:A05:667:STR8_3; Connecticut4:Evening:A08:-:OVERLAY; Delaware4:Combined:A05:006:STR8_3; Delaware4:Combined:A10:557:STR8_3`
- Profit compound events: `rows=12`, `top_events=NewJersey4:Combined:ENGINE_GOV:P85; Ohio4:Combined:ENGINE_GOV:P85; Delaware4:Combined:STRAIGHT_GATE:P80; Indiana4:Evening:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; OntarioCanada4:Combined:CARRY_PERM:P70; PuertoRico4:Evening:CARRY_PERM:P70; Virginia4:Midday:CARRY_PERM:P70`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-09/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-09/control_center/profit_alerts_eval_merged.csv` (missing)
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
