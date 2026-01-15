# Aux — v0 Audit (Cases)

Purpose: complement `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md` with concrete examples showing **when Aux helps**, **how it helps**, and **where it tends to fail** in the current v0.2 (tool‑first) consumption path.

Non‑negotiables (v0 synthesis sprint):
- No analyzer edits (Stable/DR/VTRAC/HZ).
- Baseline is `--profile tool_only` (Profit Alerts quarantined).
- Predictive “before” packs are treated as the pre‑results evidence source: `sharepacks/_predictive/<D>/...`.

Definitions used below:
- **Aux-only canonical hit**: the winning canonical appears in at least one **Aux-derived pack’s** `canonicals`, and appears in **zero** non‑Aux packs’ `canonicals` (tool_only Candidate Universe).
- **As‑consumed hit**: the winning literal appears in the pack’s `combos` (what a strict STRAIGHT would hit).
- **PlayCard B12 hit**: the budgeted `play_box_first` B12 card hits (this is the closest thing to “what we would have played”, but still an experiment).

---

## Case set A — Aux-only canonical coverage (v0 window)

These are the most important cases for the “do we need Aux?” question.

In each row below:
- the winner canonical is present in at least one Aux-derived pack, and
- the winner canonical is present in **no** non‑Aux packs (tool_only).

| Date | State | Draw | Winner | Canon | idx | Aux methods | Aux pack_ids | As-consumed hit | PlayCard B12 hit |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| 2026-01-05 | Florida4 | Evening | 994 | 499 | 35 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Evening:idx=35 | ✅ | ❌ |
| 2026-01-05 | Florida4 | Midday | 080 | 008 | 4 | due_doubles (+ mirrors) | due_doubles:Combined; due_doubles:Evening; due_doubles:Midday; due_doubles_mirror_single:Combined:seed=003; due_doubles_mirror_single:Evening:seed=003; due_doubles_mirror_single:Midday:seed=003 | ✅ | ✅ |
| 2026-01-05 | Michigan4 | Evening | 772 | 277 | 26 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Midday:idx=26 | ✅ | ❌ |
| 2026-01-06 | Delaware4 | Midday | 165 | 156 | 6 | mirror_pair_closure | mirror_pair_closure:pair=1/6 | ✅ | ❌ |
| 2026-01-06 | Michigan4 | Midday | 618 | 168 | 18 | mirror_pair_closure | mirror_pair_closure:pair=1/6 | ✅ | ❌ |
| 2026-01-06 | NewYork4 | Midday | 181 | 118 | 18 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Combined:idx=18; aux_vtrac_index_overdue:Evening:idx=18 | ✅ | ❌ |
| 2026-01-08 | Indiana4 | Evening | 242 | 224 | 28 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Combined:idx=28 | ✅ | ❌ |
| 2026-01-08 | OntarioCanada4 | Evening | 498 | 489 | 34 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Midday:idx=34 | ✅ | ❌ |
| 2026-01-08 | SouthCarolina4 | Midday | 277 | 277 | 26 | aux_vtrac_index_overdue | aux_vtrac_index_overdue:Midday:idx=26 | ✅ | ❌ |
| 2026-01-09 | NewJersey4 | Midday | 287 | 278 | 27 | mirror_pair_closure | mirror_pair_closure:pair=2/7 | ✅ | ❌ |
| 2026-01-09 | NewYork4 | Evening | 835 | 358 | 13 | mirror_pair_closure | mirror_pair_closure:pair=3/8 | ✅ | ❌ |
| 2026-01-09 | Ohio4 | Evening | 090 | 009 | 5 | due_doubles (+ mirrors) | due_doubles:Combined; due_doubles:Evening; due_doubles:Midday; due_doubles_mirror_double:Combined:seed=009; due_doubles_mirror_double:Evening:seed=009; due_doubles_mirror_double:Midday:seed=009; due_doubles_mirror_single:Combined:seed=009; due_doubles_mirror_single:Evening:seed=009; due_doubles_mirror_single:Midday:seed=009 | ✅ | ✅ |
| 2026-01-09 | Ohio4 | Midday | 785 | 578 | 11 | aux_positional | aux_positional_shortlist | ❌ | ❌ |

Key observation:
- Aux-only canonical coverage exists and is non-trivial (delta `+13` box‑equivalent hits in the v0 window; see `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md`).
- But **PlayCard B12** only converts `2/13` of these Aux-only cases into actual hits.
  - This strongly suggests the bottleneck is the **budget/selection policy**, not “Aux signal doesn’t exist”.

---

## Case set B — Aux corroborates other tool evidence (canonical overlap)

These are cases where the winner canonical appears in both:
- at least one Aux pack, and
- at least one non‑Aux pack.

| Date | State | Draw | Winner | Canon | idx | Aux packs | Non-aux packs | PlayCard B12 hit |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 2026-01-05 | NewYork4 | Midday | 080 | 008 | 4 | 1 | 3 | ✅ |
| 2026-01-05 | PuertoRico4 | Midday | 732 | 237 | 27 | 2 | 1 | ❌ |
| 2026-01-07 | Virginia4 | Evening | 990 | 099 | 15 | 1 | 1 | ❌ |
| 2026-01-08 | NewJersey4 | Evening | 055 | 055 | 1 | 1 | 1 | ❌ |
| 2026-01-08 | NewJersey4 | Midday | 089 | 089 | 14 | 1 | 1 | ❌ |
| 2026-01-08 | OntarioCanada4 | Midday | 022 | 022 | 10 | 1 | 1 | ✅ |
| 2026-01-09 | NorthCarolina4 | Evening | 960 | 069 | 9 | 1 | 3 | ❌ |
| 2026-01-09 | PuertoRico4 | Evening | 225 | 225 | 10 | 5 | 2 | ✅ |

