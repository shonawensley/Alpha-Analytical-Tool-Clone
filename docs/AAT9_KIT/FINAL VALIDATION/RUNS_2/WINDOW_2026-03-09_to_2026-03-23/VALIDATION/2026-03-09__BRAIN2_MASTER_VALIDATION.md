# Brain 2 Master Validation Run Report — D=2026-03-09 (H=2026-03-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Relationship to the arena-era workflow:
- Board runtime template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Translation sandbox template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## Rank Integrity Warning

**RANK INTEGRITY STATUS: `INVALID_STATIC_ORDER`**

Current board rank fields are legacy, state-order-dominated priority receipts. They must not be interpreted as an evidence-derived analytical ranking.

Capture@K, top-ranked-state, and rank-performance conclusions are `NOT_EVALUABLE` until Phase 2 supplies an explicit valid analytical-rank contract.

## Scope
- Results date (D): `2026-03-09`
- History workbook date (H): `2026-03-08`
- Board scope states (14): `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Full-day tracker scope: `all states represented in the frozen control_center sharepack tables`

## Locked Artifacts
- Board review bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.json`
- Board scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SCOREBOARD__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SCOREBOARD__analysis_arena_day_review.json`
- Board spillover overlay: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- Shadow DPL: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__SHADOW_DECISION_POLICY__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`
- Translation sandbox day manifest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json`
- Predictive Control Center root: `sharepacks/_predictive/2026-03-09/control_center`
- Truth/evaluation Control Center root: `sharepacks/2026-03-09/control_center`
- Predictive source integrity: `PASS` result_fields_inert=`True`
- Truth/evaluation receipts available: _none available_
- Control-arm grade directory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09_to_2026-03-23__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09_to_2026-03-23__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

## Quick Auto-Captured Anchors
- Top scoreboard rows: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`168, 189, 006`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006, 129, 259`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224, 778, 889`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011, 225, 255`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`118, 778, 188`
- Board verdict top_primary_target: `Connecticut4`
- Board verdict secondary_target: `Delaware4`
- Board verdict best_clean_host: `Connecticut4`
- Board verdict highest_context_support_state: `NorthCarolina4`
- Shadow DPL play states: _none_
- Shadow DPL watch states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- Daily doubles / mirror doubles detected: ``Delaware4` `Midday` winner=`884` type=`double` rank=`2` mirror_pairs=`-``, ``Florida4` `Evening` winner=`941` type=`mirror_double` rank=`3` mirror_pairs=`4/9``, ``Florida4` `Midday` winner=`383` type=`double` rank=`3` mirror_pairs=`3/8``, ``Michigan4` `Evening` winner=`116` type=`double` rank=`5` mirror_pairs=`1/6``, ``Michigan4` `Midday` winner=`373` type=`double` rank=`5` mirror_pairs=`-``, ``NewJersey4` `Midday` winner=`617` type=`mirror_double` rank=`6` mirror_pairs=`1/6``, ``NewYork4` `Midday` winner=`900` type=`double` rank=`7` mirror_pairs=`-``, ``NorthCarolina4` `Evening` winner=`000` type=`triple` rank=`8` mirror_pairs=`-``, ``NorthCarolina4` `Midday` winner=`855` type=`double` rank=`8` mirror_pairs=`-``, ``Ohio4` `Evening` winner=`664` type=`double` rank=`9` mirror_pairs=`-``, ``Ohio4` `Midday` winner=`848` type=`double` rank=`9` mirror_pairs=`-``, ``OntarioCanada4` `Evening` winner=`559` type=`double` rank=`10` mirror_pairs=`-``, ``Pennsylvania4` `Evening` winner=`966` type=`double` rank=`11` mirror_pairs=`-``, ``Pennsylvania4` `Midday` winner=`040` type=`double` rank=`11` mirror_pairs=`-``, ``PuertoRico4` `Evening` winner=`419` type=`mirror_double` rank=`12` mirror_pairs=`4/9``, ``PuertoRico4` `Midday` winner=`887` type=`double` rank=`12` mirror_pairs=`-``, ``SouthCarolina4` `Evening` winner=`505` type=`double` rank=`13` mirror_pairs=`0/5``, ``SouthCarolina4` `Midday` winner=`455` type=`double` rank=`13` mirror_pairs=`-``, ``Virginia4` `Evening` winner=`188` type=`double` rank=`14` mirror_pairs=`-``

