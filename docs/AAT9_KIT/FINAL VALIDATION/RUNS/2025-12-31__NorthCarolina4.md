# Master Validation Run Report — NorthCarolina4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/NorthCarolina4/`
- Winners lens: `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2025-12-31/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2025-12-31/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2025-12-31/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2025-12-31/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2025-12-31/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-12-31/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_867_20260105_052157.html`
- `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_057_20260105_052159.html`

Winners JSON files:
- `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_867_20260105_052157.json`
- `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_057_20260105_052159.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 867 (canon 678): exact_boxed=True exact_straight=True | rank 4908/5852 (rank_frac 0.839); Evening 057 (canon 057): exact_boxed=True exact_straight=True | rank 4674/5852 (rank_frac 0.799)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 867 idx21 (rank 24/35, frac 0.686), 057 idx3 (rank 9/35, frac 0.257)
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

### 2.Stable — NorthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2025-12-31)

## Midday winner 867 (canonical 678)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=6 | family_rows=216 | exact_boxed=6 | exact_straight=3 | vt_boxed=6
- Scores (patterns_scores.csv): rank 4908/5852 (rank_frac 0.8386876281613124) | score 10.0 (top 42.0, ratio 0.23809523809523808, delta 32.0) | section Midday, Set Set3, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why boxed|cov2|hp_repeat2|perm2|set_chain2
- Compound (patterns_compound.csv): rank 1005/1729 (rank_frac 0.5812608444187392) | score 12.0 (top 127.0, ratio 0.09448818897637795, delta 115.0) | section Midday, col1_hits 0, hot2 0, set_chain 2, draw_chain 0 | why set_chain2
- Families (patterns_families.csv): count 59 | rank 54/1532 (rank_frac 0.03524804177545692) | score 30.5 (top 38.0, ratio 0.8026315789473685, delta 7.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=67

## Evening winner 057 (canonical 057)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=182 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 4674/5852 (rank_frac 0.7987012987012987) | score 10.5 (top 42.0, ratio 0.25, delta 31.5) | section Midday, Set Set3, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why straight|cov1|hp_repeat2|mirror|hidden3v|set_chain2
- Compound (patterns_compound.csv): rank 934/1729 (rank_frac 0.5401966454598034) | score 12.5 (top 127.0, ratio 0.0984251968503937, delta 114.5) | section Midday, col1_hits 0, hot2 0, set_chain 2, draw_chain 0 | why set_chain2
- Families (patterns_families.csv): count 44 | rank 528/1532 (rank_frac 0.34464751958224543) | score 19.0 (top 38.0, ratio 0.5, delta 19.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=19

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 004 | section Combined | score 102.0 | col1_hits 9 | hot2 11
- rank    1 | canon 003 | section Combined | score 127.0 | col1_hits 8 | hot2 11
- rank    5 | canon 0034 | section Combined | score 86.5 | col1_hits 7 | hot2 11
- rank    4 | canon 005 | section Evening | score 92.5 | col1_hits 9 | hot2 11
- rank    5 | canon 055 | section Evening | score 86.5 | col1_hits 8 | hot2 11
- rank    8 | canon 0055 | section Evening | score 79.5 | col1_hits 8 | hot2 11
- rank    2 | canon 224 | section Midday | score 108.5 | col1_hits 7 | hot2 9
- rank   15 | canon 004 | section Midday | score 73.0 | col1_hits 5 | hot2 9
- rank   36 | canon 0029 | section Midday | score 54.5 | col1_hits 5 | hot2 8
- rank   30 | canon 0039 | section Midday | score 57.0 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1523 | family 11 | score 4.0 | hot2 0 | section Midday
- rank  378 | family 14 | score 21.0 | hot2 0 | section Midday
- rank  142 | family 5 | score 26.0 | hot2 0 | section Midday
- rank   17 | family 28 | score 34.5 | hot2 0 | section Midday
- rank 1087 | family 34 | score 12.5 | hot2 1 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 867 (canon 678): exact_boxed=True exact_straight=True | rank 4908/5852 (rank_frac 0.839); Evening 057 (canon 057): exact_boxed=True exact_straight=True | rank 4674/5852 (rank_frac 0.799)
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

### 2.Digit Reduction — NorthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260105)

## Midday winner 867 (canonical 678)
- Stamp (winner_stamp.json): items_total=134 | exact_any=24 exact_final=0 | vtrac_any=126 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=93 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=6 family_vtrac_final=0
- Flags (winner_flags.csv): rows=134 | exact_any=24 vtrac_any=126 | drop_exact_any=0 drop_vtrac_any=93 | family_exact_any=0 family_vtrac_any=6 | vt_boxed=122 vt_straight=0
- Hits (winner_hits.csv): rows=134 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=122 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 057 (canonical 057)
- Stamp (winner_stamp.json): items_total=143 | exact_any=0 exact_final=0 | vtrac_any=123 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=138 drop_vtrac_final=0 | family_exact_any=6 family_exact_final=0 | family_vtrac_any=106 family_vtrac_final=0
- Flags (winner_flags.csv): rows=143 | exact_any=0 vtrac_any=123 | drop_exact_any=0 drop_vtrac_any=138 | family_exact_any=6 family_vtrac_any=106 | vt_boxed=45 vt_straight=0
- Hits (winner_hits.csv): rows=143 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=45 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 867 (canonical 678)
- Stamp (winner_stamp.json): items_total=248 | exact_any=60 exact_final=0 | vtrac_any=240 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=97 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=248 | exact_any=60 vtrac_any=240 | drop_exact_any=0 drop_vtrac_any=97 | family_exact_any=0 family_vtrac_any=12 | vt_boxed=132 vt_straight=0
- Hits (winner_hits.csv): rows=248 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=132 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.487143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 550 | score_v2 14.127143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 5 | pattern 550 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 550 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 550 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 550 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 550 | score_v2 13.627143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 554 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw2 col 5 | pattern 550 | score_v2 13.327143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 554 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 554 | score_v2 13.127143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 550 | score_v2 14.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 554 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 552 | score_v2 13.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 522 | score_v2 12.487143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 922 | score_v2 12.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 550 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 922 | score_v2 11.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 552 | score_v2 11.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 522 | score_v2 11.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 992 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 867 (canon 678): items_total=134 exact_any=24 vtrac_any=126 | top winner_present=False best_rank=None/12; Evening 057 (canon 057): items_total=143 exact_any=0 vtrac_any=123 | top winner_present=False best_rank=None/14; Combined 867 (canon 678): items_total=248 exact_any=60 vtrac_any=240 | top winner_present=False best_rank=None/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 550, 554, 552, 522, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260105_053048)

## Top indices (from enhanced JSON)
- index 4 | score 66.29406999999998 | features: presence=45.24656999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 59.73324999999996 | features: presence=38.90574999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 48.07249500000001 | features: presence=30.54499500000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 37.1737 | features: presence=19.956199999999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 37.17083 | features: presence=25.843330000000005, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 10 | score 35.8662 | features: presence=23.198700000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 33.53075 | features: presence=23.12325, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 26.5246 | features: presence=12.537099999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 3 | score 24.206400000000002 | features: presence=16.178900000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 21.020965000000004 | features: presence=13.953465000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
034, 240, 290, 064, 092, 093, 204, 403, 406, 709

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 867 | index 21 | file NorthCarolina4_vtrac21_winner_867_20260105_052157.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 057 | index 3 | file NorthCarolina4_vtrac3_winner_057_20260105_052159.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 867 | index 21 rank 24/35 (rank_frac 0.6857142857142857) | score 3.8764583333333333 (top 66.29406999999998, ratio 0.05847368148211951, delta 62.417611666666645) | winner_in_index_straights=False | top_index_straights: 367 (1.607), 132 (0.65), 362 (0.55)
- winner 057 | index 3 rank 9/35 (rank_frac 0.2571428571428571) | score 24.206400000000002 (top 66.29406999999998, ratio 0.3651367309323445, delta 42.087669999999974) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 867→idx21 rank 24/35 (frac 0.686); 057→idx3 rank 9/35 (frac 0.257).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 4, 28, 14, 12, 2.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2025-12-31)

## Midday winner 867 (canonical 678)
- Top lanes (hot_zones_top_lanes.csv): present | rank 181/202 (rank_frac 0.8960396039603961) | score_mean 15.044 (top 22.24, ratio 0.6764388489208634, delta 7.195999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 057 (canonical 057)
- Top lanes (hot_zones_top_lanes.csv): present | rank 102/202 (rank_frac 0.504950495049505) | score_mean 16.893 (top 22.24, ratio 0.7595773381294965, delta 5.346999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 667 | vt_triad 23 | score_mean 22.24 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_straight
- rank    2 | triad 168 | vt_triad 224 | score_mean 22.196 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 119 | vt_triad 25 | score_mean 21.602 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vertical5,vt_straight
- rank    4 | triad 469 | vt_triad 255 | score_mean 20.79 | tags hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 005 | vt_triad 11 | score_mean 20.377 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 011 | vt_triad 12 | score_mean 20.141 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 006 | vt_triad 12 | score_mean 19.801 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 224 | vt_triad 35 | score_mean 19.788 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank    9 | triad 367 | vt_triad 234 | score_mean 19.718 | tags col1,hot12,hot16,hot20,hot4,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank   10 | triad 226 | vt_triad 23 | score_mean 19.702 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 867 (canon 678): rank 181/202 (rank_frac 0.896) ratio_to_top=0.6764388489208634; Evening 057 (canon 057): rank 102/202 (rank_frac 0.505) ratio_to_top=0.7595773381294965
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

Aux draws snapshot dir: `sharepacks/2025-12-31/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=879, 455, 168, 766, 911
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=455, 766, 885, 789, 157
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=879, 168, 911, 391, 226

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=23 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=40), P2:4 (gap=29), P3:2 (gap=26)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=884 sev=B
- 155: ds=872 sev=B
- 446: ds=868 sev=B
- 445: ds=808 sev=B
- 122: ds=791 sev=B
- 036: ds=787 sev=B
- 555: ds=764 sev=B
- 299: ds=761 sev=B
- 277: ds=753 sev=B
- 112: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=148 sev=red
  - 77: ds=121 sev=red
  - 33: ds=45 sev=purple
  - 99: ds=44 sev=purple
  - 44: ds=42 sev=purple
  - 22: ds=8 sev=-
  - 88: ds=5 sev=-
  - 11: ds=4 sev=-
  - 66: ds=3 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 56: ds=50 sev=blue
  - 27: ds=46 sev=blue
  - 02: ds=40 sev=blue
  - 23: ds=36 sev=purple
  - 09: ds=35 sev=purple
  - 03: ds=34 sev=purple
  - 28: ds=32 sev=purple
  - 04: ds=29 sev=purple
  - 06: ds=29 sev=purple
  - 34: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:476, 32:329, 1:103, 27:99, 31:90, 15:74, 16:72, 10:62, 4:52, 23:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=476 fs=3 fl=0 hz=0.009389671361502348, 32:ds=329 fs=1 fl=1 hz=0.005405405405405406, 1:ds=103 fs=0 fl=3 hz=0.00625, 27:ds=99 fs=15 fl=2 hz=0.02011173184357542, 31:ds=90 fs=19 fl=3 hz=0.02502844141069397, 15:ds=74 fs=16 fl=2 hz=0.019758507135016465, 16:ds=72 fs=4 fl=1 hz=0.008836524300441826, 10:ds=62 fs=21 fl=2 hz=0.027315914489311165, 4:ds=52 fs=18 fl=2 hz=0.0213903743315508, 23:ds=51 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=84 flags=purple
