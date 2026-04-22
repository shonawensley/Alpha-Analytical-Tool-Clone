# Analysis Arena Evidence Utilization Audit

Purpose: measure whether March-window winner evidence was captured, promoted, converted, underused, or only present as broad context.

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Winner events audited: `84`
- Utilization ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- Signal attribution ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- Case dossiers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- Translator redesign memo: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`

## 2. Evidence Status Counts

- CAPTURED_BUT_NOT_PROMOTED: `25` (29.8%)
- CAPTURED_AND_USED: `23` (27.4%)
- DECAY_VALIDATED: `19` (22.6%)
- CAPTURED_BUT_WRONG_LANE: `15` (17.9%)
- CAPTURED_BUT_UNDERUSED: `2` (2.4%)

## 3. Outcome Class Counts

- VTRAC_ONLY: `35` (41.7%)
- NO_CONVERSION: `21` (25.0%)
- BOX_ANY: `14` (16.7%)
- STRAIGHT: `12` (14.3%)
- BOX_GAP: `2` (2.4%)

## 4. Core Reads

- Captured-and-used events: `23`.
- Captured-but-underused events: `2`.
- Captured-but-not-promoted events: `25`.
- Captured-but-wrong-lane events: `15`.
- Decay-validated events: `19`.
- Broad-context-only events: `0`.
- Not-captured events in current machine-readable audit sources: `0`.
- Pre-draw winner-aligned attribution rows: `2170`.
- Post-result explanatory frontier/decay attribution rows: `519`.

## 5. Interpretation

- The audit separates `FIRED`, `ALIGNED`, `PROMOTED`, and `CONVERTED`; a tracked signal is not automatically a final decision signal.
- Box-gap and exact-gap rows are treated as high-value translator training cases, not ordinary misses.
- Broad support flags remain visible, but they are downgraded unless paired with sharper exact/box/frontier/decay evidence.
- Brain2 ranking is included as context, but static rank behavior must still be checked before treating top-primary as dynamic proof.

## 6. Files Generated

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__CASE_DOSSIERS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__TRANSLATOR_REDESIGN_LESSONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_AUDIT.json`
