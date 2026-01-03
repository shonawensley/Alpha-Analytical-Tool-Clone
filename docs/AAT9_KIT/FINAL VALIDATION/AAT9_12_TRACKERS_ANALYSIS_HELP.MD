AAT9 12 Trackers (Control Center) Analysis Guide — Part 1
Orientation, Contracts, and How to Read the Evaluation (v0 freeze-ready)
0) Why this guide exists (and why it matters)

The AAT9 design explicitly treats profitability tracking as a funnel: identify high‑conviction, low‑cost opportunities and then measure whether they convert over time. The “12 Trackers” are those twelve deterministic “can’t‑miss” profitability alerts (A01–A12) that aim to keep coverage small (often “under 8 box lines” or “2–4 straights”) while remaining historically effective. 

AAT9 Architecture and Master Va…

 

The Control Center’s job is to log whenever an alert fires and, over time, let you track conversions to wins. A future “Profitability Manager” layer is envisioned to track wagering/outcomes explicitly, but full ROI tracking is not implemented yet (noted as future-phase roadmap). 

AAT9 Architecture and Master Va…

 

Implication for interpretation: today, the alerts are primarily a measurement + decision-support layer (what fired, what it implied, did it hit within a window), not a “this guarantees profit” engine. 

AAT9 Architecture and Master Va…

1) What the “12 Trackers” are in AAT9 terms
1.1 Alerts as events, not “12 independent bets”

AAT9’s Control Center is framed as a cross-state dashboard/“alerts board,” and the profitability panel behaves like other alerts: an alert is an event that fires at a specific state/variant/draw context and is shown as a row while active. 

AAT9 Architecture and Master Va…

 

This matters because the system expects co-occurrence by design, and validation should explicitly check intended co-occurrences vs unexpected ones. The architecture doc even suggests that some alerts may ultimately require explicit “AND logic” (only trigger a play when another alert is also active). 

AAT9 Architecture and Master Va…

 

Rule of thumb (contract): multiple firing rows can describe one actionable situation (one play-set episode), not “12 separate wagers.” The evaluation pipeline now supports this explicitly via a deduped/merged play-set output. 

12_TRACKER_STATUS

12_TRACKER_STATUS

2) Where the 12 Trackers live (SSOT placement)
2.1 Control Center export + evaluation harness (sharepack-aligned)

The 12 trackers are integrated into a sharepack-aligned pipeline:

Export step: scripts/tools/export_control_center_sharepack.py (exports explicit ImpliedSet where required) 

12_TRACKER_STATUS

12_TRACKER_STATUS

Evaluation step: scripts/tools/evaluate_profit_alerts.py (grades set membership, applies PROMOTER rules, writes merged play-set view) 

12_TRACKER_STATUS

12_TRACKER_STATUS

Key outputs are explicitly referenced in SSOT integration notes:

sharepacks/<D>/control_center/profit_alerts_eval.md

sharepacks/<D>/control_center/profit_alerts_eval.csv

sharepacks/<D>/control_center/profit_alerts_eval_merged.csv (deduped play‑sets; avoids double counting) 

12_TRACKER_STATUS

Why this matters: you can freeze v0 semantics because the system is now described as “measurable, deterministic, and sharepack‑aligned,” rather than “mystery rows.” 

12_TRACKER_STATUS

3) The core contract that prevents “0 hits panic”
3.1 “Hit” is defined per alert, but set-membership is now first-class

The evaluation charter explicitly includes a Set hit definition when provided:
winner_literal ∈ implied_set
…and notes it’s used when the alert implies a concrete small set (e.g., STR8_8, STR8_4of8, STR8_3, or explicit BOX perms). 

12_TRACKER_STATUS

 

It also states that per-alert “what is a hit” rules live in:
docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md 

12_TRACKER_STATUS

3.2 Exporter decides the intended set; evaluator grades membership

The 2025‑12‑27 status explicitly states:

exporter updated to export ImpliedSet where required (notably A12 STR8_4of8 clamp; also BOX perms for A06/A07/A11) 

12_TRACKER_STATUS

evaluator grades set membership (winner ∈ ImpliedSet) as primary 

12_TRACKER_STATUS

