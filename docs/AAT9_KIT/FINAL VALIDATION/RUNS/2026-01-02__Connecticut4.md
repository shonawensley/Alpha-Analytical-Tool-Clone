# Master Validation Run Report — Connecticut4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/Connecticut4/`
- Winners lens: `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-02/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-02/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-02/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-02/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-02/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-02/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/Connecticut4_vtrac12_winner_970_20260105_070856.html`
- `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/Connecticut4_vtrac8_winner_356_20260105_070858.html`

Winners JSON files:
- `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/Connecticut4_vtrac12_winner_970_20260105_070856.json`
- `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/Connecticut4_vtrac8_winner_356_20260105_070858.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 970 (canon 079): exact_boxed=True exact_straight=True | rank 1803/3775 (rank_frac 0.478); Evening 356 (canon 356): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 970 idx12 (rank 30/35, frac 0.857), 356 idx8 (rank 26/35, frac 0.743)
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

### 2.Stable — Connecticut4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-02)

## Midday winner 970 (canonical 079)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=6 | family_rows=228 | exact_boxed=6 | exact_straight=6 | vt_boxed=6
- Scores (patterns_scores.csv): rank 1803/3775 (rank_frac 0.4776158940397351) | score 12.5 (top 39.5, ratio 0.31645569620253167, delta 27.0) | section Combined, Set Set1, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why straight|cov2|vstr2|hidden3v|set_chain2
- Compound (patterns_compound.csv): rank 430/1123 (rank_frac 0.38290293855743546) | score 17.0 (top 68.5, ratio 0.24817518248175183, delta 51.5) | section Combined, col1_hits 1, hot2 0, set_chain 2, draw_chain 2 | why set_chain2|draw_chain2|col1x1|vstrx1
- Families (patterns_families.csv): count 47 | rank 108/1142 (rank_frac 0.09457092819614711) | score 21.5 (top 29.5, ratio 0.7288135593220338, delta 8.0) | section Midday, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=21

## Evening winner 356 (canonical 356)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=120 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 25 | rank 359/1142 (rank_frac 0.31436077057793343) | score 16.5 (top 29.5, ratio 0.559322033898305, delta 13.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=41
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 456 | section Midday | score 58.0 | col1_hits 4 | hot2 8
- rank    7 | canon 478 | section Combined | score 52.5 | col1_hits 4 | hot2 8
- rank    2 | canon 368 | section Midday | score 61.0 | col1_hits 5 | hot2 7
- rank   19 | canon 348 | section Midday | score 44.0 | col1_hits 5 | hot2 6
- rank   21 | canon 345 | section Midday | score 40.5 | col1_hits 5 | hot2 6
- rank   22 | canon 3458 | section Midday | score 38.0 | col1_hits 3 | hot2 6
- rank    9 | canon 3468 | section Midday | score 50.0 | col1_hits 5 | hot2 5
- rank   56 | canon 568 | section Midday | score 31.5 | col1_hits 2 | hot2 5
- rank   13 | canon 048 | section Combined | score 45.0 | col1_hits 3 | hot2 5
- rank   67 | canon 35778 | section Midday | score 30.0 | col1_hits 2 | hot2 4

## Top families (patterns_families.csv)
- rank 1121 | family 29 | score 5.0 | hot2 0 | section Midday
- rank  498 | family 20 | score 14.5 | hot2 1 | section Midday
- rank  312 | family 33 | score 17.0 | hot2 0 | section Midday
- rank  446 | family 14 | score 15.0 | hot2 0 | section Midday
- rank  498 | family 8 | score 14.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 970 (canon 079): exact_boxed=True exact_straight=True | rank 1803/3775 (rank_frac 0.478); Evening 356 (canon 356): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260102)

## Midday winner 970 (canonical 079)
- Stamp (winner_stamp.json): items_total=119 | exact_any=0 exact_final=0 | vtrac_any=114 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=84 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=29 family_vtrac_final=0
- Flags (winner_flags.csv): rows=119 | exact_any=0 vtrac_any=114 | drop_exact_any=0 drop_vtrac_any=84 | family_exact_any=0 family_vtrac_any=29 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=119 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.777143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 356 (canonical 356)
- Stamp (winner_stamp.json): items_total=38 | exact_any=0 exact_final=0 | vtrac_any=36 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=11 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=38 | exact_any=0 vtrac_any=36 | drop_exact_any=2 drop_vtrac_any=11 | family_exact_any=0 family_vtrac_any=4 | vt_boxed=14 vt_straight=0
- Hits (winner_hits.csv): rows=38 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=14 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 970 (canonical 079)
- Stamp (winner_stamp.json): items_total=269 | exact_any=0 exact_final=0 | vtrac_any=247 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=214 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=92 family_vtrac_final=0
- Flags (winner_flags.csv): rows=269 | exact_any=0 vtrac_any=247 | drop_exact_any=0 drop_vtrac_any=214 | family_exact_any=0 family_vtrac_any=92 | vt_boxed=44 vt_straight=0
- Hits (winner_hits.csv): rows=269 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=44 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 554 | score_v2 13.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 554 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 433 | score_v2 11.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 10.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 544 | score_v2 10.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 10.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 10.627143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 10.387143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 10.365714 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 544 | score_v2 10.277143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 554 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 433 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 544 | score_v2 10.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 10.387143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 554 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 10.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 443 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 559 | score_v2 9.697143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 924 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 970 (canon 079): items_total=119 exact_any=0 vtrac_any=114 | top winner_present=False best_rank=None/26; Evening 356 (canon 356): items_total=38 exact_any=0 vtrac_any=36 | top winner_present=False best_rank=None/32; Combined 970 (canon 079): items_total=269 exact_any=0 vtrac_any=247 | top winner_present=False best_rank=None/34
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 554, 433, 559, 544, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_071323)

## Top indices (from enhanced JSON)
- index 23 | score 46.8734 | features: presence=33.38589999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 19 | score 33.93855 | features: presence=19.44105, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 32 | score 29.454212500000004 | features: presence=21.996712500000005, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 33 | score 22.498692500000004 | features: presence=15.531192500000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 16 | score 19.142625000000006 | features: presence=11.427000000000001, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.23229166666666665
- index 18 | score 18.429955 | features: presence=11.972454999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 17 | score 15.755975000000001 | features: presence=8.288475000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 14.7673 | features: presence=6.119799999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 21 | score 13.164800000000001 | features: presence=4.7873, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 30 | score 13.081430000000005 | features: presence=5.833930000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
683, 836, 386, 164, 641, 183, 138, 813, 834, 438

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 970 | index 12 | file Connecticut4_vtrac12_winner_970_20260105_070856.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 356 | index 8 | file Connecticut4_vtrac8_winner_356_20260105_070858.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 970 | index 12 rank 30/35 (rank_frac 0.8571428571428571) | score 0.0 (top 46.8734, ratio 0.0, delta 46.8734) | winner_in_index_straights=False | top_index_straights: (none)
- winner 356 | index 8 rank 26/35 (rank_frac 0.7428571428571429) | score 0.0 (top 46.8734, ratio 0.0, delta 46.8734) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 970→idx12 rank 30/35 (frac 0.857); 356→idx8 rank 26/35 (frac 0.743).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 19, 32, 33, 16.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-02)

## Midday winner 970 (canonical 079)
- Top lanes (hot_zones_top_lanes.csv): present | rank 45/208 (rank_frac 0.21634615384615385) | score_mean 18.565 (top 21.242, ratio 0.8739760851143961, delta 2.6769999999999996)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 356 (canonical 356)
- Top lanes (hot_zones_top_lanes.csv): present | rank 138/208 (rank_frac 0.6634615384615384) | score_mean 16.868 (top 21.242, ratio 0.7940871857640522, delta 4.374000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 055 | vt_triad 11 | score_mean 21.242 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 177 | vt_triad 23 | score_mean 20.943 | tags funnel_precol1,hot12,hot16,hot20,hot4,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    3 | triad 467 | vt_triad 235 | score_mean 20.668 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 006 | vt_triad 12 | score_mean 20.465 | tags col1,funnel_precol1,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 116 | vt_triad 22 | score_mean 20.465 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 059 | vt_triad 115 | score_mean 20.408 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 126 | vt_triad 223 | score_mean 20.3 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 007 | vt_triad 13 | score_mean 20.277 | tags funnel_precol1,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 259 | vt_triad 135 | score_mean 20.153 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 279 | vt_triad 335 | score_mean 20.1 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 970 (canon 079): rank 45/208 (rank_frac 0.216) ratio_to_top=0.8739760851143961; Evening 356 (canon 356): rank 138/208 (rank_frac 0.663) ratio_to_top=0.7940871857640522
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

Aux draws snapshot dir: `sharepacks/2026-01-02/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=109, 228, 361, 932, 467
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=228, 932, 095, 211, 042
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=109, 361, 467, 055, 279

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=2 last_repeat_gap=33 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=36), P2:8 (gap=10), P3:0 (gap=33)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=885 sev=B
- 129: ds=867 sev=B
- 288: ds=855 sev=B
- 149: ds=837 sev=B
- 445: ds=769 sev=B
- 114: ds=739 sev=B
- 069: ds=703 sev=B
- 888: ds=701 sev=B
- 688: ds=697 sev=B
- 133: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=87 sev=blue
  - 99: ds=68 sev=purple
  - 00: ds=38 sev=purple
  - 33: ds=25 sev=purple
  - 88: ds=24 sev=-
  - 66: ds=23 sev=-
  - 77: ds=13 sev=-
  - 11: ds=7 sev=-
  - 55: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 69: ds=85 sev=red
  - 48: ds=74 sev=red
  - 78: ds=70 sev=red
  - 57: ds=69 sev=red
  - 49: ds=68 sev=red
  - 25: ds=37 sev=blue
  - 06: ds=35 sev=purple
  - 07: ds=35 sev=purple
  - 37: ds=30 sev=purple
  - 18: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:403, 32:170, 25:156, 29:129, 4:127, 15:115, 31:104, 34:99, 3:84, 35:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=403 fs=1 fl=2 hz=0.01098901098901099, 32:ds=170 fs=5 fl=2 hz=0.011267605633802818, 25:ds=156 fs=22 fl=2 hz=0.029055690072639227, 29:ds=129 fs=25 fl=1 hz=0.029988465974625143, 4:ds=127 fs=21 fl=2 hz=0.027677496991576414, 15:ds=115 fs=10 fl=4 hz=0.01583710407239819, 31:ds=104 fs=32 fl=0 hz=0.03665521191294387, 34:ds=99 fs=15 fl=2 hz=0.01951779563719862, 3:ds=84 fs=27 fl=0 hz=0.030337078651685393, 35:ds=68 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=78 flags=purple
