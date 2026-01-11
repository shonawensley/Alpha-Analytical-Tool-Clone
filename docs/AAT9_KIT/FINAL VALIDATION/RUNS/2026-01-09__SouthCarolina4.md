# Master Validation Run Report — SouthCarolina4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-09/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-09/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-09/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-09/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-09/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-09/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac12_winner_295_20260110_035106.html`
- `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac7_winner_067_20260110_035104.html`

Winners JSON files:
- `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac12_winner_295_20260110_035106.json`
- `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac7_winner_067_20260110_035104.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 067 (canon 067): exact_boxed=True exact_straight=True | rank 1626/5112 (rank_frac 0.318); Evening 295 (canon 259): exact_boxed=True exact_straight=True | rank 475/5112 (rank_frac 0.093)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 295 idx12 (rank 8/35, frac 0.229), 067 idx7 (rank 18/35, frac 0.514)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — SouthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-09)

## Midday winner 067 (canonical 067)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=7 | family_rows=162 | exact_boxed=7 | exact_straight=7 | vt_boxed=7
- Scores (patterns_scores.csv): rank 1626/5112 (rank_frac 0.318075117370892) | score 14.0 (top 37.5, ratio 0.37333333333333335, delta 23.5) | section Midday, Set Set1, Draw Draw4, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 253/1842 (rank_frac 0.13735070575461455) | score 22.0 (top 83.5, ratio 0.2634730538922156, delta 61.5) | section Midday, col1_hits 0, hot2 2, set_chain 1, draw_chain 3 | why draw_chain3|hot2x2|vstrx5
- Families (patterns_families.csv): count 45 | rank 644/1423 (rank_frac 0.45256500351370343) | score 15.0 (top 37.5, ratio 0.4, delta 22.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=62

## Evening winner 295 (canonical 259)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=23 | family_rows=404 | exact_boxed=23 | exact_straight=14 | vt_boxed=23
- Scores (patterns_scores.csv): rank 475/5112 (rank_frac 0.09291862284820031) | score 18.5 (top 37.5, ratio 0.49333333333333335, delta 19.0) | section Evening, Set Set1, Draw Draw7, Col 1, hot 0, vt_straight 2.0 | why straight|cov2|vstr2|hidden3v|vtrac_straight|set_chain3|draw_chain3
- Compound (patterns_compound.csv): rank 144/1842 (rank_frac 0.0781758957654723) | score 27.0 (top 83.5, ratio 0.32335329341317365, delta 56.5) | section Evening, col1_hits 1, hot2 0, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|col1x1|hot1x1|vstrx1
- Families (patterns_families.csv): count 68 | rank 81/1423 (rank_frac 0.05692199578355587) | score 26.5 (top 37.5, ratio 0.7066666666666667, delta 11.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=117

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 059 | section Combined | score 83.5 | col1_hits 7 | hot2 10
- rank    6 | canon 579 | section Evening | score 63.5 | col1_hits 4 | hot2 8
- rank    8 | canon 049 | section Combined | score 62.5 | col1_hits 4 | hot2 8
- rank   17 | canon 459 | section Combined | score 55.0 | col1_hits 5 | hot2 7
- rank    3 | canon 099 | section Combined | score 68.0 | col1_hits 1 | hot2 6
- rank   30 | canon 569 | section Evening | score 46.0 | col1_hits 4 | hot2 6
- rank    5 | canon 599 | section Evening | score 66.5 | col1_hits 0 | hot2 6
- rank   22 | canon 678 | section Evening | score 52.0 | col1_hits 5 | hot2 6
- rank   23 | canon 00599 | section Combined | score 51.0 | col1_hits 0 | hot2 6
- rank   11 | canon 445 | section Midday | score 59.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1367 | family 29 | score 6.0 | hot2 0 | section Midday
- rank 1367 | family 4 | score 6.0 | hot2 0 | section Midday
- rank  554 | family 21 | score 16.0 | hot2 0 | section Midday
- rank  644 | family 10 | score 15.0 | hot2 0 | section Midday
- rank  728 | family 18 | score 14.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 067 (canon 067): exact_boxed=True exact_straight=True | rank 1626/5112 (rank_frac 0.318); Evening 295 (canon 259): exact_boxed=True exact_straight=True | rank 475/5112 (rank_frac 0.093)
- Q2: 4 hit criteria: see metrics_hits per winner (exact_boxed/exact_straight + vt_boxed_count).
- Q3: Winners artifacts alignment: spotlight + metrics.json consistent (see summary block).
- Q4: Dominance/noise: isolates both winners (exact boxed); use rank_frac + score_ratio_to_top to gauge strength.
- Q5: Top candidate clusters (compound canonicals): .
- Q6: Miss analysis: if a winner is absent/low, treat as tool outcome (not pipeline failure) unless gaps are listed.
- Q7: Validation (V): gaps list should be empty; if non-empty, flag as Fix-Now.
- Q8: Optimization notes: do not tune on 1 day; accumulate across days then adjust weights (Fix-Later).
- Q9: Cross-tool synergy: compare top compound canonicals vs DR top candidates + Hot Zones top lanes + Aux positional shortlist.
- Q10: Takeaway: Stable isolates both winners (exact boxed).

---

### 2.Digit Reduction — SouthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260110)

## Midday winner 067 (canonical 067)
- Stamp (winner_stamp.json): items_total=24 | exact_any=0 exact_final=0 | vtrac_any=24 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=12 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=24 | exact_any=0 vtrac_any=24 | drop_exact_any=0 drop_vtrac_any=12 | family_exact_any=0 family_vtrac_any=12 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=24 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=38 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 295 (canonical 259)
- Stamp (winner_stamp.json): items_total=142 | exact_any=98 exact_final=0 | vtrac_any=107 vtrac_final=0 | drop_exact_any=134 drop_exact_final=0 | drop_vtrac_any=138 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=30 family_vtrac_final=0
- Flags (winner_flags.csv): rows=142 | exact_any=98 vtrac_any=107 | drop_exact_any=134 drop_vtrac_any=138 | family_exact_any=0 family_vtrac_any=30 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=142 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=8 | winner_present=True | winner_best_rank=36 | winner_rank_fraction=4.5 | winner_score_v2=6.997143 top_score_v2=14.077143 | winner_score_ratio_to_top=0.4970570377810327 winner_score_delta_from_top=7.079999999999999
- Reducer scores present: True

## Combined winner 067 (canonical 067)
- Stamp (winner_stamp.json): items_total=81 | exact_any=2 exact_final=0 | vtrac_any=76 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=17 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=81 | exact_any=2 vtrac_any=76 | drop_exact_any=0 drop_vtrac_any=17 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=9 vt_straight=0
- Hits (winner_hits.csv): rows=81 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=9 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 14.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 13.127143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 13.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 12.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.927143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 599 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 11.727143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 559 | score_v2 14.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 12.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 599 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 599 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 11.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 594 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 990 | score_v2 9.94381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 559 | score_v2 9.847143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 599 | score_v2 9.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 067 (canon 067): items_total=24 exact_any=0 vtrac_any=24 | top winner_present=False best_rank=None/38; Evening 295 (canon 259): items_total=142 exact_any=98 vtrac_any=107 | top winner_present=True best_rank=36/8; Combined 067 (canon 067): items_total=81 exact_any=2 vtrac_any=76 | top winner_present=False best_rank=None/14
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 599, 599.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260110_035304)

## Top indices (from enhanced JSON)
- index 15 | score 46.68979000000001 | features: presence=32.79229000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 37.28745 | features: presence=26.289949999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 32.77875 | features: presence=19.65125, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 14 | score 31.683922499999994 | features: presence=14.306422499999993, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 30 | score 27.066050000000004 | features: presence=13.398550000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 28 | score 23.647050000000004 | features: presence=14.829550000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 31 | score 20.788350000000005 | features: presence=11.670850000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 15.101816666666666 | features: presence=7.999525, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 11.954600000000001 | features: presence=5.677100000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 11.164858333333333 | features: presence=4.7159, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
903, 937, 093, 940, 934, 932, 034, 793, 403, 923

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 295 | index 12 | file SouthCarolina4_vtrac12_winner_295_20260110_035106.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 067 | index 7 | file SouthCarolina4_vtrac7_winner_067_20260110_035104.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 295 | index 12 rank 8/35 (rank_frac 0.22857142857142856) | score 15.101816666666666 (top 46.68979000000001, ratio 0.32345008762443916, delta 31.587973333333345) | winner_in_index_straights=False | top_index_straights: 024 (6.207), 709 (2.701), 290 (2.207)
- winner 067 | index 7 rank 18/35 (rank_frac 0.5142857142857142) | score 4.990958333333333 (top 46.68979000000001, ratio 0.10689614010543488, delta 41.69883166666668) | winner_in_index_straights=False | top_index_straights: 170 (1.576), 701 (1.326), 201 (1.1)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 295→idx12 rank 8/35 (frac 0.229); 067→idx7 rank 18/35 (frac 0.514).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 15, 5, 34, 14, 30.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-09)

## Midday winner 067 (canonical 067)
- Top lanes (hot_zones_top_lanes.csv): present | rank 204/210 (rank_frac 0.9714285714285714) | score_mean 14.097 (top 24.808, ratio 0.5682441148016769, delta 10.711)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 295 (canonical 259)
- Top lanes (hot_zones_top_lanes.csv): present | rank 83/210 (rank_frac 0.3952380952380952) | score_mean 17.216 (top 24.808, ratio 0.6939696871976783, delta 7.591999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 24.808 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 227 | vt_triad 33 | score_mean 23.758 | tags funnel_precol1,guard_set1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 336 | vt_triad 24 | score_mean 21.242 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 288 | vt_triad 34 | score_mean 21.123 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 127 | vt_triad 233 | score_mean 21.05 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 124 | vt_triad 235 | score_mean 20.785 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 279 | vt_triad 335 | score_mean 20.763 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 247 | vt_triad 335 | score_mean 20.621 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 117 | vt_triad 23 | score_mean 20.406 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 224 | vt_triad 35 | score_mean 20.134 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 067 (canon 067): rank 204/210 (rank_frac 0.971) ratio_to_top=0.5682441148016769; Evening 295 (canon 259): rank 83/210 (rank_frac 0.395) ratio_to_top=0.6939696871976783
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

Aux draws snapshot dir: `sharepacks/2026-01-09/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-09/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=910, 277, 336, 288, 412
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-09/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=277, 288, 586, 171, 189
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-09/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=910, 336, 412, 712, 432

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=2 last_repeat_gap=28 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=16), P2:9 (gap=30), P3:5 (gap=20)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.81307678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=42.07872142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=37.795112142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 665: score=35.2648 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 694: score=35.19807857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 645: score=35.02445 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 698: score=33.38130714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=33.37562857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=33.308907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 845: score=33.13527857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=983 sev=B
- 449: ds=912 sev=B
- 156: ds=895 sev=B
- 778: ds=865 sev=B
- 279: ds=864 sev=B
- 033: ds=796 sev=B
- 004: ds=784 sev=B
- 688: ds=751 sev=B
- 278: ds=718 sev=B
- 377: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=192 sev=red
  - 55: ds=129 sev=red
  - 22: ds=75 sev=blue
  - 66: ds=63 sev=purple
  - 00: ds=36 sev=purple
  - 44: ds=15 sev=-
  - 11: ds=7 sev=-
  - 88: ds=3 sev=-
  - 33: ds=2 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 78: ds=64 sev=red
  - 29: ds=45 sev=blue
  - 06: ds=38 sev=blue
  - 16: ds=38 sev=blue
  - 59: ds=34 sev=purple
  - 13: ds=30 sev=purple
  - 39: ds=30 sev=purple
  - 07: ds=27 sev=purple
  - 37: ds=27 sev=purple
  - 02: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:456, 35:399, 1:180, 31:130, 4:121, 28:113, 27:96, 19:80, 18:74, 7:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=456 fs=0 fl=0 hz=0.002197802197802198, 35:ds=399 fs=0 fl=0 hz=0.001949317738791423, 1:ds=180 fs=5 fl=4 hz=0.011627906976744186, 31:ds=130 fs=26 fl=0 hz=0.03002309468822171, 4:ds=121 fs=21 fl=2 hz=0.026589595375722544, 28:ds=113 fs=16 fl=2 hz=0.021479713603818614, 27:ds=96 fs=26 fl=0 hz=0.02911534154535274, 19:ds=80 fs=15 fl=1 hz=0.0189520624303233, 18:ds=74 fs=17 fl=1 hz=0.019801980198019802, 7:ds=71 fs=49 fl=1 hz=0.05411255411255411

