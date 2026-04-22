# Stage 2 Audit Interpretation

Purpose: interpret signal exposure denominators before scoring or translator promotion.

## Executive Read

- Stage 2 confirms the right next discipline: separate evidence visibility from exposure burden.
- Broad control-arm and VTRAC signals can be valuable territory without being safe direct promotion signals.
- Fixture candidates should now be reviewed against false-positive proxy burden before any weighting experiment.

## Denominators

- Seed state-days audited: `42`
- Winner events: `84`
- Signal exposure rows: `42685`
- Scorecard source rows: `88`
- Translator fixture candidate rows: `46`

## Decision Counts

- `boxed_context_or_negative_control`: `45`
- `boxed_supporting_gate`: `18`
- `straight_context_or_negative_control`: `15`
- `vtrac_context_only`: `5`
- `vtrac_watch_decay_only_until_box_pairing`: `2`
- `sample_too_small`: `2`
- `denominator_only_broad_control`: `1`

## Lane Read

- `straight` lane: exposure rows `22442`, lane-hit rate `0.1%`.
- `boxed` lane: exposure rows `17898`, lane-hit rate `0.7%`.
- `vtrac` lane: exposure rows `2345`, lane-hit rate `5.4%`.

## Recommended Next Actions

1. Review `boxed_fixture_candidate` and `straight_fixture_candidate` sources against the 23 gap teachers.
2. Keep `boxed_supporting_gate` and `straight_supporting_gate` as pair/gate candidates, not standalone weights.
3. Keep VTRAC decisions in watch/decay mode until a boxed or exact source confirms the lane.
4. Treat broad control-arm sources as denominator controls and negative-control surfaces.
5. Run the same Stage 2 generator on older windows before locking any permanent scoring weights.

## Warnings

- No missing-control-artifact warnings.
