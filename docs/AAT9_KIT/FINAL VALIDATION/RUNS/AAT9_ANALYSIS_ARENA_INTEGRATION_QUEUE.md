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
- `RULE-022`
- `TRACK-015`
- `TOOL-009`
- `ARENA-011`
- `POLICY-015`
- `TEST-017`

Reason:
- After Stable promotion review, the biggest remaining gap is bounded closure around the right structural core, especially pair-anchor and fourth-variable situations that keep appearing in examples and competitions.
- The immediate next design vehicle for this is the DR super-harness: truth lens + DR canvas + action ledger, before any broad DR rewrites.

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

### Priority 7 — Aux / Control Center context broadening

- `TRACK-021`
- `ARENA-015`
- `TOOL-023`
- `POLICY-017`
- `TEST-022`

Reason:
- The current predictive Aux / Control Center usage is now explicitly understood as a bounded conversion subset, not the final arena contract. The next high-value move is to preserve broader structured context from existing Aux summaries and Control Center trackers before the aggregated arena phase.

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
| `FOUND-008` | `arena` | `implemented` | Aggregated arena pilot | `scripts/tools/build_aggregated_analysis_arena.py` now builds the first real per-state aggregated arena runtime artifact from Stable, DR, VTRAC, Hot Zones, and Aux / Control Center evidence, with cross-tool relations, synthesis surfaces, downstream handoff links, and review links. | `tests/test_aggregated_analysis_arena.py` + predictive smoke on `2026-03-15` + frozen pilot review on `2025-12-31` |
| `FOUND-009` | `test` | `validated` | Aggregated arena review harness | `scripts/tools/review_aggregated_analysis_arena.py` now grades the arena itself against frozen winners and compares that with Candidate Universe / Play Card behavior, writing a scoreboard plus memo with `gap_class`, winner-lane/family presence, context reinforcement, and downstream presence fields. | `tests/test_review_aggregated_analysis_arena.py` + frozen window review on `2025-12-30..2025-12-31` |
| `FOUND-010` | `test` | `validated` | Aggregated arena window review refinement | The arena review harness now emits `gap_detail` so broad review rows are split into meaningful subtypes like `lane_alive_literal_missing_front3`, `lane_alive_literal_missing_front5`, `family_alive_literal_missing_front5`, `context_reinforced_underweighted`, and `thin_conversion_gap` instead of flattening every non-ticket row into one miss bucket. | `tests/test_review_aggregated_analysis_arena.py` + frozen window review on `2025-12-30..2026-01-04` |
| `FOUND-011` | `test` | `implemented` | Aggregated arena anchor review support | `scripts/tools/export_aggregated_arena_anchor_casepack.py` now turns the six-day arena review scoreboard into a reusable anchor pack with direct arena / winner / CU / play-card artifact paths for the strongest `lane_alive`, `family_alive`, `context_reinforced_underweighted`, and `thin_conversion_gap` rows. | Smoke export to `2026-03-18__AGGREGATED_ANALYSIS_ARENA__ANCHOR_CASEPACK.md` |
| `FOUND-012` | `arena` | `implemented` | Aggregated arena synthesis refinement | `scripts/tools/build_aggregated_analysis_arena.py` now emits `arena_synthesis.vtrac_literal_watchlist`, a bounded lane-to-literal bridge built from dominant VTRAC indices, example literals, and canonicalized neighbors so `lane_alive_literal_missing_*` rows can be reviewed as live lane neighborhoods instead of generic literal misses. The arena markdown now surfaces this explicitly under `VTRAC Literal Watchlist` and adds a matching review prompt. | `tests/test_aggregated_analysis_arena.py` + rebuilt arena artifacts for `2025-12-30..2026-01-04` |
| `FOUND-013` | `test` | `implemented` | Aggregated arena source-attributed context review | `scripts/tools/review_aggregated_analysis_arena.py` now breaks context presence into concrete source families instead of one generic reinforcement blob. Per reviewed winner row it records whether Profit Alerts, Blackapple, due doubles, repeat watch, Aux overdue-index pressure, or Aux badge pressure touched the winner canonical or winner VTRAC lane, and the anchor casepack now surfaces those source labels directly. | `tests/test_review_aggregated_analysis_arena.py` + refreshed anchor casepack export |
| `FOUND-014` | `test` | `implemented` | Aggregated arena frozen-snapshot decay review | `scripts/tools/review_aggregated_analysis_arena_decay.py` now freezes each arena snapshot and measures whether its dominant canonicals, dominant VTRAC indices, dominant families, VTRAC watchlist neighborhoods, and key context episodes resolve across future draws instead of only grading the same-day results window. | `tests/test_review_aggregated_analysis_arena_decay.py` |
| `FOUND-015` | `analysis` | `validated` | Aggregated arena front-band anchor review | The first front-band anchor pass (`2026-03-19__AGGREGATED_ARENA__FRONT_BAND_ANCHOR_REVIEW.md`) confirms that the strongest `front3/front5` rows are usually not arena-missing states. They are lane-alive rows where literal closure lags. Across the current front-band set, the most common reinforcing context sources are `aux_badge`, `aux_overdue`, and `due_doubles`, and the new `D+3` decay review shows watchlist / VTRAC persistence materially outpacing same-day literal closure. | Front-band review memo + six-day review/casepack/decay outputs |
| `FOUND-016` | `analysis` | `validated` | Aggregated arena front-band source rollup | `scripts/tools/rollup_aggregated_arena_front_band.py` now joins the six-day front-band review rows to the frozen-snapshot decay review and summarizes repeated source families / source mixes instead of leaving bridge ideas as per-anchor impressions. On the current `18` front-band rows, the repeated source families are `aux_badge` (`10/18`), `aux_overdue` (`9/18`), and `due_doubles` (`7/18`). The first repeated bridge-ready source mixes are `aux_overdue+aux_badge` (`3` rows, watchlist `<=3d 2/3`), `due_doubles+aux_overdue+aux_badge` (`3` rows, watchlist `<=3d 2/3`), and `due_doubles` (`2` rows, watchlist `<=3d 2/2`). | `tests/test_rollup_aggregated_arena_front_band.py` + `2026-03-19__AGGREGATED_ARENA__FRONT_BAND_SOURCE_ROLLUP.md` |
| `FOUND-017` | `analysis` | `validated` | Aggregated arena bridge study v0 | `scripts/tools/study_aggregated_arena_bridge.py` now tests bounded watchlist-based bridge rules on measured bridge-ready cohorts without changing production conversion. On the first six-day window, `top3_perm` lifts same-day box/exact from baseline `0/8` to `2/8` and `D+3` box/exact to `3/8`; `top4_perm` lifts same-day box/exact to `3/8` and `D+3` box/exact to `4/8`. The lift is concentrated in `aux_overdue+aux_badge` (`same-day 2/6`, `D+3 4/6`) and `due_doubles` (`same-day 3/4`, `D+3 3/4`), while the heavier `due_doubles+aux_overdue+aux_badge` trio mix is `0/6`. The second January block (`2026-01-05..2026-01-09`) repeats `aux_overdue+aux_badge` as the clearest bridge cohort: baseline same-day literal `0/6`, bridge lift `3/6` same-day and `3/6` within `D+3`. The June block (`2025-06-21..2025-06-24`) keeps that same cohort alive but weakens its profile: baseline same-day literal `0/4`, bridge same-day `0/4`, bridge `D+3 2/4`; the trio mix remains `0/2`. Across all three measured windows, `aux_overdue+aux_badge` is now the first cohort with repeat support, but it still reads as a study-only bridge because its lift is stronger on some windows than others and is often decay-first rather than immediate. | `tests/test_study_aggregated_arena_bridge.py` + `2026-03-19__AGGREGATED_ARENA__BRIDGE_STUDY.md` + `2026-03-20__AGGREGATED_ARENA__BRIDGE_STUDY__2026-01-05_to_2026-01-09.md` + `2026-03-20__AGGREGATED_ARENA__BRIDGE_STUDY__2025-06-21_to_2025-06-24.md` |
| `FOUND-018` | `test` | `validated` | Aux / Control Center regeneration parity audit | `scripts/tools/audit_aux_control_center_parity.py` now runs a bounded raw-workbook parity audit against frozen sharepacks: it regenerates Aux draw snapshots and summary sections from each sample state-day’s recorded workbook cutoff, then rebuilds state-local Control Center rows and compares them with the frozen sharepack CSV outputs. The first audit sample set (`2025-12-30 NorthCarolina4`, `2025-12-31 NewJersey4`, `2026-01-09 Pennsylvania4`) passed cleanly across draw snapshots, Aux summary sections, and Control Center rows, and a follow-up bridge-cohort sample (`2025-12-30 Florida4`, `2025-12-31 Virginia4`, `2026-01-09 Delaware4`) also passed cleanly. That materially increases confidence that the Aux / CC evidence feeding the arena is being regenerated from the right historical cutoffs rather than drifting. | `tests/test_audit_aux_control_center_parity.py` + `2026-03-20__AUX_CONTROL_CENTER__PARITY_AUDIT.md` + `2026-03-20__AUX_CONTROL_CENTER__PARITY_AUDIT__BRIDGE_COHORTS.md` |
| `FOUND-019` | `analysis` | `validated` | Aggregated arena bridge corpus readback | `scripts/tools/analyze_aggregated_arena_bridge_corpus.py` now combines the measured bridge-study rows across December, January, and June and drills into the repeated `aux_overdue+aux_badge` cohort. The combined readback shows the better separator is structural frontness, not simple watchlist size: the focus cohort is `3/8` same-day, `2/8` decay-only, `3/8` miss overall, but the stronger cases cluster in `lane_alive_literal_missing_front3/front5` rows with `arena_vtrac_rank <= 5`, while the wider `family_alive_literal_missing_front5` rows skew decay-only or miss. The direct gated corpus read keeps only that narrower structural gate and lands at `3/6` same-day, `1/6` decay-only, `2/6` miss; June contributes no rows under the strict gate, which is exactly why the gate is cleaner but still not promotable. Watchlist-size bands still do not separate the cohort cleanly on their own. | `tests/test_analyze_aggregated_arena_bridge_corpus.py` + `2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_READBACK.md` + `2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_GATED_READBACK.md` |
| `FOUND-020` | `analysis` | `validated` | Aggregated arena bridge timing-profile split | The bridge-study rows now emit explicit resolution profiles (`direct_same_outcome`, `same_day_precursor_plus_same_day`, `same_day_carryforward`, `future_day_decay`, `miss`) so same-day carry-forward is not buried inside generic `decay_only` reporting. On the strict gated `aux_overdue+aux_badge` cohort (`6` rows), the current shape is `2` `direct_same_outcome`, `1` `same_day_precursor_plus_same_day`, `1` `same_day_carryforward`, and `2` `miss`. That means the only current non-same-day resolver inside the strict gate is actually same-day midday-to-evening carry-forward, not later-day decay. | `tests/test_study_aggregated_arena_bridge.py` + `tests/test_analyze_aggregated_arena_bridge_corpus.py` + `2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_GATED_READBACK.md` |

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
| `RULE-022` | `approved` | DR super-harness planning | Digit Reduction must be read through two evidence channels: pre-reduction cluster evidence and post-reduction reveal evidence. |

