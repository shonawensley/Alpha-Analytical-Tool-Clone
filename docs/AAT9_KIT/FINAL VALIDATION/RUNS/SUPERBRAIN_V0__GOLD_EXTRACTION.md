# SUPERBRAIN v0 — Gold Extraction Ledger (Synthesis, Not New Runs)

Purpose: stop “run churn” and extract the highest-value, repeatable insights (“gold”) from the existing Master Validation + Predictive corpus, without touching analyzers or contaminating timelines.

This is the document to read when you feel “we have 70+ reports and no clarity”.

---

## Non‑negotiables (keep us out of overfit + drift)

- **Do not change analyzers** (Stable / Digit Reduction / VTRAC / Hot Zones) during v0 synthesis.
- **Do not touch combined-table extraction/readers** unless explicitly scoped.
- **Predictive (“before”) stays winners‑free**: `sharepacks/_predictive/<D>/...`
- **Post-results (“after”) stays immutable SSOT**: `sharepacks/<D>/...`
- **Quarantine Profit Alerts via ablation**, do not delete while we’re still learning what they do.

---

## Where to start (the minimal “open these files” map)

- Navigation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- What exists/filled: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Fix-now vs fix-later: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/POST_RUNS_TRIAGE.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Predictive grading rollups:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup.md`
- Doubles deep dive:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`

---

## v0 corpus windows (already grouped; these are our “messy colleague” buckets)

- 3‑day starter: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`
- 6‑day expansion: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
- 5‑day Jan window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_SYNTHESIS.md`

Each window also has a Codex-authored synthesis:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CODEX_DEEP_ANALYSIS.md`

---

## What “Superbrain” is right now (so the project feels coherent)

Today’s system is intentionally split into layers:

1) **Evidence layers** (truth):
- Master Validation “after”: `sharepacks/<D>/<STATE>/...` + RUNS state reports `docs/.../RUNS/<D>__<STATE>.md`
- Predictive “before”: `sharepacks/_predictive/<D>/<STATE>/...` (no winners)

2) **Gradeable prediction substrate** (the missing bridge we added):
- Candidate Universe (broad playset): `sharepacks/_predictive/<D>/<STATE>/candidate_universe*.json`
- Play Cards (budgeted cut for controlled experiments): `sharepacks/_predictive/<D>/<STATE>/play_card*.json`
- Grading is written only to RUNS (keeps predictive packs immutable):
  - `docs/.../RUNS/<D>__CANDIDATE_UNIVERSE_GRADE*.{md,csv}`
  - `docs/.../RUNS/<D>__PLAY_CARD_GRADE*.{md,csv}`

3) **Cross‑state triage** (competition-friendly surfaces):
- `docs/.../RUNS/<D>__PREDICTIVE_PORTFOLIO*.md`

The “superbrain” is not a learned model yet; it’s a **gradeable evidence→packs→grades pipeline** that produces the dataset we need to learn weights later.

---

## Profit Alerts quarantine (ablation, not vibes)

We now measure whether Profit Alerts help or pollute using profile variants:
- `mixed`: current behavior (includes Profit Alerts packs)
- `tool_only`: excludes Profit Alerts packs
- `profit_only`: Profit Alerts packs only

Sprint spec + commands live here:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`

### v0 Jan window results (2026‑01‑05 → 2026‑01‑09)

Candidate Universe union hit rates (higher is “more likely the playset contains the winner”, not “better picks”):
- `mixed`: Evening `hit_any=0.2174`, Midday `hit_any=0.2609`
- `tool_only`: Evening `hit_any=0.2029`, Midday `hit_any=0.2609`
- `profit_only`: Evening `hit_any=0.0145`, Midday `hit_any=0.0145`

