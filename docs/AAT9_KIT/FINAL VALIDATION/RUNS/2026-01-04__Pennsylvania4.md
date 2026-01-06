# Master Validation Run Report — Pennsylvania4 — results 2026-01-04 (history workbook ~ 2026-01-03)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-04/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-04/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-04/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-04/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-04/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-04/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-04/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac14_winner_359_20260105_055150.html`
- `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac14_winner_980_20260105_055152.html`

Winners JSON files:
- `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac14_winner_359_20260105_055150.json`
- `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac14_winner_980_20260105_055152.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-04/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 359 (canon 359): exact_boxed=None exact_straight=None | rank 108/5396 (rank_frac 0.020); Evening 980 (canon 089): exact_boxed=None exact_straight=None | rank 1361/5396 (rank_frac 0.252)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 359 idx14 (rank 13/35, frac 0.371), 980 idx14 (rank 13/35, frac 0.371)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — Pennsylvania4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-04)

## Midday winner 359 (canonical 359)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=350 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 108/5396 (rank_frac 0.02001482579688658) | score 29.0 (top 38.5, ratio 0.7532467532467533, delta 9.5) | section Midday, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 0.0 | why boxed|cov4|hp_repeat3|vstr2|vstr3|hot2|perm2|set_chain3|draw_chain5
- Compound (patterns_compound.csv): rank 26/1824 (rank_frac 0.01425438596491228) | score 47.5 (top 106.5, ratio 0.4460093896713615, delta 59.0) | section Midday, col1_hits 0, hot2 1, set_chain 3, draw_chain 5 | why set_chain3|draw_chain5|hot1x9|hot2x1|vstrx2
- Families (patterns_families.csv): count 62 | rank 21/1310 (rank_frac 0.01603053435114504) | score 33.5 (top 38.5, ratio 0.8701298701298701, delta 5.0) | section Combined, hot2 9
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Evening winner 980 (canonical 089)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=39 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 1361/5396 (rank_frac 0.2522238695329874) | score 16.0 (top 38.5, ratio 0.4155844155844156, delta 22.5) | section Combined, Set Set3, Draw Draw1, Col 5, hot 0, vt_straight 0.0 | why boxed|cov3|hp_repeat2|vstr2|perm2|set_chain3
- Compound (patterns_compound.csv): rank 358/1824 (rank_frac 0.1962719298245614) | score 20.5 (top 106.5, ratio 0.19248826291079812, delta 86.0) | section Combined, col1_hits 0, hot2 0, set_chain 3, draw_chain 1 | why set_chain3|draw_chain1
- Families (patterns_families.csv): count 25 | rank 169/1310 (rank_frac 0.12900763358778625) | score 22.5 (top 38.5, ratio 0.5844155844155844, delta 16.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 559 | section Combined | score 106.5 | col1_hits 9 | hot2 11
- rank    4 | canon 599 | section Combined | score 88.5 | col1_hits 7 | hot2 11
- rank    5 | canon 5599 | section Combined | score 81.5 | col1_hits 7 | hot2 11
- rank    2 | canon 055 | section Combined | score 100.0 | col1_hits 8 | hot2 10
- rank    3 | canon 0559 | section Combined | score 89.5 | col1_hits 8 | hot2 10
- rank    8 | canon 099 | section Combined | score 73.5 | col1_hits 6 | hot2 10
- rank    9 | canon 0599 | section Combined | score 69.5 | col1_hits 6 | hot2 10
- rank   12 | canon 05599 | section Combined | score 66.0 | col1_hits 6 | hot2 10
- rank    7 | canon 455 | section Combined | score 75.5 | col1_hits 6 | hot2 8
- rank    6 | canon 499 | section Combined | score 76.0 | col1_hits 5 | hot2 8

## Top families (patterns_families.csv)
- rank 1250 | family 35 | score 6.0 | hot2 0 | section Midday
- rank  861 | family 12 | score 12.0 | hot2 0 | section Midday
- rank  920 | family 24 | score 11.5 | hot2 0 | section Midday
- rank 1250 | family 11 | score 6.0 | hot2 0 | section Midday
- rank  212 | family 14 | score 21.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 359 (canon 359): exact_boxed=None exact_straight=None | rank 108/5396 (rank_frac 0.020); Evening 980 (canon 089): exact_boxed=None exact_straight=None | rank 1361/5396 (rank_frac 0.252)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260105)

## Midday winner 359 (canonical 359)
- Stamp (winner_stamp.json): items_total=107 | exact_any=63 exact_final=0 | vtrac_any=70 vtrac_final=0 | drop_exact_any=105 drop_exact_final=0 | drop_vtrac_any=105 drop_vtrac_final=0 | family_exact_any=12 family_exact_final=0 | family_vtrac_any=62 family_vtrac_final=0
- Flags (winner_flags.csv): rows=107 | exact_any=63 vtrac_any=70 | drop_exact_any=105 drop_vtrac_any=105 | family_exact_any=12 family_vtrac_any=62 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=107 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=True | winner_best_rank=12 | winner_rank_fraction=0.8571428571428571 | winner_score_v2=10.497143 top_score_v2=14.427143 | winner_score_ratio_to_top=0.727596794458889 winner_score_delta_from_top=3.9299999999999997
- Reducer scores present: True

## Evening winner 980 (canonical 089)
- Stamp (winner_stamp.json): items_total=78 | exact_any=12 exact_final=0 | vtrac_any=66 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=24 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=78 | exact_any=12 vtrac_any=66 | drop_exact_any=0 drop_vtrac_any=24 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=14 vt_straight=0
- Hits (winner_hits.csv): rows=78 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=14 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 359 (canonical 359)
- Stamp (winner_stamp.json): items_total=223 | exact_any=63 exact_final=0 | vtrac_any=174 vtrac_final=0 | drop_exact_any=117 drop_exact_final=0 | drop_vtrac_any=135 drop_vtrac_final=0 | family_exact_any=12 family_exact_final=0 | family_vtrac_any=65 family_vtrac_final=0
- Flags (winner_flags.csv): rows=223 | exact_any=63 vtrac_any=174 | drop_exact_any=117 drop_vtrac_any=135 | family_exact_any=12 family_vtrac_any=65 | vt_boxed=40 vt_straight=0
- Hits (winner_hits.csv): rows=223 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=40 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=4 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 15.077143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 552 | score_v2 14.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 552 | score_v2 14.677143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 559 | score_v2 14.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 559 | score_v2 14.127143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 13.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 559 | score_v2 13.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 12.927143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 552 | score_v2 15.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 559 | score_v2 14.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 12.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 559 | score_v2 12.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 554 | score_v2 12.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 599 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 552 | score_v2 11.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 11.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 559 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 590 | score_v2 11.047143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 359 (canon 359): items_total=107 exact_any=63 vtrac_any=70 | top winner_present=True best_rank=12/14; Evening 980 (canon 089): items_total=78 exact_any=12 vtrac_any=66 | top winner_present=False best_rank=None/30; Combined 359 (canon 359): items_total=223 exact_any=63 vtrac_any=174 | top winner_present=False best_rank=None/4
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 559, 559, 559, 554.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_055542)

## Top indices (from enhanced JSON)
- index 15 | score 100.83499499999999 | features: presence=73.68749499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 86.74643999999998 | features: presence=63.99893999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 49.040409999999994 | features: presence=29.212910000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 1 | score 26.97245 | features: presence=18.734949999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 35 | score 25.176862500000002 | features: presence=15.1893625, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 11 | score 24.399 | features: presence=16.581500000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 21.190262500000003 | features: presence=13.052762499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 16.192350000000005 | features: presence=8.354850000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 18 | score 16.177000000000003 | features: presence=6.949500000000003, set_echo=0.6, first_hit=0.2, column_span=0.0875
- index 30 | score 13.42975 | features: presence=5.072250000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
940, 059, 945, 597, 904, 095, 759, 795, 907, 587

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 359 | index 14 | file Pennsylvania4_vtrac14_winner_359_20260105_055150.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 980 | index 14 | file Pennsylvania4_vtrac14_winner_980_20260105_055152.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 359 | index 14 rank 13/35 (rank_frac 0.37142857142857144) | score 11.4807 (top 100.83499499999999, ratio 0.1138563055415434, delta 89.354295) | winner_in_index_straights=False | top_index_straights: 598 (5.146), 985 (3.721), 908 (2.575)
- winner 980 | index 14 rank 13/35 (rank_frac 0.37142857142857144) | score 11.4807 (top 100.83499499999999, ratio 0.1138563055415434, delta 89.354295) | winner_in_index_straights=False | top_index_straights: 598 (5.146), 985 (3.721), 908 (2.575)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 359→idx14 rank 13/35 (frac 0.371); 980→idx14 rank 13/35 (frac 0.371).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 15, 5, 12, 1, 35.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-04)

## Midday winner 359 (canonical 359)
- Top lanes (hot_zones_top_lanes.csv): present | rank 82/204 (rank_frac 0.4019607843137255) | score_mean 18.062 (top 21.653, ratio 0.8341569297556921, delta 3.5909999999999975)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 980 (canonical 089)
- Top lanes (hot_zones_top_lanes.csv): present | rank 167/204 (rank_frac 0.8186274509803921) | score_mean 16.415 (top 21.653, ratio 0.7580935667113102, delta 5.2379999999999995)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 224 | vt_triad 35 | score_mean 21.653 | tags funnel_precol1,hot16,hot20,literal_draw,ls2_lane,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 099 | vt_triad 15 | score_mean 21.49 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    3 | triad 447 | vt_triad 35 | score_mean 21.374 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    4 | triad 036 | vt_triad 124 | score_mean 21.234 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 599 | vt_triad 15 | score_mean 20.723 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    6 | triad 178 | vt_triad 234 | score_mean 20.601 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    7 | triad 055 | vt_triad 11 | score_mean 20.356 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 559 | vt_triad 15 | score_mean 20.35 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    9 | triad 117 | vt_triad 23 | score_mean 20.291 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank   10 | triad 033 | vt_triad 14 | score_mean 20.188 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 359 (canon 359): rank 82/204 (rank_frac 0.402) ratio_to_top=0.8341569297556921; Evening 980 (canon 089): rank 167/204 (rank_frac 0.819) ratio_to_top=0.7580935667113102
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

Aux draws snapshot dir: `sharepacks/2026-01-04/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=909, 744, 360, 871, 328
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=744, 871, 322, 684, 186
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=909, 360, 328, 221, 173

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=27 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=14), P2:5 (gap=25), P3:7 (gap=19)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=998 sev=B
- 159: ds=886 sev=B
- 007: ds=883 sev=B
- 088: ds=847 sev=B
- 008: ds=825 sev=B
- 444: ds=801 sev=B
- 039: ds=776 sev=B
- 355: ds=766 sev=B
- 344: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=143 sev=red
  - 77: ds=82 sev=blue
  - 88: ds=81 sev=blue
  - 66: ds=69 sev=purple
  - 55: ds=46 sev=purple
  - 11: ds=31 sev=purple
  - 00: ds=29 sev=purple
  - 22: ds=5 sev=-
  - 44: ds=1 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 07: ds=49 sev=blue
  - 35: ds=42 sev=blue
  - 69: ds=40 sev=blue
  - 34: ds=35 sev=purple
  - 19: ds=33 sev=purple
  - 15: ds=25 sev=purple
  - 45: ds=22 sev=-
  - 08: ds=21 sev=-
  - 57: ds=20 sev=-
  - 79: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:285, 26:242, 16:100, 7:68, 6:63, 13:61, 19:57, 10:52, 1:46, 11:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=285 fs=2 fl=1 hz=0.007380073800738007, 26:ds=242 fs=0 fl=1 hz=0.003898635477582846, 16:ds=100 fs=3 fl=2 hz=0.007371007371007371, 7:ds=68 fs=35 fl=1 hz=0.04, 6:ds=63 fs=21 fl=1 hz=0.025611175785797437, 13:ds=61 fs=21 fl=1 hz=0.024553571428571428, 19:ds=57 fs=21 fl=3 hz=0.025695931477516063, 10:ds=52 fs=23 fl=2 hz=0.02676659528907923, 1:ds=46 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=43 fs=48 fl=0 hz=0.05128205128205128

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=94 flags=purple
- S20: ds=81 flags=purple
- S6: ds=60 flags=purple
- S25: ds=58 flags=purple

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
- current_index=31 streak=1 max=3 last_repeat_gap=35 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=24), P2:5 (gap=12), P3:5 (gap=29)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=979 sev=B
- 288: ds=966 sev=B
- 255: ds=937 sev=B
- 668: ds=919 sev=B
- 199: ds=867 sev=B
- 499: ds=793 sev=B
- 399: ds=776 sev=B
- 039: ds=764 sev=B
- 448: ds=753 sev=B
- 005: ds=745 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=188 sev=red
  - 99: ds=135 sev=red
  - 77: ds=78 sev=blue
  - 33: ds=71 sev=blue
  - 88: ds=40 sev=purple
  - 66: ds=34 sev=purple
  - 11: ds=15 sev=-
  - 00: ds=14 sev=-
  - 22: ds=2 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 59: ds=81 sev=red
  - 79: ds=75 sev=red
  - 12: ds=50 sev=blue
  - 06: ds=45 sev=blue
  - 35: ds=42 sev=blue
  - 56: ds=34 sev=purple
  - 69: ds=32 sev=purple
  - 13: ds=27 sev=purple
  - 57: ds=26 sev=purple
  - 03: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:377, 1:362, 34:216, 16:174, 15:165, 32:142, 35:119, 28:64, 5:49, 2:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=377 fs=0 fl=0 hz=0.0, 1:ds=362 fs=2 fl=2 hz=0.009124087591240877, 34:ds=216 fs=19 fl=1 hz=0.02631578947368421, 16:ds=174 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=165 fs=23 fl=0 hz=0.029411764705882353, 32:ds=142 fs=3 fl=1 hz=0.006720430107526881, 35:ds=119 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=64 fs=26 fl=2 hz=0.02997858672376874, 5:ds=49 fs=18 fl=2 hz=0.022175290390707498, 2:ds=45 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=96 flags=red+purple
