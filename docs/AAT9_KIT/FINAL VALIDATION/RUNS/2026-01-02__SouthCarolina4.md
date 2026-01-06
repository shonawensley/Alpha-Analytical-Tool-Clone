# Master Validation Run Report — SouthCarolina4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-02/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-02/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-02/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-02/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-02/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-02/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac13_winner_308_20260105_070926.html`
- `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_084_20260105_070927.html`

Winners JSON files:
- `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac13_winner_308_20260105_070926.json`
- `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_084_20260105_070927.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 308 (canon 038): exact_boxed=True exact_straight=True | rank 471/4189 (rank_frac 0.112); Evening 084 (canon 048): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 308 idx13 (rank 15/35, frac 0.429), 084 idx14 (rank 9/35, frac 0.257)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
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

### 2.Stable — SouthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-02)

## Midday winner 308 (canonical 038)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=23 | family_rows=56 | exact_boxed=23 | exact_straight=22 | vt_boxed=23
- Scores (patterns_scores.csv): rank 471/4189 (rank_frac 0.1124373358796849) | score 18.0 (top 41.5, ratio 0.43373493975903615, delta 23.5) | section Midday, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat5|mirror|hot2|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 49/988 (rank_frac 0.04959514170040486) | score 36.0 (top 68.5, ratio 0.5255474452554745, delta 32.5) | section Midday, col1_hits 2, hot2 4, set_chain 1, draw_chain 4 | why draw_chain4|col1x2|hot1x4|hot2x4|vstrx4
- Families (patterns_families.csv): count 39 | rank 726/1438 (rank_frac 0.5048678720445062) | score 15.0 (top 31.5, ratio 0.47619047619047616, delta 16.5) | section Midday, hot2 3
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=5

## Evening winner 084 (canonical 048)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=224 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 61 | rank 38/1438 (rank_frac 0.02642559109874826) | score 26.0 (top 31.5, ratio 0.8253968253968254, delta 5.5) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=26
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 008 | section Midday | score 68.0 | col1_hits 2 | hot2 7
- rank    6 | canon 118 | section Evening | score 56.5 | col1_hits 0 | hot2 6
- rank    7 | canon 009 | section Midday | score 56.0 | col1_hits 0 | hot2 6
- rank   11 | canon 089 | section Midday | score 48.0 | col1_hits 3 | hot2 6
- rank   13 | canon 378 | section Midday | score 47.0 | col1_hits 4 | hot2 6
- rank   16 | canon 0089 | section Midday | score 46.5 | col1_hits 0 | hot2 6
- rank   53 | canon 1158 | section Evening | score 35.5 | col1_hits 0 | hot2 4
- rank  120 | canon 0388 | section Midday | score 28.5 | col1_hits 2 | hot2 4
- rank  110 | canon 03788 | section Midday | score 29.5 | col1_hits 2 | hot2 4
- rank   92 | canon 3788 | section Midday | score 31.0 | col1_hits 3 | hot2 4

## Top families (patterns_families.csv)
- rank 1427 | family 4 | score 5.0 | hot2 0 | section Midday
- rank  507 | family 3 | score 18.0 | hot2 1 | section Midday
- rank  806 | family 34 | score 14.0 | hot2 2 | section Midday
- rank  778 | family 29 | score 14.5 | hot2 1 | section Midday
- rank  726 | family 7 | score 15.0 | hot2 2 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 308 (canon 038): exact_boxed=True exact_straight=True | rank 471/4189 (rank_frac 0.112); Evening 084 (canon 048): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260102)

## Midday winner 308 (canonical 038)
- Stamp (winner_stamp.json): items_total=121 | exact_any=93 exact_final=0 | vtrac_any=121 vtrac_final=0 | drop_exact_any=17 drop_exact_final=0 | drop_vtrac_any=48 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=20 family_vtrac_final=0
- Flags (winner_flags.csv): rows=121 | exact_any=93 vtrac_any=121 | drop_exact_any=17 drop_vtrac_any=48 | family_exact_any=0 family_vtrac_any=20 | vt_boxed=49 vt_straight=0
- Hits (winner_hits.csv): rows=121 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=49 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.727143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 084 (canonical 048)
- Stamp (winner_stamp.json): items_total=80 | exact_any=2 exact_final=0 | vtrac_any=48 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=55 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=80 | exact_any=2 vtrac_any=48 | drop_exact_any=0 drop_vtrac_any=55 | family_exact_any=0 family_vtrac_any=9 | vt_boxed=56 vt_straight=0
- Hits (winner_hits.csv): rows=80 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=56 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 308 (canonical 038)
- Stamp (winner_stamp.json): items_total=174 | exact_any=99 exact_final=0 | vtrac_any=156 vtrac_final=0 | drop_exact_any=18 drop_exact_final=0 | drop_vtrac_any=88 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=35 family_vtrac_final=0
- Flags (winner_flags.csv): rows=174 | exact_any=99 vtrac_any=156 | drop_exact_any=18 drop_vtrac_any=88 | family_exact_any=1 family_vtrac_any=35 | vt_boxed=90 vt_straight=0
- Hits (winner_hits.csv): rows=174 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=90 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 12.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 552 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 5 | pattern 900 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 5 | pattern 900 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 900 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 5 | pattern 900 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 5 | pattern 900 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 5 | pattern 900 | score_v2 11.177143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 552 | score_v2 12.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 559 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 900 | score_v2 11.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 559 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 10.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 599 | score_v2 10.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 552 | score_v2 10.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 591 | score_v2 10.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 900 | score_v2 10.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 308 (canon 038): items_total=121 exact_any=93 vtrac_any=121 | top winner_present=False best_rank=None/30; Evening 084 (canon 048): items_total=80 exact_any=2 vtrac_any=48 | top winner_present=False best_rank=None/22; Combined 308 (canon 038): items_total=174 exact_any=99 vtrac_any=156 | top winner_present=False best_rank=None/28
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 559, 559, 900, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_071333)

## Top indices (from enhanced JSON)
- index 18 | score 75.11271249999996 | features: presence=54.065212499999966, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 46.069682499999985 | features: presence=32.29218249999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 4 | score 43.83522 | features: presence=30.15772, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 40.97311249999999 | features: presence=26.845612499999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 40.506735 | features: presence=26.259235, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 39.67705 | features: presence=25.979550000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 28.962905000000006 | features: presence=19.685405000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 26.940749999999998 | features: presence=15.813249999999995, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 14 | score 14.216799999999997 | features: presence=7.6392999999999995, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 19 | score 12.26805 | features: presence=6.400550000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
681, 186, 081, 386, 683, 138, 836, 831, 068, 086

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 308 | index 13 | file SouthCarolina4_vtrac13_winner_308_20260105_070926.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 084 | index 14 | file SouthCarolina4_vtrac14_winner_084_20260105_070927.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 308 | index 13 rank 15/35 (rank_frac 0.42857142857142855) | score 9.636275 (top 75.11271249999996, ratio 0.1282908668755639, delta 65.47643749999996) | winner_in_index_straights=False | top_index_straights: 038 (4.744), 083 (3.805)
- winner 084 | index 14 rank 9/35 (rank_frac 0.2571428571428571) | score 14.216799999999997 (top 75.11271249999996, ratio 0.18927288772855866, delta 60.89591249999996) | winner_in_index_straights=False | top_index_straights: 093 (6.259), 098 (5.72), 809 (2.26)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 308→idx13 rank 15/35 (frac 0.429); 084→idx14 rank 9/35 (frac 0.257).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 18, 23, 4, 6, 2.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-02)

## Midday winner 308 (canonical 038)
- Top lanes (hot_zones_top_lanes.csv): present | rank 76/207 (rank_frac 0.3671497584541063) | score_mean 17.292 (top 24.85, ratio 0.6958551307847083, delta 7.558)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 084 (canonical 048)
- Top lanes (hot_zones_top_lanes.csv): present | rank 154/207 (rank_frac 0.7439613526570048) | score_mean 15.594 (top 24.85, ratio 0.6275251509054325, delta 9.256000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 679 | vt_triad 235 | score_mean 24.85 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 489 | vt_triad 455 | score_mean 22.541 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight
- rank    3 | triad 257 | vt_triad 133 | score_mean 21.642 | tags col1,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    4 | triad 499 | vt_triad 55 | score_mean 21.12 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2
- rank    5 | triad 044 | vt_triad 15 | score_mean 20.727 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    6 | triad 118 | vt_triad 24 | score_mean 20.192 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 049 | vt_triad 155 | score_mean 20.08 | tags hot16,hot20,set1_bonus,straight_lane,vertical1
- rank    8 | triad 009 | vt_triad 15 | score_mean 19.792 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 149 | vt_triad 255 | score_mean 19.788 | tags hot16,hot20,set1_bonus,straight_lane,vertical1
- rank   10 | triad 349 | vt_triad 455 | score_mean 19.74 | tags hot16,hot20,set1_bonus,straight_lane,vertical1

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 308 (canon 038): rank 76/207 (rank_frac 0.367) ratio_to_top=0.6958551307847083; Evening 084 (canon 048): rank 154/207 (rank_frac 0.744) ratio_to_top=0.6275251509054325
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

Aux draws snapshot dir: `sharepacks/2026-01-02/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=821, 910, 044, 653, 976
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=910, 653, 754, 425, 462
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=821, 044, 976, 463, 849

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=15 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=15), P2:3 (gap=31), P3:8 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 233: ds=998 sev=B
- 366: ds=970 sev=B
- 449: ds=899 sev=B
- 156: ds=882 sev=B
- 778: ds=852 sev=B
- 279: ds=851 sev=B
- 033: ds=783 sev=B
- 004: ds=771 sev=B
- 688: ds=738 sev=B
- 278: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=179 sev=red
  - 55: ds=116 sev=red
  - 77: ds=100 sev=blue
  - 33: ds=87 sev=blue
  - 88: ds=82 sev=blue
  - 22: ds=62 sev=purple
  - 66: ds=50 sev=purple
  - 00: ds=23 sev=-
  - 11: ds=19 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 15: ds=58 sev=red
  - 78: ds=51 sev=blue
  - 05: ds=47 sev=blue
  - 68: ds=39 sev=blue
  - 29: ds=32 sev=purple
  - 06: ds=25 sev=purple
  - 16: ds=25 sev=purple
  - 08: ds=24 sev=-
  - 38: ds=24 sev=-
  - 59: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:443, 35:386, 1:167, 26:155, 31:117, 4:108, 23:106, 28:100, 27:83, 19:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=443 fs=0 fl=0 hz=0.002197802197802198, 35:ds=386 fs=0 fl=0 hz=0.001949317738791423, 1:ds=167 fs=6 fl=4 hz=0.012195121951219513, 26:ds=155 fs=2 fl=0 hz=0.0062402496099844, 31:ds=117 fs=27 fl=0 hz=0.03085714285714286, 4:ds=108 fs=21 fl=2 hz=0.026589595375722544, 23:ds=106 fs=25 fl=1 hz=0.029850746268656716, 28:ds=100 fs=16 fl=2 hz=0.021479713603818614, 27:ds=83 fs=26 fl=0 hz=0.02911534154535274, 19:ds=67 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=92 flags=red+purple
