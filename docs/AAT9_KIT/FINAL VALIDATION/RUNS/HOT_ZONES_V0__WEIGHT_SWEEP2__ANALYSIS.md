# Hot Zones — HOTZ‑003 Weight Sweep v2 (VT‑Only + Col1 Arrival) — Analysis Notes

Purpose: interpret the multi-parameter sweep results **in the same language as Master Validation** (winners lens + VTRAC context), so we can decide whether HOTZ‑003 should become an analyzer change (v0.3) or stay as-is and shift effort to selection-layer fusion.

This analysis pairs:
- The weight sweep results (`HOT_ZONES_V0__WEIGHT_SWEEP2__*.md/.csv`)
- With representative winner-lens artifacts (`sharepacks/<D>/<STATE>/winners/<STATE>/*.html/.json`)
- And the corresponding Master Validation run reports (`docs/.../RUNS/<D>__<STATE>.md`)

---

## What was swept

Harness: `scripts/tools/hot_zones_weight_sweep.py`

Parameters (v2):
- `w_vt_only_lane_bonus`: `0.8, 0.9, 1.0, 1.1` (default baseline is `0.8`)
- `w_col1_arrival`: `2.1, 2.4, 2.7, 3.0` (default baseline is `2.4`)

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-06-21_to_2025-06-23.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2026-01-05_to_2026-01-09.md`

---

## High-level result (measured)

Across the v0 regression windows, adding `w_col1_arrival` to the sweep produces **only small, inconsistent** changes:
- Some windows show a slight Top8 bump when `w_col1_arrival=2.1` (typically a winner moving rank 9 → 8).
- Top12/Top20 do not show stable lift across windows.
- Increasing `w_vt_only_lane_bonus` still improves average rank for some “vt-only-visible” winners, but does not reliably pull them into top‑K.

Net: HOTZ‑003 “weight tuning” is not yet supported as a high-leverage v0.3 change.

---

## “Borderline Top8 promotion” case studies (paired with winners lens)

These are the only *unique* cases in the windows where a weight change moved the winner into Top8 from just outside it.

### Case A — NewYork4 Midday winner `080` (canonical `008`) — moved 9 → 8

- Sweep window: `2026-01-05_to_2026-01-09`
- Baseline: `vt_only=0.8,col1=2.4` → winner rank `9`
- Variant: `vt_only=0.8,col1=2.1` (also `vt_only=0.9,col1=2.1`) → winner rank `8`
- Sweep row: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2026-01-05_to_2026-01-09.csv`

Winners lens:
- `sharepacks/2026-01-05/NewYork4/winners/NewYork4/NewYork4_vtrac4_winner_080_20260110_035730.html`
- Digest: `sharepacks/2026-01-05/NewYork4/winners/NewYork4/digest.md`

Master Validation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`

Interpretation:
- This is a **strong environment** (Stable exact boxed + exact straight; winner canonical is rank‑1 dominant in winners digest).
- Hot Zones is already “seeing it”; the sweep shows only that `w_col1_arrival` can nudge borderline rank ordering.
- This does not argue for broad weight changes; Stable already isolates the winner.

### Case B — NorthCarolina4 Evening winner `879` (canonical `789`) — moved 9 → 6/7

- Sweep window: `2025-12-30_to_2026-01-04`
- Baseline: `vt_only=0.8,col1=2.4` → winner rank `9`
- Variant: `vt_only=0.8,col1=2.1` (also `vt_only=0.9,col1=2.1`) → winner rank `6`
- Variant: `vt_only=1.0,col1=2.1` (and `vt_only=1.1,col1=2.1`) → winner rank `7`

Winners lens:
- `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac30_winner_879_20260105_051207.html`
- Digest: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/digest.md`

Master Validation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NorthCarolina4.md`

Interpretation (why this is meaningful):
- Winners digest shows canonical `789` is occurrence‑rank‑1 inside the index (but literal `879` itself is 0), i.e. **boxed gateway** is the natural “hit criteria”.
- This is exactly the kind of case where Hot Zones (as a lane lens) can be valuable even when Stable misses.
- The weight change effect is still “borderline ordering”, not a systemic lift.

### Case C — Connecticut4 Midday winner `950` (canonical `059`) — moved 12 → 8

- Sweep window: `2025-06-21_to_2025-06-23`
- Baseline: `vt_only=0.8,col1=2.4` → winner rank `12`
- Variant: `vt_only=1.1,col1=2.7` (also `vt_only=1.1,col1=3.0`) → winner rank `8`

Winners lens:
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251219_164349.html`
- Digest (generated): `python3 scripts/tools/winners_json_digest.py --winners-dir sharepacks/2025-06-21/Connecticut4/winners/Connecticut4`

Master Validation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Connecticut4.md`

Interpretation:
- Winners lens shows the winner family/index is dominated by siblings (`559`, `455`); `059` is present but not dominant.
- This is a realistic “family hit but literal weak” environment.
- A VT-only bonus can help surface the weaker canonical, but the broader evidence still points to siblings; this is why Hot Zones alone won’t be a straight oracle.

---

## Takeaways (what this implies for improving Hot Zones)

1) **Weight tuning moves ordering, not coverage**
- The sweep mostly changes rank slightly.
- We rarely convert “not present” → “present”; we mostly adjust “present but low-rank”.

2) **The “4 hit criteria” lens still supports Hot Zones as a valuable tool**
- Hot Zones is most defensible as a *lane* tool:
  - it can help isolate boxed candidates (canonical) even when literal order is not present,
  - and it can support VTRAC-family thinking (especially when combined with VTRAC Enhanced + Stable).

3) **If you want bigger lift, the next lever is not weights; it’s features + consumption**
- Candidate Universe / Play Cards can convert lane correctness into bounded closures (index/mirror/pair closures).
- Analyzer-level features like “repeat_3value_score” and “true consensus flag” should be treated as v0.3 hypotheses and measured with bounded harnesses before tuning.

---

## Recommendation (operational)

- Keep Hot Zones weights unchanged in v0.2 (no stable Top‑K lift across windows).
- Keep HOTZ‑003 in v0.3 backlog as “Measured; no stable lift from bounded sweeps”.
- Next measurement upgrade (if desired): extend the harness to compute **VTRAC index hit** in Top‑K (index-hit is often the true “gateway” in your methodology), so we don’t judge Hot Zones solely by exact canonical hits.

