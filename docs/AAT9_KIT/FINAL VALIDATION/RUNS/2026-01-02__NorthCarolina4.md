# Master Validation Run Report — NorthCarolina4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-02/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-02/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-02/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-02/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-02/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.html`
- `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac32_winner_383_20260105_070917.html`

Winners JSON files:
- `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.json`
- `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac32_winner_383_20260105_070917.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 033 (canon 033): exact_boxed=True exact_straight=True | rank 4/5320 (rank_frac 0.001); Evening 383 (canon 338): exact_boxed=True exact_straight=False | rank 718/5320 (rank_frac 0.135)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 033 idx13 (rank 5/35, frac 0.143), 383 idx32 (rank 16/35, frac 0.457)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — NorthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-02)

## Midday winner 033 (canonical 033)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=35 | family_rows=113 | exact_boxed=35 | exact_straight=35 | vt_boxed=35
- Scores (patterns_scores.csv): rank 4/5320 (rank_frac 0.0007518796992481203) | score 38.0 (top 40.5, ratio 0.9382716049382716, delta 2.5) | section Combined, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 2.0 | why straight|cov4|hp_repeat6|vstr2|vstr3|cons_full|hot2|cons_3v|double_mirror|vtrac_straight|set_chain2|draw_chain5
- Compound (patterns_compound.csv): rank 4/1074 (rank_frac 0.0037243947858473) | score 88.0 (top 109.5, ratio 0.8036529680365296, delta 21.5) | section Combined, col1_hits 1, hot2 6, set_chain 2, draw_chain 5 | why set_chain2|draw_chain5|col1x1|hot1x9|hot2x6|consensusx8|vstrx11|dblmirrorx22
- Families (patterns_families.csv): count 60 | rank 31/1624 (rank_frac 0.019088669950738917) | score 33.0 (top 37.5, ratio 0.88, delta 4.5) | section Combined, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=10

## Evening winner 383 (canonical 338)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=8 | family_rows=19 | exact_boxed=8 | exact_straight=0 | vt_boxed=8
- Scores (patterns_scores.csv): rank 718/5320 (rank_frac 0.1349624060150376) | score 21.5 (top 40.5, ratio 0.5308641975308642, delta 19.0) | section Midday, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat2|vstr2|mirror|hot1|dom_last|perm2|hidden3v|double_mirror|draw_chain2
- Compound (patterns_compound.csv): rank 178/1074 (rank_frac 0.16573556797020483) | score 27.0 (top 109.5, ratio 0.2465753424657534, delta 82.5) | section Midday, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|dblmirrorx3
- Families (patterns_families.csv): count 18 | rank 493/1624 (rank_frac 0.30357142857142855) | score 20.5 (top 37.5, ratio 0.5466666666666666, delta 17.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=False | vt_boxed_count=2

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 223 | section Combined | score 109.5 | col1_hits 9 | hot2 11
- rank    7 | canon 229 | section Midday | score 83.5 | col1_hits 8 | hot2 11
- rank    4 | canon 009 | section Midday | score 88.0 | col1_hits 8 | hot2 11
- rank    3 | canon 003 | section Midday | score 91.5 | col1_hits 6 | hot2 11
- rank   13 | canon 0039 | section Midday | score 70.0 | col1_hits 6 | hot2 11
- rank    2 | canon 223 | section Midday | score 99.5 | col1_hits 8 | hot2 11
- rank   10 | canon 0229 | section Midday | score 77.5 | col1_hits 8 | hot2 10
- rank    9 | canon 00229 | section Midday | score 78.5 | col1_hits 8 | hot2 10
- rank   14 | canon 0029 | section Midday | score 69.5 | col1_hits 5 | hot2 9
- rank   15 | canon 039 | section Midday | score 68.5 | col1_hits 5 | hot2 9

## Top families (patterns_families.csv)
- rank 1580 | family 17 | score 7.0 | hot2 0 | section Midday
- rank  692 | family 4 | score 18.0 | hot2 0 | section Midday
- rank  246 | family 30 | score 24.0 | hot2 0 | section Midday
- rank  132 | family 27 | score 26.5 | hot2 0 | section Midday
- rank  105 | family 5 | score 27.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 033 (canon 033): exact_boxed=True exact_straight=True | rank 4/5320 (rank_frac 0.001); Evening 383 (canon 338): exact_boxed=True exact_straight=False | rank 718/5320 (rank_frac 0.135)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260102)

## Midday winner 033 (canonical 033)
- Stamp (winner_stamp.json): items_total=264 | exact_any=156 exact_final=13 | vtrac_any=264 vtrac_final=13 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=3 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=264 | exact_any=156 vtrac_any=264 | drop_exact_any=1 drop_vtrac_any=3 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=170 vt_straight=0
- Hits (winner_hits.csv): rows=264 | exact_final=13 vtrac_final=13 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=170 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=12 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.158571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 383 (canonical 338)
- Stamp (winner_stamp.json): items_total=72 | exact_any=12 exact_final=0 | vtrac_any=72 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=72 | exact_any=12 vtrac_any=72 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=72 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 033 (canonical 033)
- Stamp (winner_stamp.json): items_total=519 | exact_any=324 exact_final=13 | vtrac_any=519 vtrac_final=13 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=9 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=519 | exact_any=324 vtrac_any=519 | drop_exact_any=1 drop_vtrac_any=9 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=176 vt_straight=0
- Hits (winner_hits.csv): rows=519 | exact_final=13 vtrac_final=13 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=176 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=18.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 922 | score_v2 18.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 922 | score_v2 17.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 922 | score_v2 17.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 922 | score_v2 17.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 922 | score_v2 17.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 922 | score_v2 16.827143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 15.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 922 | score_v2 15.158571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 15.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 922 | score_v2 14.987143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 922 | score_v2 18.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 992 | score_v2 15.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 922 | score_v2 15.158571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 922 | score_v2 14.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 922 | score_v2 14.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 224 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 992 | score_v2 13.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 992 | score_v2 12.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 224 | score_v2 12.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 992 | score_v2 11.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 033 (canon 033): items_total=264 exact_any=156 vtrac_any=264 | top winner_present=False best_rank=None/12; Evening 383 (canon 338): items_total=72 exact_any=12 vtrac_any=72 | top winner_present=False best_rank=None/20; Combined 033 (canon 033): items_total=519 exact_any=324 vtrac_any=519 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 922, 992, 922, 922, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260105_071329)

## Top indices (from enhanced JSON)
- index 4 | score 69.49370499999996 | features: presence=49.31620499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 63.802789999999995 | features: presence=37.88529, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 62.45194499999999 | features: presence=37.40444499999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 55.06865 | features: presence=39.44115, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 48.19484000000001 | features: presence=35.99734000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 42.79996 | features: presence=28.502460000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 33.194759999999995 | features: presence=21.547259999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 11 | score 32.02959 | features: presence=19.662090000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 30.94711 | features: presence=21.459609999999998, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 14 | score 27.194700000000005 | features: presence=17.137200000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
093, 932, 203, 290, 038, 083, 032, 870, 037, 087

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 033 | index 13 | file NorthCarolina4_vtrac13_winner_033_20260105_070916.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 383 | index 32 | file NorthCarolina4_vtrac32_winner_383_20260105_070917.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 033 | index 13 rank 5/35 (rank_frac 0.14285714285714285) | score 48.19484000000001 (top 69.49370499999996, ratio 0.6935137506339608, delta 21.29886499999995) | winner_in_index_straights=False | top_index_straights: 038 (11.511), 083 (11.04)
- winner 383 | index 32 rank 16/35 (rank_frac 0.45714285714285713) | score 9.523958333333333 (top 69.49370499999996, ratio 0.13704778487970007, delta 59.96974666666663) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 033→idx13 rank 5/35 (frac 0.143); 383→idx32 rank 16/35 (frac 0.457).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 4, 10, 3, 27, 13.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-02)

## Midday winner 033 (canonical 033)
- Top lanes (hot_zones_top_lanes.csv): present | rank 37/200 (rank_frac 0.185) | score_mean 17.811 (top 22.54, ratio 0.7901952085181899, delta 4.728999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 383 (canonical 338)
- Top lanes (hot_zones_top_lanes.csv): present | rank 12/200 (rank_frac 0.06) | score_mean 19.191 (top 22.54, ratio 0.8514196983141082, delta 3.349)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 667 | vt_triad 23 | score_mean 22.54 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    2 | triad 146 | vt_triad 225 | score_mean 22.256 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_straight
- rank    3 | triad 005 | vt_triad 11 | score_mean 20.274 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 057 | vt_triad 113 | score_mean 19.766 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 007 | vt_triad 13 | score_mean 19.596 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 055 | vt_triad 11 | score_mean 19.585 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 459 | vt_triad 155 | score_mean 19.429 | tags hot16,hot20,set1_bonus,superhot_set1
- rank    7 | triad 049 | vt_triad 155 | score_mean 19.429 | tags hot16,hot20,set1_bonus,superhot_set1
- rank    9 | triad 003 | vt_triad 14 | score_mean 19.365 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 008 | vt_triad 14 | score_mean 19.322 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 033 (canon 033): rank 37/200 (rank_frac 0.185) ratio_to_top=0.7901952085181899; Evening 383 (canon 338): rank 12/200 (rank_frac 0.060) ratio_to_top=0.8514196983141082
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

Aux draws snapshot dir: `sharepacks/2026-01-02/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=053, 416, 057, 867, 879
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=416, 867, 455, 766, 885
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=053, 057, 879, 168, 911

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=3 last_repeat_gap=27 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=28), P2:4 (gap=33), P3:2 (gap=30)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=888 sev=B
- 155: ds=876 sev=B
- 446: ds=872 sev=B
- 445: ds=812 sev=B
- 122: ds=795 sev=B
- 036: ds=791 sev=B
- 555: ds=768 sev=B
- 299: ds=765 sev=B
- 277: ds=757 sev=B
- 112: ds=746 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=152 sev=red
  - 77: ds=125 sev=red
  - 33: ds=49 sev=purple
  - 99: ds=48 sev=purple
  - 44: ds=46 sev=purple
  - 22: ds=12 sev=-
  - 88: ds=9 sev=-
  - 11: ds=8 sev=-
  - 66: ds=7 sev=-
  - 55: ds=5 sev=-
