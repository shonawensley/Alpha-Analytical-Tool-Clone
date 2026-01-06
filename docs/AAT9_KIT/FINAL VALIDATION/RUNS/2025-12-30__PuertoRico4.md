# Master Validation Run Report — PuertoRico4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/PuertoRico4/`
- Winners lens: `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2025-12-30/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2025-12-30/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2025-12-30/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2025-12-30/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2025-12-30/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2025-12-30/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac14_winner_098_20260105_051214.html`
- `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac24_winner_643_20260105_051216.html`

Winners JSON files:
- `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac14_winner_098_20260105_051214.json`
- `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac24_winner_643_20260105_051216.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 098 (canon 089): exact_boxed=True exact_straight=True | rank 4999/5975 (rank_frac 0.837); Evening 643 (canon 346): exact_boxed=True exact_straight=True | rank 544/5975 (rank_frac 0.091)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 098 idx14 (rank 4/35, frac 0.114), 643 idx24 (rank 8/35, frac 0.229)
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

### 2.Stable — PuertoRico4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2025-12-30)

## Midday winner 098 (canonical 089)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=664 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 4999/5975 (rank_frac 0.836652719665272) | score 10.0 (top 35.5, ratio 0.28169014084507044, delta 25.5) | section Midday, Set Set1, Draw Draw5, Col 3, hot 0, vt_straight 2.0 | why straight|cov1|vtrac_straight|set_chain2
- Compound (patterns_compound.csv): rank 921/1863 (rank_frac 0.4943639291465378) | score 13.5 (top 88.0, ratio 0.1534090909090909, delta 74.5) | section Midday, col1_hits 0, hot2 0, set_chain 2, draw_chain 2 | why set_chain2|draw_chain2|vstrx1
- Families (patterns_families.csv): count 75 | rank 41/1397 (rank_frac 0.02934860415175376) | score 30.0 (top 37.5, ratio 0.8, delta 7.5) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=150

## Evening winner 643 (canonical 346)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=29 | family_rows=690 | exact_boxed=29 | exact_straight=19 | vt_boxed=29
- Scores (patterns_scores.csv): rank 544/5975 (rank_frac 0.09104602510460251) | score 20.5 (top 35.5, ratio 0.5774647887323944, delta 15.0) | section Combined, Set Set1, Draw Draw1, Col 1, hot 2, vt_straight 0.0 | why boxed|cov2|hp_repeat5|hot2|perm2|hidden3v|draw_chain6
- Compound (patterns_compound.csv): rank 10/1863 (rank_frac 0.005367686527106817) | score 59.5 (top 88.0, ratio 0.6761363636363636, delta 28.5) | section Combined, col1_hits 6, hot2 10, set_chain 1, draw_chain 6 | why draw_chain6|col1x6|hot1x6|hot2x10|vstrx8
- Families (patterns_families.csv): count 73 | rank 8/1397 (rank_frac 0.00572655690765927) | score 32.5 (top 37.5, ratio 0.8666666666666667, delta 5.0) | section Combined, hot2 5
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=177

## Top compound candidates (patterns_compound.csv)
- rank    8 | canon 3445 | section Midday | score 66.0 | col1_hits 5 | hot2 11
- rank    5 | canon 445 | section Midday | score 73.0 | col1_hits 7 | hot2 11
- rank    1 | canon 344 | section Midday | score 88.0 | col1_hits 7 | hot2 11
- rank    3 | canon 246 | section Evening | score 77.5 | col1_hits 8 | hot2 11
- rank    2 | canon 134 | section Combined | score 79.5 | col1_hits 8 | hot2 11
- rank    6 | canon 345 | section Midday | score 71.0 | col1_hits 6 | hot2 10
- rank   10 | canon 346 | section Combined | score 59.5 | col1_hits 6 | hot2 10
- rank   30 | canon 136 | section Combined | score 48.0 | col1_hits 6 | hot2 7
- rank   19 | canon 1346 | section Combined | score 53.5 | col1_hits 6 | hot2 7
- rank   11 | canon 144 | section Midday | score 59.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1364 | family 13 | score 5.0 | hot2 0 | section Midday
- rank   84 | family 34 | score 28.0 | hot2 0 | section Midday
- rank 1151 | family 2 | score 9.5 | hot2 0 | section Midday
- rank   55 | family 5 | score 29.0 | hot2 0 | section Midday
- rank   84 | family 34 | score 28.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 098 (canon 089): exact_boxed=True exact_straight=True | rank 4999/5975 (rank_frac 0.837); Evening 643 (canon 346): exact_boxed=True exact_straight=True | rank 544/5975 (rank_frac 0.091)
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

### 2.Digit Reduction — PuertoRico4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260105)

## Midday winner 098 (canonical 089)
- Stamp (winner_stamp.json): items_total=34 | exact_any=0 exact_final=0 | vtrac_any=24 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=32 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=34 | exact_any=0 vtrac_any=24 | drop_exact_any=0 drop_vtrac_any=32 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=24 vt_straight=0
- Hits (winner_hits.csv): rows=34 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=24 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.220476 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 643 (canonical 346)
- Stamp (winner_stamp.json): items_total=123 | exact_any=48 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=18 drop_exact_final=0 | drop_vtrac_any=53 drop_vtrac_final=0 | family_exact_any=6 family_exact_final=0 | family_vtrac_any=29 family_vtrac_final=0
- Flags (winner_flags.csv): rows=123 | exact_any=48 vtrac_any=120 | drop_exact_any=18 drop_vtrac_any=53 | family_exact_any=6 family_vtrac_any=29 | vt_boxed=47 vt_straight=0
- Hits (winner_hits.csv): rows=123 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=47 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 098 (canonical 089)
- Stamp (winner_stamp.json): items_total=94 | exact_any=0 exact_final=0 | vtrac_any=36 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=80 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=94 | exact_any=0 vtrac_any=36 | drop_exact_any=0 drop_vtrac_any=80 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=24 vt_straight=0
- Hits (winner_hits.csv): rows=94 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=24 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 11.220476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 241 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 10.987143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 10.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 10.887143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 559 | score_v2 10.837143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 10.820476 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 10.796234 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 10.787143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 5 | pattern 559 | score_v2 10.757143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 559 | score_v2 11.220476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 241 | score_v2 11.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 992 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 559 | score_v2 10.887143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 992 | score_v2 10.315714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 413 | score_v2 10.197143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 224 | score_v2 9.720476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 544 | score_v2 9.570476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 922 | score_v2 9.520476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 554 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 098 (canon 089): items_total=34 exact_any=0 vtrac_any=24 | top winner_present=False best_rank=None/10; Evening 643 (canon 346): items_total=123 exact_any=48 vtrac_any=120 | top winner_present=False best_rank=None/16; Combined 098 (canon 089): items_total=94 exact_any=0 vtrac_any=36 | top winner_present=False best_rank=None/28
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 241, 992, 559, 992.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260105_051506)

## Top indices (from enhanced JSON)
- index 33 | score 61.95756999999999 | features: presence=40.89006999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 34 | score 56.024729999999984 | features: presence=37.77722999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 51.875375 | features: presence=30.697875000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 50.78798 | features: presence=29.040480000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 42.65625000000001 | features: presence=22.05875, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 37.99149500000001 | features: presence=19.323995000000004, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 37.565374999999996 | features: presence=21.037874999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 34.197995 | features: presence=24.630495000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 32 | score 26.451417499999998 | features: presence=20.1839175, cross_section=0.5, set_echo=0.3, first_hit=0.2666666666666667
- index 23 | score 21.379212500000005 | features: presence=12.531712500000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
834, 534, 438, 583, 345, 413, 543, 134, 548, 584

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 098 | index 14 | file PuertoRico4_vtrac14_winner_098_20260105_051214.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 643 | index 24 | file PuertoRico4_vtrac24_winner_643_20260105_051216.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 098 | index 14 rank 4/35 (rank_frac 0.11428571428571428) | score 50.78798 (top 61.95756999999999, ratio 0.8197219484237359, delta 11.169589999999992) | winner_in_index_straights=False | top_index_straights: 534 (24.129), 345 (16.187), 543 (15.21)
- winner 643 | index 24 rank 8/35 (rank_frac 0.22857142857142856) | score 34.197995 (top 61.95756999999999, ratio 0.551958299849397, delta 27.75957499999999) | winner_in_index_straights=False | top_index_straights: 413 (15.686), 134 (11.726), 341 (10.419)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 098→idx14 rank 4/35 (frac 0.114); 643→idx24 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 33, 34, 15, 14, 4.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2025-12-30)

## Midday winner 098 (canonical 089)
- Top lanes (hot_zones_top_lanes.csv): present | rank 90/207 (rank_frac 0.43478260869565216) | score_mean 17.498 (top 24.62, ratio 0.7107229894394801, delta 7.122)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 643 (canonical 346)
- Top lanes (hot_zones_top_lanes.csv): present | rank 77/207 (rank_frac 0.3719806763285024) | score_mean 17.673 (top 24.62, ratio 0.7178310316815596, delta 6.947000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 24.62 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vt_straight
- rank    2 | triad 578 | vt_triad 134 | score_mean 23.303 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 029 | vt_triad 135 | score_mean 22.916 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 379 | vt_triad 345 | score_mean 21.66 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 677 | vt_triad 23 | score_mean 21.128 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 247 | vt_triad 335 | score_mean 20.84 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 279 | vt_triad 335 | score_mean 20.84 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 229 | vt_triad 35 | score_mean 20.653 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 244 | vt_triad 35 | score_mean 20.538 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank   10 | triad 477 | vt_triad 35 | score_mean 20.529 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 098 (canon 089): rank 90/207 (rank_frac 0.435) ratio_to_top=0.7107229894394801; Evening 643 (canon 346): rank 77/207 (rank_frac 0.372) ratio_to_top=0.7178310316815596
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

Aux draws snapshot dir: `sharepacks/2025-12-30/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=785, 875, 490, 793, 902
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=875, 793, 962, 087, 627
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=785, 490, 902, 517, 007

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=2 max=3 last_repeat_gap=1 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=54), P2:4 (gap=34), P3:9 (gap=29)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=998 sev=B
- 001: ds=987 sev=B
- 447: ds=978 sev=B
- 000: ds=726 sev=B
- 039: ds=714 sev=B
- 466: ds=710 sev=B
- 677: ds=688 sev=B
- 259: ds=679 sev=B
- 577: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=58 sev=purple
  - 77: ds=57 sev=purple
  - 99: ds=48 sev=purple
  - 44: ds=43 sev=purple
  - 11: ds=42 sev=purple
  - 55: ds=23 sev=-
  - 33: ds=18 sev=-
  - 66: ds=17 sev=-
  - 88: ds=10 sev=-
  - 00: ds=8 sev=-
