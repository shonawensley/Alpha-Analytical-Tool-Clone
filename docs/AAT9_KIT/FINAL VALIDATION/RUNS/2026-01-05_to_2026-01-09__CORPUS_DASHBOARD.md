# Corpus Dashboard — 2026-01-05 → 2026-01-09

- tool metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- run-report corpus: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

Total graded outcomes (state×period): **138**

## Outcome mix

| period | n | % |
|---|---:|---:|
| Midday | 69 | 50.0% |
| Evening | 69 | 50.0% |

## Tool presence / exactness (not performance claims)

- Stable families present: **134/138** (97.1%)
- Hot Zones top lanes present: **135/138** (97.8%)
- VTRAC winner index in top10: **35/138** (25.4%)
- …with Combined among supporting sections: **31/35** (88.6%)
- DR top-candidates contain winner: **5/138** (3.6%)
- Blackapple top list contains winner: **1/138** (0.7%)
- Winner VTRAC signature has repeat (mirror/double-space): **74/138** (53.6%)

## Stable evidence origin (section labels)

| stable_section | n | % |
|---|---:|---:|
| Midday | 53 | 38.4% |
| Evening | 49 | 35.5% |
| Combined | 32 | 23.2% |
| missing | 4 | 2.9% |

## Rank-fraction distributions (lower is better)

- Stable family rank_fraction: n=134 median=0.1620 p10=0.0102 p25=0.0595 p75=0.3188
- Hot Zones top_lanes rank_fraction: n=135 median=0.4429 p10=0.1019 p25=0.2333 p75=0.6934
- VTRAC index rank_fraction: n=136 median=0.5143 p10=0.1143 p25=0.2857 p75=0.6857

## Run-report synthesis (from completed RUNS)

- Run-report rows: **138**
- Cross-variant mentioned: **138/138** (100.0%)

| env_verdict | n | % |
|---|---:|---:|
| support (some Stable exact boxed hits) | 64 | 46.4% |
| strong (Stable exact boxed hits) | 58 | 42.0% |
| weak/noisy (no exact Stable hit; rely on cross-tool/Aux) | 10 | 7.2% |
| support (Hot Zones top lanes overlap) | 6 | 4.3% |

## Convergence score (heuristic; used to pick study examples)

| score | n | % | meaning |
|---:|---:|---:|---|
| 4 | 5 | 3.6% | Stable(top10%) + HotZones(top20%) + VTRAC top10 + DR best_area<=3 |
| 3 | 20 | 14.5% | 3 of the 4 convergence lenses present |
| 2 | 55 | 39.9% | 2 lenses |
| 1 | 52 | 37.7% | 1 lens |
| 0 | 6 | 4.3% | no convergence lenses |

Top convergence cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.csv`

