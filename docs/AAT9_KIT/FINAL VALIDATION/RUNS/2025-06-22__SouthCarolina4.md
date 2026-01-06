# Master Validation Run Report — SouthCarolina4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/SouthCarolina4/`
- Winners lens: `sharepacks/2025-06-22/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2025-06-22/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2025-06-22/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2025-06-22/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2025-06-22/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2025-06-22/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-06-22/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-22/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac7_winner_675_20251221_222134.html`

Winners JSON files:
- `sharepacks/2025-06-22/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac7_winner_675_20251221_222134.json`

Part A answers (fill using the template’s Part A questions):
- Q1: South Carolina has no Midday result recorded for 2025-06-22; only Evening winner exists.
  - Results line: `South Carolina\t\t675` in `data/results/2025-06-22.txt` (Midday blank; Evening=675).
  - Set1/Draw1 ladders (from winners JSON; lens only, not “outcomes”):
    - Midday: col1/col2 `51138** / 58311** / 81153** / 11835**`
    - Evening: col1 `098** / 089**`; col2 `9488** / 9884** / 8894**`
    - Combined: col1 `005**`; col2 `587** / 875** / 785**`
- Q2: Lane persistence is high (dense `**` ladders), but the printed lane universes (5/1/8/3, 0/9/8, 0/5) do not narrate the winner canonical `567`.
- Q3: Winner tagging is weak (no on-board “hit”).
  - `hit-winner` tags are absent in all variants.
  - `hit-winner-gap` exists (Evening=2, Combined=2), meaning the winner is “near” a family lane but not printed as a direct survivor.
  - Family pressure exists (hit-family totals: Midday=24, Evening=6, Combined=14), but it never resolves to an exact lane.
- Q4: Variant bias is not helpful here:
  - literal substring cells for `675` = 0 in Midday/Evening/Combined
  - canonical substring cells for `567` = 0 in Midday/Evening/Combined
- Q5: Permutation lane clarity is low (no decisive printed lane for `567` or `675`).
- Q6: Environment verdict: **pass / tiny hedge only** (good negative-control day).
- Q7: Hot Zones overlap is weak:
  - best rank 187; has_straight=False; has_vt_straight=False; winner_map triad_present=False.
- Q8: Cross-set carryover exists only as broad family pressure (`hit-family(-gap)`), not as actionable narrowing.
- Q9: Aux cues (quick lens) are not supportive:
  - VTRAC overdue list does not elevate winner idx7 (top overdue indices are 29/32/1/2/5/…).
  - Aggregated positional digits show strong cross-variant pressure (P1=5/6, P2=9/7/8, P3=4/3/5), but it does not isolate `567`.
- Q10: 4 hit criteria viability (pre-results lens): low.
  - Stable: no exact boxed/straight.
  - DR: vt_boxed exists but no finals; winner not in top candidates.
  - VTRAC analyzer: winner index rank is very weak.
  - Hot Zones: winner not in top slice.
- Q11: Exact triple presence (winners lens):
  - `hit-winner` cells=0 (Midday/Evening/Combined).
  - `hit-winner-gap` cells: 0/2/2 (Midday/Evening/Combined).
- Q12: “Profitable environment” summary:
  - Useful example of a very active board that still provides no decisive convergence to the winner.
  - Also a good workflow guard case: missing Midday result should not be treated as a “broken pipeline”.
- Q13: Dominance vs dilution:
  - Dominant ladders exist, but the winner is orthogonal to that dominance → dilution relative to the actual outcome.
- Q14: Noise check:
  - High noise / low discrimination; record as a “skip posture” environment example.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — SouthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2025-06-22)

