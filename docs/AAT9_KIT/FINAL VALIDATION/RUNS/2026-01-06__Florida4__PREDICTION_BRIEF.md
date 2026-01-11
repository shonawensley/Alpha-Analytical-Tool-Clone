# Florida4 — Prediction Brief (Pre-Results) — D=2026-01-06

This is a **pre-results** brief for the **Florida Evening** draw on results date **D=2026-01-06**.

## Provenance (what this is based on)

- Sharepack (frozen snapshot): `sharepacks/2026-01-06/Florida4/`
- World snapshot source workbook (H = D-1): `data/history/Pick3StatsC4_2026-01-05.xlsm`
- Results file (D): `data/results/2026-01-06.txt`
  - Midday known: `209`
  - Evening: **blank / pending**

Important: the Brain‑1 artifacts in this sharepack are produced from **H=2026-01-05** (the D‑1 workbook). The Midday result `209` is recorded in the results file, but it does **not** retroactively change the frozen tables/tool outputs for the day snapshot.

## “Core” candidate set (highest cross-tool convergence)

### BOX `346` (6 perms)

This is the strongest single cluster across independent lenses:

- Profit Alerts (Control Center): `A04` (Evening) recommends `BOX 346` with the full permutation set.
  - Source: `sharepacks/2026-01-06/control_center/profit_alerts.csv`
- Stable patterns (Evening) ranks `346` as a top boxed candidate.
  - Source: `sharepacks/2026-01-06/Florida4/stable/Florida4/Florida4_stable_patterns_scores.csv` (see `section=Evening`, `Canonical=346`)
- VTRAC enhanced top straights include multiple `346` perms (e.g., `634`, `436`, `364`) and the underlying index stack is hot.
  - Source: `sharepacks/2026-01-06/Florida4/vtrac/Florida4/Florida4_vtrac_enhanced_20260106_214447.json` (`top_straights`, `indices_ranked`)
- Aux positional shortlist’s highest scores include `436` and multiple 3/4/6 mixes with “Double‑Pressure” + cross‑variant tags.
  - Source: `sharepacks/2026-01-06/Florida4/aux/Florida4/summary.json` (`positional.shortlist_report.candidates`)

Permutation set (from Profit Alerts `ImpliedSet`):

- `346 364 436 463 634 643`

## Secondary “small-set” candidates (tight, double-family leverage)

These are small, high‑signal sets surfaced by the Control Center profit layer. They are also coherent with the “due doubles families” board (recent double behavior).

### STR8_3 `033` (3 perms)
- Source: Profit Alerts `A05` (Combined): `sharepacks/2026-01-06/control_center/profit_alerts.csv`
- Implied set: `033 303 330`

### STR8_3 `077` (3 perms)
- Source: Profit Alerts `A10` (Combined): `sharepacks/2026-01-06/control_center/profit_alerts.csv`
- Implied set: `077 707 770`

For context, Florida due-doubles families (as-of the frozen draw snapshot) include `077` and other mirror-double families:
- Source: `sharepacks/2026-01-06/control_center/due_doubles.csv` (rows for `Florida4`)

## Tertiary “index clamp” set (VTRAC-lane closure)

### STR8_4of8 `334` (4 canonicals)
- Source: Profit Alerts `A12` (Combined): `sharepacks/2026-01-06/control_center/profit_alerts.csv`
- Implied set: `334 339 384 389`
  - Note: `384` is a permutation of canonical `348` (same VTRAC index family).

Interpretation: this is a compact “lane closure” slice over a hot VTRAC family (the vtrac enhanced report has index‑level heat in its top stack).

## Optional adds (if you want a slightly wider card without going full scatter)

If you want to widen beyond the Profit/Stable/VTRAC core, use Aux positional shortlist to add a few high-score items not already covered by the `346` perms:

- Examples (high scoring, from Aux shortlist): `236 246 256 636 646 433 233`
  - Source: `sharepacks/2026-01-06/Florida4/aux/Florida4/summary.json`

Digit Reduction also surfaces a strong Evening candidate cluster around `559`/`550` (independent lens); treat as optional unless it starts to cohere with the other three lenses above:
- Source: `sharepacks/2026-01-06/Florida4/digit_reduction/Florida4/summary.md` (Top candidates section)

## After the Evening result posts (so this becomes “gradeable”)

Once you have the Florida Evening result for `2026-01-06`, do:

1) Update `data/results/2026-01-06.txt` to include the Evening value for Florida.
2) Regenerate Florida’s winners lens for Evening (and Combined lens if needed), then refresh DR overlay/analyzer stamp (`20260106`) for the newly known winner.
3) Re-run `python3 scripts/tools/export_control_center_sharepack.py --date 2026-01-06` so Brain‑2 reflects the full day.
4) Re-run `python3 scripts/tools/fill_master_validation_run_report.py --date 2026-01-06 --state Florida4` to re-embed updated evidence blocks into the run report.

