# Master Validation Run Report — Pennsylvania4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-07/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-07/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-07/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-07/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-07/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-07/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_263_20260110_033439.html`
- `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_060_20260110_033438.html`

Winners JSON files:
- `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_263_20260110_033439.json`
- `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac2_winner_060_20260110_033438.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 060 (canon 006): exact_boxed=True exact_straight=True | rank 780/4992 (rank_frac 0.156); Evening 263 (canon 236): exact_boxed=True exact_straight=True | rank 1872/4992 (rank_frac 0.375)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 263 idx21 (rank 3/35, frac 0.086), 060 idx2 (rank 27/35, frac 0.771)
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

### 2.Stable — Pennsylvania4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-07)

## Midday winner 060 (canonical 006)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=74 | exact_boxed=10 | exact_straight=10 | vt_boxed=10
- Scores (patterns_scores.csv): rank 780/4992 (rank_frac 0.15625) | score 16.5 (top 36.5, ratio 0.4520547945205479, delta 20.0) | section Midday, Set Set1, Draw Draw4, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|double_mirror|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 88/1853 (rank_frac 0.04749055585536967) | score 31.0 (top 88.0, ratio 0.3522727272727273, delta 57.0) | section Midday, col1_hits 0, hot2 2, set_chain 1, draw_chain 4 | why draw_chain4|hot1x1|hot2x2|vstrx6|dblmirrorx9
- Families (patterns_families.csv): count 36 | rank 19/1333 (rank_frac 0.014253563390847712) | score 28.5 (top 35.0, ratio 0.8142857142857143, delta 6.5) | section Midday, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=18

## Evening winner 263 (canonical 236)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=675 | exact_boxed=12 | exact_straight=12 | vt_boxed=12
- Scores (patterns_scores.csv): rank 1872/4992 (rank_frac 0.375) | score 13.5 (top 36.5, ratio 0.3698630136986301, delta 23.0) | section Evening, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|hidden3v|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 359/1853 (rank_frac 0.19373988127361036) | score 20.0 (top 88.0, ratio 0.22727272727272727, delta 68.0) | section Evening, col1_hits 2, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|col1x2|hot1x1|vstrx4
- Families (patterns_families.csv): count 60 | rank 48/1333 (rank_frac 0.03600900225056264) | score 27.0 (top 35.0, ratio 0.7714285714285715, delta 8.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=182

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 122 | section Combined | score 88.0 | col1_hits 7 | hot2 11
- rank    2 | canon 112 | section Combined | score 79.0 | col1_hits 6 | hot2 11
- rank    7 | canon 1122 | section Combined | score 72.0 | col1_hits 6 | hot2 11
- rank    5 | canon 009 | section Midday | score 76.0 | col1_hits 6 | hot2 8
- rank   13 | canon 1123 | section Combined | score 57.5 | col1_hits 5 | hot2 8
- rank    4 | canon 113 | section Combined | score 77.5 | col1_hits 6 | hot2 8
- rank    6 | canon 223 | section Combined | score 75.5 | col1_hits 6 | hot2 8
- rank   11 | canon 11223 | section Combined | score 61.5 | col1_hits 5 | hot2 8
- rank    2 | canon 445 | section Evening | score 79.0 | col1_hits 6 | hot2 8
- rank   17 | canon 019 | section Midday | score 52.5 | col1_hits 3 | hot2 6

## Top families (patterns_families.csv)
- rank 1056 | family 34 | score 10.0 | hot2 0 | section Midday
- rank  318 | family 18 | score 19.5 | hot2 0 | section Midday
- rank  242 | family 5 | score 21.0 | hot2 1 | section Midday
- rank   96 | family 2 | score 24.5 | hot2 2 | section Midday
- rank   96 | family 9 | score 24.5 | hot2 3 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 060 (canon 006): exact_boxed=True exact_straight=True | rank 780/4992 (rank_frac 0.156); Evening 263 (canon 236): exact_boxed=True exact_straight=True | rank 1872/4992 (rank_frac 0.375)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260110)

## Midday winner 060 (canonical 006)
- Stamp (winner_stamp.json): items_total=234 | exact_any=0 exact_final=0 | vtrac_any=194 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=88 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=26 family_vtrac_final=0
- Flags (winner_flags.csv): rows=234 | exact_any=0 vtrac_any=194 | drop_exact_any=1 drop_vtrac_any=88 | family_exact_any=0 family_vtrac_any=26 | vt_boxed=49 vt_straight=0
- Hits (winner_hits.csv): rows=234 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=49 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 263 (canonical 236)
- Stamp (winner_stamp.json): items_total=145 | exact_any=0 exact_final=0 | vtrac_any=145 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=145 | exact_any=0 vtrac_any=145 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=145 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 060 (canonical 006)
- Stamp (winner_stamp.json): items_total=250 | exact_any=1 exact_final=0 | vtrac_any=195 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=103 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=26 family_vtrac_final=0
- Flags (winner_flags.csv): rows=250 | exact_any=1 vtrac_any=195 | drop_exact_any=1 drop_vtrac_any=103 | family_exact_any=0 family_vtrac_any=26 | vt_boxed=53 vt_straight=0
- Hits (winner_hits.csv): rows=250 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=53 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=18.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 221 | score_v2 18.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 221 | score_v2 18.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 221 | score_v2 18.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 221 | score_v2 14.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 221 | score_v2 14.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 221 | score_v2 14.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 922 | score_v2 13.237143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 13.037143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 221 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 221 | score_v2 11.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 221 | score_v2 18.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 221 | score_v2 14.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 922 | score_v2 13.237143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 992 | score_v2 13.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 922 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 559 | score_v2 10.465714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 559 | score_v2 10.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 559 | score_v2 10.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 922 | score_v2 10.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 559 | score_v2 9.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 060 (canon 006): items_total=234 exact_any=0 vtrac_any=194 | top winner_present=False best_rank=None/14; Evening 263 (canon 236): items_total=145 exact_any=0 vtrac_any=145 | top winner_present=False best_rank=None/16; Combined 060 (canon 006): items_total=250 exact_any=1 vtrac_any=195 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 221, 221, 922, 992, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260110_033919)

## Top indices (from enhanced JSON)
- index 20 | score 55.96678999999999 | features: presence=39.11928999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 47.087700000000005 | features: presence=33.050200000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 25.689772500000004 | features: presence=15.8022725, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 18 | score 22.797572500000005 | features: presence=13.6500725, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 7 | score 17.484446666666667 | features: presence=8.710280000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 12.884749999999999 | features: presence=6.461, cross_section=0.5, set_echo=0.6, first_hit=0.08000000000000002
- index 12 | score 11.55645 | features: presence=4.42895, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 30 | score 10.359250000000001 | features: presence=5.161750000000001, cross_section=0.5, set_echo=0.3, first_hit=0.2
- index 27 | score 10.116825 | features: presence=5.841200000000001, cross_section=0.5, set_echo=0.3, first_hit=0.2666666666666667
- index 26 | score 9.504325 | features: presence=5.376825, first_hit=0.33333333333333337, column_span=0.25416666666666665, persistence=0.4

## Top straights (from enhanced JSON)
172, 271, 216, 162, 261, 612, 167, 617, 871, 867

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 263 | index 21 | file Pennsylvania4_vtrac21_winner_263_20260110_033439.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 060 | index 2 | file Pennsylvania4_vtrac2_winner_060_20260110_033438.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 263 | index 21 rank 3/35 (rank_frac 0.08571428571428572) | score 25.689772500000004 (top 55.96678999999999, ratio 0.4590181516574384, delta 30.277017499999985) | winner_in_index_straights=False | top_index_straights: 871 (7.188), 867 (6.525), 187 (6.303)
- winner 060 | index 2 rank 27/35 (rank_frac 0.7714285714285715) | score 2.0237499999999997 (top 55.96678999999999, ratio 0.0361598369318662, delta 53.94303999999999) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 263→idx21 rank 3/35 (frac 0.086); 060→idx2 rank 27/35 (frac 0.771).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 20, 17, 21, 18, 7.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-07)

## Midday winner 060 (canonical 006)
- Top lanes (hot_zones_top_lanes.csv): present | rank 6/212 (rank_frac 0.02830188679245283) | score_mean 21.286 (top 25.12, ratio 0.8473726114649682, delta 3.8339999999999996)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 263 (canonical 236)
- Top lanes (hot_zones_top_lanes.csv): present | rank 147/212 (rank_frac 0.6933962264150944) | score_mean 15.994 (top 25.12, ratio 0.6367038216560509, delta 9.126000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 000 | vt_triad 1 | score_mean 25.12 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical4
- rank    2 | triad 559 | vt_triad 15 | score_mean 21.83 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    3 | triad 227 | vt_triad 33 | score_mean 21.685 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 277 | vt_triad 33 | score_mean 21.569 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 499 | vt_triad 55 | score_mean 21.345 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 006 | vt_triad 12 | score_mean 21.286 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 049 | vt_triad 155 | score_mean 21.095 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 449 | vt_triad 55 | score_mean 21.082 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 459 | vt_triad 155 | score_mean 21.021 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 127 | vt_triad 233 | score_mean 20.847 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 060 (canon 006): rank 6/212 (rank_frac 0.028) ratio_to_top=0.8473726114649682; Evening 263 (canon 236): rank 147/212 (rank_frac 0.693) ratio_to_top=0.6367038216560509
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

Aux draws snapshot dir: `sharepacks/2026-01-07/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-07/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=757, 684, 600, 546, 980
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-07/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=684, 546, 359, 744, 871
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-07/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=757, 600, 980, 909, 360

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=5 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=20), P2:1 (gap=23), P3:5 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 015: score=50.92769321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 415: score=43.885828571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=43.19045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=40.57812571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 095: score=39.91507857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=39.20437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=39.18510714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 016: score=37.47012142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 014: score=36.953450000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 018: score=36.55865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 159: ds=892 sev=B
- 007: ds=889 sev=B
- 088: ds=853 sev=B
- 008: ds=831 sev=B
- 444: ds=807 sev=B
- 039: ds=782 sev=B
- 355: ds=772 sev=B
- 344: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=149 sev=red
  - 88: ds=87 sev=blue
  - 66: ds=75 sev=blue
  - 55: ds=52 sev=purple
  - 11: ds=37 sev=purple
  - 22: ds=11 sev=-
  - 44: ds=7 sev=-
  - 99: ds=6 sev=-
  - 00: ds=2 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 07: ds=55 sev=blue
  - 69: ds=46 sev=blue
  - 34: ds=41 sev=blue
  - 19: ds=39 sev=blue
  - 15: ds=31 sev=purple
  - 79: ds=26 sev=purple
  - 27: ds=25 sev=purple
  - 67: ds=25 sev=purple
  - 58: ds=24 sev=-
  - 01: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:291, 26:248, 16:106, 7:74, 6:69, 13:67, 19:63, 1:52, 11:49, 23:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=291 fs=2 fl=1 hz=0.007380073800738007, 26:ds=248 fs=0 fl=1 hz=0.003898635477582846, 16:ds=106 fs=3 fl=2 hz=0.007371007371007371, 7:ds=74 fs=35 fl=1 hz=0.04, 6:ds=69 fs=21 fl=1 hz=0.025611175785797437, 13:ds=67 fs=21 fl=1 hz=0.024553571428571428, 19:ds=63 fs=21 fl=3 hz=0.025695931477516063, 1:ds=52 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=49 fs=48 fl=0 hz=0.05128205128205128, 23:ds=43 fs=22 fl=1 hz=0.02415966386554622

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S20: ds=87 flags=purple
- S25: ds=64 flags=purple
- S4: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '3'], 'pairs': {'remaining_count': 0}}
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
- current_index=24 streak=1 max=3 last_repeat_gap=38 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=27), P2:9 (gap=14), P3:5 (gap=32)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 015: score=50.92769321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 415: score=43.885828571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=43.19045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=40.57812571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 095: score=39.91507857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=39.20437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=39.18510714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 016: score=37.47012142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 014: score=36.953450000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 018: score=36.55865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=982 sev=B
- 288: ds=969 sev=B
- 255: ds=940 sev=B
- 668: ds=922 sev=B
- 199: ds=870 sev=B
- 499: ds=796 sev=B
- 399: ds=779 sev=B
- 039: ds=767 sev=B
- 448: ds=756 sev=B
- 005: ds=748 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=191 sev=red
  - 99: ds=138 sev=red
  - 77: ds=81 sev=blue
  - 33: ds=74 sev=blue
  - 88: ds=43 sev=purple
  - 66: ds=37 sev=purple
  - 11: ds=18 sev=-
  - 00: ds=17 sev=-
  - 22: ds=5 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 79: ds=78 sev=red
  - 12: ds=53 sev=blue
  - 06: ds=48 sev=blue
  - 69: ds=35 sev=purple
  - 13: ds=30 sev=purple
  - 57: ds=29 sev=purple
  - 03: ds=28 sev=purple
  - 07: ds=27 sev=purple
  - 09: ds=23 sev=-
  - 37: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:380, 1:365, 34:219, 16:177, 15:168, 32:145, 35:122, 28:67, 5:52, 2:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=380 fs=0 fl=0 hz=0.0, 1:ds=365 fs=2 fl=2 hz=0.009124087591240877, 34:ds=219 fs=19 fl=1 hz=0.02631578947368421, 16:ds=177 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=168 fs=23 fl=0 hz=0.029411764705882353, 32:ds=145 fs=3 fl=1 hz=0.006720430107526881, 35:ds=122 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=67 fs=26 fl=1 hz=0.03515625, 5:ds=52 fs=18 fl=2 hz=0.022175290390707498, 2:ds=48 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=99 flags=red+purple