- S24: ds=70 flags=blue+purple
- S22: ds=68 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=73 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=26), P2:0 (gap=26), P3:4 (gap=30)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=879 sev=B
- 478: ds=860 sev=B
- 459: ds=855 sev=B
- 159: ds=811 sev=B
- 099: ds=792 sev=B
- 127: ds=783 sev=B
- 559: ds=725 sev=B
- 004: ds=684 sev=B
- 155: ds=680 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=91 sev=blue
  - 88: ds=51 sev=purple
  - 44: ds=43 sev=purple
  - 55: ds=28 sev=purple
  - 00: ds=24 sev=-
  - 33: ds=12 sev=-
  - 66: ds=11 sev=-
  - 77: ds=6 sev=-
  - 11: ds=3 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 78: ds=69 sev=red
  - 13: ds=56 sev=red
  - 49: ds=43 sev=blue
  - 19: ds=42 sev=blue
  - 69: ds=42 sev=blue
  - 48: ds=39 sev=blue
  - 57: ds=34 sev=purple
  - 79: ds=34 sev=purple
  - 37: ds=23 sev=-
  - 01: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:201, 25:102, 31:91, 32:89, 18:86, 3:74, 29:64, 4:63, 15:57, 34:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=201 fs=3 fl=0 hz=0.008565310492505354, 25:ds=102 fs=21 fl=1 hz=0.025974025974025976, 31:ds=91 fs=20 fl=2 hz=0.024608501118568233, 32:ds=89 fs=3 fl=4 hz=0.009510869565217392, 18:ds=86 fs=23 fl=1 hz=0.026519337016574582, 3:ds=74 fs=22 fl=2 hz=0.02631578947368421, 29:ds=64 fs=18 fl=2 hz=0.023446658851113716, 4:ds=63 fs=26 fl=0 hz=0.02931228861330327, 15:ds=57 fs=24 fl=1 hz=0.02662406815761448, 34:ds=49 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=85 flags=blue+purple
