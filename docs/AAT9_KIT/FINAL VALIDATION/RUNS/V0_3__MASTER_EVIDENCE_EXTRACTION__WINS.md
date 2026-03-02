# AAT9 — Master Evidence Extraction for Wins (V0_3)

Purpose: centralize the **most defensible, reusable evidence** we’ve collected about “what precedes wins” (and why we miss), so you don’t have to re‑interpret hundreds of scattered artifacts every time you deep dive.

This is intentionally written as an **evidence ledger** (claims + receipts), not a theory essay.

## Scope (what’s in / out)

**In scope**
- **Predictive pipeline** evidence: tools → Candidate Universe (CU) → Play Cards (`B12/B24/B36`) → grading vs posted results.
- **Selection bottleneck** evidence: recall vs retention vs conversion (where winners get lost).
- **Cross‑state profitability levers**: play/no‑play thresholds, state triage surfaces, spend geometry.
- **Aux compounding** (badges/heat/due doubles/etc.) *as it measurably changes outcomes*.

**Out of scope (for this doc)**
- Profit Alerts (quarantined; will be re‑introduced later when you choose).
- Large analyzer rewrites (we record “what we’d change” as backlog, but we don’t redesign tools inside this doc).

## Key definitions (so evidence is unambiguous)
- **Winner**: the posted 3‑digit result for a state/draw.
- **Straight hit**: exact winner string appears in the play list.
- **Boxed(any perm) hit**: any permutation of the winner digits appears in the play list.
- **Winner canonical**: sorted digits of the winner (e.g., `942 → 249`).
- **VTRAC index hit**: play list contains ≥1 combo in the winner’s VTRAC family/index (neighborhood hit).
- **Lane**: shorthand for “VTRAC index/family”; **winner lane** = the VTRAC index that contains the posted winner.
- **B12/B24/B36**: the “final predictions” shortlists (budgeted cuts) derived from CU.
- **OOS window**: “out‑of‑sample” guardrail window (we validate that a claim isn’t just in‑sample).

## How to use this ledger (fast, human-first)

This is designed so you can do **broad checks first**, then zoom into “why we missed” without drowning.

### 5‑minute workflow (broad reality check)
1) Open the RUNS portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
   - Predictive days index (what dates exist): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_DAYS_INDEX__tool_only.md`
2) Pick a window report and skim the summary tables:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
3) Pick one day from the window and open its triage surface (baseline + dc1 side-by-side):
   - Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`
   - dc1 (B36 only): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`

### 20‑minute workflow (one state, end-to-end, with receipts)
1) Choose one state row from the portfolio (prefer a “teaching case”: strict miss, lane miss, double winner, etc.).
2) Open the case’s receipts (MV run report + Winners HTML/JSON + Predictive CU + Play Cards + posted results).
3) Label the miss class using this ledger’s tags:
   - `MISS_LANE_DROP` vs `MISS_DIGIT_ASSEMBLY` vs “within‑lane depth too shallow”
4) If you find a repeatable pattern across multiple cases/windows, **add or update an `E###` claim**.

### “Promote/demote” (what it is, and what it is not)
- **Promote/demote only changes this ledger’s claim status** (`candidate` → `validated` → `rejected`), and may add/remove receipts.
- It does **not** rewrite historical sharepacks or change past predictive artifacts. Sharepacks remain frozen evidence.

## Executive summary (plain-English, operator-first)

If you remember nothing else from this entire repo:

- **Your “tools are broken” fear is not what the evidence says.** The tools + CU often see the winner *neighborhood* (lane), but the **fixed-budget cut** is a lossy compression step.
- There are two dominant bottlenecks:
  - **Lane drop**: the winner lane is present in CU but gets **0 lines** in B36 (`E004`).
  - **Within-lane conversion**: the lane is retained but we buy **too little depth / wrong member** to include the winning canonical/perm (`E002`, `E006`).
- **Portfolio ranking is triage**, not a hit guarantee: it ranks “evidence density” (top support + narrow CU), not “expected strict conversion” (`E007`).
- **Doubles/mirror structure is frequent and profit-relevant**, and double-aware closure can move strict hits, but it must be **conditional/gated** (`E003`, `E014`, `E019`, `E020`, `E023`).
- **Not every day/state is isolatable on low sets.** “Tight” convergence episodes exist but are rare; posture shifts (press/hedge/skip) are part of profitability, not a failure (`E021`, `E024`, `E027`).

What you can safely do *without* code changes:
- Start with a window report, pick 1 day, then audit 1–2 states using the 6 receipts (MV report + Winners HTML/JSON + predictive CU + predictive Play Card + results).
- For each miss, label it: `MISS_LANE_DROP` vs `MISS_DIGIT_ASSEMBLY` vs “depth too shallow”.

Top unknowns (what the current evidence does *not* yet settle):
- **Lane allocation geometry:** what is the smallest shoulder-aware rule that reduces `MISS_LANE_DROP` without exploding spend?
- **Gating:** what are the best measurable gates for “use conversion slots / doubles-closure today” vs “do not” (avoid `E019` backfires)?
- **Ranker goals:** do we want portfolio ranking to remain “triage” or evolve into “expected strict conversion”, and what features should drive that?
- **Tool-level tuning ROI:** which misses are *actually* analyzer misses vs purely selection misses (so we don’t chase tool edits prematurely)?

Next best experiments (small, high information; still doc-only):
- Pick **10 misses** from the window reports and label them into the 3 bottleneck buckets above; count them. This gives an immediate “where to spend engineering” answer without changing any code.
- Pick **5 double/triple winners** and compare BASE vs dc1 B36 outcomes; note whether closure helped (and under what environment tags).
- For 3 days, compare the top-ranked states’ `CU top support`/`CU union` to outcomes; treat it as a sanity check for triage usefulness (not a hit promise).

## The evidence-claim template (every entry must follow this)

### Claim ID: `E###` — (short name)
- **Claim (1 sentence):**
- **Layer:** `Recall (CU)` | `Retention (into B36)` | `Conversion (within lane)` | `Ranking/Triage` | `Spend/Profitability`
- **Why it matters (operator value):**
- **Receipts (open these files):**
  - (list exact filepaths)
- **Quant support (if available):**
  - window(s), counts, effect size, baselines
- **Failure mode (how it breaks):**
- **Operationalization (how to use it):**
  - “If you see X, do Y” (or “raise score for Z”)
- **Experiment to validate (small, fast):**
- **Status:** `candidate` | `validated` | `rejected` | `needs-more-data`

## Source inventory (what we will mine into this ledger)

Treat this as the “scan list”. We pull candidate claims from these sources, then **promote** only what survives receipts + quant checks.

### A) Codex deep analysis reports (post‑results reviewer)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CODEX_DEEP_ANALYSIS.md`

### B) Gold mining / “what we think we learned” ledgers
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/GOLD_RUNS_2_REPORT.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/GOLD_RUNS_2_TRIAGE.md`

### C) Corpus inventory / synthesis / dashboards (cross‑day summaries)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_DASHBOARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__CORPUS_DASHBOARD.md`

### D) “Distilled insights” already written (seed list; still must be validated)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__TOOL_EXTRACTION_MAP__tool_only__stable10.md`

### E) Master Validation “microscope” templates + navigators (how to audit a single day/state)
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Template_V0_2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPLATEH.md`

### F) Truth-layer / bottleneck quant reports (turn “feelings” into numbers)
- Portfolio vs results (broad-first):  
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
- Conversion scoreboards (where did we lose it?):  
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
- Posture buckets (MV labels joined to outcome metrics):  
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md`
  - Label gaps (why `UNLABELED` exists): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_LABEL_GAPS__B36__tool_only.md`

### G) Competition artifacts (manual time-box evidence; useful as a reference lens)
- Competition intermission scorecard (boxed-first lens): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__TESTING_COMPETITION_ANALYSIS.md`
- Competition deep-dive (doubles/mirror/VTRAC theory receipts): `tasks/COMPETITION_1_2_ANALYSIS_THEORY_REPORT.md`
- Competition log (raw): `tasks/challenge_codex.txt`
- Competition handoff memo (context): `tasks/CODEX_HANDOFF__PLAN_AND_COMPETITION.md`

## Mining status (so we actually “squeezed the orange”)

Meaning of “mined” here: at least one **validated claim (`E###`)** or **teaching case (`C###`)** in this ledger points at that source as a receipt.

| Source bucket | Status | What it contributed (examples) |
|---|---|---|
| A) Codex deep analysis reports | mined | Tool recall/tightness + convergence rarity + negative controls (`E009–E013`, `E024`, `E026`) |
| B) Gold mining ledgers | mined | Doubles/mirror frequency + profitability posture framing (`E014`, `E020`, `E021`, `E023`) |
| C) Corpus dashboards/synthesis | mined | Cross-variant bounce + convergence distributions (`E022`, `E024`) |
| D) Distilled insights | mined | Seed list cross-checked, then re-anchored to truth-layer receipts (`E004`, `E007`) |
| E) Master Validation templates/run reports | mined | Casebook proofs (filled MV reports paired with Winners HTML/JSON + predictive CU/Play Card) (`C001–C036`) |
| F) Truth-layer quant reports | mined | Window-level metrics and bottleneck attribution (portfolio-vs-results, conversion scoreboards, env verdict) (`E001–E008`, `E020`) |
| G) Competition artifacts | mined | Real-time “boxed-first” lens validating doubles/mirror closure intuition (`E020`, `C001`) |

## Extraction campaign plan (state-of-the-art, but practical)

### Macro plan tracker (keep us out of “talking circles”)
Last updated: `2026-03-01`

Status legend: `done` | `in_progress` | `pending`

| Phase | Name | Status | Notes |
|---:|---|---|---|
| 0 | Lock rubric | done | Definitions + evidence-claim template locked |
| 1 | Candidate claim backlog | done | `E001–E027` created |
| 2 | Reconcile vs gold extraction | done | Claims cross-checked against `SUPERBRAIN_V0__GOLD_EXTRACTION.md` |
| 2.5 | MV + Winners microscope receipts | done | `C001–C036` built; includes posture anchors + negative controls + baseline vs dc1 receipts |
| 3 | Corpus consolidation (de-bias) | done | Regime tags + stability map added (claims + cases) |
| 4 | Quant validation (promote/demote) | done | `E008` promoted (regime-sensitive boxed lift confirmed across windows) |
| 5 | Operator levers | done | Per-layer lever map added; decision table + triage card are now “first-class” |
| 6 | Publish outputs | done | SSOT + portal wired; posture bucket scoreboard published |

## Phase 3 output — Regime tags + stability map (de-bias)