---

## Part A — File Lock And Scope

Auto-captured anchors:
- board scope states: `Connecticut4`, `Delaware4`, `Florida4`, `Indiana4`, `Michigan4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `PuertoRico4`, `SouthCarolina4`, `Virginia4`
- frozen predictive tracker artifacts: `sharepacks/_predictive/2026-03-09/control_center/profit_alerts.csv`, `sharepacks/_predictive/2026-03-09/control_center/profit_compound_events.csv`, `sharepacks/_predictive/2026-03-09/control_center/blackapple_alerts.csv`, `sharepacks/_predictive/2026-03-09/control_center/due_doubles.csv`, `sharepacks/_predictive/2026-03-09/control_center/vtrac_repeat_watch.csv`
- post-result evaluation root (kept separate): `sharepacks/2026-03-09/control_center`
- sharepack remains the frozen raw day snapshot; board artifacts are derived arena-era receipts on top of it

Analyst conclusion:
- board scope notes: `...`
- full-day tracker scope notes: `...`
- missing artifact notes: `...`

## Part B — Board Outcome Map

Auto-captured anchors:
- top scoreboard anchors: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`168, 189, 006`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006, 129, 259`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224, 778, 889`
- daily doubles / mirror doubles on the day: ``Delaware4` `Midday` winner=`884` type=`double` rank=`2` mirror_pairs=`-``, ``Florida4` `Evening` winner=`941` type=`mirror_double` rank=`3` mirror_pairs=`4/9``, ``Florida4` `Midday` winner=`383` type=`double` rank=`3` mirror_pairs=`3/8``, ``Michigan4` `Evening` winner=`116` type=`double` rank=`5` mirror_pairs=`1/6``, ``Michigan4` `Midday` winner=`373` type=`double` rank=`5` mirror_pairs=`-``, ``NewJersey4` `Midday` winner=`617` type=`mirror_double` rank=`6` mirror_pairs=`1/6``, ``NewYork4` `Midday` winner=`900` type=`double` rank=`7` mirror_pairs=`-``, ``NorthCarolina4` `Evening` winner=`000` type=`triple` rank=`8` mirror_pairs=`-``, ``NorthCarolina4` `Midday` winner=`855` type=`double` rank=`8` mirror_pairs=`-``, ``Ohio4` `Evening` winner=`664` type=`double` rank=`9` mirror_pairs=`-``, ``Ohio4` `Midday` winner=`848` type=`double` rank=`9` mirror_pairs=`-``, ``OntarioCanada4` `Evening` winner=`559` type=`double` rank=`10` mirror_pairs=`-``, ``Pennsylvania4` `Evening` winner=`966` type=`double` rank=`11` mirror_pairs=`-``, ``Pennsylvania4` `Midday` winner=`040` type=`double` rank=`11` mirror_pairs=`-``, ``PuertoRico4` `Evening` winner=`419` type=`mirror_double` rank=`12` mirror_pairs=`4/9``, ``PuertoRico4` `Midday` winner=`887` type=`double` rank=`12` mirror_pairs=`-``, ``SouthCarolina4` `Evening` winner=`505` type=`double` rank=`13` mirror_pairs=`0/5``, ``SouthCarolina4` `Midday` winner=`455` type=`double` rank=`13` mirror_pairs=`-``, ``Virginia4` `Evening` winner=`188` type=`double` rank=`14` mirror_pairs=`-``
- direct cross-state receipts surfaced by board verdict: _none_

Analyst conclusion:
- actual strongest day states: `...`
- states that converted meaningful structure: `...`
- states that were mostly echo / ambient only: `...`
- day-level structural class: `...`
- most important truth-side board insight: `...`

## Part C — Scoreboard And Ranking Evaluation

Auto-captured anchors:
- top scoreboard rows that mattered: `#1 Connecticut4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`168, 189, 006`; `#2 Delaware4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006, 129, 259`; `#3 Florida4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224, 778, 889`; `#4 Indiana4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011, 225, 255`; `#5 Michigan4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`118, 778, 188`
- top_primary_target=`Connecticut4` secondary_target=`Delaware4`
- best_clean_host=`Connecticut4` highest_context_support_state=`NorthCarolina4`
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
- strongest overlap pairs: `Ohio4` + `OntarioCanada4` score=`36` types=`alert_implied_echo,shared_box_family,shared_lane`; `Connecticut4` + `SouthCarolina4` score=`35` types=`alert_implied_echo,shared_box_family,shared_lane`; `Indiana4` + `Pennsylvania4` score=`34` types=`alert_implied_echo,shared_box_family,shared_lane`; `NewJersey4` + `SouthCarolina4` score=`33` types=`alert_implied_echo,shared_box_family,shared_lane`; `PuertoRico4` + `Virginia4` score=`32` types=`alert_implied_echo,shared_box_family,shared_lane`
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
- highest-value alert states: `Ohio4` alerts=`10` strength_sum=`36.0` ids=`A01,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Pennsylvania4` alerts=`7` strength_sum=`24.0` ids=`A01,A04,A05,A08,A10,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Virginia4` alerts=`6` strength_sum=`22.0` ids=`A01,A04,A05,A08,A10` suggested=`BOX,OVERLAY,STR8_3,STR8_8`; `NewJersey4` alerts=`5` strength_sum=`19.0` ids=`A01,A04,A05,A08,A11` suggested=`BOX,OVERLAY,STR8_3`; `Delaware4` alerts=`4` strength_sum=`16.0` ids=`A04,A05,A10,A11` suggested=`BOX,STR8_3`
- compound-event leaders: `NewJersey4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A05,A11`; `Ohio4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A05,A11`; `Delaware4` `Combined` top_event=`STRAIGHT_GATE` priority=`80` candidates=`A05,A10,A11`; `Indiana4` `Evening` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `NorthCarolina4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `OntarioCanada4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`
- Blackapple ALERT states: `Connecticut4` `Combined` BA=`3` examples=`149 167 014`; `Connecticut4` `Evening` BA=`3` examples=`038 056 146`; `Indiana4` `Evening` BA=`3` examples=`027 126 279`; `NorthCarolina4` `Combined` BA=`3` examples=`049 058 247`; `NorthCarolina4` `Evening` BA=`3` examples=`049 058 238`; `NorthCarolina4` `Midday` BA=`3` examples=`134 017 026`; `PuertoRico4` `Combined` BA=`3` examples=`056 146 479`; `Virginia4` `Combined` BA=`3` examples=`156 489 039`
- due-double threshold states (DS>=3): `Delaware4` DS=`7`; `Pennsylvania4` DS=`4`; `Virginia4` DS=`4`; `Ohio4` DS=`3`
- repeat-watch exact hits: _none_
- separate truth/evaluation rows: alerts=`0` compounds=`0` BA=`0` due=`0` repeat=`0`

Analyst conclusion:
- most important board-scope tracker states: `...`
- most important full-day tracker states outside the board: `...`
- did tracker posture materially explain the day?: `...`
- most important aggregate-tracker insight: `...`

## Part F — Profit Alerts And Special Compound Events

Auto-captured anchors:
- highest-value alert states: `Ohio4` alerts=`10` strength_sum=`36.0` ids=`A01,A04,A05,A08,A11,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Pennsylvania4` alerts=`7` strength_sum=`24.0` ids=`A01,A04,A05,A08,A10,A12` suggested=`BOX,OVERLAY,STR8_3,STR8_4of8`; `Virginia4` alerts=`6` strength_sum=`22.0` ids=`A01,A04,A05,A08,A10` suggested=`BOX,OVERLAY,STR8_3,STR8_8`; `NewJersey4` alerts=`5` strength_sum=`19.0` ids=`A01,A04,A05,A08,A11` suggested=`BOX,OVERLAY,STR8_3`; `Delaware4` alerts=`4` strength_sum=`16.0` ids=`A04,A05,A10,A11` suggested=`BOX,STR8_3`
- top compound-event rows: `NewJersey4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A05,A11`; `Ohio4` `Combined` top_event=`ENGINE_GOV` priority=`85` candidates=`A01,A05,A11`; `Delaware4` `Combined` top_event=`STRAIGHT_GATE` priority=`80` candidates=`A05,A10,A11`; `Indiana4` `Evening` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `NorthCarolina4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`; `OntarioCanada4` `Combined` top_event=`CARRY_PERM` priority=`70` candidates=`A04,A05`
- profit alerts source: `sharepacks/_predictive/2026-03-09/control_center/profit_alerts.csv`
- compound events source: `sharepacks/_predictive/2026-03-09/control_center/profit_compound_events.csv`

Analyst conclusion:
- most important alert IDs: `...`
- implied-set conversions: `...`
- most important special compound events: `...`
- alert-rich but structurally weak states: `...`
- did profit alerts / compound events materially improve Brain 2?: `...`
- most important alert-layer lesson: `...`

## Part G — Blackapple Board Review

Auto-captured anchors:
- BA ALERT states: `Connecticut4` `Combined` BA=`3` examples=`149 167 014`; `Connecticut4` `Evening` BA=`3` examples=`038 056 146`; `Indiana4` `Evening` BA=`3` examples=`027 126 279`; `NorthCarolina4` `Combined` BA=`3` examples=`049 058 247`; `NorthCarolina4` `Evening` BA=`3` examples=`049 058 238`; `NorthCarolina4` `Midday` BA=`3` examples=`134 017 026`; `PuertoRico4` `Combined` BA=`3` examples=`056 146 479`; `Virginia4` `Combined` BA=`3` examples=`156 489 039`
- BA WATCH states: `Florida4` `Combined` BA=`2` examples=`036 045 126`; `Indiana4` `Combined` BA=`2` examples=`016 025 027`; `NewJersey4` `Combined` BA=`2` examples=`013 049 058`; `NewYork4` `Combined` BA=`2` examples=`023 059 149`; `NewYork4` `Evening` BA=`2` examples=`019 028 289`; `Ohio4` `Combined` BA=`2` examples=`015 016 045`; `Ohio4` `Evening` BA=`2` examples=`138 237 039`; `Ohio4` `Midday` BA=`2` examples=`049 058 139`
- Blackapple source: `sharepacks/_predictive/2026-03-09/control_center/blackapple_alerts.csv`

Analyst conclusion:
- important BA recommendation carries: `...`
- states where BA looked stronger than the board gave credit for: `...`
- did BA function mainly as host indicator / echo amplifier / shortlist helper / noise / mixed?: `...`
- most important BA lesson: `...`

## Part H — Due Doubles Ranked-State Evaluation

Auto-captured anchors:
- ranked due states reviewed (DS>=3): `Delaware4` DS=`7`; `Pennsylvania4` DS=`4`; `Virginia4` DS=`4`; `Ohio4` DS=`3`
- top due states that converted in-family: _none / truth receipt unavailable_
- due doubles source: `sharepacks/_predictive/2026-03-09/control_center/due_doubles.csv`

Analyst conclusion:
- top due states that failed: `...`
- threshold states (3 draws missing) that converted: `...`
- important due families / examples that converted: `...`
- conversion class notes: `...`
- most important due-doubles ranking lesson: `...`

## Part I — All Daily Doubles And Mirror Doubles Evidence Audit

Auto-captured anchors:
- daily doubles / mirror doubles reviewed: `Delaware4` `Midday` winner=`884` type=`double` rank=`2` mirror_pairs=`-`; `Florida4` `Evening` winner=`941` type=`mirror_double` rank=`3` mirror_pairs=`4/9`; `Florida4` `Midday` winner=`383` type=`double` rank=`3` mirror_pairs=`3/8`; `Michigan4` `Evening` winner=`116` type=`double` rank=`5` mirror_pairs=`1/6`; `Michigan4` `Midday` winner=`373` type=`double` rank=`5` mirror_pairs=`-`; `NewJersey4` `Midday` winner=`617` type=`mirror_double` rank=`6` mirror_pairs=`1/6`; `NewYork4` `Midday` winner=`900` type=`double` rank=`7` mirror_pairs=`-`; `NorthCarolina4` `Evening` winner=`000` type=`triple` rank=`8` mirror_pairs=`-`; `NorthCarolina4` `Midday` winner=`855` type=`double` rank=`8` mirror_pairs=`-`; `Ohio4` `Evening` winner=`664` type=`double` rank=`9` mirror_pairs=`-`; `Ohio4` `Midday` winner=`848` type=`double` rank=`9` mirror_pairs=`-`; `OntarioCanada4` `Evening` winner=`559` type=`double` rank=`10` mirror_pairs=`-`; `Pennsylvania4` `Evening` winner=`966` type=`double` rank=`11` mirror_pairs=`-`; `Pennsylvania4` `Midday` winner=`040` type=`double` rank=`11` mirror_pairs=`-`; `PuertoRico4` `Evening` winner=`419` type=`mirror_double` rank=`12` mirror_pairs=`4/9`; `PuertoRico4` `Midday` winner=`887` type=`double` rank=`12` mirror_pairs=`-`; `SouthCarolina4` `Evening` winner=`505` type=`double` rank=`13` mirror_pairs=`0/5`; `SouthCarolina4` `Midday` winner=`455` type=`double` rank=`13` mirror_pairs=`-`; `Virginia4` `Evening` winner=`188` type=`double` rank=`14` mirror_pairs=`-`
- support sources: due-doubles=`sharepacks/_predictive/2026-03-09/control_center/due_doubles.csv` BA=`sharepacks/_predictive/2026-03-09/control_center/blackapple_alerts.csv` alerts=`sharepacks/_predictive/2026-03-09/control_center/profit_alerts.csv`
- window doubles inventory: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09_to_2026-03-23__DOUBLES_MIRROR_DOUBLES__INVENTORY.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09_to_2026-03-23__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

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
- strongest boxed themes: `011` x9; `001` x9; `009` x9; `559` x9; `004` x8; `005` x8
- strongest straight themes: `090` x4; `141` x3; `101` x3; `009` x3; `900` x3; `559` x3
- strongest VT-box themes: `23` x12; `5` x12; `15` x11; `18` x10; `2` x8; `12` x8
- repeated positional shortlist carries: `168` x2; `118` x2; `688` x2; `668` x2; `011` x2; `127` x2
- repeated Blackapple carries: `013` x6; `014` x5; `016` x5; `049` x5; `015` x4; `149` x3
- profit-alert implied carries: `069` x3; `003` x3; `667` x2; `006` x2; `066` x2; `559` x2
- due-double carries: `004` x5; `566` x4; `155` x4; `066` x4; `559` x4; `044` x3
- preserved-not-budgeted canonicals: `089` x1; `499` x1; `028` x1; `157` x1; `568` x1; `068` x1

Analyst conclusion:
- most important preserved-not-budgeted cluster: `...`
- strongest translator-learning note: `...`

## Part L — Control-Arm Comparison

Auto-captured anchors:
- candidate-universe grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-09__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md`
- play-card grade: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-09__PLAY_CARD_GRADE__tool_only__arena_v0.md`
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