This is the single most important “contract lock”: the evaluator should not “guess” what the set was supposed to be; it checks membership against the exported intent. 

12_TRACKER_STATUS

4) Row types: Candidate vs PROMOTER (do not mix these up)
4.1 PROMOTER rows are not direct-hit “callers”

The status states the evaluator treats A03/A08 as PROMOTER (not gradeable as direct hits). 

12_TRACKER_STATUS

 

And Profit Part 2 explicitly categorizes promoter signals (examples include A03 and A08), and also notes a critical A11 semantic:
“A11 does NOT invent overlay by itself.” 

AAT9 Architecture and Master Va…

 

Operational interpretation:

PROMOTER rows = context/tempo/overlay/governor signals

Candidate rows = rows that imply an actionable set (directly or via a ruleset)

If you grade a promoter as if it were a set-caller, you can manufacture meaningless “0 hits” narratives—exactly the failure mode the grading matrix + PROMOTER typing is meant to prevent. 

12_TRACKER_STATUS

12_TRACKER_STATUS

5) “Episodes” and windows: what the evaluator is actually measuring
5.1 Alerts are tracked as episodes with caps and decay

The AAT9 architecture states each alert definition has:

a cap on lines to play, and

a decay threshold (“how many draws before we drop it”)
…and that validation should compute optimal decay using backtest data (e.g., median draws-to-hit). 

AAT9 Architecture and Master Va…

This aligns with the intended future instrumentation: track each alert as an “episode” with capped budget and record whether/when it paid off. 

AAT9 Architecture and Master Va…

5.2 Caution: “low hit rate” can be a valid outcome

The most recent status commentary explicitly reframes it: workflow readiness ≠ tool performance; low hit rates are a measurement outcome, not automatically “tools broken.” 

12_TRACKER_STATUS

6) How to read the evaluation outputs (what each file is for)
6.1 profit_alerts_eval.md = human-readable scorecards + merged episodes

The evaluation flow explicitly writes:

profit_alerts_eval.md

profit_alerts_eval.csv

profit_alerts_eval_merged.csv (deduped play-sets) 

12_TRACKER_STATUS

The merged play-set file is mandatory for sane interpretation because it “avoids double counting” when alerts co-fire. 

12_TRACKER_STATUS

6.2 Two lenses: variant-faithful vs any-outcome (diagnostic)

The recent plan/status introduces an additional diagnostic lens for bounce hits:

keep primary metrics variant-faithful (Midday→Midday, Evening→Evening; Combined already sequences)

add “any” lens that scans Midday+Evening outcomes within the same time-span boundary to recognize cross-variant bounce hits 

12_TRACKER_STATUS

Interpretation contract: the “any-outcome” lens is diagnostic; you use it to understand bounce behavior without silently changing the primary window semantics. 

12_TRACKER_STATUS

7) How to use the 12 Trackers analytically (what to look for first)

This is the “do not waste time” section: here is the minimum analysis loop that extracts value.

7.1 First-pass questions (fast, high signal)

Using profit_alerts_eval.md + profit_alerts_eval_merged.csv:

Which alerts actually convert (hits) and how quickly (draws-to-hit distribution)?
The architecture explicitly recommends computing median draws-to-hit and tuning decay around it. 

AAT9 Architecture and Master Va…

Which alerts require co-occurrence to be actionable?
Because co-occurrence is expected and the blueprint suggests overlays “when A05/A12 present” etc, validation should reflect that (don’t count a “miss” if it wasn’t meant to be played solo). 

AAT9 Architecture and Master Va…

Are caps being respected (cheap by design)?
The architecture emphasizes keeping “can’t skip” alerts cheap, and flags cases where an alert would exceed cap as a detection-too-broad warning. 

AAT9 Architecture and Master Va…

7.2 What to ignore (to avoid re-opening the loop)

Do not interpret “12 rows fired” as “12 bets.” Use the deduped play-set output. 

12_TRACKER_STATUS

Do not grade PROMOTER rows as direct-hit callers. (A03/A08 PROMOTER; A11 doesn’t invent overlay by itself.) 

12_TRACKER_STATUS

AAT9 Architecture and Master Va…

