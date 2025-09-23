# AAT9 – Auxiliary Draw Variants Addendum

This addendum summarizes the new "variant" dimension introduced for Auxiliary/Blackapple tooling.

## Supported Variants
- **Combined** – legacy behaviour using `<State>_draws.csv`.
- **Midday** – reads `<State>_Midday_draws.csv` when available.
- **Evening** – reads `<State>_Evening_draws.csv` when available.

All variants use the same newest-first draw contract (3-character strings) managed through `modules.aux_loaders.load_state_draws(state, variant)`.

## Control Center Updates
- Doubles tracker now lists `(State, Variant)` rows with draw counts, latest double, and source path (dev caption).
- Blackapple expands to Combined/Midday/Evening rows; the table shows triggers and examples per variant and the source caption includes the resolved CSV.

## Auxiliary Tools Page
- Variant selector (Combined, Midday, Evening) reruns the full working analysis per variant.
- Repeating/non-repeating pair panels hide the purple “Pending” rows for Midday/Evening variants, preserving Combined as the baseline reference.
- Blackapple alert panel consumes variant-specific draws; the caption displays the resolved file and draw count.

## Loader Contract
```
from modules.aux_loaders import load_state_draws

# returns (draws_list, resolved_path or None)
draws, path = load_state_draws("Connecticut4", variant="midday")
```
- Fallback order: `data/cleaned/draws/`, legacy `data/cleaned/`, optional extractor regen for Combined only.
- When a variant file is missing the UI soft-fails with an informative caption; Combined remains required for baseline analytics.

## Operational Notes
- Regenerating Midday/Evening CSVs continues to use the Aux Draws Pipeline expander; Combined regeneration is untouched.
- `python scripts/checks/smoke_aux_vtrac.py` still verifies staged modules; run it before/after large changes.
- Dev Health captions on both Control Center and Aux page list the resolved draw path and record count per variant for quick validation.