Purpose: prevent “one-window overfitting” by giving every claim a **where-it-applies** label.

Two kinds of tags are useful:
- **Environment regimes** (the day is tight vs noisy; double-heavy vs not; split vs not)
- **Failure-mode regimes** (how we missed: lane drop vs digit-assembly vs within-lane depth)

### Regime tags (operator-friendly, small set)

**Environment**
- `ENV_TIGHT` — evidence is dense (fewer competing lanes; tighter CU surface). Usually “playable / press” candidates.
- `ENV_NOISY` — evidence is diffuse (many competing lanes; weak convergence). Usually “skip / tiny hedge / broad cheap probe”.
- `WIN_DOUBLE` — winner is a double/triple (cheap to cover; closure rules matter more).
- `DAY_SPLIT` — Midday vs Evening behave differently; “one day, one verdict” is too coarse.

**Failure modes**
- `MISS_LANE_DROP` — CU contained winner lane but B36 dropped it (`E004`).
- `MISS_DIGIT_ASSEMBLY` — digits were present but no winning permutation/canonical was selected (`E002`).
- `NEG_DOMINANT_LANE_MISS` — loud/dominant lane signal but miss; do not tune weights off it (`E026`).

### Stability map (which claims are “always true” vs regime-dependent)

This table is the Phase 3 deliverable: a plain-English answer to “does this claim apply everywhere?”

| Claim | Stability | Primary regimes / tags | Notes |
|---|---|---|---|
| `E001` (B36 straight lift) | stable | (global) | Small but consistent lift vs random in both main windows. |
| `E002` (digit-assembly misses) | stable | `MISS_DIGIT_ASSEMBLY` | Dominant miss class; conversion-layer lever. |
| `E003` (double winners boost) | regime | `WIN_DOUBLE` | Double/triple winners behave differently and are cheaper to close. |
| `E004` (CU sees lane, B36 drops) | stable | `MISS_LANE_DROP` | Core bottleneck: selection geometry drops the lane. |
| `E005` (winner lane shoulder-heavy) | stable | (global) | Winners are often not in top 3–5 lanes. |
| `E006` (strict needs depth) | stable | (global) | Strict hits require meaningful within-lane depth. |
| `E007` (portfolio rank is triage) | stable | (global) | Rank ≠ conversion; it’s “where evidence is denser”. |
| `E008` (boxed(any perm) flips) | regime | `ENV_TIGHT`, `ENV_NOISY` | Treat boxed(any perm) as regime-sensitive until more windows. |
| `E009` (Stable = tightness scalar) | stable | `ENV_TIGHT`, `ENV_NOISY` | Best “posture knob”; not a top-1 caller. |
| `E010` (Hot Zones containment) | stable | `ENV_TIGHT`, `ENV_NOISY` | HZ is better as an index gateway than canonical top-K. |
| `E011` (VTRAC = coordinate) | stable | (global) | Use VTRAC as neighborhood coordinate, not just “top lane”. |
| `E012` (DR = constraint lens) | stable | `ENV_TIGHT`, `ENV_NOISY` | DR narrates pressure/constraints; don’t expect “calls”. |
| `E013` (triple convergence posctrl) | regime | `ENV_TIGHT` | Rare “all lenses align” events; best positive controls. |
| `E014` (doubles/mirror-doubles frequent) | stable | `WIN_DOUBLE` | Doubles are frequent enough to treat as primitives. |
| `E015` (CC due-doubles ↔ Aux) | stable | `WIN_DOUBLE` | Due-doubles parity aligns across layers (triage support). |
| `E016` (HZ index gateway) | stable | (global) | Grade HZ by index containment, not only canonical rank. |
| `E017` (badge pressure > overdue-only) | stable | `ENV_TIGHT` | Use badge pressure as ranking/tie-breaker, not a hard filter. |
| `E018` (DR envelopes modest lift) | stable | `ENV_NOISY` | Envelopes widen CU union modestly; treat as coverage lever. |
| `E019` (conversion slots can backfire) | stable | `ENV_TIGHT` | Lane-first spending must be gated; not always-on. |
| `E020` (mirror-pair closure budget-starved) | stable | `MISS_DIGIT_ASSEMBLY`, `WIN_DOUBLE` | Closure helps, but can be budget-starved without depth. |
| `E021` (environment classes → posture) | regime | `ENV_TIGHT`, `ENV_NOISY`, `DAY_SPLIT` | Operator “play/skip/hedge” thesis. |
| `E022` (cross-variant bounce) | stable | `DAY_SPLIT` | Combined/other period often holds the best evidence. |
| `E023` (mirror-repeat beyond doubles) | regime | `WIN_DOUBLE` | Mirror-repeat is broader than literal doubles; needs gating. |
| `E024` (full convergence rare) | stable | `ENV_NOISY` | Forces posture diversity; don’t assume every day is isolatable. |
| `E025` (Blackapple not strict oracle) | stable | (global) | Treat BA as auxiliary pressure until it proves strict lift. |
| `E026` (dominant-lane miss) | stable | `NEG_DOMINANT_LANE_MISS` | Loud doesn’t mean correct; negative control. |
| `E027` (split days) | regime | `DAY_SPLIT` | Midday vs Evening posture can differ. |

### Case tags (so you can learn regimes by example)

| Case | Tags | Why it’s worth opening |
|---|---|---|
| `C001` (NJ 2026-01-06 Eve 942) | `MISS_DIGIT_ASSEMBLY` | “Lane correctness is real” but conversion is fragile; mirror/doubles closure teaching case. |
| `C015` (NY 2026-01-05 Mid 080) | `ENV_TIGHT` | High-convergence positive control; calibrates what “tight” looks like end-to-end. |
| `C025` (NJ 2026-01-07 Eve 847) | `NEG_DOMINANT_LANE_MISS` | “Loud miss” negative control; do not tune off it. |
| `C026` (DE 2026-01-15 Eve 309) | `MISS_LANE_DROP` | CU had winner lane; baseline B36 dropped it. |
| `C028` (CT 2026-01-04 Mid 569) | `MISS_DIGIT_ASSEMBLY` | Clean “conversion delta” teaching case: BASE→dc1 strict improved without analyzer edits. |
| `C029` (SC 2026-01-21 Eve 458) | (conversion delta) | Later-window strict improvement example (BASE→dc1). |
| `C030` (NC 2026-01-08 both) | `ENV_NOISY` | Skip/tiny-hedge posture anchor: weak/noisy + 0 lane hit on both outcomes. |
| `C031` (OH 2026-01-22 Eve 048) | (conversion delta) | Another strict recovery example; shows conversion can move straights without analyzer edits. |
| `C034` (SC 2026-01-15 Eve 118) | (conversion backfire) | Proof that conversion policies must be conditional/gated (`E019`). |
| `C035` (NY 2026-01-06 Eve 342) | `MISS_LANE_DROP` | Shallow lane recall → lane dropped; dc1 can’t help if the lane gets 0 lines. |
| `C036` (DE 2026-01-02 Eve 076) | `MISS_DIGIT_ASSEMBLY` | Lane retained but 1-line depth → classic “lane hit → box miss”. |

### Phase 0 — Lock the rubric (prevents “talking circles”)
- Define the **five layers** we classify every claim into: `Recall`, `Retention`, `Conversion`, `Ranking/Triage`, `Spend/Profitability`.
- Define the **minimum evidence standard** to promote a claim:
  - at least 1 receipt file we can open
  - at least 1 quantitative check OR 2 independent qualitative sources that agree
  - specify what failure mode looks like

### Phase 1 — Build the candidate claim backlog (fast pass, high yield)
- Read the five `__CODEX_DEEP_ANALYSIS.md` reports and extract only:
  - repeated “wins came from…” patterns
  - repeated “we miss because…” patterns
  - explicit “if you see X, do Y” operator heuristics
- Create `E###` entries as **candidates** (do not mark validated yet).

### Phase 2 — Reconcile against “gold extraction” (are we aligned with our own conclusions?)
- Cross-check Phase 1 claims against:
  - `SUPERBRAIN_V0__GOLD_EXTRACTION.md`
  - `GOLD_RUNS_2_REPORT.txt`
- Outcomes:
  - confirm (gold ledger matches)
  - downgrade (gold ledger conflicts)
  - split (ledger mixes 2 distinct mechanisms)

### Phase 2.5 — Master Validation + Winners paired “microscope” pass (high confidence receipts)
- For the most important candidate claims, pick 10–20 **filled** MV run reports (`docs/.../RUNS/<D>__<STATE>.md`).
- For each case, open the paired **Winners HTML/JSON** and the corresponding **predictive CU/Play Card** artifacts, and record:
  - what the environment looked like (winners lens),
  - what the tools surfaced (run report),
  - what the predictive pipeline would have played (CU + play card),
  - where the winner was lost (if it was lost).
- Write each case as a `C###` entry and explicitly link it to one or more `E###` claims.

### Phase 3 — Consolidate via corpus synthesis (avoid one-window bias)
- Use `__CORPUS_SYNTHESIS.md` files to merge duplicates and mark:
  - which claims are stable across multiple windows
  - which claims are window-specific (“regime dependent”)

### Phase 4 — Quant validation pass (promote/demote with numbers)
- For each candidate claim, attach at least one quantitative receipt:
  - conditional rates (e.g., “when double winner, index-hit jumps”)
  - bottleneck attribution (CU vs play card miss)
  - rank-band capture (does any triage correlate with hits?)
- Promote to **validated** only when the claim improves clarity or decisions.

### Phase 5 — Convert validated claims into “operator levers”
For each validated claim, add:
- where it should live in the pipeline:
  - tool extraction, CU construction, lane allocation, within-lane closure, ranking surface, play/no-play gating
- the smallest safe experiment we can run to test it without breaking workflows

### Phase 6 — Produce two outputs (so it’s actually usable)
- **Evidence ledger** (this doc): claims + receipts + status.
- **Operator cheat sheet** (1–2 pages): “what to do when you see X”, plus recommended deep-dive drilldowns.

## Initial “starter” claims (seeds to formalize as E###)
(These are deliberately not finalized here — they get formalized into the template above with receipts and window stats.)
- “Double-pressure days behave differently; closure should exploit doubles/mirror‑doubles.”
- “A large share of misses are ‘digit-assembly’ misses: digits present but winning perm not selected.”
- “CU recall can be materially higher than B36 retention; lane allocation is a major loss surface.”

---

## Evidence ledger entries (E-series)

