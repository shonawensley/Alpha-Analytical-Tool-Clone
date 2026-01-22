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
- Added reporting-only “envelope harness” (digit-pool scoring from `*_digit_reduction_steps.csv` + gateway metrics):
  - Script: `scripts/tools/dr_envelope_harness.py`
  - Outputs (3 windows):
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
  - Interpretation notes:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__ANALYSIS.md`

### Why this improves the tool/system (in v0.2 terms)

- It separates a recurring confusion source:
  - DR often “sees” the winner in the trace/overlay (high `exact_any` / `vtrac_any`), even when the **best_pattern top-candidates** list does not.
- It measures DR in the same “gateway” language used elsewhere (canonical-hit vs `vtrac_index` hit), and shows DR’s envelope scoring is far better at index-hit than at tight canonical Top‑K.
- It makes the next work deterministic and bounded:
  - we can now review DR with a harness-driven queue (instead of browsing random days), using the winners HTML + DR overlay as the ground-truth lens.
- It keeps v0.2 additive and measurable:
  - no analyzer tuning yet; we measure and decide what DR evidence should be consumed in selection layers, and only then propose v0.3 analyzer edits with acceptance thresholds.

### Optional selection-layer experiment (v0.3 prework): DR envelope packs from steps CSV (Top2)

- Implemented an **additive** Candidate Universe pack source that converts DR trace evidence (`*_digit_reduction_steps.csv`) into bounded BOX packs:
  - `scripts/tools/create_candidate_universe.py` (`--dr-envelope-boxed-canonicals 2`)
  - New `method_id=digit_reduction_envelope_steps` packs:
    - `digit_reduction_envelope:Combined:top2`
    - `digit_reduction_envelope:Midday:top2`
    - `digit_reduction_envelope:Evening:top2`
- Important containment rule: these DR envelope packs are **excluded** from the pooled digit envelope (so they don’t silently perturb combo packs while we’re still measuring).
- Experiment summary (baseline tool_only union vs +DR envelope Top2 across all three windows):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ENVELOPE_PACK__EXPERIMENT__TOP2.md`
- Decision (current): **keep off by default** (v0.2) and treat as a measured research knob until we see a stable, non-regressing lift without unacceptable pool widening.

### Optional selection-layer experiment (v0.3 prework): DR‑004 trace → bounded BOX packs

- Spec (inputs + non-negotiables + acceptance gates): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_004__SPEC.md`
- Implementation (default-off flags): `scripts/tools/create_candidate_universe.py` (`--dr004-*`)
- Results across the three regression windows (tagged runs): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_004__EXPERIMENT__RESULTS.md`
- Decision (current): **keep off by default** (v0.2) until Play Card policy is stabilized (DR‑004 can improve union, but may reshuffle top‑budget play cards).

