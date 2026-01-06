# Master Validation Run Report — Pennsylvania4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/Pennsylvania4/`
- Winners lens: `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2025-12-30/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2025-12-30/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2025-12-30/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2025-12-30/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2025-12-30/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2025-12-30/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_186_20260105_051212.html`
- `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_173_20260105_051212.html`

Winners JSON files:
- `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac18_winner_186_20260105_051212.json`
- `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_173_20260105_051212.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 186 (canon 168): exact_boxed=True exact_straight=True | rank 1131/5664 (rank_frac 0.200); Evening 173 (canon 137): exact_boxed=True exact_straight=True | rank 1987/5664 (rank_frac 0.351)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 186 idx18 (rank 4/35, frac 0.114), 173 idx21 (rank 6/35, frac 0.171)
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

### 2.Stable — Pennsylvania4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2025-12-30)

## Midday winner 186 (canonical 168)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=21 | family_rows=332 | exact_boxed=21 | exact_straight=21 | vt_boxed=21
- Scores (patterns_scores.csv): rank 1131/5664 (rank_frac 0.1996822033898305) | score 18.0 (top 42.0, ratio 0.42857142857142855, delta 24.0) | section Evening, Set Set1, Draw Draw3, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat4|mirror|hot2|vtrac_straight|draw_chain5
- Compound (patterns_compound.csv): rank 115/1679 (rank_frac 0.0684931506849315) | score 31.5 (top 104.5, ratio 0.3014354066985646, delta 73.0) | section Evening, col1_hits 0, hot2 3, set_chain 1, draw_chain 5 | why draw_chain5|hot1x2|hot2x3|vstrx6
- Families (patterns_families.csv): count 79 | rank 6/1395 (rank_frac 0.004301075268817204) | score 35.0 (top 36.5, ratio 0.958904109589041, delta 1.5) | section Evening, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=25

## Evening winner 173 (canonical 137)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=15 | family_rows=916 | exact_boxed=15 | exact_straight=9 | vt_boxed=15
- Scores (patterns_scores.csv): rank 1987/5664 (rank_frac 0.3508121468926554) | score 15.0 (top 42.0, ratio 0.35714285714285715, delta 27.0) | section Evening, Set Set1, Draw Draw3, Col 1, hot 2, vt_straight 0.0 | why boxed|cov2|hp_repeat4|hot2|perm2|draw_chain2
- Compound (patterns_compound.csv): rank 146/1679 (rank_frac 0.08695652173913043) | score 28.5 (top 104.5, ratio 0.2727272727272727, delta 76.0) | section Evening, col1_hits 2, hot2 4, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|hot2x4|vstrx3
- Families (patterns_families.csv): count 91 | rank 22/1395 (rank_frac 0.015770609318996417) | score 32.0 (top 36.5, ratio 0.8767123287671232, delta 4.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=130

## Top compound candidates (patterns_compound.csv)
- rank    4 | canon 1133 | section Evening | score 97.5 | col1_hits 9 | hot2 11
- rank    5 | canon 138 | section Combined | score 83.0 | col1_hits 9 | hot2 11
- rank    1 | canon 133 | section Evening | score 104.5 | col1_hits 9 | hot2 11
- rank    1 | canon 113 | section Evening | score 104.5 | col1_hits 9 | hot2 11
- rank    7 | canon 177 | section Combined | score 75.0 | col1_hits 7 | hot2 11
- rank   13 | canon 778 | section Combined | score 70.0 | col1_hits 5 | hot2 10
- rank   19 | canon 1377 | section Combined | score 63.5 | col1_hits 7 | hot2 10
- rank   22 | canon 3778 | section Combined | score 61.5 | col1_hits 7 | hot2 10
- rank   12 | canon 378 | section Combined | score 70.5 | col1_hits 8 | hot2 10
- rank   10 | canon 13778 | section Combined | score 72.5 | col1_hits 7 | hot2 10

## Top families (patterns_families.csv)
- rank 1330 | family 11 | score 6.0 | hot2 0 | section Midday
- rank 1109 | family 8 | score 10.0 | hot2 0 | section Midday
- rank 1366 | family 12 | score 5.0 | hot2 0 | section Midday
- rank  279 | family 33 | score 23.5 | hot2 0 | section Midday
- rank  279 | family 23 | score 23.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 186 (canon 168): exact_boxed=True exact_straight=True | rank 1131/5664 (rank_frac 0.200); Evening 173 (canon 137): exact_boxed=True exact_straight=True | rank 1987/5664 (rank_frac 0.351)
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

### 2.Digit Reduction — Pennsylvania4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260105)

## Midday winner 186 (canonical 168)
- Stamp (winner_stamp.json): items_total=143 | exact_any=10 exact_final=0 | vtrac_any=138 vtrac_final=0 | drop_exact_any=15 drop_exact_final=0 | drop_vtrac_any=38 drop_vtrac_final=0 | family_exact_any=6 family_exact_final=0 | family_vtrac_any=13 family_vtrac_final=0
- Flags (winner_flags.csv): rows=143 | exact_any=10 vtrac_any=138 | drop_exact_any=15 drop_vtrac_any=38 | family_exact_any=6 family_vtrac_any=13 | vt_boxed=40 vt_straight=0
- Hits (winner_hits.csv): rows=143 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=40 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 173 (canonical 137)
- Stamp (winner_stamp.json): items_total=208 | exact_any=0 exact_final=0 | vtrac_any=157 vtrac_final=0 | drop_exact_any=4 drop_exact_final=0 | drop_vtrac_any=119 drop_vtrac_final=0 | family_exact_any=20 family_exact_final=0 | family_vtrac_any=37 family_vtrac_final=0
- Flags (winner_flags.csv): rows=208 | exact_any=0 vtrac_any=157 | drop_exact_any=4 drop_vtrac_any=119 | family_exact_any=20 family_vtrac_any=37 | vt_boxed=124 vt_straight=0
- Hits (winner_hits.csv): rows=208 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=124 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 186 (canonical 168)
- Stamp (winner_stamp.json): items_total=695 | exact_any=10 exact_final=0 | vtrac_any=690 vtrac_final=59 | drop_exact_any=16 drop_exact_final=0 | drop_vtrac_any=332 drop_vtrac_final=57 | family_exact_any=7 family_exact_final=0 | family_vtrac_any=224 family_vtrac_final=59
- Flags (winner_flags.csv): rows=695 | exact_any=10 vtrac_any=690 | drop_exact_any=16 drop_vtrac_any=332 | family_exact_any=7 family_vtrac_any=224 | vt_boxed=214 vt_straight=59
- Hits (winner_hits.csv): rows=695 | exact_final=0 vtrac_final=59 | drop_exact_final=0 drop_vtrac_final=57 | family_exact_final=0 family_vtrac_final=59 | vt_boxed=214 vt_straight=59
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=42 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.008571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 113 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 133 | score_v2 11.008571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 133 | score_v2 10.937143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 113 | score_v2 10.437143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 133 | score_v2 10.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 133 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 133 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 133 | score_v2 10.208571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 113 | score_v2 10.187143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 113 | score_v2 10.158571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 113 | score_v2 13.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 133 | score_v2 11.008571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 113 | score_v2 10.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 133 | score_v2 10.208571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 933 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 933 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 113 | score_v2 9.637143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 138 | score_v2 9.597143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 511 | score_v2 9.558571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 991 | score_v2 9.447143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 186 (canon 168): items_total=143 exact_any=10 vtrac_any=138 | top winner_present=False best_rank=None/22; Evening 173 (canon 137): items_total=208 exact_any=0 vtrac_any=157 | top winner_present=False best_rank=None/28; Combined 186 (canon 168): items_total=695 exact_any=10 vtrac_any=690 | top winner_present=False best_rank=None/42
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 113, 133, 113, 133, 933.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_051505)

## Top indices (from enhanced JSON)
- index 23 | score 93.96185999999999 | features: presence=66.75435999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 62.93918999999999 | features: presence=41.191689999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 58.970999999999975 | features: presence=36.76349999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 55.59864999999998 | features: presence=38.061149999999984, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 32 | score 41.9352875 | features: presence=30.207787500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 33.33734 | features: presence=23.04984, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 27 | score 30.099800000000002 | features: presence=20.0023, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 13 | score 25.719829999999998 | features: presence=13.172329999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 20 | score 24.1259 | features: presence=17.5684, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 6 | score 22.008250000000004 | features: presence=13.860750000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
183, 138, 387, 813, 793, 817, 837, 718, 983, 371

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 186 | index 18 | file Pennsylvania4_vtrac18_winner_186_20260105_051212.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 173 | index 21 | file Pennsylvania4_vtrac21_winner_173_20260105_051212.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 186 | index 18 rank 4/35 (rank_frac 0.11428571428571428) | score 55.59864999999998 (top 93.96185999999999, ratio 0.5917150852484188, delta 38.36321000000001) | winner_in_index_straights=False | top_index_straights: (none)
- winner 173 | index 21 rank 6/35 (rank_frac 0.17142857142857143) | score 33.33734 (top 93.96185999999999, ratio 0.3547965099882016, delta 60.62451999999999) | winner_in_index_straights=True | top_index_straights: 817 (14.848), 718 (13.719), 371 (9.778)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 186→idx18 rank 4/35 (frac 0.114); 173→idx21 rank 6/35 (frac 0.171).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 29, 33, 18, 32.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2025-12-30)

## Midday winner 186 (canonical 168)
- Top lanes (hot_zones_top_lanes.csv): present | rank 75/201 (rank_frac 0.373134328358209) | score_mean 17.471 (top 24.557, ratio 0.7114468379688073, delta 7.0859999999999985)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 173 (canonical 137)
- Top lanes (hot_zones_top_lanes.csv): present | rank 107/201 (rank_frac 0.5323383084577115) | score_mean 16.848 (top 24.557, ratio 0.6860772895712017, delta 7.709)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 24.557 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vt_straight
- rank    2 | triad 239 | vt_triad 345 | score_mean 22.056 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 056 | vt_triad 112 | score_mean 21.126 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 046 | vt_triad 125 | score_mean 21.123 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 025 | vt_triad 113 | score_mean 21.1 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 156 | vt_triad 122 | score_mean 20.682 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 016 | vt_triad 122 | score_mean 20.682 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 011 | vt_triad 12 | score_mean 19.916 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 133 | vt_triad 24 | score_mean 19.897 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 145 | vt_triad 125 | score_mean 19.7 | tags funnel_precol1,hot12,hot16,hot20,hot4,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 186 (canon 168): rank 75/201 (rank_frac 0.373) ratio_to_top=0.7114468379688073; Evening 173 (canon 137): rank 107/201 (rank_frac 0.532) ratio_to_top=0.6860772895712017
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

Aux draws snapshot dir: `sharepacks/2025-12-30/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=460, 239, 422, 502, 065
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=239, 502, 264, 014, 267
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=460, 422, 065, 994, 598

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=17 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=29), P2:4 (gap=22), P3:1 (gap=47)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=990 sev=B
- 666: ds=988 sev=B
- 159: ds=876 sev=B
- 007: ds=873 sev=B
- 088: ds=837 sev=B
- 008: ds=815 sev=B
- 444: ds=791 sev=B
- 039: ds=766 sev=B
- 355: ds=756 sev=B
- 344: ds=685 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=133 sev=red
  - 77: ds=72 sev=blue
  - 88: ds=71 sev=blue
  - 44: ds=65 sev=purple
  - 66: ds=59 sev=purple
  - 55: ds=36 sev=purple
  - 11: ds=21 sev=-
  - 00: ds=19 sev=-
  - 99: ds=6 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 78: ds=66 sev=red
  - 13: ds=45 sev=blue
  - 12: ds=44 sev=blue
  - 16: ds=44 sev=blue
  - 03: ds=41 sev=blue
  - 07: ds=39 sev=blue
  - 35: ds=32 sev=purple
  - 69: ds=30 sev=purple
  - 37: ds=29 sev=purple
  - 36: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:275, 26:232, 18:201, 16:90, 27:66, 7:58, 21:57, 24:55, 6:53, 13:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=275 fs=2 fl=1 hz=0.007380073800738007, 26:ds=232 fs=0 fl=1 hz=0.003898635477582846, 18:ds=201 fs=26 fl=1 hz=0.03426395939086294, 16:ds=90 fs=3 fl=2 hz=0.007371007371007371, 27:ds=66 fs=11 fl=4 hz=0.01722158438576349, 7:ds=58 fs=36 fl=1 hz=0.03965702036441586, 21:ds=57 fs=58 fl=0 hz=0.061899679829242264, 24:ds=55 fs=44 fl=0 hz=0.048245614035087724, 6:ds=53 fs=23 fl=1 hz=0.025396825396825397, 13:ds=51 fs=21 fl=1 hz=0.024553571428571428

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=84 flags=purple
- S20: ds=71 flags=purple
- S6: ds=50 flags=purple
- S25: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=30 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:7 (gap=19), P3:6 (gap=29)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=974 sev=B
- 288: ds=961 sev=B
- 255: ds=932 sev=B
- 668: ds=914 sev=B
- 199: ds=862 sev=B
- 499: ds=788 sev=B
- 399: ds=771 sev=B
- 039: ds=759 sev=B
- 448: ds=748 sev=B
- 005: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=183 sev=red
  - 99: ds=130 sev=red
  - 77: ds=73 sev=blue
  - 33: ds=66 sev=purple
  - 22: ds=59 sev=purple
  - 88: ds=35 sev=purple
  - 44: ds=32 sev=purple
  - 66: ds=29 sev=purple
  - 11: ds=10 sev=-
  - 00: ds=9 sev=-
