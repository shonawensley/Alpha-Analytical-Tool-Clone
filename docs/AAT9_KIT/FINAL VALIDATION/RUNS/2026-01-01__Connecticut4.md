# Master Validation Run Report — Connecticut4 — results 2026-01-01 (history workbook ~ 2025-12-31)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-01/Connecticut4/`
- Winners lens: `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-01/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-01/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-01/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-01/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-01/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-01/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_228_20260105_053356.html`
- `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_109_20260105_053357.html`

Winners JSON files:
- `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_228_20260105_053356.json`
- `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/Connecticut4_vtrac9_winner_109_20260105_053357.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-01/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 228 (canon 228): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 109 (canon 019): exact_boxed=True exact_straight=True | rank 2733/4723 (rank_frac 0.579)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 228 idx27 (rank 24/35, frac 0.686), 109 idx9 (rank 8/35, frac 0.229)
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

### 2.Stable — Connecticut4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-01)

## Midday winner 228 (canonical 228)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=285 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 62 | rank 130/1227 (rank_frac 0.10594947025264874) | score 21.5 (top 32.0, ratio 0.671875, delta 10.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=6
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 109 (canonical 019)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=25 | exact_boxed=10 | exact_straight=9 | vt_boxed=10
- Scores (patterns_scores.csv): rank 2733/4723 (rank_frac 0.57865763286047) | score 11.5 (top 41.5, ratio 0.27710843373493976, delta 30.0) | section Midday, Set Set3, Draw Draw1, Col 6, hot 0, vt_straight 0.0 | why straight|cov1|hp_repeat2|hidden3v|set_chain3
- Compound (patterns_compound.csv): rank 514/1812 (rank_frac 0.2836644591611479) | score 16.5 (top 80.5, ratio 0.20496894409937888, delta 64.0) | section Evening, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|vstrx2
- Families (patterns_families.csv): count 15 | rank 725/1227 (rank_frac 0.5908720456397718) | score 12.5 (top 32.0, ratio 0.390625, delta 19.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=89

## Top compound candidates (patterns_compound.csv)
- rank   15 | canon 456 | section Midday | score 44.0 | col1_hits 4 | hot2 6
- rank    6 | canon 368 | section Combined | score 50.0 | col1_hits 0 | hot2 5
- rank   21 | canon 346 | section Midday | score 40.5 | col1_hits 2 | hot2 5
- rank    6 | canon 388 | section Combined | score 50.0 | col1_hits 0 | hot2 4
- rank   16 | canon 388 | section Midday | score 43.5 | col1_hits 4 | hot2 4
- rank    5 | canon 368 | section Midday | score 52.5 | col1_hits 4 | hot2 4
- rank   26 | canon 3688 | section Midday | score 37.5 | col1_hits 4 | hot2 4
- rank   20 | canon 688 | section Midday | score 42.5 | col1_hits 4 | hot2 4
- rank   24 | canon 189 | section Evening | score 39.5 | col1_hits 3 | hot2 4
- rank   16 | canon 688 | section Combined | score 43.5 | col1_hits 0 | hot2 4

## Top families (patterns_families.csv)
- rank 1154 | family 1 | score 6.0 | hot2 0 | section Midday
- rank 1096 | family 15 | score 7.5 | hot2 0 | section Midday
- rank  463 | family 8 | score 16.0 | hot2 0 | section Midday
- rank  463 | family 14 | score 16.0 | hot2 0 | section Midday
- rank  546 | family 12 | score 15.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 228 (canon 228): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 109 (canon 019): exact_boxed=True exact_straight=True | rank 2733/4723 (rank_frac 0.579)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260105)

## Midday winner 228 (canonical 228)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=6 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=6 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.308571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 109 (canonical 019)
- Stamp (winner_stamp.json): items_total=183 | exact_any=0 exact_final=0 | vtrac_any=144 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=115 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=49 family_vtrac_final=0
- Flags (winner_flags.csv): rows=183 | exact_any=0 vtrac_any=144 | drop_exact_any=0 drop_vtrac_any=115 | family_exact_any=0 family_vtrac_any=49 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=183 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.547143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 228 (canonical 228)
- Stamp (winner_stamp.json): items_total=49 | exact_any=5 exact_final=0 | vtrac_any=41 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=20 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=49 | exact_any=5 vtrac_any=41 | drop_exact_any=3 drop_vtrac_any=20 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=49 vt_straight=0
- Hits (winner_hits.csv): rows=49 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=49 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.777143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 559 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 559 | score_v2 10.577143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 924 | score_v2 10.547143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 924 | score_v2 10.547143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 924 | score_v2 10.547143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 924 | score_v2 10.547143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 10.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 10.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 10.527143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw4 col 3 | pattern 924 | score_v2 10.447143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 924 | score_v2 10.547143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 924 | score_v2 10.547143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 924 | score_v2 10.447143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 438 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 922 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 400 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 924 | score_v2 9.647143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 992 | score_v2 9.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 228 (canon 228): items_total=12 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/28; Evening 109 (canon 019): items_total=183 exact_any=0 vtrac_any=144 | top winner_present=False best_rank=None/32; Combined 228 (canon 228): items_total=49 exact_any=5 vtrac_any=41 | top winner_present=False best_rank=None/30
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 924, 924, 924.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260105_053638)

## Top indices (from enhanced JSON)
- index 4 | score 51.56079999999999 | features: presence=32.073299999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 37.900124999999996 | features: presence=23.912625000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 27.67191 | features: presence=17.66441, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 26.281120000000005 | features: presence=19.24362, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 21 | score 23.506147500000004 | features: presence=13.2886475, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 20.915295 | features: presence=12.927795000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 13 | score 19.46962416666667 | features: presence=8.4354575, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 9 | score 19.25738 | features: presence=10.43988, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 24 | score 18.478410000000004 | features: presence=9.910910000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 30 | score 18.19677 | features: presence=11.13927, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
093, 903, 687, 683, 386, 867, 034, 593, 836, 598

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 228 | index 27 | file Connecticut4_vtrac27_winner_228_20260105_053356.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 109 | index 9 | file Connecticut4_vtrac9_winner_109_20260105_053357.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 228 | index 27 rank 24/35 (rank_frac 0.6857142857142857) | score 3.7477500000000004 (top 51.56079999999999, ratio 0.07268603280011172, delta 47.81304999999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 109 | index 9 rank 8/35 (rank_frac 0.22857142857142856) | score 19.25738 (top 51.56079999999999, ratio 0.37348877441777484, delta 32.30341999999999) | winner_in_index_straights=False | top_index_straights: 064 (7.903), 406 (6.243), 596 (5.358)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 228→idx27 rank 24/35 (frac 0.686); 109→idx9 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 4, 14, 5, 23, 21.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-01)

## Midday winner 228 (canonical 228)
- Top lanes (hot_zones_top_lanes.csv): present | rank 205/208 (rank_frac 0.9855769230769231) | score_mean 13.144 (top 21.935, ratio 0.5992249829040347, delta 8.790999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 109 (canonical 019)
- Top lanes (hot_zones_top_lanes.csv): present | rank 144/208 (rank_frac 0.6923076923076923) | score_mean 16.801 (top 21.935, ratio 0.7659448370184636, delta 5.134)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 21.935 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 055 | vt_triad 11 | score_mean 21.652 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 007 | vt_triad 13 | score_mean 21.292 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 467 | vt_triad 235 | score_mean 21.011 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 177 | vt_triad 23 | score_mean 21.009 | tags hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 116 | vt_triad 22 | score_mean 20.692 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 059 | vt_triad 115 | score_mean 20.687 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 006 | vt_triad 12 | score_mean 20.435 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight
- rank    9 | triad 011 | vt_triad 12 | score_mean 20.324 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 125 | vt_triad 123 | score_mean 20.2 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 228 (canon 228): rank 205/208 (rank_frac 0.986) ratio_to_top=0.5992249829040347; Evening 109 (canon 019): rank 144/208 (rank_frac 0.692) ratio_to_top=0.7659448370184636
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

Aux draws snapshot dir: `sharepacks/2026-01-01/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=361, 932, 467, 095, 055
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=932, 095, 211, 042, 261
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=361, 467, 055, 279, 083

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=2 last_repeat_gap=31 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=34), P2:0 (gap=40), P3:0 (gap=31)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=883 sev=B
- 129: ds=865 sev=B
- 288: ds=853 sev=B
- 149: ds=835 sev=B
- 445: ds=767 sev=B
- 114: ds=737 sev=B
- 069: ds=701 sev=B
- 888: ds=699 sev=B
- 688: ds=695 sev=B
- 133: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=85 sev=blue
  - 22: ds=73 sev=blue
  - 99: ds=66 sev=purple
  - 00: ds=36 sev=purple
  - 33: ds=23 sev=-
  - 88: ds=22 sev=-
  - 66: ds=21 sev=-
  - 77: ds=11 sev=-
  - 11: ds=5 sev=-
  - 55: ds=4 sev=-