Key takeaways (what DR is actually good at; how to consume it without “circles”):
- DR’s repeatable value is **digit-pool / envelope convergence**, not “best_pattern top‑3” calling (winners often show up in trace/overlay while top candidates miss).
- Strong pools tend to show **repeat support across multiple trace lanes** (boxes/cols/sets), plus **early arrival + persistence** in the reduction steps.
- **Cross‑variant convergence** (Midday + Evening) is a high-signal differentiator; treat Combined as a mild boost, not a requirement.
- **VTRAC index compression** is useful as a bounded gateway lens, but can raise `index_only`; treat index packs as *corroboration*, not “box it all”.
- Recency overlap penalty did not show clear lift in the v0 windows; keep it optional until evidence shows otherwise.
- If DR‑004 is allowed to directly compete in Play Card budgets, it can reshuffle ranks; a safer next step is “consume DR‑004 only when corroborated” (or when incremental lift is demonstrated).
- Next work is measurement-first: incremental contribution report + per-day “signals export” + 10-case alignment report, then only ship new DR‑004 features that pass gates.
- v3 pool-filter knobs (`unique_digits=2→4`) materially improve the **10-case signal alignment** (cluster visibility), but did not beat `dr004_v1` on Candidate Universe union lift; treat as **signals-lens** until it earns selection-layer gates:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_004__ALIGNMENT_REPORT__u2u4.md`

### Follow-up (v0.2 additive; default-off): bulk signals export + DR‑004 fusion gate

- Implemented a predictive-safe **signals bundle** export (so DR-only strong environments are never “lost” just because budgets/fusion don’t fire):
  - `scripts/tools/create_candidate_universe.py` (`--write-signals-bundle`)
  - Output: `sharepacks/<root>/<D>/<STATE>/signals_bundle__<profile>__<tag>.json`
  - Contents (all evidence-only / no winners leakage): DR‑004 trace pools + canonicals + indices, Stable top canonicals, Hot Zones top triads, VTRAC Enhanced top indices/straights, Aux shortlist + overdue indices.
- Implemented a bounded, additive **fusion gate** micro-pack that fires only on DR‑004 index convergence with other tool signals:
  - `scripts/tools/create_candidate_universe.py` (`--fusion-gate-boxed-canonicals`, `--fusion-gate-min-sources`)
  - New `method_id=fusion_gate_dr004` packs (one per section; small BOX expansion).
  - Containment: excluded from pooled digit envelope (prevents silent perturbation of derived combo packs while measuring).
- Measured on the 3 v0 windows (baseline tag `baseline_ref_20260121` → experiment `dr004_fusion_v2_u2u4`):
  - Incremental report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__from_baseline_ref_20260121__to_dr004_fusion_v2_u2u4.md`
  - Current result: +1 incremental union hit, 0 regressions, +~8.8 avg union cost → keep fusion gate off by default.

---

## 2026‑01‑21 — Aux + Control Center: Due Doubles parity + Badge Pressure harness (implemented)

Motivation:
- Doubles/mirror-doubles are a major “environment class” in the corpus, so it’s easy to misread low raw Due Doubles board hit counts as a data bug.
- The missing superbrain lever on the Aux side is not “more raw candidates”; it’s turning the boxed badge-matrix density into a **compact, compoundable index pressure signal**.

### A) Due Doubles parity audit (reporting-only; correctness + interpretation)

What we checked:
- Recompute `Draws Since Double` directly from the sharepack-local Aux draw snapshots and compare to Control Center exports.
- Validate family cell token parsing and combo membership (only known VTRAC double combos; severity thresholds consistent).
- Report **conditional** performance (only meaningful on double/triple winners) and a “most due DS → next-day double event” diagnostic.

Script:
- `scripts/tools/due_doubles_parity_audit.py`

Outputs (v0 windows):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2025-06-21_to_2025-06-23.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2025-12-30_to_2026-01-04.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2026-01-05_to_2026-01-09.md` (and `.csv`)

Key result:
- Parity is clean on the audited windows (DS mismatches = 0; token/label/threshold issues = 0). The board is not “broken”; the low unconditional hit rate is an interpretation/conditioning issue.

### B) Aux badge pressure harness (Index Pressure Contract; reporting-only)

What we built:
- A compact per-index contract from the Aux badge-matrix logic (pair colors + RC/BS combo badges), aggregated to:
  - `(state_key, variant, vtrac_index)` → pressure counts + `pressure_score` and `pressure_density`.
- A window harness that compares:
  - TopK indices by “overdue DS” (baseline) vs TopK by “badge pressure” (new signal),
  - plus a strict cross-variant intersection (Midday ∩ Evening).

Script:
- `scripts/tools/aux_badge_pressure_harness.py`

Outputs (v0 windows):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
- Index contract (large CSV, for pivoting): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__INDEX_STATS__<A>_to_<B>.csv`

Key result:
- Badge pressure TopK meaningfully outperforms “overdue DS” TopK on multiple windows (especially Evening), which justifies treating badge density as the next compounding signal in v0.2 scoring.

### C) Predictive-safe signals export (no defaults changed)

Change:
- Extended the `signals_bundle_v1` export to include `tools.aux_badge_pressure` (topK indices per variant + Midday∩Evening intersection), sourced only from sharepack-local `aux/draws/*_draws.csv`.
- This does **not** change Candidate Universe packs or Play Cards by default; it only enriches the per-state evidence bundle when `--write-signals-bundle` is enabled.

Code:
- `scripts/tools/create_candidate_universe.py` (`--write-signals-bundle`)

---