---

## Active Trackers

| ID | Status | Source | Target Layer | Tracker |
|---|---|---|---|---|
| `TRACK-001` | `approved` | Macro discussion + Example 1 | ranking / arena | `perm_lane_tightness` and `environment_cleanliness` so cheap perm-only environments can be recognized. |
| `TRACK-002` | `implemented` | Example 1 | arena / conversion | Candidate-level permutation clue strength: modal orders, repeated order fragments, pair anchors, and order persistence. |
| `TRACK-003` | `approved` | `IMPORTANT_SUPERBRAIN_GUIDE` | arena / aux | Aux convergence as first-class fields: support total, support breadth, support by variant, legend. |
| `TRACK-004` | `approved` | macro discussion | environment / policy | State-day environment metrics: dominance vs dilution, noise check, cheapest reasonable play mode, cost geometry. |
| `TRACK-005` | `validated` | Example 1 + aggregated arena phase | harness / truth-layer | Arena recall scoreboard is now live via `scripts/tools/review_aggregated_analysis_arena.py`: per outcome row it tracks winner canonical / VTRAC / family presence, context reinforcement, Candidate Universe presence, Play Card presence, `gap_class`, and `gap_detail`. The first full frozen window (`2025-12-30..2026-01-04`, `163` outcome rows) showed the current shape clearly: VTRAC present `156/163`, family present `144/163`, canonical present `125/163`, but only `39` literal downstream closures. The new `gap_detail` split isolates the strongest arena-local opportunity class as `lane_alive_literal_missing_front3` (`8` rows) plus `lane_alive_literal_missing_front5` (`5` rows), and the arena now exposes those rows with a `vtrac_literal_watchlist` so lane-linked literal neighborhoods can be reviewed before downstream conversion decisions. |
| `TRACK-019` | `implemented` | current arena-analysis phase | harness / decay | Frozen-snapshot decay review is now a first-class arena measurement: the system can keep same-day grading clean while separately checking whether dominant canonicals, dominant VTRAC lanes, watchlist neighborhoods, and major context episodes resolve within later draws. This is the correct measurement model for lingering/trapped pattern logic and should guide later conversion and packaging changes. |
| `TRACK-020` | `implemented` | current arena-analysis phase | front-band bridge cohorts | The front-band rollup is now useful mainly as a bridge-cohort discovery layer, not as the final decision layer. Early rollups surfaced `aux_badge`, `aux_overdue`, and `due_doubles` as the recurring front-band source families, but broader window work now says the only repeating bridge cohort worth active study is `aux_overdue+aux_badge`. `due_doubles` stays promising-but-unconfirmed and the heavier trio mix stays below the promotion line until it repeats cleanly across more windows. |
| `TRACK-021` | `implemented` | current arena-analysis phase | bridge-study discipline | The bounded bridge study remains measurement-only, not a production rule. Broader frozen-window confirmation now makes the hierarchy clearer: `aux_overdue+aux_badge` is the first cohort that repeats across multiple windows with real lift, but June shows that its resolution can be uneven; `due_doubles` remains promising but still only has one strong window; and the heavier trio mix still fails direct bridge scoring. The corpus readback now measures the first credible separator inside the repeated cohort: the better bridge cases cluster in `lane_alive_literal_missing_front3/front5` rows with `arena_vtrac_rank <= 5`, while watchlist-size alone is not a clean discriminator. The direct gated corpus read holds that narrower structural gate at `3/6` same-day, `1/6` decay-only, `2/6` miss, and the new timing-profile split shows that the lone non-same-day resolver is currently a same-day carry-forward case rather than a true future-day decay. That is useful enough to keep studying but still not strong enough to graduate beyond research mode. |
| `TRACK-006` | `implemented` | Example 1 + training | stable / arena | Hidden-family / clutter-reveal metrics for long strings. |
| `TRACK-007` | `approved` | Example 1 | stable / arena | Current-frontier transition metrics: `frontier_arrival`, `Col2 -> Col1` funnel behavior, and `current_frontier_alignment`. |
| `TRACK-008` | `implemented` | macro discussion | conversion | VT-straight transform recipe inventory and count of cheap transform candidates per lane. |
| `TRACK-009` | `approved` | FEEDBACKEX1_2 + MESSAGE2 | ranking / validation | Rank-vs-predictive-value measurement so ranking can later be checked against actual predictive lift over time. |
| `TRACK-010` | `approved` | FEEDBACKEX1_3 + FEEDBACKEX1_4 | tool-by-tool review | Per-tool arena contribution summary: what exact evidence this tool now adds to the arena that was previously missing. DR seed+batch2 now show the first stable contribution families clearly: `trace_strength`, `lane_only_confidence`, `competing_literal_pressure`, `double_pressure`, `row_repeat_and_final_survival`, and `empty_lens`. |
| `TRACK-011` | `implemented` | NUMBER_5 + MESSAGE_8 | compounding / observability | Variant-level compounding ledger: rows, boxes, spans, feature-part totals, peaks, provenance, and what compounding added beyond row-level scores. |
| `TRACK-012` | `approved` | 2026-03-09 competition postmortem | competition harness / grading | Competition scoreboard with `TicketBoxHit`, `TicketVTRACHit`, `ArenaCanonicalPresent`, `ArenaFamilyPresent`, `CUPresent`, and `MiddayCarryPresent`. |
| `TRACK-013` | `approved` | 2026-03-09 competition postmortem | ranking / state triage | State-mode / regime classification: doubles regime, single-progression regime, mixed regime, split-rail regime, and transition-sensitive regime. |
| `TRACK-014` | `approved` | current discussion + 2026-03-09 competition postmortem | closure / conversion | Pair-anchor and lingering-fourth-variable metrics: anchor strength, extra-variable persistence, mirror-pair coverage, and cost-efficient closure size. |
| `TRACK-015` | `in_progress` | DR super-harness planning | DR mapped-box validity ledger: classify mapped windows as core, supportive, experimental, disputed, or dead/N/A based on repeated harness evidence rather than ad hoc edits. After 11 reviewed cases, Group 1 remains strongly justified, `Set2 Draw1 Col3` remains disputed, and `Set1 Draw3 Col6` still stays only a likely dead/N/A candidate rather than a confirmed deletion. |
| `TRACK-016` | `implemented` | DR parity + broad screen + Virginia4 Midday 473 deep review | DR arena calibration | `dr_empty_lens` now classifies sections as `true_empty`, `active_low_trust`, or `positive_trace`, with confidence, cold-ratio, and positive-signal scoring so false-empty cases like Virginia4 Midday `473` are no longer flattened into the same bucket as true controls. |
| `TRACK-017` | `implemented` | Virginia4 Midday 473 deep review + 2026-03-15 DR gold-day audit | DR overlay audit | Winner-aware mismatch measurement now exists via `scripts/tools/audit_dr_gold_day.py`, which compares DR winner receipts against structured winners JSON table signals across frozen gold-day windows and surfaces `strong` / `moderate` summary mismatches instead of flattening them into generic misses. |
| `TRACK-018` | `implemented` | 2026-03-15 DR winner-promotion lab batch 6 | DR promotion gap anchors | The winner-promotion lab proved that many buried rows are not missing the winner lane entirely; they are missing a surface that reads assigned-box `box_id` / `final_value` windows directly. The new `dr_assigned_box_vtrac_strength` surface surfaced buried cases like `Indiana4 813`, `Virginia4 636`, `Michigan4 618`, `Ohio4 368`, and `Pennsylvania4 811` without any winner-aware inputs, which reframes the buried regime as an assigned-box lane-isolation problem rather than just another attractor-suppression problem. |
| `TRACK-019` | `implemented` | 2026-03-16 VTRAC + Hot Zones tool review kickoff | tool review method | The `winner-artifact-first` review method is now locked in via `2026-03-16__TOOL_REVIEW_METHOD__WINNER_ARTIFACT_FIRST.md`: inspect winners HTML / JSON / overlays first, classify gaps as tool-vs-arena-vs-conversion, and only keep bounded changes that survive the same frozen gold-day windows. |
| `TRACK-020` | `implemented` | 2026-03-16 VTRAC + Hot Zones joint assessment | cross-tool arena feed | The joint assessment and arena contract now explicitly treat VTRAC Analyzer and Hot Zones as complementary views of the same winner corridor: VTRAC contributes lane/family semantics, Hot Zones contributes pressure/location/survivorship semantics. |
| `TRACK-022` | `validated` | 2026-03-17 artifact-first confirmation on `Virginia4 2025-06-21`, `Florida4 2026-01-03`, and compact-report anchors | VTRAC / Hot Zones contract refinement | The first closeout was directionally right but too compressed. The winner-artifact confirmation showed that both tools already preserve more useful semantics than the earlier contract named: VTRAC should carry compact-report descriptors (`overlap`, `stable_cols`, `hot/superhot`, `mask_drop`, `mirror`, `double_hits`, `confidence_score`, `top_tokens`, `recommended_tokens`, `why`) plus enhanced JSON section summaries/ring votes/analyzer metrics, while Hot Zones should carry explicit count/span/tag families from `top_lanes.csv` and `per_lane.csv` (`support_count`, `hot_hits`, `superhot_hits`, `vertical_hits`, `set1_hits`, `precol1_hits`, `vt_straight_hits`, `vt_only_lane_hits`, spans, and raw `reasons`). This is an arena-contract broadening result, not a signal to reopen broad tool-local tuning. |
| `TRACK-023` | `implemented` | 2026-03-18 aggregated arena pilot | aggregated analysis arena runtime | The arena branch now has a real per-state SSOT object with stable namespaces (`metadata`, `provenance`, `string_tools`, `context_tools`, `cross_tool_relations`, `arena_synthesis`, `downstream_handoff`, `review_links`). The first frozen pilot on `2025-12-31` showed the expected current shape: winner-related VTRAC lanes are often preserved more clearly than literal winner canonicals, and downstream play-card divergence is now visible inside the same object rather than hidden across separate artifacts. |
| `TRACK-021` | `implemented` | 2026-03-16 Aux + Control Center review | Aux / Control Center arena feed | The Aux + Control Center review established that current predictive ingestion is intentionally narrow and should not be mistaken for the final arena contract. Existing predictive artifacts already carry much richer evidence: Aux `summary.json` contains positional, pairs, doubles, sums, repeat-watch, VTRAC, and Blackapple context; Control Center already emits due doubles, VTRAC repeat watch, Blackapple alerts, profit alerts, and compound events. The next move is broader structured arena preservation, not more narrow top-N trimming. |

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
| `TOOL-009` | `implemented` | DR super-harness planning | Build a DR-specific super-harness workflow and case template that compares truth receipts, DR evidence canvas, and Analyzer V2 salvage in one repeatable structure. Seed set and first case docs now live in the RUNS folder. |
| `TOOL-010` | `approved` | Virginia4 Midday 473 deep review | DR experimental reductions | Prototype one guarded `protected_core_reduction` pass that only runs after strong pre-reduction core support is detected, so likely clutter digits can be removed without destroying the live family/permutation neighborhood. |
| `TOOL-011` | `implemented` | DR gold-day winner-audit phase | DR audit workflow | `scripts/tools/audit_dr_gold_day.py` joins `DR Arena v1.1`, DR winner stamps/hits, and structured winners JSON tables into a reusable gold-day scoreboard for VTRAC capture, assigned-box winner signal, false-empty detection, and winner-aware overlay-summary mismatch measurement. |
| `TOOL-012` | `implemented` | 2026-03-15 DR promotion batch 2 | DR promotion surfaces | `dr_vtrac_cluster_strength` aggregates trace/lane/corridor/gateway/double/row-repeat/fourth-variable evidence by `VTRAC index`, and the frozen gold-day audits show it improves winner-lane promotion beyond the simpler gateway slice while still stopping well short of a rewrite-sized intervention. |
| `TOOL-013` | `validated` | 2026-03-15 DR promotion batch 3 | DR promotion surfaces | A temporary `dr_vtrac_promotion_candidates` reranker was tested on top of `dr_vtrac_cluster_strength`, but it did not improve aggregate `top-3` promotion enough to justify another persistent arena field, so it was documented and removed. |
| `TOOL-014` | `validated` | 2026-03-15 DR promotion batch 4 | DR promotion surfaces | A temporary `dr_vtrac_permutation_support` surface was tested to reward family/permutation concentration inside the same `VTRAC` neighborhood, but it underperformed `dr_vtrac_cluster_strength` on both dev and holdout windows and was removed. |
| `TOOL-015` | `implemented` | 2026-03-15 DR promotion gap anchor pass | DR diagnostics | `scripts/tools/export_dr_promotion_gap_casepack.py` turns the frozen audit CSVs into a reviewable casepack of the strongest assigned-box winner-corridor misses, with direct artifact paths for winner HTML/JSON, overlays, and stamps. Use this pack to design the next bounded attractor-suppression batch instead of tuning blindly. |
| `TOOL-016` | `implemented` | 2026-03-15 winner-promotion lab kickoff | DR diagnostics | `scripts/tools/audit_dr_gold_day.py` now widens audit-only trace/lane/double/gateway/cluster depth to `top20` and records broader rank bands plus score-gap context (`top3/top5/top8/top10/top20`, best-surface rank, cluster/gateway score gaps). This protects the lab from mistaking visibility cutoffs for genuine tool failure. |
| `TOOL-017` | `implemented` | 2026-03-15 winner-promotion lab kickoff | DR diagnostics | `scripts/tools/compare_dr_promotion_anchor_groups.py` splits matched, winner-aware DR rows into `promoted`, `visible_under_promoted`, and `buried` groups. The first pass shows `53` promoted, `33` visible-under-promoted, and `227` buried rows across the frozen windows. Use those groups to compare winner corridors vs attractor families directly before the next bounded scoring batch. |
| `TOOL-018` | `implemented` | 2026-03-15 winner-promotion lab batch 5 | DR promotion surfaces | A bounded challenger-aware rebalance now runs inside `dr_vtrac_cluster_strength` when the raw top lane is a compact double-driven monopoly and a structurally rich challenger is present. Frozen reruns improved dev cluster `top3` from `21/244` to `23/244`, best-surface `top3` from `27/244` to `29/244`, and holdout cluster `top5` from `13/110` to `14/110` without worsening holdout deeper bands. |
| `TOOL-019` | `implemented` | 2026-03-15 winner-promotion lab batch 6 | DR promotion surfaces | `dr_assigned_box_vtrac_strength` is a new predictive-side DR surface that scores `VTRAC` lanes directly from 3-digit windows inside raw assigned-box strings (`box_id`) plus bounded `final_value` windows. Frozen reruns show it is the first strong buried-regime keeper: DEV `assigned-box top10 = 84/245`, HOLDOUT `assigned-box top10 = 44/138`, and best-surface `top10` rises to `108/245` DEV and `55/138` HOLDOUT when this surface is allowed into the arena. |
| `TOOL-020` | `validated` | 2026-03-16 winner-promotion lab batch 7 | DR promotion surfaces | `dr_vtrac_fusion_strength` is a bounded agreement/rescue layer over `dr_vtrac_lane_gateway`, `dr_vtrac_cluster_strength`, and `dr_assigned_box_vtrac_strength`. It is intentionally not a replacement for assigned-box discovery. Frozen reruns show modest but real visible-band lift: DEV fusion `top3 = 25/244`, `top5 = 39/244`, best-surface `top3 = 46/245`; HOLDOUT fusion `top8 = 28/110`, best-surface `top3 = 25/138`, `top5 = 35/138`. An over-boosted rescue variant was tested and rejected, so the keeper is the first bounded fusion pass only. |
| `TOOL-021` | `validated` | 2026-03-16 VTRAC + Hot Zones joint assessment | VTRAC contract closeout | VTRAC is now documented as a lane-evidence feed, not a caller. Canonical predictive-side artifacts and winners-lens boundaries are explicit in the handoff docs, and `scripts/tools/validate_vtrac_compact_report.py` smoke-passed on representative gold-day dates (`2025-06-21`, `2025-12-31`). |
| `TOOL-022` | `validated` | 2026-03-16 VTRAC + Hot Zones joint assessment | Hot Zones contract closeout | Hot Zones is now documented as a deterministic pressure/lane extractor with primary ingest `top_lanes.csv + meta.json` and `per_lane.csv` forensic-only. `scripts/tools/hot_zones_sharepack_summary.py` smoke-passed on representative gold-day artifacts (`Virginia4 2025-06-21`, `Florida4 2026-01-03`), so the remaining finish is contract/digest framing rather than more analyzer tuning. |
| `TOOL-023` | `validated` | 2026-03-16 Aux + Control Center export slice | Aux / Control Center export layer | `scripts/tools/aux_control_center_arena.py` plus `create_candidate_universe.py --write-aux-cc-arena` now broaden preservation from Aux `summary.json` and Control Center CSVs into structured arena objects for positional pressure, VTRAC pressure, badge pressure, pair/combo context, due-double family pressure, repeat-watch context, sums context, Blackapple context, profit-alert context, and compound-event context. The signals bundle also now carries `tools.aux_control_center_context`. Validation: `tests/test_aux_control_center_arena.py` plus representative live predictive smoke on `2026-03-15` (`NorthCarolina4`, `NewJersey4`). This is an export/wiring slice, not a scorer rewrite. |

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
| `ARENA-011` | `implemented` | DR super-harness planning | DR Arena v1 now writes predictive-side `analysis/dr_arena*.json/.md` from frozen DR artifacts via `scripts/tools/dr_arena.py` and `create_candidate_universe.py --write-dr-arena`. The preserved v1/v1.1 surfaces are `dr_trace_strength`, `dr_lane_only_confidence`, `dr_competing_literal_pressure`, `dr_row_repeat_and_final_survival`, `dr_double_pressure`, `dr_empty_lens`, `dr_corridor_strength`, and `dr_structural_signals`, plus supporting ledgers for preclusters, reveals, box validity, and fourth-variable candidates. |
| `ARENA-012` | `implemented` | DR parity + broad screen + Virginia4 Midday 473 deep review | DR Arena calibration | `DR Arena v1.1` refines `dr_empty_lens` into a stricter negative-control surface that separates `true_empty`, `active_low_trust`, and `positive_trace` using reveal quality, current-band relevance, survival strength, and false-empty challenge logic rather than cold-count alone. |
| `ARENA-013` | `validated` | Virginia4 Midday 473 deep review + Batch 3 lock-in pass + 2026-03-15/16 DR gold-day audit lab | DR Arena expansion | Predictive-side structural DR surfaces now include `pre_reduction_cluster_strength`, `reveal_purity`, `family_neighborhood_saturation`, `family_asymmetry_inside_corridor`, `early_activation_strength`, `consecutive_box_progression`, `neighbor_box_support`, `core_vs_clutter_transit_score`, explicit `raw_exposure_count` vs `path_summary_count`, `dr_vtrac_lane_gateway`, `dr_vtrac_cluster_strength`, `dr_assigned_box_vtrac_strength`, and the bounded `dr_vtrac_fusion_strength` layer. The broadened audit-only `top20` view clarified the remaining gap into `visible_under_promoted` vs `buried` rows; Batch 5 helped the rich visible-under-promoted regime, Batch 6 added the first strong buried-regime keeper by reading assigned-box windows directly, and Batch 7 added a modest but real agreement/rescue fusion surface without flattening the open arena. The artifact-first anchor review in `2026-03-16__DR_ARTIFACT_FIRST_REVIEW__REMAINING_ANCHORS.md` narrowed the remaining true DR-local gap to a small same-index permutation-swarm class (`CT 234`, `FL 377`, `DE 031` style cases), while many previously discouraging anchors are now clearly good-enough arena feeds. DR is now considered wrapped for this phase per `2026-03-16__DR_WRAP_UP__HANDOFF.md`, with only one optional future path left: a tiny permutation-swarm prototype if the aggregated arena later proves it is still worth doing. |
| `ARENA-014` | `implemented` | 2026-03-16 VTRAC + Hot Zones joint assessment | VTRAC / Hot Zones arena contract | The contract is now explicit in `2026-03-16__VTRAC_HOTZ__ARENA_CONTRACT.md`: VTRAC feeds lane/family semantics (`cross_variant_lane_strength`, `straight_lane_quality`, `vt_only_lane_confidence`, `lane_dominance`, `section_lead_profile`), while Hot Zones feeds pressure/location/survivorship semantics (`late_tail_pressure_strength`, `superhot_echo_strength`, `vertical_repeat_strength`, `precol1_funnel_strength`, `col1_arrival_strength`, `repeat_3value_score`, `consensus_column_signal`). |
| `ARENA-016` | `implemented` | 2026-03-17 artifact-first confirmation | VTRAC / Hot Zones arena contract broadening | `2026-03-16__VTRAC_HOTZ__ARENA_CONTRACT.md` now explicitly preserves the concrete payload families backing the earlier semantic rollups. For VTRAC this includes enhanced JSON `indices_ranked`, `straights_ranked`, `section_summaries`, `telemetry`, and compact-report descriptors like `stable_cols`, `hot/superhot`, `mask_drop`, `mirror_supported`, `double_hits`, `confidence_score`, `top_tokens`, `recommended_tokens`, and `why`. For Hot Zones this includes `top_lanes.csv` count/span/tag fields and `per_lane.csv` row-level support/reason fields. The intent is broader arena preservation, not a narrower contract. |
| `TEST-023` | `validated` | 2026-03-17 artifact-first confirmation | VTRAC / Hot Zones anchor review | Direct anchor review of winners HTML/JSON plus live predictive outputs confirmed that neither VTRAC nor Hot Zones needs another broad scorer loop. The real remaining action was contract broadening: Hot Zones winners like `Virginia4 473` and `Florida4 611` ranked modestly but carried strong pressure/count structure, and VTRAC winners like `Virginia4 473` and `Florida4 611` showed rich same-index occurrence/persistence/stability structure in the winners lens that the predictive-side enhanced JSON and compact report already echo indirectly. |
| `ARENA-015` | `implemented` | 2026-03-16 Aux + Control Center review + export slice | Aux / Control Center arena contract | The contract is now explicit in `2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md` and live via `scripts/tools/aux_control_center_arena.py`: Aux/CC feeds the arena with structured context objects rather than only current narrow predictive methods. Primary arena objects are `aux_positional_pressure`, `aux_vtrac_pressure`, `aux_badge_pressure`, `aux_pair_band_context`, `aux_due_doubles_family_pressure`, `aux_repeat_watch_context`, `aux_sums_context`, `aux_blackapple_context`, `cc_profit_alert_context`, `cc_compound_event_context`, and `cc_tracker_context`, while full boxed badge tables / pair-status ledgers / detailed evidence JSON stay available as linked heavy truth layers. |
| `ARENA-017` | `approved` | current discussion | arena-analysis backlog | Arena-phase follow-up work is now tracked separately in `AAT9_ARENA_ANALYSIS_BACKLOG.md` so items like hidden-behind-clutter reveal, richer VTRAC compound elevation, object-registry decay, and competition carryover review do not get buried inside older tool-specific logs. |

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
| `POLICY-015` | `completed` | DR super-harness planning | Build and shake out the DR super-harness on a small seed set first; reserve live edits for obvious correctness defects and batch broader scoring/policy changes after a coherent review round. First seed set is now filled and summarized before any DR code edits. |
| `POLICY-016` | `implemented` | 2026-03-16 tool-review process shift | tool review process | Remaining tool passes now default to `winner-artifact-first`: use the winners HTML / JSON / overlay as the truth layer, derive bounded arena-feed or scoring hypotheses from that review, then validate on frozen gold-day windows before keeping anything. |
| `POLICY-017` | `implemented` | 2026-03-16 Aux + Control Center review | arena preservation discipline | For Aux / Control Center, favor broader structured arena preservation over premature trimming. Keep the bounded predictive conversion subset explicit and separate, preserve heavy truth layers via artifact links instead of silently dropping them, and let the aggregated arena decide which compound/context fields deserve later ranking or conversion weight. |

