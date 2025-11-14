# AAT9 — Central Winners Module (Draft)

## Purpose
Produce a single per-date, per-variant winners log that merges every tool’s view (Stable, V-TRAC, Digit Reduction, Aux). The module classifies each winner into four hit levels:

1. `exact_straight` — digits + order.
2. `exact_boxed` — digits, any order.
3. `vt_boxed` — winner sits in an 8-way VT index.
4. `vt_straight` — winner aligns with a VT straight lane (ordering hint).

These classes become the Analyzer’s “ground truth” when scoring tooling performance or feeding downstream decision logic.

## Inputs (per state/date)

| Tool / Artifact | Location | Fields consumed |
| --- | --- | --- |
| Stable sharepack | `sharepacks/YYYY-MM-DD/<STATE>/stable/` | `*_stable_patterns_scores.csv` (VT-straight metadata), `*_stable_patterns_compound.csv` (`vt_only_lane`, `funnel_precol1`), `*_metrics.json` (`winner_hits`), `*_winner_family_spotlight_{raw,families}.csv` (`is_exact_*`, `is_vtrac_boxed`). |
| V-TRAC analyzer | `data/outputs/analysis/vtrac/<STATE>/...` (or future sharepack) | `vtrac_compact_report.{csv,json}` (index ranks), analyzer winners HTML (VT index highlight). |
| Digit Reduction | `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/` | `*_top_candidates.csv` or winners overlay (when diagnostics enabled). |
| Aux / Control Center | e.g., repeat-watch output, positional trackers | Optional: double gaps, positional pressure hits, etc. (future phases). |

The module does **not** rerun tool code; it only reads these lean artefacts.

## Outputs

- `winners/YYYYMMDD_<Variant>_winner_map.json`
- `winners/YYYYMMDD_<Variant>_winner_flags.csv`
- Optional summary (`winners/YYYYMMDD_summary.md`) highlighting tool-by-tool hits.

Each winner record should include:

```json
{
  "winner": "733",
  "variant": "Midday",
  "state": "Florida4",
  "classes": {
    "exact_straight": true,
    "exact_boxed": true,
    "vt_boxed": true,
    "vt_straight": true
  },
  "tool_evidence": {
    "stable": { "best_compound_rank": 60, "vt_only_lane": false, ... },
    "vtrac": { "index": 29, "straight_lane": ["733", ...] },
    "digit_reduction": { "top_rank": 12, ... }
  }
}
```

## Workflow (per date)

1. Ensure sharepacks for all states (`sharepacks/YYYY-MM-DD/<STATE>/...`) and V-TRAC/Digit Reduction outputs exist.
2. The winners module:
   - Canonicalizes each winner (Midday + Evening).
   - Pulls Stable metrics/spotlight to flag exact hits and VT-family coverage.
   - Reads V-TRAC compact report to confirm VT index hits and straight lanes.
   - (Future) Reads Digit Reduction overlay to see if the winner’s family was in the top stack.
3. Emit `winner_map.json` + `winner_flags.csv` at `winners/YYYY-MM-DD/`.
4. Optionally append a summary to `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` or a future Analyzer log.

## Next Steps

1. **Prototype script** — iterate over a single date (e.g., 2025‑06‑24) using the existing sharepacks to prove the JSON/CSV structure.
2. **Integrate with Control Center** — expose a “Generate winners summary” button that calls the script and shows per-state tables.
3. **Analyzer consumption** — the Analyzer’s scoring engine will read the winner map to evaluate precision/recall across tools.

This document will evolve as we bring V-TRAC and Digit Reduction up to the same lean standard, but the overall goal stays the same: one canonical winners log per day, four hit categories, sourced entirely from the lean artefacts.
