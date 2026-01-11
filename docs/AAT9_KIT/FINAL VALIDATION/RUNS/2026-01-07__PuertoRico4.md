# Master Validation Run Report — PuertoRico4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-07/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-07/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-07/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-07/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-07/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-07/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac22_winner_426_20260110_033441.html`
- `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_969_20260110_033443.html`

Winners JSON files:
- `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac22_winner_426_20260110_033441.json`
- `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac25_winner_969_20260110_033443.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 426 (canon 246): exact_boxed=True exact_straight=True | rank 416/3933 (rank_frac 0.106); Evening 969 (canon 699): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 426 idx22 (rank 26/35, frac 0.743), 969 idx25 (rank 14/35, frac 0.400)
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

### 2.Stable — PuertoRico4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-07)

## Midday winner 426 (canonical 246)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=18 | family_rows=79 | exact_boxed=18 | exact_straight=18 | vt_boxed=18
- Scores (patterns_scores.csv): rank 416/3933 (rank_frac 0.1057716755657259) | score 17.0 (top 34.5, ratio 0.4927536231884058, delta 17.5) | section Evening, Set Set1, Draw Draw3, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hot2|vtrac_straight|set_chain3|draw_chain4
- Compound (patterns_compound.csv): rank 35/1493 (rank_frac 0.02344273275284662) | score 31.5 (top 59.5, ratio 0.5294117647058824, delta 28.0) | section Evening, col1_hits 0, hot2 3, set_chain 3, draw_chain 5 | why set_chain3|draw_chain5|hot2x3|vstrx4
- Families (patterns_families.csv): count 28 | rank 398/1138 (rank_frac 0.34973637961335674) | score 16.0 (top 31.0, ratio 0.5161290322580645, delta 15.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=17

## Evening winner 969 (canonical 699)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=26 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 17 | rank 398/1138 (rank_frac 0.34973637961335674) | score 16.0 (top 31.0, ratio 0.5161290322580645, delta 15.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=3
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    8 | canon 068 | section Evening | score 51.0 | col1_hits 3 | hot2 6
- rank    4 | canon 268 | section Evening | score 55.0 | col1_hits 1 | hot2 4
- rank    3 | canon 066 | section Midday | score 56.0 | col1_hits 0 | hot2 4
- rank   35 | canon 246 | section Evening | score 31.5 | col1_hits 0 | hot2 3
- rank   35 | canon 008 | section Evening | score 31.5 | col1_hits 0 | hot2 3
- rank   64 | canon 0048 | section Evening | score 26.5 | col1_hits 0 | hot2 3
- rank   28 | canon 006 | section Evening | score 34.5 | col1_hits 0 | hot2 3
- rank   28 | canon 004 | section Evening | score 34.5 | col1_hits 0 | hot2 3
- rank    7 | canon 006 | section Midday | score 52.5 | col1_hits 2 | hot2 3
- rank   17 | canon 366 | section Midday | score 42.0 | col1_hits 0 | hot2 3

## Top families (patterns_families.csv)
- rank 1127 | family 35 | score 4.0 | hot2 0 | section Midday
- rank  522 | family 21 | score 14.0 | hot2 0 | section Midday
- rank  345 | family 11 | score 17.0 | hot2 0 | section Midday
- rank  398 | family 21 | score 16.0 | hot2 0 | section Midday
- rank  522 | family 6 | score 14.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 426 (canon 246): exact_boxed=True exact_straight=True | rank 416/3933 (rank_frac 0.106); Evening 969 (canon 699): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260110)

## Midday winner 426 (canonical 246)
- Stamp (winner_stamp.json): items_total=24 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=24 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=12 family_vtrac_final=0
- Flags (winner_flags.csv): rows=24 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=24 | family_exact_any=0 family_vtrac_any=12 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=24 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=42 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.664643 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 969 (canonical 699)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=6 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=6 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.334643 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 426 (canonical 246)
- Stamp (winner_stamp.json): items_total=84 | exact_any=0 exact_final=0 | vtrac_any=72 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=84 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=36 family_vtrac_final=0
- Flags (winner_flags.csv): rows=84 | exact_any=0 vtrac_any=72 | drop_exact_any=0 drop_vtrac_any=84 | family_exact_any=0 family_vtrac_any=36 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=84 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.237143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 440 | score_v2 15.237143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw4 col 3 | pattern 440 | score_v2 15.087143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 440 | score_v2 15.087143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 440 | score_v2 14.987143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 006 | score_v2 12.664643 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 086 | score_v2 12.334643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 440 | score_v2 12.037143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw4 col 3 | pattern 440 | score_v2 11.887143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 440 | score_v2 11.887143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 440 | score_v2 11.787143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 440 | score_v2 15.237143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 006 | score_v2 12.664643 | tags exact,vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 086 | score_v2 12.334643 | tags exact,vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 440 | score_v2 12.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 006 | score_v2 10.864643 | tags exact,vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 008 | score_v2 10.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 544 | score_v2 10.396234 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 008 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 086 | score_v2 9.134643 | tags exact,vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 544 | score_v2 8.887143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 426 (canon 246): items_total=24 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/42; Evening 969 (canon 699): items_total=12 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/26; Combined 426 (canon 246): items_total=84 exact_any=0 vtrac_any=72 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 440, 006, 086, 440, 006.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260110_033920)

## Top indices (from enhanced JSON)
- index 23 | score 62.06613749999998 | features: presence=44.228637499999984, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 50.2879275 | features: presence=37.43042749999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 4 | score 40.922512499999996 | features: presence=26.0050125, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 40.78911 | features: presence=27.881610000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 32.2642125 | features: presence=20.8667125, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 30.478525 | features: presence=21.221025, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 17.524250000000002 | features: presence=8.716750000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 6 | score 14.364715000000002 | features: presence=9.217215000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 29 | score 12.649835 | features: presence=6.912335000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 32 | score 10.472218333333338 | features: presence=6.953260000000003, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
068, 836, 386, 183, 683, 138, 813, 831, 136, 681

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 426 | index 22 | file PuertoRico4_vtrac22_winner_426_20260110_033441.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 969 | index 25 | file PuertoRico4_vtrac25_winner_969_20260110_033443.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 426 | index 22 rank 26/35 (rank_frac 0.7428571428571429) | score 1.115875 (top 62.06613749999998, ratio 0.017978805270426248, delta 60.95026249999998) | winner_in_index_straights=False | top_index_straights: 471 (0.264)
- winner 969 | index 25 rank 14/35 (rank_frac 0.4) | score 8.8752 (top 62.06613749999998, ratio 0.14299584858168438, delta 53.19093749999998) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 426→idx22 rank 26/35 (frac 0.743); 969→idx25 rank 14/35 (frac 0.400).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 18, 4, 8, 13.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-07)

## Midday winner 426 (canonical 246)
- Top lanes (hot_zones_top_lanes.csv): present | rank 56/207 (rank_frac 0.27053140096618356) | score_mean 17.884 (top 25.054, ratio 0.7138181527899737, delta 7.169999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 969 (canonical 699)
- Top lanes (hot_zones_top_lanes.csv): present | rank 174/207 (rank_frac 0.8405797101449275) | score_mean 15.231 (top 25.054, ratio 0.6079268779436418, delta 9.822999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 279 | vt_triad 335 | score_mean 25.054 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 237 | vt_triad 334 | score_mean 23.068 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 259 | vt_triad 135 | score_mean 21.511 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    4 | triad 267 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    4 | triad 127 | vt_triad 233 | score_mean 21.25 | tags hot20,set1_bonus
- rank    6 | triad 049 | vt_triad 155 | score_mean 21.025 | tags hot16,literal_draw,straight_lane,vertical5,vt_straight
- rank    7 | triad 688 | vt_triad 24 | score_mean 19.963 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 116 | vt_triad 22 | score_mean 19.831 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 166 | vt_triad 22 | score_mean 19.762 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 359 | vt_triad 145 | score_mean 19.657 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 426 (canon 246): rank 56/207 (rank_frac 0.271) ratio_to_top=0.7138181527899737; Evening 969 (canon 699): rank 174/207 (rank_frac 0.841) ratio_to_top=0.6079268779436418
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

Aux draws snapshot dir: `sharepacks/2026-01-07/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-07/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=998 head=972, 732, 359, 529, 917
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-07/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=999 head=732, 529, 144, 451, 098
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-07/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=999 head=972, 359, 917, 913, 643

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=11 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=64), P2:6 (gap=15), P3:6 (gap=27)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=64)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 206: score=44.15442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 266: score=43.65665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 286: score=41.68634285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=40.152571428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 216: score=39.97342857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 236: score=39.38822857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 200: score=36.90694285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 260: score=36.40916428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 806: score=35.21992857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 866: score=34.72215 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=997 sev=B
- 447: ds=988 sev=B
- 000: ds=736 sev=B
- 039: ds=724 sev=B
- 466: ds=720 sev=B
- 677: ds=698 sev=B
- 577: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=68 sev=purple
  - 77: ds=67 sev=purple
  - 99: ds=58 sev=purple
  - 11: ds=52 sev=purple
  - 55: ds=33 sev=purple
  - 33: ds=28 sev=purple
  - 66: ds=27 sev=purple
  - 88: ds=20 sev=-
  - 00: ds=18 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 47: ds=176 sev=red
  - 24: ds=90 sev=red
  - 48: ds=54 sev=blue
  - 56: ds=47 sev=blue
  - 05: ds=45 sev=blue
  - 28: ds=40 sev=blue
  - 06: ds=27 sev=purple
  - 01: ds=24 sev=-
  - 03: ds=24 sev=-
  - 12: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:195, 5:99, 32:93, 26:88, 31:85, 18:59, 34:58, 33:55, 35:53, 16:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=195 fs=18 fl=1 hz=0.025477707006369428, 5:ds=99 fs=27 fl=1 hz=0.0343980343980344, 32:ds=93 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=88 fs=4 fl=2 hz=0.01020408163265306, 31:ds=85 fs=13 fl=3 hz=0.017718715393133997, 18:ds=59 fs=20 fl=0 hz=0.022727272727272728, 34:ds=58 fs=26 fl=0 hz=0.02857142857142857, 33:ds=55 fs=10 fl=0 hz=0.016516516516516516, 35:ds=53 fs=1 fl=2 hz=0.005889281507656065, 16:ds=52 fs=6 fl=2 hz=0.01107419712070875

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=85 flags=purple
- S23: ds=67 flags=blue+purple
- S26: ds=58 flags=blue+purple
- S8: ds=52 flags=purple
- S6: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '6', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 059: score=4 tags=FLT,MIR,RS
  - 149: score=4 tags=FLT,MIR,RS
  - 167: score=4 tags=FLT,MIR,RS
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 257: score=3 tags=MIR,RS
  - 347: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=62 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=32), P2:1 (gap=28), P3:6 (gap=13)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 206: score=44.15442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 266: score=43.65665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 286: score=41.68634285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=40.152571428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 216: score=39.97342857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 236: score=39.38822857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 200: score=36.90694285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 260: score=36.40916428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 806: score=35.21992857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 866: score=34.72215 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=962 sev=B
