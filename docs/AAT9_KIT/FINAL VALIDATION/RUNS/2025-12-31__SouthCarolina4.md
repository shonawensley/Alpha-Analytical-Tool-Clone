# Master Validation Run Report — SouthCarolina4 — results 2025-12-31 (history workbook ~ 2025-12-30)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-31/SouthCarolina4/`
- Winners lens: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2025-12-31/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2025-12-31/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2025-12-31/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2025-12-31/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2025-12-31/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-12-31/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac15_winner_044_20260105_052214.html`
- `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac8_winner_653_20260105_052213.html`

Winners JSON files:
- `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac15_winner_044_20260105_052214.json`
- `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac8_winner_653_20260105_052213.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 653 (canon 356): exact_boxed=True exact_straight=True | rank 2678/5346 (rank_frac 0.501); Evening 044 (canon 044): exact_boxed=True exact_straight=True | rank 2040/5346 (rank_frac 0.382)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 044 idx15 (rank 11/35, frac 0.314), 653 idx8 (rank 3/35, frac 0.086)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — SouthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2025-12-31)

## Midday winner 653 (canonical 356)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=13 | family_rows=709 | exact_boxed=13 | exact_straight=13 | vt_boxed=13
- Scores (patterns_scores.csv): rank 2678/5346 (rank_frac 0.5009352787130565) | score 13.0 (top 35.5, ratio 0.36619718309859156, delta 22.5) | section Combined, Set Set1, Draw Draw1, Col 5, hot 1, vt_straight 0.0 | why straight|cov1|hp_repeat3|hot1|set_chain2|draw_chain3
- Compound (patterns_compound.csv): rank 483/1665 (rank_frac 0.29009009009009007) | score 18.0 (top 91.5, ratio 0.19672131147540983, delta 73.5) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 4 | why draw_chain4|hot1x1|vstrx4
- Families (patterns_families.csv): count 94 | rank 2/1516 (rank_frac 0.0013192612137203166) | score 30.0 (top 30.5, ratio 0.9836065573770492, delta 0.5) | section Combined, hot2 5
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=129

