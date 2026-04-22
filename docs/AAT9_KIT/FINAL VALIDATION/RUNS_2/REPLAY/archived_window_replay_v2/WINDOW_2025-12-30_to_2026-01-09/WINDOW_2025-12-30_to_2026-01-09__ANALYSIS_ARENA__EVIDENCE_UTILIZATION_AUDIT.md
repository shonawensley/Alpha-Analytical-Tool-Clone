# Analysis Arena Evidence Utilization Audit

Purpose: measure whether March-window winner evidence was captured, promoted, converted, underused, or only present as broad context.

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Winner events audited: `301`
- Utilization ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- Signal attribution ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- Case dossiers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- Translator redesign memo: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`

## 2. Evidence Status Counts

- DECAY_VALIDATED: `94` (31.2%)
- CAPTURED_BUT_NOT_PROMOTED: `81` (26.9%)
- CAPTURED_AND_USED: `63` (20.9%)
- CAPTURED_BUT_WRONG_LANE: `51` (16.9%)
- CAPTURED_BUT_UNDERUSED: `12` (4.0%)

## 3. Outcome Class Counts

- VTRAC_ONLY: `115` (38.2%)
- NO_CONVERSION: `100` (33.2%)
- BOX_ANY: `40` (13.3%)
- STRAIGHT: `34` (11.3%)
- BOX_GAP: `12` (4.0%)

## 4. Core Reads

- Captured-and-used events: `63`.
- Captured-but-underused events: `12`.
- Captured-but-not-promoted events: `81`.
- Captured-but-wrong-lane events: `51`.
- Decay-validated events: `94`.
- Broad-context-only events: `0`.
- Not-captured events in current machine-readable audit sources: `0`.
- Pre-draw winner-aligned attribution rows: `7400`.
- Post-result explanatory frontier/decay attribution rows: `1856`.

## 5. Interpretation

- The audit separates `FIRED`, `ALIGNED`, `PROMOTED`, and `CONVERTED`; a tracked signal is not automatically a final decision signal.
- Box-gap and exact-gap rows are treated as high-value translator training cases, not ordinary misses.
- Broad support flags remain visible, but they are downgraded unless paired with sharper exact/box/frontier/decay evidence.
- Brain2 ranking is included as context, but static rank behavior must still be checked before treating top-primary as dynamic proof.

## 6. Files Generated

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.json`