- non_repeating:
  - 47: ds=166 sev=red
  - 24: ds=80 sev=red
  - 45: ds=77 sev=red
  - 25: ds=55 sev=blue
  - 89: ds=48 sev=blue
  - 48: ds=44 sev=blue
  - 23: ds=41 sev=blue
  - 56: ds=37 sev=blue
  - 59: ds=37 sev=blue
  - 05: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:185, 27:126, 5:89, 32:83, 26:78, 14:77, 31:75, 28:57, 18:49, 34:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=185 fs=18 fl=1 hz=0.025477707006369428, 27:ds=126 fs=24 fl=1 hz=0.029868578255675033, 5:ds=89 fs=27 fl=1 hz=0.0343980343980344, 32:ds=83 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=78 fs=4 fl=2 hz=0.01020408163265306, 14:ds=77 fs=44 fl=1 hz=0.049723756906077346, 31:ds=75 fs=14 fl=3 hz=0.018619934282584887, 28:ds=57 fs=26 fl=0 hz=0.0278372591006424, 18:ds=49 fs=21 fl=0 hz=0.023182297154899896, 34:ds=48 fs=26 fl=0 hz=0.02857142857142857

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=75 flags=purple
- S23: ds=57 flags=blue+purple
- S26: ds=48 flags=blue+purple
- S8: ds=42 flags=purple
- S6: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=57 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=27), P2:1 (gap=23), P3:1 (gap=16)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=957 sev=B
- 299: ds=948 sev=B
- 003: ds=939 sev=B
- 077: ds=925 sev=B
- 333: ds=874 sev=B
- 555: ds=848 sev=B
- 088: ds=819 sev=B
- 888: ds=813 sev=B
- 666: ds=798 sev=B
- 447: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=104 sev=blue
  - 22: ds=77 sev=blue
  - 11: ds=53 sev=purple
  - 99: ds=37 sev=purple
  - 77: ds=28 sev=purple
  - 33: ds=22 sev=-
  - 44: ds=21 sev=-
  - 88: ds=19 sev=-
  - 55: ds=11 sev=-
  - 66: ds=8 sev=-
