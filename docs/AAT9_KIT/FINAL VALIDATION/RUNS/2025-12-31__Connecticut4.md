# Master Validation Run Report — Connecticut4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/Connecticut4/`
- Winners lens: `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2025-12-31/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2025-12-31/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2025-12-31/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2025-12-31/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2025-12-31/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2025-12-31/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_361_20260105_052142.html`
- `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_932_20260105_052140.html`

Winners JSON files:
- `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_361_20260105_052142.json`
- `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_932_20260105_052140.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 932 (canon 239): exact_boxed=True exact_straight=True | rank 347/4814 (rank_frac 0.072); Evening 361 (canon 136): exact_boxed=True exact_straight=True | rank 4434/4814 (rank_frac 0.921)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 361 idx18 (rank 4/35, frac 0.114), 932 idx30 (rank 16/35, frac 0.457)
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

### 2.Stable — Connecticut4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2025-12-31)

## Midday winner 932 (canonical 239)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=14 | family_rows=182 | exact_boxed=14 | exact_straight=14 | vt_boxed=14
- Scores (patterns_scores.csv): rank 347/4814 (rank_frac 0.07208142916493561) | score 18.5 (top 46.0, ratio 0.40217391304347827, delta 27.5) | section Midday, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why straight|cov2|hp_repeat3|vstr2|hot1|hidden3v|set_chain2|draw_chain4
- Compound (patterns_compound.csv): rank 148/1761 (rank_frac 0.08404315729699034) | score 25.5 (top 98.5, ratio 0.25888324873096447, delta 73.0) | section Midday, col1_hits 0, hot2 0, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|hot1x3
- Families (patterns_families.csv): count 46 | rank 24/1253 (rank_frac 0.019154030327214685) | score 25.5 (top 34.5, ratio 0.7391304347826086, delta 9.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=97

## Evening winner 361 (canonical 136)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=348 | exact_boxed=2 | exact_straight=2 | vt_boxed=2
- Scores (patterns_scores.csv): rank 4434/4814 (rank_frac 0.9210635646032406) | score 8.5 (top 46.0, ratio 0.18478260869565216, delta 37.5) | section Midday, Set Set1, Draw Draw1, Col 6, hot 0, vt_straight 0.0 | why straight|cov1|mirror|hidden3v|draw_chain2
- Compound (patterns_compound.csv): rank 1432/1761 (rank_frac 0.8131743327654741) | score 9.5 (top 98.5, ratio 0.09644670050761421, delta 89.0) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2
- Families (patterns_families.csv): count 59 | rank 47/1253 (rank_frac 0.03750997605746209) | score 24.0 (top 34.5, ratio 0.6956521739130435, delta 10.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=22

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 116 | section Evening | score 59.5 | col1_hits 1 | hot2 6
- rank    6 | canon 114 | section Evening | score 53.5 | col1_hits 2 | hot2 6
- rank   31 | canon 1146 | section Evening | score 39.0 | col1_hits 0 | hot2 5
- rank  107 | canon 146 | section Evening | score 28.0 | col1_hits 0 | hot2 4
- rank    4 | canon 388 | section Combined | score 54.0 | col1_hits 4 | hot2 4
- rank   48 | canon 346 | section Midday | score 36.0 | col1_hits 3 | hot2 4
- rank    9 | canon 039 | section Midday | score 47.0 | col1_hits 1 | hot2 4
- rank   18 | canon 336 | section Combined | score 44.0 | col1_hits 4 | hot2 4
- rank   17 | canon 3388 | section Combined | score 44.5 | col1_hits 4 | hot2 4
- rank    9 | canon 688 | section Combined | score 47.0 | col1_hits 4 | hot2 4

## Top families (patterns_families.csv)
- rank 1173 | family 29 | score 6.5 | hot2 0 | section Midday
- rank  883 | family 1 | score 11.0 | hot2 0 | section Midday
- rank  287 | family 12 | score 19.0 | hot2 0 | section Midday
- rank  323 | family 23 | score 18.5 | hot2 0 | section Midday
- rank  393 | family 18 | score 17.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 932 (canon 239): exact_boxed=True exact_straight=True | rank 347/4814 (rank_frac 0.072); Evening 361 (canon 136): exact_boxed=True exact_straight=True | rank 4434/4814 (rank_frac 0.921)
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

### 2.Digit Reduction — Connecticut4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260105)

## Midday winner 932 (canonical 239)
- Stamp (winner_stamp.json): items_total=50 | exact_any=0 exact_final=0 | vtrac_any=30 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=44 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=21 family_vtrac_final=0
- Flags (winner_flags.csv): rows=50 | exact_any=0 vtrac_any=30 | drop_exact_any=2 drop_vtrac_any=44 | family_exact_any=0 family_vtrac_any=21 | vt_boxed=50 vt_straight=0
- Hits (winner_hits.csv): rows=50 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=50 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.696234 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 361 (canonical 136)
- Stamp (winner_stamp.json): items_total=240 | exact_any=0 exact_final=0 | vtrac_any=240 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=81 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=70 family_vtrac_final=0
- Flags (winner_flags.csv): rows=240 | exact_any=0 vtrac_any=240 | drop_exact_any=0 drop_vtrac_any=81 | family_exact_any=0 family_vtrac_any=70 | vt_boxed=90 vt_straight=0
- Hits (winner_hits.csv): rows=240 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=90 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.987143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 932 (canonical 239)
- Stamp (winner_stamp.json): items_total=69 | exact_any=11 exact_final=0 | vtrac_any=49 vtrac_final=0 | drop_exact_any=20 drop_exact_final=0 | drop_vtrac_any=63 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=34 family_vtrac_final=0
- Flags (winner_flags.csv): rows=69 | exact_any=11 vtrac_any=49 | drop_exact_any=20 drop_vtrac_any=63 | family_exact_any=0 family_vtrac_any=34 | vt_boxed=63 vt_straight=0
- Hits (winner_hits.csv): rows=69 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=63 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 599 | score_v2 9.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 599 | score_v2 9.858571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 9.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 9.615714 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 598 | score_v2 9.597143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 9.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 599 | score_v2 9.470476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 559 | score_v2 9.387143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 9.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 5 | pattern 559 | score_v2 9.337143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 598 | score_v2 9.597143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 599 | score_v2 9.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 924 | score_v2 8.987143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 011 | score_v2 8.94381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 411 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 411 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 598 | score_v2 8.797143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 932 (canon 239): items_total=50 exact_any=0 vtrac_any=30 | top winner_present=False best_rank=None/26; Evening 361 (canon 136): items_total=240 exact_any=0 vtrac_any=240 | top winner_present=False best_rank=None/30; Combined 932 (canon 239): items_total=69 exact_any=11 vtrac_any=49 | top winner_present=False best_rank=None/32
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 599, 559, 598, 599, 924.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_053042)

## Top indices (from enhanced JSON)
- index 24 | score 40.6267525 | features: presence=24.789252500000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 21 | score 34.7599 | features: presence=22.0124, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 17 | score 28.594450000000002 | features: presence=15.80695, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 18 | score 19.372400000000003 | features: presence=12.4149, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 18.059025000000005 | features: presence=12.211525000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 16 | score 16.817125000000004 | features: presence=10.891500000000002, set_echo=0.3, first_hit=0.33333333333333337, column_span=0.23229166666666665
- index 29 | score 14.15675 | features: presence=5.4292500000000015, set_echo=0.6, first_hit=0.2, column_span=0.0875
- index 9 | score 13.870505 | features: presence=5.943005000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 10.86465 | features: presence=5.10715, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 14 | score 10.537574999999999 | features: presence=4.520074999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
986, 968, 687, 867, 918, 936, 913, 193, 371, 198

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 361 | index 18 | file Connecticut4_vtrac18_winner_361_20260105_052142.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 932 | index 30 | file Connecticut4_vtrac30_winner_932_20260105_052140.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 361 | index 18 rank 4/35 (rank_frac 0.11428571428571428) | score 19.372400000000003 (top 40.6267525, ratio 0.47683850684348944, delta 21.2543525) | winner_in_index_straights=False | top_index_straights: 681 (5.875), 186 (5.208), 136 (4.312)
- winner 932 | index 30 rank 16/35 (rank_frac 0.45714285714285713) | score 6.0625 (top 40.6267525, ratio 0.149224331922666, delta 34.5642525) | winner_in_index_straights=False | top_index_straights: 798 (2.542), 879 (1.847), 793 (0.86)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 361→idx18 rank 4/35 (frac 0.114); 932→idx30 rank 16/35 (frac 0.457).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 24, 21, 17, 18, 23.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2025-12-31)

## Midday winner 932 (canonical 239)
- Top lanes (hot_zones_top_lanes.csv): present | rank 97/211 (rank_frac 0.4597156398104265) | score_mean 17.533 (top 24.55, ratio 0.7141751527494908, delta 7.0169999999999995)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 361 (canonical 136)
- Top lanes (hot_zones_top_lanes.csv): present | rank 43/211 (rank_frac 0.2037914691943128) | score_mean 18.437 (top 24.55, ratio 0.7509979633401223, delta 6.1129999999999995)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 24.55 | tags hot16,literal_draw,straight_lane,vertical3,vt_straight
- rank    2 | triad 279 | vt_triad 335 | score_mean 23.871 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 23.562 | tags funnel_precol1,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 177 | vt_triad 23 | score_mean 22.023 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    6 | triad 467 | vt_triad 235 | score_mean 21.238 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    7 | triad 011 | vt_triad 12 | score_mean 20.9 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 055 | vt_triad 11 | score_mean 20.543 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 007 | vt_triad 13 | score_mean 20.489 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 059 | vt_triad 115 | score_mean 20.286 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 932 (canon 239): rank 97/211 (rank_frac 0.460) ratio_to_top=0.7141751527494908; Evening 361 (canon 136): rank 43/211 (rank_frac 0.204) ratio_to_top=0.7509979633401223
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

Aux draws snapshot dir: `sharepacks/2025-12-31/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=467, 095, 055, 211, 279
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=095, 211, 042, 261, 177
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=467, 055, 279, 083, 435

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=29 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=32), P2:0 (gap=38), P3:0 (gap=29)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 355: ds=999 sev=B
- 777: ds=881 sev=B
- 129: ds=863 sev=B
- 288: ds=851 sev=B
- 136: ds=838 sev=B
- 149: ds=833 sev=B
- 445: ds=765 sev=B
- 114: ds=735 sev=B
- 069: ds=699 sev=B
- 888: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=83 sev=blue
  - 22: ds=71 sev=blue
  - 99: ds=64 sev=purple
  - 00: ds=34 sev=purple
  - 33: ds=21 sev=-
  - 88: ds=20 sev=-
  - 66: ds=19 sev=-
  - 77: ds=9 sev=-
  - 11: ds=3 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 23: ds=84 sev=red
  - 69: ds=81 sev=red
  - 48: ds=70 sev=red
  - 78: ds=66 sev=red
  - 57: ds=65 sev=red
  - 49: ds=64 sev=red
  - 19: ds=58 sev=red
  - 13: ds=50 sev=blue
  - 01: ds=39 sev=blue
  - 25: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:399, 32:166, 25:152, 29:125, 4:123, 15:111, 31:100, 34:95, 3:80, 27:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=399 fs=1 fl=2 hz=0.01098901098901099, 32:ds=166 fs=5 fl=3 hz=0.010830324909747294, 25:ds=152 fs=22 fl=2 hz=0.029055690072639227, 29:ds=125 fs=25 fl=1 hz=0.029988465974625143, 4:ds=123 fs=22 fl=2 hz=0.0273972602739726, 15:ds=111 fs=11 fl=4 hz=0.016910935738444193, 31:ds=100 fs=32 fl=0 hz=0.03665521191294387, 34:ds=95 fs=15 fl=2 hz=0.01951779563719862, 3:ds=80 fs=27 fl=0 hz=0.030337078651685393, 27:ds=79 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=97 flags=purple
