# Master Validation Run Report — NorthCarolina4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/NorthCarolina4/`
- Winners lens: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2025-12-30/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2025-12-30/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2025-12-30/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2025-12-30/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2025-12-30/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-12-30/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac30_winner_879_20260105_051207.html`
- `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac5_winner_455_20260105_051206.html`

Winners JSON files:
- `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac30_winner_879_20260105_051207.json`
- `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac5_winner_455_20260105_051206.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 455 (canon 455): exact_boxed=True exact_straight=True | rank 1459/5714 (rank_frac 0.255); Evening 879 (canon 789): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 879 idx30 (rank 33/35, frac 0.943), 455 idx5 (rank 6/35, frac 0.171)
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

### 2.Stable — NorthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2025-12-30)

## Midday winner 455 (canonical 455)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=11 | family_rows=286 | exact_boxed=11 | exact_straight=5 | vt_boxed=11
- Scores (patterns_scores.csv): rank 1459/5714 (rank_frac 0.2553377668883444) | score 16.5 (top 39.5, ratio 0.4177215189873418, delta 23.0) | section Evening, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 0.0 | why boxed|cov2|hp_repeat3|hot2|perm2|hidden3v|double_mirror|draw_chain3
- Compound (patterns_compound.csv): rank 150/1764 (rank_frac 0.08503401360544217) | score 30.5 (top 112.0, ratio 0.27232142857142855, delta 81.5) | section Evening, col1_hits 3, hot2 2, set_chain 1, draw_chain 4 | why draw_chain4|col1x3|hot1x1|hot2x2|vstrx1|dblmirrorx7
- Families (patterns_families.csv): count 84 | rank 21/1463 (rank_frac 0.014354066985645933) | score 32.5 (top 36.5, ratio 0.8904109589041096, delta 4.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=27

## Evening winner 879 (canonical 789)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=280 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 55 | rank 205/1463 (rank_frac 0.14012303485987695) | score 23.5 (top 36.5, ratio 0.6438356164383562, delta 13.0) | section Combined, hot2 3
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=57
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 003 | section Combined | score 101.0 | col1_hits 7 | hot2 11
- rank    3 | canon 004 | section Combined | score 95.0 | col1_hits 8 | hot2 11
- rank    7 | canon 0034 | section Combined | score 75.0 | col1_hits 7 | hot2 11
- rank   18 | canon 034 | section Combined | score 66.0 | col1_hits 5 | hot2 11
- rank    1 | canon 224 | section Midday | score 112.0 | col1_hits 9 | hot2 11
- rank    4 | canon 005 | section Evening | score 89.5 | col1_hits 9 | hot2 11
- rank    9 | canon 0055 | section Evening | score 70.5 | col1_hits 7 | hot2 11
- rank    6 | canon 055 | section Evening | score 77.5 | col1_hits 7 | hot2 11
- rank   28 | canon 0344 | section Combined | score 58.0 | col1_hits 4 | hot2 8
- rank   23 | canon 0044 | section Combined | score 60.0 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1415 | family 29 | score 6.5 | hot2 0 | section Midday
- rank  245 | family 12 | score 22.5 | hot2 0 | section Midday
- rank  583 | family 2 | score 17.5 | hot2 0 | section Midday
- rank  472 | family 27 | score 18.5 | hot2 0 | section Midday
- rank  472 | family 30 | score 18.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 455 (canon 455): exact_boxed=True exact_straight=True | rank 1459/5714 (rank_frac 0.255); Evening 879 (canon 789): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — NorthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260105)

