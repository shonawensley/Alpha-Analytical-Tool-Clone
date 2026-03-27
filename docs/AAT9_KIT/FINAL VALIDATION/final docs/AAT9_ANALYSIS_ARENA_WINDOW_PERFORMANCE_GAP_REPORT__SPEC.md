# AAT9 Analysis Arena Window Performance / Opportunity Gap Report — Spec

Purpose: quantify how well the Analysis Arena branch understood a full gold-day
window, how much of that understanding was actually realized by the current
control arm, and where the gap points toward future translator/budget work.

This report is explicitly not a replacement for per-state Master Validation or
Brain 2 Master Validation. It is the window-close quantitative bridge between:

- arena truth preservation
- board-level cross-state judgment
- control-arm realized performance
- future translator / budgeting development

## Scope

Use this report after a completed window under:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<...>/`

It should consume the canonical aligned window outputs only.

## Primary Inputs

- Window `ANALYSIS_ARENA/` receipts:
  - board scoreboard `json/csv`
  - board review bundle `json`
  - board spillover overlay `json`
  - shadow DPL `json`
  - translation sandbox day manifest `json`
- Predictive sharepack state artifacts:
  - `aggregated_analysis_arena__*.json`
  - `translation_sandbox_seed__*.json`
  - `candidate_universe__*.json`
  - `play_card__*.json`
- Post-results control-center tables:
  - `sharepacks/<D>/control_center/*.csv`
- Results truth:
  - `data/results/<D>.txt`
- Window doubles inventory:
  - `__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

## Output Files

- Markdown report
- JSON metrics payload
- Optional CSV ledger for per-state/day scoring rows

Recommended names:

- `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP.md`
- `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP.json`
- `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## Required Sections

### 1. Window Metadata

- window dates
- number of days
- number of states
- profile / experiment tag
- canonical artifact roots

### 2. Arena Intrinsic Quality

Quantify the system without collapsing everything into B12/B24/B36.

Examples:

- winner-state on board
- top-primary / secondary / best-clean-host correctness
- winner canonical / family / VTRAC / index containment inside arena evidence
- survivor / consensus / tracker-rich state relevance
- board shared-complex capture

### 3. Control-Arm Realized Performance

Quantify what the current downstream baseline actually realized.

Examples:

- Candidate Universe `hit_any`
- Play Card `hit_any`
- boxed/straight realization where available
- budget-level performance where available

### 4. Opportunity Gap

This is the core differentiator.

Measure where:

- arena evidence was strong
- control-arm realization was weak
- translation sandbox showed preserved-but-not-budgeted structure

Examples:

- board-right / play-miss cases
- winner family / VTRAC clearly present but cut away downstream
- tracker-rich state correctly elevated but poorly translated

### 5. Tracker / Context Attribution

Quantify how much lift appears associated with:

- profit alerts
- compound events
- due doubles / mirror doubles
- Blackapple
- positional tracker
- survivor context
- `R-Consensus`

### 6. Translator-Learning Signals

Aggregate what the window suggests for future next layers.

Examples:

- repeated boxed themes
- repeated straight themes
- repeated VT-box themes
- repeated control-arm cut patterns
- repeated state clusters that wanted broader expression

### 7. Final Promotions / Warnings

End with explicit recommendations:

- preserve
- promote to future translator investigation
- keep shadow-only
- demote / noisy

## Metric Philosophy

The report should separate:

- `arena_truth_quality`
- `control_arm_realization_quality`
- `opportunity_gap`

Do not collapse those into one score.

## Preferred Evidence Style

- machine-readable first
- markdown narrative second
- template-derived prose only as supporting explanation

## Non-Goals

- designing the final combo-forming engine
- designing the final budgeting engine
- rewriting analyzers

This report exists to provide the evidence those future layers should listen to.
