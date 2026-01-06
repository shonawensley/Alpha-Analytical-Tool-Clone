# Master Validation Run Report — Connecticut4 — results 2026-01-04 (history workbook ~ 2026-01-03)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-04/Connecticut4/`
- Winners lens: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-04/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-04/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-04/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-04/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-04/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-04/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_311_20260105_055125.html`
- `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_569_20260105_055123.html`

Winners JSON files:
- `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_311_20260105_055125.json`
- `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_569_20260105_055123.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-04/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 569 (canon 569): exact_boxed=None exact_straight=None | rank 3512/4443 (rank_frac 0.790); Evening 311 (canon 113): exact_boxed=None exact_straight=None | rank 1190/4443 (rank_frac 0.268)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 311 idx18 (rank 19/35, frac 0.543), 569 idx9 (rank 2/35, frac 0.057)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — Connecticut4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-04)

## Midday winner 569 (canonical 569)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=47 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 3512/4443 (rank_frac 0.79045689849201) | score 9.5 (top 36.5, ratio 0.2602739726027397, delta 27.0) | section Midday, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why straight|cov1|hot1|hidden3v|draw_chain3
- Compound (patterns_compound.csv): rank 975/1859 (rank_frac 0.5244755244755245) | score 12.0 (top 65.0, ratio 0.18461538461538463, delta 53.0) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|hot1x1
- Families (patterns_families.csv): count 28 | rank 440/1206 (rank_frac 0.3648424543946932) | score 15.0 (top 29.5, ratio 0.5084745762711864, delta 14.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Evening winner 311 (canonical 113)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=159 | exact_boxed=0 | exact_straight=0 | vt_boxed=12
- Scores (patterns_scores.csv): rank 1190/4443 (rank_frac 0.2678370470402881) | score 13.5 (top 36.5, ratio 0.3698630136986301, delta 23.0) | section Midday, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|hidden3v|double_mirror|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 222/1859 (rank_frac 0.11941904249596558) | score 21.0 (top 65.0, ratio 0.3230769230769231, delta 44.0) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|dblmirrorx6
- Families (patterns_families.csv): count 31 | rank 17/1206 (rank_frac 0.014096185737976783) | score 25.5 (top 29.5, ratio 0.864406779661017, delta 4.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 456 | section Midday | score 62.5 | col1_hits 4 | hot2 9
- rank    4 | canon 348 | section Midday | score 57.0 | col1_hits 6 | hot2 8
- rank    1 | canon 3468 | section Midday | score 65.0 | col1_hits 6 | hot2 8
- rank    3 | canon 368 | section Midday | score 62.0 | col1_hits 6 | hot2 8
- rank    8 | canon 345 | section Midday | score 52.5 | col1_hits 6 | hot2 8
- rank   22 | canon 3458 | section Midday | score 42.0 | col1_hits 3 | hot2 6
- rank   35 | canon 678 | section Midday | score 37.0 | col1_hits 3 | hot2 6
- rank   55 | canon 3678 | section Midday | score 33.0 | col1_hits 3 | hot2 5
- rank   13 | canon 458 | section Combined | score 45.5 | col1_hits 3 | hot2 5
- rank   28 | canon 357 | section Midday | score 39.0 | col1_hits 4 | hot2 5

## Top families (patterns_families.csv)
- rank  998 | family 27 | score 8.0 | hot2 0 | section Midday
- rank   37 | family 23 | score 23.5 | hot2 0 | section Midday
- rank  367 | family 21 | score 16.0 | hot2 0 | section Midday
- rank  367 | family 30 | score 16.0 | hot2 0 | section Midday
- rank  527 | family 28 | score 14.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 569 (canon 569): exact_boxed=None exact_straight=None | rank 3512/4443 (rank_frac 0.790); Evening 311 (canon 113): exact_boxed=None exact_straight=None | rank 1190/4443 (rank_frac 0.268)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260105)

## Midday winner 569 (canonical 569)
- Stamp (winner_stamp.json): items_total=135 | exact_any=0 exact_final=0 | vtrac_any=109 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=62 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=31 family_vtrac_final=0
- Flags (winner_flags.csv): rows=135 | exact_any=0 vtrac_any=109 | drop_exact_any=0 drop_vtrac_any=62 | family_exact_any=0 family_vtrac_any=31 | vt_boxed=69 vt_straight=0
- Hits (winner_hits.csv): rows=135 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=69 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 311 (canonical 113)
- Stamp (winner_stamp.json): items_total=84 | exact_any=48 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=84 | exact_any=48 vtrac_any=84 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=84 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.627143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 569 (canonical 569)
- Stamp (winner_stamp.json): items_total=299 | exact_any=0 exact_final=0 | vtrac_any=260 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=118 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=36 family_vtrac_final=0
- Flags (winner_flags.csv): rows=299 | exact_any=0 vtrac_any=260 | drop_exact_any=0 drop_vtrac_any=118 | family_exact_any=0 family_vtrac_any=36 | vt_boxed=87 vt_straight=0
- Hits (winner_hits.csv): rows=299 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=87 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 17.127143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 16.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 13.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 922 | score_v2 13.687143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 922 | score_v2 13.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 922 | score_v2 13.187143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 922 | score_v2 13.137143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 17.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 922 | score_v2 13.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 224 | score_v2 13.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 992 | score_v2 12.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 924 | score_v2 11.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 441 | score_v2 11.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 922 | score_v2 11.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 922 | score_v2 11.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 992 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 592 | score_v2 10.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 569 (canon 569): items_total=135 exact_any=0 vtrac_any=109 | top winner_present=False best_rank=None/20; Evening 311 (canon 113): items_total=84 exact_any=48 vtrac_any=84 | top winner_present=False best_rank=None/30; Combined 569 (canon 569): items_total=299 exact_any=0 vtrac_any=260 | top winner_present=False best_rank=None/30
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 922, 224, 992, 924.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_055534)

