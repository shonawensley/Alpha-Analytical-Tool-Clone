# Analysis Arena Control Center Daily Run Report — D=2026-03-10 (H=2026-03-09)

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
- Results date `D`: `2026-03-10`
- History date `H`: `2026-03-09`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-10/control_center`
- Truth Control Center dir: `sharepacks/2026-03-10/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`168,006,368` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:066:PERM,HP6 | Combined:0/5-4/9 | 014,023,068 | Prog:27|Hidden | tail:06|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,117,129` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:006:PERM,HP2 | Combined:0/5-3/8 | 012,039,129 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,778,066` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:046:PERSIST,BA | Combined:0/5-4/9 | 027,126,279 | Prog:27|Hidden | tail:24|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`255,027,113` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:088:PERM,HP6 | Combined:0/5-4/9 | 017,027,037 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,778,118` hints=`P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:224:PERM,HP5 | Combined:0/5-1/6 | 038,056,389 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009,459,117` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:009:HOT,CONS | Combined:0/5-1/6 | 058,148,238 | Prog:27|Hidden | tail:06|ev:7|2d:7|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`559,368,224` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP4 | Combined:0/5-1/6 | 023,239,347 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,003,188` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:003:PERM,HP5 | Combined:0/5-4/9 | 049,148,247 | Prog:27|Hidden | tail:03|ev:3|2d:3|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=20,WATCH=17`, `top_alert=Florida4:Combined:3:027 126 279; Michigan4:Combined:3:038 056 389; PuertoRico4:Combined:3:056 146 038; SouthCarolina4:Combined:3:058 238 049; SouthCarolina4:Evening:3:058 238 247`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Indiana4:4:0/5-4/9; Connecticut4:3:0/5-4/9; NewJersey4:2:0/5-1/6; Delaware4:1:0/5-3/8; Florida4:1:0/5-4/9; NewYork4:1:0/5-1/6`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=62`, `top_alerts=NewJersey4:Combined:A11:009:BOX; Ohio4:Combined:A11:003:BOX; Connecticut4:Evening:A05:066:STR8_3; Delaware4:Combined:A05:006:STR8_3; Florida4:Combined:A04:046:BOX; Florida4:Combined:A08:-:OVERLAY; Florida4:Midday:A05:778:STR8_3; Indiana4:Combined:A10:002:STR8_3`
- Profit compound events: `rows=9`, `top_events=NewJersey4:Combined:ENGINE_GOV:P85; Ohio4:Combined:ENGINE_GOV:P85; Connecticut4:Evening:CARRY_PERM:P70; Indiana4:Evening:CARRY_PERM:P70; NorthCarolina4:Combined:CARRY_PERM:P70; Connecticut4:Combined:CLAMP_4:P25; NewJersey4:Midday:CLAMP_4:P25; SouthCarolina4:Evening:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-10/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-10/control_center/profit_alerts_eval_merged.csv` (missing)
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
