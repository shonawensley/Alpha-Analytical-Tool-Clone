# Master Validation Run Report — Connecticut4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/Connecticut4/`
- Winners lens: `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2025-12-30/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2025-12-30/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2025-12-30/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2025-12-30/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2025-12-30/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2025-12-30/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/Connecticut4_vtrac22_winner_467_20260105_051146.html`
- `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_095_20260105_051145.html`

Winners JSON files:
- `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/Connecticut4_vtrac22_winner_467_20260105_051146.json`
- `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_095_20260105_051145.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 095 (canon 059): exact_boxed=True exact_straight=True | rank 42/4725 (rank_frac 0.009); Evening 467 (canon 467): exact_boxed=True exact_straight=True | rank 406/4725 (rank_frac 0.086)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 467 idx22 (rank 31/35, frac 0.886), 095 idx5 (rank 2/35, frac 0.057)
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

### 2.Stable — Connecticut4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2025-12-30)

## Midday winner 095 (canonical 059)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=24 | family_rows=224 | exact_boxed=24 | exact_straight=11 | vt_boxed=24
- Scores (patterns_scores.csv): rank 42/4725 (rank_frac 0.008888888888888889) | score 24.5 (top 46.5, ratio 0.5268817204301075, delta 22.0) | section Midday, Set Set1, Draw Draw4, Col 1, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat4|vstr2|mirror|hot2|perm2|hidden3v|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 23/1768 (rank_frac 0.013009049773755657) | score 41.5 (top 92.5, ratio 0.4486486486486487, delta 51.0) | section Midday, col1_hits 2, hot2 4, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x2|hot2x4|vstrx3
- Families (patterns_families.csv): count 70 | rank 2/1284 (rank_frac 0.001557632398753894) | score 32.5 (top 35.0, ratio 0.9285714285714286, delta 2.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=26

## Evening winner 467 (canonical 467)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=6 | family_rows=166 | exact_boxed=6 | exact_straight=6 | vt_boxed=6
- Scores (patterns_scores.csv): rank 406/4725 (rank_frac 0.08592592592592592) | score 17.5 (top 46.5, ratio 0.3763440860215054, delta 29.0) | section Evening, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 85/1768 (rank_frac 0.04807692307692308) | score 29.5 (top 92.5, ratio 0.31891891891891894, delta 63.0) | section Evening, col1_hits 1, hot2 2, set_chain 1, draw_chain 4 | why draw_chain4|col1x1|hot1x2|hot2x2|vstrx6
- Families (patterns_families.csv): count 43 | rank 44/1284 (rank_frac 0.03426791277258567) | score 24.5 (top 35.0, ratio 0.7, delta 10.5) | section Evening, hot2 8
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=49

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 039 | section Midday | score 59.0 | col1_hits 4 | hot2 9
- rank    5 | canon 116 | section Evening | score 57.0 | col1_hits 4 | hot2 8
- rank    1 | canon 011 | section Evening | score 92.5 | col1_hits 2 | hot2 7
- rank    7 | canon 114 | section Evening | score 54.0 | col1_hits 6 | hot2 7
- rank   10 | canon 1146 | section Evening | score 51.0 | col1_hits 4 | hot2 7
- rank   15 | canon 689 | section Combined | score 48.5 | col1_hits 3 | hot2 6
- rank   35 | canon 146 | section Evening | score 36.0 | col1_hits 3 | hot2 6
- rank   38 | canon 789 | section Combined | score 35.5 | col1_hits 4 | hot2 6
- rank   25 | canon 678 | section Combined | score 40.0 | col1_hits 3 | hot2 6
- rank   52 | canon 349 | section Combined | score 32.5 | col1_hits 3 | hot2 4

## Top families (patterns_families.csv)
- rank 1220 | family 22 | score 6.0 | hot2 0 | section Midday
- rank  638 | family 3 | score 14.0 | hot2 0 | section Midday
- rank  671 | family 31 | score 13.5 | hot2 0 | section Midday
- rank   44 | family 5 | score 24.5 | hot2 0 | section Midday
- rank  224 | family 28 | score 19.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 095 (canon 059): exact_boxed=True exact_straight=True | rank 42/4725 (rank_frac 0.009); Evening 467 (canon 467): exact_boxed=True exact_straight=True | rank 406/4725 (rank_frac 0.086)
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

### 2.Digit Reduction — Connecticut4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260105)

## Midday winner 095 (canonical 059)
- Stamp (winner_stamp.json): items_total=312 | exact_any=20 exact_final=0 | vtrac_any=312 vtrac_final=0 | drop_exact_any=63 drop_exact_final=0 | drop_vtrac_any=272 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=173 family_vtrac_final=0
- Flags (winner_flags.csv): rows=312 | exact_any=20 vtrac_any=312 | drop_exact_any=63 drop_vtrac_any=272 | family_exact_any=1 family_vtrac_any=173 | vt_boxed=141 vt_straight=0
- Hits (winner_hits.csv): rows=312 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=141 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=True | winner_best_rank=29 | winner_rank_fraction=1.1153846153846154 | winner_score_v2=7.697143 top_score_v2=13.377143 | winner_score_ratio_to_top=0.5753951348206414 winner_score_delta_from_top=5.680000000000001
- Reducer scores present: True

## Evening winner 467 (canonical 467)
- Stamp (winner_stamp.json): items_total=136 | exact_any=2 exact_final=0 | vtrac_any=122 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=124 drop_vtrac_final=0 | family_exact_any=3 family_exact_final=0 | family_vtrac_any=38 family_vtrac_final=0
- Flags (winner_flags.csv): rows=136 | exact_any=2 vtrac_any=122 | drop_exact_any=3 drop_vtrac_any=124 | family_exact_any=3 family_vtrac_any=38 | vt_boxed=124 vt_straight=0
- Hits (winner_hits.csv): rows=136 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=124 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 095 (canonical 059)
- Stamp (winner_stamp.json): items_total=732 | exact_any=20 exact_final=0 | vtrac_any=696 vtrac_final=0 | drop_exact_any=111 drop_exact_final=0 | drop_vtrac_any=620 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=389 family_vtrac_final=0
- Flags (winner_flags.csv): rows=732 | exact_any=20 vtrac_any=696 | drop_exact_any=111 drop_vtrac_any=620 | family_exact_any=1 family_vtrac_any=389 | vt_boxed=141 vt_straight=0
- Hits (winner_hits.csv): rows=732 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=141 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.914921 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 13.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.937143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 12.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 559 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 943 | score_v2 10.914921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 10.787143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 599 | score_v2 10.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 944 | score_v2 9.908571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 943 | score_v2 9.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 411 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 592 | score_v2 8.837143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 592 | score_v2 8.797143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 594 | score_v2 8.747143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 095 (canon 059): items_total=312 exact_any=20 vtrac_any=312 | top winner_present=True best_rank=29/26; Evening 467 (canon 467): items_total=136 exact_any=2 vtrac_any=122 | top winner_present=False best_rank=None/34; Combined 095 (canon 059): items_total=732 exact_any=20 vtrac_any=696 | top winner_present=False best_rank=None/28
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 943, 559, 599, 944.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_051458)

## Top indices (from enhanced JSON)
- index 4 | score 55.00047500000001 | features: presence=28.842975000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 54.21944750000001 | features: presence=34.25194750000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 13 | score 31.4199 | features: presence=15.3724, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 14 | score 30.815500000000004 | features: presence=18.578000000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 20.498808333333336 | features: presence=10.32985, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 33 | score 16.5292 | features: presence=8.761700000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 1 | score 16.059351666666664 | features: presence=9.465185, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 15.269500000000003 | features: presence=8.742000000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 29 | score 12.436699999999998 | features: presence=6.1692, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 11 | score 9.705549999999999 | features: presence=3.77805, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
540, 045, 054, 590, 059, 504, 093, 903, 083, 038

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 467 | index 22 | file Connecticut4_vtrac22_winner_467_20260105_051146.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 095 | index 5 | file Connecticut4_vtrac5_winner_095_20260105_051145.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 467 | index 22 rank 31/35 (rank_frac 0.8857142857142857) | score 0.0 (top 55.00047500000001, ratio 0.0, delta 55.00047500000001) | winner_in_index_straights=False | top_index_straights: (none)
- winner 095 | index 5 rank 2/35 (rank_frac 0.05714285714285714) | score 54.21944750000001 (top 55.00047500000001, ratio 0.9857996226396226, delta 0.7810275000000004) | winner_in_index_straights=False | top_index_straights: 540 (14.041), 045 (13.593), 054 (13.593)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 467→idx22 rank 31/35 (frac 0.886); 095→idx5 rank 2/35 (frac 0.057).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 4, 5, 13, 14, 15.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2025-12-30)

## Midday winner 095 (canonical 059)
- Top lanes (hot_zones_top_lanes.csv): present | rank 38/209 (rank_frac 0.18181818181818182) | score_mean 18.411 (top 24.673, ratio 0.7462002999229929, delta 6.261999999999997)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 467 (canonical 467)
- Top lanes (hot_zones_top_lanes.csv): present | rank 115/209 (rank_frac 0.5502392344497608) | score_mean 17.043 (top 24.673, ratio 0.6907550763993029, delta 7.629999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 24.673 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    2 | triad 277 | vt_triad 33 | score_mean 24.55 | tags hot16,literal_draw,straight_lane,vertical3,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 23.41 | tags col1,hot16,hot20,hot4,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 000 | vt_triad 1 | score_mean 21.92 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    5 | triad 112 | vt_triad 23 | score_mean 21.626 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 038 | vt_triad 144 | score_mean 20.659 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 011 | vt_triad 12 | score_mean 20.621 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 177 | vt_triad 23 | score_mean 20.568 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 055 | vt_triad 11 | score_mean 20.406 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 338 | vt_triad 44 | score_mean 20.336 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 095 (canon 059): rank 38/209 (rank_frac 0.182) ratio_to_top=0.7462002999229929; Evening 467 (canon 467): rank 115/209 (rank_frac 0.550) ratio_to_top=0.6907550763993029
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

Aux draws snapshot dir: `sharepacks/2025-12-30/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=055, 211, 279, 042, 083
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=211, 042, 261, 177, 893
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=055, 279, 083, 435, 829

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=1 streak=1 max=2 last_repeat_gap=27 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=30), P2:0 (gap=36), P3:0 (gap=27)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 355: ds=997 sev=B
- 777: ds=879 sev=B
- 129: ds=861 sev=B
- 288: ds=849 sev=B
- 136: ds=836 sev=B
- 149: ds=831 sev=B
- 445: ds=763 sev=B
- 114: ds=733 sev=B
- 069: ds=697 sev=B
- 888: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=81 sev=blue
  - 22: ds=69 sev=purple
  - 99: ds=62 sev=purple
  - 00: ds=32 sev=purple
  - 33: ds=19 sev=-
  - 88: ds=18 sev=-
  - 66: ds=17 sev=-
  - 77: ds=7 sev=-
  - 11: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 23: ds=82 sev=red
  - 69: ds=79 sev=red
  - 48: ds=68 sev=red
  - 78: ds=64 sev=red
  - 57: ds=63 sev=red
  - 49: ds=62 sev=red
  - 09: ds=59 sev=red
  - 19: ds=56 sev=red
  - 13: ds=48 sev=blue
  - 01: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:397, 32:164, 25:150, 29:123, 4:121, 15:109, 31:98, 34:93, 3:78, 27:77

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=397 fs=1 fl=2 hz=0.01098901098901099, 32:ds=164 fs=5 fl=3 hz=0.010830324909747294, 25:ds=150 fs=22 fl=2 hz=0.029055690072639227, 29:ds=123 fs=25 fl=1 hz=0.029988465974625143, 4:ds=121 fs=22 fl=2 hz=0.0273972602739726, 15:ds=109 fs=11 fl=4 hz=0.016910935738444193, 31:ds=98 fs=32 fl=0 hz=0.03665521191294387, 34:ds=93 fs=15 fl=2 hz=0.01951779563719862, 3:ds=78 fs=27 fl=0 hz=0.030337078651685393, 27:ds=77 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=99 flags=red+purple
- S23: ds=95 flags=purple
- S3: ds=72 flags=purple
- S24: ds=64 flags=blue+purple
- S22: ds=62 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 167: score=4 tags=FLT,MIR,RS
  - 059: score=3 tags=MIR,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=MIR,RS
  - 257: score=3 tags=MIR,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS
  - 014: score=2 tags=RS
  - 016: score=2 tags=FLT,MIR
  - 023: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=70 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=29), P2:0 (gap=23), P3:8 (gap=28)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=876 sev=B