## Top indices (from enhanced JSON)
- index 5 | score 37.85360583333334 | features: presence=27.462772500000007, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 32.54214999999999 | features: presence=19.804649999999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 29.599700000000002 | features: presence=14.652200000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 8 | score 22.006350000000005 | features: presence=9.778850000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 2 | score 20.38875 | features: presence=10.201249999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 19.236750000000004 | features: presence=11.019250000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 16 | score 18.847550000000002 | features: presence=9.880050000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 19 | score 17.5985 | features: presence=9.141000000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 15 | score 15.848958333333334 | features: presence=8.39, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 22 | score 12.073305000000001 | features: presence=6.195805000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
645, 590, 364, 546, 634, 564, 654, 540, 906, 436

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 311 | index 18 | file Connecticut4_vtrac18_winner_311_20260105_055125.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 569 | index 9 | file Connecticut4_vtrac9_winner_569_20260105_055123.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 311 | index 18 rank 19/35 (rank_frac 0.5428571428571428) | score 6.29425 (top 37.85360583333334, ratio 0.16627874310608937, delta 31.559355833333342) | winner_in_index_straights=False | top_index_straights: 136 (0.967)
- winner 569 | index 9 rank 2/35 (rank_frac 0.05714285714285714) | score 32.54214999999999 (top 37.85360583333334, ratio 0.859684283269623, delta 5.311455833333348) | winner_in_index_straights=False | top_index_straights: 645 (13.416), 546 (8.686), 564 (8.388)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 311→idx18 rank 19/35 (frac 0.543); 569→idx9 rank 2/35 (frac 0.057).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 5, 9, 24, 8, 2.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-04)

