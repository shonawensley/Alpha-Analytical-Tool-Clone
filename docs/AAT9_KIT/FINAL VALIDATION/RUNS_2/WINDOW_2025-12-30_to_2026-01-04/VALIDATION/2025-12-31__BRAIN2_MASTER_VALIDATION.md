# Brain 2 Master Validation Run Report — D=2025-12-31 (H=2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Relationship to the arena-era workflow:
- Board runtime template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Translation sandbox template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## Scope
- Results date (D): `2025-12-31`
- History workbook date (H): `2025-12-30`
- Board scope states (14): `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Full-day tracker scope: `all states represented in the frozen control_center sharepack tables`

## Locked Artifacts
- Board review bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.json`
- Board scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_SCOREBOARD__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_SCOREBOARD__analysis_arena_day_review.json`
- Board spillover overlay: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- Shadow DPL: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__SHADOW_DECISION_POLICY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`
- Translation sandbox day manifest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/ANALYSIS_ARENA/2025-12-31__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json`
- Control Center root: `sharepacks/2025-12-31/control_center`
- Control-arm grade directory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30_to_2026-01-04__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30_to_2026-01-04__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

## Quick Auto-Captured Anchors
- Top scoreboard rows: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011, 559, 003`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244, 144, 499`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677, 116, 077`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677, 244, 668`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`136, 244, 599`
- Board verdict top_primary_target: `Connecticut4`
- Board verdict secondary_target: `Delaware4`
- Board verdict best_clean_host: `Connecticut4`
- Board verdict highest_context_support_state: `Connecticut4`
- Shadow DPL play states: _none_
- Shadow DPL watch states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Daily doubles / mirror doubles detected: ``SouthCarolina4` `Evening` winner=`044` type=`double` rank=`13` DS=`8` mirror_pairs=`-``, ``Michigan4` `Midday` winner=`583` type=`mirror_double` rank=`5` DS=`6` mirror_pairs=`3/8``, ``Michigan4` `Evening` winner=`477` type=`double` rank=`5` DS=`6` mirror_pairs=`-``, ``Delaware4` `Evening` winner=`337` type=`double` rank=`2` DS=`4` mirror_pairs=`-``, ``NewYork4` `Midday` winner=`419` type=`mirror_double` rank=`7` DS=`4` mirror_pairs=`4/9``, ``NewYork4` `Evening` winner=`116` type=`double` rank=`7` DS=`4` mirror_pairs=`1/6``, ``Pennsylvania4` `Evening` winner=`221` type=`double` rank=`11` DS=`4` mirror_pairs=`-``, ``Connecticut4` `Evening` winner=`361` type=`mirror_double` rank=`1` DS=`2` mirror_pairs=`1/6``, ``NewJersey4` `Midday` winner=`366` type=`double` rank=`6` DS=`2` mirror_pairs=`-``, ``Florida4` `Evening` winner=`211` type=`double` rank=`3` DS=`1` mirror_pairs=`-``, ``NorthCarolina4` `Evening` winner=`057` type=`mirror_double` rank=`8` DS=`1` mirror_pairs=`0/5``, ``Virginia4` `Midday` winner=`686` type=`double` rank=`14` DS=`0` mirror_pairs=`-``, ``Virginia4` `Evening` winner=`636` type=`double` rank=`14` DS=`0` mirror_pairs=`-``

---

## Part A — File Lock And Scope

Auto-captured anchors:
- board scope states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- full-day tracker artifacts: `sharepacks/2025-12-31/control_center/profit_alerts.csv`, `sharepacks/2025-12-31/control_center/profit_compound_events.csv`, `sharepacks/2025-12-31/control_center/blackapple_alerts.csv`, `sharepacks/2025-12-31/control_center/due_doubles.csv`, `sharepacks/2025-12-31/control_center/vtrac_repeat_watch.csv`
- sharepack remains the frozen raw day snapshot; board artifacts are derived arena-era receipts on top of it

Analyst conclusion:
- board scope notes: `...`
- full-day tracker scope notes: `...`
- missing artifact notes: `...`

## Part B — Board Outcome Map

Auto-captured anchors:
- top scoreboard anchors: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011, 559, 003`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244, 144, 499`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677, 116, 077`
- daily doubles / mirror doubles on the day: ``SouthCarolina4` `Evening` winner=`044` type=`double` rank=`13` DS=`8` mirror_pairs=`-``, ``Michigan4` `Midday` winner=`583` type=`mirror_double` rank=`5` DS=`6` mirror_pairs=`3/8``, ``Michigan4` `Evening` winner=`477` type=`double` rank=`5` DS=`6` mirror_pairs=`-``, ``Delaware4` `Evening` winner=`337` type=`double` rank=`2` DS=`4` mirror_pairs=`-``, ``NewYork4` `Midday` winner=`419` type=`mirror_double` rank=`7` DS=`4` mirror_pairs=`4/9``, ``NewYork4` `Evening` winner=`116` type=`double` rank=`7` DS=`4` mirror_pairs=`1/6``, ``Pennsylvania4` `Evening` winner=`221` type=`double` rank=`11` DS=`4` mirror_pairs=`-``, ``Connecticut4` `Evening` winner=`361` type=`mirror_double` rank=`1` DS=`2` mirror_pairs=`1/6``, ``NewJersey4` `Midday` winner=`366` type=`double` rank=`6` DS=`2` mirror_pairs=`-``, ``Florida4` `Evening` winner=`211` type=`double` rank=`3` DS=`1` mirror_pairs=`-``, ``NorthCarolina4` `Evening` winner=`057` type=`mirror_double` rank=`8` DS=`1` mirror_pairs=`0/5``, ``Virginia4` `Midday` winner=`686` type=`double` rank=`14` DS=`0` mirror_pairs=`-``, ``Virginia4` `Evening` winner=`636` type=`double` rank=`14` DS=`0` mirror_pairs=`-``
- direct cross-state receipts surfaced by board verdict: _none_

