# Analysis Arena Evidence Utilization Audit

Purpose: measure whether March-window winner evidence was captured, promoted, converted, underused, or only present as broad context.

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- Winner events audited: `414`
- Utilization ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- Signal attribution ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- Case dossiers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- Translator redesign memo: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`

## 2. Evidence Status Counts

- CAPTURED_BUT_NOT_PROMOTED: `125` (30.2%)
- DECAY_VALIDATED: `103` (24.9%)
- CAPTURED_AND_USED: `97` (23.4%)
- CAPTURED_BUT_WRONG_LANE: `66` (15.9%)
- CAPTURED_BUT_UNDERUSED: `23` (5.6%)

## 3. Outcome Class Counts

- VTRAC_ONLY: `141` (34.1%)
- NO_CONVERSION: `138` (33.3%)
- BOX_ANY: `61` (14.7%)
- STRAIGHT: `51` (12.3%)
- BOX_GAP: `21` (5.1%)
- EXACT_GAP: `2` (0.5%)

## 4. Core Reads

- Captured-and-used events: `97`.
- Captured-but-underused events: `23`.
- Captured-but-not-promoted events: `125`.
- Captured-but-wrong-lane events: `66`.
- Decay-validated events: `103`.
- Broad-context-only events: `0`.
- Not-captured events in current machine-readable audit sources: `0`.
- Pre-draw winner-aligned attribution rows: `10990`.
- Post-result explanatory frontier/decay attribution rows: `2569`.

## 5. Interpretation

- The audit separates `FIRED`, `ALIGNED`, `PROMOTED`, and `CONVERTED`; a tracked signal is not automatically a final decision signal.
- Box-gap and exact-gap rows are treated as high-value translator training cases, not ordinary misses.
- Broad support flags remain visible, but they are downgraded unless paired with sharper exact/box/frontier/decay evidence.
- Brain2 ranking is included as context, but static rank behavior must still be checked before treating top-primary as dynamic proof.

## 6. Files Generated

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.json`
