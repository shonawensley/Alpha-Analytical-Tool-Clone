# Master Validation Run Report — SouthCarolina4 — results 2026-01-03 (history workbook ~ 2026-01-02)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-03/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-03/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-03/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-03/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-03/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-03/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-03/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac24_winner_189_20260105_054606.html`
- `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac2_winner_051_20260105_054608.html`

Winners JSON files:
- `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac24_winner_189_20260105_054606.json`
- `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac2_winner_051_20260105_054608.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 189 (canon 189): exact_boxed=True exact_straight=True | rank 273/4616 (rank_frac 0.059); Evening 051 (canon 015): exact_boxed=True exact_straight=True | rank 23/4616 (rank_frac 0.005)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 189 idx24 (rank 10/35, frac 0.286), 051 idx2 (rank 16/35, frac 0.457)
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

### 2.Stable — SouthCarolina4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-03)

## Midday winner 189 (canonical 189)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=33 | family_rows=95 | exact_boxed=33 | exact_straight=29 | vt_boxed=33
- Scores (patterns_scores.csv): rank 273/4616 (rank_frac 0.0591421143847487) | score 18.5 (top 43.5, ratio 0.42528735632183906, delta 25.0) | section Evening, Set Set3, Draw Draw1, Col 3, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat4|hot1|perm3|hidden3v|set_chain3
- Compound (patterns_compound.csv): rank 45/1641 (rank_frac 0.027422303473491772) | score 34.5 (top 73.0, ratio 0.4726027397260274, delta 38.5) | section Midday, col1_hits 4, hot2 4, set_chain 1, draw_chain 4 | why draw_chain4|col1x4|hot1x1|hot2x4|vstrx6
- Families (patterns_families.csv): count 46 | rank 94/1401 (rank_frac 0.06709493219129194) | score 23.0 (top 32.0, ratio 0.71875, delta 9.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=119

## Evening winner 051 (canonical 015)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=7 | family_rows=417 | exact_boxed=7 | exact_straight=1 | vt_boxed=7
- Scores (patterns_scores.csv): rank 23/4616 (rank_frac 0.00498266897746967) | score 26.5 (top 43.5, ratio 0.6091954022988506, delta 17.0) | section Evening, Set Set1, Draw Draw1, Col 1, hot 2, vt_straight 0.0 | why boxed|cov4|hp_repeat2|vstr2|mirror|hot2|dom_last|perm2|hidden3v|set_chain2|draw_chain3
- Compound (patterns_compound.csv): rank 14/1641 (rank_frac 0.008531383302864107) | score 42.5 (top 73.0, ratio 0.5821917808219178, delta 30.5) | section Evening, col1_hits 2, hot2 3, set_chain 2, draw_chain 3 | why set_chain2|draw_chain3|col1x2|hot1x4|hot2x3|vstrx1
- Families (patterns_families.csv): count 69 | rank 227/1401 (rank_frac 0.16202712348322626) | score 20.5 (top 32.0, ratio 0.640625, delta 11.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=13

## Top compound candidates (patterns_compound.csv)
- rank   16 | canon 079 | section Midday | score 41.5 | col1_hits 1 | hot2 5
- rank    3 | canon 677 | section Combined | score 63.0 | col1_hits 4 | hot2 4
- rank    2 | canon 002 | section Combined | score 68.5 | col1_hits 2 | hot2 4
- rank   54 | canon 256 | section Combined | score 33.0 | col1_hits 2 | hot2 4
- rank   11 | canon 178 | section Midday | score 46.0 | col1_hits 4 | hot2 4
- rank   30 | canon 089 | section Midday | score 38.0 | col1_hits 0 | hot2 4
- rank   45 | canon 189 | section Midday | score 34.5 | col1_hits 4 | hot2 4
- rank   37 | canon 078 | section Midday | score 36.5 | col1_hits 0 | hot2 4
- rank   29 | canon 378 | section Midday | score 38.5 | col1_hits 0 | hot2 4
- rank   39 | canon 039 | section Midday | score 36.0 | col1_hits 0 | hot2 4

## Top families (patterns_families.csv)
- rank 1398 | family 11 | score 4.0 | hot2 0 | section Midday
- rank  376 | family 21 | score 18.5 | hot2 0 | section Midday
- rank 1166 | family 25 | score 10.0 | hot2 0 | section Midday
- rank 1291 | family 27 | score 8.5 | hot2 0 | section Midday
- rank 1306 | family 14 | score 8.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 189 (canon 189): exact_boxed=True exact_straight=True | rank 273/4616 (rank_frac 0.059); Evening 051 (canon 015): exact_boxed=True exact_straight=True | rank 23/4616 (rank_frac 0.005)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260105)

## Midday winner 189 (canonical 189)
- Stamp (winner_stamp.json): items_total=62 | exact_any=4 exact_final=0 | vtrac_any=35 vtrac_final=0 | drop_exact_any=19 drop_exact_final=0 | drop_vtrac_any=36 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=7 family_vtrac_final=0
- Flags (winner_flags.csv): rows=62 | exact_any=4 vtrac_any=35 | drop_exact_any=19 drop_vtrac_any=36 | family_exact_any=0 family_vtrac_any=7 | vt_boxed=16 vt_straight=0
- Hits (winner_hits.csv): rows=62 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=16 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.328571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 051 (canonical 015)
- Stamp (winner_stamp.json): items_total=166 | exact_any=50 exact_final=0 | vtrac_any=91 vtrac_final=0 | drop_exact_any=100 drop_exact_final=0 | drop_vtrac_any=124 drop_vtrac_final=0 | family_exact_any=13 family_exact_final=0 | family_vtrac_any=57 family_vtrac_final=0
- Flags (winner_flags.csv): rows=166 | exact_any=50 vtrac_any=91 | drop_exact_any=100 drop_vtrac_any=124 | family_exact_any=13 family_vtrac_any=57 | vt_boxed=28 vt_straight=0
- Hits (winner_hits.csv): rows=166 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=28 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=True | winner_best_rank=40 | winner_rank_fraction=2.2222222222222223 | winner_score_v2=8.227143 top_score_v2=12.227143 | winner_score_ratio_to_top=0.6728589826748571 winner_score_delta_from_top=4.0
- Reducer scores present: True

## Combined winner 189 (canonical 189)
- Stamp (winner_stamp.json): items_total=141 | exact_any=42 exact_final=0 | vtrac_any=114 vtrac_final=0 | drop_exact_any=35 drop_exact_final=0 | drop_vtrac_any=55 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=141 | exact_any=42 vtrac_any=114 | drop_exact_any=35 drop_vtrac_any=55 | family_exact_any=0 family_vtrac_any=9 | vt_boxed=27 vt_straight=0
- Hits (winner_hits.csv): rows=141 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=27 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.608571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.608571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 13.408571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 13.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 559 | score_v2 13.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 12.937143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 12.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 12.227143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 559 | score_v2 12.108571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 13.608571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 559 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 221 | score_v2 11.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 592 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 552 | score_v2 11.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 11.208571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 922 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 599 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 599 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 189 (canon 189): items_total=62 exact_any=4 vtrac_any=35 | top winner_present=False best_rank=None/32; Evening 051 (canon 015): items_total=166 exact_any=50 vtrac_any=91 | top winner_present=True best_rank=40/18; Combined 189 (canon 189): items_total=141 exact_any=42 vtrac_any=114 | top winner_present=False best_rank=None/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 221, 592.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_054824)

## Top indices (from enhanced JSON)
- index 4 | score 49.65613750000001 | features: presence=28.48863750000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 41.785672500000004 | features: presence=27.1681725, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 3 | score 40.9929575 | features: presence=29.145457500000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 11 | score 34.40908500000001 | features: presence=20.91158500000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 32.76691 | features: presence=21.669410000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 23 | score 22.104845 | features: presence=14.047345000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 6 | score 19.906887500000003 | features: presence=13.4693875, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 21 | score 16.3579675 | features: presence=8.4504675, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 16.3292675 | features: presence=7.961767500000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 24 | score 14.689850000000003 | features: presence=7.372350000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
087, 870, 028, 082, 198, 098, 708, 208, 981, 218

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 189 | index 24 | file SouthCarolina4_vtrac24_winner_189_20260105_054606.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 051 | index 2 | file SouthCarolina4_vtrac2_winner_051_20260105_054608.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 189 | index 24 rank 10/35 (rank_frac 0.2857142857142857) | score 14.689850000000003 (top 49.65613750000001, ratio 0.295831507233119, delta 34.96628750000001) | winner_in_index_straights=False | top_index_straights: 198 (7.767), 981 (5.156), 918 (4.903)
- winner 051 | index 2 rank 16/35 (rank_frac 0.45714285714285713) | score 8.818975 (top 49.65613750000001, ratio 0.1776009058296167, delta 40.837162500000005) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 189→idx24 rank 10/35 (frac 0.286); 051→idx2 rank 16/35 (frac 0.457).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 4, 18, 3, 11, 5.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-03)

## Midday winner 189 (canonical 189)
- Top lanes (hot_zones_top_lanes.csv): present | rank 55/210 (rank_frac 0.2619047619047619) | score_mean 17.524 (top 21.067, ratio 0.8318222812930176, delta 3.5429999999999993)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 051 (canonical 015)
- Top lanes (hot_zones_top_lanes.csv): present | rank 16/210 (rank_frac 0.0761904761904762) | score_mean 18.498 (top 21.067, ratio 0.8780557269663455, delta 2.568999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 044 | vt_triad 15 | score_mean 21.067 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    2 | triad 144 | vt_triad 25 | score_mean 19.817 | tags hot16,hot20,literal_draw,set1_bonus,straight_lane,vertical1,vt_straight
- rank    3 | triad 059 | vt_triad 115 | score_mean 19.664 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    4 | triad 019 | vt_triad 125 | score_mean 19.393 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 009 | vt_triad 15 | score_mean 19.361 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 038 | vt_triad 144 | score_mean 19.303 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 158 | vt_triad 124 | score_mean 19.192 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 128 | vt_triad 234 | score_mean 19.101 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 257 | vt_triad 133 | score_mean 19.035 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 115 | vt_triad 12 | score_mean 19.025 | tags funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 189 (canon 189): rank 55/210 (rank_frac 0.262) ratio_to_top=0.8318222812930176; Evening 051 (canon 015): rank 16/210 (rank_frac 0.076) ratio_to_top=0.8780557269663455
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

Aux draws snapshot dir: `sharepacks/2026-01-03/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=084, 308, 821, 910, 044
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=308, 910, 653, 754, 425
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=084, 821, 044, 976, 463

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=17 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=17), P2:3 (gap=33), P3:2 (gap=12)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=972 sev=B
- 449: ds=901 sev=B
- 156: ds=884 sev=B
- 778: ds=854 sev=B
- 279: ds=853 sev=B
- 033: ds=785 sev=B
- 004: ds=773 sev=B
- 688: ds=740 sev=B
- 278: ds=707 sev=B
- 377: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=181 sev=red
  - 55: ds=118 sev=red
  - 77: ds=102 sev=blue
  - 33: ds=89 sev=blue
  - 88: ds=84 sev=blue
  - 22: ds=64 sev=purple
  - 66: ds=52 sev=purple
  - 00: ds=25 sev=purple
  - 11: ds=21 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 15: ds=60 sev=red
  - 78: ds=53 sev=blue
  - 05: ds=49 sev=blue
  - 68: ds=41 sev=blue
  - 29: ds=34 sev=purple
  - 06: ds=27 sev=purple
  - 16: ds=27 sev=purple
  - 59: ds=23 sev=-
  - 17: ds=21 sev=-
  - 13: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:445, 35:388, 1:169, 26:157, 31:119, 4:110, 23:108, 28:102, 27:85, 19:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=445 fs=0 fl=0 hz=0.002197802197802198, 35:ds=388 fs=0 fl=0 hz=0.001949317738791423, 1:ds=169 fs=6 fl=4 hz=0.012195121951219513, 26:ds=157 fs=2 fl=0 hz=0.0062402496099844, 31:ds=119 fs=27 fl=0 hz=0.03085714285714286, 4:ds=110 fs=21 fl=2 hz=0.026589595375722544, 23:ds=108 fs=25 fl=1 hz=0.029850746268656716, 28:ds=102 fs=16 fl=2 hz=0.021479713603818614, 27:ds=85 fs=26 fl=0 hz=0.02911534154535274, 19:ds=69 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=94 flags=red+purple
