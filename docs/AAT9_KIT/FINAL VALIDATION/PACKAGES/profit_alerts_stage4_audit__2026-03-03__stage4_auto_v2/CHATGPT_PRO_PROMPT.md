# ChatGPT Pro — Deep Research Prompt (Profit Alerts Stage-4 Audit)

## Mission
Verify Profit Alerts revamp correctness by reviewing a bounded, evidence-linked Stage-4 audit package.
Focus on **mapping/intent correctness**, not reintegration or tuning.

## Hard constraints (do not violate)
- Do not recommend analyzer edits (Stable/DR/Hot Zones/VTRAC are out of scope).
- Profit Alerts are quarantined; do not recommend enabling them in `tool_only` defaults.
- Treat Combined as a **lens**, not an outcome stream.
- Promoters (A03/A08) are not graded as candidate callers.

## SSOT rules (must follow)
- Charter (copy): `ssot/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Grading Matrix (copy): `ssot/AAT9_Profit_Alerts_Grading_Matrix.md`

## What you are given
- Audit package manifest: `MANIFEST.md`
- Audit sheet (prefilled): `AUDIT_SHEET.csv`
- Per-case packets (prefilled): `case_packets/`
- SSOT copies: `ssot/`

## How to review (repeatable)
For each case packet:
1) Read the extracted board row + eval row.
2) Check the contract locks:
   - row_type matches expected (PROMOTER vs CANDIDATE)
   - STR8_* rows have explicit ImpliedSet (no guessing)
3) If the case has a Stable locator:
   - confirm Stable excerpt row exists at that locator
   - confirm JSON environment snapshot row-ends at the same locator match the intended pattern story
4) Confirm the packet’s AutoVerdict (PASS/FAIL/AMBIG) is correct, or explain why it should change.

## Required deliverable back to us
- A short report with:
  - PASS/FAIL/AMBIG counts you agree with (or corrected)
  - Any cases where AutoVerdict is wrong and why
  - A failure taxonomy: mapping bug vs semantics misunderstanding vs missing evidence vs expectation mismatch
  - Optional: 1–3 minimal evidence-schema improvements (only if audits are ambiguous), e.g. A08 base-candidate context pointer.

## Tier-1 recommendation (review these first)
Start with HIT + PROMOTER cases (highest ROI). The audit roster is:
- `ssot/V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md`

Tier-1 quick links (open these packets first):
- `case_packets/W1_Case_2_A02_Florida4_Midday_2025-06-21.md`
- `case_packets/W1_Case_5_A05_NewJersey4_Evening_2025-06-21.md`
- `case_packets/W2_Case_3_A04_SouthCarolina4_Evening_2026-01-03.md`
- `case_packets/W2_Case_10_A11_Connecticut4_Combined_2025-12-30.md`
- `case_packets/W1_Case_10_A11_SouthCarolina4_Combined_2025-06-22.md`
- `case_packets/W1_Case_11_A12_NorthCarolina4_Evening_2025-06-22.md`
