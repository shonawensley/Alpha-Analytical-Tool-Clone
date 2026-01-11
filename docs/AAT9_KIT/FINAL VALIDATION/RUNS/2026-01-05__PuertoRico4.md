# Master Validation Run Report — PuertoRico4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-05/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-05/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-05/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-05/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-05/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-05/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac27_winner_732_20260110_035741.html`
- `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_972_20260110_035742.html`

Winners JSON files:
- `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac27_winner_732_20260110_035741.json`
- `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac28_winner_972_20260110_035742.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 732 (canon 237): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 972 (canon 279): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 732 idx27 (rank 11/35, frac 0.314), 972 idx28 (rank 14/35, frac 0.400)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (Hot Zones top lanes overlap)**.
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

### 2.Stable — PuertoRico4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-05)

## Midday winner 732 (canonical 237)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=47 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 29 | rank 464/1354 (rank_frac 0.34268833087149186) | score 17.0 (top 29.5, ratio 0.576271186440678, delta 12.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=5
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 972 (canonical 279)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=53 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 26 | rank 17/1354 (rank_frac 0.012555391432791729) | score 25.5 (top 29.5, ratio 0.864406779661017, delta 4.0) | section Evening, hot2 1
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=5
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 268 | section Evening | score 67.0 | col1_hits 6 | hot2 11
- rank   16 | canon 078 | section Combined | score 52.0 | col1_hits 5 | hot2 8
- rank   30 | canon 0788 | section Combined | score 43.5 | col1_hits 4 | hot2 6
- rank    9 | canon 688 | section Combined | score 55.5 | col1_hits 5 | hot2 6
- rank    5 | canon 006 | section Combined | score 56.5 | col1_hits 5 | hot2 6
- rank   22 | canon 6788 | section Combined | score 47.5 | col1_hits 4 | hot2 6
- rank    5 | canon 788 | section Combined | score 56.5 | col1_hits 4 | hot2 6
- rank    5 | canon 008 | section Combined | score 56.5 | col1_hits 4 | hot2 6
- rank    4 | canon 002 | section Combined | score 57.5 | col1_hits 5 | hot2 6
- rank    3 | canon 007 | section Combined | score 60.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1336 | family 31 | score 5.0 | hot2 0 | section Midday
- rank  735 | family 33 | score 13.5 | hot2 0 | section Midday
- rank 1144 | family 7 | score 9.0 | hot2 0 | section Midday
- rank 1199 | family 4 | score 8.5 | hot2 0 | section Midday
- rank 1252 | family 3 | score 7.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 732 (canon 237): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 972 (canon 279): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260110)

## Midday winner 732 (canonical 237)
- Stamp (winner_stamp.json): items_total=25 | exact_any=2 exact_final=0 | vtrac_any=11 vtrac_final=0 | drop_exact_any=5 drop_exact_final=0 | drop_vtrac_any=22 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=5 family_vtrac_final=0
- Flags (winner_flags.csv): rows=25 | exact_any=2 vtrac_any=11 | drop_exact_any=5 drop_vtrac_any=22 | family_exact_any=2 family_vtrac_any=5 | vt_boxed=13 vt_straight=0
- Hits (winner_hits.csv): rows=25 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=13 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.764921 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 972 (canonical 279)
- Stamp (winner_stamp.json): items_total=120 | exact_any=0 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=98 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=52 family_vtrac_final=0
- Flags (winner_flags.csv): rows=120 | exact_any=0 vtrac_any=120 | drop_exact_any=0 drop_vtrac_any=98 | family_exact_any=0 family_vtrac_any=52 | vt_boxed=42 vt_straight=0
- Hits (winner_hits.csv): rows=120 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=42 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 732 (canonical 237)
- Stamp (winner_stamp.json): items_total=68 | exact_any=2 exact_final=0 | vtrac_any=13 vtrac_final=0 | drop_exact_any=5 drop_exact_final=0 | drop_vtrac_any=65 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=7 family_vtrac_final=0
- Flags (winner_flags.csv): rows=68 | exact_any=2 vtrac_any=13 | drop_exact_any=5 drop_vtrac_any=65 | family_exact_any=2 family_vtrac_any=7 | vt_boxed=44 vt_straight=0
- Hits (winner_hits.csv): rows=68 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=44 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 220 | score_v2 10.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 220 | score_v2 9.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 220 | score_v2 9.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 220 | score_v2 9.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 220 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 220 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 9.377143 | match_types 
- area_rank 2 | variant Evening | section Evening | set Set1 draw Draw4 col 3 | pattern 522 | score_v2 9.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 220 | score_v2 9.177143 | match_types 
- area_rank 2 | variant Evening | section Evening | set Set1 draw Draw6 col 1 | pattern 522 | score_v2 8.987143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 220 | score_v2 8.777143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 552 | score_v2 8.777143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 220 | score_v2 10.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 220 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 224 | score_v2 9.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 522 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 592 | score_v2 8.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 592 | score_v2 8.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 552 | score_v2 8.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 554 | score_v2 8.764921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 200 | score_v2 8.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 003 | score_v2 8.664643 | tags exact,vtrac,family_exact,family_vtrac
- rank 11 | variant Evening | best_pattern 524 | score_v2 8.647143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Midday | best_pattern 554 | score_v2 8.564921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 732 (canon 237): items_total=25 exact_any=2 vtrac_any=11 | top winner_present=False best_rank=None/30; Evening 972 (canon 279): items_total=120 exact_any=0 vtrac_any=120 | top winner_present=False best_rank=None/30; Combined 732 (canon 237): items_total=68 exact_any=2 vtrac_any=13 | top winner_present=False best_rank=None/22
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 220, 220, 224, 522, 592.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260110_035939)

## Top indices (from enhanced JSON)
- index 7 | score 59.78719249999999 | features: presence=44.3396925, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 21 | score 40.484595 | features: presence=25.707095000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 24.402767500000003 | features: presence=16.1752675, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 20 | score 22.196435000000005 | features: presence=13.298935, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 19.72141666666667 | features: presence=13.854750000000003, set_echo=0.3, first_hit=0.4, column_span=0.16666666666666666
- index 23 | score 17.404325000000004 | features: presence=11.196825000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 18 | score 13.491075000000002 | features: presence=8.263575000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 13.081750000000001 | features: presence=5.834250000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 32 | score 13.012058333333336 | features: presence=8.053100000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 14 | score 9.869658333333332 | features: presence=3.2806999999999995, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
206, 062, 602, 026, 067, 268, 670, 286, 706, 362

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 732 | index 27 | file PuertoRico4_vtrac27_winner_732_20260110_035741.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 972 | index 28 | file PuertoRico4_vtrac28_winner_972_20260110_035742.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 732 | index 27 rank 11/35 (rank_frac 0.3142857142857143) | score 8.398925 (top 59.78719249999999, ratio 0.1404803378248611, delta 51.38826749999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 972 | index 28 rank 14/35 (rank_frac 0.4) | score 7.531668333333333 (top 59.78719249999999, ratio 0.12597461125697337, delta 52.25552416666665) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 732→idx27 rank 11/35 (frac 0.314); 972→idx28 rank 14/35 (frac 0.400).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 7, 21, 10, 20, 4.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-05)

## Midday winner 732 (canonical 237)
- Top lanes (hot_zones_top_lanes.csv): present | rank 66/210 (rank_frac 0.3142857142857143) | score_mean 17.445 (top 25.45, ratio 0.6854616895874264, delta 8.004999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 972 (canonical 279)
- Top lanes (hot_zones_top_lanes.csv): present | rank 6/210 (rank_frac 0.02857142857142857) | score_mean 21.25 (top 25.45, ratio 0.8349705304518664, delta 4.199999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 25.45 | tags hot20,ls_col_42,set1_bonus,vertical3,vt_only_lane,vt_straight
- rank    1 | triad 227 | vt_triad 33 | score_mean 25.45 | tags hot20,ls_col_42,set1_bonus,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 144 | vt_triad 25 | score_mean 21.729 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 259 | vt_triad 135 | score_mean 21.648 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    5 | triad 267 | vt_triad 233 | score_mean 21.333 | tags hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 247 | vt_triad 335 | score_mean 21.25 | tags hot20,set1_bonus
- rank    6 | triad 279 | vt_triad 335 | score_mean 21.25 | tags hot20,set1_bonus
- rank    8 | triad 049 | vt_triad 155 | score_mean 20.891 | tags hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical5,vt_straight
- rank    9 | triad 127 | vt_triad 233 | score_mean 20.63 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,superhot_set1,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 344 | vt_triad 45 | score_mean 20.393 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 732 (canon 237): rank 66/210 (rank_frac 0.314) ratio_to_top=0.6854616895874264; Evening 972 (canon 279): rank 6/210 (rank_frac 0.029) ratio_to_top=0.8349705304518664
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

Aux draws snapshot dir: `sharepacks/2026-01-05/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-05/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=359, 529, 917, 144, 913
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-05/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=529, 144, 451, 098, 875
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-05/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=359, 917, 913, 643, 785

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=9 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=62), P2:3 (gap=22), P3:6 (gap=25)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=62)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=995 sev=B
- 447: ds=986 sev=B
- 000: ds=734 sev=B
- 039: ds=722 sev=B
- 466: ds=718 sev=B
- 677: ds=696 sev=B
- 577: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=66 sev=purple
  - 77: ds=65 sev=purple
  - 99: ds=56 sev=purple
  - 11: ds=50 sev=purple
  - 55: ds=31 sev=purple
  - 33: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 88: ds=18 sev=-
  - 00: ds=16 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 47: ds=174 sev=red
  - 24: ds=88 sev=red
  - 48: ds=52 sev=blue
  - 23: ds=49 sev=blue
  - 56: ds=45 sev=blue
  - 05: ds=43 sev=blue
  - 28: ds=38 sev=blue
  - 06: ds=25 sev=purple
  - 01: ds=22 sev=-
  - 03: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:193, 27:134, 5:97, 32:91, 26:86, 31:83, 28:65, 18:57, 34:56, 33:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=193 fs=18 fl=1 hz=0.025477707006369428, 27:ds=134 fs=24 fl=1 hz=0.029868578255675033, 5:ds=97 fs=27 fl=1 hz=0.0343980343980344, 32:ds=91 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=86 fs=4 fl=2 hz=0.01020408163265306, 31:ds=83 fs=14 fl=3 hz=0.018619934282584887, 28:ds=65 fs=26 fl=0 hz=0.0278372591006424, 18:ds=57 fs=20 fl=0 hz=0.022727272727272728, 34:ds=56 fs=26 fl=0 hz=0.02857142857142857, 33:ds=53 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=83 flags=purple
