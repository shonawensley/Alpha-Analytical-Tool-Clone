# Master Validation Run Report — PuertoRico4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-09/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-09/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-09/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-09/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-09/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-09/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac10_winner_225_20260110_035103.html`
- `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac17_winner_126_20260110_035102.html`

Winners JSON files:
- `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac10_winner_225_20260110_035103.json`
- `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac17_winner_126_20260110_035102.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 126 (canon 126): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 225 (canon 225): exact_boxed=True exact_straight=True | rank 419/4940 (rank_frac 0.085)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 225 idx10 (rank 20/35, frac 0.571), 126 idx17 (rank 24/35, frac 0.686)
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

### 2.Stable — PuertoRico4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-09)

## Midday winner 126 (canonical 126)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=30 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 20 | rank 250/1410 (rank_frac 0.1773049645390071) | score 22.0 (top 33.5, ratio 0.6567164179104478, delta 11.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=7
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 225 (canonical 225)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=55 | exact_boxed=12 | exact_straight=3 | vt_boxed=12
- Scores (patterns_scores.csv): rank 419/4940 (rank_frac 0.08481781376518219) | score 20.0 (top 41.0, ratio 0.4878048780487805, delta 21.0) | section Evening, Set Set1, Draw Draw1, Col 5, hot 1, vt_straight 0.0 | why boxed|cov4|hp_repeat3|vstr2|hot1|perm2|double_mirror|draw_chain4
- Compound (patterns_compound.csv): rank 162/1762 (rank_frac 0.09194097616345062) | score 27.0 (top 98.5, ratio 0.27411167512690354, delta 71.5) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 4 | why draw_chain4|hot1x1|dblmirrorx8
- Families (patterns_families.csv): count 32 | rank 339/1410 (rank_frac 0.2404255319148936) | score 20.0 (top 33.5, ratio 0.5970149253731343, delta 13.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=6

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 088 | section Combined | score 98.5 | col1_hits 8 | hot2 11
- rank    2 | canon 188 | section Combined | score 77.0 | col1_hits 7 | hot2 11
- rank    4 | canon 118 | section Combined | score 67.5 | col1_hits 6 | hot2 8
- rank    5 | canon 011 | section Combined | score 66.5 | col1_hits 6 | hot2 8
- rank    8 | canon 01188 | section Combined | score 63.5 | col1_hits 6 | hot2 8
- rank   11 | canon 1188 | section Combined | score 57.5 | col1_hits 6 | hot2 8
- rank   13 | canon 0118 | section Combined | score 56.5 | col1_hits 6 | hot2 8
- rank   51 | canon 015 | section Combined | score 40.0 | col1_hits 5 | hot2 6
- rank   32 | canon 0025 | section Evening | score 46.5 | col1_hits 4 | hot2 6
- rank   25 | canon 025 | section Evening | score 48.0 | col1_hits 4 | hot2 6

## Top families (patterns_families.csv)
- rank 1357 | family 4 | score 6.0 | hot2 0 | section Midday
- rank 1401 | family 7 | score 4.0 | hot2 0 | section Midday
- rank 1095 | family 29 | score 10.0 | hot2 0 | section Midday
- rank 1247 | family 7 | score 8.0 | hot2 0 | section Midday
- rank 1247 | family 27 | score 8.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 126 (canon 126): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 225 (canon 225): exact_boxed=True exact_straight=True | rank 419/4940 (rank_frac 0.085)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260110)

## Midday winner 126 (canonical 126)
- Stamp (winner_stamp.json): items_total=131 | exact_any=4 exact_final=0 | vtrac_any=125 vtrac_final=0 | drop_exact_any=11 drop_exact_final=0 | drop_vtrac_any=29 drop_vtrac_final=0 | family_exact_any=4 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=131 | exact_any=4 vtrac_any=125 | drop_exact_any=11 drop_vtrac_any=29 | family_exact_any=4 family_vtrac_any=12 | vt_boxed=41 vt_straight=0
- Hits (winner_hits.csv): rows=131 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=41 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 225 (canonical 225)
- Stamp (winner_stamp.json): items_total=120 | exact_any=84 exact_final=0 | vtrac_any=104 vtrac_final=0 | drop_exact_any=96 drop_exact_final=0 | drop_vtrac_any=120 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=86 family_vtrac_final=0
- Flags (winner_flags.csv): rows=120 | exact_any=84 vtrac_any=104 | drop_exact_any=96 drop_vtrac_any=120 | family_exact_any=0 family_vtrac_any=86 | vt_boxed=14 vt_straight=0
- Hits (winner_hits.csv): rows=120 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=14 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=True | winner_best_rank=2 | winner_rank_fraction=0.07692307692307693 | winner_score_v2=9.927143 top_score_v2=9.927143 | winner_score_ratio_to_top=1.0 winner_score_delta_from_top=0.0
- Reducer scores present: True

## Combined winner 126 (canonical 126)
- Stamp (winner_stamp.json): items_total=277 | exact_any=5 exact_final=0 | vtrac_any=269 vtrac_final=0 | drop_exact_any=14 drop_exact_final=0 | drop_vtrac_any=53 drop_vtrac_final=0 | family_exact_any=4 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=277 | exact_any=5 vtrac_any=269 | drop_exact_any=14 drop_vtrac_any=53 | family_exact_any=4 family_vtrac_any=12 | vt_boxed=61 vt_straight=0
- Hits (winner_hits.csv): rows=277 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=61 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.937143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 11.937143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 552 | score_v2 11.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 552 | score_v2 11.758571 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 552 | score_v2 11.108571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 522 | score_v2 9.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 552 | score_v2 9.827143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 9.808571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 524 | score_v2 9.777143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 524 | score_v2 9.697143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 524 | score_v2 9.682597 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 552 | score_v2 11.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 522 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 552 | score_v2 9.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 552 | score_v2 9.808571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 524 | score_v2 9.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 524 | score_v2 9.682597 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 220 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 008 | score_v2 9.63131 | tags exact,vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 521 | score_v2 9.59381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 559 | score_v2 9.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 126 (canon 126): items_total=131 exact_any=4 vtrac_any=125 | top winner_present=False best_rank=None/36; Evening 225 (canon 225): items_total=120 exact_any=84 vtrac_any=104 | top winner_present=True best_rank=2/26; Combined 126 (canon 126): items_total=277 exact_any=5 vtrac_any=269 | top winner_present=False best_rank=None/26
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 522, 552, 552, 524.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260110_035303)

## Top indices (from enhanced JSON)
- index 23 | score 57.04910499999999 | features: presence=41.11160499999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 55.333394999999996 | features: presence=38.815895, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 45.821242500000004 | features: presence=32.6737425, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 38.594669999999994 | features: presence=24.467169999999996, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 18 | score 37.78312249999999 | features: presence=21.535622499999988, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 4 | score 36.42339499999999 | features: presence=21.905894999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 28.024235 | features: presence=17.296734999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 19 | score 14.981700000000002 | features: presence=5.744200000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 5 | score 13.911062500000002 | features: presence=7.393562500000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 9 | score 13.747979166666664 | features: presence=6.3656875, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
018, 068, 086, 810, 680, 865, 568, 586, 685, 518

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 225 | index 10 | file PuertoRico4_vtrac10_winner_225_20260110_035103.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 126 | index 17 | file PuertoRico4_vtrac17_winner_126_20260110_035102.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 225 | index 10 rank 20/35 (rank_frac 0.5714285714285714) | score 0.0 (top 57.04910499999999, ratio 0.0, delta 57.04910499999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 126 | index 17 rank 24/35 (rank_frac 0.6857142857142857) | score 0.0 (top 57.04910499999999, ratio 0.0, delta 57.04910499999999) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 225→idx10 rank 20/35 (frac 0.571); 126→idx17 rank 24/35 (frac 0.686).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 8, 2, 13, 18.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-09)

## Midday winner 126 (canonical 126)
- Top lanes (hot_zones_top_lanes.csv): present | rank 30/207 (rank_frac 0.14492753623188406) | score_mean 18.653 (top 24.9, ratio 0.7491164658634538, delta 6.247)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 225 (canonical 225)
- Top lanes (hot_zones_top_lanes.csv): present | rank 24/207 (rank_frac 0.11594202898550725) | score_mean 18.927 (top 24.9, ratio 0.7601204819277109, delta 5.972999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 24.9 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 479 | vt_triad 355 | score_mean 24.507 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    3 | triad 237 | vt_triad 334 | score_mean 22.6 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 259 | vt_triad 135 | score_mean 22.5 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 000 | vt_triad 1 | score_mean 21.9 | tags col1,hot16,straight_lane,vertical4
- rank    6 | triad 249 | vt_triad 355 | score_mean 21.817 | tags col1,guard_set1,hot16,hot20,ls2_lane,set1_bonus,superhot_set1,vertical2,vt_only_lane,vt_straight
- rank    7 | triad 699 | vt_triad 25 | score_mean 21.737 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 246 | vt_triad 235 | score_mean 20.332 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 226 | vt_triad 23 | score_mean 20.144 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 144 | vt_triad 25 | score_mean 19.847 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 126 (canon 126): rank 30/207 (rank_frac 0.145) ratio_to_top=0.7491164658634538; Evening 225 (canon 225): rank 24/207 (rank_frac 0.116) ratio_to_top=0.7601204819277109
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

Aux draws snapshot dir: `sharepacks/2026-01-09/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=479, 073, 969, 426, 972
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=073, 426, 732, 529, 144
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-09/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=479, 969, 972, 359, 917

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=3 last_repeat_gap=15 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=68), P2:0 (gap=18), P3:0 (gap=16)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=68)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=43.171328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 205: score=42.228342857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.399507142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.87625 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.746721428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.50867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 285: score=35.93326428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 204: score=35.376621428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=34.23227142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.57889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 447: ds=992 sev=B
- 000: ds=740 sev=B
- 039: ds=728 sev=B
- 466: ds=724 sev=B
- 677: ds=702 sev=B
- 577: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=72 sev=blue
  - 77: ds=71 sev=blue
  - 11: ds=56 sev=purple
  - 55: ds=37 sev=purple
  - 33: ds=32 sev=purple
  - 66: ds=31 sev=purple
  - 88: ds=24 sev=-
  - 00: ds=22 sev=-
  - 44: ds=9 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 48: ds=58 sev=red
  - 56: ds=51 sev=blue
  - 05: ds=49 sev=blue
  - 28: ds=44 sev=blue
  - 06: ds=31 sev=purple
  - 01: ds=28 sev=purple
  - 12: ds=27 sev=purple
  - 16: ds=27 sev=purple
  - 38: ds=26 sev=purple
  - 68: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:199, 5:103, 32:97, 26:92, 18:63, 34:62, 33:59, 35:57, 16:56, 19:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=199 fs=18 fl=1 hz=0.025477707006369428, 5:ds=103 fs=27 fl=1 hz=0.0343980343980344, 32:ds=97 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=92 fs=4 fl=2 hz=0.01020408163265306, 18:ds=63 fs=20 fl=0 hz=0.022727272727272728, 34:ds=62 fs=26 fl=0 hz=0.02857142857142857, 33:ds=59 fs=10 fl=0 hz=0.016516516516516516, 35:ds=57 fs=1 fl=2 hz=0.005889281507656065, 16:ds=56 fs=6 fl=2 hz=0.01107419712070875, 19:ds=54 fs=20 fl=2 hz=0.023783783783783784

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=89 flags=purple
- S23: ds=71 flags=purple
- S26: ds=62 flags=blue+purple
- S8: ds=56 flags=purple
- S6: ds=52 flags=purple
- S5: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 059: score=4 tags=FLT,MIR,RS
  - 149: score=4 tags=FLT,MIR,RS
  - 167: score=4 tags=FLT,MIR,RS
  - 257: score=4 tags=FLT,MIR,RS
  - 014: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=64 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=34), P2:1 (gap=30), P3:0 (gap=14)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=43.171328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 205: score=42.228342857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.399507142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.87625 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.746721428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.50867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 285: score=35.93326428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 204: score=35.376621428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=34.23227142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.57889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=964 sev=B
