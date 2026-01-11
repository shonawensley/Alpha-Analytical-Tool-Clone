# Master Validation Run Report — SouthCarolina4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-07/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-07/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-07/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-07/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-07/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-07/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac23_winner_336_20260110_033446.html`
- `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac29_winner_288_20260110_033445.html`

Winners JSON files:
- `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac23_winner_336_20260110_033446.json`
- `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac29_winner_288_20260110_033445.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 288 (canon 288): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 336 (canon 336): exact_boxed=True exact_straight=True | rank 430/4852 (rank_frac 0.089)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 336 idx23 (rank 15/35, frac 0.429), 288 idx29 (rank 23/35, frac 0.657)
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

### 2.Stable — SouthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-07)

## Midday winner 288 (canonical 288)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=170 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 47 | rank 46/1439 (rank_frac 0.031966643502432245) | score 25.5 (top 31.5, ratio 0.8095238095238095, delta 6.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=14
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 336 (canonical 336)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=84 | exact_boxed=17 | exact_straight=10 | vt_boxed=17
- Scores (patterns_scores.csv): rank 430/4852 (rank_frac 0.08862324814509481) | score 17.5 (top 42.0, ratio 0.4166666666666667, delta 24.5) | section Evening, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat3|vstr2|hot1|perm2|hidden3v|double_mirror|draw_chain3
- Compound (patterns_compound.csv): rank 150/1704 (rank_frac 0.0880281690140845) | score 26.0 (top 79.0, ratio 0.3291139240506329, delta 53.0) | section Midday, col1_hits 1, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|col1x1|dblmirrorx7
- Families (patterns_families.csv): count 37 | rank 344/1439 (rank_frac 0.23905489923558026) | score 18.5 (top 31.5, ratio 0.5873015873015873, delta 13.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=22

## Top compound candidates (patterns_compound.csv)
- rank   17 | canon 579 | section Evening | score 50.0 | col1_hits 3 | hot2 7
- rank   11 | canon 069 | section Combined | score 51.5 | col1_hits 4 | hot2 6
- rank   32 | canon 56699 | section Evening | score 42.0 | col1_hits 3 | hot2 6
- rank    2 | canon 599 | section Evening | score 66.5 | col1_hits 5 | hot2 6
- rank    7 | canon 366 | section Evening | score 56.5 | col1_hits 5 | hot2 6
- rank    2 | canon 399 | section Evening | score 66.5 | col1_hits 5 | hot2 6
- rank   13 | canon 566 | section Evening | score 51.0 | col1_hits 5 | hot2 6
- rank   22 | canon 699 | section Evening | score 47.0 | col1_hits 3 | hot2 6
- rank   22 | canon 669 | section Evening | score 47.0 | col1_hits 3 | hot2 6
- rank    6 | canon 667 | section Evening | score 60.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1143 | family 1 | score 10.0 | hot2 0 | section Midday
- rank  344 | family 12 | score 18.5 | hot2 5 | section Midday
- rank  512 | family 22 | score 16.5 | hot2 8 | section Midday
- rank  586 | family 15 | score 15.5 | hot2 1 | section Midday
- rank  893 | family 20 | score 12.5 | hot2 3 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 288 (canon 288): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 336 (canon 336): exact_boxed=True exact_straight=True | rank 430/4852 (rank_frac 0.089)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260110)

## Midday winner 288 (canonical 288)
- Stamp (winner_stamp.json): items_total=104 | exact_any=0 exact_final=0 | vtrac_any=104 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=6 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=104 | exact_any=0 vtrac_any=104 | drop_exact_any=0 drop_vtrac_any=6 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=48 vt_straight=0
- Hits (winner_hits.csv): rows=104 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=48 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 336 (canonical 336)
- Stamp (winner_stamp.json): items_total=228 | exact_any=60 exact_final=0 | vtrac_any=228 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=228 | exact_any=60 vtrac_any=228 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=228 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.477143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 288 (canonical 288)
- Stamp (winner_stamp.json): items_total=200 | exact_any=0 exact_final=0 | vtrac_any=200 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=18 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=200 | exact_any=0 vtrac_any=200 | drop_exact_any=0 drop_vtrac_any=18 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=79 vt_straight=0
- Hits (winner_hits.csv): rows=200 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=79 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 224 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 224 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 12.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 599 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 599 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 599 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 599 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 5 | pattern 559 | score_v2 12.127143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 990 | score_v2 12.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 990 | score_v2 11.877143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 224 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 599 | score_v2 12.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 12.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 990 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 599 | score_v2 11.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 11.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 990 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 599 | score_v2 10.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 10.358571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 599 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 288 (canon 288): items_total=104 exact_any=0 vtrac_any=104 | top winner_present=False best_rank=None/34; Evening 336 (canon 336): items_total=228 exact_any=60 vtrac_any=228 | top winner_present=False best_rank=None/18; Combined 288 (canon 288): items_total=200 exact_any=0 vtrac_any=200 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 599, 559, 990, 599.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260110_033921)

## Top indices (from enhanced JSON)
- index 11 | score 54.957150000000006 | features: presence=27.729650000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 3 | score 41.297064999999996 | features: presence=27.129564999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 34.979366666666664 | features: presence=14.245199999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 6 | score 34.671425000000006 | features: presence=20.273925000000006, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 17 | score 33.23731250000001 | features: presence=22.049812500000005, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 20 | score 18.7625925 | features: presence=10.6950925, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 27 | score 15.733299999999998 | features: presence=7.615800000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 7 | score 14.947652500000002 | features: presence=7.4101525000000015, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 10 | score 13.4506 | features: presence=7.623100000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 1 | score 12.607858333333336 | features: presence=6.318900000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
037, 532, 703, 325, 523, 537, 753, 253, 203, 032

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 336 | index 23 | file SouthCarolina4_vtrac23_winner_336_20260110_033446.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 288 | index 29 | file SouthCarolina4_vtrac29_winner_288_20260110_033445.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 336 | index 23 rank 15/35 (rank_frac 0.42857142857142855) | score 8.391058333333334 (top 54.957150000000006, ratio 0.1526836514144808, delta 46.56609166666667) | winner_in_index_straights=False | top_index_straights: (none)
- winner 288 | index 29 rank 23/35 (rank_frac 0.6571428571428571) | score 2.9175583333333335 (top 54.957150000000006, ratio 0.053087875432647674, delta 52.039591666666674) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 336→idx23 rank 15/35 (frac 0.429); 288→idx29 rank 23/35 (frac 0.657).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 11, 3, 4, 6, 17.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-07)

## Midday winner 288 (canonical 288)
- Top lanes (hot_zones_top_lanes.csv): present | rank 94/210 (rank_frac 0.44761904761904764) | score_mean 16.729 (top 20.859, ratio 0.8020039311568147, delta 4.130000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 336 (canonical 336)
- Top lanes (hot_zones_top_lanes.csv): present | rank 11/210 (rank_frac 0.05238095238095238) | score_mean 18.445 (top 20.859, ratio 0.8842705786471067, delta 2.4140000000000015)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 127 | vt_triad 233 | score_mean 20.859 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 117 | vt_triad 23 | score_mean 19.771 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 568 | vt_triad 124 | score_mean 19.299 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 124 | vt_triad 235 | score_mean 19.262 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 237 | vt_triad 334 | score_mean 18.911 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    6 | triad 279 | vt_triad 335 | score_mean 18.832 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 247 | vt_triad 335 | score_mean 18.685 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 255 | vt_triad 13 | score_mean 18.656 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 259 | vt_triad 135 | score_mean 18.585 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 278 | vt_triad 334 | score_mean 18.567 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 288 (canon 288): rank 94/210 (rank_frac 0.448) ratio_to_top=0.8020039311568147; Evening 336 (canon 336): rank 11/210 (rank_frac 0.052) ratio_to_top=0.8842705786471067
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

Aux draws snapshot dir: `sharepacks/2026-01-07/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=412, 586, 712, 171, 432
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=586, 171, 189, 308, 910
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-07/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=412, 712, 432, 051, 084

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=24 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=18), P2:9 (gap=26), P3:7 (gap=18)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.04440964285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 295: score=42.06803571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.372150000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.25620642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 297: score=37.010264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=34.88711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.472049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 265: score=33.52522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.28592142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=33.227158571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=979 sev=B
- 449: ds=908 sev=B
- 156: ds=891 sev=B
- 778: ds=861 sev=B
- 279: ds=860 sev=B
- 033: ds=792 sev=B
- 004: ds=780 sev=B
- 688: ds=747 sev=B
- 278: ds=714 sev=B
- 377: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=188 sev=red
  - 55: ds=125 sev=red
  - 77: ds=109 sev=red
  - 33: ds=96 sev=blue
  - 88: ds=91 sev=blue
  - 22: ds=71 sev=blue
  - 66: ds=59 sev=purple
  - 00: ds=32 sev=purple
  - 44: ds=11 sev=-
  - 11: ds=3 sev=-