---

## Active Tests

| ID | Status | Source | Target Layer | Test |
|---|---|---|---|---|
| `TEST-001` | `approved` | current workflow agreement | example harness | Every deep-dive case should compare `truth vs baseline vs arena branch`. |
| `TEST-002` | `validated` | Example 1 / C035 | Stable Arena | Example 1 should continue to verify that family 30 is preserved in the arena even when baseline CU misses it. |
| `TEST-003` | `validated` | Example 1 | Stable projections | After projection improvements, Example 1 should show stronger family-30 promotion without destructive pack explosion. |
| `TEST-004` | `validated` | macro discussion + aggregated arena phase | harness / windows | Window-level arena recall metrics are now live and were expanded from the first 2-day pilot to the first real 6-day frozen window. The `2025-12-30..2026-01-04` review writes a scoreboard and memo under `RUNS`, showing `163` outcome rows with arena VTRAC present `156/163`, arena family present `144/163`, arena canonical present `125/163`, arena VTRAC front3 `16/163`, `92` underweighted rows, `32` conversion-gap rows, and only `39` literal downstream closures. The follow-up `gap_detail` split now separates `lane_alive_literal_missing_front3/front5` from `thin_conversion_gap`, which is the first arena-native diagnostic split strong enough to guide the next synthesis/conversion work. |
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
| `TEST-017` | `approved` | DR super-harness planning | Re-test disputed mapped boxes through the DR super-harness before removing them, especially any box that conflicts with prior evidence-led window additions. |
| `TEST-018` | `validated` | DR Arena v1 implementation | DR arena writer | Validate the additive DR arena writer with synthetic tests and predictive smoke runs so the preserved evidence surfaces match the super-harness classes before any DR retuning or V3 redesign. |
| `TEST-019` | `validated` | DR parity audit | DR arena validation | Compare the 11 fully filled DR harness cases against `DR Arena v1` outputs and confirm whether the automated arena preserves the same evidence classes before scaling to a broader batch. |
| `TEST-020` | `validated` | DR broad screen | DR arena validation | Screen an additional 14 behavior-balanced DR cases on top of the 11 filled cases, raising the evidence base to 25 total examples and identifying `dr_empty_lens` as the main weak surface before any DR retuning or V3 decision. |
| `TEST-021` | `implemented` | 2026-03-16 VTRAC + Hot Zones closeout planning | tool handoff discipline | The VTRAC/Hot Zones handoff docs now explicitly answer: what predictive-side artifacts feed the arena, what winner artifacts remain audit-only, and what stop condition ends tool-local tuning for this phase. |
| `TEST-022` | `approved` | 2026-03-16 Aux + Control Center closeout planning | Aux / Control Center arena validation | When the broader Aux / Control Center export slice lands, validate on frozen gold-day windows and competition postmortems that the new arena objects improve explanation and ranking context without being judged only as same-day direct callers. At minimum, confirm richer coverage for badge pressure, due-double regime context, Blackapple state context, profit-alert clusters, and compound-event reinforcement against winner/VTRAC-family neighborhoods. |

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
