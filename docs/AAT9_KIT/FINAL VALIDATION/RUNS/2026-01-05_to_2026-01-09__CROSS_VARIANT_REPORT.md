# Cross‑Variant / Combined Report — 2026-01-05 → 2026-01-09

This report quantifies how often the strongest evidence appears to come from Combined or cross‑variant sources.

Data sources:
- metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- Stable cross‑variant proxy: `stable_families_section` in Stable sharepack summaries
- VTRAC Combined proxy: whether the winner’s index appears in the day’s `top_indices` and which sections support it (`vtrac_top10_sections`).

Total graded outcomes (state×period rows): **138**

## Stable origin (where the winner’s best Stable family evidence came from)

| Bucket | Count | % | Meaning |
|---|---:|---:|---|
| same_period | 52 | 37.7% | Stable’s strongest family evidence came from the same period section |
| other_period | 50 | 36.2% | Cross‑variant bounce: strongest evidence came from the opposite period section |
| combined | 32 | 23.2% | Combined lens: strongest evidence came from Combined section |
| missing | 4 | 2.9% | No Stable family evidence captured |

### Midday breakdown (n=69)

| Bucket | Count | % |
|---|---:|---:|
| same_period | 27 | 39.1% |
| other_period | 24 | 34.8% |
| combined | 18 | 26.1% |

### Evening breakdown (n=69)

| Bucket | Count | % |
|---|---:|---:|
| same_period | 25 | 36.2% |
| other_period | 26 | 37.7% |
| combined | 14 | 20.3% |
| missing | 4 | 5.8% |

## VTRAC Combined support (winner index appears in top indices)

- Winner index appears in VTRAC top indices: **35/138** (25.4%)
- Of those top-index appearances: Combined supports **31/35** (88.6%)
- Midday supports **29/35** (82.9%)
- Evening supports **28/35** (80.0%)

## Strongest cross‑variant bounce examples (Stable evidence came from opposite period)

| date | state | period | winner | stable_section | stable_rank_frac | stable_best_rank |
|---|---|---|---|---|---:|---:|
| 2026-01-08 | Delaware4 | Midday | 820 | Evening | 0.007380073800738007 | 12 |
| 2026-01-09 | Ohio4 | Midday | 785 | Evening | 0.007547169811320755 | 12 |
| 2026-01-09 | NewJersey4 | Midday | 287 | Evening | 0.00911854103343465 | 12 |
| 2026-01-08 | Ohio4 | Midday | 681 | Evening | 0.01348747591522158 | 21 |
| 2026-01-09 | OntarioCanada4 | Midday | 772 | Evening | 0.023972602739726026 | 35 |
| 2026-01-09 | Virginia4 | Midday | 380 | Evening | 0.02435723951285521 | 36 |
| 2026-01-05 | Virginia4 | Evening | 585 | Midday | 0.028219971056439943 | 39 |
| 2026-01-07 | Ohio4 | Midday | 737 | Evening | 0.032015065913371 | 51 |
| 2026-01-09 | Delaware4 | Midday | 843 | Evening | 0.0463855421686747 | 77 |
| 2026-01-08 | NewJersey4 | Evening | 055 | Midday | 0.04915730337078652 | 70 |
| 2026-01-07 | Virginia4 | Evening | 990 | Midday | 0.06935975609756098 | 91 |
| 2026-01-09 | NewYork4 | Midday | 989 | Evening | 0.07198748043818466 | 92 |
| 2026-01-06 | Virginia4 | Evening | 958 | Midday | 0.07615384615384616 | 99 |
| 2026-01-07 | NewYork4 | Evening | 286 | Midday | 0.07757951900698215 | 100 |
| 2026-01-06 | SouthCarolina4 | Midday | 586 | Evening | 0.09154437456324249 | 131 |
| 2026-01-08 | PuertoRico4 | Evening | 479 | Midday | 0.09334889148191365 | 80 |
| 2026-01-08 | Pennsylvania4 | Midday | 750 | Evening | 0.11339475549255847 | 160 |
| 2026-01-08 | Indiana4 | Midday | 325 | Evening | 0.11550733886407147 | 181 |
| 2026-01-06 | Pennsylvania4 | Midday | 684 | Evening | 0.12749003984063745 | 160 |
| 2026-01-08 | NewJersey4 | Midday | 089 | Evening | 0.12851123595505617 | 183 |

## Strongest Combined‑driven examples (Stable evidence came from Combined section)

| date | state | period | winner | stable_section | stable_rank_frac | stable_best_rank |
|---|---|---|---|---|---:|---:|
| 2026-01-05 | NewYork4 | Midday | 080 | Combined | 0.000724112961622013 | 1 |
| 2026-01-06 | Michigan4 | Evening | 578 | Combined | 0.0008710801393728223 | 1 |
| 2026-01-09 | Delaware4 | Evening | 681 | Combined | 0.0018072289156626507 | 3 |
| 2026-01-05 | SouthCarolina4 | Evening | 712 | Combined | 0.0028551034975017845 | 4 |
| 2026-01-05 | SouthCarolina4 | Midday | 171 | Combined | 0.008565310492505354 | 12 |
| 2026-01-09 | Pennsylvania4 | Evening | 014 | Combined | 0.020960108181203516 | 31 |
| 2026-01-07 | Indiana4 | Midday | 823 | Combined | 0.023353293413173652 | 39 |
| 2026-01-07 | Pennsylvania4 | Evening | 263 | Combined | 0.03600900225056264 | 48 |
| 2026-01-05 | Virginia4 | Midday | 473 | Combined | 0.05788712011577424 | 80 |
| 2026-01-05 | Pennsylvania4 | Evening | 600 | Combined | 0.0594855305466238 | 74 |
| 2026-01-06 | Delaware4 | Midday | 165 | Combined | 0.10627719080174021 | 171 |
| 2026-01-09 | NewYork4 | Evening | 835 | Combined | 0.10719874804381847 | 137 |
| 2026-01-08 | SouthCarolina4 | Midday | 277 | Combined | 0.10751932536893886 | 153 |
| 2026-01-07 | OntarioCanada4 | Midday | 547 | Combined | 0.11312545322697606 | 156 |
| 2026-01-08 | OntarioCanada4 | Midday | 022 | Combined | 0.12859097127222982 | 188 |
| 2026-01-06 | Connecticut4 | Evening | 737 | Combined | 0.16691505216095381 | 224 |
| 2026-01-08 | PuertoRico4 | Midday | 073 | Combined | 0.17036172695449242 | 146 |
| 2026-01-05 | Michigan4 | Midday | 260 | Combined | 0.17327586206896553 | 201 |
| 2026-01-06 | Florida4 | Evening | 160 | Combined | 0.191044776119403 | 320 |
| 2026-01-07 | NewYork4 | Midday | 916 | Combined | 0.2187742435996897 | 282 |

