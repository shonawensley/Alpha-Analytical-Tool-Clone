# CODEX HANDOFF — CURRENT FOCUS (AAT9)

This file is the **handoff SSOT** for a fresh Codex CLI/chat session.

Read in order:
1) `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`
2) `briefings/CODEX_HANDOFF__CURRENT_FOCUS.md` (this file)

---

## TL;DR

- **Profit Alerts revamp:** complete (including compound-event tracking). Treat as “shadow layer”; do not rework unless explicitly asked.
- **Current focus:** fix the “missing middle” between tool outputs and budgeting by building a real **analysis / aggregator arena** (EDO → CEG → DPL).
- **Stable is the starting point:** Stable emits rich evidence (row/compound/family/long canonicals), but predictive ingestion currently uses `stable_top`, which is a narrow **3‑digit-only** top-caller.
- **Goal:** preserve raw/long evidence, attach lane/canonical transforms non-destructively, score convergence *before* Play Cards spend decisions.

Status at this checkpoint: **planning + investigation complete; implementation not started yet.**

---

## Why we’re here (the bottleneck in plain English)

We’re frequently able to “see the winner neighborhood” upstream (lane/family/digits), but we lose conversion under a fixed budget surface (Play Cards B12/B24/B36).

The core correction is architectural:
- analyzers/tools generate **evidence**
- an aggregator builds **EDO + CEG**
- only then does a deterministic **DPL** decide play mode + caps (budgeting is downstream)

Reference definitions (official):
- `tasks/IMPORTANT_SUPERBRAIN_GUIDE.txt:398` (EDO)
- `tasks/IMPORTANT_SUPERBRAIN_GUIDE.txt:416` (CEG)
- `tasks/IMPORTANT_SUPERBRAIN_GUIDE.txt:434` (DPL)

---

## Evidence receipts (Stable under-consumption is real)

Stable emits long canonicals and lane/family context:
- Example day/state: `sharepacks/_predictive/2026-01-06/NewYork4/stable/NewYork4/`
  - `NewYork4_stable_patterns_scores.csv` (row-level)
  - `NewYork4_stable_patterns_compound.csv` (compound roll-up; includes long canonicals)
  - `NewYork4_stable_patterns_families.csv` (lane aggregates + survivors)

But predictive Stable ingestion today is the narrow pack `stable_top`:
- `scripts/tools/create_candidate_universe.py:569` (`_parse_stable_top`)
- Uses `scripts/tools/create_candidate_universe.py:104` (`_normalize_pick3_literal`) which drops anything not exactly **3 digits**
- Meaning: long/extended clusters (len 4–6+) are ignored *before* Superbrain ever sees them.

This matches the guidance in `tasks/STABLE_SUPPORT.txt`: “restore the missing middle; don’t judge Stable by `stable_top`.”

---

## Current deep-dive notebook (where human insights are being logged)

- Running notebook: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_DEEP_EXAMPLE_REVIEW_ANALYSIS.md`
- Casepack bookmark: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__BOOKMARK__CASEPACK_EXAMPLE_REVIEW.md`
- Casepacks index: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`

---

## Approved next build (Stable → Arena → Aggregator → DPL)

### Phase 1 — Stable Arena artifact (non-destructive)

Deliverable (per day/state; experiment-tagged):
- `sharepacks/_predictive/<D>/<STATE>/analysis/stable_arena__tool_only__<tag>.json`
- Optional companion: `...stable_arena__tool_only__<tag>.md` (plain-English “open these files” receipts)

Stable Arena should keep, per variant (Midday/Evening/Combined):
- top row patterns (scores.csv)
- top compound patterns (compound.csv)
- top family/lane evidence + survivors (families.csv; e.g. `last_remaining_3v`)
- long canonicals preserved “as extracted”
- lane-vote summaries (non-destructive transforms)

### Phase 2 — New Stable-derived Candidate Universe packs (keep `stable_top`)

Add optional pack builders (default off; behind `--experiment-tag`):
- `stable_compound_top` (from compound.csv; includes long→lane vote/closure seeding)
- `stable_family_top` (from families.csv; bounded lane closure seeds)
- `stable_last_remaining` (survivor-focused lane seeds)

Key bounded operator:
- long cluster → lane vote → small gradeable closure seed pack (cap cost units)

### Phase 3 — Aggregator “middle” artifacts

Write experiment-tagged:
- `analysis/edo__tool_only__<tag>.json`
- `analysis/ceg__tool_only__<tag>.json`

### Phase 4 — DPL after EDO/CEG (budgeting stays downstream)

Write experiment Play Cards (do not replace baseline):
- `play_card__tool_only__<tag>.json`

### Phase 5 — Case-driven validation (no guessing)

Use known hard cases (e.g., NY “lane drop”) to measure:
- Evidence recall (did CU contain winner lane/canonical?)
- Conversion (did B36 retain lane and buy meaningful depth?)
- Cost impact (caps)

---

## Two decisions to ask the user immediately (do not assume)

1) Lane closure cap: default to ~24 perms (full doubles closure) vs tighter (12–18) unless multi-tool convergence?
2) Stable compound top-N: start 15 per variant vs 8–10 to keep CU lean?

---

## Working conventions (keep changes safe)

- Always run from repo root: `/home/ser/code/Alpha-Analytical-Tool-Clone`
- Minimal diffs; experiment-tag everything.
- Don’t refactor analyzers broadly; treat them as evidence generators.
- Don’t touch Profit Alerts integration unless explicitly requested.
- Prefer new artifacts in `sharepacks/_predictive/<D>/<STATE>/analysis/` so review is 1-click.

