# Master Validation Run Report — PuertoRico4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-02/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-02/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-02/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-02/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-02/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-02/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac22_winner_917_20260105_070925.html`
- `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_144_20260105_070924.html`

Winners JSON files:
- `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac22_winner_917_20260105_070925.json`
- `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_144_20260105_070924.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 144 (canon 144): exact_boxed=True exact_straight=True | rank 115/4050 (rank_frac 0.028); Evening 917 (canon 179): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 917 idx22 (rank 4/35, frac 0.114), 144 idx25 (rank 5/35, frac 0.143)
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

### 2.Stable — PuertoRico4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-02)

## Midday winner 144 (canonical 144)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=24 | family_rows=211 | exact_boxed=24 | exact_straight=24 | vt_boxed=24
- Scores (patterns_scores.csv): rank 115/4050 (rank_frac 0.028395061728395062) | score 24.0 (top 37.0, ratio 0.6486486486486487, delta 13.0) | section Midday, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 2.0 | why straight|cov2|hp_repeat5|vstr2|hot2|double_mirror|vtrac_straight|draw_chain6
- Compound (patterns_compound.csv): rank 5/1043 (rank_frac 0.004793863854266539) | score 59.5 (top 84.5, ratio 0.7041420118343196, delta 25.0) | section Midday, col1_hits 0, hot2 6, set_chain 1, draw_chain 6 | why draw_chain6|hot1x5|hot2x6|vstrx11|dblmirrorx20
- Families (patterns_families.csv): count 55 | rank 149/1268 (rank_frac 0.11750788643533124) | score 22.5 (top 33.0, ratio 0.6818181818181818, delta 10.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=7

## Evening winner 917 (canonical 179)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=68 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 38 | rank 127/1268 (rank_frac 0.10015772870662461) | score 23.0 (top 33.0, ratio 0.696969696969697, delta 10.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=23
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    4 | canon 134 | section Midday | score 60.5 | col1_hits 5 | hot2 8
- rank    2 | canon 226 | section Combined | score 76.0 | col1_hits 6 | hot2 8
- rank    3 | canon 445 | section Midday | score 70.5 | col1_hits 2 | hot2 6
- rank   18 | canon 1344 | section Midday | score 45.0 | col1_hits 0 | hot2 6
- rank    1 | canon 344 | section Midday | score 84.5 | col1_hits 2 | hot2 6
- rank    5 | canon 144 | section Midday | score 59.5 | col1_hits 0 | hot2 6
- rank   30 | canon 236 | section Evening | score 38.5 | col1_hits 0 | hot2 5
- rank   76 | canon 135 | section Midday | score 30.0 | col1_hits 0 | hot2 5
- rank   16 | canon 268 | section Evening | score 46.5 | col1_hits 5 | hot2 5
- rank   33 | canon 11344 | section Midday | score 38.0 | col1_hits 0 | hot2 4

## Top families (patterns_families.csv)
- rank 1170 | family 11 | score 7.0 | hot2 0 | section Midday
- rank  569 | family 14 | score 15.0 | hot2 0 | section Midday
- rank  512 | family 8 | score 16.0 | hot2 0 | section Midday
- rank  638 | family 25 | score 14.0 | hot2 0 | section Midday
- rank  712 | family 19 | score 13.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 144 (canon 144): exact_boxed=True exact_straight=True | rank 115/4050 (rank_frac 0.028); Evening 917 (canon 179): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260102)

## Midday winner 144 (canonical 144)
- Stamp (winner_stamp.json): items_total=108 | exact_any=108 exact_final=0 | vtrac_any=108 vtrac_final=0 | drop_exact_any=24 drop_exact_final=0 | drop_vtrac_any=26 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=108 | exact_any=108 vtrac_any=108 | drop_exact_any=24 drop_vtrac_any=26 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=108 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.720476 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 917 (canonical 179)
- Stamp (winner_stamp.json): items_total=122 | exact_any=0 exact_final=0 | vtrac_any=122 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=78 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=36 family_vtrac_final=0
- Flags (winner_flags.csv): rows=122 | exact_any=0 vtrac_any=122 | drop_exact_any=0 drop_vtrac_any=78 | family_exact_any=0 family_vtrac_any=36 | vt_boxed=14 vt_straight=0
- Hits (winner_hits.csv): rows=122 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=14 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 144 (canonical 144)
- Stamp (winner_stamp.json): items_total=200 | exact_any=132 exact_final=0 | vtrac_any=200 vtrac_final=0 | drop_exact_any=24 drop_exact_final=0 | drop_vtrac_any=26 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=200 | exact_any=132 vtrac_any=200 | drop_exact_any=24 drop_vtrac_any=26 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=10 vt_straight=0
- Hits (winner_hits.csv): rows=200 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=10 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 220 | score_v2 11.577143 | match_types 
- area_rank 2 | variant Evening | section Evening | set Set1 draw Draw6 col 1 | pattern 522 | score_v2 10.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 522 | score_v2 9.877143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 9.808571 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 522 | score_v2 9.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 9.720476 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 592 | score_v2 9.627143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 592 | score_v2 9.627143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 592 | score_v2 9.627143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 592 | score_v2 9.627143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 220 | score_v2 11.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 522 | score_v2 10.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 522 | score_v2 9.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 9.808571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 9.720476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 592 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 559 | score_v2 9.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 592 | score_v2 9.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 524 | score_v2 9.397143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 524 | score_v2 9.397143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 144 (canon 144): items_total=108 exact_any=108 vtrac_any=108 | top winner_present=False best_rank=None/18; Evening 917 (canon 179): items_total=122 exact_any=0 vtrac_any=122 | top winner_present=False best_rank=None/22; Combined 144 (canon 144): items_total=200 exact_any=132 vtrac_any=200 | top winner_present=False best_rank=None/32
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 220, 522, 522, 559, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260105_071332)

## Top indices (from enhanced JSON)
- index 24 | score 55.937459999999994 | features: presence=36.28995999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 34 | score 50.83574999999998 | features: presence=34.71824999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 47.03866250000001 | features: presence=28.56116250000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 32.0519875 | features: presence=19.684487500000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 29.049999999999994 | features: presence=18.46249999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 26.85575 | features: presence=14.858249999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 31 | score 25.0372 | features: presence=15.359699999999997, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 3 | score 19.72141666666667 | features: presence=13.854750000000003, set_echo=0.3, first_hit=0.4, column_span=0.16666666666666666
- index 17 | score 19.0872125 | features: presence=13.569712499999998, first_hit=0.33333333333333337, column_span=0.25416666666666665, persistence=0.4
- index 28 | score 15.978700000000003 | features: presence=9.381200000000003, set_echo=0.6, first_hit=0.2, column_span=0.0875

## Top straights (from enhanced JSON)
136, 134, 634, 413, 341, 624, 364, 436, 963, 936

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 917 | index 22 | file PuertoRico4_vtrac22_winner_917_20260105_070925.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 144 | index 25 | file PuertoRico4_vtrac25_winner_144_20260105_070924.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 917 | index 22 rank 4/35 (rank_frac 0.11428571428571428) | score 32.0519875 (top 55.937459999999994, ratio 0.5729968343217587, delta 23.88547249999999) | winner_in_index_straights=False | top_index_straights: 624 (15.886), 246 (9.914), 264 (9.588)
- winner 144 | index 25 rank 5/35 (rank_frac 0.14285714285714285) | score 29.049999999999994 (top 55.937459999999994, ratio 0.5193299803030026, delta 26.88746) | winner_in_index_straights=False | top_index_straights: 964 (8.515)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 917→idx22 rank 4/35 (frac 0.114); 144→idx25 rank 5/35 (frac 0.143).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 24, 34, 18, 22, 25.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-02)

## Midday winner 144 (canonical 144)
- Top lanes (hot_zones_top_lanes.csv): present | rank 9/210 (rank_frac 0.04285714285714286) | score_mean 19.947 (top 22.565, ratio 0.8839796144471526, delta 2.618000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 917 (canonical 179)
- Top lanes (hot_zones_top_lanes.csv): present | rank 89/210 (rank_frac 0.4238095238095238) | score_mean 17.356 (top 22.565, ratio 0.7691557722136052, delta 5.209)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 379 | vt_triad 345 | score_mean 22.565 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    2 | triad 007 | vt_triad 13 | score_mean 21.208 | tags hot16,hot20,hot8,literal_draw,set1_bonus,straight_lane,vertical1,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 21.19 | tags col1,hot16,hot20,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 344 | vt_triad 45 | score_mean 20.938 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 145 | vt_triad 125 | score_mean 20.747 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 445 | vt_triad 15 | score_mean 20.419 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 346 | vt_triad 245 | score_mean 20.274 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 049 | vt_triad 155 | score_mean 20.025 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    9 | triad 144 | vt_triad 25 | score_mean 19.947 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 447 | vt_triad 35 | score_mean 19.919 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 144 (canon 144): rank 9/210 (rank_frac 0.043) ratio_to_top=0.8839796144471526; Evening 917 (canon 179): rank 89/210 (rank_frac 0.424) ratio_to_top=0.7691557722136052
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

Aux draws snapshot dir: `sharepacks/2026-01-02/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=913, 451, 643, 098, 785
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=451, 098, 875, 793, 962
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=913, 643, 785, 490, 902

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=5 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=58), P2:3 (gap=18), P3:9 (gap=33)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=58)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=991 sev=B
- 447: ds=982 sev=B
- 000: ds=730 sev=B
- 039: ds=718 sev=B
- 466: ds=714 sev=B
- 677: ds=692 sev=B
- 259: ds=683 sev=B
- 577: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=62 sev=purple
  - 77: ds=61 sev=purple
  - 99: ds=52 sev=purple
  - 44: ds=47 sev=purple
  - 11: ds=46 sev=purple
  - 55: ds=27 sev=purple
  - 33: ds=22 sev=-
  - 66: ds=21 sev=-
  - 88: ds=14 sev=-
  - 00: ds=12 sev=-