Play Card hit rates (budgeted experiments; more relevant to “what would we actually play”):
- `mixed`: best Evening `hit_any=0.0435`, best Midday `hit_any=0.0725`
- `tool_only`: best Evening `hit_any=0.0435`, best Midday `hit_any=0.0725`
- `profit_only`: best Evening `hit_any=0.0145`, best Midday `hit_any=0.0145`

Interpretation (v0 only):
- Profit Alerts alone are extremely weak in this window.
- Tool-only matches mixed for Play Cards, and is only slightly lower for Candidate Universe union.
- This strongly supports your instinct to quarantine: **Profit Alerts should not dominate selection** until they prove incremental value over tool evidence on larger windows.

---

## Tool roles (v0 posture; do not treat as “tuning rules” yet)

From the Jan window synthesis:
- Stable families present: **~97%** of outcomes
- Hot Zones present: **~98%** of outcomes
- VTRAC winner index in top10: **~25%**
- DR strict “top candidates contain winner”: **~3–4%**
- Winner has repeat/mirror VTRAC signature: **~54%**

Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CODEX_DEEP_ANALYSIS.md`

Working interpretation (v0):
- **Stable / Hot Zones** are broad structure lenses (high coverage; great for environment classification + convergence).
- **VTRAC** is a structure narrator / grouping key (often the cleanest family hedge when things are noisy).
- **Digit Reduction** is not behaving like a reliable “final-candidate picker” in this window; it behaves more like an **envelope/lane lens**. v0 action is to adjust how we *consume* DR in Candidate Universe / Play Cards before changing the analyzer.
- **Aux** is the compounding pressure layer (positional, due doubles, pairs, index pressure). It’s especially relevant for “lane hit → box hit conversion” strategies.

---

## How we capture “gold” (so nothing gets lost)

The core rule: if it matters, it must land in this ledger as an **evidence-linked entry** (not just in chat or scattered task notes).

Capture rules:
- Each entry must include concrete file pointers (run report + predictive artifacts + the deep-dive line pointer when available).
- Each entry gets a stable ID (`GOLD-0001`, `GOLD-0002`, …) so we can reference it from other docs without ambiguity.
- If an entry is actually a pipeline issue (missing artifacts, drift, schema bug), log it to `FIX_NOW_LEDGER.md` or `FIX_LATER_INDEX.md` and reference that here.

### Entry template (copy/paste)

- **GOLD-####** — `<D> <STATE> <Period>` — winner `<literal>` (canon `<canon>`, idx `<idx>`, mirrorpair `<pair>`)
  - Type: `double | mirror_double | triple | other`
  - Baseline (profile=`tool_only`): CU `index_hit=? box_hit=?`; PlayCard `hit_any=?` (note budget)
  - Evidence:
    - Deep dive: `<path:line>`
    - Run report: `<path>`
    - Predictive CU: `<path>`
    - Predictive Play Card: `<path>`
    - Winners digest: `<path>`
  - Primitives (tags): `double_pressure`, `due_doubles`, `mirror_echo`, `r_consensus_tail`, `vstraight_lane`, `hotzones_star`, `aux_pairs`, …
  - Hypothesis (1 sentence): why this was “lane hit → box miss” (or why it worked)
  - Action (bounded): what closure / consumption rule would convert it (or what to keep doing)

---

## Doubles + mirror-doubles (what the corpus says, and why you’re right to care)

Inventory over the current gold-day corpus:
- doubles: `104`
- mirror_doubles: `83`
- triples: `3`
- Most common mirror pairs: `1/6`, `2/7`, `3/8`, `4/9`, `0/5`

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`

Key audit finding:
- Control Center “due doubles DS” vs Aux “ds_since_double” deltas are **0** in the deep-dive scan (good alignment; no silent drift).
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md`

Most actionable learning target:
- **Index hit → box miss** mirror-double events (Candidate Universe hits the VTRAC lane but misses the exact box).
- These are the best examples for designing bounded closure packs that convert “lane correctness” into “box correctness” without analyzer tuning.
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`

---