- S22: ds=84 flags=purple
- S23: ds=72 flags=purple
- S3: ds=66 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 015: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=68 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=34), P2:1 (gap=40), P3:6 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 015: score=50.92769321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 415: score=43.885828571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 013: score=43.19045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=40.57812571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 095: score=39.91507857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=39.20437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=39.18510714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 016: score=37.47012142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 014: score=36.953450000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 018: score=36.55865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=978 sev=B
- 009: ds=936 sev=B
- 255: ds=894 sev=B
- 138: ds=834 sev=B
- 117: ds=817 sev=B
- 158: ds=779 sev=B
- 344: ds=772 sev=B
- 199: ds=763 sev=B
- 112: ds=723 sev=B
- 277: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=133 sev=red
  - 33: ds=75 sev=blue
  - 44: ds=46 sev=purple
  - 66: ds=42 sev=purple
  - 11: ds=33 sev=purple
  - 55: ds=26 sev=purple
  - 22: ds=6 sev=-
  - 99: ds=3 sev=-
  - 00: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 68: ds=91 sev=red
  - 07: ds=68 sev=red
  - 15: ds=56 sev=red
  - 78: ds=41 sev=blue
  - 19: ds=40 sev=blue
  - 01: ds=34 sev=purple
  - 18: ds=34 sev=purple
  - 14: ds=33 sev=purple
  - 39: ds=31 sev=purple
  - 16: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:622, 23:161, 26:124, 18:121, 13:70, 33:55, 16:53, 30:52, 24:49, 27:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=622 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=161 fs=17 fl=2 hz=0.025165562913907286, 26:ds=124 fs=2 fl=1 hz=0.0056657223796034, 18:ds=121 fs=23 fl=2 hz=0.02910360884749709, 13:ds=70 fs=20 fl=1 hz=0.024881516587677725, 33:ds=55 fs=18 fl=3 hz=0.023076923076923075, 16:ds=53 fs=5 fl=3 hz=0.009523809523809525, 30:ds=52 fs=35 fl=1 hz=0.03829787234042553, 24:ds=49 fs=37 fl=0 hz=0.04048140043763676, 27:ds=41 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=94 flags=blue+purple
