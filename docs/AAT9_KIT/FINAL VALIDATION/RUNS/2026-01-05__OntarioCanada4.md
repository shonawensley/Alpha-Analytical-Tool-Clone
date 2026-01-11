# Master Validation Run Report — OntarioCanada4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-05/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-05/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-05/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-05/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-05/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-05/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac28_winner_797_20260110_035738.html`
- `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_555_20260110_035738.html`

Winners JSON files:
- `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac28_winner_797_20260110_035738.json`
- `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_555_20260110_035738.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 555 (canon 555): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 797 (canon 779): exact_boxed=True exact_straight=True | rank 2952/4623 (rank_frac 0.639)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 797 idx28 (rank 2/35, frac 0.057)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
- Q7: Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy.
- Q8: Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries).
- Q9: Aux cues: BA score=3 (if None, BA not available); see Part 3 positional/doubles/pairs notes.
- Q10: 4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank).
- Q11: Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table.
- Q12: Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days.
- Q13: Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance.
- Q14: Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — OntarioCanada4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-05)

## Midday winner 555 (canonical 555)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=122 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 72 | rank 2/1335 (rank_frac 0.00149812734082397) | score 32.5 (top 34.5, ratio 0.9420289855072463, delta 2.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=0
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 797 (canonical 779)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=None | exact_boxed=2 | exact_straight=2 | vt_boxed=2
- Scores (patterns_scores.csv): rank 2952/4623 (rank_frac 0.6385463984425698) | score 11.0 (top 35.0, ratio 0.3142857142857143, delta 24.0) | section Combined, Set Set1, Draw Draw2, Col 3, hot 1, vt_straight 2.0 | why straight|cov1|hot1|double_mirror|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 435/1753 (rank_frac 0.24814603536794066) | score 17.0 (top 87.5, ratio 0.19428571428571428, delta 70.5) | section Combined, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|hot1x2|vstrx2|dblmirrorx2
- Families (patterns_families.csv): not present
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=15

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 477 | section Combined | score 87.5 | col1_hits 8 | hot2 11
- rank    3 | canon 177 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    4 | canon 1477 | section Combined | score 76.5 | col1_hits 7 | hot2 11
- rank    2 | canon 477 | section Midday | score 85.0 | col1_hits 7 | hot2 11
- rank   12 | canon 147 | section Combined | score 49.5 | col1_hits 4 | hot2 9
- rank    7 | canon 177 | section Midday | score 58.0 | col1_hits 5 | hot2 6
- rank    8 | canon 1477 | section Midday | score 52.0 | col1_hits 5 | hot2 6
- rank   18 | canon 234 | section Midday | score 45.5 | col1_hits 4 | hot2 6
- rank    5 | canon 677 | section Midday | score 63.0 | col1_hits 4 | hot2 5
- rank   17 | canon 246 | section Midday | score 46.0 | col1_hits 3 | hot2 5

## Top families (patterns_families.csv)
- rank 1306 | family 11 | score 5.0 | hot2 0 | section Midday
- rank  552 | family 3 | score 16.0 | hot2 0 | section Midday
- rank 1198 | family 13 | score 8.0 | hot2 0 | section Midday
- rank 1232 | family 17 | score 7.5 | hot2 0 | section Midday
- rank 1232 | family 8 | score 7.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 555 (canon 555): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 797 (canon 779): exact_boxed=True exact_straight=True | rank 2952/4623 (rank_frac 0.639)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260110)

## Midday winner 555 (canonical 555)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.537143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 797 (canonical 779)
- Stamp (winner_stamp.json): items_total=24 | exact_any=6 exact_final=0 | vtrac_any=24 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=9 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=8 family_vtrac_final=0
- Flags (winner_flags.csv): rows=24 | exact_any=6 vtrac_any=24 | drop_exact_any=3 drop_vtrac_any=9 | family_exact_any=0 family_vtrac_any=8 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=24 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.497143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 555 (canonical 555)
- Stamp (winner_stamp.json): items_total=14 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=14 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=14 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=14 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=14 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=16.78131 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 477 | score_v2 16.78131 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 417 | score_v2 13.214643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 477 | score_v2 11.98131 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 594 | score_v2 11.497143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 594 | score_v2 11.497143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 594 | score_v2 11.497143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 594 | score_v2 11.497143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 594 | score_v2 11.247143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 594 | score_v2 11.247143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 594 | score_v2 11.247143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 594 | score_v2 11.247143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 594 | score_v2 11.247143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 477 | score_v2 16.78131 | tags exact,vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 417 | score_v2 13.214643 | tags exact,vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 477 | score_v2 11.98131 | tags exact,vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 594 | score_v2 11.497143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 401 | score_v2 11.047143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 554 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 10.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 552 | score_v2 10.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 244 | score_v2 10.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 407 | score_v2 10.33131 | tags exact,vtrac,family_exact,family_vtrac
- rank 11 | variant Midday | best_pattern 552 | score_v2 10.097143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Evening | best_pattern 594 | score_v2 10.057143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 555 (canon 555): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/20; Evening 797 (canon 779): items_total=24 exact_any=6 vtrac_any=24 | top winner_present=False best_rank=None/26; Combined 555 (canon 555): items_total=14 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/34
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 477, 417, 477, 594, 401.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260110_035937)

## Top indices (from enhanced JSON)
- index 20 | score 75.45515999999998 | features: presence=51.03765999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 68.65093999999998 | features: presence=48.99343999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 37.529349999999994 | features: presence=24.93185, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 36.24399999999999 | features: presence=23.636499999999995, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 18 | score 28.7962 | features: presence=17.738699999999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 21 | score 27.269000000000002 | features: presence=15.481499999999997, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 19 | score 25.143424999999997 | features: presence=13.525924999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 26 | score 19.6915 | features: presence=9.814, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 33 | score 15.640600000000003 | features: presence=8.653100000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 17 | score 14.745975000000003 | features: presence=7.3784750000000034, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
267, 762, 724, 247, 672, 172, 417, 714, 792, 867

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 797 | index 28 | file OntarioCanada4_vtrac28_winner_797_20260110_035738.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 555 | index None | file OntarioCanada4_vtracNone_winner_555_20260110_035738.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 797 | index 28 rank 2/35 (rank_frac 0.05714285714285714) | score 68.65093999999998 (top 75.45515999999998, ratio 0.9098243248042943, delta 6.804220000000001) | winner_in_index_straights=False | top_index_straights: 724 (16.325), 247 (15.652), 792 (10.39)
- winner 555 | index None: not found in indices_ranked
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 797→idx28 rank 2/35 (frac 0.057).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 20, 28, 22, 23, 18.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-05)

## Midday winner 555 (canonical 555)
- Top lanes (hot_zones_top_lanes.csv): not present
- Per-lane (hot_zones_per_lane.csv): not present
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Coverage gaps: missing_from_top_lanes, missing_from_per_lane
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Evening winner 797 (canonical 779)
- Top lanes (hot_zones_top_lanes.csv): present | rank 55/210 (rank_frac 0.2619047619047619) | score_mean 18.136 (top 22.218, ratio 0.8162750922675308, delta 4.082000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 22.218 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 227 | vt_triad 33 | score_mean 22.041 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 238 | vt_triad 344 | score_mean 21.296 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 006 | vt_triad 12 | score_mean 20.894 | tags hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 279 | vt_triad 335 | score_mean 20.576 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 477 | vt_triad 35 | score_mean 20.431 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 247 | vt_triad 335 | score_mean 20.361 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 267 | vt_triad 233 | score_mean 20.309 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 188 | vt_triad 24 | score_mean 20.034 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 455 | vt_triad 15 | score_mean 19.985 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 555 (canon 555): rank N/A (rank_frac N/A) ratio_to_top=None; Evening 797 (canon 779): rank 55/210 (rank_frac 0.262) ratio_to_top=0.8162750922675308
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

Aux draws snapshot dir: `sharepacks/2026-01-05/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-05/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=382, 958, 032, 968, 816
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-05/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=958, 968, 053, 528, 918
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-05/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=382, 032, 816, 546, 932

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=56 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=30), P2:9 (gap=14), P3:4 (gap=29)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=42.53915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 774: score=40.431335714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 171: score=38.54714714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 164: score=38.258871428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 194: score=38.16144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=37.96344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 124: score=37.951342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.53973571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=36.15105 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=34.26686142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=927 sev=B
- 555: ds=892 sev=B
- 039: ds=783 sev=B
- 333: ds=754 sev=B
- 188: ds=727 sev=B
- 266: ds=713 sev=B
- 477: ds=711 sev=B
- 126: ds=703 sev=B
- 669: ds=698 sev=B
- 007: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=129 sev=red
  - 55: ds=85 sev=blue
  - 11: ds=44 sev=purple
  - 88: ds=38 sev=purple
  - 44: ds=29 sev=purple
  - 77: ds=20 sev=-
  - 99: ds=17 sev=-
  - 66: ds=16 sev=-
  - 33: ds=15 sev=-
  - 00: ds=13 sev=-
