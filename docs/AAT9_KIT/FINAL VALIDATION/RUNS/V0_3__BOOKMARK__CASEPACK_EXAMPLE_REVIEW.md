# Bookmark — Casepack Example Review (Pause/Resume)

Purpose: you can pause example review work and later resume in minutes without re-learning where artifacts live.

## What you do when you come back (5-minute re-entry)

1) Open the packs index (what exists + why):
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`

2) Open a casepack manifest and follow the “Open order” section:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/casepack__C035__NewYork4__2026-01-06/MANIFEST.md`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/casepack__C036__Delaware4__2026-01-02/MANIFEST.md`

3) In VS Code, open the manifest in Markdown Preview (`Ctrl+Shift+V`) so links are clickable.

4) For Winners HTML, open in a browser (not just editor source):
- Easiest: “Reveal in File Explorer” → open the `.html` in your browser.
- Or: run a local server (`python3 -m http.server 8000`) and use the `http://localhost:8000/...` URL shown in the manifest.

## The standard artifact set (so you don’t second-guess)

Every casepack manifest includes:

- **Pre-draw evidence (what the system knew)**
  - Predictive `aux_summary` (PRE snapshot; check `excel:` line)
  - Predictive Candidate Universe + evidence (what was eligible + why)
  - Predictive Play Card(s) (what would have been played under B12/B24/B36)

- **Post-draw receipts (what actually happened)**
  - MV run report (filled template)
  - Winners HTML/JSON (frozen evidence; canonical + VTRAC index)
  - Posted results line (`data/results/<D>.txt`)
  - Truth-layer grading rows (`...PORTFOLIO_VS_RESULTS...csv`)

## Why these two teaching cases matter (macro summary)

- `C035` (NewYork4, 2026-01-06 Evening): **lane drop**
  - CU barely touches the winner lane, so B36 gives it 0 lines.
- `C036` (Delaware4, 2026-01-02 Evening): **within-lane miss**
  - CU contains the winner lane + canonical, but B36 spends lines on the wrong member(s).

## Optional: when you want “physical packs” (upload/zip)

If you need a single folder/zip to share with an external model, use:
- `python3 scripts/tools/export_chatgpt_research_pack.py --mode curated --include-predictive --zip`

(Start from `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md` for common flag patterns.)

