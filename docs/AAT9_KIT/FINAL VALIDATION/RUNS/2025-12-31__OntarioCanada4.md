# Master Validation Run Report — OntarioCanada4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/OntarioCanada4/`
- Winners lens: `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-12-31/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-12-31/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-12-31/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-12-31/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2025-12-31/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2025-12-31/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_918_20260105_052203.html`
- `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac30_winner_932_20260105_052205.html`

Winners JSON files:
- `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_918_20260105_052203.json`
- `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac30_winner_932_20260105_052205.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 918 (canon 189): exact_boxed=True exact_straight=True | rank 402/5407 (rank_frac 0.074); Evening 932 (canon 239): exact_boxed=True exact_straight=True | rank 1719/5407 (rank_frac 0.318)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 918 idx24 (rank 17/35, frac 0.486), 932 idx30 (rank 8/35, frac 0.229)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
- Q7: Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy.
- Q8: Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries).
- Q9: Aux cues: BA score=3 (if None, BA not available); see Part 3 positional/doubles/pairs notes.
- Q10: 4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank).
- Q11: Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table.
- Q12: Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days.
- Q13: Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance.
- Q14: Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — OntarioCanada4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2025-12-31)

## Midday winner 918 (canonical 189)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=31 | family_rows=625 | exact_boxed=31 | exact_straight=31 | vt_boxed=31
- Scores (patterns_scores.csv): rank 402/5407 (rank_frac 0.07434806732014056) | score 20.5 (top 42.0, ratio 0.4880952380952381, delta 21.5) | section Evening, Set Set1, Draw Draw3, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|vtrac_straight|draw_chain7
- Compound (patterns_compound.csv): rank 25/1879 (rank_frac 0.013304949441192123) | score 52.0 (top 96.0, ratio 0.5416666666666666, delta 44.0) | section Evening, col1_hits 5, hot2 6, set_chain 1, draw_chain 7 | why draw_chain7|col1x5|hot1x5|hot2x6|vstrx12
- Families (patterns_families.csv): count 64 | rank 35/1343 (rank_frac 0.026061057334326135) | score 27.5 (top 33.0, ratio 0.8333333333333334, delta 5.5) | section Evening, hot2 4
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=150

## Evening winner 932 (canonical 239)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=8 | family_rows=296 | exact_boxed=8 | exact_straight=8 | vt_boxed=8
- Scores (patterns_scores.csv): rank 1719/5407 (rank_frac 0.3179212132420936) | score 15.0 (top 42.0, ratio 0.35714285714285715, delta 27.0) | section Evening, Set Set1, Draw Draw4, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hot2|vtrac_straight|set_chain2|draw_chain4
- Compound (patterns_compound.csv): rank 231/1879 (rank_frac 0.12293773283661522) | score 24.5 (top 96.0, ratio 0.2552083333333333, delta 71.5) | section Evening, col1_hits 0, hot2 2, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|hot2x2|vstrx3
- Families (patterns_families.csv): count 45 | rank 379/1343 (rank_frac 0.2822040208488459) | score 20.0 (top 33.0, ratio 0.6060606060606061, delta 13.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=91

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 188 | section Combined | score 96.0 | col1_hits 9 | hot2 11
- rank    2 | canon 114 | section Evening | score 90.5 | col1_hits 8 | hot2 11
- rank    4 | canon 118 | section Evening | score 78.0 | col1_hits 7 | hot2 11
- rank   22 | canon 148 | section Evening | score 53.5 | col1_hits 7 | hot2 9
- rank    9 | canon 1148 | section Evening | score 67.5 | col1_hits 7 | hot2 9
- rank    8 | canon 188 | section Evening | score 68.5 | col1_hits 6 | hot2 8
- rank   15 | canon 1188 | section Evening | score 58.5 | col1_hits 6 | hot2 8
- rank    5 | canon 588 | section Combined | score 76.0 | col1_hits 5 | hot2 7
- rank   23 | canon 1189 | section Evening | score 53.0 | col1_hits 5 | hot2 6
- rank   29 | canon 11889 | section Evening | score 50.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1315 | family 27 | score 5.5 | hot2 0 | section Midday
- rank 1284 | family 2 | score 7.0 | hot2 0 | section Midday
- rank  299 | family 7 | score 21.0 | hot2 0 | section Midday
- rank  632 | family 20 | score 16.5 | hot2 0 | section Midday
- rank  740 | family 32 | score 15.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 918 (canon 189): exact_boxed=True exact_straight=True | rank 402/5407 (rank_frac 0.074); Evening 932 (canon 239): exact_boxed=True exact_straight=True | rank 1719/5407 (rank_frac 0.318)
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

### 2.Digit Reduction — OntarioCanada4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260105)

## Midday winner 918 (canonical 189)
- Stamp (winner_stamp.json): items_total=48 | exact_any=0 exact_final=0 | vtrac_any=48 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=48 | exact_any=0 vtrac_any=48 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=48 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.477143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 932 (canonical 239)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.658571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 918 (canonical 189)
- Stamp (winner_stamp.json): items_total=248 | exact_any=2 exact_final=0 | vtrac_any=220 vtrac_final=0 | drop_exact_any=10 drop_exact_final=0 | drop_vtrac_any=55 drop_vtrac_final=0 | family_exact_any=7 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=248 | exact_any=2 vtrac_any=220 | drop_exact_any=10 drop_vtrac_any=55 | family_exact_any=7 family_vtrac_any=2 | vt_boxed=44 vt_straight=0
- Hits (winner_hits.csv): rows=248 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=44 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 551 | score_v2 15.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 14.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 552 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 522 | score_v2 14.127143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 522 | score_v2 14.127143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 552 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 552 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 552 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 552 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 522 | score_v2 13.877143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 551 | score_v2 15.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 552 | score_v2 14.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 522 | score_v2 14.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 551 | score_v2 11.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 221 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 10.158571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 9.658571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 599 | score_v2 9.608571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 552 | score_v2 9.587143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 221 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 918 (canon 189): items_total=48 exact_any=0 vtrac_any=48 | top winner_present=False best_rank=None/18; Evening 932 (canon 239): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/18; Combined 918 (canon 189): items_total=248 exact_any=2 vtrac_any=220 | top winner_present=False best_rank=None/14
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 551, 552, 522, 551, 221.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_053049)

## Top indices (from enhanced JSON)
- index 29 | score 46.64715 | features: presence=29.659650000000006, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 11 | score 44.956999999999994 | features: presence=27.079499999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 43.4966 | features: presence=24.549100000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 42.873455 | features: presence=30.295955, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 34.4472 | features: presence=21.479700000000005, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 12 | score 29.086825000000005 | features: presence=19.199325, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 26.419780000000003 | features: presence=13.992280000000001, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 30 | score 26.256022500000007 | features: presence=14.408522500000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 31 | score 24.143612500000003 | features: presence=18.0761125, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 34 | score 19.792362500000003 | features: presence=11.9248625, cross_section=0.5, first_hit=0.2666666666666667, column_span=0.17083333333333334

## Top straights (from enhanced JSON)
258, 524, 852, 752, 528, 875, 825, 267, 672, 762

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 918 | index 24 | file OntarioCanada4_vtrac24_winner_918_20260105_052203.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 932 | index 30 | file OntarioCanada4_vtrac30_winner_932_20260105_052205.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 918 | index 24 rank 17/35 (rank_frac 0.4857142857142857) | score 7.962858333333332 (top 46.64715, ratio 0.1707040694519029, delta 38.684291666666674) | winner_in_index_straights=False | top_index_straights: 486 (2.25), 684 (2.124), 986 (2.04)
- winner 932 | index 30 rank 8/35 (rank_frac 0.22857142857142856) | score 26.256022500000007 (top 46.64715, ratio 0.5628644515259776, delta 20.391127499999996) | winner_in_index_straights=False | top_index_straights: 248 (9.929), 824 (9.425), 847 (6.389)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 918→idx24 rank 17/35 (frac 0.486); 932→idx30 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 29, 11, 20, 10, 13.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2025-12-31)

## Midday winner 918 (canonical 189)
- Top lanes (hot_zones_top_lanes.csv): present | rank 94/210 (rank_frac 0.44761904761904764) | score_mean 16.809 (top 22.765, ratio 0.7383703052932133, delta 5.9559999999999995)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 932 (canonical 239)
- Top lanes (hot_zones_top_lanes.csv): present | rank 143/210 (rank_frac 0.680952380952381) | score_mean 15.489 (top 22.765, ratio 0.6803865583132, delta 7.276)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 22.765 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 116 | vt_triad 22 | score_mean 22.019 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 166 | vt_triad 22 | score_mean 21.635 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 267 | vt_triad 233 | score_mean 21.295 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 127 | vt_triad 233 | score_mean 21.175 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 056 | vt_triad 112 | score_mean 21.128 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 167 | vt_triad 223 | score_mean 20.989 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 169 | vt_triad 225 | score_mean 20.92 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 126 | vt_triad 223 | score_mean 20.757 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 237 | vt_triad 334 | score_mean 20.639 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 918 (canon 189): rank 94/210 (rank_frac 0.448) ratio_to_top=0.7383703052932133; Evening 932 (canon 239): rank 143/210 (rank_frac 0.681) ratio_to_top=0.6803865583132
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

Aux draws snapshot dir: `sharepacks/2025-12-31/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=372, 409, 043, 006, 297
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=409, 006, 313, 909, 497
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=372, 043, 297, 606, 056

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=46 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=20), P2:8 (gap=18), P3:4 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=997 sev=B
- 128: ds=917 sev=B
- 555: ds=882 sev=B
- 039: ds=773 sev=B
- 333: ds=744 sev=B
- 188: ds=717 sev=B
- 266: ds=703 sev=B
- 477: ds=701 sev=B
- 126: ds=693 sev=B
- 669: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=119 sev=red
  - 55: ds=75 sev=blue
  - 11: ds=34 sev=purple
  - 88: ds=28 sev=purple
  - 44: ds=19 sev=-
  - 77: ds=10 sev=-
  - 99: ds=7 sev=-
  - 66: ds=6 sev=-
  - 33: ds=5 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 89: ds=79 sev=red
  - 01: ds=54 sev=blue
  - 68: ds=52 sev=blue
  - 15: ds=51 sev=blue
  - 17: ds=45 sev=blue
  - 18: ds=45 sev=blue
  - 12: ds=31 sev=purple
  - 69: ds=30 sev=purple
  - 24: ds=29 sev=purple
  - 26: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:329, 16:283, 17:155, 20:133, 33:79, 12:78, 26:73, 30:63, 34:60, 8:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=329 fs=1 fl=0 hz=0.005698005698005698, 16:ds=283 fs=2 fl=0 hz=0.006329113924050633, 17:ds=155 fs=19 fl=1 hz=0.024242424242424242, 20:ds=133 fs=14 fl=2 hz=0.01853997682502897, 33:ds=79 fs=24 fl=1 hz=0.027472527472527472, 12:ds=78 fs=45 fl=0 hz=0.04928806133625411, 26:ds=73 fs=2 fl=1 hz=0.006075334143377886, 30:ds=63 fs=39 fl=1 hz=0.04405286343612335, 34:ds=60 fs=14 fl=2 hz=0.019698725376593278, 8:ds=56 fs=39 fl=2 hz=0.044956140350877194

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=97 flags=red+purple
- S23: ds=74 flags=blue+purple
- S21: ds=71 flags=purple
- S4: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 136: score=4 tags=FLT,MIR,RS
  - 019: score=3 tags=FLT,RS
  - 028: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=2 last_repeat_gap=15 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=25), P2:7 (gap=21), P3:8 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=993 sev=B
