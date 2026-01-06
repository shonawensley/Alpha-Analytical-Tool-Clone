# Master Validation Run Report — Connecticut4 — results 2026-01-03 (history workbook ~ 2026-01-02)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-03/Connecticut4/`
- Winners lens: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-03/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-03/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-03/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-03/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-03/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-03/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac13_winner_533_20260105_054533.html`
- `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_181_20260105_054534.html`

Winners JSON files:
- `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac13_winner_533_20260105_054533.json`
- `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/Connecticut4_vtrac18_winner_181_20260105_054534.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-03/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 533 (canon 335): exact_boxed=True exact_straight=True | rank 3661/4443 (rank_frac 0.824); Evening 181 (canon 118): exact_boxed=True exact_straight=True | rank 116/4443 (rank_frac 0.026)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 533 idx13 (rank 30/35, frac 0.857), 181 idx18 (rank 13/35, frac 0.371)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — Connecticut4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-03)

## Midday winner 533 (canonical 335)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=47 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 3661/4443 (rank_frac 0.8239927976592393) | score 9.0 (top 36.5, ratio 0.2465753424657534, delta 27.5) | section Combined, Set Set1, Draw Draw6, Col 2, hot 0, vt_straight 2.0 | why straight|cov1|double_mirror|vtrac_straight
- Compound (patterns_compound.csv): rank 1272/1859 (rank_frac 0.684238838084992) | score 10.5 (top 65.0, ratio 0.16153846153846155, delta 54.5) | section Combined, col1_hits 0, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1|vstrx1|dblmirrorx1
- Families (patterns_families.csv): count 28 | rank 440/1206 (rank_frac 0.3648424543946932) | score 15.0 (top 29.5, ratio 0.5084745762711864, delta 14.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=11

## Evening winner 181 (canonical 118)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=15 | family_rows=159 | exact_boxed=15 | exact_straight=5 | vt_boxed=15
- Scores (patterns_scores.csv): rank 116/4443 (rank_frac 0.026108485257708754) | score 21.0 (top 36.5, ratio 0.5753424657534246, delta 15.5) | section Evening, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat3|vstr2|hot1|perm2|double_mirror|set_chain3|draw_chain3
- Compound (patterns_compound.csv): rank 61/1859 (rank_frac 0.0328133405056482) | score 32.0 (top 65.0, ratio 0.49230769230769234, delta 33.0) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|hot1x1|dblmirrorx9
- Families (patterns_families.csv): count 31 | rank 17/1206 (rank_frac 0.014096185737976783) | score 25.5 (top 29.5, ratio 0.864406779661017, delta 4.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=22

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
- Q1: Winners evidence: Midday 533 (canon 335): exact_boxed=True exact_straight=True | rank 3661/4443 (rank_frac 0.824); Evening 181 (canon 118): exact_boxed=True exact_straight=True | rank 116/4443 (rank_frac 0.026)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260105)

## Midday winner 533 (canonical 335)
- Stamp (winner_stamp.json): items_total=210 | exact_any=6 exact_final=0 | vtrac_any=144 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=102 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=26 family_vtrac_final=0
- Flags (winner_flags.csv): rows=210 | exact_any=6 vtrac_any=144 | drop_exact_any=12 drop_vtrac_any=102 | family_exact_any=0 family_vtrac_any=26 | vt_boxed=42 vt_straight=0
- Hits (winner_hits.csv): rows=210 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=42 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.727143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 181 (canonical 118)
- Stamp (winner_stamp.json): items_total=108 | exact_any=68 exact_final=0 | vtrac_any=108 vtrac_final=0 | drop_exact_any=9 drop_exact_final=0 | drop_vtrac_any=11 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=108 | exact_any=68 vtrac_any=108 | drop_exact_any=9 drop_vtrac_any=11 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=13 vt_straight=0
- Hits (winner_hits.csv): rows=108 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=13 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.547143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 533 (canonical 335)
- Stamp (winner_stamp.json): items_total=270 | exact_any=6 exact_final=0 | vtrac_any=204 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=102 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=26 family_vtrac_final=0
- Flags (winner_flags.csv): rows=270 | exact_any=6 vtrac_any=204 | drop_exact_any=12 drop_vtrac_any=102 | family_exact_any=0 family_vtrac_any=26 | vt_boxed=42 vt_straight=0
- Hits (winner_hits.csv): rows=270 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=42 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.19381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 488 | score_v2 11.19381 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 544 | score_v2 10.727143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 924 | score_v2 10.547143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 544 | score_v2 10.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 544 | score_v2 10.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 924 | score_v2 10.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 5 | pattern 924 | score_v2 10.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 924 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 924 | score_v2 10.197143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 924 | score_v2 10.197143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 488 | score_v2 11.19381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 544 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 924 | score_v2 10.547143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 924 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 922 | score_v2 10.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 924 | score_v2 10.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 241 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 418 | score_v2 9.997143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 922 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 924 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 533 (canon 335): items_total=210 exact_any=6 vtrac_any=144 | top winner_present=False best_rank=None/26; Evening 181 (canon 118): items_total=108 exact_any=68 vtrac_any=108 | top winner_present=False best_rank=None/36; Combined 533 (canon 335): items_total=270 exact_any=6 vtrac_any=204 | top winner_present=False best_rank=None/34
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 488, 544, 924, 924, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_054814)