- S22: ds=81 flags=purple
- S23: ds=69 flags=purple
- S3: ds=63 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=65 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:1 (gap=37), P3:6 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=975 sev=B
- 009: ds=933 sev=B
- 255: ds=891 sev=B
- 138: ds=831 sev=B
- 117: ds=814 sev=B
- 158: ds=776 sev=B
- 344: ds=769 sev=B
- 199: ds=760 sev=B
- 112: ds=720 sev=B
- 277: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=130 sev=red
  - 33: ds=72 sev=blue
  - 44: ds=43 sev=purple
  - 77: ds=41 sev=purple
  - 66: ds=39 sev=purple
  - 11: ds=30 sev=purple
  - 55: ds=23 sev=-
  - 00: ds=17 sev=-
  - 22: ds=3 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 68: ds=88 sev=red
  - 07: ds=65 sev=red
  - 15: ds=53 sev=blue
  - 78: ds=38 sev=blue
  - 19: ds=37 sev=blue
  - 01: ds=31 sev=purple
  - 18: ds=31 sev=purple
  - 14: ds=30 sev=purple
  - 39: ds=28 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:619, 23:158, 26:121, 18:118, 13:67, 33:52, 16:50, 30:49, 24:46, 27:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=619 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=158 fs=17 fl=2 hz=0.025165562913907286, 26:ds=121 fs=2 fl=1 hz=0.0056657223796034, 18:ds=118 fs=23 fl=2 hz=0.02910360884749709, 13:ds=67 fs=20 fl=1 hz=0.024881516587677725, 33:ds=52 fs=19 fl=3 hz=0.023255813953488372, 16:ds=50 fs=5 fl=3 hz=0.009523809523809525, 30:ds=49 fs=35 fl=1 hz=0.03829787234042553, 24:ds=46 fs=37 fl=0 hz=0.04048140043763676, 27:ds=38 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=91 flags=blue+purple
