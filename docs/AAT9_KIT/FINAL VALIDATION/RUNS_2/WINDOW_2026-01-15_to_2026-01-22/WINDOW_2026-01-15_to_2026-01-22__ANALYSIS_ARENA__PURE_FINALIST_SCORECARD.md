# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Winner-event denominator: `221`
- Credited-hit denominator: `142`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `90/221` (40.7%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `85/221` (38.5%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `20/221` (9.0%)
- Explicit arena box / exact signals: `19` / `2`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `118/142` (83.1%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `48/142` (33.8%)
- Straight hits with finalist support: `27/30` (90.0%)
- Strict box hits with finalist support: `11/12` (91.7%)
- Hits with box-like arena support: `19/142` (13.4%)
- Hits with VT-like arena support: `69/142` (48.6%)
- Finalist signature buckets: `CLEAR_ARENA_FINALIST` x4, `CONTROL_ARM_ONLY_CATCH` x24, `LIGHT_ARENA_FINALIST` x70, `PARTIAL_ARENA_FINALIST` x44

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 39 | 79.5% | 28.2% | 10.3% | 38.5% |
| `STRAIGHT` | 30 | 90.0% | 53.3% | 40.0% | 66.7% |
| `VTRAC_ONLY` | 73 | 82.2% | 28.8% | 4.1% | 46.6% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `11/221` (5.0%)
- Gap rows with explicit arena box signal: `11/11` (100.0%)
- Gap rows with sandbox box seed: `7/11` (63.6%)
- Gap rows ranked top5: `3/11` (27.3%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x10, `FEEDER_TO_FRONTIER` x65, `HIDDEN_COMPRESSED_FRONTIER` x91, `VTRAC_FRONTIER` x54
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2026-01-18` `Connecticut4` `Midday` winner `238` rank=`1` sig=`CLEAR_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2026-01-18` `Connecticut4` `Evening` winner `781` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-15` `Connecticut4` `Midday` winner `495` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-16` `Connecticut4` `Evening` winner `431` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`True` vtlike=`False`
  - `2026-01-22` `Connecticut4` `Midday` winner `556` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-16` `Delaware4` `Evening` winner `107` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2026-01-20` `Delaware4` `Midday` winner `099` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-21` `Delaware4` `Midday` winner `029` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2026-01-16` `Connecticut4` `Evening` winner `431` rank=`1` arena_box=`True` sandbox_box=`True`
  - `2026-01-16` `Delaware4` `Evening` winner `107` rank=`2` arena_box=`True` sandbox_box=`True`
  - `2026-01-19` `Michigan4` `Evening` winner `402` rank=`5` arena_box=`True` sandbox_box=`True`
  - `2026-01-16` `NewJersey4` `Evening` winner `180` rank=`6` arena_box=`True` sandbox_box=`True`
  - `2026-01-18` `NewJersey4` `Evening` winner `955` rank=`6` arena_box=`True` sandbox_box=`False`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
