# Master Validation Run Report — Connecticut4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/Connecticut4/`
- Winners lens: `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2025-06-22/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2025-06-22/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2025-06-22/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2025-06-22/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2025-06-22/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2025-06-22/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4/Connecticut4_vtrac13_winner_835_20251221_222109.html`
- `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4/Connecticut4_vtrac21_winner_281_20251221_222107.html`

Winners JSON files:
- `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4/Connecticut4_vtrac13_winner_835_20251221_222109.json`
- `sharepacks/2025-06-22/Connecticut4/winners/Connecticut4/Connecticut4_vtrac21_winner_281_20251221_222107.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 col1 ladders are extremely hot, but they do **not** anchor either winner.
  - Midday table (Draw1): col1 ladders are `057**` / `075**` and col2 ladders are `557**` / `755**` → no `128`/`281` lane.
  - Evening table (Draw1): col1/2 ladders are `4436** / 6344** / 3644**` → no `358`/`835` lane.
  - Combined table (Draw1): col1/2 ladders are `4488** / 8844**` → heavy 4/8 lane dominance.
- Q2: Column‑1/2 persistence is **strong** (lots of `**` and dense ladders), but it persists into *non‑winner* clusters.
  - This is a cautionary example: “col1 heat” is real, but it is not the deciding signal on this day.
- Q3: Last survivors are abundant (`ls-box`/`ls-box-edge` density is high) and mostly reinforce the dominant 0/5/7 and 4/8 lanes, not the winners.
  - The winners lens shows family/VT tagging, but neither winner appears as an explicit in‑table literal/canonical substring anywhere in the tables (see Q11).
- Q4: Variant bias:
  - Midday winner 281 (canon 128) shows its strongest family tagging in **Combined** (Set2→Set1), but still does not resolve into an explicit lane.
  - Evening winner 835 (canon 358) shows the strongest “VT‑straight lane tagging” in **Evening** (hit‑vt‑straight tags are concentrated there).
- Q5: Permutation lane clarity is **diffuse**.
  - Winner/family tagging is spread across many columns (no “tight endgame lane”), and the winners are not printed explicitly in the progression cells.
- Q6: Environment verdict: **weak / noisy**.
  - Despite hot col1/2 ladders, the day is dominated by other clusters and both winners are “cold” in the winners lens stats (0 occurrence/persistence/stability).
- Q7: Hot Zones overlap is present but weak.
  - Hot Zones marks both winners as `has_vt_straight=True`, but ranks are poor (Midday best rank 169; Evening best rank 125) and neither appears in `winner_map` (triad_present=False).
- Q8: Cross‑set carryover exists as *family pressure*, not as a winner lane.
  - Midday winner 281: Midday has hit-family carry Set3→Set1 (9→6→31), and Combined is strongest (Set2=20, Set1=49).
  - Evening winner 835: Evening has strong carryover (Set3=15, Set2=12, Set1=25); Combined also carries (Set3=10, Set2=12, Set1=37).
- Q9: Aux cues (quick lens):
  - Combined Aux VTRAC overlay shows **idx13** as the top overdue index (`ds=170`) which matches the Evening winner’s index (13). This is the only strong “structural” cue for the actual outcome.
- Q10: 4 hit criteria viability (pre‑results lens):
  - Exact boxed / Exact straight: weak for both winners (no explicit lane printing).
  - VT‑boxed / VT‑straight: the only plausible hedge path (especially Evening idx13 due-ness).
- Q11: Exact triple presence:
  - Neither `281`/`128` nor `835`/`358` appears as an explicit in-table substring in the winners lens tables (all variants). Treat this as an “off-board / non‑printed lane” day.
- Q12: Profitable environment summary:
  - Negative-control traits: very hot col1/2 ladders that do not align to winners, heavy competing clusters, and winners that are cold/undominant across stats.
  - Actionable trait (if any): structural VT pressure (idx13 overdue) can still matter even when string lanes do not print the winner.
- Q13: Dominance vs dilution:
  - Both winners have 0 stats across occurrence/persistence/stability; dominant families (e.g., 867/817 or 533/885 lanes) carry the day’s printed structure.
- Q14: Noise check:
  - Highly noisy/diluted: many competing lanes, high ls-box density, and no clean “winner lane” convergence.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — Connecticut4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2025-06-22)

## Midday winner 281 (canonical 128)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=52 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 40 rows contain digits; best rank 125, section Evening, score 25.0, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=86
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 835 (canonical 358)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=311 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 53 rows contain digits; best rank 43, section Combined, score 27.5, hot2 5
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=8
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 344 | section Evening | score 89.0 | col1_hits 8 | hot2 11
- rank    5 | canon 4488 | section Combined | score 65.5 | col1_hits 6 | hot2 11
- rank    2 | canon 488 | section Combined | score 71.5 | col1_hits 6 | hot2 11
- rank    3 | canon 448 | section Combined | score 71.0 | col1_hits 6 | hot2 11
- rank    4 | canon 446 | section Evening | score 70.0 | col1_hits 4 | hot2 7
- rank   28 | canon 3448 | section Evening | score 45.5 | col1_hits 5 | hot2 6
- rank   24 | canon 3446 | section Evening | score 48.5 | col1_hits 4 | hot2 6
- rank   32 | canon 346 | section Evening | score 44.5 | col1_hits 4 | hot2 6
- rank   32 | canon 348 | section Evening | score 44.5 | col1_hits 5 | hot2 6
- rank   13 | canon 368 | section Evening | score 56.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1382 | family 19 | score 7.0 | hot2 0 | section Midday
- rank 1382 | family 19 | score 7.0 | hot2 0 | section Midday
- rank  139 | family 20 | score 24.5 | hot2 1 | section Midday
- rank  852 | family 7 | score 14.0 | hot2 2 | section Midday
- rank 1112 | family 10 | score 11.0 | hot2 1 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday `128`: absent from `patterns_scores.csv` and `patterns_compound.csv`; only weak family presence (best family rank 125).
  - Evening `358`: absent from `patterns_scores.csv` and `patterns_compound.csv`; family presence is stronger but still not decisive (best family rank 43).
- Q2: 4 hit criteria mapping
  - Exact boxed/straight: not supported (`exact_* = False`).
  - VT-boxed: not supported directly by Stable rows (`vt_boxed=0` in spotlight for both winners).
- Q3: Winners output alignment
  - Spotlight/metrics are consistent with a miss: family rows exist, but no exact canonical rows and no exact hits.
- Q4: Dominance / noise
  - Stable’s dominant lanes are 4/8 heavy (`344`, `488`, `448`, `446`, `368`), which matches the printed col1 environment but not the winners.
- Q5: Top candidate clusters (what Stable wanted)
  - Primary: `344` (rank 1), then `488/448/446/368/346/348` style lanes.
  - Treat as “competing dominant lane” evidence, not as winner-isolators for this day.
- Q6: Miss analysis
  - Stable is doing its job (finding dominant col1/hot2 lanes), but the winners are off-board relative to those lanes.
- Q7: Validation checks (V)
  - Outputs present; no schema issues observed. Misses are performance outcomes, not pipeline corruption.
- Q8: Optimization notes
  - None to implement now; log this as a “winner cold/off-board” day for later corpus-based tuning (avoid overfitting).
- Q9: Cross-tool synergy seed
  - Stable’s `344` lane overlaps Hot Zones top lanes (rank 8) → useful synergy for lane detection, even though it missed the actual winners.
- Q10: Analyst’s extra insight
  - Stable behaves here as an environment/lane detector (4/8-heavy dominance), not as a direct caller.

---

### 2.Digit Reduction — Connecticut4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20251222)

## Midday winner 281 (canonical 128)
- Stamp (winner_stamp.json): items_total=130 | exact_any=6 exact_final=0 | vtrac_any=114 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=78 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=17 family_vtrac_final=0
- Flags (winner_flags.csv): rows=130 | exact_any=6 vtrac_any=114 | drop_exact_any=12 drop_vtrac_any=78 | family_exact_any=0 family_vtrac_any=17 | vt_boxed=84 vt_straight=0
- Hits (winner_hits.csv): rows=130 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=84 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 835 (canonical 358)
- Stamp (winner_stamp.json): items_total=150 | exact_any=0 exact_final=0 | vtrac_any=150 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=150 | exact_any=0 vtrac_any=150 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=150 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 281 (canonical 128)
- Stamp (winner_stamp.json): items_total=397 | exact_any=6 exact_final=0 | vtrac_any=380 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=84 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=19 family_vtrac_final=0
- Flags (winner_flags.csv): rows=397 | exact_any=6 vtrac_any=380 | drop_exact_any=12 drop_vtrac_any=84 | family_exact_any=0 family_vtrac_any=19 | vt_boxed=123 vt_straight=0
- Hits (winner_hits.csv): rows=397 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=123 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 224 | score_v2 14.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 244 | score_v2 14.277143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 11.758571 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 11.758571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 443 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 559 | score_v2 11.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 559 | score_v2 11.527143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 224 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 244 | score_v2 11.077143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw2 col 5 | pattern 440 | score_v2 10.927143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 14.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 244 | score_v2 14.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 11.758571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 443 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 224 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 244 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 440 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 10.658571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 443 | score_v2 10.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 400 | score_v2 9.810476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Both winners are **not** in DR’s top-candidate list (`winner_best_rank=None`), even though DR logs many VTRAC-any matches.
- Q2: 4 hit criteria mapping
  - Midday `128`: `exact_any=6` but `exact_final=0`; `vt_boxed=84` → DR “sees” VT family coverage but does not isolate the winner as a candidate.
  - Evening `358`: `exact_any=0`; `vt_boxed=6` → minimal VT-boxed presence only.
- Q3: Winners output alignment
  - Stamp/flags/hits are coherent (no mismatch): this is an honest “no final hit” day for DR.
- Q4: Dominance / noise
  - Very high `vtrac_any` counts make DR non-discriminative here; it is not acting as a narrow isolator.
- Q5: Top candidate clusters
  - Not extracted here (winner not present as candidate); treat DR as an overlay lens, not the primary play driver on this day.
- Q6: Miss analysis
  - This is a DR-negative day: it tags broad VT coverage but doesn’t elevate either winner into a small candidate set.
- Q7: Validation checks (V)
  - Reducer scores present; winners artifacts exist; no pipeline errors.
- Q8: Optimization notes
  - Keep DR as a confirming overlay only when its top candidates intersect Stable/HZ/VTRAC on the same VT lane (not the case here).
- Q9: Cross-tool synergy seed
  - DR’s VT-boxed counts can be used as “coverage pressure”, but only when a separate lane detector (Stable/HZ/VTRAC/Aux) points to the same index.
- Q10: Analyst’s extra insight
  - Useful example of “DR logs a lot but tells you little”: a reason to require cross-tool confirmation before acting.

---

### 2.VTRAC Analyzer — Connecticut4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20251221_222519)

## Top indices (from enhanced JSON)
- index 33 | score 101.88661249999994 | features: presence=64.90911249999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 85.63669999999995 | features: presence=58.88919999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 31.7993 | features: presence=16.651799999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 28.7832 | features: presence=15.415699999999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 27.83235 | features: presence=19.27485, set_echo=0.3, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 15 | score 22.2472625 | features: presence=15.119762500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 3 | score 21.598250000000007 | features: presence=12.630750000000003, set_echo=0.3, first_hit=0.4, column_span=0.3375
- index 22 | score 20.783860000000004 | features: presence=9.396360000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 13 | score 19.739300000000004 | features: presence=9.731800000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 29 | score 19.655725000000004 | features: presence=9.298225000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
834, 438, 983, 597, 934, 984, 943, 795, 759, 345

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 835 | index 13 | file Connecticut4_vtrac13_winner_835_20251221_222109.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 281 | index 21 | file Connecticut4_vtrac21_winner_281_20251221_222107.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 835 | index 13 rank 9/35 | score 19.739300000000004 | winner_in_index_straights=False | top_index_straights: 583 (5.352)
- winner 281 | index 21 rank 22/35 | score 6.084158333333332 | winner_in_index_straights=False | top_index_straights: 817 (2.706), 718 (1.58), 187 (1.22)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Winner idx13 (835) is mid-pack (rank 9/35); winner idx21 (281) is low (rank 22/35). Neither is a top-ranked index.
- Q2: 4 hit criteria mapping
  - The winner straights are not in the “top index straights” list (`winner_in_index_straights=False`), so VTRAC-as-direct-caller is weak here.
  - The only viable VTRAC-mode hedge would be VT-family (vstraight/index) rather than “top straights”.
- Q3: Winners output alignment
  - Winners lens exists under sharepack; enhanced JSON rank placement is consistent (no mismatch).
- Q4: Dominance / noise
  - Index ranking is not winner-dominant; multiple competing indices outrank both winners.
- Q5: Top candidate clusters (what VTRAC wanted)
  - Top index straights are led by non-winner lanes (e.g., `583` and the `817/718/187` family).
- Q6: Miss analysis
  - This is a “VTRAC underweights the winning indices” day. Log as corpus evidence; do not tune based on one case.
- Q7: Validation checks (V)
  - Enhanced JSON is present and parseable; the report is complete.
- Q8: Optimization notes
  - Later: compare VTRAC’s index ranks to Aux “overdue indices” (here, Aux strongly supports idx13) to see whether an Aux overlay should gate VTRAC actions.
- Q9: Cross-tool synergy seed
  - Use VTRAC primarily as a structural lens (index selection) only when Aux overdue + Hot Zones vt-straight both agree (partial for idx13 here).
- Q10: Analyst’s extra insight
  - A good example of why “top index straights” is not the same thing as “best index family hedge”.

---

### 2.Hot Zones — Connecticut4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2025-06-22)

## Midday winner 281 (canonical 128)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 169
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 835 (canonical 358)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 125
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 059 | vt_triad 115 | score_mean 21.316 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 127 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    2 | triad 267 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    4 | triad 012 | vt_triad 123 | score_mean 21.183 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 007 | vt_triad 13 | score_mean 20.837 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 155 | vt_triad 12 | score_mean 20.528 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 366 | vt_triad 24 | score_mean 20.426 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 344 | vt_triad 45 | score_mean 20.299 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 367 | vt_triad 234 | score_mean 20.158 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 026 | vt_triad 123 | score_mean 20.076 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Both winners are present in top lanes but **very low** (Midday best rank 169; Evening best rank 125) and not present in `winner_map` (triad_present=False).
- Q2: 4 hit criteria mapping
  - `has_vt_straight=True` for both winners suggests VT-straight lane overlap exists, but Hot Zones does not isolate a small winner lane by rank.
- Q3: Winners output alignment
  - Winner map exists, but is a Top‑N snapshot; “not present” is expected when rank is large.
- Q4: Dominance / noise
  - Hot Zones is dominated by a competing lane universe (top lanes include `059`, `012`, `007`, `155`, `366`, `344`), not the winners.
- Q5: Top candidate clusters (what Hot Zones wanted)
  - `059` (rank 1) and other strong col1/funnel lanes (`012`, `007`, `155`, `366`, `344`) define the environment’s “hot lane”, but they miss both winners.
- Q6: Miss analysis
  - The winners are not in the top lanes; treat Hot Zones here as an environment descriptor, not a winner isolator.
- Q7: Validation checks (V)
  - All expected Hot Zones artifacts are present; winner_map is present but does not include the winners (expected given low ranks).
- Q8: Optimization notes
  - Later: define how to handle “vt-straight overlap but poor rank” (cheap hedge tier vs pass).
- Q9: Cross-tool synergy seed
  - Strong overlap with Stable on the `344` lane suggests a coherent “dominant lane” story even when it misses outcomes.
- Q10: Analyst’s extra insight
  - Keep this as a negative-control example for Hot Zones: lots of heat, low predictive resolution.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Stable + Hot Zones both point strongly to a **4/8-heavy** dominant lane universe (e.g., Stable top `344/488/448`, Hot Zones top `059/012/155/366/344`).
  - Aux also indicates heavy doubles/pairs pressure and strong positional consensus around digits 4/7/5 (Combined).
- Conflicts/noise:
  - Neither winner is isolated by Stable/DR/VTRAC/HZ by rank; both winners are effectively “cold” in the winners lens stats.
  - The best single alignment to the actual outcome is structural: Aux VTRAC overlay has **idx13** as top overdue (Evening winner index).
- Aggregator/aux hooks to test next:
  - Treat “Aux top-overdue index + HZ vt-straight overlap” as a cheap hedge trigger (VT-straight pack) when the string lanes are hot but misaligned.
  - Log this day as a “dominant-lane miss” (high heat ≠ correct lane).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=155, 950, 763, 913, 201
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=950, 913, 620, 221, 894
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=155, 763, 201, 070, 059

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=5 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=19), P3:7 (gap=24)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=938 sev=B
- 111: ds=922 sev=B
- 145: ds=897 sev=B
- 448: ds=839 sev=B
- 004: ds=830 sev=B
- 223: ds=811 sev=B
- 099: ds=802 sev=B
- 001: ds=785 sev=B
- 127: ds=784 sev=B
- 466: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=165 sev=red
  - 88: ds=31 sev=purple
  - 44: ds=30 sev=purple
  - 99: ds=23 sev=-
  - 11: ds=16 sev=-
  - 66: ds=13 sev=-
  - 77: ds=10 sev=-
  - 22: ds=7 sev=-
  - 00: ds=6 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 14: ds=87 sev=red
  - 03: ds=45 sev=blue
  - 56: ds=41 sev=blue
  - 04: ds=40 sev=blue
  - 47: ds=37 sev=blue
  - 68: ds=29 sev=purple
  - 27: ds=28 sev=purple
  - 57: ds=27 sev=purple
  - 17: ds=24 sev=-
  - 79: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:170, 4:83, 23:74, 8:68, 14:63, 10:47, 15:43, 6:41, 9:40, 30:37

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=170 fs=16 fl=2 hz=0.022140221402214024, 4:ds=83 fs=25 fl=2 hz=0.029900332225913623, 23:ds=74 fs=17 fl=2 hz=0.021372328458942633, 8:ds=68 fs=43 fl=0 hz=0.04658721560130011, 14:ds=63 fs=31 fl=0 hz=0.033879781420765025, 10:ds=47 fs=17 fl=1 hz=0.022641509433962266, 15:ds=43 fs=17 fl=3 hz=0.02107481559536354, 6:ds=41 fs=31 fl=0 hz=0.03311965811965812, 9:ds=40 fs=35 fl=1 hz=0.03761755485893417, 30:ds=37 fs=55 fl=0 hz=0.05789473684210526

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=88 flags=red+purple
- S4: ds=68 flags=purple
- S12: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 126: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=32 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:0 (gap=26), P3:7 (gap=13)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=892 sev=B
- 337: ds=855 sev=B
- 889: ds=825 sev=B
- 234: ds=776 sev=B
- 225: ds=752 sev=B
- 077: ds=733 sev=B
- 009: ds=726 sev=B
- 279: ds=699 sev=B
- 117: ds=685 sev=B
- 128: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=82 sev=blue
  - 11: ds=73 sev=blue
  - 00: ds=41 sev=purple
  - 44: ds=38 sev=purple
  - 77: ds=24 sev=-
  - 88: ds=15 sev=-
  - 55: ds=12 sev=-
  - 99: ds=11 sev=-
  - 66: ds=6 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 18: ds=91 sev=red
  - 69: ds=68 sev=red
  - 14: ds=43 sev=blue
  - 04: ds=35 sev=purple
  - 45: ds=31 sev=purple
  - 58: ds=31 sev=purple
  - 67: ds=27 sev=purple
  - 01: ds=26 sev=purple
  - 28: ds=25 sev=purple
  - 29: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:143, 13:124, 19:105, 23:91, 17:73, 2:66, 8:58, 27:50, 31:47, 12:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=143 fs=2 fl=0 hz=0.006006006006006006, 13:ds=124 fs=16 fl=1 hz=0.021013597033374538, 19:ds=105 fs=21 fl=1 hz=0.026284348864994027, 23:ds=91 fs=22 fl=1 hz=0.02561247216035635, 17:ds=73 fs=32 fl=2 hz=0.037158469945355196, 2:ds=66 fs=22 fl=1 hz=0.026713124274099886, 8:ds=58 fs=53 fl=0 hz=0.05644302449414271, 27:ds=50 fs=16 fl=3 hz=0.020452099031216364, 31:ds=47 fs=20 fl=3 hz=0.024390243902439025, 12:ds=42 fs=50 fl=0 hz=0.052576235541535225

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=93 flags=purple
- S6: ds=66 flags=red+purple
- S9: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=3 tags=MIR,RS
  - 025: score=3 tags=MIR,RS
  - 079: score=3 tags=FLT,RS
  - 169: score=3 tags=MIR,RS
  - 178: score=3 tags=FLT,RS
  - 349: score=3 tags=MIR,RS
  - 358: score=3 tags=MIR,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 027: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=24 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=18), P2:3 (gap=37), P3:6 (gap=13)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 255: ds=934 sev=B
- 034: ds=911 sev=B
- 228: ds=889 sev=B
- 088: ds=887 sev=B
- 223: ds=848 sev=B
- 666: ds=836 sev=B
- 225: ds=811 sev=B
- 678: ds=712 sev=B
- 668: ds=709 sev=B
- 399: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=85 sev=blue
  - 88: ds=50 sev=purple
  - 99: ds=16 sev=-
  - 44: ds=15 sev=-
  - 66: ds=13 sev=-
  - 11: ds=8 sev=-
  - 22: ds=6 sev=-
  - 77: ds=5 sev=-
  - 00: ds=3 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 35: ds=89 sev=red
  - 14: ds=78 sev=red
  - 56: ds=73 sev=red
  - 16: ds=44 sev=blue
  - 08: ds=36 sev=purple
  - 03: ds=34 sev=purple
  - 57: ds=32 sev=purple
  - 39: ds=31 sev=purple
  - 34: ds=30 sev=purple
  - 47: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 20:224, 15:145, 32:131, 16:118, 34:94, 13:85, 4:56, 6:54, 33:50, 10:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 20:ds=224 fs=18 fl=2 hz=0.0258732212160414, 15:ds=145 fs=14 fl=1 hz=0.01873536299765808, 32:ds=131 fs=2 fl=0 hz=0.004120879120879121, 16:ds=118 fs=2 fl=1 hz=0.005961251862891207, 34:ds=94 fs=20 fl=2 hz=0.025, 13:ds=85 fs=23 fl=3 hz=0.028540065861690448, 4:ds=56 fs=22 fl=1 hz=0.024918743228602384, 6:ds=54 fs=16 fl=1 hz=0.0196078431372549, 33:ds=50 fs=29 fl=0 hz=0.03176341730558598, 10:ds=42 fs=20 fl=3 hz=0.02561247216035635

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=94 flags=red+purple
- S8: ds=92 flags=red+purple
- S24: ds=71 flags=purple
- S20: ds=70 flags=purple
- S6: ds=58 flags=purple
- S2: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 044 -> combined:697(B); evening:704(B)
- 145 -> combined:897(B); evening:673(B)
- 223 -> combined:811(B); evening:848(B)
- 225 -> evening:811(B); midday:752(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:45(blue); evening:34(purple)
- 04 -> combined:40(blue); midday:35(purple)
- 14 -> combined:87(red); evening:78(red); midday:43(blue)
- 33 -> combined:165(red); evening:85(blue); midday:82(blue)
- 44 -> combined:30(purple); midday:38(purple)
- 47 -> combined:37(blue); evening:30(purple)
- 56 -> combined:41(blue); evening:73(red)
- 57 -> combined:27(purple); evening:32(purple)
- 88 -> combined:31(purple); evening:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(3.585585714285714)[R2,XVAR-Cons(CE)], 5(2.5846642857142856)[R1,XVAR-Cons(CM)], 4(1.8571071428571428)[R3,XVAR-Cons(CE)], 1(1.4762857142857142)[R1,Double-Pressure], 8(1.3989285714285713)[R1,Mirror-Echo]
- P2: 4(5.6524214285714285)[R1,XVAR-Cons(CEM)], 3(3.4805714285714284)[R3,Mirror-Echo], 8(3.4802142857142857)[R2,Mirror-Echo], 0(1.4462857142857144)[R1,Double-Pressure], 1(1.2643)[R2,Double-Pressure]
- P3: 7(7.170371428571428)[R1,Mirror-Echo], 6(3.244142857142857)[R2,XVAR-Cons(CE)], 9(0.8998999999999999)[R2,Double-Pressure], 2(0.5125714285714286)[R3,Mirror-Echo], 4(0.24779285714285712)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state Connecticut4 --strict` → OK.
- Q2:
  - Positional pressure is coherent (strong XVAR consensus notes), but it does not cleanly explain either literal winner.
  - Combined top due digits: P1=5, P2=4, P3=7 (high pressure on 4/7/5 lanes).
