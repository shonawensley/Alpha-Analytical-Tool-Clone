# Master Validation Run Report — Pennsylvania4 — results 2026-01-01 (history workbook ~ 2025-12-31)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-01/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-01/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-01/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-01/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-01/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-01/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-01/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac27_winner_322_20260105_053422.html`
- `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac29_winner_328_20260105_053423.html`

Winners JSON files:
- `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac27_winner_322_20260105_053422.json`
- `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac29_winner_328_20260105_053423.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 322 (canon 223): exact_boxed=True exact_straight=True | rank 798/5150 (rank_frac 0.155); Evening 328 (canon 238): exact_boxed=True exact_straight=True | rank 4061/5150 (rank_frac 0.789)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 322 idx27 (rank 6/35, frac 0.171), 328 idx29 (rank 8/35, frac 0.229)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — Pennsylvania4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-01)

## Midday winner 322 (canonical 223)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=9 | family_rows=77 | exact_boxed=9 | exact_straight=9 | vt_boxed=9
- Scores (patterns_scores.csv): rank 798/5150 (rank_frac 0.1549514563106796) | score 17.0 (top 35.0, ratio 0.4857142857142857, delta 18.0) | section Combined, Set Set1, Draw Draw5, Col 2, hot 2, vt_straight 2.0 | why straight|cov2|hp_repeat2|vstr2|hot2|double_mirror|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 221/1700 (rank_frac 0.13) | score 23.0 (top 69.5, ratio 0.33093525179856115, delta 46.5) | section Combined, col1_hits 0, hot2 1, set_chain 1, draw_chain 2 | why draw_chain2|hot2x1|vstrx3|dblmirrorx3
- Families (patterns_families.csv): count 40 | rank 225/1350 (rank_frac 0.16666666666666666) | score 21.0 (top 32.0, ratio 0.65625, delta 11.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=6

## Evening winner 328 (canonical 238)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=223 | exact_boxed=2 | exact_straight=2 | vt_boxed=2
- Scores (patterns_scores.csv): rank 4061/5150 (rank_frac 0.7885436893203883) | score 10.0 (top 35.0, ratio 0.2857142857142857, delta 25.0) | section Combined, Set Set1, Draw Draw5, Col 3, hot 0, vt_straight 2.0 | why straight|cov1|mirror|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 1146/1700 (rank_frac 0.6741176470588235) | score 11.5 (top 69.5, ratio 0.16546762589928057, delta 58.0) | section Combined, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|vstrx1
- Families (patterns_families.csv): count 75 | rank 56/1350 (rank_frac 0.04148148148148148) | score 26.0 (top 32.0, ratio 0.8125, delta 6.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=15

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 359 | section Midday | score 69.5 | col1_hits 6 | hot2 8
- rank   10 | canon 079 | section Combined | score 55.0 | col1_hits 5 | hot2 8
- rank    9 | canon 378 | section Evening | score 56.5 | col1_hits 4 | hot2 7
- rank   18 | canon 057 | section Combined | score 47.0 | col1_hits 3 | hot2 6
- rank   31 | canon 0557 | section Combined | score 42.5 | col1_hits 3 | hot2 6
- rank    6 | canon 138 | section Evening | score 63.5 | col1_hits 1 | hot2 6
- rank   15 | canon 579 | section Midday | score 49.0 | col1_hits 3 | hot2 6
- rank    4 | canon 559 | section Combined | score 64.0 | col1_hits 5 | hot2 6
- rank    7 | canon 055 | section Combined | score 57.0 | col1_hits 5 | hot2 6
- rank   12 | canon 0559 | section Combined | score 53.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1341 | family 16 | score 4.0 | hot2 0 | section Midday
- rank  479 | family 21 | score 17.0 | hot2 0 | section Midday
- rank  899 | family 14 | score 12.0 | hot2 0 | section Midday
- rank 1094 | family 25 | score 9.0 | hot2 0 | section Midday
- rank 1141 | family 7 | score 8.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 322 (canon 223): exact_boxed=True exact_straight=True | rank 798/5150 (rank_frac 0.155); Evening 328 (canon 238): exact_boxed=True exact_straight=True | rank 4061/5150 (rank_frac 0.789)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260105)

## Midday winner 322 (canonical 223)
- Stamp (winner_stamp.json): items_total=101 | exact_any=0 exact_final=0 | vtrac_any=101 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=9 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=101 | exact_any=0 vtrac_any=101 | drop_exact_any=0 drop_vtrac_any=9 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=45 vt_straight=0
- Hits (winner_hits.csv): rows=101 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=45 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.527143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 328 (canonical 238)
- Stamp (winner_stamp.json): items_total=99 | exact_any=0 exact_final=0 | vtrac_any=99 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=21 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=99 | exact_any=0 vtrac_any=99 | drop_exact_any=0 drop_vtrac_any=21 | family_exact_any=0 family_vtrac_any=4 | vt_boxed=20 vt_straight=0
- Hits (winner_hits.csv): rows=99 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=20 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 322 (canonical 223)
- Stamp (winner_stamp.json): items_total=319 | exact_any=0 exact_final=0 | vtrac_any=319 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=26 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=319 | exact_any=0 vtrac_any=319 | drop_exact_any=0 drop_vtrac_any=26 | family_exact_any=0 family_vtrac_any=4 | vt_boxed=76 vt_straight=0
- Hits (winner_hits.csv): rows=319 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=76 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=18.477143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 18.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 18.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 18.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 559 | score_v2 18.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 18.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 18.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 18.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 559 | score_v2 17.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 559 | score_v2 17.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 559 | score_v2 17.777143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 18.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 14.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 12.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 599 | score_v2 11.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 11.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 594 | score_v2 11.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 599 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 559 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 593 | score_v2 10.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 994 | score_v2 10.708571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 322 (canon 223): items_total=101 exact_any=0 vtrac_any=101 | top winner_present=False best_rank=None/24; Evening 328 (canon 238): items_total=99 exact_any=0 vtrac_any=99 | top winner_present=False best_rank=None/28; Combined 322 (canon 223): items_total=319 exact_any=0 vtrac_any=319 | top winner_present=False best_rank=None/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 599, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_053646)

## Top indices (from enhanced JSON)
- index 18 | score 61.90063750000001 | features: presence=35.433137499999994, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 20 | score 25.054730000000003 | features: presence=16.35723, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 17 | score 24.873685000000005 | features: presence=16.856185000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 24.4731375 | features: presence=12.585637499999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 21 | score 22.965087500000003 | features: presence=12.8975875, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 27 | score 19.596655000000002 | features: presence=10.269155000000001, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 6 | score 19.490950000000005 | features: presence=11.363450000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 29 | score 12.9515725 | features: presence=5.964072500000002, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 7 | score 10.512400000000001 | features: presence=5.014900000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 2 | score 8.801608333333334 | features: presence=4.32265, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
186, 681, 187, 871, 617, 167, 867, 718, 817, 687

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 322 | index 27 | file Pennsylvania4_vtrac27_winner_322_20260105_053422.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 328 | index 29 | file Pennsylvania4_vtrac29_winner_328_20260105_053423.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 322 | index 27 rank 6/35 (rank_frac 0.17142857142857143) | score 19.596655000000002 (top 61.90063750000001, ratio 0.3165824423052186, delta 42.303982500000004) | winner_in_index_straights=False | top_index_straights: (none)
- winner 328 | index 29 rank 8/35 (rank_frac 0.22857142857142856) | score 12.9515725 (top 61.90063750000001, ratio 0.20923164967404412, delta 48.94906500000001) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 322→idx27 rank 6/35 (frac 0.171); 328→idx29 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 18, 20, 17, 23, 21.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-01)

## Midday winner 322 (canonical 223)
- Top lanes (hot_zones_top_lanes.csv): present | rank 158/203 (rank_frac 0.7783251231527094) | score_mean 15.215 (top 25.1, ratio 0.6061752988047808, delta 9.885000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 328 (canonical 238)
- Top lanes (hot_zones_top_lanes.csv): present | rank 93/203 (rank_frac 0.458128078817734) | score_mean 16.666 (top 25.1, ratio 0.66398406374502, delta 8.434000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 25.1 | tags hot16,hot20,literal_draw,set1_bonus,straight_lane,vertical1,vt_straight
- rank    2 | triad 006 | vt_triad 12 | score_mean 20.633 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vt_straight
- rank    3 | triad 499 | vt_triad 55 | score_mean 20.55 | tags col1,hot16,hot20,hot4,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_straight
- rank    4 | triad 168 | vt_triad 224 | score_mean 20.376 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 011 | vt_triad 12 | score_mean 20.185 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 117 | vt_triad 23 | score_mean 19.897 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    7 | triad 113 | vt_triad 24 | score_mean 19.831 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    8 | triad 122 | vt_triad 23 | score_mean 19.823 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    9 | triad 339 | vt_triad 45 | score_mean 19.821 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 046 | vt_triad 125 | score_mean 19.816 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 322 (canon 223): rank 158/203 (rank_frac 0.778) ratio_to_top=0.6061752988047808; Evening 328 (canon 238): rank 93/203 (rank_frac 0.458) ratio_to_top=0.66398406374502
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

Aux draws snapshot dir: `sharepacks/2026-01-01/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=221, 684, 173, 186, 460
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=684, 186, 239, 502, 264
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=221, 173, 460, 422, 065

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=21 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=33), P2:4 (gap=26), P3:7 (gap=13)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=994 sev=B
- 666: ds=992 sev=B
- 159: ds=880 sev=B
- 007: ds=877 sev=B
- 088: ds=841 sev=B
- 008: ds=819 sev=B
- 444: ds=795 sev=B
- 039: ds=770 sev=B
- 355: ds=760 sev=B
- 344: ds=689 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=137 sev=red
  - 77: ds=76 sev=blue
  - 88: ds=75 sev=blue
  - 44: ds=69 sev=purple
  - 66: ds=63 sev=purple
  - 55: ds=40 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=23 sev=-
  - 99: ds=10 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 78: ds=70 sev=red
  - 03: ds=45 sev=blue
  - 07: ds=43 sev=blue
  - 35: ds=36 sev=purple
  - 69: ds=34 sev=purple
  - 36: ds=31 sev=purple
  - 09: ds=30 sev=purple
  - 34: ds=29 sev=purple
  - 38: ds=29 sev=purple
  - 19: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:279, 26:236, 16:94, 27:70, 7:62, 6:57, 13:55, 19:51, 10:46, 31:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=279 fs=2 fl=1 hz=0.007380073800738007, 26:ds=236 fs=0 fl=1 hz=0.003898635477582846, 16:ds=94 fs=3 fl=2 hz=0.007371007371007371, 27:ds=70 fs=11 fl=4 hz=0.01722158438576349, 7:ds=62 fs=36 fl=1 hz=0.03965702036441586, 6:ds=57 fs=22 fl=1 hz=0.02454642475987193, 13:ds=55 fs=21 fl=1 hz=0.024553571428571428, 19:ds=51 fs=21 fl=3 hz=0.025695931477516063, 10:ds=46 fs=23 fl=2 hz=0.02676659528907923, 31:ds=42 fs=22 fl=2 hz=0.02531645569620253

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=88 flags=purple
- S20: ds=75 flags=purple
- S6: ds=54 flags=purple
- S25: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=32 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=26), P2:7 (gap=21), P3:5 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=976 sev=B
- 288: ds=963 sev=B
- 255: ds=934 sev=B
- 668: ds=916 sev=B
- 199: ds=864 sev=B
- 499: ds=790 sev=B
- 399: ds=773 sev=B
- 039: ds=761 sev=B
- 448: ds=750 sev=B
- 005: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=185 sev=red
  - 99: ds=132 sev=red
  - 77: ds=75 sev=blue
  - 33: ds=68 sev=purple
  - 22: ds=61 sev=purple
  - 88: ds=37 sev=purple
  - 44: ds=34 sev=purple
  - 66: ds=31 sev=purple
  - 11: ds=12 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 59: ds=78 sev=red
  - 79: ds=72 sev=red
  - 12: ds=47 sev=blue
  - 78: ds=45 sev=blue
  - 06: ds=42 sev=blue
  - 35: ds=39 sev=blue
  - 56: ds=31 sev=purple
  - 69: ds=29 sev=purple
  - 13: ds=24 sev=-
  - 57: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:374, 1:359, 34:213, 16:171, 15:162, 32:139, 35:116, 27:83, 28:61, 5:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=374 fs=0 fl=0 hz=0.0, 1:ds=359 fs=2 fl=2 hz=0.009124087591240877, 34:ds=213 fs=19 fl=1 hz=0.02631578947368421, 16:ds=171 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=162 fs=23 fl=0 hz=0.029411764705882353, 32:ds=139 fs=3 fl=1 hz=0.006720430107526881, 35:ds=116 fs=1 fl=1 hz=0.0035587188612099642, 27:ds=83 fs=22 fl=2 hz=0.028605482717520857, 28:ds=61 fs=26 fl=2 hz=0.02997858672376874, 5:ds=46 fs=18 fl=2 hz=0.022175290390707498

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=93 flags=red+purple
- S22: ds=78 flags=purple
- S23: ds=66 flags=purple
- S3: ds=60 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 567: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 579: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 679: score=2 tags=FLT,PAT
  - 789: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 017: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=62 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=28), P2:1 (gap=34), P3:6 (gap=18)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=972 sev=B
