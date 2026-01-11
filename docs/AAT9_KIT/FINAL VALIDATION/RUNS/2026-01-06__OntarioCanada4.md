# Master Validation Run Report — OntarioCanada4 — results 2026-01-06 (history workbook ~ 2026-01-05)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-06/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-06/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-06/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-06/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-06/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-06/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-06/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac33_winner_433_20260107_052315.html`
- `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_111_20260107_052315.html`

Winners JSON files:
- `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac33_winner_433_20260107_052315.json`
- `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtracNone_winner_111_20260107_052315.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-06/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 111 (canon 111): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 433 (canon 334): exact_boxed=True exact_straight=True | rank 3679/4691 (rank_frac 0.784)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 433 idx33 (rank 31/35, frac 0.886)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
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

### 2.Stable — OntarioCanada4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-06)

## Midday winner 111 (canonical 111)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=64 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 27 | rank 248/1340 (rank_frac 0.18507462686567164) | score 21.0 (top 35.5, ratio 0.5915492957746479, delta 14.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=0
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 433 (canonical 334)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=5 | family_rows=None | exact_boxed=5 | exact_straight=5 | vt_boxed=5
- Scores (patterns_scores.csv): rank 3679/4691 (rank_frac 0.784267746749094) | score 10.0 (top 36.0, ratio 0.2777777777777778, delta 26.0) | section Midday, Set Set1, Draw Draw7, Col 1, hot 0, vt_straight 2.0 | why straight|cov1|double_mirror|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 646/1688 (rank_frac 0.38270142180094785) | score 15.0 (top 95.5, ratio 0.15706806282722513, delta 80.5) | section Midday, col1_hits 1, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|col1x1|vstrx1|dblmirrorx4
- Families (patterns_families.csv): not present
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=19

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 477 | section Midday | score 95.5 | col1_hits 8 | hot2 11
- rank    7 | canon 1477 | section Midday | score 65.5 | col1_hits 6 | hot2 8
- rank    4 | canon 177 | section Midday | score 71.0 | col1_hits 6 | hot2 8
- rank   17 | canon 234 | section Midday | score 51.5 | col1_hits 4 | hot2 8
- rank   11 | canon 014 | section Combined | score 58.0 | col1_hits 4 | hot2 7
- rank    6 | canon 1477 | section Combined | score 68.0 | col1_hits 2 | hot2 6
- rank    7 | canon 144 | section Combined | score 65.5 | col1_hits 6 | hot2 6
- rank   11 | canon 044 | section Combined | score 58.0 | col1_hits 5 | hot2 6
- rank   28 | canon 346 | section Midday | score 46.0 | col1_hits 4 | hot2 6
- rank   28 | canon 1367 | section Midday | score 46.0 | col1_hits 4 | hot2 6

## Top families (patterns_families.csv)
- rank 1271 | family 9 | score 6.0 | hot2 0 | section Midday
- rank 1271 | family 16 | score 6.0 | hot2 0 | section Midday
- rank  466 | family 28 | score 17.5 | hot2 0 | section Midday
- rank  499 | family 17 | score 17.0 | hot2 0 | section Midday
- rank  583 | family 12 | score 16.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 111 (canon 111): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 433 (canon 334): exact_boxed=True exact_straight=True | rank 3679/4691 (rank_frac 0.784)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260107)

## Midday winner 111 (canonical 111)
- Stamp (winner_stamp.json): items_total=106 | exact_any=0 exact_final=0 | vtrac_any=106 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=49 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=45 family_vtrac_final=0
- Flags (winner_flags.csv): rows=106 | exact_any=0 vtrac_any=106 | drop_exact_any=0 drop_vtrac_any=49 | family_exact_any=0 family_vtrac_any=45 | vt_boxed=106 vt_straight=0
- Hits (winner_hits.csv): rows=106 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=106 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.364643 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 433 (canonical 334)
- Stamp (winner_stamp.json): items_total=2 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=2 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=2 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 111 (canonical 111)
- Stamp (winner_stamp.json): items_total=334 | exact_any=0 exact_final=0 | vtrac_any=334 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=197 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=218 family_vtrac_final=0
- Flags (winner_flags.csv): rows=334 | exact_any=0 vtrac_any=334 | drop_exact_any=0 drop_vtrac_any=197 | family_exact_any=0 family_vtrac_any=218 | vt_boxed=324 vt_straight=0
- Hits (winner_hits.csv): rows=334 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=324 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 440 | score_v2 14.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 440 | score_v2 14.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 440 | score_v2 13.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 401 | score_v2 12.880476 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 6 | pattern 554 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 12.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 5 | pattern 554 | score_v2 11.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 247 | score_v2 11.364643 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 244 | score_v2 11.337143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 244 | score_v2 11.187143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 440 | score_v2 14.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 401 | score_v2 12.880476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 554 | score_v2 12.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 247 | score_v2 11.364643 | tags exact,vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 244 | score_v2 11.337143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 224 | score_v2 11.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 241 | score_v2 10.997143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 440 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 246 | score_v2 10.447143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 111 (canon 111): items_total=106 exact_any=0 vtrac_any=106 | top winner_present=False best_rank=None/18; Evening 433 (canon 334): items_total=2 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/20; Combined 111 (canon 111): items_total=334 exact_any=0 vtrac_any=334 | top winner_present=False best_rank=None/32
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 440, 401, 554, 559, 247.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260107_052527)

## Top indices (from enhanced JSON)
- index 28 | score 98.29292499999994 | features: presence=69.98542499999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 63.468249999999976 | features: presence=42.76074999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 31.4852625 | features: presence=20.737762500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 27.89391666666667 | features: presence=18.929750000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 26 | score 26.660875000000008 | features: presence=15.395250000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 26.096866666666664 | features: presence=15.652699999999992, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 23.989108333333334 | features: presence=13.648275000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 18.527220000000003 | features: presence=9.54972, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 5 | score 14.270508333333334 | features: presence=6.45155, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 3 | score 14.221500000000002 | features: presence=7.764000000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
247, 724, 417, 712, 217, 714, 051, 015, 041, 014

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 433 | index 33 | file OntarioCanada4_vtrac33_winner_433_20260107_052315.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 111 | index None | file OntarioCanada4_vtracNone_winner_111_20260107_052315.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 433 | index 33 rank 31/35 (rank_frac 0.8857142857142857) | score 0.630375 (top 98.29292499999994, ratio 0.006413228622507677, delta 97.66254999999994) | winner_in_index_straights=False | top_index_straights: (none)
- winner 111 | index None: not found in indices_ranked
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 433→idx33 rank 31/35 (frac 0.886).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 20, 22, 2, 26.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-06)

## Midday winner 111 (canonical 111)
- Top lanes (hot_zones_top_lanes.csv): not present
- Per-lane (hot_zones_per_lane.csv): not present
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Coverage gaps: missing_from_top_lanes, missing_from_per_lane
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Evening winner 433 (canonical 334)
- Top lanes (hot_zones_top_lanes.csv): present | rank 36/212 (rank_frac 0.16981132075471697) | score_mean 18.623 (top 25.535, ratio 0.7293127080477776, delta 6.911999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 555 | vt_triad 1 | score_mean 25.535 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 000 | vt_triad 1 | score_mean 23.5 | tags hot20,set1_bonus,superhot_set1
- rank    3 | triad 277 | vt_triad 33 | score_mean 23.36 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 227 | vt_triad 33 | score_mean 23.195 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 238 | vt_triad 344 | score_mean 22.146 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 247 | vt_triad 335 | score_mean 22.054 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 279 | vt_triad 335 | score_mean 22.046 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 267 | vt_triad 233 | score_mean 21.782 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 127 | vt_triad 233 | score_mean 21.414 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 688 | vt_triad 24 | score_mean 21.097 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 111 (canon 111): rank N/A (rank_frac N/A) ratio_to_top=None; Evening 433 (canon 334): rank 36/212 (rank_frac 0.170) ratio_to_top=0.7293127080477776
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

Aux draws snapshot dir: `sharepacks/2026-01-06/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-06

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-06/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-05.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=797, 555, 382, 958, 032
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=555, 958, 968, 053, 528
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-06/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=797, 382, 032, 816, 546

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=58 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=32), P2:0 (gap=13), P3:4 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=44.51489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 124: score=43.314978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 171: score=41.72574071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 121: score=40.52582642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=38.48417857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=38.32546428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.76219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=37.613992857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 170: score=37.55722142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 674: score=36.83016428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=929 sev=B
- 039: ds=785 sev=B
- 333: ds=756 sev=B
- 188: ds=729 sev=B
- 266: ds=715 sev=B
- 477: ds=713 sev=B
- 126: ds=705 sev=B
- 669: ds=700 sev=B
- 007: ds=690 sev=B
- 005: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=131 sev=red
  - 11: ds=46 sev=purple
  - 88: ds=40 sev=purple
  - 44: ds=31 sev=purple
  - 99: ds=19 sev=-
  - 66: ds=18 sev=-
  - 33: ds=17 sev=-
  - 00: ds=15 sev=-
  - 55: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 01: ds=66 sev=red
  - 15: ds=63 sev=red
  - 17: ds=57 sev=red
  - 12: ds=43 sev=blue
  - 24: ds=41 sev=blue
  - 26: ds=41 sev=blue
  - 67: ds=38 sev=blue
  - 36: ds=35 sev=purple
  - 48: ds=34 sev=purple
  - 08: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:341, 16:295, 17:167, 20:145, 33:91, 12:90, 26:85, 34:72, 8:68, 7:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=341 fs=1 fl=0 hz=0.005698005698005698, 16:ds=295 fs=2 fl=0 hz=0.006329113924050633, 17:ds=167 fs=19 fl=1 hz=0.024242424242424242, 20:ds=145 fs=13 fl=2 hz=0.01847290640394089, 33:ds=91 fs=23 fl=1 hz=0.026578073089700997, 12:ds=90 fs=44 fl=0 hz=0.04932735426008968, 26:ds=85 fs=2 fl=1 hz=0.006075334143377886, 34:ds=72 fs=14 fl=2 hz=0.019698725376593278, 8:ds=68 fs=39 fl=2 hz=0.044956140350877194, 7:ds=52 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=83 flags=purple
