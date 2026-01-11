# Master Validation Run Report — Pennsylvania4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-05/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-05/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-05/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-05/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-05/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-05/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_600_20260110_035740.html`
- `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_546_20260110_035739.html`

Winners JSON files:
- `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_600_20260110_035740.json`
- `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac9_winner_546_20260110_035739.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 546 (canon 456): exact_boxed=True exact_straight=True | rank 1186/5107 (rank_frac 0.232); Evening 600 (canon 006): exact_boxed=True exact_straight=True | rank 303/5107 (rank_frac 0.059)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 600 idx2 (rank 3/35, frac 0.086), 546 idx9 (rank 8/35, frac 0.229)
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

### 2.Stable — Pennsylvania4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-05)

## Midday winner 546 (canonical 456)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=14 | family_rows=95 | exact_boxed=14 | exact_straight=14 | vt_boxed=14
- Scores (patterns_scores.csv): rank 1186/5107 (rank_frac 0.23223027217544548) | score 15.0 (top 42.5, ratio 0.35294117647058826, delta 27.5) | section Evening, Set Set1, Draw Draw4, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hot2|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 128/1996 (rank_frac 0.06412825651302605) | score 26.5 (top 74.0, ratio 0.3581081081081081, delta 47.5) | section Evening, col1_hits 3, hot2 2, set_chain 1, draw_chain 4 | why draw_chain4|col1x3|hot1x1|hot2x2|vstrx3
- Families (patterns_families.csv): count 43 | rank 117/1244 (rank_frac 0.09405144694533762) | score 23.5 (top 35.5, ratio 0.6619718309859155, delta 12.0) | section Midday, hot2 5
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=159

## Evening winner 600 (canonical 006)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=581 | exact_boxed=17 | exact_straight=16 | vt_boxed=17
- Scores (patterns_scores.csv): rank 303/5107 (rank_frac 0.059330330918347364) | score 20.0 (top 42.5, ratio 0.47058823529411764, delta 22.5) | section Combined, Set Set3, Draw Draw1, Col 4, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat4|vstr2|hot1|perm2|double_mirror|set_chain3
- Compound (patterns_compound.csv): rank 63/1996 (rank_frac 0.03156312625250501) | score 33.0 (top 74.0, ratio 0.44594594594594594, delta 41.0) | section Midday, col1_hits 3, hot2 2, set_chain 1, draw_chain 3 | why draw_chain3|col1x3|hot1x1|hot2x2|vstrx6|dblmirrorx6
- Families (patterns_families.csv): count 54 | rank 74/1244 (rank_frac 0.0594855305466238) | score 26.0 (top 35.5, ratio 0.7323943661971831, delta 9.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=21

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 557 | section Evening | score 69.5 | col1_hits 6 | hot2 8
- rank    3 | canon 059 | section Midday | score 67.5 | col1_hits 6 | hot2 6
- rank    4 | canon 005 | section Midday | score 65.5 | col1_hits 5 | hot2 6
- rank   26 | canon 256 | section Combined | score 43.0 | col1_hits 5 | hot2 6
- rank   18 | canon 4557 | section Evening | score 44.5 | col1_hits 3 | hot2 6
- rank    5 | canon 455 | section Evening | score 62.5 | col1_hits 5 | hot2 6
- rank   10 | canon 578 | section Evening | score 49.5 | col1_hits 1 | hot2 5
- rank    9 | canon 009 | section Midday | score 52.0 | col1_hits 4 | hot2 5
- rank   31 | canon 156 | section Combined | score 41.5 | col1_hits 3 | hot2 5
- rank   54 | canon 2256 | section Combined | score 35.0 | col1_hits 4 | hot2 4

## Top families (patterns_families.csv)
- rank 1174 | family 3 | score 6.0 | hot2 0 | section Midday
- rank  429 | family 3 | score 16.0 | hot2 0 | section Midday
- rank  183 | family 3 | score 21.0 | hot2 0 | section Midday
- rank  269 | family 12 | score 19.0 | hot2 0 | section Midday
- rank  365 | family 15 | score 17.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 546 (canon 456): exact_boxed=True exact_straight=True | rank 1186/5107 (rank_frac 0.232); Evening 600 (canon 006): exact_boxed=True exact_straight=True | rank 303/5107 (rank_frac 0.059)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260110)

## Midday winner 546 (canonical 456)
- Stamp (winner_stamp.json): items_total=158 | exact_any=0 exact_final=0 | vtrac_any=122 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=118 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=48 family_vtrac_final=0
- Flags (winner_flags.csv): rows=158 | exact_any=0 vtrac_any=122 | drop_exact_any=0 drop_vtrac_any=118 | family_exact_any=0 family_vtrac_any=48 | vt_boxed=46 vt_straight=0
- Hits (winner_hits.csv): rows=158 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=46 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 600 (canonical 006)
- Stamp (winner_stamp.json): items_total=33 | exact_any=0 exact_final=0 | vtrac_any=20 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=33 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=20 family_vtrac_final=0
- Flags (winner_flags.csv): rows=33 | exact_any=0 vtrac_any=20 | drop_exact_any=0 drop_vtrac_any=33 | family_exact_any=0 family_vtrac_any=20 | vt_boxed=21 vt_straight=0
- Hits (winner_hits.csv): rows=33 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=21 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 546 (canonical 456)
- Stamp (winner_stamp.json): items_total=364 | exact_any=41 exact_final=0 | vtrac_any=294 vtrac_final=0 | drop_exact_any=69 drop_exact_final=0 | drop_vtrac_any=244 drop_vtrac_final=0 | family_exact_any=6 family_exact_final=0 | family_vtrac_any=83 family_vtrac_final=0
- Flags (winner_flags.csv): rows=364 | exact_any=41 vtrac_any=294 | drop_exact_any=69 drop_vtrac_any=244 | family_exact_any=6 family_vtrac_any=83 | vt_boxed=152 vt_straight=0
- Hits (winner_hits.csv): rows=364 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=152 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.520476 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 554 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 554 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 554 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 554 | score_v2 13.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 11.520476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 11.520476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 11.487143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 11.487143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 11.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 11.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 11.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 11.332597 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 554 | score_v2 13.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 11.520476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 11.520476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 11.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 559 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 10.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 511 | score_v2 9.74381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 552 | score_v2 9.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 522 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 11 | variant Evening | best_pattern 113 | score_v2 9.460476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Combined | best_pattern 522 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 546 (canon 456): items_total=158 exact_any=0 vtrac_any=122 | top winner_present=False best_rank=None/16; Evening 600 (canon 006): items_total=33 exact_any=0 vtrac_any=20 | top winner_present=False best_rank=None/26; Combined 546 (canon 456): items_total=364 exact_any=41 vtrac_any=294 | top winner_present=False best_rank=None/12
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 554, 559, 559, 559, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260110_035938)

## Top indices (from enhanced JSON)
- index 15 | score 66.39276499999997 | features: presence=47.98526499999997, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 63.618759999999966 | features: presence=45.80125999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 36.5910675 | features: presence=24.3135675, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 1 | score 25.480007499999992 | features: presence=16.462507499999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 24.004150000000003 | features: presence=11.826650000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 35 | score 14.788837500000001 | features: presence=9.691337500000001, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 34 | score 13.497958333333335 | features: presence=5.6690000000000005, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 9 | score 12.4472425 | features: presence=7.219742500000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 25 | score 12.04645 | features: presence=6.43895, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 13 | score 7.33975 | features: presence=1.916, cross_section=0.5, set_echo=0.6, first_hit=0.08000000000000002

## Top straights (from enhanced JSON)
059, 590, 940, 095, 904, 945, 594, 056, 593, 065

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 600 | index 2 | file Pennsylvania4_vtrac2_winner_600_20260110_035740.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 546 | index 9 | file Pennsylvania4_vtrac9_winner_546_20260110_035739.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 600 | index 2 rank 3/35 (rank_frac 0.08571428571428572) | score 36.5910675 (top 66.39276499999997, ratio 0.551130345301932, delta 29.801697499999968) | winner_in_index_straights=False | top_index_straights: 056 (11.7), 065 (10.732), 605 (6.642)
- winner 546 | index 9 rank 8/35 (rank_frac 0.22857142857142856) | score 12.4472425 (top 66.39276499999997, ratio 0.18747889924451866, delta 53.94552249999997) | winner_in_index_straights=False | top_index_straights: 906 (4.957), 064 (4.336), 645 (3.994)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 600→idx2 rank 3/35 (frac 0.086); 546→idx9 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 15, 5, 2, 1, 14.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-05)

## Midday winner 546 (canonical 456)
- Top lanes (hot_zones_top_lanes.csv): present | rank 84/210 (rank_frac 0.4) | score_mean 18.205 (top 28.1, ratio 0.6478647686832739, delta 9.895000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 600 (canonical 006)
- Top lanes (hot_zones_top_lanes.csv): present | rank 66/210 (rank_frac 0.3142857142857143) | score_mean 18.563 (top 28.1, ratio 0.6606049822064056, delta 9.537000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 000 | vt_triad 1 | score_mean 28.1 | tags col1,hot16,hot20,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical4
- rank    2 | triad 119 | vt_triad 25 | score_mean 22.467 | tags hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 447 | vt_triad 35 | score_mean 22.26 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    4 | triad 466 | vt_triad 25 | score_mean 22.2 | tags hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical4,vt_straight
- rank    5 | triad 555 | vt_triad 1 | score_mean 21.5 | tags hot16,hot20,set1_bonus,superhot_set1
- rank    6 | triad 099 | vt_triad 15 | score_mean 21.125 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 599 | vt_triad 15 | score_mean 20.872 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    8 | triad 056 | vt_triad 112 | score_mean 20.827 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 059 | vt_triad 115 | score_mean 20.488 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 359 | vt_triad 145 | score_mean 20.477 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 546 (canon 456): rank 84/210 (rank_frac 0.400) ratio_to_top=0.6478647686832739; Evening 600 (canon 006): rank 66/210 (rank_frac 0.314) ratio_to_top=0.6606049822064056
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

Aux draws snapshot dir: `sharepacks/2026-01-05/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-05/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=980, 359, 909, 744, 360
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-05/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=359, 744, 871, 322, 684
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-05/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=980, 909, 360, 328, 221

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=2 max=3 last_repeat_gap=1 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=16), P2:1 (gap=19), P3:7 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=37.35445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=37.05059285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=36.79664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=36.49277857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=36.31917142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 016: score=36.01530714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 515: score=34.55727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 413: score=33.181628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=32.877764285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.41069 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 159: ds=888 sev=B
- 007: ds=885 sev=B
- 088: ds=849 sev=B
- 008: ds=827 sev=B
- 444: ds=803 sev=B
- 039: ds=778 sev=B
- 355: ds=768 sev=B
- 344: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=145 sev=red
  - 77: ds=84 sev=blue
  - 88: ds=83 sev=blue
  - 66: ds=71 sev=blue
  - 55: ds=48 sev=purple
  - 11: ds=33 sev=purple
  - 00: ds=31 sev=purple
  - 22: ds=7 sev=-
  - 44: ds=3 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 07: ds=51 sev=blue
  - 69: ds=42 sev=blue
  - 34: ds=37 sev=blue
  - 19: ds=35 sev=purple
  - 15: ds=27 sev=purple
  - 45: ds=24 sev=-
  - 57: ds=22 sev=-
  - 79: ds=22 sev=-
  - 27: ds=21 sev=-
  - 67: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:287, 26:244, 16:102, 7:70, 6:65, 13:63, 19:59, 10:54, 1:48, 11:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=287 fs=2 fl=1 hz=0.007380073800738007, 26:ds=244 fs=0 fl=1 hz=0.003898635477582846, 16:ds=102 fs=3 fl=2 hz=0.007371007371007371, 7:ds=70 fs=35 fl=1 hz=0.04, 6:ds=65 fs=21 fl=1 hz=0.025611175785797437, 13:ds=63 fs=21 fl=1 hz=0.024553571428571428, 19:ds=59 fs=21 fl=3 hz=0.025695931477516063, 10:ds=54 fs=23 fl=2 hz=0.02676659528907923, 1:ds=48 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=45 fs=48 fl=0 hz=0.05128205128205128

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=96 flags=purple
- S20: ds=83 flags=purple
- S6: ds=62 flags=purple
- S25: ds=60 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 0}}
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
- current_index=14 streak=1 max=3 last_repeat_gap=36 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=25), P2:9 (gap=12), P3:5 (gap=30)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=37.35445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=37.05059285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=36.79664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=36.49277857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=36.31917142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 016: score=36.01530714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 515: score=34.55727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 413: score=33.181628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=32.877764285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.41069 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=980 sev=B
- 288: ds=967 sev=B
- 255: ds=938 sev=B
- 668: ds=920 sev=B
- 199: ds=868 sev=B
- 499: ds=794 sev=B
- 399: ds=777 sev=B
- 039: ds=765 sev=B
- 448: ds=754 sev=B
- 005: ds=746 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=189 sev=red
  - 99: ds=136 sev=red
  - 77: ds=79 sev=blue
  - 33: ds=72 sev=blue
  - 88: ds=41 sev=purple
  - 66: ds=35 sev=purple
  - 11: ds=16 sev=-
  - 00: ds=15 sev=-
  - 22: ds=3 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 79: ds=76 sev=red
  - 12: ds=51 sev=blue
  - 06: ds=46 sev=blue
  - 56: ds=35 sev=purple
  - 69: ds=33 sev=purple
  - 13: ds=28 sev=purple
  - 57: ds=27 sev=purple
  - 03: ds=26 sev=purple
  - 07: ds=25 sev=purple
  - 09: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:378, 1:363, 34:217, 16:175, 15:166, 32:143, 35:120, 28:65, 5:50, 2:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=378 fs=0 fl=0 hz=0.0, 1:ds=363 fs=2 fl=2 hz=0.009124087591240877, 34:ds=217 fs=19 fl=1 hz=0.02631578947368421, 16:ds=175 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=166 fs=23 fl=0 hz=0.029411764705882353, 32:ds=143 fs=3 fl=1 hz=0.006720430107526881, 35:ds=120 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=65 fs=26 fl=2 hz=0.02997858672376874, 5:ds=50 fs=18 fl=2 hz=0.022175290390707498, 2:ds=46 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=97 flags=red+purple
