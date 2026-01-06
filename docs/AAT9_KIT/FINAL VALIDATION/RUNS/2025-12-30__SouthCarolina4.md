# Master Validation Run Report — SouthCarolina4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/SouthCarolina4/`
- Winners lens: `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2025-12-30/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2025-12-30/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2025-12-30/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2025-12-30/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2025-12-30/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-12-30/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac12_winner_754_20260105_051218.html`
- `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac22_winner_976_20260105_051219.html`

Winners JSON files:
- `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac12_winner_754_20260105_051218.json`
- `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac22_winner_976_20260105_051219.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 754 (canon 457): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 976 (canon 679): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 754 idx12 (rank 17/35, frac 0.486), 976 idx22 (rank 29/35, frac 0.829)
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

### 2.Stable — SouthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2025-12-30)

## Midday winner 754 (canonical 457)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=277 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 71 | rank 132/1446 (rank_frac 0.0912863070539419) | score 24.0 (top 32.0, ratio 0.75, delta 8.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=91
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 976 (canonical 679)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=146 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 29 | rank 338/1446 (rank_frac 0.23374827109266944) | score 20.0 (top 32.0, ratio 0.625, delta 12.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=59
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 189 | section Evening | score 79.5 | col1_hits 7 | hot2 11
- rank    1 | canon 189 | section Combined | score 80.5 | col1_hits 7 | hot2 11
- rank    5 | canon 017 | section Combined | score 60.0 | col1_hits 5 | hot2 8
- rank    3 | canon 006 | section Midday | score 75.5 | col1_hits 7 | hot2 8
- rank   10 | canon 1389 | section Combined | score 53.5 | col1_hits 5 | hot2 7
- rank    6 | canon 389 | section Combined | score 56.5 | col1_hits 5 | hot2 7
- rank   34 | canon 039 | section Combined | score 43.0 | col1_hits 4 | hot2 7
- rank   18 | canon 137 | section Combined | score 50.5 | col1_hits 4 | hot2 7
- rank   57 | canon 079 | section Combined | score 38.5 | col1_hits 3 | hot2 6
- rank   15 | canon 068 | section Midday | score 52.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1394 | family 14 | score 6.0 | hot2 0 | section Midday
- rank  493 | family 31 | score 18.0 | hot2 0 | section Midday
- rank  530 | family 3 | score 17.5 | hot2 0 | section Midday
- rank  530 | family 23 | score 17.5 | hot2 0 | section Midday
- rank  530 | family 5 | score 17.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 754 (canon 457): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 976 (canon 679): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — SouthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260105)

## Midday winner 754 (canonical 457)
- Stamp (winner_stamp.json): items_total=115 | exact_any=0 exact_final=0 | vtrac_any=114 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=115 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=68 family_vtrac_final=0
- Flags (winner_flags.csv): rows=115 | exact_any=0 vtrac_any=114 | drop_exact_any=0 drop_vtrac_any=115 | family_exact_any=0 family_vtrac_any=68 | vt_boxed=10 vt_straight=0
- Hits (winner_hits.csv): rows=115 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=10 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 976 (canonical 679)
- Stamp (winner_stamp.json): items_total=6 | exact_any=0 exact_final=0 | vtrac_any=6 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=6 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=6 | exact_any=0 vtrac_any=6 | drop_exact_any=0 drop_vtrac_any=6 | family_exact_any=0 family_vtrac_any=4 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=6 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.047143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 754 (canonical 457)
- Stamp (winner_stamp.json): items_total=176 | exact_any=0 exact_final=0 | vtrac_any=171 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=158 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=102 family_vtrac_final=0
- Flags (winner_flags.csv): rows=176 | exact_any=0 vtrac_any=171 | drop_exact_any=0 drop_vtrac_any=158 | family_exact_any=0 family_vtrac_any=102 | vt_boxed=39 vt_straight=0
- Hits (winner_hits.csv): rows=176 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=39 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 901 | score_v2 12.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 901 | score_v2 11.397143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 900 | score_v2 11.287143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 900 | score_v2 11.087143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 900 | score_v2 11.037143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 599 | score_v2 10.987143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 599 | score_v2 10.937143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 10.820476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 599 | score_v2 10.787143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 599 | score_v2 10.708571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 901 | score_v2 12.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 900 | score_v2 11.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 599 | score_v2 10.987143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 900 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 901 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 10.247143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 991 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 990 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 918 | score_v2 10.047143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 599 | score_v2 9.987143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 754 (canon 457): items_total=115 exact_any=0 vtrac_any=114 | top winner_present=False best_rank=None/28; Evening 976 (canon 679): items_total=6 exact_any=0 vtrac_any=6 | top winner_present=False best_rank=None/30; Combined 754 (canon 457): items_total=176 exact_any=0 vtrac_any=171 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 901, 900, 599, 900, 901.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_051507)

## Top indices (from enhanced JSON)
- index 6 | score 47.602349999999994 | features: presence=28.74485, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 45.7886 | features: presence=29.621100000000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 41.3102375 | features: presence=25.142737500000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 33.9354 | features: presence=20.987900000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 15 | score 30.497825000000002 | features: presence=19.910325, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 24.1216 | features: presence=17.3841, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 5 | score 22.644733333333335 | features: presence=14.573899999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 22.643125 | features: presence=11.645625, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 24 | score 16.755565 | features: presence=9.968065000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 13 | score 14.036925000000002 | features: presence=6.049425000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
506, 605, 065, 938, 893, 983, 968, 986, 598, 836

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 754 | index 12 | file SouthCarolina4_vtrac12_winner_754_20260105_051218.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 976 | index 22 | file SouthCarolina4_vtrac22_winner_976_20260105_051219.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 754 | index 12 rank 17/35 (rank_frac 0.4857142857142857) | score 10.625974999999999 (top 47.602349999999994, ratio 0.22322374840737905, delta 36.976375) | winner_in_index_straights=False | top_index_straights: 759 (2.618), 709 (2.425), 592 (2.1)
- winner 976 | index 22 rank 29/35 (rank_frac 0.8285714285714286) | score 2.039083333333333 (top 47.602349999999994, ratio 0.042835770362877744, delta 45.563266666666664) | winner_in_index_straights=False | top_index_straights: 796 (0.576), 296 (0.466)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 754→idx12 rank 17/35 (frac 0.486); 976→idx22 rank 29/35 (frac 0.829).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 6, 2, 33, 34, 15.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2025-12-30)

## Midday winner 754 (canonical 457)
- Top lanes (hot_zones_top_lanes.csv): present | rank 200/203 (rank_frac 0.9852216748768473) | score_mean 13.0 (top 24.446, ratio 0.531784340996482, delta 11.446000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 976 (canonical 679)
- Top lanes (hot_zones_top_lanes.csv): present | rank 42/203 (rank_frac 0.20689655172413793) | score_mean 17.988 (top 24.446, ratio 0.7358259019880552, delta 6.458000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 257 | vt_triad 133 | score_mean 24.446 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight
- rank    2 | triad 379 | vt_triad 345 | score_mean 20.942 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 489 | vt_triad 455 | score_mean 20.712 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 124 | vt_triad 235 | score_mean 20.091 | tags hot16,hot20,literal_draw,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 889 | vt_triad 45 | score_mean 19.989 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 037 | vt_triad 134 | score_mean 19.426 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 249 | vt_triad 355 | score_mean 19.39 | tags hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    8 | triad 258 | vt_triad 134 | score_mean 19.332 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    9 | triad 246 | vt_triad 235 | score_mean 19.265 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 189 | vt_triad 245 | score_mean 19.242 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 754 (canon 457): rank 200/203 (rank_frac 0.985) ratio_to_top=0.531784340996482; Evening 976 (canon 679): rank 42/203 (rank_frac 0.207) ratio_to_top=0.7358259019880552
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

Aux draws snapshot dir: `sharepacks/2025-12-30/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-12-30/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=463, 425, 849, 257, 462
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-30/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=425, 462, 144, 528, 391
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-30/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=463, 849, 257, 240, 326

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=9 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=24), P2:7 (gap=45), P3:1 (gap=11)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 676: score=46.647924999999994 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 631: score=45.383667857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 671: score=45.05211357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 636: score=44.47660714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 678: score=43.758337857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 031: score=42.656528571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 071: score=42.237785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 036: score=41.61741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 638: score=41.469471428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=41.40107142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 225: ds=995 sev=B
- 233: ds=992 sev=B
- 366: ds=964 sev=B
- 449: ds=893 sev=B
- 156: ds=876 sev=B
- 778: ds=846 sev=B
- 279: ds=845 sev=B
- 033: ds=777 sev=B
- 004: ds=765 sev=B
- 688: ds=732 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=173 sev=red
  - 55: ds=110 sev=red
  - 77: ds=94 sev=blue
  - 33: ds=81 sev=blue
  - 88: ds=76 sev=blue
  - 22: ds=56 sev=purple
  - 66: ds=44 sev=purple
  - 00: ds=17 sev=-
  - 11: ds=13 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 35: ds=102 sev=red
  - 15: ds=52 sev=blue
  - 18: ds=50 sev=blue
  - 47: ds=46 sev=blue
  - 78: ds=45 sev=blue
  - 05: ds=41 sev=blue
  - 68: ds=33 sev=purple
  - 29: ds=26 sev=purple
  - 67: ds=23 sev=-
  - 09: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:437, 35:380, 1:161, 26:149, 31:111, 4:102, 23:100, 28:94, 15:84, 27:77

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=437 fs=0 fl=0 hz=0.002197802197802198, 35:ds=380 fs=0 fl=0 hz=0.001949317738791423, 1:ds=161 fs=6 fl=4 hz=0.012195121951219513, 26:ds=149 fs=2 fl=0 hz=0.0062402496099844, 31:ds=111 fs=28 fl=0 hz=0.03160270880361174, 4:ds=102 fs=21 fl=2 hz=0.026589595375722544, 23:ds=100 fs=25 fl=1 hz=0.029850746268656716, 28:ds=94 fs=16 fl=2 hz=0.021479713603818614, 15:ds=84 fs=14 fl=3 hz=0.020506634499396863, 27:ds=77 fs=26 fl=0 hz=0.02911534154535274

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=86 flags=red+purple
- S8: ds=60 flags=red+purple
- S0: ds=59 flags=blue+purple
- S23: ds=48 flags=blue+purple
- S5: ds=47 flags=purple
- S24: ds=45 flags=blue+purple
- S4: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=2 tags=RS
  - 278: score=2 tags=RS
  - 359: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=58 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=27), P2:3 (gap=36), P3:9 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 676: score=46.647924999999994 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 631: score=45.383667857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 671: score=45.05211357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 636: score=44.47660714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 678: score=43.758337857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 031: score=42.656528571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 071: score=42.237785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 036: score=41.61741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 638: score=41.469471428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=41.40107142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=874 sev=B
