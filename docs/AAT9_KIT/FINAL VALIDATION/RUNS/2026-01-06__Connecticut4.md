# Master Validation Run Report — Connecticut4 — results 2026-01-06 (history workbook ~ 2026-01-05)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-06/Connecticut4/`
- Winners lens: `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-06/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-06/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-06/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-06/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-06/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-06/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_737_20260107_052253.html`
- `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/Connecticut4_vtrac7_winner_576_20260107_052251.html`

Winners JSON files:
- `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/Connecticut4_vtrac27_winner_737_20260107_052253.json`
- `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/Connecticut4_vtrac7_winner_576_20260107_052251.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-06/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 576 (canon 567): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 737 (canon 377): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 737 idx27 (rank 7/35, frac 0.200), 576 idx7 (rank 29/35, frac 0.829)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — Connecticut4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-06)

## Midday winner 576 (canonical 567)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=48 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 15 | rank 826/1342 (rank_frac 0.6154992548435171) | score 13.0 (top 35.5, ratio 0.36619718309859156, delta 22.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=21
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 737 (canonical 377)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=88 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 55 | rank 224/1342 (rank_frac 0.16691505216095381) | score 21.5 (top 35.5, ratio 0.6056338028169014, delta 14.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=8
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    4 | canon 2244 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    1 | canon 224 | section Combined | score 91.0 | col1_hits 7 | hot2 11
- rank    1 | canon 244 | section Combined | score 91.0 | col1_hits 7 | hot2 11
- rank    8 | canon 468 | section Midday | score 69.5 | col1_hits 6 | hot2 11
- rank    7 | canon 448 | section Combined | score 71.0 | col1_hits 4 | hot2 9
- rank   13 | canon 22448 | section Combined | score 59.0 | col1_hits 4 | hot2 8
- rank   26 | canon 2248 | section Combined | score 51.0 | col1_hits 4 | hot2 8
- rank   10 | canon 2249 | section Evening | score 65.0 | col1_hits 6 | hot2 8
- rank    6 | canon 229 | section Evening | score 71.5 | col1_hits 6 | hot2 8
- rank    5 | canon 224 | section Evening | score 80.0 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1336 | family 4 | score 4.0 | hot2 0 | section Midday
- rank  630 | family 25 | score 15.0 | hot2 2 | section Midday
- rank 1139 | family 6 | score 9.0 | hot2 0 | section Midday
- rank 1196 | family 29 | score 8.5 | hot2 0 | section Midday
- rank 1286 | family 5 | score 6.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 576 (canon 567): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 737 (canon 377): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260107)

## Midday winner 576 (canonical 567)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 737 (canonical 377)
- Stamp (winner_stamp.json): items_total=122 | exact_any=0 exact_final=0 | vtrac_any=108 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=14 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=122 | exact_any=0 vtrac_any=108 | drop_exact_any=0 drop_vtrac_any=14 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=50 vt_straight=0
- Hits (winner_hits.csv): rows=122 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=50 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 576 (canonical 567)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=16.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 224 | score_v2 16.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 224 | score_v2 16.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 224 | score_v2 16.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 224 | score_v2 16.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 224 | score_v2 15.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 922 | score_v2 14.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 224 | score_v2 14.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 448 | score_v2 14.110476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 922 | score_v2 14.037143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 224 | score_v2 13.977143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 16.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 922 | score_v2 14.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 224 | score_v2 14.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 448 | score_v2 14.110476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 224 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 592 | score_v2 13.065714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 922 | score_v2 12.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 992 | score_v2 12.615714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 992 | score_v2 12.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 924 | score_v2 12.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 576 (canon 567): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/20; Evening 737 (canon 377): items_total=122 exact_any=0 vtrac_any=108 | top winner_present=False best_rank=None/20; Combined 576 (canon 567): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 922, 224, 448, 224.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260107_052520)

## Top indices (from enhanced JSON)
- index 30 | score 66.64623749999997 | features: presence=45.94873749999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 61.18901 | features: presence=35.48151, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 57.35458749999999 | features: presence=39.95708749999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 32.517675000000004 | features: presence=21.470175000000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 28 | score 31.4786 | features: presence=21.8511, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 27.409875 | features: presence=16.982374999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 27 | score 27.07355 | features: presence=19.31605, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 25.910854999999994 | features: presence=16.293355, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 19.7227 | features: presence=11.495199999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 33 | score 18.463450000000005 | features: presence=8.115950000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
824, 684, 284, 486, 847, 248, 864, 874, 487, 784

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 737 | index 27 | file Connecticut4_vtrac27_winner_737_20260107_052253.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 576 | index 7 | file Connecticut4_vtrac7_winner_576_20260107_052251.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 737 | index 27 rank 7/35 (rank_frac 0.2) | score 27.07355 (top 66.64623749999997, ratio 0.40622773341105733, delta 39.57268749999997) | winner_in_index_straights=False | top_index_straights: 872 (6.648), 782 (6.142)
- winner 576 | index 7 rank 29/35 (rank_frac 0.8285714285714286) | score 0.671875 (top 66.64623749999997, ratio 0.010081214262095446, delta 65.97436249999997) | winner_in_index_straights=False | top_index_straights: 170 (0.06), 701 (0.06)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 737→idx27 rank 7/35 (frac 0.200); 576→idx7 rank 29/35 (frac 0.829).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 30, 24, 31, 21, 28.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-06)

## Midday winner 576 (canonical 567)
- Top lanes (hot_zones_top_lanes.csv): present | rank 40/210 (rank_frac 0.19047619047619047) | score_mean 18.908 (top 23.08, ratio 0.8192374350086656, delta 4.171999999999997)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 737 (canonical 377)
- Top lanes (hot_zones_top_lanes.csv): present | rank 71/210 (rank_frac 0.3380952380952381) | score_mean 18.08 (top 23.08, ratio 0.7833622183708838, delta 5.0)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 066 | vt_triad 12 | score_mean 23.08 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 017 | vt_triad 123 | score_mean 21.975 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    3 | triad 227 | vt_triad 33 | score_mean 21.85 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 113 | vt_triad 24 | score_mean 21.797 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 277 | vt_triad 33 | score_mean 21.542 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 668 | vt_triad 24 | score_mean 21.355 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 118 | vt_triad 24 | score_mean 21.254 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    8 | triad 388 | vt_triad 44 | score_mean 21.07 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    9 | triad 278 | vt_triad 334 | score_mean 20.947 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 237 | vt_triad 334 | score_mean 20.826 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 576 (canon 567): rank 40/210 (rank_frac 0.190) ratio_to_top=0.8192374350086656; Evening 737 (canon 377): rank 71/210 (rank_frac 0.338) ratio_to_top=0.7833622183708838
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

Aux draws snapshot dir: `sharepacks/2026-01-06/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-06

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-06/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-05.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-06/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=660, 071, 311, 569, 181
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-06/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=071, 569, 533, 970, 228
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-06/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=660, 311, 181, 356, 109

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=6 streak=1 max=2 last_repeat_gap=41 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=44), P2:4 (gap=17), P3:4 (gap=30)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=44.09955 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=44.049749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 724: score=39.86718571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 704: score=39.26110714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 747: score=37.876078571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.82627857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.593807142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 754: score=37.29047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 727: score=33.64371428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=33.03763571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=893 sev=B
- 129: ds=875 sev=B
- 288: ds=863 sev=B
- 149: ds=845 sev=B
- 445: ds=777 sev=B
- 114: ds=747 sev=B
- 069: ds=711 sev=B
- 888: ds=709 sev=B
- 688: ds=705 sev=B
- 133: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=95 sev=blue
  - 99: ds=76 sev=blue
  - 00: ds=46 sev=purple
  - 88: ds=32 sev=purple
  - 77: ds=21 sev=-
  - 55: ds=14 sev=-
  - 22: ds=9 sev=-
  - 33: ds=5 sev=-
  - 11: ds=2 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 48: ds=82 sev=red
  - 78: ds=78 sev=red
  - 57: ds=77 sev=red
  - 49: ds=76 sev=red
  - 25: ds=45 sev=blue
  - 37: ds=38 sev=blue
  - 58: ds=27 sev=purple
  - 68: ds=27 sev=purple
  - 14: ds=25 sev=purple
  - 15: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:411, 32:178, 25:164, 29:137, 4:135, 15:123, 31:112, 34:107, 3:92, 35:76

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=411 fs=1 fl=2 hz=0.01098901098901099, 32:ds=178 fs=5 fl=2 hz=0.011267605633802818, 25:ds=164 fs=22 fl=2 hz=0.029055690072639227, 29:ds=137 fs=24 fl=1 hz=0.03071253071253071, 4:ds=135 fs=21 fl=2 hz=0.027677496991576414, 15:ds=123 fs=9 fl=4 hz=0.015531660692951015, 31:ds=112 fs=32 fl=0 hz=0.03665521191294387, 34:ds=107 fs=15 fl=2 hz=0.01951779563719862, 3:ds=92 fs=27 fl=0 hz=0.030337078651685393, 35:ds=76 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=86 flags=purple
- S24: ds=78 flags=blue+purple
- S22: ds=76 flags=purple
- S25: ds=68 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=77 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=30), P2:0 (gap=30), P3:4 (gap=34)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=44.09955 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=44.049749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 724: score=39.86718571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 704: score=39.26110714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 747: score=37.876078571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.82627857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.593807142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 754: score=37.29047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 727: score=33.64371428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=33.03763571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=883 sev=B
- 478: ds=864 sev=B
- 459: ds=859 sev=B
- 159: ds=815 sev=B
- 099: ds=796 sev=B
- 127: ds=787 sev=B
- 559: ds=729 sev=B
- 004: ds=688 sev=B
- 155: ds=684 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=95 sev=blue
  - 88: ds=55 sev=purple
  - 44: ds=47 sev=purple
  - 55: ds=32 sev=purple
  - 00: ds=28 sev=purple
  - 66: ds=15 sev=-
  - 77: ds=10 sev=-
  - 11: ds=7 sev=-
  - 22: ds=4 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 78: ds=73 sev=red
  - 13: ds=60 sev=red
  - 49: ds=47 sev=blue
  - 19: ds=46 sev=blue
  - 48: ds=43 sev=blue
  - 57: ds=38 sev=blue
  - 37: ds=27 sev=purple
  - 08: ds=25 sev=purple
  - 36: ds=23 sev=-
  - 25: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:205, 25:106, 31:95, 32:93, 18:90, 3:78, 29:68, 4:67, 15:61, 34:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=205 fs=3 fl=0 hz=0.008565310492505354, 25:ds=106 fs=21 fl=1 hz=0.025974025974025976, 31:ds=95 fs=20 fl=2 hz=0.024608501118568233, 32:ds=93 fs=3 fl=4 hz=0.009510869565217392, 18:ds=90 fs=23 fl=1 hz=0.026519337016574582, 3:ds=78 fs=22 fl=2 hz=0.02631578947368421, 29:ds=68 fs=18 fl=2 hz=0.023446658851113716, 4:ds=67 fs=26 fl=0 hz=0.02931228861330327, 15:ds=61 fs=23 fl=1 hz=0.02564102564102564, 34:ds=53 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=89 flags=blue+purple
