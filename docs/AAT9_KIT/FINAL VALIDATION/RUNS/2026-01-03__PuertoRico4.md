# Master Validation Run Report — PuertoRico4 — results 2026-01-03 (history workbook ~ 2026-01-02)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-03/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-03/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-03/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-03/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-03/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-03/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-03/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac12_winner_529_20260105_054602.html`
- `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac14_winner_359_20260105_054604.html`

Winners JSON files:
- `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac12_winner_529_20260105_054602.json`
- `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac14_winner_359_20260105_054604.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-03/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 529 (canon 259): exact_boxed=True exact_straight=True | rank 497/4661 (rank_frac 0.107); Evening 359 (canon 359): exact_boxed=True exact_straight=True | rank 1586/4661 (rank_frac 0.340)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 529 idx12 (rank 20/35, frac 0.571), 359 idx14 (rank 10/35, frac 0.286)
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

### 2.Stable — PuertoRico4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-03)

## Midday winner 529 (canonical 259)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=15 | family_rows=309 | exact_boxed=15 | exact_straight=3 | vt_boxed=15
- Scores (patterns_scores.csv): rank 497/4661 (rank_frac 0.10662947865264964) | score 17.5 (top 36.5, ratio 0.4794520547945205, delta 19.0) | section Evening, Set Set3, Draw Draw1, Col 4, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat2|vstr2|hot1|perm2|hidden3v|set_chain3
- Compound (patterns_compound.csv): rank 159/1792 (rank_frac 0.08872767857142858) | score 24.5 (top 97.5, ratio 0.2512820512820513, delta 73.0) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|hot1x1
- Families (patterns_families.csv): count 48 | rank 38/1307 (rank_frac 0.029074215761285386) | score 25.5 (top 32.5, ratio 0.7846153846153846, delta 7.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=84

## Evening winner 359 (canonical 359)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=15 | family_rows=319 | exact_boxed=15 | exact_straight=15 | vt_boxed=15
- Scores (patterns_scores.csv): rank 1586/4661 (rank_frac 0.3402703282557391) | score 13.5 (top 36.5, ratio 0.3698630136986301, delta 23.0) | section Midday, Set Set1, Draw Draw7, Col 1, hot 0, vt_straight 2.0 | why straight|cov1|hidden3v|vtrac_straight|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 317/1792 (rank_frac 0.17689732142857142) | score 20.5 (top 97.5, ratio 0.21025641025641026, delta 77.0) | section Midday, col1_hits 1, hot2 0, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x1|vstrx1
- Families (patterns_families.csv): count 45 | rank 38/1307 (rank_frac 0.029074215761285386) | score 25.5 (top 32.5, ratio 0.7846153846153846, delta 7.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=106

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 226 | section Combined | score 97.5 | col1_hits 8 | hot2 11
- rank    2 | canon 022 | section Combined | score 71.5 | col1_hits 6 | hot2 8
- rank    4 | canon 268 | section Evening | score 59.5 | col1_hits 6 | hot2 8
- rank    8 | canon 134 | section Midday | score 48.5 | col1_hits 0 | hot2 6
- rank   22 | canon 236 | section Midday | score 39.5 | col1_hits 2 | hot2 4
- rank  113 | canon 026 | section Midday | score 27.5 | col1_hits 2 | hot2 4
- rank   79 | canon 2268 | section Combined | score 30.5 | col1_hits 2 | hot2 4
- rank   93 | canon 268 | section Combined | score 29.5 | col1_hits 2 | hot2 4
- rank   24 | canon 2256 | section Combined | score 39.0 | col1_hits 4 | hot2 4
- rank    7 | canon 225 | section Combined | score 52.5 | col1_hits 4 | hot2 4

## Top families (patterns_families.csv)
- rank 1302 | family 11 | score 4.0 | hot2 0 | section Midday
- rank 1282 | family 3 | score 5.0 | hot2 0 | section Midday
- rank  632 | family 34 | score 14.0 | hot2 0 | section Midday
- rank  761 | family 21 | score 12.5 | hot2 0 | section Midday
- rank  789 | family 25 | score 12.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 529 (canon 259): exact_boxed=True exact_straight=True | rank 497/4661 (rank_frac 0.107); Evening 359 (canon 359): exact_boxed=True exact_straight=True | rank 1586/4661 (rank_frac 0.340)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260105)

## Midday winner 529 (canonical 259)
- Stamp (winner_stamp.json): items_total=132 | exact_any=12 exact_final=0 | vtrac_any=108 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=122 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=72 family_vtrac_final=0
- Flags (winner_flags.csv): rows=132 | exact_any=12 vtrac_any=108 | drop_exact_any=12 drop_vtrac_any=122 | family_exact_any=0 family_vtrac_any=72 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=132 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=True | winner_best_rank=40 | winner_rank_fraction=1.5384615384615385 | winner_score_v2=8.427143 top_score_v2=9.977143 | winner_score_ratio_to_top=0.8446449048590362 winner_score_delta_from_top=1.5500000000000007
- Reducer scores present: True

## Evening winner 359 (canonical 359)
- Stamp (winner_stamp.json): items_total=58 | exact_any=0 exact_final=0 | vtrac_any=8 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=56 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=8 family_vtrac_final=0
- Flags (winner_flags.csv): rows=58 | exact_any=0 vtrac_any=8 | drop_exact_any=2 drop_vtrac_any=56 | family_exact_any=0 family_vtrac_any=8 | vt_boxed=34 vt_straight=0
- Hits (winner_hits.csv): rows=58 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=34 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 529 (canonical 259)
- Stamp (winner_stamp.json): items_total=496 | exact_any=156 exact_final=0 | vtrac_any=422 vtrac_final=0 | drop_exact_any=186 drop_exact_final=0 | drop_vtrac_any=458 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=296 family_vtrac_final=0
- Flags (winner_flags.csv): rows=496 | exact_any=156 vtrac_any=422 | drop_exact_any=186 drop_vtrac_any=458 | family_exact_any=2 family_vtrac_any=296 | vt_boxed=38 vt_straight=0
- Hits (winner_hits.csv): rows=496 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=38 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=True | winner_best_rank=20 | winner_rank_fraction=1.0 | winner_score_v2=9.627143 top_score_v2=16.627143 | winner_score_ratio_to_top=0.5790016360597849 winner_score_delta_from_top=7.0
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 220 | score_v2 16.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 220 | score_v2 16.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 226 | score_v2 15.114643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 522 | score_v2 14.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 522 | score_v2 14.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 226 | score_v2 14.064643 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 522 | score_v2 13.977143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw4 col 3 | pattern 522 | score_v2 13.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 13.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 522 | score_v2 13.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 220 | score_v2 16.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 226 | score_v2 15.114643 | tags exact,vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 522 | score_v2 14.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 552 | score_v2 13.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 220 | score_v2 12.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 522 | score_v2 12.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 226 | score_v2 11.914643 | tags exact,vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 552 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 552 | score_v2 10.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 522 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 529 (canon 259): items_total=132 exact_any=12 vtrac_any=108 | top winner_present=True best_rank=40/26; Evening 359 (canon 359): items_total=58 exact_any=0 vtrac_any=8 | top winner_present=False best_rank=None/26; Combined 529 (canon 259): items_total=496 exact_any=156 vtrac_any=422 | top winner_present=True best_rank=20/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 220, 226, 522, 552, 220.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260105_054823)

## Top indices (from enhanced JSON)
- index 20 | score 49.65784 | features: presence=35.660340000000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 46.6877675 | features: presence=31.630267500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 34 | score 36.1979 | features: presence=23.8204, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 27.564360000000004 | features: presence=17.62686, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 15 | score 26.373250000000002 | features: presence=15.735750000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 24.342717500000003 | features: presence=14.975217500000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 21 | score 20.165012500000007 | features: presence=12.437512500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 25 | score 19.322150000000004 | features: presence=11.99465, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 23 | score 18.33675 | features: presence=11.219249999999997, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 14 | score 18.105050000000002 | features: presence=10.191300000000002, set_echo=0.6, first_hit=0.4, column_span=0.29375

## Top straights (from enhanced JSON)
136, 534, 134, 631, 613, 413, 341, 634, 624, 762

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 529 | index 12 | file PuertoRico4_vtrac12_winner_529_20260105_054602.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 359 | index 14 | file PuertoRico4_vtrac14_winner_359_20260105_054604.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 529 | index 12 rank 20/35 (rank_frac 0.5714285714285714) | score 10.421750000000001 (top 49.65784, ratio 0.20987119053104206, delta 39.23609) | winner_in_index_straights=False | top_index_straights: 524 (5.44), 245 (3.655)
- winner 359 | index 14 rank 10/35 (rank_frac 0.2857142857142857) | score 18.105050000000002 (top 49.65784, ratio 0.36459600337026343, delta 31.552789999999998) | winner_in_index_straights=False | top_index_straights: 534 (13.791)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 529→idx12 rank 20/35 (frac 0.571); 359→idx14 rank 10/35 (frac 0.286).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 20, 18, 34, 24, 15.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-03)

## Midday winner 529 (canonical 259)
- Top lanes (hot_zones_top_lanes.csv): present | rank 62/210 (rank_frac 0.29523809523809524) | score_mean 17.521 (top 21.768, ratio 0.8048970966556414, delta 4.247)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 359 (canonical 359)
- Top lanes (hot_zones_top_lanes.csv): present | rank 110/210 (rank_frac 0.5238095238095238) | score_mean 16.386 (top 21.768, ratio 0.7527563395810363, delta 5.3820000000000014)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 144 | vt_triad 25 | score_mean 21.768 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 227 | vt_triad 33 | score_mean 21.025 | tags funnel_precol1,hot12,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 277 | vt_triad 33 | score_mean 21.025 | tags funnel_precol1,hot12,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 344 | vt_triad 45 | score_mean 20.919 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 336 | vt_triad 24 | score_mean 20.395 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 267 | vt_triad 233 | score_mean 20.23 | tags funnel_precol1,hot12,hot16,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 445 | vt_triad 15 | score_mean 20.222 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 145 | vt_triad 125 | score_mean 19.93 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 049 | vt_triad 155 | score_mean 19.91 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank   10 | triad 139 | vt_triad 245 | score_mean 19.828 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 529 (canon 259): rank 62/210 (rank_frac 0.295) ratio_to_top=0.8048970966556414; Evening 359 (canon 359): rank 110/210 (rank_frac 0.524) ratio_to_top=0.7527563395810363
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

Aux draws snapshot dir: `sharepacks/2026-01-03/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=917, 144, 913, 451, 643
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=144, 451, 098, 875, 793
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=917, 913, 643, 785, 490

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=7 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=60), P2:3 (gap=20), P3:9 (gap=35)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=60)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=993 sev=B
- 447: ds=984 sev=B
- 000: ds=732 sev=B
- 039: ds=720 sev=B
- 466: ds=716 sev=B
- 677: ds=694 sev=B
- 259: ds=685 sev=B
- 577: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=64 sev=purple
  - 77: ds=63 sev=purple
  - 99: ds=54 sev=purple
  - 11: ds=48 sev=purple
  - 55: ds=29 sev=purple
  - 33: ds=24 sev=-
  - 66: ds=23 sev=-
  - 88: ds=16 sev=-
  - 00: ds=14 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 47: ds=172 sev=red
  - 24: ds=86 sev=red
  - 25: ds=61 sev=red
  - 48: ds=50 sev=blue
  - 23: ds=47 sev=blue
  - 56: ds=43 sev=blue
  - 59: ds=43 sev=blue
  - 05: ds=41 sev=blue
  - 28: ds=36 sev=purple
  - 35: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:191, 27:132, 5:95, 32:89, 26:84, 31:81, 28:63, 18:55, 34:54, 33:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=191 fs=18 fl=1 hz=0.025477707006369428, 27:ds=132 fs=24 fl=1 hz=0.029868578255675033, 5:ds=95 fs=27 fl=1 hz=0.0343980343980344, 32:ds=89 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=84 fs=4 fl=2 hz=0.01020408163265306, 31:ds=81 fs=14 fl=3 hz=0.018619934282584887, 28:ds=63 fs=26 fl=0 hz=0.0278372591006424, 18:ds=55 fs=20 fl=0 hz=0.022727272727272728, 34:ds=54 fs=26 fl=0 hz=0.02857142857142857, 33:ds=51 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=81 flags=purple
