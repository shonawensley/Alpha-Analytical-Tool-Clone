# Master Validation Run Report — OntarioCanada4 — results 2026-01-01 (history workbook ~ 2025-12-31)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-01/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-01/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-01/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-01/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-01/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-01/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-01/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_528_20260105_053419.html`
- `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_546_20260105_053420.html`

Winners JSON files:
- `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_528_20260105_053419.json`
- `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_546_20260105_053420.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-01/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 528 (canon 258): exact_boxed=True exact_straight=True | rank 802/5291 (rank_frac 0.152); Evening 546 (canon 456): exact_boxed=True exact_straight=True | rank 2667/5291 (rank_frac 0.504)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 528 idx11 (rank 25/35, frac 0.714), 546 idx9 (rank 33/35, frac 0.943)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
- Q7: Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy.
- Q8: Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries).
- Q9: Aux cues: BA score=2 (if None, BA not available); see Part 3 positional/doubles/pairs notes.
- Q10: 4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank).
- Q11: Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table.
- Q12: Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days.
- Q13: Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance.
- Q14: Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — OntarioCanada4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-01)

## Midday winner 528 (canonical 258)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=11 | family_rows=206 | exact_boxed=11 | exact_straight=10 | vt_boxed=11
- Scores (patterns_scores.csv): rank 802/5291 (rank_frac 0.15157815157815158) | score 18.0 (top 40.0, ratio 0.45, delta 22.0) | section Combined, Set Set3, Draw Draw1, Col 3, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat6|hot1|vtrac_straight|set_chain3
- Compound (patterns_compound.csv): rank 132/1877 (rank_frac 0.07032498668087374) | score 29.5 (top 98.0, ratio 0.3010204081632653, delta 68.5) | section Combined, col1_hits 0, hot2 0, set_chain 3, draw_chain 1 | why set_chain3|draw_chain1|hot1x5|vstrx2
- Families (patterns_families.csv): count 39 | rank 424/1321 (rank_frac 0.3209689629068887) | score 19.5 (top 30.5, ratio 0.639344262295082, delta 11.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=85

## Evening winner 546 (canonical 456)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=4 | family_rows=198 | exact_boxed=4 | exact_straight=4 | vt_boxed=4
- Scores (patterns_scores.csv): rank 2667/5291 (rank_frac 0.5040635040635041) | score 12.5 (top 40.0, ratio 0.3125, delta 27.5) | section Evening, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|hidden3v|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 404/1877 (rank_frac 0.21523708044752266) | score 18.0 (top 98.0, ratio 0.1836734693877551, delta 80.0) | section Evening, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|vstrx3
- Families (patterns_families.csv): count 30 | rank 464/1321 (rank_frac 0.35124905374716126) | score 19.0 (top 30.5, ratio 0.6229508196721312, delta 11.5) | section Midday, hot2 10
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=85

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 118 | section Evening | score 85.5 | col1_hits 8 | hot2 11
- rank   11 | canon 148 | section Evening | score 66.0 | col1_hits 7 | hot2 11
- rank   18 | canon 1488 | section Evening | score 56.0 | col1_hits 6 | hot2 11
- rank    8 | canon 11488 | section Evening | score 67.5 | col1_hits 6 | hot2 11
- rank    3 | canon 488 | section Evening | score 81.0 | col1_hits 7 | hot2 11
- rank    5 | canon 188 | section Evening | score 76.5 | col1_hits 7 | hot2 11
- rank    7 | canon 1148 | section Evening | score 69.5 | col1_hits 7 | hot2 11
- rank    1 | canon 114 | section Evening | score 98.0 | col1_hits 8 | hot2 11
- rank   10 | canon 1188 | section Evening | score 66.5 | col1_hits 7 | hot2 11
- rank   30 | canon 556 | section Combined | score 50.5 | col1_hits 4 | hot2 8

## Top families (patterns_families.csv)
- rank 1311 | family 1 | score 4.0 | hot2 0 | section Midday
- rank  651 | family 8 | score 16.0 | hot2 2 | section Midday
- rank   47 | family 10 | score 26.5 | hot2 0 | section Midday
- rank  107 | family 23 | score 24.5 | hot2 0 | section Midday
- rank  153 | family 3 | score 23.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 528 (canon 258): exact_boxed=True exact_straight=True | rank 802/5291 (rank_frac 0.152); Evening 546 (canon 456): exact_boxed=True exact_straight=True | rank 2667/5291 (rank_frac 0.504)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260105)

## Midday winner 528 (canonical 258)
- Stamp (winner_stamp.json): items_total=71 | exact_any=0 exact_final=0 | vtrac_any=43 vtrac_final=0 | drop_exact_any=21 drop_exact_final=0 | drop_vtrac_any=47 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=5 family_vtrac_final=0
- Flags (winner_flags.csv): rows=71 | exact_any=0 vtrac_any=43 | drop_exact_any=21 drop_vtrac_any=47 | family_exact_any=0 family_vtrac_any=5 | vt_boxed=47 vt_straight=0
- Hits (winner_hits.csv): rows=71 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=47 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.627143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 546 (canonical 456)
- Stamp (winner_stamp.json): items_total=177 | exact_any=0 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=7 drop_exact_final=0 | drop_vtrac_any=137 drop_vtrac_final=0 | family_exact_any=4 family_exact_final=0 | family_vtrac_any=51 family_vtrac_final=0
- Flags (winner_flags.csv): rows=177 | exact_any=0 vtrac_any=120 | drop_exact_any=7 drop_vtrac_any=137 | family_exact_any=4 family_vtrac_any=51 | vt_boxed=113 vt_straight=0
- Hits (winner_hits.csv): rows=177 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=113 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.827143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 528 (canonical 258)
- Stamp (winner_stamp.json): items_total=74 | exact_any=0 exact_final=0 | vtrac_any=43 vtrac_final=0 | drop_exact_any=21 drop_exact_final=0 | drop_vtrac_any=50 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=5 family_vtrac_final=0
- Flags (winner_flags.csv): rows=74 | exact_any=0 vtrac_any=43 | drop_exact_any=21 drop_vtrac_any=50 | family_exact_any=0 family_vtrac_any=5 | vt_boxed=50 vt_straight=0
- Hits (winner_hits.csv): rows=74 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=50 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 552 | score_v2 15.627143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 15.627143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 552 | score_v2 15.327143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 552 | score_v2 15.327143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 552 | score_v2 15.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 552 | score_v2 15.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 5 | pattern 552 | score_v2 15.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 552 | score_v2 15.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 552 | score_v2 14.827143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 14.277143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 552 | score_v2 15.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 522 | score_v2 14.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 551 | score_v2 12.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 554 | score_v2 12.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 552 | score_v2 11.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 551 | score_v2 11.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 441 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 411 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 220 | score_v2 10.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 552 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 528 (canon 258): items_total=71 exact_any=0 vtrac_any=43 | top winner_present=False best_rank=None/20; Evening 546 (canon 456): items_total=177 exact_any=0 vtrac_any=120 | top winner_present=False best_rank=None/18; Combined 528 (canon 258): items_total=74 exact_any=0 vtrac_any=43 | top winner_present=False best_rank=None/14
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 522, 551, 554, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_053645)

## Top indices (from enhanced JSON)
- index 23 | score 60.34520749999999 | features: presence=43.867707499999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 51.12424999999999 | features: presence=35.126749999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 33.18675 | features: presence=23.269250000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 30.382027499999996 | features: presence=22.2845275, set_echo=0.3, first_hit=0.4, column_span=0.3375
- index 31 | score 29.277205000000002 | features: presence=21.009705, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 26.554320000000004 | features: presence=16.52682, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 25 | score 26.513075 | features: presence=15.725574999999997, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 25.207085000000006 | features: presence=16.929585000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 23.491875000000004 | features: presence=14.664375000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 21 | score 22.600182500000006 | features: presence=14.082682500000004, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
183, 813, 924, 817, 841, 718, 824, 194, 418, 218

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 528 | index 11 | file OntarioCanada4_vtrac11_winner_528_20260105_053419.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 546 | index 9 | file OntarioCanada4_vtrac9_winner_546_20260105_053420.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 528 | index 11 rank 25/35 (rank_frac 0.7142857142857143) | score 7.649209999999998 (top 60.34520749999999, ratio 0.12675753911360732, delta 52.69599749999999) | winner_in_index_straights=False | top_index_straights: 825 (3.232), 258 (3.151), 753 (1.469)
- winner 546 | index 9 rank 33/35 (rank_frac 0.9428571428571428) | score 1.1737499999999998 (top 60.34520749999999, ratio 0.019450591830345434, delta 59.17145749999999) | winner_in_index_straights=False | top_index_straights: 159 (0.3)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 528→idx11 rank 25/35 (frac 0.714); 546→idx9 rank 33/35 (frac 0.943).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 19, 18, 4, 31.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-01)

## Midday winner 528 (canonical 258)
- Top lanes (hot_zones_top_lanes.csv): present | rank 106/210 (rank_frac 0.5047619047619047) | score_mean 16.69 (top 20.992, ratio 0.7950647865853658, delta 4.302)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 546 (canonical 456)
- Top lanes (hot_zones_top_lanes.csv): present | rank 58/210 (rank_frac 0.2761904761904762) | score_mean 17.765 (top 20.992, ratio 0.8462747713414634, delta 3.2270000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 20.992 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 189 | vt_triad 245 | score_mean 20.605 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    3 | triad 237 | vt_triad 334 | score_mean 20.245 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 188 | vt_triad 24 | score_mean 20.244 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 244 | vt_triad 35 | score_mean 20.18 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    6 | triad 114 | vt_triad 25 | score_mean 20.099 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 227 | vt_triad 33 | score_mean 20.075 | tags col1,hot16,ls2_lane,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 277 | vt_triad 33 | score_mean 20.075 | tags col1,hot16,ls2_lane,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 144 | vt_triad 25 | score_mean 19.938 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 448 | vt_triad 45 | score_mean 19.743 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 528 (canon 258): rank 106/210 (rank_frac 0.505) ratio_to_top=0.7950647865853658; Evening 546 (canon 456): rank 58/210 (rank_frac 0.276) ratio_to_top=0.8462747713414634
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

Aux draws snapshot dir: `sharepacks/2026-01-01/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=932, 918, 372, 409, 043
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=918, 409, 006, 313, 909
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=932, 372, 043, 297, 606

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=48 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=22), P2:8 (gap=20), P3:4 (gap=21)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=999 sev=B
- 128: ds=919 sev=B
- 555: ds=884 sev=B
- 039: ds=775 sev=B
- 333: ds=746 sev=B
- 188: ds=719 sev=B
- 266: ds=705 sev=B
- 477: ds=703 sev=B
- 126: ds=695 sev=B
- 669: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=121 sev=red
  - 55: ds=77 sev=blue
  - 11: ds=36 sev=purple
  - 88: ds=30 sev=purple
  - 44: ds=21 sev=-
  - 77: ds=12 sev=-
  - 99: ds=9 sev=-
  - 66: ds=8 sev=-
  - 33: ds=7 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 01: ds=56 sev=red
  - 68: ds=54 sev=blue
  - 15: ds=53 sev=blue
  - 17: ds=47 sev=blue
  - 12: ds=33 sev=purple
  - 69: ds=32 sev=purple
  - 24: ds=31 sev=purple
  - 26: ds=31 sev=purple
  - 67: ds=28 sev=purple
  - 36: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:331, 16:285, 17:157, 20:135, 33:81, 12:80, 26:75, 34:62, 8:58, 9:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=331 fs=1 fl=0 hz=0.005698005698005698, 16:ds=285 fs=2 fl=0 hz=0.006329113924050633, 17:ds=157 fs=19 fl=1 hz=0.024242424242424242, 20:ds=135 fs=14 fl=2 hz=0.01853997682502897, 33:ds=81 fs=24 fl=1 hz=0.027472527472527472, 12:ds=80 fs=45 fl=0 hz=0.04928806133625411, 26:ds=75 fs=2 fl=1 hz=0.006075334143377886, 34:ds=62 fs=14 fl=2 hz=0.019698725376593278, 8:ds=58 fs=39 fl=2 hz=0.044956140350877194, 9:ds=53 fs=44 fl=0 hz=0.04751619870410367

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=99 flags=red+purple
- S23: ds=76 flags=blue+purple
- S21: ds=73 flags=purple
- S4: ds=67 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 046: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 037: score=2 tags=RS
  - 127: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=16 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:7 (gap=22), P3:0 (gap=14)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=994 sev=B