## Evening winner 044 (canonical 044)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=94 | exact_boxed=10 | exact_straight=10 | vt_boxed=10
- Scores (patterns_scores.csv): rank 2040/5346 (rank_frac 0.38159371492704824) | score 14.0 (top 35.5, ratio 0.39436619718309857, delta 21.5) | section Midday, Set Set1, Draw Draw1, Col 5, hot 1, vt_straight 0.0 | why straight|cov1|hp_repeat3|hot1|double_mirror|set_chain2|draw_chain3
- Compound (patterns_compound.csv): rank 217/1665 (rank_frac 0.13033033033033034) | score 24.5 (top 91.5, ratio 0.2677595628415301, delta 67.0) | section Midday, col1_hits 0, hot2 0, set_chain 2, draw_chain 3 | why set_chain2|draw_chain3|hot1x2|dblmirrorx10
- Families (patterns_families.csv): count 43 | rank 49/1516 (rank_frac 0.032321899736147755) | score 26.0 (top 30.5, ratio 0.8524590163934426, delta 4.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=12

## Top compound candidates (patterns_compound.csv)
- rank    4 | canon 138 | section Combined | score 67.0 | col1_hits 7 | hot2 11
- rank    1 | canon 006 | section Midday | score 91.5 | col1_hits 8 | hot2 10
- rank   14 | canon 038 | section Combined | score 58.5 | col1_hits 5 | hot2 9
- rank    8 | canon 0138 | section Combined | score 63.5 | col1_hits 5 | hot2 9
- rank   19 | canon 1138 | section Combined | score 54.5 | col1_hits 6 | hot2 8
- rank   15 | canon 0113 | section Combined | score 58.0 | col1_hits 6 | hot2 8
- rank    9 | canon 068 | section Midday | score 63.0 | col1_hits 6 | hot2 8
- rank   10 | canon 01138 | section Combined | score 62.5 | col1_hits 6 | hot2 8
- rank    7 | canon 113 | section Combined | score 64.5 | col1_hits 6 | hot2 8
- rank    6 | canon 0068 | section Midday | score 65.5 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1506 | family 28 | score 4.0 | hot2 0 | section Midday
- rank  168 | family 8 | score 23.0 | hot2 4 | section Midday
- rank 1036 | family 33 | score 12.5 | hot2 0 | section Midday
- rank 1082 | family 1 | score 12.0 | hot2 0 | section Midday
- rank 1082 | family 4 | score 12.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 653 (canon 356): exact_boxed=True exact_straight=True | rank 2678/5346 (rank_frac 0.501); Evening 044 (canon 044): exact_boxed=True exact_straight=True | rank 2040/5346 (rank_frac 0.382)
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

### 2.Digit Reduction — SouthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260105)

## Midday winner 653 (canonical 356)
- Stamp (winner_stamp.json): items_total=136 | exact_any=0 exact_final=0 | vtrac_any=109 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=80 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=23 family_vtrac_final=0
- Flags (winner_flags.csv): rows=136 | exact_any=0 vtrac_any=109 | drop_exact_any=0 drop_vtrac_any=80 | family_exact_any=0 family_vtrac_any=23 | vt_boxed=81 vt_straight=0
- Hits (winner_hits.csv): rows=136 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=81 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 044 (canonical 044)
- Stamp (winner_stamp.json): items_total=156 | exact_any=0 exact_final=0 | vtrac_any=156 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=156 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=120 family_vtrac_final=0
- Flags (winner_flags.csv): rows=156 | exact_any=0 vtrac_any=156 | drop_exact_any=0 drop_vtrac_any=156 | family_exact_any=0 family_vtrac_any=120 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=156 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 653 (canonical 356)
- Stamp (winner_stamp.json): items_total=559 | exact_any=0 exact_final=0 | vtrac_any=493 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=370 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=159 family_vtrac_final=0
- Flags (winner_flags.csv): rows=559 | exact_any=0 vtrac_any=493 | drop_exact_any=0 drop_vtrac_any=370 | family_exact_any=0 family_vtrac_any=159 | vt_boxed=338 vt_straight=0
- Hits (winner_hits.csv): rows=559 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=338 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.237143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 990 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 900 | score_v2 13.327143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 900 | score_v2 13.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 990 | score_v2 12.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 990 | score_v2 12.777143 | match_types 
- area_rank 2 | variant Midday | section Midday | set Set1 draw Draw6 col 1 | pattern 990 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 200 | score_v2 11.237143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 901 | score_v2 10.227143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 7 | pattern 559 | score_v2 10.027143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 501 | score_v2 9.977143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 990 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 900 | score_v2 13.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 200 | score_v2 11.237143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 901 | score_v2 10.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 501 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 501 | score_v2 9.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 590 | score_v2 9.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 552 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 901 | score_v2 9.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 653 (canon 356): items_total=136 exact_any=0 vtrac_any=109 | top winner_present=False best_rank=None/26; Evening 044 (canon 044): items_total=156 exact_any=0 vtrac_any=156 | top winner_present=False best_rank=None/28; Combined 653 (canon 356): items_total=559 exact_any=0 vtrac_any=493 | top winner_present=False best_rank=None/18
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 990, 900, 200, 901, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_053052)

