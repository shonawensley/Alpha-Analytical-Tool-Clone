# Master Validation Run Report — OntarioCanada4 — results 2026-01-04 (history workbook ~ 2026-01-03)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-04/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-04/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-04/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-04/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-04/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-04/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-04/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac14_winner_958_20260105_055147.html`
- `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac29_winner_382_20260105_055149.html`

Winners JSON files:
- `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac14_winner_958_20260105_055147.json`
- `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac29_winner_382_20260105_055149.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-04/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 958 (canon 589): exact_boxed=None exact_straight=None | rank 925/4859 (rank_frac 0.190); Evening 382 (canon 238): exact_boxed=None exact_straight=None | rank 1708/4859 (rank_frac 0.352)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 958 idx14 (rank 27/35, frac 0.771), 382 idx29 (rank 20/35, frac 0.571)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — OntarioCanada4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-04)

## Midday winner 958 (canonical 589)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=162 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 925/4859 (rank_frac 0.19036838855731633) | score 16.0 (top 37.5, ratio 0.4266666666666667, delta 21.5) | section Evening, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hot2|vtrac_straight|set_chain2|draw_chain3
- Compound (patterns_compound.csv): rank 95/1804 (rank_frac 0.05266075388026607) | score 29.0 (top 74.5, ratio 0.38926174496644295, delta 45.5) | section Evening, col1_hits 1, hot2 1, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|col1x1|hot1x5|hot2x1|vstrx2
- Families (patterns_families.csv): count 23 | rank 282/1288 (rank_frac 0.21894409937888198) | score 20.0 (top 29.5, ratio 0.6779661016949152, delta 9.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Evening winner 382 (canonical 238)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=555 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 1708/4859 (rank_frac 0.35151265692529327) | score 13.5 (top 37.5, ratio 0.36, delta 24.0) | section Evening, Set Set1, Draw Draw7, Col 1, hot 0, vt_straight 2.0 | why straight|cov1|mirror|hidden3v|vtrac_straight|set_chain2|draw_chain3
- Compound (patterns_compound.csv): rank 312/1804 (rank_frac 0.1729490022172949) | score 20.0 (top 74.5, ratio 0.2684563758389262, delta 54.5) | section Evening, col1_hits 1, hot2 0, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|col1x1|hot1x1|vstrx1
- Families (patterns_families.csv): count 61 | rank 33/1288 (rank_frac 0.02562111801242236) | score 25.5 (top 29.5, ratio 0.864406779661017, delta 4.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Top compound candidates (patterns_compound.csv)
- rank   11 | canon 267 | section Midday | score 50.5 | col1_hits 4 | hot2 8
- rank    6 | canon 677 | section Midday | score 57.5 | col1_hits 5 | hot2 6
- rank   25 | canon 246 | section Midday | score 42.5 | col1_hits 5 | hot2 6
- rank    7 | canon 477 | section Midday | score 56.0 | col1_hits 5 | hot2 6
- rank    1 | canon 188 | section Evening | score 74.5 | col1_hits 2 | hot2 6
- rank    3 | canon 1188 | section Evening | score 64.0 | col1_hits 2 | hot2 6
- rank    2 | canon 118 | section Evening | score 74.0 | col1_hits 2 | hot2 6
- rank   50 | canon 256 | section Midday | score 34.5 | col1_hits 0 | hot2 5
- rank   32 | canon 047 | section Combined | score 40.0 | col1_hits 3 | hot2 5
- rank   25 | canon 167 | section Combined | score 42.5 | col1_hits 0 | hot2 5

## Top families (patterns_families.csv)
- rank 1226 | family 14 | score 6.0 | hot2 0 | section Midday
- rank  316 | family 21 | score 19.5 | hot2 0 | section Midday
- rank  587 | family 22 | score 15.5 | hot2 5 | section Midday
- rank  658 | family 7 | score 14.5 | hot2 3 | section Midday
- rank  658 | family 10 | score 14.5 | hot2 3 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 958 (canon 589): exact_boxed=None exact_straight=None | rank 925/4859 (rank_frac 0.190); Evening 382 (canon 238): exact_boxed=None exact_straight=None | rank 1708/4859 (rank_frac 0.352)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260105)

## Midday winner 958 (canonical 589)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 382 (canonical 238)
- Stamp (winner_stamp.json): items_total=60 | exact_any=0 exact_final=0 | vtrac_any=60 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=60 | exact_any=0 vtrac_any=60 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=60 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.097143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 958 (canonical 589)
- Stamp (winner_stamp.json): items_total=4 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=4 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=4 | exact_any=0 vtrac_any=0 | drop_exact_any=3 drop_vtrac_any=4 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=4 vt_straight=0
- Hits (winner_hits.csv): rows=4 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=4 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.227143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 554 | score_v2 12.227143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 552 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 552 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 552 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 552 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 552 | score_v2 11.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 552 | score_v2 11.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 5 | pattern 552 | score_v2 11.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 552 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 7 | pattern 552 | score_v2 11.627143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 554 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 552 | score_v2 12.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 544 | score_v2 11.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 594 | score_v2 11.097143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 552 | score_v2 10.737143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 594 | score_v2 10.447143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 554 | score_v2 10.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 554 | score_v2 9.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 554 | score_v2 9.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 599 | score_v2 9.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 958 (canon 589): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/20; Evening 382 (canon 238): items_total=60 exact_any=0 vtrac_any=60 | top winner_present=False best_rank=None/20; Combined 958 (canon 589): items_total=4 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/36
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 554, 552, 544, 594, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_055541)

## Top indices (from enhanced JSON)
- index 19 | score 39.177910000000004 | features: presence=22.13041, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 17 | score 38.51989 | features: presence=22.07239, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 25.682637500000002 | features: presence=17.905137500000002, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 25 | score 20.74225 | features: presence=9.90475, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 3 | score 18.324199166666666 | features: presence=11.751907499999998, set_echo=0.6, first_hit=0.4, column_span=0.23229166666666665
- index 34 | score 15.587558333333336 | features: presence=5.408600000000002, set_echo=0.6, first_hit=0.13333333333333336, column_span=0.06562499999999999
- index 16 | score 15.547350000000002 | features: presence=6.029850000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 6 | score 14.064485000000003 | features: presence=7.996985000000001, cross_section=0.5, set_echo=0.3, first_hit=0.2
- index 22 | score 11.857619999999999 | features: presence=6.35012, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 7 | score 10.208295000000001 | features: presence=5.710795, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
617, 167, 671, 716, 164, 047, 704, 416, 196, 016

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 958 | index 14 | file OntarioCanada4_vtrac14_winner_958_20260105_055147.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 382 | index 29 | file OntarioCanada4_vtrac29_winner_382_20260105_055149.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 958 | index 14 rank 27/35 (rank_frac 0.7714285714285715) | score 1.155375 (top 39.177910000000004, ratio 0.02949047052280226, delta 38.022535000000005) | winner_in_index_straights=False | top_index_straights: 034 (0.103)
- winner 382 | index 29 rank 20/35 (rank_frac 0.5714285714285714) | score 3.63625 (top 39.177910000000004, ratio 0.09281378205218195, delta 35.54166000000001) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 958→idx14 rank 27/35 (frac 0.771); 382→idx29 rank 20/35 (frac 0.571).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 19, 17, 12, 25, 3.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-04)

## Midday winner 958 (canonical 589)
- Top lanes (hot_zones_top_lanes.csv): present | rank 159/210 (rank_frac 0.7571428571428571) | score_mean 16.276 (top 20.665, ratio 0.7876119041858215, delta 4.388999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 382 (canonical 238)
- Top lanes (hot_zones_top_lanes.csv): present | rank 156/210 (rank_frac 0.7428571428571429) | score_mean 16.294 (top 20.665, ratio 0.7884829421727559, delta 4.370999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 006 | vt_triad 12 | score_mean 20.665 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 267 | vt_triad 233 | score_mean 20.525 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 035 | vt_triad 114 | score_mean 20.36 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 188 | vt_triad 24 | score_mean 19.879 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 168 | vt_triad 224 | score_mean 19.628 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    6 | triad 255 | vt_triad 13 | score_mean 19.598 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 127 | vt_triad 233 | score_mean 19.525 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 488 | vt_triad 45 | score_mean 19.42 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    9 | triad 667 | vt_triad 23 | score_mean 19.41 | tags funnel_precol1,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 118 | vt_triad 24 | score_mean 19.408 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 958 (canon 589): rank 159/210 (rank_frac 0.757) ratio_to_top=0.7876119041858215; Evening 382 (canon 238): rank 156/210 (rank_frac 0.743) ratio_to_top=0.7884829421727559
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

Aux draws snapshot dir: `sharepacks/2026-01-04/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=032, 968, 816, 053, 546
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=968, 053, 528, 918, 409
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=032, 816, 546, 932, 372

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=54 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=28), P2:8 (gap=26), P3:4 (gap=27)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=925 sev=B
- 555: ds=890 sev=B
- 039: ds=781 sev=B
- 333: ds=752 sev=B
- 188: ds=725 sev=B
- 266: ds=711 sev=B
- 477: ds=709 sev=B
- 126: ds=701 sev=B
- 669: ds=696 sev=B
- 007: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=127 sev=red
  - 55: ds=83 sev=blue
  - 11: ds=42 sev=purple
  - 88: ds=36 sev=purple
  - 44: ds=27 sev=purple
  - 77: ds=18 sev=-
  - 99: ds=15 sev=-
  - 66: ds=14 sev=-
  - 33: ds=13 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 01: ds=62 sev=red
  - 15: ds=59 sev=red
  - 17: ds=53 sev=blue
  - 12: ds=39 sev=blue
  - 24: ds=37 sev=blue
  - 26: ds=37 sev=blue
  - 67: ds=34 sev=purple
  - 36: ds=31 sev=purple
  - 48: ds=30 sev=purple
  - 08: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:337, 16:291, 17:163, 20:141, 33:87, 12:86, 26:81, 34:68, 8:64, 7:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=337 fs=1 fl=0 hz=0.005698005698005698, 16:ds=291 fs=2 fl=0 hz=0.006329113924050633, 17:ds=163 fs=19 fl=1 hz=0.024242424242424242, 20:ds=141 fs=13 fl=2 hz=0.01847290640394089, 33:ds=87 fs=24 fl=1 hz=0.027472527472527472, 12:ds=86 fs=45 fl=0 hz=0.04928806133625411, 26:ds=81 fs=2 fl=1 hz=0.006075334143377886, 34:ds=68 fs=14 fl=2 hz=0.019698725376593278, 8:ds=64 fs=39 fl=2 hz=0.044956140350877194, 7:ds=48 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=79 flags=purple
