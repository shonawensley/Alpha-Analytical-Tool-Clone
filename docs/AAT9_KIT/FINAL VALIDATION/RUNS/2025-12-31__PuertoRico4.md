# Master Validation Run Report — PuertoRico4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/PuertoRico4/`
- Winners lens: `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2025-12-31/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2025-12-31/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2025-12-31/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2025-12-31/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2025-12-31/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2025-12-31/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac24_winner_913_20260105_052211.html`
- `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac9_winner_451_20260105_052209.html`

Winners JSON files:
- `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac24_winner_913_20260105_052211.json`
- `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac9_winner_451_20260105_052209.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 451 (canon 145): exact_boxed=True exact_straight=True | rank 2596/5516 (rank_frac 0.471); Evening 913 (canon 139): exact_boxed=True exact_straight=True | rank 2596/5516 (rank_frac 0.471)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 913 idx24 (rank 6/35, frac 0.171), 451 idx9 (rank 12/35, frac 0.343)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
- Q7: Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy.
- Q8: Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries).
- Q9: Aux cues: BA score=1 (if None, BA not available); see Part 3 positional/doubles/pairs notes.
- Q10: 4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank).
- Q11: Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table.
- Q12: Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days.
- Q13: Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance.
- Q14: Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — PuertoRico4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2025-12-31)

## Midday winner 451 (canonical 145)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=5 | family_rows=266 | exact_boxed=5 | exact_straight=5 | vt_boxed=5
- Scores (patterns_scores.csv): rank 2596/5516 (rank_frac 0.4706308919506889) | score 13.5 (top 37.0, ratio 0.36486486486486486, delta 23.5) | section Combined, Set Set3, Draw Draw1, Col 3, hot 1, vt_straight 2.0 | why straight|cov1|hot1|hidden3v|vtrac_straight|set_chain3
- Compound (patterns_compound.csv): rank 270/1762 (rank_frac 0.1532349602724177) | score 23.0 (top 97.0, ratio 0.23711340206185566, delta 74.0) | section Combined, col1_hits 0, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|hot1x4|vstrx1
- Families (patterns_families.csv): count 60 | rank 368/1371 (rank_frac 0.2684172137126185) | score 19.5 (top 36.5, ratio 0.5342465753424658, delta 17.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=74

## Evening winner 913 (canonical 139)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=4 | family_rows=662 | exact_boxed=4 | exact_straight=4 | vt_boxed=4
- Scores (patterns_scores.csv): rank 2596/5516 (rank_frac 0.4706308919506889) | score 13.5 (top 37.0, ratio 0.36486486486486486, delta 23.5) | section Combined, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|hidden3v|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 388/1762 (rank_frac 0.22020431328036322) | score 20.0 (top 97.0, ratio 0.20618556701030927, delta 77.0) | section Combined, col1_hits 2, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|col1x2|hot1x1|vstrx4
- Families (patterns_families.csv): count 77 | rank 22/1371 (rank_frac 0.016046681254558718) | score 30.5 (top 36.5, ratio 0.8356164383561644, delta 6.0) | section Combined, hot2 5
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=172

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 344 | section Midday | score 97.0 | col1_hits 8 | hot2 11
- rank    2 | canon 445 | section Midday | score 83.0 | col1_hits 8 | hot2 11
- rank    4 | canon 345 | section Midday | score 68.5 | col1_hits 5 | hot2 9
- rank    5 | canon 3445 | section Midday | score 68.0 | col1_hits 5 | hot2 9
- rank    3 | canon 144 | section Midday | score 72.5 | col1_hits 6 | hot2 8
- rank   15 | canon 1344 | section Midday | score 57.0 | col1_hits 6 | hot2 8
- rank    8 | canon 116 | section Combined | score 64.0 | col1_hits 5 | hot2 7
- rank   52 | canon 135 | section Midday | score 37.5 | col1_hits 4 | hot2 6
- rank   34 | canon 134 | section Midday | score 42.0 | col1_hits 3 | hot2 6
- rank   20 | canon 11344 | section Midday | score 51.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1367 | family 7 | score 3.0 | hot2 0 | section Midday
- rank  550 | family 32 | score 17.0 | hot2 0 | section Midday
- rank  679 | family 23 | score 15.0 | hot2 0 | section Midday
- rank  800 | family 6 | score 13.5 | hot2 0 | section Midday
- rank  836 | family 13 | score 13.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 451 (canon 145): exact_boxed=True exact_straight=True | rank 2596/5516 (rank_frac 0.471); Evening 913 (canon 139): exact_boxed=True exact_straight=True | rank 2596/5516 (rank_frac 0.471)
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

### 2.Digit Reduction — PuertoRico4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260105)

## Midday winner 451 (canonical 145)
- Stamp (winner_stamp.json): items_total=132 | exact_any=31 exact_final=0 | vtrac_any=115 vtrac_final=0 | drop_exact_any=54 drop_exact_final=0 | drop_vtrac_any=57 drop_vtrac_final=0 | family_exact_any=9 family_exact_final=0 | family_vtrac_any=31 family_vtrac_final=0
- Flags (winner_flags.csv): rows=132 | exact_any=31 vtrac_any=115 | drop_exact_any=54 drop_vtrac_any=57 | family_exact_any=9 family_vtrac_any=31 | vt_boxed=46 vt_straight=0
- Hits (winner_hits.csv): rows=132 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=46 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.387143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 913 (canonical 139)
- Stamp (winner_stamp.json): items_total=100 | exact_any=0 exact_final=0 | vtrac_any=100 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=26 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=100 | exact_any=0 vtrac_any=100 | drop_exact_any=1 drop_vtrac_any=26 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=100 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.54381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 451 (canonical 145)
- Stamp (winner_stamp.json): items_total=466 | exact_any=87 exact_final=0 | vtrac_any=353 vtrac_final=0 | drop_exact_any=203 drop_exact_final=0 | drop_vtrac_any=214 drop_vtrac_final=0 | family_exact_any=9 family_exact_final=0 | family_vtrac_any=75 family_vtrac_final=0
- Flags (winner_flags.csv): rows=466 | exact_any=87 vtrac_any=353 | drop_exact_any=203 drop_vtrac_any=214 | family_exact_any=9 family_vtrac_any=75 | vt_boxed=69 vt_straight=0
- Hits (winner_hits.csv): rows=466 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=69 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=True | winner_best_rank=30 | winner_rank_fraction=1.1538461538461537 | winner_score_v2=8.727143 top_score_v2=17.777143 | winner_score_ratio_to_top=0.490919322638064 winner_score_delta_from_top=9.049999999999999
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 221 | score_v2 17.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 221 | score_v2 12.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 559 | score_v2 11.387143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 559 | score_v2 11.387143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 10.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 10.537143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 4 | pattern 559 | score_v2 10.387143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 4 | pattern 559 | score_v2 10.387143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 10.337143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 522 | score_v2 10.327143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 221 | score_v2 17.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 221 | score_v2 12.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 11.387143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 559 | score_v2 11.387143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 522 | score_v2 10.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 592 | score_v2 10.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 554 | score_v2 9.965714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 554 | score_v2 9.965714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 241 | score_v2 9.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 413 | score_v2 9.697143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 451 (canon 145): items_total=132 exact_any=31 vtrac_any=115 | top winner_present=False best_rank=None/12; Evening 913 (canon 139): items_total=100 exact_any=0 vtrac_any=100 | top winner_present=False best_rank=None/22; Combined 451 (canon 145): items_total=466 exact_any=87 vtrac_any=353 | top winner_present=True best_rank=30/26
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 221, 221, 559, 559, 522.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260105_053051)

## Top indices (from enhanced JSON)
- index 15 | score 57.245974999999994 | features: presence=36.708475, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 43.042415000000005 | features: presence=24.842415000000003, set_echo=0.6, first_hit=0.4, column_span=0.25
- index 5 | score 39.86125 | features: presence=21.31375, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 34.97208 | features: presence=16.63458, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 33.496125 | features: presence=20.4205, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 30.183390000000003 | features: presence=13.775890000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 4 | score 26.106000000000005 | features: presence=13.078500000000002, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 31 | score 22.868375 | features: presence=14.720875000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 14 | score 21.989800000000002 | features: presence=9.5623, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 21.900230000000004 | features: presence=13.862729999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
624, 416, 641, 264, 164, 614, 246, 186, 418, 584

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 913 | index 24 | file PuertoRico4_vtrac24_winner_913_20260105_052211.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 451 | index 9 | file PuertoRico4_vtrac9_winner_451_20260105_052209.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 913 | index 24 rank 6/35 (rank_frac 0.17142857142857143) | score 30.183390000000003 (top 57.245974999999994, ratio 0.5272578552465916, delta 27.06258499999999) | winner_in_index_straights=False | top_index_straights: 418 (9.448), 864 (9.005), 684 (8.52)
- winner 451 | index 9 rank 12/35 (rank_frac 0.34285714285714286) | score 19.121337500000003 (top 57.245974999999994, ratio 0.33402064511959145, delta 38.12463749999999) | winner_in_index_straights=False | top_index_straights: 564 (6.516), 154 (6.099), 541 (5.478)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 913→idx24 rank 6/35 (frac 0.171); 451→idx9 rank 12/35 (frac 0.343).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 15, 19, 5, 34, 22.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2025-12-31)

## Midday winner 451 (canonical 145)
- Top lanes (hot_zones_top_lanes.csv): present | rank 63/207 (rank_frac 0.30434782608695654) | score_mean 17.978 (top 25.1, ratio 0.7162549800796812, delta 7.122)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 913 (canonical 139)
- Top lanes (hot_zones_top_lanes.csv): present | rank 166/207 (rank_frac 0.8019323671497585) | score_mean 15.654 (top 25.1, ratio 0.6236653386454183, delta 9.446000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 25.1 | tags hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vt_straight
- rank    2 | triad 379 | vt_triad 345 | score_mean 23.261 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    3 | triad 578 | vt_triad 134 | score_mean 22.155 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 029 | vt_triad 135 | score_mean 21.7 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 007 | vt_triad 13 | score_mean 21.038 | tags hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical4,vertical5,vt_only_lane,vt_straight
- rank    6 | triad 447 | vt_triad 35 | score_mean 20.512 | tags funnel_precol1,hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 445 | vt_triad 15 | score_mean 20.453 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 344 | vt_triad 45 | score_mean 20.339 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 299 | vt_triad 35 | score_mean 20.3 | tags funnel_precol1,hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 225 | vt_triad 13 | score_mean 20.254 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 451 (canon 145): rank 63/207 (rank_frac 0.304) ratio_to_top=0.7162549800796812; Evening 913 (canon 139): rank 166/207 (rank_frac 0.802) ratio_to_top=0.6236653386454183
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

Aux draws snapshot dir: `sharepacks/2025-12-31/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=643, 098, 785, 875, 490
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=098, 875, 793, 962, 087
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=643, 785, 490, 902, 517

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=3 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=56), P2:5 (gap=25), P3:9 (gap=31)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=56)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=989 sev=B
- 447: ds=980 sev=B
- 000: ds=728 sev=B
- 039: ds=716 sev=B
- 466: ds=712 sev=B
- 677: ds=690 sev=B
- 259: ds=681 sev=B
- 577: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=60 sev=purple
  - 77: ds=59 sev=purple
  - 99: ds=50 sev=purple
  - 44: ds=45 sev=purple
  - 11: ds=44 sev=purple
  - 55: ds=25 sev=purple
  - 33: ds=20 sev=-
  - 66: ds=19 sev=-
  - 88: ds=12 sev=-
  - 00: ds=10 sev=-
