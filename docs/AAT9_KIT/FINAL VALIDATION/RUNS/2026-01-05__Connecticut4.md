# Master Validation Run Report — Connecticut4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/Connecticut4/`
- Winners lens: `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-05/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-05/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-05/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-05/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-05/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-05/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_660_20260110_035717.html`
- `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/Connecticut4_vtrac7_winner_071_20260110_035716.html`

Winners JSON files:
- `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_660_20260110_035717.json`
- `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/Connecticut4_vtrac7_winner_071_20260110_035716.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 071 (canon 017): exact_boxed=True exact_straight=True | rank 815/4701 (rank_frac 0.173); Evening 660 (canon 066): exact_boxed=True exact_straight=True | rank 1053/4701 (rank_frac 0.224)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 660 idx6 (rank 23/35, frac 0.657), 071 idx7 (rank 25/35, frac 0.714)
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

### 2.Stable — Connecticut4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-05)

## Midday winner 071 (canonical 017)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=14 | family_rows=31 | exact_boxed=14 | exact_straight=4 | vt_boxed=14
- Scores (patterns_scores.csv): rank 815/4701 (rank_frac 0.17336736864496916) | score 16.5 (top 40.0, ratio 0.4125, delta 23.5) | section Midday, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 0.0 | why boxed|cov2|hp_repeat3|hot2|perm2|hidden3v|draw_chain4
- Compound (patterns_compound.csv): rank 193/1748 (rank_frac 0.11041189931350115) | score 26.5 (top 96.0, ratio 0.2760416666666667, delta 69.5) | section Midday, col1_hits 3, hot2 2, set_chain 1, draw_chain 4 | why draw_chain4|col1x3|hot1x1|hot2x2
- Families (patterns_families.csv): count 20 | rank 366/1304 (rank_frac 0.28067484662576686) | score 17.5 (top 32.5, ratio 0.5384615384615384, delta 15.0) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=35

## Evening winner 660 (canonical 066)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=9 | family_rows=79 | exact_boxed=9 | exact_straight=9 | vt_boxed=9
- Scores (patterns_scores.csv): rank 1053/4701 (rank_frac 0.22399489470325462) | score 15.5 (top 40.0, ratio 0.3875, delta 24.5) | section Midday, Set Set1, Draw Draw5, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot2|hidden3v|double_mirror|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 220/1748 (rank_frac 0.12585812356979406) | score 24.0 (top 96.0, ratio 0.25, delta 72.0) | section Midday, col1_hits 0, hot2 1, set_chain 1, draw_chain 4 | why draw_chain4|hot2x1|vstrx3|dblmirrorx6
- Families (patterns_families.csv): count 19 | rank 550/1304 (rank_frac 0.4217791411042945) | score 15.0 (top 32.5, ratio 0.46153846153846156, delta 17.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=5

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 447 | section Combined | score 96.0 | col1_hits 8 | hot2 11
- rank   10 | canon 468 | section Midday | score 59.5 | col1_hits 6 | hot2 9
- rank    8 | canon 678 | section Midday | score 61.0 | col1_hits 6 | hot2 8
- rank    7 | canon 2244 | section Combined | score 61.5 | col1_hits 5 | hot2 6
- rank   60 | canon 228 | section Combined | score 38.0 | col1_hits 3 | hot2 6
- rank   11 | canon 229 | section Evening | score 58.0 | col1_hits 5 | hot2 6
- rank    5 | canon 448 | section Combined | score 65.0 | col1_hits 4 | hot2 6
- rank   87 | canon 2248 | section Combined | score 34.5 | col1_hits 3 | hot2 6
- rank   14 | canon 447 | section Midday | score 53.5 | col1_hits 5 | hot2 6
- rank   15 | canon 446 | section Midday | score 52.5 | col1_hits 4 | hot2 6

## Top families (patterns_families.csv)
- rank 1296 | family 30 | score 4.0 | hot2 0 | section Midday
- rank  738 | family 25 | score 13.0 | hot2 2 | section Midday
- rank  336 | family 33 | score 18.0 | hot2 0 | section Midday
- rank  192 | family 21 | score 20.5 | hot2 0 | section Midday
- rank  192 | family 23 | score 20.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 071 (canon 017): exact_boxed=True exact_straight=True | rank 815/4701 (rank_frac 0.173); Evening 660 (canon 066): exact_boxed=True exact_straight=True | rank 1053/4701 (rank_frac 0.224)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260110)

## Midday winner 071 (canonical 017)
- Stamp (winner_stamp.json): items_total=3 | exact_any=0 exact_final=0 | vtrac_any=3 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=3 | exact_any=0 vtrac_any=3 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=3 vt_straight=0
- Hits (winner_hits.csv): rows=3 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=3 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 660 (canonical 066)
- Stamp (winner_stamp.json): items_total=48 | exact_any=11 exact_final=0 | vtrac_any=48 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=48 | exact_any=11 vtrac_any=48 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=48 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 071 (canonical 017)
- Stamp (winner_stamp.json): items_total=9 | exact_any=0 exact_final=0 | vtrac_any=9 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=4 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=9 | exact_any=0 vtrac_any=9 | drop_exact_any=0 drop_vtrac_any=4 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=9 vt_straight=0
- Hits (winner_hits.csv): rows=9 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=9 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 224 | score_v2 17.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 224 | score_v2 17.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 224 | score_v2 17.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 224 | score_v2 17.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 447 | score_v2 16.714643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 447 | score_v2 15.664643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 224 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 224 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 224 | score_v2 13.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 224 | score_v2 13.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 441 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 447 | score_v2 12.714643 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 17.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 447 | score_v2 16.714643 | tags exact,vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 224 | score_v2 13.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 441 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 447 | score_v2 12.714643 | tags exact,vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 924 | score_v2 12.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 924 | score_v2 11.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 554 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 11.607143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 224 | score_v2 11.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 11 | variant Combined | best_pattern 922 | score_v2 11.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Evening | best_pattern 592 | score_v2 11.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 071 (canon 017): items_total=3 exact_any=0 vtrac_any=3 | top winner_present=False best_rank=None/20; Evening 660 (canon 066): items_total=48 exact_any=11 vtrac_any=48 | top winner_present=False best_rank=None/28; Combined 071 (canon 017): items_total=9 exact_any=0 vtrac_any=9 | top winner_present=False best_rank=None/22
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 447, 224, 441, 447.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260110_035929)

## Top indices (from enhanced JSON)
- index 23 | score 32.0499 | features: presence=22.492399999999996, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 30.66171 | features: presence=19.15421, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 30.329750000000004 | features: presence=17.12225, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 8 | score 24.750960000000006 | features: presence=11.943460000000004, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 22.96955 | features: presence=14.27205, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 34 | score 19.258619999999997 | features: presence=11.931119999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 9 | score 18.523950000000003 | features: presence=9.966450000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 16.537400000000005 | features: presence=6.969900000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 18 | score 14.49863333333334 | features: presence=7.989675000000004, cross_section=0.5, set_echo=0.3, first_hit=0.13333333333333336
- index 5 | score 13.589725000000003 | features: presence=6.482225000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
543, 386, 836, 534, 568, 683, 364, 684, 645, 438

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 660 | index 6 | file Connecticut4_vtrac6_winner_660_20260110_035717.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 071 | index 7 | file Connecticut4_vtrac7_winner_071_20260110_035716.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 660 | index 6 rank 23/35 (rank_frac 0.6571428571428571) | score 3.8487500000000003 (top 32.0499, ratio 0.12008617811600036, delta 28.201150000000002) | winner_in_index_straights=False | top_index_straights: (none)
- winner 071 | index 7 rank 25/35 (rank_frac 0.7142857142857143) | score 2.566875 (top 32.0499, ratio 0.08008995347879401, delta 29.483025) | winner_in_index_straights=False | top_index_straights: 256 (0.165), 152 (0.15)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 660→idx6 rank 23/35 (frac 0.657); 071→idx7 rank 25/35 (frac 0.714).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 24, 14, 8, 33.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-05)

## Midday winner 071 (canonical 017)
- Top lanes (hot_zones_top_lanes.csv): present | rank 101/210 (rank_frac 0.48095238095238096) | score_mean 17.34 (top 21.202, ratio 0.8178473728893499, delta 3.862000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 660 (canonical 066)
- Top lanes (hot_zones_top_lanes.csv): present | rank 120/210 (rank_frac 0.5714285714285714) | score_mean 17.12 (top 21.202, ratio 0.8074709933025186, delta 4.082000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 335 | vt_triad 14 | score_mean 21.202 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 113 | vt_triad 24 | score_mean 20.941 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 055 | vt_triad 11 | score_mean 20.832 | tags funnel_precol1,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 449 | vt_triad 55 | score_mean 20.706 | tags funnel_precol1,hot16,hot20,hot4,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 368 | vt_triad 244 | score_mean 20.692 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 118 | vt_triad 24 | score_mean 20.678 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    7 | triad 569 | vt_triad 125 | score_mean 20.622 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 499 | vt_triad 55 | score_mean 20.556 | tags funnel_precol1,hot16,hot20,hot4,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 668 | vt_triad 24 | score_mean 20.466 | tags funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 388 | vt_triad 44 | score_mean 20.456 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 071 (canon 017): rank 101/210 (rank_frac 0.481) ratio_to_top=0.8178473728893499; Evening 660 (canon 066): rank 120/210 (rank_frac 0.571) ratio_to_top=0.8074709933025186
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

Aux draws snapshot dir: `sharepacks/2026-01-05/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-05/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=311, 569, 181, 533, 356
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-05/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=569, 533, 970, 228, 932
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-05/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=311, 181, 356, 109, 361

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=2 last_repeat_gap=39 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=42), P2:4 (gap=15), P3:4 (gap=28)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=38.42825714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 794: score=38.38385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=37.626883571428564 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.58248357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 644: score=35.32472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.28032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=34.2715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 704: score=33.70117857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 727: score=33.470126428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=32.899805 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=891 sev=B
- 129: ds=873 sev=B
- 288: ds=861 sev=B
- 149: ds=843 sev=B
- 445: ds=775 sev=B
- 114: ds=745 sev=B
- 069: ds=709 sev=B
- 888: ds=707 sev=B
- 688: ds=703 sev=B
- 133: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=93 sev=blue
  - 99: ds=74 sev=blue
  - 00: ds=44 sev=purple
  - 88: ds=30 sev=purple
  - 66: ds=29 sev=purple
  - 77: ds=19 sev=-
  - 55: ds=12 sev=-
  - 22: ds=7 sev=-
  - 33: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 48: ds=80 sev=red
  - 78: ds=76 sev=red
  - 57: ds=75 sev=red
  - 49: ds=74 sev=red
  - 25: ds=43 sev=blue
  - 06: ds=41 sev=blue
  - 37: ds=36 sev=purple
  - 58: ds=25 sev=purple
  - 68: ds=25 sev=purple
  - 14: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:409, 32:176, 25:162, 29:135, 4:133, 15:121, 31:110, 34:105, 3:90, 35:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=409 fs=1 fl=2 hz=0.01098901098901099, 32:ds=176 fs=5 fl=2 hz=0.011267605633802818, 25:ds=162 fs=22 fl=2 hz=0.029055690072639227, 29:ds=135 fs=24 fl=1 hz=0.03071253071253071, 4:ds=133 fs=21 fl=2 hz=0.027677496991576414, 15:ds=121 fs=9 fl=4 hz=0.015531660692951015, 31:ds=110 fs=32 fl=0 hz=0.03665521191294387, 34:ds=105 fs=15 fl=2 hz=0.01951779563719862, 3:ds=90 fs=27 fl=0 hz=0.030337078651685393, 35:ds=74 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=84 flags=purple