- non_repeating:
  - 69: ds=83 sev=red
  - 48: ds=72 sev=red
  - 78: ds=68 sev=red
  - 57: ds=67 sev=red
  - 49: ds=66 sev=red
  - 19: ds=60 sev=red
  - 01: ds=41 sev=blue
  - 25: ds=35 sev=purple
  - 06: ds=33 sev=purple
  - 07: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:401, 32:168, 25:154, 29:127, 4:125, 15:113, 31:102, 34:97, 3:82, 27:81

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=401 fs=1 fl=2 hz=0.01098901098901099, 32:ds=168 fs=5 fl=3 hz=0.010830324909747294, 25:ds=154 fs=22 fl=2 hz=0.029055690072639227, 29:ds=127 fs=25 fl=1 hz=0.029988465974625143, 4:ds=125 fs=21 fl=2 hz=0.027677496991576414, 15:ds=113 fs=10 fl=4 hz=0.01583710407239819, 31:ds=102 fs=32 fl=0 hz=0.03665521191294387, 34:ds=97 fs=15 fl=2 hz=0.01951779563719862, 3:ds=82 fs=27 fl=0 hz=0.030337078651685393, 27:ds=81 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=99 flags=purple
- S3: ds=76 flags=purple
- S24: ds=68 flags=blue+purple
- S22: ds=66 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 348: score=2 tags=FLT,MIR
  - 358: score=2 tags=FLT,MIR
  - 368: score=2 tags=FLT,MIR
  - 378: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=72 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=25), P2:0 (gap=25), P3:8 (gap=30)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=878 sev=B
