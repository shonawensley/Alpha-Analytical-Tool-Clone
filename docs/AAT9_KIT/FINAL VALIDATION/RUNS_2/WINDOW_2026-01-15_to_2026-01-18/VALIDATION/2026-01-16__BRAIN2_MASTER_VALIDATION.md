# Brain 2 Master Validation Run Report — D=2026-01-16 (H=2026-01-15)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Relationship to the arena-era workflow:
- Board runtime template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Translation sandbox template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## Scope
- Results date (D): `2026-01-16`
- History workbook date (H): `2026-01-15`
- Board scope states (14): `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Full-day tracker scope: `all states represented in the frozen control_center sharepack tables`

## Locked Artifacts
- Board review bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.json`
- Board scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_SCOREBOARD__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_SCOREBOARD__analysis_arena_day_review.json`
- Board spillover overlay: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- Shadow DPL: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__SHADOW_DECISION_POLICY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`
- Translation sandbox day manifest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/ANALYSIS_ARENA/2026-01-16__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json`
- Control Center root: `sharepacks/2026-01-16/control_center`
- Control-arm grade directory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15_to_2026-01-18__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15_to_2026-01-18__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

## Quick Auto-Captured Anchors
- Top scoreboard rows: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`899, 599, 389`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009, 249, 059`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225, 577, 255`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368, 599, 366`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344, 245, 559`
- Board verdict top_primary_target: `Connecticut4`
- Board verdict secondary_target: `Delaware4`
- Board verdict best_clean_host: `Connecticut4`
- Board verdict highest_context_support_state: `Pennsylvania4`
- Shadow DPL play states: _none_
- Shadow DPL watch states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Daily doubles / mirror doubles detected: ``OntarioCanada4` `Midday` winner=`998` type=`double` rank=`10` DS=`10` mirror_pairs=`-``, ``NewYork4` `Evening` winner=`496` type=`mirror_double` rank=`7` DS=`5` mirror_pairs=`4/9``, ``NorthCarolina4` `Midday` winner=`169` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`1/6``, ``NorthCarolina4` `Evening` winner=`083` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`3/8``, ``Virginia4` `Evening` winner=`627` type=`mirror_double` rank=`14` DS=`3` mirror_pairs=`2/7``, ``Ohio4` `Midday` winner=`585` type=`double` rank=`9` DS=`2` mirror_pairs=`-``, ``Ohio4` `Evening` winner=`646` type=`double` rank=`9` DS=`2` mirror_pairs=`-``, ``Pennsylvania4` `Evening` winner=`439` type=`mirror_double` rank=`11` DS=`2` mirror_pairs=`4/9``, ``PuertoRico4` `Midday` winner=`729` type=`mirror_double` rank=`12` DS=`2` mirror_pairs=`2/7``, ``PuertoRico4` `Evening` winner=`222` type=`triple` rank=`12` DS=`2` mirror_pairs=`-``, ``Florida4` `Midday` winner=`273` type=`mirror_double` rank=`3` DS=`1` mirror_pairs=`2/7``, ``Florida4` `Evening` winner=`100` type=`double` rank=`3` DS=`1` mirror_pairs=`-``, ``Indiana4` `Midday` winner=`954` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`4/9``, ``Indiana4` `Evening` winner=`836` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`3/8``, ``Michigan4` `Midday` winner=`946` type=`mirror_double` rank=`5` DS=`0` mirror_pairs=`4/9``, ``Michigan4` `Evening` winner=`633` type=`double` rank=`5` DS=`0` mirror_pairs=`-``, ``NewJersey4` `Midday` winner=`877` type=`double` rank=`6` DS=`0` mirror_pairs=`-``, ``SouthCarolina4` `Midday` winner=`884` type=`double` rank=`13` DS=`0` mirror_pairs=`-``

---

## Part A — File Lock And Scope

Auto-captured anchors:
- board scope states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- full-day tracker artifacts: `sharepacks/2026-01-16/control_center/profit_alerts.csv`, `sharepacks/2026-01-16/control_center/profit_compound_events.csv`, `sharepacks/2026-01-16/control_center/blackapple_alerts.csv`, `sharepacks/2026-01-16/control_center/due_doubles.csv`, `sharepacks/2026-01-16/control_center/vtrac_repeat_watch.csv`
- sharepack remains the frozen raw day snapshot; board artifacts are derived arena-era receipts on top of it

Analyst conclusion:
- board scope notes: `...`
- full-day tracker scope notes: `...`
- missing artifact notes: `...`

## Part B — Board Outcome Map

Auto-captured anchors:
- top scoreboard anchors: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`899, 599, 389`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009, 249, 059`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225, 577, 255`
- daily doubles / mirror doubles on the day: ``OntarioCanada4` `Midday` winner=`998` type=`double` rank=`10` DS=`10` mirror_pairs=`-``, ``NewYork4` `Evening` winner=`496` type=`mirror_double` rank=`7` DS=`5` mirror_pairs=`4/9``, ``NorthCarolina4` `Midday` winner=`169` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`1/6``, ``NorthCarolina4` `Evening` winner=`083` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`3/8``, ``Virginia4` `Evening` winner=`627` type=`mirror_double` rank=`14` DS=`3` mirror_pairs=`2/7``, ``Ohio4` `Midday` winner=`585` type=`double` rank=`9` DS=`2` mirror_pairs=`-``, ``Ohio4` `Evening` winner=`646` type=`double` rank=`9` DS=`2` mirror_pairs=`-``, ``Pennsylvania4` `Evening` winner=`439` type=`mirror_double` rank=`11` DS=`2` mirror_pairs=`4/9``, ``PuertoRico4` `Midday` winner=`729` type=`mirror_double` rank=`12` DS=`2` mirror_pairs=`2/7``, ``PuertoRico4` `Evening` winner=`222` type=`triple` rank=`12` DS=`2` mirror_pairs=`-``, ``Florida4` `Midday` winner=`273` type=`mirror_double` rank=`3` DS=`1` mirror_pairs=`2/7``, ``Florida4` `Evening` winner=`100` type=`double` rank=`3` DS=`1` mirror_pairs=`-``, ``Indiana4` `Midday` winner=`954` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`4/9``, ``Indiana4` `Evening` winner=`836` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`3/8``, ``Michigan4` `Midday` winner=`946` type=`mirror_double` rank=`5` DS=`0` mirror_pairs=`4/9``, ``Michigan4` `Evening` winner=`633` type=`double` rank=`5` DS=`0` mirror_pairs=`-``, ``NewJersey4` `Midday` winner=`877` type=`double` rank=`6` DS=`0` mirror_pairs=`-``, ``SouthCarolina4` `Midday` winner=`884` type=`double` rank=`13` DS=`0` mirror_pairs=`-``
- direct cross-state receipts surfaced by board verdict: _none_

Analyst conclusion:
- actual strongest day states: `...`
- states that converted meaningful structure: `...`
- states that were mostly echo / ambient only: `...`
- day-level structural class: `...`
- most important truth-side board insight: `...`

## Part C — Scoreboard And Ranking Evaluation

Auto-captured anchors:
- top scoreboard rows that mattered: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`899, 599, 389`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009, 249, 059`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225, 577, 255`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368, 599, 366`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344, 245, 559`
- top_primary_target=`Connecticut4` secondary_target=`Delaware4`
- best_clean_host=`Connecticut4` highest_context_support_state=`Pennsylvania4`
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
- strongest overlap pairs: `Delaware4` + `Virginia4` score=`34` types=`alert_implied_echo,shared_box_family,shared_lane`; `Indiana4` + `NewYork4` score=`34` types=`alert_implied_echo,shared_box_family,shared_lane`; `NewYork4` + `SouthCarolina4` score=`34` types=`alert_implied_echo,shared_box_family,shared_lane`; `Delaware4` + `NewYork4` score=`33` types=`alert_implied_echo,shared_box_family,shared_lane`; `NewYork4` + `PuertoRico4` score=`33` types=`alert_implied_echo,shared_box_family,shared_lane`
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
- highest-value alert states: `OntarioCanada4` alerts=`8` strength_sum=`30.0` ids=`A01,A02,A04,A05,A08,A10,A11` suggested=`BOX,OVERLAY,STR8_3`; `NewJersey4` alerts=`8` strength_sum=`27.0` ids=`A01,A03,A04,A05,A08,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Pennsylvania4` alerts=`7` strength_sum=`25.0` ids=`A02,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Virginia4` alerts=`7` strength_sum=`22.0` ids=`A02,A04,A05,A08,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `NewYork4` alerts=`6` strength_sum=`21.0` ids=`A01,A04,A05,A08,A09,A10` suggested=`BOX,OVERLAY,STR8_3,STR8_8`
- compound-event leaders: _none_
- Blackapple ALERT states: `Indiana4` `Combined` BA=`3` examples=`015 024 123`; `Michigan4` `Midday` BA=`3` examples=`049 058 238`; `Pennsylvania4` `Midday` BA=`3` examples=`049 058 247`
- due-double threshold states (DS>=3): `OntarioCanada4` DS=`10`; `NewYork4` DS=`5`; `NorthCarolina4` DS=`5`; `Connecticut4` DS=`3`; `Virginia4` DS=`3`
- repeat-watch exact hits: _none_

