# Master Validation Run Report — Pennsylvania4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/Pennsylvania4/`
- Winners lens: `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2025-12-31/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2025-12-31/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2025-12-31/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2025-12-31/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2025-12-31/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2025-12-31/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac20_winner_221_20260105_052208.html`
- `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac24_winner_684_20260105_052207.html`

Winners JSON files:
- `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac20_winner_221_20260105_052208.json`
- `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac24_winner_684_20260105_052207.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 684 (canon 468): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 221 (canon 122): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 221 idx20 (rank 7/35, frac 0.200), 684 idx24 (rank 11/35, frac 0.314)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
- Q7: Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy.
- Q8: Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries).
- Q9: Aux cues: BA score=0 (if None, BA not available); see Part 3 positional/doubles/pairs notes.
- Q10: 4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank).
- Q11: Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table.
- Q12: Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days.
- Q13: Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance.
- Q14: Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — Pennsylvania4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2025-12-31)

## Midday winner 684 (canonical 468)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=80 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 56 | rank 77/1388 (rank_frac 0.05547550432276657) | score 27.0 (top 34.5, ratio 0.782608695652174, delta 7.5) | section Combined, hot2 1
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=136
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 221 (canonical 122)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=463 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 52 | rank 444/1388 (rank_frac 0.31988472622478387) | score 19.5 (top 34.5, ratio 0.5652173913043478, delta 15.0) | section Midday, hot2 9
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=4
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 138 | section Evening | score 82.5 | col1_hits 7 | hot2 10
- rank    5 | canon 778 | section Combined | score 76.5 | col1_hits 2 | hot2 6
- rank    8 | canon 177 | section Combined | score 70.0 | col1_hits 1 | hot2 6
- rank    7 | canon 377 | section Combined | score 71.0 | col1_hits 2 | hot2 6
- rank    6 | canon 1133 | section Evening | score 71.5 | col1_hits 2 | hot2 6
- rank    9 | canon 338 | section Evening | score 63.5 | col1_hits 0 | hot2 6
- rank   13 | canon 118 | section Evening | score 58.5 | col1_hits 0 | hot2 6
- rank   17 | canon 11338 | section Evening | score 58.0 | col1_hits 0 | hot2 6
- rank   20 | canon 1338 | section Evening | score 54.0 | col1_hits 0 | hot2 6
- rank   13 | canon 1377 | section Combined | score 58.5 | col1_hits 1 | hot2 6

## Top families (patterns_families.csv)
- rank 1140 | family 19 | score 9.0 | hot2 0 | section Midday
- rank  780 | family 21 | score 14.0 | hot2 0 | section Midday
- rank 1219 | family 11 | score 8.0 | hot2 0 | section Midday
- rank 1326 | family 3 | score 6.0 | hot2 0 | section Midday
- rank 1326 | family 12 | score 6.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 221 (canon 122): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q2: 4 hit criteria: see metrics_hits per winner (exact_boxed/exact_straight + vt_boxed_count).
- Q3: Winners artifacts alignment: spotlight + metrics.json consistent (see summary block).
- Q4: Dominance/noise: does not isolate winners (no exact boxed); use rank_frac + score_ratio_to_top to gauge strength.
- Q5: Top candidate clusters (compound canonicals): .
- Q6: Miss analysis: if a winner is absent/low, treat as tool outcome (not pipeline failure) unless gaps are listed.
- Q7: Validation (V): gaps list should be empty; if non-empty, flag as Fix-Now.
- Q8: Optimization notes: do not tune on 1 day; accumulate across days then adjust weights (Fix-Later).
- Q9: Cross-tool synergy: compare top compound canonicals vs DR top candidates + Hot Zones top lanes + Aux positional shortlist.
- Q10: Takeaway: Stable does not isolate winners (no exact boxed).

---

### 2.Digit Reduction — Pennsylvania4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260105)

## Midday winner 684 (canonical 468)
- Stamp (winner_stamp.json): items_total=85 | exact_any=0 exact_final=0 | vtrac_any=73 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=49 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=85 | exact_any=0 vtrac_any=73 | drop_exact_any=0 drop_vtrac_any=49 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=85 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 221 (canonical 122)
- Stamp (winner_stamp.json): items_total=52 | exact_any=3 exact_final=0 | vtrac_any=38 vtrac_final=0 | drop_exact_any=17 drop_exact_final=0 | drop_vtrac_any=17 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=52 | exact_any=3 vtrac_any=38 | drop_exact_any=17 drop_vtrac_any=17 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=52 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.527143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 684 (canonical 468)
- Stamp (winner_stamp.json): items_total=166 | exact_any=1 exact_final=0 | vtrac_any=125 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=112 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=17 family_vtrac_final=0
- Flags (winner_flags.csv): rows=166 | exact_any=1 vtrac_any=125 | drop_exact_any=3 drop_vtrac_any=112 | family_exact_any=0 family_vtrac_any=17 | vt_boxed=27 vt_straight=0
- Hits (winner_hits.csv): rows=166 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=27 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.127143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 12.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 12.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.677143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 13.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 594 | score_v2 11.647143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 11.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 552 | score_v2 11.29381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 522 | score_v2 11.210476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 10.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 10.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 10.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 520 | score_v2 10.197143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 994 | score_v2 10.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): items_total=85 exact_any=0 vtrac_any=73 | top winner_present=False best_rank=None/24; Evening 221 (canon 122): items_total=52 exact_any=3 vtrac_any=38 | top winner_present=False best_rank=None/30; Combined 684 (canon 468): items_total=166 exact_any=1 vtrac_any=125 | top winner_present=False best_rank=None/32
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 594, 559, 552, 522.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_053050)

## Top indices (from enhanced JSON)
- index 23 | score 111.31747499999996 | features: presence=80.46997499999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 72.90816249999995 | features: presence=51.000662499999954, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 32 | score 54.507299999999994 | features: presence=41.499799999999986, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 29 | score 51.951825 | features: presence=35.744325, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 47.54967499999999 | features: presence=33.102174999999995, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 33 | score 47.48094999999999 | features: presence=30.203449999999993, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 42.728975 | features: presence=29.041475, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 30 | score 24.716700000000003 | features: presence=14.179200000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 24.122374999999998 | features: presence=14.544875, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 16.131825000000003 | features: presence=10.334325000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
138, 183, 386, 831, 813, 683, 793, 837, 681, 387

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 221 | index 20 | file Pennsylvania4_vtrac20_winner_221_20260105_052208.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 684 | index 24 | file Pennsylvania4_vtrac24_winner_684_20260105_052207.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 221 | index 20 rank 7/35 (rank_frac 0.2) | score 42.728975 (top 111.31747499999996, ratio 0.38384786395846665, delta 68.58849999999995) | winner_in_index_straights=False | top_index_straights: (none)
- winner 684 | index 24 rank 11/35 (rank_frac 0.3142857142857143) | score 11.875700000000002 (top 111.31747499999996, ratio 0.10668316003394801, delta 99.44177499999995) | winner_in_index_straights=False | top_index_straights: 963 (4.115), 364 (3.66), 341 (2.961)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 221→idx20 rank 7/35 (frac 0.200); 684→idx24 rank 11/35 (frac 0.314).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 18, 32, 29, 27.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2025-12-31)

## Midday winner 684 (canonical 468)
- Top lanes (hot_zones_top_lanes.csv): present | rank 183/205 (rank_frac 0.8926829268292683) | score_mean 13.865 (top 25.05, ratio 0.5534930139720559, delta 11.185)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 221 (canonical 122)
- Top lanes (hot_zones_top_lanes.csv): present | rank 191/205 (rank_frac 0.9317073170731708) | score_mean 13.362 (top 25.05, ratio 0.5334131736526946, delta 11.688)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 25.05 | tags hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vt_straight
- rank    2 | triad 006 | vt_triad 12 | score_mean 21.258 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vt_straight
- rank    3 | triad 016 | vt_triad 122 | score_mean 20.633 | tags hot16,hot20,ls_col_42,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 156 | vt_triad 122 | score_mean 20.633 | tags hot16,hot20,ls_col_42,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    5 | triad 239 | vt_triad 345 | score_mean 20.542 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 499 | vt_triad 55 | score_mean 20.488 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    7 | triad 155 | vt_triad 12 | score_mean 20.258 | tags hot12,hot16,hot20,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    8 | triad 046 | vt_triad 125 | score_mean 20.243 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 011 | vt_triad 12 | score_mean 19.841 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 001 | vt_triad 12 | score_mean 19.794 | tags hot12,hot16,hot20,hot8,set1_bonus,straight_lane,vertical2,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): rank 183/205 (rank_frac 0.893) ratio_to_top=0.5534930139720559; Evening 221 (canon 122): rank 191/205 (rank_frac 0.932) ratio_to_top=0.5334131736526946
- Q2: 4 hit criteria: Hot Zones is boxed-family pressure; use as support when Stable/DR identify the same family/lane.
- Q3: Winners artifacts alignment: winner_map is a top-20 snapshot; ‘not in map’ is not corruption if rank > 20.
- Q4: Dominance/noise: low rank_frac (<0.1) suggests good overlap; high rank_frac suggests weak Hot Zones isolation.
- Q5: Top lanes: see summary block; use best_rank and score_ratio_to_top as comparables across states/days.
- Q6: Miss analysis: if winner has weak rank or absent, treat as tool outcome; log and move on.
- Q7: Validation (V): gaps list should be empty; missing winner_map files = Fix-Now.
- Q8: Optimization notes: do not tune Hot Zones weights yet; accumulate day-level patterns first.
- Q9: Cross-tool synergy: Hot Zones is strongest when Stable compound + DR top patterns share the same family/VT lane.
- Q10: Takeaway: Hot Zones is a support lens; record overlap strength vs winners.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals: See Stable/DR/HotZones/VTRAC winners lines + Aux top candidates; log overlaps in Part 5.
- Conflicts/noise: If Stable exact hits are absent but other tools show heat, treat as noisy/negative-control; do not tune yet.
- Aggregator/aux hooks to test next: cross-variant bounce metrics + mirror/double pressure closure (Fix-Later).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-12-31/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=173, 186, 460, 239, 422
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=186, 239, 502, 264, 014
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=173, 460, 422, 065, 994

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=19 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=31), P2:4 (gap=24), P3:1 (gap=49)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=992 sev=B
- 666: ds=990 sev=B
- 159: ds=878 sev=B
- 007: ds=875 sev=B
- 088: ds=839 sev=B
- 008: ds=817 sev=B
- 444: ds=793 sev=B
- 039: ds=768 sev=B
- 355: ds=758 sev=B
- 344: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=135 sev=red
  - 77: ds=74 sev=blue
  - 88: ds=73 sev=blue
  - 44: ds=67 sev=purple
  - 66: ds=61 sev=purple
  - 55: ds=38 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=21 sev=-
  - 99: ds=8 sev=-
  - 22: ds=4 sev=-
- non_repeating:
  - 78: ds=68 sev=red
  - 12: ds=46 sev=blue
  - 03: ds=43 sev=blue
  - 07: ds=41 sev=blue
  - 35: ds=34 sev=purple
  - 69: ds=32 sev=purple
  - 36: ds=29 sev=purple
  - 09: ds=28 sev=purple
  - 34: ds=27 sev=purple
  - 38: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:277, 26:234, 16:92, 27:68, 7:60, 24:57, 6:55, 13:53, 19:49, 10:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=277 fs=2 fl=1 hz=0.007380073800738007, 26:ds=234 fs=0 fl=1 hz=0.003898635477582846, 16:ds=92 fs=3 fl=2 hz=0.007371007371007371, 27:ds=68 fs=11 fl=4 hz=0.01722158438576349, 7:ds=60 fs=36 fl=1 hz=0.03965702036441586, 24:ds=57 fs=44 fl=0 hz=0.048245614035087724, 6:ds=55 fs=22 fl=1 hz=0.02454642475987193, 13:ds=53 fs=21 fl=1 hz=0.024553571428571428, 19:ds=49 fs=21 fl=3 hz=0.025695931477516063, 10:ds=44 fs=24 fl=2 hz=0.027253668763102725

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=86 flags=purple
- S20: ds=73 flags=purple
- S6: ds=52 flags=purple
- S25: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=31 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=25), P2:7 (gap=20), P3:5 (gap=25)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=975 sev=B
- 288: ds=962 sev=B
- 255: ds=933 sev=B
- 668: ds=915 sev=B
- 199: ds=863 sev=B
- 499: ds=789 sev=B
- 399: ds=772 sev=B
- 039: ds=760 sev=B
- 448: ds=749 sev=B
- 005: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=184 sev=red
  - 99: ds=131 sev=red
  - 77: ds=74 sev=blue
  - 33: ds=67 sev=purple
  - 22: ds=60 sev=purple
  - 88: ds=36 sev=purple
  - 44: ds=33 sev=purple
  - 66: ds=30 sev=purple
  - 11: ds=11 sev=-
  - 00: ds=10 sev=-
- non_repeating:
  - 59: ds=77 sev=red
  - 79: ds=71 sev=red
  - 12: ds=46 sev=blue
  - 78: ds=44 sev=blue
  - 06: ds=41 sev=blue
  - 35: ds=38 sev=blue
  - 56: ds=30 sev=purple
  - 69: ds=28 sev=purple
  - 13: ds=23 sev=-
  - 57: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:373, 1:358, 34:212, 16:170, 15:161, 32:138, 35:115, 27:82, 28:60, 5:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=373 fs=0 fl=0 hz=0.0, 1:ds=358 fs=2 fl=2 hz=0.009124087591240877, 34:ds=212 fs=19 fl=1 hz=0.02631578947368421, 16:ds=170 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=161 fs=23 fl=0 hz=0.029411764705882353, 32:ds=138 fs=3 fl=1 hz=0.006720430107526881, 35:ds=115 fs=1 fl=1 hz=0.0035587188612099642, 27:ds=82 fs=22 fl=2 hz=0.028605482717520857, 28:ds=60 fs=26 fl=2 hz=0.02997858672376874, 5:ds=45 fs=18 fl=2 hz=0.022175290390707498

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=92 flags=red+purple
- S22: ds=77 flags=purple
- S23: ds=65 flags=purple
- S3: ds=59 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=61 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=27), P2:1 (gap=33), P3:1 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=971 sev=B
- 009: ds=929 sev=B
- 255: ds=887 sev=B
- 138: ds=827 sev=B
- 117: ds=810 sev=B
- 158: ds=772 sev=B
- 344: ds=765 sev=B
- 199: ds=756 sev=B
- 112: ds=716 sev=B
- 277: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=126 sev=red
  - 33: ds=68 sev=purple
  - 44: ds=39 sev=purple
  - 77: ds=37 sev=purple
  - 66: ds=35 sev=purple
  - 11: ds=26 sev=purple
  - 55: ds=19 sev=-
  - 00: ds=13 sev=-
  - 99: ds=4 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 68: ds=84 sev=red
  - 07: ds=61 sev=red
  - 15: ds=49 sev=blue
  - 38: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 03: ds=43 sev=blue
  - 78: ds=34 sev=purple
  - 19: ds=33 sev=purple
  - 28: ds=32 sev=purple
  - 01: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:615, 23:154, 26:117, 18:114, 13:63, 29:56, 33:48, 16:46, 30:45, 24:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=615 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=154 fs=17 fl=2 hz=0.025165562913907286, 26:ds=117 fs=2 fl=1 hz=0.0056657223796034, 18:ds=114 fs=23 fl=2 hz=0.02910360884749709, 13:ds=63 fs=20 fl=1 hz=0.024881516587677725, 29:ds=56 fs=16 fl=3 hz=0.020540540540540542, 33:ds=48 fs=19 fl=3 hz=0.023255813953488372, 16:ds=46 fs=5 fl=3 hz=0.009523809523809525, 30:ds=45 fs=35 fl=1 hz=0.03829787234042553, 24:ds=42 fs=37 fl=0 hz=0.04048140043763676

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=87 flags=blue+purple
- S1: ds=72 flags=blue+purple
- S5: ds=69 flags=purple
- S24: ds=55 flags=blue+purple
- S3: ds=43 flags=purple
- S20: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 128: score=1 tags=FLT
  - 138: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:768(B); midday:760(B)
- 066 -> combined:992(B); midday:738(B)
- 199 -> evening:756(B); midday:863(B)
- 255 -> evening:887(B); midday:933(B)
- 344 -> combined:687(B); evening:765(B)
- 444 -> combined:793(B); evening:971(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:43(blue); evening:43(blue)
- 07 -> combined:41(blue); evening:61(red)
- 12 -> combined:46(blue); midday:46(blue)
- 19 -> combined:25(purple); evening:33(purple)
- 33 -> combined:135(red); evening:68(purple); midday:67(purple)
- 35 -> combined:34(purple); midday:38(blue)
- 38 -> combined:27(purple); evening:48(blue)
- 44 -> combined:67(purple); evening:39(purple); midday:33(purple)
- 55 -> combined:38(purple); midday:184(red)
- 66 -> combined:61(purple); evening:35(purple); midday:30(purple)
- 69 -> combined:32(purple); midday:28(purple)
- 77 -> combined:74(blue); evening:37(purple); midday:74(blue)
- 78 -> combined:68(red); evening:34(purple); midday:44(blue)
- 88 -> combined:73(blue); evening:126(red); midday:36(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.55115)[R1,Mirror-Echo], 8(4.6125)[R2,Mirror-Echo], 7(3.0575714285714284)[R3,XVAR-Cons(CM)], 4(1.1179999999999999)[R2,Double-Pressure], 2(0.2746642857142857)[R3,Swap]
- P2: 1(3.2125714285714286)[R3,XVAR-Cons(CE)], 4(3.025821428571428)[R1,XVAR-Cons(CM)], 5(2.6621)[R2,XVAR-Cons(CE)], 7(1.4586428571428571)[R1,Mirror-Echo], 2(1.3267285714285713)[R2,Mirror-Echo]
- P3: 1(8.539385714285714)[R1,XVAR-Cons(CEM)], 5(1.4464285714285714)[R1,Double-Pressure], 6(1.3781571428571429)[R2,Mirror-Echo], 7(0.942)[R2,Double-Pressure], 3(0.3552785714285714)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:3(gap=31), P2:4(gap=24), P3:1(gap=49); top cartesian candidates: 311, 341, 351, 371, 321.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 015, 025, 035, 045, 056.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:768(B),midday:760(B); 066→combined:992(B),midday:738(B); 199→midday:863(B),evening:756(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:277, 26:234, 16:92, 27:68, 7:60.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=684 Evening=221; check whether winners appear in positional/BA candidate lists.
- Q8: Pack translation hook: use Aux positional shortlist to rank within the candidate universe selected from string tools.
- Q9: Synergy: strongest when Aux (positional/doubles/pairs) reinforces the same digit pool/VT lane seen in Part 2.
- Q10: Takeaway: record Aux as compounding evidence; do not treat as standalone caller until corpus is larger.

---

## Part 4 — Combination / Permutation Translation (candidate pack)
Use Part 4 prompts in the master template to produce:
- A small candidate universe per draw (Midday/Evening)
- Evidence vectors per candidate (tools + aux signals)
- Coverage mapping (perm-only vs boxed vs VTRAC-straight vs full index-box)

Reference:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

Part 4 notes / answers:
- Candidate universe (Midday): BOX 468 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 122 (post-hoc); Stable exact_boxed=False
- Evidence vectors: Use Stable/DR/HotZones/VTRAC summaries + Aux shortlist tags to justify pack size/mode.
- Coverage mapping + pack decision: Rule of thumb: BOX when family present but permutation unclear; VTRAC-straight when lanes are clean; index-box only when uncertainty is high.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday winner 684 (canon 468): box `468` covers winner `684` (boxed hit).
  - Evening winner 221 (canon 122): box `122` covers winner `221` (boxed hit).
- Key tags:
  - cross-variant convergence | VT lane density | doubles/mirror pressure | hot columns/col1 funnels | Aux positional pressure
- Drivers:
  - Overall: weak/noisy (no exact Stable hit; rely on cross-tool/Aux).
- Conflicts:
  - If tools disagree (Stable/DR/VTRAC/HotZones), treat as noisy day; log as negative-control (do not tune yet).
- Fix-now vs fix-later:
  - Fix-now: none (sharepack artifacts exist; audit PASS).
  - Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
- Next run:
  - Continue filling remaining states/days; then generate day synthesis + re-export corpus summary.
