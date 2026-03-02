# V0_3 Operator Decision Table (Predictive)

Purpose: turn the validated evidence (`E001–E027`) into **plain-English “what to do next” rules** so you can deep dive efficiently without needing to understand every artifact.

Use this with:
- Daily checklist: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__DAILY_TRIAGE_CARD__PREDICTIVE.md`
- Evidence SSOT: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`

---

## 0) Two important reminders (so you don’t get misled)

1) **Predictive Portfolio ≠ a hit-rate claim.**  
The portfolio is primarily a **triage surface** (where evidence is denser), not a guarantee of strict conversion (`E007`).

2) Our current bottleneck is usually: **lane recall is decent → conversion is lossy under budget** (`E004`, `E002`).  
So the best next steps are usually **conversion/selection posture choices**, not “rewrite the tools”.

---

## 1) The only 4 metrics you need (operator lens)

You’ll see these in `__PORTFOLIO_VS_RESULTS__` and `__CONVERSION_SCOREBOARD__`:

- **`index_hit`** (winner VTRAC lane retained): “Did we fund the correct neighborhood?” (`E004`, `E005`)
- **`canonical_hit`** (boxed any perm): “Did we assemble the winner digits into a box-canonical?” (`E002`, `E020`)
- **`pack_straight_hit` / Straight**: “Did we hit exact order?” (`E001`)
- **`CoverAll+NoBoxPerm`**: “We had all 3 digits somewhere, but didn’t pick any winning permutation” (`E002`)

If you learn to interpret these 4, you can diagnose 80% of what matters.

---

## 2) Decision table (symptom → meaning → what to do)

Each row tells you: **what you see**, **what it means**, and the **next best action**.

### A) Retention / lane allocation problems (we dropped the neighborhood)

**If you see**
- `CU union vtrac_index_hit` is high, but **B36 `index_hit` is much lower**, or
- `CU_LANE_BUT_PLAY_MISS` is non-trivial (conversion scoreboard)

**Meaning (plain English)**
- The tools/CU *knew the right lane*, but the B36 spend didn’t fund it. This is the “budget geometry” bottleneck (`E004`, `E005`).

**Do next**
- Compare strategies using conversion scoreboards and prefer the one with **lower `CU_LANE_BUT_PLAY_MISS`** (even if straight stays flat for now).
- Treat “top lanes only” policies as fragile; shoulder lanes matter (`E005`).

**Evidence**
- `E004`, `E005`, `E019`, `E026`

---

### B) Within-lane conversion problems (we funded the lane, but didn’t close it)

**If you see**
- `index_hit` is decent, but `canonical_hit` is low, or
- Winner-lane depth is thin (low `pct(in>=6)`), or
- You keep getting **lane hits without box hits**

**Meaning**
- You were in the right VTRAC family, but you didn’t spend enough lines **inside that lane** to include the winner canonical/perms (`E006`).

**Do next**
- Prefer a conversion policy that increases **within-lane depth** (without over-committing to only the top 1–2 lanes).
- On double-heavy days, prioritize closure rules that exploit doubles/mirror structure (cheaper closure) (`E003`, `E014`, `E020`, `E023`).

**Evidence**
- `E006`, `E020`, `E003`, `E014`, `E023`

---

### C) Digit-assembly problems (we saw digits, failed to assemble a winning permutation)

**If you see**
- `DigitCoverAll` is high and `CoverAll+NoBoxPerm` is high (Portfolio vs Results report)

**Meaning**
- This is the signature “we basically had it, but didn’t assemble it” miss (`E002`).

**Do next**
- Treat this as a **combination-forming / closure** problem, not a “rank” problem.
- Prefer policies that explicitly add compact closure in-lane (mirror-pairs / doubles closure) rather than widening to unrelated lanes.

**Evidence**
- `E002`, `E020`

---

### D) Straight is low but boxed(any perm) is improving (you’re at the right layer)

**If you see**
- `canonical_hit` improves, but Straight stays roughly flat

**Meaning**
- You’re improving **canonical conversion**, but straight requires another layer: **permutation targeting** (VTRAC-straight / ordered-pattern logic), which is not fully expressed by tool_only B36 yet (`E001`).

**Do next**
- Track progress in this order: `index_hit` → `canonical_hit` → Straight.
- Don’t panic if Straight is stubborn while canonical is moving; it’s a normal “harder metric” staircase (`E001`).

