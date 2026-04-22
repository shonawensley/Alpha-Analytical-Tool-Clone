# Stage 2 Audit Interpretation

Purpose: interpret signal exposure denominators before scoring or translator promotion.

## Executive Read

- Stage 2 confirms the right next discipline: separate evidence visibility from exposure burden.
- Broad control-arm and VTRAC signals can be valuable territory without being safe direct promotion signals.
- Fixture candidates should now be reviewed against false-positive proxy burden before any weighting experiment.

## Denominators

- Seed state-days audited: `154`
- Winner events: `301`
- Signal exposure rows: `156360`
- Scorecard source rows: `88`
- Translator fixture candidate rows: `56`

## Decision Counts

- `boxed_context_or_negative_control`: `52`
- `straight_context_or_negative_control`: `15`
- `boxed_supporting_gate`: `12`
- `vtrac_context_only`: `6`
- `vtrac_watch_decay_only_until_box_pairing`: `1`
- `sample_too_small`: `1`
- `denominator_only_broad_control`: `1`

## Lane Read

- `straight` lane: exposure rows `81706`, lane-hit rate `0.2%`.
- `boxed` lane: exposure rows `65546`, lane-hit rate `0.8%`.
- `vtrac` lane: exposure rows `9108`, lane-hit rate `4.9%`.

## Recommended Next Actions

1. Review `boxed_fixture_candidate` and `straight_fixture_candidate` sources against the 23 gap teachers.
2. Keep `boxed_supporting_gate` and `straight_supporting_gate` as pair/gate candidates, not standalone weights.
3. Keep VTRAC decisions in watch/decay mode until a boxed or exact source confirms the lane.
4. Treat broad control-arm sources as denominator controls and negative-control surfaces.
5. Run the same Stage 2 generator on older windows before locking any permanent scoring weights.

## Warnings

- No missing-control-artifact warnings.
