# Master Validation Run Report — Pennsylvania4 — results 2026-01-06 (history workbook ~ 2026-01-05)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-06/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-06/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-06/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-06/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-06/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-06/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-06/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac10_winner_757_20260107_052318.html`
- `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac24_winner_684_20260107_052316.html`

Winners JSON files:
- `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac10_winner_757_20260107_052318.json`
- `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac24_winner_684_20260107_052316.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-06/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 684 (canon 468): exact_boxed=True exact_straight=True | rank 829/5087 (rank_frac 0.163); Evening 757 (canon 577): exact_boxed=True exact_straight=True | rank 185/5087 (rank_frac 0.036)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 757 idx10 (rank 26/35, frac 0.743), 684 idx24 (rank 20/35, frac 0.571)
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

### 2.Stable — Pennsylvania4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-06)

## Midday winner 684 (canonical 468)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=8 | family_rows=69 | exact_boxed=8 | exact_straight=3 | vt_boxed=8
- Scores (patterns_scores.csv): rank 829/5087 (rank_frac 0.16296441910752898) | score 16.0 (top 35.5, ratio 0.4507042253521127, delta 19.5) | section Evening, Set Set1, Draw Draw3, Col 3, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat3|hot1|perm3|draw_chain4
- Compound (patterns_compound.csv): rank 392/2046 (rank_frac 0.19159335288367546) | score 19.5 (top 84.5, ratio 0.23076923076923078, delta 65.0) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 4 | why draw_chain4|hot1x1|vstrx1
- Families (patterns_families.csv): count 44 | rank 160/1255 (rank_frac 0.12749003984063745) | score 22.0 (top 33.0, ratio 0.6666666666666666, delta 11.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=122

## Evening winner 757 (canonical 577)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=18 | family_rows=278 | exact_boxed=18 | exact_straight=18 | vt_boxed=18
- Scores (patterns_scores.csv): rank 185/5087 (rank_frac 0.03636721053666208) | score 22.0 (top 35.5, ratio 0.6197183098591549, delta 13.5) | section Evening, Set Set1, Draw Draw4, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|double_mirror|vtrac_straight|set_chain3|draw_chain4
- Compound (patterns_compound.csv): rank 15/2046 (rank_frac 0.007331378299120235) | score 51.0 (top 84.5, ratio 0.6035502958579881, delta 33.5) | section Evening, col1_hits 4, hot2 4, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|col1x4|hot1x1|hot2x4|vstrx9|dblmirrorx11
- Families (patterns_families.csv): count 41 | rank 407/1255 (rank_frac 0.3243027888446215) | score 16.5 (top 33.0, ratio 0.5, delta 16.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=9

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 557 | section Evening | score 84.5 | col1_hits 7 | hot2 11
- rank    2 | canon 455 | section Evening | score 74.0 | col1_hits 6 | hot2 8
- rank    5 | canon 447 | section Evening | score 59.0 | col1_hits 5 | hot2 6
- rank    7 | canon 4455 | section Evening | score 54.5 | col1_hits 5 | hot2 6
- rank    9 | canon 118 | section Combined | score 54.0 | col1_hits 5 | hot2 6
- rank   17 | canon 1178 | section Combined | score 48.5 | col1_hits 5 | hot2 6
- rank    3 | canon 009 | section Midday | score 67.0 | col1_hits 5 | hot2 6
- rank    4 | canon 445 | section Evening | score 62.0 | col1_hits 5 | hot2 6
- rank    6 | canon 122 | section Combined | score 58.0 | col1_hits 3 | hot2 6
- rank   12 | canon 117 | section Combined | score 53.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1223 | family 29 | score 5.5 | hot2 0 | section Midday
- rank  593 | family 8 | score 14.0 | hot2 0 | section Midday
- rank  637 | family 21 | score 13.5 | hot2 0 | section Midday
- rank  673 | family 10 | score 13.0 | hot2 0 | section Midday
- rank  766 | family 1 | score 12.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): exact_boxed=True exact_straight=True | rank 829/5087 (rank_frac 0.163); Evening 757 (canon 577): exact_boxed=True exact_straight=True | rank 185/5087 (rank_frac 0.036)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260107)

## Midday winner 684 (canonical 468)
- Stamp (winner_stamp.json): items_total=45 | exact_any=0 exact_final=0 | vtrac_any=37 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=35 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=45 | exact_any=0 vtrac_any=37 | drop_exact_any=0 drop_vtrac_any=35 | family_exact_any=0 family_vtrac_any=12 | vt_boxed=27 vt_straight=0
- Hits (winner_hits.csv): rows=45 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=27 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 757 (canonical 577)
- Stamp (winner_stamp.json): items_total=39 | exact_any=3 exact_final=0 | vtrac_any=39 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=36 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=39 | exact_any=3 vtrac_any=39 | drop_exact_any=0 drop_vtrac_any=36 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=3 vt_straight=0
- Hits (winner_hits.csv): rows=39 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=3 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 684 (canonical 468)
- Stamp (winner_stamp.json): items_total=139 | exact_any=14 exact_final=0 | vtrac_any=131 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=52 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=139 | exact_any=14 vtrac_any=131 | drop_exact_any=0 drop_vtrac_any=52 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=90 vt_straight=0
- Hits (winner_hits.csv): rows=139 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=90 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 221 | score_v2 17.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 221 | score_v2 17.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 554 | score_v2 14.327143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 554 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 554 | score_v2 14.077143 | match_types 
- area_rank 2 | variant Evening | section Evening | set Set1 draw Draw4 col 3 | pattern 554 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 221 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 221 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 557 | score_v2 12.464643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 221 | score_v2 11.877143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 221 | score_v2 17.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 554 | score_v2 14.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 221 | score_v2 13.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 557 | score_v2 12.464643 | tags exact,vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 559 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 552 | score_v2 10.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 511 | score_v2 10.460476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 559 | score_v2 10.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 559 | score_v2 10.165714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 590 | score_v2 10.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): items_total=45 exact_any=0 vtrac_any=37 | top winner_present=False best_rank=None/20; Evening 757 (canon 577): items_total=39 exact_any=3 vtrac_any=39 | top winner_present=False best_rank=None/20; Combined 684 (canon 468): items_total=139 exact_any=14 vtrac_any=131 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 221, 554, 221, 557, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260107_052528)

## Top indices (from enhanced JSON)
- index 5 | score 45.568130000000004 | features: presence=31.170630000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 35.565997499999995 | features: presence=20.108497499999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 31.60201 | features: presence=22.174509999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 6 | score 28.776565 | features: presence=17.619065, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 7 | score 28.6408 | features: presence=21.7833, first_hit=0.4, column_span=0.3375, persistence=0.4
- index 9 | score 21.974930000000004 | features: presence=12.417430000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 8 | score 14.580608333333336 | features: presence=6.901650000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 14 | score 14.473700000000003 | features: presence=7.616200000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 14.230558333333336 | features: presence=7.901600000000003, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 34 | score 13.7508 | features: presence=8.393300000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
590, 059, 095, 021, 105, 056, 012, 561, 065, 615

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 757 | index 10 | file Pennsylvania4_vtrac10_winner_757_20260107_052318.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 684 | index 24 | file Pennsylvania4_vtrac24_winner_684_20260107_052316.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 757 | index 10 rank 26/35 (rank_frac 0.7428571428571429) | score 0.0 (top 45.568130000000004, ratio 0.0, delta 45.568130000000004) | winner_in_index_straights=False | top_index_straights: (none)
- winner 684 | index 24 rank 20/35 (rank_frac 0.5714285714285714) | score 4.865458333333333 (top 45.568130000000004, ratio 0.10677327187517531, delta 40.702671666666674) | winner_in_index_straights=False | top_index_straights: 193 (1.314), 986 (1.309), 198 (1.29)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 757→idx10 rank 26/35 (frac 0.743); 684→idx24 rank 20/35 (frac 0.571).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 5, 2, 15, 6, 7.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-06)

## Midday winner 684 (canonical 468)
- Top lanes (hot_zones_top_lanes.csv): present | rank 106/212 (rank_frac 0.5) | score_mean 17.261 (top 26.925, ratio 0.6410770659238625, delta 9.664000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 757 (canonical 577)
- Top lanes (hot_zones_top_lanes.csv): present | rank 147/212 (rank_frac 0.6933962264150944) | score_mean 16.5 (top 26.925, ratio 0.6128133704735376, delta 10.425)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 000 | vt_triad 1 | score_mean 26.925 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical4
- rank    2 | triad 249 | vt_triad 355 | score_mean 23.53 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 479 | vt_triad 355 | score_mean 23.13 | tags hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 006 | vt_triad 12 | score_mean 21.256 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 559 | vt_triad 15 | score_mean 21.157 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    6 | triad 447 | vt_triad 35 | score_mean 21.114 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    7 | triad 599 | vt_triad 15 | score_mean 20.786 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    8 | triad 059 | vt_triad 115 | score_mean 20.778 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 555 | vt_triad 1 | score_mean 20.625 | tags hot16,hot20,set1_bonus,superhot_set1
- rank   10 | triad 359 | vt_triad 145 | score_mean 20.529 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 684 (canon 468): rank 106/212 (rank_frac 0.500) ratio_to_top=0.6410770659238625; Evening 757 (canon 577): rank 147/212 (rank_frac 0.693) ratio_to_top=0.6128133704735376
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

Aux draws snapshot dir: `sharepacks/2026-01-06/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-06

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-06/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-05.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-06/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=600, 546, 980, 359, 909
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-06/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=546, 359, 744, 871, 322
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-06/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=600, 980, 909, 360, 328

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=3 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=18), P2:1 (gap=21), P3:7 (gap=23)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=40.73419464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 413: score=38.20585714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=37.80790714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 015: score=36.200607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=36.05064285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 017: score=35.65269285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=33.22096428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.69660857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 418: score=32.31641428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=32.268499999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 159: ds=890 sev=B
- 007: ds=887 sev=B
- 088: ds=851 sev=B
- 008: ds=829 sev=B
- 444: ds=805 sev=B
- 039: ds=780 sev=B
- 355: ds=770 sev=B
- 344: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=147 sev=red
  - 77: ds=86 sev=blue
  - 88: ds=85 sev=blue
  - 66: ds=73 sev=blue
  - 55: ds=50 sev=purple
  - 11: ds=35 sev=purple
  - 22: ds=9 sev=-
  - 44: ds=5 sev=-
  - 99: ds=4 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 07: ds=53 sev=blue
  - 69: ds=44 sev=blue
  - 34: ds=39 sev=blue
  - 19: ds=37 sev=blue
  - 15: ds=29 sev=purple
  - 57: ds=24 sev=-
  - 79: ds=24 sev=-
  - 27: ds=23 sev=-
  - 67: ds=23 sev=-
  - 58: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:289, 26:246, 16:104, 7:72, 6:67, 13:65, 19:61, 10:56, 1:50, 11:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=289 fs=2 fl=1 hz=0.007380073800738007, 26:ds=246 fs=0 fl=1 hz=0.003898635477582846, 16:ds=104 fs=3 fl=2 hz=0.007371007371007371, 7:ds=72 fs=35 fl=1 hz=0.04, 6:ds=67 fs=21 fl=1 hz=0.025611175785797437, 13:ds=65 fs=21 fl=1 hz=0.024553571428571428, 19:ds=61 fs=21 fl=3 hz=0.025695931477516063, 10:ds=56 fs=23 fl=2 hz=0.02676659528907923, 1:ds=50 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=47 fs=48 fl=0 hz=0.05128205128205128

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=98 flags=purple
- S20: ds=85 flags=purple
- S25: ds=62 flags=purple
- S4: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '7'], 'pairs': {'remaining_count': 0}}
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
- current_index=9 streak=1 max=3 last_repeat_gap=37 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=26), P2:9 (gap=13), P3:5 (gap=31)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=40.73419464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 413: score=38.20585714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=37.80790714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 015: score=36.200607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=36.05064285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 017: score=35.65269285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=33.22096428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.69660857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 418: score=32.31641428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=32.268499999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=981 sev=B
- 288: ds=968 sev=B
- 255: ds=939 sev=B
- 668: ds=921 sev=B
- 199: ds=869 sev=B
- 499: ds=795 sev=B
- 399: ds=778 sev=B
- 039: ds=766 sev=B
- 448: ds=755 sev=B
- 005: ds=747 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=190 sev=red
  - 99: ds=137 sev=red
  - 77: ds=80 sev=blue
  - 33: ds=73 sev=blue
  - 88: ds=42 sev=purple
  - 66: ds=36 sev=purple
  - 11: ds=17 sev=-
  - 00: ds=16 sev=-
  - 22: ds=4 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 79: ds=77 sev=red
  - 12: ds=52 sev=blue
  - 06: ds=47 sev=blue
  - 69: ds=34 sev=purple
  - 13: ds=29 sev=purple
  - 57: ds=28 sev=purple
  - 03: ds=27 sev=purple
  - 07: ds=26 sev=purple
  - 09: ds=22 sev=-
  - 37: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:379, 1:364, 34:218, 16:176, 15:167, 32:144, 35:121, 28:66, 5:51, 2:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=379 fs=0 fl=0 hz=0.0, 1:ds=364 fs=2 fl=2 hz=0.009124087591240877, 34:ds=218 fs=19 fl=1 hz=0.02631578947368421, 16:ds=176 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=167 fs=23 fl=0 hz=0.029411764705882353, 32:ds=144 fs=3 fl=1 hz=0.006720430107526881, 35:ds=121 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=66 fs=26 fl=1 hz=0.03515625, 5:ds=51 fs=18 fl=2 hz=0.022175290390707498, 2:ds=47 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=98 flags=red+purple