- S0: ds=67 flags=blue+purple
- S23: ds=56 flags=purple
- S5: ds=55 flags=purple
- S24: ds=53 flags=blue+purple
- S4: ds=45 flags=purple
- S3: ds=44 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=4 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=14), P2:3 (gap=40), P3:9 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=878 sev=B
- 555: ds=873 sev=B
- 222: ds=850 sev=B
- 337: ds=827 sev=B
- 003: ds=818 sev=B
- 228: ds=809 sev=B
- 556: ds=711 sev=B
- 449: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=113 sev=red
  - 55: ds=77 sev=blue
  - 77: ds=46 sev=purple
  - 33: ds=40 sev=purple
  - 88: ds=38 sev=purple
  - 22: ds=36 sev=purple
  - 66: ds=23 sev=-
  - 00: ds=14 sev=-
  - 11: ds=9 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 49: ds=54 sev=blue
  - 67: ds=48 sev=blue
  - 34: ds=47 sev=blue
  - 27: ds=41 sev=blue
  - 07: ds=32 sev=purple
  - 05: ds=29 sev=purple
  - 15: ds=27 sev=purple
  - 18: ds=26 sev=purple
  - 78: ds=26 sev=purple
  - 69: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:414, 26:192, 35:178, 27:143, 6:111, 5:80, 1:77, 15:72, 34:58, 31:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=414 fs=1 fl=2 hz=0.006993006993006993, 26:ds=192 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=178 fs=1 fl=1 hz=0.004968944099378882, 27:ds=143 fs=18 fl=3 hz=0.026582278481012658, 6:ds=111 fs=24 fl=2 hz=0.02957906712172924, 5:ds=80 fs=20 fl=1 hz=0.023102310231023104, 1:ds=77 fs=7 fl=3 hz=0.012127894156560088, 15:ds=72 fs=17 fl=3 hz=0.021691973969631236, 34:ds=58 fs=28 fl=1 hz=0.03159041394335512, 31:ds=54 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=81 flags=purple