- S24: ds=76 flags=blue+purple
- S22: ds=74 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4', '7'], 'pairs': {'remaining_count': 0}}
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
- current_index=9 streak=1 max=3 last_repeat_gap=76 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=29), P2:0 (gap=29), P3:4 (gap=33)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=38.42825714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 794: score=38.38385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=37.626883571428564 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.58248357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 644: score=35.32472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.28032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=34.2715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 704: score=33.70117857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 727: score=33.470126428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=32.899805 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=882 sev=B
- 478: ds=863 sev=B
- 459: ds=858 sev=B
- 159: ds=814 sev=B
- 099: ds=795 sev=B
- 127: ds=786 sev=B
- 559: ds=728 sev=B
- 004: ds=687 sev=B
- 155: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=94 sev=blue
  - 88: ds=54 sev=purple
  - 44: ds=46 sev=purple
  - 55: ds=31 sev=purple
  - 00: ds=27 sev=purple
  - 66: ds=14 sev=-
  - 77: ds=9 sev=-
  - 11: ds=6 sev=-
  - 22: ds=3 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 78: ds=72 sev=red
  - 13: ds=59 sev=red
  - 49: ds=46 sev=blue
  - 19: ds=45 sev=blue
  - 48: ds=42 sev=blue
  - 57: ds=37 sev=blue
  - 37: ds=26 sev=purple
  - 01: ds=24 sev=-
  - 08: ds=24 sev=-
  - 36: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:204, 25:105, 31:94, 32:92, 18:89, 3:77, 29:67, 4:66, 15:60, 34:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=204 fs=3 fl=0 hz=0.008565310492505354, 25:ds=105 fs=21 fl=1 hz=0.025974025974025976, 31:ds=94 fs=20 fl=2 hz=0.024608501118568233, 32:ds=92 fs=3 fl=4 hz=0.009510869565217392, 18:ds=89 fs=23 fl=1 hz=0.026519337016574582, 3:ds=77 fs=22 fl=2 hz=0.02631578947368421, 29:ds=67 fs=18 fl=2 hz=0.023446658851113716, 4:ds=66 fs=26 fl=0 hz=0.02931228861330327, 15:ds=60 fs=24 fl=1 hz=0.02662406815761448, 34:ds=52 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=88 flags=blue+purple