## 2026‑01‑21 — v0.2 Closeout: coverage ledger + portal link audit + superbrain config harness (implemented + measured)

Motivation:
- Context resets were repeatedly causing “did we miss something?” loops.
- We needed a mechanical way to (a) prove v0.2 coverage and (b) measure triage/ranking policies using both `hit_any` and `box_hit` without touching analyzers.

### A) v0.2 coverage ledger (generated; completeness proof)

What it does:
- Enumerates every `GOLD-####` entry + every dated v0.2 integration-log block.
- Extracts evidence refs and reports whether referenced repo artifacts exist.

Script:
- `scripts/tools/build_v0_2_coverage_ledger.py`

Output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__COVERAGE_LEDGER.md`

### B) Portal link audit (generated; navigation integrity)

What it does:
- Audits the RUNS portal + v0.2 integration log for broken repo-local links (docs/scripts/sharepacks/data paths).
- Ignores placeholders (e.g., `<D>`, wildcards) to avoid false positives.

Script:
- `scripts/tools/audit_v0_2_portal_links.py`

Output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__PORTAL_LINK_AUDIT.md`

### C) Superbrain config harness (Brain‑2 triage/ranking policies)

What it does:
- Compares cross-state Top‑N ranking policies across a window (baseline tool-first vs “pressure tiebreak”).
- Grades the Top‑N set using:
  - Candidate Universe union `hit_any` and `box_hit` (lane visibility),
  - Play Card `hit_any`/`box_hit` for a chosen strategy (default: `play_box_first/B12`).
- Uses Aux badge pressure index stats as the pressure signal source (predictive-safe; winners used only for grading).

Script:
- `scripts/tools/superbrain_config_harness.py`

Outputs (v0 windows):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_CONFIG__HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_CONFIG__HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_CONFIG__HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)

Key result:
- Badge pressure as a **tie-breaker** can help in some windows and hurt in others. That’s the desired outcome of v0.2: we can now measure the trade-off explicitly and decide whether pressure becomes a default ranking lever or remains a research-only knob.

---

## 2026‑01‑22 — Play Card: “perm-hit” metric + bounded conditional conversion (implemented + measured)

Motivation:
- We repeatedly saw “lane is present, but B12 doesn’t convert” frustration.
- The missing measurement was: *did we at least include the winner’s canonical (any permutation), even when we didn’t include the exact straight?*
- The missing selection lever was: *a bounded (1–2 lines at B12) conversion policy that can compete with box-first without the blunt always-on reservation of `conversion_box_first`.*

### A) New grading metric: `canon_hit_any_perm` (“perm-hit”)

Change:
- Added `canon_hit_any_perm` to Play Card grading output (reported as `perm_hit` in rollups).
- Rollups now display: `hit_any` (straight), `perm_hit` (canonical present), `closure_hit` (box hit), `vtrac_hit`.

Code:
- `scripts/tools/grade_play_card.py`
- `scripts/tools/rollup_play_card_corpus.py`

Baseline rollup (updated columns):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only.md`

### B) New Play Card strategies: conditional conversion (lenient/strict) + lane presets (A/B)

Change:
- Added 4 strategies (emitted directly as strategies, not CLI flags):
  - `conversion_box_first_conditional_lenient_presetA`
  - `conversion_box_first_conditional_lenient_presetB`
  - `conversion_box_first_conditional_strict_presetA`
  - `conversion_box_first_conditional_strict_presetB`
- Presets:
  - `presetA`: existing “lane methods”
  - `presetB`: `presetA` + `{R-perm-4, PackA_vt8, PackB_mirror3rd}` (conversion fuel ablation)
- Bounded conversion reservation (only from Candidate Universe; no new combos invented):
  - lenient: `B12=1`, `B24=2`, `B36=4`
  - strict: `B12=2`, `B24=4`, `B36=6`

Code:
- `scripts/tools/create_play_card.py`

Diagnostics:
- Each conditional card records a `conversion_gate` snapshot (top convergence stats + closure strength).

### C) Measurement (3 windows, `tool_only`, experiment-tagged)

Artifacts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__condconv_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__condconv_v3.md`

