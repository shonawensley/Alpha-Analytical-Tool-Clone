# Glass‑Box Trace — OntarioCanada4 (2026‑01‑15)

Purpose: a single, concrete “end‑to‑end” walkthrough so the pipeline stops feeling abstract.

Scope: `tool_only` + `stable10` posture (selection‑layer focus).

Strategy under inspection:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail` @ `B36`

---

## Orientation: start with the winners lens (what actually happened)

Open:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__WINNERS_DIGEST.md`

Ontario section shows (Midday + Evening):
- Midday winner: `598` (canonical `589`) — VTRAC index `14`
- Evening winner: `791` (canonical `179`) — VTRAC index `22`

Related winners overlay artifacts (from the digest):
- `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac14_winner_598_20260127_014847.json`
- `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac22_winner_791_20260127_014849.json`

Raw results file (same day; optional cross-check):
- `data/results/2026-01-15.txt`

---

## The 5 questions (run twice: Midday and Evening)

The key insight: **CU and Play Card are different contracts**.

- CU union (“could we have played the lane?”) lives in the CU grade.
- Play Card (“what did we actually select under B36?”) lives in the Play Card grade.
- Lane allocation (“how many lanes + how many lines on winner lane?”) quantifies the squeeze.

### A) Midday (OntarioCanada4, winner_label=Midday)

Winner facts:
- winner straight: `598`
- canonical: `589`
- lane (VTRAC index): `14`

1) Did CU union touch the lane?
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__CANDIDATE_UNIVERSE_GRADE__tool_only__stable10.csv`
- Find the `__UNION__` row for OntarioCanada4 + Midday winner `598`.
  - Expected: `vtrac_index_hit=1` and `hit_any=0` (lane signal present; exact not present).

2) Did the Play Card retain the lane at B36 for our strategy?
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PLAY_CARD_GRADE__tool_only__stable10.csv`
- Find the row:
  - `state_key=OntarioCanada4`
  - `winner_label=Midday`
  - `strategy=v0_2_default_multi_pack_packheavy_spine4_index_tail`
  - `budget_label=B36`
  - Expected: `hit_any_inclusive=1`, `vtrac_index_hit=1`, `hit_any=0`

3) How much of B36 was spent *on the winner lane* (depth), and how many lanes were touched (breadth)?
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.csv`
- Find the OntarioCanada4 + Midday row (winner `598`).
  - Expected: `indices_touched_count=16`
  - Expected: `winner_lane_present=1`
  - Expected: `winner_lane_lines=1`

4) What bucket is this outcome in (where did it break)?
- This is **HIT_INCLUSIVE** (lane retained, strict miss).
- Cross-check: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`

5) Where are the raw artifacts to inspect?
- CU JSON: `sharepacks/_predictive/2026-01-15/OntarioCanada4/candidate_universe__tool_only__stable10.json`
- CU evidence (provenance): `sharepacks/_predictive/2026-01-15/OntarioCanada4/candidate_universe_evidence__tool_only__stable10.csv`
- Signals bundle: `sharepacks/_predictive/2026-01-15/OntarioCanada4/signals_bundle__tool_only__stable10.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.json`

Interpretation (why this matters):
- **Evidence posture worked** (CU touched the winner lane).
- **Selection retained the lane** (Play Card touched the lane).
- **Conversion was shallow** on the winner lane (`winner_lane_lines=1`), so strict hit didn’t happen at B36.

This is the “conversion geometry” problem in its cleanest form.

---

### B) Evening (OntarioCanada4, winner_label=Evening)

Winner facts:
- winner straight: `791`
- canonical: `179`
- lane (VTRAC index): `22`

1) Did CU union touch the lane?
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__CANDIDATE_UNIVERSE_GRADE__tool_only__stable10.csv`
- Find the `__UNION__` row for OntarioCanada4 + Evening winner `791`.
  - Expected: `vtrac_index_hit=0` and `hit_any=0`

2) Did the Play Card retain the lane at B36 for our strategy?
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PLAY_CARD_GRADE__tool_only__stable10.csv`
- Find the row:
  - `state_key=OntarioCanada4`
  - `winner_label=Evening`
  - `strategy=v0_2_default_multi_pack_packheavy_spine4_index_tail`
  - `budget_label=B36`
  - Expected: `hit_any_inclusive=0`, `vtrac_index_hit=0`, `hit_any=0`

3) Lane allocation confirmation
- Open: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.csv`
- OntarioCanada4 + Evening row (winner `791`)
  - Expected: `cu_union_vtrac_index_hit=0`
  - Expected: `winner_lane_present=0`, `winner_lane_lines=0`

4) Bucket
- This is **CU_MISS** (the evidence posture didn’t touch the lane, so selection can’t “recover” it).
- Cross-check: conversion casebook (same path as above).

Interpretation:
- This is *not* a budgeting/conversion failure; it’s an **evidence recall miss** for that outcome.
- Fixing this requires analyzer/evidence posture work (separate lane of work; not selection geometry).

---

## What this single state teaches (without hand-waving)

Ontario shows both major failure classes in one day:

1) **HIT_INCLUSIVE (Midday)**: we had the neighborhood and kept it, but depth was too shallow to convert.
2) **CU_MISS (Evening)**: the neighborhood never entered CU, so no selection policy can “buy it back”.

This is why we separate:
- analyzer/evidence posture (CU recall)  
from
- selection geometry (budget allocation across lanes and within lanes)

