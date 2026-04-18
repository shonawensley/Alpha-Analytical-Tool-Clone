# Analysis Arena Control Center Daily Run Report — D=2026-01-06 (H=2026-01-05)

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
- Results date `D`: `2026-01-06`
- History date `H`: `2026-01-05`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive Control Center dir: `sharepacks/_predictive/2026-01-06/control_center`
- Truth Control Center dir: `sharepacks/2026-01-06/control_center`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## 1) Brain 2 Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,244,468` hints=`P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:224:PERM,HP7 | Combined:0/5-4/9 | 012,014,023 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,003,118` hints=`P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A04:348:PERSIST,BA | Combined:2/7-3/8 | 016,169,349 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,033,346` hints=`P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)) | A05:033:PERM,HP7 | Combined:3/8-4/9 | 059,257,023 | Prog:27|Hidden | tail:33|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,366,066` hints=`P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:244:PERM,HP6 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`118,144,668` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:344:PERM,HP2 | Combined:1/6-2/7 | 058,238,013 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,088,788` hints=`P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:778:PERM,HP7 | Combined:3/8-4/9 | 038,058,138 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`008,005,025` hints=`P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)) | A05:005:PERM,HP7 | Combined:0/5-1/6 | 016,025,124 | Prog:27|Hidden | tail:11|ev:6|2d:6|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,229,299` hints=`P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)) | A05:044:PERM,HP7 | Combined:0/5-4/9 | 018,027,036 | Prog:27|Hidden | tail:44|ev:2|2d:2|trial|strong`

## 2) Core Control Center Boards

- Blackapple: `rows=42`, `status_counts=ALERT=7,OFF=24,WATCH=11`, `top_alert=Delaware4:Combined:3:016 169 349; Florida4:Combined:3:059 257 023; Michigan4:Combined:3:058 238 013; Ohio4:Midday:3:012 013 014; PuertoRico4:Combined:3:059 149 167`
- Due doubles: `rows=42`, `combined_rows=14`, `top_combined=NewJersey4:6:3/8-4/9; PuertoRico4:5:1/6-4/9; Delaware4:4:2/7-3/8; Indiana4:4:1/6-2/7; NewYork4:1:0/5-1/6; NorthCarolina4:1:0/5-4/9`
- VTRAC repeat watch: `rows=42`, `current_equals_winner_vtrac=0`, `hit_rows=-`
- Profit alerts: `rows=58`, `top_alerts=SouthCarolina4:Midday:A01:078:BOX; Virginia4:Combined:A11:009:BOX; Connecticut4:Combined:A05:224:STR8_3; Delaware4:Combined:A04:348:BOX; Delaware4:Combined:A08:-:OVERLAY; Delaware4:Midday:A05:003:STR8_3; Florida4:Combined:A05:033:STR8_3; Florida4:Combined:A08:-:OVERLAY`
- Profit compound events: `rows=8`, `top_events=Virginia4:Combined:ENGINE_GOV:P85; Pennsylvania4:Midday:CARRY_PERM:P70; Florida4:Combined:CLAMP_4:P25; NewYork4:Evening:CLAMP_4:P25; Ohio4:Evening:CLAMP_4:P25; Pennsylvania4:Evening:CLAMP_4:P25; PuertoRico4:Midday:CLAMP_4:P25; SouthCarolina4:Combined:CLAMP_4:P25`

## 3) Post-Results Profit Alert Evaluation

- Eval CSV: `sharepacks/2026-01-06/control_center/profit_alerts_eval.csv`
- Eval merged CSV: `sharepacks/2026-01-06/control_center/profit_alerts_eval_merged.csv`
- Eval summary: `rows=72`, `hit_decay=0`, `hit_any_decay=0`
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
