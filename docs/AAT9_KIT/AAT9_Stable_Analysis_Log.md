# AAT9 — Stable Analysis Log

Purpose: capture reverse-engineering notes for each (state, date) run so we can spot which Stable features/weights consistently precede wins. Every entry follows the agreed template (winner overlay → Stable evidence → Top-30 context → takeaways) and tags whether the hit was exact straight, exact boxed, or V-TRAC family aligned.

---

## 2025-06-24 — Connecticut4 (Midday 494 / Evening 858)

### A) Winner Overlay (V-TRAC HTML)
- **VT index 35 (494 straight):** Combined table shows canonical `449` rolling from Set3→Set1 down columns 7→1; Set1 Draws 2–6 light up Column 2/** and Column 1/** repeatedly, with column-2 hits carrying double stars before the winner collapses into Column 1 (reports/stable/winners_by_date/2025-06-24/Connecticut4/Connecticut4_vtrac35_winner_494_20251113_025703.html).
- **VT index 13 (858 → canonical 588):** Heat concentrates around Combined Set1 column 4 (8 hits) and column 5 (9 hits) with only a handful of column-2 touches; most cells stay at 0–1 star, so the path is “settled” rather than spiking into ** range (reports/stable/winners_by_date/2025-06-24/Connecticut4/Connecticut4_vtrac13_winner_858_20251113_025703.html).
- **Consensus/mirror context:** 494’s ladders carry mirrored 44/99 streaks plus column-2 consensus blocks, while 858 rides the 58*/85* mirror pairs without much consensus support. VT references stay tight: 494 lives inside vtrac35 double-mirror families; 858 sits in vtrac13 (5/8/0/3 family) but rarely forms VT-straight lanes in the HTML.

### B) Stable Spotlight & Compound Evidence
- **Row scores:** Canonical `449` rows peak at `score=16` with `score_straight=6`, `score_hot=2`, and `score_vtrac_straight=2`, yet hot levels drop back to `hot=0–1` whenever the pattern reaches Column 1 (`data/outputs/analysis/patterns/Connecticut4/Connecticut4_stable_patterns_scores.csv`).
- **Compound ranks:** `449`’s best Combined compound score is only `20.5` (rank ~102) because `col1_hits=0`, `hot2_count=0`, and chain depth never incremented beyond `set_chain=2 / draw_chain=0` despite the HTML showing Column 1 landings all the way through Draw6 (`..._compound.csv`).
- **Evening winner (`588` canonical):** Stable only emitted Combined rows (scores 12/10/9) with `score_hot=0/1`, `score_cons=0`, and no direct VT-straight hits even though vtrac13 highlights padded 9244/92446 trails. Compound score `16.5` similarly lacked `col1_hits` or `hot2_count`, so the signal failed to bubble up.
- **Spotlight coverage:** Winner spotlight CSV tagged the 494 permutations as exact-boxed hits (family_canonical_3v=449) but produced no rows for raw `858`—only the canonical `588` entries—so evening hits currently surface as family/VTRAC relations rather than literal 858 entries (`.../Connecticut4_winner_family_spotlight_raw.csv`).

### C) Top-30 / Compound Context
- Combined Top-30 remains dominated by the 244/447/446 families (scores 27–36) with rich `hot2` counts and VT-straight hits (see `compound_top5.py` output), so neither 449 nor 588 appears in the leaderboard even though both numbers sat inside the same column-1 funnels as those leaders.
- Compound Top-5 for Combined (447/244/446/4467/44) all carry `col1_hits>=4` plus double-digit hot2 counts and explicit VT-straight tallies (data/outputs/analysis/patterns/Connecticut4/Connecticut4_stable_patterns_compound.csv).
- False positives: canonicals like `688` and `6788` scored >90 compound despite missing winners because the weights heavily reward extended double-mirror streaks in Column 1; they drown out the 449/588 families that lacked the same `col1` bookkeeping.

### D) Takeaways & Next Actions
- Stable under-credits column-1 arrivals when the path uses Column 2 → Column 1 (449 chain) versus landing straight in Column 1. Need to treat “Column 2 with ** followed by Column 1 *” as equivalent evidence for compound + row scoring.
- Winner spotlight should include raw 858 rows (and is_exact_boxed/straight flags) so we don’t lose track of literal evening hits when only the canonical 588 is logged.
- Consider boosting `score_hot`/compound weights when a canonical carries consecutive double-star cells even if the numeric `hot2_count` lives in Column 2 (current contract ignores those transitions).
- Capture VT straight alignment better: 494 had `score_vtrac_straight=2` yet compound rank stayed >100; raising the contribution or adding a “VT-lane near Column 2→1” bonus would make these straight-lane hits visible before we rely on Control Center.