## Evening winner 675 (canonical 567)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=151 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 47 | rank 518/1507 (rank_frac 0.34372926343729265) | score 17.5 (top 32.5, ratio 0.5384615384615384, delta 15.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=42
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    6 | canon 138 | section Midday | score 76.0 | col1_hits 8 | hot2 11
- rank    2 | canon 118 | section Midday | score 89.5 | col1_hits 9 | hot2 11
- rank    1 | canon 113 | section Midday | score 94.5 | col1_hits 8 | hot2 11
- rank    5 | canon 1138 | section Midday | score 77.0 | col1_hits 8 | hot2 11
- rank    3 | canon 115 | section Midday | score 84.0 | col1_hits 7 | hot2 10
- rank    4 | canon 11358 | section Midday | score 82.5 | col1_hits 7 | hot2 10
- rank    7 | canon 1135 | section Midday | score 70.0 | col1_hits 6 | hot2 10
- rank   11 | canon 358 | section Midday | score 61.5 | col1_hits 7 | hot2 10
- rank   16 | canon 1358 | section Midday | score 57.5 | col1_hits 7 | hot2 9
- rank   13 | canon 117 | section Midday | score 60.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1468 | family 4 | score 6.5 | hot2 0 | section Midday
- rank  454 | family 4 | score 18.5 | hot2 0 | section Midday
- rank  341 | family 33 | score 20.0 | hot2 0 | section Midday
- rank  269 | family 14 | score 21.0 | hot2 0 | section Midday
- rank  225 | family 17 | score 21.5 | hot2 0 | section Midday
```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Winner canonical `567` is not present in scores/compound; only weak family presence (best family rank 518; score 17.5).
  - One-winner day: Midday is blank in results; analysis uses the Evening winner `675`.
- Q2: 4 hit criteria mapping
  - No exact boxed/straight (exact_boxed=False, exact_straight=False).
  - vt_boxed_count=42 indicates broad VTRAC-family presence, not isolation.
- Q3: Output integrity
  - Stable artifacts exist; this is a true “no isolation” outcome, not missing tool output.
- Q4: Dominance / noise
  - Top compounds are dominated by non-winner canonicals (113/118/138/1138/11358/…), not `567`.
- Q5: Where the winner shows up
  - Family-only presence; no actionable candidate rank.
- Q6: Miss analysis
  - Stable miss (no candidate isolation for `567`).
- Q7: Validation checks (V)
  - Brain outputs present + winners lens present.
- Q8: Optimization notes
  - None now (avoid tuning from a single miss day).
- Q9: Cross-tool synergy seed
  - Stable’s dominant “11* / 13* / 18*” environment aligns loosely with DR’s top Midday patterns (511/551), but neither aligns to the winner.
- Q10: Analyst’s extra insight
  - This is a good “active board, wrong universe” example: Stable produces rich top compounds, but the winner lives outside them.

---

### 2.Digit Reduction — SouthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20251222)

## Midday: no winner in results file
- Skipped: state missing or blank for this period

## Evening winner 675 (canonical 567)
- Stamp (winner_stamp.json): items_total=23 | exact_any=0 exact_final=0 | vtrac_any=17 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=11 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=8 family_vtrac_final=0
- Flags (winner_flags.csv): rows=23 | exact_any=0 vtrac_any=17 | drop_exact_any=0 drop_vtrac_any=11 | family_exact_any=0 family_vtrac_any=8 | vt_boxed=15 vt_straight=0
- Hits (winner_hits.csv): rows=23 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=15 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 675 (canonical 567)
- Stamp (winner_stamp.json): items_total=103 | exact_any=0 exact_final=0 | vtrac_any=50 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=85 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=23 family_vtrac_final=0
- Flags (winner_flags.csv): rows=103 | exact_any=0 vtrac_any=50 | drop_exact_any=0 drop_vtrac_any=85 | family_exact_any=0 family_vtrac_any=23 | vt_boxed=56 vt_straight=0
- Hits (winner_hits.csv): rows=103 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=56 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.047143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 513 | score_v2 15.047143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 513 | score_v2 15.047143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 551 | score_v2 12.827143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 551 | score_v2 12.827143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 551 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 511 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 551 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 551 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 513 | score_v2 11.847143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 513 | score_v2 11.847143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 513 | score_v2 15.047143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 551 | score_v2 12.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 511 | score_v2 12.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 551 | score_v2 12.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 513 | score_v2 11.847143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 511 | score_v2 11.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 599 | score_v2 11.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 559 | score_v2 11.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 559 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 559 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday has no winner in the results file (one-winner day) and is skipped.
  - Evening/Combined winner `675` (canon `567`) is not present in top candidates (winner_present=False) despite broad VT contact.
  - vt_boxed is non-zero (Evening=15, Combined=56) but no finals (exact_final=0, vtrac_final=0).
- Q2: 4 hit criteria mapping
  - DR provides broad VT coverage (vt_boxed>0), but it does not isolate the winner as a top candidate.
- Q3: Output integrity (important)
  - Evening/Combined overlays exist and validate cleanly (stamp ↔ flags ↔ hits).
  - Midday overlay is intentionally absent because there is no Midday result in the results file.
- Q4: What DR wanted (top candidates)
  - Top patterns are 513 (Combined) and 551/511 (Midday); no lift toward `567`.
- Q5: Miss analysis
  - As graded by DR’s own top-candidates lens, this is a miss day.
- Q6: Validation checks (V)
  - Reducer scores exist; Evening/Combined overlays exist; Midday skipped (expected).
- Q7: Cross-tool synergy seed
  - None (Stable/DR/HotZones/VTRAC do not converge on a shared winner-adjacent cluster).
- Q8: Optimization notes
  - None now.
- Q9: Aux hook
  - Treat vt_boxed>0 as “broad VT-family contact,” not isolation.
- Q10: Analyst’s extra insight
  - Keep this as a regression case: missing Midday results should not be interpreted as a tool/pipeline failure.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20251221_222528)

## Top indices (from enhanced JSON)
- index 15 | score 42.1971875 | features: presence=24.919687500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 37.2865 | features: presence=22.759, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 14 | score 27.933885000000004 | features: presence=14.306385, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 31 | score 27.8406725 | features: presence=16.7431725, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 26.707500000000003 | features: presence=15.980000000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 24.10775 | features: presence=14.850249999999999, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 5 | score 20.128445000000003 | features: presence=10.560945000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 6 | score 19.933750000000003 | features: presence=12.796250000000002, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 3 | score 19.433850000000003 | features: presence=8.926350000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 12 | score 18.8613 | features: presence=9.2038, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
534, 153, 541, 345, 341, 531, 135, 024, 524, 134

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 675 | index 7 | file SouthCarolina4_vtrac7_winner_675_20251221_222134.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 675 | index 7 rank 29/35 | score 3.3089583333333334 | winner_in_index_straights=False | top_index_straights: 175 (1.24), 170 (0.55)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Winner idx7 ranks 29/35 (very weak) with score 3.31 vs top 42.20 (ratio ~0.08).
- Q2: What VTRAC wanted (top straights / indices)
  - Top indices are 15/18/14/31/…; top straights include 534/153/541/… — none point to idx7 as a priority.
- Q3: Winner index isolation
  - winner_in_index_straights=False; treat idx7 as not isolated.
- Q4: Consensus / cross-section
  - consensus_col1/2 are False across variants; no structural convergence.
- Q5: Miss analysis
  - VTRAC analyzer is a miss day for this winner.
- Q6: Validation checks (V)
  - Artifacts exist; winners lens JSON/HTML present.
- Q7: Cross-tool synergy seed
  - Supports the “pass/tiny” posture due to lack of convergence.
- Q8: Optimization notes
  - None now.
- Q9: Aux hook
  - Aux overdue indices do not elevate idx7; treat as non-support.
- Q10: Analyst’s extra insight
  - Good negative-control day where all three brain tools (Stable/DR/VTRAC) fail to isolate the winner.

---

### 2.Hot Zones — SouthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2025-06-22)

## Evening winner 675 (canonical 567)
- Top lanes (hot_zones_top_lanes.csv): present | rank 187/204 (rank_frac 0.9166666666666666) | score_mean 13.792 (top 23.119, ratio 0.5965655953977248, delta 9.327)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 237 | vt_triad 334 | score_mean 23.119 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 278 | vt_triad 334 | score_mean 21.29 | tags hot16,hot20,set1_bonus,vertical2,vt_only_lane,vt_straight
- rank    3 | triad 244 | vt_triad 35 | score_mean 20.171 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_straight
- rank    4 | triad 069 | vt_triad 125 | score_mean 19.869 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 113 | vt_triad 24 | score_mean 19.652 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    6 | triad 588 | vt_triad 14 | score_mean 19.482 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 118 | vt_triad 24 | score_mean 19.397 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 469 | vt_triad 255 | score_mean 19.386 | tags hot12,hot16,hot20,hot4,literal_draw,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 388 | vt_triad 44 | score_mean 19.236 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank   10 | triad 889 | vt_triad 45 | score_mean 19.184 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Winner triad `567` is weak: best rank 187; triad_present=False; has_straight=False; has_vt_straight=False.
- Q2: What Hot Zones wanted (top lanes)
  - Top lanes are dominated by other triads (237/278/244/069/113/…); no alignment to `567`.
- Q3: Winner map interpretation
  - triad_present=False is expected for non-top slices; interpret as signal weakness (not corruption).
- Q4: Miss analysis
  - Hot Zones does not isolate the winner.
- Q5: Validation checks (V)
  - Outputs exist; winner map artifacts present.
- Q6: Cross-tool synergy seed
  - None for the winner; Hot Zones aligns with the “pass/tiny” posture.
- Q7: Optimization notes
  - None now.
- Q8: Aux hook
  - No decisive doubles/pairs event aligns with `567`.
- Q9: Guardrails / notes
  - Missing Midday results should not be interpreted as a Hot Zones pipeline failure.
- Q10: Analyst’s extra insight
  - This day is useful to test “skip policies” based on low Hot Zones rank + no winners-lens hit-winner tags.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - No convergence cluster for winner `675/567`; each tool highlights different non-winner structures (Stable 11*/13*, DR 513/551, Hot Zones 237/278/…, VTRAC idx15/18/…).
- Conflicts/noise:
  - Winner is broadly off-board (no hit-winner tags anywhere; only small hit-winner-gap counts).
  - Results feed irregularity: Midday missing (one-winner day). Workflow now treats this as expected (summaries use Evening winner; DR skips Midday).
- Aggregator/aux hooks to test next:
  - Add/confirm a runbook guard: when Midday is blank, treat this as “one-winner day” and do not label Evening as “unknown”.
  - Use “hit-winner present vs absent” as a simple binary gate (here: absent → skip posture).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=847, 069, 402, 442, 351
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=069, 442, 968, 237, 029
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=847, 402, 351, 002, 116

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=60 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=21), P2:9 (gap=32), P3:4 (gap=29)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=935 sev=B
- 288: ds=903 sev=B
- 466: ds=822 sev=B
- 238: ds=814 sev=B
- 788: ds=725 sev=B
- 388: ds=716 sev=B
- 228: ds=707 sev=B
- 557: ds=706 sev=B
- 137: ds=687 sev=B
- 668: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=87 sev=blue
  - 33: ds=50 sev=purple
  - 99: ds=27 sev=purple
  - 55: ds=24 sev=-
  - 22: ds=22 sev=-
  - 77: ds=20 sev=-
  - 88: ds=17 sev=-
  - 11: ds=8 sev=-
  - 00: ds=6 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 28: ds=141 sev=red
  - 56: ds=81 sev=red
  - 18: ds=72 sev=red
  - 01: ds=38 sev=blue
  - 17: ds=38 sev=blue
  - 14: ds=37 sev=blue
  - 19: ds=37 sev=blue
  - 08: ds=36 sev=purple
  - 45: ds=34 sev=purple
  - 39: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 2:187, 1:145, 5:104, 19:94, 34:93, 32:84, 6:83, 4:80, 15:61, 26:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 2:ds=187 fs=9 fl=4 hz=0.016414141414141416, 1:ds=145 fs=5 fl=3 hz=0.011299435028248588, 5:ds=104 fs=21 fl=1 hz=0.028061224489795922, 19:ds=94 fs=13 fl=1 hz=0.016968325791855206, 34:ds=93 fs=26 fl=2 hz=0.031180400890868598, 32:ds=84 fs=2 fl=2 hz=0.005675368898978434, 6:ds=83 fs=21 fl=1 hz=0.02480270574971815, 4:ds=80 fs=26 fl=2 hz=0.03153153153153153, 15:ds=61 fs=13 fl=3 hz=0.01845444059976932, 26:ds=57 fs=2 fl=0 hz=0.007894736842105263

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=93 flags=blue+purple
- S25: ds=82 flags=purple
- S3: ds=59 flags=purple
- S13: ds=47 flags=purple
- S20: ds=45 flags=purple
- S17: ds=42 flags=purple
- S4: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=2 tags=RS
  - 049: score=2 tags=RS
  - 058: score=2 tags=RS
  - 067: score=2 tags=RS
  - 139: score=2 tags=RS
  - 148: score=2 tags=RS
  - 157: score=2 tags=RS
  - 238: score=2 tags=RS
  - 247: score=2 tags=RS
  - 256: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=36 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=47), P2:8 (gap=25), P3:1 (gap=27)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 144: ds=976 sev=B
- 777: ds=975 sev=B
- 224: ds=946 sev=B
- 011: ds=766 sev=B
- 277: ds=712 sev=B
- 555: ds=707 sev=B
- 222: ds=684 sev=B
- 048: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=61 sev=purple
  - 00: ds=54 sev=purple
  - 88: ds=41 sev=purple
  - 66: ds=40 sev=purple
  - 33: ds=23 sev=-
  - 99: ds=12 sev=-
  - 55: ds=11 sev=-
  - 22: ds=10 sev=-
  - 77: ds=9 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 78: ds=126 sev=red
  - 04: ds=85 sev=red
  - 28: ds=65 sev=red
  - 08: ds=41 sev=blue
  - 56: ds=37 sev=blue
  - 15: ds=35 sev=purple
  - 35: ds=34 sev=purple
  - 18: ds=33 sev=purple
  - 16: ds=29 sev=purple
  - 67: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:294, 32:248, 1:168, 2:86, 5:85, 16:61, 8:60, 4:54, 34:44, 19:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=294 fs=23 fl=0 hz=0.03412462908011869, 32:ds=248 fs=1 fl=2 hz=0.006993006993006993, 1:ds=168 fs=4 fl=3 hz=0.00963855421686747, 2:ds=86 fs=11 fl=1 hz=0.015435501653803748, 5:ds=85 fs=20 fl=0 hz=0.02531645569620253, 16:ds=61 fs=3 fl=1 hz=0.009191176470588236, 8:ds=60 fs=42 fl=1 hz=0.04767184035476718, 4:ds=54 fs=26 fl=2 hz=0.030871003307607496, 34:ds=44 fs=27 fl=1 hz=0.03083700440528634, 19:ds=43 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=97 flags=blue+purple
- S4: ds=92 flags=purple
- S21: ds=43 flags=purple
- S16: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=72 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=83), P2:9 (gap=17), P3:4 (gap=33)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=83)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 114: ds=974 sev=B
- 238: ds=891 sev=B
- 558: ds=869 sev=B
- 477: ds=856 sev=B
- 000: ds=853 sev=B
- 556: ds=819 sev=B
- 115: ds=814 sev=B
- 111: ds=801 sev=B
- 999: ds=786 sev=B
- 078: ds=773 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=113 sev=red
  - 66: ds=83 sev=blue
  - 44: ds=59 sev=purple
  - 22: ds=57 sev=purple
  - 55: ds=31 sev=purple
  - 33: ds=30 sev=purple
  - 99: ds=24 sev=-
  - 88: ds=9 sev=-
  - 11: ds=4 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 28: ds=90 sev=red
  - 56: ds=49 sev=blue
  - 09: ds=47 sev=blue
  - 18: ds=42 sev=blue
  - 06: ds=39 sev=blue
  - 34: ds=36 sev=purple
  - 46: ds=33 sev=purple
  - 49: ds=33 sev=purple
  - 68: ds=28 sev=purple
  - 23: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:291, 19:211, 26:204, 6:146, 10:109, 2:106, 1:78, 15:75, 5:56, 14:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=291 fs=3 fl=1 hz=0.017391304347826087, 19:ds=211 fs=16 fl=2 hz=0.02319587628865979, 26:ds=204 fs=0 fl=0 hz=0.002628120893561104, 6:ds=146 fs=23 fl=2 hz=0.030637254901960783, 10:ds=109 fs=20 fl=0 hz=0.024110218140068886, 2:ds=106 fs=13 fl=3 hz=0.01875732708089097, 1:ds=78 fs=2 fl=0 hz=0.005440696409140369, 15:ds=75 fs=24 fl=1 hz=0.027056277056277056, 5:ds=56 fs=16 fl=3 hz=0.0202991452991453, 14:ds=52 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S3: ds=72 flags=purple
- S22: ds=67 flags=purple
- S26: ds=50 flags=blue+purple
- S7: ds=48 flags=purple
- S14: ds=45 flags=purple
- S25: ds=44 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 129: score=1 tags=FLT
  - 139: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 115 -> combined:673(B); evening:814(B)
- 238 -> combined:814(B); evening:891(B)
- 788 -> combined:725(B); evening:758(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:38(blue); midday:27(purple)
- 08 -> combined:36(purple); midday:41(blue)
- 18 -> combined:72(red); evening:42(blue); midday:33(purple)
- 19 -> combined:37(blue); evening:25(purple)
- 28 -> combined:141(red); evening:90(red); midday:65(red)
- 33 -> combined:50(purple); evening:30(purple)
- 34 -> combined:29(purple); evening:36(purple)
- 56 -> combined:81(red); evening:49(blue); midday:37(blue)
- 66 -> combined:87(blue); evening:83(blue); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(4.205)[R1,XVAR-Cons(CM)], 6(3.240571428571428)[R3,XVAR-Cons(CE)], 2(1.4015)[R2,Double-Pressure], 3(1.0344)[R2,Double-Pressure], 7(0.986)[R2,Double-Pressure]
- P2: 9(7.098257142857143)[R1,XVAR-Cons(CEM)], 7(3.4234999999999998)[R2,XVAR-Cons(CE)], 8(3.0268571428571427)[R3,XVAR-Cons(CM)], 1(1.0252999999999999)[R2,Double-Pressure], 3(0.2881)[R3,Swap]
- P3: 4(8.078414285714285)[R1,XVAR-Cons(CEM)], 3(3.5928999999999998)[R2,XVAR-Cons(CE)], 5(1.6882214285714285)[R3,XVAR-Cons(CM)], 1(1.4061428571428571)[R1,Double-Pressure], 0(0.2552785714285714)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state SouthCarolina4 --strict` → OK.
- Q2:
  - Positional pressure is active but non-isolating:
    - Aggregated positional digits show heavy cross-variant pressure (P1=5/6, P2=9/7/8, P3=4/3/5), which does not isolate `567`.
