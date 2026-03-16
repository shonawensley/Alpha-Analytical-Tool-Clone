# DR Gold-Day Winner Audit

- Purpose: winner-aware audit of `DR Arena v1.1` over frozen gold-day sharepacks.
- Dates audited: `2026-01-05, 2026-01-06, 2026-01-07, 2026-01-08, 2026-01-09`
- Rows are Midday/Evening state outcomes only; Combined is excluded from grading.

## Overview

| Metric | Count | % |
|---|---|---|
| Rows audited | 138 | 100.0% |
| exact_any > 0 | 48 | 34.8% |
| vtrac_any > 0 | 119 | 86.2% |
| family_vtrac_any > 0 | 76 | 55.1% |
| trace winner VTRAC rank <= 3 | 11 | 8.0% |
| corridor winner VTRAC rank <= 3 | 11 | 8.0% |
| double winner VTRAC rank <= 3 | 10 | 7.2% |
| gateway winner VTRAC rank <= 3 | 12 | 8.7% |
| cluster winner VTRAC rank <= 3 | 11 | 8.0% |
| assigned-box winner VTRAC rank <= 3 | 15 | 10.9% |
| fusion winner VTRAC rank <= 3 | 11 | 8.0% |
| gateway winner VTRAC rank <= 5 | 16 | 11.6% |
| cluster winner VTRAC rank <= 5 | 18 | 13.0% |
| assigned-box winner VTRAC rank <= 5 | 22 | 15.9% |
| fusion winner VTRAC rank <= 5 | 22 | 15.9% |
| gateway winner VTRAC rank <= 8 | 25 | 18.1% |
| cluster winner VTRAC rank <= 8 | 28 | 20.3% |
| assigned-box winner VTRAC rank <= 8 | 31 | 22.5% |
| fusion winner VTRAC rank <= 8 | 37 | 26.8% |
| gateway winner VTRAC rank <= 10 | 26 | 18.8% |
| cluster winner VTRAC rank <= 10 | 28 | 20.3% |
| assigned-box winner VTRAC rank <= 10 | 44 | 31.9% |
| fusion winner VTRAC rank <= 10 | 43 | 31.2% |
| gateway winner VTRAC rank <= 20 | 27 | 19.6% |
| cluster winner VTRAC rank <= 20 | 30 | 21.7% |
| assigned-box winner VTRAC rank <= 20 | 82 | 59.4% |
| fusion winner VTRAC rank <= 20 | 43 | 31.2% |
| best surface winner VTRAC rank <= 3 | 25 | 18.1% |
| best surface winner VTRAC rank <= 5 | 35 | 25.4% |
| best surface winner VTRAC rank <= 8 | 48 | 34.8% |
| best surface winner VTRAC rank <= 10 | 55 | 39.9% |
| best surface winner VTRAC rank <= 20 | 85 | 61.6% |
| winner JSON matched | 110 | 79.7% |
| winner JSON unavailable/unmatched | 28 | 20.3% |
| winner tables strong signal | 109 | 79.0% |
| strong overlay-summary mismatch | 14 | 10.1% |
| moderate overlay-summary mismatch | 0 | 0.0% |

## Alignment Classes

| Class | Count | % |
|---|---|---|
| active_low_trust | 2 | 1.4% |
| false_empty | 9 | 6.5% |
| literal_capture | 48 | 34.8% |
| miss | 8 | 5.8% |
| vtrac_capture | 71 | 51.4% |

## By Date

| Date | Rows | vtrac_any | trace_vtrac_top3 | corridor_vtrac_top3 | gateway_vtrac_top3 | cluster_vtrac_top3 | box_vtrac_top3 | fusion_vtrac_top3 | cluster_vtrac_top10 | box_vtrac_top10 | fusion_vtrac_top10 | best_surface_top10 | winner_json_matched | mismatch>=moderate | strong_signal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-05 | 28 | 23 | 3 | 3 | 3 | 2 | 4 | 3 | 7 | 10 | 12 | 13 | 0 | 0 | 0 |
| 2026-01-06 | 26 | 22 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 6 | 5 | 6 | 26 | 4 | 25 |
| 2026-01-07 | 28 | 27 | 1 | 1 | 1 | 1 | 2 | 0 | 7 | 9 | 9 | 14 | 28 | 1 | 28 |
| 2026-01-08 | 28 | 23 | 3 | 3 | 4 | 4 | 1 | 3 | 5 | 8 | 7 | 10 | 28 | 5 | 28 |
| 2026-01-09 | 28 | 24 | 2 | 2 | 2 | 2 | 5 | 3 | 7 | 11 | 10 | 12 | 28 | 4 | 28 |

