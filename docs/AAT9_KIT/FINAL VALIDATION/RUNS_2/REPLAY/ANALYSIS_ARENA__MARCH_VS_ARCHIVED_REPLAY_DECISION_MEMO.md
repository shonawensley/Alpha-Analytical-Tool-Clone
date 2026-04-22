# Analysis Arena March vs Archived Replay Decision Memo

## Guardrail

This memo is read-only. It compares completed Stage 6B through Stage 7B evidence and does not change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Source Selection

- March canonical source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- March same-window replay source inspected: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- Archived replay source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- Caveat: the March same-window replay subfolder has zeroed core Stage 6B candidate metrics for baseline/primary/support lanes because it is an isolated single-window replay root and the Stage 3 through Stage 6B chain requires cross-window evidence for candidate/support promotion. For this memo, the canonical `RUNS_2` March Stage 6B/7B stack is the valid March metric source. If an official same-window root-level Stage 6B replay baseline is needed, it should be rebuilt as a corpus-mirrored replay root rather than treating the isolated March replay folder as corrupted.

## Executive Decision

- Archived replay v2 does not confirm the March primary restrained lane strongly enough to start Stage 8A implementation or any live downstream rewrite.
- It does confirm the value of the guardrail architecture: lane separation, duplicate-credit restraint, support-as-context, decay-as-companion, and soft-before-hard restraint all remain necessary.
- The primary restrained candidate expression remains a testable research spine, but its status is downgraded from March-positive seed to fresh-window confirmation target.
- The next useful work is a fresh-window confirmation run or, if no fresh window is ready, a corpus-mirrored same-window replay baseline design that preserves cross-window promotion gates while keeping archived replay as a stress-test package.

## Core Metric Read

| scenario | March FP | Archived FP | March yield | Archived yield | March pool | Archived pool | read |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `baseline_clean_boxed` | 60.4% | 35.4% | 12.407 | 55.897 | 50.642 | 8.864 | archived baseline is much sharper than March baseline |
| `primary_restrained_candidate_expression` | 46.8% | 47.3% | 16.075 | 51.487 | 69.032 | 78.481 | weakened: March improved baseline, archived loses to its sharper baseline and expands pool |
| `candidate_rows_with_support_context` | 55.4% | 51.0% | 12.969 | 46.737 | 131.218 | 61.885 | support-on remains too broad/weak as a positive modifier |
| `candidate_rows_without_support_context` | 48.9% | 51.5% | 23.895 | 48.511 | 44.292 | 71.375 | support-off/reference remains at least as sharp as support-on |
| `decay_watch_companion_excluded` | 82.5% | 83.0% | 3.920 | 9.781 | 106.788 | 110.485 | repeated companion-only behavior; useful context but high false-positive pressure |
| `restraint_retest_surface_excluded` | 32.8% | 49.0% | 22.492 | 49.229 | 13.149 | 29.290 | promising research surface, but not hard-veto permission |

## Requirement Comparison

| requirement | target | March | Archived | interpretation |
| --- | --- | --- | --- | --- |
| `S6B-001` | `primary_restrained_candidate_expression` | `pass_with_concentration_warning` | `fail` | weakened: March primary passed with concentration warning, archived primary failed versus its baseline |
| `S6B-002` | `secondary_lineage_supported_restrained` | `partial_modifier_only` | `partial_modifier_only` | repeated as modifier-only: secondary lineage should not become independent expansion |
| `S6B-003` | `support_context_modifier` | `fail_as_positive_modifier` | `fail_as_positive_modifier` | repeated block: support context is not a broad positive modifier |
| `S6B-004` | `restraint_calibration_surface` | `pass_research_not_live` | `pass_research_not_live` | repeated research lane: restraint is soft-penalty research, not hard veto |
| `S6B-005` | `source_a_source_b_overlap` | `pass` | `pass` | repeated guardrail: overlap is narrowing/restraint, not duplicate credit |
| `S6B-006` | `window_and_state_concentration` | `pass_with_warning` | `fail` | weakened: concentration warning becomes an explicit fail in archived replay |
| `S6B-007` | `decay_watch_companion` | `pass_excluded` | `pass_excluded` | repeated boundary: decay remains companion/context only |

