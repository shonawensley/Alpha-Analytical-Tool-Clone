# DR Gold-Day Winner Audit

- Purpose: winner-aware audit of `DR Arena v1.1` over frozen gold-day sharepacks.
- Dates audited: `2025-06-21, 2025-06-22, 2025-06-23, 2025-12-30, 2025-12-31, 2026-01-01, 2026-01-02, 2026-01-03, 2026-01-04`
- Rows are Midday/Evening state outcomes only; Combined is excluded from grading.

## Overview

| Metric | Count | % |
|---|---|---|
| Rows audited | 245 | 100.0% |
| exact_any > 0 | 92 | 37.6% |
| vtrac_any > 0 | 218 | 89.0% |
| family_vtrac_any > 0 | 159 | 64.9% |
| trace winner VTRAC rank <= 3 | 20 | 8.2% |
| corridor winner VTRAC rank <= 3 | 19 | 7.8% |
| double winner VTRAC rank <= 3 | 18 | 7.3% |
| gateway winner VTRAC rank <= 3 | 19 | 7.8% |
| cluster winner VTRAC rank <= 3 | 23 | 9.4% |
| assigned-box winner VTRAC rank <= 3 | 24 | 9.8% |
| fusion winner VTRAC rank <= 3 | 25 | 10.2% |
| gateway winner VTRAC rank <= 5 | 33 | 13.5% |
| cluster winner VTRAC rank <= 5 | 34 | 13.9% |
| assigned-box winner VTRAC rank <= 5 | 41 | 16.7% |
| fusion winner VTRAC rank <= 5 | 39 | 15.9% |
| gateway winner VTRAC rank <= 8 | 48 | 19.6% |
| cluster winner VTRAC rank <= 8 | 51 | 20.8% |
| assigned-box winner VTRAC rank <= 8 | 68 | 27.8% |
| fusion winner VTRAC rank <= 8 | 57 | 23.3% |
| gateway winner VTRAC rank <= 10 | 52 | 21.2% |
| cluster winner VTRAC rank <= 10 | 55 | 22.4% |
| assigned-box winner VTRAC rank <= 10 | 84 | 34.3% |
| fusion winner VTRAC rank <= 10 | 73 | 29.8% |
| gateway winner VTRAC rank <= 20 | 55 | 22.4% |
| cluster winner VTRAC rank <= 20 | 64 | 26.1% |
| assigned-box winner VTRAC rank <= 20 | 149 | 60.8% |
| fusion winner VTRAC rank <= 20 | 73 | 29.8% |
| best surface winner VTRAC rank <= 3 | 46 | 18.8% |
| best surface winner VTRAC rank <= 5 | 66 | 26.9% |
| best surface winner VTRAC rank <= 8 | 92 | 37.6% |
| best surface winner VTRAC rank <= 10 | 110 | 44.9% |
| best surface winner VTRAC rank <= 20 | 154 | 62.9% |
| winner JSON matched | 244 | 99.6% |
| winner JSON unavailable/unmatched | 1 | 0.4% |
| winner tables strong signal | 243 | 99.2% |
| strong overlay-summary mismatch | 27 | 11.0% |
| moderate overlay-summary mismatch | 0 | 0.0% |

## Alignment Classes

| Class | Count | % |
|---|---|---|
| active_low_trust | 4 | 1.6% |
| false_empty | 15 | 6.1% |
| literal_capture | 92 | 37.6% |
| miss | 8 | 3.3% |
| vtrac_capture | 126 | 51.4% |

## By Date