- 555: ds=869 sev=B
- 222: ds=846 sev=B
- 337: ds=823 sev=B
- 003: ds=814 sev=B
- 228: ds=805 sev=B
- 556: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=109 sev=red
  - 55: ds=73 sev=blue
  - 77: ds=42 sev=purple
  - 33: ds=36 sev=purple
  - 88: ds=34 sev=purple
  - 22: ds=32 sev=purple
  - 66: ds=19 sev=-
  - 00: ds=10 sev=-
  - 11: ds=5 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 49: ds=50 sev=blue
  - 35: ds=46 sev=blue
  - 67: ds=44 sev=blue
  - 34: ds=43 sev=blue
  - 09: ds=40 sev=blue
  - 27: ds=37 sev=blue
  - 07: ds=28 sev=purple
  - 05: ds=25 sev=purple
  - 36: ds=24 sev=-
  - 15: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:410, 26:188, 35:174, 27:139, 6:107, 5:76, 1:73, 15:68, 34:54, 31:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=410 fs=1 fl=2 hz=0.006993006993006993, 26:ds=188 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=174 fs=1 fl=1 hz=0.004968944099378882, 27:ds=139 fs=18 fl=3 hz=0.026582278481012658, 6:ds=107 fs=24 fl=2 hz=0.02957906712172924, 5:ds=76 fs=20 fl=1 hz=0.023102310231023104, 1:ds=73 fs=7 fl=3 hz=0.012127894156560088, 15:ds=68 fs=17 fl=3 hz=0.021691973969631236, 34:ds=54 fs=28 fl=1 hz=0.03159041394335512, 31:ds=50 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=77 flags=purple