8) “Freeze v0” statement (SSOT-ready)

You can declare the 12 Trackers “frozen enough for now” when the following are true (and they are explicitly claimed as achieved in status):

Profit Alerts are “measurable, deterministic, and sharepack-aligned.” 

12_TRACKER_STATUS

Exporter provides explicit ImpliedSet where required, and evaluator grades winner ∈ ImpliedSet. 

12_TRACKER_STATUS

A03/A08 are PROMOTER (not graded as direct hits). 

12_TRACKER_STATUS

Merged play-set output exists to avoid double counting spend. 

12_TRACKER_STATUS

12_TRACKER_STATUS

9) Operational safety note (prevents “year of work destroyed” fear)

The status includes a heads-up that git status shows ~3316 deletions under legacy sharepacks/DR_2025-06-21/ and offers two clean options: restore them if you want to keep legacy artifacts, otherwise commit as cleanup. 

12_TRACKER_STATUS

 

This is not a “12 trackers logic” issue; it’s a repo hygiene/separation issue—keep it isolated from Profit Alerts logic commits. 

12_TRACKER_STATUS

Part 2 preview (what I’ll build next from your next message)

Part 2 will be a per-alert interpretation map (A01–A12), but only in the “contract-locked” way that avoids semantic churn:

For each AID: row type, what it implies (set vs promoter), hit definition, expected co-occurrences, cap/decay intent, and what evidence fields matter most (so AI sessions stop re-litigating meanings). 

12_TRACKER_STATUS

AAT9 Architecture and Master Va…

Sanity Check

Open one gold-day artifact path listed in status (e.g., sharepacks/2025-06-21/control_center/profit_alerts_eval.md) and confirm you see both the candidate grading and the merged play-set concept referenced in docs/status. 

12_TRACKER_STATUS

12_TRACKER_STATUS

Verify your interpretation discipline: pick any A03/A08 row and confirm you are treating it as PROMOTER context, not as a direct “number caller.” 

12_TRACKER_STATUS

AAT9 Architecture and Master Va…

TL;DR: Part 2 is the “how to measure + interpret the 12 trackers without getting trapped in semantics.” It explains (1) the eval artifacts, (2) episode/window semantics (Variant‑faithful vs Any‑outcome), (3) what each status/column actually means, and (4) an analysis playbook to judge whether the trackers are useful signals vs noise—especially via merged play‑sets (deduped episodes) and promoter lift.

AAT9 — 12 Trackers (Control Center) Analysis Guide
Part 2 of 3 — How to Measure & Interpret Profit Alerts Without Getting Lost
Scope of Part 2

Part 2 is about measurement discipline: how to read profit_alerts_eval.*, what “hit” means, how to interpret the two lenses, and how to analyze value using merged play‑sets rather than raw “12 alerts fired” panic.

 

This is explicitly an evaluation layer (SSOT + evaluator), not “the app taking over your workflow.” The SSOT semantics locked include: candidate vs promoter/overlay; Combined is a lens; set‑based grading when Suggested implies a set; evaluator never guesses clamp subsets (uses implied_set).

12_TRACKER_STATUS

1) The four artifacts you must treat as the “source of truth” for interpretation

When you run evaluation, you should think of outputs in two tiers:

Tier A — Row‑level evaluation (“what each alert row did”)

profit_alerts_eval.csv — machine‑readable scoring output (per row).

profit_alerts_eval.md — human‑readable report view.

Tier B — Merged evaluation (“what the system actually recommended as play-sets”)

profit_alerts_eval_merged.csv — deduped play‑sets (collapses co‑firing into actionable episodes). This prevents misreading “12 alerts fired” as “12 independent bets.”

12_trackers_advice

The merged file is not optional if you want sanity: co‑firing is a design feature and must be interpreted as one episode with supporting signals, not multiple separate “bets.” (That’s why the merged output exists.)

12_trackers_advice

How evaluation is invoked

The evaluator is designed to be run per date, producing the above artifacts under the sharepack date directory (the doc references running it as python3 scripts/tools/evaluate_profit_alerts.py --date <D>).

12_trackers_advice

2) Episode semantics: the only model that keeps you out of the panic loop
2.1 Each alert firing becomes an “episode”

