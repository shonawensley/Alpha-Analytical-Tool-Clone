# Aux + Control Center Handoff

Date: `2026-03-16`

## Current Role

`Aux + Control Center` should now be treated as:

- the system's broadest predictive context layer
- a compound-pressure and regime-description layer
- a family / index reinforcement layer

It should **not** be treated as a tiny direct-caller oracle.

## Predictive-Side Artifacts To Feed The Arena

Primary:

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`
- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

## Most Valuable Arena Contribution

The best arena contribution is broad structured context:

- positional pressure
- VTRAC pressure
- badge pressure
- pair / combo overdue context
- due-double family pressure
- repeat-watch context
- sums context
- Blackapple context
- profit-alert context
- compound-event context

## Heavy Truth Layers To Keep Reachable

Keep available for deep arena review:

- full boxed VTRAC badge tables
- raw badge rows and organized badge criteria
- full pair-status tables
- Blackapple candidate ledgers
- detailed profit-alert evidence JSON

These do not all need to be flattened into the arena, but they should not disappear.

## Important Boundary

Current narrow predictive methods such as:

- `aux_positional`
- `aux_vtrac_index_overdue`
- `mirror_pair_closure`
- `due_doubles`

remain useful as bounded conversion surfaces.

They are **not** the final statement of Aux / Control Center value.

## One Bounded Finish Still Worth Doing

That slice has now landed:

- `scripts/tools/aux_control_center_arena.py`
- `create_candidate_universe.py --write-aux-cc-arena`
- signals bundle `tools.aux_control_center_context`

The bounded finish was:

- one broader export/wiring pass from existing Aux summary + Control Center artifacts into richer arena objects

Not:

- another narrow scoring loop
- another effort to force Aux / Control Center into a tiny top-caller

## Freeze Criteria

Freeze `Aux + Control Center` for this phase when:

1. the arena contract is explicit
2. the current narrow predictive subset is clearly labeled as conversion-only
3. heavy truth layers are linked rather than silently dropped
4. one final export/wiring decision is made

Current status:

- criteria `1-4` are now satisfied for this phase

## Recommended Next Step After Freeze

Move `Aux + Control Center` into the aggregated analysis arena as the broad compound-context layer and judge any remaining gap there before reopening tool-local tuning.
