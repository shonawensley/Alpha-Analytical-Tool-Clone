# Analysis Arena Control Center Daily Run Report — D=2026-03-19 (H=2026-03-18)

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
- Results date `D`: `2026-03-19`
- History date `H`: `2026-03-18`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-03-19/control_center`
- Truth Control Center dir: `sharepacks/2026-03-19/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,113,355` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP4 | Combined:0/5-4/9 | 012,013,015 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`099,001,069` hints=`P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:069:PERSIST,BA | Combined:0/5-3/8 | 127,136,469 | Prog:27|Hidden | tail:93|ev:5|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,224,244` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP3 | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,599,455` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:599:PERM,HP6 | Combined:0/5-4/9 | 015,025,035 | Prog:27|Hidden | tail:4|ev:2|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,001,059` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:009:HOT,CONS | Combined:0/5-1/6 | 037,136,235 | Prog:27|Hidden | tail:09|ev:6|2d:6|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`499,559,023` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A01:049:CONS,3V | Combined:3/8-4/9 | 015,025,035 | Prog:27|Hidden | tail:94|ev:6|2d:6|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`036,066,366` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 013,049,058 | Prog:27|Hidden | tail:66|ev:2|2d:2|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`299,112,117` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:008:PERM,HP2 | Combined:0/5-4/9 | 049,238,247 | Prog:27|Hidden | tail:08|ev:5|2d:5|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=6,OFF=21,WATCH=15`, `top_alert=Delaware4:Combined:3:127 136 469; NewJersey4:Evening:3:058 238 049; NorthCarolina4:Combined:3:049 238 247; NorthCarolina4:Evening:3:238 247 013; Ohio4:Midday:3:589 013 058`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=Ohio4:8:1/6-4/9; NewJersey4:7:3/8-4/9; Indiana4:6:0/5-4/9; Michigan4:4:0/5-1/6; Pennsylvania4:3:0/5-4/9; OntarioCanada4:2:2/7-3/8`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=65`, `top_alerts=Michigan4:Combined:A11:009:BOX; NewJersey4:Evening:A01:049:BOX; Ohio4:Combined:A11:006:BOX; Connecticut4:Combined:A05:224:STR8_3; Delaware4:Combined:A04:069:BOX; Delaware4:Combined:A08:-:OVERLAY; Delaware4:Midday:A05:099:STR8_3; Florida4:Combined:A05:224:STR8_3`
- Profit compound events: `rows=16`, `top_events=Michigan4:Combined:ENGINE_GOV:P85; Ohio4:Combined:ENGINE_GOV:P85; NewJersey4:Evening:CARRY_PERM:P70; NorthCarolina4:Midday:CARRY_PERM:P70; Ohio4:Midday:CARRY_PERM:P70; Pennsylvania4:Evening:CARRY_PERM:P70; SouthCarolina4:Midday:CARRY_PERM:P70; NewYork4:Evening:IDX_ECHO_BASE:P60`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-03-19/control_center/profit_alerts_eval.csv` (missing)
- Eval merged CSV: `sharepacks/2026-03-19/control_center/profit_alerts_eval_merged.csv` (missing)
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
