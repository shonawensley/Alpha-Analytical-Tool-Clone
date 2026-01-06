# Master Validation Run Report — SouthCarolina4 — results 2026-01-01 (history workbook ~ 2025-12-31)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-01/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-01/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-01/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-01/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-01/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-01/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-01/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac21_winner_821_20260105_053426.html`
- `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac9_winner_910_20260105_053424.html`

Winners JSON files:
- `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac21_winner_821_20260105_053426.json`
- `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac9_winner_910_20260105_053424.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-01/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 910 (canon 019): exact_boxed=True exact_straight=True | rank 329/5317 (rank_frac 0.062); Evening 821 (canon 128): exact_boxed=True exact_straight=True | rank 2875/5317 (rank_frac 0.541)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 821 idx21 (rank 11/35, frac 0.314), 910 idx9 (rank 8/35, frac 0.229)
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

### 2.Stable — SouthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-01)

## Midday winner 910 (canonical 019)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=31 | family_rows=387 | exact_boxed=31 | exact_straight=20 | vt_boxed=31
- Scores (patterns_scores.csv): rank 329/5317 (rank_frac 0.061876998307316154) | score 20.5 (top 37.0, ratio 0.5540540540540541, delta 16.5) | section Combined, Set Set3, Draw Draw1, Col 2, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat6|hot1|perm3|hidden3v|set_chain3
- Compound (patterns_compound.csv): rank 49/1582 (rank_frac 0.030973451327433628) | score 40.5 (top 89.0, ratio 0.4550561797752809, delta 48.5) | section Combined, col1_hits 3, hot2 2, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x3|hot1x6|hot2x2|vstrx3
- Families (patterns_families.csv): count 77 | rank 57/1561 (rank_frac 0.03651505445227418) | score 26.5 (top 33.0, ratio 0.803030303030303, delta 6.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=85

## Evening winner 821 (canonical 128)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=529 | exact_boxed=2 | exact_straight=2 | vt_boxed=2
- Scores (patterns_scores.csv): rank 2875/5317 (rank_frac 0.5407184502539025) | score 13.0 (top 37.0, ratio 0.35135135135135137, delta 24.0) | section Combined, Set Set1, Draw Draw3, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot2|vtrac_straight
- Compound (patterns_compound.csv): rank 421/1582 (rank_frac 0.2661188369152971) | score 19.5 (top 89.0, ratio 0.21910112359550563, delta 69.5) | section Combined, col1_hits 1, hot2 2, set_chain 1, draw_chain 1 | why draw_chain1|col1x1|hot2x2|vstrx2
- Families (patterns_families.csv): count 62 | rank 101/1561 (rank_frac 0.0647021140294683) | score 25.0 (top 33.0, ratio 0.7575757575757576, delta 8.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=86

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 118 | section Combined | score 89.0 | col1_hits 8 | hot2 11
- rank    2 | canon 011 | section Combined | score 84.5 | col1_hits 8 | hot2 11
- rank    4 | canon 0118 | section Combined | score 74.5 | col1_hits 7 | hot2 11
- rank    6 | canon 118 | section Evening | score 69.0 | col1_hits 6 | hot2 8
- rank    7 | canon 009 | section Midday | score 67.5 | col1_hits 6 | hot2 8
- rank    5 | canon 008 | section Midday | score 74.0 | col1_hits 6 | hot2 8
- rank   26 | canon 158 | section Evening | score 47.5 | col1_hits 3 | hot2 7
- rank   35 | canon 0011 | section Combined | score 44.0 | col1_hits 0 | hot2 6
- rank   31 | canon 00118 | section Combined | score 45.5 | col1_hits 0 | hot2 6
- rank   13 | canon 0079 | section Midday | score 56.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1509 | family 16 | score 7.0 | hot2 0 | section Midday
- rank  906 | family 9 | score 14.5 | hot2 0 | section Midday
- rank 1272 | family 11 | score 11.0 | hot2 0 | section Midday
- rank 1272 | family 13 | score 11.0 | hot2 0 | section Midday
- rank 1162 | family 27 | score 12.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 910 (canon 019): exact_boxed=True exact_straight=True | rank 329/5317 (rank_frac 0.062); Evening 821 (canon 128): exact_boxed=True exact_straight=True | rank 2875/5317 (rank_frac 0.541)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260105)

## Midday winner 910 (canonical 019)
- Stamp (winner_stamp.json): items_total=81 | exact_any=17 exact_final=0 | vtrac_any=81 vtrac_final=0 | drop_exact_any=17 drop_exact_final=0 | drop_vtrac_any=23 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=5 family_vtrac_final=0
- Flags (winner_flags.csv): rows=81 | exact_any=17 vtrac_any=81 | drop_exact_any=17 drop_vtrac_any=23 | family_exact_any=1 family_vtrac_any=5 | vt_boxed=28 vt_straight=0
- Hits (winner_hits.csv): rows=81 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=28 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.327143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 821 (canonical 128)
- Stamp (winner_stamp.json): items_total=155 | exact_any=4 exact_final=0 | vtrac_any=137 vtrac_final=0 | drop_exact_any=7 drop_exact_final=0 | drop_vtrac_any=41 drop_vtrac_final=0 | family_exact_any=7 family_exact_final=0 | family_vtrac_any=6 family_vtrac_final=0
- Flags (winner_flags.csv): rows=155 | exact_any=4 vtrac_any=137 | drop_exact_any=7 drop_vtrac_any=41 | family_exact_any=7 family_vtrac_any=6 | vt_boxed=58 vt_straight=0
- Hits (winner_hits.csv): rows=155 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=58 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.227143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 910 (canonical 019)
- Stamp (winner_stamp.json): items_total=439 | exact_any=221 exact_final=0 | vtrac_any=337 vtrac_final=0 | drop_exact_any=233 drop_exact_final=0 | drop_vtrac_any=311 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=96 family_vtrac_final=0
- Flags (winner_flags.csv): rows=439 | exact_any=221 vtrac_any=337 | drop_exact_any=233 drop_vtrac_any=311 | family_exact_any=1 family_vtrac_any=96 | vt_boxed=64 vt_straight=0
- Hits (winner_hits.csv): rows=439 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=64 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=True | winner_best_rank=32 | winner_rank_fraction=1.3333333333333333 | winner_score_v2=8.29381 top_score_v2=10.658571 | winner_score_ratio_to_top=0.7781352678515723 winner_score_delta_from_top=2.3647609999999997
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 990 | score_v2 14.327143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 990 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 990 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 990 | score_v2 13.827143 | match_types 
- area_rank 2 | variant Midday | section Midday | set Set1 draw Draw4 col 3 | pattern 990 | score_v2 13.727143 | match_types 
- area_rank 2 | variant Midday | section Midday | set Set1 draw Draw6 col 1 | pattern 990 | score_v2 13.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 900 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 3 | pattern 900 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 008 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 552 | score_v2 12.227143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 990 | score_v2 14.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 900 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 008 | score_v2 12.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 552 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 922 | score_v2 10.658571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 590 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 992 | score_v2 9.587143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 592 | score_v2 9.464921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 599 | score_v2 9.237143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 992 | score_v2 9.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 910 (canon 019): items_total=81 exact_any=17 vtrac_any=81 | top winner_present=False best_rank=None/30; Evening 821 (canon 128): items_total=155 exact_any=4 vtrac_any=137 | top winner_present=False best_rank=None/24; Combined 910 (canon 019): items_total=439 exact_any=221 vtrac_any=337 | top winner_present=True best_rank=32/24
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 990, 900, 008, 552, 922.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_053647)

## Top indices (from enhanced JSON)
- index 18 | score 59.609334999999994 | features: presence=45.191835, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 58.18760749999998 | features: presence=42.45010749999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 47.7874 | features: presence=34.6299, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 43.51345 | features: presence=28.235950000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 43.022605000000006 | features: presence=31.135105000000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 35.2953 | features: presence=25.0178, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 29.514900000000004 | features: presence=21.817400000000006, cross_section=0.5, first_hit=0.4, column_span=0.3375
- index 9 | score 19.356817500000002 | features: presence=11.3593175, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 25 | score 15.672050000000004 | features: presence=8.864550000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 33 | score 15.459100000000005 | features: presence=9.291600000000004, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
138, 831, 198, 918, 183, 386, 683, 086, 819, 836

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 821 | index 21 | file SouthCarolina4_vtrac21_winner_821_20260105_053426.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 910 | index 9 | file SouthCarolina4_vtrac9_winner_910_20260105_053424.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 821 | index 21 rank 11/35 (rank_frac 0.3142857142857143) | score 15.128160000000003 (top 59.609334999999994, ratio 0.25378843766668435, delta 44.48117499999999) | winner_in_index_straights=False | top_index_straights: 371 (6.64), 867 (6.348), 817 (5.247)
- winner 910 | index 9 rank 8/35 (rank_frac 0.22857142857142856) | score 19.356817500000002 (top 59.609334999999994, ratio 0.32472795578075153, delta 40.252517499999996) | winner_in_index_straights=False | top_index_straights: 901 (9.328), 906 (6.901), 019 (6.718)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 821→idx21 rank 11/35 (frac 0.314); 910→idx9 rank 8/35 (frac 0.229).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 18, 23, 6, 24, 8.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-01

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-01)

## Midday winner 910 (canonical 019)
- Top lanes (hot_zones_top_lanes.csv): present | rank 83/201 (rank_frac 0.4129353233830846) | score_mean 17.273 (top 24.514, ratio 0.7046177694378722, delta 7.241)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 821 (canonical 128)
- Top lanes (hot_zones_top_lanes.csv): present | rank 156/201 (rank_frac 0.7761194029850746) | score_mean 15.835 (top 24.514, ratio 0.6459574120910501, delta 8.678999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 257 | vt_triad 133 | score_mean 24.514 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical4,vt_straight
- rank    2 | triad 679 | vt_triad 235 | score_mean 24.47 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    3 | triad 489 | vt_triad 455 | score_mean 22.261 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 044 | vt_triad 15 | score_mean 20.317 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 124 | vt_triad 235 | score_mean 20.125 | tags hot16,literal_draw,straight_lane,vertical2,vt_straight
- rank    6 | triad 006 | vt_triad 12 | score_mean 20.047 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_straight
- rank    7 | triad 244 | vt_triad 35 | score_mean 19.918 | tags hot16,hot20,set1_bonus,straight_lane,vertical3
- rank    8 | triad 246 | vt_triad 235 | score_mean 19.553 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 118 | vt_triad 24 | score_mean 19.542 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 688 | vt_triad 24 | score_mean 19.388 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 910 (canon 019): rank 83/201 (rank_frac 0.413) ratio_to_top=0.7046177694378722; Evening 821 (canon 128): rank 156/201 (rank_frac 0.776) ratio_to_top=0.6459574120910501
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

Aux draws snapshot dir: `sharepacks/2026-01-01/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=044, 653, 976, 754, 463
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=653, 754, 425, 462, 144
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=044, 976, 463, 849, 257

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=2 last_repeat_gap=13 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=13), P2:3 (gap=29), P3:1 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 225: ds=999 sev=B
- 233: ds=996 sev=B
- 366: ds=968 sev=B
- 449: ds=897 sev=B
- 156: ds=880 sev=B
- 778: ds=850 sev=B
- 279: ds=849 sev=B
- 033: ds=781 sev=B
- 004: ds=769 sev=B
- 688: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=177 sev=red
  - 55: ds=114 sev=red
  - 77: ds=98 sev=blue
  - 33: ds=85 sev=blue
  - 88: ds=80 sev=blue
  - 22: ds=60 sev=purple
  - 66: ds=48 sev=purple
  - 00: ds=21 sev=-
  - 11: ds=17 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 15: ds=56 sev=red
  - 18: ds=54 sev=blue
  - 78: ds=49 sev=blue
  - 05: ds=45 sev=blue
  - 68: ds=37 sev=blue
  - 29: ds=30 sev=purple
  - 09: ds=25 sev=purple
  - 06: ds=23 sev=-
  - 16: ds=23 sev=-
  - 08: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:441, 35:384, 1:165, 26:153, 31:115, 4:106, 23:104, 28:98, 27:81, 19:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=441 fs=0 fl=0 hz=0.002197802197802198, 35:ds=384 fs=0 fl=0 hz=0.001949317738791423, 1:ds=165 fs=6 fl=4 hz=0.012195121951219513, 26:ds=153 fs=2 fl=0 hz=0.0062402496099844, 31:ds=115 fs=27 fl=0 hz=0.03085714285714286, 4:ds=106 fs=21 fl=2 hz=0.026589595375722544, 23:ds=104 fs=25 fl=1 hz=0.029850746268656716, 28:ds=98 fs=16 fl=2 hz=0.021479713603818614, 27:ds=81 fs=26 fl=0 hz=0.02911534154535274, 19:ds=65 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=90 flags=red+purple
