# CODEX HANDOFF (Power-off safe) — Crossroads “Glass-Box” Savepoint

Timestamp: 2026-02-13

Goal of this savepoint:
- Preserve the **Crossroads Pack v1** (D=2026-01-15, stable10, tool_only, B36-only).
- Ensure ChatGPT Pro Deep Research can open the actual artifacts (via an upload zip).
- Leave a clean “resume map” so we don’t re-enter spiral loops after a reset.

## Repo state (tracked; safe)

- Repo root: `/home/ser/code/Alpha-Analytical-Tool-Clone`
- Branch: `checkpoint/v0_3-stable10-shoulder-depth`
- HEAD: `a9da24a9` (`Crossroads: add tracked savepoint resume doc`)
- Remote: `origin` (branch pushed and up to date)
- Working tree: clean (`git status -s` empty)

## The one file to upload to ChatGPT Pro Deep Research (untracked; regeneratable)

- Upload zip: `sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK.zip`
  - Size: ~2.8MB
  - SHA256: `2d53bf4664842eebc665fb0f92511ac586ca240538b92ec3170e74f9c78065e2`

This zip is **not** committed by design (it includes `sharepacks/` + dated `RUNS/` outputs).
If it goes missing, regenerate it from repo root:

```bash
python3 scripts/tools/export_chatgpt_research_pack.py \
  --mode window --dates 2026-01-15 2026-01-16 \
  --states OntarioCanada4 NewYork4 NorthCarolina4 Delaware4 \
  --profile tool_only --experiment-tag stable10 --include-predictive --include-control-center \
  --extra-window 2026-01-15:2026-01-22 \
  --extra-window 2026-01-01:2026-01-09 \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_SYNTHESIS__2026-01-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CODEX_DEEP_RESEARCH__CROSSROADS__2026-01-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv" \
  --out "sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK" \
  --zip
```

## “Resume in 60 seconds” (no hunting)

1) Open the pack index + prompt:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`

2) Open the two new “clarity” artifacts:
- Codex deep research mirror memo: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CODEX_DEEP_RESEARCH__CROSSROADS__2026-01-15.md`
- Crossroads case matrix (5 cases, one table): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`

3) If you feel lost, use the SSOT map:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

## What we locked (so we don’t re-open old debates)

- Gold anchor: `D=2026-01-15`
- Posture: `tool_only` + `stable10`
- Budget: **B36 only** (Crossroads Pack v1)
- Objective: **isolation-first** (reduce `CU_LANE_BUT_PLAY_MISS`)
- Guardrail: **OOS strict B36 must not regress**
- No analyzer edits in this phase; selection-layer only.

## What changed since the older (Jan) power-off handoff (high level)

- Deep Research access issue resolved via an upload zip (no more “repo access can’t open sharepacks” confusion).
- Winner lane rank reports regenerated to include the Crossroads baseline strategy.
- Added:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CODEX_DEEP_RESEARCH__CROSSROADS__2026-01-15.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`
  - `scripts/tools/create_crossroads_case_matrix.py`

---

## Archive note

This file replaces an older v0.2-era “power-off” snapshot (2026-01-16). The new project state is Crossroads Pack v1 + stable10 truth-layer instrumentation + upload-pack workflow.
