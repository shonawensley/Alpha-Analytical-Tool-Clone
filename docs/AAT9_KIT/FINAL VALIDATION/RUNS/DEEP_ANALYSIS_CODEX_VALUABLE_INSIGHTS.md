# Deep Analysis — Codex Valuable Insights (SSOT Synthesis)

Purpose: extract the **most valuable, state‑of‑the‑art** insights from the Codex deep‑analysis corpus and the newer stable10 conversion truth layer, with an explicit bias toward:
- what correlates with **hits/wins**,
- what breaks (and where),
- and what levers are highest‑EV to pull **next** (selection layer first; no analyzer edits in this phase).

Scope (strict):
- **Analysis only** (no analyzer edits).
- Evidence sources are SSOT:
  - Deep analysis reports under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/*__CODEX_DEEP_ANALYSIS.md`
  - Conversion truth layer (stable10): `__CONVERSION_SCOREBOARD__`, `__CONVERSION_LADDER__`, `__LANE_ALLOCATION__`, `__WINNER_LANE_RANK__`, `__CONVERSION_CASEBOOK__`, `__GLASS_BOX_TRACE__`.

If you remember only one sentence:
> **The system is not “missing signal”; it is losing probability mass in the B36 selection cut.**

---

## 0) Start Here (if you took a break)

### The “one page map”
- Portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- Policy (coverage vs conversion; stable10): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- Glossary (strict vs inclusive semantics): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- Glass-box pipeline flow: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`

### The deterministic Crossroads study bundle (Ontario-first; B36-only)
- Pack entrypoint: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`
- Case index: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

---

## 1) Cross‑report invariants (the “tool roles” that stayed true across months)

These invariants show up consistently across multiple deep‑analysis windows:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__CODEX_DEEP_ANALYSIS.md`

### 1.1 Stable is best treated as an “environment strength scalar” (not a strict top‑1 caller)

Old corpus evidence (June):
- Stable winner rank fraction separates “strong” vs “weak/noisy” sharply.
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`

Gold expansion evidence (Dec→Jan):
- Stable present ≈ `76–77%` containment; Stable exact boxed/straight are high when measured as hits inside Stable’s own lens.
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`

Practical interpretation:
- Stable is a **posture controller**: when Stable is tight, you can spend tighter; when it’s noisy, you should hedge or broaden lanes (or pass).

### 1.2 Hot Zones is near‑universal containment; not “take the #1 lane”

Across multiple corpora:
- Hot Zones “winner containment” is ~`99%`, but the winner is often mid‑rank.
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`

Practical interpretation:
- Hot Zones is best as a **lane prior / coverage shaper**, especially as an intersection partner with Stable (and later Aux constraints).

### 1.3 VTRAC is the shared “lane coordinate” (structure narrator + hedge surface)

Across corpora:
- Winner index placement is almost always present, but often mid‑rank (median rank-fraction ~0.43–0.46).
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`

Practical interpretation:
- VTRAC is an **alignment surface**: it lets multiple tools vote in the same coordinate system.
- “Top index only” is not supported; you need a shoulder‑aware selection policy.

### 1.4 Digit Reduction strict top‑list hit rate is not the correct contract

Across corpora:
- DR strict “top list contains winner” is single‑digit percent (often ~`2–7%` depending on window).
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
  - Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__CODEX_DEEP_ANALYSIS.md`

Practical interpretation:
- DR behaves like a **constraint / pressure narrator**, not a “top 3 straight caller”.

---

## 2) The Crossroads truth layer (stable10 • tool_only • B36)

This is the “current day” measurement surface that removed 8‑hour spiral loops:
- it’s deterministic,
- it separates evidence recall from selection cuts,
- and it gives you explicit buckets for failure modes.

Primary in-sample (Jan gold window):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

Primary OOS guardrail:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

### 2.1 Baseline metrics (locked)

Baseline strategy:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail` @ `B36`

Jan window:
- CU union recall:
  - `hit_any`: `27.5%`
  - `vtrac_index_hit`: `78.8%`
- Play Card conversion:
  - strict `hit_any`: `5.7%`
  - coverage `hit_any_inclusive`: `47.2%`
  - `CU_LANE_BUT_PLAY_MISS`: `26.9%`
  - `CU_EXACT_BUT_PLAY_MISS`: `4.7%`

OOS window:
- CU union recall:
  - `hit_any`: `25.7%`
  - `vtrac_index_hit`: `71.0%`
- Play Card conversion:
  - strict `hit_any`: `4.1%`
  - coverage `hit_any_inclusive`: `42.0%`
  - `CU_LANE_BUT_PLAY_MISS`: `24.1%`
  - `CU_EXACT_BUT_PLAY_MISS`: `4.9%`

Key insight:
- **The big loss is not “tools are broken”; it is the lossy compression step (Play Card under B36).**

Evidence:
- Jan ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10.md`
- OOS ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10.md`

---

## 3) The deepest mechanical insight (why the “shoe” squeezes wrong)

This is the most important “engineering truth” in the current system:

### 3.1 Lane ranking is shoulder-heavy, not top-heavy

Winner lane rank distribution (packs-first; baseline evidence rank):
- Jan window (among `lane_present=1`):
  - median rank: `14`
  - p90 rank: `24`
  - `P(rank<=15)`: `57.2%`
  - `P(rank<=20)`: `71.7%`
- OOS window (among `lane_present=1`):
  - median rank: `14`
  - p90 rank: `25`
  - `P(rank<=15)`: `53.4%`
  - `P(rank<=20)`: `70.7%`

Evidence sources:
- Jan lane-rank (baseline + shoulder-depth): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SHOULDER_DEPTH.md`
- OOS lane-rank (baseline + shoulder-depth): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SHOULDER_DEPTH.md`

Meaning:
- The winner lane is often not in top 3–5.
- A selection policy that “commits to top lanes” is structurally fragile.

### 3.2 Lane retention is basically perfect for top‑10 ranks — then collapses

Jan window (baseline, packs-first ranks):
- If winner lane rank is `<=10`: retention is `100%`
- Ranks `11–15`: retention is `81.2%`
- Ranks `16–20`: retention is `31.8%`
- Ranks `21–35`: retention is `7.0%`

OOS window (baseline):
- If rank `<=10`: retention is ~`96%+`
- Ranks `11–15`: retention is ~`93%`
- Ranks `16–20`: retention is `23.3%`
- Ranks `21–35`: retention is `13.7%`

This is the exact quantitative definition of “the conversion policy over-commits too narrowly.”

### 3.3 Strict hits are not evenly distributed — they’re “depth events”

Among outcomes where the Play Card **retained the winner lane**:
- Jan window:
  - `P(strict hit_any | lane retained)` ≈ `12.1%`
  - strict-hit cases have `winner_lane_lines` median `6` (mean `6.36`)
  - strict-miss cases have `winner_lane_lines` median `1` (mean `2.15`)
- OOS window:
  - `P(strict hit_any | lane retained)` ≈ `9.7%`
  - strict-hit cases have `winner_lane_lines` median `6` (mean `5.6`)
  - strict-miss cases have `winner_lane_lines` median `1`

Translation:
- Today, a strict hit is usually achieved by buying **~6+ lines** inside the winner lane.
- If the winner lane is treated as “tail” (1 line), strict is extremely unlikely.

Evidence:
- Jan lane allocation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md` (+ `.csv`)
- OOS lane allocation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md` (+ `.csv`)

### 3.4 Box/canonical conversion is also rank‑dependent

Within retained lanes (Jan window, baseline):
- If winner lane rank is `1–3`: `pack_box_hit` ≈ `92.9%`
- If rank is `4–5`: `pack_box_hit` ≈ `60.9%`
- If rank is `6–10`: `pack_box_hit` ≈ `50.0%`
- If rank is `11–15`: `pack_box_hit` ≈ `19.2%`
- If rank is `16–20`: `pack_box_hit` ≈ `0%` (in this window)

Implication:
- When a lane is strongly evidenced, the pack composition tends to include the winner canonical frequently.
- When a lane is weakly evidenced, we often retain it with only 1 line and miss both canonical and straight.

(This matters for any future “boxed ticket” cost model: `pack_box_hit` can become economically meaningful.)

---

## 4) Why “shoulder depth” felt promising — and why it regressed

The shoulder-depth experiment teaches a crucial lesson:
- Depth improves conditional strict, **but paying for depth by dropping lanes is too expensive under B36**.

Jan window:
- Baseline indices touched mean: `15.4` → lane retained `47.6%`
- Shoulder-depth indices touched mean: `11.4` → lane retained `39.3%`
- Conditional strict given lane retained improves:
  - `12.1%` → `14.7%`
- But inclusive coverage regresses:
  - `47.2%` → `38.9%`

OOS window repeats the same physics:
- Inclusive regresses (baseline `42.0%` → shoulder `30.2%`) while conditional strict improves.

Evidence:
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SHOULDER_DEPTH.md`
- OOS scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SHOULDER_DEPTH.md`

Most important conclusion:
> **Depth is not wrong. The way we purchased depth was wrong.**

---

## 5) What this means for the project’s ultimate goal (hits → profitability)

The project goal (in plain English):
- Discover repeatable evidence patterns that correlate with wins,
- then design a selection + spend policy that captures that signal at low cost,
- then only then consider analyzer edits to improve the signal itself.

The current system already supports a professional “quant research” posture:
- Evidence → CU (unbounded) → Play Card (budgeted) → Grading → Ladders/Scoreboards → Promotion gates.
- That loop is what prevents us from “optimizing by vibes”.

The critical nuance:
- Master Validation + winners HTML are the **forensic microscope** (POST; spec formation).
- The stable10 conversion truth layer is the **pre-results execution contract** (PRE/DECISION/TRUTH; selection geometry).

If you treat MV as “the predictor”, you will keep feeling like:
“we know how wins look, why can’t we just make the predictor do that?”

The correct translation layer is:
1) Write the hypothesis in MV (winner-aware),
2) Encode it into selection policy (winner-free),
3) Regrade it on Jan + OOS using scoreboards/ladders,
4) Promote only if it improves and does not regress.

---

## 6) High‑EV “steering” actions (selection layer; no analyzers)

These are the most actionable, evidence-supported moves implied by the reports:

### 6.1 Primary objective: reduce `CU_LANE_BUT_PLAY_MISS` (isolation-first)

What it means:
- The system “saw” the winner lane (CU),
- but the Play Card did not retain it under B36.

What’s required to improve:
- A geometry that allocates at least **1 line** to more shoulder lanes (ranks ~16–25) *without* collapsing indices touched.

Why this is the right lever:
- Winner lanes are shoulder-heavy (median rank 14; p90 24–25).
- Current policy retains lanes almost perfectly up through ~15, but collapses after.

### 6.2 Secondary objective: improve within-lane selection quality for low-depth lanes

The strict-hit analysis shows:
- strict hits are currently “depth events” (median 6 lines).

But the economically better future is:
- achieve more strict hits with **1–2 “smart lines”** per lane,
  instead of brute forcing 6 lines.

This is where the “integration log” tool-interpretation insights matter:
- they are not automatically executable,
- but they are a spec for “how to pick smarter within a lane” without touching analyzers.

### 6.3 Keep strict as the guardrail, not the primary objective (for now)

Reason:
- optimizing strict at B36 will tempt you into breadth collapse (which the shoulder-depth experiment demonstrated).
- keeping strict as a guardrail prevents self-deception (“we got strict up by sacrificing the whole coverage contract”).

---

## 7) Concrete study exemplars (Ontario-first; no hunting)

### 7.1 Ontario (cleanest “conversion geometry” and “CU miss” contrast)
- Ontario walkthrough: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLASS_BOX_TRACE__ONTARIOCANADA4__2026-01-15.md`

Ontario teaches in one day:
- Midday is **HIT_INCLUSIVE** (lane retained, depth=1, strict miss).
- Evening is **CU_MISS** (evidence miss; selection can’t recover).

### 7.2 Multi-state Crossroads Pack (bucket coverage)
- Pack entrypoint: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`

### 7.3 Casebooks + trace bundles (fastest way to keep intuition grounded)
- Jan casebook: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`
- Jan trace bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__GLASS_BOX_TRACE_BUNDLE__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`
- OOS trace bundle: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__GLASS_BOX_TRACE_BUNDLE__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`

---

## 8) The most important “don’t lose this” conclusion

The deep analysis reports + the stable10 truth layer converge on the same architectural truth:

> **Tools are producing usable lane evidence. The bottleneck is allocation geometry under a fixed budget.**

This is *good news*, because it means:
- you can improve outcomes without destabilizing analyzers,
- you can run controlled experiments,
- you can promote policies deterministically,
- and you can stop the emotional “nothing works” loop.

Next “Crossroads‑safe” work should stay inside:
- selection policy,
- instrumentation,
- and promotion gates.

