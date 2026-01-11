# Master Validation Run Report — Pennsylvania4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-09/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-09/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-09/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-09/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-09/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-09/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_811_20260110_035059.html`
- `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_014_20260110_035100.html`

Winners JSON files:
- `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_811_20260110_035059.json`
- `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_014_20260110_035100.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 811 (canon 118): exact_boxed=True exact_straight=True | rank 19/5619 (rank_frac 0.003); Evening 014 (canon 014): exact_boxed=True exact_straight=True | rank 483/5619 (rank_frac 0.086)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 811 idx18 (rank 4/35, frac 0.114), 014 idx9 (rank 8/35, frac 0.229)
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

### 2.Stable — Pennsylvania4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-09)

## Midday winner 811 (canonical 118)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=53 | family_rows=248 | exact_boxed=53 | exact_straight=38 | vt_boxed=53
- Scores (patterns_scores.csv): rank 19/5619 (rank_frac 0.003381384588004983) | score 29.0 (top 41.5, ratio 0.6987951807228916, delta 12.5) | section Evening, Set Set1, Draw Draw3, Col 1, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat5|vstr2|hot2|dom_last|perm2|double_mirror|draw_chain6
- Compound (patterns_compound.csv): rank 4/1788 (rank_frac 0.0022371364653243847) | score 79.0 (top 88.5, ratio 0.8926553672316384, delta 9.5) | section Combined, col1_hits 6, hot2 8, set_chain 3, draw_chain 7 | why set_chain3|draw_chain7|col1x6|hot1x4|hot2x8|vstrx15|dblmirrorx27
- Families (patterns_families.csv): count 50 | rank 31/1479 (rank_frac 0.020960108181203516) | score 28.0 (top 33.0, ratio 0.8484848484848485, delta 5.0) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=20

## Evening winner 014 (canonical 014)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=4 | family_rows=245 | exact_boxed=4 | exact_straight=3 | vt_boxed=4
- Scores (patterns_scores.csv): rank 483/5619 (rank_frac 0.08595835557928456) | score 20.5 (top 41.5, ratio 0.4939759036144578, delta 21.0) | section Evening, Set Set1, Draw Draw1, Col 1, hot 2, vt_straight 0.0 | why boxed|cov4|vstr2|hot2|dom_last|perm2|hidden3v
- Compound (patterns_compound.csv): rank 256/1788 (rank_frac 0.14317673378076062) | score 24.0 (top 88.5, ratio 0.2711864406779661, delta 64.5) | section Evening, col1_hits 1, hot2 1, set_chain 1, draw_chain 1 | why draw_chain1|col1x1|hot2x1
- Families (patterns_families.csv): count 75 | rank 31/1479 (rank_frac 0.020960108181203516) | score 28.0 (top 33.0, ratio 0.8484848484848485, delta 5.0) | section Combined, hot2 3
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=71

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 113 | section Combined | score 88.5 | col1_hits 7 | hot2 11
- rank    2 | canon 119 | section Combined | score 85.0 | col1_hits 7 | hot2 11
- rank   11 | canon 239 | section Combined | score 68.0 | col1_hits 7 | hot2 11
- rank   30 | canon 1399 | section Combined | score 53.0 | col1_hits 5 | hot2 8
- rank   17 | canon 138 | section Combined | score 61.5 | col1_hits 6 | hot2 8
- rank   15 | canon 1138 | section Combined | score 62.0 | col1_hits 6 | hot2 8
- rank   19 | canon 238 | section Combined | score 61.0 | col1_hits 5 | hot2 8
- rank   20 | canon 113899 | section Combined | score 60.5 | col1_hits 5 | hot2 8
- rank   33 | canon 2899 | section Combined | score 52.5 | col1_hits 5 | hot2 8
- rank    5 | canon 114 | section Evening | score 78.0 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1472 | family 31 | score 4.0 | hot2 0 | section Midday
- rank 1408 | family 20 | score 7.0 | hot2 0 | section Midday
- rank  684 | family 28 | score 16.5 | hot2 0 | section Midday
- rank  684 | family 27 | score 16.5 | hot2 0 | section Midday
- rank  684 | family 12 | score 16.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 811 (canon 118): exact_boxed=True exact_straight=True | rank 19/5619 (rank_frac 0.003); Evening 014 (canon 014): exact_boxed=True exact_straight=True | rank 483/5619 (rank_frac 0.086)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260110)

## Midday winner 811 (canonical 118)
- Stamp (winner_stamp.json): items_total=185 | exact_any=9 exact_final=0 | vtrac_any=180 vtrac_final=0 | drop_exact_any=30 drop_exact_final=0 | drop_vtrac_any=96 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=47 family_vtrac_final=0
- Flags (winner_flags.csv): rows=185 | exact_any=9 vtrac_any=180 | drop_exact_any=30 drop_vtrac_any=96 | family_exact_any=0 family_vtrac_any=47 | vt_boxed=101 vt_straight=0
- Hits (winner_hits.csv): rows=185 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=101 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.827143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 014 (canonical 014)
- Stamp (winner_stamp.json): items_total=50 | exact_any=12 exact_final=0 | vtrac_any=28 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=39 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=13 family_vtrac_final=0
- Flags (winner_flags.csv): rows=50 | exact_any=12 vtrac_any=28 | drop_exact_any=0 drop_vtrac_any=39 | family_exact_any=0 family_vtrac_any=13 | vt_boxed=30 vt_straight=0
- Hits (winner_hits.csv): rows=50 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=30 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.565714 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 811 (canonical 118)
- Stamp (winner_stamp.json): items_total=749 | exact_any=165 exact_final=0 | vtrac_any=744 vtrac_final=0 | drop_exact_any=215 drop_exact_final=0 | drop_vtrac_any=449 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=409 family_vtrac_final=0
- Flags (winner_flags.csv): rows=749 | exact_any=165 vtrac_any=744 | drop_exact_any=215 drop_vtrac_any=449 | family_exact_any=0 family_vtrac_any=409 | vt_boxed=536 vt_straight=0
- Hits (winner_hits.csv): rows=749 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=536 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.34381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 221 | score_v2 12.34381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 5 | pattern 221 | score_v2 12.24381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 221 | score_v2 12.24381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 221 | score_v2 11.89381 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 922 | score_v2 11.827143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 922 | score_v2 11.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 921 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 922 | score_v2 11.608571 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 922 | score_v2 11.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 922 | score_v2 11.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 221 | score_v2 12.34381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 922 | score_v2 11.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 921 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 922 | score_v2 11.608571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 992 | score_v2 11.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 922 | score_v2 11.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 992 | score_v2 10.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 221 | score_v2 10.74381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 554 | score_v2 10.565714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 211 | score_v2 10.38131 | tags exact,vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 811 (canon 118): items_total=185 exact_any=9 vtrac_any=180 | top winner_present=False best_rank=None/16; Evening 014 (canon 014): items_total=50 exact_any=12 vtrac_any=28 | top winner_present=False best_rank=None/20; Combined 811 (canon 118): items_total=749 exact_any=165 vtrac_any=744 | top winner_present=False best_rank=None/18
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 221, 922, 921, 922, 992.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260110_035302)

## Top indices (from enhanced JSON)
- index 5 | score 51.49129999999999 | features: presence=33.853799999999985, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 37.421049999999994 | features: presence=25.733549999999997, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 27 | score 36.542739999999995 | features: presence=20.785239999999995, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 18 | score 35.304362499999996 | features: presence=23.7368625, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 3 | score 32.04245 | features: presence=15.58495, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 20 | score 27.181580000000007 | features: presence=17.934080000000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 21.358975 | features: presence=14.741474999999998, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 9 | score 21.241750000000007 | features: presence=13.944250000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 20.958000000000002 | features: presence=13.130500000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 21 | score 19.571150000000003 | features: presence=9.453650000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
590, 193, 059, 095, 019, 932, 237, 732, 132, 091

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 811 | index 18 | file Pennsylvania4_vtrac18_winner_811_20260110_035059.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 014 | index 9 | file Pennsylvania4_vtrac9_winner_014_20260110_035100.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 811 | index 18 rank 4/35 (rank_frac 0.11428571428571428) | score 35.304362499999996 (top 51.49129999999999, ratio 0.6856374280703731, delta 16.186937499999992) | winner_in_index_straights=False | top_index_straights: (none)
- winner 014 | index 9 rank 8/35 (rank_frac 0.22857142857142856) | score 21.241750000000007 (top 51.49129999999999, ratio 0.41253085472691525, delta 30.24954999999998) | winner_in_index_straights=False | top_index_straights: 019 (10.165), 091 (8.252), 195 (3.14)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 811→idx18 rank 4/35 (frac 0.114); 014→idx9 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 5, 17, 27, 18, 3.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-09)

## Midday winner 811 (canonical 118)
- Top lanes (hot_zones_top_lanes.csv): present | rank 77/210 (rank_frac 0.36666666666666664) | score_mean 17.338 (top 23.581, ratio 0.7352529578898266, delta 6.2429999999999986)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 014 (canonical 014)
- Top lanes (hot_zones_top_lanes.csv): present | rank 16/210 (rank_frac 0.0761904761904762) | score_mean 20.886 (top 23.581, ratio 0.8857130740850685, delta 2.6950000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 006 | vt_triad 12 | score_mean 23.581 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    2 | triad 057 | vt_triad 113 | score_mean 22.82 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 146 | vt_triad 225 | score_mean 22.215 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 169 | vt_triad 225 | score_mean 22.015 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    6 | triad 056 | vt_triad 112 | score_mean 21.975 | tags hot12,hot16,hot20,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 015 | vt_triad 112 | score_mean 21.975 | tags hot12,hot16,hot20,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 559 | vt_triad 15 | score_mean 21.784 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    9 | triad 456 | vt_triad 125 | score_mean 21.724 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 005 | vt_triad 11 | score_mean 21.22 | tags funnel_precol1,hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 811 (canon 118): rank 77/210 (rank_frac 0.367) ratio_to_top=0.7352529578898266; Evening 014 (canon 014): rank 16/210 (rank_frac 0.076) ratio_to_top=0.8857130740850685
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

Aux draws snapshot dir: `sharepacks/2026-01-09/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-09/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=574, 750, 263, 060, 757
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-09/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=750, 060, 684, 546, 359
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-09/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=574, 263, 757, 600, 980

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=9 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=20), P2:1 (gap=27), P3:5 (gap=24)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=53.172853571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 495: score=45.59496285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 418: score=44.07040785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 412: score=42.6780525 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 815: score=42.26435714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 435: score=41.998914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 413: score=39.21647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=38.27984285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 498: score=36.49251714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 445: score=35.940664285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 159: ds=896 sev=B
- 007: ds=893 sev=B
- 088: ds=857 sev=B
- 008: ds=835 sev=B
- 444: ds=811 sev=B
- 039: ds=786 sev=B
- 355: ds=776 sev=B
- 344: ds=705 sev=B
- 788: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=153 sev=red
  - 88: ds=91 sev=blue
  - 66: ds=79 sev=blue
  - 55: ds=56 sev=purple
  - 11: ds=41 sev=purple
  - 22: ds=15 sev=-
  - 44: ds=11 sev=-
  - 99: ds=10 sev=-
  - 77: ds=4 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 69: ds=50 sev=blue
  - 34: ds=45 sev=blue
  - 19: ds=43 sev=blue
  - 15: ds=35 sev=purple
  - 79: ds=30 sev=purple
  - 27: ds=29 sev=purple
  - 67: ds=29 sev=purple
  - 58: ds=28 sev=purple
  - 01: ds=27 sev=purple
  - 14: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:295, 26:252, 16:110, 7:78, 6:73, 13:71, 19:67, 1:56, 11:53, 23:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=295 fs=2 fl=1 hz=0.007380073800738007, 26:ds=252 fs=0 fl=1 hz=0.003898635477582846, 16:ds=110 fs=3 fl=2 hz=0.007371007371007371, 7:ds=78 fs=35 fl=1 hz=0.04, 6:ds=73 fs=21 fl=1 hz=0.025611175785797437, 13:ds=71 fs=21 fl=1 hz=0.024553571428571428, 19:ds=67 fs=20 fl=3 hz=0.02558398220244716, 1:ds=56 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=53 fs=48 fl=0 hz=0.05128205128205128, 23:ds=47 fs=22 fl=1 hz=0.02415966386554622

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S20: ds=91 flags=purple
- S25: ds=68 flags=purple
- S4: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=40 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=29), P2:9 (gap=16), P3:5 (gap=34)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=53.172853571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 495: score=45.59496285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 418: score=44.07040785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 412: score=42.6780525 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 815: score=42.26435714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 435: score=41.998914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 413: score=39.21647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=38.27984285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 498: score=36.49251714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 445: score=35.940664285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=984 sev=B
- 288: ds=971 sev=B
- 255: ds=942 sev=B
- 668: ds=924 sev=B
- 199: ds=872 sev=B
- 499: ds=798 sev=B
- 399: ds=781 sev=B
- 039: ds=769 sev=B
- 448: ds=758 sev=B
- 005: ds=750 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=193 sev=red
  - 99: ds=140 sev=red
  - 77: ds=83 sev=blue
  - 33: ds=76 sev=blue
  - 88: ds=45 sev=purple
  - 66: ds=39 sev=purple
  - 11: ds=20 sev=-
  - 22: ds=7 sev=-
  - 44: ds=5 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 79: ds=80 sev=red
  - 12: ds=55 sev=blue
  - 69: ds=37 sev=blue
  - 13: ds=32 sev=purple
  - 03: ds=30 sev=purple
  - 09: ds=25 sev=purple
  - 37: ds=24 sev=-
  - 36: ds=23 sev=-
  - 34: ds=22 sev=-
  - 38: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:382, 1:367, 34:221, 16:179, 15:170, 32:147, 35:124, 28:69, 5:54, 7:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=382 fs=0 fl=0 hz=0.0, 1:ds=367 fs=2 fl=2 hz=0.009124087591240877, 34:ds=221 fs=19 fl=1 hz=0.02631578947368421, 16:ds=179 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=170 fs=23 fl=0 hz=0.029411764705882353, 32:ds=147 fs=3 fl=1 hz=0.006720430107526881, 35:ds=124 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=69 fs=26 fl=1 hz=0.03515625, 5:ds=54 fs=17 fl=2 hz=0.021253985122210415, 7:ds=41 fs=40 fl=1 hz=0.04311251314405889

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S23: ds=74 flags=purple
- S3: ds=68 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 123: score=2 tags=FLT,PAT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=70 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=36), P2:1 (gap=42), P3:6 (gap=26)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=53.172853571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 495: score=45.59496285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 418: score=44.07040785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 412: score=42.6780525 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 815: score=42.26435714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 435: score=41.998914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 413: score=39.21647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=38.27984285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 498: score=36.49251714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 445: score=35.940664285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=980 sev=B
- 009: ds=938 sev=B
- 255: ds=896 sev=B
- 138: ds=836 sev=B
- 117: ds=819 sev=B
- 158: ds=781 sev=B
- 344: ds=774 sev=B
- 199: ds=765 sev=B
- 112: ds=725 sev=B
- 277: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=135 sev=red
  - 33: ds=77 sev=blue
  - 44: ds=48 sev=purple
  - 66: ds=44 sev=purple
  - 11: ds=35 sev=purple
  - 55: ds=28 sev=purple
  - 22: ds=8 sev=-
  - 99: ds=5 sev=-
  - 00: ds=3 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 68: ds=93 sev=red
  - 07: ds=70 sev=red
  - 15: ds=58 sev=red
  - 78: ds=43 sev=blue
  - 19: ds=42 sev=blue
  - 01: ds=36 sev=purple
  - 18: ds=36 sev=purple
  - 14: ds=35 sev=purple
  - 39: ds=33 sev=purple
  - 16: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:624, 23:163, 26:126, 18:123, 13:72, 33:57, 16:55, 30:54, 24:51, 27:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=624 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=163 fs=17 fl=2 hz=0.025165562913907286, 26:ds=126 fs=2 fl=1 hz=0.0056657223796034, 18:ds=123 fs=23 fl=2 hz=0.02910360884749709, 13:ds=72 fs=20 fl=1 hz=0.024881516587677725, 33:ds=57 fs=18 fl=3 hz=0.023076923076923075, 16:ds=55 fs=4 fl=3 hz=0.009080590238365494, 30:ds=54 fs=35 fl=1 hz=0.03829787234042553, 24:ds=51 fs=37 fl=0 hz=0.04048140043763676, 27:ds=43 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=96 flags=blue+purple