## “Gold” study queue (read these before reading 70 reports)

10–20 examples is enough to produce v0.1 hypotheses without drowning.

Start with convergence cases (cross-tool alignment):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`

Then read the top doubles/mirror-double “index hit → box miss” cases:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`

For each picked row:
1) Open the Master Validation report: `docs/.../RUNS/<D>__<STATE>.md`
2) Open the winners digest: `docs/.../RUNS/<D>__WINNERS_DIGEST.md`
3) Open the predictive artifacts (if present):
   - `sharepacks/_predictive/<D>/<STATE>/candidate_universe*.json`
   - `sharepacks/_predictive/<D>/<STATE>/play_card*.json`

---

## v0.1 output target (what “progress” looks like next)

Without touching analyzers, v0.1 should deliver:

1) A stable default “competition mode” that does not depend on Profit Alerts:
- Use `--profile tool_only` for Candidate Universe / Play Cards / Portfolio.

2) A clearer state-vs-state “strength” ranking that is evidence-based:
- Prefer “boundedness + convergence” signals (small playsets + multi-method support), not just alert count.

3) One updated “Superbrain primitives” entry per synthesis batch:
- Append to `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`

4) A decision about whether Profit Alerts stay quarantined, get reworked, or get removed from default surfaces:
- Based on rollups across larger windows, not one day or one competition.

---

## Gold entries (v0) — in progress

These are the first “concrete gold” entries extracted from the doubles/mirror-doubles study queue. Expect this section to grow as we work the queue.