## Top indices (from enhanced JSON)
- index 24 | score 52.806940000000004 | features: presence=35.37944, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 40.7415175 | features: presence=29.2640175, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 40.704600000000006 | features: presence=29.897100000000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 35.6898 | features: presence=24.3423, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 27.16025 | features: presence=15.852749999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 25.931170000000005 | features: presence=16.113670000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 13 | score 25.230195 | features: presence=12.982694999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 23.230060000000005 | features: presence=13.652560000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 21 | score 21.328517500000004 | features: presence=14.201017499999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 21.1957725 | features: presence=12.6182725, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
198, 918, 901, 819, 013, 138, 981, 019, 018, 908

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 044 | index 15 | file SouthCarolina4_vtrac15_winner_044_20260105_052214.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 653 | index 8 | file SouthCarolina4_vtrac8_winner_653_20260105_052213.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 044 | index 15 rank 11/35 (rank_frac 0.3142857142857143) | score 20.236515 (top 52.806940000000004, ratio 0.38321695974051895, delta 32.570425) | winner_in_index_straights=False | top_index_straights: (none)
- winner 653 | index 8 rank 3/35 (rank_frac 0.08571428571428572) | score 40.704600000000006 (top 52.806940000000004, ratio 0.7708191385450474, delta 12.102339999999998) | winner_in_index_straights=False | top_index_straights: 013 (16.306), 018 (15.296), 081 (11.409)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 044→idx15 rank 11/35 (frac 0.314); 653→idx8 rank 3/35 (frac 0.086).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 24, 23, 8, 9, 14.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2025-12-31

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2025-12-31)

