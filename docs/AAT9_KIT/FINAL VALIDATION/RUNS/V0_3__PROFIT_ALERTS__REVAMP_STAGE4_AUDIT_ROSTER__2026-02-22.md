# V0.3 — Profit Alerts Revamp (Quarantined) — Stage 4 Audit Roster

Timestamp (UTC): `2026-02-22`

Purpose:
- Provide a **bounded, deterministic** manual-audit roster so you can confirm:
  - each alert is firing on the intended underlying evidence (Stable/JSON/aux),
  - and “low hit rate” is not just a **mapping/intent mismatch**.

Hard invariants:
- Profit Alerts stay quarantined (no reintegration into `tool_only` predictive pipeline).
- No analyzer edits (Stable/DR/Hot Zones/VTRAC unchanged).

Entry points (portable, GitHub-visible):
- Known-good window evidence pack:
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/CASEBOOK.md`
- Reported-bad window evidence pack:
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/CASEBOOK.md`

## How to audit a case (repeatable checklist)

For any case in an evidence pack `CASEBOOK.md`:
1) Open the mirrored `profit_alerts_eval.csv` row referenced by `row_num`.
2) Open the mirrored `profit_alerts.csv` row (board CSV) and inspect `Evidence` JSON.
3) If the case prints a “Stable locator”, open the Stable excerpt and confirm the exact row exists:
   - match keys: `(section, Set, Draw, Column, Canonical)`
4) Open the mirrored `*_tables.json` snapshot and confirm the pattern exists in the same neighborhood you expect.
5) Open the winners HTML/JSON (if present) for qualitative confirmation.
6) Record a verdict:
   - **Correct** (matches intent + evidence)
   - **Unclear** (needs more context)
   - **Wrong** (mapping bug, rule mismatch, or evaluation expectation mismatch)

## Tiered audit roster (do in order)

The evidence packs contain a curated set of 24 cases (two windows). Use the tiers below to control time.

### Tier 1 (highest ROI; do these first)

These establish “is the wiring + intent basically right?” quickly:

**HIT cases (prove positive semantics):**
- W1 Case 2 — `A02` — Florida4 — Midday — `HIT` — `033` — `STR8_3` — `CONS/DBL`
- W1 Case 5 — `A05` — NewJersey4 — Evening — `HIT` — `788` — `STR8_3` — `PERM/HP7`
- W2 Case 3 — `A04` — SouthCarolina4 — Evening — `HIT` — `015` — `BOX` — `PERSIST`
- W2 Case 10 — `A12` — NewJersey4 — Midday — `HIT` — `089` — `STR8_4of8` — `PERM/CLAMP`

**Promoter-only cases (prove we’re not grading them like candidates):**
- W1 Case 10 — `A03` — Pennsylvania4 — Combined — `PROMOTER` — `OVERLAY` — `CONS/XVAR`
- W1 Case 11 — `A08` — Delaware4 — Combined — `PROMOTER` — `OVERLAY` — `BA/TEMPO`

### Tier 2 (coverage of “non-Strict” signal types)

These validate the “environment / lane / regime” alerts:

- W1 Case 7 — `A09` — NewYork4 — Midday — `EXPIRED` — `STR8_8` — `VTRAC/REP`
- W2 Case 8 — `A09` — Florida4 — Evening — `EXPIRED` — `STR8_8` — `VTRAC/REP`
- W1 Case 8 — `A10` — Connecticut4 — Combined — `EXPIRED` — `225` — `STR8_3` — `DBL/RANK1`
- W2 Case 9 — `A10` — Connecticut4 — Combined — `EXPIRED` — `355` — `STR8_3` — `DBL/RANK3`
- W2 Case 6 — `A06` — SouthCarolina4 — Combined — `EXPIRED` — `259` — `BOX` — `DR/3V`

### Tier 3 (finish the full curated set)

Complete coverage across the windows and edge semantics:

**Known-good window (`2025-06-21..2025-06-23`):**
- W1 Case 1 — `A01` — Michigan4 — Evening — `EXPIRED` — `057` — `BOX` — `CONS/3V`
- W1 Case 3 — `A02` — NewYork4 — Evening — `EXPIRED` — `055` — `STR8_3` — `CONS/DBL/A10/BA`
- W1 Case 4 — `A04` — Michigan4 — Evening — `EXPIRED` — `057` — `BOX` — `PERSIST`
- W1 Case 6 — `A05` — NewYork4 — Combined — `EXPIRED` — `449` — `STR8_3` — `PERM/HP7`
- W1 Case 9 — `A12` — NorthCarolina4 — Evening — `EXPIRED` — `455` — `STR8_4of8` — `PERM/CLAMP`

**Reported-bad window (`2025-12-30..2026-01-09`):**
- W2 Case 1 — `A01` — SouthCarolina4 — Combined — `EXPIRED` — `019` — `BOX` — `CONS/3V/BA`
- W2 Case 2 — `A02` — OntarioCanada4 — Midday — `EXPIRED` — `022` — `STR8_3` — `CONS/DBL/A10`
- W2 Case 4 — `A04` — Delaware4 — Combined — `EXPIRED` — `348` — `BOX` — `PERSIST/BA`
- W2 Case 5 — `A05` — OntarioCanada4 — Midday — `EXPIRED` — `022` — `STR8_3` — `PERM/HP2`
- W2 Case 7 — `A07` — Delaware4 — Midday — `EXPIRED` — `035` — `BOX` — `BA/MIRROR`
- W2 Case 11 — `A12` — SouthCarolina4 — Midday — `EXPIRED` — `006` — `STR8_4of8` — `PERM/CLAMP`
- W2 Case 12 — `A03` — Michigan4 — Combined — `PROMOTER` — `OVERLAY` — `CONS/XVAR`
- W2 Case 13 — `A08` — Indiana4 — Combined — `PROMOTER` — `OVERLAY` — `BA/TEMPO`

## “Possible missing feature” short list (only if audits demand it)

Stage 4 is primarily about **confirming intent**. If (and only if) audits show that something is hard to validate or conceptually ambiguous, these are the most likely evidence/feature upgrades:

1) **A08 base-candidate context** (SSOT requirement)
   - Grading matrix says A08 “must identify base candidate context”.
   - If audits show ambiguity, exporter should include evidence like:
     - `base_candidate_required=1` (already present as `requires_base_box`),
     - plus a concrete pointer such as `base_candidate_alert_ids` or `base_candidate_canonical` when present.

2) **A03 stub provenance enrichment**
   - A03 already carries the triggering tail/col/sections; audits may still want stronger “why” breadcrumbs.
   - If needed: include a richer `stub_locators` payload (e.g., also include family/why fields for the stub rows).

3) **Optional: stable row disambiguator**
   - If you ever see duplicate rows matching the same `(section, Set, Draw, Column, Canonical)`, add a stable row index/uuid to `Evidence`.
   - This is usually unnecessary, but it’s the cleanest “no ambiguity ever” option.

## Stage 4 decision gate (what happens after audit)

After Tier 1 + Tier 2:
- If you find **true mapping/intent mismatch**, do **targeted tuning/fix** next (one alert at a time, re-grade with the same rollups/casebooks).
- If alerts look **conceptually correct** but rare, do **corpus expansion** next to stabilize per-alert behavior.

