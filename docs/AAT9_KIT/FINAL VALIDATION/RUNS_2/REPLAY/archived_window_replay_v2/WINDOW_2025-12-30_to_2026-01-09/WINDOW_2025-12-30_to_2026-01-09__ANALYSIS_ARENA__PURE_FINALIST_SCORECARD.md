# Pure Arena Finalist / Candidate Scorecard

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Winner-event denominator: `301`
- Credited-hit denominator: `200`
- Performance ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`
- Hit roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__HIT_ROSTER.csv`

## 2. Event-Level Finalist Territory

- Any candidate-like arena evidence: `115/301` (38.2%)
- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `109/301` (36.2%)
- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `24/301` (8.0%)
- Explicit arena box / exact signals: `22` / `4`

## 3. Converted-Hit Arena Support

- Credited hits with non-control-arm finalist signature: `160/200` (80.0%)
- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `66/200` (33.0%)
- Straight hits with finalist support: `35/39` (89.7%)
- Strict box hits with finalist support: `18/21` (85.7%)
- Hits with box-like arena support: `23/200` (11.5%)
- Hits with VT-like arena support: `93/200` (46.5%)
- Finalist signature buckets: `CLEAR_ARENA_FINALIST` x3, `CONTROL_ARM_ONLY_CATCH` x40, `LIGHT_ARENA_FINALIST` x94, `PARTIAL_ARENA_FINALIST` x63

| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |
|---|---:|---:|---:|---:|---:|
| `CANONICAL_BOX` | 44 | 77.3% | 31.8% | 9.1% | 56.8% |
| `STRAIGHT` | 39 | 89.7% | 59.0% | 43.6% | 56.4% |
| `VTRAC_ONLY` | 117 | 77.8% | 24.8% | 1.7% | 39.3% |

## 4. Opportunity-Gap Box Layer

- Opportunity-gap box rows: `12/301` (4.0%)
- Gap rows with explicit arena box signal: `12/12` (100.0%)
- Gap rows with sandbox box seed: `9/12` (75.0%)
- Gap rows ranked top5: `2/12` (16.7%)

## 5. Frontier Corroboration

- Frontier signature mix: `FAMILY_FRONTIER` x16, `FEEDER_TO_FRONTIER` x86, `HIDDEN_COMPRESSED_FRONTIER` x110, `LITERAL_FRONTIER` x1, `VTRAC_FRONTIER` x88
- Frontier promotion themes: `Hidden compressed winner-family frontier`, `Feeder-to-frontier progression`, `Double-anchored frontier compression`

## 6. Notable Cases

- Candidate-supported hit examples:
  - `2025-12-30` `Connecticut4` `Midday` winner `095` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`True` vtlike=`True`
  - `2025-12-31` `Connecticut4` `Evening` winner `361` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-03` `Connecticut4` `Evening` winner `181` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-09` `Connecticut4` `Midday` winner `234` rank=`1` sig=`PARTIAL_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-04` `Connecticut4` `Midday` winner `569` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-04` `Connecticut4` `Evening` winner `311` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-06` `Connecticut4` `Midday` winner `576` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
  - `2026-01-08` `Connecticut4` `Evening` winner `331` rank=`1` sig=`LIGHT_ARENA_FINALIST` boxlike=`False` vtlike=`True`
- Opportunity-gap examples:
  - `2026-01-05` `Connecticut4` `Midday` winner `071` rank=`1` arena_box=`True` sandbox_box=`True`
  - `2026-01-07` `Florida4` `Evening` winner `963` rank=`3` arena_box=`True` sandbox_box=`False`
  - `2025-12-31` `NewYork4` `Evening` winner `116` rank=`7` arena_box=`True` sandbox_box=`True`
  - `2025-12-30` `NorthCarolina4` `Midday` winner `455` rank=`8` arena_box=`True` sandbox_box=`False`
  - `2026-01-01` `NorthCarolina4` `Evening` winner `053` rank=`8` arena_box=`True` sandbox_box=`True`

## 7. Practical Read

- The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
- Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
- The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.
