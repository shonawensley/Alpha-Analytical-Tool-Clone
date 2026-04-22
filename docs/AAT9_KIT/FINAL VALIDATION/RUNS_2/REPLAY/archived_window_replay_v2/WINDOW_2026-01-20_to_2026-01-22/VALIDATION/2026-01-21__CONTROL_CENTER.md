# Analysis Arena Control Center Daily Run Report — D=2026-01-21 (H=2026-01-20)

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
- Results date `D`: `2026-01-21`
- History date `H`: `2026-01-20`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/control_center`
- Truth Control Center dir: `sharepacks/2026-01-21/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,255,355` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:001:PERM,HP4 | Combined:0/5-4/9 | 015,016,025 | Prog:27|Hidden | tail:06|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`255,559,336` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:259:PERSIST,BA | Combined:0/5-4/9 | 059,257,023 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`259,378,008` hints=`P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:008:PERM,HP3 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`001,077,244` hints=`P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:014:CONS,3V | Combined:1/6-2/7 | 014,024,034 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:01|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,477,017` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A01:017:CONS,3V | Combined:1/6-2/7 | 013,017,023 | Prog:27|Hidden | tail:07|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,559,004` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:004:PERM,HP3 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:04|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,337,115` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:337:PERM,HP6 | Combined:0/5-1/6 | 014,023,059 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,006,366` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A11:006:HOT,CONS | Combined:0/5-4/9 | 014,059,068 | Prog:27|Hidden | tail:06|ev:7|2d:7|xvar|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=6,OFF=23,WATCH=13`, `top_alert=Delaware4:Combined:3:059 257 023; Delaware4:Evening:3:027 045 126; Ohio4:Evening:3:015 025 027; Ohio4:Midday:3:013 589 679; OntarioCanada4:Midday:3:127 469 019`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=SouthCarolina4:8:0/5-1/6; Indiana4:7:1/6-2/7; Connecticut4:6:0/5-4/9; Virginia4:6:1/6-4/9; Florida4:5:0/5-4/9; PuertoRico4:4:1/6-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=66`, `top_alerts=NorthCarolina4:Combined:A11:006:BOX; OntarioCanada4:Combined:A11:044:BOX; Connecticut4:Midday:A05:001:STR8_3; Delaware4:Combined:A08:-:OVERLAY; Delaware4:Evening:A04:259:BOX; Delaware4:Evening:A08:-:OVERLAY; Delaware4:Midday:A05:003:STR8_3; Florida4:Combined:A05:008:STR8_3`
- Profit compound events: `rows=9`, `top_events=OntarioCanada4:Combined:STRAIGHT_GATE:P80; Connecticut4:Midday:CARRY_PERM:P70; Florida4:Combined:CARRY_PERM:P70; NorthCarolina4:Evening:CARRY_PERM:P70; Virginia4:Evening:CARRY_PERM:P70; Connecticut4:Evening:CLAMP_4:P25; NewJersey4:Midday:CLAMP_4:P25; NewYork4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-21/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-21/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=80`, `hit_decay=0`, `hit_any_decay=0`
- Merged summary: `rows=53`, `hit_decay=0`, `hit_any_decay=0`, `top_hits=-`

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