- S4: ds=73 flags=purple
- S3: ds=62 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 037: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS
  - 136: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=19 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=28), P2:7 (gap=25), P3:0 (gap=17)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=997 sev=B
- 333: ds=980 sev=B
- 255: ds=947 sev=B
- 355: ds=912 sev=B
- 466: ds=833 sev=B
- 446: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=63 sev=purple
  - 55: ds=41 sev=purple
  - 11: ds=31 sev=purple
  - 77: ds=24 sev=-
  - 88: ds=20 sev=-
  - 66: ds=15 sev=-
  - 44: ds=13 sev=-
  - 99: ds=7 sev=-
  - 33: ds=6 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 34: ds=72 sev=red
  - 07: ds=69 sev=red
  - 16: ds=55 sev=blue
  - 39: ds=43 sev=blue
  - 37: ds=38 sev=blue
  - 67: ds=38 sev=blue
  - 48: ds=35 sev=purple
  - 01: ds=31 sev=purple
  - 15: ds=29 sev=purple
  - 45: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:168, 34:163, 16:145, 27:100, 12:97, 14:82, 17:81, 20:70, 19:55, 33:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=168 fs=4 fl=3 hz=0.010432190760059612, 34:ds=163 fs=8 fl=4 hz=0.014423076923076924, 16:ds=145 fs=3 fl=0 hz=0.007462686567164179, 27:ds=100 fs=15 fl=2 hz=0.0189520624303233, 12:ds=97 fs=45 fl=0 hz=0.05079006772009029, 14:ds=82 fs=39 fl=0 hz=0.04276315789473684, 17:ds=81 fs=29 fl=2 hz=0.033879781420765025, 20:ds=70 fs=24 fl=3 hz=0.029315960912052113, 19:ds=55 fs=20 fl=2 hz=0.023732470334412083, 33:ds=43 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S25: ds=75 flags=purple
