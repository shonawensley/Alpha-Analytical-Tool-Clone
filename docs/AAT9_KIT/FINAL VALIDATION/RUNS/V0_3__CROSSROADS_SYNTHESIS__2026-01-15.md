# Crossroads Synthesis — D=2026‑01‑15 (stable10 • tool_only • B36)

Purpose: a “wake up after a break” re‑entry memo that anchors the Crossroads work to one gold day, one posture, one budget.

This memo is **selection-layer only**. It does not propose analyzer edits.

## Locked posture (SSOT)

- Profile: `tool_only` (Profit Alerts quarantined)
- CU posture: `stable10`
- Budget: `B36` only
- Baseline strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail`
- Objective: **isolation-first**
  - Primary: reduce `CU_LANE_BUT_PLAY_MISS` (lane present in CU, dropped by the Play Card cut)
  - Guardrail: OOS strict (B36) must not regress vs baseline scoreboards

Reference:
- Policy: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- Glossary: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- Flow: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`

## The one rule that stops spirals

Always review using **3-view triangulation**:
- PRE (winners‑free): predictive report + `sharepacks/_predictive/<D>/...`
- DECISION: glass‑box trace (`__GLASS_BOX_TRACE__...`)
- POST (winner‑aware): MV report + winners HTML (`sharepacks/<D>/.../winners/...`)

Do not mix “POST insights” into “PRE narratives”. POST is forensics/spec; PRE is what existed; DECISION is what we cut.

## Crossroads Pack v1 (the deterministic study set)

Pack entrypoint:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`

Case index:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

## What the 5 cases are designed to answer

| Bucket | Question it answers | What to look at first |
|---|---|---|
| `CU_MISS` | Did evidence even touch the winner’s lane? | CU union grade + Predictive CU JSON |
| `CU_LANE_BUT_PLAY_MISS` | Lane was present — why did the Play Card drop it? | Glass‑box lane allocation (`indices_touched_count`, `winner_lane_lines`) |
| `CU_EXACT_BUT_PLAY_MISS` | Exact winner was in CU — why was it cut? | Trace + CU evidence provenance (`candidate_universe_evidence...csv`) |
| `HIT_INCLUSIVE` | Lane retained but strict missed — is it a depth problem? | `winner_lane_lines` + pack bridge fields |
| strict hit (`hit_any=1`) | What does “good” look like mechanically? | Compare the strict-hit trace vs the misses |

## Anti‑spiral checklist (5 minutes)

1) Confirm you’re reading the right posture (stable10 + tool_only):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

2) Confirm the truth layer (don’t argue with memory):
- Jan window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- OOS guardrail: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

3) If you need examples, read the casebook and then open the matching traces:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__GLASS_BOX_TRACE_BUNDLE__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`

## What “success” looks like next (selection-layer only)

After reviewing Crossroads Pack v1 (human + ChatGPT Pro deep research):
- We can name 1–2 geometry changes that should reduce `CU_LANE_BUT_PLAY_MISS`.
- Each change has explicit acceptance criteria on:
  - Jan window improvement (primary objective),
  - OOS non‑regression (guardrail),
  - no analyzer edits required.

