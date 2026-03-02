# V0.3 — Profit Alerts (Quarantined) — Example Deep Dive Notes

Purpose:
- Capture the “we audit together” micro-sessions from `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md:1`.
- Keep each case **evidence-linked** (Stable locator + mirrored files) so we can make fixes without talking in circles.

Hard invariants:
- Profit Alerts remain quarantined (no reintegration into `tool_only` predictive pipeline).
- No analyzer edits (Stable/DR/Hot Zones/VTRAC unchanged).

---

## Example 1 — W2 Case 10 — `A12` — NewJersey4 — Midday — D=`2026-01-08` (HIT)

Roster reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md:1`
- Evidence pack casebook: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/CASEBOOK.md:152`

### 1) What fired (board/eval facts)

- Alert: `A12` (Badges: `PERM/CLAMP`)
- Status: `HIT`
- Suggested: `STR8_4of8` (implied set size `4`)
- Canonical: `089`
- Strength: `3`
- DecayDraws: `2`
- Eval: `strict_hit=Y` (hit_type: `Straight+Boxed`, same draw)

### 2) Evidence receipts (files to open)

Portable (evidence pack, GitHub-visible):
- Eval row source (row_num=66): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/control_center/profit_alerts_eval.csv`
- Profit board (csv): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/control_center/profit_alerts.csv`
- Stable excerpt (locator target): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores__profit_alerts_excerpt.csv`
- Winners HTML/JSON dir: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/winners/NewJersey4`
  - Open (Midday winner): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/winners/NewJersey4/NewJersey4_vtrac14_winner_089_20260110_034428.html`
- JSON tables snapshot: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/json/NewJersey4_tables.json`

Local equivalents (same artifacts, outside the pack):
- Winners HTML: `sharepacks/2026-01-08/NewJersey4/winners/NewJersey4/NewJersey4_vtrac14_winner_089_20260110_034428.html`
- JSON tables: `sharepacks/2026-01-08/NewJersey4/json/NewJersey4_tables.json`

### 3) What we expect to see (intent ↔ evidence)

`A12` intent (current spec):
- “Permutation Clamp” (low order entropy / order dominance across R-rows) → safely shrink an 8-combo lane into ~4-combo straight overlay.
- Spec: `docs/AAT9_KIT/FINAL VALIDATION/12 TRACKERS ALERT SPEC.MD.txt:221`

In this case, the board evidence encodes:
- `order_dominance = 0.75` and `orders_modal_value = 098` with `orders_modal_rows = 3`
- clamp rule: `STR8_4of8:first_digit`
- implied set: `["034","039","084","089"]`

So we expect:
- In winners HTML (Set1/Draw1/Col1): “row-end” reductions show `098**` in 3 of 4 rows, and a minority row ending `089**`.
- In JSON tables (Midday → Set1 → Draw1 → pattern_variations): the same `098**` vs `089**` split across `R2/R4/R6/R8`.

### 4) Audit questions (yes/no)

1) Do the row-end strings show `098**` in 3 of 4 rows (R2/R4/R8) and `089**` in 1 row (R6)?
2) Does the Stable excerpt row match the locator (`Midday`, `Set1`, `Draw1`, col `1`, canonical `089`) and show `orders_modal_value=098`, `orders_modal_rows=3`?
3) Do HTML and JSON snapshots agree on the above (no drift between representations)?
4) Does the implied set `["034","039","084","089"]` “feel consistent” with what you see as the environment (your R2/R4/R6/R8 read)?

### 5) Notes / verdict

- Your notes:
- Codex notes:
- Verdict: (Correct / Unclear / Wrong)
- Next action:

### 6) Context (same-day alerts for this state; not part of the “case”)

On `2026-01-08`, `NewJersey4` had **6** Profit Alerts on the board across variants:

- **Midday:** `A04` (PERSIST) + `A12` (PERM/CLAMP) — both anchored to canonical `089` (same Stable locator).
  - `A04` suggested full BOX perms of `089`: `["089","098","809","890","908","980"]` with `persistence_set_count=2`.
  - `A12` suggested a clamped straight subset (4-of-8 posture): `["034","039","084","089"]` with `order_dominance=0.75` and modal order `098` across 3 rows.
- **Evening:** `A05` (PERM/HP5) — canonical `778` — implied set `["778","787","877"]` with modal order `877` across 3 rows.
- **Combined:** `A01` (CONS/3V) — canonical `035` — tail consensus `03` — implied set `["035","053","305","350","503","530"]`.
- **Combined:** `A10` (DBL/RANK1) — canonical `556` — due doubles rank `1` — implied set `["556","565","655"]`.
- **Combined:** `A11` (HOT/CONS) — canonical `078` — `star_level=2` (evidence tags) — implied set `["078","087","708","780","807","870"]`.

---

## Stack Lens (Where / When / How) — for fast “co-fire” reasoning

This lens is a **human-friendly way** to read days where many alerts fire without getting lost.

Categories (from the Executive Summary’s “why this set works together”):
- **WHERE** (find the neighborhood): `A01`, `A03`, `A11`
- **WHEN** (repeat / timing): `A04`, `A09`, `A10`
- **HOW** (take the straight cheaply): `A02`, `A05`, `A12`
- **FOUNDATION / HEALTH** (filter days): `A06`, `A08`
- **ROUTE / SPLIT** (mirror handling): `A07`

### Example 1 (NewJersey4, 2026-01-08): what co-fired?

**WHERE signals present (same day, state):**
- `A01` (Combined) — CONS/3V — canonical `035` — tail consensus `03` (BOX perms)
- `A11` (Combined) — HOT/CONS — canonical `078` — `star_level=2` (BOX perms)

**WHEN signals present:**
- `A04` (Midday) — PERSIST — canonical `089` — persistence (`persistence_set_count=2`) (BOX perms)
- `A10` (Combined) — DBL/RANK1 — canonical `556` (STR8_3 perms)

**HOW signals present:**
- `A12` (Midday) — PERM/CLAMP — canonical `089` — order clamp (STR8_4of8 subset)
- `A05` (Evening) — PERM/HP5 — canonical `778` — order modal `877` (STR8_3 perms)

**What is the “cleanest” stacked story for the winner (089 Midday)?**
- Winner anchor is canonical `089` (Midday).
- The directly-relevant co-fire stack is:
  - `A04` (WHEN: persistence) + `A12` (HOW: clamp) on the **same canonical**.
- That is a textbook “where to look + how to pay less” combo:
  - `A04` says “keep the box neighborhood” (`089` perms).
  - `A12` says “order is clamped enough to safely shrink the straight overlay” (4-of-8 posture).

Audit outcome for this example should be:
- Evidence alignment: Stable locator row exists and matches.
- Environment alignment: HTML winners output and JSON mirror show `098**` as modal order across 3 rows and `089**` as the minority row-end (so dominance 3/4).
- Action alignment: implied_set is consistent with clamp rule and the winner is in it.
