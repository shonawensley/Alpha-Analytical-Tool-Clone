# Analysis Arena Control Center Daily Run Report — D=2026-01-16 (H=2026-01-15)

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
- Results date `D`: `2026-01-16`
- History date `H`: `2026-01-15`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive Control Center dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/control_center`
- Truth Control Center dir: `sharepacks/2026-01-16/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`899,599,389` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:899:PERM,HP5 | Combined:0/5-4/9 | 035,038,058 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009,249,059` hints=`P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:599:PERM,HP5 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225,577,255` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:223:PERM,HP4 | Combined:3/8-4/9 | 012,015,018 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368,599,366` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A04:368:PERSIST,BA | Combined:1/6-2/7 | 015,024,123 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,245,559` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:011:PERM,HP3 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:01|ev:2|2d:2|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,008,019` hints=`P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:788:PERM,HP3 | Combined:3/8-4/9 | 578,038,128 | Prog:27|Hidden | tail:01|ev:2|2d:2|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`337,377,334` hints=`P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A09::VTRAC,REP | Combined:0/5-1/6 | 023,167,239 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,344,255` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP4 | Combined:0/5-4/9 | 038,047,137 | Prog:27|Hidden | tail:00|ev:3|2d:3|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=3,OFF=19,WATCH=20`, `top_alert=Indiana4:Combined:3:015 024 123; Michigan4:Midday:3:049 058 238; Pennsylvania4:Midday:3:049 058 247`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=OntarioCanada4:10:0/5-4/9; NewYork4:5:0/5-1/6; NorthCarolina4:5:0/5-4/9; Connecticut4:3:0/5-4/9; Virginia4:3:1/6-4/9; Ohio4:2:0/5-1/6`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=63`, `top_alerts=OntarioCanada4:Combined:A11:003:BOX; Connecticut4:Midday:A05:899:STR8_3; Delaware4:Evening:A05:599:STR8_3; Florida4:Evening:A05:223:STR8_3; Indiana4:Combined:A04:368:BOX; Indiana4:Combined:A05:339:STR8_3; Indiana4:Combined:A08:-:OVERLAY; Michigan4:Evening:A05:011:STR8_3`
- Profit compound events: `rows=12`, `top_events=OntarioCanada4:Combined:ENGINE_GOV:P85; Delaware4:Evening:CARRY_PERM:P70; Florida4:Evening:CARRY_PERM:P70; Indiana4:Combined:CARRY_PERM:P70; NewYork4:Evening:CARRY_PERM:P70; SouthCarolina4:Combined:CARRY_PERM:P70; PuertoRico4:Combined:IDX_ECHO_BASE:P60; Virginia4:Evening:DBL_BA:P45`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-16/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-16/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=75`, `hit_decay=2`, `hit_any_decay=2`
- Merged summary: `rows=48`, `hit_decay=2`, `hit_any_decay=2`, `top_hits=Indiana4:Combined:A04:A08; OntarioCanada4:Combined:A01:A08`

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
