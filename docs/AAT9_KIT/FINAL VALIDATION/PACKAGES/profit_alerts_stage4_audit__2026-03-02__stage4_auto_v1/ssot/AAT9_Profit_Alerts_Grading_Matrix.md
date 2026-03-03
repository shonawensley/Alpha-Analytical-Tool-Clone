# AAT9 Profit Alerts (A01–A12) — Grading Matrix (SSOT)

Purpose: define **what a “hit” means per alert** so Master Validation doesn’t fall into the “0 hits” panic loop caused by grading the wrong object.

Scope:
- This is **evaluation-only** (Brain‑2). It does **not** change core analyzers (Stable/DR/VTRAC/Hot Zones) or string-table extraction.
- It applies to the sharepack-aligned export:
  - `sharepacks/<D>/control_center/profit_alerts.csv`
  - Evaluations written by: `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`
- It complements (does not replace) the global evaluation rules in:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

---

## Non‑negotiable SSOT locks

### 1) Combined is a lens, not an outcome stream
- Outcomes are only `Midday` and `Evening`.
- `Combined` alerts must be graded against the real Midday/Evening results sequence per the Charter.

### 2) Set-based grading is mandatory when `Suggested` implies a set
If the alert is a “small coverage” play (BOX/STR8), the evaluator must grade:
> `winner ∈ implied_set` within the window

To make this deterministic:
- The exporter must include an explicit `implied_set` (JSON list of `"000"` strings) whenever `Suggested` is `STR8_*` (and optionally for `BOX` if you want explicit membership instead of canonical‑derived perms).
- The evaluator must **never guess clamp subsets** (e.g., STR8_4-of-8); it must grade membership against the exported list.

### 3) A08 is TEMPO/promoter only
- A08 is an overlay/promoter signal: it **never invents a box**.
- A08 is graded as **lift/relationship** on co‑firing candidate episodes (not as a standalone “winner hit”).

### 4) A10:DUE_DOUBLES is a playable small set (primary grade = STR8_3 membership)
- A10’s primary grading is: `winner ∈ implied_set (STR8_3)` within window.
- Secondary diagnostic (not primary): “did a double occur within window?” / “did winner fall into due double family?”

---

## Row types (how to think about alerts)

- **Candidate**: the row implies a concrete play set (boxed set / straight set / VT-straights set).
- **Promoter / Overlay**: the row is a condition/timing booster; it does not create a standalone play.
- **Governor**: like a promoter, but must be stratified (e.g., by star level).

The evaluator should report both:
- **Raw rows** (what fired), and
- **Merged episodes** (what you would actually act on when multiple rows co-fire).

---

## Grading matrix (v0)

Legend:
- `primary` = the metric that decides HIT/EXPIRED/CENSORED for the row’s own window.
- `secondary` = diagnostics / relationship metrics (do not treat as “the hit rate”).

| AlertId | Type | Primary graded object | Required export fields | Notes |
|---:|---|---|---|---|
| A01 | Candidate (BOX) | Box-set membership | `Canonical` (3-digit), optional `implied_set` | Grade boxed membership; if no `implied_set`, evaluator may derive perms from `Canonical` (safe). |
| A02 | Candidate (STR8_3) | Straight-set membership | `Canonical` (double), `implied_set` | `implied_set` should be the 3 perms of the double. |
| A03 | Promoter/Overlay | Lift/relationship (not winner membership) | `Evidence` must include triggering tail/col/sections | A03 should not be graded as “did canonical hit”. |
| A04 | Candidate (BOX) | Box-set membership | `Canonical`, optional `implied_set` | Similar to A01 but driven by persistence. |
| A05 | Candidate (STR8_3 / STR8_8) | Set membership | `Evidence.orders_modal_value`, `implied_set` | STR8_3 = perms of a double. STR8_8 = V-straights lane (8). |
| A06 | Candidate (BOX) | Box-set membership | `Canonical`, optional `implied_set` | DR survivor-style candidate. |
| A07 | Candidate (BOX) | Box-set membership | `Canonical`, optional `implied_set` | Mirror timing candidate derived from BA mirror + consensus tail. |
| A08 | Promoter/TEMPO | Lift/relationship | must identify base candidate context | A08 never invents a box; grade as lift when co-firing with candidate episodes. |
| A09 | Candidate (STR8_8) | Set membership | `Evidence.current_index`, `implied_set` | `implied_set` is V-straights lane for current_index. |
| A10 | Candidate (STR8_3) | Set membership | `implied_set`, evidence about due-doubles canonical/gap | Primary grade is `winner ∈ implied_set`. Secondary diagnostics can track double-event. |
| A11 | Candidate + Governor | Box-set membership, stratified by star_level | `Evidence.a11_star_score`, `Evidence.star_level`, `Canonical` | Must report hit/time-to-hit stratified by star_level. |
| A12 | Candidate (STR8 clamp) | Set membership | `Evidence.orders_modal_value`, `implied_set` | Clamp subsets must be exported (never guessed by evaluator). |

---

## Suggested tokens → implied_set contract (v0)

The exporter must emit `implied_set` as a JSON list of 3-digit strings when `Suggested` implies a set:

- `STR8_8`: **V‑Straights lane** (8 combos) keyed by the V-code (e.g., `v224`), or derived from `current_index` via the VTRAC index→V-code mapping.
- `STR8_4of8`: 4-combo clamp subset of the STR8_8 lane (exact rule must be encoded in exporter; evaluator only checks membership).
- `STR8_3`: 3 permutations of a double (e.g., `005/050/500`).
- `BOX`: optional to export. If absent, evaluator may derive box perms from `Canonical`.