- 299: ds=955 sev=B
- 003: ds=946 sev=B
- 077: ds=932 sev=B
- 333: ds=881 sev=B
- 555: ds=855 sev=B
- 088: ds=826 sev=B
- 888: ds=820 sev=B
- 666: ds=805 sev=B
- 447: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=111 sev=red
  - 22: ds=84 sev=blue
  - 11: ds=60 sev=purple
  - 99: ds=44 sev=purple
  - 77: ds=35 sev=purple
  - 33: ds=29 sev=purple
  - 88: ds=26 sev=purple
  - 55: ds=18 sev=-
  - 66: ds=15 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 47: ds=117 sev=red
  - 38: ds=48 sev=blue
  - 04: ds=47 sev=blue
  - 35: ds=45 sev=blue
  - 48: ds=37 sev=blue
  - 19: ds=36 sev=purple
  - 18: ds=33 sev=purple
  - 13: ds=30 sev=purple
  - 49: ds=28 sev=purple
  - 56: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:101, 10:99, 26:95, 3:88, 16:60, 23:55, 15:53, 5:51, 32:48, 31:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=101 fs=16 fl=2 hz=0.020809248554913295, 10:ds=99 fs=20 fl=3 hz=0.026376146788990827, 26:ds=95 fs=7 fl=2 hz=0.011682242990654207, 3:ds=88 fs=31 fl=0 hz=0.03506787330316742, 16:ds=60 fs=4 fl=2 hz=0.009695290858725763, 23:ds=55 fs=31 fl=1 hz=0.034782608695652174, 15:ds=53 fs=25 fl=0 hz=0.026939655172413795, 5:ds=51 fs=28 fl=0 hz=0.03181818181818182, 32:ds=48 fs=2 fl=1 hz=0.006112469437652812, 31:ds=44 fs=22 fl=1 hz=0.024338624338624337

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=47 flags=purple
- S25: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 018: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 128: score=1 tags=FLT
  - 138: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=2 last_repeat_gap=6 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=34), P2:2 (gap=36), P3:6 (gap=26)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=43.171328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 205: score=42.228342857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.399507142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.87625 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.746721428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.50867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 285: score=35.93326428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 204: score=35.376621428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=34.23227142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.57889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=996 sev=B