- S24: ds=85 flags=blue+purple
- S8: ds=55 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=2 max=3 last_repeat_gap=1 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=21), P2:9 (gap=18), P3:0 (gap=22)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=38.42825714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 794: score=38.38385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=37.626883571428564 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.58248357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 644: score=35.32472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.28032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=34.2715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 704: score=33.70117857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 727: score=33.470126428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=32.899805 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=909 sev=B
- 668: ds=906 sev=B
- 399: ds=905 sev=B
- 044: ds=901 sev=B
- 133: ds=898 sev=B
- 145: ds=870 sev=B
- 677: ds=777 sev=B
- 333: ds=772 sev=B
- 112: ds=724 sev=B
- 344: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=116 sev=red
  - 22: ds=73 sev=blue
  - 99: ds=37 sev=purple
  - 77: ds=31 sev=purple
  - 66: ds=26 sev=purple
  - 33: ds=23 sev=-
  - 00: ds=22 sev=-
  - 88: ds=15 sev=-
  - 55: ds=6 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 57: ds=52 sev=blue
  - 69: ds=50 sev=blue
  - 23: ds=47 sev=blue
  - 25: ds=45 sev=blue
  - 06: ds=44 sev=blue
  - 07: ds=44 sev=blue
  - 48: ds=40 sev=blue
  - 78: ds=38 sev=blue
  - 49: ds=37 sev=blue
  - 15: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:315, 26:143, 4:126, 34:95, 32:88, 25:81, 29:69, 15:68, 2:58, 31:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=315 fs=2 fl=1 hz=0.005961251862891207, 26:ds=143 fs=3 fl=1 hz=0.008680555555555556, 4:ds=126 fs=18 fl=1 hz=0.02243211334120425, 34:ds=95 fs=14 fl=3 hz=0.019144144144144143, 32:ds=88 fs=2 fl=0 hz=0.008450704225352114, 25:ds=81 fs=21 fl=0 hz=0.023836549375709424, 29:ds=69 fs=27 fl=0 hz=0.030100334448160536, 15:ds=68 fs=15 fl=1 hz=0.019698725376593278, 2:ds=58 fs=23 fl=2 hz=0.028344671201814057, 31:ds=55 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=95 flags=blue+purple
