# AAT9 – Aux Roadmap (Training / Feature Dev)

## Current Baseline (Phase-1)
- **SSOT constants** live in `core/aux_config.py` (pairs, positional, sums, V-TRAC, combo windows + thresholds)
- Aux captions, Dev Health, and Control Center Repeat Watch all read from that SSOT
- V-TRAC mini + working table share `_build_vtrac_overlay`; repeat stats via `_summarize_vtrac_repeats`
- Staged smoke (`scripts/checks/smoke_aux_vtrac.py`) bootstraps `src/` so it resolves the same SSOT
- Guardrails: `tests/test_analyze_pairs_semantics.py`, headless Streamlit boot, preflight note updated

## Ready for Training
- Digit Reduction + V-TRAC analyzer fixes are deployed; current UI compiles + smokes pass
- You can resume data runs (e.g., with the fresh Pick3StatsC4) before we add more features

## Immediate Follow-ups (Phase-1B)
1. **Aux feature extractor** – implement `aux_features.extract(state, variant)` returning the agreed dict (pair bands, V-TRAC overdue/recent flags + draws-since, sums due flags)
   - Mirror results into the existing run logs + winners overlay outputs (align with AUX_WATCH definition of done)
2. **Runtime validation** – re-run Digit Reduction Analyzer V2 and the refreshed V-TRAC page against the new Pick3StatsC4 drop; capture results to verify hardened pipelines on fresh data

## Deferred / Phase-2
- Add additive Aux scoring weights (after logging evidence)
- Control Center “Aux heat” leaderboard and BA tweaks based on SSOT thresholds
- Extended logging/analytics (e.g., trending repeat deltas, Aux feature joins in Winners logging)
- Hot Zones module, aggregate profitability dashboards, ML experiments (see BIG_PICTURE)

## References
- `tasks/AUX_WATCH.TXT` – operational checklist for Aux feature work
- `tasks/AUX_RESEARCH.TXT`, `AUX_VALIDATE.TXT`, `AUX_1.TXT`, `AUX_2.TXT` – research + validation deep dives
- `tasks/BIG_PICTURE.TXT` – overarching vision + remaining macro tasks
- `tasks/FIX_80.TXT` – latest audit + plan sign-off


## Aux Scoring Outlook
- **What’s ready:** SSOT windows/thresholds (`core/aux_config.py`), shared V-TRAC overlay + repeat watch, positional/pairs/sums snapshots, and regression guards (pytest + smokes). These outputs already expose the raw signals we will score later.
- **Stage 1 – Feature export:** implement `aux_features.extract(state, variant)` returning pair bands, V-TRAC overdue/recent stats, sums flags, positional consensus. Mirror into daily run logs and winners overlays once the Official Post flow exists.
  - Shipped: Control Center now surfaces Top 5 V-TRAC double families per state (red/blue severity, variant badges) replacing the ad-hoc pair/combo columns; Aux page shows the same rankings and a family column on the V-TRAC table.
- **Stage 2 – Evidence gathering:** use the run packages to accumulate feature vectors alongside string-tool outputs and winners so we can quantify which signals deserve weight.
- **Stage 3 – Scoring/aggregation:** design additive weights or rules (state-level “Aux heat”, candidate-level boosts) only after Stage 2 confirms signal quality—Aux remains a compounding input so Stable/DR/V-TRAC stay primary.
- **Stage 4 – Control Center integration:** surface validated Aux rankings/alerts (repeat streak heat, overdue pairs, positional pressure) in aggregate dashboards and gating logic.
- **Open TODOs:** Stage 1 extractor & logging (Phase-1B), Official Post run packaging, later Stage 3/4 scoring guardrails.