- Q3:
  - Positional shortlist (Combined top): heavily targets `*47` (e.g., `347/547/747/337/387/...`) which is a different lane than either winner.
- Q4:
  - Repeat watch does not explain either winner (current indices do not match winners).
- Q5:
  - VTRAC overlay is the key Aux alignment here:
    - Combined top overdue indices include **idx13** as #1 (`ds=170`) which matches the Evening winner’s index (13).
    - Midday winner idx21 is not a top overdue index → weak Aux support for Midday.
- Q6:
  - Doubles/pairs pressure is very high (many sev=B doubles, repeating pair alerts), reinforcing “noisy environment”.
- Q7:
  - Sums are broadly flagged (many purple/red+purple), offering little discrimination for these specific winners.
- Q8:
  - Blackapple (Combined score=2; pairs remaining=0) surfaces top candidates like `018/045/189/234/378/459/468/...` which do not include the winners → disagreement.
- Q9:
  - Cross-variant alerts show many due doubles/pairs across variants; treat as environment pressure only (not a narrow call).
- Q10:
  - Apply Aux here primarily as:
    - an “environment noise detector”, and
    - a structural VT overlay (idx13) for cheap VT-straight hedging when strings/tools don’t isolate.

---

## Part 4 — Combination / Permutation Translation (candidate pack)
Use Part 4 prompts in the master template to produce:
- A small candidate universe per draw (Midday/Evening)
- Evidence vectors per candidate (tools + aux signals)
- Coverage mapping (perm-only vs boxed vs VTRAC-straight vs full index-box)