## Stage 7B Readiness Comparison

- March queue status counts: `{'ready_for_fresh_confirmation': 1, 'ready_but_watch': 9, 'research_only': 2, 'blocked_by_requirements': 1}`
- Archived queue status counts: `{'ready_but_watch': 9, 'research_only': 2, 'blocked_by_requirements': 1}`
- March requirement coverage counts: `{'ready_for_fresh_confirmation': 1, 'ready_but_watch': 6, 'research_only': 1, 'blocked_by_requirements': 1}`
- Archived requirement coverage counts: `{'ready_for_fresh_confirmation': 1, 'ready_but_watch': 6, 'research_only': 1, 'blocked_by_requirements': 1}`
- March blocker recheck counts: `{'ready_for_fresh_confirmation': 2, 'ready_but_watch': 4}`
- Archived blocker recheck counts: `{'ready_for_fresh_confirmation': 3, 'ready_but_watch': 3}`

Interpretation: both packages keep the translator/scoring rewrite blocked. March has one queue item ready for fresh confirmation; archived keeps the same primary requirement testable but removes the positive queue posture because archived replay did not repeat the primary advantage.

## What Repeated

- `support_context_modifier` failed as a broad positive modifier in both canonical March and archived replay.
- `restraint_calibration_surface` remains research-positive, but only as soft-penalty work, not hard veto.
- `source_a_source_b_overlap` remains useful as narrowing/restraint, not duplicate scoring credit.
- `decay_watch_companion` remains explicitly companion-only and should stay out of candidate-pool spend metrics.
- Stage 7B continues to allow fresh-window confirmation replay while blocking live scoring/candidate/budget changes.

## What Weakened

- The March primary restrained lane did not repeat as a positive archived-window result: March primary had FP `46.8%` and yield `16.075` versus March baseline FP `60.4%` and yield `12.407`; archived primary had FP `47.3%` and yield `51.487` versus archived baseline FP `35.4%` and yield `55.897`.
- Concentration moved from March `pass_with_warning` to archived `fail`, so concentration must stay an active blocker.
- Broad support remains weaker than the sharper reference/off surfaces, so support should be narrowed or paired, not promoted broadly.

## Decision

- Do not begin Stage 8A implementation yet.
- Keep Stage 8A as design-ready but evidence-blocked until fresh-window confirmation repeats or quarantines the primary lane.
- Preserve the archived replay package as a stress-test/negative-control package because it exposed where March-positive evidence fails to generalize.
- Use the next fresh window to test only the explicit Stage 7A/7B gates: primary restrained candidate expression, concentration, narrow support, soft restraint, duplicate-credit, and decay boundary.

## Optimal Next Step

1. Do not treat `REPLAY/march_2026_15day_replay_v2` Stage 6B zero lanes as random corruption; if an official same-window root-level Stage 6B baseline is needed, build a corpus-mirrored replay root with enough windows to preserve cross-window promotion behavior.
2. Prepare the next fresh-window run using the Stage 7A/7B checklist, with archived replay v2 treated as the stress-test comparison layer.
3. After fresh-window Stage 6B through Stage 7B exists, produce a three-way comparison: canonical March vs archived replay v2 vs fresh window.
4. Only if the fresh window repeats or cleanly quarantines the open blockers should Stage 8A move from design brief to shadow candidate-object specification.

## Outputs

- memo_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO.json`
- scenario_comparison_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__SCENARIO_COMPARISON.csv`
- requirement_comparison_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__REQUIREMENT_COMPARISON.csv`
- lane_comparison_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__LANE_COMPARISON.csv`
- blocker_comparison_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/ANALYSIS_ARENA__MARCH_VS_ARCHIVED_REPLAY_DECISION_MEMO__BLOCKER_COMPARISON.csv`