---

## 2025-06-24 — Indiana4 (Midday 273 / Evening 167)

### A) Winner Overlay (V-TRAC HTML)
- **VT index 27 (273 straight):** Combined Set1 column 3 lights up from Draw1–5 with alternating * and **, then the family slides into column 2 (***) before a single column-1 hit at Draw7 (reports/stable/winners_by_date/2025-06-24/Indiana4/Indiana4_vtrac27_winner_273_20251113_025705.html). It is a textbook Set3→Set1 chain hugging middle columns before tipping into column 1 right before the hit.
- **VT index 17 (167 straight):** Combined table spreads across columns 4–5 with occasional column 1/2 echoes; only three cells hit ** (column 1 twice, column 2 once). Mirror pairs (16/61) and hidden 167 cores appear mainly in Set1 rows (reports/.../Indiana4_vtrac17_winner_167_20251113_025705.html).
- **Permutation cues:** The 273 family is represented as canonical 237 all along the ladder (R2/R4 sequences), meaning VT paths and Stable rows agree on the same 3-value order; the 167 hit shows up as 167/6677 permutation clusters with minimal consensus support.

-### B) Stable Spotlight & Compound Evidence
- **Canonical 237:** Row scores sit at 20–24 with strong `score_straight` + `score_vtrac_straight` (2) and active `score_hot` whenever the ladder touched column 3→2. Evening compound entries peak at `37.5` (set_chain=3, draw_chain=2, col1_hits=1, vstr=3) but the Combined compound row is only `8.5` with `draw_chain=1` because the aggregation drops the Set1 column‑3 → column‑2 persistence that is obvious in the HTML.
- **Canonical 167:** Only one spotlight row exists (Evening Set1 Draw2 Column5) with `score=7.5`, `score_straight=6`, `score_hot=0`, and no VT-straight credit even though V-TRAC index 17 is purely a straight lane. Compound score stagnated at `8` with `draw_chain1`, failing to acknowledge the mirrored 1677 tail repeated in columns 4/5.
- **Spotlight completeness:** Winner spotlight CSV captured the canonical 167 hit but emitted zero rows for raw `273`; everything is stored under `raw_canonical` values like 237/23377. We need per-draw metadata that calls out which permutations correspond to the actual published numbers so analysis isn’t forced to translate.

### C) Top-30 / Compound Context
- Combined Top-5 compound canonicals (`24`, `468`, `688`, `246`, `68`) all have `col1_hits≥3` and `hot1_count>5`, so 237/167 never get close even though the 237 ladder actually touches column 1 late in Draw7 (data/outputs/analysis/patterns/Indiana4/Indiana4_stable_patterns_compound.csv).
- Top-30 score list is likewise dominated by double families (224/223/226) with consensus bonuses; 237/167 don’t appear in the first 30 rows of `Indiana4_stable_patterns_scores.csv`, reinforcing that the current weights over-index on consensus/double cues relative to VT-straight evidence.
- False positives include `24` and `468` (Compound 66 & 50) which never translated into wins on 6/24 but consumed the top ranks thanks to long-standing hot streaks.

### D) Takeaways & Next Actions
- Stable correctly identifies VT-straight evidence for 237 but the Combined compound writer collapses the draw chain back to 1; need to reconcile the row-level chain metrics with the compound aggregation so Set1 column‑3 → column‑2 cascades boost compound_score.
- Extend spotlight output to carry the literal published number (273) alongside the canonical/permutation fields; otherwise we have to reverse-map digits every time we log an example.
- Increase visibility of “column 3 funnel into column 2/1” patterns—both 273 and 167 winners used that path, yet compound scoring only rewards direct column-1 persistence. A derived metric like “column2_to_col1_hits” or “pre-col1 chain” would help.
- Evening 167 hit highlights hidden3v coverage rather than consensus or VT lanes; we should log hidden-core occurrences in the analysis doc and consider bumping their score contribution so these stealth wins migrate upward without adding noise.

---

## 2025-06-24 — Florida4 (Midday 733 / Evening 271)