- S0: ds=63 flags=blue+purple
- S23: ds=52 flags=blue+purple
- S5: ds=51 flags=purple
- S24: ds=49 flags=blue+purple
- S4: ds=41 flags=purple
- S3: ds=40 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '8'], 'pairs': {'remaining_count': 0}}
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
- current_index=8 streak=1 max=3 last_repeat_gap=2 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=29), P2:3 (gap=38), P3:9 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=876 sev=B
- 555: ds=871 sev=B
- 222: ds=848 sev=B
- 337: ds=825 sev=B
- 003: ds=816 sev=B
- 228: ds=807 sev=B
- 556: ds=709 sev=B
- 449: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=111 sev=red
  - 55: ds=75 sev=blue
  - 77: ds=44 sev=purple
  - 33: ds=38 sev=purple
  - 88: ds=36 sev=purple
  - 22: ds=34 sev=purple
  - 66: ds=21 sev=-
  - 00: ds=12 sev=-
  - 11: ds=7 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 49: ds=52 sev=blue
  - 67: ds=46 sev=blue
  - 34: ds=45 sev=blue
  - 09: ds=42 sev=blue
  - 27: ds=39 sev=blue
  - 07: ds=30 sev=purple
  - 05: ds=27 sev=purple
  - 15: ds=25 sev=purple
  - 18: ds=24 sev=-
  - 78: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:412, 26:190, 35:176, 27:141, 6:109, 5:78, 1:75, 15:70, 34:56, 31:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=412 fs=1 fl=2 hz=0.006993006993006993, 26:ds=190 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=176 fs=1 fl=1 hz=0.004968944099378882, 27:ds=141 fs=18 fl=3 hz=0.026582278481012658, 6:ds=109 fs=24 fl=2 hz=0.02957906712172924, 5:ds=78 fs=20 fl=1 hz=0.023102310231023104, 1:ds=75 fs=7 fl=3 hz=0.012127894156560088, 15:ds=70 fs=17 fl=3 hz=0.021691973969631236, 34:ds=56 fs=28 fl=1 hz=0.03159041394335512, 31:ds=52 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S25: ds=76 flags=purple