- S23: ds=68 flags=blue+purple
- S4: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=2 last_repeat_gap=94 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=33), P2:9 (gap=23), P3:2 (gap=36)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=971 sev=B
- 123: ds=946 sev=B
- 446: ds=923 sev=B
- 777: ds=883 sev=B
- 119: ds=848 sev=B
- 222: ds=818 sev=B
- 155: ds=780 sev=B
- 488: ds=774 sev=B
- 177: ds=750 sev=B
- 007: ds=729 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=153 sev=red
  - 00: ds=128 sev=red
  - 77: ds=60 sev=purple
  - 99: ds=48 sev=purple
  - 22: ds=36 sev=purple
  - 33: ds=22 sev=-
  - 11: ds=6 sev=-
  - 88: ds=2 sev=-
  - 66: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 48: ds=144 sev=red
  - 68: ds=72 sev=red
  - 25: ds=57 sev=red
  - 07: ds=52 sev=blue
  - 28: ds=44 sev=blue
  - 23: ds=39 sev=blue
  - 26: ds=39 sev=blue
  - 02: ds=36 sev=purple
  - 29: ds=33 sev=purple
  - 56: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:376, 25:184, 32:164, 35:138, 4:128, 11:103, 31:96, 2:92, 33:75, 12:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=376 fs=1 fl=0 hz=0.005905511811023622, 25:ds=184 fs=15 fl=1 hz=0.02165087956698241, 32:ds=164 fs=3 fl=1 hz=0.007416563658838071, 35:ds=138 fs=0 fl=2 hz=0.005201560468140442, 4:ds=128 fs=12 fl=3 hz=0.017241379310344827, 11:ds=103 fs=50 fl=0 hz=0.056882821387940846, 31:ds=96 fs=25 fl=0 hz=0.02793296089385475, 2:ds=92 fs=13 fl=3 hz=0.018223234624145785, 33:ds=75 fs=21 fl=2 hz=0.025136612021857924, 12:ds=53 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=87 flags=purple
