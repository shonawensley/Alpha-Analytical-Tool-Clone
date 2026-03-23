# AAT9 Analysis Arena Branch System Map

Date: `2026-03-21`

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
7. downstream baseline control arm

## Operating Picture

The cleanest way to think about the branch now is:

### Brain 1

Per-state predictive analysis.

This is where the system:

- builds fresh state artifacts
- preserves rich tool evidence
- synthesizes the aggregated analysis arena
- classifies local structure, pressure, and context

### Brain 2

Board-level comparison and decision support.

This is where the system should:

- compare strong states against each other
- rank states
- detect spillover and shared family complexes
- separate spent vs unspent families after Midday
- preserve final findings before combination forming

### Master Validation

Post-results deep learning and reverse-engineering.

This is where the system should:

- inspect winners truth first
- compare that truth against the arena and tool evidence
- learn what deserves later policy or conversion promotion
- shape future final-findings and combination-forming logic from actual data instead of guesswork

This separation matters:

- Brain 1 is the live per-state predictive runtime
- Brain 2 is the live board/decision runtime
- Master Validation is the learning loop that improves both

That is why analysis, final findings, combination forming, and budgeting are related without being the same layer.

## Layer 1 — Predictive-Day Tool Generation

This is the rebuilt predictive shell that creates fresh state artifacts from a history workbook.

Main entry:

- `scripts/tools/run_predictive_day.py`

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

## Layer 6 — Competition-Style Board Reads

This is where live predictive days and Midday -> Evening reranks are being used to stress-test the branch.

Recent receipts:

- `2026-03-21__COMPETITION8__CT_ON_VA_NJ_NC.md`
- `2026-03-21__COMPETITION8__EVENING_RERANK_AFTER_MIDDAY.md`
- `2026-03-21__COMPETITION8__CROSS_STATE_CROSSOVER_LEDGER.md`
- `2026-03-21__BOARD_SPILLOVER_OVERLAY__competition8_evening_rerank_after_midday.md`

Current runtime artifact:

- `scripts/tools/build_board_spillover_overlay.py`
- `scripts/tools/create_board_scoreboard.py`
- `scripts/tools/create_board_review_bundle.py`
- `scripts/tools/create_day_arena_board_review.py`

Important new learning from this layer:

- some strong family complexes are board-level, not purely state-local
- that means a new layer is needed above per-state arena analysis
- the first reusable board spillover overlay now exists, but its overlap scoring is still intentionally conservative and review-first
- the Brain 2 runtime now preserves richer context hints from Aux / Control Center, especially Blackapple recommendations, positional notes, compound events, and due-double family examples

## Layer 7 — Downstream Baseline Control Arm

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

## Current Big Strengths

The branch is currently strongest at:

- preserving structural evidence broadly
- trapping live VTRAC/family environments
- distinguishing arena recall from downstream conversion
- separating row-level vs state-day accounting
- supporting stronger post-results review

## Current Big Gaps

The branch is not yet final in:

- arena-native combination forming
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

### 3. Advanced Combination Forming

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
4. promote only bounded ideas that repeat
5. add board-level relationship logic above the per-state layer, not inside it

This is the current stable development doctrine for the analysis-arena branch.