## Midday winner 455 (canonical 455)
- Stamp (winner_stamp.json): items_total=256 | exact_any=0 exact_final=0 | vtrac_any=214 vtrac_final=0 | drop_exact_any=4 drop_exact_final=0 | drop_vtrac_any=131 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=56 family_vtrac_final=0
- Flags (winner_flags.csv): rows=256 | exact_any=0 vtrac_any=214 | drop_exact_any=4 drop_vtrac_any=131 | family_exact_any=0 family_vtrac_any=56 | vt_boxed=122 vt_straight=0
- Hits (winner_hits.csv): rows=256 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=122 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 879 (canonical 789)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 455 (canonical 455)
- Stamp (winner_stamp.json): items_total=766 | exact_any=79 exact_final=0 | vtrac_any=710 vtrac_final=54 | drop_exact_any=93 drop_exact_final=0 | drop_vtrac_any=563 drop_vtrac_final=32 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=389 family_vtrac_final=22
- Flags (winner_flags.csv): rows=766 | exact_any=79 vtrac_any=710 | drop_exact_any=93 drop_vtrac_any=563 | family_exact_any=0 family_vtrac_any=389 | vt_boxed=323 vt_straight=22
- Hits (winner_hits.csv): rows=766 | exact_final=0 vtrac_final=54 | drop_exact_final=0 drop_vtrac_final=32 | family_exact_final=0 family_vtrac_final=22 | vt_boxed=323 vt_straight=22
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=True | winner_best_rank=15 | winner_rank_fraction=0.6818181818181818 | winner_score_v2=12.365714 top_score_v2=16.977143 | winner_score_ratio_to_top=0.7283742617942253 winner_score_delta_from_top=4.611429000000001
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 400 | score_v2 16.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 400 | score_v2 16.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 440 | score_v2 15.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 550 | score_v2 14.577143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 550 | score_v2 14.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 540 | score_v2 14.327143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 550 | score_v2 14.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 540 | score_v2 14.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 550 | score_v2 14.027143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 550 | score_v2 13.977143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 400 | score_v2 16.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 440 | score_v2 15.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 550 | score_v2 14.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 540 | score_v2 14.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 224 | score_v2 13.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 522 | score_v2 13.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 400 | score_v2 13.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 544 | score_v2 13.487143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 592 | score_v2 13.447143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 224 | score_v2 13.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 455 (canon 455): items_total=256 exact_any=0 vtrac_any=214 | top winner_present=False best_rank=None/12; Evening 879 (canon 789): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/16; Combined 455 (canon 455): items_total=766 exact_any=79 vtrac_any=710 | top winner_present=True best_rank=15/22
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 400, 440, 550, 540, 224.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260105_051503)

## Top indices (from enhanced JSON)
- index 10 | score 71.93827499999996 | features: presence=43.00077499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 1 | score 68.19545999999995 | features: presence=48.467959999999955, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 49.35287500000001 | features: presence=31.465375000000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 28 | score 46.43637499999999 | features: presence=32.73887499999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 41.18343000000001 | features: presence=26.165930000000007, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 36.559267500000004 | features: presence=23.841767500000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 30.015475 | features: presence=19.907975, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 28.942300000000003 | features: presence=13.794800000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 14 | score 27.877660000000002 | features: presence=18.74016, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 24.03065000000001 | features: presence=15.573150000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
034, 240, 501, 105, 506, 015, 605, 250, 204, 052

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 879 | index 30 | file NorthCarolina4_vtrac30_winner_879_20260105_051207.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 455 | index 5 | file NorthCarolina4_vtrac5_winner_455_20260105_051206.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 879 | index 30 rank 33/35 (rank_frac 0.9428571428571428) | score 0.0 (top 71.93827499999996, ratio 0.0, delta 71.93827499999996) | winner_in_index_straights=False | top_index_straights: (none)
- winner 455 | index 5 rank 6/35 (rank_frac 0.17142857142857143) | score 36.559267500000004 (top 71.93827499999996, ratio 0.5082032826058176, delta 35.37900749999996) | winner_in_index_straights=False | top_index_straights: 540 (8.724), 504 (7.77), 045 (6.817)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 879→idx30 rank 33/35 (frac 0.943); 455→idx5 rank 6/35 (frac 0.171).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 10, 1, 2, 28, 4.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2025-12-30)

