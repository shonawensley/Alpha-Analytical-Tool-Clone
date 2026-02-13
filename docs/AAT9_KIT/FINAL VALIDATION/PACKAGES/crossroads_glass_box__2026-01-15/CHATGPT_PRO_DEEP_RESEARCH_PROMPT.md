# ChatGPT Pro — Deep Research Prompt (Crossroads Glass‑Box; 2026‑01‑15; B36‑only)

## Mission

Resolve the “Crossroads” question with evidence, not vibes:
- **Where** do we lose wins? (CU miss vs lane dropped vs exact dropped)
- What does the current **budget geometry** (B36) imply about breadth vs depth?
- What are the smallest **selection-layer** changes (no analyzer edits) that improve isolation-first outcomes without regressing OOS strict?

## Access check (must pass; otherwise stop)

This prompt requires the actual Crossroads artifacts (traces/scoreboards/sharepacks). If you only have “repo access”, you may not be able to open them because many `sharepacks/` and dated `RUNS/` outputs are not versioned by default.

Minimum files you must be able to open:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__OntarioCanada4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

If you cannot open these, stop and request an uploaded export zip generated with:

```bash
python3 scripts/tools/export_chatgpt_research_pack.py \
  --mode window --dates 2026-01-15 2026-01-16 \
  --states OntarioCanada4 NewYork4 NorthCarolina4 Delaware4 \
  --profile tool_only --experiment-tag stable10 --include-predictive --include-control-center \
  --extra-window 2026-01-15:2026-01-22 \
  --extra-window 2026-01-01:2026-01-09 \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_SYNTHESIS__2026-01-15.md" \
  --out "sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK" \
  --zip
```

## Locked constraints (do not violate)

- **No analyzer edits** (Stable/DR/VTRAC/Hot Zones). Assume analyzers are evidence producers.
- Stay winners‑safe: predictive sharepacks (`sharepacks/_predictive/...`) are winners‑free; MV + winners HTML are post‑results forensics/spec only.
- **Budget is fixed:** `B36` only in this pack.
- Posture: `tool_only` + `stable10`.
- Baseline strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail`.
- Objective: **isolation-first**
  - Primary: reduce lane-dropped failure modes (esp. `CU_LANE_BUT_PLAY_MISS`)
  - Guardrail: **OOS strict (B36) must not regress** vs baseline scoreboards.

## Read order (strict)

1) Pack index:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/MANIFEST.md`

2) SSOT semantics:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_ROADMAP.md`

3) TRUTH layer (scoreboards + buckets):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36.md`

4) For each of the 5 cases (from `CASES.md`), do the 3‑view triangulation:
- PRE: `...__PREDICTIVE__tool_only.md`
- DECISION: `...__GLASS_BOX_TRACE__...__B36__stable10.md`
- POST: `.../<D>__<STATE>.md` + the specific winners HTML link

## Deliverables (copy/pasteable, structured)

1) **One‑page plain-English budget explainer**
- What B36 means (lines), what “lane” means (VTRAC index), what packs/spine/tail mean, and where the squeeze happens.

2) **Bucket anatomy summary (from the 5 cases)**
- For each bucket: what is the typical mechanical failure signature?
- Explicitly separate: evidence problem (CU miss) vs selection problem (lane dropped / exact dropped).

3) **Isolation-first shoe design memo**
- Based on the cases + lane allocation reports: what breadth/depth geometry is implied?
- What should be treated as “spine” (must retain) vs “tail” (hedge / keep lane visibility)?

4) **Two minimal selection-layer improvements (no analyzers)**
Each proposal must include:
- What to change (in Play Card selection geometry; not analyzer logic)
- What metrics should improve (name the exact scoreboard columns)
- Promotion gate:
  - Must improve isolation-first goal in the Jan window
  - Must **not regress** OOS strict B36 vs baseline scoreboards

5) **Top 5 “spiral triggers”**
- List the 5 most common ways humans misread these artifacts and how to prevent it (by pointing to specific SSOT docs).