- S21: ds=56 flags=purple
- S20: ds=52 flags=purple
- S17: ds=50 flags=purple
- S8: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=29 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=15), P2:8 (gap=19), P3:1 (gap=22)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=979 sev=B
- 117: ds=890 sev=B
- 005: ds=876 sev=B
- 577: ds=853 sev=B
- 155: ds=833 sev=B
- 777: ds=832 sev=B
- 669: ds=824 sev=B
- 179: ds=806 sev=B
- 366: ds=772 sev=B
- 222: ds=766 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=96 sev=blue
  - 77: ds=83 sev=blue
  - 66: ds=75 sev=blue
  - 33: ds=71 sev=blue
  - 55: ds=62 sev=purple
  - 88: ds=56 sev=purple
  - 22: ds=33 sev=purple
  - 11: ds=22 sev=-
  - 00: ds=12 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 58: ds=97 sev=red
  - 35: ds=64 sev=red
  - 29: ds=59 sev=red
  - 47: ds=49 sev=blue
  - 15: ds=45 sev=blue
  - 18: ds=31 sev=purple
  - 19: ds=31 sev=purple
  - 78: ds=27 sev=purple
  - 05: ds=25 sev=purple
  - 08: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:484, 1:271, 32:238, 31:217, 4:137, 28:110, 19:106, 23:101, 26:83, 16:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=484 fs=3 fl=1 hz=0.017391304347826087, 1:ds=271 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=238 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=217 fs=16 fl=1 hz=0.021935483870967745, 4:ds=137 fs=21 fl=3 hz=0.028742514970059883, 28:ds=110 fs=10 fl=4 hz=0.017676767676767676, 19:ds=106 fs=12 fl=2 hz=0.016968325791855206, 23:ds=101 fs=24 fl=0 hz=0.02937576499388005, 26:ds=83 fs=0 fl=0 hz=0.002347417840375587, 16:ds=79 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=62 flags=purple
