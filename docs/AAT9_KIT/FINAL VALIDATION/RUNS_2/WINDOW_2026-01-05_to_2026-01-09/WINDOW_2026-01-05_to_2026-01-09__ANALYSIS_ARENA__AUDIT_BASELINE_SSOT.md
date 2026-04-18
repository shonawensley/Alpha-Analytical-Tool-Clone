# Analysis Arena Audit Baseline SSOT

Purpose: freeze the authoritative March/window audit package before Stage 2 is used as a teaching baseline.

## Authoritative Counts

- Winner events: `0`
- Winner signal attribution rows: `0`
- Stage 2 exposure rows: `71030`
- Stage 2 scorecard source rows: `88`

Evidence status counts:

Outcome class counts:

## Metric Map

- `Arena truth` [headline]: Measures whether Analysis Arena preserved winner territory/evidence.
- `Stage 2 exposure` [headline]: Measures denominator and false-positive proxy burden for signals before scoring changes.
- `Brain2 ranking` [diagnostic]: Evaluates rank/static-board behavior; should not be treated as pure Arena weakness.
- `Old control-arm conversion` [diagnostic]: Grades how old CU/play-card infrastructure expressed Arena-era evidence.
- `Translator opportunity` [teaching-only]: Finds gap/wrong-lane/decay fixtures; not a raw performance scoreboard.
- `Decay/carryforward` [diagnostic]: Measures short-horizon resolution separately from same-day scoring.

## Authoritative Files

- `performance_gap_ledger` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv` exists=`yes` rows=`138`
- `evidence_utilization_ledger` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv` exists=`no` rows=`0`
- `evidence_utilization_audit` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.json` exists=`no` rows=`0`
- `winner_signal_attribution_ledger` [teaching]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv` exists=`no` rows=`0`
- `audit_interpretation_pass` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json` exists=`no` rows=`0`
- `priority_cases` [teaching]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv` exists=`no` rows=`0`
- `signal_decisions` [teaching]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv` exists=`no` rows=`0`
- `decay_scorecard` [diagnostic]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.json` exists=`yes` rows=`70`
- `frontier_analysis` [diagnostic]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json` exists=`yes` rows=`138`
- `stage2_signal_exposure_ledger` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_SIGNAL_EXPOSURE_LEDGER.csv` exists=`no` rows=`71030`
- `stage2_false_positive_scorecard` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json` exists=`no` rows=`88`
- `stage2_promotion_decision_matrix` [teaching]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_SIGNAL_PROMOTION_DECISION_MATRIX.csv` exists=`no` rows=`88`
- `stage2_lane_sharpness_report` [diagnostic]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_LANE_SHARPNESS_REPORT.md` exists=`no` rows=`0`
- `stage2_translator_fixture_candidates` [teaching]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_TRANSLATOR_FIXTURE_CANDIDATES.csv` exists=`no` rows=`0`
- `stage2_audit_interpretation` [headline]: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__STAGE2_AUDIT_INTERPRETATION.json` exists=`no` rows=`0`

## Supersession Rule

- Intermediate conversation/log counts are not the SSOT. Use the regenerated files listed here.
- Teaching-only metrics should not be read as raw system performance.
- Stage 2 denominators are required before any new scoring or budget promotion.

## PRO Feedback Integration

- Integrated governance/context from `tasks/PRO_92.txt`
- Integrated governance/context from `tasks/PRO_93.txt`