### Quick index (scan-first)
| ID | Status | Layer | Short name |
|---|---|---|---|
| `E001` | validated | Conversion | B36 straight above random |
| `E002` | validated | Conversion | Digit-assembly misses dominate |
| `E003` | validated | Spend | Double winners boost performance |
| `E004` | validated | Retention | CU sees lane; B36 drops it |
| `E005` | validated | Retention | Winner lane is shoulder-heavy |
| `E006` | validated | Conversion | Strict needs depth in lane |
| `E007` | validated | Ranking | Portfolio rank is triage (weak concentrator) |
| `E008` | validated | Conversion | B36 boxed(any perm) regime-sensitive |
| `E009` | validated | Ranking | Stable as environment strength scalar |
| `E010` | validated | Recall | Hot Zones containment, mid-rank |
| `E011` | validated | Recall | VTRAC as lane coordinate (not top-only) |
| `E012` | validated | Recall | DR as constraint/overlay lens |
| `E013` | validated | Ranking | Triple convergence positive controls |
| `E014` | validated | Spend | Doubles/mirror-doubles are frequent |
| `E015` | validated | Recall | CC due-doubles DS matches Aux |
| `E016` | validated | Recall | Hot Zones index gateway (not canonical top-K) |
| `E017` | validated | Ranking | Aux badge pressure beats overdue-only |
| `E018` | validated | Recall | DR envelope packs: modest lift, widen union |
| `E019` | validated | Conversion | Conversion slots can backfire |
| `E020` | validated | Conversion | Mirror-pair closure can be budget-starved |
| `E021` | validated | Spend | Environment classes → posture shifts |
| `E022` | validated | Recall | Cross-variant bounce; Combined required lens |
| `E023` | validated | Spend | Mirror-repeat beyond literal doubles |
| `E024` | validated | Ranking | Full convergence is rare (posture needed) |
| `E025` | validated | Recall | Blackapple not a strict oracle (near-zero) |
| `E026` | validated | Ranking | Dominant-lane miss negative control |
| `E027` | validated | Spend | Split days → per-period decisions |

### Claim ID: `E001` — B36 straight is above random baseline
- **Claim (1 sentence):** B36 straight hits are consistently above the random baseline in both scored windows (small but real lift).
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** This is a “sanity anchor” that the system is not behaving like random picks on the hardest metric; the bottleneck is improving conversion, not “starting over”.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
- **Quant support (if available):**
  - OOS window B36 straight: `4.5% (11/245)` vs expected random `3.6%`
  - Jan window B36 straight: `4.7% (9/193)` vs expected random `3.6%`
- **Failure mode (how it breaks):** If a policy chases only “coverage” (too broad), straight lift can collapse back toward random.
- **Operationalization (how to use it):** Treat straight lift as a north‑star metric for conversion policies; don’t evaluate purely on lane recall.
- **Experiment to validate (small, fast):** Compare B36 variants using the same windows in `__PORTFOLIO_VS_RESULTS__` and `__CONVERSION_SCOREBOARD__` reports.
- **Status:** `validated`

### Claim ID: `E002` — Digit-assembly misses dominate at B36
- **Claim (1 sentence):** At B36, we almost always capture the winner digits somewhere, but we often fail to include any winner permutation (digit-assembly is a primary miss mode).
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** This reframes “misses” from “tools didn’t see it” to “we didn’t assemble/allocate the right permutations”, which is fixable at the selection/combination-forming layer.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
- **Quant support (if available):**
  - OOS window B36: digit-cover(all unique) `95.1% (233/245)`; CoverAll+NoBoxPerm `80.4% (197/245)`
  - Jan window B36: digit-cover(all unique) `95.9% (185/193)`; CoverAll+NoBoxPerm `74.1% (143/193)`
- **Failure mode (how it breaks):** “Digit cover” can be high even when the list is not near the correct lane; you still need lane-aware closure to avoid false confidence.
- **Operationalization (how to use it):** When CoverAll+NoBoxPerm is high, prioritize conversion rules (within-lane closure, doubles closure, mirror-pair completion) over adding more evidence sources.
- **Experiment to validate (small, fast):** Add a bounded “closure pack” (index closure / doubles closure) and re-run the same window report to see if Boxed(any perm) rises without tanking Straight.
- **Status:** `validated`

### Claim ID: `E003` — Doubles winners are a different regime (and a profit lever)
- **Claim (1 sentence):** Performance is materially stronger when the posted winner is a double/triple, supporting the “doubles/mirror‑doubles matter” thesis.
- **Layer:** `Spend/Profitability`
- **Why it matters (operator value):** Doubles are cheaper to cover (3 perms), and the system’s measured hit rates improve on double-winner rows—so “double-aware closure” is a high-EV spend lever.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`
- **Quant support (if available):**
  - OOS window B36 doubles vs singles:
    - straight: `7.1%` vs `3.4%`
    - boxed(any perm): `24.3%` vs `10.9%`
    - VTRAC idx hit: `71.4%` vs `48.6%`
  - Jan window B36 doubles vs singles:
    - straight: `9.6%` vs `2.8%`
    - boxed(any perm): `25.0%` vs `20.6%`
- **Failure mode (how it breaks):** If closure rules “flood” too many doubles across too many indices, you can destroy lane breadth and regress strict conversion.
- **Operationalization (how to use it):** Treat doubles-heavy indices as “cheap closure candidates”; design conversion rules that preferentially close doubles within already-selected lanes.
- **Experiment to validate (small, fast):** Evaluate “doubles closure” variants against baseline on both windows (see `__DOUBLES_CLOSURE_SWEEP.md`).
- **Status:** `validated`

### Claim ID: `E004` — CU sees the winner lane often; B36 drops it (primary bottleneck)
- **Claim (1 sentence):** Candidate Universe lane recall is high (winner VTRAC index is usually present), but the B36 selection cut frequently drops that lane (`CU_LANE_BUT_PLAY_MISS` is large).
- **Layer:** `Retention (into B36)`
- **Why it matters (operator value):** This is the clearest evidence that (today) we should debug selection geometry before touching analyzers: the signal is often present, but the spend plan loses it.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
  - Strict miss split (lane drop vs within-lane): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`
  - Strict miss split (lane drop vs within-lane): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- **Quant support (if available):**
  - Jan window (baseline strategy): CU union `vtrac_index_hit=78.8%`; B36 `hit_any_inclusive=63.7%`; strict `hit_any=4.7%`; `CU_LANE_BUT_PLAY_MISS=13.5%`
  - OOS window (baseline strategy): CU union `vtrac_index_hit=71.0%`; B36 `hit_any_inclusive=55.1%`; strict `hit_any=4.5%`; `CU_LANE_BUT_PLAY_MISS=13.9%`
  - B36 lane retention (how often the budgeted card even touches the winner lane):
    - Jan: `59.1% (114/193)`; strict-miss lane dropped share: `42.9% (79/184)`
    - OOS: `53.1% (130/245)`; strict-miss lane dropped share: `48.9% (115/235)`
- **Failure mode (how it breaks):** If CU lane recall drops (true evidence failure), selection-only fixes won’t help; you must verify `CU_MISS` is not dominating.
- **Operationalization (how to use it):** Treat `CU_LANE_BUT_PLAY_MISS` reduction as the most important “selection-layer win” target under fixed budget.
- **Experiment to validate (small, fast):** Compare any new B36 strategy by its `CU_LANE_BUT_PLAY_MISS` delta first, then strict/boxed.
- **Status:** `validated`

### Claim ID: `E005` — Winner lane rank is shoulder-heavy; “top lanes only” is structurally fragile
- **Claim (1 sentence):** Even when the winner lane is present, it usually does not rank in the top few lanes; so top‑lane commitment is guaranteed to miss a large fraction of outcomes.
- **Layer:** `Retention (into B36)`
- **Why it matters (operator value):** It explains why “top 3–5 lanes only” feels like it should work (great when it hits) but collapses in aggregate: winners often live in the shoulder.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SHOULDER_DEPTH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SHOULDER_DEPTH.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- **Quant support (if available):**
  - Jan window (packs-first): winner lane rank<=5 `19.2%`, rank<=10 `28.5%`
  - OOS window (packs-first): winner lane rank<=5 `15.1%`, rank<=10 `26.1%`
- **Failure mode (how it breaks):** If you “fix” this by narrowing to fewer lanes to buy depth, you can reduce lane retention further (breadth collapse).
- **Operationalization (how to use it):** Any conversion policy must be shoulder-aware (buy some probability mass beyond the top 3–5 lanes).
- **Experiment to validate (small, fast):** Compare a shoulder-aware lane allocation schedule vs baseline on both windows using the stable10 reports.
- **Status:** `validated`

### Claim ID: `E006` — Strict conversion requires depth inside the winner lane (≈6+ lines)
- **Claim (1 sentence):** Strict hits are typically “depth events”: when the winner lane is retained, you usually need ~6+ lines inside that lane to capture the exact winner permutation.
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** This gives you a concrete conversion target: it’s not enough to “touch” the correct VTRAC index; you must allocate meaningful line depth to it.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- **Quant support (if available):**
  - Jan window baseline allocation: lines on winner lane (including 0) p90 `6`, max `8`, median `0` (most outcomes buy no depth on the correct lane).
- **Failure mode (how it breaks):** If max lines concentrate on the wrong lane (spikiness), depth doesn’t help strict conversion.
- **Operationalization (how to use it):** Use lane-aware closure rules (especially for doubles-heavy indices) to increase winner-lane depth without destroying breadth.
- **Experiment to validate (small, fast):** Track how `pct(in>=6)` changes in `__PORTFOLIO_VS_RESULTS__` and whether strict hits rise accordingly.
- **Status:** `validated`

### Claim ID: `E007` — Portfolio rank is weak as a “hit concentrator”; use it as triage
- **Claim (1 sentence):** The portfolio’s daily state ranking does not strongly concentrate inclusive hits (boxed(any perm), VTRAC index hits), so it should be treated as a triage surface rather than a “hit-rate claim”.
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** It prevents misusing rank as a promise; it’s still useful for deciding where to spend attention/budget, but it won’t “save” a lossy conversion policy.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
- **Quant support (if available):**
  - OOS window B36:
    - boxed(any perm) Top3 lift `0.99x`
    - VTRAC idx hit Top3 lift `0.95x`
  - Jan window B36:
    - boxed(any perm) Top3 lift `1.09x`
    - VTRAC idx hit Top3 lift `1.16x`
- **Failure mode (how it breaks):** If we chase rank improvements without fixing conversion, we can “look smarter” while strict conversion stays flat.
- **Operationalization (how to use it):** Use rank to prioritize which states to deep-dive, not as a betting threshold without additional gating.
- **Experiment to validate (small, fast):** Rebuild rank features only after we have a conversion policy that retains the correct lane more reliably.
- **Status:** `validated`

