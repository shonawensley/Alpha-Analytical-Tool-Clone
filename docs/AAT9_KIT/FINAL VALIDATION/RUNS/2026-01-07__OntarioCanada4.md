# Master Validation Run Report — OntarioCanada4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-07/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-07/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-07/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-07/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-07/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-07/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac12_winner_547_20260110_033434.html`
- `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_698_20260110_033436.html`

Winners JSON files:
- `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac12_winner_547_20260110_033434.json`
- `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_698_20260110_033436.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 547 (canon 457): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 698 (canon 689): exact_boxed=True exact_straight=True | rank 2437/4904 (rank_frac 0.497)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 547 idx12 (rank 23/35, frac 0.657), 698 idx24 (rank 19/35, frac 0.543)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
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

### 2.Stable — OntarioCanada4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-07)

## Midday winner 547 (canonical 457)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=373 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 65 | rank 156/1379 (rank_frac 0.11312545322697606) | score 22.5 (top 34.5, ratio 0.6521739130434783, delta 12.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=132
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 698 (canonical 689)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=5 | family_rows=346 | exact_boxed=5 | exact_straight=5 | vt_boxed=5
- Scores (patterns_scores.csv): rank 2437/4904 (rank_frac 0.4969412724306688) | score 12.5 (top 38.0, ratio 0.32894736842105265, delta 25.5) | section Combined, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hot2|hidden3v|vtrac_straight
- Compound (patterns_compound.csv): rank 458/1767 (rank_frac 0.2591963780418789) | score 18.0 (top 102.0, ratio 0.17647058823529413, delta 84.0) | section Evening, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|vstrx3
- Families (patterns_families.csv): count 64 | rank 239/1379 (rank_frac 0.17331399564902103) | score 20.5 (top 34.5, ratio 0.5942028985507246, delta 14.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=124

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 477 | section Midday | score 102.0 | col1_hits 9 | hot2 11
- rank    3 | canon 015 | section Evening | score 76.5 | col1_hits 8 | hot2 10
- rank   11 | canon 234 | section Midday | score 59.0 | col1_hits 4 | hot2 9
- rank    9 | canon 3677 | section Midday | score 62.0 | col1_hits 5 | hot2 8
- rank   14 | canon 367 | section Midday | score 56.0 | col1_hits 5 | hot2 8
- rank    2 | canon 677 | section Midday | score 87.5 | col1_hits 6 | hot2 8
- rank   17 | canon 236 | section Midday | score 55.0 | col1_hits 5 | hot2 8
- rank   23 | canon 346 | section Midday | score 52.0 | col1_hits 4 | hot2 8
- rank    4 | canon 244 | section Midday | score 75.5 | col1_hits 5 | hot2 6
- rank   59 | canon 026 | section Midday | score 39.0 | col1_hits 3 | hot2 6

## Top families (patterns_families.csv)
- rank 1347 | family 15 | score 5.0 | hot2 0 | section Midday
- rank  467 | family 8 | score 17.0 | hot2 0 | section Midday
- rank  725 | family 34 | score 14.0 | hot2 0 | section Midday
- rank  685 | family 12 | score 14.5 | hot2 0 | section Midday
- rank  635 | family 9 | score 15.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 547 (canon 457): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 698 (canon 689): exact_boxed=True exact_straight=True | rank 2437/4904 (rank_frac 0.497)
- Q2: 4 hit criteria: see metrics_hits per winner (exact_boxed/exact_straight + vt_boxed_count).
- Q3: Winners artifacts alignment: spotlight + metrics.json consistent (see summary block).
- Q4: Dominance/noise: isolates at least one winner; use rank_frac + score_ratio_to_top to gauge strength.
- Q5: Top candidate clusters (compound canonicals): .
- Q6: Miss analysis: if a winner is absent/low, treat as tool outcome (not pipeline failure) unless gaps are listed.
- Q7: Validation (V): gaps list should be empty; if non-empty, flag as Fix-Now.
- Q8: Optimization notes: do not tune on 1 day; accumulate across days then adjust weights (Fix-Later).
- Q9: Cross-tool synergy: compare top compound canonicals vs DR top candidates + Hot Zones top lanes + Aux positional shortlist.
- Q10: Takeaway: Stable isolates at least one winner.

---

### 2.Digit Reduction — OntarioCanada4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260110)

## Midday winner 547 (canonical 457)
- Stamp (winner_stamp.json): items_total=136 | exact_any=0 exact_final=0 | vtrac_any=77 vtrac_final=0 | drop_exact_any=20 drop_exact_final=0 | drop_vtrac_any=135 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=57 family_vtrac_final=0
- Flags (winner_flags.csv): rows=136 | exact_any=0 vtrac_any=77 | drop_exact_any=20 drop_vtrac_any=135 | family_exact_any=0 family_vtrac_any=57 | vt_boxed=21 vt_straight=0
- Hits (winner_hits.csv): rows=136 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=21 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.527143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 698 (canonical 689)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=12 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=12 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.527143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 547 (canonical 457)
- Stamp (winner_stamp.json): items_total=377 | exact_any=0 exact_final=0 | vtrac_any=292 vtrac_final=0 | drop_exact_any=22 drop_exact_final=0 | drop_vtrac_any=348 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=151 family_vtrac_final=0
- Flags (winner_flags.csv): rows=377 | exact_any=0 vtrac_any=292 | drop_exact_any=22 drop_vtrac_any=348 | family_exact_any=0 family_vtrac_any=151 | vt_boxed=100 vt_straight=0
- Hits (winner_hits.csv): rows=377 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=100 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.087143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 13.527143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 13.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 244 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 224 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 244 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 244 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 224 | score_v2 13.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 244 | score_v2 12.977143 | match_types 
- area_rank 2 | variant Midday | section Midday | set Set1 draw Draw4 col 3 | pattern 244 | score_v2 12.827143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 559 | score_v2 13.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 224 | score_v2 13.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 244 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 11.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 247 | score_v2 11.38131 | tags exact,vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 11.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 922 | score_v2 11.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 924 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 922 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 592 | score_v2 10.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 547 (canon 457): items_total=136 exact_any=0 vtrac_any=77 | top winner_present=False best_rank=None/20; Evening 698 (canon 689): items_total=12 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/22; Combined 547 (canon 457): items_total=377 exact_any=0 vtrac_any=292 | top winner_present=False best_rank=None/26
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 224, 244, 559, 247.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260110_033918)

## Top indices (from enhanced JSON)
- index 28 | score 60.51592499999998 | features: presence=40.348424999999985, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 59.99512999999998 | features: presence=40.307629999999975, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 37.536537499999994 | features: presence=21.959037499999997, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 30 | score 31.059900000000003 | features: presence=22.702400000000004, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 27 | score 26.976875000000007 | features: presence=18.339375000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 24.873224999999998 | features: presence=17.665725, set_echo=0.3, first_hit=0.4, column_span=0.3375
- index 21 | score 23.023375000000005 | features: presence=14.045875000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 26 | score 20.441300000000005 | features: presence=9.243800000000002, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 9 | score 16.85240416666667 | features: presence=10.368237500000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 16.29172 | features: presence=9.80422, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
724, 247, 762, 712, 241, 324, 417, 647, 264, 714

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 547 | index 12 | file OntarioCanada4_vtrac12_winner_547_20260110_033434.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 698 | index 24 | file OntarioCanada4_vtrac24_winner_698_20260110_033436.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 547 | index 12 rank 23/35 (rank_frac 0.6571428571428571) | score 4.50925 (top 60.51592499999998, ratio 0.07451344418845124, delta 56.00667499999998) | winner_in_index_straights=False | top_index_straights: 704 (1.952), 240 (0.83)
- winner 698 | index 24 rank 19/35 (rank_frac 0.5428571428571428) | score 7.456499999999999 (top 60.51592499999998, ratio 0.12321550071324204, delta 53.05942499999998) | winner_in_index_straights=False | top_index_straights: 413 (5.325), 634 (1.484)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 547→idx12 rank 23/35 (frac 0.657); 698→idx24 rank 19/35 (frac 0.543).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 20, 22, 30, 27.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-07)

## Midday winner 547 (canonical 457)
- Top lanes (hot_zones_top_lanes.csv): present | rank 182/213 (rank_frac 0.8544600938967136) | score_mean 15.754 (top 25.581, ratio 0.6158476994644463, delta 9.827)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 698 (canonical 689)
- Top lanes (hot_zones_top_lanes.csv): present | rank 25/213 (rank_frac 0.11737089201877934) | score_mean 19.654 (top 25.581, ratio 0.7683046010711074, delta 5.927)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 111 | vt_triad 2 | score_mean 25.581 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_straight
- rank    2 | triad 555 | vt_triad 1 | score_mean 24.85 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    3 | triad 666 | vt_triad 2 | score_mean 23.5 | tags hot20,set1_bonus,superhot_set1
- rank    4 | triad 238 | vt_triad 344 | score_mean 22.841 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 277 | vt_triad 33 | score_mean 22.755 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 227 | vt_triad 33 | score_mean 22.605 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 267 | vt_triad 233 | score_mean 22.115 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 334 | vt_triad 45 | score_mean 22.112 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 127 | vt_triad 233 | score_mean 21.89 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 035 | vt_triad 114 | score_mean 21.889 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 547 (canon 457): rank 182/213 (rank_frac 0.854) ratio_to_top=0.6158476994644463; Evening 698 (canon 689): rank 25/213 (rank_frac 0.117) ratio_to_top=0.7683046010711074
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

Aux draws snapshot dir: `sharepacks/2026-01-07/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-07/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=433, 111, 797, 555, 382
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-07/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=111, 555, 958, 968, 053
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-07/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=433, 797, 382, 032, 816

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=60 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=20), P2:0 (gap=15), P3:4 (gap=33)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=46.10935178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 224: score=44.709292500000004 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 674: score=43.0871 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 624: score=41.86965714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 279: score=40.3415775 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 270: score=39.39267035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 679: score=37.74555714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=37.39882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=37.27310714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 664: score=36.99952857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=931 sev=B
- 039: ds=787 sev=B
- 333: ds=758 sev=B
- 188: ds=731 sev=B
- 266: ds=717 sev=B
- 477: ds=715 sev=B
- 126: ds=707 sev=B
- 669: ds=702 sev=B
- 007: ds=692 sev=B
- 005: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=133 sev=red
  - 88: ds=42 sev=purple
  - 44: ds=33 sev=purple
  - 99: ds=21 sev=-
  - 66: ds=20 sev=-
  - 00: ds=17 sev=-
  - 55: ds=3 sev=-
  - 77: ds=2 sev=-
  - 11: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 01: ds=68 sev=red
  - 15: ds=65 sev=red
  - 17: ds=59 sev=red
  - 12: ds=45 sev=blue
  - 24: ds=43 sev=blue
  - 26: ds=43 sev=blue
  - 67: ds=40 sev=blue
  - 36: ds=37 sev=blue
  - 48: ds=36 sev=purple
  - 08: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:343, 16:297, 17:169, 20:147, 12:92, 26:87, 34:74, 8:70, 7:54, 21:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=343 fs=1 fl=0 hz=0.005698005698005698, 16:ds=297 fs=2 fl=0 hz=0.006329113924050633, 17:ds=169 fs=19 fl=1 hz=0.024242424242424242, 20:ds=147 fs=13 fl=2 hz=0.01847290640394089, 12:ds=92 fs=44 fl=0 hz=0.04932735426008968, 26:ds=87 fs=2 fl=1 hz=0.006075334143377886, 34:ds=74 fs=14 fl=2 hz=0.019698725376593278, 8:ds=70 fs=39 fl=2 hz=0.044956140350877194, 7:ds=54 fs=43 fl=1 hz=0.04675876726886291, 21:ds=53 fs=37 fl=0 hz=0.03952991452991453

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=85 flags=purple
- S4: ds=79 flags=purple
- S16: ds=58 flags=purple
- S24: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6'], 'pairs': {'remaining_count': 0}}
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
- current_index=14 streak=1 max=2 last_repeat_gap=22 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=28), P2:7 (gap=28), P3:0 (gap=20)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=46.10935178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 224: score=44.709292500000004 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 674: score=43.0871 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 624: score=41.86965714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 279: score=40.3415775 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 270: score=39.39267035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 679: score=37.74555714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=37.39882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=37.27310714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 664: score=36.99952857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=983 sev=B
- 255: ds=950 sev=B
- 355: ds=915 sev=B
- 466: ds=836 sev=B
- 446: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=66 sev=purple
  - 77: ds=27 sev=purple
  - 88: ds=23 sev=-
  - 66: ds=18 sev=-
  - 44: ds=16 sev=-
  - 99: ds=10 sev=-
  - 33: ds=9 sev=-
  - 00: ds=8 sev=-
  - 55: ds=1 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 34: ds=75 sev=red
  - 07: ds=72 sev=red
  - 16: ds=58 sev=red
  - 39: ds=46 sev=blue
  - 37: ds=41 sev=blue
  - 67: ds=41 sev=blue
  - 48: ds=38 sev=blue
  - 01: ds=34 sev=purple
  - 15: ds=32 sev=purple
  - 45: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:171, 34:166, 16:148, 27:103, 12:100, 17:84, 20:73, 19:58, 33:46, 26:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=171 fs=4 fl=3 hz=0.010432190760059612, 34:ds=166 fs=8 fl=4 hz=0.014423076923076924, 16:ds=148 fs=3 fl=0 hz=0.007462686567164179, 27:ds=103 fs=14 fl=2 hz=0.0196078431372549, 12:ds=100 fs=45 fl=0 hz=0.05079006772009029, 17:ds=84 fs=29 fl=2 hz=0.033879781420765025, 20:ds=73 fs=24 fl=3 hz=0.029315960912052113, 19:ds=58 fs=20 fl=2 hz=0.023732470334412083, 33:ds=46 fs=18 fl=2 hz=0.021119324181626188, 26:ds=43 fs=0 fl=3 hz=0.005376344086021506

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=78 flags=purple
- S1: ds=67 flags=blue+purple
- S5: ds=65 flags=purple
- S9: ds=55 flags=purple
- S21: ds=42 flags=red+purple
- S4: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
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
- current_index=33 streak=1 max=3 last_repeat_gap=59 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=17), P2:6 (gap=20), P3:9 (gap=44)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=46.10935178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 224: score=44.709292500000004 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 674: score=43.0871 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 624: score=41.86965714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 279: score=40.3415775 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 270: score=39.39267035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 679: score=37.74555714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=37.39882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=37.27310714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 664: score=36.99952857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=907 sev=B
- 113: ds=858 sev=B
- 378: ds=851 sev=B
- 566: ds=840 sev=B
- 199: ds=832 sev=B
- 899: ds=810 sev=B
- 126: ds=806 sev=B
- 559: ds=801 sev=B
- 477: ds=790 sev=B
- 558: ds=756 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=236 sev=red
  - 22: ds=67 sev=purple
  - 00: ds=54 sev=purple
  - 44: ds=37 sev=purple
  - 11: ds=24 sev=-
  - 99: ds=22 sev=-
  - 88: ds=21 sev=-
  - 66: ds=10 sev=-
  - 77: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 36: ds=79 sev=red
  - 24: ds=63 sev=red
  - 89: ds=57 sev=red
  - 15: ds=56 sev=red
  - 78: ds=55 sev=blue
  - 49: ds=49 sev=blue
  - 57: ds=46 sev=blue
  - 09: ds=36 sev=purple
  - 01: ds=34 sev=purple
  - 12: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:432, 1:347, 16:198, 26:130, 17:108, 20:99, 3:78, 23:71, 31:65, 12:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=432 fs=0 fl=2 hz=0.005366726296958855, 1:ds=347 fs=0 fl=0 hz=0.0, 16:ds=198 fs=3 fl=1 hz=0.007853403141361256, 26:ds=130 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=108 fs=13 fl=3 hz=0.018626309662398137, 20:ds=99 fs=15 fl=2 hz=0.01925254813137033, 3:ds=78 fs=15 fl=4 hz=0.02092511013215859, 23:ds=71 fs=25 fl=2 hz=0.03085714285714286, 31:ds=65 fs=23 fl=0 hz=0.02666666666666667, 12:ds=46 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=88 flags=purple