- 333: ds=977 sev=B
- 255: ds=944 sev=B
- 355: ds=909 sev=B
- 466: ds=830 sev=B
- 446: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=60 sev=purple
  - 55: ds=38 sev=purple
  - 11: ds=28 sev=purple
  - 77: ds=21 sev=-
  - 88: ds=17 sev=-
  - 66: ds=12 sev=-
  - 44: ds=10 sev=-
  - 99: ds=4 sev=-
  - 33: ds=3 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 34: ds=69 sev=red
  - 07: ds=66 sev=red
  - 16: ds=52 sev=blue
  - 39: ds=40 sev=blue
  - 68: ds=36 sev=purple
  - 37: ds=35 sev=purple
  - 67: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 48: ds=32 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:165, 34:160, 16:142, 27:97, 12:94, 14:79, 17:78, 20:67, 19:52, 33:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=165 fs=4 fl=3 hz=0.010432190760059612, 34:ds=160 fs=8 fl=4 hz=0.014423076923076924, 16:ds=142 fs=3 fl=0 hz=0.007462686567164179, 27:ds=97 fs=15 fl=2 hz=0.0189520624303233, 12:ds=94 fs=45 fl=0 hz=0.05079006772009029, 14:ds=79 fs=39 fl=0 hz=0.04276315789473684, 17:ds=78 fs=29 fl=2 hz=0.033879781420765025, 20:ds=67 fs=24 fl=3 hz=0.029315960912052113, 19:ds=52 fs=20 fl=2 hz=0.023732470334412083, 33:ds=40 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=76 flags=purple
