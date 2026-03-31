# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Winner-event denominator: `163`
- Credited-hit denominator: `103`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `64/163` (39.3%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `61/163` (37.4%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `14/163` (8.6%)
- Explicit arena box / exact signals: `11` / `1`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `81/103` (78.6%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `32/103` (31.1%)
- Straight hits with finalist support: `19/20` (95.0%)
- Strict box hits with finalist support: `10/10` (100.0%)
- Hits with box-like arena support: `14/103` (13.6%)
- Hits with VT-like arena support: `50/103` (48.5%)
- Finalist signature buckets: `CONTROL_ARM_ONLY_CATCH` x22, `LIGHT_ARENA_FINALIST` x49, `PARTIAL_ARENA_FINALIST` x32

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 26 | 69.2% | 26.9% | 7.7% | 50.0% |
| `STRAIGHT` | 20 | 95.0% | 45.0% | 55.0% | 60.0% |
| `VTRAC_ONLY` | 57 | 77.2% | 28.1% | 1.8% | 43.9% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `5/163` (3.1%)
- Gap rows with explicit arena box signal: `5/5` (100.0%)
- Gap rows with sandbox box seed: `2/5` (40.0%)
- Gap rows ranked top5: `0/5` (0.0%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x8, `FEEDER_TO_FRONTIER` x49, `HIDDEN_COMPRESSED_FRONTIER` x62, `VTRAC_FRONTIER` x44
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2025-12-30` `Connecticut4` `Midday` winner `095` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2025-12-31` `Connecticut4` `Evening` winner `361` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-02` `Connecticut4` `Midday` winner `970` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-03` `Connecticut4` `Evening` winner `181` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-04` `Connecticut4` `Midday` winner `569` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-04` `Connecticut4` `Evening` winner `311` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2025-12-30` `Delaware4` `Midday` winner `706` rank=`2` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-01` `Delaware4` `Midday` winner `149` rank=`2` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2025-12-31` `NewYork4` `Evening` winner `116` rank=`7` arena_box=`True` sandbox_box=`False`
  - `2025-12-30` `NorthCarolina4` `Midday` winner `455` rank=`8` arena_box=`True` sandbox_box=`False`
  - `2026-01-01` `NorthCarolina4` `Evening` winner `053` rank=`8` arena_box=`True` sandbox_box=`True`
  - `2025-12-30` `Pennsylvania4` `Evening` winner `173` rank=`11` arena_box=`True` sandbox_box=`True`
  - `2026-01-03` `SouthCarolina4` `Midday` winner `189` rank=`13` arena_box=`True` sandbox_box=`False`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
