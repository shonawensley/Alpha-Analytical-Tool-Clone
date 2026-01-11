# Master Validation Run Report — Connecticut4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/Connecticut4/`
- Winners lens: `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-09/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-09/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-09/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-09/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-09/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-09/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_234_20260110_035031.html`
- `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac8_winner_513_20260110_035033.html`

Winners JSON files:
- `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_234_20260110_035031.json`
- `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac8_winner_513_20260110_035033.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 234 (canon 234): exact_boxed=True exact_straight=True | rank 6402/6411 (rank_frac 0.999); Evening 513 (canon 135): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 234 idx30 (rank 5/35, frac 0.143), 513 idx8 (rank 20/35, frac 0.571)
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

### 2.Stable — Connecticut4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-09)

## Midday winner 234 (canonical 234)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=146 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 6402/6411 (rank_frac 0.99859616284511) | score 6.0 (top 39.5, ratio 0.1518987341772152, delta 33.5) | section Evening, Set Set3, Draw Draw1, Col 6, hot 0, vt_straight 0.0 | why straight|cov1
- Compound (patterns_compound.csv): rank 1553/1557 (rank_frac 0.9974309569685292) | score 6.0 (top 112.0, ratio 0.05357142857142857, delta 106.0) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 0 | why nan
- Families (patterns_families.csv): count 33 | rank 601/1396 (rank_frac 0.4305157593123209) | score 19.0 (top 37.5, ratio 0.5066666666666667, delta 18.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=179

## Evening winner 513 (canonical 135)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=1469 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 110 | rank 141/1396 (rank_frac 0.1010028653295129) | score 31.0 (top 37.5, ratio 0.8266666666666667, delta 6.5) | section Evening, hot2 9
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=52
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 224 | section Combined | score 112.0 | col1_hits 9 | hot2 11
- rank    1 | canon 244 | section Combined | score 112.0 | col1_hits 9 | hot2 11
- rank   46 | canon 228899 | section Combined | score 64.5 | col1_hits 6 | hot2 11
- rank   45 | canon 2299 | section Combined | score 65.0 | col1_hits 7 | hot2 11
- rank   44 | canon 2248899 | section Combined | score 65.5 | col1_hits 6 | hot2 11
- rank   40 | canon 224488 | section Combined | score 69.5 | col1_hits 7 | hot2 11
- rank   35 | canon 22448899 | section Combined | score 72.5 | col1_hits 6 | hot2 11
- rank   39 | canon 8899 | section Combined | score 70.0 | col1_hits 7 | hot2 11
- rank   38 | canon 4488 | section Combined | score 71.5 | col1_hits 8 | hot2 11
- rank   35 | canon 2889 | section Combined | score 72.5 | col1_hits 7 | hot2 11

## Top families (patterns_families.csv)
- rank 1329 | family 29 | score 7.5 | hot2 0 | section Midday
- rank  229 | family 31 | score 27.5 | hot2 2 | section Midday
- rank 1021 | family 24 | score 13.0 | hot2 0 | section Midday
- rank 1092 | family 18 | score 12.0 | hot2 0 | section Midday
- rank 1166 | family 20 | score 11.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 234 (canon 234): exact_boxed=True exact_straight=True | rank 6402/6411 (rank_frac 0.999); Evening 513 (canon 135): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260110)

## Midday winner 234 (canonical 234)
- Stamp (winner_stamp.json): items_total=94 | exact_any=0 exact_final=0 | vtrac_any=86 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=81 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=94 | exact_any=0 vtrac_any=86 | drop_exact_any=0 drop_vtrac_any=81 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=94 vt_straight=0
- Hits (winner_hits.csv): rows=94 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=94 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=18.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 513 (canonical 135)
- Stamp (winner_stamp.json): items_total=62 | exact_any=0 exact_final=0 | vtrac_any=62 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=62 | exact_any=0 vtrac_any=62 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=62 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.037143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 234 (canonical 234)
- Stamp (winner_stamp.json): items_total=209 | exact_any=12 exact_final=0 | vtrac_any=201 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=91 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=209 | exact_any=12 vtrac_any=201 | drop_exact_any=0 drop_vtrac_any=91 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=130 vt_straight=0
- Hits (winner_hits.csv): rows=209 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=130 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=19.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 19.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 19.327143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 224 | score_v2 18.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 5 | pattern 224 | score_v2 18.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 224 | score_v2 18.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 224 | score_v2 18.477143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 18.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 17.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 17.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 17.387143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 992 | score_v2 19.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 224 | score_v2 18.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 992 | score_v2 17.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 448 | score_v2 17.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 992 | score_v2 17.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 922 | score_v2 16.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 922 | score_v2 16.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 992 | score_v2 15.887143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 992 | score_v2 15.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 922 | score_v2 15.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 234 (canon 234): items_total=94 exact_any=0 vtrac_any=86 | top winner_present=False best_rank=None/18; Evening 513 (canon 135): items_total=62 exact_any=0 vtrac_any=62 | top winner_present=False best_rank=None/10; Combined 234 (canon 234): items_total=209 exact_any=12 vtrac_any=201 | top winner_present=False best_rank=None/10
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 992, 224, 992, 448, 992.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260110_035254)

## Top indices (from enhanced JSON)
- index 28 | score 181.95200000000008 | features: presence=133.13450000000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 130.155665 | features: presence=94.58816499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 90.30739999999997 | features: presence=69.06989999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 76.87616999999997 | features: presence=55.33866999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 30 | score 66.73809999999997 | features: presence=43.18059999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 33.7598 | features: presence=22.422300000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 22.398850000000003 | features: presence=12.66135, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 14 | score 21.903625000000005 | features: presence=11.696125000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 24 | score 19.143500000000003 | features: presence=10.386000000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 29 | score 16.9266 | features: presence=10.1491, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
984, 298, 892, 982, 248, 834, 438, 932, 983, 893

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 234 | index 30 | file Connecticut4_vtrac30_winner_234_20260110_035031.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 513 | index 8 | file Connecticut4_vtrac8_winner_513_20260110_035033.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 234 | index 30 rank 5/35 (rank_frac 0.14285714285714285) | score 66.73809999999997 (top 181.95200000000008, ratio 0.366789592859655, delta 115.21390000000011) | winner_in_index_straights=False | top_index_straights: 298 (28.233), 892 (25.883), 982 (24.319)
- winner 513 | index 8 rank 20/35 (rank_frac 0.5714285714285714) | score 3.1768750000000003 (top 181.95200000000008, ratio 0.01745996196799155, delta 178.7751250000001) | winner_in_index_straights=False | top_index_straights: 103 (0.44), 013 (0.275), 810 (0.26)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 234→idx30 rank 5/35 (frac 0.143); 513→idx8 rank 20/35 (frac 0.571).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 34, 31, 33, 30.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-09)

## Midday winner 234 (canonical 234)
- Top lanes (hot_zones_top_lanes.csv): present | rank 137/210 (rank_frac 0.6523809523809524) | score_mean 16.979 (top 24.309, ratio 0.6984655888765477, delta 7.330000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 513 (canonical 135)
- Top lanes (hot_zones_top_lanes.csv): present | rank 108/210 (rank_frac 0.5142857142857142) | score_mean 17.747 (top 24.309, ratio 0.7300588259492369, delta 6.562000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 016 | vt_triad 122 | score_mean 24.309 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 156 | vt_triad 122 | score_mean 23.708 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 066 | vt_triad 12 | score_mean 22.953 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 355 | vt_triad 14 | score_mean 22.679 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical5,vt_straight
- rank    5 | triad 017 | vt_triad 123 | score_mean 22.541 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    6 | triad 567 | vt_triad 123 | score_mean 21.681 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    7 | triad 113 | vt_triad 24 | score_mean 21.459 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 117 | vt_triad 23 | score_mean 21.235 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    9 | triad 149 | vt_triad 255 | score_mean 21.2 | tags hot16,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 469 | vt_triad 255 | score_mean 21.2 | tags hot16,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 234 (canon 234): rank 137/210 (rank_frac 0.652) ratio_to_top=0.6984655888765477; Evening 513 (canon 135): rank 108/210 (rank_frac 0.514) ratio_to_top=0.7300588259492369
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

Aux draws snapshot dir: `sharepacks/2026-01-09/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-09/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=331, 106, 553, 156, 737
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-09/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=106, 156, 576, 071, 569
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-09/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=331, 553, 737, 660, 311

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=2 last_repeat_gap=47 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=28), P2:4 (gap=23), P3:4 (gap=36)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=43.518771428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=40.907024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 244: score=40.50610714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=37.422871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 842: score=36.1695 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=34.81112428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 242: score=34.596087857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 294: score=34.41020714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=34.07085 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 848: score=33.31993857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=899 sev=B
- 129: ds=881 sev=B
- 288: ds=869 sev=B
- 149: ds=851 sev=B
- 445: ds=783 sev=B
- 114: ds=753 sev=B
- 069: ds=717 sev=B
- 888: ds=715 sev=B
- 688: ds=711 sev=B
- 459: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=101 sev=blue
  - 99: ds=82 sev=blue
  - 00: ds=52 sev=purple
  - 88: ds=38 sev=purple
  - 22: ds=15 sev=-
  - 11: ds=8 sev=-
  - 66: ds=6 sev=-
  - 77: ds=4 sev=-
  - 55: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 48: ds=88 sev=red
  - 78: ds=84 sev=red
  - 49: ds=82 sev=red
  - 25: ds=51 sev=blue
  - 58: ds=33 sev=purple
  - 68: ds=33 sev=purple
  - 14: ds=31 sev=purple
  - 89: ds=28 sev=purple
  - 34: ds=26 sev=purple
  - 45: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:417, 32:184, 25:170, 29:143, 15:129, 31:118, 34:113, 3:98, 35:82, 2:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=417 fs=1 fl=2 hz=0.01098901098901099, 32:ds=184 fs=5 fl=2 hz=0.011267605633802818, 25:ds=170 fs=22 fl=2 hz=0.029055690072639227, 29:ds=143 fs=24 fl=1 hz=0.03071253071253071, 15:ds=129 fs=9 fl=4 hz=0.015531660692951015, 31:ds=118 fs=32 fl=0 hz=0.03665521191294387, 34:ds=113 fs=15 fl=2 hz=0.01951779563719862, 3:ds=98 fs=27 fl=0 hz=0.030337078651685393, 35:ds=82 fs=13 fl=4 hz=0.018743109151047408, 2:ds=71 fs=21 fl=3 hz=0.026344676180021953

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=92 flags=purple
- S24: ds=84 flags=blue+purple
- S22: ds=82 flags=purple
- S25: ds=74 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=6 streak=2 max=3 last_repeat_gap=1 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=33), P2:8 (gap=16), P3:4 (gap=37)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=43.518771428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=40.907024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 244: score=40.50610714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=37.422871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 842: score=36.1695 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=34.81112428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 242: score=34.596087857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 294: score=34.41020714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=34.07085 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 848: score=33.31993857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=886 sev=B
- 478: ds=867 sev=B
- 459: ds=862 sev=B
- 159: ds=818 sev=B
- 099: ds=799 sev=B
- 127: ds=790 sev=B
- 559: ds=732 sev=B
- 004: ds=691 sev=B
- 155: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=98 sev=blue
  - 88: ds=58 sev=purple
  - 44: ds=50 sev=purple
  - 55: ds=35 sev=purple
  - 00: ds=31 sev=purple
  - 66: ds=18 sev=-
  - 77: ds=13 sev=-
  - 11: ds=10 sev=-
  - 22: ds=7 sev=-
  - 33: ds=5 sev=-