- S25: ds=74 flags=purple
- S21: ds=54 flags=purple
- S20: ds=50 flags=purple
- S17: ds=48 flags=purple
- S8: ds=46 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 125: score=2 tags=RS
  - 134: score=2 tags=RS
  - 269: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=27 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=22), P2:7 (gap=25), P3:1 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 676: score=46.647924999999994 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 631: score=45.383667857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 671: score=45.05211357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 636: score=44.47660714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 678: score=43.758337857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 031: score=42.656528571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 071: score=42.237785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 036: score=41.61741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 638: score=41.469471428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=41.40107142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=977 sev=B
- 117: ds=888 sev=B
- 005: ds=874 sev=B
- 577: ds=851 sev=B
- 155: ds=831 sev=B
- 777: ds=830 sev=B
- 669: ds=822 sev=B
- 179: ds=804 sev=B
- 366: ds=770 sev=B
- 222: ds=764 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=94 sev=blue
  - 77: ds=81 sev=blue
  - 66: ds=73 sev=blue
  - 33: ds=69 sev=purple
  - 55: ds=60 sev=purple
  - 88: ds=54 sev=purple
  - 22: ds=31 sev=purple
  - 11: ds=20 sev=-
  - 44: ds=19 sev=-
  - 00: ds=10 sev=-