- S1: ds=76 flags=blue+purple
- S24: ds=59 flags=blue+purple
- S3: ds=47 flags=purple
- S20: ds=41 flags=purple
- S6: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:776(B); midday:764(B)
- 199 -> evening:760(B); midday:867(B)
- 255 -> evening:891(B); midday:937(B)
- 344 -> combined:695(B); evening:769(B)
- 444 -> combined:801(B); evening:975(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:49(blue); evening:65(red)
- 11 -> combined:31(purple); evening:30(purple)
- 15 -> combined:25(purple); evening:53(blue)
- 19 -> combined:33(purple); evening:37(blue)
- 33 -> combined:143(red); evening:72(blue); midday:71(blue)
- 34 -> combined:35(purple); evening:25(purple)
- 35 -> combined:42(blue); midday:42(blue)
- 55 -> combined:46(purple); midday:188(red)
- 66 -> combined:69(purple); evening:39(purple); midday:34(purple)
- 69 -> combined:40(blue); midday:32(purple)
- 77 -> combined:82(blue); evening:41(purple); midday:78(blue)
- 88 -> combined:81(blue); evening:130(red); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(3.05)[R3,XVAR-Cons(CM)], 0(2.7174857142857145)[R1,Mirror-Echo], 8(1.5255714285714284)[R1,Double-Pressure], 9(1.3601142857142856)[R2,Mirror-Echo], 5(1.186)[R2,Mirror-Echo]
- P2: 1(6.836485714285715)[R2,XVAR-Cons(CEM)], 5(6.785842857142857)[R1,XVAR-Cons(CEM)], 9(2.5261857142857145)[R3,XVAR-Cons(CM)], 3(1.1389)[R2,Double-Pressure]
- P3: 5(3.8738571428571427)[R2,XVAR-Cons(CM)], 7(3.3061428571428575)[R1,XVAR-Cons(CE)], 6(2.7942857142857145)[R3,XVAR-Cons(CE)], 3(1.2478785714285714)[R2,Mirror-Echo], 8(0.4362928571428571)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-03.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=14), P2:5(gap=25), P3:7(gap=19); top cartesian candidates: 415, 455, 015, 055, 417.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 015, 025, 035, 045, 056.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:776(B),midday:764(B); 199→midday:867(B),evening:760(B); 255→midday:937(B),evening:891(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:285, 26:242, 16:100, 7:68, 6:63.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=359 Evening=980; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 359 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 089 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 359 (canon 359): box `359` covers winner `359` (boxed hit).
  - Evening winner 980 (canon 089): box `089` covers winner `980` (boxed hit).
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