- 478: ds=857 sev=B
- 459: ds=852 sev=B
- 159: ds=808 sev=B
- 099: ds=789 sev=B
- 127: ds=780 sev=B
- 559: ds=722 sev=B
- 004: ds=681 sev=B
- 155: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=88 sev=blue
  - 88: ds=48 sev=purple
  - 44: ds=40 sev=purple
  - 22: ds=34 sev=purple
  - 55: ds=25 sev=purple
  - 00: ds=21 sev=-
  - 33: ds=9 sev=-
  - 66: ds=8 sev=-
  - 77: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 23: ds=73 sev=red
  - 78: ds=66 sev=red
  - 13: ds=53 sev=blue
  - 49: ds=40 sev=blue
  - 19: ds=39 sev=blue
  - 69: ds=39 sev=blue
  - 48: ds=36 sev=purple
  - 57: ds=31 sev=purple
  - 79: ds=31 sev=purple
  - 09: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:198, 25:99, 31:88, 32:86, 18:83, 30:73, 3:71, 29:61, 4:60, 15:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=198 fs=3 fl=0 hz=0.008565310492505354, 25:ds=99 fs=21 fl=1 hz=0.025974025974025976, 31:ds=88 fs=21 fl=2 hz=0.025246981339187704, 32:ds=86 fs=3 fl=4 hz=0.009510869565217392, 18:ds=83 fs=23 fl=1 hz=0.026519337016574582, 30:ds=73 fs=35 fl=0 hz=0.03914988814317673, 3:ds=71 fs=22 fl=2 hz=0.02631578947368421, 29:ds=61 fs=18 fl=2 hz=0.023446658851113716, 4:ds=60 fs=26 fl=0 hz=0.02931228861330327, 15:ds=54 fs=24 fl=1 hz=0.02662406815761448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=82 flags=blue+purple
