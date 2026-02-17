# Savepoint — Crossroads Pack v1 (stable10 • tool_only • B36) — 2026‑02‑13 (updated 2026‑02‑17)

Purpose: a power-off safe, **tracked** “resume card” so you can reboot, re-open the repo, and immediately know:
- what branch/commit contains the Crossroads work,
- what to upload to ChatGPT Pro Deep Research,
- and what files to open first to avoid re-entering jargon loops.

---

## Repo state (tracked)

- Branch: `checkpoint/v0_3-stable10-spinecap6`
- Latest: (run `git log -1 --oneline` to confirm; this savepoint was updated 2026‑02‑17 to include the constraint chooser eval + robustness strict gate v2 + lane-allocation collision fix)

Quick resume commands:

```bash
git checkout checkpoint/v0_3-stable10-spinecap6
git pull
```

---

## Upload pack (untracked; regeneratable)

Deep Research cannot reliably open `sharepacks/` + dated `RUNS/` outputs via “repo access”, so we use an export zip.

- Upload this file:
  - `sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK_v4.zip`
  - SHA256: `4a768eeddef3b87fb6bf8da41a2ab6fdd6634f1980cd2af8294c9ebbbfa1067d`

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
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_PROMOTION__2026-02-14.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP_SWEEP__2026-02-14.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__DELTA__CLASSIC_DEEP_ANALYSIS__TO__CROSSROADS_TRUTH_LAYER.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6644_PROMOTION__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6644_PROMOTION__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6633_EVAL__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6633_EVAL__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6643_EVAL__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6643_EVAL__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__ROBUSTNESS_WINDOWS__2026-02-16.md" \
  --include-path "docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_EVAL__2026-02-16.md" \
  --out "sharepacks/_scratch/crossroads_glass_box__2026-01-15__UPLOAD_PACK_v4" \
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
- Robustness strict gate (FEB17 onward): count-based material regress for strict hits on small‑N robustness windows (see SSOT policy).
- Current promoted B36 geometry (isolation-first): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md`
- Latest evaluation (tail representative quality; not promoted):
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md`
- Robustness baselines (adds Holdout A/B windows; baseline-only truth):
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__ROBUSTNESS_WINDOWS__2026-02-16.md`
- Latest evaluation (split chooser; not promoted):
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_EVAL__2026-02-16.md`
- Latest evaluation (constraint chooser; not promoted):
  - Brief: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_CONSTRAINT_CHOOSER_EVAL__2026-02-17.md`

---

## Open these first (60-second re-entry)

1) Pack index + cases:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

2) “One table / one memo” clarity shortcuts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CODEX_DEEP_RESEARCH__CROSSROADS__2026-01-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_PROMOTION__2026-02-14.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_HYBRID_SPINECHOOSER__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_HYBRID_SPINECHOOSER__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6644_PROMOTION__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6644_PROMOTION__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_TAIL_SCORE_FIRST_SWEEP__2026-02-16.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6633_EVAL__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6633_EVAL__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6643_EVAL__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6643_EVAL__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md`
 - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md`

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