- non_repeating:
  - 47: ds=170 sev=red
  - 24: ds=84 sev=red
  - 25: ds=59 sev=red
  - 48: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 56: ds=41 sev=blue
  - 59: ds=41 sev=blue
  - 05: ds=39 sev=blue
  - 28: ds=34 sev=purple
  - 35: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:189, 27:130, 5:93, 32:87, 26:82, 31:79, 28:61, 18:53, 34:52, 33:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=189 fs=18 fl=1 hz=0.025477707006369428, 27:ds=130 fs=24 fl=1 hz=0.029868578255675033, 5:ds=93 fs=27 fl=1 hz=0.0343980343980344, 32:ds=87 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=82 fs=4 fl=2 hz=0.01020408163265306, 31:ds=79 fs=14 fl=3 hz=0.018619934282584887, 28:ds=61 fs=26 fl=0 hz=0.0278372591006424, 18:ds=53 fs=20 fl=0 hz=0.022727272727272728, 34:ds=52 fs=26 fl=0 hz=0.02857142857142857, 33:ds=49 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=79 flags=purple
- S23: ds=61 flags=blue+purple
- S26: ds=52 flags=blue+purple
- S8: ds=46 flags=purple
- S6: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=59 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=29), P2:1 (gap=25), P3:9 (gap=16)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=959 sev=B
- 299: ds=950 sev=B
- 003: ds=941 sev=B
- 077: ds=927 sev=B
- 333: ds=876 sev=B
- 555: ds=850 sev=B
- 088: ds=821 sev=B
- 888: ds=815 sev=B
- 666: ds=800 sev=B
- 447: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=106 sev=blue
  - 22: ds=79 sev=blue
  - 11: ds=55 sev=purple
  - 99: ds=39 sev=purple
  - 77: ds=30 sev=purple
  - 33: ds=24 sev=-
  - 44: ds=23 sev=-
  - 88: ds=21 sev=-
  - 55: ds=13 sev=-
  - 66: ds=10 sev=-