- S24: ds=79 flags=blue+purple
- S8: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 129: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=1 streak=1 max=3 last_repeat_gap=7 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=15), P2:0 (gap=18), P3:1 (gap=19)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=903 sev=B
- 668: ds=900 sev=B
- 399: ds=899 sev=B
- 044: ds=895 sev=B
- 133: ds=892 sev=B
- 145: ds=864 sev=B
- 677: ds=771 sev=B
- 333: ds=766 sev=B
- 112: ds=718 sev=B
- 344: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=110 sev=red
  - 22: ds=67 sev=purple
  - 99: ds=31 sev=purple
  - 77: ds=25 sev=purple
  - 66: ds=20 sev=-
  - 11: ds=19 sev=-
  - 33: ds=17 sev=-
  - 00: ds=16 sev=-
  - 88: ds=9 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 09: ds=62 sev=red
  - 57: ds=46 sev=blue
  - 69: ds=44 sev=blue
  - 23: ds=41 sev=blue
  - 25: ds=39 sev=blue
  - 06: ds=38 sev=blue
  - 07: ds=38 sev=blue
  - 01: ds=36 sev=purple
  - 48: ds=34 sev=purple
  - 78: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:309, 26:137, 4:120, 34:89, 32:82, 25:75, 29:63, 15:62, 2:52, 31:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=309 fs=2 fl=1 hz=0.005961251862891207, 26:ds=137 fs=3 fl=1 hz=0.008680555555555556, 4:ds=120 fs=19 fl=1 hz=0.022753128555176336, 34:ds=89 fs=14 fl=3 hz=0.019144144144144143, 32:ds=82 fs=2 fl=0 hz=0.008450704225352114, 25:ds=75 fs=21 fl=0 hz=0.023836549375709424, 29:ds=63 fs=27 fl=0 hz=0.030100334448160536, 15:ds=62 fs=15 fl=1 hz=0.019698725376593278, 2:ds=52 fs=23 fl=2 hz=0.028344671201814057, 31:ds=49 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=89 flags=blue+purple
