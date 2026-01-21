# Predictive Workflow — v0.2 Addendum (Selection + Measurement)

Purpose: capture what changed in v0.2 so predictive runs remain coherent after context resets.

This is an addendum to:
- Predictive day quickstart: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`
- v0.2 integration narrative: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- v0.2 defaults: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

---

## v0.2 posture (what is “real” now)

- Predictive sharepacks (`sharepacks/_predictive/<D>/...`) are the immutable **BEFORE** snapshot (winners-free).
- RUNS is the **grading + review layer** (writes analysis outputs only; never mutates predictive packs).
- v0.2 avoids analyzer edits; improvements come from:
  - making evidence deterministic + explainable, and
  - adding bounded, measurable selection-layer transforms (default-off unless proven).

Default ablation posture:
- `--profile tool_only` (Profit Alerts quarantined; still measurable via `mixed`/`profit_only`).

---

## What we added during v0.2 (so you can actually debug/iterate)

### 1) Candidate Universe “evidence view” (audit/debug)

When generating Candidate Universe, add:
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --write-evidence
```

This writes `candidate_universe_evidence__tool_only.{csv,md}` next to the JSON so you can separate:
- direct tool/board evidence, vs
- derived/transform packs (and why they exist).

### 2) Signals bundle export (predictive-safe superbrain input)

When you need a stable “signals contract” for later aggregation, add:
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --write-signals-bundle --experiment-tag <TAG>
```

This writes:
- `signals_bundle__tool_only__<TAG>.json`

### 3) Brain‑2 policy comparison harness (Top‑N triage; tracks `hit_any` + `box_hit`)

This is the “stop going in circles” harness for portfolio/ranking ideas:
```bash
python3 scripts/tools/superbrain_config_harness.py --start-date <A> --end-date <B> --sharepacks-root sharepacks/_predictive --profile tool_only
```

Outputs (RUNS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_CONFIG__HARNESS__<A>_to_<B>.{md,csv}`

Notes:
- `hit_any` ≈ “did we cover the winner as played” (straight or boxed semantics).
- `box_hit` ≈ “did we at least surface the winning canonical” (lane visibility, conversion potential).

---

## Where to start when you feel lost

- Portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- Coverage proof: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__COVERAGE_LEDGER.md`
- v0.2 defaults: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

