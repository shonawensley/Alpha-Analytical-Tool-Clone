# Master Validation Run Report — NorthCarolina4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-09/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-09/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-09/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-09/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-09/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-09/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac20_winner_177_20260110_035051.html`
- `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac9_winner_960_20260110_035052.html`

Winners JSON files:
- `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac20_winner_177_20260110_035051.json`
- `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac9_winner_960_20260110_035052.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 177 (canon 177): exact_boxed=True exact_straight=False | rank 2273/6271 (rank_frac 0.362); Evening 960 (canon 069): exact_boxed=True exact_straight=True | rank 602/6271 (rank_frac 0.096)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 177 idx20 (rank 32/35, frac 0.914), 960 idx9 (rank 11/35, frac 0.314)
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

### 2.Stable — NorthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-09)

## Midday winner 177 (canonical 177)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=579 | exact_boxed=12 | exact_straight=0 | vt_boxed=12
- Scores (patterns_scores.csv): rank 2273/6271 (rank_frac 0.3624621272524318) | score 15.0 (top 38.5, ratio 0.38961038961038963, delta 23.5) | section Combined, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why boxed|cov2|hp_repeat4|hot1|perm2|double_mirror|draw_chain4
- Compound (patterns_compound.csv): rank 230/1782 (rank_frac 0.12906846240179573) | score 25.0 (top 107.0, ratio 0.2336448598130841, delta 82.0) | section Combined, col1_hits 0, hot2 0, set_chain 1, draw_chain 4 | why draw_chain4|hot1x3|dblmirrorx10
- Families (patterns_families.csv): count 84 | rank 79/1740 (rank_frac 0.045402298850574715) | score 29.0 (top 36.5, ratio 0.7945205479452054, delta 7.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=False | vt_boxed_count=5

## Evening winner 960 (canonical 069)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=25 | family_rows=89 | exact_boxed=25 | exact_straight=21 | vt_boxed=25
- Scores (patterns_scores.csv): rank 602/6271 (rank_frac 0.09599744857279541) | score 21.0 (top 38.5, ratio 0.5454545454545454, delta 17.5) | section Midday, Set Set1, Draw Draw2, Col 1, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat6|vstr2|hot2|perm2|draw_chain2
- Compound (patterns_compound.csv): rank 96/1782 (rank_frac 0.05387205387205387) | score 37.0 (top 107.0, ratio 0.34579439252336447, delta 70.0) | section Combined, col1_hits 4, hot2 4, set_chain 1, draw_chain 4 | why draw_chain4|col1x4|hot1x1|hot2x4|vstrx9
- Families (patterns_families.csv): count 52 | rank 419/1740 (rank_frac 0.24080459770114943) | score 22.0 (top 36.5, ratio 0.6027397260273972, delta 14.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=122

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 466 | section Combined | score 103.0 | col1_hits 9 | hot2 11
- rank    1 | canon 066 | section Combined | score 107.0 | col1_hits 9 | hot2 11
- rank    2 | canon 446 | section Evening | score 106.5 | col1_hits 9 | hot2 11
- rank    4 | canon 099 | section Midday | score 99.0 | col1_hits 9 | hot2 11
- rank    6 | canon 4466 | section Evening | score 90.5 | col1_hits 8 | hot2 11
- rank    5 | canon 466 | section Evening | score 97.5 | col1_hits 8 | hot2 11
- rank    8 | canon 667 | section Combined | score 82.0 | col1_hits 6 | hot2 10
- rank   56 | canon 699 | section Midday | score 44.0 | col1_hits 4 | hot2 7
- rank    7 | canon 366 | section Combined | score 85.5 | col1_hits 6 | hot2 7
- rank   22 | canon 0699 | section Midday | score 55.5 | col1_hits 4 | hot2 7

## Top families (patterns_families.csv)
- rank 1694 | family 19 | score 6.5 | hot2 0 | section Midday
- rank  673 | family 8 | score 19.0 | hot2 0 | section Midday
- rank  918 | family 25 | score 16.0 | hot2 0 | section Midday
- rank  918 | family 6 | score 16.0 | hot2 0 | section Midday
- rank 1120 | family 17 | score 14.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 177 (canon 177): exact_boxed=True exact_straight=False | rank 2273/6271 (rank_frac 0.362); Evening 960 (canon 069): exact_boxed=True exact_straight=True | rank 602/6271 (rank_frac 0.096)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260110)

## Midday winner 177 (canonical 177)
- Stamp (winner_stamp.json): items_total=36 | exact_any=0 exact_final=0 | vtrac_any=36 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=36 | exact_any=0 vtrac_any=36 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=36 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=6 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 960 (canonical 069)
- Stamp (winner_stamp.json): items_total=147 | exact_any=0 exact_final=0 | vtrac_any=146 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=45 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=147 | exact_any=0 vtrac_any=146 | drop_exact_any=0 drop_vtrac_any=45 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=28 vt_straight=0
- Hits (winner_hits.csv): rows=147 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=28 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.458571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 177 (canonical 177)
- Stamp (winner_stamp.json): items_total=204 | exact_any=0 exact_final=0 | vtrac_any=204 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=204 | exact_any=0 vtrac_any=204 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=204 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.227143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 992 | score_v2 12.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 992 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 11.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 11.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 7 | pattern 992 | score_v2 11.487143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 7 | pattern 992 | score_v2 11.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 992 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 400 | score_v2 11.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 400 | score_v2 11.227143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set2 draw Draw1 col 6 | pattern 992 | score_v2 11.227143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 992 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 992 | score_v2 11.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 400 | score_v2 11.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 559 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 440 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 406 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 924 | score_v2 10.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 940 | score_v2 10.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 994 | score_v2 10.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 559 | score_v2 9.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 177 (canon 177): items_total=36 exact_any=0 vtrac_any=36 | top winner_present=False best_rank=None/6; Evening 960 (canon 069): items_total=147 exact_any=0 vtrac_any=146 | top winner_present=False best_rank=None/24; Combined 177 (canon 177): items_total=204 exact_any=0 vtrac_any=204 | top winner_present=False best_rank=None/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 992, 992, 400, 559, 440.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260110_035300)

## Top indices (from enhanced JSON)
- index 25 | score 90.43150499999996 | features: presence=57.47400499999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 80.20932499999995 | features: presence=55.601824999999955, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 68.55818749999997 | features: presence=44.60068749999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 48.36541249999999 | features: presence=35.68791249999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 41.1589875 | features: presence=29.681487500000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 16 | score 32.1813 | features: presence=22.683800000000005, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 35 | score 28.59125 | features: presence=11.86375, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 27.5314125 | features: presence=18.223912499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 23.227135000000004 | features: presence=11.519635000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 2 | score 22.534980000000004 | features: presence=15.287480000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
416, 964, 194, 694, 614, 136, 619, 196, 036, 940

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 177 | index 20 | file NorthCarolina4_vtrac20_winner_177_20260110_035051.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 960 | index 9 | file NorthCarolina4_vtrac9_winner_960_20260110_035052.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 177 | index 20 rank 32/35 (rank_frac 0.9142857142857143) | score 0.0 (top 90.43150499999996, ratio 0.0, delta 90.43150499999996) | winner_in_index_straights=False | top_index_straights: (none)
- winner 960 | index 9 rank 11/35 (rank_frac 0.3142857142857143) | score 21.1506625 (top 90.43150499999996, ratio 0.23388599470947663, delta 69.28084249999996) | winner_in_index_straights=False | top_index_straights: 406 (8.178), 604 (5.992), 019 (5.662)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 177→idx20 rank 32/35 (frac 0.914); 960→idx9 rank 11/35 (frac 0.314).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 25, 19, 15, 18, 6.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-09)

## Midday winner 177 (canonical 177)
- Top lanes (hot_zones_top_lanes.csv): present | rank 67/204 (rank_frac 0.3284313725490196) | score_mean 16.821 (top 22.25, ratio 0.7560000000000001, delta 5.4289999999999985)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 960 (canonical 069)
- Top lanes (hot_zones_top_lanes.csv): present | rank 110/204 (rank_frac 0.5392156862745098) | score_mean 15.948 (top 22.25, ratio 0.7167640449438203, delta 6.302)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 338 | vt_triad 44 | score_mean 22.25 | tags hot16,hot20,literal_draw,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 123 | vt_triad 234 | score_mean 21.721 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 022 | vt_triad 13 | score_mean 20.387 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_straight
- rank    4 | triad 247 | vt_triad 335 | score_mean 20.3 | tags hot16,hot20,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    4 | triad 279 | vt_triad 335 | score_mean 20.3 | tags hot16,hot20,set1_bonus,vertical1,vt_only_lane,vt_straight
- rank    6 | triad 244 | vt_triad 35 | score_mean 20.058 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    7 | triad 299 | vt_triad 35 | score_mean 19.846 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 146 | vt_triad 225 | score_mean 19.649 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 255 | vt_triad 13 | score_mean 19.589 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank   10 | triad 169 | vt_triad 225 | score_mean 19.5 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 177 (canon 177): rank 67/204 (rank_frac 0.328) ratio_to_top=0.7560000000000001; Evening 960 (canon 069): rank 110/204 (rank_frac 0.539) ratio_to_top=0.7167640449438203
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

Aux draws snapshot dir: `sharepacks/2026-01-09/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-09/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=571, 132, 202, 184, 298
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-09/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=132, 184, 552, 553, 187
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-09/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=571, 202, 298, 895, 887

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=10 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=29), P2:4 (gap=47), P3:0 (gap=38)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=51.12089107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 940: score=44.38727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=43.54786428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 646: score=40.37421857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 920: score=40.1561 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 648: score=36.43705 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=36.14304714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 649: score=36.027049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 644: score=35.92365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 690: score=35.62297857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=890 sev=B
- 446: ds=886 sev=B
- 445: ds=826 sev=B
- 122: ds=809 sev=B
- 036: ds=805 sev=B
- 555: ds=782 sev=B
- 299: ds=779 sev=B
- 277: ds=771 sev=B
- 112: ds=760 sev=B
- 034: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=166 sev=red
  - 77: ds=139 sev=red
  - 99: ds=62 sev=purple
  - 44: ds=60 sev=purple
  - 11: ds=22 sev=-
  - 66: ds=21 sev=-
  - 33: ds=12 sev=-
  - 88: ds=8 sev=-
  - 55: ds=5 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 56: ds=68 sev=red
  - 27: ds=64 sev=red
  - 09: ds=53 sev=blue
  - 04: ds=47 sev=blue
  - 06: ds=47 sev=blue
  - 24: ds=43 sev=blue
  - 01: ds=37 sev=blue
  - 08: ds=37 sev=blue
  - 36: ds=29 sev=purple
  - 49: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:494, 1:121, 27:117, 31:108, 15:92, 16:90, 23:69, 35:60, 12:58, 6:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=494 fs=3 fl=0 hz=0.009389671361502348, 1:ds=121 fs=0 fl=3 hz=0.00625, 27:ds=117 fs=15 fl=2 hz=0.02463768115942029, 31:ds=108 fs=19 fl=3 hz=0.02502844141069397, 15:ds=92 fs=15 fl=2 hz=0.019495412844036695, 16:ds=90 fs=4 fl=1 hz=0.008836524300441826, 23:ds=69 fs=17 fl=3 hz=0.024330900243309, 35:ds=60 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=58 fs=45 fl=1 hz=0.04962243797195254, 6:ds=55 fs=22 fl=3 hz=0.02771618625277162

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=43 flags=blue+purple
- S18: ds=36 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 036: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 027: score=2 tags=RS
  - 045: score=2 tags=RS
  - 135: score=2 tags=RS
  - 189: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=103 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=42), P2:9 (gap=32), P3:8 (gap=28)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=51.12089107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 940: score=44.38727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=43.54786428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 646: score=40.37421857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 920: score=40.1561 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 648: score=36.43705 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=36.14304714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 649: score=36.027049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 644: score=35.92365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 690: score=35.62297857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=980 sev=B