- S0: ds=65 flags=blue+purple
- S23: ds=54 flags=purple
- S5: ds=53 flags=purple
- S24: ds=51 flags=blue+purple
- S4: ds=43 flags=purple
- S3: ds=42 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=3 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=13), P2:3 (gap=39), P3:9 (gap=24)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=877 sev=B
- 555: ds=872 sev=B
- 222: ds=849 sev=B
- 337: ds=826 sev=B
- 003: ds=817 sev=B
- 228: ds=808 sev=B
- 556: ds=710 sev=B
- 449: ds=668 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=112 sev=red
  - 55: ds=76 sev=blue
  - 77: ds=45 sev=purple
  - 33: ds=39 sev=purple
  - 88: ds=37 sev=purple
  - 22: ds=35 sev=purple
  - 66: ds=22 sev=-
  - 00: ds=13 sev=-
  - 11: ds=8 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 49: ds=53 sev=blue
  - 67: ds=47 sev=blue
  - 34: ds=46 sev=blue
  - 27: ds=40 sev=blue
  - 07: ds=31 sev=purple
  - 05: ds=28 sev=purple
  - 15: ds=26 sev=purple
  - 18: ds=25 sev=purple
  - 78: ds=25 sev=purple
  - 69: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:413, 26:191, 35:177, 27:142, 6:110, 5:79, 1:76, 15:71, 34:57, 31:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=413 fs=1 fl=2 hz=0.006993006993006993, 26:ds=191 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=177 fs=1 fl=1 hz=0.004968944099378882, 27:ds=142 fs=18 fl=3 hz=0.026582278481012658, 6:ds=110 fs=24 fl=2 hz=0.02957906712172924, 5:ds=79 fs=20 fl=1 hz=0.023102310231023104, 1:ds=76 fs=7 fl=3 hz=0.012127894156560088, 15:ds=71 fs=17 fl=3 hz=0.021691973969631236, 34:ds=57 fs=28 fl=1 hz=0.03159041394335512, 31:ds=53 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=80 flags=purple
