# DR Envelope Pack Experiment (Top2) — Candidate Universe

Purpose: compare baseline tool-only Candidate Universe vs adding optional DR envelope packs derived from DR steps CSV.

- New packs: `method_id=digit_reduction_envelope_steps`, per section `Combined/Midday/Evening`, `BOX`, seeded by top-2 canonicals.
- Baseline: existing `tool_only` CU (no DR caller; `--top-n-dr 0`).

## Summary (Union rows)

| Window | Baseline hit_any | +DR env hit_any | Baseline box_hit | +DR env box_hit | Baseline idx_hit | +DR env idx_hit | Baseline idx_only | +DR env idx_only | Avg union cost (base → env) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `2025-06-21→2025-06-23` | 28.4% | 28.4% | 28.4% | 28.4% | 56.8% | 59.3% | 28.4% | 30.9% | 170.8 → 185.3 |
| `2025-12-30→2026-01-04` | 22.7% | 23.9% | 22.7% | 23.9% | 66.3% | 67.5% | 43.6% | 43.6% | 163.2 → 176.9 |
| `2026-01-05→2026-01-09` | 22.5% | 23.9% | 22.5% | 23.9% | 65.2% | 66.7% | 42.8% | 43.5% | 160.3 → 172.7 |

## DR Envelope Pack (method rows)

| Window | Rows | hit_any | box_hit | idx_hit | idx_only | avg cost_units |
|---|---:|---:|---:|---:|---:|---:|
| `2025-06-21→2025-06-23` | 243 | 0.4% | 0.4% | 2.9% | 2.5% | 8.2 |
| `2025-12-30→2026-01-04` | 489 | 1.2% | 1.2% | 5.3% | 4.1% | 8.1 |
| `2026-01-05→2026-01-09` | 414 | 1.4% | 1.4% | 3.4% | 2.4% | 7.7 |