- 299: ds=953 sev=B
- 003: ds=944 sev=B
- 077: ds=930 sev=B
- 333: ds=879 sev=B
- 555: ds=853 sev=B
- 088: ds=824 sev=B
- 888: ds=818 sev=B
- 666: ds=803 sev=B
- 447: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=109 sev=red
  - 22: ds=82 sev=blue
  - 11: ds=58 sev=purple
  - 99: ds=42 sev=purple
  - 77: ds=33 sev=purple
  - 33: ds=27 sev=purple
  - 88: ds=24 sev=-
  - 55: ds=16 sev=-
  - 66: ds=13 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 47: ds=115 sev=red
  - 24: ds=61 sev=red
  - 38: ds=46 sev=blue
  - 03: ds=45 sev=blue
  - 04: ds=45 sev=blue
  - 35: ds=43 sev=blue
  - 48: ds=35 sev=purple
  - 19: ds=34 sev=purple
  - 18: ds=31 sev=purple
  - 13: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:99, 10:97, 26:93, 3:86, 16:58, 23:53, 15:51, 5:49, 32:46, 31:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=99 fs=16 fl=2 hz=0.020809248554913295, 10:ds=97 fs=20 fl=3 hz=0.026376146788990827, 26:ds=93 fs=7 fl=2 hz=0.011682242990654207, 3:ds=86 fs=31 fl=0 hz=0.03506787330316742, 16:ds=58 fs=4 fl=2 hz=0.009695290858725763, 23:ds=53 fs=31 fl=1 hz=0.034782608695652174, 15:ds=51 fs=25 fl=0 hz=0.026939655172413795, 5:ds=49 fs=28 fl=0 hz=0.03181818181818182, 32:ds=46 fs=2 fl=1 hz=0.006112469437652812, 31:ds=42 fs=22 fl=1 hz=0.024338624338624337

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=45 flags=purple
- S25: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=2 last_repeat_gap=4 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=32), P2:2 (gap=34), P3:6 (gap=24)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 206: score=44.15442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 266: score=43.65665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 286: score=41.68634285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=40.152571428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 216: score=39.97342857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 236: score=39.38822857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 200: score=36.90694285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 260: score=36.40916428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 806: score=35.21992857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 866: score=34.72215 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=994 sev=B
- 579: ds=975 sev=B
- 114: ds=919 sev=B
- 555: ds=858 sev=B
- 888: ds=766 sev=B
- 067: ds=755 sev=B
- 446: ds=742 sev=B
- 259: ds=740 sev=B
- 224: ds=726 sev=B
- 449: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=146 sev=red
  - 44: ds=142 sev=red
  - 77: ds=44 sev=purple
  - 66: ds=35 sev=purple
  - 22: ds=34 sev=purple
  - 99: ds=29 sev=purple
  - 11: ds=26 sev=purple
  - 33: ds=14 sev=-
  - 88: ds=10 sev=-
  - 00: ds=9 sev=-