### Claim ID: `E008` — B36 boxed(any perm) is regime-sensitive (needs more windows)
- **Claim (1 sentence):** B36 boxed(any perm) flips from below-random in one window to above-random in another, so we should treat boxed(any perm) as regime-sensitive until we expand windows.
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** It’s a warning against overreacting to a single “bad” block or “good” block.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PORTFOLIO_VS_RESULTS__tool_only.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.csv`
- **Quant support (if available):**
  - Window `2025-06-21→2025-06-23`: B36 boxed(any perm) `12.3%` vs expected `17.2%` (n=`3` days)
  - Window `2026-01-01→2026-01-09`: B36 boxed(any perm) `14.7%` vs expected `17.1%` (daily range `7.7%→25.0%`, n=`9` days)
  - Window `2026-01-15→2026-01-22`: B36 boxed(any perm) `21.8%` vs expected `17.2%` (daily range `14.3%→28.6%`, n=`7` days)
- **Failure mode (how it breaks):** Boxed(any perm) can rise simply because the winner is a more “box-friendly” type (doubles/triples) in that window.
- **Operationalization (how to use it):** Always interpret boxed(any perm) alongside the doubles-lens breakdown.
- **Experiment to validate (small, fast):** Add more windows and re-check “boxed lift” stability before locking a policy.
- **Status:** `validated`

### Claim ID: `E009` — Stable is an environment strength scalar (not a strict top-1 caller)
- **Claim (1 sentence):** Stable is a strong discriminator for “how tight the environment is”, but it is not a safe top‑k “caller” by itself.
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** It’s the cleanest lever for posture shifts (hedge/broaden/pass) without analyzer edits.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_DASHBOARD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md`
- **Quant support (if available):**
  - Stable present: `76.7% (125/163)`
  - Stable winner rank fraction: p10 `0.033`, median `0.340`, p90 `0.915` (widely distributed)
  - Stable “exact spotlight” (tool lens, not Play Card): exact_boxed `105/163`, exact_straight `100/163`
  - Posture corroboration (Jan window, B36): `VTRAC idx hit` is higher on `STRONG/SUPPORT` than `WEAK_NOISY` (see env-verdict scoreboard).
- **Failure mode (how it breaks):** Treating Stable as “always take the #1 candidate” overfits to positive-control days.
- **Operationalization (how to use it):** Use Stable tightness to decide spend posture, then let other lenses decide lane allocation.
- **Experiment to validate (small, fast):** Compare strict conversion when Stable rank fraction is in low deciles vs high deciles (stratify outcomes).
- **Status:** `validated`

### Claim ID: `E010` — Hot Zones is near-universal containment, but mid-rank (coverage shaper)
- **Claim (1 sentence):** Hot Zones almost always contains the winner, but the winner lane is frequently mid-ranked, so Hot Zones is best used to shape coverage rather than to pick a single top lane.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It’s a highly reliable “where to look” surface; misuse (top lane only) creates systematic misses.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- **Quant support (if available):**
  - Hot Zones present: `99.4% (162/163)`; rank fraction median `0.505`
- **Failure mode (how it breaks):** If you narrow to Hot Zones top lanes only, you lose shoulder winners.
- **Operationalization (how to use it):** Use Hot Zones as a prior/coverage shaper and intersection partner (with Stable/VTRAC), not as a sole chooser.
- **Experiment to validate (small, fast):** Measure strict conversion by “HZ tightness” buckets (rank fraction deciles).
- **Status:** `validated`

### Claim ID: `E011` — VTRAC is the shared lane coordinate; top-index-only is unsupported
- **Claim (1 sentence):** VTRAC nearly always places the winner into an index, but that index is often mid-ranked; VTRAC should be used as a lane coordinate for alignment/hedging, not “top index only”.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It’s how tools “speak the same language” for convergence (and how we explain lane hits vs box misses).
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- **Quant support (if available):**
  - VTRAC placement present: `99.4% (162/163)`; index rank fraction median `0.457`
- **Failure mode (how it breaks):** If selection commits to only the top index, it will drop correct-lane cases that sit in the shoulder.
- **Operationalization (how to use it):** Treat VTRAC as the axis for shoulder-aware allocation and for doubles/mirror-double closure rules.
- **Experiment to validate (small, fast):** Quantify strict conversion uplift when the correct index is in rank bands (1–3 vs 4–10 vs 11–20).
- **Status:** `validated`

### Claim ID: `E012` — Digit Reduction top-list is a constraint lens, not a strict caller
- **Claim (1 sentence):** Digit Reduction’s strict “top list contains the winner” rate is very low, implying DR should be used as a constraint/overlay rather than a standalone top-caller.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It prevents discarding DR as “broken” and instead uses it for what it does best: pressure/constraint narration.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- **Quant support (if available):**
  - DR strict top list winner present: `4.9% (8/163)`
- **Failure mode (how it breaks):** If we grade DR only by “top list strict hits”, we will incorrectly delete a useful constraint lens.
- **Operationalization (how to use it):** Use DR to reweight or prune candidates inside already-selected lanes (not to choose lanes).
- **Experiment to validate (small, fast):** Compare conversion when DR pressure agrees vs disagrees with Stable/HZ posture (intersection buckets).
- **Status:** `validated`

### Claim ID: `E013` — Triple convergence is rare but a high-value positive control
- **Claim (1 sentence):** Stable+HotZones+VTRAC “tightness” convergence is rare, but those episodes are the best positive controls for validating aggregator logic.
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** It gives you a small set of “anchor” examples to reverse-engineer without drowning in hundreds of mixed-quality days.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
  - `sharepacks/2025-12-31/NewYork4/stable/NewYork4/summary.json`
  - `sharepacks/2025-12-31/NewYork4/hot_zones/NewYork4/summary.json`
  - `sharepacks/2025-12-31/NewYork4/vtrac/NewYork4/summary.json`
- **Quant support (if available):**
  - Triple convergence count: `4 / 163` outcomes (in the cited corpus window)
- **Failure mode (how it breaks):** If we tune only to these rare positives, we overfit; they are a validation set, not a training set.
- **Operationalization (how to use it):** Use triple convergence cases to test whether “convergence-aware conversion” rules behave sanely.
- **Experiment to validate (small, fast):** Run a closure policy only on triple-convergence cases and measure conversion delta vs baseline.
- **Status:** `validated`

### Claim ID: `E014` — Doubles/mirror-doubles are frequent and measurable (not anecdotal)
- **Claim (1 sentence):** Doubles and mirror‑doubles occur at high frequency in the gold corpus, so “double-aware” conversion is not a niche edge case.
- **Layer:** `Spend/Profitability`
- **Why it matters (operator value):** It justifies spending engineering effort on doubles/mirror‑double closure policies (they apply often, and doubles are cheaper to cover).
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`
- **Quant support (if available):**
  - Gold corpus inventory: doubles `104`, mirror_doubles `83`, triples `3`
- **Failure mode (how it breaks):** Treating every “double-ish” signal as bet-worthy can still overbet weak/noisy environments.
- **Operationalization (how to use it):** Make doubles/mirror‑double detection a first-class “mode” in conversion; don’t rely on ad-hoc manual spotting.
- **Experiment to validate (small, fast):** Compare baseline vs doubles-closure strategies only on mirror-double subsets (stratified evaluation).
- **Status:** `validated`

### Claim ID: `E015` — Control Center due-doubles DS matches Aux DS (no silent drift)
- **Claim (1 sentence):** Control Center “due doubles DS” and Aux `ds_since_double` are aligned (delta=0) in the deep-dive scan, so due-doubles features are trustworthy as shared primitives.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It removes a major class of “is the system reading the right thing?” doubt—so we can focus on conversion geometry instead of chasing phantom data drift.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- **Quant support (if available):**
  - Deep-dive scan summary: delta(cc-aux)=`0` for DS audits (see the cited deep-dive report)
- **Failure mode (how it breaks):** If future state-mapping changes (new states, multi-draw states), DS alignment must be re-audited.
- **Operationalization (how to use it):** Use due-doubles DS and mirror-pair frequency as stable features for triage and for conditional conversion slots.
- **Experiment to validate (small, fast):** Re-run the DS audit scan after adding any new states (Tri-State, GA, TX) or changing draw mappings.
- **Status:** `validated`

### Claim ID: `E016` — Hot Zones “canonical top‑K” is the wrong lens; index gateway is the right lens
- **Claim (1 sentence):** Hot Zones looks weak if you grade it by “winner canonical in top‑K”, but it is materially stronger as a VTRAC index gateway lens (often “rail correct, box miss”).
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It prevents throwing away a powerful lens; it also tells us *what kind of fix* to attempt (conversion, not weight tuning).
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- **Quant support (if available):**
  - Window `2025-12-30→2026-01-04`: canonical Top12 `14/163 (0.086)` vs index-hit Top12 `61/163 (0.374)`; index-hit-only Top12 `47/163 (0.288)`
  - Window `2026-01-05→2026-01-09`: canonical Top12 `9/138 (0.065)` vs index-hit Top12 `39/138 (0.283)`; index-hit-only Top12 `30/138 (0.217)`
- **Failure mode (how it breaks):** Changing Hot Zones weights can produce inconsistent, window-specific lifts; it’s not a high-leverage lever by itself.
- **Operationalization (how to use it):** Keep Hot Zones weights stable; treat Hot Zones as an “index prior” and solve the miss via bounded lane→box closure packs.
- **Experiment to validate (small, fast):** Run a Hot Zones index-closure experiment as a selection-layer ablation (see the referenced gold entry/harness docs).
- **Status:** `validated`

### Claim ID: `E017` — Aux badge pressure beats overdue-only index ranking (TopK winner-index capture)
- **Claim (1 sentence):** Ranking VTRAC indices by Aux badge pressure density captures the winner index more often than ranking by overdue-only DS (especially Evening).
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** It’s a measurable way to use “badges” (boxed matrix pressure) as a real triage signal rather than a vibe; it may later drive conversion-slot allocation.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2026-01-05_to_2026-01-09.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- **Quant support (if available):**
  - `2025-12-30→2026-01-04` Evening topK hit: Overlay `7/82 (0.085)` vs Pressure `15/82 (0.183)`
  - `2026-01-05→2026-01-09` Evening topK hit: Overlay `7/69 (0.101)` vs Pressure `10/69 (0.145)`
  - Cross-variant pressure intersection is low coverage (≈`0.02–0.03`), so treat it as gating, not a universal filter.
- **Failure mode (how it breaks):** Using badge pressure as a hard filter can drop too many lanes (coverage collapse).
- **Operationalization (how to use it):** Use badge pressure for ranking/triage and conditional budget allocation, not for expanding the union set.
- **Experiment to validate (small, fast):** Use badge pressure as a tie-breaker for lane allocation, then measure `CU_LANE_BUT_PLAY_MISS` and strict conversion deltas.
- **Status:** `validated`

### Claim ID: `E018` — DR envelope packs provide modest union lift, but widen the union (explicit knob only)
- **Claim (1 sentence):** Adding DR envelope packs (Top2) slightly lifts Candidate Universe union hit rates across windows, but it widens the union cost and can increase “index-hit-only”.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It’s a safe “research knob” for recall, but it should stay default-off until we prove it doesn’t worsen conversion by flooding.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ENVELOPE_PACK__EXPERIMENT__TOP2.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- **Quant support (if available):**
  - Window `2025-12-30→2026-01-04`: union hit_any `22.7% → 23.9%`; avg union cost `163.2 → 176.9`
  - Window `2026-01-05→2026-01-09`: union hit_any `22.5% → 23.9%`; avg union cost `160.3 → 172.7`
- **Failure mode (how it breaks):** Union lift can be illusory if it increases `idx_only` and does not convert under B36.
- **Operationalization (how to use it):** Keep DR envelope packs additive and explicit; never let them silently perturb baseline packs while we’re still measuring.
- **Experiment to validate (small, fast):** Run the same stable10 conversion truth layer with DR envelope packs enabled and check whether strict hits improve or regress.
- **Status:** `validated`

### Claim ID: `E019` — “Conversion slots” can backfire under tight budgets (must be conditional)
- **Claim (1 sentence):** Naively reserving “conversion slots” (lane-first spending) can increase neighborhood hits while reducing strict hits under tight budgets; conversion slots must be conditional/gated.
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** It prevents repeating a common failure mode: buying more indices but starving the few boxable closures that actually produce strict hits.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__stable10.md`
- **Quant support (if available):**
  - Rollup (mixed dates; Evening B36): `play_box_first` strict `0.0400` vs `conversion_box_first` strict `0.0291` (strict drops while box rises)
  - Rollup (mixed dates; Evening B36): `conversion_box_first_conditional_*` strict `0.0482` (n=`83`; subset) (gating can recover strict)
  - Rollup (stable10; Evening B36): `play_box_first` strict `0.0545` vs `conversion_box_first` strict `0.0500` (same direction)