## Midday winner 653 (canonical 356)
- Top lanes (hot_zones_top_lanes.csv): present | rank 79/201 (rank_frac 0.39303482587064675) | score_mean 17.437 (top 24.946, ratio 0.6989898180068949, delta 7.509)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 044 (canonical 044)
- Top lanes (hot_zones_top_lanes.csv): present | rank 93/201 (rank_frac 0.4626865671641791) | score_mean 17.272 (top 24.946, ratio 0.692375531147278, delta 7.674000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 679 | vt_triad 235 | score_mean 24.946 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 257 | vt_triad 133 | score_mean 24.6 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical4,vt_straight
- rank    3 | triad 124 | vt_triad 235 | score_mean 23.713 | tags col1,guard_set1,hot16,hot20,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    4 | triad 224 | vt_triad 35 | score_mean 22.817 | tags hot16,hot20,set1_bonus,straight_lane,vertical3
- rank    5 | triad 379 | vt_triad 345 | score_mean 22.422 | tags funnel_precol1,hot16,hot20,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_only_lane,vt_straight
- rank    6 | triad 248 | vt_triad 345 | score_mean 21.857 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,vertical1,vertical2,vt_only_lane,vt_straight
- rank    7 | triad 489 | vt_triad 455 | score_mean 21.622 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 457 | vt_triad 135 | score_mean 20.472 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    9 | triad 246 | vt_triad 235 | score_mean 20.349 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 779 | vt_triad 35 | score_mean 19.917 | tags hot16,hot20,set1_bonus

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 653 (canon 356): rank 79/201 (rank_frac 0.393) ratio_to_top=0.6989898180068949; Evening 044 (canon 044): rank 93/201 (rank_frac 0.463) ratio_to_top=0.692375531147278
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

Aux draws snapshot dir: `sharepacks/2025-12-31/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=976, 754, 463, 425, 849
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=754, 425, 462, 144, 528
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=976, 463, 849, 257, 240

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=11 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=26), P2:3 (gap=27), P3:1 (gap=13)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 225: ds=997 sev=B
- 233: ds=994 sev=B
- 366: ds=966 sev=B
- 449: ds=895 sev=B
- 156: ds=878 sev=B
- 778: ds=848 sev=B
- 279: ds=847 sev=B
- 033: ds=779 sev=B
- 004: ds=767 sev=B
- 688: ds=734 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=175 sev=red
  - 55: ds=112 sev=red
  - 77: ds=96 sev=blue
  - 33: ds=83 sev=blue
  - 88: ds=78 sev=blue
  - 22: ds=58 sev=purple
  - 66: ds=46 sev=purple
  - 00: ds=19 sev=-
  - 11: ds=15 sev=-
  - 44: ds=8 sev=-
- non_repeating:
  - 35: ds=104 sev=red
  - 15: ds=54 sev=blue
  - 18: ds=52 sev=blue
  - 78: ds=47 sev=blue
  - 05: ds=43 sev=blue
  - 68: ds=35 sev=purple
  - 29: ds=28 sev=purple
  - 09: ds=23 sev=-
  - 06: ds=21 sev=-
  - 16: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:439, 35:382, 1:163, 26:151, 31:113, 4:104, 23:102, 28:96, 15:86, 27:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=439 fs=0 fl=0 hz=0.002197802197802198, 35:ds=382 fs=0 fl=0 hz=0.001949317738791423, 1:ds=163 fs=6 fl=4 hz=0.012195121951219513, 26:ds=151 fs=2 fl=0 hz=0.0062402496099844, 31:ds=113 fs=28 fl=0 hz=0.03160270880361174, 4:ds=104 fs=21 fl=2 hz=0.026589595375722544, 23:ds=102 fs=25 fl=1 hz=0.029850746268656716, 28:ds=96 fs=16 fl=2 hz=0.021479713603818614, 15:ds=86 fs=14 fl=3 hz=0.020506634499396863, 27:ds=79 fs=26 fl=0 hz=0.02911534154535274

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=88 flags=red+purple
- S8: ds=62 flags=red+purple
- S0: ds=61 flags=blue+purple
- S23: ds=50 flags=blue+purple
- S5: ds=49 flags=purple
- S24: ds=47 flags=blue+purple
- S4: ds=39 flags=purple

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
- current_index=12 streak=2 max=3 last_repeat_gap=1 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=28), P2:3 (gap=37), P3:9 (gap=22)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=875 sev=B
- 555: ds=870 sev=B
- 222: ds=847 sev=B
- 337: ds=824 sev=B
- 003: ds=815 sev=B
- 228: ds=806 sev=B
- 556: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=110 sev=red
  - 55: ds=74 sev=blue
  - 77: ds=43 sev=purple
  - 33: ds=37 sev=purple
  - 88: ds=35 sev=purple
  - 22: ds=33 sev=purple
  - 66: ds=20 sev=-
  - 00: ds=11 sev=-
  - 11: ds=6 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 49: ds=51 sev=blue
  - 35: ds=47 sev=blue
  - 67: ds=45 sev=blue
  - 34: ds=44 sev=blue
  - 09: ds=41 sev=blue
  - 27: ds=38 sev=blue
  - 07: ds=29 sev=purple
  - 05: ds=26 sev=purple
  - 36: ds=25 sev=purple
  - 15: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:411, 26:189, 35:175, 27:140, 6:108, 5:77, 1:74, 15:69, 34:55, 31:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=411 fs=1 fl=2 hz=0.006993006993006993, 26:ds=189 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=175 fs=1 fl=1 hz=0.004968944099378882, 27:ds=140 fs=18 fl=3 hz=0.026582278481012658, 6:ds=108 fs=24 fl=2 hz=0.02957906712172924, 5:ds=77 fs=20 fl=1 hz=0.023102310231023104, 1:ds=74 fs=7 fl=3 hz=0.012127894156560088, 15:ds=69 fs=17 fl=3 hz=0.021691973969631236, 34:ds=55 fs=28 fl=1 hz=0.03159041394335512, 31:ds=51 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=78 flags=purple
- S25: ds=75 flags=purple
- S21: ds=55 flags=purple
- S20: ds=51 flags=purple
- S17: ds=49 flags=purple
- S8: ds=47 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 125: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=28 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=23), P2:8 (gap=18), P3:1 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=978 sev=B
- 117: ds=889 sev=B
- 005: ds=875 sev=B
- 577: ds=852 sev=B
- 155: ds=832 sev=B
- 777: ds=831 sev=B
- 669: ds=823 sev=B
- 179: ds=805 sev=B
- 366: ds=771 sev=B
- 222: ds=765 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=95 sev=blue
  - 77: ds=82 sev=blue
  - 66: ds=74 sev=blue
  - 33: ds=70 sev=purple
  - 55: ds=61 sev=purple
  - 88: ds=55 sev=purple
  - 22: ds=32 sev=purple
  - 11: ds=21 sev=-
  - 44: ds=20 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 58: ds=96 sev=red
  - 35: ds=63 sev=red
  - 29: ds=58 sev=red
  - 47: ds=48 sev=blue
  - 15: ds=44 sev=blue
  - 18: ds=30 sev=purple
  - 19: ds=30 sev=purple
  - 78: ds=26 sev=purple
  - 05: ds=24 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:483, 1:270, 32:237, 31:216, 4:136, 28:109, 19:105, 23:100, 26:82, 16:78

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=483 fs=3 fl=1 hz=0.017391304347826087, 1:ds=270 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=237 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=216 fs=16 fl=1 hz=0.021935483870967745, 4:ds=136 fs=21 fl=3 hz=0.028742514970059883, 28:ds=109 fs=10 fl=4 hz=0.017676767676767676, 19:ds=105 fs=12 fl=2 hz=0.016968325791855206, 23:ds=100 fs=24 fl=0 hz=0.02937576499388005, 26:ds=82 fs=0 fl=0 hz=0.002347417840375587, 16:ds=78 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=61 flags=purple
- S15: ds=52 flags=red+purple
- S9: ds=49 flags=purple
- S17: ds=48 flags=purple

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
- 222 -> evening:765(B); midday:847(B)
- 366 -> combined:966(B); evening:771(B)
- 688 -> combined:734(B); evening:730(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:43(blue); midday:26(purple)
- 15 -> combined:54(blue); evening:44(blue)
- 18 -> combined:52(blue); evening:30(purple)
- 22 -> combined:58(purple); evening:32(purple); midday:33(purple)
- 29 -> combined:28(purple); evening:58(red)
- 33 -> combined:83(blue); evening:70(purple); midday:37(purple)
- 35 -> combined:104(red); evening:63(red); midday:47(blue)
- 55 -> combined:112(red); evening:61(purple); midday:74(blue)
- 66 -> combined:46(purple); evening:74(blue)
- 77 -> combined:96(blue); evening:82(blue); midday:43(purple)
- 78 -> combined:47(blue); evening:26(purple)
- 88 -> combined:78(blue); evening:55(purple); midday:35(purple)
- 99 -> combined:175(red); evening:95(blue); midday:110(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(7.006878571428571)[R2,XVAR-Cons(CEM)], 0(6.822364285714285)[R1,Mirror-Echo], 9(1.536)[R1,Double-Pressure], 5(0.527)[R3,Mirror-Echo], 1(0.2807928571428571)[R3,Mirror-Echo]
- P2: 3(8.63632142857143)[R1,Mirror-Echo], 8(7.545564285714286)[R2,Mirror-Echo], 9(1.8182142857142858)[R3,XVAR-Cons(CE)], 7(0.43889999999999996)[R2]
- P3: 1(3.5355714285714286)[R1,XVAR-Cons(CE)], 8(3.2973)[R2,XVAR-Cons(CE)], 0(1.5736642857142857)[R3,XVAR-Cons(CM)], 9(1.3568571428571428)[R1,Double-Pressure], 6(0.9135)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_30.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=26), P2:3(gap=27), P3:1(gap=13); top cartesian candidates: 631, 031, 638, 038, 030.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1'], 'pairs': {'remaining_count': 1}}; top candidates: 017, 026, 035, 089, 125.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:847(B),evening:765(B); 366→combined:966(B),evening:771(B); 688→combined:734(B),evening:730(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:439, 35:382, 1:163, 26:151, 31:113.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=653 Evening=044; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 356 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 044 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 653 (canon 356): box `356` covers winner `653` (boxed hit).
  - Evening winner 044 (canon 044): box `044` covers winner `044` (boxed hit).
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