- non_repeating:
  - 47: ds=112 sev=red
  - 24: ds=58 sev=red
  - 38: ds=43 sev=blue
  - 03: ds=42 sev=blue
  - 04: ds=42 sev=blue
  - 35: ds=40 sev=blue
  - 48: ds=32 sev=purple
  - 19: ds=31 sev=purple
  - 25: ds=29 sev=purple
  - 18: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:138, 29:96, 10:94, 27:93, 26:90, 3:83, 16:55, 23:50, 15:48, 5:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=138 fs=18 fl=0 hz=0.02211874272409779, 29:ds=96 fs=16 fl=2 hz=0.020809248554913295, 10:ds=94 fs=20 fl=3 hz=0.026376146788990827, 27:ds=93 fs=19 fl=1 hz=0.024721878862793572, 26:ds=90 fs=7 fl=2 hz=0.011682242990654207, 3:ds=83 fs=31 fl=0 hz=0.03506787330316742, 16:ds=55 fs=4 fl=2 hz=0.009695290858725763, 23:ds=50 fs=31 fl=1 hz=0.034782608695652174, 15:ds=48 fs=25 fl=0 hz=0.026939655172413795, 5:ds=46 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=42 flags=purple
- S25: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- _no candidates_

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=2 max=2 last_repeat_gap=1 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=29), P2:5 (gap=45), P3:6 (gap=21)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=991 sev=B
- 579: ds=972 sev=B
- 114: ds=916 sev=B
- 555: ds=855 sev=B
- 888: ds=763 sev=B
- 067: ds=752 sev=B
- 446: ds=739 sev=B
- 259: ds=737 sev=B
- 224: ds=723 sev=B
- 449: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=143 sev=red
  - 44: ds=139 sev=red
  - 77: ds=41 sev=purple
  - 66: ds=32 sev=purple
  - 22: ds=31 sev=purple
  - 99: ds=26 sev=purple
  - 11: ds=23 sev=-
  - 33: ds=11 sev=-
  - 88: ds=7 sev=-
  - 00: ds=6 sev=-