## Midday winner 455 (canonical 455)
- Top lanes (hot_zones_top_lanes.csv): present | rank 191/206 (rank_frac 0.9271844660194175) | score_mean 14.777 (top 22.387, ratio 0.6600705766739625, delta 7.610000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 879 (canonical 789)
- Top lanes (hot_zones_top_lanes.csv): present | rank 95/206 (rank_frac 0.46116504854368934) | score_mean 16.909 (top 22.387, ratio 0.7553044177424397, delta 5.4780000000000015)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 119 | vt_triad 25 | score_mean 22.387 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vertical5,vt_straight
- rank    2 | triad 667 | vt_triad 23 | score_mean 22.312 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_straight
- rank    3 | triad 469 | vt_triad 255 | score_mean 22.137 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    5 | triad 588 | vt_triad 14 | score_mean 21.414 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 114 | vt_triad 25 | score_mean 21.25 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    7 | triad 669 | vt_triad 25 | score_mean 20.95 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vt_only_lane,vt_straight
- rank    8 | triad 011 | vt_triad 12 | score_mean 20.812 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 168 | vt_triad 224 | score_mean 20.787 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank   10 | triad 226 | vt_triad 23 | score_mean 20.197 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 455 (canon 455): rank 191/206 (rank_frac 0.927) ratio_to_top=0.6600705766739625; Evening 879 (canon 789): rank 95/206 (rank_frac 0.461) ratio_to_top=0.7553044177424397
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

Aux draws snapshot dir: `sharepacks/2025-12-30/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=168, 766, 911, 885, 391
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=766, 885, 789, 157, 673
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=168, 911, 391, 226, 964

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=21 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=38), P2:4 (gap=27), P3:2 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=882 sev=B
- 155: ds=870 sev=B
- 446: ds=866 sev=B
- 445: ds=806 sev=B
- 122: ds=789 sev=B
- 036: ds=785 sev=B
- 555: ds=762 sev=B
- 299: ds=759 sev=B
- 277: ds=751 sev=B
- 112: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=146 sev=red
  - 77: ds=119 sev=red
  - 55: ds=101 sev=blue
  - 33: ds=43 sev=purple
  - 99: ds=42 sev=purple
  - 44: ds=40 sev=purple
  - 22: ds=6 sev=-
  - 88: ds=3 sev=-
  - 11: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 45: ds=109 sev=red
  - 56: ds=48 sev=blue
  - 27: ds=44 sev=blue
  - 02: ds=38 sev=blue
  - 23: ds=34 sev=purple
  - 09: ds=33 sev=purple
  - 03: ds=32 sev=purple
  - 28: ds=30 sev=purple
  - 04: ds=27 sev=purple
  - 06: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:474, 32:327, 1:101, 27:97, 31:88, 15:72, 16:70, 10:60, 4:50, 23:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=474 fs=3 fl=0 hz=0.009389671361502348, 32:ds=327 fs=1 fl=1 hz=0.005405405405405406, 1:ds=101 fs=0 fl=3 hz=0.00625, 27:ds=97 fs=15 fl=2 hz=0.02011173184357542, 31:ds=88 fs=19 fl=3 hz=0.02502844141069397, 15:ds=72 fs=16 fl=2 hz=0.019758507135016465, 16:ds=70 fs=4 fl=1 hz=0.008836524300441826, 10:ds=60 fs=21 fl=2 hz=0.027315914489311165, 4:ds=50 fs=18 fl=2 hz=0.0213903743315508, 23:ds=49 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=82 flags=purple
- S23: ds=66 flags=blue+purple
- S4: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 059: score=4 tags=FLT,MIR,RS
  - 149: score=4 tags=FLT,MIR,RS
  - 257: score=4 tags=FLT,MIR,RS
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 167: score=3 tags=MIR,RS
  - 239: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=93 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=32), P2:9 (gap=22), P3:2 (gap=35)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=970 sev=B
- 123: ds=945 sev=B
- 446: ds=922 sev=B
- 777: ds=882 sev=B
- 119: ds=847 sev=B
- 222: ds=817 sev=B
- 155: ds=779 sev=B
- 488: ds=773 sev=B
- 177: ds=749 sev=B
- 007: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=152 sev=red
  - 00: ds=127 sev=red
  - 77: ds=59 sev=purple
  - 55: ds=50 sev=purple
  - 99: ds=47 sev=purple
  - 22: ds=35 sev=purple
  - 33: ds=21 sev=-
  - 11: ds=5 sev=-
  - 88: ds=1 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 48: ds=143 sev=red
  - 68: ds=71 sev=red
  - 25: ds=56 sev=red
  - 45: ds=54 sev=blue
  - 07: ds=51 sev=blue
  - 28: ds=43 sev=blue
  - 23: ds=38 sev=blue
  - 26: ds=38 sev=blue
  - 02: ds=35 sev=purple
  - 29: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:375, 25:183, 32:163, 35:137, 4:127, 11:102, 31:95, 2:91, 33:74, 12:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=375 fs=1 fl=0 hz=0.005905511811023622, 25:ds=183 fs=15 fl=1 hz=0.02165087956698241, 32:ds=163 fs=3 fl=1 hz=0.007416563658838071, 35:ds=137 fs=0 fl=2 hz=0.005201560468140442, 4:ds=127 fs=12 fl=3 hz=0.017241379310344827, 11:ds=102 fs=50 fl=0 hz=0.056882821387940846, 31:ds=95 fs=25 fl=0 hz=0.02793296089385475, 2:ds=91 fs=13 fl=3 hz=0.018223234624145785, 33:ds=74 fs=21 fl=2 hz=0.025136612021857924, 12:ds=52 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=86 flags=purple
- S20: ds=74 flags=red+purple
- S2: ds=65 flags=purple
- S5: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4'], 'pairs': {'remaining_count': 1}}
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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=17 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=25), P2:4 (gap=32), P3:3 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=971 sev=B
- 299: ds=928 sev=B
- 223: ds=858 sev=B
- 122: ds=847 sev=B
- 116: ds=824 sev=B
- 039: ds=807 sev=B
- 377: ds=795 sev=B
- 277: ds=781 sev=B
- 188: ds=769 sev=B
- 557: ds=768 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=176 sev=red
  - 55: ds=119 sev=red
  - 33: ds=118 sev=red
  - 77: ds=77 sev=blue
  - 00: ds=73 sev=blue
  - 66: ds=35 sev=purple
  - 99: ds=21 sev=-
  - 44: ds=20 sev=-
  - 22: ds=3 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 45: ds=96 sev=red
  - 79: ds=44 sev=blue
  - 34: ds=37 sev=blue
  - 59: ds=36 sev=purple
  - 04: ds=32 sev=purple
  - 06: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 58: ds=25 sev=purple
  - 56: ds=24 sev=-
  - 17: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:255, 26:237, 13:202, 32:176, 1:144, 23:113, 5:94, 17:93, 27:50, 31:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=255 fs=18 fl=0 hz=0.024896265560165977, 26:ds=237 fs=1 fl=2 hz=0.006666666666666667, 13:ds=202 fs=20 fl=0 hz=0.025284450063211127, 32:ds=176 fs=2 fl=2 hz=0.007416563658838071, 1:ds=144 fs=2 fl=3 hz=0.007434944237918215, 23:ds=113 fs=14 fl=3 hz=0.019384264538198404, 5:ds=94 fs=15 fl=2 hz=0.020809248554913295, 17:ds=93 fs=29 fl=0 hz=0.03553921568627451, 27:ds=50 fs=22 fl=3 hz=0.027085590465872156, 31:ds=44 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=87 flags=purple
- S0: ds=73 flags=blue+purple
- S4: ds=62 flags=blue+purple
- S22: ds=42 flags=purple
- S2: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=4 tags=FLT,MIR,RS
  - 025: score=4 tags=FLT,MIR,RS
  - 034: score=4 tags=FLT,PAT,RS
  - 358: score=4 tags=FLT,MIR,RS
  - 079: score=3 tags=FLT,RS
  - 124: score=3 tags=PAT,RS
  - 169: score=3 tags=MIR,RS
  - 178: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 349: score=3 tags=MIR,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:785(B); evening:721(B)
- 122 -> combined:789(B); evening:847(B)
- 155 -> combined:870(B); midday:779(B)
- 277 -> combined:751(B); evening:781(B)
- 299 -> combined:759(B); evening:928(B)
- 338 -> combined:882(B); midday:708(B)
- 446 -> combined:866(B); midday:922(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:146(red); evening:73(blue); midday:127(red)
- 02 -> combined:38(blue); midday:35(purple)
- 04 -> combined:27(purple); evening:32(purple)
- 06 -> combined:27(purple); evening:26(purple)
- 23 -> combined:34(purple); midday:38(blue)
- 28 -> combined:30(purple); midday:43(blue)
- 33 -> combined:43(purple); evening:118(red)
- 34 -> combined:25(purple); evening:37(blue)
- 44 -> combined:40(purple); midday:152(red)
- 45 -> combined:109(red); evening:96(red); midday:54(blue)
- 55 -> combined:101(blue); evening:119(red); midday:50(purple)
- 56 -> combined:48(blue); midday:26(purple)
- 77 -> combined:119(red); evening:77(blue); midday:59(purple)
- 99 -> combined:42(purple); midday:47(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.24407857142857)[R1,Mirror-Echo], 5(3.382292857142857)[R2,Mirror-Echo], 2(1.5554285714285714)[R1,Double-Pressure], 8(1.4164285714285714)[R1,Double-Pressure], 3(0.38215)[R3,Swap]
- P2: 4(8.274271428571428)[R1,XVAR-Cons(CEM)], 0(3.651464285714286)[R2,XVAR-Cons(CE)], 9(1.4503571428571427)[R1,Mirror-Echo], 5(0.45842142857142854)[R3,Mirror-Echo], 3(0.3262857142857143)[R3,Swap]
- P3: 2(7.260514285714287)[R1,XVAR-Cons(CEM)], 3(2.843857142857143)[R3,XVAR-Cons(CE)], 0(2.6706642857142855)[R2,XVAR-Cons(CM)], 8(1.0461999999999998)[R2,Double-Pressure], 5(1.0252999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:0(gap=38), P2:4(gap=27), P3:2(gap=24); top cartesian candidates: 042, 040, 043, 002, 542.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4'], 'pairs': {'remaining_count': 1}}; top candidates: 059, 149, 257, 014, 023.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:785(B),evening:721(B); 122→combined:789(B),evening:847(B); 155→combined:870(B),midday:779(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:474, 32:327, 1:101, 27:97, 31:88.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=455 Evening=879; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 455 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 789 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 455 (canon 455): box `455` covers winner `455` (boxed hit).
  - Evening winner 879 (canon 789): box `789` covers winner `879` (boxed hit).
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