- S1: ds=64 flags=blue+purple
- S5: ds=62 flags=purple
- S9: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 127: score=1 tags=FLT
  - 137: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=56 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=15), P2:6 (gap=17), P3:9 (gap=41)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=904 sev=B
- 113: ds=855 sev=B
- 378: ds=848 sev=B
- 566: ds=837 sev=B
- 199: ds=829 sev=B
- 899: ds=807 sev=B
- 126: ds=803 sev=B
- 559: ds=798 sev=B
- 477: ds=787 sev=B
- 558: ds=753 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=233 sev=red
  - 22: ds=64 sev=purple
  - 00: ds=51 sev=purple
  - 44: ds=34 sev=purple
  - 11: ds=21 sev=-
  - 99: ds=19 sev=-
  - 88: ds=18 sev=-
  - 33: ds=16 sev=-
  - 77: ds=9 sev=-
  - 66: ds=7 sev=-
- non_repeating:
  - 36: ds=76 sev=red
  - 24: ds=60 sev=red
  - 89: ds=54 sev=blue
  - 15: ds=53 sev=blue
  - 78: ds=52 sev=blue
  - 49: ds=46 sev=blue
  - 57: ds=43 sev=blue
  - 09: ds=33 sev=purple
  - 01: ds=31 sev=purple
  - 12: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:429, 1:344, 16:195, 26:127, 17:105, 20:96, 3:75, 23:68, 33:66, 31:62

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=429 fs=0 fl=2 hz=0.005366726296958855, 1:ds=344 fs=0 fl=0 hz=0.0, 16:ds=195 fs=3 fl=1 hz=0.007853403141361256, 26:ds=127 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=105 fs=13 fl=3 hz=0.018626309662398137, 20:ds=96 fs=15 fl=2 hz=0.01925254813137033, 3:ds=75 fs=15 fl=4 hz=0.02092511013215859, 23:ds=68 fs=25 fl=2 hz=0.03085714285714286, 33:ds=66 fs=27 fl=1 hz=0.030803080308030802, 31:ds=62 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S2: ds=75 flags=blue+purple
- S4: ds=73 flags=purple
- S25: ds=62 flags=purple
- S20: ds=55 flags=purple
- S9: ds=53 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:701(B); evening:803(B)
- 128 -> combined:925(B); evening:904(B)
- 333 -> combined:752(B); midday:980(B)
- 477 -> combined:709(B); evening:787(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:62(red); evening:31(purple); midday:31(purple)
- 11 -> combined:42(purple); midday:31(purple)
- 12 -> combined:39(blue); evening:31(purple)
- 15 -> combined:59(red); evening:53(blue); midday:29(purple)
- 17 -> combined:53(blue); evening:27(purple); midday:26(purple)
- 22 -> combined:127(red); evening:64(purple); midday:63(purple)
- 24 -> combined:37(blue); evening:60(red)
- 36 -> combined:31(purple); evening:76(red)
- 44 -> combined:27(purple); evening:34(purple)
- 48 -> combined:30(purple); midday:35(purple)
- 55 -> combined:83(blue); evening:233(red); midday:41(purple)
- 67 -> combined:34(purple); midday:38(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.938600000000001)[R1,Mirror-Echo], 7(5.846878571428571)[R2,XVAR-Cons(CEM)], 2(1.3690714285714285)[R2,Mirror-Echo], 4(1.1178571428571429)[R1,Double-Pressure], 6(0.6980000000000001)[R3,Mirror-Echo]
- P2: 8(7.2801285714285715)[R1,XVAR-Cons(CEM)], 7(1.4464285714285714)[R1,Double-Pressure], 6(1.2075714285714285)[R1,Double-Pressure], 9(0.964)[R2,Double-Pressure], 3(0.3512285714285714)[R3,Mirror-Echo]
- P3: 4(6.366642857142857)[R1,XVAR-Cons(CEM)], 1(2.6776142857142857)[R3,XVAR-Cons(CE)], 9(1.8488214285714286)[R1,Mirror-Echo], 0(1.2075714285714285)[R1,Double-Pressure], 5(1.062)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-03.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=28), P2:8(gap=26), P3:4(gap=27); top cartesian candidates: 184, 784, 181, 781, 189.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 037, 127, 379, 478, 019.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:701(B),evening:803(B); 128→combined:925(B),evening:904(B); 333→combined:752(B),midday:980(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:337, 16:291, 17:163, 20:141, 33:87.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=958 Evening=382; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 589 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 238 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 958 (canon 589): box `589` covers winner `958` (boxed hit).
  - Evening winner 382 (canon 238): box `238` covers winner `382` (boxed hit).
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