- S25: ds=77 flags=purple
- S21: ds=57 flags=purple
- S20: ds=53 flags=purple
- S17: ds=51 flags=purple
- S8: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 089: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 125: score=2 tags=RS
  - 134: score=2 tags=RS
  - 179: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=30 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=16), P2:8 (gap=20), P3:8 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=980 sev=B
- 117: ds=891 sev=B
- 005: ds=877 sev=B
- 577: ds=854 sev=B
- 155: ds=834 sev=B
- 777: ds=833 sev=B
- 669: ds=825 sev=B
- 179: ds=807 sev=B
- 366: ds=773 sev=B
- 222: ds=767 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=97 sev=blue
  - 77: ds=84 sev=blue
  - 66: ds=76 sev=blue
  - 33: ds=72 sev=blue
  - 55: ds=63 sev=purple
  - 88: ds=57 sev=purple
  - 22: ds=34 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=13 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 58: ds=98 sev=red
  - 35: ds=65 sev=red
  - 29: ds=60 sev=red
  - 47: ds=50 sev=blue
  - 15: ds=46 sev=blue
  - 19: ds=32 sev=purple
  - 78: ds=28 sev=purple
  - 05: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 68: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:485, 1:272, 32:239, 31:218, 4:138, 28:111, 19:107, 23:102, 26:84, 16:80

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=485 fs=3 fl=1 hz=0.017391304347826087, 1:ds=272 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=239 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=218 fs=16 fl=1 hz=0.021935483870967745, 4:ds=138 fs=21 fl=3 hz=0.028742514970059883, 28:ds=111 fs=10 fl=4 hz=0.017676767676767676, 19:ds=107 fs=12 fl=2 hz=0.016968325791855206, 23:ds=102 fs=24 fl=0 hz=0.02937576499388005, 26:ds=84 fs=0 fl=0 hz=0.002347417840375587, 16:ds=80 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=63 flags=purple
- S15: ds=54 flags=red+purple
- S9: ds=51 flags=purple
- S17: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 126: score=2 tags=RS
  - 189: score=2 tags=RS
  - 234: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:767(B); midday:849(B)
