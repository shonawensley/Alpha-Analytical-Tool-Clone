# Crossroads — Glass‑Box Deep Research Pack (2026‑01‑15; B36‑only)

Purpose: a deterministic, “no hunting” review bundle to get us out of the Crossroads fog by studying one gold day end‑to‑end with **glass‑box visibility**.

This pack is pointer‑only (it links to existing RUNS + sharepacks artifacts; it does not copy/zip them).

## Locked posture (SSOT)

- Gold day anchor: `D=2026-01-15` (Ontario first; multi‑state examples included)
- Profile: `tool_only` (Profit Alerts quarantined)
- Candidate Universe posture: `stable10`
- Budget: `B36` only (no B24 appendix in v1)
- Default strategy under study: `v0_2_default_multi_pack_packheavy_spine4_index_tail`
- Objective (North Star): **isolation-first**
  - Primary: reduce “lane dropped” failures (e.g., `CU_LANE_BUT_PLAY_MISS`)
  - Guardrail: **OOS strict (B36) must not regress** vs baseline scoreboards

## Artifact layers (labeling prevents leakage debates)

- **SSOT (semantics / posture):** definitions + what to trust.
- **PRE (winners‑free evidence):** predictive sharepacks + predictive run reports.
- **DECISION (the squeeze):** glass‑box traces (what we actually selected under B36).
- **TRUTH (measured outcomes):** scoreboards/ladders/casebooks (windowed grading).
- **POST (winner‑aware forensics):** MV reports + winners HTML/JSON (used only to audit/spec).

## Start here (fast path)

1) Read this pack’s case index:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

2) Read SSOT flow + glossary:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

3) Use the prompt (copy/paste to ChatGPT Pro):
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`

## If ChatGPT Pro can’t open the examples

Deep Research typically cannot open `sharepacks/` and dated `RUNS/` outputs via “repo access” because they are gitignored by default. Use an upload export zip instead (command is included at the top of the prompt).

If Deep Research still can’t open zip contents reliably, fall back to the “7-file minimal truth layer” upload described in:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`
You can generate a ready-to-upload mini bundle with:
- `python3 scripts/tools/export_crossroads_truth_layer_mini_pack.py --force`

## What “done” looks like

- We can explain, for each bucket case, **where the miss happens** (CU miss vs lane dropped vs exact dropped).
- We produce 1–2 **selection-layer** changes (no analyzer edits) with explicit promotion gates against the OOS scoreboard.