**Evidence**
- `E001`, `E002`

---

### E) Ranking confusion (rank isn’t correlating with hits)

**If you see**
- Top3 lift is ≈1.0 (or even <1) for strict metrics

**Meaning**
- That is expected today: portfolio rank is triage, not a conversion guarantee (`E007`).

**Do next**
- Use rank to decide **where to look**, not **what will hit**.
- If you want a “play threshold”, base it on **posture signals** (tight/loose regime) and **conversion readiness** (lane retention + depth), not rank alone (`E021`, `E024`).

**Evidence**
- `E007`, `E021`, `E024`

---

### F) Environment is noisy (don’t force a win)

**If you see**
- Weak convergence signals, low lane retention, lots of “loud misses” / dominant-lane negatives

**Meaning**
- Not every day/state has a clean “low-set isolate” path; posture matters (`E024`, `E026`).

**Do next**
- Treat “skip / tiny hedge / broad cheap probe” as an explicit posture, not a failure (`E021`, `E024`).

**Evidence**
- `E021`, `E024`, `E026`

---

## 3) Exactly which artifacts answer each question (fast map)

- “Did we fund the winner lane?” → `__CONVERSION_SCOREBOARD__` (`index_hit`, `CU_LANE_BUT_PLAY_MISS`)
- “Did we assemble the canonical?” → `__CONVERSION_SCOREBOARD__` (`canonical_hit`) + `__PORTFOLIO_VS_RESULTS__` (boxed any perm)
- “Is it digit-assembly?” → `__PORTFOLIO_VS_RESULTS__` (`CoverAll+NoBoxPerm`)
- “Is it a doubles regime?” → `__PORTFOLIO_VS_RESULTS__` (Doubles lens table)
- “Should I deep dive this state?” → `__PORTFOLIO_VS_RESULTS__` (State leaderboard) + the Predictive Portfolio (rank as triage)

---

## 4) Operator goal ladder (so you feel progress)

If you’re looking for a “we’re getting closer” signal, measure in this order:

1) **Lane retention** rises (`index_hit`)
2) **Canonical conversion** rises (`canonical_hit`)
3) **Straight** rises (hardest, slowest)

This ladder is consistent with the training logic: first locate the correct neighborhood, then close it, then tighten permutations.

---

## 5) Lever map (where changes actually live)

Purpose: make it obvious **what you would change**, **where it lives**, and **how you’d verify it**.

| Lever (plain English) | Pipeline layer | What it changes | Where you see it (open these) | How you measure it | Evidence |
|---|---|---|---|---|---|
| **Triage / “where do I look?”** | Ranking/Triage | State order + context snapshot | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md` | Does *attention* go to tighter states? (Not a hit promise.) | `E007`, Phase‑3 regime tags |
| **Candidate pool breadth** | Recall (CU) | Which canonicals/lanes are even eligible | `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json` + `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv` | CU “contains winner lane?” (pre‑condition for everything else) | `E004`, `E010–E012`, `E018` |
| **Lane allocation geometry** | Retention (into B36) | Which VTRAC indices get funded at all | `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json` (B36 vtrac pack) + lane allocation reports (`__LANE_ALLOCATION__*.md`) | `CU_LANE_BUT_PLAY_MISS` drops; `index_hit` rises | `E004`, `E005`, `E019`, `E026` |
| **Within‑lane closure** | Conversion (within lane) | Whether we “close” the funded lane (esp doubles/mirrors) | `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__dc1.json` (B36 closure trace) | `canonical_hit` rises without collapsing `index_hit` | `E002`, `E003`, `E020`, `E023` |
| **Permutation targeting (Straight)** | Conversion (hardest) | Turning “canonical right” into exact order | (Today: mostly diagnostic; not fully encoded in tool_only B36) | Straight lift vs random improves *after* canonical improves | `E001`, `E006` |
| **Posture (play / hedge / skip)** | Spend/Profitability | Whether you spend at all (and how much) | SSOT tags/anchors: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md` + posture buckets: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md` | Cost‑adjusted EV improves even if raw hit% doesn’t | `E009`, `E021`, `E024`, `E027` |

If you want the “one sentence summary”:
- **Tools/CU decide what’s possible.**  
- **Play cards decide what you actually funded.**  
- Most pain is in the last two rows: **lane allocation + within‑lane closure**.