Each row is scored over a window defined by its DecayDraws (plus two fixed horizons). The key contract:

Primary evaluation = “hit within DecayDraws draw‑steps.”

strict_hit is a diagnostic that grades D‑only and is not the primary metric.

That strict diagnostic exists to stop a recurring confusion: “it didn’t hit on D” ≠ “it never hit within the intended window.” The eval code explicitly calls strict “diagnostic” and primary “per‑row decay window.”

REVIEW_5

2.2 Status meanings: HIT vs EXPIRED vs CENSORED (do not improvise)

From the evaluator logic:

HIT: a hit is found within the decay window; status = HIT and hit_within_decay = "Y"

REVIEW_5

EXPIRED: no hit found and the window boundary is fully known (enough steps exist); hit_within_decay = "N"

REVIEW_5

CENSORED: not enough future results exist to fully evaluate the window; hit_within_decay = "?"

REVIEW_5

And the workflow docs reinforce: if future data/results/<D+k>.txt files are missing, episodes are marked CENSORED (unknown), not failed

12_TRACKER_STATUS

.

 

Interpretation rule:
If you see a lot of CENSORED, that’s a data availability problem (future results missing), not a tracker-performance problem.

12_TRACKER_STATUS

3) Draw-steps & variants: the single most common “silent misgrading” trap

The evaluator defines “draw-steps” by Variant:

Combined: steps through real outcomes in sequence:
D Midday, D Evening, D+1 Midday, D+1 Evening, …

Midday: steps only Midday outcomes:
D Midday, D+1 Midday, D+2 Midday, …

Evening: steps only Evening outcomes:
D Evening, D+1 Evening, D+2 Evening, …

A key locked semantic (called out explicitly): Combined is a lens, not an outcome stream—only Midday/Evening are real results. Combined alerts must be evaluated against actual Midday/Evening results, not a fictional “Combined draw.”

4) The two scoring lenses you now have (and how to use them correctly)
4.1 Variant‑faithful lens (primary)

This is “grade it in the same variant it fired in”:

Midday alert → Midday outcomes only

Evening alert → Evening outcomes only

Combined alert → full Midday+Evening sequence

This lens defines the actual primary status and hit_within_decay concept.

4.2 Any‑outcome lens (diagnostic)

This exists to capture “bounce hits” (Midday signal resolves on Evening, or vice versa) without changing the primary status.

 

Rules are explicitly defined in the Charter update:

It is diagnostic; does not change the primary status.

12_TRACKER_STATUS

The window boundary stays the same “time-span boundary” as the variant-faithful window (Nth variant-faithful step).

12_TRACKER_STATUS

Within that boundary, scan any real outcomes (Midday + Evening).

12_TRACKER_STATUS

For Combined rows, any-outcome is equivalent to primary (Combined already steps through real outcomes).

12_TRACKER_STATUS

The eval outputs now include explicit “Any” fields in the markdown tables (and correspondingly in the CSV rows), e.g. Any(decay) / AnyWhen, and row columns like hit_any_within_decay and hit_any_when.

12_TRACKER_STATUS

12_TRACKER_STATUS

 

Interpretation rule:

If variant-faithful = N but any-outcome = Y, that does not mean the tracker is “broken.” It means the tracker might be timing/tempo/cycle-aware but not strictly variant-aligned—which is an important analytic finding, not a failure. This is exactly why the any-outcome lens was added.

12_TRACKER_STATUS

5) Hit types: what “counts as a hit” depends on what the row actually implies

The evaluation supports “v0 hit modes” including:

Straight hit: winner == canonical

Boxed hit: winner is a permutation of canonical

VTRAC-index hit: winner maps to same VTRAC index as canonical

Set hit: winner_literal ∈ implied_set (this is the key fix that prevents “0 hits” from grading the wrong object)

The critical architectural boundary (never blur this)

The exporter decides the intended set via implied_set.

The evaluator checks membership; it must not guess clamp subsets.

12_trackers_advice

This is the core determinism boundary that stopped the “graded object” panic loop in the first place.

12_trackers_advice

6) Promoters vs Candidates: how to avoid the “why is hit-rate 0??” illusion

