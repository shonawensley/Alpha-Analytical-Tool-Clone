# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18`
- Winner-event denominator: `109`
- Credited-hit denominator: `79`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `50/109` (45.9%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `46/109` (42.2%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `12/109` (11.0%)
- Explicit arena box / exact signals: `12` / `3`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `65/79` (82.3%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `31/79` (39.2%)
- Straight hits with finalist support: `16/16` (100.0%)
- Strict box hits with finalist support: `11/11` (100.0%)
- Hits with box-like arena support: `12/79` (15.2%)
- Hits with VT-like arena support: `41/79` (51.9%)
- Finalist signature buckets: `CLEAR_ARENA_FINALIST` x3, `CONTROL_ARM_ONLY_CATCH` x14, `LIGHT_ARENA_FINALIST` x34, `PARTIAL_ARENA_FINALIST` x28

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 21 | 95.2% | 33.3% | 14.3% | 57.1% |
| `STRAIGHT` | 16 | 100.0% | 56.2% | 56.2% | 68.8% |
| `VTRAC_ONLY` | 42 | 69.0% | 35.7% | 0.0% | 42.9% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `4/109` (3.7%)
- Gap rows with explicit arena box signal: `4/4` (100.0%)
- Gap rows with sandbox box seed: `2/4` (50.0%)
- Gap rows ranked top5: `2/4` (50.0%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x4, `FEEDER_TO_FRONTIER` x26, `HIDDEN_COMPRESSED_FRONTIER` x50, `VTRAC_FRONTIER` x28
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2026-01-18` `Connecticut4` `Midday` winner `238` rank=`1` sig=`CLEAR_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2026-01-18` `Connecticut4` `Evening` winner `781` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-15` `Connecticut4` `Midday` winner `495` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-16` `Connecticut4` `Evening` winner `431` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`True` vtlike=`False`
  - `2026-01-16` `Delaware4` `Evening` winner `107` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2026-01-16` `Delaware4` `Midday` winner `902` rank=`2` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-17` `Delaware4` `Midday` winner `126` rank=`2` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-18` `Delaware4` `Midday` winner `490` rank=`2` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2026-01-16` `Connecticut4` `Evening` winner `431` rank=`1` arena_box=`True` sandbox_box=`True`
  - `2026-01-16` `Delaware4` `Evening` winner `107` rank=`2` arena_box=`True` sandbox_box=`True`
  - `2026-01-18` `NewJersey4` `Evening` winner `955` rank=`6` arena_box=`True` sandbox_box=`False`
  - `2026-01-15` `NorthCarolina4` `Midday` winner `045` rank=`8` arena_box=`True` sandbox_box=`False`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
