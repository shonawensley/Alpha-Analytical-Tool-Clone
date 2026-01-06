# Master Validation Run Report — NorthCarolina4 — results 2026-01-01 (history workbook ~ 2025-12-31)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-01/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-01/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-01/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-01/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-01/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-01/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-01/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac19_winner_416_20260105_053414.html`
- `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_053_20260105_053415.html`

Winners JSON files:
- `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac19_winner_416_20260105_053414.json`
- `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac4_winner_053_20260105_053415.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-01/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 416 (canon 146): exact_boxed=True exact_straight=True | rank 6060/6134 (rank_frac 0.988); Evening 053 (canon 035): exact_boxed=True exact_straight=True | rank 204/6134 (rank_frac 0.033)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 416 idx19 (rank 27/35, frac 0.771), 053 idx4 (rank 2/35, frac 0.057)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — NorthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-01)

## Midday winner 416 (canonical 146)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=316 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 6060/6134 (rank_frac 0.9879360939028367) | score 7.0 (top 42.0, ratio 0.16666666666666666, delta 35.0) | section Evening, Set Set3, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why straight|cov1|mirror
- Compound (patterns_compound.csv): rank 1600/1629 (rank_frac 0.9821976672805403) | score 7.0 (top 108.0, ratio 0.06481481481481481, delta 101.0) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 0 | why nan
- Families (patterns_families.csv): count 90 | rank 1/1672 (rank_frac 0.0005980861244019139) | score 38.0 (top 38.0, ratio 1.0, delta 0.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=14

## Evening winner 053 (canonical 035)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=39 | exact_boxed=17 | exact_straight=14 | vt_boxed=17
- Scores (patterns_scores.csv): rank 204/6134 (rank_frac 0.03325725464623411) | score 27.0 (top 42.0, ratio 0.6428571428571429, delta 15.0) | section Evening, Set Set1, Draw Draw2, Col 1, hot 2, vt_straight 0.0 | why boxed|cov4|hp_repeat2|vstr2|mirror|hot2|dom_last|perm3|draw_chain5
- Compound (patterns_compound.csv): rank 61/1629 (rank_frac 0.0374462860650706) | score 47.0 (top 108.0, ratio 0.4351851851851852, delta 61.0) | section Evening, col1_hits 5, hot2 5, set_chain 1, draw_chain 5 | why draw_chain5|col1x5|hot1x1|hot2x5|vstrx3
- Families (patterns_families.csv): count 13 | rank 1210/1672 (rank_frac 0.7236842105263158) | score 12.5 (top 38.0, ratio 0.32894736842105265, delta 25.5) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=27

## Top compound candidates (patterns_compound.csv)
- rank   32 | canon 0029 | section Midday | score 62.5 | col1_hits 5 | hot2 11
- rank   32 | canon 0039 | section Midday | score 62.5 | col1_hits 6 | hot2 11
- rank    6 | canon 003 | section Midday | score 85.5 | col1_hits 6 | hot2 11
- rank   11 | canon 229 | section Midday | score 80.5 | col1_hits 7 | hot2 11
- rank    5 | canon 223 | section Midday | score 93.0 | col1_hits 7 | hot2 11
- rank   12 | canon 009 | section Midday | score 79.0 | col1_hits 7 | hot2 11
- rank   24 | canon 029 | section Midday | score 66.5 | col1_hits 5 | hot2 11
- rank   32 | canon 00229 | section Midday | score 62.5 | col1_hits 5 | hot2 11
- rank   21 | canon 024 | section Combined | score 72.5 | col1_hits 7 | hot2 11
- rank   20 | canon 0224 | section Combined | score 73.5 | col1_hits 7 | hot2 11

## Top families (patterns_families.csv)
- rank 1668 | family 11 | score 4.0 | hot2 0 | section Midday
- rank 1157 | family 20 | score 13.0 | hot2 0 | section Midday
- rank  115 | family 30 | score 27.5 | hot2 0 | section Midday
- rank   95 | family 27 | score 28.5 | hot2 0 | section Midday
- rank    2 | family 28 | score 37.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 416 (canon 146): exact_boxed=True exact_straight=True | rank 6060/6134 (rank_frac 0.988); Evening 053 (canon 035): exact_boxed=True exact_straight=True | rank 204/6134 (rank_frac 0.033)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260105)

## Midday winner 416 (canonical 146)
- Stamp (winner_stamp.json): items_total=7 | exact_any=1 exact_final=0 | vtrac_any=7 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=7 | exact_any=1 vtrac_any=7 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=1 family_vtrac_any=1 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=7 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.087143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 053 (canonical 035)
- Stamp (winner_stamp.json): items_total=141 | exact_any=11 exact_final=0 | vtrac_any=137 vtrac_final=0 | drop_exact_any=18 drop_exact_final=0 | drop_vtrac_any=20 drop_vtrac_final=0 | family_exact_any=11 family_exact_final=0 | family_vtrac_any=13 family_vtrac_final=0
- Flags (winner_flags.csv): rows=141 | exact_any=11 vtrac_any=137 | drop_exact_any=18 drop_vtrac_any=20 | family_exact_any=11 family_vtrac_any=13 | vt_boxed=22 vt_straight=0
- Hits (winner_hits.csv): rows=141 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=22 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 416 (canonical 146)
- Stamp (winner_stamp.json): items_total=83 | exact_any=3 exact_final=0 | vtrac_any=77 vtrac_final=0 | drop_exact_any=5 drop_exact_final=0 | drop_vtrac_any=56 drop_vtrac_final=0 | family_exact_any=4 family_exact_final=0 | family_vtrac_any=30 family_vtrac_final=0
- Flags (winner_flags.csv): rows=83 | exact_any=3 vtrac_any=77 | drop_exact_any=5 drop_vtrac_any=56 | family_exact_any=4 family_vtrac_any=30 | vt_boxed=83 vt_straight=0
- Hits (winner_hits.csv): rows=83 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=83 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.727143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 224 | score_v2 14.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 224 | score_v2 14.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 224 | score_v2 14.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 224 | score_v2 14.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 224 | score_v2 14.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 224 | score_v2 13.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 922 | score_v2 13.087143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 922 | score_v2 12.837143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 922 | score_v2 12.837143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 922 | score_v2 12.787143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 14.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 922 | score_v2 13.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 922 | score_v2 12.837143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 922 | score_v2 12.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 224 | score_v2 12.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 922 | score_v2 11.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 552 | score_v2 10.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 592 | score_v2 10.587143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 992 | score_v2 10.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 992 | score_v2 10.387143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 416 (canon 146): items_total=7 exact_any=1 vtrac_any=7 | top winner_present=False best_rank=None/12; Evening 053 (canon 035): items_total=141 exact_any=11 vtrac_any=137 | top winner_present=False best_rank=None/12; Combined 416 (canon 146): items_total=83 exact_any=3 vtrac_any=77 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 922, 922, 922, 224.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260105_053643)

## Top indices (from enhanced JSON)
- index 1 | score 104.95573499999996 | features: presence=76.06823499999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 88.33877499999996 | features: presence=63.19127499999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 84.64164999999996 | features: presence=62.88414999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 52.18064999999999 | features: presence=38.703149999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 49.306250000000006 | features: presence=32.298750000000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 46.241302499999996 | features: presence=31.7338025, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 44.5693 | features: presence=29.511800000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 39.9257375 | features: presence=28.2582375, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 32.53979 | features: presence=22.13229, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 11 | score 28.6383 | features: presence=19.7208, cross_section=0.5, set_echo=0.3, first_hit=0.4

## Top straights (from enhanced JSON)
034, 240, 053, 032, 085, 093, 805, 290, 403, 098

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 416 | index 19 | file NorthCarolina4_vtrac19_winner_416_20260105_053414.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 053 | index 4 | file NorthCarolina4_vtrac4_winner_053_20260105_053415.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 416 | index 19 rank 27/35 (rank_frac 0.7714285714285715) | score 1.73975 (top 104.95573499999996, ratio 0.016576035602056435, delta 103.21598499999996) | winner_in_index_straights=False | top_index_straights: (none)
- winner 053 | index 4 rank 2/35 (rank_frac 0.05714285714285714) | score 88.33877499999996 (top 104.95573499999996, ratio 0.8416764934283961, delta 16.616960000000006) | winner_in_index_straights=True | top_index_straights: 053 (20.577), 085 (18.205), 805 (17.936)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 416→idx19 rank 27/35 (frac 0.771); 053→idx4 rank 2/35 (frac 0.057).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 1, 4, 28, 5, 14.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-01)

## Midday winner 416 (canonical 146)
- Top lanes (hot_zones_top_lanes.csv): present | rank 167/200 (rank_frac 0.835) | score_mean 14.408 (top 22.703, ratio 0.6346297846099634, delta 8.295)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 053 (canonical 035)
- Top lanes (hot_zones_top_lanes.csv): present | rank 31/200 (rank_frac 0.155) | score_mean 18.347 (top 22.703, ratio 0.8081310839977096, delta 4.355999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 667 | vt_triad 23 | score_mean 22.703 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight
- rank    2 | triad 469 | vt_triad 255 | score_mean 21.58 | tags hot16,hot20,literal_draw,set1_bonus,straight_lane,vertical1,vt_straight
- rank    3 | triad 257 | vt_triad 133 | score_mean 21.25 | tags hot20,set1_bonus
- rank    3 | triad 027 | vt_triad 133 | score_mean 21.25 | tags hot20,set1_bonus
- rank    5 | triad 005 | vt_triad 11 | score_mean 20.696 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 055 | vt_triad 11 | score_mean 19.916 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 168 | vt_triad 224 | score_mean 19.734 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight
- rank    8 | triad 224 | vt_triad 35 | score_mean 19.657 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3
- rank    9 | triad 003 | vt_triad 14 | score_mean 19.593 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 259 | vt_triad 135 | score_mean 19.45 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 416 (canon 146): rank 167/200 (rank_frac 0.835) ratio_to_top=0.6346297846099634; Evening 053 (canon 035): rank 31/200 (rank_frac 0.155) ratio_to_top=0.8081310839977096
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

Aux draws snapshot dir: `sharepacks/2026-01-01/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=057, 867, 879, 455, 168
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=867, 455, 766, 885, 789
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=057, 879, 168, 911, 391

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=25 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:4 (gap=31), P3:2 (gap=28)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=886 sev=B
- 155: ds=874 sev=B
- 446: ds=870 sev=B
- 445: ds=810 sev=B
- 122: ds=793 sev=B
- 036: ds=789 sev=B
- 555: ds=766 sev=B
- 299: ds=763 sev=B
- 277: ds=755 sev=B
- 112: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=150 sev=red
  - 77: ds=123 sev=red
  - 33: ds=47 sev=purple
  - 99: ds=46 sev=purple
  - 44: ds=44 sev=purple
  - 22: ds=10 sev=-
  - 88: ds=7 sev=-
  - 11: ds=6 sev=-
  - 66: ds=5 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 56: ds=52 sev=blue
  - 27: ds=48 sev=blue
  - 02: ds=42 sev=blue
  - 23: ds=38 sev=blue
  - 09: ds=37 sev=blue
  - 03: ds=36 sev=purple
  - 28: ds=34 sev=purple
  - 04: ds=31 sev=purple
  - 06: ds=31 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:478, 32:331, 1:105, 27:101, 31:92, 15:76, 16:74, 10:64, 4:54, 23:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=478 fs=3 fl=0 hz=0.009389671361502348, 32:ds=331 fs=1 fl=1 hz=0.005405405405405406, 1:ds=105 fs=0 fl=3 hz=0.00625, 27:ds=101 fs=15 fl=2 hz=0.02011173184357542, 31:ds=92 fs=19 fl=3 hz=0.02502844141069397, 15:ds=76 fs=16 fl=2 hz=0.019758507135016465, 16:ds=74 fs=4 fl=1 hz=0.008836524300441826, 10:ds=64 fs=21 fl=2 hz=0.027315914489311165, 4:ds=54 fs=18 fl=2 hz=0.0213903743315508, 23:ds=53 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=86 flags=purple
