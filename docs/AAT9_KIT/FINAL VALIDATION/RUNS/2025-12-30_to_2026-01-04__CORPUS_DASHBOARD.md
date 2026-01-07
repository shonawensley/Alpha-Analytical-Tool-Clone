# Corpus Dashboard — 2025-12-30 → 2026-01-04

- tool metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- run-report corpus: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

Total graded outcomes (state×period): **163**

## Outcome mix

| period | n | % |
|---|---:|---:|
| Midday | 81 | 49.7% |
| Evening | 82 | 50.3% |

## Tool presence / exactness (not performance claims)

- Stable families present: **158/163** (96.9%)
- Hot Zones top lanes present: **162/163** (99.4%)
- VTRAC winner index in top10: **52/163** (31.9%)
- …with Combined among supporting sections: **48/52** (92.3%)
- DR top-candidates contain winner: **8/163** (4.9%)
- Blackapple top list contains winner: **0/163** (0.0%)
- Winner VTRAC signature has repeat (mirror/double-space): **75/163** (46.0%)

## Stable evidence origin (section labels)

| stable_section | n | % |
|---|---:|---:|
| Evening | 63 | 38.7% |
| Midday | 54 | 33.1% |
| Combined | 41 | 25.2% |
| missing | 5 | 3.1% |

## Rank-fraction distributions (lower is better)

- Stable family rank_fraction: n=158 median=0.1176 p10=0.0160 p25=0.0352 p75=0.2822
- Hot Zones top_lanes rank_fraction: n=162 median=0.5049 p10=0.1381 p25=0.2972 p75=0.7619
- VTRAC index rank_fraction: n=162 median=0.4571 p10=0.1143 p25=0.2286 p75=0.7143

## Run-report synthesis (from completed RUNS)

- Run-report rows: **163**
- Cross-variant mentioned: **163/163** (100.0%)

| env_verdict | n | % |
|---|---:|---:|
| strong (Stable exact boxed hits) | 80 | 49.1% |
| support (some Stable exact boxed hits) | 50 | 30.7% |
| weak/noisy (no exact Stable hit; rely on cross-tool/Aux) | 25 | 15.3% |
| support (Hot Zones top lanes overlap) | 8 | 4.9% |

## Convergence score (heuristic; used to pick study examples)

| score | n | % | meaning |
|---:|---:|---:|---|
| 4 | 4 | 2.5% | Stable(top10%) + HotZones(top20%) + VTRAC top10 + DR best_area<=3 |
| 3 | 37 | 22.7% | 3 of the 4 convergence lenses present |
| 2 | 57 | 35.0% | 2 lenses |
| 1 | 58 | 35.6% | 1 lens |
| 0 | 7 | 4.3% | no convergence lenses |

Top convergence cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERGENCE_CASES.csv`