- non_repeating:
  - 01: ds=64 sev=red
  - 15: ds=61 sev=red
  - 17: ds=55 sev=blue
  - 12: ds=41 sev=blue
  - 24: ds=39 sev=blue
  - 26: ds=39 sev=blue
  - 67: ds=36 sev=purple
  - 36: ds=33 sev=purple
  - 48: ds=32 sev=purple
  - 08: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:339, 16:293, 17:165, 20:143, 33:89, 12:88, 26:83, 34:70, 8:66, 7:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=339 fs=1 fl=0 hz=0.005698005698005698, 16:ds=293 fs=2 fl=0 hz=0.006329113924050633, 17:ds=165 fs=19 fl=1 hz=0.024242424242424242, 20:ds=143 fs=13 fl=2 hz=0.01847290640394089, 33:ds=89 fs=24 fl=1 hz=0.027472527472527472, 12:ds=88 fs=44 fl=0 hz=0.04932735426008968, 26:ds=83 fs=2 fl=1 hz=0.006075334143377886, 34:ds=70 fs=14 fl=2 hz=0.019698725376593278, 8:ds=66 fs=39 fl=2 hz=0.044956140350877194, 7:ds=50 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=81 flags=purple
- S4: ds=75 flags=purple
- S3: ds=64 flags=blue+purple
- S16: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 469: score=4 tags=FLT,MIR,RS
  - 037: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 136: score=3 tags=MIR,RS
  - 145: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 027: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=20 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=29), P2:7 (gap=26), P3:0 (gap=18)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=42.53915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 774: score=40.431335714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 171: score=38.54714714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 164: score=38.258871428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 194: score=38.16144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=37.96344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 124: score=37.951342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.53973571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=36.15105 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=34.26686142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=998 sev=B