- S25: ds=72 flags=purple
- S1: ds=61 flags=blue+purple
- S5: ds=59 flags=purple
- S8: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=53 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=15), P2:1 (gap=51), P3:9 (gap=38)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=51)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=901 sev=B
- 113: ds=852 sev=B
- 378: ds=845 sev=B
- 566: ds=834 sev=B
- 199: ds=826 sev=B
- 899: ds=804 sev=B
- 126: ds=800 sev=B
- 559: ds=795 sev=B
- 477: ds=784 sev=B
- 558: ds=750 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=230 sev=red
  - 22: ds=61 sev=purple
  - 00: ds=48 sev=purple
  - 44: ds=31 sev=purple
  - 11: ds=18 sev=-
  - 99: ds=16 sev=-
  - 88: ds=15 sev=-
  - 33: ds=13 sev=-
  - 77: ds=6 sev=-
  - 66: ds=4 sev=-
- non_repeating:
  - 36: ds=73 sev=red
  - 24: ds=57 sev=red
  - 18: ds=51 sev=blue
  - 89: ds=51 sev=blue
  - 15: ds=50 sev=blue
  - 78: ds=49 sev=blue
  - 49: ds=43 sev=blue
  - 57: ds=40 sev=blue
  - 09: ds=30 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:426, 1:341, 16:192, 26:124, 18:109, 17:102, 20:93, 3:72, 23:65, 33:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=426 fs=0 fl=2 hz=0.005366726296958855, 1:ds=341 fs=0 fl=0 hz=0.0, 16:ds=192 fs=3 fl=1 hz=0.007853403141361256, 26:ds=124 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=109 fs=16 fl=1 hz=0.019384264538198404, 17:ds=102 fs=13 fl=3 hz=0.018626309662398137, 20:ds=93 fs=15 fl=2 hz=0.01925254813137033, 3:ds=72 fs=15 fl=4 hz=0.02092511013215859, 23:ds=65 fs=25 fl=2 hz=0.03085714285714286, 33:ds=63 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=82 flags=purple
