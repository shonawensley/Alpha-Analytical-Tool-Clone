# Env Verdict Scoreboard — B36 (baseline vs dc1)

Purpose
- Quantify outcomes by **post-hoc environment verdict** buckets (tight vs noisy vs split).
- Compare baseline (`stable10`) vs `dc1` closure on the same rows (B36).

Important
- `env_verdict` comes from MV synthesis (`corpus_summary.csv`). It is **not a predictive claim**.
- Use this to validate posture/regime claims (`E021/E009`): when conversion changes help and when they don’t.
- `CoverAll+NoBoxPerm` is a **bad** metric (we had all 3 digits but picked no winning permutation). Lower is better.
- `UNLABELED` means the MV `env_verdict` label is missing for that row (not “unknown regime”).

Evidence inputs
- Env labels: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Window `2026-01-01_to_2026-01-09` baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv`
- Window `2026-01-01_to_2026-01-09` dc1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv`
- Window `2026-01-15_to_2026-01-22` baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.csv`
- Window `2026-01-15_to_2026-01-22` dc1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.csv`

Bucket mapping (collapsed)
- `STRONG`: strong/playable days (often Stable exact boxed hits present)
- `SUPPORT`: partial structure/support days
- `WEAK_NOISY`: weak/noisy/cautious/mixed/pass/low-confidence days
- `SPLIT`: explicitly split (Midday vs Evening differs)
- `UNKNOWN` / `OTHER`: misc buckets
- `UNLABELED`: missing MV label in `corpus_summary.csv` for that row

## Window — 2026-01-01_to_2026-01-09

- Rows (winner-present, B36): baseline `245`, dc1 `245`
- Rows with non-empty `env_verdict`: baseline `245` (100.0%), dc1 `245` (100.0%)

| Bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |
|---|---:|---|---|---|---|---|---:|
| STRONG | 100 | 5.0% (5/100) → 4.0% (4/100) (-1.0pp) | 18.0% (18/100) → 17.0% (17/100) (-1.0pp) | 61.0% (61/100) → 61.0% (61/100) (+0.0pp) | 78.0% (78/100) → 79.0% (79/100) (+1.0pp) | 1.11 → 1.11 (+0.00) | 34.0% |
| SUPPORT | 116 | 4.3% (5/116) → 4.3% (5/116) (+0.0pp) | 13.8% (16/116) → 13.8% (16/116) (+0.0pp) | 50.9% (59/116) → 50.9% (59/116) (+0.0pp) | 81.9% (95/116) → 81.9% (95/116) (+0.0pp) | 0.98 → 0.98 (+0.00) | 29.3% |
| WEAK_NOISY | 29 | 3.4% (1/29) → 6.9% (2/29) (+3.4pp) | 6.9% (2/29) → 13.8% (4/29) (+6.9pp) | 51.7% (15/29) → 51.7% (15/29) (+0.0pp) | 82.8% (24/29) → 72.4% (21/29) (-10.3pp) | 0.90 → 0.90 (+0.00) | 6.9% |

### Collapsed totals (operator view)

| Collapsed bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |
|---|---:|---|---|---|---|---|---:|
| TIGHT_TOTAL (STRONG+SUPPORT) | 216 | 4.6% → 4.2% (-0.5pp) | 15.7% → 15.3% (-0.5pp) | 55.6% → 55.6% (+0.0pp) | 80.1% → 80.6% (+0.5pp) | 1.04 → 1.04 (+0.00) | 31.5% |
| NOISY_TOTAL (WEAK+OTHER+…) | 29 | 3.4% → 6.9% (+3.4pp) | 6.9% → 13.8% (+6.9pp) | 51.7% → 51.7% (+0.0pp) | 82.8% → 72.4% (-10.3pp) | 0.90 → 0.90 (+0.00) | 6.9% |
| SPLIT_TOTAL | 0 | - | - | - | - | - | - |
| ALL_TOTAL | 245 | 4.5% → 4.5% (+0.0pp) | 14.7% → 15.1% (+0.4pp) | 55.1% → 55.1% (+0.0pp) | 80.4% → 79.6% (-0.8pp) | 1.02 → 1.02 (+0.00) | 28.6% |

## Window — 2026-01-15_to_2026-01-22

- Rows (winner-present, B36): baseline `193`, dc1 `193`
- Rows with non-empty `env_verdict`: baseline `193` (100.0%), dc1 `193` (100.0%)

| Bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |
|---|---:|---|---|---|---|---|---:|
| STRONG | 95 | 5.3% (5/95) → 5.3% (5/95) (+0.0pp) | 26.3% (25/95) → 24.2% (23/95) (-2.1pp) | 72.6% (69/95) → 72.6% (69/95) (+0.0pp) | 71.6% (68/95) → 73.7% (70/95) (+2.1pp) | 1.40 → 1.40 (+0.00) | 28.4% |
| SUPPORT | 58 | 5.2% (3/58) → 5.2% (3/58) (+0.0pp) | 22.4% (13/58) → 22.4% (13/58) (+0.0pp) | 60.3% (35/58) → 60.3% (35/58) (+0.0pp) | 75.9% (44/58) → 75.9% (44/58) (+0.0pp) | 1.12 → 1.12 (+0.00) | 29.3% |
| WEAK_NOISY | 38 | 2.6% (1/38) → 5.3% (2/38) (+2.6pp) | 10.5% (4/38) → 10.5% (4/38) (+0.0pp) | 47.4% (18/38) → 47.4% (18/38) (+0.0pp) | 76.3% (29/38) → 76.3% (29/38) (+0.0pp) | 0.76 → 0.76 (+0.00) | 18.4% |
| UNKNOWN | 2 | 0.0% (0/2) → 0.0% (0/2) (+0.0pp) | 0.0% (0/2) → 0.0% (0/2) (+0.0pp) | 50.0% (1/2) → 50.0% (1/2) (+0.0pp) | 100.0% (2/2) → 100.0% (2/2) (+0.0pp) | 2.00 → 2.00 (+0.00) | 50.0% |

### Collapsed totals (operator view)

| Collapsed bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |
|---|---:|---|---|---|---|---|---:|
| TIGHT_TOTAL (STRONG+SUPPORT) | 153 | 5.2% → 5.2% (+0.0pp) | 24.8% → 23.5% (-1.3pp) | 68.0% → 68.0% (+0.0pp) | 73.2% → 74.5% (+1.3pp) | 1.29 → 1.29 (+0.00) | 28.8% |
| NOISY_TOTAL (WEAK+OTHER+…) | 40 | 2.5% → 5.0% (+2.5pp) | 10.0% → 10.0% (+0.0pp) | 47.5% → 47.5% (+0.0pp) | 77.5% → 77.5% (+0.0pp) | 0.82 → 0.82 (+0.00) | 20.0% |
| SPLIT_TOTAL | 0 | - | - | - | - | - | - |
| ALL_TOTAL | 193 | 4.7% → 5.2% (+0.5pp) | 21.8% → 20.7% (-1.0pp) | 63.7% → 63.7% (+0.0pp) | 74.1% → 75.1% (+1.0pp) | 1.20 → 1.20 (+0.00) | 26.9% |

