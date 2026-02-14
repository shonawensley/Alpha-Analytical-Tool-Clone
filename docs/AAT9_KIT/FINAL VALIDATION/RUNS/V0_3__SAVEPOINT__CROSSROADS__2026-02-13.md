# Savepoint — Crossroads Pack v1 (stable10 • tool_only • B36) — 2026‑02‑13

Purpose: a power-off safe, **tracked** “resume card” so you can reboot, re-open the repo, and immediately know:
- what branch/commit contains the Crossroads work,
- what to upload to ChatGPT Pro Deep Research,
- and what files to open first to avoid re-entering jargon loops.

---

## Repo state (tracked)

- Branch: `checkpoint/v0_3-stable10-shoulder-depth`
- Tip: run `git log -1 --oneline` to confirm the current branch tip

Quick resume commands:

```bash
git checkout checkpoint/v0_3-stable10-shoulder-depth
git pull
```

---

## Upload pack (untracked; regeneratable)

Deep Research cannot reliably open `sharepacks/` + dated `RUNS/` outputs via “repo access”, so we use an export zip.

- Upload this file:
  - `sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK.zip`
  - SHA256: `2d53bf4664842eebc665fb0f92511ac586ca240538b92ec3170e74f9c78065e2`

If it’s missing, regenerate (repo root):

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

If Deep Research can’t open zip contents (or can’t access the checkpoint branch), use the **7-file minimal truth layer** instead:

```bash
python3 scripts/tools/export_crossroads_truth_layer_mini_pack.py --force
```

Then upload either:
- `sharepacks/_scratch/crossroads_truth_layer_mini__2026-01-15/BUNDLE.md` (1 file), plus
- `sharepacks/_scratch/crossroads_truth_layer_mini__2026-01-15/PROMPT.md` (copy/paste prompt).

---

## What’s locked (do not reopen during Crossroads v1)

- Gold day anchor: `D=2026-01-15` (Ontario teaching case; multi-state examples included)
- Profile: `tool_only`
- Candidate Universe posture: `stable10`
- Budget: **B36 only** (Crossroads Pack v1)
- Objective: **isolation-first** (reduce `CU_LANE_BUT_PLAY_MISS`)
- Guardrail: **OOS strict B36 must not regress**
- **No analyzer edits** in this phase (selection-layer only).
- Current promoted B36 geometry (isolation-first): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_PROMOTION__2026-02-14.md`

---

## Open these first (60-second re-entry)

1) Pack index + cases:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

2) “One table / one memo” clarity shortcuts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CODEX_DEEP_RESEARCH__CROSSROADS__2026-01-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_PROMOTION__2026-02-14.md`

3) SSOT semantics (prevents spirals):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__DELTA__CLASSIC_DEEP_ANALYSIS__TO__CROSSROADS_TRUTH_LAYER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

4) If you feel lost, open the portal:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

---

## Next action (when you’re ready)

Upload the zip to ChatGPT Pro Deep Research and paste:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`
