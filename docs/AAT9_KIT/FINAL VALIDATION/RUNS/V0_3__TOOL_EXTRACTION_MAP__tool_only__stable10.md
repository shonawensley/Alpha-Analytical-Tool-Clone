# v0.3 Tool Extraction Map (tool_only, stable10)

Purpose
- Give you one plain‑English, “single-file” answer to: **what do we extract from each tool, how does it become predictions, and how do I verify it’s actually happening in the current checkpoint?**
- Reduce the “are we even using the tools the way we learned?” anxiety by pointing you to **receipts you can open** (no trust required).

Scope (what this document describes)
- Posture: `tool_only`
  - Profit Alerts are quarantined (available via other profiles, but excluded here by design).
- Experiment tag: `stable10`
- Deep-dive checkpoint pack: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8`
- “Default best” B36 policy for this checkpoint:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

If you only read one thing in the repo about “what counts as predictions and why strict looks low”, read:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

---

## 0) The 2-minute “am I looking at the latest checkpoint?” proof

Pick any day/state that exists under `sharepacks/_predictive/<D>/<STATE>/`.

1) Open the deep-dive manifest:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8/MANIFEST.csv`
2) Find the row for your day/state.
   - `promoted_tag_present=1` means the promoted baseline strategy key is present in that state’s Play Card JSON.
3) Open the Play Card JSON for that row (column `play_card_json`) and search for the promoted strategy key:
   - It contains: `tail_xlens_inject_methods18_packs22`
4) Open the human-readable Play Card markdown (column `play_card_md`).
   - At the top you’ll see “Ranked candidates … methods=…”.
   - Those `methods=...` tags are your receipts that tool extraction + transforms were actually used.

If steps (1)–(4) are true, you are looking at the current “latest checkpoint” selection policy for this posture.

---

## 1) One-page architecture (where “final predictions” come from)

The system is intentionally split into two layers:

### A) Evidence (tools)
Each analyzer produces evidence files inside the predictive sharepack:
- `sharepacks/_predictive/<D>/<STATE>/(stable|hot_zones|vtrac|aux|digit_reduction)/...`

### B) Selection (what we would play)
We convert tool evidence into two gradeable “prediction surfaces”:

1) **Candidate Universe (CU)** = “plausible combos” (unbudgeted; broader)
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json`
- Evidence/provenance (most important for understanding “why is this combo here?”):
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`

2) **Play Card** = “what we would play under a fixed budget” (budgeted; final list)
- `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json`
- Human-readable version (best “start here” file):
  - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.md`

### Portfolio is just a cross-state view (not a model)
The Predictive Portfolio is a daily “index page” that:
- sorts states (triage), and
- prints each state’s default Play Cards for B12/B24/B36.

Example (deep-dive, pinned):
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8/portfolio/2026-01-01__PREDICTIVE_PORTFOLIO__tool_only__DEEP_DIVE.md`

---

## 1.1) How selection actually happens (the “votes → score → budget” story)

This is the core “adoption” mechanism you’ve been asking about:
we did not just write docs saying “use the tools this way” — we wired those rules into how we form packs and score candidates.

1) Tools emit small, bounded “packs”
- Example: Stable emits top canonicals; Hot Zones emits top triads; Aux emits an overdue-index overlay.
2) The Candidate Universe is the union of those packs
- Every combo keeps a provenance record (which pack(s) it came from).
3) The Play Card ranks combos using those provenance “votes”
- In the Play Card markdown you’ll see lines like:
  - `` `090` score=... methods=aux_positional,due_doubles,...,stable_top ``
- That `methods=...` list is literally the cross-tool agreement signal.
4) Then the Play Card applies a budget (B12/B24/B36)
- A budget is just: “how many lines can we afford?”
- Different strategies decide how to spend those lines (but they all start from the same CU + method evidence).

If you want to see this as code (optional; not required for manual deep-dive):
- Packs are built in: `scripts/tools/create_candidate_universe.py`
- Ranking + budgets are built in: `scripts/tools/create_play_card.py`

---

