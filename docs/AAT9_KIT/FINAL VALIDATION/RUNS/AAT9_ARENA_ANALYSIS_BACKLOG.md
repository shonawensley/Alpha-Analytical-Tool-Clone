# AAT9 Arena Analysis Backlog

Purpose: keep arena-phase follow-up work visible after tool integration so high-value ideas do not get buried in older tool logs or chat context.

Ground rule:

- this backlog is for **arena-analysis** work, not for reopening broad tool rewrites
- additions here should be aggressive but evidence-driven
- items move forward when arena review, anchor review, or decay review proves they matter

## Active Threads

| ID | Status | Focus | Why it matters | Trigger to elevate |
|---|---|---|---|---|
| `AAB-001` | `implemented` | source-attributed context review | lets us see when Profit Alerts, Blackapple, due doubles, repeat watch, Aux overdue-index pressure, and badge pressure actually touched the winner lane/object | keep refining only if repeated anchors show missing attribution detail |
| `AAB-002` | `implemented` | frozen-snapshot decay review | measures whether a trapped arena object resolves after same-day, which is essential for lingering-pattern logic | expand windows and reporting once first corpus reviews are stable |

## Approved Next Additions

| ID | Status | Focus | Why it matters | Evidence target |
|---|---|---|---|---|
| `AAB-003` | `approved` | hidden-behind-1-clutter-digit reveal mechanism | winners HTML repeatedly shows real patterns surviving behind one clutter digit; predictive-side arena should preserve that reveal instead of relying only on manual winner review | show repeated lift on lane/family recall or watchlist usefulness |
| `AAB-004` | `approved` | richer VTRAC compound elevation criteria | overdue indices, badge-index pressure, and boxed-VTRAC matrix ideas are powerful, but should move from linked truth layer to core arena objects only when attribution/decay proves they matter | source-attributed review + decay review show consistent short-window resolution |
| `AAB-005` | `approved` | arena object registry for high-scoring pattern clusters | a formal registry of top canonicals, top lanes, top families, and top watchlist neighborhoods will make decay/carryover review cleaner and support later conversion work | repeated need to compare “what the arena actually trapped” across days |
| `AAB-006` | `approved` | competition carryover / decay scoreboard | live competitions kept showing strong states converting one or more draws later; this needs to be measured explicitly instead of treated as anecdote | frozen decay harness proves value on gold windows first |
| `AAB-007` | `approved` | regime-conditioned decay splits | doubles-heavy, split-rail, and lane-clean environments may decay differently; this matters for state ranking and later packaging | decay metrics show materially different behavior by regime |
| `AAB-008` | `implemented` | context source precision rollups | the front-band rollup now summarizes repeated source families and source mixes against `D+3` dominant-VTRAC and watchlist-box behavior, turning row-level flags into corpus evidence | keep expanding only if broader windows materially change the current source ordering |

## Watchlist Items

| ID | Status | Focus | Notes |
|---|---|---|---|
| `AAB-009` | `watch` | heavier boxed VTRAC badge matrix export | currently stays as a linked truth/reporting layer; revisit only if arena review keeps needing more combo-level badge semantics than the current structured summaries preserve |
| `AAB-010` | `implemented` | same-day midday-to-evening carry-forward inside decay | bridge-study rows and corpus readback now emit explicit resolution profiles, so same-day carry-forward and same-day precursor hits are no longer buried in generic decay buckets. Current strict-gate evidence shows the only non-same-day resolver is actually a same-day carry-forward case, which validates this split as a real measurement need |
| `AAB-011` | `implemented` | conversion-side lane-to-literal bridge scoring | the bounded bridge-study harness now exists, has been run across December, January, June, and late-January follow-up blocks, and now has a direct gated corpus read plus family scoreboard. `aux_overdue+aux_badge` remains the only repeating bridge cohort, and the first credible structural gate is `lane_alive_literal_missing_front3/front5` with `arena_vtrac_rank <= 5`, but broader confirmation keeps it mixed rather than promotable. The current family scoreboard has `aux_overdue+aux_badge` at `3/8` direct same-outcome, `1/8` same-day precursor plus same-day, `1/8` same-day carry-forward, `3/8` miss; `due_doubles+aux_badge` at `1/2` direct and `1/2` future-day decay; `profit_alert+aux_badge` at `1/3` direct, `1/3` future-day decay, `1/3` miss; and the heavier four-source pileup still weak at `1/3` future-day decay, `2/3` miss | keep in study mode until one source family repeats cleanly enough in its natural mode (direct, carry-forward, or future-day decay) to justify the next bounded bridge rule |
| `AAB-012` | `implemented` | bridge family scoreboard | source-family-specific bridge behavior is now summarized directly from measured strict/gated bridge rows via `scripts/tools/summarize_aggregated_arena_bridge_families.py`, so bridge research no longer has to rely on pooled cohort prose. This keeps `aux_overdue+aux_badge`, `due_doubles+aux_badge`, `profit_alert+aux_badge`, and heavier mixes comparable by reviewed outcome and resolution profile across windows | expand only if new windows materially change the current family ordering or reveal a new repeating family |
| `AAB-013` | `implemented` | bridge family casepack / mode split | source-family bridge rows can now be reviewed as concrete casepacks via `scripts/tools/export_aggregated_arena_bridge_family_casepack.py`, which exposed the first real family-mode differences: `due_doubles+aux_badge` is currently Evening-only, `profit_alert+aux_badge` is currently Midday-only, and `aux_overdue+aux_badge` is mixed but materially cleaner on Evening than Midday rows | elevate only if repeated windows keep the same family/mode pairing and the next bounded bridge experiment can target that mode directly |
| `AAB-014` | `implemented` | bridge family mode sufficiency scoreboard | source-family / reviewed-outcome slices are now labeled as `thin`, `provisional`, or `measured` via `scripts/tools/summarize_aggregated_arena_bridge_family_modes.py`, so the bridge branch can answer “do we have enough examples yet?” with data instead of intuition. Current corpus status: only `aux_overdue+aux_badge` on Midday is measured, `profit_alert+aux_badge` on Midday is provisional, and the Evening slices are still thin | request more gold-day inventory only when the next bounded experiment depends on a family/mode pair that is still thin or merely provisional |
| `AAB-015` | `implemented` | bridge state-day rollup | measured bridge rows can now be collapsed from outcome rows into one `state-day-family` performance unit via `scripts/tools/summarize_aggregated_arena_bridge_state_days.py`, which is the right companion lens for same-state Midday/Evening crossover. Current bridge corpus only shrinks from `16` rows to `15` state-days, so state-day rollup improves accounting clarity more than it changes results, but it is now the right way to answer “did this family resolve on that state-day at all?” | keep this as the performance lens above row-level diagnostics; expand it to broader arena review if state-day accounting becomes the dominant evaluation mode |

## Operating Rule

Use this backlog only after checking:

1. same-day arena review
2. anchor casepack review
3. frozen-snapshot decay review

If an item is not justified by one of those, it stays backlog-only.