- non_repeating:
  - 78: ds=60 sev=red
  - 29: ds=41 sev=blue
  - 06: ds=34 sev=purple
  - 16: ds=34 sev=purple
  - 59: ds=30 sev=purple
  - 13: ds=26 sev=purple
  - 39: ds=26 sev=purple
  - 07: ds=23 sev=-
  - 37: ds=23 sev=-
  - 02: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:452, 35:395, 1:176, 26:164, 31:126, 4:117, 23:115, 28:109, 27:92, 19:76

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=452 fs=0 fl=0 hz=0.002197802197802198, 35:ds=395 fs=0 fl=0 hz=0.001949317738791423, 1:ds=176 fs=6 fl=4 hz=0.012195121951219513, 26:ds=164 fs=2 fl=0 hz=0.0062402496099844, 31:ds=126 fs=26 fl=0 hz=0.03002309468822171, 4:ds=117 fs=21 fl=2 hz=0.026589595375722544, 23:ds=115 fs=25 fl=1 hz=0.029850746268656716, 28:ds=109 fs=16 fl=2 hz=0.021479713603818614, 27:ds=92 fs=26 fl=0 hz=0.02911534154535274, 19:ds=76 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S17: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=74 flags=blue+purple
- S23: ds=63 flags=purple
- S5: ds=62 flags=purple
- S24: ds=60 flags=blue+purple
- S4: ds=52 flags=purple
- S3: ds=51 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}
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
- current_index=8 streak=1 max=3 last_repeat_gap=7 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=17), P2:3 (gap=43), P3:7 (gap=13)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.04440964285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 295: score=42.06803571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.372150000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.25620642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 297: score=37.010264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=34.88711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.472049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 265: score=33.52522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.28592142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=33.227158571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=881 sev=B
- 555: ds=876 sev=B
- 222: ds=853 sev=B
- 337: ds=830 sev=B
- 003: ds=821 sev=B
- 228: ds=812 sev=B
- 556: ds=714 sev=B
- 449: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=116 sev=red
  - 55: ds=80 sev=blue
  - 77: ds=49 sev=purple
  - 33: ds=43 sev=purple
  - 88: ds=41 sev=purple
  - 22: ds=39 sev=purple
  - 66: ds=26 sev=purple
  - 00: ds=17 sev=-
  - 44: ds=9 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 49: ds=57 sev=red
  - 67: ds=51 sev=blue
  - 34: ds=50 sev=blue
  - 27: ds=44 sev=blue
  - 07: ds=35 sev=purple
  - 05: ds=32 sev=purple
  - 15: ds=30 sev=purple
  - 78: ds=29 sev=purple
  - 69: ds=28 sev=purple
  - 16: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:417, 26:195, 35:181, 27:146, 6:114, 5:83, 1:80, 15:75, 34:61, 31:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=417 fs=1 fl=2 hz=0.006993006993006993, 26:ds=195 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=181 fs=1 fl=1 hz=0.004968944099378882, 27:ds=146 fs=18 fl=3 hz=0.026582278481012658, 6:ds=114 fs=24 fl=2 hz=0.02957906712172924, 5:ds=83 fs=20 fl=1 hz=0.023102310231023104, 1:ds=80 fs=7 fl=3 hz=0.012127894156560088, 15:ds=75 fs=17 fl=3 hz=0.021691973969631236, 34:ds=61 fs=28 fl=1 hz=0.03159041394335512, 31:ds=57 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=84 flags=purple