- **Failure mode (how it breaks):** If conversion slots are always-on, they can degrade strict conversion even when lane recall is fine.
- **Operationalization (how to use it):** Only allocate conversion slots when (a) lane evidence is strong but (b) there is no compact boxable closure already present.
- **Experiment to validate (small, fast):** Compare conditional conversion-slot strategies vs baseline on both OOS and in-sample windows.
- **Status:** `validated`

### Claim ID: `E020` — Doubles/mirror closure is a compact lane→box conversion primitive (but can be budget-starved)
- **Claim (1 sentence):** Doubles/mirror closure packs can encode a compact lane→box conversion set (especially on mirror/doubles structure), but the play-card budget allocator can starve them even when they contain the winner.
- **Layer:** `Conversion (within lane)`
- **Why it matters (operator value):** This is the concrete “convert lane hit → boxed hit without flooding” mechanism we keep circling; it’s cheap, explainable, and aligns with your training logic.
- **Receipts (open these files):**
  - Strategy spec: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PLAY_CARD_STRATEGY__B36__DOUBLES_CLOSURE.md`
  - Truth layer (OOS): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
  - Truth layer (Jan): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`
  - Competition lens (boxed-first; shows “lane hit → box miss”): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__TESTING_COMPETITION_ANALYSIS.md`
  - Competition theory notes (mirror/doubles/index closure): `tasks/COMPETITION_ANALYSIS.TXT`
  - Competition deep-dive (Codex synthesis of the same connection): `tasks/COMPETITION_1_2_ANALYSIS_THEORY_REPORT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (see `GOLD-0027`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Delaware4.md`
  - `sharepacks/_predictive/2026-01-06/Delaware4/candidate_universe__tool_only__stable10.json`
  - `sharepacks/_predictive/2026-01-06/Delaware4/play_card__tool_only__stable10.json`
  - Starved-closure receipts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1869`
  - Starved-closure receipts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2605`
  - Starved-closure receipts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2622`
- **Quant support (if available):**
  - OOS sweep (B36 strict hit_any): baseline `4.5%`; closure v1 `4.9%`; closure v2 `4.5%`
  - Jan sweep (B36 strict hit_any): baseline `4.7%`; closure v1 `4.7%`; closure v2 `5.2%`
  - Mirror-double deep-dive scan: `best_box=mirror_pair_closure@18` appears `4` times; Play Card `box_hit=False` in `3/4` cases (see cited deep-dive pointers).
- **Failure mode (how it breaks):** If mirror closure is always-on without gating, it can waste budget on weak/noisy days.
- **Operationalization (how to use it):** Treat mirror-pair closure as a conditional “conversion slot”: reserve it only when (a) mirror-double structure is present and (b) lane evidence supports the same family.
- **Experiment to validate (small, fast):** Add a single reserved closure line for `mirror_pair_closure` when present; measure whether `index_hit_only` cases convert to `box_hit` without strict regression.
- **Status:** `validated`

### Claim ID: `E021` — “Environment classes” are real; profitability requires posture shifts (play/skip, hedge/narrow)
- **Claim (1 sentence):** The corpus contains clear positive-control vs negative-control days, supporting an “environment class” concept where the optimal action may be to narrow aggressively *or* skip/broaden.
- **Layer:** `Spend/Profitability`
- **Why it matters (operator value):** It directly supports your “profitability threshold” idea: not every state/day should be played the same way, even if tools are working correctly.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/GOLD_RUNS_2_TRIAGE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md`
- **Quant support (if available):**
  - 6-day corpus (`n=168` outcomes): `strong=80`, `support=58`, `weak/noisy=26`, `unknown=4` (missing winners)
  - Day polarity is extreme at times (built-in anti-overfit): `2025-12-31` is `24/28 strong` (positive control), `2026-01-04` is `20/28 weak/noisy` (negative control)
  - Posture buckets are measurably different (B36): `STRONG/SUPPORT` retains the winner lane more often than `WEAK_NOISY` in the Jan window (see env-verdict scoreboard).
- **Failure mode (how it breaks):** If environment labels are prose-only and not backed by numeric tool evidence, they become overfit narratives.
- **Operationalization (how to use it):** Convert environment classes into measurable gates (Stable tightness, HZ/VTRAC rank-fraction thresholds, badge pressure) before encoding play/no-play rules.
- **Experiment to validate (small, fast):** Stratify portfolio-vs-results metrics by environment bucket and look for cost-adjusted EV lift.
- **Status:** `validated`

### Claim ID: `E022` — Cross-variant bounce is common; Combined is a required evidence lens (not optional)
- **Claim (1 sentence):** The strongest evidence for a Midday/Evening outcome frequently comes from the opposite period or the Combined lens, so “Combined is a lens” must be treated as a core evidence surface.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It validates your intuition that we can’t interpret the system as “two independent draws”; cross-variant structure is a real, measurable part of how winners are supported.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- **Quant support (if available):**
  - Stable origin buckets (n=138): same_period `37.7%`, other_period `36.2%`, combined `23.2%`
  - When the winner index appears in VTRAC top indices: Combined supports `88.6%` of those appearances (31/35)
- **Failure mode (how it breaks):** If Combined is treated like a third “outcome” instead of an evidence lens, it can corrupt grading semantics.
- **Operationalization (how to use it):** Always allow Combined to contribute evidence, but grade outcomes only against Midday/Evening winners.
- **Experiment to validate (small, fast):** Add a “cross-variant boost” only at the selection layer (not analyzers) and check for strict conversion lift without coverage regression.
- **Status:** `validated`

### Claim ID: `E023` — Mirror-repeat structure is common even when the winner is not a literal double
- **Claim (1 sentence):** A large share of winners show “mirror/double-space” repeat structure in VTRAC signature even when they are literal singles, so conversion policies should not key only on literal doubles.
- **Layer:** `Spend/Profitability`
- **Why it matters (operator value):** It widens the set of “double-like” episodes where mirror/doubles closure logic may apply profitably.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__MIRROR_DOUBLE_FREQUENCY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- **Quant support (if available):**
  - Signature has repeats: `74/138 (53.6%)`
  - Mirror-repeat but literal SINGLE: `31/138 (22.5%)`
- **Failure mode (how it breaks):** Not every mirror-repeat episode is “strong”; it still needs posture gates (Stable/HZ tightness, badge pressure).
- **Operationalization (how to use it):** Treat mirror-repeat as a measurable primitive used to gate closure policies, not as a stand-alone bet trigger.
- **Experiment to validate (small, fast):** Stratify conversion results by mirror-repeat flag and see whether closure strategies improve strictly on that subset.
- **Status:** `validated`

### Claim ID: `E024` — Full multi-lens convergence is rare (so “always isolate on low sets” is an over-expectation)
- **Claim (1 sentence):** High-confidence “all lenses align” convergence events are rare, so the system must support multiple postures (narrow, hedge, skip) rather than assuming every day is an “easy isolation” day.
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** It prevents discouragement loops: absence of convergence does not mean the tools are broken; it means the environment is ambiguous and needs a different spend plan.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- **Quant support (if available):**
  - Convergence score distribution (n=138): score4 `3.6%`, score3 `14.5%`, score2 `39.9%`, score1 `37.7%`, score0 `4.3%`
- **Failure mode (how it breaks):** If you only play “score4” events, you’ll almost never play; if you play everything the same, you’ll waste spend.
- **Operationalization (how to use it):** Use convergence score (or similar) to decide: narrow/press vs hedge vs skip.
- **Experiment to validate (small, fast):** Evaluate a “play/no-play” threshold policy using convergence score bands and cost-adjusted EV.
- **Status:** `validated`

### Claim ID: `E025` — Blackapple top-list “exact caller” behavior is extremely low (treat as auxiliary, not a strict oracle)
- **Claim (1 sentence):** Blackapple’s strict “top list contains winner” rate is near-zero in the gold windows we’ve measured, so it should not be interpreted as a direct top-caller.
- **Layer:** `Recall (CU)`
- **Why it matters (operator value):** It prevents misreading BA as “broken” (or as a primary predictor) and instead frames it as a compounding/gating feature if/when it’s used.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_DASHBOARD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- **Quant support (if available):**
  - `2025-12-30→2026-01-04`: BA top list contains winner `0/163 (0.0%)`
  - `2026-01-05→2026-01-09`: BA top list contains winner `1/138 (0.7%)`
- **Failure mode (how it breaks):** If BA is consumed as a hard filter or primary list, it can destroy coverage and hurt conversion.
- **Operationalization (how to use it):** Use BA only as an auxiliary “pressure” signal or tie-breaker until it demonstrates measurable lift as a candidate source.
- **Experiment to validate (small, fast):** Compare play-card performance with BA-only variants vs tool-only baselines across multiple windows.
- **Status:** `validated`

### Claim ID: `E026` — “Dominant-lane miss” and “Stable exact present but low rank” are critical negative controls
- **Claim (1 sentence):** The corpus repeatedly shows (a) winners that are exactly present but low-ranked and (b) “loud” dominance on a non-winner lane, so rank loudness is not a safe proxy for correctness.
- **Layer:** `Ranking/Triage`
- **Why it matters (operator value):** These are the two failure modes that create “chasing” behavior; explicitly tagging them prevents us from tuning the system into loud-but-wrong overfit.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Delaware4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewJersey4.md`
- **Quant support (if available):** This is primarily a qualitative pattern (negative-control class), but it is explicitly called out as critical in the June deep analysis and repeatedly referenced in fix-later rollups.
- **Failure mode (how it breaks):** If we tune weights based on only positive controls, we accidentally amplify “dominant-lane miss” days.
- **Operationalization (how to use it):** Add explicit reporting tags for dominant-lane-miss days (log-first), and do not chase “loudness” as a proxy for correctness.
- **Experiment to validate (small, fast):** Build a detector that flags “dominant lane but miss” using rank-fraction + top-score gaps, then evaluate whether skipping those days improves cost-adjusted EV.
- **Status:** `validated`

### Claim ID: `E027` — Split days are common; decisions must be per-period (Midday vs Evening)
- **Claim (1 sentence):** “Split” environments (different posture Midday vs Evening) occur frequently enough that “one state, one verdict” is often too coarse.
- **Layer:** `Spend/Profitability`
- **Why it matters (operator value):** It supports per-period betting thresholds and prevents wasting budget by applying a single day-level posture to both draws.
- **Receipts (open these files):**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Michigan4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewJersey4.md`
- **Quant support (if available):**
  - June corpus: `split` bucket appears `14` times in `84` outcomes (see cited deep analysis).
- **Failure mode (how it breaks):** If we only rank/triage at the state/day level, we can miss that one period is “play” while the other is “pass”.
- **Operationalization (how to use it):** Treat Midday/Evening as separate decision surfaces; allow Combined evidence to support both without redefining outcomes.
- **Experiment to validate (small, fast):** Run portfolio-vs-results stratified by period and compare rank/coverage/conversion separately.
- **Status:** `validated`

---

## MV + Winners paired case receipts (C-series)

Purpose: anchor the E-claims in **concrete, human-auditable examples** where you can open:
1) the filled MV run report, 2) the Winners HTML/JSON, 3) the predictive CU/Play Card artifacts.

Dating sanity:
- For predictive packs under `sharepacks/_predictive/<D>/...`, grade against `data/results/<D>.txt` (same date).

### Mirror-double “index hit → box miss” queue (highest-leverage conversion cases)
Source queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`

### Case ID: `C001` — 2026-01-06 NewJersey4 Evening — winner `942` (canon `249`, idx `31`)
- Supports: `E003`, `E004`, `E005`, `E014`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md`
  - Winners HTML: `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4/NewJersey4_vtrac31_winner_942_20260107_052306.html`
  - Winners JSON: `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4/NewJersey4_vtrac31_winner_942_20260107_052306.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/NewJersey4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only__stable10.json`
  - Predictive Play Card (closure variant): `sharepacks/_predictive/2026-01-06/NewJersey4/play_card__tool_only__doubles_closure_v1.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1936`
  - Posted results: `data/results/2026-01-06.txt`
- What to look for (quick checklist):
  - Does the Winners lens show a dense lane family (idx31) + mirror/doubles behavior?
  - Does the CU contain idx31 strongly (and/or contain `249` as a boxable canonical)?
  - Does the Play Card allocate meaningful depth to idx31, or is it starved by other indices?

### Case ID: `C002` — 2026-01-06 Delaware4 Midday — winner `165` (canon `156`, idx `6`)
- Supports: `E004`, `E015`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Delaware4.md`
  - Winners HTML: `sharepacks/2026-01-06/Delaware4/winners/Delaware4/Delaware4_vtrac6_winner_165_20260107_052254.html`
  - Winners JSON: `sharepacks/2026-01-06/Delaware4/winners/Delaware4/Delaware4_vtrac6_winner_165_20260107_052254.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/Delaware4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/Delaware4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1869`
  - Posted results: `data/results/2026-01-06.txt`
- What to look for (quick checklist):
  - Confirm CC vs Aux due-doubles DS alignment is sane for this day/state.
  - Check whether mirror-pair closure or due-double closure evidence exists in CU but is missing from B36.

### Case ID: `C003` — 2026-01-09 Delaware4 Evening — winner `681` (canon `168`, idx `18`)
- Supports: `E003`, `E004`, `E014`, `E015`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Delaware4.md`
  - Winners HTML: `sharepacks/2026-01-09/Delaware4/winners/Delaware4/Delaware4_vtrac18_winner_681_20260110_035036.html`
  - Winners JSON: `sharepacks/2026-01-09/Delaware4/winners/Delaware4/Delaware4_vtrac18_winner_681_20260110_035036.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-09/Delaware4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__stable10.json`
  - Predictive Play Card (closure variant): `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__doubles_closure_v1.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2537`
  - Posted results: `data/results/2026-01-09.txt`
- What to look for (quick checklist):
  - Confirm the winner is a mirror-double type and identify its mirror pair (1/6 family).
  - Check whether B36 retained idx18 at all; if retained, how many lines were allocated inside idx18.

### Case ID: `C004` — 2026-01-07 NewJersey4 Midday — winner `361` (canon `136`, idx `18`)
- Supports: `E003`, `E004`, `E014`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewJersey4.md`
  - Winners HTML: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4/NewJersey4_vtrac18_winner_361_20260110_033422.html`
  - Winners JSON: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4/NewJersey4_vtrac18_winner_361_20260110_033422.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/NewJersey4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__stable10.json`
  - Predictive Play Card (closure variant): `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__doubles_closure_v1.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2135`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - This is a prime “mirror_pair_closure” case; confirm whether the CU carries the closure pack but the B36 cut starves it.

### Case ID: `C005` — 2026-01-08 Florida4 Midday — winner `429` (canon `249`, idx `31`)
- Supports: `E003`, `E004`, `E014`, `E020`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Florida4.md`
  - Winners HTML: `sharepacks/2026-01-08/Florida4/winners/Florida4/Florida4_vtrac31_winner_429_20260110_034419.html`
  - Winners JSON: `sharepacks/2026-01-08/Florida4/winners/Florida4/Florida4_vtrac31_winner_429_20260110_034419.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-08/Florida4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__stable10.json`
  - Predictive Play Card (closure variant): `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__doubles_closure_v1.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2337`
  - Posted results: `data/results/2026-01-08.txt`
- What to look for (quick checklist):
  - Winner canonical `249` is a classic “cheap doubles lane” closure target (idx31); check if B36 buys depth in idx31 or just touches it.

### Case ID: `C006` — 2026-01-05 PuertoRico4 Evening — winner `972` (canon `279`, idx `28`)
- Supports: `E003`, `E004`, `E014`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PuertoRico4.md`
  - Winners HTML: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_972_20260128_160527.html`
  - Winners JSON: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_972_20260128_160527.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-05/PuertoRico4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1767`
  - Posted results: `data/results/2026-01-05.txt`
- What to look for (quick checklist):
  - Look for DR / long-box “reveal” mechanics in the winners lens, and whether CU retains the lane without converting to box.

### Case ID: `C007` — 2026-01-05 SouthCarolina4 Evening — winner `712` (canon `127`, idx `20`)
- Supports: `E003`, `E004`, `E014`, `E021`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__SouthCarolina4.md`
  - Winners HTML: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac20_winner_712_20260128_160529.html`
  - Winners JSON: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac20_winner_712_20260128_160529.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-05/SouthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1801`
  - Posted results: `data/results/2026-01-05.txt`
- What to look for (quick checklist):
  - This case is valuable for “profit-first vs tool-only” contrast (note: Profit Alerts reintegration is deferred, but evidence is still informative).

### Case ID: `C008` — 2026-01-09 Virginia4 Midday — winner `380` (canon `038`, idx `13`)
- Supports: `E004`, `E005`, `E014`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Virginia4.md`
  - Winners HTML: `sharepacks/2026-01-09/Virginia4/winners/Virginia4/Virginia4_vtrac13_winner_380_20260110_035108.html`
  - Winners JSON: `sharepacks/2026-01-09/Virginia4/winners/Virginia4/Virginia4_vtrac13_winner_380_20260110_035108.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-09/Virginia4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2772`
  - Posted results: `data/results/2026-01-09.txt`
- What to look for (quick checklist):
  - “WL cells = 0” style cases are useful as negative controls: verify what “lane present” really means in low-structure environments.

### Case ID: `C009` — 2026-01-08 Connecticut4 Midday — winner `106` (canon `016`, idx `6`)
- Supports: `E003`, `E004`, `E014`, `E020`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Connecticut4.md`
  - Winners HTML: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_106_20260110_034414.html`
  - Winners JSON: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_106_20260110_034414.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-08/Connecticut4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2321`
  - Posted results: `data/results/2026-01-08.txt`
- What to look for (quick checklist):
  - Another idx6 mirror-repeat family; compare to other idx6 cases (156, 160, 165) for “conversion policy” consistency.

### Case ID: `C010` — 2026-01-08 PuertoRico4 Evening — winner `479` (canon `479`, idx `31`)
- Supports: `E003`, `E004`, `E014`, `E020`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PuertoRico4.md`
  - Winners HTML: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_479_20260110_034446.html`
  - Winners JSON: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_479_20260110_034446.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-08/PuertoRico4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2504`
  - Posted results: `data/results/2026-01-08.txt`
- What to look for (quick checklist):
  - Another idx31 closure target; compare to `C001`/`C005` for “idx31 depth vs breadth” behavior.

### Case ID: `C011` — 2026-01-07 Connecticut4 Midday — winner `156` (canon `156`, idx `6`)
- Supports: `E003`, `E004`, `E014`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Connecticut4.md`
  - Winners HTML: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_156_20260110_033410.html`
  - Winners JSON: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_156_20260110_033410.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/Connecticut4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2053`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - Mirror-double “cheap closure” archetype; compare with 165/160/106.

### Case ID: `C012` — 2026-01-07 Indiana4 Midday — winner `823` (canon `238`, idx `29`)
- Supports: `E004`, `E014`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Indiana4.md`
  - Winners HTML: `sharepacks/2026-01-07/Indiana4/winners/Indiana4/Indiana4_vtrac29_winner_823_20260110_033417.html`
  - Winners JSON: `sharepacks/2026-01-07/Indiana4/winners/Indiana4/Indiana4_vtrac29_winner_823_20260110_033417.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/Indiana4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:2102`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - “WL cells = 0” style case: validate whether we touched the correct lane but failed to allocate any depth.

### Case ID: `C013` — 2026-01-06 Florida4 Evening — winner `160` (canon `016`, idx `6`)
- Supports: `E003`, `E004`, `E014`, `E020`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Florida4.md`
  - Winners HTML: `sharepacks/2026-01-06/Florida4/winners/Florida4/Florida4_vtrac6_winner_160_20260107_052258.html`
  - Winners JSON: `sharepacks/2026-01-06/Florida4/winners/Florida4/Florida4_vtrac6_winner_160_20260107_052258.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/Florida4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/Florida4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1886`
  - Posted results: `data/results/2026-01-06.txt`
- What to look for (quick checklist):
  - “consensus_double_9” evidence: check whether the system recognized double-pressure but still failed to box-convert.

### Case ID: `C014` — 2026-01-06 Indiana4 Evening — winner `961` (canon `169`, idx `19`)
- Supports: `E003`, `E004`, `E014`, `E020`, `E022`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Indiana4.md`
  - Winners HTML: `sharepacks/2026-01-06/Indiana4/winners/Indiana4/Indiana4_vtrac19_winner_961_20260107_052301.html`
  - Winners JSON: `sharepacks/2026-01-06/Indiana4/winners/Indiana4/Indiana4_vtrac19_winner_961_20260107_052301.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/Indiana4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__stable10.json`
  - Deep dive pointer: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md:1902`
  - Posted results: `data/results/2026-01-06.txt`
- What to look for (quick checklist):
  - Another “mirror_pair_closure” case; check whether we had the closure but didn’t allocate a slot for it.

### High-convergence anchors (score=4) — “when multiple lenses agree”
Source list: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`

### Case ID: `C015` — 2026-01-05 NewYork4 Midday — winner `080` (canon `008`, idx `4`)
- Supports: `E013`, `E022`, `E024`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`
  - Winners HTML: `sharepacks/2026-01-05/NewYork4/winners/NewYork4/NewYork4_vtrac4_winner_080_20260128_160515.html`
  - Winners JSON: `sharepacks/2026-01-05/NewYork4/winners/NewYork4/NewYork4_vtrac4_winner_080_20260128_160515.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__stable10.json`
  - Posted results: `data/results/2026-01-05.txt`
- What to look for (quick checklist):
  - This is a “positive control” convergence event; use it to calibrate what “tightness” looks like end-to-end.

### Case ID: `C016` — 2026-01-07 Florida4 Midday — winner `434` (canon `344`, idx `34`)
- Supports: `E013`, `E022`, `E024`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
  - Winners HTML: `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac34_winner_434_20260110_033415.html`
  - Winners JSON: `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac34_winner_434_20260110_033415.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/Florida4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__stable10.json`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - Compare this “convergence hit” to `C005` (same state, different date) to see what changes between strong vs weak conversion.

### Case ID: `C017` — 2026-01-07 Florida4 Evening — winner `963` (canon `369`, idx `24`)
- Supports: `E013`, `E022`, `E024`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
  - Winners HTML: `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac24_winner_963_20260110_033415.html`
  - Winners JSON: `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac24_winner_963_20260110_033415.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/Florida4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__stable10.json`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - Another “positive control” convergence event; good for validating cross-variant evidence routing.

### Case ID: `C018` — 2026-01-09 NewJersey4 Evening — winner `028` (canon `028`, idx `11`)
- Supports: `E013`, `E022`, `E024`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md`
  - Winners HTML: `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4/NewJersey4_vtrac11_winner_028_20260110_035047.html`
  - Winners JSON: `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4/NewJersey4_vtrac11_winner_028_20260110_035047.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-09/NewJersey4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__stable10.json`
  - Posted results: `data/results/2026-01-09.txt`
- What to look for (quick checklist):
  - Validate whether this “convergence case” still shows lane-to-box conversion problems (or whether it’s a clean strict hit).

### Case ID: `C019` — 2026-01-09 Pennsylvania4 Evening — winner `014` (canon `014`, idx `9`)
- Supports: `E001`, `E009`, `E013`, `E021`, `E022`, `E024`
- Posture anchor: **press / playable** (positive-control example)
- CSV snapshot (baseline B36): `straight=1`, `boxed_any=1`, `vtrac_index_hit=1`, `in_winner_index=4` (rank `12`, CU union `211`)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Pennsylvania4.md`
  - Winners HTML: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_014_20260110_035100.html`
  - Winners JSON: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_014_20260110_035100.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-09/Pennsylvania4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__stable10.json`
  - Predictive portfolio (triage surface): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PREDICTIVE_PORTFOLIO__tool_only.md`
  - Posted results: `data/results/2026-01-09.txt`
- What to look for (quick checklist):
  - This is the “good day” example: strict hit exists (B36 contains the winner), even though portfolio rank is not top‑3 (`E007`).
  - This is a BA_contains=1 convergence case; good for validating how BA behaves as an auxiliary signal (not a strict caller).

### Teaching cases — major miss modes + dc1 deltas

These are “broad-first” teaching examples pulled directly from the `__PORTFOLIO_VS_RESULTS__` surfaces.

### Case ID: `C020` — 2026-01-07 Michigan4 Evening — winner `616` (canon `166`, idx `16`)
- Supports: `E002`, `E003`, `E006`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=1`, `in_winner_index=1`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Michigan4.md`
  - Winners HTML: `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.html`
  - Winners JSON: `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/Michigan4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - A classic “digit-assembly miss”: digits are present, lane is touched, but no winner permutation exists in the list (`E002`).
  - Winner is a double regime example (cheap closure should matter), but within-lane depth is still thin (`E003`, `E006`).

### Case ID: `C021` — 2026-01-01 NorthCarolina4 Evening — winner `053` (canon `035`, idx `4`)
- Supports: `E002`, `E006`, `E007`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=1`, `in_winner_index=1`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NorthCarolina4.md`
  - Winners HTML: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_053_20260105_053415.html`
  - Winners JSON: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_053_20260105_053415.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-01/NorthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-01.txt`
- What to look for (quick checklist):
  - “High rank, still miss” reminder: rank is triage, not conversion (`E007`).
  - Shallow lane touch (1 line in winner index) is usually not enough for strict/boxed conversion (`E006`).

### Case ID: `C022` — 2026-01-02 SouthCarolina4 Midday — winner `308` (canon `038`, idx `13`)
- Supports: `E002`, `E006`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=1`, `in_winner_index=1`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__SouthCarolina4.md`
  - Winners HTML: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac13_winner_308_20260105_070926.html`
  - Winners JSON: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac13_winner_308_20260105_070926.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-02/SouthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-02.txt`
- What to look for (quick checklist):
  - Another clean “digits present, no perm chosen” example; good for practicing the diagnosis ladder (`E002`).

### Case ID: `C023` — 2026-01-05 Florida4 Evening — winner `994` (canon `499`, idx `35`)
- Supports: `E002`, `E003`, `E006`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=1`, `in_winner_index=1`
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Florida4.md`
  - Winners HTML: `sharepacks/2026-01-05/Florida4/winners/Florida4/Florida4_vtrac35_winner_994_20260128_160507.html`
  - Winners JSON: `sharepacks/2026-01-05/Florida4/winners/Florida4/Florida4_vtrac35_winner_994_20260128_160507.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-05.txt`
- What to look for (quick checklist):
  - Double-heavy winner, but still only “touch” depth in the lane → the conversion budget didn’t assemble a perm (`E003`, `E006`).

### Case ID: `C024` — 2026-01-02 Pennsylvania4 Midday — winner `871` (canon `178`, idx `21`)
- Supports: `E004`, `E007`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0`
- Quick fact: CU union contains winner idx `21` (lane recall), but baseline B36 drops the lane entirely (`E004`).
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Pennsylvania4.md`
  - Winners HTML: `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_871_20260105_070920.html`
  - Winners JSON: `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_871_20260105_070920.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-02/Pennsylvania4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-02.txt`
- What to look for (quick checklist):
  - Rank is high, but this is a lane-drop miss → reinforces “triage rank is not conversion” (`E007`).

### Case ID: `C025` — 2026-01-07 NewJersey4 Evening — winner `847` (canon `478`, idx `30`)
- Supports: `E004`, `E007`, `E026`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0`
- Quick fact: CU union contains winner idx `30` (lane recall), but baseline B36 drops the lane entirely (`E004`).
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewJersey4.md`
  - Winners HTML: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4/NewJersey4_vtrac30_winner_847_20260110_033423.html`
  - Winners JSON: `sharepacks/2026-01-07/NewJersey4/winners/NewJersey4/NewJersey4_vtrac30_winner_847_20260110_033423.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-07/NewJersey4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-07.txt`
- What to look for (quick checklist):
  - A good negative-control teaching case: don’t “tune weights” off loud confident misses (`E026`).

### Case ID: `C026` — 2026-01-15 Delaware4 Evening — winner `309` (canon `039`, idx `14`)
- Supports: `E004`, `E007`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0`
- Quick fact: CU union contains winner idx `14` (lane recall), but baseline B36 drops the lane entirely (`E004`).
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Delaware4.md`
  - Winners HTML: `sharepacks/2026-01-15/Delaware4/winners/Delaware4/Delaware4_vtrac14_winner_309_20260127_014828.html`
  - Winners JSON: `sharepacks/2026-01-15/Delaware4/winners/Delaware4/Delaware4_vtrac14_winner_309_20260127_014828.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-15/Delaware4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-15.txt`
- What to look for (quick checklist):
  - A “later window” lane-drop example so you don’t overfit to the early block (`E008`).

### Case ID: `C027` — 2026-01-06 Virginia4 Evening — winner `958` (canon `589`, idx `14`)
- Supports: `E002`, `E020`
- Delta (BASE → dc1, B36): `boxed_any 0→1` (canonical conversion improved)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Virginia4.md`
  - Winners HTML: `sharepacks/2026-01-06/Virginia4/winners/Virginia4/Virginia4_vtrac14_winner_958_20260107_052324.html`
  - Winners JSON: `sharepacks/2026-01-06/Virginia4/winners/Virginia4/Virginia4_vtrac14_winner_958_20260107_052324.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/Virginia4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-06.txt`
- What to look for (quick checklist):
  - This is the “canonical conversion” win: same lane retained, but dc1 spends within the lane differently (`E020`).

### Case ID: `C028` — 2026-01-04 Connecticut4 Midday — winner `569` (canon `569`, idx `9`)
- Supports: `E001`, `E020`
- Delta (BASE → dc1, B36): `straight 0→1` (strict conversion improved)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Connecticut4.md`
  - Winners HTML: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_569_20260105_055123.html`
  - Winners JSON: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_569_20260105_055123.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-04/Connecticut4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-04.txt`
- What to look for (quick checklist):
  - A clean demonstration that strict improvements can happen without changing analyzers: this is selection/closure geometry (`E001`, `E020`).

### Case ID: `C029` — 2026-01-21 SouthCarolina4 Evening — winner `458` (canon `458`, idx `14`)
- Supports: `E001`, `E020`
- Delta (BASE → dc1, B36): `straight 0→1` (strict conversion improved)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__SouthCarolina4.md`
  - Winners HTML: `sharepacks/2026-01-21/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_458_20260127_020851.html`
  - Winners JSON: `sharepacks/2026-01-21/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_458_20260127_020851.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-21/SouthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-21.txt`
- What to look for (quick checklist):
  - A later-window strict improvement example (helps separate “real lift” from one-day luck) (`E008`).

### Case ID: `C030` — 2026-01-08 NorthCarolina4 (both draws) — winners `132` (canon `123`, idx `21`) + `571` (canon `157`, idx `7`)
- Supports: `E021`, `E024`, `E027`
- Posture anchor: **skip / tiny hedge / broad cheap probe** (negative-control example)
- CSV snapshot (baseline B36):
  - Midday 132: `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0` (rank `9`, CU union `193`)
  - Evening 571: `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0` (rank `9`, CU union `193`)
- Quick fact: This is a “weak/noisy” environment verdict with **0 lane hit** on both outcomes (not just “conversion failed”).
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NorthCarolina4.md`
  - Winners HTML (Midday): `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_132_20260110_034433.html`
  - Winners HTML (Evening): `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac7_winner_571_20260110_034434.html`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-08/NorthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__dc1.json`
  - Predictive portfolio (triage surface): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PREDICTIVE_PORTFOLIO__tool_only.md`
  - Posted results: `data/results/2026-01-08.txt`
- What to look for (quick checklist):
  - This is the clearest “don’t force it” example: weak/noisy + wrong funded lane → expected miss (`E021`, `E024`).
  - Useful for validating “split day” thinking: both outcomes miss, but by different winner lanes (`E027`).

---

### Case ID: `C031` — 2026-01-22 Ohio4 Evening — winner `048` (canon `048`, idx `14`)
- Supports: `E001`, `E020`
- Delta (BASE → dc1, B36): `straight 0→1` (strict conversion improved; canonical already present)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__Ohio4.md`
  - Winners HTML: `sharepacks/2026-01-22/Ohio4/winners/Ohio4/Ohio4_vtrac14_winner_048_20260128_032340.html`
  - Winners JSON: `sharepacks/2026-01-22/Ohio4/winners/Ohio4/Ohio4_vtrac14_winner_048_20260128_032340.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-22/Ohio4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-22.txt`
- What to look for (quick checklist):
  - This is a pure “perm targeting” win: we were already in the right lane + canonical; dc1 recovered the exact straight without any analyzer edits.

### Case ID: `C032` — 2026-01-20 Virginia4 Evening — winner `367` (canon `367`, idx `21`)
- Supports: `E001`, `E020`
- Delta (BASE → dc1, B36): `straight 0→1` (strict conversion improved; canonical already present)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Virginia4.md`
  - Winners HTML: `sharepacks/2026-01-20/Virginia4/winners/Virginia4/Virginia4_vtrac21_winner_367_20260127_020458.html`
  - Winners JSON: `sharepacks/2026-01-20/Virginia4/winners/Virginia4/Virginia4_vtrac21_winner_367_20260127_020458.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-20/Virginia4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-20.txt`
- What to look for (quick checklist):
  - Another “straight recovery” example that is not a one-off (later window). Treat these as proof that selection/conversion can move strict hits.

### Case ID: `C033` — 2026-01-18 OntarioCanada4 Midday — winner `573` (canon `357`, idx `11`)
- Supports: `E002`, `E020`
- Delta (BASE → dc1, B36): `boxed_any 0→1` (canonical conversion improved; lane retained in both)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__OntarioCanada4.md`
  - Winners HTML: `sharepacks/2026-01-18/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_573_20260127_020041.html`
  - Winners JSON: `sharepacks/2026-01-18/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_573_20260127_020041.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-18/OntarioCanada4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-18.txt`
- What to look for (quick checklist):
  - A clean “lane hit → box hit” conversion improvement (dc1 changes within-lane spend enough to include the winner canonical).

### Case ID: `C034` — 2026-01-15 SouthCarolina4 Evening — winner `118` (canon `118`, idx `18`)
- Supports: `E019`, `E020`
- Delta (BASE → dc1, B36): `straight 1→0` and `boxed_any 1→0` (conversion backfire; lane still retained)
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__SouthCarolina4.md`
  - Winners HTML: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac18_winner_118_20260127_014857.html`
  - Winners JSON: `sharepacks/2026-01-15/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac18_winner_118_20260127_014857.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-15/SouthCarolina4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-15.txt`
- What to look for (quick checklist):
  - The key teaching point: conversion policies must be gated/conditional (`E019`). This is a real example where “spend differently inside the lane” loses a previously-captured strict/boxed hit.

### Case ID: `C035` — 2026-01-06 NewYork4 Evening — winner `342` (canon `234`, idx `30`)
- Supports: `E004`, `E006`, `E007`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=0`, `in_winner_index=0`
- Quick fact: CU union touches winner idx `30` via `379` (1 line), but baseline B36 allocates 0 lines to idx30; dc1 also allocates 0 (because dc1 can’t help if the lane is dropped).
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewYork4.md`
  - Winners HTML: `sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.html`
  - Winners JSON: `sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-06.txt`
  - Context (optional): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__TESTING_COMPETITION_ANALYSIS.md`
- What to look for (quick checklist):
  - A “shallow lane recall” example: the winner index exists in CU but with too little mass to survive lane allocation (`E004`, `E006`).
  - Rank reminder: portfolio triage rank is not a hit guarantee (`E007`).

### Case ID: `C036` — 2026-01-02 Delaware4 Evening — winner `076` (canon `067`, idx `7`)
- Supports: `E002`, `E006`
- CSV snapshot (baseline B36): `digit_cover_all=1`, `boxed_any=0`, `vtrac_index_hit=1`, `in_winner_index=1`
- Quick fact: B36 retained the winner lane (idx `7`) but with only 1 line; CU union contains a winner permutation; classic “lane hit → box miss” due to shallow within-lane depth.
- Open these files (in order):
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Delaware4.md`
  - Winners HTML: `sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.html`
  - Winners JSON: `sharepacks/2026-01-02/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_076_20260105_070900.json`
  - Predictive CU (tool_only): `sharepacks/_predictive/2026-01-02/Delaware4/candidate_universe__tool_only__stable10.json`
  - Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.json`
  - Predictive Play Card (dc1): `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__dc1.json`
  - Posted results: `data/results/2026-01-02.txt`
- What to look for (quick checklist):
  - “Lane retained but no perm” diagnosis: a single line in the correct index is usually not enough for boxed conversion (`E006`).
  - “Digit cover” is not conversion (`E002`).

## Operator cheat sheet (v1; evidence-derived, not guarantees)

If you want the “fastest path” for reviewing a single day, use:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__DAILY_TRIAGE_CARD__PREDICTIVE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__OPERATOR_DECISION_TABLE__PREDICTIVE.md`

If you only remember 9 things:
- **The tools aren’t “dead”; selection is lossy.** CU lane recall can be high while B36 strict hits stay low (`E004`).
- **Stable is the best single posture knob.** Use Stable tightness to decide narrow/hedge/skip; don’t treat it as “top-1 must hit” (`E009`).
- **Don’t trust “top lane only”.** Winners are often in the shoulder, not top 3–5 (`E005`).
- **Don’t chase loudness.** “Dominant‑lane miss” and “exact present but low rank” are real negative controls (`E026`).
- **Depth matters.** Strict hits typically require meaningful line depth inside the correct lane (`E006`).
- **Digit-cover ≠ conversion.** B36 often contains all digits but not a winning permutation (`E002`).
- **Doubles/mirror-repeat are profit primitives.** They are frequent and cheaper to close (`E003`, `E014`, `E023`).
- **Hot Zones is an index gateway lens.** Grade it by index hits, not only canonical top‑K (`E016`).
- **Combined / cross-variant evidence is core.** Best evidence often comes from other period / Combined (`E022`).
- **Conversion slots must be conditional.** Always-on conversion-slot spending can reduce strict hits (`E019`).

Quick “what to do next” mapping:
- If you see **high `CoverAll+NoBoxPerm`** in a window report → focus on **lane→box closure**, not new analyzers (`E002`, `E020`).
- If you see **high `CU_LANE_BUT_PLAY_MISS`** in a stable10 scoreboard → adjust **lane allocation geometry** first (`E004`).
- If a day looks **weak/noisy** (low tightness, low convergence) → treat “skip / tiny hedge / broad cheap probe” as a real posture, not a failure (`E021`, `E024`).
- If you see **a “loud miss” / dominant-lane signature** → tag it and don’t tune weights off it (`E026`).
- If you’re adding **conversion slots** → start with **conditional presets** (not always-on) (`E019`).

## Appendix — Profit Alerts quarantine evidence (archived notes; not reintegration)

This appendix is here only so we **don’t lose** evidence we already paid to collect. It does **not** change the current `tool_only` posture or any predictive artifacts.

- What the v0 ablation showed (small window; directional only):
  - `profit_only` (Profit Alerts only) was extremely weak in the measured v0 Jan window.
  - `tool_only` matched `mixed` at the Play Card layer in that same window.
- Receipts (open these files):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.md`

When you choose to revisit Profit Alerts: treat them as an **incremental candidate source** that must prove lift over tool evidence (not as a default ranker).