- S3: ds=74 flags=purple
- S24: ds=66 flags=blue+purple
- S22: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=71 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=30), P2:0 (gap=24), P3:8 (gap=29)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=877 sev=B
- 478: ds=858 sev=B
- 459: ds=853 sev=B
- 159: ds=809 sev=B
- 099: ds=790 sev=B
- 127: ds=781 sev=B
- 559: ds=723 sev=B
- 004: ds=682 sev=B
- 155: ds=678 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=89 sev=blue
  - 88: ds=49 sev=purple
  - 44: ds=41 sev=purple
  - 22: ds=35 sev=purple
  - 55: ds=26 sev=purple
  - 00: ds=22 sev=-
  - 33: ds=10 sev=-
  - 66: ds=9 sev=-
  - 77: ds=4 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 23: ds=74 sev=red
  - 78: ds=67 sev=red
  - 13: ds=54 sev=blue
  - 49: ds=41 sev=blue
  - 19: ds=40 sev=blue
  - 69: ds=40 sev=blue
  - 48: ds=37 sev=blue
  - 57: ds=32 sev=purple
  - 79: ds=32 sev=purple
  - 37: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:199, 25:100, 31:89, 32:87, 18:84, 30:74, 3:72, 29:62, 4:61, 15:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=199 fs=3 fl=0 hz=0.008565310492505354, 25:ds=100 fs=21 fl=1 hz=0.025974025974025976, 31:ds=89 fs=20 fl=2 hz=0.024608501118568233, 32:ds=87 fs=3 fl=4 hz=0.009510869565217392, 18:ds=84 fs=23 fl=1 hz=0.026519337016574582, 30:ds=74 fs=35 fl=0 hz=0.03914988814317673, 3:ds=72 fs=22 fl=2 hz=0.02631578947368421, 29:ds=62 fs=18 fl=2 hz=0.023446658851113716, 4:ds=61 fs=26 fl=0 hz=0.02931228861330327, 15:ds=55 fs=24 fl=1 hz=0.02662406815761448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=83 flags=blue+purple