- non_repeating:
  - 47: ds=168 sev=red
  - 24: ds=82 sev=red
  - 45: ds=79 sev=red
  - 25: ds=57 sev=red
  - 48: ds=46 sev=blue
  - 23: ds=43 sev=blue
  - 56: ds=39 sev=blue
  - 59: ds=39 sev=blue
  - 05: ds=37 sev=blue
  - 19: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:187, 27:128, 5:91, 32:85, 26:80, 31:77, 28:59, 18:51, 34:50, 33:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=187 fs=18 fl=1 hz=0.025477707006369428, 27:ds=128 fs=24 fl=1 hz=0.029868578255675033, 5:ds=91 fs=27 fl=1 hz=0.0343980343980344, 32:ds=85 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=80 fs=4 fl=2 hz=0.01020408163265306, 31:ds=77 fs=14 fl=3 hz=0.018619934282584887, 28:ds=59 fs=26 fl=0 hz=0.0278372591006424, 18:ds=51 fs=20 fl=0 hz=0.022727272727272728, 34:ds=50 fs=26 fl=0 hz=0.02857142857142857, 33:ds=47 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=77 flags=purple
- S23: ds=59 flags=blue+purple
- S26: ds=50 flags=blue+purple
- S8: ds=44 flags=purple
- S6: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=58 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=28), P2:1 (gap=24), P3:1 (gap=17)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=958 sev=B
- 299: ds=949 sev=B
- 003: ds=940 sev=B
- 077: ds=926 sev=B
- 333: ds=875 sev=B
- 555: ds=849 sev=B
- 088: ds=820 sev=B
- 888: ds=814 sev=B
- 666: ds=799 sev=B
- 447: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=105 sev=blue
  - 22: ds=78 sev=blue
  - 11: ds=54 sev=purple
  - 99: ds=38 sev=purple
  - 77: ds=29 sev=purple
  - 33: ds=23 sev=-
  - 44: ds=22 sev=-
  - 88: ds=20 sev=-
  - 55: ds=12 sev=-
  - 66: ds=9 sev=-