Some rows are not “number callers.” They are promoters/tempo/overlays.

A03 & A08 are PROMOTER rows (not direct hit rows)

Codified rule: treat A03/A08 as PROMOTER and do not grade them as direct winner hits

12_trackers_advice

.

 

For A08 specifically, the Profit spec notes it is “a booster… never forms a box… never invents a box.”

 

What you measure for promoters (A03/A08):
Not “hit rate.” You measure conditional lift and episode quality:

Do merged play‑sets that include promoter signals hit faster / more often than those without?

Do promoter-tagged episodes correlate with tighter implied sets or higher “strength” plays?

This is exactly what the architecture doc expects: validation should examine logical relationships/overlap between alerts and confirm intended co-occurrences (rather than treating each as an independent bet).

AAT9 Architecture and Master Va…

7) The merged play‑set view: the only view that matches “how you’d actually bet”
Why merged exists

Merged episodes are mandatory because co-firing is by design; you want a single “actionable episode” view (what set would you actually play), not a pile of rows. The merged file prevents double counting and misinterpretation of spend/plays.

12_trackers_advice

How to use merged in practice

When doing analysis, always start from merged episodes:

Filter to candidate episodes (exclude pure promoter-only cases).

Compare outcomes under:

variant‑faithful status

any‑outcome status

Only then drill down into the raw row list to see which alerts contributed.

This keeps you aligned with the architecture intent: “how many combos were recommended, how much they cost, distribution of time‑to‑hit and cost per alert.”

AAT9 Architecture and Master Va…

8) A concrete analysis playbook (how to judge value without endless semantic debates)

This is the “stop looping” evaluation sequence I recommend for every state/date corpus slice.

Step 1 — Data availability sanity

If you see lots of CENSORED, first check whether future results files exist; censored is explicitly “unknown, not failed.”

12_TRACKER_STATUS

Step 2 — Start with merged episodes

Evaluate the system as “plays,” not as rows.

Use merged to answer: “How many distinct actionable sets were recommended?” (This is what merged was created for.)

12_trackers_advice

Step 3 — Compare the two lenses

For each alert type / merged episode type:

variant‑faithful hit rate (primary)

any‑outcome hit rate (diagnostic bounce)

This is explicitly reported in the Charter as two evaluation views: variant-faithful and any-outcome.

12_TRACKER_STATUS

Step 4 — Cost/time-to-hit analysis (the real “profitability” question)

The architecture doc spells out the intended evaluation: measure line count cap (cost proxy) and time-to-hit distribution, and refine alerts with long time-to-hit or too-high cost per hit.

AAT9 Architecture and Master Va…

 

So your value metrics are:

Hit@Decay and Hit@7/14 (already part of reporting)

Median draw-steps to hit (use t_hit / time-to-hit step concept in outputs)

REVIEW_5

Cost proxy: “line cap” × “how often it fires” (architecture doc calls out per-alert cap).

AAT9 Architecture and Master Va…

Step 5 — Promoter lift (instead of “promoter hit rate”)

Because promoters are not meant to be direct callers

12_trackers_advice

, measure:

Δ(hit rate) for merged episodes with promoter present vs absent

Δ(time-to-hit) with promoter present vs absent

If promoter presence correlates with tighter implied_set sizes (if you log those sizes)

9) Evidence-first debugging: how to decide “bug vs signal” fast

Here’s a deterministic triage table that prevents circular debates:

If you see…

Row says Suggested implies a set but implied_set missing/empty
→ exporter bug (because evaluator must not guess; implied_set is required for STR8_* set grading).

12_trackers_advice

EXPIRED variant-faithful but HIT on any-outcome
→ not a bug; this is exactly the bounce behavior the diagnostic lens is designed to reveal.

12_TRACKER_STATUS

CENSORED
→ missing future results, not a tracker failure.

12_TRACKER_STATUS

Promoter row “not hitting”
→ irrelevant metric: promoters are explicitly not graded as direct hit rows.

12_trackers_advice

10) “Deep future potential” notes (so later sessions know what to improve vs what to freeze)

Part 2 is not asking you to re-open implementation, but it is important to label what is “spec math” vs “v0 operationalization,” so future AI doesn’t rewrite history.