Analyst conclusion:
- actual strongest day states: `...`
- states that converted meaningful structure: `...`
- states that were mostly echo / ambient only: `...`
- day-level structural class: `...`
- most important truth-side board insight: `...`

## Part C — Scoreboard And Ranking Evaluation

Auto-captured anchors:
- top scoreboard rows that mattered: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011, 559, 003`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244, 144, 499`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677, 116, 077`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677, 244, 668`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`136, 244, 599`
- top_primary_target=`Connecticut4` secondary_target=`Delaware4`
- best_clean_host=`Connecticut4` highest_context_support_state=`Connecticut4`
- tight_core_states=-
- watch_only_states=-
- small_shoulder_states=`Connecticut4`, `Delaware4`, `Florida4`

Analyst conclusion:
- highest-converting actual state rank(s): `...`
- bucket quality notes: `...`
- did the scoreboard ranking help or distort the day?: `...`
- most important scoreboard lesson: `...`

## Part D — Shared Complexes, Carryover, And Spillover

Auto-captured anchors:
- strongest overlap pairs: `Indiana4` + `NewYork4` score=`39` types=`alert_implied_echo,shared_box_family,shared_lane`; `Connecticut4` + `SouthCarolina4` score=`36` types=`alert_implied_echo,shared_box_family,shared_lane`; `Indiana4` + `SouthCarolina4` score=`34` types=`alert_implied_echo,shared_box_family,shared_lane`; `Delaware4` + `Indiana4` score=`33` types=`alert_implied_echo,shared_box_family,shared_lane`; `Pennsylvania4` + `Virginia4` score=`33` types=`alert_implied_echo,shared_box_family,shared_lane`
- direct cross-state receipts: _none_
- best relationship source: `-`

Analyst conclusion:
- most important shared complexes: `...`
- most important host state: `...`
- most important echo state: `...`
- most important cross-state carryover receipt: `...`
- did the board correctly treat the day as a shared pending complex?: `...`
- most important spillover lesson: `...`

## Part E — Aggregate Tracker Inventory

Auto-captured anchors:
- highest-value alert states: `Connecticut4` alerts=`8` strength_sum=`31.0` ids=`A01,A02,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `OntarioCanada4` alerts=`7` strength_sum=`23.0` ids=`A02,A04,A05,A08` suggested=`BOX,OVERLAY,STR8_3`; `Ohio4` alerts=`6` strength_sum=`23.0` ids=`A01,A02,A04,A05,A08` suggested=`BOX,OVERLAY,STR8_3`; `PuertoRico4` alerts=`6` strength_sum=`23.0` ids=`A02,A04,A05,A10,A11,A12` suggested=`BOX,STR8_3,STR8_4of8`; `Michigan4` alerts=`6` strength_sum=`20.0` ids=`A01,A04,A05,A08,A10,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`
- compound-event leaders: `Connecticut4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A04,A11`; `NewJersey4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A02,A04,A05`; `NewYork4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A01,A04,A05`; `NorthCarolina4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `Ohio4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A02,A04,A05`; `SouthCarolina4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05,A09,A12`
- Blackapple ALERT states: `Connecticut4` `Midday` BA=`3` examples=`138 237 489`; `NorthCarolina4` `Evening` BA=`3` examples=`034 124 016`; `Ohio4` `Midday` BA=`3` examples=`035 278 026`; `OntarioCanada4` `Combined` BA=`3` examples=`127 136 019`
- due-double threshold states (DS>=3): `PuertoRico4` DS=`10`; `SouthCarolina4` DS=`8`; `Michigan4` DS=`6`; `Delaware4` DS=`4`; `NewYork4` DS=`4`; `Pennsylvania4` DS=`4`; `OntarioCanada4` DS=`3`
- repeat-watch exact hits: `PuertoRico4` `Evening` idx=`24`

