# Master Validation Run Report — NorthCarolina4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-08/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-08/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-08/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-08/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-08/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-08/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_132_20260110_034433.html`
- `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac7_winner_571_20260110_034434.html`

Winners JSON files:
- `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_132_20260110_034433.json`
- `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac7_winner_571_20260110_034434.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 132 (canon 123): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 571 (canon 157): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 132 idx21 (rank 24/35, frac 0.686), 571 idx7 (rank 16/35, frac 0.457)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — NorthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-08)

## Midday winner 132 (canonical 123)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=215 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 44 | rank 641/1739 (rank_frac 0.36860264519838987) | score 19.5 (top 39.0, ratio 0.5, delta 19.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=60
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 571 (canonical 157)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=212 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 52 | rank 830/1739 (rank_frac 0.4772857964347326) | score 17.5 (top 39.0, ratio 0.44871794871794873, delta 21.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=72
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 066 | section Combined | score 97.5 | col1_hits 9 | hot2 11
- rank    9 | canon 0366 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    5 | canon 466 | section Combined | score 92.5 | col1_hits 8 | hot2 11
- rank   18 | canon 3466 | section Combined | score 67.0 | col1_hits 7 | hot2 11
- rank    9 | canon 366 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    2 | canon 299 | section Midday | score 98.5 | col1_hits 9 | hot2 11
- rank    4 | canon 099 | section Midday | score 93.0 | col1_hits 9 | hot2 11
- rank   11 | canon 144 | section Evening | score 79.0 | col1_hits 5 | hot2 11
- rank   13 | canon 166 | section Evening | score 77.5 | col1_hits 7 | hot2 11
- rank    6 | canon 0299 | section Midday | score 90.0 | col1_hits 9 | hot2 11

## Top families (patterns_families.csv)
- rank 1709 | family 21 | score 6.5 | hot2 0 | section Midday
- rank  437 | family 5 | score 22.5 | hot2 0 | section Midday
- rank  914 | family 34 | score 16.5 | hot2 0 | section Midday
- rank  830 | family 21 | score 17.5 | hot2 0 | section Midday
- rank  830 | family 3 | score 17.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 132 (canon 123): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 571 (canon 157): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260110)

## Midday winner 132 (canonical 123)
- Stamp (winner_stamp.json): items_total=43 | exact_any=3 exact_final=0 | vtrac_any=40 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=3 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=43 | exact_any=3 vtrac_any=40 | drop_exact_any=0 drop_vtrac_any=3 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=43 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=4 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 571 (canonical 157)
- Stamp (winner_stamp.json): items_total=1 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=1 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=1 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.487143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 132 (canonical 123)
- Stamp (winner_stamp.json): items_total=69 | exact_any=3 exact_final=0 | vtrac_any=52 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=18 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=69 | exact_any=3 vtrac_any=52 | drop_exact_any=0 drop_vtrac_any=18 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=22 vt_straight=0
- Hits (winner_hits.csv): rows=69 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=22 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.877143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 7 | pattern 992 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 992 | score_v2 13.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 12.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 992 | score_v2 12.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 7 | pattern 992 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 6 | pattern 992 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 12.277143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 12.277143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 992 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 992 | score_v2 12.077143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 992 | score_v2 13.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 12.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 992 | score_v2 12.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 559 | score_v2 11.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 10.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 559 | score_v2 10.487143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 10.247143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 10.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 922 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 922 | score_v2 9.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 132 (canon 123): items_total=43 exact_any=3 vtrac_any=40 | top winner_present=False best_rank=None/4; Evening 571 (canon 157): items_total=1 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/22; Combined 132 (canon 123): items_total=69 exact_any=3 vtrac_any=52 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 992, 559, 992, 559, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260110_034640)

## Top indices (from enhanced JSON)
- index 31 | score 116.37547999999998 | features: presence=81.71797999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 111.68920999999999 | features: presence=76.93170999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 62.39799999999998 | features: presence=43.70049999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 61.49049999999999 | features: presence=43.163, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 59.26557499999999 | features: presence=40.188075, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 57.182849999999995 | features: presence=38.85535, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 53.58914249999999 | features: presence=36.82164249999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 46.872029999999995 | features: presence=31.514529999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 27.23455 | features: presence=16.34705, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 26.89695 | features: presence=16.39945, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
924, 416, 964, 196, 619, 614, 016, 610, 641, 624

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 132 | index 21 | file NorthCarolina4_vtrac21_winner_132_20260110_034433.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 571 | index 7 | file NorthCarolina4_vtrac7_winner_571_20260110_034434.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 132 | index 21 rank 24/35 (rank_frac 0.6857142857142857) | score 3.11375 (top 116.37547999999998, ratio 0.026756065796678136, delta 113.26172999999999) | winner_in_index_straights=False | top_index_straights: 187 (0.5), 871 (0.44), 817 (0.4)
- winner 571 | index 7 rank 16/35 (rank_frac 0.45714285714285713) | score 8.63625 (top 116.37547999999998, ratio 0.07421022022852237, delta 107.73922999999998) | winner_in_index_straights=False | top_index_straights: 201 (3.604), 170 (1.66), 701 (1.45)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 132→idx21 rank 24/35 (frac 0.686); 571→idx7 rank 16/35 (frac 0.457).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 31, 28, 6, 19, 25.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-08)

## Midday winner 132 (canonical 123)
- Top lanes (hot_zones_top_lanes.csv): present | rank 107/204 (rank_frac 0.5245098039215687) | score_mean 16.033 (top 23.407, ratio 0.684966035801256, delta 7.373999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 571 (canonical 157)
- Top lanes (hot_zones_top_lanes.csv): present | rank 168/204 (rank_frac 0.8235294117647058) | score_mean 14.548 (top 23.407, ratio 0.6215234758832828, delta 8.859)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 338 | vt_triad 44 | score_mean 23.407 | tags hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 355 | vt_triad 14 | score_mean 22.65 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    3 | triad 127 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    5 | triad 247 | vt_triad 335 | score_mean 20.925 | tags hot16,hot20,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    5 | triad 279 | vt_triad 335 | score_mean 20.925 | tags hot16,hot20,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    7 | triad 244 | vt_triad 35 | score_mean 20.836 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    8 | triad 366 | vt_triad 24 | score_mean 19.937 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 148 | vt_triad 245 | score_mean 19.757 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 224 | vt_triad 35 | score_mean 19.733 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 132 (canon 123): rank 107/204 (rank_frac 0.525) ratio_to_top=0.684966035801256; Evening 571 (canon 157): rank 168/204 (rank_frac 0.824) ratio_to_top=0.6215234758832828
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

Aux draws snapshot dir: `sharepacks/2026-01-08/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-08/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=202, 184, 298, 552, 895
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-08/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=184, 552, 553, 187, 374
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-08/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=202, 298, 895, 887, 178

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=8 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=27), P2:4 (gap=45), P3:0 (gap=36)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.27271428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.81597857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=39.96957142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 620: score=39.548407142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 941: score=36.53801428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=36.11685 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 948: score=32.91605714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 648: score=32.49489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 944: score=32.411614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 921: score=32.270442857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=888 sev=B
- 446: ds=884 sev=B
- 445: ds=824 sev=B
- 122: ds=807 sev=B
- 036: ds=803 sev=B
- 555: ds=780 sev=B
- 299: ds=777 sev=B
- 277: ds=769 sev=B
- 112: ds=758 sev=B
- 034: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=164 sev=red
  - 77: ds=137 sev=red
  - 99: ds=60 sev=purple
  - 44: ds=58 sev=purple
  - 11: ds=20 sev=-
  - 66: ds=19 sev=-
  - 33: ds=10 sev=-
  - 88: ds=6 sev=-
  - 55: ds=3 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 56: ds=66 sev=red
  - 27: ds=62 sev=red
  - 23: ds=52 sev=blue
  - 09: ds=51 sev=blue
  - 04: ds=45 sev=blue
  - 06: ds=45 sev=blue
  - 24: ds=41 sev=blue
  - 12: ds=40 sev=blue
  - 01: ds=35 sev=purple
  - 08: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:492, 1:119, 27:115, 31:106, 15:90, 16:88, 23:67, 35:58, 12:56, 6:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=492 fs=3 fl=0 hz=0.009389671361502348, 1:ds=119 fs=0 fl=3 hz=0.00625, 27:ds=115 fs=15 fl=2 hz=0.02463768115942029, 31:ds=106 fs=19 fl=3 hz=0.02502844141069397, 15:ds=90 fs=15 fl=2 hz=0.019495412844036695, 16:ds=88 fs=4 fl=1 hz=0.008836524300441826, 23:ds=67 fs=17 fl=3 hz=0.024330900243309, 35:ds=58 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=56 fs=46 fl=1 hz=0.049893842887473464, 6:ds=53 fs=22 fl=3 hz=0.02771618625277162

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=41 flags=blue+purple
- S18: ds=34 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=3 tags=FLT,RS
  - 036: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=102 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=41), P2:9 (gap=31), P3:8 (gap=27)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.27271428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.81597857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=39.96957142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 620: score=39.548407142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 941: score=36.53801428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=36.11685 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 948: score=32.91605714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 648: score=32.49489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 944: score=32.411614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 921: score=32.270442857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=979 sev=B