- S25: ds=81 flags=purple
- S21: ds=61 flags=purple
- S20: ds=57 flags=purple
- S17: ds=55 flags=purple
- S8: ds=53 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 026: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 017: score=2 tags=RS
  - 035: score=2 tags=RS
  - 089: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=35 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=21), P2:9 (gap=17), P3:8 (gap=24)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.04440964285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 295: score=42.06803571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.372150000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.25620642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 297: score=37.010264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=34.88711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.472049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 265: score=33.52522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.28592142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=33.227158571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=985 sev=B
- 117: ds=896 sev=B
- 005: ds=882 sev=B
- 577: ds=859 sev=B
- 155: ds=839 sev=B
- 777: ds=838 sev=B
- 669: ds=830 sev=B
- 179: ds=812 sev=B
- 366: ds=778 sev=B
- 222: ds=772 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=102 sev=blue
  - 77: ds=89 sev=blue
  - 66: ds=81 sev=blue
  - 33: ds=77 sev=blue
  - 55: ds=68 sev=purple
  - 88: ds=62 sev=purple
  - 22: ds=39 sev=purple
  - 11: ds=28 sev=purple
  - 00: ds=18 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 58: ds=103 sev=red
  - 35: ds=70 sev=red
  - 29: ds=65 sev=red
  - 47: ds=55 sev=blue
  - 19: ds=37 sev=blue
  - 78: ds=33 sev=purple
  - 68: ds=30 sev=purple
  - 38: ds=24 sev=-
  - 13: ds=22 sev=-
  - 09: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:490, 1:277, 32:244, 31:223, 4:143, 28:116, 19:112, 23:107, 26:89, 16:85

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=490 fs=3 fl=1 hz=0.017391304347826087, 1:ds=277 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=244 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=223 fs=16 fl=1 hz=0.021935483870967745, 4:ds=143 fs=21 fl=3 hz=0.028742514970059883, 28:ds=116 fs=10 fl=4 hz=0.017676767676767676, 19:ds=112 fs=12 fl=2 hz=0.016968325791855206, 23:ds=107 fs=24 fl=0 hz=0.02937576499388005, 26:ds=89 fs=0 fl=0 hz=0.002347417840375587, 16:ds=85 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=68 flags=purple
- S15: ds=59 flags=red+purple
- S17: ds=55 flags=purple
- S23: ds=52 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:772(B); midday:853(B)
- 366 -> combined:979(B); evening:778(B)
- 449 -> combined:908(B); midday:672(B)
- 688 -> combined:747(B); evening:737(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 16 -> combined:34(purple); midday:26(purple)
- 22 -> combined:71(blue); evening:39(purple); midday:39(purple)
- 29 -> combined:41(blue); evening:65(red)
- 33 -> combined:96(blue); evening:77(blue); midday:43(purple)
- 55 -> combined:125(red); evening:68(purple); midday:80(blue)
- 66 -> combined:59(purple); evening:81(blue); midday:26(purple)
- 77 -> combined:109(red); evening:89(blue); midday:49(purple)
- 78 -> combined:60(red); evening:33(purple); midday:29(purple)
- 88 -> combined:91(blue); evening:62(purple); midday:41(purple)
- 99 -> combined:188(red); evening:102(blue); midday:116(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(3.7619999999999996)[R2,XVAR-Cons(CE)], 2(3.4001142857142854)[R1,XVAR-Cons(CM)], 1(1.3312)[R2,Mirror-Echo], 0(1.2075714285714285)[R1,Double-Pressure], 9(0.2414285714285714)[R3,Swap]
- P2: 9(7.580292857142857)[R1,Mirror-Echo], 6(2.5374857142857143)[R2,XVAR-Cons(CE)], 4(2.1224214285714287)[R3,Mirror-Echo], 3(1.7449999999999999)[R1,Double-Pressure], 0(0.9717)[R2,Double-Pressure]
- P3: 5(6.087628571428572)[R2,XVAR-Cons(CEM)], 7(3.529857142857143)[R1,XVAR-Cons(CM)], 8(1.3865714285714286)[R1,Double-Pressure], 2(0.9436285714285714)[R2,Mirror-Echo], 0(0.2997928571428571)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=18), P2:9(gap=26), P3:7(gap=18); top cartesian candidates: 695, 295, 697, 595, 297.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:853(B),evening:772(B); 366→combined:979(B),evening:778(B); 449→combined:908(B),midday:672(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:452, 35:395, 1:176, 26:164, 31:126.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=288 Evening=336; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 288 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 336 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 288 (canon 288): box `288` covers winner `288` (boxed hit).
  - Evening winner 336 (canon 336): box `336` covers winner `336` (boxed hit).
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