- non_repeating:
  - 25: ds=102 sev=red
  - 47: ds=88 sev=red
  - 45: ds=72 sev=red
  - 26: ds=65 sev=red
  - 24: ds=45 sev=blue
  - 05: ds=41 sev=blue
  - 56: ds=41 sev=blue
  - 23: ds=32 sev=purple
  - 89: ds=29 sev=purple
  - 48: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:451, 32:166, 4:120, 10:107, 31:95, 5:85, 33:71, 27:68, 1:60, 30:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=451 fs=5 fl=1 hz=0.01662049861495845, 32:ds=166 fs=6 fl=1 hz=0.009987515605493134, 4:ds=120 fs=23 fl=2 hz=0.03071253071253071, 10:ds=107 fs=16 fl=2 hz=0.0234375, 31:ds=95 fs=18 fl=3 hz=0.02394526795895097, 5:ds=85 fs=18 fl=2 hz=0.022446689113355782, 33:ds=71 fs=12 fl=1 hz=0.017361111111111112, 27:ds=68 fs=18 fl=1 hz=0.02358490566037736, 1:ds=60 fs=4 fl=4 hz=0.00909090909090909, 30:ds=45 fs=42 fl=0 hz=0.044823906083244394

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=78 flags=purple
- S24: ds=69 flags=purple
- S23: ds=49 flags=blue+purple
- S16: ds=44 flags=red+purple
- S12: ds=40 flags=purple

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
- 447 -> combined:988(B); midday:742(B)
- 555 -> evening:858(B); midday:853(B)
- 888 -> evening:766(B); midday:818(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:45(blue); evening:41(blue)
- 11 -> combined:52(purple); evening:26(purple); midday:58(purple)
- 22 -> combined:68(purple); evening:34(purple); midday:82(blue)
- 24 -> combined:90(red); evening:45(blue); midday:61(red)
- 33 -> combined:28(purple); midday:27(purple)
- 47 -> combined:176(red); evening:88(red); midday:115(red)
- 48 -> combined:54(blue); evening:27(purple); midday:35(purple)
- 55 -> combined:33(purple); evening:146(red)
- 56 -> combined:47(blue); evening:41(blue)
- 66 -> combined:27(purple); evening:35(purple)
- 77 -> combined:67(purple); evening:44(purple); midday:33(purple)
- 99 -> combined:58(purple); evening:29(purple); midday:42(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.910857142857143)[R1,XVAR-Cons(CEM)], 8(2.476357142857143)[R2,XVAR-Cons(CE)], 3(1.2225)[R2,Double-Pressure], 1(1.0553)[R2,Double-Pressure], 0(0.22728571428571429)[R3,Swap]
- P2: 0(3.2169999999999996)[R2,XVAR-Cons(CM)], 6(2.7192214285714287)[R1,XVAR-Cons(CE)], 8(1.7489142857142856)[R3,XVAR-Cons(CM)], 2(1.715142857142857)[R1,Double-Pressure], 1(1.536)[R1,Double-Pressure]
- P3: 6(8.02657142857143)[R1,XVAR-Cons(CEM)], 0(3.2790857142857144)[R2,Mirror-Echo], 1(0.5869428571428571)[R3,Mirror-Echo], 4(0.3970999999999999)[R2], 5(0.3314285714285714)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=64), P2:6(gap=15), P3:6(gap=27); top cartesian candidates: 206, 266, 286, 226, 216.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '6', '8'], 'pairs': {'remaining_count': 1}}; top candidates: 059, 149, 167, 014, 023.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 447→combined:988(B),midday:742(B); 555→midday:853(B),evening:858(B); 888→midday:818(B),evening:766(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:195, 5:99, 32:93, 26:88, 31:85.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=426 Evening=969; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 246 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 699 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 426 (canon 246): box `246` covers winner `426` (boxed hit).
  - Evening winner 969 (canon 699): box `699` covers winner `969` (boxed hit).
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