- **GOLD-0001** — `2026-01-09 Delaware4 Evening` — winner `681` (canon `168`, idx `18`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2537`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Delaware4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/Delaware4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx18`, `hot_zones_top_index`, `wl_family_dense(col1/2)`
  - Hypothesis: we correctly surfaced the **index/lane**, but the budgeted Play Card didn’t allocate any coverage to the “right canonical inside the lane”.
  - Action (bounded): add/strengthen an “index→box conversion” rule in Play Cards (e.g., reserve 1–2 BOX canonicals from each top index pack, or promote mirror-pair closure canonicals when present).

- **GOLD-0002** — `2026-01-07 NewJersey4 Midday` — winner `361` (canon `136`, idx `18`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2135`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewJersey4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/NewJersey4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx18`, `mirror_pair_closure`, `wl_vt_straight_dense(col1/2)`
  - Hypothesis: mirror-pair structure was “visible” (lane hit), but our bounded selection didn’t carry the winning canonical `136` (classic lane-hit → box-miss failure).
  - Action (bounded): treat `mirror_pair_closure` packs as first-class for mirror-double days and ensure the Play Card always includes at least 1 canonical from that closure when it fires.

- **GOLD-0003** — `2026-01-08 Florida4 Midday` — winner `429` (canon `249`, idx `31`, mirrorpair `4/9`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2337`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Florida4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-08/Florida4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(4/9)`, `vtrac_idx31`, `stable_top_index`, `wl_family+winner_dense(col1/2)`
  - Hypothesis: Stable/Hot structure caught the family strongly, but the budget cut still missed the exact canonical in the same index.
  - Action (bounded): when a tool-driven index pack is strong (Stable/Hot Zones), include a tiny “index slice” (top 1–2 canonicals) rather than only non-index doubles plays.

- **GOLD-0004** — `2026-01-05 PuertoRico4 Evening` — winner `972` (canon `279`, idx `28`, mirrorpair `2/7`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1767`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PuertoRico4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-05/PuertoRico4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(2/7)`, `vtrac_idx28`, `cc_due_doubles_ds=8`, `wl_family_dense(col1/2)`, `wl_vt_straight_present(col1/2)`, `dr_analyzer_v2_index_hit`
  - Hypothesis: we got the right **index**, but the budgeted boxed-first selection never allocated any canonicals from idx28 (lane-correct → box-miss via budget policy).
  - Action (bounded): when `CU index_hit=True` and `wl_family_cells>=10`, force-include 1 BOX canonical from the top hitting index (an “index slice” slot).

- **GOLD-0005** — `2026-01-05 SouthCarolina4 Evening` — winner `712` (canon `127`, idx `20`, mirrorpair `2/7`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1801`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__SouthCarolina4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-05/SouthCarolina4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(2/7)`, `vtrac_idx20`, `cc_due_doubles_ds=4`, `wl_family_dense(col1/2)`, `wl_vt_straight_dense(col1/2)`
  - Hypothesis: strong winners-lens lane structure (family + vt-straight cells) but no boxed-first closure into the winning canonical.
  - Action (bounded): treat “vt-straight dense + mirror_pair present” as a trigger to include 1 BOX canonical from that index even if it isn’t a due-double.

- **GOLD-0006** — `2026-01-06 NewJersey4 Evening` — winner `942` (canon `249`, idx `31`, mirrorpair `4/9`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1936`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-06/NewJersey4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(4/9)`, `vtrac_idx31`, `wl_winner_cells(col1/2)>0`, `hz_top20pct`, `dr_best_area<=3`
  - Hypothesis: the system was “rail-correct” (idx31), but our bounded boxed-first selection didn’t carry any idx31 canonicals.
  - Action (bounded): if any pack produces `vtrac_index_hit`, reserve a small portion of the budget for **index representative canonicals** (1–2) instead of only double-family boxes.

- **GOLD-0007** — `2026-01-09 Virginia4 Midday` — winner `380` (canon `038`, idx `13`, mirrorpair `3/8`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2772`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Virginia4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/Virginia4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(3/8)`, `vtrac_idx13`, `wl_silent(col1/2)`
  - Hypothesis: this looks like a **low-evidence lane hit** (winners lens shows no family/winner/vt-straight presence in Set1 col1/2), so “idx hit” may be coincidental.
  - Action (bounded): do not tune on this class; tag as `low_signal_lane_hit` and exclude from closure-rule design unless corroborated by convergence cases.

- **GOLD-0008** — `2026-01-08 Connecticut4 Midday` — winner `106` (canon `016`, idx `6`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2321`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Connecticut4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-08/Connecticut4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx6`, `wl_silent(col1/2)`
  - Hypothesis: same low-signal pattern as GOLD-0007 (winners lens is effectively silent).
  - Action (bounded): treat as `low_signal_lane_hit` and do not use it to justify adding broader closures.

- **GOLD-0009** — `2026-01-08 PuertoRico4 Evening` — winner `479` (canon `479`, idx `31`, mirrorpair `4/9`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2504`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PuertoRico4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-08/PuertoRico4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(4/9)`, `vtrac_idx31`, `wl_silent(col1/2)`
  - Hypothesis: no winners-lens corroboration (including `ls_box=0`), so this is a poor closure-design example.
  - Action (bounded): exclude from closure-rule design; keep only as “false-positive lane hit” reference.

- **GOLD-0010** — `2026-01-07 Connecticut4 Midday` — winner `156` (canon `156`, idx `6`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2053`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Connecticut4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/Connecticut4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx6`, `wl_silent(col1/2)`
  - Hypothesis: winners lens doesn’t corroborate the lane structurally; treat as low-signal.
  - Action (bounded): exclude from closure-rule design.

- **GOLD-0011** — `2026-01-07 Indiana4 Midday` — winner `823` (canon `238`, idx `29`, mirrorpair `3/8`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2102`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Indiana4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/Indiana4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(3/8)`, `vtrac_idx29`, `wl_silent(col1/2)`
  - Hypothesis: low-evidence lane hit.
  - Action (bounded): exclude from closure-rule design.

- **GOLD-0012** — `2026-01-06 Florida4 Evening` — winner `160` (canon `016`, idx `6`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1886`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Florida4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-06/Florida4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-06/Florida4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx6`, `wl_silent(col1/2)`
  - Hypothesis: low-evidence lane hit.
  - Action (bounded): exclude from closure-rule design.

- **GOLD-0013** — `2026-01-06 Indiana4 Evening` — winner `961` (canon `169`, idx `19`, mirrorpair `1/6`)
  - Type: `mirror_double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1902`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Indiana4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-06/Indiana4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__WINNERS_DIGEST.md`
  - Primitives (tags): `mirror_pair(1/6)`, `vtrac_idx19`, `wl_silent(col1/2)`
  - Hypothesis: low-evidence lane hit.
  - Action (bounded): exclude from closure-rule design.

- **GOLD-0014** — `2026-01-05 NewYork4 Midday` — winner `080` (canon `008`, idx `4`, mirrorpair ``)
  - Type: `double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `hit_any=True box_hit=True index_hit=True`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1649`
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:9`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__WINNERS_DIGEST.md`
  - Primitives (tags): `consensus_double_9`, `due_doubles`, `wl_family_dense(col1/2)`, `xvar_winner_present`
  - Hypothesis: this is a clean “convergence → cheap boxed hit” case (the closure methods that seed doubles can convert to box).
  - Action (bounded): keep `consensus_double_9` + due-doubles mirror packs as first-class in v0.2 play-box-first selection.

- **GOLD-0015** — `2026-01-07 Florida4 Midday` — winner `434` (canon `344`, idx `34`, mirrorpair ``)
  - Type: `double`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Deep dive: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2085`
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:11`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/Florida4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `stable_top10pct`, `hz_top20pct`, `vtrac_top10`, `dr_best_area<=3`, `wl_winner_dense(col1/2)`
  - Hypothesis: extreme evidence density but the `stable_top`/boxed ingestion didn’t carry canonical `344` into Candidate Universe.
  - Action (bounded): extend `stable_top` pack generation to include **top boxed canonicals from stable_scores.csv** (variant-specific), not only compound/family summaries.

- **GOLD-0016** — `2026-01-07 Florida4 Evening` — winner `963` (canon `369`, idx `24`, mirrorpair ``)
  - Type: `other`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `index_hit=True box_hit=False`
  - Evidence:
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:12`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/Florida4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `stable_top10pct`, `hz_top20pct`, `vtrac_top10`, `dr_best_area<=3`
  - Hypothesis: Candidate Universe contained the winner, but boxed-first budget allocation skipped the best non-double canonical.
  - Action (bounded): add a “non-double convergence slot” (1 BOX canonical) when convergence score is 4/4, even if doubles are present.

- **GOLD-0017** — `2026-01-09 Pennsylvania4 Evening` — winner `014` (canon `014`, idx `9`, mirrorpair ``)
  - Type: `other`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `index_hit=True box_hit=False`
  - Evidence:
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:13`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Pennsylvania4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/Pennsylvania4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `BA_contains`, `stable_top10pct`, `hz_top20pct`, `vtrac_top10`, `dr_best_area<=3`
  - Hypothesis: Candidate Universe had a box hit, but boxed-first budget allocation didn’t surface it.
  - Action (bounded): when `BA_contains=1` and convergence score is 4/4, reserve 1 box slot for a BA-supported canonical.

- **GOLD-0018** — `2026-01-09 NewJersey4 Evening` — winner `028` (canon `028`, idx `11`, mirrorpair ``)
  - Type: `other`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:10`
    - Stable shows 028 strongly (predictive snapshot): `sharepacks/_predictive/2026-01-09/NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores.csv:317`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/NewJersey4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `stable_top10pct`, `hz_top20pct`, `vtrac_top10`, `dr_best_area<=3`
  - Hypothesis: Stable clearly surfaced the winner as a boxed candidate, but our `stable_top` pack didn’t carry it into Candidate Universe.
  - Action (bounded): adjust Candidate Universe `stable_top` extraction to include top boxed canonicals from `stable_patterns_scores.csv` (per variant), not only compound/family surfaces.

- **GOLD-0019** — `2026-01-07 Pennsylvania4 Midday` — winner `060` (canon `006`, idx `2`, mirrorpair ``)
  - Type: `canonical_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `index_hit=True box_hit=False`
  - Evidence:
    - Hot Zones audit case list: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Pennsylvania4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-07/Pennsylvania4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__WINNERS_DIGEST.md`
  - Primitives (tags): `hz_topN`, `canonicalization(006)`, `leading_zero`, `vtrac_idx2`
  - Hypothesis: Hot Zones surfaced `006` as a top triad, which is a BOX-equivalent hit for winner `060` (canonical `006`). This is a repeatable failure mode: **lane/canonical is present**, but our
    default consumption treats it as straight-only (so the play cut can miss).
  - Action (bounded): add a research-only “BOX-equivalent canonicalization” derived pack (from Hot Zones top triads → canonical → BOX) and allow Play Cards to allocate 1 BOX slot to it when convergence is
    otherwise strong (don’t make it a default caller yet; grade first).

- **GOLD-0020** — `2026-01-08 Delaware4 Evening` — winner `031` (canon `013`, idx `8`, mirrorpair ``)
  - Type: `canonical_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - VTRAC audit case list: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Delaware4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-08/Delaware4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `vtrac_topN`, `canonicalization(013)`, `leading_zero`, `vtrac_idx8`
  - Hypothesis: VTRAC top straights included `013` (canonical hit), but the actual winner was `031`. This is the same canonical-only conversion opportunity as GOLD-0019 (tool is “right about the box” even
    when wrong about the exact straight).
  - Action (bounded): add a research-only “VTRAC top straights → canonical → BOX” derived pack (bounded top-N canonicals) and grade whether it converts index/canonical hits into true box hits under
    realistic budgets.

- **GOLD-0021** — `2026-01-09 Michigan4 Midday` — winner `842` (canon `248`, idx `30`, mirrorpair ``)
  - Type: `canonical_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=True`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Hot Zones audit case list: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Michigan4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/Michigan4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `hz_topN`, `canonicalization(248)`, `vtrac_idx30`
  - Hypothesis: This is a second, non-leading-zero instance of the same canonical-only pattern (Hot Zones triad `248` surfaced, winner was `842`). That strongly suggests canonical-only conversion is a
    general property of how these lane tools behave, not a one-off “033→33” dtype issue.
  - Action (bounded): treat “canonical-only conversion” as a first-class measured primitive (track it in tool audits + gold ledger) and evaluate a small BOX-equivalent derived pack under `--profile
    tool_only` before making any analyzer edits.

- **GOLD-0022** — `2026-01-08 Delaware4 Midday` — winner `820` (canon `028`, idx `11`, mirrorpair ``)
  - Type: `index_hit_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:17`
    - Cross-variant bounce: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md:49`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Delaware4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-08/Delaware4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `hz_topN`, `canonicalization(028)`, `leading_zero`, `vtrac_idx11`, `cross_variant_bounce(stable_section=Evening)`
  - Hypothesis: Hot Zones correctly called the **winner’s VTRAC index** (idx11) but did not carry the winning canonical `028` into the bounded play cut, and Stable’s strongest evidence was from the opposite
    period section (bounce). This is a textbook “index hit → box miss” failure mode on a leading-zero canonical.
  - Action (bounded): prioritize the already-identified conversion experiments for this failure mode:
    - `hot_zones_top_triads → canonical → BOX` (GOLD-0019)
    - and a small “pick 1 canonical inside each top-hit index” closure rule (from the VTRAC reference) when `union.index_hit=True` but `union.box_hit=False`.

- **GOLD-0023** — `2026-01-09 Florida4 Evening` — winner `093` (canon `039`, idx `14`, mirrorpair ``)
  - Type: `index_hit_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Convergence case: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md:15`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Florida4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-09/Florida4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__WINNERS_DIGEST.md`
  - Primitives (tags): `vtrac_topN`, `canonicalization(039)`, `leading_zero`, `vtrac_idx14`
  - Hypothesis: VTRAC top straights called the correct **index 14 rail**, but none of the bounded canonicals inside that rail matched the winner’s canonical `039`. This is the same “rail correct, box
    incorrect” pattern as GOLD-0020, but now as an index-hit-only miss (not a canonical hit).
  - Action (bounded): treat this as an index-closure candidate:
    - keep the research-only `vtrac_top_straights → canonical → BOX` derived pack (GOLD-0020), and
    - add a small within-index closure (pick 1–2 canonicals inside the hit index) when `union.index_hit=True` but `union.box_hit=False`.

- **GOLD-0024** — `2026-01-06 Michigan4 Evening` — winner `578` (canon `578`, idx `11`, mirrorpair ``)
  - Type: `stable_families_only`
  - Baseline (profile=`tool_only`): CU union `index_hit=True box_hit=False`; PlayCard (play_box_first B12) `index_hit=False box_hit=False`
  - Evidence:
    - Cross-variant combined-driven example (Stable families best_rank=1): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md:75`
    - Stable summary shows the key gap: `sharepacks/2026-01-06/Michigan4/stable/Michigan4/summary.json` (Evening: `families.best_rank=1`, gaps include `missing_from_scores`, `missing_from_compound`)
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Michigan4.md`
    - Predictive CU: `sharepacks/_predictive/2026-01-06/Michigan4/candidate_universe__tool_only.json`
    - Predictive Play Card: `sharepacks/_predictive/2026-01-06/Michigan4/play_card__tool_only.json`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__WINNERS_DIGEST.md`
  - Primitives (tags): `stable_families`, `stable_missing_from_scores`, `stable_missing_from_compound`, `combined_lens`, `vtrac_idx11`
  - Hypothesis: This is the cleanest proof (in our current window) that **Stable families can isolate the winner even when Stable scores/compound do not contain it**. Our Candidate Universe `stable_top`
    consumption is therefore incomplete: it should ingest the top Stable families surface, not only the scores/compound surfaces.
  - Action (bounded): extend the Candidate Universe Stable ingestion to include bounded top-N canonicals from Stable families (per variant + combined), and measure whether this converts “families-only” cases
    into CU box hits (before any analyzer changes).

- **GOLD-0025** — `2026-01-08 NewJersey4 Evening` — winner `055` (canon `055`, idx `1`, mirrorpair ``)
  - Type: `budget_sensitivity (doubles)`
  - Baseline (profile=`tool_only`): CU union `hit_any=True box_hit=True`; PlayCard (play_box_first B12) `hit_any=False box_hit=False`
  - Evidence:
    - Cross-variant bounce: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md:58`
    - Predictive Play Card shows the budget boundary: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only.json`
      - `play_box_first/B12` excludes `055`, while `play_box_first/B24` includes `055`
    - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewJersey4.md`
    - Winners digest: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__WINNERS_DIGEST.md`
  - Primitives (tags): `double_winner`, `budget_sensitivity`, `cross_variant_bounce(stable_section=Midday)`, `vtrac_idx1`
  - Hypothesis: Even when the Candidate Universe contains the exact winning double, a tight B12 play card can still miss if the selection policy prioritizes other closures first. This supports using
    multiple budget “cuts” as experiments (B12/B24/B36) instead of treating a single small card as authoritative.
  - Action (bounded): keep B12 as a strict experiment, but treat B24 as the default competition card for doubles-heavy states (until rollups show otherwise), or explicitly reserve 1 “doubles slot” at B12
    when due-doubles + multi-variant double-pressure is high.
