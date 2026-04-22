# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Winner-event denominator: `84`
- Credited-hit denominator: `63`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `32/84` (38.1%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `31/84` (36.9%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `5/84` (6.0%)
- Explicit arena box / exact signals: `4` / `1`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `50/63` (79.4%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `17/63` (27.0%)
- Straight hits with finalist support: `9/13` (69.2%)
- Strict box hits with finalist support: `3/5` (60.0%)
- Hits with box-like arena support: `5/63` (7.9%)
- Hits with VT-like arena support: `27/63` (42.9%)
- Finalist signature buckets: `CONTROL_ARM_ONLY_CATCH` x13, `LIGHT_ARENA_FINALIST` x33, `PARTIAL_ARENA_FINALIST` x17

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 15 | 73.3% | 20.0% | 6.7% | 26.7% |
| `STRAIGHT` | 13 | 69.2% | 61.5% | 30.8% | 61.5% |
| `VTRAC_ONLY` | 35 | 85.7% | 17.1% | 0.0% | 42.9% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `2/84` (2.4%)
- Gap rows with explicit arena box signal: `2/2` (100.0%)
- Gap rows with sandbox box seed: `1/2` (50.0%)
- Gap rows ranked top5: `0/2` (0.0%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x5, `FEEDER_TO_FRONTIER` x30, `HIDDEN_COMPRESSED_FRONTIER` x28, `VTRAC_FRONTIER` x21
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2026-01-22` `Connecticut4` `Midday` winner `556` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-20` `Delaware4` `Midday` winner `099` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-21` `Delaware4` `Midday` winner `029` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-21` `Florida4` `Midday` winner `350` rank=`3` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-20` `Indiana4` `Evening` winner `208` rank=`4` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-22` `Indiana4` `Evening` winner `757` rank=`4` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-21` `Indiana4` `Midday` winner `458` rank=`4` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-22` `Indiana4` `Midday` winner `286` rank=`4` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2026-01-21` `NorthCarolina4` `Evening` winner `577` rank=`8` arena_box=`True` sandbox_box=`False`
  - `2026-01-22` `Virginia4` `Evening` winner `100` rank=`14` arena_box=`True` sandbox_box=`True`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