- S8: ds=66 flags=red+purple
- S20: ds=49 flags=purple
- S3: ds=36 flags=blue+purple
- S24: ds=32 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:687(B); evening:892(B)
- 355 -> combined:997(B); evening:684(B)
- 445 -> combined:763(B); evening:687(B)
- 459 -> combined:672(B); midday:852(B)
- 888 -> combined:695(B); evening:695(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:37(blue); evening:36(purple)
- 06 -> combined:29(purple); evening:38(blue)
- 07 -> combined:29(purple); evening:38(blue)
- 09 -> combined:59(red); evening:62(red); midday:29(purple)
- 13 -> combined:48(blue); midday:53(blue)
- 19 -> combined:56(red); evening:28(purple); midday:39(blue)
- 22 -> combined:69(purple); evening:67(purple); midday:34(purple)
- 23 -> combined:82(red); evening:41(blue); midday:73(red)
- 25 -> combined:31(purple); evening:39(blue)
- 44 -> combined:81(blue); evening:110(red); midday:40(purple)
- 47 -> combined:25(purple); evening:25(purple)
- 48 -> combined:68(red); evening:34(purple); midday:36(purple)
- 49 -> combined:62(red); evening:31(purple); midday:40(blue)
- 57 -> combined:63(red); evening:46(blue); midday:31(purple)
- 69 -> combined:79(red); evening:44(blue); midday:39(blue)
- 78 -> combined:64(red); evening:32(purple); midday:66(red)
- 99 -> combined:62(purple); evening:31(purple); midday:88(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.781414285714286)[R1,XVAR-Cons(CEM)], 9(7.709557142857143)[R2,XVAR-Cons(CEM)], 3(1.9299428571428572)[R3,XVAR-Cons(CE)], 5(0.27153571428571427)[R3,Swap]
- P2: 0(8.324142857142856)[R1,XVAR-Cons(CEM)], 9(2.4592285714285715)[R2,XVAR-Cons(CE)], 2(2.362142857142857)[R3,XVAR-Cons(CM)], 6(0.9135)[R2,Double-Pressure], 3(0.22092142857142857)[R3,Swap]
- P3: 0(6.7576357142857155)[R1,XVAR-Cons(CEM)], 8(3.8019999999999996)[R2,XVAR-Cons(CM)], 4(2.8305857142857143)[R3,XVAR-Cons(CM)], 1(1.1672857142857143)[R1,Double-Pressure], 7(0.23122857142857145)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=30), P2:0(gap=36), P3:0(gap=27); top cartesian candidates: 700, 900, 708, 908, 704.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 167, 059, 068, 149, 257.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:687(B),evening:892(B); 355→combined:997(B),evening:684(B); 445→combined:763(B),evening:687(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:397, 32:164, 25:150, 29:123, 4:121.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=095 Evening=467; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 059 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 467 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 095 (canon 059): box `059` covers winner `095` (boxed hit).
  - Evening winner 467 (canon 467): box `467` covers winner `467` (boxed hit).
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
