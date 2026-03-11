# AAT9 ANALYSIS ARENA INTEGRATION QUEUE

Purpose: a single live queue for converting deep-dive findings into real integration work.

Use this alongside:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_DEEP_EXAMPLE_REVIEW_ANALYSIS.md`
- casepacks / winners HTML+JSON
- predictive artifacts (baseline and arena-branch)

This queue is for the **analysis arena branch** of the system and is intentionally comparative:
- `truth` = winners artifacts / post-results receipts
- `baseline` = latest predictive system behavior
- `arena branch` = new evidence-preserving / conversion-aware branch we are building

The point is not to collect ideas passively. The point is to make every important finding land in one of these buckets:
- `rule`
- `tracker`
- `tool`
- `arena`
- `policy`
- `test`

Status legend:
- `noted` = captured, but not approved yet
- `approved` = direction agreed; ready to implement
- `implemented` = coded / wired
- `validated` = checked on real examples / tests
- `deferred` = intentionally postponed

---

## Working Method

For each example:
1) inspect `truth`
2) inspect `baseline`
3) inspect `arena branch`
4) log every important outcome here
5) implement the clear items during or immediately after the example when practical
6) re-check the same example

Guardrail:
- do not let important findings stay only in prose if they clearly belong in tracking, scoring, extraction, or policy.

---

## Current Priority Order

This keeps the queue actionable. It answers: “what should we code next, in what order?”

### Priority 1 — Stable compounding observability [done]

- `TRACK-011`
- `TOOL-007`
- `TEST-009`

Reason:
- The first post-Arena implementation slice is now making the R2/R4/R6/R8 roll-up explicit, so we can inspect what compounding adds before touching hidden-family logic or retuning weights.

### Priority 2 — Stable hidden-family preservation [done, observability-only]

- `TOOL-001`
- `TOOL-002`
- `ARENA-001`
- `TRACK-006`
- `TEST-005`

Reason:
- Example 1 already proved the winners artifact is exposing family evidence that the predictive path does not yet preserve explicitly enough.
- The slice is now implemented and validated as an arena evidence surface; calibration still comes later before any ranking or promotion use.

### Priority 3 — Stable order / VT-straight conversion [done, observability-only]

- `TOOL-003`
- `TOOL-004`
- `ARENA-002`
- `TRACK-002`
- `TRACK-008`
- `POLICY-004`

Reason:
- Example 1 also proved that modal order / fragment evidence may be one of the cleanest bridges from lane correctness to strict conversion.
- The slice is now implemented as an arena evidence surface; transform promotion still needs later calibration and bounded policy work.

### Priority 4 — Stable family-lane promotion review [done]

- `TOOL-005`
- `TEST-002`
- `TEST-003`
- `TEST-016`

Reason:
- `stable_family_vote_v2` is now implemented and validated as a bounded extra family-lane promotion rule using richer arena evidence.
- See `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-11__STABLE_FAMILY_VOTE_V2__VALIDATION.md`.

### Priority 5 — Pair-anchor / lingering fourth-variable closure

- `RULE-020`
- `TRACK-014`
- `TOOL-008`
- `ARENA-010`
- `TEST-015`

Reason:
- After Stable promotion review, the biggest remaining gap is bounded closure around the right structural core, especially pair-anchor and fourth-variable situations that keep appearing in examples and competitions.

### Priority 6 — Cross-tool arena scaffolding

- `TRACK-003`
- `TRACK-004`
- `TRACK-009`
- `TRACK-010`
- `TRACK-011`
- `TRACK-012`
- `TRACK-013`
- `TRACK-014`
- `ARENA-003`
- `ARENA-004`
- `ARENA-005`
- `ARENA-007`
- `ARENA-008`
- `ARENA-009`
- `ARENA-010`
- `POLICY-006`
- `POLICY-007`
- `POLICY-008`
- `POLICY-009`
- `POLICY-010`
- `POLICY-011`
- `POLICY-012`
- `POLICY-013`
- `POLICY-014`
- `TEST-004`
- `TEST-006`
- `TEST-007`
- `TEST-008`
- `TEST-009`
- `TEST-010`
- `TEST-013`
- `TEST-014`
- `TEST-015`

Reason:
- Once Stable’s next evidence upgrades land, the next highest-value move is preparing the arena schema for multi-tool convergence and environment scoring.

---

## Implemented Foundation

| ID | Type | Status | Source | Description | Validation |
|---|---|---|---|---|---|
| `FOUND-001` | `arena` | `implemented` | Stable integration phase | Stable Arena v1 preserves row evidence, pattern ledgers, family rollups, and survivor frontiers. | Unit tests + smoke run on `2026-01-06 NewYork4` |
| `FOUND-002` | `tool` | `implemented` | Stable integration phase | Stable projection operators v1: `stable_compound_top`, `stable_family_vote`, `stable_last_remaining`. | Unit tests + smoke CU/play-card run |
| `FOUND-003` | `rule` | `implemented` | Example review setup | Deep example review notebook created and populated with macro mission + universal analytical notes. | Active notebook in RUNS |
| `FOUND-004` | `arena` | `implemented` | Stable compounding observability slice | Stable Arena compounding ledger v2 now preserves box-level contributors, frontier counts, peak-part provenance, top modal orders, and linked compound context in the section-level pattern ledgers. | Unit tests + smoke reruns on `C035 NewYork4` and `C036 Delaware4` |
| `FOUND-005` | `arena` | `implemented` | Stable hidden-family slice | Stable Arena hidden-family / clutter-reveal v1 now preserves source literals, source locators, row-level reveal objects, and family/pattern reveal summaries. | Unit tests + 4-case smoke set on `C035 NewYork4`, `C036 Delaware4`, `2026-01-09 Pennsylvania4`, `2026-01-08 NorthCarolina4` |
| `FOUND-006` | `arena` | `implemented` | Stable order-transform slice | Stable Arena order / VT-straight v1 now preserves row-level transform hints plus canonical/family rollup summaries for modal-order and hidden-fragment seeds. | Unit tests + 4-case smoke set on `C035 NewYork4`, `C036 Delaware4`, `2026-01-09 Pennsylvania4`, `2026-01-08 NorthCarolina4` |
| `FOUND-007` | `tool` | `validated` | Stable family-lane promotion slice | `stable_family_vote_v2` adds one extra bounded family-lane pack per variant/section using richer Stable Arena evidence and arena-vs-legacy rank lift. | Unit tests + 4-case gate + `2026-01-01..2026-01-09` harness in `2026-03-11__STABLE_FAMILY_VOTE_V2__VALIDATION.md` |

---

## Rules Snapshot

Full running rule language lives in the example-review notebook. This section keeps the current highest-priority rules visible for implementation decisions.

| ID | Status | Source | Rule |
|---|---|---|---|
| `RULE-001` | `approved` | Macro discussion | Optimize extraction quality and interpretation; do not demand a winner every draw. |
| `RULE-002` | `approved` | Macro discussion | Rank states by predictive quality and cost-adjusted value, not raw signal volume. |
| `RULE-003` | `approved` | Macro discussion | Long-term profitability comes from selective play and expense control. |
| `RULE-004` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | Convergence beats any single signal. |
| `RULE-005` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | Strings lead; Aux compounds. |
| `RULE-006` | `approved` | Training + macro discussion | Evaluate per variant first; add cross-variant convergence second. |
| `RULE-007` | `approved` | RUNS evidence ledger | Separate evidence recall from budget conversion. |
| `RULE-008` | `approved` | Training + Example 1 | Pattern order / permutation clues are real evidence, especially for VT-straight conversion. |
| `RULE-009` | `approved` | validation templates | Grade and reason in multiple match modes: exact straight, exact box, VT-box, VT-straight. |
| `RULE-010` | `approved` | FEEDBACKEX1_1 + FEEDBACKEX1_2 + MESSAGE2 | Lingering / surviving patterns are a primary predictive evidence class and must be preserved before downstream projection or budgeting. |
| `RULE-011` | `approved` | FEEDBACKEX1_1 + MESSAGE2 | The system should think in winner family / transformation corridor terms, not only literal winner presence. |
| `RULE-012` | `approved` | FEEDBACKEX1_2 + MESSAGE2 | Arena learning comes before serious combination-forming redesign. |
| `RULE-013` | `approved` | FEEDBACKEX1_2 + MESSAGE2 | Final state ranking should eventually correlate positively with predictive value over time. |
| `RULE-014` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | The analysis arena is an evidence-preservation and inspection stage, not a hidden play-card prefilter. |
| `RULE-015` | `approved` | NUMBER_5 + MESSAGE_8 | Top-N is a summary surface, not the truth model of what the extractor or arena preserved. |
| `RULE-016` | `approved` | current discussion | Do not force every new phenomenon into the legacy tool boundaries; create a new focused tool when that produces clearer extraction semantics and cleaner arena evidence. |
| `RULE-017` | `approved` | current discussion | Keep `Brain 1` (per-state arena analysis) distinct from `Brain 2` (cross-state ranking / profitability triage). |
| `RULE-018` | `approved` | 2026-03-09 competition postmortem | Grade ticket performance separately from arena / candidate-universe preservation so we do not hide real progress inside a missed final ticket. |
| `RULE-019` | `approved` | 2026-03-09 competition postmortem | Treat doubles / mirror-doubles as a distinct predictive regime rather than mixing them blindly with 6-way single states. |
| `RULE-020` | `approved` | 2026-03-09 competition postmortem + current discussion | A strong pair-anchor plus one lingering fourth variable is a real closure principle and should be modeled explicitly. |
| `RULE-021` | `approved` | 2026-03-09 competition postmortem | Same-day midday-to-evening transition is first-class evidence and should be scored explicitly rather than handled ad hoc. |

---

## Active Trackers

| ID | Status | Source | Target Layer | Tracker |
|---|---|---|---|---|
| `TRACK-001` | `approved` | Macro discussion + Example 1 | ranking / arena | `perm_lane_tightness` and `environment_cleanliness` so cheap perm-only environments can be recognized. |
| `TRACK-002` | `implemented` | Example 1 | arena / conversion | Candidate-level permutation clue strength: modal orders, repeated order fragments, pair anchors, and order persistence. |
| `TRACK-003` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | arena / aux | Aux convergence as first-class fields: support total, support breadth, support by variant, legend. |
| `TRACK-004` | `approved` | macro discussion | environment / policy | State-day environment metrics: dominance vs dilution, noise check, cheapest reasonable play mode, cost geometry. |
| `TRACK-005` | `approved` | Example 1 | harness / truth-layer | Arena recall scoreboard: lane present, canonical present, long-family present, survivor present, projected pack hit. |
| `TRACK-006` | `implemented` | Example 1 + training | stable / arena | Hidden-family / clutter-reveal metrics for long strings. |
| `TRACK-007` | `approved` | Example 1 | stable / arena | Current-frontier transition metrics: `frontier_arrival`, `Col2 -> Col1` funnel behavior, and `current_frontier_alignment`. |
| `TRACK-008` | `implemented` | macro discussion | conversion | VT-straight transform recipe inventory and count of cheap transform candidates per lane. |
| `TRACK-009` | `approved` | FEEDBACKEX1_2 + MESSAGE2 | ranking / validation | Rank-vs-predictive-value measurement so ranking can later be checked against actual predictive lift over time. |
| `TRACK-010` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | tool-by-tool review | Per-tool arena contribution summary: what exact evidence this tool now adds to the arena that was previously missing. |
| `TRACK-011` | `implemented` | NUMBER_5 + MESSAGE_8 | compounding / observability | Variant-level compounding ledger: rows, boxes, spans, feature-part totals, peaks, provenance, and what compounding added beyond row-level scores. |
| `TRACK-012` | `approved` | 2026-03-09 competition postmortem | competition harness / grading | Competition scoreboard with `TicketBoxHit`, `TicketVTRACHit`, `ArenaCanonicalPresent`, `ArenaFamilyPresent`, `CUPresent`, and `MiddayCarryPresent`. |
| `TRACK-013` | `approved` | 2026-03-09 competition postmortem | ranking / state triage | State-mode / regime classification: doubles regime, single-progression regime, mixed regime, split-rail regime, and transition-sensitive regime. |
| `TRACK-014` | `approved` | current discussion + 2026-03-09 competition postmortem | closure / conversion | Pair-anchor and lingering-fourth-variable metrics: anchor strength, extra-variable persistence, mirror-pair coverage, and cost-efficient closure size. |

---

## Active Tool Changes

| ID | Status | Source | Target Tool | Change |
|---|---|---|---|---|
| `TOOL-001` | `implemented` | Example 1 / C035 | Stable | Preserve source cell locator and original source literal for high-value long-cluster / family evidence. |
| `TOOL-002` | `implemented` | Example 1 / winners HTML | Stable | Detect and surface family fragments inside clutter digits, not just final canonical/family rollups. |
| `TOOL-003` | `implemented` | Example 1 | Stable | Promote modal order evidence more explicitly so clues like `847 -> 342` can be used predictively. |
| `TOOL-004` | `implemented` | Example 1 | Stable | Add bounded VT-straight transform candidate generation from modal orders / family fragments / repeated pairs. |
| `TOOL-005` | `validated` | Example 1 | Stable projections | Revisit family-lane promotion logic so strong family evidence is not lost just because the lane ranks outside the current top family cut. Implemented as `stable_family_vote_v2`, using richer arena evidence, current/frontier signals, and arena-vs-legacy rank lift. |
| `TOOL-006` | `noted` | training + macro discussion | Stable / DR | Quantify long-cluster strength by how much digit structure is still holding inside the cluster. |
| `TOOL-007` | `implemented` | NUMBER_5 | Stable | Expose how R2/R4/R6/R8 mini-progressions are compounded into total pattern scoring, including totals, peaks, contributing boxes, frontier hits, and compound-row context. |
| `TOOL-008` | `approved` | current discussion + 2026-03-09 competition postmortem | DR / closure helpers | Detect and preserve the lingering fourth variable around a strong 3-value or pair-anchor core, including digit and mirror-pair variants that yield cheap bounded closure sets. |

---

## Active Arena Changes

| ID | Status | Source | Target Layer | Change |
|---|---|---|---|---|
| `ARENA-001` | `implemented` | Example 1 | Stable Arena | Preserve source literals / source fragments when a family is being inferred from a long string. |
| `ARENA-002` | `implemented` | Example 1 | Stable Arena | Add explicit order / transform surfaces to family and canonical rollups, not only buried `top_modal_orders`. |
| `ARENA-003` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | Arena / future CEG | Add explicit convergence breakdown objects: tools found, variants found, sections found, tags, overlap counts. |
| `ARENA-004` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | Arena schema | Keep `consensus_r_table` separate from `consensus_xvar_positional`. |
| `ARENA-005` | `approved` | Stable-first architecture | Arena / future EDO | Build toward `EDO -> CEG -> DPL` rather than collapsing evidence directly into picks. |
| `ARENA-006` | `implemented` | Stable integration phase | Stable Arena | Survivor frontiers are preserved as a distinct evidence class, not only top compounds. |
| `ARENA-007` | `approved` | FEEDBACKEX1_1 + MESSAGE2 | Arena schema | Preserve raw literal, canonical, family, and VTRAC-linked views together for important evidence objects. |
| `ARENA-008` | `approved` | NUMBER_5 + MESSAGE_8 | Arena schema | Use shared semantic fields across tools for comparison: horizontal persistence, vertical box/straight support, family alignment, survivor status, frontier arrival, VT-straight hint, cluster-size strength. |
| `ARENA-009` | `approved` | current discussion | Arena architecture | Arena inputs are not limited to the original core analyzers; new focused tools may feed the arena as first-class evidence producers if they follow the shared evidence contract. |
| `ARENA-010` | `approved` | current discussion + 2026-03-09 competition postmortem | Arena schema | Add `pair_anchor_closure` evidence objects carrying core anchor, mirror-pair space, lingering fourth-variable candidates, bounded closure sets, and cost-to-cover. |

---

## Active Policy Changes

| ID | Status | Source | Target Layer | Policy |
|---|---|---|---|---|
| `POLICY-001` | `approved` | current workflow agreement | Example review process | Implement clear fixes during or at the end of each example; do not leave them as vague future notes. |
| `POLICY-002` | `approved` | macro discussion | ranking / state triage | Compare `arena branch vs baseline` on every major teaching case. |
| `POLICY-003` | `approved` | macro discussion + templates | play mode selection | Prefer the cheapest rational mode: perm-only, VT-box, VT-straight, hedge, or skip depending on environment quality. |
| `POLICY-004` | `approved` | Example 1 + training | conversion | Treat VT-straight trapping as a separate conversion mode, not just a boxed-lane afterthought. |
| `POLICY-005` | `approved` | profitability vision | state selection | Focus spend on states with stronger evidence quality and cleaner conversion paths, not just more activity. |
| `POLICY-006` | `approved` | MESSAGE2 | ranking / validation | Treat ranking correlation as a hard design goal now, but only as a hard validation gate later after more arena fields / tool feeds are in place. |
| `POLICY-007` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | build order | Use tool-by-tool arena feeding as the active development cadence: Stable, DR, Hot Zones, VTRAC analyzer, then Aux / Control Center context. |
| `POLICY-008` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | evaluation discipline | Do not let profitability or final combination-forming questions act as the immediate pass/fail test for a tool slice before arena fidelity is explicit. |
| `POLICY-009` | `approved` | NUMBER_5 + MESSAGE_8 | scoring discipline | Retune feature weights only after compounding observability is explicit; instrument first, retune second. |
| `POLICY-010` | `approved` | current discussion | tool design discipline | If a phenomenon has distinct extraction logic, scoring, or provenance needs, prefer a new focused tool over forcing the logic into an unrelated legacy tool. |
| `POLICY-011` | `approved` | current discussion | architecture / evaluation | Keep `Brain 1` and `Brain 2` separate in design and testing: validate per-state arena fidelity before leaning on macro ranking or profitability conclusions. |
| `POLICY-012` | `approved` | 2026-03-09 competition postmortem | grading / development | In competitions and live reviews, always log `ticket result` and `arena result` separately so postmortems preserve development value. |
| `POLICY-013` | `approved` | current discussion | ranking / conversion | Give doubles / mirror-doubles their own promotion lane and budget logic instead of forcing them through the same thresholds as 6-way singles. |
| `POLICY-014` | `approved` | 2026-03-09 competition postmortem | live competition workflow | Before evening predictions, score midday results as both carry-forward pressure and reduction pressure. |

---

## Active Tests

| ID | Status | Source | Target Layer | Test |
|---|---|---|---|---|
| `TEST-001` | `approved` | current workflow agreement | example harness | Every deep-dive case should compare `truth vs baseline vs arena branch`. |
| `TEST-002` | `validated` | Example 1 / C035 | Stable Arena | Example 1 should continue to verify that family 30 is preserved in the arena even when baseline CU misses it. |
| `TEST-003` | `validated` | Example 1 | Stable projections | After projection improvements, Example 1 should show stronger family-30 promotion without destructive pack explosion. |
| `TEST-004` | `approved` | macro discussion | harness / windows | Add window-level arena recall metrics once 2-3 tools have been fed into the arena. |
| `TEST-005` | `validated` | Example 1 | Stable hidden-family work | Add regression coverage for source literal + clutter-reveal + transform candidate fields once implemented. |
| `TEST-011` | `approved` | hidden reveal live validation | Stable hidden-family work | Keep hidden-family / clutter-reveal observability-only until positive/noisy controls show a reliable calibration threshold for ranking or promotion. |
| `TEST-012` | `validated` | order-transform live validation | Stable order-transform work | Keep order / VT-straight transform evidence observability-only until positive/noisy controls show what transform thresholds are predictive rather than merely descriptive. |
| `TEST-006` | `approved` | FEEDBACKEX1_2 + MESSAGE2 | ranking / windows | After more arena fields / tool feeds exist, validate that higher-ranked states trend toward stronger predictive value over time. |
| `TEST-007` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | tool-by-tool review | For each tool pass, explicitly answer: what did this tool add to the arena that was previously missing? |
| `TEST-008` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | case sequence | Keep example coverage across casebook buckets: preservation/lane-drop, within-lane miss, conversion recovery, positive control, and noisy control. |
| `TEST-009` | `validated` | NUMBER_5 + MESSAGE_8 | compounding / observability | For one example, answer what compounding added beyond row-level scores, what survivor/frontier inventory added, and what remained absent from old CU despite now being visible in the arena. |
| `TEST-010` | `approved` | current discussion | architecture / tool design | When a new phenomenon is introduced, explicitly decide whether it belongs in an existing tool or a new focused tool, and record why that choice yields the cleaner arena input. |
| `TEST-013` | `approved` | 2026-03-09 competition postmortem | competition harness | For each live competition, write a postmortem that grades `ticket vs arena vs CU vs midday-transition` rather than ticket-only. |
| `TEST-014` | `approved` | 2026-03-09 competition postmortem | teaching cases | Keep `Ontario 559` and `Connecticut 019/091` as conversion teaching cases where the arena preserved the winner before the final ticket missed. |
| `TEST-015` | `approved` | current discussion | closure logic | Before promoting pair-anchor plus fourth-variable closure into production ranking, validate it on multiple examples as a bounded-cost conversion rule rather than a combinatoric expansion. |
| `TEST-016` | `validated` | Stable family-lane promotion slice | Stable projections | Run a January-window harness comparing `stable10` baseline vs `stable_family_vote_v2` for exact-box-lane rescue without pack explosion. |

---

## Example 1 Current Readout

Example anchor:
- `C035` / `2026-01-06` / `NewYork4` / winner `342` / canonical `234` / VTRAC `30`

What the queue should remember from Example 1 right now:
- the winner artifact is crediting family-30 structure through fragments like `243`, `324`, `347` and long clusters like `29688447`
- Stable predictive evidence already preserves a meaningful family-30 story
- the new Stable Arena preserves that story better than baseline CU
- hidden-reveal v1 now makes that family story explicit with source literals, fragments, and rollup summaries instead of leaving it implicit inside raw long canonicals
- current projection logic still does not carry family 30 far enough into candidate packs
- `stable_family_vote_v2` now promotes family 30 into candidate packs and rescues the evening winner canonical `234` on Example 1
- order-transform v1 now makes the straight-conversion story explicit too: family 30 in Evening now shows seeds like `847` with bounded recipes `direct_perms`, `vt8_expand_ordered`, and `pair_mirror_third_12`
- order-fragment evidence like `847` suggests a strong VT-straight conversion opportunity that the current predictive path does not yet exploit
- the compounding-ledger rerun now makes box-level contributors, frontier counts, and compound-context totals visible without needing to hand-merge `scores.csv` and `compound.csv`
- hidden-reveal is broad enough across positive and noisy controls that it should remain an inspection/evidence surface until later calibration, not a direct promotion signal
- order-transform evidence is also broad across the case set, so it should remain an inspection/evidence surface until later calibration, not a direct promotion signal
- C035 is mainly a preservation / projection / lane-drop case, not the final answer on within-lane conversion policy

Primary active items linked to Example 1:
- `TRACK-002`
- `TRACK-006`
- `TRACK-008`
- `TRACK-010`
- `TOOL-001`
- `TOOL-002`
- `TOOL-003`
- `TOOL-004`
- `TOOL-005`
- `ARENA-001`
- `ARENA-002`
- `TEST-002`
- `TEST-003`
- `TEST-016`
- `TEST-007`
- `TEST-011`
- `TEST-012`

---

## Open Questions

- Should long-cluster reveal logic live first in Stable extraction, in arena post-processing, or in a cross-tool CEG layer?
- What calibration threshold makes hidden-family / clutter-reveal strong enough to influence ranking or promotion without flooding noisy states?
- What calibration threshold makes order / VT-straight transform evidence strong enough to influence ranking or promotion without flooding noisy states?
- Which VT-straight transform recipes deserve first-class support first: pair-anchored, mirror-anchored, full 8-combo index straight, or a bounded hybrid?