Key results:
- `condconv_v2`: gate never fired (closure test too strict), so conditional strategies collapsed to `convergence_box_first`.
- `condconv_v3`: gate fires in most environments and produces measurable deltas:
  - B12 (overall): `conversion_box_first_conditional_lenient_*` matched `play_box_first` on `hit_any`, while materially increasing `perm_hit` (lane visibility).
  - Strict variants tended to regress `hit_any` at B12 and are not recommended as defaults.

Current posture (v0.2):
- Keep these conditional-conversion strategies as experiment-tagged levers (default-off).
- Portfolio/default selection is now budget-split (see `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`):
  - B12: `analysis_prefix`
  - B24/B36: `vtrac_pack_boxed_first`

---

## 2026‑01‑22 — “0% hit” incident: clarify semantics + add windowed grading (aligned to training’s 2–5 draws)

Observed issue:
- A “0% hit rate” report triggered a crisis review.

Root cause:
- The “0%” was **not** Play Card hit rate — it was the `condconv_v2` **conversion gate fire rate**, which was 0% because the gate was too strict.
- Separately, training docs explicitly frame success as “hit within 2–5 draws”, so same-draw grading alone can look “dead” even when the lane is present.

### A) Add two explicit “hit-any” semantics (strict vs box vs inclusive)

Change:
- Extend Play Card grading to compute two additional derived hit metrics:
  - `hit_any_box`: (`straight_hit` OR `canon_hit_any_perm`)
  - `hit_any_inclusive`: (`straight_hit` OR `canon_hit_any_perm` OR `vtrac_index_hit`)
- Keep existing `hit_any` as “strict”: (`straight_hit` OR `closure_hit`).

Code:
- `scripts/tools/grade_play_card.py`
- `scripts/tools/rollup_play_card_corpus.py`

Why it matters:
- This makes the “lane present vs closure purchased vs straight hit” distinction explicit, so we stop talking past each other when reviewing rollups.

### B) New harness: Play Card windowed grading (N draws)

Change:
- Add a windowed grader to evaluate: “if we replayed the Play Card across the next N draw-slots (Midday/Evening), did it hit?”
- Default is `N=5` to match training’s “2–5 draws” framing.

Code:
- `scripts/tools/grade_play_card_windowed.py`

Outputs (examples):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v3__N5.md` (+ `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v3__N5.md` (+ `.csv`)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PLAY_CARD_WINDOWED_GRADE__tool_only__condconv_v3__N5.md` (+ `.csv`)

Key observation:
- Windowed `hit_any_inclusive` is **~0.66–0.80** in the gold windows, which is far closer to the training expectation (high hit probability within 5 draws) than same-draw `hit_any`.
- Windowed strict/box conversion still lags — reinforcing that the tools are often right about the **lane**, and the remaining lift is in **bounded conversion policies** that don’t explode cost.

### C) Retune conditional conversion gate (condconv_v4) + decouple input CU from output tag

Change:
- Add `--input-experiment-tag` to `create_play_card.py` so selection-only experiments can read baseline Candidate Universe while writing tagged Play Cards.
- Retune the conditional conversion gate to **not** be “always-on” (lower fire rate vs `condconv_v3`).

Code:
- `scripts/tools/create_play_card.py`