- S20: ds=75 flags=red+purple
- S2: ds=66 flags=purple
- S5: ds=62 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 1}}
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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=18 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=20), P2:4 (gap=33), P3:3 (gap=25)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=972 sev=B
- 299: ds=929 sev=B
- 223: ds=859 sev=B
- 122: ds=848 sev=B
- 116: ds=825 sev=B
- 039: ds=808 sev=B
- 377: ds=796 sev=B
- 277: ds=782 sev=B
- 188: ds=770 sev=B
- 557: ds=769 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=177 sev=red
  - 55: ds=120 sev=red
  - 33: ds=119 sev=red
  - 77: ds=78 sev=blue
  - 00: ds=74 sev=blue
  - 66: ds=36 sev=purple
  - 99: ds=22 sev=-
  - 44: ds=21 sev=-
  - 22: ds=4 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 45: ds=97 sev=red
  - 34: ds=38 sev=blue
  - 59: ds=37 sev=blue
  - 04: ds=33 sev=purple
  - 06: ds=27 sev=purple
  - 08: ds=26 sev=purple
  - 58: ds=26 sev=purple
  - 56: ds=25 sev=purple
  - 17: ds=23 sev=-
  - 27: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:256, 26:238, 13:203, 32:177, 1:145, 23:114, 5:95, 17:94, 27:51, 31:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=256 fs=18 fl=0 hz=0.024896265560165977, 26:ds=238 fs=1 fl=2 hz=0.006666666666666667, 13:ds=203 fs=20 fl=0 hz=0.025284450063211127, 32:ds=177 fs=2 fl=2 hz=0.007416563658838071, 1:ds=145 fs=2 fl=3 hz=0.007434944237918215, 23:ds=114 fs=14 fl=3 hz=0.019384264538198404, 5:ds=95 fs=15 fl=2 hz=0.020809248554913295, 17:ds=94 fs=29 fl=0 hz=0.03553921568627451, 27:ds=51 fs=22 fl=3 hz=0.027085590465872156, 31:ds=45 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=88 flags=purple
