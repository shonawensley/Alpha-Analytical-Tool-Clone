# B36 Strategy — Doubles / Mirror‑Doubles Closure (v1)

This document specifies the **additive** B36 play-card strategy:

- Strategy ids:
  - `v0_3_b36_doubles_closure_v1` (aggressive doubles-first closure)
  - `v0_3_b36_doubles_closure_v2` (mixed: preserves singles when depth≥4; evidence-first when depth=1)
- Implemented in: `scripts/tools/create_play_card.py`
- Profile intent: `tool_only` + `stable10`

Purpose (plain English)
---
We often **touch the right VTRAC index (“lane hit”)** but miss the **winner’s canonical** inside that lane when the lane is treated as a shallow tail (often 1 line).

This strategy keeps the **same lane chooser + geometry** as the promoted v0.3 B36 policy, but changes **what we buy inside a lane** so that when we spend any lines in a lane, we spend them in a way that is more likely to convert to canonicals (especially doubles).

Non‑goals (v1)
---
- Not a Superbrian rewrite.
- Does **not** change analyzers (Stable / VTRAC / Hot Zones / Digit Reduction).
- Does **not** change lane ranking / lane breadth (that’s a separate allocator problem).
- Does **not** reintegrate Profit Alerts (still quarantined).

Invariants (what stays the same)
---
This strategy intentionally preserves the existing v0.3 B36 posture:

- Lane chooser: identical to the promoted policy (`methods_first` spine + tail spread + XLens injection methods@18 + packs@22).
- Geometry: `spinecap6 + taper6644`:
  - Spine (top 4 indices): caps = `6 / 6 / 4 / 4`
  - Tail (next indices): `1 line per index` until the `B36` budget is filled
- Tail depth: remains `1` line (v1 is “depth inside lanes” without buying depth by dropping lanes).

What changes (the conversion rule)
---
Inside each touched VTRAC index, we pick members using **bounded closure order**:

### A) Doubles‑bearing indices (6 members)
If the index has doubles in `modules/vtrac_reference.VTRAC_DISPLAY`:
- Buy **doubles first** (up to the per‑index cap for that index).
- If the cap still has room, buy **singles next**, ranked by evidence where possible.

### B) No‑doubles indices (8 members)
If the index has no doubles:
- Prefer **mirror pairs** (digit mirroring = VTRAC pairing rule: `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`).
- Under a 4‑line cap, this means **2 mirror pairs** (4 canonicals).
- If a lane is only given 1 line (tail), we take the best single for that lane by evidence (since we cannot buy a full pair with 1 line).

Explainability: “closure trace”
---
When this strategy is used, the emitted play card includes a small audit trace:

- Path: `play_card*.json` → `strategies["v0_3_b36_doubles_closure_v1"]["B36"]["vtrac_pack"]["closure_trace"]`
- (Same path for v2, just swap the strategy id key.)
- Each entry records:
  - `phase`: `spine` or `tail`
  - `index`: VTRAC numeric index
  - `want`: how many lines were allocated to that index
  - `chosen`: the member(s) selected from that index
  - `chosen_reasons`: why each member was selected (`double`, `mirror_pair`, `single`, etc.)

How to run (repro)
---
### 1) Regenerate play cards (adds the strategy into existing `play_card__tool_only__stable10.json`)

```bash
python3 scripts/tools/create_play_card.py \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --experiment-tag stable10 \
  --input-experiment-tag stable10 \
  --date 2026-01-04 \
  --force
```

### 2) Grade play cards against results (writes into `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`)

```bash
python3 scripts/tools/grade_play_card.py \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --experiment-tag stable10 \
  --date 2026-01-04 \
  --force
```

### 3) Build ladder + scoreboard comparisons (Jan window + OOS)

OOS window (`2026-01-01..2026-01-09`):

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-01 --date-to 2026-01-09 \
  --profile tool_only --experiment-tag stable10 \
  --strategy v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22 \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-01 --date-to 2026-01-09 \
  --profile tool_only --experiment-tag stable10 \
  --strategy v0_3_b36_doubles_closure_v1 \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

Jan gold window (`2026-01-15..2026-01-22`):

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-15 --date-to 2026-01-22 \
  --profile tool_only --experiment-tag stable10 \
  --strategy v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22 \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

```bash
python3 scripts/tools/create_conversion_ladder_report.py \
  --date-from 2026-01-15 --date-to 2026-01-22 \
  --profile tool_only --experiment-tag stable10 \
  --strategy v0_3_b36_doubles_closure_v1 \
  --write-casebook --casebook-budget B36 --casebook-n 5
```

Then build the side-by-side scoreboard:

```bash
python3 scripts/tools/create_conversion_scoreboard.py \
  --date-from 2026-01-01 --date-to 2026-01-09 \
  --profile tool_only --experiment-tag stable10 \
  --strategies v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22,v0_3_b36_doubles_closure_v1 \
  --budgets B36
```

(Repeat the scoreboard command for the Jan window range.)
