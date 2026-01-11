# Master Validation Run Report — NorthCarolina4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-07/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-07/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-07/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-07/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-07/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-07/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac10_winner_202_20260110_033430.html`
- `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac24_winner_184_20260110_033428.html`

Winners JSON files:
- `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac10_winner_202_20260110_033430.json`
- `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac24_winner_184_20260110_033428.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 184 (canon 148): exact_boxed=True exact_straight=True | rank 2714/6800 (rank_frac 0.399); Evening 202 (canon 022): exact_boxed=True exact_straight=True | rank 600/6800 (rank_frac 0.088)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 202 idx10 (rank 13/35, frac 0.371), 184 idx24 (rank 24/35, frac 0.686)
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

### 2.Stable — NorthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-07)

## Midday winner 184 (canonical 148)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=5 | family_rows=83 | exact_boxed=5 | exact_straight=5 | vt_boxed=5
- Scores (patterns_scores.csv): rank 2714/6800 (rank_frac 0.3991176470588235) | score 15.5 (top 39.5, ratio 0.3924050632911392, delta 24.0) | section Midday, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 285/1754 (rank_frac 0.16248574686431014) | score 26.0 (top 112.0, ratio 0.23214285714285715, delta 86.0) | section Midday, col1_hits 2, hot2 2, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|hot2x2|vstrx5
- Families (patterns_families.csv): count 57 | rank 367/1719 (rank_frac 0.2134962187318208) | score 24.0 (top 38.0, ratio 0.631578947368421, delta 14.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=123

## Evening winner 202 (canonical 022)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=25 | family_rows=471 | exact_boxed=25 | exact_straight=25 | vt_boxed=25
- Scores (patterns_scores.csv): rank 600/6800 (rank_frac 0.08823529411764706) | score 22.0 (top 39.5, ratio 0.5569620253164557, delta 17.5) | section Midday, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat5|hot2|double_mirror|vtrac_straight|set_chain3|draw_chain4
- Compound (patterns_compound.csv): rank 20/1754 (rank_frac 0.011402508551881414) | score 70.0 (top 112.0, ratio 0.625, delta 42.0) | section Midday, col1_hits 2, hot2 5, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|col1x2|hot1x13|hot2x5|vstrx14|dblmirrorx25
- Families (patterns_families.csv): count 59 | rank 548/1719 (rank_frac 0.31878999418266435) | score 20.5 (top 38.0, ratio 0.5394736842105263, delta 17.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=5

## Top compound candidates (patterns_compound.csv)
- rank    9 | canon 0299 | section Midday | score 80.5 | col1_hits 8 | hot2 11
- rank    8 | canon 099 | section Midday | score 84.5 | col1_hits 8 | hot2 11
- rank    4 | canon 299 | section Midday | score 91.5 | col1_hits 8 | hot2 11
- rank    5 | canon 446 | section Evening | score 88.0 | col1_hits 7 | hot2 11
- rank    1 | canon 244 | section Evening | score 112.0 | col1_hits 9 | hot2 11
- rank   16 | canon 0066 | section Combined | score 75.5 | col1_hits 7 | hot2 11
- rank   12 | canon 004 | section Combined | score 78.5 | col1_hits 7 | hot2 11
- rank    7 | canon 006 | section Combined | score 85.5 | col1_hits 7 | hot2 11
- rank    3 | canon 066 | section Combined | score 94.5 | col1_hits 8 | hot2 11
- rank   51 | canon 14466 | section Evening | score 49.5 | col1_hits 4 | hot2 8

## Top families (patterns_families.csv)
- rank 1701 | family 1 | score 5.0 | hot2 0 | section Midday
- rank 1630 | family 14 | score 8.0 | hot2 0 | section Midday
- rank  130 | family 28 | score 30.0 | hot2 0 | section Midday
- rank 1717 | family 11 | score 3.0 | hot2 0 | section Midday
- rank 1707 | family 2 | score 4.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 184 (canon 148): exact_boxed=True exact_straight=True | rank 2714/6800 (rank_frac 0.399); Evening 202 (canon 022): exact_boxed=True exact_straight=True | rank 600/6800 (rank_frac 0.088)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260110)

## Midday winner 184 (canonical 148)
- Stamp (winner_stamp.json): items_total=173 | exact_any=58 exact_final=0 | vtrac_any=166 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=106 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=11 family_vtrac_final=0
- Flags (winner_flags.csv): rows=173 | exact_any=58 vtrac_any=166 | drop_exact_any=0 drop_vtrac_any=106 | family_exact_any=0 family_vtrac_any=11 | vt_boxed=173 vt_straight=0
- Hits (winner_hits.csv): rows=173 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=173 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=8 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 202 (canonical 022)
- Stamp (winner_stamp.json): items_total=96 | exact_any=0 exact_final=0 | vtrac_any=60 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=96 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=24 family_vtrac_final=0
- Flags (winner_flags.csv): rows=96 | exact_any=0 vtrac_any=60 | drop_exact_any=0 drop_vtrac_any=96 | family_exact_any=0 family_vtrac_any=24 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=96 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 184 (canonical 148)
- Stamp (winner_stamp.json): items_total=210 | exact_any=58 exact_final=0 | vtrac_any=199 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=120 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=18 family_vtrac_final=0
- Flags (winner_flags.csv): rows=210 | exact_any=58 vtrac_any=199 | drop_exact_any=0 drop_vtrac_any=120 | family_exact_any=0 family_vtrac_any=18 | vt_boxed=190 vt_straight=0
- Hits (winner_hits.csv): rows=210 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=190 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 440 | score_v2 17.027143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 440 | score_v2 16.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 440 | score_v2 16.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 440 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 992 | score_v2 12.927143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 440 | score_v2 12.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 440 | score_v2 12.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 5 | pattern 992 | score_v2 12.677143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 12.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 992 | score_v2 12.427143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 440 | score_v2 17.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 440 | score_v2 13.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 992 | score_v2 12.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 992 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 559 | score_v2 11.070476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 10.082597 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 224 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 9.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 922 | score_v2 9.837143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 992 | score_v2 9.264921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 184 (canon 148): items_total=173 exact_any=58 vtrac_any=166 | top winner_present=False best_rank=None/8; Evening 202 (canon 022): items_total=96 exact_any=0 vtrac_any=60 | top winner_present=False best_rank=None/18; Combined 184 (canon 148): items_total=210 exact_any=58 vtrac_any=199 | top winner_present=False best_rank=None/12
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 440, 440, 992, 992, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260110_033917)

## Top indices (from enhanced JSON)
- index 28 | score 155.414915 | features: presence=113.857415, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 109.08710749999996 | features: presence=80.54960749999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 62.37559249999997 | features: presence=43.87809249999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 47.408367500000004 | features: presence=34.69086750000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 45.08644 | features: presence=31.918940000000006, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 19 | score 44.450160000000004 | features: presence=29.242660000000004, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 25 | score 43.805510000000005 | features: presence=28.90801000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 42.398199999999996 | features: presence=29.2307, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 40.225649999999995 | features: presence=26.348149999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 33.382925 | features: presence=21.9673, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
924, 240, 092, 290, 264, 245, 624, 964, 920, 259

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 202 | index 10 | file NorthCarolina4_vtrac10_winner_202_20260110_033430.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 184 | index 24 | file NorthCarolina4_vtrac24_winner_184_20260110_033428.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 202 | index 10 rank 13/35 (rank_frac 0.37142857142857144) | score 21.880585 (top 155.414915, ratio 0.14078819269051493, delta 133.53433) | winner_in_index_straights=False | top_index_straights: (none)
- winner 184 | index 24 rank 24/35 (rank_frac 0.6857142857142857) | score 5.711458333333333 (top 155.414915, ratio 0.036749743956899714, delta 149.70345666666668) | winner_in_index_straights=False | top_index_straights: 634 (1.535), 436 (1.243), 963 (0.875)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 202→idx10 rank 13/35 (frac 0.371); 184→idx24 rank 24/35 (frac 0.686).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 31, 15, 5, 6.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-07)

## Midday winner 184 (canonical 148)
- Top lanes (hot_zones_top_lanes.csv): present | rank 142/204 (rank_frac 0.696078431372549) | score_mean 15.048 (top 24.044, ratio 0.6258526035601397, delta 8.996)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 202 (canonical 022)
- Top lanes (hot_zones_top_lanes.csv): present | rank 38/204 (rank_frac 0.18627450980392157) | score_mean 17.563 (top 24.044, ratio 0.7304525037431375, delta 6.481000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 338 | vt_triad 44 | score_mean 24.044 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 355 | vt_triad 14 | score_mean 22.327 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 038 | vt_triad 144 | score_mean 20.788 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2
- rank    4 | triad 224 | vt_triad 35 | score_mean 20.125 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank    5 | triad 388 | vt_triad 44 | score_mean 19.917 | tags hot16,hot20,set1_bonus
- rank    6 | triad 244 | vt_triad 35 | score_mean 19.833 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 788 | vt_triad 34 | score_mean 19.716 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_straight
- rank    8 | triad 255 | vt_triad 13 | score_mean 19.713 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    9 | triad 229 | vt_triad 35 | score_mean 19.678 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 378 | vt_triad 344 | score_mean 19.363 | tags hot16,hot20,set1_bonus,straight_lane,vertical1

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 184 (canon 148): rank 142/204 (rank_frac 0.696) ratio_to_top=0.6258526035601397; Evening 202 (canon 022): rank 38/204 (rank_frac 0.186) ratio_to_top=0.7304525037431375
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

Aux draws snapshot dir: `sharepacks/2026-01-07/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-07/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=298, 552, 895, 553, 887
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-07/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=552, 553, 187, 374, 033
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-07/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=298, 895, 887, 178, 383

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=6 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=25), P2:4 (gap=43), P3:0 (gap=34)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.23381142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.67075714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 941: score=36.31120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 900: score=35.85797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=35.77865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=35.32541428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=32.80869285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 942: score=32.637685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=32.276135714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 642: score=32.10512857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=886 sev=B
- 446: ds=882 sev=B
- 445: ds=822 sev=B
- 122: ds=805 sev=B
- 036: ds=801 sev=B
- 555: ds=778 sev=B
- 299: ds=775 sev=B
- 277: ds=767 sev=B
- 112: ds=756 sev=B
- 034: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=162 sev=red
  - 77: ds=135 sev=red
  - 99: ds=58 sev=purple
  - 44: ds=56 sev=purple
  - 22: ds=22 sev=-
  - 11: ds=18 sev=-
  - 66: ds=17 sev=-
  - 33: ds=8 sev=-
  - 88: ds=4 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 56: ds=64 sev=red
  - 27: ds=60 sev=red
  - 02: ds=54 sev=blue
  - 23: ds=50 sev=blue
  - 09: ds=49 sev=blue
  - 04: ds=43 sev=blue
  - 06: ds=43 sev=blue
  - 24: ds=39 sev=blue
  - 12: ds=38 sev=blue
  - 01: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:490, 1:117, 27:113, 31:104, 15:88, 16:86, 10:76, 23:65, 35:56, 12:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=490 fs=3 fl=0 hz=0.009389671361502348, 1:ds=117 fs=0 fl=3 hz=0.00625, 27:ds=113 fs=15 fl=2 hz=0.02463768115942029, 31:ds=104 fs=19 fl=3 hz=0.02502844141069397, 15:ds=88 fs=16 fl=2 hz=0.019758507135016465, 16:ds=86 fs=4 fl=1 hz=0.008836524300441826, 10:ds=76 fs=21 fl=2 hz=0.027315914489311165, 23:ds=65 fs=17 fl=3 hz=0.024330900243309, 35:ds=56 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=54 fs=46 fl=1 hz=0.049893842887473464

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=98 flags=purple
- S4: ds=57 flags=purple
- S7: ds=39 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 027: score=3 tags=FLT,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=2 last_repeat_gap=101 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=40), P2:9 (gap=30), P3:8 (gap=26)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.23381142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.67075714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 941: score=36.31120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 900: score=35.85797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=35.77865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=35.32541428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=32.80869285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 942: score=32.637685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=32.276135714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 642: score=32.10512857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=978 sev=B
- 123: ds=953 sev=B
- 446: ds=930 sev=B
- 777: ds=890 sev=B
- 119: ds=855 sev=B
- 222: ds=825 sev=B
- 155: ds=787 sev=B
- 488: ds=781 sev=B
- 177: ds=757 sev=B
- 007: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=160 sev=red
  - 00: ds=135 sev=red
  - 77: ds=67 sev=purple
  - 99: ds=55 sev=purple
  - 22: ds=43 sev=purple
  - 11: ds=13 sev=-
  - 88: ds=9 sev=-
  - 66: ds=8 sev=-
  - 33: ds=4 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 48: ds=151 sev=red
  - 07: ds=59 sev=red
  - 28: ds=51 sev=blue
  - 23: ds=46 sev=blue
  - 26: ds=46 sev=blue
  - 02: ds=43 sev=blue
  - 29: ds=40 sev=blue
  - 56: ds=34 sev=purple
  - 27: ds=31 sev=purple
  - 38: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:383, 25:191, 32:171, 35:145, 11:110, 31:103, 2:99, 33:82, 12:60, 1:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=383 fs=1 fl=0 hz=0.005905511811023622, 25:ds=191 fs=15 fl=1 hz=0.02165087956698241, 32:ds=171 fs=3 fl=1 hz=0.007416563658838071, 35:ds=145 fs=0 fl=2 hz=0.005201560468140442, 11:ds=110 fs=50 fl=0 hz=0.056882821387940846, 31:ds=103 fs=25 fl=0 hz=0.02793296089385475, 2:ds=99 fs=13 fl=3 hz=0.018223234624145785, 33:ds=82 fs=21 fl=2 hz=0.025136612021857924, 12:ds=60 fs=47 fl=0 hz=0.05181918412348401, 1:ds=58 fs=2 fl=2 hz=0.00641025641025641

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=94 flags=purple
- S20: ds=82 flags=red+purple
- S2: ds=73 flags=purple
- S5: ds=69 flags=purple
- S8: ds=64 flags=purple

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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=25 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=19), P2:4 (gap=40), P3:2 (gap=20)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:4 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.23381142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.67075714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 941: score=36.31120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 900: score=35.85797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=35.77865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=35.32541428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=32.80869285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 942: score=32.637685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=32.276135714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 642: score=32.10512857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=979 sev=B
- 299: ds=936 sev=B
- 223: ds=866 sev=B
- 122: ds=855 sev=B
- 116: ds=832 sev=B
- 039: ds=815 sev=B
- 377: ds=803 sev=B
- 277: ds=789 sev=B
- 188: ds=777 sev=B
- 557: ds=776 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=127 sev=red
  - 77: ds=85 sev=blue
  - 00: ds=81 sev=blue
  - 66: ds=43 sev=purple
  - 99: ds=29 sev=purple
  - 44: ds=28 sev=purple
  - 22: ds=11 sev=-
  - 11: ds=9 sev=-
  - 33: ds=4 sev=-
  - 88: ds=2 sev=-