- S23: ds=65 flags=blue+purple
- S26: ds=56 flags=blue+purple
- S8: ds=50 flags=purple
- S6: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6', '8'], 'pairs': {'remaining_count': 1}}
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
- current_index=12 streak=1 max=3 last_repeat_gap=61 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=31), P2:1 (gap=27), P3:6 (gap=12)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=961 sev=B
- 299: ds=952 sev=B
- 003: ds=943 sev=B
- 077: ds=929 sev=B
- 333: ds=878 sev=B
- 555: ds=852 sev=B
- 088: ds=823 sev=B
- 888: ds=817 sev=B
- 666: ds=802 sev=B
- 447: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=108 sev=red
  - 22: ds=81 sev=blue
  - 11: ds=57 sev=purple
  - 99: ds=41 sev=purple
  - 77: ds=32 sev=purple
  - 33: ds=26 sev=purple
  - 88: ds=23 sev=-
  - 55: ds=15 sev=-
  - 66: ds=12 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 47: ds=114 sev=red
  - 24: ds=60 sev=red
  - 38: ds=45 sev=blue
  - 03: ds=44 sev=blue
  - 04: ds=44 sev=blue
  - 35: ds=42 sev=blue
  - 48: ds=34 sev=purple
  - 19: ds=33 sev=purple
  - 18: ds=30 sev=purple
  - 13: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:98, 10:96, 27:95, 26:92, 3:85, 16:57, 23:52, 15:50, 5:48, 32:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=98 fs=16 fl=2 hz=0.020809248554913295, 10:ds=96 fs=20 fl=3 hz=0.026376146788990827, 27:ds=95 fs=19 fl=1 hz=0.024721878862793572, 26:ds=92 fs=7 fl=2 hz=0.011682242990654207, 3:ds=85 fs=31 fl=0 hz=0.03506787330316742, 16:ds=57 fs=4 fl=2 hz=0.009695290858725763, 23:ds=52 fs=31 fl=1 hz=0.034782608695652174, 15:ds=50 fs=25 fl=0 hz=0.026939655172413795, 5:ds=48 fs=28 fl=0 hz=0.03181818181818182, 32:ds=45 fs=2 fl=1 hz=0.006112469437652812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=44 flags=purple