- S22: ds=82 flags=purple
- S23: ds=70 flags=purple
- S3: ds=64 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=66 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=32), P2:1 (gap=38), P3:6 (gap=22)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=37.35445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=37.05059285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=36.79664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=36.49277857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=36.31917142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 016: score=36.01530714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 515: score=34.55727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 413: score=33.181628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=32.877764285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.41069 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=976 sev=B
- 009: ds=934 sev=B
- 255: ds=892 sev=B
- 138: ds=832 sev=B
- 117: ds=815 sev=B
- 158: ds=777 sev=B
- 344: ds=770 sev=B
- 199: ds=761 sev=B
- 112: ds=721 sev=B
- 277: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=131 sev=red
  - 33: ds=73 sev=blue
  - 44: ds=44 sev=purple
  - 77: ds=42 sev=purple
  - 66: ds=40 sev=purple
  - 11: ds=31 sev=purple
  - 55: ds=24 sev=-
  - 00: ds=18 sev=-
  - 22: ds=4 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 68: ds=89 sev=red
  - 07: ds=66 sev=red
  - 15: ds=54 sev=blue
  - 78: ds=39 sev=blue
  - 19: ds=38 sev=blue
  - 01: ds=32 sev=purple
  - 18: ds=32 sev=purple
  - 14: ds=31 sev=purple
  - 39: ds=29 sev=purple
  - 16: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:620, 23:159, 26:122, 18:119, 13:68, 33:53, 16:51, 30:50, 24:47, 27:39

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=620 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=159 fs=17 fl=2 hz=0.025165562913907286, 26:ds=122 fs=2 fl=1 hz=0.0056657223796034, 18:ds=119 fs=23 fl=2 hz=0.02910360884749709, 13:ds=68 fs=20 fl=1 hz=0.024881516587677725, 33:ds=53 fs=19 fl=3 hz=0.023255813953488372, 16:ds=51 fs=5 fl=3 hz=0.009523809523809525, 30:ds=50 fs=35 fl=1 hz=0.03829787234042553, 24:ds=47 fs=37 fl=0 hz=0.04048140043763676, 27:ds=39 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=92 flags=blue+purple
- S1: ds=77 flags=blue+purple
- S24: ds=60 flags=blue+purple
- S3: ds=48 flags=purple
- S20: ds=42 flags=purple
- S6: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:778(B); midday:765(B)
- 199 -> evening:761(B); midday:868(B)
- 255 -> evening:892(B); midday:938(B)
- 344 -> combined:697(B); evening:770(B)
- 444 -> combined:803(B); evening:976(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:51(blue); evening:66(red); midday:25(purple)
- 11 -> combined:33(purple); evening:31(purple)
- 15 -> combined:27(purple); evening:54(blue)
- 19 -> combined:35(purple); evening:38(blue)
- 33 -> combined:145(red); evening:73(blue); midday:72(blue)
- 34 -> combined:37(blue); evening:26(purple)
- 55 -> combined:48(purple); midday:189(red)
- 66 -> combined:71(blue); evening:40(purple); midday:35(purple)
- 69 -> combined:42(blue); midday:33(purple)
- 77 -> combined:84(blue); evening:42(purple); midday:79(blue)
- 88 -> combined:83(blue); evening:131(red); midday:41(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(3.117642857142857)[R3,XVAR-Cons(CM)], 0(2.8137785714285712)[R1,Mirror-Echo], 8(1.6254285714285714)[R1,Double-Pressure], 9(1.3945857142857143)[R2,Mirror-Echo], 5(1.2585714285714285)[R2,Mirror-Echo]
- P2: 1(7.789100000000001)[R1,XVAR-Cons(CEM)], 9(3.4242857142857144)[R2,XVAR-Cons(CM)], 3(2.743657142857143)[R3,XVAR-Cons(CE)], 5(0.3552785714285714)[R3,Swap], 6(0.2929857142857143)[R3,Mirror-Echo]
- P3: 5(3.9477142857142855)[R2,XVAR-Cons(CM)], 7(3.3899)[R1,XVAR-Cons(CE)], 6(2.9124285714285714)[R3,XVAR-Cons(CE)], 3(1.2748857142857142)[R2,Mirror-Echo], 8(0.45922857142857143)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=16), P2:1(gap=19), P3:7(gap=21); top cartesian candidates: 415, 015, 417, 017, 416.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:778(B),midday:765(B); 199→midday:868(B),evening:761(B); 255→midday:938(B),evening:892(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:287, 26:244, 16:102, 7:70, 6:65.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=546 Evening=600; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 456 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 006 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 546 (canon 456): box `456` covers winner `546` (boxed hit).
  - Evening winner 600 (canon 006): box `006` covers winner `600` (boxed hit).
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