| Date | Rows | vtrac_any | trace_vtrac_top3 | corridor_vtrac_top3 | gateway_vtrac_top3 | cluster_vtrac_top3 | box_vtrac_top3 | fusion_vtrac_top3 | cluster_vtrac_top10 | box_vtrac_top10 | fusion_vtrac_top10 | best_surface_top10 | winner_json_matched | mismatch>=moderate | strong_signal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-06-21 | 28 | 26 | 4 | 4 | 4 | 5 | 3 | 4 | 8 | 11 | 12 | 16 | 28 | 2 | 28 |
| 2025-06-22 | 25 | 21 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 4 | 4 | 7 | 25 | 4 | 25 |
| 2025-06-23 | 28 | 27 | 0 | 0 | 1 | 2 | 4 | 3 | 5 | 13 | 11 | 13 | 28 | 1 | 28 |
| 2025-12-30 | 28 | 26 | 3 | 3 | 3 | 3 | 2 | 4 | 6 | 8 | 5 | 10 | 28 | 2 | 27 |
| 2025-12-31 | 28 | 26 | 6 | 6 | 5 | 5 | 4 | 5 | 7 | 11 | 11 | 14 | 28 | 2 | 28 |
| 2026-01-01 | 26 | 23 | 4 | 3 | 2 | 3 | 2 | 4 | 10 | 11 | 9 | 15 | 26 | 3 | 26 |
| 2026-01-02 | 28 | 24 | 0 | 0 | 0 | 0 | 5 | 1 | 4 | 11 | 10 | 13 | 28 | 4 | 28 |
| 2026-01-03 | 28 | 25 | 2 | 2 | 3 | 3 | 2 | 4 | 5 | 10 | 6 | 11 | 28 | 3 | 28 |
| 2026-01-04 | 26 | 20 | 1 | 1 | 1 | 2 | 1 | 0 | 6 | 5 | 5 | 11 | 25 | 6 | 25 |

## Strongest False-Empty / Mismatch Cases

| Date | State | Var | Winner | Empty | Mismatch | Signal | JSON | LS signal | Trace VT | Corridor VT |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-03 | NewYork4 | Midday | 243 | positive_trace | strong | strong | matched_literal | 31 | - | - |
| 2025-06-22 | Michigan4 | Evening | 700 | positive_trace | strong | strong | matched_literal | 29 | - | - |
| 2025-06-23 | SouthCarolina4 | Midday | 958 | positive_trace | strong | strong | matched_literal | 28 | - | - |
| 2026-01-04 | NewYork4 | Midday | 793 | positive_trace | strong | strong | matched_literal | 25 | - | - |
| 2025-12-31 | NewYork4 | Evening | 116 | positive_trace | strong | strong | matched_literal | 21 | - | - |
| 2025-06-21 | Virginia4 | Midday | 473 | positive_trace | strong | strong | matched_literal | 29 | - | - |
| 2026-01-02 | NewYork4 | Evening | 256 | positive_trace | strong | strong | matched_literal | 21 | - | - |
| 2026-01-04 | Delaware4 | Evening | 269 | positive_trace | strong | strong | matched_literal | 43 | - | - |
| 2025-12-30 | Delaware4 | Evening | 563 | positive_trace | strong | strong | matched_literal | 43 | - | - |
| 2026-01-02 | Indiana4 | Evening | 359 | positive_trace | strong | strong | matched_literal | 22 | - | - |
| 2026-01-04 | OntarioCanada4 | Midday | 958 | positive_trace | strong | strong | matched_literal | 22 | - | - |
| 2026-01-04 | Delaware4 | Midday | 057 | active_low_trust | strong | strong | matched_literal | 18 | - | - |

## Strongest VTRAC-Lane Captures