- S22: ds=83 flags=purple
- S23: ds=71 flags=purple
- S3: ds=65 flags=blue+purple

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
- current_index=2 streak=1 max=3 last_repeat_gap=67 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=33), P2:1 (gap=39), P3:6 (gap=23)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=40.73419464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 413: score=38.20585714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=37.80790714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 015: score=36.200607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=36.05064285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 017: score=35.65269285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=33.22096428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=32.69660857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 418: score=32.31641428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=32.268499999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=977 sev=B
- 009: ds=935 sev=B
- 255: ds=893 sev=B
- 138: ds=833 sev=B
- 117: ds=816 sev=B
- 158: ds=778 sev=B
- 344: ds=771 sev=B
- 199: ds=762 sev=B
- 112: ds=722 sev=B
- 277: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=132 sev=red
  - 33: ds=74 sev=blue
  - 44: ds=45 sev=purple
  - 77: ds=43 sev=purple
  - 66: ds=41 sev=purple
  - 11: ds=32 sev=purple
  - 55: ds=25 sev=purple
  - 22: ds=5 sev=-
  - 99: ds=2 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 68: ds=90 sev=red
  - 07: ds=67 sev=red
  - 15: ds=55 sev=blue
  - 78: ds=40 sev=blue
  - 19: ds=39 sev=blue
  - 01: ds=33 sev=purple
  - 18: ds=33 sev=purple
  - 14: ds=32 sev=purple
  - 39: ds=30 sev=purple
  - 16: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:621, 23:160, 26:123, 18:120, 13:69, 33:54, 16:52, 30:51, 24:48, 27:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=621 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=160 fs=17 fl=2 hz=0.025165562913907286, 26:ds=123 fs=2 fl=1 hz=0.0056657223796034, 18:ds=120 fs=23 fl=2 hz=0.02910360884749709, 13:ds=69 fs=20 fl=1 hz=0.024881516587677725, 33:ds=54 fs=18 fl=3 hz=0.023076923076923075, 16:ds=52 fs=5 fl=3 hz=0.009523809523809525, 30:ds=51 fs=35 fl=1 hz=0.03829787234042553, 24:ds=48 fs=37 fl=0 hz=0.04048140043763676, 27:ds=40 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=93 flags=blue+purple