- S15: ds=53 flags=red+purple
- S9: ds=50 flags=purple
- S17: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 045: score=2 tags=RS
  - 234: score=2 tags=RS
  - 279: score=2 tags=RS
  - 369: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:766(B); midday:848(B)
- 366 -> combined:968(B); evening:772(B)
- 449 -> combined:897(B); midday:667(B)
- 688 -> combined:736(B); evening:731(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:45(blue); evening:25(purple); midday:27(purple)
- 09 -> combined:25(purple); midday:42(blue)
- 15 -> combined:56(red); evening:45(blue); midday:25(purple)
- 18 -> combined:54(blue); evening:31(purple)
- 22 -> combined:60(purple); evening:33(purple); midday:34(purple)
- 29 -> combined:30(purple); evening:59(red)
- 33 -> combined:85(blue); evening:71(blue); midday:38(purple)
- 55 -> combined:114(red); evening:62(purple); midday:75(blue)
- 66 -> combined:48(purple); evening:75(blue)
- 77 -> combined:98(blue); evening:83(blue); midday:44(purple)
- 78 -> combined:49(blue); evening:27(purple)
- 88 -> combined:80(blue); evening:56(purple); midday:36(purple)
- 99 -> combined:177(red); evening:96(blue); midday:111(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(2.4958)[R3,XVAR-Cons(CE)], 9(1.5658571428571428)[R1,Double-Pressure], 6(1.1618571428571427)[R1,Mirror-Echo], 5(1.0085714285714285)[R1,Double-Pressure], 3(0.942)[R2,Double-Pressure]
- P2: 3(8.819757142857142)[R1,Mirror-Echo], 8(7.670928571428572)[R2,Mirror-Echo], 9(1.8599357142857142)[R3,XVAR-Cons(CE)], 7(0.5598)[R2,Swap]
- P3: 1(3.628285714285714)[R1,XVAR-Cons(CE)], 8(3.3622)[R2,XVAR-Cons(CE)], 0(1.6153857142857144)[R3,XVAR-Cons(CM)], 9(1.3867142857142856)[R1,Double-Pressure], 6(0.9343999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2025_12_31.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=13), P2:3(gap=29), P3:1(gap=15); top cartesian candidates: 131, 181, 138, 188, 130.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '8'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:848(B),evening:766(B); 366→combined:968(B),evening:772(B); 449→combined:897(B),midday:667(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:441, 35:384, 1:165, 26:153, 31:115.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=910 Evening=821; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 019 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 128 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 910 (canon 019): box `019` covers winner `910` (boxed hit).
  - Evening winner 821 (canon 128): box `128` covers winner `821` (boxed hit).
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