Artifacts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__condconv_v4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__condconv_v4__N5__2025-12-30_to_2026-01-04.md` (and other windows)

Conclusion:
- `condconv_v4` successfully lowers gate fire rate, but does **not** consistently improve conversion metrics over `condconv_v3` yet.
- Next likely lever (training-aligned): add a Play Card strategy that explicitly targets the “8 VTRAC combinations” set (v‑code 8‑pack) as a bounded conversion pack, rather than relying on closure-first heuristics.

---

## 2026‑01‑22 — Play Card: VTRAC boxed-member pack strategies (vtracpack_v1) (implemented + measured)

Motivation:
- Training repeatedly frames a “small boxed VTRAC pack” as a high-leverage conversion move (usually 8 for singles; fewer for doubles/triples-like groups).
- We want to convert a lane/index signal into the **exact boxed-member pack** (not the full straight closure) without touching analyzers.

### A) New Play Card strategies: `vtrac_pack_boxed_only` + `vtrac_pack_boxed_first`

Change:
- Added two experiment-only strategies:
  - `vtrac_pack_boxed_only`: play the chosen boxed-member pack, then fill remaining lines from score-ranked candidates.
  - `vtrac_pack_boxed_first`: play the chosen boxed-member pack, then fill remaining lines by convergence ranking.

How it works (key semantics):
- Chooses exactly one VTRAC numeric index (“lane”) by aggregating Candidate Universe evidence across top-ranked candidates (union support across methods/variants + strength).
- Emits the boxed-member pack from `modules.vtrac_reference.VTRAC_DISPLAY`:
  - This is the **boxed-member pack** (≤8 lines; often fewer for doubles), not the straight-line closure returned by `get_index_set`.
- Each Play Card stores a `vtrac_pack` diagnostics blob (chosen index + pack combos + chooser snapshot), and `play_card.md` prints it for audit.

Code:
- `scripts/tools/create_play_card.py`

### B) Measurement (3 windows, `tool_only`, `--input-experiment-tag -`)

Artifacts:
- Same-day rollup:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__vtracpack_v1.md` (+ `.csv`)
- Windowed rollups (N=5):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2026-01-05_to_2026-01-09.md`

Key results (windowed N=5; “hit_any_inclusive”):
- `vtrac_pack_boxed_first` materially improves conversion at higher budgets without exploding cost:
  - 2025‑12‑30→2026‑01‑04: `B36` inclusive ≈ `0.8810` (vs `analysis_prefix` ≈ `0.7976`)
  - 2025‑06‑21→2025‑06‑23: `B36` inclusive ≈ `0.8810` (vs `analysis_prefix` ≈ `0.6667`)
- At `B12`, inclusive rates are comparable to `analysis_prefix`, but `hit_any_box` improves in both post-results windows (more canonical “lane present” capture).

Interpretation:
- This is the first selection-layer change that directly implements the training’s “boxed-member pack” move and shows a strong, repeatable lift in windowed outcomes (especially B24/B36).

### C) Winners-linked study queues (post-results windows only)

Script:
- `scripts/tools/build_play_card_vtrac_pack_study_queue.py`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__VTRAC_PACK_STUDY_QUEUE__vtracpack_v1__N5.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__VTRAC_PACK_STUDY_QUEUE__vtracpack_v1__N5.md`

Next iteration lever (if needed):
- If we want the pack to be a **purer** “one-lane bet” (less influenced by non-lane fill lines), consider a stricter `vtrac_pack_*` variant that constrains filler to the chosen index (or logs “hit came from pack vs hit came from filler” as a separate diagnostic metric).

### D) Pack vs filler diagnostics (implemented; reduces “did we win via filler luck?” ambiguity)

Change:
- Extend Play Card grading + windowed grading to report whether the *pack subset* itself hit vs the *filler subset*.
- This is emitted as additional columns in the grade CSVs and surfaced in the rollups.

Code:
- `scripts/tools/grade_play_card.py` (adds `pack_hit_any_inclusive`, `pack_only_hit_any_inclusive`, etc.)
- `scripts/tools/rollup_play_card_corpus.py` (adds rollup columns: `pack_hit`, `pack_only`, `filler_hit`, `pack_idx_hit`, `avg_pack`)
- `scripts/tools/grade_play_card_windowed.py` (adds windowed rollup columns: `pack_hit`, `pack_only`, `filler_hit`)

Where to look:
- Same-day: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__vtracpack_v1.md`
- Windowed N=5 (per window):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2026-01-05_to_2026-01-09.md`

Interpretation (quick):
- `pack_hit`: pack hits at least once (within the grading horizon).
- `pack_only`: pack hits in cases where filler does **not** (unique pack contribution).

---

## 2026‑01‑22 — VTRAC pack chooser ablation: lane‑methods‑only (vtracpack_v2) (implemented + measured)

Motivation:
- We observed that the v1 index chooser aggregates evidence across *all* supporting methods, which can bias the chosen lane toward high-volume “non-lane” sources.
- Hypothesis: choosing the VTRAC index using *lane-method-only evidence* increases `pack_hit` / `pack_only` and makes the pack more “real”, even under tight budgets.