A11: score → level semantics exist in the spec

The Part 2 spec defines A11 scoring configuration with explicit thresholds (level3_min, level2_min, level1_min) and weights, implying a score-to-level mapping is intended by spec.

 

Actionable guidance (analysis-first):
Use A11 as a stratifier: compare hit/time-to-hit for different star levels (whatever the pipeline currently outputs), then decide later whether strict spec mapping is worth the effort.

A12: clamp sizing is explicitly described as a product of pinned-position allow-sets

The spec wiring shows clamp size is computed as:
clamp_size = |allow_p1| × |allow_p2| × |allow_p3|

12 PART PROFIT

 

And the Profit notes show A12 evidence is expected to expose pins/survivors and derived clamp size (example evidence payload includes pins and dr_survivors, etc.).

12 PART PROFIT

 

Actionable guidance (analysis-first):
Treat A12’s implied_set as the measured object (winner ∈ implied_set) and use clamp size as a key feature for “cost vs payoff” analysis.

Sanity Check (2 actions)

Open a gold-day profit_alerts_eval.md and confirm the tables include Any(decay) / AnyWhen columns and that the Charter language says the any-outcome lens is diagnostic (does not change primary status).

12_TRACKER_STATUS

12_TRACKER_STATUS

Pick one day with missing future results files and confirm episodes are marked CENSORED (unknown), not failed—then add the missing data/results/<D+k>.txt and rerun to see CENSORED resolve to HIT/EXPIRED.

12_TRACKER_STATUS

REVIEW_5

TL;DR: Part 3 is about turning the 12 “can’t‑miss” trackers into a stable, measurable profitability signal layer: treat each alert fire as an episode, analyze it via the row‑level evaluator + merged play‑set view, use the variant‑faithful lens as truth and the any‑outcome lens as diagnostic, then freeze semantics and move on to Master Validation + corpus expansion. The result is: you stop re‑debating meanings and start extracting real edge from data.

AAT9 12 TRACKERS (CONTROL CENTER) — ANALYSIS GUIDE (PART 3/3)
Measurement, Decisioning, Freeze Criteria, and “Future Upgrade” Roadmap
1) The unit of analysis is an “episode,” not a tracker row

The AAT9 architecture explicitly frames profitability tracking as: each alert fires → you track whether it hits and how quickly (time‑to‑hit), then compute indicator‑level metrics (hit rate, average draws‑to‑hit, ROI).

AAT9 Architecture and Master Va…

So in practice:

Raw row(s) = “alert fired in this state/variant/draw context” (informational event).

AAT9 Architecture and Master Va…

Episode = “the actionable play‑set implied by the row, tracked until hit/expiry/censor.” (This is what you can score and compare.)

codex_log_12

This is the mental model that prevents the “12 trackers are taking over the app” feeling: they are alerts/events logged by Control Center, not “new core workflow.”

AAT9 Architecture and Master Va…

2) Your measurement stack: what files matter and how to read them
2.1 The “shared alert schema” is the contract (not interpretations in chat)

The Profit spec defines a shared daily alerts schema (columns like alert_id, state, section, canonical, suggested_kind, cap_lines, decay_in_draws, evidence_json, etc.).

12 PART PROFIT

That is what makes resets survivable: the alert generator is deterministic, and the evaluator consumes that schema.

Also: the same doc explicitly shows the Control Center Alerts Panel being fed by “per‑state alerts CSVs.”

12 PART PROFIT

2.2 The evaluator outputs are designed to stop the “panic loop”

Your evaluator’s purpose (per the Codex log) is to produce:

profit_alerts_eval.md as the human‑readable summary and scorecards,

profit_alerts_eval.csv as row‑level scored output,

plus “merged episode” views to avoid double‑counting co‑fires.

codex_log_12

codex_log_12

Key: these are evaluation harness outputs, not changes to the underlying analyzers.

3) Two lenses: “variant‑faithful” truth vs “any‑outcome” diagnostic
3.1 Why two lenses exist

Codex added a cross‑variant diagnostic explicitly described as:

boundary is defined by the variant‑faithful Nth step (time‑span), and we search any real outcome (Midday/Evening) within that same boundary

