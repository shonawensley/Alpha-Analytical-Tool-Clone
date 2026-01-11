# Master Validation Run Report — NorthCarolina4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-05/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-05/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-05/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-05/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-05/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-05/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac14_winner_895_20260110_035734.html`
- `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_553_20260110_035733.html`

Winners JSON files:
- `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac14_winner_895_20260110_035734.json`
- `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_553_20260110_035733.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 553 (canon 355): exact_boxed=True exact_straight=True | rank 2456/6169 (rank_frac 0.398); Evening 895 (canon 589): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 895 idx14 (rank 21/35, frac 0.600), 553 idx4 (rank 23/35, frac 0.657)
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

### 2.Stable — NorthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-05)

## Midday winner 553 (canonical 355)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=121 | exact_boxed=10 | exact_straight=10 | vt_boxed=10
- Scores (patterns_scores.csv): rank 2456/6169 (rank_frac 0.3981196304101151) | score 15.0 (top 40.0, ratio 0.375, delta 25.0) | section Evening, Set Set3, Draw Draw1, Col 4, hot 1, vt_straight 0.0 | why straight|cov1|hp_repeat4|hot1|double_mirror|set_chain3
- Compound (patterns_compound.csv): rank 267/1833 (rank_frac 0.14566284779050737) | score 26.0 (top 102.5, ratio 0.25365853658536586, delta 76.5) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|hot1x1|dblmirrorx10
- Families (patterns_families.csv): count 36 | rank 215/1567 (rank_frac 0.1372048500319081) | score 27.0 (top 39.5, ratio 0.6835443037974683, delta 12.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=23

## Evening winner 895 (canonical 589)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=373 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 49 | rank 240/1567 (rank_frac 0.15315890236119975) | score 26.0 (top 39.5, ratio 0.6582278481012658, delta 13.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=108
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 229 | section Midday | score 102.0 | col1_hits 9 | hot2 11
- rank    3 | canon 0229 | section Midday | score 92.5 | col1_hits 8 | hot2 11
- rank    5 | canon 022 | section Midday | score 91.0 | col1_hits 8 | hot2 11
- rank   12 | canon 226 | section Evening | score 81.0 | col1_hits 7 | hot2 11
- rank   15 | canon 22446 | section Evening | score 77.0 | col1_hits 7 | hot2 11
- rank   17 | canon 446 | section Evening | score 74.0 | col1_hits 7 | hot2 11
- rank   19 | canon 2246 | section Evening | score 71.0 | col1_hits 7 | hot2 11
- rank    1 | canon 229 | section Combined | score 102.5 | col1_hits 9 | hot2 11
- rank   12 | canon 226 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    4 | canon 299 | section Combined | score 91.5 | col1_hits 8 | hot2 11

## Top families (patterns_families.csv)
- rank 1486 | family 1 | score 7.0 | hot2 0 | section Midday
- rank 1039 | family 34 | score 13.5 | hot2 1 | section Midday
- rank  242 | family 12 | score 25.5 | hot2 0 | section Midday
- rank   84 | family 28 | score 30.5 | hot2 0 | section Midday
- rank 1447 | family 30 | score 8.0 | hot2 4 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 553 (canon 355): exact_boxed=True exact_straight=True | rank 2456/6169 (rank_frac 0.398); Evening 895 (canon 589): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260110)

## Midday winner 553 (canonical 355)
- Stamp (winner_stamp.json): items_total=102 | exact_any=0 exact_final=0 | vtrac_any=102 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=102 | exact_any=0 vtrac_any=102 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=90 vt_straight=0
- Hits (winner_hits.csv): rows=102 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=90 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=8 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=20.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 895 (canonical 589)
- Stamp (winner_stamp.json): items_total=38 | exact_any=0 exact_final=0 | vtrac_any=38 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=38 | exact_any=0 vtrac_any=38 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=38 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 553 (canonical 355)
- Stamp (winner_stamp.json): items_total=248 | exact_any=0 exact_final=0 | vtrac_any=248 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=248 | exact_any=0 vtrac_any=248 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=92 vt_straight=0
- Hits (winner_hits.csv): rows=248 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=92 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=19.337143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 922 | score_v2 20.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 922 | score_v2 20.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 922 | score_v2 19.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 4 | pattern 922 | score_v2 19.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 599 | score_v2 19.337143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 599 | score_v2 19.337143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 5 | pattern 599 | score_v2 19.337143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 599 | score_v2 19.308571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 599 | score_v2 19.308571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 599 | score_v2 19.308571 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 3 | pattern 922 | score_v2 19.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 599 | score_v2 19.058571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 922 | score_v2 20.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 599 | score_v2 19.337143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 19.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 992 | score_v2 18.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 592 | score_v2 18.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 922 | score_v2 17.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 992 | score_v2 17.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 992 | score_v2 15.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 15.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 599 | score_v2 14.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 11 | variant Combined | best_pattern 922 | score_v2 14.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Evening | best_pattern 224 | score_v2 14.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 553 (canon 355): items_total=102 exact_any=0 vtrac_any=102 | top winner_present=False best_rank=None/8; Evening 895 (canon 589): items_total=38 exact_any=0 vtrac_any=38 | top winner_present=False best_rank=None/22; Combined 553 (canon 355): items_total=248 exact_any=0 vtrac_any=248 | top winner_present=False best_rank=None/10
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 922, 599, 559, 992, 592.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260110_035935)

## Top indices (from enhanced JSON)
- index 28 | score 164.42193750000007 | features: presence=116.89443750000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 76.80036999999996 | features: presence=56.002869999999966, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 57.921617499999996 | features: presence=34.384117499999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 55.170765 | features: presence=36.793265000000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 41.49875000000001 | features: presence=29.851250000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 15.659684999999998 | features: presence=8.172185, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 19 | score 12.288608333333334 | features: presence=4.709650000000001, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 15 | score 11.632175000000002 | features: presence=5.264675000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 34 | score 11.28647 | features: presence=4.64897, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 5 | score 10.830600000000002 | features: presence=4.4731000000000005, set_echo=0.6, first_hit=0.2, column_span=0.0875

## Top straights (from enhanced JSON)
192, 294, 241, 264, 962, 291, 941, 471, 179, 719

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 895 | index 14 | file NorthCarolina4_vtrac14_winner_895_20260110_035734.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 553 | index 4 | file NorthCarolina4_vtrac4_winner_553_20260110_035733.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 895 | index 14 rank 21/35 (rank_frac 0.6) | score 4.948558333333333 (top 164.42193750000007, ratio 0.030096703691582096, delta 159.47337916666675) | winner_in_index_straights=False | top_index_straights: 584 (0.959), 548 (0.945), 845 (0.936)
- winner 553 | index 4 rank 23/35 (rank_frac 0.6571428571428571) | score 3.5535583333333336 (top 164.42193750000007, ratio 0.02161243437076839, delta 160.86837916666673) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 895→idx14 rank 21/35 (frac 0.600); 553→idx4 rank 23/35 (frac 0.657).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 31, 22, 25, 20.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-05)

## Midday winner 553 (canonical 355)
- Top lanes (hot_zones_top_lanes.csv): present | rank 25/206 (rank_frac 0.12135922330097088) | score_mean 18.157 (top 21.878, ratio 0.829920468050096, delta 3.721)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 895 (canonical 589)
- Top lanes (hot_zones_top_lanes.csv): present | rank 79/206 (rank_frac 0.38349514563106796) | score_mean 16.928 (top 21.878, ratio 0.7737453149282384, delta 4.949999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 338 | vt_triad 44 | score_mean 21.878 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 178 | vt_triad 234 | score_mean 21.055 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 347 | vt_triad 345 | score_mean 20.699 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 033 | vt_triad 14 | score_mean 20.527 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    5 | triad 244 | vt_triad 35 | score_mean 20.148 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 224 | vt_triad 35 | score_mean 19.877 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank    7 | triad 035 | vt_triad 114 | score_mean 19.782 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 788 | vt_triad 34 | score_mean 19.706 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    9 | triad 229 | vt_triad 35 | score_mean 19.68 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 226 | vt_triad 23 | score_mean 19.418 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 553 (canon 355): rank 25/206 (rank_frac 0.121) ratio_to_top=0.829920468050096; Evening 895 (canon 589): rank 79/206 (rank_frac 0.383) ratio_to_top=0.7737453149282384
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

Aux draws snapshot dir: `sharepacks/2026-01-05/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-05/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=887, 187, 178, 374, 383
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-05/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=187, 374, 033, 416, 867
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-05/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=887, 178, 383, 053, 057

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=2 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=34), P2:4 (gap=39), P3:2 (gap=36)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.639094285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=54.003015 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.38910285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.496964285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.860884999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 545: score=43.57747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 240: score=43.520628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=40.429221428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=40.067414285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.982902857142854 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=882 sev=B
- 446: ds=878 sev=B
- 445: ds=818 sev=B
- 122: ds=801 sev=B
- 036: ds=797 sev=B
- 555: ds=774 sev=B
- 299: ds=771 sev=B
- 277: ds=763 sev=B
- 112: ds=752 sev=B
- 034: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=158 sev=red
  - 77: ds=131 sev=red
  - 99: ds=54 sev=purple
  - 44: ds=52 sev=purple
  - 22: ds=18 sev=-
  - 11: ds=14 sev=-
  - 66: ds=13 sev=-
  - 55: ds=11 sev=-
  - 33: ds=4 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 56: ds=60 sev=red
  - 27: ds=56 sev=red
  - 02: ds=50 sev=blue
  - 23: ds=46 sev=blue
  - 09: ds=45 sev=blue
  - 28: ds=42 sev=blue
  - 04: ds=39 sev=blue
  - 06: ds=39 sev=blue
  - 29: ds=36 sev=purple
  - 24: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:486, 1:113, 27:109, 31:100, 15:84, 16:82, 10:72, 23:61, 35:52, 12:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=486 fs=3 fl=0 hz=0.009389671361502348, 1:ds=113 fs=0 fl=3 hz=0.00625, 27:ds=109 fs=15 fl=2 hz=0.02463768115942029, 31:ds=100 fs=19 fl=3 hz=0.02502844141069397, 15:ds=84 fs=16 fl=2 hz=0.019758507135016465, 16:ds=82 fs=4 fl=1 hz=0.008836524300441826, 10:ds=72 fs=21 fl=2 hz=0.027315914489311165, 23:ds=61 fs=17 fl=3 hz=0.024330900243309, 35:ds=52 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=50 fs=46 fl=1 hz=0.049893842887473464

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=94 flags=purple
- S4: ds=53 flags=purple
- S22: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '5', '6', '9'], 'pairs': {'remaining_count': 0}}
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
- current_index=21 streak=1 max=2 last_repeat_gap=99 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=38), P2:9 (gap=28), P3:2 (gap=41)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.639094285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=54.003015 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.38910285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.496964285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.860884999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 545: score=43.57747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 240: score=43.520628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=40.429221428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=40.067414285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.982902857142854 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=976 sev=B
- 123: ds=951 sev=B
- 446: ds=928 sev=B
- 777: ds=888 sev=B
- 119: ds=853 sev=B
- 222: ds=823 sev=B
- 155: ds=785 sev=B
- 488: ds=779 sev=B
- 177: ds=755 sev=B
- 007: ds=734 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=158 sev=red
  - 00: ds=133 sev=red
  - 77: ds=65 sev=purple
  - 99: ds=53 sev=purple
  - 22: ds=41 sev=purple
  - 11: ds=11 sev=-
  - 88: ds=7 sev=-
  - 66: ds=6 sev=-
  - 55: ds=5 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 48: ds=149 sev=red
  - 25: ds=62 sev=red
  - 07: ds=57 sev=red
  - 28: ds=49 sev=blue
  - 23: ds=44 sev=blue
  - 26: ds=44 sev=blue
  - 02: ds=41 sev=blue
  - 29: ds=38 sev=blue
  - 56: ds=32 sev=purple
  - 27: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:381, 25:189, 32:169, 35:143, 4:133, 11:108, 31:101, 2:97, 33:80, 12:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=381 fs=1 fl=0 hz=0.005905511811023622, 25:ds=189 fs=15 fl=1 hz=0.02165087956698241, 32:ds=169 fs=3 fl=1 hz=0.007416563658838071, 35:ds=143 fs=0 fl=2 hz=0.005201560468140442, 4:ds=133 fs=11 fl=3 hz=0.0166073546856465, 11:ds=108 fs=50 fl=0 hz=0.056882821387940846, 31:ds=101 fs=25 fl=0 hz=0.02793296089385475, 2:ds=97 fs=13 fl=3 hz=0.018223234624145785, 33:ds=80 fs=21 fl=2 hz=0.025136612021857924, 12:ds=58 fs=47 fl=0 hz=0.05181918412348401

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=92 flags=purple
- S20: ds=80 flags=red+purple
- S2: ds=71 flags=purple
- S5: ds=67 flags=purple
- S8: ds=62 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=23 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=17), P2:4 (gap=38), P3:5 (gap=23)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.639094285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=54.003015 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.38910285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.496964285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.860884999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 545: score=43.57747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 240: score=43.520628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=40.429221428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=40.067414285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.982902857142854 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=977 sev=B
- 299: ds=934 sev=B
- 223: ds=864 sev=B
- 122: ds=853 sev=B
- 116: ds=830 sev=B
- 039: ds=813 sev=B
- 377: ds=801 sev=B
- 277: ds=787 sev=B
- 188: ds=775 sev=B
- 557: ds=774 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=125 sev=red
  - 77: ds=83 sev=blue
  - 00: ds=79 sev=blue
  - 66: ds=41 sev=purple
  - 99: ds=27 sev=purple
  - 44: ds=26 sev=purple
  - 22: ds=9 sev=-
  - 11: ds=7 sev=-
  - 33: ds=2 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 45: ds=102 sev=red
  - 34: ds=43 sev=blue
  - 59: ds=42 sev=blue
  - 04: ds=38 sev=blue
  - 06: ds=32 sev=purple
  - 08: ds=31 sev=purple
  - 58: ds=31 sev=purple
  - 56: ds=30 sev=purple
  - 27: ds=28 sev=purple
  - 02: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:261, 26:243, 13:208, 1:150, 23:119, 5:100, 17:99, 27:56, 31:50, 14:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=261 fs=18 fl=0 hz=0.024896265560165977, 26:ds=243 fs=1 fl=2 hz=0.006666666666666667, 13:ds=208 fs=20 fl=0 hz=0.025284450063211127, 1:ds=150 fs=2 fl=3 hz=0.007434944237918215, 23:ds=119 fs=14 fl=3 hz=0.019384264538198404, 5:ds=100 fs=15 fl=2 hz=0.020809248554913295, 17:ds=99 fs=29 fl=0 hz=0.03553921568627451, 27:ds=56 fs=22 fl=3 hz=0.027085590465872156, 31:ds=50 fs=21 fl=2 hz=0.024338624338624337, 14:ds=48 fs=41 fl=1 hz=0.0445859872611465

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=93 flags=purple
- S0: ds=79 flags=blue+purple
- S4: ds=68 flags=purple
- S22: ds=48 flags=purple
- S2: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4', '6', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:797(B); evening:727(B)
- 122 -> combined:801(B); evening:853(B)
- 155 -> combined:882(B); midday:785(B)
- 277 -> combined:763(B); evening:787(B)
- 299 -> combined:771(B); evening:934(B)
- 446 -> combined:878(B); midday:928(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:158(red); evening:79(blue); midday:133(red)
- 02 -> combined:50(blue); evening:25(purple); midday:41(blue)
- 04 -> combined:39(blue); evening:38(blue)
- 06 -> combined:39(blue); evening:32(purple)
- 08 -> combined:29(purple); evening:31(purple)
- 09 -> combined:45(blue); evening:25(purple)
- 23 -> combined:46(blue); midday:44(blue)
- 25 -> combined:34(purple); midday:62(red)
- 27 -> combined:56(red); evening:28(purple); midday:29(purple)
- 28 -> combined:42(blue); midday:49(blue)
- 29 -> combined:36(purple); midday:38(blue)
- 44 -> combined:52(purple); evening:26(purple); midday:158(red)
- 48 -> combined:26(purple); midday:149(red)
- 56 -> combined:60(red); evening:30(purple); midday:32(purple)
- 59 -> combined:27(purple); evening:42(blue)
- 77 -> combined:131(red); evening:83(blue); midday:65(purple)
- 99 -> combined:54(purple); evening:27(purple); midday:53(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.9250428571428575)[R1,XVAR-Cons(CEM)], 2(3.399571428571429)[R3,XVAR-Cons(CM)], 7(0.9625999999999999)[R2,Double-Pressure], 6(0.46199999999999997)[R2], 4(0.2746642857142857)[R3,Swap]
- P2: 4(8.892100000000001)[R1,XVAR-Cons(CEM)], 0(3.9859)[R2,XVAR-Cons(CE)], 2(1.9829785714285717)[R3,XVAR-Cons(CM)], 9(1.6864999999999999)[R1,Mirror-Echo], 3(0.2581)[R3,Swap]
- P3: 2(8.5212)[R1,XVAR-Cons(CEM)], 0(6.228957142857142)[R2,XVAR-Cons(CEM)], 5(1.4483214285714285)[R1,Mirror-Echo], 8(0.5716)[R2,Swap], 1(0.198)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=34), P2:4(gap=39), P3:2(gap=36); top cartesian candidates: 542, 540, 242, 502, 500.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '5', '6', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:797(B),evening:727(B); 122→combined:801(B),evening:853(B); 155→combined:882(B),midday:785(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:486, 1:113, 27:109, 31:100, 15:84.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=553 Evening=895; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 355 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 589 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 553 (canon 355): box `355` covers winner `553` (boxed hit).
  - Evening winner 895 (canon 589): box `589` covers winner `895` (boxed hit).
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
