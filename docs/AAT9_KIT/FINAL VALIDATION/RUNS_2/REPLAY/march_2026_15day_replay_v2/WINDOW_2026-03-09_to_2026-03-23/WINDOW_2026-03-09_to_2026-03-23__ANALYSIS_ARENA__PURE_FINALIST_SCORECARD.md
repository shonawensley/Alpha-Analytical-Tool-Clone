# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`
- Winner-event denominator: `414`
- Credited-hit denominator: `274`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `168/414` (40.6%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `162/414` (39.1%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `40/414` (9.7%)
- Explicit arena box / exact signals: `35` / `9`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `229/274` (83.6%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `118/274` (43.1%)
- Straight hits with finalist support: `46/54` (85.2%)
- Strict box hits with finalist support: `24/29` (82.8%)
- Hits with box-like arena support: `38/274` (13.9%)
- Hits with VT-like arena support: `141/274` (51.5%)
- Finalist signature buckets: `CLEAR_ARENA_FINALIST` x3, `CONTROL_ARM_ONLY_CATCH` x45, `LIGHT_ARENA_FINALIST` x111, `PARTIAL_ARENA_FINALIST` x115

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 73 | 87.7% | 49.3% | 16.4% | 57.5% |
| `STRAIGHT` | 54 | 85.2% | 50.0% | 37.0% | 57.4% |
| `VTRAC_ONLY` | 147 | 81.0% | 37.4% | 4.1% | 46.3% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `21/414` (5.1%)
- Gap rows with explicit arena box signal: `21/21` (100.0%)
- Gap rows with sandbox box seed: `15/21` (71.4%)
- Gap rows ranked top5: `8/21` (38.1%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x21, `FEEDER_TO_FRONTIER` x132, `HIDDEN_COMPRESSED_FRONTIER` x156, `LITERAL_FRONTIER` x2, `VTRAC_FRONTIER` x103
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2026-03-09` `Connecticut4` `Evening` winner `091` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2026-03-10` `Connecticut4` `Evening` winner `556` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-18` `Connecticut4` `Midday` winner `848` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-19` `Connecticut4` `Midday` winner `699` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-21` `Connecticut4` `Midday` winner `954` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-12` `Connecticut4` `Evening` winner `802` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-13` `Connecticut4` `Midday` winner `404` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-03-17` `Connecticut4` `Midday` winner `991` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2026-03-09` `Connecticut4` `Evening` winner `091` rank=`1` arena_box=`True` sandbox_box=`True`
  - `2026-03-11` `Florida4` `Midday` winner `700` rank=`3` arena_box=`True` sandbox_box=`True`
  - `2026-03-23` `Florida4` `Midday` winner `196` rank=`3` arena_box=`True` sandbox_box=`False`
  - `2026-03-10` `Indiana4` `Evening` winner `070` rank=`4` arena_box=`True` sandbox_box=`True`
  - `2026-03-14` `Indiana4` `Midday` winner `080` rank=`4` arena_box=`True` sandbox_box=`True`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