- non_repeating:
  - 47: ds=110 sev=red
  - 24: ds=56 sev=red
  - 38: ds=41 sev=blue
  - 03: ds=40 sev=blue
  - 04: ds=40 sev=blue
  - 35: ds=38 sev=blue
  - 45: ds=38 sev=blue
  - 48: ds=30 sev=purple
  - 89: ds=30 sev=purple
  - 19: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:136, 29:94, 10:92, 27:91, 26:88, 3:81, 16:53, 23:48, 15:46, 5:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=136 fs=18 fl=0 hz=0.02211874272409779, 29:ds=94 fs=16 fl=2 hz=0.020809248554913295, 10:ds=92 fs=20 fl=3 hz=0.026376146788990827, 27:ds=91 fs=19 fl=1 hz=0.024721878862793572, 26:ds=88 fs=7 fl=2 hz=0.011682242990654207, 3:ds=81 fs=31 fl=0 hz=0.03506787330316742, 16:ds=53 fs=4 fl=2 hz=0.009695290858725763, 23:ds=48 fs=31 fl=1 hz=0.034782608695652174, 15:ds=46 fs=25 fl=0 hz=0.026939655172413795, 5:ds=44 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=40 flags=purple
- S25: ds=37 flags=purple

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
- current_index=11 streak=1 max=2 last_repeat_gap=6 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=27), P2:5 (gap=43), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=989 sev=B
- 579: ds=970 sev=B
- 114: ds=914 sev=B
- 555: ds=853 sev=B
- 888: ds=761 sev=B
- 067: ds=750 sev=B
- 446: ds=737 sev=B
- 259: ds=735 sev=B
- 224: ds=721 sev=B
- 449: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=141 sev=red
  - 44: ds=137 sev=red
  - 77: ds=39 sev=purple
  - 66: ds=30 sev=purple
  - 22: ds=29 sev=purple
  - 99: ds=24 sev=-
  - 11: ds=21 sev=-
  - 33: ds=9 sev=-
  - 88: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 25: ds=97 sev=red
  - 47: ds=83 sev=red
  - 45: ds=67 sev=red
  - 26: ds=60 sev=red
  - 39: ds=53 sev=blue
  - 59: ds=53 sev=blue
  - 79: ds=44 sev=blue
  - 24: ds=40 sev=blue
  - 34: ds=40 sev=blue
  - 05: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:446, 32:161, 4:115, 22:114, 10:102, 31:90, 5:80, 33:66, 27:63, 1:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=446 fs=5 fl=1 hz=0.01662049861495845, 32:ds=161 fs=6 fl=1 hz=0.009987515605493134, 4:ds=115 fs=23 fl=2 hz=0.03071253071253071, 22:ds=114 fs=34 fl=0 hz=0.04, 10:ds=102 fs=16 fl=2 hz=0.0234375, 31:ds=90 fs=18 fl=3 hz=0.02394526795895097, 5:ds=80 fs=18 fl=2 hz=0.022446689113355782, 33:ds=66 fs=12 fl=1 hz=0.017361111111111112, 27:ds=63 fs=18 fl=1 hz=0.02358490566037736, 1:ds=55 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=73 flags=purple