- 333: ds=981 sev=B
- 255: ds=948 sev=B
- 355: ds=913 sev=B
- 466: ds=834 sev=B
- 446: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=64 sev=purple
  - 55: ds=42 sev=purple
  - 11: ds=32 sev=purple
  - 77: ds=25 sev=purple
  - 88: ds=21 sev=-
  - 66: ds=16 sev=-
  - 44: ds=14 sev=-
  - 99: ds=8 sev=-
  - 33: ds=7 sev=-
  - 00: ds=6 sev=-
- non_repeating:
  - 34: ds=73 sev=red
  - 07: ds=70 sev=red
  - 16: ds=56 sev=red
  - 39: ds=44 sev=blue
  - 37: ds=39 sev=blue
  - 67: ds=39 sev=blue
  - 48: ds=36 sev=purple
  - 01: ds=32 sev=purple
  - 15: ds=30 sev=purple
  - 45: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:169, 34:164, 16:146, 27:101, 12:98, 17:82, 20:71, 19:56, 33:44, 26:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=169 fs=4 fl=3 hz=0.010432190760059612, 34:ds=164 fs=8 fl=4 hz=0.014423076923076924, 16:ds=146 fs=3 fl=0 hz=0.007462686567164179, 27:ds=101 fs=15 fl=2 hz=0.0189520624303233, 12:ds=98 fs=45 fl=0 hz=0.05079006772009029, 17:ds=82 fs=29 fl=2 hz=0.033879781420765025, 20:ds=71 fs=24 fl=3 hz=0.029315960912052113, 19:ds=56 fs=20 fl=2 hz=0.023732470334412083, 33:ds=44 fs=18 fl=2 hz=0.021119324181626188, 26:ds=41 fs=0 fl=3 hz=0.005376344086021506

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=76 flags=purple
- S1: ds=65 flags=blue+purple
- S5: ds=63 flags=purple
- S9: ds=53 flags=purple
- S21: ds=40 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=57 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=16), P2:6 (gap=18), P3:9 (gap=42)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=42.53915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 774: score=40.431335714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 171: score=38.54714714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 164: score=38.258871428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 194: score=38.16144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=37.96344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 124: score=37.951342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.53973571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=36.15105 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=34.26686142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=905 sev=B
- 113: ds=856 sev=B
- 378: ds=849 sev=B
- 566: ds=838 sev=B
- 199: ds=830 sev=B
- 899: ds=808 sev=B
- 126: ds=804 sev=B
- 559: ds=799 sev=B
- 477: ds=788 sev=B
- 558: ds=754 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=234 sev=red
  - 22: ds=65 sev=purple
  - 00: ds=52 sev=purple
  - 44: ds=35 sev=purple
  - 11: ds=22 sev=-
  - 99: ds=20 sev=-
  - 88: ds=19 sev=-
  - 33: ds=17 sev=-
  - 77: ds=10 sev=-
  - 66: ds=8 sev=-