- S23: ds=70 flags=blue+purple
- S4: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 034: score=2 tags=FLT,PAT
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 123: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=95 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=34), P2:9 (gap=24), P3:2 (gap=37)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=972 sev=B
- 123: ds=947 sev=B
- 446: ds=924 sev=B
- 777: ds=884 sev=B
- 119: ds=849 sev=B
- 222: ds=819 sev=B
- 155: ds=781 sev=B
- 488: ds=775 sev=B
- 177: ds=751 sev=B
- 007: ds=730 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=154 sev=red
  - 00: ds=129 sev=red
  - 77: ds=61 sev=purple
  - 99: ds=49 sev=purple
  - 22: ds=37 sev=purple
  - 33: ds=23 sev=-
  - 11: ds=7 sev=-
  - 88: ds=3 sev=-
  - 66: ds=2 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 48: ds=145 sev=red
  - 25: ds=58 sev=red
  - 07: ds=53 sev=blue
  - 28: ds=45 sev=blue
  - 23: ds=40 sev=blue
  - 26: ds=40 sev=blue
  - 02: ds=37 sev=blue
  - 29: ds=34 sev=purple
  - 56: ds=28 sev=purple
  - 27: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:377, 25:185, 32:165, 35:139, 4:129, 11:104, 31:97, 2:93, 33:76, 12:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=377 fs=1 fl=0 hz=0.005905511811023622, 25:ds=185 fs=15 fl=1 hz=0.02165087956698241, 32:ds=165 fs=3 fl=1 hz=0.007416563658838071, 35:ds=139 fs=0 fl=2 hz=0.005201560468140442, 4:ds=129 fs=12 fl=3 hz=0.017241379310344827, 11:ds=104 fs=50 fl=0 hz=0.056882821387940846, 31:ds=97 fs=25 fl=0 hz=0.02793296089385475, 2:ds=93 fs=13 fl=3 hz=0.018223234624145785, 33:ds=76 fs=21 fl=2 hz=0.025136612021857924, 12:ds=54 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=88 flags=purple
