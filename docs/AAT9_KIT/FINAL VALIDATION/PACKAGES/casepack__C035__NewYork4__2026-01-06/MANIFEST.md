# Case Pack — C035 — NewYork4 — D=2026-01-06 (Evening winner `342`)

Purpose: make this example **1-click navigable** (no chasing artifacts). This is a **lane-drop** teaching case.

Tip: open this file in a Markdown preview so the links are clickable (VS Code: `Ctrl+Shift+V`). In the editor view, use `Ctrl/Cmd+click`.

Viewing winners HTML: the links below open the `.html` file (often as source in your editor). To see the rendered page in your browser:
1) Easiest: right-click the `.html` file → “Reveal in File Explorer” → open it in your browser.
2) Or: run a local server from repo root (`python3 -m http.server 8000`) and open the `http://localhost:8000/...` URL listed under the HTML link.

## What this case is demonstrating (plain English)
- Winner: `342` → canonical `234` → VTRAC index `30`
- Candidate Universe (CU) barely touches idx `30` (only a single member).
- Baseline B36 allocates **0 lines** to idx `30` (lane dropped) → strict miss.
- dc1/closure strategies cannot help if the lane gets **0 lines**.

## Open order (click these, in order)

### A) Broad context (day-level)
- Portfolio (baseline): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only.md](../../RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only.md) (start at line 1)
- Portfolio (dc1 B36): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md](../../RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md) (start at line 1)
- Posted results (New York line): [data/results/2026-01-06.txt](../../../../../data/results/2026-01-06.txt) (line 28)
- Graded summary (baseline): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06_to_2026-01-06__PORTFOLIO_VS_RESULTS__tool_only.md](../../RUNS/2026-01-06_to_2026-01-06__PORTFOLIO_VS_RESULTS__tool_only.md) (start at line 1)
- Graded summary (dc1 B36; window file): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md) (start at line 1)
- Truth row (baseline B36): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06_to_2026-01-06__PORTFOLIO_VS_RESULTS__tool_only.csv](../../RUNS/2026-01-06_to_2026-01-06__PORTFOLIO_VS_RESULTS__tool_only.csv) (line 25)
- Truth row (dc1 B36; window file): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv) (line 445)

### B) Deep receipts (state-level; this is the “why”)
- MV run report: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewYork4.md](../../RUNS/2026-01-06__NewYork4.md) (start at line 1)

### C0) Aux snapshot (PRE; what Aux “knew” pre-results)
- Aux Summary (predictive; human): [sharepacks/_predictive/2026-01-06/NewYork4/aux/NewYork4/summary.md](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/aux/NewYork4/summary.md) (start at line 1)
- Aux Summary (predictive; JSON): [sharepacks/_predictive/2026-01-06/NewYork4/aux/NewYork4/summary.json](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/aux/NewYork4/summary.json) (start at line 1)

### C) Winners lens (environment view; human-first)
- Winners HTML (Evening winner): [sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.html](../../../../../sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.html) (start at line 1)
  - Browser URL (if server running): http://localhost:8000/sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.html
- Winners JSON (Evening winner): [sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.json](../../../../../sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.json) (start at line 1)
- (Optional) Winners digest: [sharepacks/2026-01-06/NewYork4/winners/NewYork4/digest.md](../../../../../sharepacks/2026-01-06/NewYork4/winners/NewYork4/digest.md) (start at line 1)

### D) Predictive evidence (what we knew pre-results)
- Predictive CU (tool_only): [sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe__tool_only__stable10.json](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe__tool_only__stable10.json) (start at line 1)
- CU evidence (human-readable): [sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe_evidence__tool_only__stable10.md](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe_evidence__tool_only__stable10.md) (start at line 1)

### E) Play Cards (what we would have played)
- Play Card (baseline JSON): [sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.json](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.json) (start at line 1)
- Play Card (baseline human): [sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.md](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.md) (start at line 1)
- Play Card (dc1 JSON): [sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__dc1.json](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__dc1.json) (start at line 1)
- (Optional) Play Card (doubles-closure v1 JSON): [sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__doubles_closure_v1.json](../../../../../sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__doubles_closure_v1.json) (start at line 1)

## Quick checks (so we stay focused)
1) Confirm winner + lane:
   - In `data/results/2026-01-06.txt`, New York Evening is `342`.
   - In the Winners HTML/JSON, confirm VTRAC index is `30`.
2) Confirm “CU barely touched idx30”:
   - In `candidate_universe__tool_only__stable10.json`, search `union_combos` for `379` (it should be the only idx30 member).
3) Confirm “Play Card dropped the lane”:
   - In `play_card__tool_only__stable10.md`, search the B36 block for `379` (it is missing).
4) Label the miss:
   - `MISS_LANE_DROP` (lane got 0 lines).
5) Confirm Aux is pre-results:
   - In `sharepacks/_predictive/2026-01-06/NewYork4/aux/NewYork4/summary.md`, confirm `excel:` points to `Pick3StatsC4_2026-01-05` (yesterday’s upload).
