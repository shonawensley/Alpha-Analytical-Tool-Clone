# Master Validation Run Report — OntarioCanada4 — results 2025-12-30 (history workbook ~ 2025-12-29)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-12-30/OntarioCanada4/`
- Winners lens: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-12-30/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-12-30/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-12-30/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-12-30/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2025-12-30/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2025-12-30/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac15_winner_409_20260105_051210.html`
- `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac27_winner_372_20260105_051211.html`

Winners JSON files:
- `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac15_winner_409_20260105_051210.json`
- `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac27_winner_372_20260105_051211.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2025-12-30/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 409 (canon 049): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 372 (canon 237): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 409 idx15 (rank 33/35, frac 0.943), 372 idx27 (rank 18/35, frac 0.514)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — OntarioCanada4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2025-12-30)

## Midday winner 409 (canonical 049)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=41 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 26 | rank 51/1307 (rank_frac 0.03902065799540933) | score 26.0 (top 33.5, ratio 0.7761194029850746, delta 7.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=7
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 372 (canonical 237)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=70 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 32 | rank 338/1307 (rank_frac 0.25860749808722266) | score 19.5 (top 33.5, ratio 0.582089552238806, delta 14.0) | section Midday, hot2 1
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=10
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 114 | section Evening | score 86.0 | col1_hits 7 | hot2 11
- rank    1 | canon 188 | section Combined | score 92.5 | col1_hits 7 | hot2 11
- rank    4 | canon 288 | section Combined | score 82.5 | col1_hits 6 | hot2 11
- rank   15 | canon 1488 | section Combined | score 56.5 | col1_hits 4 | hot2 9
- rank   17 | canon 148 | section Combined | score 55.5 | col1_hits 4 | hot2 9
- rank   21 | canon 1288 | section Combined | score 52.5 | col1_hits 4 | hot2 9
- rank   23 | canon 2488 | section Combined | score 51.0 | col1_hits 3 | hot2 9
- rank   25 | canon 248 | section Combined | score 50.0 | col1_hits 3 | hot2 9
- rank    3 | canon 588 | section Combined | score 84.5 | col1_hits 6 | hot2 9
- rank    8 | canon 488 | section Combined | score 68.5 | col1_hits 4 | hot2 9

## Top families (patterns_families.csv)
- rank 1257 | family 13 | score 6.0 | hot2 0 | section Midday
- rank  844 | family 27 | score 12.5 | hot2 0 | section Midday
- rank  918 | family 27 | score 11.5 | hot2 0 | section Midday
- rank  918 | family 18 | score 11.5 | hot2 0 | section Midday
- rank 1014 | family 22 | score 10.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 409 (canon 049): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 372 (canon 237): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — OntarioCanada4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260105)

## Midday winner 409 (canonical 049)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 372 (canonical 237)
- Stamp (winner_stamp.json): items_total=6 | exact_any=0 exact_final=0 | vtrac_any=3 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=3 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=6 | exact_any=0 vtrac_any=3 | drop_exact_any=0 drop_vtrac_any=3 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=6 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 409 (canonical 049)
- Stamp (winner_stamp.json): items_total=244 | exact_any=0 exact_final=0 | vtrac_any=96 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=208 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=60 family_vtrac_final=0
- Flags (winner_flags.csv): rows=244 | exact_any=0 vtrac_any=96 | drop_exact_any=12 drop_vtrac_any=208 | family_exact_any=0 family_vtrac_any=60 | vt_boxed=4 vt_straight=0
- Hits (winner_hits.csv): rows=244 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=4 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.487143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 228 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 12.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 4 | pattern 522 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 522 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 522 | score_v2 12.487143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 552 | score_v2 12.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 522 | score_v2 12.458571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 522 | score_v2 12.458571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 522 | score_v2 12.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 522 | score_v2 12.337143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 228 | score_v2 13.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 552 | score_v2 12.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 522 | score_v2 12.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 522 | score_v2 12.487143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 552 | score_v2 11.587143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 11.487143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 221 | score_v2 11.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 552 | score_v2 11.115714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 522 | score_v2 10.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 522 | score_v2 10.887143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 409 (canon 049): items_total=12 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/18; Evening 372 (canon 237): items_total=6 exact_any=0 vtrac_any=3 | top winner_present=False best_rank=None/22; Combined 409 (canon 049): items_total=244 exact_any=0 vtrac_any=96 | top winner_present=False best_rank=None/14
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 228, 552, 522, 522, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_051505)