- 579: ds=977 sev=B
- 114: ds=921 sev=B
- 555: ds=860 sev=B
- 888: ds=768 sev=B
- 067: ds=757 sev=B
- 446: ds=744 sev=B
- 259: ds=742 sev=B
- 224: ds=728 sev=B
- 449: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=148 sev=red
  - 44: ds=144 sev=red
  - 77: ds=46 sev=purple
  - 66: ds=37 sev=purple
  - 22: ds=36 sev=purple
  - 11: ds=28 sev=purple
  - 33: ds=16 sev=-
  - 88: ds=12 sev=-
  - 00: ds=11 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 25: ds=104 sev=red
  - 45: ds=74 sev=red
  - 26: ds=67 sev=red
  - 24: ds=47 sev=blue
  - 05: ds=43 sev=blue
  - 56: ds=43 sev=blue
  - 23: ds=34 sev=purple
  - 89: ds=31 sev=purple
  - 48: ds=29 sev=purple
  - 16: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:453, 32:168, 4:122, 10:109, 5:87, 33:73, 27:70, 1:62, 30:47, 26:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=453 fs=5 fl=1 hz=0.01662049861495845, 32:ds=168 fs=6 fl=1 hz=0.009987515605493134, 4:ds=122 fs=23 fl=2 hz=0.03071253071253071, 10:ds=109 fs=16 fl=2 hz=0.0234375, 5:ds=87 fs=18 fl=2 hz=0.022446689113355782, 33:ds=73 fs=12 fl=1 hz=0.017361111111111112, 27:ds=70 fs=18 fl=1 hz=0.02358490566037736, 1:ds=62 fs=4 fl=4 hz=0.00909090909090909, 30:ds=47 fs=42 fl=0 hz=0.044823906083244394, 26:ds=46 fs=1 fl=2 hz=0.005411255411255411

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=80 flags=purple
- S23: ds=51 flags=blue+purple
- S16: ds=46 flags=red+purple
- S12: ds=42 flags=purple
- S21: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 057: score=4 tags=FLT,MIR,RS
  - 138: score=4 tags=FLT,MIR,RS
  - 489: score=4 tags=FLT,MIR,RS
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 156: score=3 tags=MIR,RS
  - 237: score=3 tags=MIR,RS
  - 678: score=3 tags=FLT,RS
  - 015: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 447 -> combined:992(B); midday:744(B)