- non_repeating:
  - 56: ds=54 sev=blue
  - 27: ds=50 sev=blue
  - 02: ds=44 sev=blue
  - 23: ds=40 sev=blue
  - 09: ds=39 sev=blue
  - 28: ds=36 sev=purple
  - 04: ds=33 sev=purple
  - 06: ds=33 sev=purple
  - 34: ds=31 sev=purple
  - 29: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:480, 32:333, 1:107, 27:103, 31:94, 15:78, 16:76, 10:66, 23:55, 35:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=480 fs=3 fl=0 hz=0.009389671361502348, 32:ds=333 fs=1 fl=1 hz=0.005405405405405406, 1:ds=107 fs=0 fl=3 hz=0.00625, 27:ds=103 fs=15 fl=2 hz=0.02011173184357542, 31:ds=94 fs=19 fl=3 hz=0.02502844141069397, 15:ds=78 fs=16 fl=2 hz=0.019758507135016465, 16:ds=76 fs=4 fl=1 hz=0.008836524300441826, 10:ds=66 fs=21 fl=2 hz=0.027315914489311165, 23:ds=55 fs=17 fl=3 hz=0.024330900243309, 35:ds=46 fs=1 fl=1 hz=0.0053533190578158455

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=88 flags=purple
- S23: ds=72 flags=blue+purple
- S4: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 234: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=2 last_repeat_gap=96 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=35), P2:9 (gap=25), P3:2 (gap=38)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=973 sev=B
- 123: ds=948 sev=B
- 446: ds=925 sev=B
- 777: ds=885 sev=B
- 119: ds=850 sev=B
- 222: ds=820 sev=B
- 155: ds=782 sev=B
- 488: ds=776 sev=B
- 177: ds=752 sev=B
- 007: ds=731 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=155 sev=red
  - 00: ds=130 sev=red
  - 77: ds=62 sev=purple
  - 99: ds=50 sev=purple
  - 22: ds=38 sev=purple
  - 33: ds=24 sev=-
  - 11: ds=8 sev=-
  - 88: ds=4 sev=-
  - 66: ds=3 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 48: ds=146 sev=red
  - 25: ds=59 sev=red
  - 07: ds=54 sev=blue
  - 28: ds=46 sev=blue
  - 23: ds=41 sev=blue
  - 26: ds=41 sev=blue
  - 02: ds=38 sev=blue
  - 29: ds=35 sev=purple
  - 56: ds=29 sev=purple
  - 27: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:378, 25:186, 32:166, 35:140, 4:130, 11:105, 31:98, 2:94, 33:77, 12:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=378 fs=1 fl=0 hz=0.005905511811023622, 25:ds=186 fs=15 fl=1 hz=0.02165087956698241, 32:ds=166 fs=3 fl=1 hz=0.007416563658838071, 35:ds=140 fs=0 fl=2 hz=0.005201560468140442, 4:ds=130 fs=11 fl=3 hz=0.0166073546856465, 11:ds=105 fs=50 fl=0 hz=0.056882821387940846, 31:ds=98 fs=25 fl=0 hz=0.02793296089385475, 2:ds=94 fs=13 fl=3 hz=0.018223234624145785, 33:ds=77 fs=21 fl=2 hz=0.025136612021857924, 12:ds=55 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=89 flags=purple
