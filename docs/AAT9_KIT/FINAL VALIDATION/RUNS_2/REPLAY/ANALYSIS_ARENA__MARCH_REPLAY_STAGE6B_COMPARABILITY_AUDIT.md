# Analysis Arena March Replay Stage 6B Comparability Audit

## Guardrail

This audit is read-only. It diagnoses the March same-window replay Stage 6B zero-candidate-lane issue and does not change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Finding

The March same-window replay package is not a safe root-level Stage 6B metric baseline because it is an isolated single-window replay root. The Stage 3 through Stage 6B chain expects cross-window evidence for boxed candidate/support promotion. With only one window present, Stage 3 correctly labels most rows as `needs_more_windows`, so downstream Stage 4C, Stage 5, and Stage 6B have no boxed candidate/support/restraint lanes to score.

This means the zeroed Stage 6B candidate-lane metrics are a comparability mismatch, not evidence that the March window-close replay artifacts are unusable.

## Evidence

| root | Stage 3 registry rows | Stage 3 `promote_candidate` | Stage 3 `supporting_gate` | Stage 3 `needs_more_windows` | Stage 3 windows_seen profile | Stage 4 replay rows | Stage 4C lane shape | Stage 5 value rows | Stage 6B candidate-lane result |
| --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | --- |
| canonical `RUNS_2` | 4312 | 164 | 562 | 92 | mostly `5` | 5675 | candidate/support/restraint/decay lanes present | 14752 | nonzero candidate/support/restraint metrics |
| `REPLAY/march_2026_15day_replay_v2` | 4113 | 0 | 0 | 3451 | all `1` | 104 | only `decay_watch_only` | 2698 | boxed candidate/support/restraint lanes zeroed |
| `REPLAY/archived_window_replay_v2` | 4120 | 147 | 400 | 95 | mostly `3` | 3291 | candidate/support/restraint/decay lanes present | 7656 | nonzero candidate/support/restraint metrics |

## Interpretation

- The March replay folder remains useful for same-window replay of window-close surfaces.
- It should not be used as the official root-level Stage 6B metric baseline unless it is rebuilt as a corpus-mirrored replay root with enough windows to satisfy cross-window gates.
- The canonical `RUNS_2` Stage 6B stack remains the valid March-side metric source for March-vs-archived readback.
- The archived replay v2 package remains a valid stress-test package because it contains multiple clean replay windows and therefore satisfies the cross-window promotion structure.

## Recommended Handling

1. Do not treat the isolated March replay Stage 6B zero lanes as random corruption.
2. Keep the isolated March replay package for window-close artifact replay and traceability checks.
3. If an official same-window root-level Stage 6B replay baseline is required, build a corpus-mirrored replay root that includes enough replay windows to preserve cross-window promotion behavior.
4. For current Stage 8 readiness decisions, continue using canonical March `RUNS_2` vs archived replay v2, then require a true fresh-window Stage 6B-through-Stage 7B comparison before any downstream rewrite.