- S24: ds=80 flags=blue+purple
- S8: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 138: score=4 tags=FLT,MIR,RS
  - 237: score=4 tags=FLT,MIR,RS
  - 489: score=4 tags=FLT,MIR,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=MIR,RS
  - 156: score=3 tags=MIR,RS
  - 345: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=8 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=16), P2:0 (gap=19), P3:1 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=904 sev=B
- 668: ds=901 sev=B
- 399: ds=900 sev=B
- 044: ds=896 sev=B
- 133: ds=893 sev=B
- 145: ds=865 sev=B
- 677: ds=772 sev=B
- 333: ds=767 sev=B
- 112: ds=719 sev=B
- 344: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=111 sev=red
  - 22: ds=68 sev=purple
  - 99: ds=32 sev=purple
  - 77: ds=26 sev=purple
  - 66: ds=21 sev=-
  - 11: ds=20 sev=-
  - 33: ds=18 sev=-
  - 00: ds=17 sev=-
  - 88: ds=10 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 09: ds=63 sev=red
  - 57: ds=47 sev=blue
  - 69: ds=45 sev=blue
  - 23: ds=42 sev=blue
  - 25: ds=40 sev=blue
  - 06: ds=39 sev=blue
  - 07: ds=39 sev=blue
  - 01: ds=37 sev=blue
  - 48: ds=35 sev=purple
  - 78: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:310, 26:138, 4:121, 34:90, 32:83, 25:76, 29:64, 15:63, 2:53, 31:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=310 fs=2 fl=1 hz=0.005961251862891207, 26:ds=138 fs=3 fl=1 hz=0.008680555555555556, 4:ds=121 fs=18 fl=1 hz=0.02243211334120425, 34:ds=90 fs=14 fl=3 hz=0.019144144144144143, 32:ds=83 fs=2 fl=0 hz=0.008450704225352114, 25:ds=76 fs=21 fl=0 hz=0.023836549375709424, 29:ds=64 fs=27 fl=0 hz=0.030100334448160536, 15:ds=63 fs=15 fl=1 hz=0.019698725376593278, 2:ds=53 fs=23 fl=2 hz=0.028344671201814057, 31:ds=50 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=90 flags=blue+purple