### A) Winner Overlay (V-TRAC HTML)
- **VT index 29 (733 straight):** Combined Set1 is saturated—43 hits in column 1 and 34 in column 2, with 67 double-star cells overall as the family snakes from column 6→1 before the win (reports/stable/winners_by_date/2025-06-24/Florida4/Florida4_vtrac29_winner_733_20251113_025704.html). It’s the most column‑1‑heavy ladder we’ve logged so far.
- **VT index 20 (271 straight → family 127):** Combined Set1 spreads across columns 4–5 (11 hits in column 5) while column‑1 only lights five times; VT lane lives mostly in the hidden 677/177 permutations, mirroring the Control Center view (reports/.../Florida4_vtrac20_winner_271_20251113_025704.html).
- **Permutation cues:** Spotlight shows the 733 hit as canonical 337/3377 ladders, but the literal 733 never appears—everything is already folded into the extended strings (677?, 337?). Evening 271 is represented via 677/177/2266 entries, so we have to map back to the published number manually.

### B) Stable Spotlight & Compound Evidence
- **Canonical 337 (midday winner):** Stable only produced Evening rows (score 22–24 with high `score_hot` and `score_vtrac_straight`), so the Combined ledger never saw this canonical. Compound’s best entry is `40.5` in Evening with `col1_hits=4`, but no Combined record means the midday straight never ranks despite dominating the column-1 funnel.
- **Canonical 677 / 177 (evening winner family):** Combined rows carry scores ~13–15 with `score_hot=1`, `score_vtrac_straight=2`, and `score_persistence_draw=2`, yet the Combined compound rank is still 67 (compound=27.5, `col1_hits=1`). The boxed 177 permutations fare slightly better (rank 30, compound=34.5) because they trigger `set_chain3` bonuses, not because of explicit VT evidence.
- **Spotlight completeness:** Winner spotlight CSV only lists canonical permutations (677/177/2266) with `family_canonical_3v=127`; raw columns for literal 733/271 remain empty, which complicates example logging and hides whether we landed an exact straight vs. VT-boxed hit.

### C) Top-30 / Compound Context
- Combined Top-5 is overloaded with high double families (788/688/889) thanks to huge double-mirror counts (compound_top5 output); none of the 733 permutations crack the top 30 even though they owned Column 1.
- Canonical 177 barely slides into Combined rank 30 while canonical 677 stays in the mid-60s, underscoring that boxed evidence is rewarded far more than the straight lane that actually hit.
- False positives: 788 (Combined compound 105) and 688 (95.5) never converted to winners on 6/24 but still control the leaderboard because the weights prioritize sustained double-mirror streaks on column 1, regardless of VT alignment.

### D) Takeaways & Next Actions
- Combined aggregation must ingest the Evening and Midday rows equally; otherwise midday straits (like 733) never surface in the Combined ledger even when the HTML shows overwhelming evidence.
- Spotlight/CSV outputs should record the literal winning numbers (733, 271) with `is_exact_straight` / `is_vtrac_boxed` flags so we can log exact hits without decoding permutations.
- Consider adding a “column1 dominance” bonus that depends on star density rather than `col1_hits` counts—733’s ladder has 40+ column‑1 cells but only increments `col1_hits` by 1 in compound because it only counts unique draws.
- Review compound weights for VT-straight hits; canonical 677 only receives +1 to `compound_score` per VT lane, which is not enough to compete with double family stacks.

---

## 2025-06-24 — OntarioCanada4 (Midday 290 / Evening 771)

### A) Winner Overlay (V-TRAC HTML)
- **VT index 12 (290 straight):** Combined Set1 column 1 is hit 47 times with constant ** tails from Draw3–6; columns 2/3 also carry 35 and 38 hits respectively (reports/stable/winners_by_date/2025-06-24/OntarioCanada4/OntarioCanada4_vtrac12_winner_290_20251113_025712.html). The ladder is a textbook Set3→Set1 collapse into column 1.
- **VT index 20 (771 straight):** Much sparser—column 5 (5 hits) and column 3 (6 hits) do most of the work while column 1 never illuminates (reports/.../OntarioCanada4_vtrac20_winner_771_20251113_025713.html). The hit relies more on VT-lane evidence than on hot-column persistence.
- **Permutation cues:** Family 12 (canonical 29) uses permutations like 259/2249; family 20 (canonical 177) surfaces as 226/677 permutations, so we need to keep linking them back to 290/771 in the log.