| Date | State | Var | Winner | VTRAC idx | trace VT | corridor VT | double VT | gateway VT | cluster VT | box VT | fusion VT | best VT | Signal | JSON | Top corridor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-06-21 | NorthCarolina4 | Midday | 427 | 28 | 1 | 1 | 1 | 1 | 1 | 7 | 2 | 1 | strong | matched_literal | 224 |
| 2025-06-21 | PuertoRico4 | Midday | 910 | 9 | 2 | 2 | 6 | 3 | 3 | 3 | 1 | 1 | strong | matched_literal | 049 |
| 2025-06-21 | SouthCarolina4 | Midday | 069 | 9 | 1 | 1 | 1 | 1 | 2 | 5 | 1 | 1 | strong | matched_literal | 145 |
| 2025-06-23 | NorthCarolina4 | Midday | 920 | 12 | 5 | 5 | 5 | 3 | 3 | 1 | 1 | 1 | strong | matched_literal | 224 |
| 2025-12-31 | Florida4 | Midday | 407 | 12 | 1 | 1 | 3 | 1 | 1 | 8 | 2 | 1 | strong | matched_literal | 259 |
| 2025-12-31 | Indiana4 | Midday | 204 | 12 | 1 | 1 | 1 | 3 | 3 | 15 | 7 | 1 | strong | matched_literal | 259 |
| 2025-12-31 | NewJersey4 | Midday | 366 | 18 | - | - | - | - | - | 1 | 7 | 1 | strong | matched_literal | 225 |
| 2025-12-31 | SouthCarolina4 | Evening | 044 | 15 | 1 | 1 | 1 | 1 | 1 | 4 | 1 | 1 | strong | matched_literal | 599 |
| 2026-01-01 | Connecticut4 | Evening | 109 | 9 | 2 | 2 | 1 | 4 | 3 | 4 | 2 | 1 | strong | matched_literal | 249 |
| 2026-01-01 | Indiana4 | Evening | 909 | 15 | 2 | 2 | 2 | 3 | 3 | 1 | 2 | 1 | strong | matched_literal | 244 |
| 2025-06-21 | Pennsylvania4 | Evening | 360 | 8 | - | - | - | - | - | 2 | 8 | 2 | strong | matched_literal | 024 |
| 2025-12-30 | SouthCarolina4 | Midday | 754 | 12 | 3 | 3 | 5 | 2 | 3 | 8 | 3 | 2 | strong | matched_literal | 559 |

## Visible But Under-Promoted Winner Lanes

| Date | State | Var | Winner | VT idx | cluster rank | cluster band | cluster gap | gateway rank | box rank | fusion rank | best VT | Signal | Top attractor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-03 | Delaware4 | Midday | 422 | 28 | 6 | top8 | 47.839 | 6 | 20 | 8 | 5 | strong | 244 |
| 2026-01-02 | Connecticut4 | Midday | 970 | 12 | 6 | top8 | 54.156 | 6 | 9 | 4 | 4 | strong | 559 |
| 2026-01-02 | PuertoRico4 | Evening | 917 | 22 | 6 | top8 | 66.766 | 4 | 7 | 3 | 3 | strong | 259 |
| 2026-01-04 | Ohio4 | Evening | 492 | 31 | 6 | top8 | 75.244 | 6 | 13 | 9 | 5 | strong | 559 |
| 2026-01-04 | Connecticut4 | Midday | 569 | 9 | 6 | top8 | 81.556 | 6 | 11 | 6 | 6 | strong | 345 |
| 2025-06-22 | Indiana4 | Evening | 702 | 10 | 6 | top8 | 116.13 | 7 | - | - | 6 | strong | 229 |
| 2025-06-23 | PuertoRico4 | Evening | 454 | 15 | 6 | top8 | 137.645 | 6 | 3 | 3 | 3 | strong | 249 |
| 2025-06-22 | Virginia4 | Evening | 938 | 33 | 6 | top8 | 164.054 | - | 16 | - | 6 | strong | 559 |
| 2025-06-22 | Florida4 | Midday | 330 | 13 | 7 | top8 | 17.724 | 6 | 7 | 4 | 3 | strong | 049 |
| 2026-01-02 | Florida4 | Evening | 589 | 14 | 7 | top8 | 86.627 | 7 | 17 | 8 | 7 | strong | 259 |
| 2025-12-31 | Ohio4 | Evening | 197 | 22 | 7 | top8 | 95.71 | 7 | 15 | 9 | 7 | strong | 299 |
| 2025-06-23 | Florida4 | Midday | 665 | 6 | 8 | top8 | 31.64 | 9 | 5 | 5 | 5 | strong | 049 |