- non_repeating:
  - 47: ds=111 sev=red
  - 24: ds=57 sev=red
  - 38: ds=42 sev=blue
  - 03: ds=41 sev=blue
  - 04: ds=41 sev=blue
  - 35: ds=39 sev=blue
  - 45: ds=39 sev=blue
  - 48: ds=31 sev=purple
  - 19: ds=30 sev=purple
  - 25: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:137, 29:95, 10:93, 27:92, 26:89, 3:82, 16:54, 23:49, 15:47, 5:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=137 fs=18 fl=0 hz=0.02211874272409779, 29:ds=95 fs=16 fl=2 hz=0.020809248554913295, 10:ds=93 fs=20 fl=3 hz=0.026376146788990827, 27:ds=92 fs=19 fl=1 hz=0.024721878862793572, 26:ds=89 fs=7 fl=2 hz=0.011682242990654207, 3:ds=82 fs=31 fl=0 hz=0.03506787330316742, 16:ds=54 fs=4 fl=2 hz=0.009695290858725763, 23:ds=49 fs=31 fl=1 hz=0.034782608695652174, 15:ds=47 fs=25 fl=0 hz=0.026939655172413795, 5:ds=45 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=41 flags=purple
- S25: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=7 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=28), P2:5 (gap=44), P3:6 (gap=20)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=990 sev=B
- 579: ds=971 sev=B
- 114: ds=915 sev=B
- 555: ds=854 sev=B
- 888: ds=762 sev=B
- 067: ds=751 sev=B
- 446: ds=738 sev=B
- 259: ds=736 sev=B
- 224: ds=722 sev=B
- 449: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=142 sev=red
  - 44: ds=138 sev=red
  - 77: ds=40 sev=purple
  - 66: ds=31 sev=purple
  - 22: ds=30 sev=purple
  - 99: ds=25 sev=purple
  - 11: ds=22 sev=-
  - 33: ds=10 sev=-
  - 88: ds=6 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 25: ds=98 sev=red
  - 47: ds=84 sev=red
  - 45: ds=68 sev=red
  - 26: ds=61 sev=red
  - 39: ds=54 sev=blue
  - 59: ds=54 sev=blue
  - 79: ds=45 sev=blue
  - 24: ds=41 sev=blue
  - 05: ds=37 sev=blue
  - 56: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:447, 32:162, 4:116, 22:115, 10:103, 31:91, 5:81, 33:67, 27:64, 1:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=447 fs=5 fl=1 hz=0.01662049861495845, 32:ds=162 fs=6 fl=1 hz=0.009987515605493134, 4:ds=116 fs=23 fl=2 hz=0.03071253071253071, 22:ds=115 fs=34 fl=0 hz=0.04, 10:ds=103 fs=16 fl=2 hz=0.0234375, 31:ds=91 fs=18 fl=3 hz=0.02394526795895097, 5:ds=81 fs=18 fl=2 hz=0.022446689113355782, 33:ds=67 fs=12 fl=1 hz=0.017361111111111112, 27:ds=64 fs=18 fl=1 hz=0.02358490566037736, 1:ds=56 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=74 flags=purple