- non_repeating:
  - 45: ds=104 sev=red
  - 34: ds=45 sev=blue
  - 04: ds=40 sev=blue
  - 06: ds=34 sev=purple
  - 08: ds=33 sev=purple
  - 56: ds=32 sev=purple
  - 27: ds=30 sev=purple
  - 02: ds=27 sev=purple
  - 09: ds=27 sev=purple
  - 23: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:263, 26:245, 13:210, 1:152, 23:121, 5:102, 17:101, 27:58, 31:52, 15:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=263 fs=18 fl=0 hz=0.024896265560165977, 26:ds=245 fs=1 fl=2 hz=0.006666666666666667, 13:ds=210 fs=19 fl=0 hz=0.024675324675324673, 1:ds=152 fs=2 fl=3 hz=0.007434944237918215, 23:ds=121 fs=14 fl=3 hz=0.019384264538198404, 5:ds=102 fs=15 fl=2 hz=0.020809248554913295, 17:ds=101 fs=29 fl=0 hz=0.03553921568627451, 27:ds=58 fs=22 fl=3 hz=0.027085590465872156, 31:ds=52 fs=21 fl=2 hz=0.024338624338624337, 15:ds=44 fs=16 fl=1 hz=0.01829924650161464

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=95 flags=purple
- S0: ds=81 flags=blue+purple
- S4: ds=70 flags=purple
- S2: ds=49 flags=purple
- S21: ds=36 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '4', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:801(B); evening:729(B)
- 122 -> combined:805(B); evening:855(B)
- 155 -> combined:886(B); midday:787(B)
- 277 -> combined:767(B); evening:789(B)
- 299 -> combined:775(B); evening:936(B)
- 446 -> combined:882(B); midday:930(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:162(red); evening:81(blue); midday:135(red)
- 02 -> combined:54(blue); evening:27(purple); midday:43(blue)
- 04 -> combined:43(blue); evening:40(blue)
- 06 -> combined:43(blue); evening:34(purple)
- 08 -> combined:33(purple); evening:33(purple)
- 09 -> combined:49(blue); evening:27(purple)
- 23 -> combined:50(blue); evening:25(purple); midday:46(blue)
- 27 -> combined:60(red); evening:30(purple); midday:31(purple)
- 44 -> combined:56(purple); evening:28(purple); midday:160(red)
- 48 -> combined:30(purple); midday:151(red)
- 56 -> combined:64(red); evening:32(purple); midday:34(purple)
- 77 -> combined:135(red); evening:85(blue); midday:67(purple)
- 99 -> combined:58(purple); evening:29(purple); midday:55(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.3795)[R2,XVAR-Cons(CM)], 6(2.846942857142857)[R1,XVAR-Cons(CM)], 7(2.6148285714285713)[R3,XVAR-Cons(CE)], 2(1.7449999999999999)[R1,Double-Pressure], 5(1.2372857142857143)[R1,Double-Pressure]
- P2: 4(8.961042857142857)[R1,XVAR-Cons(CEM)], 0(4.1157)[R2,XVAR-Cons(CE)], 2(2.0664214285714286)[R3,XVAR-Cons(CM)], 9(1.7952142857142857)[R1,Mirror-Echo], 3(0.2849714285714286)[R3,Swap]
- P3: 0(7.862771428571428)[R1,XVAR-Cons(CEM)], 1(2.4706642857142858)[R2,XVAR-Cons(CM)], 2(1.2971428571428572)[R1,Double-Pressure], 8(0.8462857142857143)[R1,Swap], 9(0.29800000000000004)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=25), P2:4(gap=43), P3:0(gap=34); top cartesian candidates: 940, 640, 941, 900, 641.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '4', '6'], 'pairs': {'remaining_count': 0}}; top candidates: 018, 027, 036, 045, 126.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:801(B),evening:729(B); 122→combined:805(B),evening:855(B); 155→combined:886(B),midday:787(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:490, 1:117, 27:113, 31:104, 15:88.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=184 Evening=202; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 148 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 022 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 184 (canon 148): box `148` covers winner `184` (boxed hit).
  - Evening winner 202 (canon 022): box `022` covers winner `202` (boxed hit).
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