- S24: ds=82 flags=blue+purple
- S8: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=10 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:9 (gap=15), P3:0 (gap=19)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=906 sev=B
- 668: ds=903 sev=B
- 399: ds=902 sev=B
- 044: ds=898 sev=B
- 133: ds=895 sev=B
- 145: ds=867 sev=B
- 677: ds=774 sev=B
- 333: ds=769 sev=B
- 112: ds=721 sev=B
- 344: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=113 sev=red
  - 22: ds=70 sev=purple
  - 99: ds=34 sev=purple
  - 77: ds=28 sev=purple
  - 66: ds=23 sev=-
  - 11: ds=22 sev=-
  - 33: ds=20 sev=-
  - 00: ds=19 sev=-
  - 88: ds=12 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 57: ds=49 sev=blue
  - 69: ds=47 sev=blue
  - 23: ds=44 sev=blue
  - 25: ds=42 sev=blue
  - 06: ds=41 sev=blue
  - 07: ds=41 sev=blue
  - 48: ds=37 sev=blue
  - 78: ds=35 sev=purple
  - 49: ds=34 sev=purple
  - 15: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:312, 26:140, 4:123, 34:92, 32:85, 25:78, 29:66, 15:65, 2:55, 31:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=312 fs=2 fl=1 hz=0.005961251862891207, 26:ds=140 fs=3 fl=1 hz=0.008680555555555556, 4:ds=123 fs=18 fl=1 hz=0.02243211334120425, 34:ds=92 fs=14 fl=3 hz=0.019144144144144143, 32:ds=85 fs=2 fl=0 hz=0.008450704225352114, 25:ds=78 fs=21 fl=0 hz=0.023836549375709424, 29:ds=66 fs=27 fl=0 hz=0.030100334448160536, 15:ds=65 fs=15 fl=1 hz=0.019698725376593278, 2:ds=55 fs=23 fl=2 hz=0.028344671201814057, 31:ds=52 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=92 flags=blue+purple
