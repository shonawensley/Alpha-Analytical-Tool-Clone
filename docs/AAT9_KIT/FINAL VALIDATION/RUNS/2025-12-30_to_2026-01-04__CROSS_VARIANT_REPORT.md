# Cross‑Variant / Combined Report — 2025-12-30 → 2026-01-04

This report quantifies how often the strongest evidence appears to come from Combined or cross‑variant sources.

Data sources:
- metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- Stable cross‑variant proxy: `stable_families_section` in Stable sharepack summaries
- VTRAC Combined proxy: whether the winner’s index appears in the day’s `top_indices` and which sections support it (`vtrac_top10_sections`).

Total graded outcomes (state×period rows): **163**

## Stable origin (where the winner’s best Stable family evidence came from)

| Bucket | Count | % | Meaning |
|---|---:|---:|---|
| same_period | 55 | 33.7% | Stable’s strongest family evidence came from the same period section |
| other_period | 62 | 38.0% | Cross‑variant bounce: strongest evidence came from the opposite period section |
| combined | 41 | 25.2% | Combined lens: strongest evidence came from Combined section |
| missing | 5 | 3.1% | No Stable family evidence captured |

### Midday breakdown (n=81)

| Bucket | Count | % |
|---|---:|---:|
| same_period | 26 | 32.1% |
| other_period | 34 | 42.0% |
| combined | 21 | 25.9% |

### Evening breakdown (n=82)

| Bucket | Count | % |
|---|---:|---:|
| same_period | 29 | 35.4% |
| other_period | 28 | 34.1% |
| combined | 20 | 24.4% |
| missing | 5 | 6.1% |

## VTRAC Combined support (winner index appears in top indices)

- Winner index appears in VTRAC top indices: **52/163** (31.9%)
- Of those top-index appearances: Combined supports **48/52** (92.3%)
- Midday supports **43/52** (82.7%)
- Evening supports **41/52** (78.8%)

## Strongest cross‑variant bounce examples (Stable evidence came from opposite period)

| date | state | period | winner | stable_section | stable_rank_frac | stable_best_rank |
|---|---|---|---|---|---:|---:|
| 2025-12-31 | Michigan4 | Midday | 583 | Evening | 0.0007037297677691766 | 1 |
| 2025-12-30 | Pennsylvania4 | Midday | 186 | Evening | 0.004301075268817204 | 6 |
| 2026-01-03 | Connecticut4 | Evening | 181 | Midday | 0.014096185737976783 | 17 |
| 2026-01-04 | Connecticut4 | Evening | 311 | Midday | 0.014096185737976783 | 17 |
| 2025-12-30 | Florida4 | Midday | 377 | Evening | 0.020172910662824207 | 28 |
| 2025-12-31 | OntarioCanada4 | Midday | 918 | Evening | 0.026061057334326135 | 35 |
| 2026-01-02 | SouthCarolina4 | Evening | 084 | Midday | 0.02642559109874826 | 38 |
| 2026-01-03 | PuertoRico4 | Midday | 529 | Evening | 0.029074215761285386 | 38 |
| 2026-01-03 | PuertoRico4 | Evening | 359 | Midday | 0.029074215761285386 | 38 |
| 2026-01-03 | Virginia4 | Evening | 976 | Midday | 0.029333333333333333 | 44 |
| 2026-01-04 | Virginia4 | Evening | 217 | Midday | 0.029333333333333333 | 44 |
| 2026-01-02 | Ohio4 | Midday | 747 | Evening | 0.03190596137699412 | 38 |
| 2026-01-02 | Ohio4 | Evening | 133 | Midday | 0.03190596137699412 | 38 |
| 2025-12-31 | NorthCarolina4 | Midday | 867 | Evening | 0.03524804177545692 | 54 |
| 2026-01-03 | Ohio4 | Midday | 563 | Evening | 0.03802281368821293 | 50 |
| 2026-01-04 | Ohio4 | Midday | 674 | Evening | 0.03802281368821293 | 50 |
| 2025-12-30 | OntarioCanada4 | Midday | 409 | Evening | 0.03902065799540933 | 51 |
| 2026-01-03 | NorthCarolina4 | Evening | 178 | Midday | 0.06675224646983312 | 104 |
| 2026-01-04 | NorthCarolina4 | Evening | 887 | Midday | 0.06675224646983312 | 104 |
| 2026-01-03 | Delaware4 | Midday | 422 | Evening | 0.08022130013831259 | 116 |

## Strongest Combined‑driven examples (Stable evidence came from Combined section)

| date | state | period | winner | stable_section | stable_rank_frac | stable_best_rank |
|---|---|---|---|---|---:|---:|
| 2026-01-01 | NorthCarolina4 | Midday | 416 | Combined | 0.0005980861244019139 | 1 |
| 2025-12-31 | Florida4 | Evening | 211 | Combined | 0.0007662835249042146 | 1 |
| 2025-12-31 | SouthCarolina4 | Midday | 653 | Combined | 0.0013192612137203166 | 2 |
| 2025-12-30 | PuertoRico4 | Evening | 643 | Combined | 0.00572655690765927 | 8 |
| 2026-01-01 | Delaware4 | Midday | 149 | Combined | 0.00739247311827957 | 11 |
| 2025-12-30 | NorthCarolina4 | Midday | 455 | Combined | 0.014354066985645933 | 21 |
| 2025-12-30 | Pennsylvania4 | Evening | 173 | Combined | 0.015770609318996417 | 22 |
| 2026-01-03 | Pennsylvania4 | Midday | 744 | Combined | 0.01603053435114504 | 21 |
| 2026-01-04 | Pennsylvania4 | Midday | 359 | Combined | 0.01603053435114504 | 21 |
| 2025-12-31 | PuertoRico4 | Evening | 913 | Combined | 0.016046681254558718 | 22 |
| 2026-01-01 | NewYork4 | Midday | 117 | Combined | 0.01653486700215672 | 23 |
| 2026-01-02 | NorthCarolina4 | Midday | 033 | Combined | 0.019088669950738917 | 31 |
| 2025-12-31 | Connecticut4 | Midday | 932 | Combined | 0.019154030327214685 | 24 |
| 2025-12-31 | SouthCarolina4 | Evening | 044 | Combined | 0.032321899736147755 | 49 |
| 2025-12-30 | Indiana4 | Evening | 512 | Combined | 0.032577903682719546 | 46 |
| 2026-01-01 | SouthCarolina4 | Midday | 910 | Combined | 0.03651505445227418 | 57 |
| 2025-12-31 | Connecticut4 | Evening | 361 | Combined | 0.03750997605746209 | 47 |
| 2026-01-01 | Pennsylvania4 | Evening | 328 | Combined | 0.04148148148148148 | 56 |
| 2025-12-31 | Pennsylvania4 | Midday | 684 | Combined | 0.05547550432276657 | 77 |
| 2026-01-03 | NewJersey4 | Evening | 963 | Combined | 0.06479481641468683 | 90 |

