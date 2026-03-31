# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Winner-event denominator: `138`
- Credited-hit denominator: `94`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `52/138` (37.7%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `48/138` (34.8%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `11/138` (8.0%)
- Explicit arena box / exact signals: `10` / `3`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `76/94` (80.9%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `32/94` (34.0%)
- Straight hits with finalist support: `16/18` (88.9%)
- Strict box hits with finalist support: `10/12` (83.3%)
- Hits with box-like arena support: `10/94` (10.6%)
- Hits with VT-like arena support: `43/94` (45.7%)
- Finalist signature buckets: `CLEAR_ARENA_FINALIST` x3, `CONTROL_ARM_ONLY_CATCH` x18, `LIGHT_ARENA_FINALIST` x44, `PARTIAL_ARENA_FINALIST` x29

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 18 | 83.3% | 44.4% | 16.7% | 55.6% |
| `STRAIGHT` | 18 | 88.9% | 66.7% | 38.9% | 61.1% |
| `VTRAC_ONLY` | 58 | 77.6% | 20.7% | 0.0% | 37.9% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `5/138` (3.6%)
- Gap rows with explicit arena box signal: `5/5` (100.0%)
- Gap rows with sandbox box seed: `4/5` (80.0%)
- Gap rows ranked top5: `2/5` (40.0%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x8, `FEEDER_TO_FRONTIER` x37, `HIDDEN_COMPRESSED_FRONTIER` x48, `LITERAL_FRONTIER` x1, `VTRAC_FRONTIER` x44
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2026-01-09` `Connecticut4` `Midday` winner `234` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-06` `Connecticut4` `Midday` winner `576` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-08` `Connecticut4` `Evening` winner `331` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-06` `Delaware4` `Midday` winner `165` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-09` `Delaware4` `Midday` winner `843` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-09` `Delaware4` `Evening` winner `681` rank=`2` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-05` `Florida4` `Midday` winner `080` rank=`3` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`False`
  - `2026-01-07` `Florida4` `Evening` winner `963` rank=`3` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
- Opportunity-gap examples:
  - `2026-01-05` `Connecticut4` `Midday` winner `071` rank=`1` arena_box=`True` sandbox_box=`True`
  - `2026-01-07` `Florida4` `Evening` winner `963` rank=`3` arena_box=`True` sandbox_box=`False`
  - `2026-01-08` `Ohio4` `Evening` winner `580` rank=`9` arena_box=`True` sandbox_box=`True`
  - `2026-01-09` `Pennsylvania4` `Midday` winner `811` rank=`11` arena_box=`True` sandbox_box=`True`
  - `2026-01-09` `Pennsylvania4` `Evening` winner `014` rank=`11` arena_box=`True` sandbox_box=`True`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