## Midday winner 569 (canonical 569)
- Top lanes (hot_zones_top_lanes.csv): present | rank 64/210 (rank_frac 0.3047619047619048) | score_mean 18.355 (top 21.448, ratio 0.8557907497202536, delta 3.093)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 311 (canonical 113)
- Top lanes (hot_zones_top_lanes.csv): present | rank 147/210 (rank_frac 0.7) | score_mean 16.514 (top 21.448, ratio 0.7699552405818724, delta 4.934000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 055 | vt_triad 11 | score_mean 21.448 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 255 | vt_triad 13 | score_mean 21.175 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 559 | vt_triad 15 | score_mean 21.15 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 007 | vt_triad 13 | score_mean 21.125 | tags hot16,hot20,hot8,set1_bonus,straight_lane,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 335 | vt_triad 14 | score_mean 20.978 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 499 | vt_triad 55 | score_mean 20.964 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 033 | vt_triad 14 | score_mean 20.928 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 449 | vt_triad 55 | score_mean 20.921 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 588 | vt_triad 14 | score_mean 20.806 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 003 | vt_triad 14 | score_mean 20.608 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 569 (canon 569): rank 64/210 (rank_frac 0.305) ratio_to_top=0.8557907497202536; Evening 311 (canon 113): rank 147/210 (rank_frac 0.700) ratio_to_top=0.7699552405818724
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

Aux draws snapshot dir: `sharepacks/2026-01-04/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=181, 533, 356, 970, 109
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=533, 970, 228, 932, 095
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=181, 356, 109, 361, 467

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=2 last_repeat_gap=37 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=40), P2:4 (gap=13), P3:4 (gap=26)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=889 sev=B
- 129: ds=871 sev=B
- 288: ds=859 sev=B
- 149: ds=841 sev=B
- 445: ds=773 sev=B
- 114: ds=743 sev=B
- 069: ds=707 sev=B
- 888: ds=705 sev=B
- 688: ds=701 sev=B
- 133: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=91 sev=blue
  - 99: ds=72 sev=blue
  - 00: ds=42 sev=purple
  - 88: ds=28 sev=purple
  - 66: ds=27 sev=purple
  - 77: ds=17 sev=-
  - 55: ds=10 sev=-
  - 22: ds=5 sev=-
  - 33: ds=1 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 69: ds=89 sev=red
  - 48: ds=78 sev=red
  - 78: ds=74 sev=red
  - 57: ds=73 sev=red
  - 49: ds=72 sev=red
  - 25: ds=41 sev=blue
  - 06: ds=39 sev=blue
  - 37: ds=34 sev=purple
  - 58: ds=23 sev=-
  - 68: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:407, 32:174, 25:160, 29:133, 4:131, 15:119, 31:108, 34:103, 3:88, 35:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=407 fs=1 fl=2 hz=0.01098901098901099, 32:ds=174 fs=5 fl=2 hz=0.011267605633802818, 25:ds=160 fs=22 fl=2 hz=0.029055690072639227, 29:ds=133 fs=24 fl=1 hz=0.03071253071253071, 4:ds=131 fs=21 fl=2 hz=0.027677496991576414, 15:ds=119 fs=9 fl=4 hz=0.015531660692951015, 31:ds=108 fs=32 fl=0 hz=0.03665521191294387, 34:ds=103 fs=15 fl=2 hz=0.01951779563719862, 3:ds=88 fs=27 fl=0 hz=0.030337078651685393, 35:ds=72 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=82 flags=purple
- S24: ds=74 flags=blue+purple
- S22: ds=72 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=75 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:0 (gap=28), P3:4 (gap=32)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=881 sev=B
- 478: ds=862 sev=B
- 459: ds=857 sev=B
- 159: ds=813 sev=B
- 099: ds=794 sev=B
- 127: ds=785 sev=B
- 559: ds=727 sev=B
- 004: ds=686 sev=B
- 155: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=93 sev=blue
  - 88: ds=53 sev=purple
  - 44: ds=45 sev=purple
  - 55: ds=30 sev=purple
  - 00: ds=26 sev=purple
  - 66: ds=13 sev=-
  - 77: ds=8 sev=-
  - 11: ds=5 sev=-
  - 22: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 78: ds=71 sev=red
  - 13: ds=58 sev=red
  - 49: ds=45 sev=blue
  - 19: ds=44 sev=blue
  - 69: ds=44 sev=blue
  - 48: ds=41 sev=blue
  - 57: ds=36 sev=purple
  - 37: ds=25 sev=purple
  - 01: ds=23 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:203, 25:104, 31:93, 32:91, 18:88, 3:76, 29:66, 4:65, 15:59, 34:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=203 fs=3 fl=0 hz=0.008565310492505354, 25:ds=104 fs=21 fl=1 hz=0.025974025974025976, 31:ds=93 fs=20 fl=2 hz=0.024608501118568233, 32:ds=91 fs=3 fl=4 hz=0.009510869565217392, 18:ds=88 fs=23 fl=1 hz=0.026519337016574582, 3:ds=76 fs=22 fl=2 hz=0.02631578947368421, 29:ds=66 fs=18 fl=2 hz=0.023446658851113716, 4:ds=65 fs=26 fl=0 hz=0.02931228861330327, 15:ds=59 fs=24 fl=1 hz=0.02662406815761448, 34:ds=51 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=87 flags=blue+purple
- S24: ds=84 flags=blue+purple
- S8: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6'], 'pairs': {'remaining_count': 0}}
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
  - 026: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=12 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=20), P2:9 (gap=17), P3:0 (gap=21)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=908 sev=B
- 668: ds=905 sev=B
- 399: ds=904 sev=B
- 044: ds=900 sev=B
- 133: ds=897 sev=B
- 145: ds=869 sev=B
- 677: ds=776 sev=B
- 333: ds=771 sev=B
- 112: ds=723 sev=B
- 344: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=115 sev=red
  - 22: ds=72 sev=blue
  - 99: ds=36 sev=purple
  - 77: ds=30 sev=purple
  - 66: ds=25 sev=purple
  - 33: ds=22 sev=-
  - 00: ds=21 sev=-
  - 88: ds=14 sev=-
  - 55: ds=5 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 57: ds=51 sev=blue
  - 69: ds=49 sev=blue
  - 23: ds=46 sev=blue
  - 25: ds=44 sev=blue
  - 06: ds=43 sev=blue
  - 07: ds=43 sev=blue
  - 48: ds=39 sev=blue
  - 78: ds=37 sev=blue
  - 49: ds=36 sev=purple
  - 15: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:314, 26:142, 4:125, 34:94, 32:87, 25:80, 29:68, 15:67, 2:57, 31:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=314 fs=2 fl=1 hz=0.005961251862891207, 26:ds=142 fs=3 fl=1 hz=0.008680555555555556, 4:ds=125 fs=18 fl=1 hz=0.02243211334120425, 34:ds=94 fs=14 fl=3 hz=0.019144144144144143, 32:ds=87 fs=2 fl=0 hz=0.008450704225352114, 25:ds=80 fs=21 fl=0 hz=0.023836549375709424, 29:ds=68 fs=27 fl=0 hz=0.030100334448160536, 15:ds=67 fs=15 fl=1 hz=0.019698725376593278, 2:ds=57 fs=23 fl=2 hz=0.028344671201814057, 31:ds=54 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=94 flags=blue+purple
- S8: ds=71 flags=red+purple
- S20: ds=54 flags=purple
- S3: ds=41 flags=blue+purple
- S24: ds=37 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:697(B); evening:897(B)
- 445 -> combined:773(B); evening:692(B)
- 459 -> combined:682(B); midday:857(B)
- 888 -> combined:705(B); evening:700(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:42(purple); midday:26(purple)
- 06 -> combined:39(blue); evening:43(blue)
- 25 -> combined:41(blue); evening:44(blue)
- 37 -> combined:34(purple); midday:25(purple)
- 44 -> combined:91(blue); evening:115(red); midday:45(purple)
- 48 -> combined:78(red); evening:39(blue); midday:41(blue)
- 49 -> combined:72(red); evening:36(purple); midday:45(blue)
- 57 -> combined:73(red); evening:51(blue); midday:36(purple)
- 66 -> combined:27(purple); evening:25(purple)
- 69 -> combined:89(red); evening:49(blue); midday:44(blue)
- 78 -> combined:74(red); evening:37(blue); midday:71(red)
- 88 -> combined:28(purple); midday:53(purple)
- 99 -> combined:72(blue); evening:36(purple); midday:93(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.233142857142859)[R1,XVAR-Cons(CEM)], 6(5.538457142857143)[R2,XVAR-Cons(CEM)], 9(1.0761999999999998)[R2,Double-Pressure], 3(0.8926)[R2,Double-Pressure], 8(0.35457142857142854)[R3,Swap]
- P2: 1(3.2164)[R2,XVAR-Cons(CE)], 9(3.0121785714285716)[R3,Mirror-Echo], 4(2.9986785714285715)[R1,Mirror-Echo], 0(1.5970714285714285)[R1,Mirror-Echo], 8(0.9299)[R2,Double-Pressure]
- P3: 4(4.605571428571428)[R1,XVAR-Cons(CM)], 9(1.4268857142857143)[R2,Mirror-Echo], 0(1.327)[R1,Double-Pressure], 2(0.9135)[R2,Double-Pressure], 5(0.8979999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-03.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=40), P2:4(gap=13), P3:4(gap=26); top cartesian candidates: 794, 744, 714, 694, 614.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 014, 023, 024, 025.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:697(B),evening:897(B); 445→combined:773(B),evening:692(B); 459→combined:682(B),midday:857(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:407, 32:174, 25:160, 29:133, 4:131.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=569 Evening=311; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 569 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 113 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 569 (canon 569): box `569` covers winner `569` (boxed hit).
  - Evening winner 311 (canon 113): box `113` covers winner `311` (boxed hit).
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
