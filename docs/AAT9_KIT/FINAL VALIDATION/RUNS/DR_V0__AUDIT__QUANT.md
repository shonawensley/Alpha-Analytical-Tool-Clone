# Digit Reduction — v0 Audit (Quantitative)

Purpose: quantify whether **Digit Reduction (DR)**, as currently consumed in the *prediction layers* (Candidate Universe / Play Cards), behaves like:

- a **primary caller** (it directly produces winners at meaningful rates), or
- a **supporting corroborator** / **environment lens** (it contains useful structure, but not as “top picks”).

This is an audit of *consumption*, not a tuning of the DR analyzer.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`

Non‑negotiables (v0 synthesis sprint):
- No analyzer edits (Stable/DR/VTRAC/HZ).
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Inputs

- Aggregated results: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.csv`
- Window: `2026-01-05` → `2026-01-09`
- States: 14 tracked
- Outcomes: Midday + Evening (Combined excluded as an outcome)

Expected opportunities:
- 14 states × 5 days × 2 outcomes = 140
- Observed measured opportunities in this window = **138** (2 missing winners; expected in early v0 windows)

---

## What “DR” means in this quant audit

This refers specifically to how Candidate Universe currently ingests DR:

- Source file: `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
- Pack type: `method_id=digit_reduction_analyzer_v2`
- Default selection: top‑N per variant (`--top-n-dr`, default 3)
- Current play mode: `STRAIGHT` (no BOX expansion)

If DR is valuable but being consumed wrong, we should expect:
- low/zero direct hits (as “top 3 straights”), but
- strong “trace coverage” in post‑results overlays (handled in the case audit).

---

## Results snapshot (tool_only, 2026‑01‑05..09)

From `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.csv`:

| method_id | opps | hit_any | hit_any_rate | index_hit |
|---|---:|---:|---:|---:|
| digit_reduction_analyzer_v2 | 138 | 0 | 0.0000 | 15 |
| stable_top | 138 | 2 | 0.0145 | 23 |
| hot_zones_top | 138 | 1 | 0.0072 | 23 |
| vtrac_enhanced_top | 138 | 1 | 0.0072 | 16 |
| due_doubles | 138 | 2 | 0.0145 | 13 |
| mirror_pair_closure | 138 | 5 | 0.0362 | 16 |
| aux_vtrac_index_overdue | 138 | 9 | 0.0652 | 9 |
| union (all packs) | 138 | 32 | 0.2319 | 92 |

Interpretation of columns:
- `hit_any`: the pack directly contains the winner (straight and/or boxed, depending on pack play_mode).
- `index_hit`: the pack’s canonicals land in the same `vtrac_index` family as the winner (lane hit, not an exact hit).

---

## Key quantitative conclusions (v0)

1) **As currently ingested (top‑N “best_pattern” straights), DR does not produce direct hits in this window.**
   - `digit_reduction_analyzer_v2`: `hit_any=0/138`.

2) **DR does often land in the correct VTRAC family (“lane hit”), but that lane signal is not converting into hits via this pack.**
   - `index_hit=15/138`.

3) **This supports the design-intent hypothesis: DR is behaving like a trace/envelope lens, not a “top picks” caller.**
   - The next step is to confirm this qualitatively by reading DR overlays and traces for high-signal cases.

---

## Next (links)

- Case audit (why DR “sees” the winner but doesn’t elevate it): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
- Feature decisions (what DR outputs should feed v0.2 superbrain layers): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`