Analyst conclusion:
- most important board-scope tracker states: `...`
- most important full-day tracker states outside the board: `...`
- did tracker posture materially explain the day?: `...`
- most important aggregate-tracker insight: `...`

## Part F — Profit Alerts And Special Compound Events

Auto-captured anchors:
- highest-value alert states: `OntarioCanada4` alerts=`8` strength_sum=`30.0` ids=`A01,A02,A04,A05,A08,A10,A11` suggested=`BOX,OVERLAY,STR8_3`; `NewJersey4` alerts=`8` strength_sum=`27.0` ids=`A01,A03,A04,A05,A08,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Pennsylvania4` alerts=`7` strength_sum=`25.0` ids=`A02,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Virginia4` alerts=`7` strength_sum=`22.0` ids=`A02,A04,A05,A08,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `NewYork4` alerts=`6` strength_sum=`21.0` ids=`A01,A04,A05,A08,A09,A10` suggested=`BOX,OVERLAY,STR8_3,STR8_8`
- top compound-event rows: _none_
- profit alerts source: `sharepacks/2026-01-16/control_center/profit_alerts.csv`
- compound events source: `sharepacks/2026-01-16/control_center/profit_compound_events.csv`

Analyst conclusion:
- most important alert IDs: `...`
- implied-set conversions: `...`
- most important special compound events: `...`
- alert-rich but structurally weak states: `...`
- did profit alerts / compound events materially improve Brain 2?: `...`
- most important alert-layer lesson: `...`

## Part G — Blackapple Board Review

Auto-captured anchors:
- BA ALERT states: `Indiana4` `Combined` BA=`3` examples=`015 024 123`; `Michigan4` `Midday` BA=`3` examples=`049 058 238`; `Pennsylvania4` `Midday` BA=`3` examples=`049 058 247`
- BA WATCH states: `Connecticut4` `Combined` BA=`2` examples=`035 038 058`; `Connecticut4` `Evening` BA=`2` examples=`015 025 035`; `Delaware4` `Evening` BA=`2` examples=`018 027 126`; `Florida4` `Evening` BA=`2` examples=`023 059 158`; `Florida4` `Midday` BA=`2` examples=`013 023 034`; `Indiana4` `Evening` BA=`2` examples=`015 016 035`; `NewJersey4` `Combined` BA=`2` examples=`578 038 128`; `NewJersey4` `Midday` BA=`2` examples=`027 045 018`
- Blackapple source: `sharepacks/2026-01-16/control_center/blackapple_alerts.csv`

Analyst conclusion:
- important BA recommendation carries: `...`
- states where BA looked stronger than the board gave credit for: `...`
- did BA function mainly as host indicator / echo amplifier / shortlist helper / noise / mixed?: `...`
- most important BA lesson: `...`

## Part H — Due Doubles Ranked-State Evaluation

Auto-captured anchors:
- ranked due states reviewed (DS>=3): `OntarioCanada4` DS=`10`; `NewYork4` DS=`5`; `NorthCarolina4` DS=`5`; `Connecticut4` DS=`3`; `Virginia4` DS=`3`
- top due states that converted in-family: _none_
- due doubles source: `sharepacks/2026-01-16/control_center/due_doubles.csv`

Analyst conclusion:
- top due states that failed: `...`
- threshold states (3 draws missing) that converted: `...`
- important due families / examples that converted: `...`
- conversion class notes: `...`
- most important due-doubles ranking lesson: `...`

## Part I — All Daily Doubles And Mirror Doubles Evidence Audit

Auto-captured anchors:
- daily doubles / mirror doubles reviewed: `OntarioCanada4` `Midday` winner=`998` type=`double` rank=`10` DS=`10` mirror_pairs=`-`; `NewYork4` `Evening` winner=`496` type=`mirror_double` rank=`7` DS=`5` mirror_pairs=`4/9`; `NorthCarolina4` `Midday` winner=`169` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`1/6`; `NorthCarolina4` `Evening` winner=`083` type=`mirror_double` rank=`8` DS=`5` mirror_pairs=`3/8`; `Virginia4` `Evening` winner=`627` type=`mirror_double` rank=`14` DS=`3` mirror_pairs=`2/7`; `Ohio4` `Midday` winner=`585` type=`double` rank=`9` DS=`2` mirror_pairs=`-`; `Ohio4` `Evening` winner=`646` type=`double` rank=`9` DS=`2` mirror_pairs=`-`; `Pennsylvania4` `Evening` winner=`439` type=`mirror_double` rank=`11` DS=`2` mirror_pairs=`4/9`; `PuertoRico4` `Midday` winner=`729` type=`mirror_double` rank=`12` DS=`2` mirror_pairs=`2/7`; `PuertoRico4` `Evening` winner=`222` type=`triple` rank=`12` DS=`2` mirror_pairs=`-`; `Florida4` `Midday` winner=`273` type=`mirror_double` rank=`3` DS=`1` mirror_pairs=`2/7`; `Florida4` `Evening` winner=`100` type=`double` rank=`3` DS=`1` mirror_pairs=`-`; `Indiana4` `Midday` winner=`954` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`4/9`; `Indiana4` `Evening` winner=`836` type=`mirror_double` rank=`4` DS=`1` mirror_pairs=`3/8`; `Michigan4` `Midday` winner=`946` type=`mirror_double` rank=`5` DS=`0` mirror_pairs=`4/9`; `Michigan4` `Evening` winner=`633` type=`double` rank=`5` DS=`0` mirror_pairs=`-`; `NewJersey4` `Midday` winner=`877` type=`double` rank=`6` DS=`0` mirror_pairs=`-`; `SouthCarolina4` `Midday` winner=`884` type=`double` rank=`13` DS=`0` mirror_pairs=`-`
- support sources: due-doubles=`sharepacks/2026-01-16/control_center/due_doubles.csv` BA=`sharepacks/2026-01-16/control_center/blackapple_alerts.csv` alerts=`sharepacks/2026-01-16/control_center/profit_alerts.csv`
- window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15_to_2026-01-18__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15_to_2026-01-18__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

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
- strongest boxed themes: `004` x9; `001` x9; `013` x7; `017` x7; `014` x7; `009` x6
- strongest straight themes: `009` x3; `090` x3; `101` x3; `004` x3; `040` x3; `400` x3
- strongest VT-box themes: `23` x13; `15` x12; `33` x11; `12` x11; `5` x9; `18` x9
- repeated positional shortlist carries: `013` x3; `047` x3; `011` x3; `357` x3; `036` x3; `367` x3
- repeated Blackapple carries: `014` x6; `012` x5; `015` x5; `038` x4; `013` x4; `016` x4
- profit-alert implied carries: `349` x3; `059` x2; `009` x2; `045` x2; `339` x2; `019` x2
- due-double carries: `559` x4; `004` x4; `009` x4; `448` x4; `155` x4; `556` x4
- preserved-not-budgeted canonicals: `036` x2; `449` x2; `028` x2; `089` x1; `037` x1; `225` x1

Analyst conclusion:
- most important preserved-not-budgeted cluster: `...`
- strongest translator-learning note: `...`

## Part L — Control-Arm Comparison

Auto-captured anchors:
- candidate-universe grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md`
- play-card grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__PLAY_CARD_GRADE__tool_only__arena_v0.md`
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