## Strongest False-Empty / Mismatch Cases

| Date | State | Var | Winner | Empty | Mismatch | Signal | JSON | LS signal | Trace VT | Corridor VT |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-08 | Indiana4 | Midday | 325 | positive_trace | strong | strong | matched_literal | 18 | - | - |
| 2026-01-09 | Indiana4 | Midday | 219 | positive_trace | strong | strong | matched_literal | 27 | - | - |
| 2026-01-08 | NorthCarolina4 | Evening | 571 | positive_trace | strong | strong | matched_literal | 29 | - | - |
| 2026-01-06 | Ohio4 | Evening | 064 | positive_trace | strong | strong | matched_literal | 16 | - | - |
| 2026-01-09 | Michigan4 | Midday | 842 | positive_trace | strong | strong | matched_literal | 0 | - | - |
| 2026-01-06 | Connecticut4 | Midday | 576 | positive_trace | strong | strong | matched_literal | 11 | - | - |
| 2026-01-06 | OntarioCanada4 | Evening | 433 | positive_trace | strong | strong | matched_literal | 7 | - | - |
| 2026-01-08 | OntarioCanada4 | Evening | 498 | positive_trace | strong | strong | matched_literal | 5 | - | - |
| 2026-01-07 | Delaware4 | Midday | 657 | active_low_trust | strong | strong | matched_literal | 6 | - | - |
| 2026-01-06 | Michigan4 | Evening | 578 | positive_trace | strong | strong | matched_literal | 6 | - | - |
| 2026-01-09 | Michigan4 | Evening | 273 | positive_trace | strong | strong | matched_literal | 11 | - | - |
| 2026-01-08 | NewYork4 | Midday | 199 | positive_trace | strong | strong | matched_literal | 7 | - | - |

## Strongest VTRAC-Lane Captures

| Date | State | Var | Winner | VTRAC idx | trace VT | corridor VT | double VT | gateway VT | cluster VT | box VT | fusion VT | best VT | Signal | JSON | Top corridor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-05 | Indiana4 | Midday | 458 | 14 | 1 | 1 | - | 2 | 7 | 11 | 4 | 1 | unavailable | unmatched_literal | 034 |
| 2026-01-06 | Florida4 | Midday | 209 | 12 | 1 | 1 | 1 | 1 | 1 | 5 | 1 | 1 | strong | matched_literal | 259 |
| 2026-01-08 | PuertoRico4 | Midday | 073 | 11 | 1 | 1 | 2 | 2 | 2 | 6 | 2 | 1 | strong | matched_literal | 023 |
| 2026-01-09 | Ohio4 | Evening | 090 | 5 | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | strong | matched_literal | 559 |
| 2026-01-07 | Pennsylvania4 | Midday | 060 | 2 | - | - | - | - | 5 | 2 | 4 | 2 | strong | matched_literal | 559 |
| 2026-01-07 | Indiana4 | Evening | 290 | 12 | 3 | 3 | 3 | 3 | 3 | - | - | 3 | strong | matched_literal | 244 |
| 2026-01-05 | NorthCarolina4 | Evening | 577 | 10 | 4 | 5 | 4 | 4 | 4 | 15 | 6 | 4 | unavailable | unmatched_literal | 245 |
| 2026-01-07 | NewJersey4 | Midday | 361 | 18 | - | - | - | - | - | 4 | 7 | 4 | strong | matched_literal | 299 |
| 2026-01-07 | Pennsylvania4 | Evening | 263 | 21 | - | - | - | - | - | 4 | 5 | 4 | strong | matched_literal | 559 |
| 2026-01-09 | Florida4 | Midday | 860 | 8 | 8 | 7 | - | 7 | 5 | 10 | 4 | 4 | strong | matched_literal | 259 |
| 2026-01-05 | Virginia4 | Evening | 469 | 25 | 9 | 9 | 7 | 6 | 7 | 9 | 5 | 5 | unavailable | unmatched_literal | 599 |
| 2026-01-06 | SouthCarolina4 | Midday | 586 | 8 | - | - | - | - | - | 5 | - | 5 | strong | matched_literal | 099 |