- S23: ds=63 flags=blue+purple
- S26: ds=54 flags=blue+purple
- S8: ds=48 flags=purple
- S6: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '8'], 'pairs': {'remaining_count': 1}}
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
- current_index=25 streak=1 max=3 last_repeat_gap=60 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:1 (gap=26), P3:9 (gap=17)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=960 sev=B
- 299: ds=951 sev=B
- 003: ds=942 sev=B
- 077: ds=928 sev=B
- 333: ds=877 sev=B
- 555: ds=851 sev=B
- 088: ds=822 sev=B
- 888: ds=816 sev=B
- 666: ds=801 sev=B
- 447: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=107 sev=red
  - 22: ds=80 sev=blue
  - 11: ds=56 sev=purple
  - 99: ds=40 sev=purple
  - 77: ds=31 sev=purple
  - 33: ds=25 sev=purple
  - 88: ds=22 sev=-
  - 55: ds=14 sev=-
  - 66: ds=11 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 47: ds=113 sev=red
  - 24: ds=59 sev=red
  - 38: ds=44 sev=blue
  - 03: ds=43 sev=blue
  - 04: ds=43 sev=blue
  - 35: ds=41 sev=blue
  - 48: ds=33 sev=purple
  - 19: ds=32 sev=purple
  - 25: ds=30 sev=purple
  - 18: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:97, 10:95, 27:94, 26:91, 3:84, 16:56, 23:51, 15:49, 5:47, 32:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=97 fs=16 fl=2 hz=0.020809248554913295, 10:ds=95 fs=20 fl=3 hz=0.026376146788990827, 27:ds=94 fs=19 fl=1 hz=0.024721878862793572, 26:ds=91 fs=7 fl=2 hz=0.011682242990654207, 3:ds=84 fs=31 fl=0 hz=0.03506787330316742, 16:ds=56 fs=4 fl=2 hz=0.009695290858725763, 23:ds=51 fs=31 fl=1 hz=0.034782608695652174, 15:ds=49 fs=25 fl=0 hz=0.026939655172413795, 5:ds=47 fs=28 fl=0 hz=0.03181818181818182, 32:ds=44 fs=2 fl=1 hz=0.006112469437652812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=43 flags=purple