- 446: ds=932 sev=B
- 777: ds=892 sev=B
- 119: ds=857 sev=B
- 222: ds=827 sev=B
- 155: ds=789 sev=B
- 488: ds=783 sev=B
- 177: ds=759 sev=B
- 007: ds=738 sev=B
- 338: ds=718 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=162 sev=red
  - 00: ds=137 sev=red
  - 77: ds=69 sev=purple
  - 99: ds=57 sev=purple
  - 22: ds=45 sev=purple
  - 11: ds=15 sev=-
  - 88: ds=11 sev=-
  - 66: ds=10 sev=-
  - 33: ds=6 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 07: ds=61 sev=red
  - 28: ds=53 sev=blue
  - 26: ds=48 sev=blue
  - 02: ds=45 sev=blue
  - 29: ds=42 sev=blue
  - 56: ds=36 sev=purple
  - 27: ds=33 sev=purple
  - 38: ds=28 sev=purple
  - 05: ds=26 sev=purple
  - 09: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:385, 25:193, 32:173, 35:147, 11:112, 31:105, 2:101, 33:84, 12:62, 1:60

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=385 fs=1 fl=0 hz=0.005905511811023622, 25:ds=193 fs=15 fl=1 hz=0.02165087956698241, 32:ds=173 fs=3 fl=1 hz=0.007416563658838071, 35:ds=147 fs=0 fl=2 hz=0.005201560468140442, 11:ds=112 fs=50 fl=0 hz=0.056882821387940846, 31:ds=105 fs=24 fl=0 hz=0.02793946449359721, 2:ds=101 fs=13 fl=3 hz=0.018223234624145785, 33:ds=84 fs=21 fl=2 hz=0.025136612021857924, 12:ds=62 fs=47 fl=0 hz=0.05181918412348401, 1:ds=60 fs=2 fl=2 hz=0.00641025641025641

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=96 flags=purple
- S20: ds=84 flags=red+purple
- S2: ds=75 flags=purple
- S5: ds=71 flags=purple
- S8: ds=66 flags=purple

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
- current_index=7 streak=1 max=3 last_repeat_gap=27 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:4 (gap=42), P3:0 (gap=19)
- consensus_notes: P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:4 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=51.12089107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 940: score=44.38727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 620: score=43.54786428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 646: score=40.37421857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 920: score=40.1561 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 648: score=36.43705 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=36.14304714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 649: score=36.027049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 644: score=35.92365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 690: score=35.62297857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=981 sev=B
- 299: ds=938 sev=B
- 223: ds=868 sev=B
- 122: ds=857 sev=B
- 116: ds=834 sev=B
- 039: ds=817 sev=B
- 377: ds=805 sev=B
- 277: ds=791 sev=B
- 188: ds=779 sev=B
- 557: ds=778 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=129 sev=red
  - 77: ds=87 sev=blue
  - 00: ds=83 sev=blue
  - 66: ds=45 sev=purple
  - 99: ds=31 sev=purple
  - 44: ds=30 sev=purple
  - 11: ds=11 sev=-
  - 33: ds=6 sev=-
  - 88: ds=4 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 45: ds=106 sev=red
  - 34: ds=47 sev=blue
  - 04: ds=42 sev=blue
  - 06: ds=36 sev=purple
  - 08: ds=35 sev=purple
  - 56: ds=34 sev=purple
  - 27: ds=32 sev=purple
  - 09: ds=29 sev=purple
  - 23: ds=27 sev=purple
  - 24: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:265, 26:247, 13:212, 1:154, 23:123, 5:104, 17:103, 27:60, 31:54, 15:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=265 fs=18 fl=0 hz=0.024896265560165977, 26:ds=247 fs=1 fl=2 hz=0.006666666666666667, 13:ds=212 fs=19 fl=0 hz=0.024675324675324673, 1:ds=154 fs=2 fl=3 hz=0.007434944237918215, 23:ds=123 fs=13 fl=3 hz=0.019184652278177457, 5:ds=104 fs=15 fl=2 hz=0.020809248554913295, 17:ds=103 fs=29 fl=0 hz=0.03553921568627451, 27:ds=60 fs=22 fl=3 hz=0.027085590465872156, 31:ds=54 fs=21 fl=2 hz=0.024338624338624337, 15:ds=46 fs=16 fl=1 hz=0.01829924650161464

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=97 flags=purple
- S0: ds=83 flags=blue+purple
- S2: ds=51 flags=purple
- S21: ds=38 flags=red+purple
- S7: ds=36 flags=purple

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
- 036 -> combined:805(B); evening:731(B)
- 122 -> combined:809(B); evening:857(B)
- 155 -> combined:890(B); midday:789(B)
- 277 -> combined:771(B); evening:791(B)
- 299 -> combined:779(B); evening:938(B)
- 446 -> combined:886(B); midday:932(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:166(red); evening:83(blue); midday:137(red)
- 04 -> combined:47(blue); evening:42(blue)
- 06 -> combined:47(blue); evening:36(purple)
- 08 -> combined:37(blue); evening:35(purple)
- 09 -> combined:53(blue); evening:29(purple); midday:26(purple)
- 24 -> combined:43(blue); evening:25(purple)
- 26 -> combined:26(purple); midday:48(blue)
- 27 -> combined:64(red); evening:32(purple); midday:33(purple)
- 44 -> combined:60(purple); evening:30(purple); midday:162(red)
- 56 -> combined:68(red); evening:34(purple); midday:36(purple)
- 77 -> combined:139(red); evening:87(blue); midday:69(purple)
- 99 -> combined:62(purple); evening:31(purple); midday:57(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(5.401064285714286)[R1,XVAR-Cons(CEM)], 9(3.5092999999999996)[R2,XVAR-Cons(CM)], 7(2.8744285714285716)[R3,XVAR-Cons(CE)], 2(1.7449999999999999)[R1,Double-Pressure], 4(1.0553)[R2,Double-Pressure]
- P2: 4(9.029985714285715)[R1,XVAR-Cons(CEM)], 2(5.798814285714286)[R2,XVAR-Cons(CEM)], 9(1.8739285714285714)[R1,Mirror-Echo], 3(1.0461999999999998)[R2,Double-Pressure], 6(0.34042857142857147)[R3,Swap]
- P3: 0(7.847985714285715)[R1,XVAR-Cons(CEM)], 6(1.7868071428571428)[R3,XVAR-Cons(CE)], 8(1.506)[R1,Double-Pressure], 9(1.0959999999999999)[R2,Double-Pressure], 4(0.9925999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=29), P2:4(gap=47), P3:0(gap=38); top cartesian candidates: 640, 940, 620, 646, 920.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 036, 126, 369, 468, 567.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:805(B),evening:731(B); 122→combined:809(B),evening:857(B); 155→combined:890(B),midday:789(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:494, 1:121, 27:117, 31:108, 15:92.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=177 Evening=960; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 177 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 069 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 177 (canon 177): box `177` covers winner `177` (boxed hit).
  - Evening winner 960 (canon 069): box `069` covers winner `960` (boxed hit).
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