- S25: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=3 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=31), P2:2 (gap=33), P3:6 (gap=23)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=993 sev=B
- 579: ds=974 sev=B
- 114: ds=918 sev=B
- 555: ds=857 sev=B
- 888: ds=765 sev=B
- 067: ds=754 sev=B
- 446: ds=741 sev=B
- 259: ds=739 sev=B
- 224: ds=725 sev=B
- 449: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=145 sev=red
  - 44: ds=141 sev=red
  - 77: ds=43 sev=purple
  - 66: ds=34 sev=purple
  - 22: ds=33 sev=purple
  - 99: ds=28 sev=purple
  - 11: ds=25 sev=purple
  - 33: ds=13 sev=-
  - 88: ds=9 sev=-
  - 00: ds=8 sev=-
- non_repeating:
  - 25: ds=101 sev=red
  - 47: ds=87 sev=red
  - 45: ds=71 sev=red
  - 26: ds=64 sev=red
  - 24: ds=44 sev=blue
  - 05: ds=40 sev=blue
  - 56: ds=40 sev=blue
  - 23: ds=31 sev=purple
  - 89: ds=28 sev=purple
  - 48: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:450, 32:165, 4:119, 10:106, 31:94, 5:84, 33:70, 27:67, 1:59, 30:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=450 fs=5 fl=1 hz=0.01662049861495845, 32:ds=165 fs=6 fl=1 hz=0.009987515605493134, 4:ds=119 fs=23 fl=2 hz=0.03071253071253071, 10:ds=106 fs=16 fl=2 hz=0.0234375, 31:ds=94 fs=18 fl=3 hz=0.02394526795895097, 5:ds=84 fs=18 fl=2 hz=0.022446689113355782, 33:ds=70 fs=12 fl=1 hz=0.017361111111111112, 27:ds=67 fs=18 fl=1 hz=0.02358490566037736, 1:ds=59 fs=4 fl=4 hz=0.00909090909090909, 30:ds=44 fs=42 fl=0 hz=0.044823906083244394

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=77 flags=purple
- S24: ds=68 flags=purple
- S18: ds=53 flags=red+purple
- S23: ds=48 flags=blue+purple
- S16: ds=43 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 447 -> combined:986(B); midday:741(B)
- 555 -> evening:857(B); midday:852(B)
- 888 -> evening:765(B); midday:817(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:43(blue); evening:40(blue)
- 11 -> combined:50(purple); evening:25(purple); midday:57(purple)
- 22 -> combined:66(purple); evening:33(purple); midday:81(blue)
- 23 -> combined:49(blue); evening:31(purple)
- 24 -> combined:88(red); evening:44(blue); midday:60(red)
- 33 -> combined:26(purple); midday:26(purple)
- 47 -> combined:174(red); evening:87(red); midday:114(red)
- 48 -> combined:52(blue); evening:26(purple); midday:34(purple)
- 55 -> combined:31(purple); evening:145(red)
- 56 -> combined:45(blue); evening:40(blue)
- 66 -> combined:25(purple); evening:34(purple)
- 77 -> combined:65(purple); evening:43(purple); midday:32(purple)
- 99 -> combined:56(purple); evening:28(purple); midday:41(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.902571428571429)[R1,Mirror-Echo], 8(2.3589214285714286)[R2,XVAR-Cons(CE)], 3(1.2016)[R2,Double-Pressure], 1(1.0344)[R2,Double-Pressure], 7(0.7131428571428572)[R3,Mirror-Echo]
- P2: 3(6.4809214285714285)[R1,XVAR-Cons(CEM)], 2(1.8372857142857142)[R1,Mirror-Echo], 0(1.7906357142857143)[R3,XVAR-Cons(CM)], 1(1.5061428571428572)[R1,Double-Pressure], 7(1.4822571428571427)[R2,Mirror-Echo]
- P3: 6(7.8678928571428575)[R1,XVAR-Cons(CEM)], 0(1.8713285714285715)[R3,XVAR-Cons(CM)], 2(0.964)[R2,Double-Pressure], 1(0.5599357142857142)[R3,Mirror-Echo], 4(0.3761999999999999)[R2]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=62), P2:3(gap=22), P3:6(gap=25); top cartesian candidates: 236, 206, 226, 276, 232.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6', '8'], 'pairs': {'remaining_count': 1}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 447→combined:986(B),midday:741(B); 555→midday:852(B),evening:857(B); 888→midday:817(B),evening:765(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:193, 27:134, 5:97, 32:91, 26:86.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=732 Evening=972; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 237 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 279 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 732 (canon 237): box `237` covers winner `732` (boxed hit).
  - Evening winner 972 (canon 279): box `279` covers winner `972` (boxed hit).
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
