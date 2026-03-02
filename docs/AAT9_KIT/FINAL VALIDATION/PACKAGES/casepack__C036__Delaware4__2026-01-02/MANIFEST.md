# Case Pack — C036 — Delaware4 — D=2026-01-02 (Evening winner `076`)

Purpose: make this example **1-click navigable** (no chasing artifacts). This is a **within-lane miss** teaching case.

Tip: open this file in a Markdown preview so the links are clickable (VS Code: `Ctrl+Shift+V`). In the editor view, use `Ctrl/Cmd+click`.

Viewing winners HTML: the links below open the `.html` file (often as source in your editor). To see the rendered page in your browser:
1) Easiest: right-click the `.html` file → “Reveal in File Explorer” → open it in your browser.
2) Or: run a local server from repo root (`python3 -m http.server 8000`) and open the `http://localhost:8000/...` URL listed under the HTML link.

## What this case is demonstrating (plain English)
- Winner: `076` → canonical `067` → VTRAC index `7`
- Candidate Universe (CU) contains the winner lane (idx `7`) and includes the winner canonical `067`.
- Baseline B36 keeps idx `7` (lane retained) but spends lines on the wrong member(s) (notably `017`), so it misses the canonical.
- Closure strategies don’t automatically fix this because idx `7` is an **all-singles** lane (no cheap doubles to “close” the family).

## Open order (click these, in order)

### A) Broad context (day-level)
- Portfolio (baseline): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only.md](../../RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only.md) (start at line 1)
- Portfolio (dc1 B36): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md](../../RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md) (start at line 1)
- Posted results (Delaware line): [data/results/2026-01-02.txt](../../../../../data/results/2026-01-02.txt) (line 8)
- Graded summary (baseline; window file): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md) (start at line 1)
- Graded summary (dc1 B36; window file): [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md) (start at line 1)
- Truth rows (baseline; Delaware4 Evening):
  - B12: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv) (line 101)
  - B24: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv) (line 102)
  - B36: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv) (line 103)
- Truth rows (dc1; Delaware4 Evening):
  - B12: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv) (line 101)
  - B24: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv) (line 102)
  - B36: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv](../../RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv) (line 103)

### B) Deep receipts (state-level; this is the “why”)
- MV run report: [docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Delaware4.md](../../RUNS/2026-01-02__Delaware4.md) (start at line 1)

### C0) Aux snapshot (PRE; what Aux “knew” pre-results)
- Aux Summary (predictive; human): [sharepacks/_predictive/2026-01-02/Delaware4/aux/Delaware4/summary.md](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/aux/Delaware4/summary.md) (start at line 1)
- Aux Summary (predictive; JSON): [sharepacks/_predictive/2026-01-02/Delaware4/aux/Delaware4/summary.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/aux/Delaware4/summary.json) (start at line 1)

### C) Winners lens (environment view; human-first)
- Winners HTML (Evening winner): [sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.html](../../../../../sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.html) (start at line 1)
  - Browser URL (if server running): http://localhost:8000/sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.html
- Winners JSON (Evening winner): [sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.json](../../../../../sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.json) (start at line 1)
- (Optional) Winners digest: [sharepacks/2026-01-02/Delaware4/winners/Delaware4/digest.md](../../../../../sharepacks/2026-01-02/Delaware4/winners/Delaware4/digest.md) (start at line 1)
- (Optional) Midday winner HTML/JSON:
  - [sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.html](../../../../../sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.html) (start at line 1)
    - Browser URL (if server running): http://localhost:8000/sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.html
  - [sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.json](../../../../../sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac17_winner_126_20260105_070859.json) (start at line 1)

### D) Predictive evidence (what we knew pre-results)
- Predictive CU (tool_only): [sharepacks/_predictive/2026-01-02/Delaware4/candidate_universe__tool_only__stable10.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/candidate_universe__tool_only__stable10.json) (start at line 1)
- CU evidence (human-readable): [sharepacks/_predictive/2026-01-02/Delaware4/candidate_universe_evidence__tool_only__stable10.md](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/candidate_universe_evidence__tool_only__stable10.md) (start at line 1)
- (Optional) Signals bundle (tool_only): [sharepacks/_predictive/2026-01-02/Delaware4/signals_bundle__tool_only__stable10.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/signals_bundle__tool_only__stable10.json) (start at line 1)

### E) Play Cards (what we would have played)
- Play Card (baseline JSON): [sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.json) (start at line 1)
- Play Card (baseline human): [sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.md](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.md) (start at line 1)
- Play Card (dc1 JSON): [sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__dc1.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__dc1.json) (start at line 1)
- (Optional) Play Card (doubles-closure v1 JSON): [sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__doubles_closure_v1.json](../../../../../sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__doubles_closure_v1.json) (start at line 1)

## Quick checks (so we stay focused)
1) Confirm winner + lane:
   - In `data/results/2026-01-02.txt`, Delaware Evening is `0-7-6` (winner `076`).
   - In the Winners HTML/JSON, confirm winner canonical is `067` and VTRAC index is `7`.
2) Confirm “CU contained the winner canonical”:
   - In `candidate_universe__tool_only__stable10.json`, search for `067`.
3) Confirm “Play Card kept the lane but missed the member”:
   - In the truth row for B36 (`...PORTFOLIO_VS_RESULTS...csv:103`), confirm `vtrac_index_hit=1` and `in_winner_index=1` (lane retained).
   - In `play_card__tool_only__stable10.md`, search the B36 block for `017` (present) vs `067` (missing).
4) Label the miss:
   - `MISS_MEMBER_WITHIN_LANE` (lane retained, wrong member(s) allocated).
5) Confirm Aux is pre-results:
   - In `sharepacks/_predictive/2026-01-02/Delaware4/aux/Delaware4/summary.md`, confirm `excel:` points to `Pick3StatsC4_2026-01-01` (yesterday’s upload).