- non_repeating:
  - 59: ds=76 sev=red
  - 79: ds=70 sev=red
  - 12: ds=45 sev=blue
  - 78: ds=43 sev=blue
  - 06: ds=40 sev=blue
  - 35: ds=37 sev=blue
  - 56: ds=29 sev=purple
  - 69: ds=27 sev=purple
  - 16: ds=23 sev=-
  - 13: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:372, 1:357, 34:211, 16:169, 15:160, 32:137, 35:114, 18:100, 27:81, 28:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=372 fs=0 fl=0 hz=0.0, 1:ds=357 fs=2 fl=2 hz=0.009124087591240877, 34:ds=211 fs=19 fl=1 hz=0.02631578947368421, 16:ds=169 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=160 fs=23 fl=0 hz=0.029411764705882353, 32:ds=137 fs=3 fl=1 hz=0.006720430107526881, 35:ds=114 fs=1 fl=1 hz=0.0035587188612099642, 18:ds=100 fs=28 fl=0 hz=0.0343980343980344, 27:ds=81 fs=22 fl=2 hz=0.028605482717520857, 28:ds=59 fs=26 fl=2 hz=0.02997858672376874

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=91 flags=red+purple
- S22: ds=76 flags=purple
- S23: ds=64 flags=purple
- S3: ds=58 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 568: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 589: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 689: score=2 tags=FLT,PAT
  - 789: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 018: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=60 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=26), P2:1 (gap=32), P3:1 (gap=25)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=970 sev=B