This is important: it does not “cheat by extending the window,” it just detects bounce behavior within the same time‑span.

3.2 How to interpret them correctly

Variant‑faithful lens = the primary measurement. (Midday rows resolve on Midday steps; Evening on Evening steps; Combined already steps real outcomes.)

Any‑outcome lens = diagnostic only. It exists to answer: “Did we miss because the alert’s intended set hit on the opposite period?”

Your markdown report is explicitly structured to surface both (variant‑faithful scorecard + any‑outcome scorecard).

Practical rule:
If an alert “looks weak” under variant‑faithful but “strong” under any‑outcome, that’s not proof the alert is bad—it’s proof you should treat it as timing/variant‑sensitive and decide whether Combined/episode logic should carry it (later), rather than rewriting semantics again.

4) Promoters/overlays: measure their lift, don’t grade them as “callers”

Your own Profit spec is explicit that some alerts are boosters/promoters. The clearest example:

A08 is a booster and “never creates a box”; it requires has_box == 1 and only strengthens an existing lane.

That means the correct analysis is not “did A08 hit?” but:

When A08 co‑fires with an actionable set episode, does it increase:

hit rate,

speed to hit,

or justify escalation (e.g., straight overlays later)?

Also, the evaluator logic treats PROMOTER rows as non‑graded (hit fields NA).

So your analysis job becomes causal‑ish:

Compare episodes with promoters vs without promoters (same alert_id group, same state, same variant cohort).

Look at delta in hit rate and delta in median draws‑to‑hit.

No more semantic debates needed to do that.

5) “Profit Manager” analysis: what to compute (minimum viable + high leverage)

The architecture doc lays out exactly what profitability tracking is meant to evolve into: episodes with capped budget, logging plays/cost/return, and computing hit rate + average draws to hit + ROI per indicator.

AAT9 Architecture and Master Va…

Even if full ROI ledger isn’t implemented yet, you can still do high‑value v0 analytics right now:

5.1 Core per‑alert metrics (per state + per variant)

From profit_alerts_eval.*:

Fired count (how often it triggers)

Hit rate within decay window (variant‑faithful)

Median / mean draws‑to‑hit

“CENSORED” rate (missing future results; don’t misread as failure)

codex_log_12

5.2 Cost pressure & cap validation

The architecture explicitly says: track how many combos were recommended and the cost, using each alert’s cap; alerts that require too many combos or have long time‑to‑hit should be refined.

AAT9 Architecture and Master Va…

AAT9 Architecture and Master Va…

This yields a very actionable refinement loop:

If a “can’t skip” alert sometimes exceeds cap → the detection criteria may be too broad, or needs tie‑break logic (example given: choose the higher BA‑score option).

5.3 Logical relationship validation (prevents false blame)

The architecture is explicit that many alerts are conditional or overlap by design, and validation should check intended co‑occurrences (examples: A03 as extension of A01/A02; A01 + A05 combo as strong straight trigger).

AAT9 Architecture and Master Va…

This matters because it tells you how to interpret misses:

“A01 fired but no straight win” might be expected if the “straight overlay” condition (A05/A12/A11 promoter context) wasn’t present.

AAT9 Architecture and Master Va…

So: don’t downgrade an alert because you’re implicitly grading it as something the system wouldn’t actually bet.

6) Freeze criteria: what “DONE ENOUGH” means (so you stop reopening it)

Your own tracker guidance explicitly supports: implement indicators as signals/alerts now, and leave “profitability manager / progression” for later—i.e., don’t perfect scoring/progression right now.

12_trackers_advice

So “freeze v0” is justified when:

Schema is stable (alerts emitted deterministically with the shared fields).

12 PART PROFIT

Evaluator is episode‑based (can compute hit/time‑to‑hit; merged episodes exist).

codex_log_12

Promoter semantics are locked (measured as lift, not as callers—A08 is explicitly booster‑only).

Variant ambiguity is handled without semantic churn (any‑outcome lens exists as diagnostic, not truth).

After that: you pivot to Master Validation synthesis and corpus growth.

7) Future upgrades (keep these as separate, named sprints only)