Reference:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

Part 4 notes / answers:
- Candidate universe (Midday):
  - Primary: VT family hedge for idx21 (winner’s index) **only as a tiny hedge** (weak tool support).
  - Optional competing lane marker (if playing at all): `059` / `344` (dominant lane from Hot Zones + Stable) as “what the environment wanted”.
- Candidate universe (Evening):
  - Primary: VT family hedge for **idx13** (Aux overdue #1; matches the Evening winner’s index).
- Evidence vectors:
  - Midday: weak winner isolation; strongest evidence is only “family pressure carryover” in the winners lens (not literal presence) + Hot Zones `has_vt_straight=True` for the winner.
  - Evening: Aux VTRAC overdue (`idx13 ds=170`) + Hot Zones `has_vt_straight=True` support a VT-straight hedge.
- Coverage mapping + pack decision:
  - Midday: recommend **pass** or a tiny VT‑straight hedge on idx21 (8 straights) if you must play.
  - Evening: play **VT‑straight** (8 straights) on idx13 as the cheapest coherent hedge aligned to Aux overdue structure.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday: a VT-straight hedge on idx21 would cover `281` straight (if chosen); dominant-lane boxes (`059/344`) would not.
  - Evening: VT‑straight on idx13 would cover `835` straight.
- Key tags:
  - `high col1/2 heat, low winner alignment`
  - `dominant 4/8 lane`
  - `winners cold / not printed in progression`
  - `Aux overdue index signal (idx13)`
- Drivers:
  - The only “explainable” driver is structural VT pressure for the Evening winner’s index (Aux overdue idx13).
- Conflicts:
  - Stable/Hot Zones strongly favor competing lanes (`344`, `059/012/155/...`) that miss both winners.
  - Blackapple candidates disagree with winners.
- Fix-now vs fix-later:
  - Fix-now: none (alignment OK; artifacts present).
  - Fix-later: keep as a negative-control case for aggregator gating (“high heat but wrong lane”).
- Next run:
  - Continue to the next state for `D=2025-06-22` and look for contrast cases where winners are actually printed / elevated by at least 2 tools.