### Sums (source: aux_validation.sums_stats_by_variant)
- S17: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=78 flags=blue+purple
- S23: ds=67 flags=purple
- S5: ds=66 flags=purple
- S24: ds=64 flags=blue+purple
- S4: ds=56 flags=purple
- S3: ds=55 flags=blue+purple

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
- current_index=26 streak=1 max=3 last_repeat_gap=9 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=19), P2:3 (gap=45), P3:2 (gap=10)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.81307678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=42.07872142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=37.795112142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 665: score=35.2648 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 694: score=35.19807857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 645: score=35.02445 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 698: score=33.38130714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=33.37562857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=33.308907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 845: score=33.13527857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=878 sev=B
- 222: ds=855 sev=B
- 337: ds=832 sev=B
- 003: ds=823 sev=B
- 228: ds=814 sev=B
- 556: ds=716 sev=B
- 449: ds=674 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=118 sev=red
  - 55: ds=82 sev=blue
  - 33: ds=45 sev=purple
  - 22: ds=41 sev=purple
  - 66: ds=28 sev=purple
  - 00: ds=19 sev=-
  - 44: ds=11 sev=-
  - 11: ds=3 sev=-
  - 88: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 49: ds=59 sev=red
  - 67: ds=53 sev=blue
  - 34: ds=52 sev=blue
  - 07: ds=37 sev=blue
  - 05: ds=34 sev=purple
  - 15: ds=32 sev=purple
  - 78: ds=31 sev=purple
  - 69: ds=30 sev=purple
  - 16: ds=28 sev=purple
  - 48: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:419, 35:183, 27:148, 6:116, 5:85, 1:82, 15:77, 34:63, 31:59, 20:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=419 fs=1 fl=2 hz=0.006993006993006993, 35:ds=183 fs=1 fl=1 hz=0.004968944099378882, 27:ds=148 fs=18 fl=3 hz=0.026582278481012658, 6:ds=116 fs=24 fl=2 hz=0.02957906712172924, 5:ds=85 fs=20 fl=1 hz=0.023102310231023104, 1:ds=82 fs=7 fl=3 hz=0.012127894156560088, 15:ds=77 fs=17 fl=3 hz=0.021691973969631236, 34:ds=63 fs=28 fl=1 hz=0.03159041394335512, 31:ds=59 fs=33 fl=0 hz=0.035752979414951244, 20:ds=58 fs=23 fl=2 hz=0.027173913043478264

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S25: ds=83 flags=purple
- S21: ds=63 flags=purple
- S20: ds=59 flags=purple
- S17: ds=57 flags=purple
- S8: ds=55 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=4 tags=FLT,MIR,RS
  - 368: score=4 tags=FLT,MIR,RS
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 278: score=3 tags=MIR,RS
  - 359: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=37 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=23), P2:9 (gap=19), P3:8 (gap=26)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.81307678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=42.07872142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=37.795112142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 665: score=35.2648 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 694: score=35.19807857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 645: score=35.02445 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 698: score=33.38130714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=33.37562857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=33.308907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 845: score=33.13527857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=987 sev=B