- S20: ds=76 flags=red+purple
- S2: ds=67 flags=purple
- S5: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '2', '3'], 'pairs': {'remaining_count': 1}}
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
- current_index=3 streak=1 max=3 last_repeat_gap=19 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=13), P2:4 (gap=34), P3:3 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=973 sev=B
- 299: ds=930 sev=B
- 223: ds=860 sev=B
- 122: ds=849 sev=B
- 116: ds=826 sev=B
- 039: ds=809 sev=B
- 377: ds=797 sev=B
- 277: ds=783 sev=B
- 188: ds=771 sev=B
- 557: ds=770 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=178 sev=red
  - 55: ds=121 sev=red
  - 33: ds=120 sev=red
  - 77: ds=79 sev=blue
  - 00: ds=75 sev=blue
  - 66: ds=37 sev=purple
  - 99: ds=23 sev=-
  - 44: ds=22 sev=-
  - 22: ds=5 sev=-
  - 11: ds=3 sev=-
- non_repeating:
  - 45: ds=98 sev=red
  - 34: ds=39 sev=blue
  - 59: ds=38 sev=blue
  - 04: ds=34 sev=purple
  - 06: ds=28 sev=purple
  - 08: ds=27 sev=purple
  - 58: ds=27 sev=purple
  - 56: ds=26 sev=purple
  - 17: ds=24 sev=-
  - 27: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:257, 26:239, 13:204, 32:178, 1:146, 23:115, 5:96, 17:95, 27:52, 31:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=257 fs=18 fl=0 hz=0.024896265560165977, 26:ds=239 fs=1 fl=2 hz=0.006666666666666667, 13:ds=204 fs=20 fl=0 hz=0.025284450063211127, 32:ds=178 fs=2 fl=2 hz=0.007416563658838071, 1:ds=146 fs=2 fl=3 hz=0.007434944237918215, 23:ds=115 fs=14 fl=3 hz=0.019384264538198404, 5:ds=96 fs=15 fl=2 hz=0.020809248554913295, 17:ds=95 fs=29 fl=0 hz=0.03553921568627451, 27:ds=52 fs=22 fl=3 hz=0.027085590465872156, 31:ds=46 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=89 flags=purple