## Top indices (from enhanced JSON)
- index 20 | score 74.63571249999997 | features: presence=47.29821249999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 54.01079999999998 | features: presence=33.80329999999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 23 | score 49.1208275 | features: presence=36.3533275, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 36.84815 | features: presence=25.270650000000003, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 11 | score 32.903757500000005 | features: presence=20.766257500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 26.69377 | features: presence=16.93627, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 32 | score 23.89999 | features: presence=16.98249, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 25 | score 22.988000000000007 | features: presence=15.650500000000001, first_hit=0.33333333333333337, column_span=0.25416666666666665, persistence=0.4
- index 29 | score 22.7978125 | features: presence=14.490312499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 21.489845000000003 | features: presence=13.032345000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
172, 267, 271, 217, 216, 712, 162, 258, 261, 612

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 409 | index 15 | file OntarioCanada4_vtrac15_winner_409_20260105_051210.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 372 | index 27 | file OntarioCanada4_vtrac27_winner_372_20260105_051211.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 409 | index 15 rank 33/35 (rank_frac 0.9428571428571428) | score 0.0 (top 74.63571249999997, ratio 0.0, delta 74.63571249999997) | winner_in_index_straights=False | top_index_straights: (none)
- winner 372 | index 27 rank 18/35 (rank_frac 0.5142857142857142) | score 11.633525 (top 74.63571249999997, ratio 0.1558707569114451, delta 63.00218749999997) | winner_in_index_straights=False | top_index_straights: 732 (2.1)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 409→idx15 rank 33/35 (frac 0.943); 372→idx27 rank 18/35 (frac 0.514).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 20, 17, 23, 19, 11.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2025-12-30

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2025-12-30)

## Midday winner 409 (canonical 049)
- Top lanes (hot_zones_top_lanes.csv): present | rank 187/210 (rank_frac 0.8904761904761904) | score_mean 13.475 (top 23.25, ratio 0.5795698924731183, delta 9.775)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 372 (canonical 237)
- Top lanes (hot_zones_top_lanes.csv): present | rank 192/210 (rank_frac 0.9142857142857143) | score_mean 13.262 (top 23.25, ratio 0.5704086021505377, delta 9.988)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 116 | vt_triad 22 | score_mean 23.25 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 166 | vt_triad 22 | score_mean 22.865 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 279 | vt_triad 335 | score_mean 22.01 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 056 | vt_triad 112 | score_mean 21.802 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 169 | vt_triad 225 | score_mean 21.45 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 167 | vt_triad 223 | score_mean 21.373 | tags funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 126 | vt_triad 223 | score_mean 20.996 | tags funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 146 | vt_triad 225 | score_mean 20.897 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 006 | vt_triad 12 | score_mean 20.857 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank   10 | triad 114 | vt_triad 25 | score_mean 20.756 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 409 (canon 049): rank 187/210 (rank_frac 0.890) ratio_to_top=0.5795698924731183; Evening 372 (canon 237): rank 192/210 (rank_frac 0.914) ratio_to_top=0.5704086021505377
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