- S8: ds=67 flags=red+purple
- S20: ds=50 flags=purple
- S3: ds=37 flags=blue+purple
- S24: ds=33 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:689(B); evening:893(B)
- 355 -> combined:999(B); evening:685(B)
- 445 -> combined:765(B); evening:688(B)
- 459 -> combined:674(B); midday:853(B)
- 888 -> combined:697(B); evening:696(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:39(blue); evening:37(blue)
- 06 -> combined:31(purple); evening:39(blue)
- 07 -> combined:31(purple); evening:39(blue)
- 13 -> combined:50(blue); evening:25(purple); midday:54(blue)
- 19 -> combined:58(red); evening:29(purple); midday:40(blue)
- 22 -> combined:71(blue); evening:68(purple); midday:35(purple)
- 23 -> combined:84(red); evening:42(blue); midday:74(red)
- 25 -> combined:33(purple); evening:40(blue)
- 44 -> combined:83(blue); evening:111(red); midday:41(purple)
- 48 -> combined:70(red); evening:35(purple); midday:37(blue)
- 49 -> combined:64(red); evening:32(purple); midday:41(blue)
- 57 -> combined:65(red); evening:47(blue); midday:32(purple)
- 69 -> combined:81(red); evening:45(blue); midday:40(blue)
- 78 -> combined:66(red); evening:33(purple); midday:67(red)
- 99 -> combined:64(purple); evening:32(purple); midday:89(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.895028571428571)[R1,XVAR-Cons(CEM)], 9(7.704314285714286)[R2,XVAR-Cons(CEM)], 3(1.9716642857142859)[R3,XVAR-Cons(CE)], 5(0.2849714285714286)[R3,Swap]
- P2: 0(8.383857142857142)[R1,XVAR-Cons(CEM)], 2(3.1498999999999997)[R2,XVAR-Cons(CM)], 3(1.7475)[R3,XVAR-Cons(CM)], 9(0.9717)[R2,Double-Pressure], 1(0.16122857142857144)[R3]
- P3: 0(6.8548285714285715)[R1,XVAR-Cons(CEM)], 8(3.945857142857143)[R2,XVAR-Cons(CM)], 4(2.8797714285714284)[R3,XVAR-Cons(CM)], 1(0.5971428571428571)[R1], 2(0.24779285714285712)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=32), P2:0(gap=38), P3:0(gap=29); top cartesian candidates: 700, 900, 708, 908, 704.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 013, 018, 023, 028, 034.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:689(B),evening:893(B); 355→combined:999(B),evening:685(B); 445→combined:765(B),evening:688(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:399, 32:166, 25:152, 29:125, 4:123.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=932 Evening=361; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 239 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 136 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 932 (canon 239): box `239` covers winner `932` (boxed hit).
  - Evening winner 361 (canon 136): box `136` covers winner `361` (boxed hit).
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