## Visible But Under-Promoted Winner Lanes

| Date | State | Var | Winner | VT idx | cluster rank | cluster band | cluster gap | gateway rank | box rank | fusion rank | best VT | Signal | Top attractor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-07 | Virginia4 | Evening | 990 | 15 | 6 | top8 | 78.439 | 6 | 12 | 6 | 6 | strong | 229 |
| 2026-01-09 | Florida4 | Evening | 093 | 14 | 6 | top8 | 78.574 | 6 | 6 | 6 | 6 | strong | 445 |
| 2026-01-07 | NorthCarolina4 | Evening | 202 | 10 | 6 | top8 | 85.256 | 6 | 15 | 7 | 6 | strong | 229 |
| 2026-01-09 | OntarioCanada4 | Evening | 104 | 9 | 6 | top8 | 96.24 | 6 | 1 | 4 | 1 | strong | 459 |
| 2026-01-05 | Indiana4 | Midday | 458 | 14 | 7 | top8 | 18.9 | 2 | 11 | 4 | 1 | unavailable | 034 |
| 2026-01-07 | Florida4 | Midday | 434 | 34 | 7 | top8 | 56.157 | 8 | 10 | 8 | 7 | strong | 259 |
| 2026-01-05 | Virginia4 | Evening | 469 | 25 | 7 | top8 | 63.104 | 6 | 9 | 5 | 5 | unavailable | 599 |
| 2026-01-05 | Delaware4 | Midday | 029 | 12 | 8 | top8 | 78.663 | 8 | 13 | 9 | 8 | unavailable | 455 |
| 2026-01-07 | Michigan4 | Evening | 616 | 16 | 8 | top8 | 138.315 | - | 9 | - | 8 | strong | 059 |
| 2026-01-08 | Ohio4 | Evening | 580 | 4 | 8 | top8 | 155.645 | - | 4 | 6 | 4 | strong | 559 |
| 2026-01-07 | PuertoRico4 | Midday | 426 | 22 | 11 | top20 | 67.04 | 10 | - | - | 10 | strong | 245 |
| 2026-01-09 | SouthCarolina4 | Midday | 067 | 7 | 11 | top20 | 81.082 | 11 | - | - | 11 | strong | 259 |

## Strongest Assigned-Box Winner Corridors

| Date | State | Var | Winner | LS signal | Signal | JSON | Best perm rank | Best family rank | Assigned-box VT | Fusion VT | Top trace | Top corridor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-06 | Michigan4 | Midday | 618 | 70 | strong | matched_literal | 3 | 1 | 1 | 7 | 449 | 449 |
| 2026-01-07 | Indiana4 | Evening | 290 | 67 | strong | matched_literal | 7 | 1 | - | - | 244 | 244 |
| 2026-01-07 | Ohio4 | Evening | 204 | 62 | strong | matched_literal | 6 | 1 | 5 | 7 | 559 | 559 |
| 2026-01-09 | Pennsylvania4 | Midday | 811 | 59 | strong | matched_literal | 2 | 1 | 3 | 5 | 559 | 559 |
| 2026-01-07 | Florida4 | Evening | 963 | 56 | strong | matched_literal | 2 | 1 | 13 | - | 445 | 445 |
| 2026-01-08 | Delaware4 | Evening | 031 | 54 | strong | matched_literal | 1 | 1 | - | - | 259 | 259 |
| 2026-01-09 | NorthCarolina4 | Evening | 960 | 53 | strong | matched_literal | 1 | 1 | 8 | 10 | 229 | 229 |
| 2026-01-09 | Ohio4 | Evening | 090 | 50 | strong | matched_literal | 4 | 1 | 3 | 1 | 559 | 559 |
| 2026-01-09 | Connecticut4 | Midday | 234 | 49 | strong | matched_literal | 5 | 1 | - | - | 229 | 229 |
| 2026-01-06 | NewJersey4 | Evening | 942 | 48 | strong | matched_literal | 2 | 1 | 2 | 1 | 299 | 299 |
| 2026-01-07 | NorthCarolina4 | Evening | 202 | 48 | strong | matched_literal | 3 | 1 | 15 | 7 | 229 | 229 |
| 2026-01-09 | OntarioCanada4 | Evening | 104 | 48 | strong | matched_literal | 1 | 1 | 1 | 4 | 459 | 459 |

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