- 009: ds=928 sev=B
- 255: ds=886 sev=B
- 138: ds=826 sev=B
- 117: ds=809 sev=B
- 158: ds=771 sev=B
- 344: ds=764 sev=B
- 199: ds=755 sev=B
- 112: ds=715 sev=B
- 277: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=125 sev=red
  - 33: ds=67 sev=purple
  - 44: ds=38 sev=purple
  - 77: ds=36 sev=purple
  - 66: ds=34 sev=purple
  - 11: ds=25 sev=purple
  - 55: ds=18 sev=-
  - 00: ds=12 sev=-
  - 99: ds=3 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 68: ds=83 sev=red
  - 13: ds=61 sev=red
  - 07: ds=60 sev=red
  - 37: ds=55 sev=blue
  - 17: ds=50 sev=blue
  - 15: ds=48 sev=blue
  - 38: ds=47 sev=blue
  - 23: ds=44 sev=blue
  - 03: ds=42 sev=blue
  - 78: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:614, 23:153, 26:116, 18:113, 21:83, 13:62, 29:55, 33:47, 16:45, 30:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=614 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=153 fs=17 fl=2 hz=0.025165562913907286, 26:ds=116 fs=2 fl=1 hz=0.0056657223796034, 18:ds=113 fs=23 fl=2 hz=0.02910360884749709, 21:ds=83 fs=54 fl=0 hz=0.059275521405049394, 13:ds=62 fs=20 fl=1 hz=0.024881516587677725, 29:ds=55 fs=16 fl=3 hz=0.020540540540540542, 33:ds=47 fs=19 fl=3 hz=0.023255813953488372, 16:ds=45 fs=5 fl=3 hz=0.009523809523809525, 30:ds=44 fs=36 fl=1 hz=0.0387434554973822

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=86 flags=blue+purple
- S1: ds=71 flags=blue+purple
- S5: ds=68 flags=purple
- S24: ds=54 flags=blue+purple
- S3: ds=42 flags=purple
- S20: ds=36 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '7'], 'pairs': {'remaining_count': 0}}
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
  - 027: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:766(B); midday:759(B)