- 009: ds=930 sev=B
- 255: ds=888 sev=B
- 138: ds=828 sev=B
- 117: ds=811 sev=B
- 158: ds=773 sev=B
- 344: ds=766 sev=B
- 199: ds=757 sev=B
- 112: ds=717 sev=B
- 277: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=127 sev=red
  - 33: ds=69 sev=purple
  - 44: ds=40 sev=purple
  - 77: ds=38 sev=purple
  - 66: ds=36 sev=purple
  - 11: ds=27 sev=purple
  - 55: ds=20 sev=-
  - 00: ds=14 sev=-
  - 99: ds=5 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 68: ds=85 sev=red
  - 07: ds=62 sev=red
  - 15: ds=50 sev=blue
  - 38: ds=49 sev=blue
  - 23: ds=46 sev=blue
  - 03: ds=44 sev=blue
  - 78: ds=35 sev=purple
  - 19: ds=34 sev=purple
  - 28: ds=33 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:616, 23:155, 26:118, 18:115, 13:64, 29:57, 33:49, 16:47, 30:46, 24:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=616 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=155 fs=17 fl=2 hz=0.025165562913907286, 26:ds=118 fs=2 fl=1 hz=0.0056657223796034, 18:ds=115 fs=23 fl=2 hz=0.02910360884749709, 13:ds=64 fs=20 fl=1 hz=0.024881516587677725, 29:ds=57 fs=16 fl=3 hz=0.020540540540540542, 33:ds=49 fs=19 fl=3 hz=0.023255813953488372, 16:ds=47 fs=5 fl=3 hz=0.009523809523809525, 30:ds=46 fs=35 fl=1 hz=0.03829787234042553, 24:ds=43 fs=37 fl=0 hz=0.04048140043763676

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=88 flags=blue+purple
- S1: ds=73 flags=blue+purple
- S24: ds=56 flags=blue+purple
- S3: ds=44 flags=purple
- S20: ds=38 flags=purple
- S6: ds=27 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:770(B); midday:761(B)
- 066 -> combined:994(B); midday:739(B)
- 199 -> evening:757(B); midday:864(B)
- 255 -> evening:888(B); midday:934(B)
- 344 -> combined:689(B); evening:766(B)
- 444 -> combined:795(B); evening:972(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:45(blue); evening:44(blue)
- 07 -> combined:43(blue); evening:62(red)
- 11 -> combined:25(purple); evening:27(purple)
- 19 -> combined:27(purple); evening:34(purple)
- 33 -> combined:137(red); evening:69(purple); midday:68(purple)
- 35 -> combined:36(purple); midday:39(blue)
- 38 -> combined:29(purple); evening:49(blue)
- 44 -> combined:69(purple); evening:40(purple); midday:34(purple)
- 55 -> combined:40(purple); midday:185(red)
- 66 -> combined:63(purple); evening:36(purple); midday:31(purple)
- 69 -> combined:34(purple); midday:29(purple)
- 77 -> combined:76(blue); evening:38(purple); midday:75(blue)
- 78 -> combined:70(red); evening:35(purple); midday:45(blue)
- 88 -> combined:75(blue); evening:127(red); midday:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.681914285714286)[R1,Mirror-Echo], 7(5.976942857142857)[R3,XVAR-Cons(CEM)], 8(4.724428571428572)[R2,Mirror-Echo], 4(1.1389)[R2,Double-Pressure]
- P2: 1(3.270714285714286)[R3,XVAR-Cons(CE)], 4(3.102114285714286)[R1,XVAR-Cons(CM)], 5(2.719535714285714)[R2,XVAR-Cons(CE)], 7(1.4979999999999998)[R1,Mirror-Echo], 2(1.3312)[R2,Mirror-Echo]
- P3: 5(2.9894285714285713)[R3,XVAR-Cons(CM)], 7(2.6026214285714286)[R1,XVAR-Cons(CE)], 1(1.2225)[R2,Double-Pressure], 6(1.2074285714285713)[R1,Double-Pressure], 9(0.9834999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_31.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:3(gap=33), P2:4(gap=26), P3:7(gap=13); top cartesian candidates: 315, 345, 317, 717, 355.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 015, 019, 025, 029, 035.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:770(B),midday:761(B); 066→combined:994(B),midday:739(B); 199→midday:864(B),evening:757(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:279, 26:236, 16:94, 27:70, 7:62.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=322 Evening=328; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 223 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 238 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 322 (canon 223): box `223` covers winner `322` (boxed hit).
  - Evening winner 328 (canon 238): box `238` covers winner `328` (boxed hit).
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