- Q3:
  - Positional shortlist does not surface `675` as a top candidate (treat as non-supportive).
- Q4:
  - Repeat watch is active (current_index=30 across variants), but it does not support winner idx7.
- Q5:
  - VTRAC overlay overdue list does not elevate idx7; treat as non-support.
- Q6:
  - Doubles/pairs multi-variant alerts show broad pressure, but nothing narrows to the winner.
- Q7:
  - Sums are broadly flagged (many purple/red+purple) → low discrimination.
- Q8:
  - Blackapple is low signal (scores 0–1; candidates mostly float clusters like *x9 / 0x9*) and does not isolate `567`.
- Q9:
  - Cross-variant alerts are useful as context only; they do not provide a clean “winner lane” here.
- Q10:
  - Use Aux as corroboration for environment activity; treat this as a “skip posture” day because it does not converge on the winner.

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
  - N/A (Midday result is blank for South Carolina on 2025-06-22; treat this as a one-winner day).
- Candidate universe (Evening):
  - Default posture: pass/tiny (no cross-tool convergence on `567` / winner `675`).
- Evidence vectors:
  - Stable/DR/VTRAC/Hot Zones all fail to isolate `567` (and winners lens has no hit-winner tags).
  - Aux is active but non-isolating.
- Coverage mapping + pack decision:
  - No recommended pack; if forced, keep spend minimal and treat as a negative-control example.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Evening: winner `675` (canon `567`) is off-board and not isolated by any tool → expected miss under a “convergence-only” posture.
  - Midday: N/A (no result recorded).
- Key tags:
  - Missing Midday result (one-winner day).
  - Winner is off-board (`hit-winner` absent; only small `hit-winner-gap` counts).
- Drivers:
  - None (no dominant convergent signal).
- Conflicts:
  - Cross-tool miss day; strong “other-universe” dominance that excludes the winner.
- Fix-now vs fix-later:
  - Fix-now: none (workflow handles one-winner days; Midday is skipped and Evening is labeled correctly).
  - Fix-later: none.
- Next run:
  - Continue to the next state/day; use this as a regression case for missing-results handling.
