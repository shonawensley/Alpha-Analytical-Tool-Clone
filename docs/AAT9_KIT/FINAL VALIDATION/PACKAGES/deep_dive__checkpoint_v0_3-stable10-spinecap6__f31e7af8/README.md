# Deep Dive Pack (Checkpoint-Pinned)

Purpose: give you a **single, checkpoint-pinned workspace** for manual deep dive so you don’t have to hunt across hundreds of `RUNS/` files and wonder “am I looking at the latest system?”

This pack is **navigation + freshness guarantees**, not duplicated artifact copies.

---

## 0) Checkpoint anchors (what “latest system” means)

- Git branch: `checkpoint/v0_3-stable10-spinecap6`
- Git commit: `f31e7af8`
- SSOT policy (default posture + promoted B36 baseline strategy):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- Promoted baseline tag (forensic key; must be present in Play Card JSON):
  - `tail_xlens_inject_methods18_packs22`
- Promotion receipt:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAIL_XLENS_INJECT_METHODS18_PACKS22_PROMOTION__2026-02-18.md`

---

## 1) Golden rule (prevents stale deep dives)

Treat a state/day as “current baseline behavior” only if:
- `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json` contains the substring `tail_xlens_inject_methods18_packs22`

The manifest enforces this rule (column `promoted_tag_present`).

---

## 2) What’s inside this pack

- `MANIFEST.csv`
  - One row per `(date, state)` under `sharepacks/_predictive/`
  - Links to the canonical artifacts you actually open during a deep dive:
    - PRE (predictive evidence): play card, signals bundle, CU evidence
    - POST (winner-aware forensics): MV report + winners HTML folder
  - Includes `generated_at` from Play Card JSON so you can sanity-check recency.

- `portfolio/`
  - Per-day portfolio snapshots regenerated into this pack so the B36 “defaults” surface matches the **current promoted baseline** (instead of relying on potentially stale `RUNS/*__PREDICTIVE_PORTFOLIO__tool_only.md`).

---

## 3) Included dates (derived from `sharepacks/_predictive/`)

This pack includes exactly the date directories present under `sharepacks/_predictive/`.

Known gap:
- `2026-01-19` is missing (upstream Sunday ingest issue); it is intentionally skipped.

---

## 4) Quick start (broad → narrow, Ontario example)

1) Broad triage (ranked states for the day):
   - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8/portfolio/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only__DEEP_DIVE.md`
2) What the baseline would play (canonical source of truth):
   - `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.json`
   - Search within that JSON for `tail_xlens_inject_methods18_packs22`, then read `B36.combos`.
3) Why it played that (provenance):
   - `sharepacks/_predictive/2026-01-15/OntarioCanada4/signals_bundle__tool_only__stable10.json`
   - `sharepacks/_predictive/2026-01-15/OntarioCanada4/candidate_universe_evidence__tool_only__stable10.csv`
4) What actually happened (post-results forensic layer):
   - MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md`
   - Winners HTML: `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/`

---

## 5) Helpful maps (so you don’t spiral)

- Artifact map (PRE → DECISION → TRUTH → POST):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__SIDE_REVIEW_GUIDE__ARTIFACTS.md`
- Portal (broader navigation):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

---

## 6) Baseline “truth-layer” receipts (windows + scoreboards)

If you want the measured performance receipts (not per-day intuition), start here:
- Jan window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
- OOS window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
- Holdout A: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
- Holdout B: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`