- S4: ds=77 flags=purple
- S3: ds=66 flags=blue+purple
- S16: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 028: score=2 tags=RS
  - 037: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=21 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=30), P2:7 (gap=27), P3:0 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=44.51489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 124: score=43.314978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 171: score=41.72574071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 121: score=40.52582642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=38.48417857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=38.32546428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.76219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=37.613992857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 170: score=37.55722142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 674: score=36.83016428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=999 sev=B
- 333: ds=982 sev=B
- 255: ds=949 sev=B
- 355: ds=914 sev=B
- 466: ds=835 sev=B
- 446: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=65 sev=purple
  - 11: ds=33 sev=purple
  - 77: ds=26 sev=purple
  - 88: ds=22 sev=-
  - 66: ds=17 sev=-
  - 44: ds=15 sev=-
  - 99: ds=9 sev=-
  - 33: ds=8 sev=-
  - 00: ds=7 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 34: ds=74 sev=red
  - 07: ds=71 sev=red
  - 16: ds=57 sev=red
  - 39: ds=45 sev=blue
  - 37: ds=40 sev=blue
  - 67: ds=40 sev=blue
  - 48: ds=37 sev=blue
  - 01: ds=33 sev=purple
  - 15: ds=31 sev=purple
  - 45: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:170, 34:165, 16:147, 27:102, 12:99, 17:83, 20:72, 19:57, 33:45, 26:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=170 fs=4 fl=3 hz=0.010432190760059612, 34:ds=165 fs=8 fl=4 hz=0.014423076923076924, 16:ds=147 fs=3 fl=0 hz=0.007462686567164179, 27:ds=102 fs=15 fl=2 hz=0.0189520624303233, 12:ds=99 fs=45 fl=0 hz=0.05079006772009029, 17:ds=83 fs=29 fl=2 hz=0.033879781420765025, 20:ds=72 fs=24 fl=3 hz=0.029315960912052113, 19:ds=57 fs=20 fl=2 hz=0.023732470334412083, 33:ds=45 fs=18 fl=2 hz=0.021119324181626188, 26:ds=42 fs=0 fl=3 hz=0.005376344086021506

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=77 flags=purple
- S1: ds=66 flags=blue+purple
- S5: ds=64 flags=purple
- S9: ds=54 flags=purple
- S21: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=58 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=17), P2:6 (gap=19), P3:9 (gap=43)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 174: score=44.51489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 124: score=43.314978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 171: score=41.72574071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 121: score=40.52582642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=38.48417857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 104: score=38.32546428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 184: score=37.76219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=37.613992857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 170: score=37.55722142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 674: score=36.83016428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=906 sev=B
- 113: ds=857 sev=B
- 378: ds=850 sev=B
- 566: ds=839 sev=B
- 199: ds=831 sev=B
- 899: ds=809 sev=B
- 126: ds=805 sev=B
- 559: ds=800 sev=B
- 477: ds=789 sev=B
- 558: ds=755 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=235 sev=red
  - 22: ds=66 sev=purple
  - 00: ds=53 sev=purple
  - 44: ds=36 sev=purple
  - 11: ds=23 sev=-
  - 99: ds=21 sev=-
  - 88: ds=20 sev=-
  - 33: ds=18 sev=-
  - 66: ds=9 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 36: ds=78 sev=red
  - 24: ds=62 sev=red
  - 89: ds=56 sev=red
  - 15: ds=55 sev=blue
  - 78: ds=54 sev=blue
  - 49: ds=48 sev=blue
  - 57: ds=45 sev=blue
  - 09: ds=35 sev=purple
  - 01: ds=33 sev=purple
  - 12: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:431, 1:346, 16:197, 26:129, 17:107, 20:98, 3:77, 23:70, 33:68, 31:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=431 fs=0 fl=2 hz=0.005366726296958855, 1:ds=346 fs=0 fl=0 hz=0.0, 16:ds=197 fs=3 fl=1 hz=0.007853403141361256, 26:ds=129 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=107 fs=13 fl=3 hz=0.018626309662398137, 20:ds=98 fs=15 fl=2 hz=0.01925254813137033, 3:ds=77 fs=15 fl=4 hz=0.02092511013215859, 23:ds=70 fs=25 fl=2 hz=0.03085714285714286, 33:ds=68 fs=27 fl=1 hz=0.030803080308030802, 31:ds=64 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S2: ds=77 flags=blue+purple