Aux draws snapshot dir: `sharepacks/2025-12-30/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=043, 006, 297, 313, 606
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=006, 313, 909, 497, 941
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=043, 297, 606, 056, 770

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=44 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=18), P2:8 (gap=16), P3:2 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=995 sev=B
- 128: ds=915 sev=B
- 555: ds=880 sev=B
- 039: ds=771 sev=B
- 333: ds=742 sev=B
- 188: ds=715 sev=B
- 266: ds=701 sev=B
- 477: ds=699 sev=B
- 126: ds=691 sev=B
- 669: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=117 sev=red
  - 55: ds=73 sev=blue
  - 11: ds=32 sev=purple
  - 88: ds=26 sev=purple
  - 44: ds=17 sev=-
  - 77: ds=8 sev=-
  - 99: ds=5 sev=-
  - 66: ds=4 sev=-
  - 33: ds=3 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 89: ds=77 sev=red
  - 01: ds=52 sev=blue
  - 68: ds=50 sev=blue
  - 15: ds=49 sev=blue
  - 17: ds=43 sev=blue
  - 18: ds=43 sev=blue
  - 12: ds=29 sev=purple
  - 69: ds=28 sev=purple
  - 24: ds=27 sev=purple
  - 26: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:327, 16:281, 17:153, 27:144, 20:131, 33:77, 12:76, 26:71, 30:61, 34:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=327 fs=1 fl=0 hz=0.005698005698005698, 16:ds=281 fs=2 fl=0 hz=0.006329113924050633, 17:ds=153 fs=19 fl=1 hz=0.024242424242424242, 27:ds=144 fs=11 fl=4 hz=0.0178359096313912, 20:ds=131 fs=14 fl=2 hz=0.01853997682502897, 33:ds=77 fs=24 fl=1 hz=0.027472527472527472, 12:ds=76 fs=45 fl=0 hz=0.04928806133625411, 26:ds=71 fs=2 fl=1 hz=0.006075334143377886, 30:ds=61 fs=39 fl=1 hz=0.04405286343612335, 34:ds=58 fs=14 fl=2 hz=0.019698725376593278

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=95 flags=red+purple
- S23: ds=72 flags=blue+purple
- S21: ds=69 flags=purple
- S4: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 028: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 037: score=2 tags=RS
  - 046: score=2 tags=RS
  - 127: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=14 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=24), P2:7 (gap=20), P3:8 (gap=30)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=992 sev=B
- 333: ds=975 sev=B
- 255: ds=942 sev=B
- 355: ds=907 sev=B
- 466: ds=828 sev=B
- 446: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=58 sev=purple
  - 55: ds=36 sev=purple
  - 11: ds=26 sev=purple
  - 77: ds=19 sev=-
  - 88: ds=15 sev=-
  - 66: ds=10 sev=-
  - 44: ds=8 sev=-
  - 99: ds=2 sev=-
  - 33: ds=1 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 34: ds=67 sev=red
  - 07: ds=64 sev=red
  - 04: ds=57 sev=red
  - 16: ds=50 sev=blue
  - 39: ds=38 sev=blue
  - 89: ds=38 sev=blue
  - 68: ds=34 sev=purple
  - 37: ds=33 sev=purple
  - 67: ds=33 sev=purple
  - 03: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:163, 34:158, 16:140, 27:95, 12:92, 14:77, 17:76, 20:65, 19:50, 24:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=163 fs=4 fl=3 hz=0.010432190760059612, 34:ds=158 fs=8 fl=4 hz=0.014423076923076924, 16:ds=140 fs=3 fl=0 hz=0.007462686567164179, 27:ds=95 fs=15 fl=2 hz=0.0189520624303233, 12:ds=92 fs=45 fl=0 hz=0.05079006772009029, 14:ds=77 fs=39 fl=0 hz=0.04276315789473684, 17:ds=76 fs=29 fl=2 hz=0.033879781420765025, 20:ds=65 fs=24 fl=3 hz=0.029315960912052113, 19:ds=50 fs=20 fl=2 hz=0.023732470334412083, 24:ds=40 fs=48 fl=0 hz=0.052805280528052806

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=74 flags=purple
- S25: ds=70 flags=purple
- S1: ds=59 flags=blue+purple
- S5: ds=57 flags=purple
- S8: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 058: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 247: score=3 tags=FLT,RS
  - 256: score=3 tags=FLT,RS
  - 589: score=3 tags=FLT,RS
  - 013: score=2 tags=RS
  - 049: score=2 tags=RS
  - 067: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=51 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=14), P2:1 (gap=49), P3:9 (gap=36)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=49)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=899 sev=B
- 113: ds=850 sev=B
- 378: ds=843 sev=B
- 566: ds=832 sev=B
- 199: ds=824 sev=B
- 899: ds=802 sev=B
- 126: ds=798 sev=B
- 559: ds=793 sev=B
- 477: ds=782 sev=B
- 558: ds=748 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=228 sev=red
  - 22: ds=59 sev=purple
  - 00: ds=46 sev=purple
  - 44: ds=29 sev=purple
  - 11: ds=16 sev=-
  - 99: ds=14 sev=-
  - 88: ds=13 sev=-
  - 33: ds=11 sev=-
  - 77: ds=4 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 36: ds=71 sev=red
  - 24: ds=55 sev=blue
  - 18: ds=49 sev=blue
  - 89: ds=49 sev=blue
  - 15: ds=48 sev=blue
  - 78: ds=47 sev=blue
  - 49: ds=41 sev=blue
  - 57: ds=38 sev=blue
  - 09: ds=28 sev=purple
  - 01: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:424, 1:339, 16:190, 26:122, 18:107, 17:100, 20:91, 27:72, 3:70, 23:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=424 fs=0 fl=2 hz=0.005366726296958855, 1:ds=339 fs=0 fl=0 hz=0.0, 16:ds=190 fs=3 fl=1 hz=0.007853403141361256, 26:ds=122 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=107 fs=16 fl=1 hz=0.019384264538198404, 17:ds=100 fs=13 fl=3 hz=0.018626309662398137, 20:ds=91 fs=15 fl=2 hz=0.01925254813137033, 27:ds=72 fs=12 fl=1 hz=0.015486725663716814, 3:ds=70 fs=16 fl=4 hz=0.02152852529601722, 23:ds=63 fs=25 fl=2 hz=0.03085714285714286

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=80 flags=purple
- S2: ds=70 flags=blue+purple
- S4: ds=68 flags=purple
- S25: ds=57 flags=purple
- S20: ds=50 flags=purple
- S9: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:691(B); evening:798(B)
- 128 -> combined:915(B); evening:899(B)
- 333 -> combined:742(B); midday:975(B)
- 477 -> combined:699(B); evening:782(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:52(blue); evening:26(purple); midday:26(purple)
- 11 -> combined:32(purple); midday:26(purple)
- 12 -> combined:29(purple); evening:26(purple)
- 15 -> combined:49(blue); evening:48(blue)
- 18 -> combined:43(blue); evening:49(blue)
- 22 -> combined:117(red); evening:59(purple); midday:58(purple)
- 24 -> combined:27(purple); evening:55(blue)
- 55 -> combined:73(blue); evening:228(red); midday:36(purple)
- 68 -> combined:50(blue); evening:25(purple); midday:34(purple)
- 69 -> combined:28(purple); midday:25(purple)
- 89 -> combined:77(red); evening:49(blue); midday:38(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.7464142857142857)[R1,XVAR-Cons(CM)], 8(3.3248785714285716)[R2,XVAR-Cons(CE)], 5(2.786285714285714)[R3,XVAR-Cons(CM)], 9(1.018)[R1,Double-Pressure], 3(0.3712928571428571)[R3,Mirror-Echo]
- P2: 8(6.463842857142857)[R1,Mirror-Echo], 6(2.9213714285714283)[R3,XVAR-Cons(CE)], 1(1.859)[R1,Mirror-Echo], 7(1.3404285714285713)[R1,Mirror-Echo], 3(1.2365714285714284)[R2,Mirror-Echo]
- P3: 2(6.67225)[R1,XVAR-Cons(CEM)], 8(3.1937142857142855)[R3,XVAR-Cons(CM)], 9(1.645)[R1,Double-Pressure], 4(0.974)[R2,Double-Pressure], 0(0.8508)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025-12-29.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=18), P2:8(gap=16), P3:2(gap=23); top cartesian candidates: 882, 182, 888, 282, 862.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 028, 145, 235, 289, 478.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:691(B),evening:798(B); 128→combined:915(B),evening:899(B); 333→combined:742(B),midday:975(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:327, 16:281, 17:153, 27:144, 20:131.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=409 Evening=372; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 049 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 237 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 409 (canon 049): box `049` covers winner `409` (boxed hit).
  - Evening winner 372 (canon 237): box `237` covers winner `372` (boxed hit).
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
