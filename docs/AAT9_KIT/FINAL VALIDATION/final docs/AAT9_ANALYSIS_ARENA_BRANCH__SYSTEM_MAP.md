# AAT9 Analysis Arena Branch System Map

Date: `2026-03-23`

## Why This Document Exists

This is the durable branch-level map for the analysis-arena system.

Its purpose is to prevent important architecture and development direction from living only in chat context.

Use it to answer:

- what is already implemented?
- what layer does each artifact belong to?
- what is still downstream baseline only?
- what are the next major layers we are trying to add?

This is especially important for maintaining continuity when:

- many run artifacts exist
- multiple experiments have landed
- a no-coder owner needs a stable summary of the branch

## Current High-Level System

The arena branch currently has these major layers:

1. predictive-day tool generation
2. per-tool arena/feed preservation
3. aggregated per-state analysis arena
4. review and scoreboards
5. bridge / decay / state-day analysis
6. competition-style board reads
7. decision policy and translators
8. downstream baseline control arm

## Operating Picture

The cleanest way to think about the branch now is:

### Brain 1

Per-state predictive analysis.

This is where the system:

- builds fresh state artifacts
- preserves rich tool evidence
- synthesizes the aggregated analysis arena
- classifies local structure, pressure, and context

### Brain 2A

State-local aggregate context and command-hub inputs.

This is where the system should preserve and organize:

- Control Center alert context
- profit alerts and compound events
- due doubles and repeat-watch state
- Blackapple standing and recommendation context
- Aux compound evidence that influences posture

### Brain 2B

Board-level comparison and decision support.

This is where the system should:

- compare strong states against each other
- rank states
- detect spillover and shared family complexes
- separate spent vs unspent families after Midday
- preserve final findings before combination forming

### Decision Policy Layer

The first action-taking bridge.

This is where the system should:

- decide `PLAY / WATCH / SKIP`
- elect the cheapest rational play mode
- assign a coverage cap class
- route the state to the correct translator family

### Master Validation

Post-results deep learning and reverse-engineering.

This is where the system should:

- inspect winners truth first
- compare that truth against the arena and tool evidence
- learn what deserves later policy or conversion promotion
- shape future final-findings and combination-forming logic from actual data instead of guesswork

This separation matters:

- Brain 1 is the live per-state predictive runtime
- Brain 2A is the live state-local context/event runtime
- Brain 2B is the live board/decision runtime
- the Decision Policy Layer is the live posture/mode bridge
- Master Validation is the learning loop that improves all of them

That is why analysis, final findings, decision policy, combination forming, and budgeting are related without being the same layer.

Current review shells now split as:

- per-state Master Validation template
- Brain 2 runtime/operating template
- Brain 2 Master Validation companion

That means the branch now has:

- one deep state-level reverse-engineer shell
- one board-level operating shell
- one board-level post-results grading shell

## Layer 1 — Predictive-Day Tool Generation

This is the rebuilt predictive shell that creates fresh state artifacts from a history workbook.

Main entry:

- `scripts/tools/run_predictive_day.py`
- `scripts/tools/run_analysis_arena_cycle.py` (arena-era operator wrapper)

Primary outputs:

- string tables + JSON mirrors
- Stable outputs
- Digit Reduction outputs
- Hot Zones outputs
- VTRAC outputs
- Aux summaries + draw snapshots
- Control Center sharepack bundle

## Layer 2 — Per-Tool Arena / Feed Preservation

This is where rich tool evidence is preserved before downstream narrowing.

Main reference docs:

- `AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`

Current emphasis:

- Stable = family/lane, compounding, survivor/frontier, hidden/transform clues
- DR = reduction reveal, corridor, assigned-box extractability, currentness
- VTRAC = lane/index truth, same-index neighborhood, descriptor-backed currentness
- Hot Zones = pressure environment, survivorship, funnel/currentness
- Aux / Control Center = context reinforcement, pressure classification, alert/tracker context

## Layer 3 — Aggregated Per-State Analysis Arena

This is the main Brain-1 runtime object.

Primary contract:

- `AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`

Primary builder:

- `scripts/tools/build_aggregated_analysis_arena.py`

Key namespaces:

- `string_tools`
- `context_tools`
- `cross_tool_relations`
- `arena_synthesis`
- `downstream_handoff`
- `review_links`

This layer is now real and implemented.

It is more than storage:

- it aggregates
- compares tools
- surfaces dominant canonicals, families, and lanes
- exposes watchlists and review prompts
- now carries `stable_survivor_context` so survivor/frontier, last-remaining, progression, and hidden-terminal truth remain visible in Brain 1 instead of only inside Stable
- now also carries bounded `r_consensus_context` so `R-Consensus` / tail-consensus remains preserved as a measured Brain-1 event object instead of living only in reverse-engineer harnesses

## Layer 4 — Review And Scoreboards

This is where the arena branch became measurable instead of theoretical.

Main tools:

- `scripts/tools/review_aggregated_analysis_arena.py`
- `scripts/tools/review_aggregated_analysis_arena_decay.py`
- bridge family and bridge state-day scoreboards
- broader arena review state-day scoreboards

Current review posture:

- row-level diagnostics remain the best truth-analysis lens
- state-day rollups are now the best accounting/performance lens

## Layer 5 — Bridge / Decay / State-Day Analysis

This layer studies how trapped structural truth might convert later.

Current status:

- real and productive
- still research-only
- not yet promoted into a broad production bridge rule

Main current finding:

- one universal bridge does not exist yet
- source-family-specific bridge behavior appears more realistic
- special-event research harnesses are the right place to study high-value event families before promotion

## Layer 6 — Competition-Style Board Reads

This is where live predictive days and Midday -> Evening reranks are being used to stress-test the branch.

Recent receipts:

- `2026-03-21__COMPETITION8__CT_ON_VA_NJ_NC.md`
- `2026-03-21__COMPETITION8__EVENING_RERANK_AFTER_MIDDAY.md`
- `2026-03-21__COMPETITION8__CROSS_STATE_CROSSOVER_LEDGER.md`
- `2026-03-21__BOARD_SPILLOVER_OVERLAY__competition8_evening_rerank_after_midday.md`

Current runtime artifact:

- arena-era fresh-run receipts now belong under:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`
- historical/control-arm comparison receipts remain under:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

Companion flow reference:

- `AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`

- `scripts/tools/build_board_spillover_overlay.py`
- `scripts/tools/create_board_scoreboard.py`
- `scripts/tools/create_board_review_bundle.py`

## Special Research Harnesses

The branch now also carries focused research harnesses for event families that are
too valuable to ignore but too specialized to promote without direct measurement.

Current examples:

- survivor / frontier audit
- `R-Consensus` harness and integration memo

These should stay:

- evidence-first
- review-heavy
- reverse-engineer driven

until the branch has enough casework to justify operational promotion.
- `scripts/tools/create_day_arena_board_review.py`
- `scripts/tools/build_shadow_decision_policy.py`

Recent promotion boundary:

- `R-Consensus` is now preserved in runtime as `r_consensus_context`
- it is visible in Brain 1, Brain 2, and shadow DPL
- it is still shadow/scored only and not active translator logic

Important new learning from this layer:

- some strong family complexes are board-level, not purely state-local
- that means a new layer is needed above per-state arena analysis
- the first reusable board spillover overlay now exists, but its overlap scoring is still intentionally conservative and review-first
- the Brain 2 runtime now preserves richer context hints from Aux / Control Center, especially Blackapple recommendations, positional notes, compound events, and due-double family examples
- the Brain 2 runtime now also carries survivor-aware state hints so survivor-rich / last-remaining-rich states are visible at board-review and shadow-DPL time

## Layer 7 — Decision Policy And Translators

This is the next architectural layer after Brain 2.

Primary new branch specs:

- `AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_TRANSLATOR_ARCHITECTURE__ANALYSIS_ARENA_BRANCH.md`

Recommended purpose:

- turn evidence into posture
- separate `PLAY / WATCH / SKIP`
- elect `perm_only / boxed / vt_box / vt_straight / hybrid`
- keep boxed and straight translation separate
- keep coverage logic separate from later economics

Current role:

- shadow runtime + architecture/spec layer
- current runtime is read-only and review-first
- it now emits posture/mode/cap-class/route receipts without taking control away from the current downstream control arm
- translation-sandbox seeds now exist as a downstream learning companion so near-final cluster geometry can be collected without pretending active translators already exist

## Layer 8 — Downstream Baseline Control Arm

These remain in place:

- Candidate Universe
- Play Card
- current combination-forming / budget infrastructure

Current role:

- baseline/control arm
- downstream comparison target

Current non-role:

- they are not the definition of arena truth
- they are not yet the final arena-native end state

## Translation Sandbox Companion

This is a bounded learning layer between:

- shadow DPL
- future active translators

Primary runtime:

- `scripts/tools/create_translation_sandbox_seed.py`

Primary companion note:

- `AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Purpose:

- collect provisional boxed / straight / vt-box seed geometry
- preserve shortlist / survivor / `R-Consensus` carry-through
- compare what the control arm kept vs cut
- learn from fresh runs without activating live translator logic

## Current Big Strengths

The branch is currently strongest at:

- preserving structural evidence broadly
- trapping live VTRAC/family environments
- distinguishing arena recall from downstream conversion
- separating row-level vs state-day accounting
- supporting stronger post-results review

## Current Big Gaps

The branch is not yet final in:

- active decision policy thresholds
- arena-native split translators
- arena-native budgeting
- final findings relationship logic
- refined board-level spillover / crossover scoring and scoreboard integration

## Immediate Next Structural Layers

### 1. Board Spillover Overlay

Purpose:

- compare strong states against each other
- detect shared lanes/families
- detect spent vs unspent family behavior after Midday

Current status:

- `v0` runtime artifact exists
- compact scoreboard consumer now exists
- one-step board review bundle now exists
- next work is further refinement and stronger Brain-2 handoff discipline

### 2. Final Findings Relationship Layer

Purpose:

- preserve direct, lane/family, and composite relationships
- hand cleaner findings to future combination forming

Primary design note:

- `AAT9_FINAL_FINDINGS_RELATIONSHIP_LAYER__ARENA_BRANCH.md`

### 3. Decision Policy Layer

Purpose:

- convert Brain 1 truth + Brain 2 opportunity into action posture
- choose play/watch/skip
- choose mode
- choose cap class
- route states into the correct translator family

Primary design note:

- `AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md`

### 4. Split Translator Layer

Purpose:

- replace one-size-fits-all downstream compression with bounded mode-specific translation

Primary families:

- boxed translator
- straight translator
- VT-box translator
- later special translators such as consensus-trial translation

Primary design note:

- `AAT9_TRANSLATOR_ARCHITECTURE__ANALYSIS_ARENA_BRANCH.md`

### 5. Advanced Combination Forming

Purpose:

- consume final findings rather than only local top-N surfaces
- use relationship-aware and board-aware results

This is future-facing and should come after the relationship layer is better defined.

## Stable Repo Sources Of Truth

Use these documents to preserve continuity:

### Stable architecture / contracts

- `AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- `AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `AAT9_FINAL_FINDINGS_RELATIONSHIP_LAYER__ARENA_BRANCH.md`
- `AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_TRANSLATOR_ARCHITECTURE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `scripts/tools/build_board_spillover_overlay.py`
- `scripts/tools/create_board_scoreboard.py`
- `scripts/tools/create_board_review_bundle.py`
- `scripts/tools/create_day_arena_board_review.py`

### Live trackers

- `AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `AAT9_ARENA_ANALYSIS_BACKLOG.md`

### Run receipts

- competition memos
- arena review memos
- bridge scoreboards
- casepacks

## Working Doctrine

The branch should continue to follow this order:

1. preserve evidence broadly
2. review it honestly against truth
3. separate direct findings from hypotheses
4. add board-level relationship logic above the per-state layer, not inside it
5. convert truth into posture before translation
6. translate mode-specifically before economics
7. promote only bounded ideas that repeat

This is the current stable development doctrine for the analysis-arena branch.