- S25: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=2 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:5 (gap=46), P3:6 (gap=22)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=992 sev=B
- 579: ds=973 sev=B
- 114: ds=917 sev=B
- 555: ds=856 sev=B
- 888: ds=764 sev=B
- 067: ds=753 sev=B
- 446: ds=740 sev=B
- 259: ds=738 sev=B
- 224: ds=724 sev=B
- 449: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=144 sev=red
  - 44: ds=140 sev=red
  - 77: ds=42 sev=purple
  - 66: ds=33 sev=purple
  - 22: ds=32 sev=purple
  - 99: ds=27 sev=purple
  - 11: ds=24 sev=-
  - 33: ds=12 sev=-
  - 88: ds=8 sev=-
  - 00: ds=7 sev=-
- non_repeating:
  - 25: ds=100 sev=red
  - 47: ds=86 sev=red
  - 45: ds=70 sev=red
  - 26: ds=63 sev=red
  - 59: ds=56 sev=red
  - 24: ds=43 sev=blue
  - 05: ds=39 sev=blue
  - 56: ds=39 sev=blue
  - 23: ds=30 sev=purple
  - 89: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:449, 32:164, 4:118, 10:105, 31:93, 5:83, 33:69, 27:66, 1:58, 14:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=449 fs=5 fl=1 hz=0.01662049861495845, 32:ds=164 fs=6 fl=1 hz=0.009987515605493134, 4:ds=118 fs=23 fl=2 hz=0.03071253071253071, 10:ds=105 fs=16 fl=2 hz=0.0234375, 31:ds=93 fs=18 fl=3 hz=0.02394526795895097, 5:ds=83 fs=18 fl=2 hz=0.022446689113355782, 33:ds=69 fs=12 fl=1 hz=0.017361111111111112, 27:ds=66 fs=18 fl=1 hz=0.02358490566037736, 1:ds=58 fs=4 fl=4 hz=0.00909090909090909, 14:ds=48 fs=37 fl=1 hz=0.04171240395170143

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=76 flags=purple
- S24: ds=67 flags=purple
- S18: ds=52 flags=red+purple
- S23: ds=47 flags=blue+purple
- S16: ds=42 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:685(B); evening:738(B)
- 447 -> combined:984(B); midday:740(B)
- 555 -> evening:856(B); midday:851(B)
- 888 -> evening:764(B); midday:816(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:41(blue); evening:39(blue)
- 11 -> combined:48(purple); midday:56(purple)
- 22 -> combined:64(purple); evening:32(purple); midday:80(blue)
- 23 -> combined:47(blue); evening:30(purple)
- 24 -> combined:86(red); evening:43(blue); midday:59(red)
- 25 -> combined:61(red); evening:100(red); midday:30(purple)
- 47 -> combined:172(red); evening:86(red); midday:113(red)
- 48 -> combined:50(blue); evening:25(purple); midday:33(purple)
- 55 -> combined:29(purple); evening:144(red)
- 56 -> combined:43(blue); evening:39(blue)
- 59 -> combined:43(blue); evening:56(red)
- 77 -> combined:63(purple); evening:42(purple); midday:31(purple)
- 99 -> combined:54(purple); evening:27(purple); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.891428571428571)[R1,XVAR-Cons(CEM)], 3(6.397621428571428)[R2,XVAR-Cons(CEM)], 5(1.9518642857142858)[R3,XVAR-Cons(CM)], 1(1.0135)[R2,Double-Pressure]
- P2: 2(3.790407142857143)[R2,XVAR-Cons(CE)], 3(3.5793714285714286)[R1,XVAR-Cons(CM)], 1(1.4762857142857142)[R1,Double-Pressure], 5(1.145)[R1,Swap], 7(0.5755357142857142)[R3,Mirror-Echo]
- P3: 9(7.829392857142857)[R1,XVAR-Cons(CEM)], 6(7.362757142857143)[R2,XVAR-Cons(CEM)], 4(0.4184071428571428)[R3,Mirror-Echo], 2(0.2414285714285714)[R3,Swap], 0(0.20435714285714285)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-02.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=60), P2:3(gap=20), P3:9(gap=35); top cartesian candidates: 229, 239, 226, 236, 329.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '8'], 'pairs': {'remaining_count': 1}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 259→combined:685(B),evening:738(B); 447→combined:984(B),midday:740(B); 555→midday:851(B),evening:856(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:191, 27:132, 5:95, 32:89, 26:84.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=529 Evening=359; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 259 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 359 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 529 (canon 259): box `259` covers winner `529` (boxed hit).
  - Evening winner 359 (canon 359): box `359` covers winner `359` (boxed hit).
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