- S24: ds=86 flags=blue+purple
- S23: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=6 streak=1 max=3 last_repeat_gap=2 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=22), P2:9 (gap=19), P3:2 (gap=17)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=44.09955 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=44.049749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 724: score=39.86718571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 704: score=39.26110714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 747: score=37.876078571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=37.82627857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.593807142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 754: score=37.29047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 727: score=33.64371428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=33.03763571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=910 sev=B
- 668: ds=907 sev=B
- 399: ds=906 sev=B
- 044: ds=902 sev=B
- 133: ds=899 sev=B
- 145: ds=871 sev=B
- 677: ds=778 sev=B
- 333: ds=773 sev=B
- 112: ds=725 sev=B
- 344: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=117 sev=red
  - 22: ds=74 sev=blue
  - 99: ds=38 sev=purple
  - 77: ds=32 sev=purple
  - 33: ds=24 sev=-
  - 00: ds=23 sev=-
  - 88: ds=16 sev=-
  - 55: ds=7 sev=-
  - 11: ds=1 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 57: ds=53 sev=blue
  - 69: ds=51 sev=blue
  - 23: ds=48 sev=blue
  - 25: ds=46 sev=blue
  - 07: ds=45 sev=blue
  - 48: ds=41 sev=blue
  - 78: ds=39 sev=blue
  - 49: ds=38 sev=blue
  - 15: ds=31 sev=purple
  - 02: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:316, 26:144, 4:127, 34:96, 32:89, 25:82, 29:70, 15:69, 2:59, 31:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=316 fs=2 fl=1 hz=0.005961251862891207, 26:ds=144 fs=3 fl=1 hz=0.008680555555555556, 4:ds=127 fs=18 fl=1 hz=0.02243211334120425, 34:ds=96 fs=14 fl=3 hz=0.019144144144144143, 32:ds=89 fs=2 fl=0 hz=0.008450704225352114, 25:ds=82 fs=21 fl=0 hz=0.023836549375709424, 29:ds=70 fs=27 fl=0 hz=0.030100334448160536, 15:ds=69 fs=15 fl=1 hz=0.019698725376593278, 2:ds=59 fs=23 fl=2 hz=0.028344671201814057, 31:ds=56 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=96 flags=blue+purple