Observation:
- These are the “good” candidates for v0.2: multiple lenses agree on the same canonical.
- Even here, B12 conversion is limited (`3/8`), which again points to budget policy / allocation decisions.

---

## Deep dives (representative)

These are not meant to be exhaustive; they are “pattern exemplars” for consumption decisions.

### A) `aux_vtrac_index_overdue` behaves like bounded index closure (often missed by B12)

Example: `2026-01-05 Florida4 Evening` winner `994` (canon `499`, idx `35`)
- Predictive pack evidence:
  - CU pack: `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe__tool_only.json` → `pack_id=aux_vtrac_index_overdue:Evening:idx=35`
  - Aux evidence: `sharepacks/_predictive/2026-01-05/Florida4/aux/Florida4/summary.json`
  - Pack semantics:
    - `why_tags` includes `idx:35` + `ds:681` (very overdue), and the pack is already a compact closure set: `449/494/944 + 499/949/994`.
- Post-results confirmation:
  - Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Florida4.md`
- B12 conversion:
  - `play_box_first` B12 (tool_only) missed this winner: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PLAY_CARD_GRADE__tool_only.csv`.

Interpretation:
- This is the “lane exists pre-results; our budgeted cut didn’t allocate to it” failure mode.
- v0.2 implication: treat `aux_vtrac_index_overdue` as a **priority closure candidate** (at least 1 boxed canonical per top overdue index) rather than a “nice to have” pack.

Example: `2026-01-08 Indiana4 Evening` winner `242` (canon `224`, idx `28`)
- Predictive CU: `sharepacks/_predictive/2026-01-08/Indiana4/candidate_universe__tool_only.json` → `pack_id=aux_vtrac_index_overdue:Combined:idx=28`
- B12 conversion: missed (`docs/.../2026-01-08__PLAY_CARD_GRADE__tool_only.csv`).

---

### B) `mirror_pair_closure` is a “conversion helper” (stronger than the due-doubles mirror expansions in v0)

Example: `2026-01-06 Delaware4 Midday` winner `165` (canon `156`, idx `6`)
- Predictive CU: `sharepacks/_predictive/2026-01-06/Delaware4/candidate_universe__tool_only.json` → `pack_id=mirror_pair_closure:pair=1/6`
- Pack behavior:
  - BOX pack (`n=18`), seeded from Aux aggregated digits and VTRAC-pair mirror pairing, then third-digit closure.
- B12 conversion: missed (even though the closure set is bounded): `docs/.../2026-01-06__PLAY_CARD_GRADE__tool_only.csv`.

Example: `2026-01-09 NewYork4 Evening` winner `835` (canon `358`, idx `13`)
- Predictive CU: `sharepacks/_predictive/2026-01-09/NewYork4/candidate_universe__tool_only.json` → `pack_id=mirror_pair_closure:pair=3/8`
- B12 conversion: missed.

Interpretation:
- These are “lane-correct → canonical-correct” converters, but the selection layer has to actually reserve budget for them.
- v0.2 implication: treat `mirror_pair_closure` as a first-class “index→box conversion” pack (especially on mirror-double days).

---

### C) `due_doubles` (+ mirror expansions) produces compact, cheap closures (and sometimes hits directly)

Example: `2026-01-05 Florida4 Midday` winner `080` (canon `008`, idx `4`)
- Predictive CU: `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe__tool_only.json`
  - `pack_id=due_doubles:*` includes `080` directly.
  - `pack_id=due_doubles_mirror_single:*:seed=003` includes `{003,008}` boxed permutations.
- B12 conversion: hit (`docs/.../2026-01-05__PLAY_CARD_GRADE__tool_only.csv`).

Example: `2026-01-09 Ohio4 Evening` winner `090` (canon `009`, idx `5`)
- Predictive CU: `sharepacks/_predictive/2026-01-09/Ohio4/candidate_universe__tool_only.json`
  - `due_doubles` includes `009/090/900` and other compact doubles.
  - Mirror expansions (`due_doubles_mirror_single` / `due_doubles_mirror_double`) also include `090` directly.
- B12 conversion: hit.

Interpretation:
- Due Doubles is already a “good citizen” in v0.2: bounded, cheap, and aligned with the system’s “reduced doubles family closure” strategy.

---

### D) `aux_positional` is not a strict straight caller (but can carry useful canonicals)

Example: `2026-01-09 Ohio4 Midday` winner `785` (canon `578`, idx `11`)
- Predictive CU: `sharepacks/_predictive/2026-01-09/Ohio4/candidate_universe__tool_only.json` → `pack_id=aux_positional_shortlist`
- The positional shortlist selected literal perms like `875`/`878`/`879`, but the winner literal `785` was not present.
- The winner canonical `578` *is* present in the pack’s `canonicals`, which is why Aux positional shows up in box‑equivalent rates.
- B12 conversion: missed.

Interpretation:
- `aux_positional` should be treated as a **structure lens / digit-envelope signal**, not as a primary STRAIGHT list.

---

## Caution notes (why we don’t ingest “all Aux” as prediction)

The raw signal overlap rates (not predictive packs) show several “high overlap / low specificity” traps:
- Non-repeating pairs overlap top10 ~43–49% (but this is likely “pairs are common”, not a sharp predictor).
- Repeating pairs overlap top10 ~27–35%.

Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__SIGNALS__QUANT.csv`

This is why v0.2 keeps Aux as bounded, deterministic packs (index closure, mirror closure, due doubles) rather than ingesting all Aux signals directly.