- S0: ds=75 flags=blue+purple
- S4: ds=64 flags=blue+purple
- S22: ds=44 flags=purple
- S2: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=4 tags=FLT,MIR,RS
  - 034: score=4 tags=FLT,PAT,RS
  - 124: score=4 tags=FLT,PAT,RS
  - 349: score=4 tags=FLT,MIR,RS
  - 016: score=3 tags=MIR,RS
  - 169: score=3 tags=MIR,RS
  - 259: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=MIR,RS
  - 457: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:789(B); evening:723(B)
- 122 -> combined:793(B); evening:849(B)
- 155 -> combined:874(B); midday:781(B)
- 277 -> combined:755(B); evening:783(B)
- 299 -> combined:763(B); evening:930(B)
- 338 -> combined:886(B); midday:710(B)
- 446 -> combined:870(B); midday:924(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:150(red); evening:75(blue); midday:129(red)
- 02 -> combined:42(blue); midday:37(blue)
- 04 -> combined:31(purple); evening:34(purple)
- 06 -> combined:31(purple); evening:28(purple)
- 23 -> combined:38(blue); midday:40(blue)
- 25 -> combined:26(purple); midday:58(red)
- 27 -> combined:48(blue); midday:25(purple)
- 28 -> combined:34(purple); midday:45(blue)
- 29 -> combined:28(purple); midday:34(purple)
- 33 -> combined:47(purple); evening:120(red)
- 34 -> combined:29(purple); evening:39(blue)
- 44 -> combined:44(purple); midday:154(red)
- 56 -> combined:52(blue); evening:26(purple); midday:28(purple)
- 77 -> combined:123(red); evening:79(blue); midday:61(purple)
- 99 -> combined:46(purple); midday:49(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(3.845285714285714)[R1,XVAR-Cons(CE)], 2(3.1565714285714286)[R3,XVAR-Cons(CM)], 0(1.2016)[R2,Double-Pressure], 7(0.879)[R2,Double-Pressure], 3(0.40902142857142854)[R3,Swap]
- P2: 4(8.528642857142858)[R1,XVAR-Cons(CEM)], 0(3.7263)[R2,XVAR-Cons(CE)], 3(1.9172142857142858)[R3,XVAR-Cons(CE)], 9(1.5290714285714284)[R1,Mirror-Echo], 2(0.2746642857142857)[R3,Swap]
- P3: 2(7.413099999999999)[R1,XVAR-Cons(CEM)], 3(3.060142857142857)[R3,XVAR-Cons(CE)], 0(2.785535714285714)[R2,XVAR-Cons(CM)], 8(1.0879999999999999)[R2,Double-Pressure], 5(1.0671)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_31.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=26), P2:4(gap=31), P3:2(gap=28); top cartesian candidates: 242, 542, 202, 543, 540.
- Q3: Blackapple: score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '3'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 023, 024, 025.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:789(B),evening:723(B); 122→combined:793(B),evening:849(B); 155→combined:874(B),midday:781(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:478, 32:331, 1:105, 27:101, 31:92.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=416 Evening=053; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 146 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 035 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 416 (canon 146): box `146` covers winner `416` (boxed hit).
  - Evening winner 053 (canon 035): box `035` covers winner `053` (boxed hit).
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