- S24: ds=65 flags=purple
- S18: ds=50 flags=red+purple
- S23: ds=45 flags=blue+purple
- S16: ds=40 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS
  - 129: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS
  - 237: score=2 tags=RS
  - 246: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:681(B); evening:736(B)
- 447 -> combined:980(B); midday:738(B)
- 555 -> evening:854(B); midday:849(B)
- 888 -> evening:762(B); midday:814(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:37(blue); evening:37(blue)
- 11 -> combined:44(purple); midday:54(purple)
- 19 -> combined:36(purple); midday:30(purple)
- 22 -> combined:60(purple); evening:30(purple); midday:78(blue)
- 23 -> combined:43(blue); evening:28(purple)
- 24 -> combined:82(red); evening:41(blue); midday:57(red)
- 25 -> combined:57(red); evening:98(red); midday:28(purple)
- 44 -> combined:45(purple); evening:138(red)
- 45 -> combined:79(red); evening:68(red); midday:39(blue)
- 47 -> combined:168(red); evening:84(red); midday:111(red)
- 48 -> combined:46(blue); midday:31(purple)
- 55 -> combined:25(purple); evening:142(red)
- 56 -> combined:39(blue); evening:37(blue)
- 59 -> combined:39(blue); evening:54(blue)
- 77 -> combined:59(purple); evening:40(purple); midday:29(purple)
- 99 -> combined:50(purple); evening:25(purple); midday:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.772)[R1,XVAR-Cons(CEM)], 3(4.674200000000001)[R3,XVAR-Cons(CEM)], 1(3.3017)[R2,XVAR-Cons(CE)], 4(1.0597999999999999)[R2,Double-Pressure]
- P2: 5(7.0919428571428575)[R1,XVAR-Cons(CEM)], 2(2.9619642857142856)[R3,XVAR-Cons(CE)], 1(1.4165714285714284)[R1,Double-Pressure], 4(1.1598)[R2,Double-Pressure], 7(0.5296642857142857)[R3,Mirror-Echo]
- P3: 9(7.866664285714286)[R1,Mirror-Echo], 4(6.254250000000001)[R2,Mirror-Echo], 6(2.9058571428571427)[R3,XVAR-Cons(CE)], 1(1.1075714285714284)[R1,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=56), P2:5(gap=25), P3:9(gap=31); top cartesian candidates: 259, 254, 229, 359, 256.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 1}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 259→combined:681(B),evening:736(B); 447→combined:980(B),midday:738(B); 555→midday:849(B),evening:854(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:187, 27:128, 5:91, 32:85, 26:80.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=451 Evening=913; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 145 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 139 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 451 (canon 145): box `145` covers winner `451` (boxed hit).
  - Evening winner 913 (canon 139): box `139` covers winner `913` (boxed hit).
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