- non_repeating:
  - 36: ds=77 sev=red
  - 24: ds=61 sev=red
  - 89: ds=55 sev=blue
  - 15: ds=54 sev=blue
  - 78: ds=53 sev=blue
  - 49: ds=47 sev=blue
  - 57: ds=44 sev=blue
  - 09: ds=34 sev=purple
  - 01: ds=32 sev=purple
  - 12: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:430, 1:345, 16:196, 26:128, 17:106, 20:97, 3:76, 23:69, 33:67, 31:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=430 fs=0 fl=2 hz=0.005366726296958855, 1:ds=345 fs=0 fl=0 hz=0.0, 16:ds=196 fs=3 fl=1 hz=0.007853403141361256, 26:ds=128 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=106 fs=13 fl=3 hz=0.018626309662398137, 20:ds=97 fs=15 fl=2 hz=0.01925254813137033, 3:ds=76 fs=15 fl=4 hz=0.02092511013215859, 23:ds=69 fs=25 fl=2 hz=0.03085714285714286, 33:ds=67 fs=27 fl=1 hz=0.030803080308030802, 31:ds=63 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S2: ds=76 flags=blue+purple
- S4: ds=74 flags=purple
- S25: ds=63 flags=purple
- S20: ds=56 flags=purple
- S9: ds=54 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:703(B); evening:804(B)
- 128 -> combined:927(B); evening:905(B)
- 333 -> combined:754(B); midday:981(B)
- 477 -> combined:711(B); evening:788(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:64(red); evening:32(purple); midday:32(purple)
- 11 -> combined:44(purple); midday:32(purple)
- 12 -> combined:41(blue); evening:32(purple)
- 15 -> combined:61(red); evening:54(blue); midday:30(purple)
- 17 -> combined:55(blue); evening:28(purple); midday:27(purple)
- 22 -> combined:129(red); evening:65(purple); midday:64(purple)
- 24 -> combined:39(blue); evening:61(red)
- 26 -> combined:39(blue); evening:25(purple)
- 36 -> combined:33(purple); evening:77(red)
- 44 -> combined:29(purple); evening:35(purple)
- 48 -> combined:32(purple); midday:36(purple)
- 55 -> combined:85(blue); evening:234(red); midday:42(purple)
- 57 -> combined:25(purple); evening:44(blue)
- 67 -> combined:36(purple); midday:39(blue)
- 78 -> combined:25(purple); evening:53(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(8.065071428571429)[R1,Mirror-Echo], 7(5.95725)[R2,XVAR-Cons(CEM)], 2(1.3960785714285713)[R2,Mirror-Echo], 4(1.1477142857142857)[R1,Double-Pressure], 6(0.7548571428571429)[R3,Mirror-Echo]
- P2: 7(3.017714285714286)[R3,XVAR-Cons(CM)], 6(1.2374285714285713)[R1,Double-Pressure], 9(1.1400000000000001)[R1,Double-Pressure], 0(0.942)[R2,Double-Pressure], 2(0.9299)[R2,Double-Pressure]
- P3: 4(6.456371428571428)[R1,XVAR-Cons(CEM)], 1(2.7268)[R3,XVAR-Cons(CE)], 9(1.8549285714285713)[R1,Mirror-Echo], 0(1.2374285714285713)[R1,Double-Pressure], 5(1.206)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=30), P2:9(gap=14), P3:4(gap=29); top cartesian candidates: 174, 774, 171, 164, 194.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 127, 469, 037, 046, 136.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:703(B),evening:804(B); 128→combined:927(B),evening:905(B); 333→combined:754(B),midday:981(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:339, 16:293, 17:165, 20:143, 33:89.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=555 Evening=797; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 555 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 779 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 555 (canon 555): box `555` covers winner `555` (boxed hit).
  - Evening winner 797 (canon 779): box `779` covers winner `797` (boxed hit).
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