## Top indices (from enhanced JSON)
- index 14 | score 36.8003675 | features: presence=25.102867500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 28.145649999999996 | features: presence=17.008149999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 25.671450000000004 | features: presence=16.78395, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 25.351500000000005 | features: presence=14.294000000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 30 | score 24.5361775 | features: presence=14.628677499999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 22.800487500000003 | features: presence=11.392987500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 16 | score 20.036 | features: presence=13.158500000000002, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 5 | score 18.901058333333335 | features: presence=8.2521, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 33 | score 18.304022500000002 | features: presence=8.106522500000002, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 23 | score 18.140705000000004 | features: presence=10.553205000000002, set_echo=0.6, first_hit=0.2, column_span=0.0875

## Top straights (from enhanced JSON)
084, 048, 086, 645, 847, 068, 864, 874, 548, 546

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 533 | index 13 | file Connecticut4_vtrac13_winner_533_20260105_054533.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 181 | index 18 | file Connecticut4_vtrac18_winner_181_20260105_054534.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 533 | index 13 rank 30/35 (rank_frac 0.8571428571428571) | score 1.6321250000000003 (top 36.8003675, ratio 0.04435077992087987, delta 35.1682425) | winner_in_index_straights=False | top_index_straights: (none)
- winner 181 | index 18 rank 13/35 (rank_frac 0.37142857142857144) | score 11.935874999999998 (top 36.8003675, ratio 0.32434119034273223, delta 24.864492500000004) | winner_in_index_straights=False | top_index_straights: 186 (0.963), 681 (0.65)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 533→idx13 rank 30/35 (frac 0.857); 181→idx18 rank 13/35 (frac 0.371).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 14, 2, 9, 8, 30.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-03)

