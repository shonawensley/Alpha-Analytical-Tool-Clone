# Compact Candidate Slates

## Purpose

These shadow tools create three complementary extraction routes without changing
Candidate Universe, Play Cards, Analysis Arena, or the runtime cadence.

1. `structural_convergence_anchor_slate` answers: what does the existing
   predictive evidence directly support?
2. `bounded_vtrac_closure_slate` answers: can bounded VTRAC, double, mirror, and
   key-digit translation improve that direct extraction?
3. `merit_allocated_vtrac_cluster_slate` answers: which independently qualified
   lingering VTRAC clusters deserve protected candidate allocation before one
   global ranking exhausts the list?

They are diagnostic experimental surfaces. They are not selected, funded, or
realized predictions unless a separate pre-result receipt says so.

## Inputs

The Anchor Slate requires a Candidate Universe JSON. It automatically discovers
the matching Aggregated Arena and Translation Sandbox JSON files when they are
present beside a standard predictive sharepack.

The Merit-Allocated route additionally requires the state's frozen predictive
`*_tables.json`. It scans only R2/R4/R6/R8 pattern rows. It automatically
discovers the matching Arena, Sandbox, and Aux summary when available.

Shadow mode rejects Candidate Universe payloads that declare winner artifacts or
leakage issues. A historical reconstruction must explicitly use
`--run-mode development_replay`, and its outputs remain replay evidence.

Static scoreboard order is never used as a score.

## Run

```bash
python3 scripts/tools/create_structural_convergence_anchor_slate.py \
  --candidate-universe sharepacks/_predictive/<DATE>/<STATE>/candidate_universe__tool_only__arena_v0.json \
  --target-period Evening
```

```bash
python3 scripts/tools/create_bounded_vtrac_closure_slate.py \
  --anchor-slate sharepacks/_predictive/<DATE>/<STATE>/analysis/structural_convergence_anchor_slate__tool_only__arena_v0.json
```

```bash
python3 scripts/tools/create_merit_allocated_vtrac_cluster_slate.py \
  --candidate-universe sharepacks/_predictive/<DATE>/<STATE>/candidate_universe__tool_only__arena_v0.json \
  --target-period Day
```

After the result exists, grade into a separate result-dependent artifact:

```bash
python3 scripts/tools/grade_compact_candidate_slates.py \
  --slate <ANCHOR_SLATE.json> \
  --slate <CLOSURE_SLATE.json> \
  --winner 091 \
  --period Evening \
  --output <POST_RESULT_GRADE.json>
```

```bash
python3 scripts/tools/grade_merit_allocated_vtrac_cluster_slate.py \
  --slate <MERIT_ALLOCATED_SLATE.json> \
  --winner 091 \
  --period Evening \
  --output <POST_RESULT_GRADE.json>
```

Each command writes JSON plus a matching Markdown view.

## Anchor Scoring

The Anchor Slate normalizes evidence rather than adding incompatible raw tool
scores. Its score components cover:

- Arena and Sandbox promotion roles.
- Independent source families.
- Cross-variant agreement.
- survivor/frontier recurrence.
- VTRAC corridor rank or watchlist support.
- Aux, Due Doubles, Profit Alert, consensus, and positional confirmation.
- Straight-equivalent cost.
- Sparse or single-source noise penalties.

Repeated renderings from the same source family, variant, and role share one
lineage. They preserve all source IDs but receive one scored vote.

## Closure Rules

The Closure Slate starts from the Anchor Slate and permits only bounded,
traceable transformations:

- Preserve the direct anchor.
- Replace one repeated digit with its VTRAC mirror.
- Apply a full repeated-pair mirror only with independent support.
- Mirror the key digit only with independent support.
- Apply combined repeated/key mirrors only through stronger gates.
- Recombine a supported VTRAC mirror pair with a supported lingering key digit.
- Permit single-digit mirror closure for unique-digit anchors only when at least
  two supporting lineages or direct candidate support exists.

The generator never performs unrestricted digit recombination or blindly closes
an entire VTRAC index.

The project terms `Mirror-Echo` and `Double-Pressure` are evidence gates. The
candidate transformation itself is recorded separately, for example
`double_anchor_one_mirror`.

## Merit-Allocated Cluster Rules

The third route starts from the raw pattern progression rather than the global
candidate ranking. It:

- Excludes draw data before extracting any triples.
- Measures vertical R-row agreement, horizontal persistence, Set1/currentness,
  short survivor-like cells, long-string structure, and cross-variant breadth.
- Requires a structural eligibility gate before Arena or Aux can add merit.
- Protects structurally qualified Arena top-three VTRAC clusters.
- Allocates two initial candidate opportunities per qualified cluster when
  direct candidates exist.
- Allocates remaining positions by marginal cluster and candidate merit.
- Caps one cluster at six positions and never force-fills weak candidates.
- Deduplicates evidence by source type rather than adding repeated renderings as
  independent discoveries.

The route emits two sibling surfaces from one cluster ledger:

- `BOXED12`: up to 12 canonical boxes for territory trapping.
- `STRAIGHT12`: up to 12 ordered literals. It uses direct order, ordered Vcode
  recurrence, Sandbox/Candidate Universe order, positional evidence, and bounded
  VSTRAIGHT lane mates. It does not blindly permute every boxed candidate.

`BOXED12` candidate count is not the same as wager-line count. The artifact also
reports straight-equivalent cost for each canonical box.

## Width and Cost

The Anchor and Closure routes produce nested widths:

- `CORE3`: up to three boxed canonicals.
- `EXTENDED6`: contains all CORE3 candidates and adds up to three more.

Weak evidence can leave slots unused. Every tier records boxed count and
straight-equivalent line cost:

- unique-digit box: 6 straight lines;
- double: 3 straight lines;
- triple: 1 straight line.

The Merit-Allocated route is separate from these nested tiers. Its two surfaces
each cap at 12 candidates, can leave slots unused, and record allocation by
VTRAC cluster.

## Post-Result Interpretation

The grader separates:

- `CANONICAL_BOX`;
- `VTRAC_ONLY`;
- `NO_MATCH`;
- ordered-hint observation, which does not receive funded straight credit;
- direct-anchor versus derived-translation canonical matches;
- CORE3 versus EXTENDED6 incremental lift.

Joint diagnosis then reports whether the direct slate, closure slate, both, or
neither captured the canonical winner.

The Merit-Allocated grader separately reports:

- whether the winning VTRAC cluster survived cluster selection;
- `BOXED12` canonical-box or VTRAC-only credit;
- `STRAIGHT12` exact straight, canonical-order miss, VTRAC-only, or no-match;
- candidate width and boxed straight-equivalent cost.

## Deep Review Placement

When these artifacts are admitted into the Deep Review, keep them as three
separate experimental rows:

- Experimental direct structural extractor.
- Experimental bounded translation/closure extractor.
- Experimental merit-allocated multi-VTRAC extractor, with `BOXED12` and
  `STRAIGHT12` shown as separate sub-rows.

Compare them with Arena/Sandbox, Candidate Universe, and legacy Play Cards.
Do not merge their evidence votes, and do not label any surface selected or
funded without a frozen receipt. Brain 2 can aggregate their hit type, width,
cost, direct-versus-derived attribution, marginal EXTENDED6 lift, winning-cluster
retention, and secondary-cluster allocation lift.

The Connecticut4 `091` replay and exact D5-D10/E mapping are documented in
`briefings/MERIT_ALLOCATED_VTRAC_CLUSTER_WORKED_EXAMPLE__CONNECTICUT4__091.md`.