- S20: ds=77 flags=red+purple
- S2: ds=68 flags=purple
- S5: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '3', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=3 last_repeat_gap=20 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=35), P3:5 (gap=20)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=974 sev=B
- 299: ds=931 sev=B
- 223: ds=861 sev=B
- 122: ds=850 sev=B
- 116: ds=827 sev=B
- 039: ds=810 sev=B
- 377: ds=798 sev=B
- 277: ds=784 sev=B
- 188: ds=772 sev=B
- 557: ds=771 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=179 sev=red
  - 55: ds=122 sev=red
  - 33: ds=121 sev=red
  - 77: ds=80 sev=blue
  - 00: ds=76 sev=blue
  - 66: ds=38 sev=purple
  - 99: ds=24 sev=-
  - 44: ds=23 sev=-
  - 22: ds=6 sev=-
  - 11: ds=4 sev=-
- non_repeating:
  - 45: ds=99 sev=red
  - 34: ds=40 sev=blue
  - 59: ds=39 sev=blue
  - 04: ds=35 sev=purple
  - 06: ds=29 sev=purple
  - 08: ds=28 sev=purple
  - 58: ds=28 sev=purple
  - 56: ds=27 sev=purple
  - 17: ds=25 sev=purple
  - 27: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:258, 26:240, 13:205, 32:179, 1:147, 23:116, 5:97, 17:96, 27:53, 31:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=258 fs=18 fl=0 hz=0.024896265560165977, 26:ds=240 fs=1 fl=2 hz=0.006666666666666667, 13:ds=205 fs=20 fl=0 hz=0.025284450063211127, 32:ds=179 fs=2 fl=2 hz=0.007416563658838071, 1:ds=147 fs=2 fl=3 hz=0.007434944237918215, 23:ds=116 fs=14 fl=3 hz=0.019384264538198404, 5:ds=97 fs=15 fl=2 hz=0.020809248554913295, 17:ds=96 fs=29 fl=0 hz=0.03553921568627451, 27:ds=53 fs=22 fl=3 hz=0.027085590465872156, 31:ds=47 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=90 flags=purple