Change:
- Add two ablation strategies that select the index using only the lane-method presetB set (`vtrac_top/hot_zones/aux overdue/mirror closure + {R-perm-4, PackA_vt8, PackB_mirror3rd}`):
  - `vtrac_pack_boxed_first_laneonly_presetB`
  - `vtrac_pack_boxed_only_laneonly_presetB`

Code:
- `scripts/tools/create_play_card.py`

Artifacts:
- Same-day rollup: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__vtracpack_v2.md`
- Windowed rollups (N=5):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v2__N5__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v2__N5__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v2__N5__2026-01-05_to_2026-01-09.md`

Key findings:
- Lane-only chooser increases `pack_hit` / `pack_only` in some windows (the pack becomes more directly responsible for hits),
  but it does **not** improve `hit_any_inclusive_window` consistently; in the 2025‑12‑30→2026‑01‑04 window it regresses B12/B24.

Decision (v0.2 posture):
- Keep lane-only chooser as a **research knob** for study queues / diagnostics.
- Continue to treat `vtrac_pack_boxed_first` (v1 chooser) as the leading B24/B36 conversion-friendly policy.

---

## 2026‑01‑22 — Play Card: encode v0.2 budget‑split defaults as a single strategy + B12 pack-gate ablation (v0_2_default_v1) (implemented + measured)

Motivation:
- The v0.2 posture is explicitly **budget-split** (B12 conservative, B24/B36 conversion-friendly), but the Play Card artifact emits multiple strategies and requires a manual mapping.
- Encode the posture as a single named strategy to reduce drift and make “what to play” review simpler.
- Also test (and then either adopt or discard) the tempting idea: “at B12, insert a boxed-member VTRAC pack only when the chosen index looks dominant.”

### A) New strategies emitted in `play_card*.json`

Change:
- Add three convenience strategies:
  - `v0_2_default`: `B12=analysis_prefix`, `B24/B36=vtrac_pack_boxed_first`
  - `v0_2_default_b12pack_lenient`: same as `v0_2_default`, but B12 *may* insert a VTRAC pack under a lenient dominance gate
  - `v0_2_default_b12pack_strict`: same as above, but stricter gate

Code:
- `scripts/tools/create_play_card.py`

### B) Measurement (3 windows, N=5; mixed sharepacks roots)

Notes:
- Windows 1–2 used `sharepacks/` (Candidate Universe present in those day sharepacks).
- Window 3 used `sharepacks/_predictive/` (those predictive packs contain Candidate Universe + Play Cards).

Artifacts:
- Same-day rollup:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__v0_2_default_v1.md`
- Windowed rollups (N=5):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2026-01-05_to_2026-01-09.md`

Key findings (windowed N=5; “hit_any_inclusive”):
- `v0_2_default` exactly reproduces the intended posture:
  - B12 matches `analysis_prefix`
  - B24/B36 match `vtrac_pack_boxed_first` (material lift vs `analysis_prefix` in the first two windows; see the rollups above).
- The B12 pack-gated variants **do not** improve `hit_any_inclusive_window` consistently (they usually regress it vs `analysis_prefix`), because they concentrate coverage into one lane under a tight budget.

Decision (v0.2 posture):
- Keep `v0_2_default` as a convenience strategy (reduces policy drift).
- Keep `v0_2_default_b12pack_*` as research-only; do not adopt as B12 default.

---

## 2026‑01‑22 — v0.3 cadence wrapper + portfolio tag preference (implemented)

Motivation:
- Reduce drift/cognitive load: encode the “predictive day → candidate universe → play cards → portfolio” cadence into one wrapper.
- Preserve auditability: write a lightweight RUNS receipt so a run can be reproduced without chat history.
- Enable experiments: allow the portfolio report to prefer a tagged `play_card*.json` when running strategy experiments.

Changes:
- Add cadence wrapper (pre + post):
  - `scripts/tools/run_v0_3_cycle.py`
- Add portfolio option to prefer tagged play cards:
  - `scripts/tools/create_predictive_portfolio_report.py` (`--prefer-experiment-tags`)

Docs:
- Defaults + workflow pointers:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Predictive_Workflow_V0_2_Addendum.md`