- S0: ds=74 flags=blue+purple
- S4: ds=63 flags=blue+purple
- S22: ds=43 flags=purple
- S2: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 034: score=4 tags=FLT,PAT,RS
  - 124: score=4 tags=FLT,PAT,RS
  - 016: score=3 tags=FLT,RS
  - 025: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 349: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 012: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:787(B); evening:722(B)
- 122 -> combined:791(B); evening:848(B)
- 155 -> combined:872(B); midday:780(B)
- 277 -> combined:753(B); evening:782(B)
- 299 -> combined:761(B); evening:929(B)
- 338 -> combined:884(B); midday:709(B)
- 446 -> combined:868(B); midday:923(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:148(red); evening:74(blue); midday:128(red)
- 02 -> combined:40(blue); midday:36(purple)
- 04 -> combined:29(purple); evening:33(purple)
- 06 -> combined:29(purple); evening:27(purple)
- 23 -> combined:36(purple); midday:39(blue)
- 28 -> combined:32(purple); midday:44(blue)
- 29 -> combined:26(purple); midday:33(purple)
- 33 -> combined:45(purple); evening:119(red)
- 34 -> combined:27(purple); evening:38(blue)
- 44 -> combined:42(purple); midday:153(red)
- 56 -> combined:50(blue); evening:25(purple); midday:27(purple)
- 77 -> combined:121(red); evening:78(blue); midday:60(purple)
- 99 -> combined:44(purple); midday:48(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.531842857142857)[R1,Mirror-Echo], 5(4.220228571428572)[R2,Mirror-Echo], 2(1.5852857142857142)[R1,Double-Pressure], 3(0.39558571428571426)[R3,Swap], 7(0.19092142857142858)[R3,Swap]
- P2: 4(8.201457142857143)[R1,XVAR-Cons(CEM)], 0(3.7224714285714287)[R2,XVAR-Cons(CE)], 9(1.4197142857142857)[R1,Mirror-Echo], 5(0.4813571428571428)[R3,Mirror-Echo], 3(0.35457142857142854)[R3,Swap]
- P3: 2(7.336807142857143)[R1,XVAR-Cons(CEM)], 3(2.902)[R3,XVAR-Cons(CE)], 0(2.7281)[R2,XVAR-Cons(CM)], 8(1.0671)[R2,Double-Pressure], 5(1.0461999999999998)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=40), P2:4(gap=29), P3:2(gap=26); top cartesian candidates: 042, 040, 542, 043, 002.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 023, 024.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:787(B),evening:722(B); 122→combined:791(B),evening:848(B); 155→combined:872(B),midday:780(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:476, 32:329, 1:103, 27:99, 31:90.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=867 Evening=057; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 678 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 057 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 867 (canon 678): box `678` covers winner `867` (boxed hit).
  - Evening winner 057 (canon 057): box `057` covers winner `057` (boxed hit).
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
