# Analysis Arena Evidence Utilization Audit

Purpose: measure whether March-window winner evidence was captured, promoted, converted, underused, or only present as broad context.

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18`
- Winner events audited: `109`
- Utilization ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- Signal attribution ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- Case dossiers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- Translator redesign memo: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`

## 2. Evidence Status Counts

- CAPTURED_AND_USED: `30` (27.5%)
- DECAY_VALIDATED: `30` (27.5%)
- CAPTURED_BUT_NOT_PROMOTED: `23` (21.1%)
- CAPTURED_BUT_WRONG_LANE: `22` (20.2%)
- CAPTURED_BUT_UNDERUSED: `4` (3.7%)

## 3. Outcome Class Counts

- VTRAC_ONLY: `42` (38.5%)
- NO_CONVERSION: `30` (27.5%)
- BOX_ANY: `18` (16.5%)
- STRAIGHT: `15` (13.8%)
- BOX_GAP: `4` (3.7%)

## 4. Core Reads

- Captured-and-used events: `30`.
- Captured-but-underused events: `4`.
- Captured-but-not-promoted events: `23`.
- Captured-but-wrong-lane events: `22`.
- Decay-validated events: `30`.
- Broad-context-only events: `0`.
- Not-captured events in current machine-readable audit sources: `0`.
- Pre-draw winner-aligned attribution rows: `2743`.
- Post-result explanatory frontier/decay attribution rows: `690`.

## 5. Interpretation

- The audit separates `FIRED`, `ALIGNED`, `PROMOTED`, and `CONVERTED`; a tracked signal is not automatically a final decision signal.
- Box-gap and exact-gap rows are treated as high-value translator training cases, not ordinary misses.
- Broad support flags remain visible, but they are downgraded unless paired with sharper exact/box/frontier/decay evidence.
- Brain2 ranking is included as context, but static rank behavior must still be checked before treating top-primary as dynamic proof.

## 6. Files Generated

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.json`