- S25: ds=78 flags=purple
- S21: ds=58 flags=purple
- S20: ds=54 flags=purple
- S17: ds=52 flags=purple
- S8: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=3 tags=MIR,RS
  - 134: score=3 tags=PAT,RS
  - 278: score=3 tags=MIR,RS
  - 368: score=3 tags=MIR,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 089: score=2 tags=RS
  - 125: score=2 tags=RS
  - 179: score=2 tags=RS
  - 269: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=31 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=17), P2:3 (gap=18), P3:8 (gap=20)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=981 sev=B
- 117: ds=892 sev=B
- 005: ds=878 sev=B
- 577: ds=855 sev=B
- 155: ds=835 sev=B
- 777: ds=834 sev=B
- 669: ds=826 sev=B
- 179: ds=808 sev=B
- 366: ds=774 sev=B
- 222: ds=768 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=98 sev=blue
  - 77: ds=85 sev=blue
  - 66: ds=77 sev=blue
  - 33: ds=73 sev=blue
  - 55: ds=64 sev=purple
  - 88: ds=58 sev=purple
  - 22: ds=35 sev=purple
  - 11: ds=24 sev=-
  - 00: ds=14 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 58: ds=99 sev=red
  - 35: ds=66 sev=red
  - 29: ds=61 sev=red
  - 47: ds=51 sev=blue
  - 15: ds=47 sev=blue
  - 19: ds=33 sev=purple
  - 78: ds=29 sev=purple
  - 05: ds=27 sev=purple
  - 68: ds=26 sev=purple
  - 38: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:486, 1:273, 32:240, 31:219, 4:139, 28:112, 19:108, 23:103, 26:85, 16:81

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=486 fs=3 fl=1 hz=0.017391304347826087, 1:ds=273 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=240 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=219 fs=16 fl=1 hz=0.021935483870967745, 4:ds=139 fs=21 fl=3 hz=0.028742514970059883, 28:ds=112 fs=10 fl=4 hz=0.017676767676767676, 19:ds=108 fs=12 fl=2 hz=0.016968325791855206, 23:ds=103 fs=24 fl=0 hz=0.02937576499388005, 26:ds=85 fs=0 fl=0 hz=0.002347417840375587, 16:ds=81 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=64 flags=purple
- S15: ds=55 flags=red+purple
- S9: ds=52 flags=purple
- S17: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 126: score=2 tags=RS
  - 189: score=2 tags=RS
  - 234: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:768(B); midday:850(B)