- 555 -> evening:860(B); midday:855(B)
- 888 -> evening:768(B); midday:820(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:49(blue); evening:43(blue)
- 11 -> combined:56(purple); evening:28(purple); midday:60(purple)
- 16 -> combined:27(purple); evening:25(purple)
- 22 -> combined:72(blue); evening:36(purple); midday:84(blue)
- 33 -> combined:32(purple); midday:29(purple)
- 38 -> combined:26(purple); midday:48(blue)
- 48 -> combined:58(red); evening:29(purple); midday:37(blue)
- 55 -> combined:37(purple); evening:148(red)
- 56 -> combined:51(blue); evening:43(blue); midday:25(purple)
- 66 -> combined:31(purple); evening:37(purple)
- 77 -> combined:71(blue); evening:46(purple); midday:35(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(9.030285714285714)[R1,XVAR-Cons(CEM)], 8(2.591228571428571)[R2,XVAR-Cons(CE)], 6(1.687507142857143)[R3,XVAR-Cons(CM)], 3(1.2643)[R2,Double-Pressure], 1(1.0971)[R2,Double-Pressure]
- P2: 0(6.337435714285714)[R1,XVAR-Cons(CEM)], 8(2.542357142857143)[R2,XVAR-Cons(CM)], 2(1.7449999999999999)[R1,Double-Pressure], 1(1.5957142857142856)[R1,Double-Pressure], 3(0.9925999999999999)[R2,Double-Pressure]
- P3: 0(3.803607142857143)[R1,Mirror-Echo], 5(2.8606214285714286)[R2,Mirror-Echo], 6(1.5317857142857143)[R1,Mirror-Echo], 7(0.879)[R2,Double-Pressure], 1(0.6409571428571429)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=68), P2:0(gap=18), P3:0(gap=16); top cartesian candidates: 200, 205, 206, 280, 207.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 059, 149, 167, 257, 014.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 447→combined:992(B),midday:744(B); 555→midday:855(B),evening:860(B); 888→midday:820(B),evening:768(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:199, 5:103, 32:97, 26:92, 18:63.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=126 Evening=225; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 126 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 225 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 126 (canon 126): box `126` covers winner `126` (boxed hit).
  - Evening winner 225 (canon 225): box `225` covers winner `225` (boxed hit).
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
