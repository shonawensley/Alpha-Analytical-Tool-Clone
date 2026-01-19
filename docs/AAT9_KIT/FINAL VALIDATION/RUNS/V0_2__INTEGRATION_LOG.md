# v0.2 Integration Log — “Make It Coherent” (Stable → DR → Hot Zones → VTRAC → Selection)

Purpose: a single, human-readable log of what we changed while converting the “messy corpus” (runs/templates/sharepacks) into a **coherent v0.2 baseline**.

This complements (does not replace):
- Gold ledger (repeatable, hit-linked learnings): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- v0.2 defaults (what we do by default): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Fix-now vs fix-later (defects vs hypotheses): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Analyzer-change backlog (“nothing gets missed” for tool edits): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ANALYZER_CHANGE_BACKLOG.md`

Mental model (keep this in your head)
-------------------------------------
- **Sharepacks** are the immutable evidence snapshots.
- **RUNS** is the review + grading + triage layer.
- v0.2 is “selection + measurement integrity” (no speculative analyzer tuning).
- v0.3 is “analyzer edits” (only after we can measure deltas and avoid overfitting).

This log exists because:
- context resets happen,
- there are many moving parts,
- and you want one place where the “what changed / why / what remains” story lives.

---

## Current posture (so we don’t relapse into chaos)

### Profit Alerts (Brain‑2) posture
- Profit Alerts are quarantined by ablation profiles; v0.2 defaults are `tool_only`.
- Profit Alerts are not deleted yet (they remain as an ablation/control surface), but they should have **zero default influence** on predictive artifacts.

### Predictive vs post-results
- Predictive (“BEFORE”): `sharepacks/_predictive/<D>/...` must remain winners-free.
- Post-results (“AFTER”): `sharepacks/<D>/...` includes winners lens + evaluation artifacts.
- Candidate Universe / Play Cards are **additive** artifacts that make “what we would have played” gradeable.

---

## Training loop vs deployment loop (how the system improves without “leakage”)

This is the confusion trap we kept hitting, so here is the SSOT answer:

- “Leakage” does **not** mean “Master Validation can’t improve predictions.”
- “Leakage” means: *don’t claim something was predicted pre-results if you used winners-dependent artifacts to produce it for that same day.*

### Training loop (post-results; winner known)

Goal: extract repeatable, hit-linked learnings (“gold”) and convert them into explicit decisions:
- what each tool is good for (caller vs corroborator vs envelope),
- what inputs should feed forward into selection layers,
- what defects are correctness bugs (Fix‑Now) vs hypotheses (Fix‑Later),
- which changes belong in v0.2 (selection/measurement) vs v0.3 (analyzer edits).

Inputs (evidence + labels):
- `sharepacks/<D>/<STATE>/winners/<STATE>/*.html` + `.json`
- `sharepacks/<D>/<STATE>/(stable|digit_reduction|hot_zones|vtrac)/...`
- Master Validation run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

Outputs (decisions; durable homes):
- Gold (repeatable learnings + bounded actions): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- v0.2 defaults (what we run by default): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Tool consumption decisions (keep/demote/eval-only as predictive inputs): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/*_V0__FEATURE_DECISIONS.md`
- Fix-now vs fix-later: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Analyzer edits backlog (v0.3 inventory; “nothing gets missed”): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ANALYZER_CHANGE_BACKLOG.md`

### Deployment loop (pre-results; winner unknown)

Goal: produce an immutable “before” snapshot and explicit, gradeable prediction artifacts.

Inputs (frozen evidence only; no labels):
- Predictive sharepack: `sharepacks/_predictive/<D>/...` (built from the H workbook where `D = H + 1`)
- v0.2 defaults (so we run the same way every time)

Outputs (pre-results artifacts; gradeable later):
- Candidate Universe (gradeable playset): `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
- Play cards (budgeted cuts): `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only.json`
- Portfolio triage: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`

Then, once `data/results/<D>.txt` exists, grading happens **outside** predictive sharepacks:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE__tool_only.*`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE__tool_only.*`

### Where the two loops meet (the actual “compounding improvement” process)

Master Validation does not “auto-train” Candidate Universe. Instead:
- Master Validation (training loop) produces explicit decisions (feature decisions + gold + defaults).
- v0.2 defaults encode those decisions.
- Candidate Universe / Play Cards then become the deterministic “what we would have played” artifacts under those defaults.
- Grading + rollups show whether the decisions improve results across windows (and out-of-sample once we resume runs).

This is the clean way to get your desired effect (“daily gold reports compound into a better system”) without confusing hindsight with prediction.

### Budgets (important clarity)
- Budgets (B12/B24/B36) are **play-card cuts**, not tool behavior.
- They do not change the underlying sharepack evidence and they do not change Candidate Universe packs.
- They exist so we can run controlled experiments and grade “small playable sets” without changing analyzers.

---

## 2026‑01‑17 — Stable: correctness gates + compound behavior fixes (implemented)

### What we fixed (and why it mattered)

**Stable schema validation (tracked-state gate by default)**
- Goal: prevent “the tool changed shape silently” (a common reason run reports feel inconsistent).
- Code: `scripts/checks/validate_stable_schema.py`
- Commit: `2082b5ae` (“checks: make Stable schema gate tracked-state by default”)

**Stable score_len non-negative contract**
- Goal: ensure “extra length bonus” doesn’t become a penalty in tail/edge cases.
- Code: `alpha_analytical/stable/__init__.py`, with a guard in `scripts/checks/validate_stable_schema.py`
- Commit: `88232ece` (“Stable: clamp extra length bonus; gate score_len”)
- Backlog pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ANALYZER_CHANGE_BACKLOG.md` (STABLE-005)

**Stable compound flag parsing + score contracts**
- Goal: stop “compound” output from drifting due to brittle parsing or ambiguous flags.
- Code: `alpha_analytical/stable/compound.py`
- Tests added to lock behavior:
  - `tests/test_stable_compound.py`
  - `tests/test_stable_contracts.py`
- Commit: `b7a42db3` (“Fix Stable compound flag parsing and update score contracts”)

### Why this is aligned with the Master Validation mission
Master Validation templates repeatedly depend on Stable being “the contract”: downstream analysis can’t reliably reason about what Stable meant if:
- canonicals are malformed,
- scores can go negative unexpectedly,
- or compound flags change interpretation across days.

So these are not “performance tuning”; they are **measurement integrity**.

---

## 2026‑01‑17 — Hot Zones: determinism + selective guard behavior (contract-locked)

### What was locked (and why it mattered)

**HOTZ‑002: deterministic ordering / tie-break**
- Goal: prevent score ties from reshuffling output order (which looks like “different results” run-to-run).
- Test: `tests/test_hot_zones_scanner.py`
- Commit: `a954b752` (“Add Hot Zones deterministic top-lane tie-break test”)

**HOTZ‑001: guard/selective injection gates**
- Goal: keep the candidate pool bounded while ensuring the obvious Set1 funnel triads don’t get “dropped” from exported artifacts.
- Test: `tests/test_hot_zones_guard.py`
- Commit: `973d67d7` (“Hot Zones: lock guard selectivity gates (HOTZ-001)”)

### What “3-digit only” means (important disambiguation)
The “3-digit only” constraint applies only to:
- deriving a guard seed from the literal Set1/Draw1 col_value.

It does **not** mean:
- “Hot Zones only supports 3-digit patterns.”

Hot Zones still mines triads out of longer strings via substring extraction (evidence still comes from long patterns); the guard is just a bounded safety net.

### Why this helps “superbrain” later
Superbrain/selection only becomes meaningful once every tool’s outputs are:
- deterministic,
- reproducible,
- and explainable.

Hot Zones is now safe to consume as an index/lane lens (not a strict top‑8 straight oracle).

---

## 2026‑01‑18 — Candidate Universe: add an “evidence view” export (new)

### Why we added it
To address the exact paranoia you described:
- “Is Candidate Universe just a bunch of combo/budget rules that override evidence?”

The answer is: it shouldn’t be. So we now have an explicit “what is direct tool evidence vs what is derived” view.

### What changed
`scripts/tools/create_candidate_universe.py` now supports:
- `--write-evidence` → writes:
  - `candidate_universe_evidence__<profile>.csv`
  - `candidate_universe_evidence__<profile>.md`

These files do **not** apply budgets and do **not** choose picks; they list canonicals and their provenance:
- source_class = `tool` / `control_center` / `derived`
- method_id + pack_id + variant + evidence_paths + transform_chain

This makes it easy to verify:
- the raw evidence universe is still present,
- derived packs are explicitly labelled,
- budgets are only applied in Play Cards (separate step).

---

## Hot Zones deep-brainstorm (task docs) — what we keep vs what we treat as backlog

You wrote a lot of Hot Zones “theory” content. It was not wasted.
The value is: it clarifies the *intended* division of labor:
- Hot Zones = deterministic extractor + evidence tags
- Analysis / selection = fusion + bounded transforms

What we keep as “real” today:
- The winners HTML shows * and ** in the late columns (survivorship pressure) and that aligns with how Hot Zones is supposed to focus attention.
- The current Hot Zones implementation already has several of the primitives your docs emphasize:
  - vertical support signals
  - vt_only_lane evidence
  - precol1 funnel signals
  - superhot slot scoring (Set1 col1/2)

What we treat as v0.3 backlog (not something we jam into v0.2 blindly):
- “repeat_3value_score” (box-to-box / column-to-column / set-to-set repeats)
- “consensus flag” (true column consensus in col1/2)
- “transit-digit reveal delta” (rerun elimination passes to see what stabilizes)

Those belong in the analyzer backlog unless we can first measure their lift via a bounded harness.

---

## 2026-01-19 — Hot Zones weight sweep harness (HOTZ‑003) (implemented + measured)

Purpose: measure whether a bounded weight tweak (VT-only lane bonus) meaningfully improves winner visibility *without* “winning by widening”.

- Harness: `scripts/tools/hot_zones_weight_sweep.py`
  - Replays Hot Zones from frozen sharepack JSON tables: `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`
  - Grades against official results: `data/results/<D>.txt`
  - Writes CSV/MD into RUNS (reporting-only; no sharepack mutation; no analyzer writes)
- Sweep (bounded): `w_vt_only_lane_bonus` = `0.8` (baseline), `0.9`, `1.0`, `1.1`
- Outputs (3 regression windows):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-06-21_to_2025-06-23.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-12-30_to_2026-01-04.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2026-01-05_to_2026-01-09.md` (and `.csv`)

Measured result (high-level):
- Increasing `w_vt_only_lane_bonus` does **not** materially improve winner-in-top‑K rates (Top8/Top12/Top20) on these windows.
- It *can* improve **average rank** for “VT-only visible” winners, but not enough to move them into top‑K reliably.

Follow-up (multi-parameter sweep):
- We ran a second sweep that adds `w_col1_arrival` (so we can test “arrival/funnel lift” alongside VT-only lift).
- Outputs (3 regression windows):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-06-21_to_2025-06-23.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-12-30_to_2026-01-04.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2026-01-05_to_2026-01-09.md` (and `.csv`)
- Result summary:
  - `w_col1_arrival=2.1` can produce **small** Top8 gains in some windows (typically a borderline winner moving rank 9→8).
  - It does not create a stable lift in Top12/Top20 across windows, and vt-only-visible winners still do not rise into top‑K reliably.

Measurement upgrade (gateway lens):
- We extended the harness to report **VTRAC index hit** in top‑K (the same “gateway language” as Master Validation’s 4 hit criteria):
  - `vtrac_index_hit_top8/top12/top20`
  - `vtrac_index_hit_only_topK` (index hit, but canonical missing: classic “lane correct, box miss”)
- Sweep v3 outputs (same windows, same parameter space; adds index metrics):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-06-21_to_2025-06-23.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-12-30_to_2026-01-04.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2026-01-05_to_2026-01-09.md` (and `.csv`)
- Interpretation notes (paired with winners lens + RUNS cases):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__ANALYSIS.md`

Key conclusion after v3:
- Hot Zones’ **canonical Top‑K** rates remain low and weight tweaks do not create stable lift.
- Hot Zones’ **index-hit** rates are materially higher (and a large fraction is index-hit-only), which validates Hot Zones as a lane/index lens.
- Weight tuning is still not a v0.2 lever; the next high-confidence lever is selection-layer “index-hit → box-hit conversion” experiments.

Optional selection-layer experiment (Hot Zones index-closure pack):
- Implemented an additive, bounded conversion helper (`method_id=hot_zones_index_closure`) and graded it on the Jan window.
- Result: **no measurable lift** in Candidate Universe union hits or Play Card hits; slight pool widening only.
- Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_INDEX_CLOSURE__EXPERIMENT__2026-01-05_to_2026-01-09.md`
- Decision: keep it **off by default** (v0.2), leave as a research knob only.

Interpretation:
- HOTZ‑003 weight tuning is not (so far) the lever that produces meaningful lift on the baseline windows.
- Even with `w_vt_only_lane_bonus` + `w_col1_arrival`, the effects are small and inconsistent (mostly “borderline nudges”).
- v0.2 posture remains: treat Hot Zones as an **evidence/lane lens** feeding selection policies, not as an 8-straight oracle.

## Next work (high confidence, low regret)

1) Close the HOTZ‑003 loop (decision + backlog hygiene)
- Keep default Hot Zones weights unchanged for now (no measured top‑K lift on the v0 windows).
- Update HOTZ‑003 in the v0.3 analyzer backlog with the measured sweep outputs + conclusion (sweep v1/v2/v3).

2) Keep converting “lane correctness” into bounded selection transforms
- This is the core “index_hit_only → box_hit” conversion problem.
- It is primarily solved in selection-layer policies, not by trying to make every tool a perfect straight caller.

3) Only then: consider true analyzer tuning (v0.3)
- Anything that is “correctness bug” becomes Fix‑Now.
- Anything else becomes a v0.3 backlog item with measured deltas + regression plan.

---

## 2026‑01‑19 — VTRAC Enhanced block completed (gateway harness + semantics)

- Goal: measure VTRAC Enhanced as a **gateway lens** (index-hit / lane-hit / box-hit decomposition), not a standalone “top‑K straight caller”.
- Terminology guardrail (prevents the “doubles are excluded” confusion):
  - `vtrac_index` is defined for **unique** and **double** winners (1–35). **Triples** intentionally have no `vtrac_index` (legacy behavior).
  - `modules.vtrac_reference.VTRAC_DISPLAY` is a **boxed/canonical UI view**: it lists the 8 boxed members (canonicals) per index (and the smaller double-only members for double-heavy indices).
  - `modules.vtrac_reference.get_index_set(index)` returns the full **straight-line** closure for an index (explicit 3-digit permutations), so sizes are typically **48** (8 canonicals × 6 perms), **24** (mixed singles+doubles), or **6** (pure double indices like index 1).
- Actions (planned): harness across the three regression windows + a small curated winners-lens review set, then explicit feature decisions:
  - Fix‑Now (if correctness/schema issues exist)
  - v0.2 selection-layer consumption changes (only if measured lift)
  - v0.3 analyzer tuning backlog (if it looks promising but is not yet proven)

### Status (done)

- Added reporting-only harness + outputs (3 windows):
  - Script: `scripts/tools/vtrac_enhanced_harness.py`
  - Outputs:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
- Expanded the v0 cases doc to be harness-driven across all three windows:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
- Updated the v0 audits/decisions to reflect the clarified semantics and measured harness outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
  - (guardrail wording): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`
- Updated navigation + backlog so the tool-by-tool process stays unified:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ANALYZER_CHANGE_BACKLOG.md`
- Captured the repeatable “why it matters” as a bounded Gold entry:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (`GOLD-0030`)

### Why this improves the tool/system (in v0.2 terms)

- It measures VTRAC Enhanced in the same **gateway language** you actually reason with in Master Validation (box/canonical and index-hit), instead of judging it as “top‑K straight only”.
- It removes a major recurring confusion source by explicitly disambiguating:
  - “8 boxed canonicals per index” (UI view) vs
  - “straight-line closure size” (48/24/6 lines depending the index composition),
  - and “doubles have an index; triples don’t”.
- It creates a stable, repeatable harness across three windows, so any future v0.3 tuning proposals are evidence-gated (measured deltas + regression expectations), not vibes.

---

## 2026‑01‑19 — Digit Reduction block completed (correctness validation + harness-driven study queue)

- Goal: treat DR as a **trace/envelope lens** (as per design intent), and stop mistaking “top candidates” for the right predictive surface.
- Baseline posture is already locked in v0.2 defaults: DR “top candidates” are **off** by default (`--top-n-dr 0`) in tool-first mode.

### Status (done)

- Correctness validation (frozen sharepacks): DR winners artifacts are internally consistent (stamp ↔ flags ↔ hits) on a multi-window sentinel set:
  - `scripts/tools/validate_dr_winners.py` (run in warn-only mode on representative sharepacks)
- Cross-window DR lens reports (activation + trace visibility):
  - Added the missing early-window lens report:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__DR_LENS_REPORT.md`
  - Existing window lens reports (already present and referenced via range-pack patterns):
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__DR_LENS_REPORT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__DR_LENS_REPORT.md`
- Harness-driven DR study queue (bounded, high-signal “buried-but-present” + “empty lens” cases):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md`
  - Wired into the DR case-audit doc:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`

### Why this improves the tool/system (in v0.2 terms)

- It separates a recurring confusion source:
  - DR often “sees” the winner in the trace/overlay (high `exact_any` / `vtrac_any`), even when the **best_pattern top-candidates** list does not.
- It makes the next work deterministic and bounded:
  - we can now review DR with a harness-driven queue (instead of browsing random days), using the winners HTML + DR overlay as the ground-truth lens.
- It keeps v0.2 additive and measurable:
  - no analyzer tuning yet; we measure and decide what DR evidence should be consumed in selection layers, and only then propose v0.3 analyzer edits with acceptance thresholds.