## 2) Plain-English glossary (so you don’t get trapped by jargon)

- **Canonical**: digits sorted, e.g. `942 → 249`. Used for “boxed-family” grouping.
- **VTRAC index / lane**: the winner’s “neighborhood” bucket (boxed-family index), not a column in the HTML tables.
- **Pack**: a small list contributed by one source (a tool or a derived rule). Packs are labeled by `method_id`.
- **Method (`method_id`)**: “why the system included this combo.”
  - You’ll see these in `candidate_universe_evidence__*.csv` and as `methods=...` in `play_card__*.md`.
- **BOX vs STRAIGHT**
  - `BOX`: includes unique permutations of a canonical (cost 1/3/6 lines depending on triple/double/all-distinct).
  - `STRAIGHT`: exact 3-digit string (cost 1 line each).
- **Candidate Universe (CU)**: the union of all packs. Broad “recall” surface.
- **Play Card**: a budgeted cut (B12/B24/B36). This is what you should call “predictions”.

---

## 3) The “breakthrough” we locked in (the recurring theme)

Across audits + scoreboards, the consistent pattern is:

1) Tools are often good at **neighborhood correctness** (getting into the winner’s VTRAC index family).
2) But strict “top caller” hits (exact winner in a tiny list) are scarce at low budgets.
3) Therefore, we measure and optimize in two steps:
   - **Coverage / isolation**: “did we keep the right neighborhood?”
   - **Conversion**: “did we pick the right canonical inside the neighborhood under budget?”

This is why you’ll see two kinds of success in grading:
- `vtrac_index_hit` (lane hit): “we touched the right neighborhood”
- `hit_any` / `straight_hit` / `canon_hit_any_perm` (stricter): “we had the actual digits (in some form)”

If you want the “truth-layer” scoreboard view of this split, open:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`

---

## 4) What we extract from each tool (and how it becomes predictions)

This section answers your core question:
> “We did audits / integration logs / mined gold — are we *actually using* the tools the way we learned?”

The practical answer is: **yes**, primarily through the Candidate Universe pack builders + Play Card scoring/selection.
We didn’t rewrite analyzers during Crossroads; we wired their outputs into a gradeable selection layer.

The receipts are always the same three files:
- `signals_bundle__tool_only__stable10.json` (what we extracted from tools)
- `candidate_universe_evidence__tool_only__stable10.csv` (which packs were created + why)
- `play_card__tool_only__stable10.md` (how candidates were ranked + which made the budget)

Below, each tool section lists:
- **Role** (what the tool is used for)
- **What we extract**
- **Where to open receipts**
- **What we intentionally do NOT use (yet)**

### Stable10 knobs (quick reference)

These are the “how much do we take from each tool?” settings you’ll see reflected in `why_tags` inside `candidate_universe_evidence__tool_only__stable10.csv`:

- Stable (`stable_top`): `top_n:10` per section (Combined / Midday / Evening), BOX-expanded
- Hot Zones (`hot_zones_top`): `top_n:8` triads, STRAIGHT
- VTRAC Enhanced (`vtrac_enhanced_top`): `top_n:8` straights, STRAIGHT
- Aux positional shortlist (`aux_positional`): `top_n:10` combos, STRAIGHT
- Aux overdue indices (`aux_vtrac_index_overdue`): `top_n:2` indices per variant (members become STRAIGHT combos)
- Due Doubles (`due_doubles`): `top_n:4` canonicals per variant, BOX-expanded

If you see different `top_n:*` values in a given day/state evidence CSV, that means you’re looking at a different experiment tag or a one-off experiment run.

### 4.1 Stable Pattern Extractor (“Stable”)

Role (plain English)
- Strong at: surfacing **important canonicals/families** that often live in the winner’s neighborhood.
- Weak at: being a reliable “top-3 exact caller” by itself.
- So in `tool_only` it’s consumed as:
  - a convergence voter (agreement signal), and
  - a lane/neighborhood lens (help retain the right index families).

What we extract (stable10)
- File: `<STATE>_stable_patterns_scores.csv`
- We extract the top Stable canonicals per section (Combined / Midday / Evening) and BOX-expand them.
- In stable10, the Stable pack is typically `top_n=10` per section (you can confirm in evidence CSV).

Receipts to open
- Tool extraction summary:
  - `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - Look at: `tools.stable.sections`