## Strongest Assigned-Box Winner Corridors

| Date | State | Var | Winner | LS signal | Signal | JSON | Best perm rank | Best family rank | Assigned-box VT | Fusion VT | Top trace | Top corridor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-06-22 | Florida4 | Midday | 330 | 66 | strong | matched_literal | 2 | 1 | 7 | 4 | 049 | 049 |
| 2026-01-01 | Delaware4 | Midday | 149 | 65 | strong | matched_literal | 4 | 1 | 13 | - | 499 | 499 |
| 2026-01-04 | Indiana4 | Midday | 813 | 64 | strong | matched_literal | 5 | 1 | 1 | 5 | 259 | 259 |
| 2025-12-31 | SouthCarolina4 | Midday | 653 | 62 | strong | matched_literal | 2 | 1 | 7 | 10 | 559 | 559 |
| 2025-12-31 | Virginia4 | Evening | 636 | 61 | strong | matched_literal | 13 | 1 | 1 | 7 | 299 | 299 |
| 2025-12-31 | Virginia4 | Midday | 686 | 61 | strong | matched_literal | 19 | 1 | 2 | 1 | 145 | 145 |
| 2025-06-21 | NewJersey4 | Midday | 182 | 61 | strong | matched_literal | 4 | 1 | 5 | - | 599 | 599 |
| 2026-01-01 | NorthCarolina4 | Evening | 053 | 59 | strong | matched_literal | 2 | 1 | 4 | 6 | 055 | 055 |
| 2025-06-21 | Pennsylvania4 | Evening | 360 | 59 | strong | matched_literal | 8 | 1 | 2 | 8 | 024 | 024 |
| 2026-01-02 | OntarioCanada4 | Evening | 816 | 58 | strong | matched_literal | 1 | 1 | 1 | 10 | 259 | 259 |
| 2025-12-30 | Pennsylvania4 | Midday | 186 | 58 | strong | matched_literal | 3 | 1 | 6 | - | 559 | 559 |
| 2026-01-01 | Pennsylvania4 | Evening | 328 | 58 | strong | matched_literal | 6 | 1 | 7 | - | 011 | 011 |

## Notes

- `winner_json_signal_class` comes from the structured winners JSON tables, not from DR receipts.
- `winner_json_status=unmatched_literal` means the sharepack has winners JSON files, but not for the actual stamped winner; treat those rows as artifact gaps, not genuine dead environments.
- `overlay_summary_mismatch` is winner-aware here: it flags rows where DR receipts stay at zero while the winner tables still show meaningful corridor activity.
- Audit-only payload depth is widened to `top20` for trace/lane/competing/double/gateway/cluster/assigned-box/fusion so broader visibility can be measured without narrowing the evaluation window.
- `trace/corridor/double/gateway/cluster/assigned-box/fusion winner VTRAC rank` checks whether the strongest predictive DR surfaces align to the eventual winner’s VTRAC lane, even when the literal winner is absent.
- `assigned-box` is a predictive surface built from 3-digit windows inside raw DR `box_id` / `final_value` strings; it is intended to preserve buried assigned-box corridor truth without using winner artifacts.
- `fusion` is a bounded promotion surface: it boosts lanes when assigned-box agrees with cluster/gateway, and it allows guarded assigned-box rescue when cluster/gateway are still dead.
- `best surface winner VTRAC rank` is the minimum visible rank across trace/corridor/double/candidate/gateway/cluster/assigned-box/fusion for that row.
- `gateway_score_gap` / `cluster_score_gap` / `box_score_gap` / `fusion_score_gap` measure how far the visible top score sits above the winner lane when the winner lane is present in that broader audit view.