- S4: ds=75 flags=purple
- S25: ds=64 flags=purple
- S20: ds=57 flags=purple
- S9: ds=55 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:705(B); evening:805(B)
- 128 -> combined:929(B); evening:906(B)
- 226 -> combined:667(B); evening:707(B)
- 333 -> combined:756(B); midday:982(B)
- 477 -> combined:713(B); evening:789(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:66(red); evening:33(purple); midday:33(purple)
- 11 -> combined:46(purple); midday:33(purple)
- 12 -> combined:43(blue); evening:33(purple)
- 15 -> combined:63(red); evening:55(blue); midday:31(purple)
- 17 -> combined:57(red); evening:29(purple); midday:28(purple)
- 22 -> combined:131(red); evening:66(purple); midday:65(purple)
- 24 -> combined:41(blue); evening:62(red)
- 26 -> combined:41(blue); evening:26(purple)
- 36 -> combined:35(purple); evening:78(red)
- 44 -> combined:31(purple); evening:36(purple)
- 48 -> combined:34(purple); midday:37(blue)
- 57 -> combined:27(purple); evening:45(blue)
- 67 -> combined:38(blue); midday:40(blue)
- 78 -> combined:27(purple); evening:54(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(8.310792857142857)[R1,Mirror-Echo], 6(3.1260642857142855)[R2,Mirror-Echo], 2(3.049371428571429)[R3,XVAR-Cons(CM)], 4(1.1075714285714284)[R1,Double-Pressure], 7(0.7058285714285715)[R3,Mirror-Echo]
- P2: 7(3.798)[R2,Mirror-Echo], 2(2.5980857142857143)[R3,Mirror-Echo], 6(1.2672857142857143)[R1,Double-Pressure], 0(1.1085714285714285)[R1,Double-Pressure], 8(0.5452999999999999)[R2,Mirror-Echo]
- P3: 4(6.4061)[R1,XVAR-Cons(CEM)], 1(3.5567)[R2,XVAR-Cons(CE)], 0(2.9484285714285714)[R3,XVAR-Cons(CM)], 9(1.7610357142857143)[R1,Mirror-Echo], 2(1.0761999999999998)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-05.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=32), P2:0(gap=13), P3:4(gap=31); top cartesian candidates: 174, 124, 171, 121, 164.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6'], 'pairs': {'remaining_count': 0}}; top candidates: 019, 046, 127, 136, 145.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:705(B),evening:805(B); 128→combined:929(B),evening:906(B); 226→combined:667(B),evening:707(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:341, 16:295, 17:167, 20:145, 33:91.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=111 Evening=433; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 111 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 334 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 111 (canon 111): box `111` covers winner `111` (boxed hit).
  - Evening winner 433 (canon 334): box `334` covers winner `433` (boxed hit).
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