### B) Stable Spotlight & Compound Evidence
- **Family 12 (midday winner):** Combined rows for canonical 259 score 21–23 with `score_persistence_draw=4`, `score_hot=2`, and appear multiple times across Draw3–5. Compound scores land in the mid‑40s (`compound_score=48.5`, `col1_hits=5`, `hot2_count=6`, `vtrac_straight_hits=3`), so Stable already ranks the winner near the top; this is our baseline for “ideal” alignment.
- **Family 20 (evening winner):** Canonical 226/677 rows only score in the 12–15 range inside Combined, and compound stays ≤23.5 unless we look at Midday-only entries where `compound_score` spikes to 38 due to long set chains. V-TRAC perks exist (`vtrac_straight_hits=3`), but lack of column‑1 landings keeps Combined ranks low.
- **Spotlight coverage:** Unlike Florida, the Ontario spotlight lists dozens of rows for both families, so exact-vs-variant hits are easy to tag—this run is perfect for documenting the “good” pipeline behavior.

### C) Top-30 / Compound Context
- Combined Top-5 is still ruled by the “always-hot” canonicals (9/5/4/49/59), but family 12 permutations sit immediately behind them with compound 44–48, proving that Stable will surface the 290 family as soon as we scroll beyond the first handful of rows.
- Family 20 permutations never reach Combined Top-30 even though they post `compound_score≈23`; instead the upper ranks are occupied by the column‑1 powerhouses above. This highlights the gap between VT-lane hits (771) and column‑1 heat.
- False positives remain the extremely persistent column‑1 loops (canonical 9/5) that did not hit on 6/24 but still score >90 because they satisfy every hot/double metric.

### D) Takeaways & Next Actions
- Use the 290 example as the “gold” reference: every feature (column-1 persistence, hot2 count, VT-straight hits) aligned and the log captures it cleanly. Future tuning should keep this behavior untouched.
- Evening 771 shows that VT-only signals still fall behind when `col1_hits` stays at zero; consider adding a smaller compound bonus for VT lanes that hover in columns 3–5 so they aren’t buried.
- Maintain the habit of tagging family_id + literal number in the analysis log—the Ontario run demonstrates how quickly we can reason about hits when both are present.

---

## Cross-run Insights & Follow-ups (2025-06-24 batch)
- **Literal winner visibility:** Spotlight CSVs must emit the exact Midday/Evening numbers (733, 271, 494, 858, 273, 290, etc.) with `is_exact_{straight,boxed}` and `is_vtrac_boxed` so we stop reverse-mapping permutations during analysis. This likely means extending the writers in `alpha_analytical/stable/post_pass_families.py`.
- **Column‑2 → Column‑1 funnels:** Connecticut and Indiana showed repeated ** hits in column 2 right before collapsing into column 1, yet compound scoring ignored them because `col1_hits` only counts distinct column‑1 rows. Introduce a derived metric (e.g., `pre_col1_funnel` or “adjacent column1 streak”) that boosts both row and compound scores when Column 2 carries consecutive stars before landing in Column 1.
- **Combined coverage gaps:** Florida’s canonical `337` rows only exist in Evening even though the midday winner is straight. Need to audit the Combined aggregation so all variants are represented (likely a regression in the multi-variant ingest) and add a contract check that ensures every spotlighted canonical has a Combined row.
- **VT-lane weighting outside column 1:** Ontario’s 771 and Florida’s 271 rely on VT-straight lanes across columns 3–5, but compound only adds +1 for those hits. We should bump the VT-straight contribution (or add a “mid-column VT lane” term) so these winners don’t trail behind the double-mirror families that dominate column 1.
- **Documentation/workflow:** Analysis runs now live here (`docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md`). Every new batch should append entries plus an updated “Insights & Follow-ups” list so future sessions restart from a single source.

---

## 2025-06-24 — Extended State Sweep (Delaware → Virginia)

After landing the literal-logging and compound upgrades, we reran the full roster of tracked states (sharepacks under `sharepacks/2025-06-24/<STATE>/`). The table below captures the new best-compound ranks; dashes indicate the winner still failed to surface in Combined.