- S8: ds=73 flags=red+purple
- S20: ds=56 flags=purple
- S3: ds=43 flags=blue+purple
- S24: ds=39 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:701(B); evening:899(B)
- 445 -> combined:777(B); evening:694(B)
- 459 -> combined:686(B); midday:859(B)
- 888 -> combined:709(B); evening:702(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:46(purple); midday:28(purple)
- 15 -> combined:25(purple); evening:31(purple)
- 25 -> combined:45(blue); evening:46(blue)
- 37 -> combined:38(blue); midday:27(purple)
- 44 -> combined:95(blue); evening:117(red); midday:47(purple)
- 48 -> combined:82(red); evening:41(blue); midday:43(blue)
- 49 -> combined:76(red); evening:38(blue); midday:47(blue)
- 57 -> combined:77(red); evening:53(blue); midday:38(blue)
- 78 -> combined:78(red); evening:39(blue); midday:73(red)
- 88 -> combined:32(purple); midday:55(purple)
- 99 -> combined:76(blue); evening:38(purple); midday:95(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.562571428571427)[R1,XVAR-Cons(CEM)], 8(1.184)[R2,Double-Pressure], 9(1.1179999999999999)[R2,Double-Pressure], 3(0.9343999999999999)[R2,Double-Pressure], 5(0.2746642857142857)[R3,Swap]
- P2: 4(3.977442857142857)[R1,Mirror-Echo], 9(3.9276428571428568)[R2,Mirror-Echo], 2(1.7450785714285715)[R3,XVAR-Cons(CE)], 0(1.6389999999999998)[R1,Mirror-Echo], 8(0.9717)[R2,Double-Pressure]
- P3: 4(7.5595357142857145)[R1,XVAR-Cons(CEM)], 7(1.7440714285714287)[R3,XVAR-Cons(CM)], 2(1.2075714285714285)[R1,Double-Pressure], 8(1.0344)[R2,Double-Pressure], 5(0.986)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-05.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=44), P2:4(gap=17), P3:4(gap=30); top cartesian candidates: 744, 794, 724, 704, 747.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 014, 023, 024, 025.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:701(B),evening:899(B); 445→combined:777(B),evening:694(B); 459→combined:686(B),midday:859(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:411, 32:178, 25:164, 29:137, 4:135.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=576 Evening=737; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 567 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 377 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 576 (canon 567): box `567` covers winner `576` (boxed hit).
  - Evening winner 737 (canon 377): box `377` covers winner `737` (boxed hit).
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