- S0: ds=76 flags=blue+purple
- S4: ds=65 flags=blue+purple
- S22: ds=45 flags=purple
- S2: ds=44 flags=purple

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
- 036 -> combined:791(B); evening:724(B)
- 122 -> combined:795(B); evening:850(B)
- 155 -> combined:876(B); midday:782(B)
- 277 -> combined:757(B); evening:784(B)
- 299 -> combined:765(B); evening:931(B)
- 338 -> combined:888(B); midday:711(B)
- 446 -> combined:872(B); midday:925(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:152(red); evening:76(blue); midday:130(red)
- 02 -> combined:44(blue); midday:38(blue)
- 04 -> combined:33(purple); evening:35(purple)
- 06 -> combined:33(purple); evening:29(purple)
- 23 -> combined:40(blue); midday:41(blue)
- 25 -> combined:28(purple); midday:59(red)
- 27 -> combined:50(blue); evening:25(purple); midday:26(purple)
- 28 -> combined:36(purple); midday:46(blue)
- 29 -> combined:30(purple); midday:35(purple)
- 33 -> combined:49(purple); evening:121(red)
- 34 -> combined:31(purple); evening:40(blue)
- 44 -> combined:46(purple); midday:155(red)
- 56 -> combined:54(blue); evening:27(purple); midday:29(purple)
- 77 -> combined:125(red); evening:80(blue); midday:62(purple)
- 99 -> combined:48(purple); midday:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(3.938)[R1,XVAR-Cons(CE)], 2(3.214714285714286)[R3,XVAR-Cons(CM)], 0(1.2225)[R2,Double-Pressure], 7(0.8998999999999999)[R2,Double-Pressure], 3(0.42245714285714286)[R3,Swap]
- P2: 4(8.755828571428571)[R1,XVAR-Cons(CEM)], 0(3.7912)[R2,XVAR-Cons(CE)], 3(1.9589357142857144)[R3,XVAR-Cons(CE)], 9(1.5684285714285715)[R1,Mirror-Echo], 2(0.2881)[R3,Swap]
- P3: 2(8.201357142857143)[R1,XVAR-Cons(CEM)], 0(5.9756285714285715)[R2,XVAR-Cons(CEM)], 5(1.3404285714285713)[R1,Mirror-Echo], 8(0.5089)[R2,Swap], 4(0.29800000000000004)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=28), P2:4(gap=33), P3:2(gap=30); top cartesian candidates: 542, 242, 540, 240, 040.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 012, 023, 024, 025, 027.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:791(B),evening:724(B); 122→combined:795(B),evening:850(B); 155→combined:876(B),midday:782(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:480, 32:333, 1:107, 27:103, 31:94.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=033 Evening=383; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 033 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 338 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 033 (canon 033): box `033` covers winner `033` (boxed hit).
  - Evening winner 383 (canon 338): box `338` covers winner `383` (boxed hit).
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