| State | Midday Winner (Best Compound Rank) | Evening Winner (Best Compound Rank) |
| --- | --- | --- |
| Connecticut4 | 494 (#305) | 858 (#590) |
| Delaware4 | 999 (-) | 271 (-) |
| Florida4 | 733 (#60) | 271 (-) |
| Indiana4 | 273 (#31) | 167 (#1684) |
| Michigan4 | 106 (-) | 213 (-) |
| NewJersey4 | 229 (#96) | 431 (#1616) |
| NewYork4 | 885 (-) | 587 (-) |
| NorthCarolina4 | 562 (#1296) | 682 (#722) |
| Ohio4 | 697 (-) | 403 (#432) |
| OntarioCanada4 | 290 (#86) | 771 (#564) |
| Pennsylvania4 | 893 (#13) | 222 (-) |
| PuertoRico4 | 138 (#293) | 070 (#3) |
| SouthCarolina4 | 005 (#457) | 584 (#911) |
| Virginia4 | 188 (#847) | 775 (#197, vt_only_lane=True) |

### Highlights & Notes
- **VT-only bonus firing:** Virginia’s evening 775 straight hit arrived purely through the VT lane; after the new vt-only boost it climbs to rank #197 (vs previously buried in the thousands). No other winner triggered the vt-only flag yet, confirming the guardrails keep the boost narrow.
- **Funnel metric ready:** None of the new winners exhibited the full “col2 ** then col1 hit” funnel in Set1, but the `funnel_precol1` column is now present in every sharepack so future examples can prove out the bonus.
- **High performers:** Pennsylvania’s midday 893 now sits at #13, Puerto Rico’s evening 070 at #3, and Florida’s midday 733 at #60—these are the reference runs we’ll use when tuning cross-tool weights.
- **Still outstanding:** VT-heavy winners with little column‑1 presence (Delaware 271, Florida 271, Michigan 213, New York 587, etc.) remain off the board despite the vt-only hook because they still retain hot2/col1 traces. These should be the first candidates when we resume tuning after the Analyzer integration.
- **Sharepacks:** Each state subfolder includes the updated metrics JSON (with `winner_hits`), the new compound CSV columns (`funnel_precol1`, `vt_only_lane`), fresh winners HTML, and `README.md` documenting the exact commands/labels.

Next action is to fold these results back into the cross-tool Analyzer work: now that every state/date run is packaged, we can script summaries (e.g., winner rank histograms) and feed them into the weight calibration discussions described in `stable_plan.txt`.

---

## 2025-06-23 — Extended State Sweep (Connecticut4 → Virginia4)

Using the prior workbook (Pick3StatsC4_2025-06-22.xlsm) we regenerated tables, reran Stable for the full roster, and published unzipped sharepacks under `sharepacks/2025-06-23/<STATE>/` plus a consolidated winners map (`winners/2025-06-23/2025-06-23_winners_map.{json,csv}`). The table below shows the new winner ranks with the updated contract (`funnel_precol1`, `vt_only_lane`, literal hits, health metrics).

| State | Midday Winner (Best Compound Rank) | Evening Winner (Best Compound Rank) |
| --- | --- | --- |
| Connecticut4 | 130 (#988) | 938 (#510) |
| Delaware4 | 669 (#1020) | 919 (#57) |
| Florida4 | 665 (#115) | 465 (#362) |
| Indiana4 | 110 (#46) | 032 (#510) |
| Michigan4 | 392 (#349) | 964 (#184) |
| NewJersey4 | 106 (#81) | 152 (#976) |
| NewYork4 | 638 (#322) | 767 (#421) |
| NorthCarolina4 | 920 (#521) | 145 (#23) |
| Ohio4 | 734 (#92) | 368 (#298) |
| OntarioCanada4 | 325 (-) | 438 (#1314) |
| Pennsylvania4 | 164 (-) | 040 (#177) |
| PuertoRico4 | 858 (-) | 454 (#116) |
| SouthCarolina4 | 958 (#141) | 314 (#81) |
| Virginia4 | 579 (-) | 385 (#317) |

### Highlights & Notes
- **First vt-only confirmation outside Virginia:** Ohio’s midday 734 fired the `vt_only_lane=True` flag (`best_compound_rank` #92) with zero column‑1 hits, validating the bonus logic on a new state/date.
- **Funnel metric exercised:** Florida’s evening 465 posted `funnel_precol1=1`, showing how column‑2 star surges preceding a column‑1 landing are now recorded in the sharepacks for downstream weighting.
- **Top-rank standouts:** Indiana’s midday 110 (#46) and North Carolina’s evening 145 (#23) both climbed into the Combined Top‑50; these will anchor the Analyzer regression set for mid-tier performers.
- **Coverage gaps documented:** Ontario (325), Pennsylvania (164), Puerto Rico (858), and Virginia (579) still lack Combined rows for the midday winners; the new `validate_stable_schema.py` check will catch these regressions automatically when the tables issue is addressed.
- **Artifacts ready for Analyzer:** Every state/date folder now includes the Lean bundle + README + headers snapshot, and the winners module prototype can ingest both the 2025-06-24 and 2025-06-23 maps without additional wiring.

---