## Midday winner 533 (canonical 335)
- Top lanes (hot_zones_top_lanes.csv): present | rank 191/210 (rank_frac 0.9095238095238095) | score_mean 14.909 (top 23.017, ratio 0.6477386279706304, delta 8.107999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 181 (canonical 118)
- Top lanes (hot_zones_top_lanes.csv): present | rank 149/210 (rank_frac 0.7095238095238096) | score_mean 16.498 (top 23.017, ratio 0.7167745579354391, delta 6.518999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 127 | vt_triad 233 | score_mean 23.017 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 267 | vt_triad 233 | score_mean 22.45 | tags hot16,hot20,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 279 | vt_triad 335 | score_mean 21.755 | tags col1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 079 | vt_triad 135 | score_mean 21.256 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 117 | vt_triad 23 | score_mean 21.122 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 467 | vt_triad 235 | score_mean 20.64 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 177 | vt_triad 23 | score_mean 20.614 | tags funnel_precol1,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 055 | vt_triad 11 | score_mean 20.566 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 266 | vt_triad 23 | score_mean 20.333 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 136 | vt_triad 224 | score_mean 20.31 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 533 (canon 335): rank 191/210 (rank_frac 0.910) ratio_to_top=0.6477386279706304; Evening 181 (canon 118): rank 149/210 (rank_frac 0.710) ratio_to_top=0.7167745579354391
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

Aux draws snapshot dir: `sharepacks/2026-01-03/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=356, 970, 109, 228, 361
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=970, 228, 932, 095, 211
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=356, 109, 361, 467, 055

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=2 last_repeat_gap=35 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=38), P2:8 (gap=12), P3:4 (gap=24)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=887 sev=B
- 129: ds=869 sev=B
- 288: ds=857 sev=B
- 149: ds=839 sev=B
- 445: ds=771 sev=B
- 114: ds=741 sev=B
- 069: ds=705 sev=B
- 888: ds=703 sev=B
- 688: ds=699 sev=B
- 133: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=89 sev=blue
  - 99: ds=70 sev=purple
  - 00: ds=40 sev=purple
  - 33: ds=27 sev=purple
  - 88: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 77: ds=15 sev=-
  - 11: ds=9 sev=-
  - 55: ds=8 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 69: ds=87 sev=red
  - 48: ds=76 sev=red
  - 78: ds=72 sev=red
  - 57: ds=71 sev=red
  - 49: ds=70 sev=red
  - 25: ds=39 sev=blue
  - 06: ds=37 sev=blue
  - 37: ds=32 sev=purple
  - 18: ds=29 sev=purple
  - 58: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:405, 32:172, 25:158, 29:131, 4:129, 15:117, 31:106, 34:101, 3:86, 35:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=405 fs=1 fl=2 hz=0.01098901098901099, 32:ds=172 fs=5 fl=2 hz=0.011267605633802818, 25:ds=158 fs=22 fl=2 hz=0.029055690072639227, 29:ds=131 fs=25 fl=1 hz=0.029988465974625143, 4:ds=129 fs=21 fl=2 hz=0.027677496991576414, 15:ds=117 fs=9 fl=4 hz=0.015531660692951015, 31:ds=106 fs=32 fl=0 hz=0.03665521191294387, 34:ds=101 fs=15 fl=2 hz=0.01951779563719862, 3:ds=86 fs=27 fl=0 hz=0.030337078651685393, 35:ds=70 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=80 flags=purple
- S24: ds=72 flags=blue+purple
- S22: ds=70 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=74 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=27), P2:0 (gap=27), P3:4 (gap=31)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=880 sev=B
- 478: ds=861 sev=B
- 459: ds=856 sev=B
- 159: ds=812 sev=B
- 099: ds=793 sev=B
- 127: ds=784 sev=B
- 559: ds=726 sev=B
- 004: ds=685 sev=B
- 155: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=92 sev=blue
  - 88: ds=52 sev=purple
  - 44: ds=44 sev=purple
  - 55: ds=29 sev=purple
  - 00: ds=25 sev=purple
  - 33: ds=13 sev=-
  - 66: ds=12 sev=-
  - 77: ds=7 sev=-
  - 11: ds=4 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 78: ds=70 sev=red
  - 13: ds=57 sev=red
  - 49: ds=44 sev=blue
  - 19: ds=43 sev=blue
  - 69: ds=43 sev=blue
  - 48: ds=40 sev=blue
  - 57: ds=35 sev=purple
  - 37: ds=24 sev=-
  - 01: ds=22 sev=-
  - 08: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:202, 25:103, 31:92, 32:90, 18:87, 3:75, 29:65, 4:64, 15:58, 34:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=202 fs=3 fl=0 hz=0.008565310492505354, 25:ds=103 fs=21 fl=1 hz=0.025974025974025976, 31:ds=92 fs=20 fl=2 hz=0.024608501118568233, 32:ds=90 fs=3 fl=4 hz=0.009510869565217392, 18:ds=87 fs=23 fl=1 hz=0.026519337016574582, 3:ds=75 fs=22 fl=2 hz=0.02631578947368421, 29:ds=65 fs=18 fl=2 hz=0.023446658851113716, 4:ds=64 fs=26 fl=0 hz=0.02931228861330327, 15:ds=58 fs=24 fl=1 hz=0.02662406815761448, 34:ds=50 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=86 flags=blue+purple
- S24: ds=83 flags=blue+purple
- S8: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=11 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=19), P2:9 (gap=16), P3:0 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=907 sev=B
- 668: ds=904 sev=B
- 399: ds=903 sev=B
- 044: ds=899 sev=B
- 133: ds=896 sev=B
- 145: ds=868 sev=B
- 677: ds=775 sev=B
- 333: ds=770 sev=B
- 112: ds=722 sev=B
- 344: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=114 sev=red
  - 22: ds=71 sev=blue
  - 99: ds=35 sev=purple
  - 77: ds=29 sev=purple
  - 66: ds=24 sev=-
  - 11: ds=23 sev=-
  - 33: ds=21 sev=-
  - 00: ds=20 sev=-
  - 88: ds=13 sev=-
  - 55: ds=4 sev=-
- non_repeating:
  - 57: ds=50 sev=blue
  - 69: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 25: ds=43 sev=blue
  - 06: ds=42 sev=blue
  - 07: ds=42 sev=blue
  - 48: ds=38 sev=blue
  - 78: ds=36 sev=purple
  - 49: ds=35 sev=purple
  - 15: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:313, 26:141, 4:124, 34:93, 32:86, 25:79, 29:67, 15:66, 2:56, 31:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=313 fs=2 fl=1 hz=0.005961251862891207, 26:ds=141 fs=3 fl=1 hz=0.008680555555555556, 4:ds=124 fs=18 fl=1 hz=0.02243211334120425, 34:ds=93 fs=14 fl=3 hz=0.019144144144144143, 32:ds=86 fs=2 fl=0 hz=0.008450704225352114, 25:ds=79 fs=21 fl=0 hz=0.023836549375709424, 29:ds=67 fs=27 fl=0 hz=0.030100334448160536, 15:ds=66 fs=15 fl=1 hz=0.019698725376593278, 2:ds=56 fs=23 fl=2 hz=0.028344671201814057, 31:ds=53 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=93 flags=blue+purple
- S8: ds=70 flags=red+purple
- S20: ds=53 flags=purple
- S3: ds=40 flags=blue+purple
- S24: ds=36 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:695(B); evening:896(B)
- 445 -> combined:771(B); evening:691(B)
- 459 -> combined:680(B); midday:856(B)
- 888 -> combined:703(B); evening:699(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:40(purple); midday:25(purple)
- 06 -> combined:37(blue); evening:42(blue)
- 25 -> combined:39(blue); evening:43(blue)
- 44 -> combined:89(blue); evening:114(red); midday:44(purple)
- 48 -> combined:76(red); evening:38(blue); midday:40(blue)
- 49 -> combined:70(red); evening:35(purple); midday:44(blue)
- 57 -> combined:71(red); evening:50(blue); midday:35(purple)
- 69 -> combined:87(red); evening:48(blue); midday:43(blue)
- 78 -> combined:72(red); evening:36(purple); midday:70(red)
- 88 -> combined:26(purple); midday:52(purple)
- 99 -> combined:70(purple); evening:35(purple); midday:92(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.173428571428571)[R1,XVAR-Cons(CEM)], 5(2.679957142857143)[R3,XVAR-Cons(CM)], 6(2.6632285714285713)[R2,XVAR-Cons(CE)], 9(1.0252999999999999)[R2,Double-Pressure], 3(0.24466428571428572)[R3,Swap]
- P2: 8(3.286142857142857)[R1,XVAR-Cons(CM)], 4(2.747242857142857)[R2,XVAR-Cons(CE)], 1(2.480785714285714)[R3,XVAR-Cons(CE)], 0(1.5611071428571428)[R1,Mirror-Echo], 9(1.2632142857142856)[R1,Mirror-Echo]
- P3: 4(4.503357142857142)[R1,XVAR-Cons(CM)], 9(1.3924142857142856)[R2,Mirror-Echo], 0(1.2971428571428572)[R1,Double-Pressure], 3(0.9339999999999999)[R2,Double-Pressure], 2(0.8926)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-02.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=38), P2:8(gap=12), P3:4(gap=24); top cartesian candidates: 744, 784, 714, 704, 794.
- Q3: Blackapple: score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 014, 024, 034, 045, 046.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:695(B),evening:896(B); 445→combined:771(B),evening:691(B); 459→combined:680(B),midday:856(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:405, 32:172, 25:158, 29:131, 4:129.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=533 Evening=181; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 335 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 118 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 533 (canon 335): box `335` covers winner `533` (boxed hit).
  - Evening winner 181 (canon 118): box `118` covers winner `181` (boxed hit).
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