- non_repeating:
  - 58: ds=95 sev=red
  - 35: ds=62 sev=red
  - 29: ds=57 sev=red
  - 47: ds=47 sev=blue
  - 15: ds=43 sev=blue
  - 18: ds=29 sev=purple
  - 19: ds=29 sev=purple
  - 78: ds=25 sev=purple
  - 05: ds=23 sev=-
  - 08: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:482, 1:269, 32:236, 31:215, 4:135, 28:108, 19:104, 23:99, 26:81, 16:77

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=482 fs=3 fl=1 hz=0.017391304347826087, 1:ds=269 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=236 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=215 fs=16 fl=1 hz=0.021935483870967745, 4:ds=135 fs=21 fl=3 hz=0.028742514970059883, 28:ds=108 fs=10 fl=4 hz=0.017676767676767676, 19:ds=104 fs=12 fl=2 hz=0.016968325791855206, 23:ds=99 fs=24 fl=0 hz=0.02937576499388005, 26:ds=81 fs=0 fl=0 hz=0.002347417840375587, 16:ds=77 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=60 flags=purple
- S15: ds=51 flags=red+purple
- S9: ds=48 flags=purple
- S17: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 089: score=2 tags=RS
  - 269: score=2 tags=RS
  - 278: score=2 tags=RS
  - 359: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:764(B); midday:846(B)
- 366 -> combined:964(B); evening:770(B)
- 688 -> combined:732(B); evening:729(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:41(blue); midday:25(purple)
- 15 -> combined:52(blue); evening:43(blue)
- 18 -> combined:50(blue); evening:29(purple)
- 22 -> combined:56(purple); evening:31(purple); midday:32(purple)
- 29 -> combined:26(purple); evening:57(red)
- 33 -> combined:81(blue); evening:69(purple); midday:36(purple)
- 35 -> combined:102(red); evening:62(red); midday:46(blue)
- 47 -> combined:46(blue); evening:47(blue)
- 55 -> combined:110(red); evening:60(purple); midday:73(blue)
- 66 -> combined:44(purple); evening:73(blue)
- 77 -> combined:94(blue); evening:81(blue); midday:42(purple)
- 78 -> combined:45(blue); evening:25(purple)
- 88 -> combined:76(blue); evening:54(purple); midday:34(purple)
- 99 -> combined:173(red); evening:94(blue); midday:109(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(6.853899999999999)[R2,XVAR-Cons(CEM)], 0(6.785499999999999)[R1,XVAR-Cons(CEM)], 9(5.764371428571429)[R3,XVAR-Cons(CEM)]
- P2: 7(7.964428571428571)[R1,XVAR-Cons(CEM)], 3(7.383171428571428)[R2,Mirror-Echo], 8(3.073657142857143)[R3,Mirror-Echo], 5(0.3418428571428571)[R3,Swap]
- P3: 1(3.487857142857143)[R1,Mirror-Echo], 8(3.2324)[R2,XVAR-Cons(CE)], 6(2.4487428571428573)[R3,Mirror-Echo], 9(1.2269999999999999)[R1,Double-Pressure], 5(0.2074857142857143)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=24), P2:7(gap=45), P3:1(gap=11); top cartesian candidates: 676, 631, 671, 636, 678.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1'], 'pairs': {'remaining_count': 1}}; top candidates: 017, 026, 035, 089, 125.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:846(B),evening:764(B); 366→combined:964(B),evening:770(B); 688→combined:732(B),evening:729(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:437, 35:380, 1:161, 26:149, 31:111.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=754 Evening=976; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 457 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 679 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 754 (canon 457): box `457` covers winner `754` (boxed hit).
  - Evening winner 976 (canon 679): box `679` covers winner `976` (boxed hit).
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
