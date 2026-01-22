# DR‑004 Experiment Results (tool_only)

Scope: selection‑layer experiments only (Candidate Universe / Play Cards). No analyzer edits.

## Configs evaluated

All experiments were run across the three frozen windows:
- `2025-06-21→2025-06-23`
- `2025-12-30→2026-01-04`
- `2026-01-05→2026-01-09`

Key tags:

- `dr004_v1`
  - `--dr004-boxed-canonicals 2`
  - `--dr004-recent-draws 2`
  - `--dr004-max-cost-units 12`
  - index gateway **off**
- `dr004_v2_idx2`
  - same as `dr004_v1`, plus:
  - `--dr004-index-boxed-canonicals 2` (adds `digit_reduction_dr004_index` packs)

Other tags tried (no `hit_any` lift vs `dr004_v1`): `dr004_v1_norec`, `dr004_v2_k3`.

---

## Candidate Universe union (tool_only)

### Baseline vs `dr004_v1`

| Window | base hit_any | dr004 hit_any | base idx_hit | dr004 idx_hit | base idx_only | dr004 idx_only | avg union cost (base→dr004) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `2025-06-21→2025-06-23` | 28.395% | 28.395% | 56.790% | 58.025% | 28.395% | 29.630% | 170.8 → 182.6 |
| `2025-12-30→2026-01-04` | 22.699% | 23.926% | 66.258% | 67.485% | 43.558% | 43.558% | 163.2 → 175.1 |
| `2026-01-05→2026-01-09` | 22.464% | 23.913% | 65.217% | 66.667% | 42.754% | 43.478% | 160.3 → 170.8 |

### Baseline vs `dr004_v2_idx2` (adds index gateway packs)

| Window | base hit_any | exp hit_any | base idx_hit | exp idx_hit | base idx_only | exp idx_only | avg union cost (base→exp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `2025-06-21→2025-06-23` | 28.395% | 28.395% | 56.790% | 59.259% | 28.395% | 30.864% | 170.8 → 190.5 |
| `2025-12-30→2026-01-04` | 22.699% | 23.926% | 66.258% | 68.098% | 43.558% | 44.172% | 163.2 → 182.9 |
| `2026-01-05→2026-01-09` | 22.464% | 25.362% | 65.217% | 68.116% | 42.754% | 43.478% | 160.3 → 179.0 |

---

## DR‑004 method rows (in experiment grades)

### `dr004_v2_idx2` method-level (shows what the added index pack contributes)

| Window | method_id | hit_any | idx_only | avg cost_units |
|---|---|---:|---:|---:|
| `2025-06-21→2025-06-23` | `digit_reduction_dr004` | 0.000% | 1.646% | 7.0 |
| `2025-06-21→2025-06-23` | `digit_reduction_dr004_index` | 0.412% | 4.115% | 10.8 |
| `2025-12-30→2026-01-04` | `digit_reduction_dr004` | 1.022% | 2.863% | 7.2 |
| `2025-12-30→2026-01-04` | `digit_reduction_dr004_index` | 1.636% | 4.908% | 10.6 |
| `2026-01-05→2026-01-09` | `digit_reduction_dr004` | 0.966% | 1.932% | 6.9 |
| `2026-01-05→2026-01-09` | `digit_reduction_dr004_index` | 1.691% | 3.623% | 10.6 |

---

## Play Cards (play_box_first) hit_any

These are **not** a DR‑004 win yet: DR‑004 improves Candidate Universe union in some windows, but can reshuffle Play Card ranking.

| Window | B12 base | B12 dr004_v1 | B12 dr004_v2_idx2 | B24 base | B24 dr004_v1 | B24 dr004_v2_idx2 | B36 base | B36 dr004_v1 | B36 dr004_v2_idx2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `2025-06-21→2025-06-23` | 1.235% | 1.235% | 1.235% | 2.469% | 2.469% | 2.469% | 2.469% | 2.469% | 2.469% |
| `2025-12-30→2026-01-04` | 0.613% | 0.613% | 0.613% | 2.454% | 2.454% | 1.840% | 4.294% | 3.681% | 3.067% |
| `2026-01-05→2026-01-09` | 3.623% | 2.899% | 0.725% | 5.797% | 4.348% | 5.072% | 5.797% | 6.522% | 8.696% |

---

## Current recommendation

- Treat `dr004_v1` as the **default research baseline** (modest union lift in 2/3 windows, bounded cost increase).
- Treat `dr004_v2_idx2` as **high-risk/high-reward research** (bigger Jan-window union lift, but higher cost and Play Card B12 volatility).

Next: if we want DR‑004 to be “real” for Play Cards (B12/B24), we need a stricter consumption policy (e.g., require cross-method convergence before DR‑004 can move a combo into the top budgets), rather than simply adding more DR‑derived BOX candidates.

---

## v3 experiments (pool filter knobs; envelope4 as signal lens)

We added optional DR‑004 pool filters (default behavior unchanged):
- `--dr004-min-unique-digits` (default `1`)
- `--dr004-max-unique-digits` (default `3`; `4` enables “envelope4” pools)

### Tagged sweeps run (3 windows; tool_only)

- `dr004_v3_min2`
  - Flags: `--dr004-min-unique-digits 2 --dr004-max-unique-digits 3` (plus v1 defaults)
  - Incremental vs baseline (union hit_any): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v3_min2.md`
- `dr004_v3_u2u4`
  - Flags: `--dr004-min-unique-digits 2 --dr004-max-unique-digits 4` (plus v1 defaults; “envelope4” enabled)
  - Incremental vs baseline (union hit_any): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v3_u2u4.md`

High-level outcome:
- Neither v3 tag beats `dr004_v1` on Candidate Universe union lift; both increase average union cost.
- However, the **signal lens** improves materially on the 10-case queue when using `unique_digits=2→4`:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_004__ALIGNMENT_REPORT__u2u4.md`

Decision (current):
- Keep DR‑004 pack emission **off by default** (v0.2).
- Treat `unique_digits=2→4` as a **signals export / superbrain fusion** setting (great for “where is the cluster?”), not a proven selection-layer union-lift knob yet.