- S1: ds=79 flags=blue+purple
- S24: ds=62 flags=blue+purple
- S3: ds=50 flags=purple
- S20: ds=44 flags=purple
- S25: ds=32 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4'], 'pairs': {'remaining_count': 0}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:782(B); midday:767(B)
- 199 -> evening:763(B); midday:870(B)
- 255 -> evening:894(B); midday:940(B)
- 344 -> combined:701(B); evening:772(B)
- 444 -> combined:807(B); evening:978(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:55(blue); evening:68(red); midday:27(purple)
- 11 -> combined:37(purple); evening:33(purple)
- 15 -> combined:31(purple); evening:56(red)
- 19 -> combined:39(blue); evening:40(blue)
- 33 -> combined:149(red); evening:75(blue); midday:74(blue)
- 34 -> combined:41(blue); evening:28(purple)
- 55 -> combined:52(purple); evening:26(purple); midday:191(red)
- 66 -> combined:75(blue); evening:42(purple); midday:37(purple)
- 69 -> combined:46(blue); midday:35(purple)
- 79 -> combined:26(purple); midday:78(red)
- 88 -> combined:87(blue); evening:133(red); midday:43(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(5.524721428571429)[R1,XVAR-Cons(CEM)], 4(4.038642857142857)[R2,XVAR-Cons(CM)], 8(1.685142857142857)[R1,Double-Pressure], 9(1.4635285714285713)[R2,Mirror-Echo], 5(0.9118714285714286)[R2,Mirror-Echo]
- P2: 1(8.028828571428571)[R1,XVAR-Cons(CEM)], 9(3.572)[R2,XVAR-Cons(CM)], 3(2.842028571428571)[R3,XVAR-Cons(CE)], 4(0.3552785714285714)[R3,Swap], 6(0.33885714285714286)[R3,Mirror-Echo]
- P3: 5(6.818357142857144)[R1,XVAR-Cons(CEM)], 3(3.6369)[R2,XVAR-Cons(CM)], 6(1.4165714285714284)[R1,Double-Pressure], 4(0.8998999999999999)[R2,Double-Pressure], 8(0.5051)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=20), P2:1(gap=23), P3:5(gap=20); top cartesian candidates: 015, 415, 013, 515, 095.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '3'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:782(B),midday:767(B); 199→midday:870(B),evening:763(B); 255→midday:940(B),evening:894(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:291, 26:248, 16:106, 7:74, 6:69.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=060 Evening=263; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 006 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 236 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 060 (canon 006): box `006` covers winner `060` (boxed hit).
  - Evening winner 263 (canon 236): box `236` covers winner `263` (boxed hit).
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
