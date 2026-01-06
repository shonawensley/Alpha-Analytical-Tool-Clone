# Master Validation Run Report — NorthCarolina4 — results 2026-01-04 (history workbook ~ 2026-01-03)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-04/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-04/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-04/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-04/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-04/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-04/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-04/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_187_20260105_055142.html`
- `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac29_winner_887_20260105_055144.html`

Winners JSON files:
- `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac21_winner_187_20260105_055142.json`
- `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac29_winner_887_20260105_055144.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-04/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 187 (canon 178): exact_boxed=True exact_straight=True | rank 1173/5808 (rank_frac 0.202); Evening 887 (canon 788): exact_boxed=None exact_straight=None | rank 1970/5808 (rank_frac 0.339)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 187 idx21 (rank 29/35, frac 0.829), 887 idx29 (rank 11/35, frac 0.314)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
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

### 2.Stable — NorthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-04)

## Midday winner 187 (canonical 178)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=216 | exact_boxed=12 | exact_straight=9 | vt_boxed=12
- Scores (patterns_scores.csv): rank 1173/5808 (rank_frac 0.20196280991735538) | score 17.5 (top 42.5, ratio 0.4117647058823529, delta 25.0) | section Combined, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|vtrac_straight|set_chain2|draw_chain2
- Compound (patterns_compound.csv): rank 130/1783 (rank_frac 0.07291082445316882) | score 30.0 (top 99.5, ratio 0.3015075376884422, delta 69.5) | section Combined, col1_hits 2, hot2 2, set_chain 2, draw_chain 2 | why set_chain2|draw_chain2|col1x2|hot1x1|hot2x2|vstrx5
- Families (patterns_families.csv): count 43 | rank 566/1558 (rank_frac 0.3632862644415918) | score 18.5 (top 39.5, ratio 0.46835443037974683, delta 21.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=69

## Evening winner 887 (canonical 788)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=476 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 1970/5808 (rank_frac 0.3391873278236915) | score 15.0 (top 42.5, ratio 0.35294117647058826, delta 27.5) | section Evening, Set Set2, Draw Draw1, Col 5, hot 0, vt_straight 0.0 | why straight|cov2|hp_repeat3|vstr2|double_mirror|set_chain2
- Compound (patterns_compound.csv): rank 323/1783 (rank_frac 0.18115535614133482) | score 21.0 (top 99.5, ratio 0.21105527638190955, delta 78.5) | section Evening, col1_hits 0, hot2 0, set_chain 2, draw_chain 2 | why set_chain2|draw_chain2|dblmirrorx6
- Families (patterns_families.csv): count 87 | rank 104/1558 (rank_frac 0.06675224646983312) | score 26.5 (top 39.5, ratio 0.6708860759493671, delta 13.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 229 | section Midday | score 99.5 | col1_hits 9 | hot2 11
- rank    3 | canon 0229 | section Midday | score 91.5 | col1_hits 8 | hot2 11
- rank    1 | canon 229 | section Combined | score 99.5 | col1_hits 8 | hot2 11
- rank    6 | canon 022 | section Midday | score 77.5 | col1_hits 8 | hot2 10
- rank   31 | canon 019 | section Midday | score 53.0 | col1_hits 5 | hot2 7
- rank   10 | canon 029 | section Midday | score 70.0 | col1_hits 5 | hot2 7
- rank    8 | canon 009 | section Midday | score 72.5 | col1_hits 2 | hot2 6
- rank   22 | canon 226 | section Evening | score 57.5 | col1_hits 5 | hot2 6
- rank   53 | canon 1224 | section Combined | score 44.0 | col1_hits 4 | hot2 6
- rank   35 | canon 2246 | section Evening | score 50.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1393 | family 24 | score 9.5 | hot2 0 | section Midday
- rank  314 | family 12 | score 21.5 | hot2 0 | section Midday
- rank  237 | family 2 | score 23.0 | hot2 0 | section Midday
- rank  175 | family 27 | score 24.5 | hot2 0 | section Midday
- rank  145 | family 5 | score 25.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 187 (canon 178): exact_boxed=True exact_straight=True | rank 1173/5808 (rank_frac 0.202); Evening 887 (canon 788): exact_boxed=None exact_straight=None | rank 1970/5808 (rank_frac 0.339)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260105)

## Midday winner 187 (canonical 178)
- Stamp (winner_stamp.json): items_total=43 | exact_any=24 exact_final=0 | vtrac_any=43 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=43 | exact_any=24 vtrac_any=43 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=43 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=19.227143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 887 (canonical 788)
- Stamp (winner_stamp.json): items_total=98 | exact_any=60 exact_final=0 | vtrac_any=98 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=98 | exact_any=60 vtrac_any=98 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=98 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=16.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 187 (canonical 178)
- Stamp (winner_stamp.json): items_total=199 | exact_any=24 exact_final=0 | vtrac_any=199 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=199 | exact_any=24 vtrac_any=199 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=199 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=19.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 922 | score_v2 19.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 922 | score_v2 19.277143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 922 | score_v2 19.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 922 | score_v2 19.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 922 | score_v2 18.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 922 | score_v2 18.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 992 | score_v2 18.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 992 | score_v2 18.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 992 | score_v2 18.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 922 | score_v2 18.327143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 922 | score_v2 19.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 922 | score_v2 19.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 992 | score_v2 18.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 992 | score_v2 17.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 922 | score_v2 16.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 922 | score_v2 15.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 599 | score_v2 15.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 592 | score_v2 15.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 992 | score_v2 14.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 992 | score_v2 14.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 187 (canon 178): items_total=43 exact_any=24 vtrac_any=43 | top winner_present=False best_rank=None/10; Evening 887 (canon 788): items_total=98 exact_any=60 vtrac_any=98 | top winner_present=False best_rank=None/28; Combined 187 (canon 178): items_total=199 exact_any=24 vtrac_any=199 | top winner_present=False best_rank=None/10
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 922, 922, 992, 992, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260105_055539)

## Top indices (from enhanced JSON)
- index 28 | score 93.44959999999999 | features: presence=69.4921, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 64.30907499999998 | features: presence=37.96157499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 39.34616249999999 | features: presence=23.468662499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 36.795249999999996 | features: presence=22.24775, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 31.89458 | features: presence=17.63708, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 31.836875000000003 | features: presence=17.329375000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 30.901055 | features: presence=16.573555, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 1 | score 29.703799999999998 | features: presence=17.716299999999997, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 12 | score 28.296729999999997 | features: presence=19.52923, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 24.943625 | features: presence=12.986125000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
093, 503, 035, 290, 932, 053, 092, 903, 590, 059

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 187 | index 21 | file NorthCarolina4_vtrac21_winner_187_20260105_055142.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 887 | index 29 | file NorthCarolina4_vtrac29_winner_887_20260105_055144.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 187 | index 21 rank 29/35 (rank_frac 0.8285714285714286) | score 0.0 (top 93.44959999999999, ratio 0.0, delta 93.44959999999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 887 | index 29 rank 11/35 (rank_frac 0.3142857142857143) | score 23.21695 (top 93.44959999999999, ratio 0.24844354603979046, delta 70.23264999999999) | winner_in_index_straights=False | top_index_straights: 837 (5.764), 387 (5.145), 832 (4.45)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 187→idx21 rank 29/35 (frac 0.829); 887→idx29 rank 11/35 (frac 0.314).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 4, 27, 5, 14.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-04)

## Midday winner 187 (canonical 178)
- Top lanes (hot_zones_top_lanes.csv): present | rank 35/206 (rank_frac 0.16990291262135923) | score_mean 17.924 (top 21.558, ratio 0.8314314871509416, delta 3.6340000000000003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 887 (canonical 788)
- Top lanes (hot_zones_top_lanes.csv): present | rank 79/206 (rank_frac 0.38349514563106796) | score_mean 16.67 (top 21.558, ratio 0.7732628258651082, delta 4.887999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 338 | vt_triad 44 | score_mean 21.558 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 035 | vt_triad 114 | score_mean 20.398 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 057 | vt_triad 113 | score_mean 20.357 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 033 | vt_triad 14 | score_mean 20.33 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 347 | vt_triad 345 | score_mean 20.29 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 229 | vt_triad 35 | score_mean 19.768 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 001 | vt_triad 12 | score_mean 19.69 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 224 | vt_triad 35 | score_mean 19.422 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank    9 | triad 667 | vt_triad 23 | score_mean 19.306 | tags funnel_precol1,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 003 | vt_triad 14 | score_mean 19.179 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 187 (canon 178): rank 35/206 (rank_frac 0.170) ratio_to_top=0.8314314871509416; Evening 887 (canon 788): rank 79/206 (rank_frac 0.383) ratio_to_top=0.7732628258651082
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

Aux draws snapshot dir: `sharepacks/2026-01-04/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=178, 374, 383, 033, 053
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=374, 033, 416, 867, 455
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=178, 383, 053, 057, 879

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=31 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=32), P2:4 (gap=37), P3:2 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=880 sev=B
- 446: ds=876 sev=B
- 445: ds=816 sev=B
- 122: ds=799 sev=B
- 036: ds=795 sev=B
- 555: ds=772 sev=B
- 299: ds=769 sev=B
- 277: ds=761 sev=B
- 112: ds=750 sev=B
- 034: ds=684 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=156 sev=red
  - 77: ds=129 sev=red
  - 99: ds=52 sev=purple
  - 44: ds=50 sev=purple
  - 22: ds=16 sev=-
  - 88: ds=13 sev=-
  - 11: ds=12 sev=-
  - 66: ds=11 sev=-
  - 55: ds=9 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 56: ds=58 sev=red
  - 27: ds=54 sev=blue
  - 02: ds=48 sev=blue
  - 23: ds=44 sev=blue
  - 09: ds=43 sev=blue
  - 28: ds=40 sev=blue
  - 04: ds=37 sev=blue
  - 06: ds=37 sev=blue
  - 29: ds=34 sev=purple
  - 24: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:484, 1:111, 27:107, 31:98, 15:82, 16:80, 10:70, 23:59, 35:50, 12:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=484 fs=3 fl=0 hz=0.009389671361502348, 1:ds=111 fs=0 fl=3 hz=0.00625, 27:ds=107 fs=15 fl=2 hz=0.02463768115942029, 31:ds=98 fs=19 fl=3 hz=0.02502844141069397, 15:ds=82 fs=16 fl=2 hz=0.019758507135016465, 16:ds=80 fs=4 fl=1 hz=0.008836524300441826, 10:ds=70 fs=21 fl=2 hz=0.027315914489311165, 23:ds=59 fs=17 fl=3 hz=0.024330900243309, 35:ds=50 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=48 fs=46 fl=1 hz=0.049893842887473464

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=92 flags=purple
- S23: ds=76 flags=blue+purple
- S4: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=98 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=37), P2:9 (gap=27), P3:2 (gap=40)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=975 sev=B
- 123: ds=950 sev=B
- 446: ds=927 sev=B
- 777: ds=887 sev=B
- 119: ds=852 sev=B
- 222: ds=822 sev=B
- 155: ds=784 sev=B
- 488: ds=778 sev=B
- 177: ds=754 sev=B
- 007: ds=733 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=157 sev=red
  - 00: ds=132 sev=red
  - 77: ds=64 sev=purple
  - 99: ds=52 sev=purple
  - 22: ds=40 sev=purple
  - 11: ds=10 sev=-
  - 88: ds=6 sev=-
  - 66: ds=5 sev=-
  - 55: ds=4 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 48: ds=148 sev=red
  - 25: ds=61 sev=red
  - 07: ds=56 sev=red
  - 28: ds=48 sev=blue
  - 23: ds=43 sev=blue
  - 26: ds=43 sev=blue
  - 02: ds=40 sev=blue
  - 29: ds=37 sev=blue
  - 56: ds=31 sev=purple
  - 27: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:380, 25:188, 32:168, 35:142, 4:132, 11:107, 31:100, 2:96, 33:79, 12:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=380 fs=1 fl=0 hz=0.005905511811023622, 25:ds=188 fs=15 fl=1 hz=0.02165087956698241, 32:ds=168 fs=3 fl=1 hz=0.007416563658838071, 35:ds=142 fs=0 fl=2 hz=0.005201560468140442, 4:ds=132 fs=11 fl=3 hz=0.0166073546856465, 11:ds=107 fs=50 fl=0 hz=0.056882821387940846, 31:ds=100 fs=25 fl=0 hz=0.02793296089385475, 2:ds=96 fs=13 fl=3 hz=0.018223234624145785, 33:ds=79 fs=21 fl=2 hz=0.025136612021857924, 12:ds=57 fs=47 fl=0 hz=0.05181918412348401

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=91 flags=purple
- S20: ds=79 flags=red+purple
- S2: ds=70 flags=purple
- S5: ds=66 flags=purple
- S8: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=22 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=16), P2:4 (gap=37), P3:5 (gap=22)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=976 sev=B
- 299: ds=933 sev=B
- 223: ds=863 sev=B
- 122: ds=852 sev=B
- 116: ds=829 sev=B
- 039: ds=812 sev=B
- 377: ds=800 sev=B
- 277: ds=786 sev=B
- 188: ds=774 sev=B
- 557: ds=773 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=181 sev=red
  - 55: ds=124 sev=red
  - 77: ds=82 sev=blue
  - 00: ds=78 sev=blue
  - 66: ds=40 sev=purple
  - 99: ds=26 sev=purple
  - 44: ds=25 sev=purple
  - 22: ds=8 sev=-
  - 11: ds=6 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 45: ds=101 sev=red
  - 34: ds=42 sev=blue
  - 59: ds=41 sev=blue
  - 04: ds=37 sev=blue
  - 06: ds=31 sev=purple
  - 08: ds=30 sev=purple
  - 58: ds=30 sev=purple
  - 56: ds=29 sev=purple
  - 27: ds=27 sev=purple
  - 02: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:260, 26:242, 13:207, 1:149, 23:118, 5:99, 17:98, 27:55, 31:49, 14:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=260 fs=18 fl=0 hz=0.024896265560165977, 26:ds=242 fs=1 fl=2 hz=0.006666666666666667, 13:ds=207 fs=20 fl=0 hz=0.025284450063211127, 1:ds=149 fs=2 fl=3 hz=0.007434944237918215, 23:ds=118 fs=14 fl=3 hz=0.019384264538198404, 5:ds=99 fs=15 fl=2 hz=0.020809248554913295, 17:ds=98 fs=29 fl=0 hz=0.03553921568627451, 27:ds=55 fs=22 fl=3 hz=0.027085590465872156, 31:ds=49 fs=21 fl=2 hz=0.024338624338624337, 14:ds=47 fs=41 fl=1 hz=0.0445859872611465

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=92 flags=purple
- S0: ds=78 flags=blue+purple
- S4: ds=67 flags=blue+purple
- S22: ds=47 flags=purple
- S2: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:795(B); evening:726(B)
- 122 -> combined:799(B); evening:852(B)
- 155 -> combined:880(B); midday:784(B)
- 277 -> combined:761(B); evening:786(B)
- 299 -> combined:769(B); evening:933(B)
- 446 -> combined:876(B); midday:927(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:156(red); evening:78(blue); midday:132(red)
- 02 -> combined:48(blue); midday:40(blue)
- 04 -> combined:37(blue); evening:37(blue)
- 06 -> combined:37(blue); evening:31(purple)
- 08 -> combined:27(purple); evening:30(purple)
- 23 -> combined:44(blue); midday:43(blue)
- 25 -> combined:32(purple); midday:61(red)
- 27 -> combined:54(blue); evening:27(purple); midday:28(purple)
- 28 -> combined:40(blue); midday:48(blue)
- 29 -> combined:34(purple); midday:37(blue)
- 44 -> combined:50(purple); evening:25(purple); midday:157(red)
- 56 -> combined:58(red); evening:29(purple); midday:31(purple)
- 59 -> combined:25(purple); evening:41(blue)
- 77 -> combined:129(red); evening:82(blue); midday:64(purple)
- 99 -> combined:52(purple); evening:26(purple); midday:52(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.811428571428571)[R1,XVAR-Cons(CEM)], 2(3.3712857142857144)[R3,XVAR-Cons(CM)], 7(0.9417)[R2,Double-Pressure], 6(0.4179999999999999)[R2], 4(0.2612285714285714)[R3,Swap]
- P2: 4(8.857628571428572)[R1,XVAR-Cons(CEM)], 0(3.921)[R2,XVAR-Cons(CE)], 2(1.9412571428571428)[R3,XVAR-Cons(CM)], 9(1.647142857142857)[R1,Mirror-Echo], 3(0.24466428571428572)[R3,Swap]
- P3: 2(8.468871428571429)[R1,XVAR-Cons(CEM)], 0(6.144514285714286)[R2,XVAR-Cons(CEM)], 5(1.4123571428571429)[R1,Mirror-Echo], 8(0.5507)[R2,Swap], 1(0.16971428571428573)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-03.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=32), P2:4(gap=37), P3:2(gap=34); top cartesian candidates: 542, 540, 242, 502, 500.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 016, 019, 023, 024.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:795(B),evening:726(B); 122→combined:799(B),evening:852(B); 155→combined:880(B),midday:784(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:484, 1:111, 27:107, 31:98, 15:82.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=187 Evening=887; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 178 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 788 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 187 (canon 178): box `178` covers winner `187` (boxed hit).
  - Evening winner 887 (canon 788): box `788` covers winner `887` (boxed hit).
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