- Raw Stable source files:
  - `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
  - (Also present but not used as picks by default: `*_compound.csv`, `*_families.csv`, `*_metrics.json`)
- Pack provenance (proof it became candidates):
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
  - Filter `method_id == stable_top`
- Play card ranking view (proof it influenced selection):
  - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.md`
  - In “Ranked candidates …” you’ll see `methods=...stable_top...`

What we intentionally do NOT use as predictive inputs (yet)
- Stable “winner spotlight” artifacts and anything winners-dependent (post-results only).
- Stable metrics (`*_metrics.json`) are treated as tool-health diagnostics and explanation-only, not direct pick generators.
- Stable compound/families leaderboards are currently “support/evidence” (useful for future bounded index-vote packs, but not turned into primary picks by default).

Related “why this posture exists” doc:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`

---

### 4.2 Hot Zones

Role (plain English)
- Strong at: producing a **small, tagged triad list** that often points into the right neighborhood.
- Weak at: being a strict straight caller at small top‑K.
- So it is consumed as a convergence voter + lane lens.

What we extract (stable10)
- File: `<D>_hot_zones_winner_map.json`
- We extract the top Hot Zones triads (typically `top_n=8`, straight strings).

Receipts to open
- Tool extraction summary:
  - `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - Look at: `tools.hot_zones.triads`
- Raw Hot Zones source file:
  - `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`
- Pack provenance:
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
  - Filter `method_id == hot_zones_top`
- Play card ranking view:
  - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.md` (look for `hot_zones_top` in `methods=...`)

What we intentionally do NOT use as predictive inputs (yet)
- “BOX-equivalent” canonicalization of Hot Zones triads is research-only (can widen cost quickly).
- Post-results-only Hot Zones diagnostics are kept for explanation, not prediction.

Related posture doc:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`

---

### 4.3 VTRAC Enhanced

Role (plain English)
- Strong at: ranking VTRAC indices + providing a small set of “top straights” that often reflect the active neighborhood.
- Weak at: strict straight hits at small top‑K.
- So it’s used for convergence and neighborhood evidence, not “play top-8 and expect a hit”.

What we extract (stable10)
- From the VTRAC Enhanced JSON, we extract:
  - Top indices (ranked)
  - Top straights (typically `top_n=8`)