- 066 -> combined:990(B); midday:737(B)
- 199 -> evening:755(B); midday:862(B)
- 255 -> evening:886(B); midday:932(B)
- 344 -> combined:685(B); evening:764(B)
- 444 -> combined:791(B); evening:970(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:41(blue); evening:42(blue)
- 07 -> combined:39(blue); evening:60(red)
- 12 -> combined:44(blue); midday:45(blue)
- 13 -> combined:45(blue); evening:61(red)
- 33 -> combined:133(red); evening:67(purple); midday:66(purple)
- 35 -> combined:32(purple); midday:37(blue)
- 37 -> combined:29(purple); evening:55(blue)
- 38 -> combined:25(purple); evening:47(blue)
- 44 -> combined:65(purple); evening:38(purple); midday:32(purple)
- 55 -> combined:36(purple); midday:183(red)
- 66 -> combined:59(purple); evening:34(purple); midday:29(purple)
- 68 -> combined:27(purple); evening:83(red)
- 69 -> combined:30(purple); midday:27(purple)
- 77 -> combined:72(blue); evening:36(purple); midday:73(blue)
- 78 -> combined:66(red); evening:33(purple); midday:43(blue)
- 88 -> combined:71(blue); evening:125(red); midday:35(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(6.671100000000001)[R1,Mirror-Echo], 8(4.432714285714286)[R2,Mirror-Echo], 7(3.0994285714285716)[R3,XVAR-Cons(CM)], 4(1.0971)[R2,Double-Pressure], 1(1.0597999999999999)[R2,Double-Pressure]
- P2: 7(3.0172857142857143)[R3,XVAR-Cons(CM)], 4(2.8795285714285717)[R1,XVAR-Cons(CM)], 5(2.6046642857142857)[R2,XVAR-Cons(CE)], 1(1.6554285714285715)[R1,Double-Pressure], 2(1.2622571428571427)[R2,Mirror-Echo]
- P3: 1(8.15245)[R1,Mirror-Echo], 6(7.153149999999999)[R3,Mirror-Echo], 3(3.8507)[R2,XVAR-Cons(CE)], 5(1.2016)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:3(gap=29), P2:4(gap=22), P3:1(gap=47); top cartesian candidates: 371, 376, 341, 351, 346.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '7', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:766(B),midday:759(B); 066→combined:990(B),midday:737(B); 199→midday:862(B),evening:755(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:275, 26:232, 18:201, 16:90, 27:66.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=186 Evening=173; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 168 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 137 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 186 (canon 168): box `168` covers winner `186` (boxed hit).
  - Evening winner 173 (canon 137): box `137` covers winner `173` (boxed hit).
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