- non_repeating:
  - 78: ds=76 sev=red
  - 13: ds=63 sev=red
  - 49: ds=50 sev=blue
  - 19: ds=49 sev=blue
  - 48: ds=46 sev=blue
  - 37: ds=30 sev=purple
  - 08: ds=28 sev=purple
  - 36: ds=26 sev=purple
  - 25: ds=25 sev=purple
  - 03: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:208, 25:109, 31:98, 32:96, 18:93, 3:81, 29:71, 4:70, 15:64, 34:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=208 fs=3 fl=0 hz=0.008565310492505354, 25:ds=109 fs=21 fl=1 hz=0.025974025974025976, 31:ds=98 fs=20 fl=2 hz=0.024608501118568233, 32:ds=96 fs=3 fl=4 hz=0.009510869565217392, 18:ds=93 fs=23 fl=1 hz=0.026519337016574582, 3:ds=81 fs=22 fl=2 hz=0.02631578947368421, 29:ds=71 fs=18 fl=2 hz=0.023446658851113716, 4:ds=70 fs=26 fl=0 hz=0.02931228861330327, 15:ds=64 fs=22 fl=1 hz=0.025136612021857924, 34:ds=56 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=92 flags=blue+purple
- S24: ds=89 flags=purple
- S23: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3', '4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=5 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=23), P2:9 (gap=22), P3:2 (gap=20)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=43.518771428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=40.907024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 244: score=40.50610714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=37.422871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 842: score=36.1695 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=34.81112428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 242: score=34.596087857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 294: score=34.41020714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=34.07085 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 848: score=33.31993857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=913 sev=B
- 668: ds=910 sev=B
- 399: ds=909 sev=B
- 044: ds=905 sev=B
- 145: ds=874 sev=B
- 677: ds=781 sev=B
- 333: ds=776 sev=B
- 112: ds=728 sev=B
- 344: ds=708 sev=B
- 888: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=120 sev=red
  - 22: ds=77 sev=blue
  - 99: ds=41 sev=purple
  - 00: ds=26 sev=purple
  - 88: ds=19 sev=-
  - 11: ds=4 sev=-
  - 66: ds=3 sev=-
  - 77: ds=2 sev=-
  - 55: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 57: ds=56 sev=red
  - 69: ds=54 sev=blue
  - 23: ds=51 sev=blue
  - 25: ds=49 sev=blue
  - 07: ds=48 sev=blue
  - 48: ds=44 sev=blue
  - 78: ds=42 sev=blue
  - 49: ds=41 sev=blue
  - 15: ds=34 sev=purple
  - 02: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:319, 26:147, 34:99, 32:92, 25:85, 29:73, 15:72, 2:62, 31:59, 10:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=319 fs=2 fl=1 hz=0.005961251862891207, 26:ds=147 fs=3 fl=1 hz=0.008680555555555556, 34:ds=99 fs=14 fl=3 hz=0.019144144144144143, 32:ds=92 fs=2 fl=0 hz=0.008450704225352114, 25:ds=85 fs=21 fl=0 hz=0.023836549375709424, 29:ds=73 fs=27 fl=0 hz=0.030100334448160536, 15:ds=72 fs=15 fl=1 hz=0.019698725376593278, 2:ds=62 fs=23 fl=2 hz=0.028344671201814057, 31:ds=59 fs=23 fl=1 hz=0.03296703296703297, 10:ds=56 fs=14 fl=4 hz=0.019823788546255508

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=99 flags=blue+purple
- S8: ds=76 flags=red+purple
- S20: ds=59 flags=purple
- S3: ds=46 flags=blue+purple
- S24: ds=42 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 445 -> combined:783(B); evening:697(B)
- 459 -> combined:692(B); midday:862(B)
- 888 -> combined:715(B); evening:705(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:52(purple); evening:26(purple); midday:31(purple)
- 25 -> combined:51(blue); evening:49(blue); midday:25(purple)
- 44 -> combined:101(blue); evening:120(red); midday:50(purple)
- 48 -> combined:88(red); evening:44(blue); midday:46(blue)
- 49 -> combined:82(red); evening:41(blue); midday:50(blue)
- 78 -> combined:84(red); evening:42(blue); midday:76(red)
- 88 -> combined:38(purple); midday:58(purple)
- 99 -> combined:82(blue); evening:41(purple); midday:98(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(3.8726000000000003)[R1,XVAR-Cons(CE)], 2(1.8599357142857142)[R3,XVAR-Cons(CE)], 7(1.6552857142857142)[R1,Double-Pressure], 9(1.3867142857142856)[R1,Double-Pressure], 4(1.0959999999999999)[R2,Double-Pressure]
- P2: 4(7.859328571428572)[R1,Mirror-Echo], 9(4.263428571428571)[R2,Mirror-Echo], 2(1.9002428571428571)[R3,XVAR-Cons(CE)], 8(1.1777142857142857)[R1,Double-Pressure], 1(0.13435714285714284)[R3]
- P3: 4(7.786842857142856)[R1,XVAR-Cons(CEM)], 2(2.9375714285714283)[R3,XVAR-Cons(CE)], 5(1.8389214285714286)[R2,XVAR-Cons(CM)], 8(1.0971)[R2,Double-Pressure], 7(0.9417)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:8(gap=28), P2:4(gap=23), P3:4(gap=36); top cartesian candidates: 844, 444, 244, 894, 842.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 014, 018, 019, 023.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 445→combined:783(B),evening:697(B); 459→combined:692(B),midday:862(B); 888→combined:715(B),evening:705(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:417, 32:184, 25:170, 29:143, 15:129.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=234 Evening=513; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 234 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 135 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 234 (canon 234): box `234` covers winner `234` (boxed hit).
  - Evening winner 513 (canon 135): box `135` covers winner `513` (boxed hit).
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