- 478: ds=859 sev=B
- 459: ds=854 sev=B
- 159: ds=810 sev=B
- 099: ds=791 sev=B
- 127: ds=782 sev=B
- 559: ds=724 sev=B
- 004: ds=683 sev=B
- 155: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=90 sev=blue
  - 88: ds=50 sev=purple
  - 44: ds=42 sev=purple
  - 22: ds=36 sev=purple
  - 55: ds=27 sev=purple
  - 00: ds=23 sev=-
  - 33: ds=11 sev=-
  - 66: ds=10 sev=-
  - 77: ds=5 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 78: ds=68 sev=red
  - 13: ds=55 sev=blue
  - 49: ds=42 sev=blue
  - 19: ds=41 sev=blue
  - 69: ds=41 sev=blue
  - 48: ds=38 sev=blue
  - 57: ds=33 sev=purple
  - 79: ds=33 sev=purple
  - 37: ds=22 sev=-
  - 01: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:200, 25:101, 31:90, 32:88, 18:85, 3:73, 29:63, 4:62, 15:56, 34:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=200 fs=3 fl=0 hz=0.008565310492505354, 25:ds=101 fs=21 fl=1 hz=0.025974025974025976, 31:ds=90 fs=20 fl=2 hz=0.024608501118568233, 32:ds=88 fs=3 fl=4 hz=0.009510869565217392, 18:ds=85 fs=23 fl=1 hz=0.026519337016574582, 3:ds=73 fs=22 fl=2 hz=0.02631578947368421, 29:ds=63 fs=18 fl=2 hz=0.023446658851113716, 4:ds=62 fs=26 fl=0 hz=0.02931228861330327, 15:ds=56 fs=24 fl=1 hz=0.02662406815761448, 34:ds=48 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=84 flags=blue+purple
