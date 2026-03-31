# Analysis Arena Control Center Daily Run Report — D=2026-01-20 (H=2026-01-19)

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
- Results date `D`: `2026-01-20`
- History date `H`: `2026-01-19`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-01-20/control_center`
- Truth Control Center dir: `sharepacks/2026-01-20/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`006,005,255` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:355:PERM,HP3 | Combined:0/5-4/9 | 038,056,029 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`559,259,007` hints=`P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:259:PERSIST,BA | Combined:0/5-4/9 | 059,257,023 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`378,255,259` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:778:PERM,HP4 | Combined:0/5-4/9 | 017,027,037 | Prog:27|Hidden | tail:07|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`077,224,007` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:007:HOT,CONS | Combined:1/6-2/7 | 012,023,024 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,778,007` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP7 | Combined:1/6-2/7 | 016,017,026 | Prog:27|Hidden | tail:07|ev:5|2d:5|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,559,004` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A11:001:HOT,CONS | Combined:3/8-4/9 | 047,056,128 | Prog:27|Hidden | tail:04|ev:9|2d:9|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`378,377,113` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 014,023,149 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,244,368` hints=`P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:244:PERM,HP6 | Combined:0/5-4/9 | 014,068,149 | Prog:27|Hidden | tail:04|ev:6|2d:6|xvar|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=5,OFF=18,WATCH=19`, `top_alert=Connecticut4:Combined:3:038 056 029; Delaware4:Combined:3:059 257 023; Delaware4:Evening:3:027 045 126; Ohio4:Evening:3:027 038 057; SouthCarolina4:Combined:3:015 348 024`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=SouthCarolina4:6:0/5-1/6; Indiana4:5:1/6-2/7; Connecticut4:4:0/5-4/9; Ohio4:4:0/5-1/6; Virginia4:4:1/6-4/9; Florida4:3:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=68`, `top_alerts=Indiana4:Combined:A11:007:BOX; NewJersey4:Combined:A11:001:BOX; Pennsylvania4:Combined:A11:000:BOX; Connecticut4:Combined:A08:-:OVERLAY; Connecticut4:Evening:A05:355:STR8_3; Delaware4:Combined:A08:-:OVERLAY; Delaware4:Evening:A04:259:BOX; Delaware4:Evening:A08:-:OVERLAY`
- Profit compound events: `rows=10`, `top_events=Indiana4:Combined:ENGINE_GOV:P85; NewJersey4:Evening:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; Ohio4:Combined:CARRY_PERM:P70; Pennsylvania4:Midday:CARRY_PERM:P70; PuertoRico4:Evening:CARRY_PERM:P70; NewJersey4:Combined:DBL_BA:P45; Virginia4:Evening:DBL_BA:P45`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-20/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-20/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=89`, `hit_decay=1`, `hit_any_decay=1`
- Merged summary: `rows=58`, `hit_decay=1`, `hit_any_decay=1`, `top_hits=Virginia4:Midday:A01:A08`

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