- 123: ds=954 sev=B
- 446: ds=931 sev=B
- 777: ds=891 sev=B
- 119: ds=856 sev=B
- 222: ds=826 sev=B
- 155: ds=788 sev=B
- 488: ds=782 sev=B
- 177: ds=758 sev=B
- 007: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=161 sev=red
  - 00: ds=136 sev=red
  - 77: ds=68 sev=purple
  - 99: ds=56 sev=purple
  - 22: ds=44 sev=purple
  - 11: ds=14 sev=-
  - 88: ds=10 sev=-
  - 66: ds=9 sev=-
  - 33: ds=5 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 07: ds=60 sev=red
  - 28: ds=52 sev=blue
  - 23: ds=47 sev=blue
  - 26: ds=47 sev=blue
  - 02: ds=44 sev=blue
  - 29: ds=41 sev=blue
  - 56: ds=35 sev=purple
  - 27: ds=32 sev=purple
  - 38: ds=27 sev=purple
  - 05: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:384, 25:192, 32:172, 35:146, 11:111, 31:104, 2:100, 33:83, 12:61, 1:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=384 fs=1 fl=0 hz=0.005905511811023622, 25:ds=192 fs=15 fl=1 hz=0.02165087956698241, 32:ds=172 fs=3 fl=1 hz=0.007416563658838071, 35:ds=146 fs=0 fl=2 hz=0.005201560468140442, 11:ds=111 fs=50 fl=0 hz=0.056882821387940846, 31:ds=104 fs=25 fl=0 hz=0.02793296089385475, 2:ds=100 fs=13 fl=3 hz=0.018223234624145785, 33:ds=83 fs=21 fl=2 hz=0.025136612021857924, 12:ds=61 fs=47 fl=0 hz=0.05181918412348401, 1:ds=59 fs=2 fl=2 hz=0.00641025641025641

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=95 flags=purple
- S20: ds=83 flags=red+purple
- S2: ds=74 flags=purple
- S5: ds=70 flags=purple
- S8: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6', '9'], 'pairs': {'remaining_count': 0}}
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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=26 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=20), P2:4 (gap=41), P3:0 (gap=18)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:4 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 940: score=47.27271428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 640: score=43.81597857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 920: score=39.96957142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 620: score=39.548407142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 941: score=36.53801428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 641: score=36.11685 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 948: score=32.91605714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 648: score=32.49489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 944: score=32.411614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 921: score=32.270442857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=980 sev=B
- 299: ds=937 sev=B
- 223: ds=867 sev=B
- 122: ds=856 sev=B
- 116: ds=833 sev=B
- 039: ds=816 sev=B
- 377: ds=804 sev=B
- 277: ds=790 sev=B
- 188: ds=778 sev=B
- 557: ds=777 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=128 sev=red
  - 77: ds=86 sev=blue
  - 00: ds=82 sev=blue
  - 66: ds=44 sev=purple
  - 99: ds=30 sev=purple
  - 44: ds=29 sev=purple
  - 11: ds=10 sev=-
  - 33: ds=5 sev=-
  - 88: ds=3 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 45: ds=105 sev=red
  - 34: ds=46 sev=blue
  - 04: ds=41 sev=blue
  - 06: ds=35 sev=purple
  - 08: ds=34 sev=purple
  - 56: ds=33 sev=purple
  - 27: ds=31 sev=purple
  - 09: ds=28 sev=purple
  - 23: ds=26 sev=purple
  - 24: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:264, 26:246, 13:211, 1:153, 23:122, 5:103, 17:102, 27:59, 31:53, 15:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=264 fs=18 fl=0 hz=0.024896265560165977, 26:ds=246 fs=1 fl=2 hz=0.006666666666666667, 13:ds=211 fs=19 fl=0 hz=0.024675324675324673, 1:ds=153 fs=2 fl=3 hz=0.007434944237918215, 23:ds=122 fs=14 fl=3 hz=0.019384264538198404, 5:ds=103 fs=15 fl=2 hz=0.020809248554913295, 17:ds=102 fs=29 fl=0 hz=0.03553921568627451, 27:ds=59 fs=22 fl=3 hz=0.027085590465872156, 31:ds=53 fs=21 fl=2 hz=0.024338624338624337, 15:ds=45 fs=16 fl=1 hz=0.01829924650161464

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=96 flags=purple
- S0: ds=82 flags=blue+purple
- S2: ds=50 flags=purple
- S21: ds=37 flags=red+purple
- S7: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:803(B); evening:730(B)
- 122 -> combined:807(B); evening:856(B)
- 155 -> combined:888(B); midday:788(B)
- 277 -> combined:769(B); evening:790(B)
- 299 -> combined:777(B); evening:937(B)
- 446 -> combined:884(B); midday:931(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:164(red); evening:82(blue); midday:136(red)
- 04 -> combined:45(blue); evening:41(blue)
- 06 -> combined:45(blue); evening:35(purple)
- 08 -> combined:35(purple); evening:34(purple)
- 09 -> combined:51(blue); evening:28(purple); midday:25(purple)
- 23 -> combined:52(blue); evening:26(purple); midday:47(blue)
- 27 -> combined:62(red); evening:31(purple); midday:32(purple)
- 44 -> combined:58(purple); evening:29(purple); midday:161(red)
- 56 -> combined:66(red); evening:33(purple); midday:35(purple)
- 77 -> combined:137(red); evening:86(blue); midday:68(purple)
- 99 -> combined:60(purple); evening:30(purple); midday:56(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.4444)[R2,XVAR-Cons(CM)], 6(3.0232357142857147)[R1,XVAR-Cons(CM)], 7(2.664014285714286)[R3,XVAR-Cons(CE)], 2(1.7449999999999999)[R1,Double-Pressure], 5(1.197142857142857)[R1,Double-Pressure]
- P2: 4(8.995514285714286)[R1,XVAR-Cons(CEM)], 2(5.727942857142857)[R2,XVAR-Cons(CEM)], 9(1.8345714285714283)[R1,Mirror-Echo], 3(1.0252999999999999)[R2,Double-Pressure], 6(0.3121428571428571)[R3,Swap]
- P3: 0(7.797228571428571)[R1,XVAR-Cons(CEM)], 1(2.5981)[R2,XVAR-Cons(CM)], 8(1.4761428571428572)[R1,Double-Pressure], 4(0.9717)[R2,Double-Pressure], 9(0.3262857142857143)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=27), P2:4(gap=45), P3:0(gap=36); top cartesian candidates: 940, 640, 920, 620, 941.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 027, 036, 126, 135, 234.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:803(B),evening:730(B); 122→combined:807(B),evening:856(B); 155→combined:888(B),midday:788(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:492, 1:119, 27:115, 31:106, 15:90.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=132 Evening=571; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 123 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 157 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 132 (canon 123): box `123` covers winner `132` (boxed hit).
  - Evening winner 571 (canon 157): box `157` covers winner `571` (boxed hit).
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