- S2: ds=72 flags=blue+purple
- S4: ds=70 flags=purple
- S25: ds=59 flags=purple
- S20: ds=52 flags=purple
- S9: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
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
  - 028: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:695(B); evening:800(B)
- 128 -> combined:919(B); evening:901(B)
- 333 -> combined:746(B); midday:977(B)
- 477 -> combined:703(B); evening:784(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:56(red); evening:28(purple); midday:28(purple)
- 11 -> combined:36(purple); midday:28(purple)
- 12 -> combined:33(purple); evening:28(purple)
- 15 -> combined:53(blue); evening:50(blue); midday:26(purple)
- 22 -> combined:121(red); evening:61(purple); midday:60(purple)
- 24 -> combined:31(purple); evening:57(red)
- 36 -> combined:25(purple); evening:73(red)
- 55 -> combined:77(blue); evening:230(red); midday:38(purple)
- 67 -> combined:28(purple); midday:35(purple)
- 68 -> combined:54(blue); evening:27(purple); midday:36(purple)
- 69 -> combined:32(purple); midday:27(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(6.731721428571428)[R1,XVAR-Cons(CEM)], 8(3.521857142857143)[R2,XVAR-Cons(CE)], 5(2.9025714285714286)[R3,XVAR-Cons(CM)], 4(0.8508)[R2,Double-Pressure], 2(0.39558571428571426)[R3,Swap]
- P2: 8(6.518228571428572)[R1,XVAR-Cons(CEM)], 6(3.7376)[R2,XVAR-Cons(CE)], 2(2.0846714285714287)[R3,XVAR-Cons(CM)], 1(1.878)[R1,Mirror-Echo], 7(1.3423571428571428)[R1,Mirror-Echo]
- P3: 4(5.957457142857143)[R1,XVAR-Cons(CEM)], 1(2.630057142857143)[R3,XVAR-Cons(CE)], 9(1.7305)[R1,Mirror-Echo], 0(1.018)[R1,Double-Pressure], 2(0.9717)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_31.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=22), P2:8(gap=20), P3:4(gap=21); top cartesian candidates: 184, 181, 164, 884, 124.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6'], 'pairs': {'remaining_count': 0}}; top candidates: 046, 136, 145, 235, 469.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:695(B),evening:800(B); 128→combined:919(B),evening:901(B); 333→combined:746(B),midday:977(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:331, 16:285, 17:157, 20:135, 33:81.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=528 Evening=546; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 258 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 456 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 528 (canon 258): box `258` covers winner `528` (boxed hit).
  - Evening winner 546 (canon 456): box `456` covers winner `546` (boxed hit).
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
