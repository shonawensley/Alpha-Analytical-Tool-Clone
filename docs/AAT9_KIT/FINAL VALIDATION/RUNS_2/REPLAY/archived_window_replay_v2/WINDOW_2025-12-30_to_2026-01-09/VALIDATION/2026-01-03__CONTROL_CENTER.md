# Analysis Arena Control Center Daily Run Report — D=2026-01-03 (H=2026-01-02)

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
- Results date `D`: `2026-01-03`
- History date `H`: `2026-01-02`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-03/control_center`
- Truth Control Center dir: `sharepacks/2026-01-03/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`048,478,368` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:006:PERM,HP2 | Combined:0/5-4/9 | 014,024,034 | Prog:27|Hidden | tail:01|ev:5|2d:5|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,004,599` hints=`P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:004:HOT,CONS | Combined:2/7-3/8 | 015,018,025 | Prog:27|Hidden | tail:04|ev:15|2d:14|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`138,599,559` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:559:PERM,HP3 | Combined:0/5-3/8 | 014,023,059 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,368,668` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:1/6-2/7 | 019,028,046 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,668,016` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A11:006:HOT,CONS | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`299,599,899` hints=`P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:3/8-4/9 | 012,019,023 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`788,889,038` hints=`P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:889:PERM,HP7 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`229,224,299` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:044:PERM,HP6 | Combined:0/5-4/9 | 025,027,049 | Prog:27|Hidden | tail:04|ev:5|2d:5|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=2,OFF=30,WATCH=10`, `top_alert=NorthCarolina4:Evening:4:025 034 124; SouthCarolina4:Midday:3:035 134 278`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=OntarioCanada4:9:0/5-4/9; Delaware4:4:2/7-3/8; Florida4:4:0/5-3/8; Michigan4:4:1/6-2/7; SouthCarolina4:4:0/5-1/6; Virginia4:4:1/6-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=59`, `top_alerts=Delaware4:Combined:A11:004:BOX; Michigan4:Combined:A11:006:BOX; SouthCarolina4:Combined:A11:002:BOX; Connecticut4:Midday:A05:006:STR8_3; Delaware4:Combined:A01:045:BOX; Delaware4:Evening:A05:449:STR8_3; Delaware4:Midday:A01:014:BOX; Delaware4:Midday:A01:014:BOX`
- Profit compound events: `rows=7`, `top_events=Delaware4:Combined:ENGINE_GOV:P85; Michigan4:Combined:ENGINE_GOV:P85; Ohio4:Combined:CARRY_PERM:P70; Connecticut4:Combined:CLAMP_4:P25; Michigan4:Midday:CLAMP_4:P25; Pennsylvania4:Combined:CLAMP_4:P25; SouthCarolina4:Midday:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-03/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-03/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=66`, `hit_decay=1`, `hit_any_decay=1`
- Merged summary: `rows=49`, `hit_decay=1`, `hit_any_decay=1`, `top_hits=SouthCarolina4:Evening:A04:`

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