- S2: ds=78 flags=blue+purple
- S4: ds=76 flags=purple
- S25: ds=65 flags=purple
- S20: ds=58 flags=purple
- S9: ds=56 flags=red+purple

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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:707(B); evening:806(B)
- 128 -> combined:931(B); evening:907(B)
- 226 -> combined:669(B); evening:708(B)
- 333 -> combined:758(B); midday:983(B)
- 477 -> combined:715(B); evening:790(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:68(red); evening:34(purple); midday:34(purple)
- 12 -> combined:45(blue); evening:34(purple)
- 15 -> combined:65(red); evening:56(red); midday:32(purple)
- 17 -> combined:59(red); evening:30(purple); midday:29(purple)
- 22 -> combined:133(red); evening:67(purple); midday:66(purple)
- 24 -> combined:43(blue); evening:63(red)
- 26 -> combined:43(blue); evening:27(purple)
- 36 -> combined:37(blue); evening:79(red)
- 44 -> combined:33(purple); evening:37(purple)
- 48 -> combined:36(purple); midday:38(blue)
- 57 -> combined:29(purple); evening:46(blue)
- 67 -> combined:40(blue); midday:41(blue)
- 78 -> combined:29(purple); evening:55(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(7.009421428571429)[R2,XVAR-Cons(CEM)], 6(6.610128571428572)[R1,XVAR-Cons(CEM)], 7(1.6443)[R2,Mirror-Echo], 1(1.2025714285714286)[R1,Mirror-Echo], 8(0.21314285714285713)[R3,Swap]
- P2: 7(3.884714285714286)[R2,Mirror-Echo], 2(2.6672714285714285)[R3,Mirror-Echo], 6(1.2971428571428572)[R1,Double-Pressure], 0(1.1714285714285715)[R1,Double-Pressure], 8(0.6723071428571428)[R2,Mirror-Echo]
- P3: 4(6.592257142857143)[R1,Mirror-Echo], 0(3.7951428571428574)[R2,XVAR-Cons(CM)], 9(3.750714285714286)[R3,Mirror-Echo], 1(1.1016)[R2,Double-Pressure], 2(1.0971)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=20), P2:0(gap=15), P3:4(gap=33); top cartesian candidates: 274, 224, 674, 624, 279.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:707(B),evening:806(B); 128→combined:931(B),evening:907(B); 226→combined:669(B),evening:708(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:343, 16:297, 17:169, 20:147, 12:92.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=547 Evening=698; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 457 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 689 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 547 (canon 457): box `457` covers winner `547` (boxed hit).
  - Evening winner 698 (canon 689): box `689` covers winner `698` (boxed hit).
- Key tags:
  - cross-variant convergence | VT lane density | doubles/mirror pressure | hot columns/col1 funnels | Aux positional pressure
- Drivers:
  - Overall: support (some Stable exact boxed hits).
- Conflicts:
  - If tools disagree (Stable/DR/VTRAC/HotZones), treat as noisy day; log as negative-control (do not tune yet).
- Fix-now vs fix-later:
  - Fix-now: none (sharepack artifacts exist; audit PASS).
  - Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
- Next run:
  - Continue filling remaining states/days; then generate day synthesis + re-export corpus summary.