- non_repeating:
  - 25: ds=99 sev=red
  - 47: ds=85 sev=red
  - 45: ds=69 sev=red
  - 26: ds=62 sev=red
  - 59: ds=55 sev=blue
  - 79: ds=46 sev=blue
  - 24: ds=42 sev=blue
  - 05: ds=38 sev=blue
  - 56: ds=38 sev=blue
  - 23: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:448, 32:163, 4:117, 22:116, 10:104, 31:92, 5:82, 33:68, 27:65, 1:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=448 fs=5 fl=1 hz=0.01662049861495845, 32:ds=163 fs=6 fl=1 hz=0.009987515605493134, 4:ds=117 fs=23 fl=2 hz=0.03071253071253071, 22:ds=116 fs=34 fl=0 hz=0.04, 10:ds=104 fs=16 fl=2 hz=0.0234375, 31:ds=92 fs=18 fl=3 hz=0.02394526795895097, 5:ds=82 fs=18 fl=2 hz=0.022446689113355782, 33:ds=68 fs=12 fl=1 hz=0.017361111111111112, 27:ds=65 fs=18 fl=1 hz=0.02358490566037736, 1:ds=57 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=75 flags=purple
- S24: ds=66 flags=purple
- S18: ds=51 flags=red+purple
- S23: ds=46 flags=blue+purple
- S16: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS
  - 129: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS
  - 237: score=2 tags=RS
  - 246: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:683(B); evening:737(B)
- 447 -> combined:982(B); midday:739(B)
- 555 -> evening:855(B); midday:850(B)
- 888 -> evening:763(B); midday:815(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:39(blue); evening:38(blue)
- 11 -> combined:46(purple); midday:55(purple)
- 22 -> combined:62(purple); evening:31(purple); midday:79(blue)
- 23 -> combined:45(blue); evening:29(purple)
- 24 -> combined:84(red); evening:42(blue); midday:58(red)
- 25 -> combined:59(red); evening:99(red); midday:29(purple)
- 44 -> combined:47(purple); evening:139(red)
- 47 -> combined:170(red); evening:85(red); midday:112(red)
- 48 -> combined:48(blue); midday:32(purple)
- 55 -> combined:27(purple); evening:143(red)
- 56 -> combined:41(blue); evening:38(blue)
- 59 -> combined:41(blue); evening:55(blue)
- 77 -> combined:61(purple); evening:41(purple); midday:30(purple)
- 99 -> combined:52(purple); evening:26(purple); midday:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.831714285714286)[R1,XVAR-Cons(CEM)], 3(5.593571428571428)[R3,XVAR-Cons(CEM)], 1(3.3666)[R2,XVAR-Cons(CE)], 5(0.3687142857142857)[R3,Swap]
- P2: 2(3.7194)[R2,XVAR-Cons(CE)], 3(2.813507142857143)[R1,XVAR-Cons(CM)], 1(1.4464285714285714)[R1,Double-Pressure], 4(1.1806999999999999)[R2,Double-Pressure], 5(1.145)[R1,Swap]
- P3: 9(8.184171428571428)[R1,Mirror-Echo], 4(7.119942857142856)[R2,Mirror-Echo], 6(5.828357142857143)[R3,XVAR-Cons(CEM)]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=58), P2:3(gap=18), P3:9(gap=33); top cartesian candidates: 229, 224, 239, 234, 226.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}; top candidates: 012, 023, 024, 025, 026.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 259→combined:683(B),evening:737(B); 447→combined:982(B),midday:739(B); 555→midday:850(B),evening:855(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:189, 27:130, 5:93, 32:87, 26:82.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=144 Evening=917; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 144 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 179 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 144 (canon 144): box `144` covers winner `144` (boxed hit).
  - Evening winner 917 (canon 179): box `179` covers winner `917` (boxed hit).
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