- 333: ds=976 sev=B
- 255: ds=943 sev=B
- 355: ds=908 sev=B
- 466: ds=829 sev=B
- 446: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=59 sev=purple
  - 55: ds=37 sev=purple
  - 11: ds=27 sev=purple
  - 77: ds=20 sev=-
  - 88: ds=16 sev=-
  - 66: ds=11 sev=-
  - 44: ds=9 sev=-
  - 99: ds=3 sev=-
  - 33: ds=2 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 34: ds=68 sev=red
  - 07: ds=65 sev=red
  - 16: ds=51 sev=blue
  - 39: ds=39 sev=blue
  - 89: ds=39 sev=blue
  - 68: ds=35 sev=purple
  - 37: ds=34 sev=purple
  - 67: ds=34 sev=purple
  - 03: ds=32 sev=purple
  - 48: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:164, 34:159, 16:141, 27:96, 12:93, 14:78, 17:77, 20:66, 19:51, 24:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=164 fs=4 fl=3 hz=0.010432190760059612, 34:ds=159 fs=8 fl=4 hz=0.014423076923076924, 16:ds=141 fs=3 fl=0 hz=0.007462686567164179, 27:ds=96 fs=15 fl=2 hz=0.0189520624303233, 12:ds=93 fs=45 fl=0 hz=0.05079006772009029, 14:ds=78 fs=39 fl=0 hz=0.04276315789473684, 17:ds=77 fs=29 fl=2 hz=0.033879781420765025, 20:ds=66 fs=24 fl=3 hz=0.029315960912052113, 19:ds=51 fs=20 fl=2 hz=0.023732470334412083, 24:ds=41 fs=48 fl=0 hz=0.052805280528052806

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=75 flags=purple
- S25: ds=71 flags=purple
- S1: ds=60 flags=blue+purple
- S5: ds=58 flags=purple
- S8: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=52 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=15), P2:1 (gap=50), P3:9 (gap=37)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=50)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=900 sev=B
- 113: ds=851 sev=B
- 378: ds=844 sev=B
- 566: ds=833 sev=B
- 199: ds=825 sev=B
- 899: ds=803 sev=B
- 126: ds=799 sev=B
- 559: ds=794 sev=B
- 477: ds=783 sev=B
- 558: ds=749 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=229 sev=red
  - 22: ds=60 sev=purple
  - 00: ds=47 sev=purple
  - 44: ds=30 sev=purple
  - 11: ds=17 sev=-
  - 99: ds=15 sev=-
  - 88: ds=14 sev=-
  - 33: ds=12 sev=-
  - 77: ds=5 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 36: ds=72 sev=red
  - 24: ds=56 sev=red
  - 18: ds=50 sev=blue
  - 89: ds=50 sev=blue
  - 15: ds=49 sev=blue
  - 78: ds=48 sev=blue
  - 49: ds=42 sev=blue
  - 57: ds=39 sev=blue
  - 09: ds=29 sev=purple
  - 01: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:425, 1:340, 16:191, 26:123, 18:108, 17:101, 20:92, 3:71, 23:64, 33:62

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=425 fs=0 fl=2 hz=0.005366726296958855, 1:ds=340 fs=0 fl=0 hz=0.0, 16:ds=191 fs=3 fl=1 hz=0.007853403141361256, 26:ds=123 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=108 fs=16 fl=1 hz=0.019384264538198404, 17:ds=101 fs=13 fl=3 hz=0.018626309662398137, 20:ds=92 fs=15 fl=2 hz=0.01925254813137033, 3:ds=71 fs=15 fl=4 hz=0.02092511013215859, 23:ds=64 fs=25 fl=2 hz=0.03085714285714286, 33:ds=62 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=81 flags=purple
- S2: ds=71 flags=blue+purple
- S4: ds=69 flags=purple
- S25: ds=58 flags=purple
- S20: ds=51 flags=purple
- S9: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:693(B); evening:799(B)
- 128 -> combined:917(B); evening:900(B)
- 333 -> combined:744(B); midday:976(B)
- 477 -> combined:701(B); evening:783(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:54(blue); evening:27(purple); midday:27(purple)
- 11 -> combined:34(purple); midday:27(purple)
- 12 -> combined:31(purple); evening:27(purple)
- 15 -> combined:51(blue); evening:49(blue); midday:25(purple)
- 18 -> combined:45(blue); evening:50(blue)
- 22 -> combined:119(red); evening:60(purple); midday:59(purple)
- 24 -> combined:29(purple); evening:56(red)
- 55 -> combined:75(blue); evening:229(red); midday:37(purple)
- 67 -> combined:26(purple); midday:34(purple)
- 68 -> combined:52(blue); evening:26(purple); midday:35(purple)
- 69 -> combined:30(purple); midday:26(purple)
- 89 -> combined:79(red); evening:50(blue); midday:39(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.8301714285714286)[R1,XVAR-Cons(CM)], 8(3.3226)[R2,XVAR-Cons(CE)], 5(2.8444285714285718)[R3,XVAR-Cons(CM)], 9(1.1150357142857141)[R1,Mirror-Echo], 4(0.3513642857142857)[R3,Mirror-Echo]
- P2: 8(6.581035714285714)[R1,Mirror-Echo], 6(2.970557142857143)[R3,XVAR-Cons(CE)], 1(1.8684999999999998)[R1,Mirror-Echo], 3(1.2791428571428571)[R2,Mirror-Echo], 7(0.706392857142857)[R1,Mirror-Echo]
- P3: 8(3.9775714285714283)[R2,XVAR-Cons(CM)], 4(3.146807142857143)[R1,XVAR-Cons(CE)], 9(1.724392857142857)[R1,Mirror-Echo], 1(1.0252999999999999)[R2,Double-Pressure], 0(0.8716999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=20), P2:8(gap=18), P3:4(gap=19); top cartesian candidates: 888, 184, 188, 884, 189.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 127, 136, 019, 028, 145.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:693(B),evening:799(B); 128→combined:917(B),evening:900(B); 333→combined:744(B),midday:976(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:329, 16:283, 17:155, 20:133, 33:79.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=918 Evening=932; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 189 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 239 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 918 (canon 189): box `189` covers winner `918` (boxed hit).
  - Evening winner 932 (canon 239): box `239` covers winner `932` (boxed hit).
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