Analyst conclusion:
- most important board-scope tracker states: `...`
- most important full-day tracker states outside the board: `...`
- did tracker posture materially explain the day?: `...`
- most important aggregate-tracker insight: `...`

## Part F — Profit Alerts And Special Compound Events

Auto-captured anchors:
- highest-value alert states: `Connecticut4` alerts=`8` strength_sum=`31.0` ids=`A01,A02,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `OntarioCanada4` alerts=`7` strength_sum=`23.0` ids=`A02,A04,A05,A08` suggested=`BOX,OVERLAY,STR8_3`; `Ohio4` alerts=`6` strength_sum=`23.0` ids=`A01,A02,A04,A05,A08` suggested=`BOX,OVERLAY,STR8_3`; `PuertoRico4` alerts=`6` strength_sum=`23.0` ids=`A02,A04,A05,A10,A11,A12` suggested=`BOX,STR8_3,STR8_4of8`; `Michigan4` alerts=`6` strength_sum=`20.0` ids=`A01,A04,A05,A08,A10,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`
- top compound-event rows: `Connecticut4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A04,A11`; `NewJersey4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A02,A04,A05`; `NewYork4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A01,A04,A05`; `NorthCarolina4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `Ohio4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A02,A04,A05`; `SouthCarolina4` `Midday` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05,A09,A12`
- profit alerts source: `sharepacks/2025-12-31/control_center/profit_alerts.csv`
- compound events source: `sharepacks/2025-12-31/control_center/profit_compound_events.csv`

Analyst conclusion:
- most important alert IDs: `...`
- implied-set conversions: `...`
- most important special compound events: `...`
- alert-rich but structurally weak states: `...`
- did profit alerts / compound events materially improve Brain 2?: `...`
- most important alert-layer lesson: `...`

## Part G — Blackapple Board Review

Auto-captured anchors:
- BA ALERT states: `Connecticut4` `Midday` BA=`3` examples=`138 237 489`; `NorthCarolina4` `Evening` BA=`3` examples=`034 124 016`; `Ohio4` `Midday` BA=`3` examples=`035 278 026`; `OntarioCanada4` `Combined` BA=`3` examples=`127 136 019`
- BA WATCH states: `Florida4` `Combined` BA=`2` examples=`014 059 068`; `Indiana4` `Combined` BA=`2` examples=`037 127 136`; `Michigan4` `Evening` BA=`2` examples=`036 045 135`; `NewYork4` `Evening` BA=`2` examples=`016 079 169`; `NorthCarolina4` `Combined` BA=`2` examples=`012 013 014`; `Ohio4` `Combined` BA=`2` examples=`015 016 025`; `OntarioCanada4` `Evening` BA=`2` examples=`015 016 038`; `OntarioCanada4` `Midday` BA=`2` examples=`015 025 027`
- Blackapple source: `sharepacks/2025-12-31/control_center/blackapple_alerts.csv`

Analyst conclusion:
- important BA recommendation carries: `...`
- states where BA looked stronger than the board gave credit for: `...`
- did BA function mainly as host indicator / echo amplifier / shortlist helper / noise / mixed?: `...`
- most important BA lesson: `...`

## Part H — Due Doubles Ranked-State Evaluation

Auto-captured anchors:
- ranked due states reviewed (DS>=3): `PuertoRico4` DS=`10`; `SouthCarolina4` DS=`8`; `Michigan4` DS=`6`; `Delaware4` DS=`4`; `NewYork4` DS=`4`; `Pennsylvania4` DS=`4`; `OntarioCanada4` DS=`3`
- top due states that converted in-family: `Delaware4` DS=`4` midday_in_family=`False` evening_in_family=`True`
- due doubles source: `sharepacks/2025-12-31/control_center/due_doubles.csv`

Analyst conclusion:
- top due states that failed: `...`
- threshold states (3 draws missing) that converted: `...`
- important due families / examples that converted: `...`
- conversion class notes: `...`
- most important due-doubles ranking lesson: `...`

## Part I — All Daily Doubles And Mirror Doubles Evidence Audit

Auto-captured anchors:
- daily doubles / mirror doubles reviewed: `SouthCarolina4` `Evening` winner=`044` type=`double` rank=`13` DS=`8` mirror_pairs=`-`; `Michigan4` `Midday` winner=`583` type=`mirror_double` rank=`5` DS=`6` mirror_pairs=`3/8`; `Michigan4` `Evening` winner=`477` type=`double` rank=`5` DS=`6` mirror_pairs=`-`; `Delaware4` `Evening` winner=`337` type=`double` rank=`2` DS=`4` mirror_pairs=`-`; `NewYork4` `Midday` winner=`419` type=`mirror_double` rank=`7` DS=`4` mirror_pairs=`4/9`; `NewYork4` `Evening` winner=`116` type=`double` rank=`7` DS=`4` mirror_pairs=`1/6`; `Pennsylvania4` `Evening` winner=`221` type=`double` rank=`11` DS=`4` mirror_pairs=`-`; `Connecticut4` `Evening` winner=`361` type=`mirror_double` rank=`1` DS=`2` mirror_pairs=`1/6`; `NewJersey4` `Midday` winner=`366` type=`double` rank=`6` DS=`2` mirror_pairs=`-`; `Florida4` `Evening` winner=`211` type=`double` rank=`3` DS=`1` mirror_pairs=`-`; `NorthCarolina4` `Evening` winner=`057` type=`mirror_double` rank=`8` DS=`1` mirror_pairs=`0/5`; `Virginia4` `Midday` winner=`686` type=`double` rank=`14` DS=`0` mirror_pairs=`-`; `Virginia4` `Evening` winner=`636` type=`double` rank=`14` DS=`0` mirror_pairs=`-`
- support sources: due-doubles=`sharepacks/2025-12-31/control_center/due_doubles.csv` BA=`sharepacks/2025-12-31/control_center/blackapple_alerts.csv` alerts=`sharepacks/2025-12-31/control_center/profit_alerts.csv`
- window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30_to_2026-01-04__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30_to_2026-01-04__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

Analyst conclusion:
- most important strong-evidence double: `...`
- most important weak-evidence double: `...`
- most important doubles / mirror-doubles lesson: `...`

## Part J — Shadow DPL And Board Posture Evaluation

Auto-captured anchors:
- play states: _none_
- watch states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- skip states: _none_
- top useful reason codes: `HOST_STATE` x14; `DOUBLE_HEAVY` x14; `CTX_REINFORCED` x14; `VTRAC_ALIGNED` x14; `SURVIVOR_PRESSURE` x14; `SURVIVOR_PROGRESSION` x14; `HIDDEN_TERMINAL_SUPPORT` x14; `PROFIT_ALERT` x14
- top_play_state=`-` top_watch_state=`Connecticut4`

Analyst conclusion:
- watch states that should maybe have been play: `...`
- play states that were overpromoted: `...`
- mode / cap quality: `...`
- most important misleading reason codes: `...`
- most important DPL lesson: `...`

## Part K — Translation Sandbox / Combination Learning Capture

Auto-captured anchors:
- strongest boxed themes: `011` x9; `017` x9; `006` x8; `007` x7; `009` x6; `005` x6
- strongest straight themes: `900` x4; `090` x4; `040` x4; `011` x3; `009` x3; `004` x3
- strongest VT-box themes: `23` x13; `18` x12; `12` x10; `15` x9; `6` x7; `9` x7
- repeated positional shortlist carries: `113` x3; `067` x3; `688` x3; `137` x3; `007` x2; `009` x2
- repeated Blackapple carries: `014` x6; `017` x6; `018` x5; `028` x5; `016` x5; `019` x5
- profit-alert implied carries: `368` x2; `016` x2; `244` x2; `077` x2; `226` x2; `267` x2
- due-double carries: `556` x4; `044` x3; `445` x3; `559` x3; `223` x3; `778` x3
- preserved-not-budgeted canonicals: `067` x2; `016` x1; `078` x1; `026` x1; `056` x1; `267` x1

Analyst conclusion:
- most important preserved-not-budgeted cluster: `...`
- strongest translator-learning note: `...`

## Part L — Control-Arm Comparison

Auto-captured anchors:
- candidate-universe grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md`
- play-card grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__PLAY_CARD_GRADE__tool_only__arena_v0.md`
- B12/B24/B36 remain the baseline/control-arm comparison surface, not the arena branch truth

Analyst conclusion:
- most important control-arm success: `...`
- most important control-arm suppression: `...`
- did the control arm outperform, underperform, or mostly lag Brain 2 truth?: `...`
- most important control-arm lesson: `...`

## Part M — Final Board Lessons And Promotions

Auto-captured anchors:
- top board runtime artifacts locked above; use this section to end with board-level lessons rather than state-by-state repetition

Analyst conclusion:
- strongest board-level insight: `...`
- strongest tracker insight: `...`
- strongest cross-state carryover insight: `...`
- strongest doubles / mirror-doubles insight: `...`
- strongest translation-learning insight: `...`
- one thing that deserves later promotion: `...`
- one thing that should remain research-only for now: `...`
- one structural follow-up target: `...`
- one thing to watch on the next fresh runs: `...`