- 117: ds=898 sev=B
- 005: ds=884 sev=B
- 577: ds=861 sev=B
- 155: ds=841 sev=B
- 777: ds=840 sev=B
- 669: ds=832 sev=B
- 179: ds=814 sev=B
- 366: ds=780 sev=B
- 222: ds=774 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=104 sev=blue
  - 77: ds=91 sev=blue
  - 66: ds=83 sev=blue
  - 55: ds=70 sev=purple
  - 88: ds=64 sev=purple
  - 22: ds=41 sev=purple
  - 11: ds=30 sev=purple
  - 00: ds=20 sev=-
  - 44: ds=8 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 58: ds=105 sev=red
  - 35: ds=72 sev=red
  - 29: ds=67 sev=red
  - 47: ds=57 sev=red
  - 78: ds=35 sev=purple
  - 68: ds=32 sev=purple
  - 38: ds=26 sev=purple
  - 13: ds=24 sev=-
  - 39: ds=22 sev=-
  - 06: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:492, 1:279, 32:246, 31:225, 4:145, 28:118, 19:114, 26:91, 16:87, 13:86

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=492 fs=3 fl=1 hz=0.017391304347826087, 1:ds=279 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=246 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=225 fs=15 fl=1 hz=0.023289665211062592, 4:ds=145 fs=21 fl=3 hz=0.028742514970059883, 28:ds=118 fs=10 fl=4 hz=0.017676767676767676, 19:ds=114 fs=12 fl=2 hz=0.016968325791855206, 26:ds=91 fs=0 fl=0 hz=0.002347417840375587, 16:ds=87 fs=6 fl=4 hz=0.011820330969267141, 13:ds=86 fs=22 fl=0 hz=0.024363233665559245

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=70 flags=purple
- S15: ds=61 flags=red+purple
- S17: ds=57 flags=purple
- S23: ds=54 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:774(B); midday:855(B)
- 235 -> combined:667(B); evening:693(B)
- 366 -> combined:983(B); evening:780(B)
- 449 -> combined:912(B); midday:674(B)
- 688 -> combined:751(B); evening:739(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:27(purple); midday:37(blue)
- 16 -> combined:38(blue); midday:28(purple)
- 22 -> combined:75(blue); evening:41(purple); midday:41(purple)
- 29 -> combined:45(blue); evening:67(red)
- 55 -> combined:129(red); evening:70(purple); midday:82(blue)
- 66 -> combined:63(purple); evening:83(blue); midday:28(purple)
- 78 -> combined:64(red); evening:35(purple); midday:31(purple)
- 99 -> combined:192(red); evening:104(blue); midday:118(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(4.079571428571429)[R1,XVAR-Cons(CE)], 8(3.1904000000000003)[R2,XVAR-Cons(CM)], 0(2.7945714285714285)[R3,XVAR-Cons(CM)], 1(1.4001428571428571)[R2,Mirror-Echo], 5(0.22840714285714284)[R3]
- P2: 9(7.855449999999999)[R1,Mirror-Echo], 6(2.652357142857143)[R2,XVAR-Cons(CE)], 4(2.412007142857143)[R3,Mirror-Echo], 3(1.7449999999999999)[R1,Double-Pressure], 0(1.0135)[R2,Double-Pressure]
- P3: 5(7.032871428571429)[R1,XVAR-Cons(CEM)], 4(1.7630571428571429)[R3,XVAR-Cons(CM)], 8(1.4462857142857144)[R1,Double-Pressure], 3(1.0519999999999998)[R2,Double-Pressure], 2(0.29857142857142854)[R1]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=16), P2:9(gap=30), P3:5(gap=20); top cartesian candidates: 695, 895, 595, 665, 694.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 015, 025, 035, 045, 056.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:855(B),evening:774(B); 235→combined:667(B),evening:693(B); 366→combined:983(B),evening:780(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:456, 35:399, 1:180, 31:130, 4:121.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=067 Evening=295; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 067 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 259 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 067 (canon 067): box `067` covers winner `067` (boxed hit).
  - Evening winner 295 (canon 259): box `259` covers winner `295` (boxed hit).
- Key tags:
  - cross-variant convergence | VT lane density | doubles/mirror pressure | hot columns/col1 funnels | Aux positional pressure
- Drivers:
  - Overall: strong (Stable exact boxed hits).
- Conflicts:
  - If tools disagree (Stable/DR/VTRAC/HotZones), treat as noisy day; log as negative-control (do not tune yet).
- Fix-now vs fix-later:
  - Fix-now: none (sharepack artifacts exist; audit PASS).
  - Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
- Next run:
  - Continue filling remaining states/days; then generate day synthesis + re-export corpus summary.
