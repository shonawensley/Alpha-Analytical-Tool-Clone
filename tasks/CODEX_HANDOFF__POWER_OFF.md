# CODEX HANDOFF (Power-off safe) — v0.2 Synthesis Status

Timestamp: 2026-01-16

## Repo state

- Repo root: `/home/ser/code/Alpha-Analytical-Tool-Clone`
- Branch: `checkpoint/gold-days-2025-12-30_to_2026-01-04`
- Latest commits (already pushed to `origin/`):
  - `f85b3146` — Link v0.2 defaults to tool audit decisions
  - `e8f2830c` — Add Aux v0 consumption audit and promote v0.2 posture
  - Prior context commits: `bb9bc425`, `34d6520f`, `5bbda21b`

## Uncommitted work since the above commits

- Enforced “tool_only by default” across prediction/rollup scripts (Profit Alerts quarantined unless explicitly requested).
- Regenerated tool_only grading/rollups for the v0 Jan window (`2026-01-05` → `2026-01-09`) and produced per-state predictive RUNS (`__PREDICTIVE__tool_only.md`) for all tracked states/days.
- Added a new Play Card strategy experiment (`conversion_box_first`) and logged the negative result (helps vtrac_index_hit but hurts hit_any in v0 window).

## What changed (high level)

- Added Aux v0 consumption audit docs (quant + cases + feature decisions) and wired them into RUNS navigation + v0.2 defaults.
- v0.2 defaults now link to **all** tool audit decision docs (DR/Aux/Stable/Hot Zones/VTRAC).

## Key files to open first (map)

- RUNS portal (navigation): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- v0.2 defaults (what “the system” does by default): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Gold capture ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`

## Aux audit outputs (new)

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`

## Working tree note

- Tracked files have **uncommitted** changes (scripts + docs + RUNS outputs); `git status -sb` also shows lots of **untracked** artifacts (sharepacks, scratch tasks, and extra `data/results/*.txt`).
- No sharepacks are intended to be committed in this sprint; keep any future commit strictly `scripts/` + `docs/` (+ RUNS markdown/csv as desired).
