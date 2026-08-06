# Merit-Allocated VTRAC Cluster Worked Example

## Case Boundary

| Field | Value |
|---|---|
| State | `Connecticut4` |
| Results date | `2026-03-09` |
| Graded period | `Evening` |
| Winner | `091` |
| Canonical winner | `019` |
| Internal boxed VTRAC index | `9` |
| Generator | `merit_allocated_vtrac_cluster_slate_v1` |
| Generation mode | `DEVELOPMENT_WINDOW_REPLAY` |
| Claim class | retrospective winner-free, in-sample diagnostic |

The route was created after this historical result, but the generator did not
receive the winner and read only frozen predictive artifacts. It therefore
supports implementation diagnosis, not original or holdout predictive credit.

## Why This Is A Third Route

The route does not replace either compact slate:

1. The Anchor route ranks direct structural candidate evidence.
2. The Closure route applies bounded mirror, VTRAC, double, and key-digit
   translations to those anchors.
3. This route first identifies independently qualified lingering boxed VTRAC
   clusters, protects more than one cluster from global-rank exhaustion, and
   allocates separate boxed and ordered candidates by merit.

One cluster ledger feeds two distinct surfaces:

- `BOXED12` traps canonical territory across multiple qualified VTRAC clusters.
- `STRAIGHT12` selects ordered literals only when direct pattern, Vcode,
  Candidate Universe, Sandbox, or positional order evidence exists.

The straight surface is not a permutation expansion of `BOXED12`.

## Input And Safety Receipt

The replay consumed:

- predictive `Connecticut4_tables.json`;
- Candidate Universe;
- Aggregated Analysis Arena;
- Translation Sandbox;
- Aux summary.

Only `R2/R4/R6/R8` pattern rows were scanned. `draw_data` was excluded before
triple extraction, so the prior draw-data inflation around `591` did not create
pattern merit.

Static scoreboard order was not used. Aux could reinforce a structurally
qualified cluster but could not make a cluster eligible.

## Cluster Merit

| Merit Rank | VTRAC Index | Structural | Arena | Aux | Total | Strict Cells | Short Cells | Full R-Row Boxes | Horizontal Groups | Selection Read |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 18 | 97.709 | 20.000 | 5.000 | 122.709 | 256 | 79 | 34 | 69 | Arena top-three and structural gate |
| 2 | 23 | 75.203 | 10.922 | 2.500 | 88.625 | 189 | 25 | 20 | 56 | Arena top-three and structural gate |
| 3 | 24 | 54.391 | 9.017 | 5.000 | 68.407 | 128 | 62 | 8 | 38 | highest remaining merit |
| 6 | 9 | 46.147 | 11.993 | 2.500 | 60.640 | 116 | 47 | 8 | 27 | Arena top-three and structural gate |

Index `9` was not the highest global cluster, but it independently cleared the
structural gate and received protected allocation. This is the intended
multi-cluster behavior: a dominant index cannot consume every slot before a
qualified secondary corridor is represented.

## D5-D7 Route Ledger Projection

| Route ID | Family | Mode | Play | Members | Count | Cost | Claim / Readiness |
|---|---|---|---|---|---:|---:|---|
| `CT4-RPL-MAVC-BOX12-v1` | `BOX_DIVERSIFIED` | `DEVELOPMENT_WINDOW_REPLAY` | BOX | `168,019,368,689,668,069,688,189,118,138,366,336` | 12 | 57 straight-equivalent lines | in-sample diagnostic |
| `CT4-RPL-MAVC-STR12-v1` | `STR_DIVERSIFIED` | `DEVELOPMENT_WINDOW_REPLAY` | STRAIGHT | `681,906,688,198,668,901,683,986,386,186,836,138` | 12 | 12 literal lines | in-sample diagnostic |

The machine-readable artifact carries the corresponding template locators under
`deep_review_mapping.surface_routes`.

## D10 Pack Comparison Projection

| Pack | Geometry | Width | Candidate Coverage | String Merit | Aux Role | Transformation Distance | Decision |
|---|---|---:|---|---|---|---|---|
| `BOXED12` | four qualified boxed VTRAC clusters | 12 boxes | protected primary and secondary lanes | direct pattern-led | reinforce only | canonical territory | `RESEARCH_ONLY` |
| `STRAIGHT12` | bounded ordered candidates from the same clusters | 12 literals | no blind canonical permutation closure | direct order plus bounded lane evidence | shape/tie-break | ordered literal | `RESEARCH_ONLY` |

## E1 Outcome Projection

| Surface | Exact `091` Present? | Canonical `019` Present? | Winning Index Selected? | Grade |
|---|---|---|---|---|
| `BOXED12` | represented canonically | yes, slot 2 | yes | `CANONICAL_BOX` |
| `STRAIGHT12` | no | yes through `901`, slot 6 | yes | `CANONICAL_ORDER_MISS` |

This is a meaningful but bounded result. The route preserved the winning VTRAC
cluster and trapped the winning box without using the result. It did not prove
the exact order.

The exact `091` order was not selected. Any future rule that promotes an
ordered lane mate must be tested across frozen cases and cannot be inferred
from this result after the fact.

## Harness Questions

- Does protected multi-cluster allocation improve boxed hit efficiency on
  untouched cases versus one global ranking?
- Is two base slots per qualified cluster preferable to one or three?
- Does the six-slot per-cluster cap prevent dominant-lane over-allocation?
- Which independent order features can move a correct ordered lane member into
  `STRAIGHT12` without draw-data support or full-lane expansion?
- At equal width, does `BOXED12` add canonical lift beyond Anchor `CORE3`,
  Anchor `EXTENDED6`, and Closure `EXTENDED6`?
- Does the secondary-cluster allocation retain useful hits often enough to
  justify its opportunity cost?

No answer from this one case authorizes a runtime score, route, or allocation
change.

## Reproduction

```bash
python3 scripts/tools/create_merit_allocated_vtrac_cluster_slate.py \
  --candidate-universe \
  sharepacks/_replay_rpattern_current/2026-03-09/Connecticut4/candidate_universe__tool_only__rpattern_current_v1.json \
  --target-period Day \
  --run-mode development_replay \
  --output \
  .codex/shadow_slate_commit_smoke/Connecticut4_merit.json
```

```bash
python3 scripts/tools/grade_merit_allocated_vtrac_cluster_slate.py \
  --slate \
  .codex/shadow_slate_commit_smoke/Connecticut4_merit.json \
  --winner 091 \
  --period Evening \
  --output \
  .codex/shadow_slate_commit_smoke/Connecticut4_merit_grade.json
```