- 366 -> combined:972(B); evening:774(B)
- 449 -> combined:901(B); midday:669(B)
- 688 -> combined:740(B); evening:733(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:49(blue); evening:27(purple); midday:29(purple)
- 15 -> combined:60(red); evening:47(blue); midday:27(purple)
- 22 -> combined:64(purple); evening:35(purple); midday:36(purple)
- 29 -> combined:34(purple); evening:61(red)
- 33 -> combined:89(blue); evening:73(blue); midday:40(purple)
- 55 -> combined:118(red); evening:64(purple); midday:77(blue)
- 66 -> combined:52(purple); evening:77(blue)
- 68 -> combined:41(blue); evening:26(purple)
- 77 -> combined:102(blue); evening:85(blue); midday:46(purple)
- 78 -> combined:53(blue); evening:29(purple); midday:26(purple)
- 88 -> combined:84(blue); evening:58(purple); midday:38(purple)
- 99 -> combined:181(red); evening:98(blue); midday:113(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.501314285714286)[R2,XVAR-Cons(CE)], 2(2.3972714285714285)[R3,XVAR-Cons(CM)], 6(1.3405714285714285)[R1,Mirror-Echo], 5(1.1342857142857143)[R1,Double-Pressure], 0(1.018)[R1,Double-Pressure]
- P2: 3(8.602857142857143)[R1,XVAR-Cons(CEM)], 9(3.3897)[R2,XVAR-Cons(CE)], 7(1.2016)[R2,Double-Pressure], 8(0.7362285714285715)[R3,Mirror-Echo], 1(0.23435714285714285)[R3,Swap]
- P3: 9(2.987857142857143)[R3,XVAR-Cons(CM)], 2(2.674935714285714)[R1,Mirror-Echo], 7(2.5477857142857143)[R2,Mirror-Echo], 8(1.2971428571428572)[R1,Double-Pressure], 6(1.0761999999999998)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-02.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=17), P2:3(gap=33), P3:2(gap=12); top cartesian candidates: 132, 137, 232, 139, 237.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 015, 016, 017, 025, 026.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:850(B),evening:768(B); 366→combined:972(B),evening:774(B); 449→combined:901(B),midday:669(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:445, 35:388, 1:169, 26:157, 31:119.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=189 Evening=051; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 189 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 015 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 189 (canon 189): box `189` covers winner `189` (boxed hit).
  - Evening winner 051 (canon 015): box `015` covers winner `051` (boxed hit).
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
