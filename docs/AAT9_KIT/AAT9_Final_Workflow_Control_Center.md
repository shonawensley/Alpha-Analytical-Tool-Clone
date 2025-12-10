# AAT9 Final Workflow – Control Center Pause Log

Date: 2025-12-09 (UTC)

## What is done (Brain2 / Control Center)
- Snapshot/alerts pipeline lives in `scripts/tools/cc_sanity_snapshot.py` (read-only). It checks table freshness vs draws, computes draws-since-double, flags VTRAC repeats, ingests Blackapple alerts, and tags hits (exact/boxed/vt_boxed/vt_straight).
- Alert contract is frozen in `reports/control_center/alert_schema.json`; state labels resolve through `reports/control_center/state_map.json`.
- BA ingest is explicit: reads `reports/control_center/control_center.md` when present, or `--ba-csv/--ba-json` flags. Missing BA is warned, not silent.
- Outputs land under `reports/control_center/cc_snapshot_<timestamp>.{json,csv,_alerts.csv,.md}`; alert summaries list counts/hits by alert id (blackapple, due_doubles, vtrac_repeat).
- Regression guard: `scripts/checks/test_cc_snapshot_schema.py` validates outputs against the schema.

## How to run the snapshot
```bash
python3 scripts/tools/cc_sanity_snapshot.py \
  --results-file data/results/2025-06-21.txt \
  --state-map reports/control_center/state_map.json
```
Outputs are written to `reports/control_center/` with the timestamp. Freshness compares `data/outputs/tables/<STATE>/Combined_Combined.csv` Set1/Draw1 col1/col2 to the latest draw in `data/cleaned/draws/<STATE>_draws.csv`.

Regression check:
```bash
python3 scripts/checks/test_cc_snapshot_schema.py
```

## Pause line (pre-A01–A12)
- Implemented alerts: `blackapple`, `due_doubles`, `vtrac_repeat` with hit tagging across four criteria.
- Not yet implemented: A01–A12 profitability indicators. Schema and hit tagging are ready; add them as detectors emitting the same alert shape.
- State matching is deterministic via `state_map.json`; avoid heuristic matching going forward.

## When resuming Control Center
- Keep the alert schema stable; emit `{id, state, variant, date, strength?, status?, evidence, hits}` for any new indicator.
- Use the BA ingest flags if `control_center.md` is absent; warn if BA cannot be parsed.
- Reuse `modules.vtrac_reference` for VT hit tagging; do not change VT mappings.
- Consider a short Markdown summary per snapshot run for quick human review (freshness mismatches, top due-doubles, alert hit counts).

## Pivot focus (Brain1 / Aggregator prep)
- Brain1 work resumes next: lean evidence bundles per tool, unified winners logger, and an aggregator “super brain” consuming the bundles.
- Keep Control Center paused here until the Brain1/aggregator pass is defined; then return to add A01–A12 using the frozen alert schema/hit pipeline.