- S24: ds=64 flags=purple
- S18: ds=49 flags=red+purple
- S23: ds=44 flags=blue+purple
- S16: ds=39 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 039: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:679(B); evening:735(B)
- 447 -> combined:978(B); midday:737(B)
- 555 -> evening:853(B); midday:848(B)
- 888 -> evening:761(B); midday:813(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:35(purple); evening:36(purple)
- 11 -> combined:42(purple); midday:53(purple)
- 19 -> combined:34(purple); midday:29(purple)
- 22 -> combined:58(purple); evening:29(purple); midday:77(blue)
- 23 -> combined:41(blue); evening:27(purple)
- 24 -> combined:80(red); evening:40(blue); midday:56(red)
- 25 -> combined:55(blue); evening:97(red); midday:27(purple)
- 44 -> combined:43(purple); evening:137(red)
- 45 -> combined:77(red); evening:67(red); midday:38(blue)
- 47 -> combined:166(red); evening:83(red); midday:110(red)
- 48 -> combined:44(blue); midday:30(purple)
- 56 -> combined:37(blue); evening:36(purple)
- 59 -> combined:37(blue); evening:53(blue)
- 77 -> combined:57(purple); evening:39(purple); midday:28(purple)
- 89 -> combined:48(blue); midday:30(purple)
- 99 -> combined:48(purple); midday:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.612285714285715)[R1,XVAR-Cons(CEM)], 1(3.3039785714285714)[R2,XVAR-Cons(CE)], 3(1.8384285714285715)[R3,XVAR-Cons(CM)], 4(1.1389)[R2,Double-Pressure], 6(0.3317928571428571)[R3,Mirror-Echo]
- P2: 4(7.135878571428571)[R1,XVAR-Cons(CEM)], 5(6.798792857142857)[R2,XVAR-Cons(CEM)], 1(1.3867142857142856)[R1,Double-Pressure], 2(1.3060999999999998)[R2,Double-Pressure], 3(0.29800000000000004)[R3,Swap]
- P3: 9(7.040328571428572)[R1,Mirror-Echo], 4(3.281885714285714)[R2,Mirror-Echo], 6(2.847714285714286)[R3,XVAR-Cons(CE)], 1(1.0777142857142856)[R1,Double-Pressure], 8(0.38349999999999995)[R2,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=54), P2:4(gap=34), P3:9(gap=29); top cartesian candidates: 249, 259, 244, 254, 149.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6'], 'pairs': {'remaining_count': 1}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 259→combined:679(B),evening:735(B); 447→combined:978(B),midday:737(B); 555→midday:848(B),evening:853(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:185, 27:126, 5:89, 32:83, 26:78.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=098 Evening=643; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 089 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 346 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 098 (canon 089): box `089` covers winner `098` (boxed hit).
  - Evening winner 643 (canon 346): box `346` covers winner `643` (boxed hit).
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
