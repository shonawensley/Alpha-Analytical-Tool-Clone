# March 9 Post-Result Assessment Contract

Status: `COMPLETE__EXPLICIT_RESULT_REVEAL_AUTHORIZED_2026-08-02`

## Purpose

This contract defines the result-aware outputs that follow the frozen March 9
predictive analysis. Its rules were frozen before reveal; the separately written
`POST_RESULT` package now executes them after explicit result authorization. Its
purpose is to prevent performance definitions, decay clocks, or credit rules
from being chosen after outcomes are known.

Frozen predictive authority:

- `PREDICTIVE/PREDICTIVE_FREEZE_MANIFEST.json`
- `PREDICTIVE/GOLD_DAY_PREDICTIVE_SYNTHESIS.json`
- `PREDICTIVE/<STATE>/PREDICTIVE_ANALYSIS.json`

The frozen reports are immutable. Post-result analysis must write to a separate
`POST_RESULT` tree.

Completion authority:

- generator: `.codex/march9_post_result_zone_audit.py`;
- package manifest: `POST_RESULT/POST_RESULT_MANIFEST.json`;
- 28 case autopsies: `POST_RESULT/cases/<STATE>/<PERIOD>__<RESULT>/`;
- Gold Day synthesis: `POST_RESULT/GOLD_DAY_POST_RESULT_SYNTHESIS.md`;
- straight ledger: `POST_RESULT/STRAIGHT_PATHWAY_LEDGER.md`.

## Table 1 - Immediate Extraction Evidence Versus Result

One row is required for each state and target period. Preserve these fields:

- state, target period, clock label, result, canonical result, ordered-VTRAC
  identity, boxed-VTRAC index, double subtype, and Fireball availability;
- frozen opportunity classification, emitted family identities, exact route
  members, cumulative width, rank depth, equal-or-stronger competitors, and
  abstention status;
- immediate exact-literal, canonical-box, ordered-VTRAC, boxed-VTRAC, pair,
  double, hidden-core, and extended-cluster capture as separate booleans/ranks;
- strongest valid Extraction Zone 1/2/3 pathway and its de-duplicated lineage;
- first material success or loss stage;
- predictive credit label and post-result discovery label.

Credit rules:

- `PREDICTIVE_CAPTURE` applies only when the frozen route contains the result at
  the exact product level being credited.
- `POST_RESULT_CONFIRMATION` may explain a frozen structure but cannot upgrade
  its original product level.
- `POST_RESULT_DISCOVERY` records a valid reveal-only pathway and receives zero
  predictive credit.
- Exact, canonical/box, ordered-VTRAC, and boxed-VTRAC credits never collapse
  into one generic hit column.
- One underlying string lineage may satisfy multiple descriptive views but is
  counted once as an independent root.

## Dedicated Straight-Pathways Review

Every one of the 28 case autopsies must contain a `Straight Pathways` section.
The target-conditioned winner renderer is secondary evidence; the review must
also scan the corrected raw tables independently so missing renderer tags do not
erase persistent ordered structure.

Required distinctions:

- exact literal persistence, canonical permutations, ordered-VTRAC lane, and
  boxed-VTRAC territory remain separate products;
- canonical-family x ordered-lane intersections list every surviving literal,
  their width, and whether the lane actually reduces the canonical family;
- exact-order isolation and bounded straight portfolios are different outcomes;
- a literal double route retains all three distinct permutations, while a
  three-distinct-digit route retains all six unless a frozen selector narrows it;
- front, back, and end-cap pair orientation, strict consensus, reduction,
  Positional, hidden-core, and extended-cluster clues retain provenance;
- pair, winner-conditioned consensus keys, non-frozen reduction, hidden-core,
  and extended-cluster queries are support-only and cannot independently create
  a defensible straight route;
- a computed lane unsupported by the official VTRAC reference is research-only
  and receives no official ordered-VTRAC credit.

Candidate-symmetric merit is mandatory. Rank `1-14` is the high-merit research
band, rank `15-36` is bounded merit, and lower-ranked winner queries remain weak
or exploratory. These are audit bands, not calibrated live thresholds. Frozen
pre-result evidence that was not emitted is labeled separately from predictive
capture and from reveal-only discovery.

## Table 2 - Five-Draw Decay And Fireball Assessment

Evaluate two cohorts separately:

- frozen pre-result emitted families and order routes;
- frozen pre-result straight evidence that existed but was not emitted;
- strong reveal-only extraction pathways labeled `POST_RESULT_DISCOVERY`.

For every eligible identity, inspect the next five chronological observations
in each available channel:

- Evening;
- Combined;
- bonus-ball sidecar, including Fireball/Wild Ball/Superball only where the
  source digit is verified.

Required fields:

- source state/period, identity type, exact members, original burden, channel,
  offset `D0-D5`, event date/period, result, Fireball value where applicable,
  exact/canonical/ordered-VTRAC/boxed-VTRAC relationship, and first qualifying
  offset;
- whether the pathway persisted, strengthened, contradicted, conveyed, or
  expired;
- unique event ID so the same physical draw is not double-credited through an
  Evening and Combined representation;
- separate denominators for identities, state-period opportunities, channel
  observations, and unique physical draws.

The five-draw boundary measures carry and convey behavior. It does not convert a
later occurrence into an immediate predictive hit. Bonus-ball four-digit
containment is descriptive only: jurisdiction substitution and payout semantics
remain unresolved, so no bonus row may receive combination credit.

## Table 3 - Doubles And Mirror-Doubles Ranking Versus Outcomes

Freeze and hash the pre-result state-ranking source before joining outcomes.
For each state and period, record:

- Gold Day state rank and the exact ranking feature/source;
- whether the result is a literal double, mirror double, triple, or neither;
- exact result and canonical identity;
- frozen extraction classification, emitted double families, route width, and
  immediate/decay capture;
- rank bucket, all-state denominator, doubles-event denominator, and any state
  tie handling.

The table must distinguish state ranking quality from combination containment.
A correctly ranked doubles state is not a combination hit unless the frozen
route also contains the result at the credited product level.

## Required Readbacks Before Analysis

1. Revalidate all manifest hashes and confirm state predictive reports are
   unchanged.
2. Inventory authoritative result, subsequent-draw, and Fireball source paths,
   cutoffs, schemas, and duplicate physical-draw relationships.
3. Confirm the doubles ranking source is genuinely pre-result and hash-freeze
   it before result join.
4. Produce the 28 result-aware conversion autopsies before Gold Day aggregation.
5. Report immediate and decay findings separately, including misses,
   abstentions, burden, and unresolved semantics.

Completion receipt: all 28 JSON and Markdown autopsies, all three requested
tables, the straight-pathway ledger, Gold Day synthesis, and hash manifest pass
the generator's `--validate-only` audit. No profitability, bankroll, or
runtime-policy claim is allowed without later action-cost, payout, holdout, and
live-shadow validation.