- S8: ds=69 flags=red+purple
- S20: ds=52 flags=purple
- S3: ds=39 flags=blue+purple
- S24: ds=35 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 128: score=1 tags=FLT
  - 138: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:693(B); evening:895(B)
- 445 -> combined:769(B); evening:690(B)
- 459 -> combined:678(B); midday:855(B)
- 888 -> combined:701(B); evening:698(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:35(purple); evening:41(blue)
- 07 -> combined:35(purple); evening:41(blue)
- 25 -> combined:37(blue); evening:42(blue)
- 44 -> combined:87(blue); evening:113(red); midday:43(purple)
- 48 -> combined:74(red); evening:37(blue); midday:39(blue)
- 49 -> combined:68(red); evening:34(purple); midday:43(blue)
- 57 -> combined:69(red); evening:49(blue); midday:34(purple)
- 69 -> combined:85(red); evening:47(blue); midday:42(blue)
- 78 -> combined:70(red); evening:35(purple); midday:69(red)
- 99 -> combined:68(purple); evening:34(purple); midday:91(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.313714285714287)[R1,XVAR-Cons(CEM)], 5(2.6307714285714283)[R3,XVAR-Cons(CM)], 6(2.535792857142857)[R2,XVAR-Cons(CE)], 9(1.0044)[R2,Double-Pressure], 3(0.23122857142857145)[R3,Swap]
- P2: 8(3.2023857142857146)[R1,XVAR-Cons(CM)], 4(2.6762357142857143)[R2,XVAR-Cons(CE)], 0(1.5251428571428571)[R1,Mirror-Echo], 9(1.22725)[R1,Mirror-Echo], 1(0.9625999999999999)[R2,Double-Pressure]
- P3: 0(7.8388285714285715)[R1,XVAR-Cons(CEM)], 4(4.153)[R2,XVAR-Cons(CM)], 2(0.9417)[R2,Double-Pressure], 9(0.6683714285714285)[R3,Mirror-Echo], 6(0.29628571428571426)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=36), P2:8(gap=10), P3:0(gap=33); top cartesian candidates: 740, 780, 784, 700, 790.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 015, 025, 035, 045, 056.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:693(B),evening:895(B); 445→combined:769(B),evening:690(B); 459→combined:678(B),midday:855(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:403, 32:170, 25:156, 29:129, 4:127.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=970 Evening=356; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 079 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 356 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 970 (canon 079): box `079` covers winner `970` (boxed hit).
  - Evening winner 356 (canon 356): box `356` covers winner `356` (boxed hit).
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