Receipts to open
- Tool extraction summary:
  - `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - Look at: `tools.vtrac_enhanced.top_indices` and `tools.vtrac_enhanced.top_straights`
- Raw VTRAC Enhanced source file:
  - `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/*vtrac_enhanced*.json`
- Pack provenance:
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
  - Filter `method_id == vtrac_enhanced_top`
- Play card ranking view:
  - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.md` (look for `vtrac_enhanced_top` in methods)

What we intentionally do NOT use as predictive inputs (yet)
- Winners placement diagnostics (`winner_index_placements`) are post-results only.
- Any large default index-closure packs seeded from VTRAC indices (can be added later as bounded experiments, but not default).

Related posture doc:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`

---

### 4.4 Digit Reduction (DR)

Role (plain English)
- DR is valuable as an **envelope / structure lens**, but the “top candidates” caller surface was repeatedly weak in audits.
- In stable10 tool-only defaults, we keep DR evidence on disk, but we do not let “DR top candidates” dominate predictions.

What we extract (stable10)
- We extract DR signals for inspection (DR004 signals) from the DR steps trace:
  - Top canonicals / indices / pools per variant
  - These are for analysis and future bounded “envelope packs”, not automatic picks by default.

Receipts to open
- Tool extraction summary:
  - `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - Look at: `tools.digit_reduction_dr004.sections`
- Raw DR steps source file:
  - `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`
- Proof it is NOT currently a default “pick pack”:
  - In `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
  - You should *not* see `method_id == digit_reduction_analyzer_v2` unless you explicitly enabled DR top-N in an experiment.

Why this posture exists
- The v0 audit found the “DR top candidates” caller surface had `hit_any=0/138` in the v0 Jan audit window, despite DR being rich in post-hoc overlays.

Related posture doc:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`

---

### 4.5 Aux (Auxiliary / compound features)

Role (plain English)
- Aux produces “pressure” / “overdue” / “doubles” style signals that are often:
  - compact (cheap) closures, and
  - good at pointing to neighborhoods (indices) or giving conversion helpers.
- In tool-only, we keep Aux packs **bounded** (small top-N) so they add signal without exploding cost.

What we extract (stable10)
From Aux summary, we extract:
- A positional shortlist (top candidates; primarily for structure/pressure, not strict straight hits)
- A VTRAC overlay “overdue indices” list (a direct neighborhood hint)

We also consume Control Center “due doubles” as compact BOX closures:
- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`

Receipts to open
- Tool extraction summary:
  - `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - Look at: `tools.aux.positional_shortlist` and `tools.aux.vtrac_overlay_top`
- Raw Aux source file:
  - `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`
- Pack provenance (what actually became Candidate Universe packs):
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
  - Filter `method_id` in:
    - `aux_positional`
    - `aux_vtrac_index_overdue`
    - `due_doubles`
    - `due_doubles_mirror_single`
    - `due_doubles_mirror_double`
    - `mirror_pair_closure`

Related posture doc:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`

---

## 5) “What are these weird method tags?” (the compound/derived layer)

This is the part that often feels like “jargon”, but it’s actually your strongest receipt:
it tells you exactly which “breakthrough primitives” were applied.

The easiest way to learn these is to open:
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`

Then look at these columns:
- `source_class` (tool vs derived)
- `method_id` (what rule/tool contributed it)
- `why_tags` (high-level reason)
- `evidence_paths` (which raw file it came from)
- `transform_chain` (the literal transformations)

Common method_ids you’ll see in stable10 tool-only (examples):

Tool-fed packs (direct tool extraction)
- `stable_top` (Stable top canonicals, BOX-expanded)
- `hot_zones_top` (Hot Zones top triads, STRAIGHT)
- `vtrac_enhanced_top` (VTRAC Enhanced top straights, STRAIGHT)
- `aux_positional` (Aux positional shortlist, STRAIGHT)
- `aux_vtrac_index_overdue` (Aux “overdue indices” → members of that index, STRAIGHT)

Control Center / compact closures
- `due_doubles` (compact doubles canonicals, BOX-expanded)

Derived conversion helpers (built from other signals)
- `due_doubles_mirror_single` / `due_doubles_mirror_double`
  - “mirror” here uses the vtrac-pair mapping: `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`
- `mirror_pair_closure`
  - “if a mirror pair looks active, generate bounded closures using a few strong ‘third digits’”

Derived combo packs / transforms
- `R-perm-4`
  - built from a 4-digit envelope → choose-3 triads → bounded permutation set
- `PackA_vt8`, `PackB_mirror3rd`
  - small deterministic transforms that create cheap “lane-like” coverage around a seed triad

If you want one concrete “see it with your own eyes” example:
- `sharepacks/_predictive/2026-01-01/Ohio4/candidate_universe_evidence__tool_only__stable10.csv`

---

## 6) “But are we actually trying to hit?” (the simplest truthful answer)

Yes. The **Play Cards are the predictions**, and they are graded directly against results.

What is *not* a “hit model” today is the **portfolio ranking**, which is a triage sort order.
That is intentional (see v0.2 defaults doc for the original justification):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

In plain English, the `tool_only` portfolio ranking is:
1) higher cross-tool agreement (`CU top support`)
2) smaller total candidate universe (`CU union`)
3) more compact doubles-closure opportunities (`due_doubles_count`)
4) more packs present (`CU packs`)

It’s a “which state looks clearest?” ordering, not “guaranteed hit probability”.

If you want one place that summarizes broad performance without manual CSV work:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__stable10.md`

That rollup already aggregates strict and inclusive metrics across the full 16-day deep-dive range.

---

## 7) Appendix — the “V report” you remembered (where it lives today)

You were remembering something real. It just isn’t one file named “V report” anymore.

Today it’s split into:
- Per-tool “how to consume this tool” (SSOT):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`
- Integration log (ties the story together, explains training vs deployment loop):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- v0.3 policy (current “what’s default / what’s promoted / why conversion is the bottleneck”):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

---

## 8) Appendix — deep dive dates available (current repo inventory)

Dates present under `sharepacks/_predictive/` (and included in the deep-dive package manifest):
- `2026-01-01` → `2026-01-09`
- `2026-01-15` → `2026-01-18`
- `2026-01-20` → `2026-01-22`

If you ever want to re-check this without guessing, open:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8/MANIFEST.csv`

---

## 9) Appendix — one worked example (OntarioCanada4, D=2026-01-15)

This is here for one reason: when you feel “there are too many artifacts”, this gives you a single repeatable “open order” you can memorize.

### 9.1 The 5 files you actually need (broad manual checking)

1) Cross‑state daily briefing (shows the final Play Cards for every state):
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/deep_dive__checkpoint_v0_3-stable10-spinecap6__f31e7af8/portfolio/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only__DEEP_DIVE.md`

2) The results you grade against (same date as the portfolio):
- `data/results/2026-01-15.txt`

3) The “final predictions” for this state (human‑friendly):
- `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.md`

4) The “final predictions” for this state (machine JSON; same content, different format):
- `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.json`

5) The “why is this combo even here?” provenance table:
- `sharepacks/_predictive/2026-01-15/OntarioCanada4/candidate_universe_evidence__tool_only__stable10.csv`

Optional (if you want the system’s own grading summary rather than doing it by hand):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PLAY_CARD_GRADE__tool_only__stable10.md`

### 9.2 How to use those 5 files (no jargon)

Step A — Start broad (portfolio)
- Open the portfolio and find `OntarioCanada4` in the ranked table.
- That ranked table is *not* a hit-rate claim. It’s just saying: “how tight / convergent does the evidence look today?”
- Then scroll down to the `### B36 (...)` section and find the Ontario B36 list.
  - That B36 list is the best “latest stable10 tool_only baseline” surface to manually compare vs results.

Step B — Compare the Play Card to results
- Open `data/results/2026-01-15.txt` and locate the Ontario winners for that date (Midday/Evening).
- Then check whether the winners show up in:
  - the Ontario B36 list in the portfolio, or
  - `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.md`

Step C — If it missed: answer the *right* question first
When you miss, don’t jump straight to “tools failed”.
The fastest diagnostic is:
- Did we miss because we never *kept the right neighborhood* (lane/index miss)?
- Or did we keep the neighborhood but fail to pick the right canonical inside it (conversion miss)?

You can see that “what stage missed?” story in two places:
- the grade report (easy mode): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PLAY_CARD_GRADE__tool_only__stable10.md`
- the Play Card itself (manual mode): look at the highest-ranked lines and their `methods=...` tags in `play_card__tool_only__stable10.md`

Step D — If you want “what did we extract from tools on that day?”
- Open: `sharepacks/_predictive/2026-01-15/OntarioCanada4/signals_bundle__tool_only__stable10.json`
  - That is the compact “tool extraction” snapshot (what the system saw and extracted).

Step E — If you want “prove this was actually adopted into selection”
- In `play_card__tool_only__stable10.md`, each top candidate prints `methods=...`.
- Then open `candidate_universe_evidence__tool_only__stable10.csv` and filter by that `method_id`.
  - That is the bridge from “tool output exists” → “the system actually used it to build candidates”.

### 9.3 One key mental-model lock (stops 80% of confusion)

- Portfolio **ranking**: “which states look cleanest / most convergent today?”
- Play Cards **(B12/B24/B36)**: “what the system would actually play under that budget”.

So yes: you *should* evaluate Play Cards against results.
You should not treat the portfolio rank itself as “predicted hit probability”.