- S1: ds=78 flags=blue+purple
- S24: ds=61 flags=blue+purple
- S3: ds=49 flags=purple
- S20: ds=43 flags=purple
- S25: ds=31 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '5', '7'], 'pairs': {'remaining_count': 0}}
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
  - 025: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:780(B); midday:766(B)
- 199 -> evening:762(B); midday:869(B)
- 255 -> evening:893(B); midday:939(B)
- 344 -> combined:699(B); evening:771(B)
- 444 -> combined:805(B); evening:977(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:53(blue); evening:67(red); midday:26(purple)
- 11 -> combined:35(purple); evening:32(purple)
- 15 -> combined:29(purple); evening:55(blue)
- 19 -> combined:37(blue); evening:39(blue)
- 33 -> combined:147(red); evening:74(blue); midday:73(blue)
- 34 -> combined:39(blue); evening:27(purple)
- 55 -> combined:50(purple); evening:25(purple); midday:190(red)
- 66 -> combined:73(blue); evening:41(purple); midday:36(purple)
- 69 -> combined:44(blue); midday:34(purple)
- 77 -> combined:86(blue); evening:43(purple); midday:80(blue)
- 88 -> combined:85(blue); evening:132(red); midday:42(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(3.8952857142857145)[R2,XVAR-Cons(CM)], 0(2.7400714285714285)[R1,XVAR-Cons(CM)], 8(1.6552857142857142)[R1,Double-Pressure], 9(1.4290571428571428)[R2,Mirror-Echo], 7(0.9552999999999999)[R2,Double-Pressure]
- P2: 1(7.9389642857142855)[R1,XVAR-Cons(CEM)], 9(3.498142857142857)[R2,XVAR-Cons(CM)], 3(2.7928428571428574)[R3,XVAR-Cons(CE)], 5(0.3687142857142857)[R3,Swap], 6(0.3159214285714286)[R3,Mirror-Echo]
- P3: 5(4.021571428571429)[R2,XVAR-Cons(CM)], 7(3.4736571428571428)[R1,XVAR-Cons(CE)], 3(2.871607142857143)[R3,XVAR-Cons(CM)], 6(1.3867142857142856)[R1,Double-Pressure], 8(0.4821642857142857)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-05.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=18), P2:1(gap=21), P3:7(gap=23); top cartesian candidates: 415, 413, 417, 015, 013.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:780(B),midday:766(B); 199→midday:869(B),evening:762(B); 255→midday:939(B),evening:893(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:289, 26:246, 16:104, 7:72, 6:67.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=684 Evening=757; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 468 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 577 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 684 (canon 468): box `468` covers winner `684` (boxed hit).
  - Evening winner 757 (canon 577): box `577` covers winner `757` (boxed hit).
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