- S8: ds=72 flags=red+purple
- S20: ds=55 flags=purple
- S3: ds=42 flags=blue+purple
- S24: ds=38 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:699(B); evening:898(B)
- 445 -> combined:775(B); evening:693(B)
- 459 -> combined:684(B); midday:858(B)
- 888 -> combined:707(B); evening:701(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:44(purple); midday:27(purple)
- 06 -> combined:41(blue); evening:44(blue)
- 25 -> combined:43(blue); evening:45(blue)
- 37 -> combined:36(purple); midday:26(purple)
- 44 -> combined:93(blue); evening:116(red); midday:46(purple)
- 48 -> combined:80(red); evening:40(blue); midday:42(blue)
- 49 -> combined:74(red); evening:37(blue); midday:46(blue)
- 57 -> combined:75(red); evening:52(blue); midday:37(blue)
- 66 -> combined:29(purple); evening:26(purple)
- 78 -> combined:76(red); evening:38(blue); midday:72(red)
- 88 -> combined:30(purple); midday:54(purple)
- 99 -> combined:74(blue); evening:37(purple); midday:94(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.502857142857142)[R1,XVAR-Cons(CEM)], 6(5.399328571428572)[R2,XVAR-Cons(CEM)], 9(1.0971)[R2,Double-Pressure], 3(0.9135)[R2,Double-Pressure], 8(0.38285714285714284)[R3,Swap]
- P2: 4(3.8601142857142854)[R1,Mirror-Echo], 9(3.815714285714286)[R2,Mirror-Echo], 2(1.703357142857143)[R3,XVAR-Cons(CE)], 0(1.6330357142857144)[R1,Mirror-Echo], 8(0.9508)[R2,Double-Pressure]
- P3: 4(4.565285714285714)[R1,XVAR-Cons(CM)], 7(1.70235)[R3,XVAR-Cons(CM)], 0(1.3568571428571428)[R1,Double-Pressure], 2(1.0344)[R2,Double-Pressure], 5(0.942)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=42), P2:4(gap=15), P3:4(gap=28); top cartesian candidates: 744, 794, 747, 797, 644.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:699(B),evening:898(B); 445→combined:775(B),evening:693(B); 459→combined:684(B),midday:858(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:409, 32:176, 25:162, 29:135, 4:133.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=071 Evening=660; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 017 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 066 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 071 (canon 017): box `017` covers winner `071` (boxed hit).
  - Evening winner 660 (canon 066): box `066` covers winner `660` (boxed hit).
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
