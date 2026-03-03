# Codex Second‑Pass Review — Profit Alerts Stage‑4 Audit (A01–A12)

Stamp: `2026-03-02`  
Package: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_stage4_audit__2026-03-02__stage4_auto_v1/`

## What this report is (plain English)

This is a **second set of eyes** on the Stage‑4 audit package.

Goal:
- Confirm the Profit Alerts revamp is **wired to the intended evidence** (Stable row + environment),
- Confirm the evaluator/exporter contracts (Charter + Matrix) are being honored,
- Surface any **real mapping/intent mismatches** (not “hit-rate panic”).

What this is **not**:
- Not a reintegration proposal (Profit Alerts remain quarantined).
- Not analyzer edits (Stable/DR/Hot Zones/VTRAC are out of scope).
- Not a “hit-rate claim” across the corpus (this is a bounded wiring audit).

## SSOT used (must match)

- Charter (copy): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_stage4_audit__2026-03-02__stage4_auto_v1/ssot/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Grading Matrix (copy): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_stage4_audit__2026-03-02__stage4_auto_v1/ssot/AAT9_Profit_Alerts_Grading_Matrix.md`
- Roster (copy): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_stage4_audit__2026-03-02__stage4_auto_v1/ssot/V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md`

## Summary verdict (Codex)

### 1) Extraction integrity (raw-source re-derivation)

Across all **24** curated cases:
- Board row identity (`StateKey/Variant/AlertId/Suggested`) matches the referenced row number.
- Eval row identity (`row_type`, and promoter NA locks) matches the referenced row number.
- For `STR8_*` rows, `ImpliedSet` exists, parses, and matches expected size.
- For Stable‑anchored cases:
  - The Stable excerpt row exists at the locator and matches `family_id` + `why`.
  - The JSON environment snapshot is extractable at the same locator and matches the packet snapshot.

Result: **Integrity PASS 24/24**.

**One non-fatal display nuance (worth knowing):**
- `W2 Case 6` (`A06`, SouthCarolina4 Combined) shows `Canonical=592` on the board even though the box family is `259`.
  - This is still the **same boxed family** (`canonicalize(592) == canonicalize(259)`), and the board’s `ImpliedSet` contains the full box perms.
  - So evaluation is safe (membership/canonicalization), but it can confuse humans reading “Canonical” as a boxed label.

### 2) Semantic correctness (intent ↔ evidence)

Using the Charter + Matrix definitions:
- Candidate vs promoter typing is correct (A03/A08 are promoters; everything else here is candidate).
- The “set membership” contract is honored for set-based rows (`STR8_3`, `STR8_8`, `STR8_4of8`).
- Combined is treated as a **lens** (not a third draw) and promoters are not misgraded as hits.
- Stable + JSON cross-checks show the intended pattern neighborhoods where locators exist.

Result: **Semantics PASS 24/24** on this roster.

## Case index (all 24)

| Case | Alert | State | Variant | D | Status | Suggested | Canonical | StableLoc | ImpliedSet | Packet |
|---|---|---|---|---|---|---|---|---|---:|---|
| W1 1 | A01 | Michigan4 | Evening | 2025-06-21 | EXPIRED | BOX | 057 | Y | 6 | `case_packets/W1_Case_1_A01_Michigan4_Evening_2025-06-21.md` |
| W1 2 | A02 | Florida4 | Midday | 2025-06-21 | HIT | STR8_3 | 033 | Y | 3 | `case_packets/W1_Case_2_A02_Florida4_Midday_2025-06-21.md` |
| W1 3 | A02 | NewYork4 | Evening | 2025-06-21 | EXPIRED | STR8_3 | 055 | Y | 3 | `case_packets/W1_Case_3_A02_NewYork4_Evening_2025-06-21.md` |
| W1 4 | A04 | Michigan4 | Evening | 2025-06-21 | EXPIRED | BOX | 057 | Y | 6 | `case_packets/W1_Case_4_A04_Michigan4_Evening_2025-06-21.md` |
| W1 5 | A05 | NewJersey4 | Evening | 2025-06-21 | HIT | STR8_3 | 788 | Y | 3 | `case_packets/W1_Case_5_A05_NewJersey4_Evening_2025-06-21.md` |
| W1 6 | A05 | NewYork4 | Combined | 2025-06-23 | EXPIRED | STR8_3 | 449 | Y | 3 | `case_packets/W1_Case_6_A05_NewYork4_Combined_2025-06-23.md` |
| W1 7 | A09 | NewYork4 | Midday | 2025-06-22 | EXPIRED | STR8_8 | - | N | 8 | `case_packets/W1_Case_7_A09_NewYork4_Midday_2025-06-22.md` |
| W1 8 | A10 | Connecticut4 | Combined | 2025-06-21 | EXPIRED | STR8_3 | 225 | N | 3 | `case_packets/W1_Case_8_A10_Connecticut4_Combined_2025-06-21.md` |
| W1 9 | A12 | NorthCarolina4 | Evening | 2025-06-22 | EXPIRED | STR8_4of8 | 455 | Y | 4 | `case_packets/W1_Case_9_A12_NorthCarolina4_Evening_2025-06-22.md` |
| W1 10 | A03 | Pennsylvania4 | Combined | 2025-06-21 | PROMOTER | OVERLAY | - | N | 0 | `case_packets/W1_Case_10_A03_Pennsylvania4_Combined_2025-06-21.md` |
| W1 11 | A08 | Delaware4 | Combined | 2025-06-21 | PROMOTER | OVERLAY | - | N | 0 | `case_packets/W1_Case_11_A08_Delaware4_Combined_2025-06-21.md` |
| W2 1 | A01 | SouthCarolina4 | Combined | 2025-12-30 | EXPIRED | BOX | 019 | Y | 6 | `case_packets/W2_Case_1_A01_SouthCarolina4_Combined_2025-12-30.md` |
| W2 2 | A02 | OntarioCanada4 | Midday | 2026-01-02 | EXPIRED | STR8_3 | 022 | Y | 3 | `case_packets/W2_Case_2_A02_OntarioCanada4_Midday_2026-01-02.md` |
| W2 3 | A04 | SouthCarolina4 | Evening | 2026-01-03 | HIT | BOX | 015 | Y | 6 | `case_packets/W2_Case_3_A04_SouthCarolina4_Evening_2026-01-03.md` |
| W2 4 | A04 | Delaware4 | Combined | 2026-01-06 | EXPIRED | BOX | 348 | Y | 6 | `case_packets/W2_Case_4_A04_Delaware4_Combined_2026-01-06.md` |
| W2 5 | A05 | OntarioCanada4 | Midday | 2026-01-02 | EXPIRED | STR8_3 | 022 | Y | 3 | `case_packets/W2_Case_5_A05_OntarioCanada4_Midday_2026-01-02.md` |
| W2 6 | A06 | SouthCarolina4 | Combined | 2026-01-04 | EXPIRED | BOX | 259 | N | 6 | `case_packets/W2_Case_6_A06_SouthCarolina4_Combined_2026-01-04.md` |
| W2 7 | A07 | Delaware4 | Midday | 2026-01-07 | EXPIRED | BOX | 035 | Y | 6 | `case_packets/W2_Case_7_A07_Delaware4_Midday_2026-01-07.md` |
| W2 8 | A09 | Florida4 | Evening | 2025-12-31 | EXPIRED | STR8_8 | - | N | 8 | `case_packets/W2_Case_8_A09_Florida4_Evening_2025-12-31.md` |
| W2 9 | A10 | Connecticut4 | Combined | 2026-01-01 | EXPIRED | STR8_3 | 355 | N | 3 | `case_packets/W2_Case_9_A10_Connecticut4_Combined_2026-01-01.md` |
| W2 10 | A12 | NewJersey4 | Midday | 2026-01-08 | HIT | STR8_4of8 | 089 | Y | 4 | `case_packets/W2_Case_10_A12_NewJersey4_Midday_2026-01-08.md` |
| W2 11 | A12 | SouthCarolina4 | Midday | 2025-12-31 | EXPIRED | STR8_4of8 | 006 | Y | 4 | `case_packets/W2_Case_11_A12_SouthCarolina4_Midday_2025-12-31.md` |
| W2 12 | A03 | Michigan4 | Combined | 2026-01-01 | PROMOTER | OVERLAY | - | N | 0 | `case_packets/W2_Case_12_A03_Michigan4_Combined_2026-01-01.md` |
| W2 13 | A08 | Indiana4 | Combined | 2025-12-30 | PROMOTER | OVERLAY | - | N | 0 | `case_packets/W2_Case_13_A08_Indiana4_Combined_2025-12-30.md` |

## Cross-cutting “contract wins” (why this is encouraging)

### A) Stable ↔ JSON alignment is real (when a locator exists)

When a case has a Stable locator (`StableLoc=Y`), you can always do the same human proof:
1) The exporter says: “this alert fired because of this specific Stable row.”
2) The packet proves the row exists in the Stable excerpt (`*_profit_alerts_excerpt.csv`).
3) The packet also shows the **coded-table environment** (R2/R4/R6/R8 row-end tokens) at the same locator column.

This is exactly the “R2/R4/R6/R8 environment cross-check” you want for confidence.

### B) The lossy/ambiguous part is not in the evaluator

The evaluator is now deterministic in the ways that used to cause major confusion:
- **Combined is a lens**, not an outcome stream.
- **Set-based suggestions** are graded by membership in the exported `ImpliedSet` (no guessing clamp subsets).
- **Promoters** (A03/A08) are typed as `PROMOTER` and not misgraded as “did it hit”.

### C) A12 dominance math is correctly tied to the environment

A12 is the most “fragile” to audit because JSON row-end tokens can be longer than 3 digits (e.g. `5541**`).

We now treat dominance as:
- “does the modal 3-digit order appear inside the row-end token’s digits stream?”

That makes the audit robust (and it matches how humans read the coded environment).

## Tier‑1 deep checks (high ROI cases)

These are the 6 cases that best prove “the revamp is wired correctly”.

### 1) A02 (HIT): Florida4 Midday — `033` — `STR8_3`
Packet: `case_packets/W1_Case_2_A02_Florida4_Midday_2025-06-21.md`
- Meaning: single-tail consensus resolving as a **double** play (3 perms).
- Evidence: Stable row shows `orders_modal_value=033`, and the JSON snapshot shows `033` at the locator in all four rows.
- Contract: `ImpliedSet=["033","303","330"]` is explicit and gradeable.

### 2) A05 (HIT): NewJersey4 Evening — `788` — `STR8_3`
Packet: `case_packets/W1_Case_5_A05_NewJersey4_Evening_2025-06-21.md`
- Meaning: horizontal straight drift in a double family; output is the “3 perms” set.
- Evidence: Stable row canonical is `788` but the modal straight order is `887` (this is expected: the stable row is a *box family*, and it reports the dominant straight order inside it).
- Environment: JSON row-end tokens contain `887` in multiple rows at the locator column (strong drift signature).

### 3) A04 (HIT): SouthCarolina4 Evening — `015` — `BOX`
Packet: `case_packets/W2_Case_3_A04_SouthCarolina4_Evening_2026-01-03.md`
- Meaning: persistence carry; the box family remains “alive” into the near horizon.
- Evidence: Stable locator + JSON snapshot show both `015` and its dominant sibling order `051` active in the environment.
- Result: strict hit and window hit both align with the box membership semantics.

### 4) A12 (HIT): NewJersey4 Midday — `STR8_4of8`
Packet: `case_packets/W2_Case_10_A12_NewJersey4_Midday_2026-01-08.md`
- Meaning: low order entropy (same modal order appears in most R-rows) → clamp to a 4-of-8 subset.
- Evidence: modal order `098` appears in 3 of 4 JSON row ends at the locator.
- Contract: clamp subset is explicitly exported (`ImpliedSet=["034","039","084","089"]`), and the winner (`089`) is in the set.

### 5) A03 (PROMOTER): Pennsylvania4 Combined — Cross-variant consensus
Packet: `case_packets/W1_Case_10_A03_Pennsylvania4_Combined_2025-06-21.md`
- Meaning: “this tail is being supported in ≥2 sections” (cross-variant).
- Evidence: `stub_locators` lists two concrete consensus stubs in different sections.
- Contract: row is typed `PROMOTER`, and eval fields are `NA` (not misgraded as a candidate).

### 6) A08 (PROMOTER): Delaware4 Combined — BA/TEMPO overlay
Packet: `case_packets/W1_Case_11_A08_Delaware4_Combined_2025-06-21.md`
- Meaning: “tempo/regime overlay” driven by BA remaining pairs; does not invent a box.
- Evidence: includes `ba_score`, `pairs_remaining`, and locks (`promoter_only`, `requires_base_box`).
- Contract: row is typed `PROMOTER`, eval fields are `NA`.

## Notes / potential follow-ups (not required for Stage‑4 PASS)

1) **A08 base-candidate context pointer**
   - Matrix says A08 should identify base-candidate context.
   - Evidence includes `requires_base_box=1` but does not point to which candidate row(s) are being promoted.
   - If you want to make A08 fully self-auditing later: add a minimal pointer like `base_candidate_alert_ids` or `base_candidate_canonicals` when present.

2) **A06 board “Canonical” display**
   - Consider standardizing board `Canonical` to the boxed label (sorted digits) for human readability (evaluation is already safe).

3) **Roster coverage note**
   - This Stage‑4 roster does not include an A11 case. A11 still needs its own bounded audit roster when you’re ready.

