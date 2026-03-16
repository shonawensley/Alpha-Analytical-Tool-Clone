# DR Gold-Day Audit Synthesis

Date: `2026-03-15`

Inputs:
- [DEV audit markdown](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__DEV__V1_1.md)
- [HOLDOUT audit markdown](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__HOLDOUT__V1_1.md)
- [audit_dr_gold_day.py](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/audit_dr_gold_day.py)

## Purpose

This audit was the first winner-aware pass after `DR Arena v1.1`, and it now includes two bounded promotion follow-ups:

- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`
- `dr_vtrac_fusion_strength`

It was designed to answer:

1. Does DR already see the eventual winner VTRAC lane often enough to justify promotion-style tuning instead of another extraction rewrite?
2. Are false-empty cases still recurring after `v1.1`, and if so which cases should anchor the next calibration pass?
3. Do the winners JSON tables support the thesis that winner / VTRAC winner corridors are usually living inside the assigned long-string boxes?

## Windows

Development windows:
- `2025-06-21 -> 2025-06-23`
- `2025-12-30 -> 2026-01-04`

Holdout window:
- `2026-01-05 -> 2026-01-09`

## Core Findings

### 1. DR is already catching the eventual VTRAC lane far more often than it is surfacing that lane near the top

Development rows: `245`
- matched winner-JSON rows: `244`
- `exact_any > 0`: `92` (`37.6%`)
- `vtrac_any > 0`: `218` (`89.0%`)
- `family_vtrac_any > 0`: `159` (`64.9%`)
- `trace winner VTRAC rank <= 3`: `20 / 244` (`8.2%`)
- `corridor winner VTRAC rank <= 3`: `19 / 244` (`7.8%`)
- `gateway winner VTRAC rank <= 3`: `19 / 244` (`7.8%`)
- `cluster winner VTRAC rank <= 3`: `23 / 244` (`9.4%`)
- `cluster winner VTRAC rank <= 5`: `34 / 244` (`13.9%`)
- `assigned-box winner VTRAC rank <= 3`: `24 / 244` (`9.8%`)
- `assigned-box winner VTRAC rank <= 10`: `84 / 244` (`34.4%`)
- `fusion winner VTRAC rank <= 3`: `25 / 244` (`10.2%`)
- `fusion winner VTRAC rank <= 5`: `39 / 244` (`16.0%`)

Holdout rows: `138`
- matched winner-JSON rows: `110`
- `exact_any > 0`: `48` (`34.8%`)
- `vtrac_any > 0`: `119` (`86.2%`)
- `family_vtrac_any > 0`: `76` (`55.1%`)
- `trace winner VTRAC rank <= 3`: `9 / 110` (`8.2%`)
- `corridor winner VTRAC rank <= 3`: `9 / 110` (`8.2%`)
- `gateway winner VTRAC rank <= 3`: `9 / 110` (`8.2%`)
- `cluster winner VTRAC rank <= 3`: `9 / 110` (`8.2%`)
- `cluster winner VTRAC rank <= 5`: `14 / 110` (`12.7%`)
- `assigned-box winner VTRAC rank <= 3`: `11 / 110` (`10.0%`)
- `assigned-box winner VTRAC rank <= 10`: `34 / 110` (`30.9%`)
- `fusion winner VTRAC rank <= 3`: `8 / 110` (`7.3%`)
- `fusion winner VTRAC rank <= 8`: `28 / 110` (`25.5%`)

The important gap is:

- DEV matched rows with `vtrac_any > 0` but **not** top-3 trace/corridor/gateway/cluster: `193 / 217` (`88.9%`)
- HOLDOUT matched rows with `vtrac_any > 0` but **not** top-3 trace/corridor/gateway/cluster: `87 / 96` (`90.6%`)

Interpretation:

- DR is already seeing the right eventual VTRAC lane in its receipts.
- `dr_vtrac_lane_gateway` helped modestly.
- `dr_vtrac_cluster_strength` helped a bit more for the visible-under-promoted regime.
- `dr_assigned_box_vtrac_strength` is the first strong buried-regime keeper: it recovers winner lanes directly from raw assigned-box windows even when the family-led surfaces stay dead.
- `dr_vtrac_fusion_strength` is a bounded agreement/rescue layer, not a replacement surface. It modestly improves the visible band when assigned-box and cluster/gateway agree, and it nudges best-surface top-3/top-5 up on the frozen reruns without needing a broad retune.
- The bottleneck is no longer just generic promotion / packaging. It splits into:
  - `visible-under-promoted` rows where cluster/gateway need bounded help
  - `buried` rows where assigned-box lane isolation is the missing predictive surface
- This still argues against a full extractor rewrite as the next move.

### 2. `v1.1` is now conservative on empty classification; the remaining problem is promotion inside active-low-trust states

Development:
- `positive_trace`: `207 / 245` (`84.5%`)
- `active_low_trust`: `38 / 245` (`15.5%`)
- `true_empty`: `0 / 245`

Holdout:
- `positive_trace`: `112 / 138` (`81.2%`)
- `active_low_trust`: `26 / 138` (`18.8%`)
- `true_empty`: `0 / 138`

That matters because it changes the meaning of the next calibration pass.

The current audit is no longer dominated by rows being flattened into `true_empty`.
The remaining problem is that many structurally live rows are still only being preserved as `active_low_trust`, while the strongest winner lane remains under-promoted.

Recurring or high-value false-empty / mismatch anchors from the broader DR work are still the right calibration set:
- `Virginia4 Midday 473`
- `NewYork4 Evening 116`
- `NewYork4 Midday 243`
- `NewYork4 Midday 793`
- `NewYork4 Evening 256`
- `OntarioCanada4 Evening 498`
- `Indiana4 Midday 325`
- `Indiana4 Midday 219`
- `NorthCarolina4 Evening 571`
- `Connecticut4 Midday 576`
- `Ohio4 Evening 064`

State concentration:
- DEV false-empty leaders: `NewYork4`, `OntarioCanada4`, `Michigan4`, `Delaware4`
- HOLDOUT false-empty leaders: `Michigan4`, `OntarioCanada4`, then `Connecticut4` / `Ohio4` / `NewYork4`

Interpretation:

- `dr_empty_lens` is better than it was.
- The next tuning batch should target **winner-lane promotion in active-low-trust conditions**, not another broad empty-vs-nonempty rewrite.

### 3. The assigned-box / winners-HTML thesis is strongly supported

Matched winners JSON rows with `ls_signal_cells > 0`:
- DEV: `242 / 244` (`99.2%`)
- HOLDOUT: `105 / 110` (`95.5%`)

Interpretation:

- Across the rows where structured winners JSON was available and matched to the stamped winner, the winner-family / VT corridor is almost always visibly present inside the long-string boxes.
- The main question is **not** whether those corridors exist.
- The main question is how to score and promote the right corridor instead of allowing competing literal worlds (`559`, `229`, `259`, `299`, `499`, etc.) to dominate the caller-facing surfaces.

### 4. `2026-01-05` exposed an artifact-coverage issue, not a DR truth failure

Holdout rows for `2026-01-05`:
- `winner_json_matched = 0 / 28`
- `winner_json_status = unmatched_literal` on all rows

Interpretation:

- The DR winner stamps existed and were usable.
- The sharepack `winners/<STATE>/*.json` files did not correspond to the actual stamped winners for that date.
- Those rows should be treated as an artifact gap, not as evidence that the winners tables were dead that day.

This is now surfaced explicitly by the audit instead of being silently flattened into “no signal”.

## Best Validated DR Strengths After `v1.1`

1. **Winner-lane visibility**
   - DR receipts keep catching the eventual VTRAC lane at very high rates.

2. **Stable false-empty identification**
   - The audit can now isolate structurally active false-empty cases instead of treating them like generic controls.

3. **Assigned-box truth layer**
   - The winners JSON tables confirm that winner-family / VTRAC corridors are usually living in the mapped long-string environments.

4. **Cross-window stability**
   - `literal_capture`, `vtrac_capture`, and false-empty rates stayed remarkably close between dev and holdout windows.

## What The Next Optimization Batch Should Target

### Priority 1: keep the bounded fusion keeper, do not broaden it yet

The bounded fusion pass has now been tested. The correct next move is to keep it as a modest promotion aid, not to keep stretching it into a hard replacement for assigned-box or cluster.

In practical terms:

- keep `dr_assigned_box_vtrac_strength` as its own arena object
- keep `dr_vtrac_fusion_strength` as a separate arena object
- use it mainly for:
  - assigned-box + cluster/gateway agreement
  - guarded assigned-box rescue
- do **not** force it to replace the raw assigned-box buried-lane view

### Priority 2: artifact-first review of rescued vs still-buried anchors

The next useful DR work is no longer another score invention pass.
It is direct winner-artifact review of:
- fusion-helped visible rows
- fusion-failed buried rows
- controls / low-trust rows

In practical terms, this means:
- review those groups directly against winners HTML / overlays
- verify whether the remaining misses are truly DR-local
- only code more DR if the artifact review yields one narrow, reusable rule

### Priority 3: winner-aware mismatch / false-empty refinement

Use the recurring anchors above to refine:
- `overlay_summary_mismatch`
- false-empty detection
- active-low-trust vs positive-trace discrimination

This should remain a bounded, winner-aware audit-side loop first.

### Priority 4: prepare DR for arena handoff

The predictive writer now has a credible keeper set:
- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`
- `dr_vtrac_fusion_strength`

That is likely enough to feed the aggregated analysis arena unless one more artifact-first rule proves clearly reusable.

## What Should *Not* Happen Next

- Do **not** jump to `Analyzer V3` yet.
- Do **not** retune everything at once.
- Do **not** delete mapped boxes from these results alone.
- Do **not** treat the raw existence of winner-family signal in the tables as the main problem; that part is already strongly supported.

## Recommended Next Step

Proceed with a bounded `DR Gold-Day Winner Audit` tuning loop:

1. Keep the current frozen windows.
2. Treat the current 4-surface keeper set as the DR baseline.
3. Do artifact-first review before any more DR coding.
4. Only add another DR rule if it clearly improves the same dev + holdout gates.

The evidence now says the highest-leverage work is:

**keep the assigned-box + cluster/gateway + bounded-fusion DR package intact, then decide whether the next lift belongs inside DR or in the aggregated analysis arena.**