This is where you preserve long‑term potential without derailing workflow again.

7.1 A11: star scoring must either match spec thresholds or be labeled “heuristic”

The Profit Part 2 spec defines an A11 star score as a weighted sum of evidence components (e.g., w_tail, w_cross_section, w_rowcov, etc.).
It then maps to star levels via thresholds (level3_min, level2_min, level1_min).
And it states A11 “never invents overlay by itself” (promotion depends on other context).
The Blueprint also frames A11 as a promoter with a11_star_level in {1,2,3}.

Upgrade sprint (later): “A11 Star Scoring Alignment”
Definition of done: implement exact score + thresholds, and ensure A11 acts as promoter/governor per spec.

7.2 A12: clamp math depends on allow_p* cartesian product (spec)

The Profit spec defines clamp sizing as:

size = len(allow_p1) * len(allow_p2) * len(allow_p3)

…and explains how clamp sizes arise from how many positions are pinned (8, 4, 2, 1).
It also specifies the evidence payload should include allow_p1/allow_p2/allow_p3.

Upgrade sprint (later): “A12 Allow‑P Clamp Implementation”
Definition of done: exporter emits allow_p* sets; implied_set is built from the cartesian product; evaluator remains membership‑based.

8) Codex / new‑chat handoff block (safe + minimal + no semantic re‑litigation)

Below is what I would paste into Codex (or a takeover chat) to prevent regression.

8.1 Guardrails (non‑negotiable)

Do not restart semantic debates; we are in “analysis mode” now. The log explicitly warns: no behavior‑changing tuning without explicit approval.

codex_log_12

Treat any giant deletion batch as a separate decision; don’t mix with Profit Alerts commits. (Codex notes large DR sharepack deletions showing in status.)

TRACK_7

8.2 Copy/paste command block (no placeholders)
git status -sb
git branch -vv
git diff --name-only --diff-filter=D | head -n 120
git diff --stat

# If you see mass deletions under sharepacks/DR_2025-06-21, DO NOT commit them with code/docs.
# Safest: restore them to remove noise.
git restore --source=HEAD --worktree sharepacks/DR_2025-06-21

# Confirm Profit Alerts evaluator outputs exist for gold days (as already reported in the log).
python3 -m py_compile scripts/tools/evaluate_profit_alerts.py
python3 scripts/tools/evaluate_profit_alerts.py --date 2025-06-21
python3 scripts/tools/evaluate_profit_alerts.py --date 2025-06-22
python3 scripts/tools/evaluate_profit_alerts.py --date 2025-06-23

# Verify the evaluator wrote the expected artifacts (paths are documented in the log).
ls -la sharepacks/2025-06-21/control_center/ | sed -n '1,200p'
ls -la sharepacks/2025-06-22/control_center/ | sed -n '1,200p'
ls -la sharepacks/2025-06-23/control_center/ | sed -n '1,200p'


(Those artifact paths and re‑evaluation are explicitly recorded in the Codex log.)

codex_log_12

9) How to decide “are the 12 trackers worth using?”

You don’t decide this by vibe. You decide it from the Master Validation + profitability metrics loop:

The architecture explicitly expects using backtest data to refine caps/decay, validate co‑occurrences, and decide whether alerts should be “watch only unless combined with others.”

AAT9 Architecture and Master Va…

So the correct “worth it?” question becomes:

Which alerts produce high hit rate at low cost, within sensible decay windows?

Which alerts act as genuine promoters (measurable lift) vs noise?

Which alerts are redundant (always co‑fire) and could be merged later?

That’s how you get value without further development rabbit holes.

Sanity Check

Evaluation sanity check: Open one gold day’s profit_alerts_eval.md and confirm the report includes both the variant‑faithful scorecard and the any‑outcome scorecard (diagnostic). This dual‑lens structure is explicitly written by the evaluator logic.

Git safety sanity check: Run git diff --name-only --diff-filter=D | head -n 120 and verify whether deletions are concentrated under sharepacks/DR_2025-06-21. If yes, restore them (or isolate them) and do not mix them into any Profit Alerts code/doc commit, per the guidance to keep cleanup separate.

TRACK_7

AAT9_Checkpoint_Log