- S24: ds=81 flags=blue+purple
- S8: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 489: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=9 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=17), P2:0 (gap=20), P3:0 (gap=18)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=905 sev=B
- 668: ds=902 sev=B
- 399: ds=901 sev=B
- 044: ds=897 sev=B
- 133: ds=894 sev=B
- 145: ds=866 sev=B
- 677: ds=773 sev=B
- 333: ds=768 sev=B
- 112: ds=720 sev=B
- 344: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=112 sev=red
  - 22: ds=69 sev=purple
  - 99: ds=33 sev=purple
  - 77: ds=27 sev=purple
  - 66: ds=22 sev=-
  - 11: ds=21 sev=-
  - 33: ds=19 sev=-
  - 00: ds=18 sev=-
  - 88: ds=11 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 09: ds=64 sev=red
  - 57: ds=48 sev=blue
  - 69: ds=46 sev=blue
  - 23: ds=43 sev=blue
  - 25: ds=41 sev=blue
  - 06: ds=40 sev=blue
  - 07: ds=40 sev=blue
  - 01: ds=38 sev=blue
  - 48: ds=36 sev=purple
  - 78: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:311, 26:139, 4:122, 34:91, 32:84, 25:77, 29:65, 15:64, 2:54, 31:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=311 fs=2 fl=1 hz=0.005961251862891207, 26:ds=139 fs=3 fl=1 hz=0.008680555555555556, 4:ds=122 fs=18 fl=1 hz=0.02243211334120425, 34:ds=91 fs=14 fl=3 hz=0.019144144144144143, 32:ds=84 fs=2 fl=0 hz=0.008450704225352114, 25:ds=77 fs=21 fl=0 hz=0.023836549375709424, 29:ds=65 fs=27 fl=0 hz=0.030100334448160536, 15:ds=64 fs=15 fl=1 hz=0.019698725376593278, 2:ds=54 fs=23 fl=2 hz=0.028344671201814057, 31:ds=51 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=91 flags=blue+purple
- S8: ds=68 flags=red+purple
- S20: ds=51 flags=purple
- S3: ds=38 flags=blue+purple
- S24: ds=34 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=MIR
  - 016: score=1 tags=MIR
  - 025: score=1 tags=MIR
  - 027: score=1 tags=MIR
  - 035: score=1 tags=MIR
  - 038: score=1 tags=MIR
  - 045: score=1 tags=MIR
  - 049: score=1 tags=MIR
  - 056: score=1 tags=MIR
  - 057: score=1 tags=MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:691(B); evening:894(B)
- 445 -> combined:767(B); evening:689(B)
- 459 -> combined:676(B); midday:854(B)
- 888 -> combined:699(B); evening:697(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:41(blue); evening:38(blue)
- 06 -> combined:33(purple); evening:40(blue)
- 07 -> combined:33(purple); evening:40(blue)
- 19 -> combined:60(red); evening:30(purple); midday:41(blue)
- 22 -> combined:73(blue); evening:69(purple); midday:36(purple)
- 25 -> combined:35(purple); evening:41(blue)
- 44 -> combined:85(blue); evening:112(red); midday:42(purple)
- 48 -> combined:72(red); evening:36(purple); midday:38(blue)
- 49 -> combined:66(red); evening:33(purple); midday:42(blue)
- 57 -> combined:67(red); evening:48(blue); midday:33(purple)
- 69 -> combined:83(red); evening:46(blue); midday:41(blue)
- 78 -> combined:68(red); evening:34(purple); midday:68(red)
- 99 -> combined:66(purple); evening:33(purple); midday:90(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.232571428571429)[R1,XVAR-Cons(CEM)], 5(2.621585714285714)[R3,XVAR-Cons(CM)], 9(0.9135)[R2,Double-Pressure], 6(0.44399999999999995)[R2,Swap], 3(0.21779285714285712)[R3,Swap]
- P2: 0(8.443571428571428)[R1,XVAR-Cons(CEM)], 2(3.2148000000000003)[R2,XVAR-Cons(CM)], 8(1.7206285714285716)[R3,XVAR-Cons(CM)], 9(0.9625999999999999)[R2,Double-Pressure], 1(0.24466428571428572)[R3,Swap]
- P3: 0(7.11325)[R1,XVAR-Cons(CEM)], 8(6.927507142857143)[R2,XVAR-Cons(CEM)], 4(2.9289571428571426)[R3,XVAR-Cons(CM)], 2(0.9508)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_31.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=34), P2:0(gap=40), P3:0(gap=31); top cartesian candidates: 700, 708, 704, 720, 728.
- Q3: Blackapple: score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 038, 058, 138, 168, 238.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:691(B),evening:894(B); 445→combined:767(B),evening:689(B); 459→combined:676(B),midday:854(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:401, 32:168, 25:154, 29:127, 4:125.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=228 Evening=109; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 228 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 019 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 228 (canon 228): box `228` covers winner `228` (boxed hit).
  - Evening winner 109 (canon 019): box `019` covers winner `109` (boxed hit).
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