- 366 -> combined:970(B); evening:773(B)
- 449 -> combined:899(B); midday:668(B)
- 688 -> combined:738(B); evening:732(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:47(blue); evening:26(purple); midday:28(purple)
- 15 -> combined:58(red); evening:46(blue); midday:26(purple)
- 22 -> combined:62(purple); evening:34(purple); midday:35(purple)
- 29 -> combined:32(purple); evening:60(red)
- 33 -> combined:87(blue); evening:72(blue); midday:39(purple)
- 55 -> combined:116(red); evening:63(purple); midday:76(blue)
- 66 -> combined:50(purple); evening:76(blue)
- 68 -> combined:39(blue); evening:25(purple)
- 77 -> combined:100(blue); evening:84(blue); midday:45(purple)
- 78 -> combined:51(blue); evening:28(purple); midday:25(purple)
- 88 -> combined:82(blue); evening:57(purple); midday:37(purple)
- 99 -> combined:179(red); evening:97(blue); midday:112(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(2.558557142857143)[R3,XVAR-Cons(CE)], 6(1.2012142857142856)[R1,Mirror-Echo], 5(1.0714285714285714)[R1,Double-Pressure], 0(0.9881428571428571)[R1,Double-Pressure], 3(0.986)[R2,Double-Pressure]
- P2: 3(8.943192857142858)[R1,Mirror-Echo], 8(7.7962928571428565)[R2,Mirror-Echo], 9(1.901657142857143)[R3,XVAR-Cons(CE)], 7(1.1806999999999999)[R2,Double-Pressure]
- P3: 8(3.738714285714286)[R1,XVAR-Cons(CE)], 2(2.4522142857142857)[R2,Mirror-Echo], 7(1.7482071428571428)[R3,Mirror-Echo], 6(0.9552999999999999)[R2,Double-Pressure], 5(0.8299)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=15), P2:3(gap=31), P3:8(gap=15); top cartesian candidates: 138, 132, 188, 137, 182.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: N/A.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:849(B),evening:767(B); 366→combined:970(B),evening:773(B); 449→combined:899(B),midday:668(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:443, 35:386, 1:167, 26:155, 31:117.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=308 Evening=084; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 038 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 048 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 308 (canon 038): box `038` covers winner `308` (boxed hit).
  - Evening winner 084 (canon 048): box `048` covers winner `084` (boxed hit).
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
