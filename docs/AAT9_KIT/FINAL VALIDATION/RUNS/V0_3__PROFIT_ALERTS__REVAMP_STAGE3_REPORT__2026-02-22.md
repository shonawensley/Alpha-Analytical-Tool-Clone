# V0.3 — Profit Alerts Revamp (Quarantined) — Stage 3 Report

Timestamp (UTC): `2026-02-22`

Scope:
- Profit Alerts (A01–A12) only (quarantined; **does not** touch `tool_only` selection/analyzers).
- Stage 3 goal is **provenance + portability**: make manual audits and Deep Research deterministic without relying on local `sharepacks/`.

Hard invariants:
- No analyzer edits (Stable/DR/Hot Zones/VTRAC unchanged).
- No changes to `tool_only` posture or play-card selection.
- No overwrite footguns: window outputs are label-suffixed.

## What Stage 3 adds (vs Stage 2)

Stage 2 gave us: rollups + integrity + deterministic casebooks.

Stage 3 adds two missing pieces that blocked “deep research” and fast human audits:

1) **Stable provenance locators** embedded into each `profit_alerts.csv` row’s `Evidence` JSON:
   - `stable_scores_relpath`
   - `stable_section`, `stable_set`, `stable_draw`, `stable_column`
   - `stable_family_id`, `stable_why`
   - Plus consensus-stub locators for cross-variant tail consensus alerts (`stub_*`) and `vtrac_index` for A09.

2) **Machine-readable case roster** for automation:
   - `CASES.csv` emitted by the casebook generator (one row per curated case with file pointers + locators).

3) **Portable “evidence packs”** (GitHub-visible mirrors):
   - Because root `sharepacks/` are intentionally gitignored (large/local), Deep Research agents can’t inspect them.
   - Evidence packs mirror only the minimal `sharepacks/<D>/...` files needed for the curated cases into `docs/.../PACKAGES/...`.

## Scripts changed / added

- Exporter (adds locator/provenance fields into `Evidence` JSON):
  - `scripts/tools/export_control_center_sharepack.py`
- Casebook generator (prints locators + emits `CASES.csv`):
  - `scripts/tools/create_profit_alerts_casebook.py`
- New evidence-pack exporter (builds GitHub-visible minimal mirrors):
  - `scripts/tools/export_profit_alerts_evidence_pack.py`

## Outputs (Stage 3 packages)

Two windows (same as Stage 2):
- “Known-good mini corpus”: `2025-06-21..2025-06-23`
- “Reported-bad window”: `2025-12-30..2026-01-09`

For each window there are now **two** package types:

### A) Revamp packages (truth layer + casebooks + locators)

- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/`

Each contains:
- `CASEBOOK.md` (now includes Stable locator + consensus-stub locator lines)
- `CASES.csv` (machine-readable; drives evidence-pack export)
- `MANIFEST.md`
- Window rollups + integrity summaries (label `provloc_v1`)

### B) Evidence packs (portable mirrors for Deep Research + bounded audits)

- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/`

Each contains:
- `README.md`, `CASEBOOK.md`, `CASES.csv`
- `sharepacks/<D>/control_center/...` (profit board + eval files)
- `sharepacks/<D>/<StateKey>/winners/<StateKey>/...` (digest + HTML/JSON copies where present)
- `sharepacks/<D>/<StateKey>/json/<StateKey>_tables.json`
- Stable excerpt files: `<StateKey>_stable_patterns_scores__profit_alerts_excerpt.csv` for cases that have stable locators

## How to use (fast path)

If you want a deterministic manual audit or a Deep Research attachment:

1) Pick a window’s evidence pack and open `CASEBOOK.md`.
2) For any case:
   - open the mirrored `profit_alerts_eval.csv` row (by `row_num`)
   - open the mirrored `profit_alerts.csv` row and inspect `Evidence` JSON
   - open the mirrored winners HTML/JSON + `*_tables.json`
   - open the Stable excerpt and confirm the locator matches the case

## Why this matters

Stage 3 eliminates the “can’t find the exact evidence row” problem:
- You no longer have to search Stable by text; the casebook tells you exactly which `(section, Set, Draw, Column)` row fired.
- Deep Research no longer fails due to missing local sharepack access: the evidence pack is repo-visible and bounded.

## Recommended next step (Stage 4 decision)

Now that provenance is solved, the next step should be **one** of:

1) **Corpus expansion** (stabilize small-N): run Stage 2/3 suite on a larger recent window.
2) **Targeted tuning** (only if audits show misalignment): change one alert rule/threshold at a time and re-grade via the same rollup lenses.

Do not stack: keep Profit Alerts quarantined until we can point to concrete, casebook-backed improvements.

