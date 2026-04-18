# Signal Source Dictionary And Parser Coverage

This dictionary documents what the post-run audit can currently parse and where each source lives.

## 1. Parsed Sources

- `performance_gap__ledger.csv`: event-level winner alignment booleans, old play-card hits, candidate universe flags, broad support flags, opportunity gaps.
- `HIT_ROSTER.csv`: credited hit fields, strategy hit metadata, profit-alert direct/implied matches, due-double ranks, blackapple status, compound events, final candidate signatures.
- `TRANSLATOR_LEARNING_LEDGER.csv`: translator cohorts, hit classes, frontier columns copied into teaching rows.
- `C1_C2_FRONTIER_CASES.csv`: post-result C1/C2 vertical frontier signatures, strengths, fired tests, double-anchor and compression scores.
- `DECAY_CARRYOVER_ROWS.csv`: state-day signal values and bounded future resolution profiles.
- `BOARD_SCOREBOARD` JSON: board rank, top canonicals, top VTRAC indices, tracker hints.
- `TRANSLATION_SANDBOX_SEED` JSON: Brain1 core, Brain2 context, sandbox hypotheses, control-arm candidate universe, old play-card, and shadow-policy focus.

## 2. Match Modes

- `EXACT`: ordered 3-digit signal value equals the winner.
- `BOX`: canonical sorted digits equal the winner canonical.
- `VTRAC_STRAIGHT`: ordered VTRAC digit pattern equals the winner VTRAC pattern when a literal combo is available.
- `VTRAC_BOX`: VTRAC index/family equals the winner VTRAC index.

## 3. Current Coverage Limits

- Broad flags such as due-double support, blackapple support, survivor support, and profit-alert support are retained as context unless exact/canonical value lists are available.
- Frontier evidence is post-result explanatory evidence in this audit; it is not counted as a live pre-draw firing source unless future tooling exports pre-draw frontier candidates.
- Family labels that are not canonical digits are not force-matched; they need a separate family parser if we want them credited directly.
- Stage 2 should add a full exposure/false-positive ledger for emitted signals that did not match winners.

## 4. Generated Outputs

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.md`