- S1: ds=81 flags=blue+purple
- S24: ds=64 flags=blue+purple
- S3: ds=52 flags=purple
- S20: ds=46 flags=purple
- S25: ds=34 flags=purple

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
- 039 -> combined:786(B); midday:769(B)
- 199 -> evening:765(B); midday:872(B)
- 255 -> evening:896(B); midday:942(B)
- 344 -> combined:705(B); evening:774(B)
- 444 -> combined:811(B); evening:980(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:27(purple); evening:36(purple)
- 11 -> combined:41(purple); evening:35(purple)
- 14 -> combined:27(purple); evening:35(purple)
- 15 -> combined:35(purple); evening:58(red)
- 19 -> combined:43(blue); evening:42(blue)
- 33 -> combined:153(red); evening:77(blue); midday:76(blue)
- 34 -> combined:45(blue); evening:30(purple)
- 55 -> combined:56(purple); evening:28(purple); midday:193(red)
- 66 -> combined:79(blue); evening:44(purple); midday:39(purple)
- 69 -> combined:50(blue); evening:25(purple); midday:37(blue)
- 79 -> combined:30(purple); midday:80(red)
- 88 -> combined:91(blue); evening:135(red); midday:45(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(7.198285714285714)[R1,XVAR-Cons(CEM)], 8(3.2688571428571427)[R3,XVAR-Cons(CE)], 9(1.5324714285714285)[R2,Mirror-Echo], 1(1.0959999999999999)[R2,Double-Pressure], 0(0.9508)[R2,Double-Pressure]
- P2: 1(8.135271428571428)[R1,XVAR-Cons(CEM)], 9(3.7197142857142858)[R2,XVAR-Cons(CM)], 3(2.9404000000000003)[R3,XVAR-Cons(CE)], 4(0.38215)[R3,Swap], 0(0.24779285714285712)[R3,Swap]
- P3: 5(7.860228571428571)[R1,XVAR-Cons(CEM)], 8(2.1189714285714287)[R3,XVAR-Cons(CM)], 2(1.7777928571428572)[R2,XVAR-Cons(CE)], 6(1.4462857142857144)[R1,Double-Pressure], 3(1.3829142857142855)[R2,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:4(gap=20), P2:1(gap=27), P3:5(gap=24); top cartesian candidates: 415, 495, 418, 412, 815.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:786(B),midday:769(B); 199→midday:872(B),evening:765(B); 255→midday:942(B),evening:896(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:295, 26:252, 16:110, 7:78, 6:73.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=811 Evening=014; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 118 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 014 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 811 (canon 118): box `118` covers winner `811` (boxed hit).
  - Evening winner 014 (canon 014): box `014` covers winner `014` (boxed hit).
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
