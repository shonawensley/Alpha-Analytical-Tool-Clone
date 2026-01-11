# Master Validation Run Report — OntarioCanada4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-08/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-08/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-08/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-08/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-08/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac10_winner_022_20260110_034438.html`
- `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_498_20260110_034440.html`

Winners JSON files:
- `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac10_winner_022_20260110_034438.json`
- `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_498_20260110_034440.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 022 (canon 022): exact_boxed=True exact_straight=True | rank 287/5098 (rank_frac 0.056); Evening 498 (canon 489): exact_boxed=True exact_straight=True | rank 4058/5098 (rank_frac 0.796)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 022 idx10 (rank 22/35, frac 0.629), 498 idx34 (rank 29/35, frac 0.829)
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

### 2.Stable — OntarioCanada4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-08)

## Midday winner 022 (canonical 022)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=14 | family_rows=72 | exact_boxed=14 | exact_straight=13 | vt_boxed=14
- Scores (patterns_scores.csv): rank 287/5098 (rank_frac 0.056296586896822286) | score 20.5 (top 38.0, ratio 0.5394736842105263, delta 17.5) | section Combined, Set Set1, Draw Draw4, Col 1, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat2|vstr2|hot2|perm2|hidden3v|double_mirror|draw_chain4
- Compound (patterns_compound.csv): rank 46/1801 (rank_frac 0.025541365907828985) | score 42.0 (top 87.5, ratio 0.48, delta 45.5) | section Combined, col1_hits 4, hot2 4, set_chain 1, draw_chain 4 | why draw_chain4|col1x4|hot1x1|hot2x4|vstrx6|dblmirrorx7
- Families (patterns_families.csv): count 48 | rank 188/1462 (rank_frac 0.12859097127222982) | score 21.5 (top 34.5, ratio 0.6231884057971014, delta 13.0) | section Combined, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=11

## Evening winner 498 (canonical 489)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=33 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 4058/5098 (rank_frac 0.7959984307571597) | score 10.0 (top 38.0, ratio 0.2631578947368421, delta 28.0) | section Evening, Set Set1, Draw Draw1, Col 5, hot 1, vt_straight 0.0 | why straight|cov1|hp_repeat2|mirror|hot1|draw_chain2
- Compound (patterns_compound.csv): rank 1037/1801 (rank_frac 0.5757912270960578) | score 12.0 (top 87.5, ratio 0.13714285714285715, delta 75.5) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|hot1x1
- Families (patterns_families.csv): count 31 | rank 548/1462 (rank_frac 0.3748290013679891) | score 16.5 (top 34.5, ratio 0.4782608695652174, delta 18.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=5

## Top compound candidates (patterns_compound.csv)
- rank    7 | canon 236 | section Midday | score 65.0 | col1_hits 5 | hot2 11
- rank    5 | canon 367 | section Midday | score 68.5 | col1_hits 5 | hot2 11
- rank    2 | canon 015 | section Evening | score 78.0 | col1_hits 7 | hot2 11
- rank    1 | canon 006 | section Combined | score 87.5 | col1_hits 8 | hot2 9
- rank   12 | canon 346 | section Midday | score 55.0 | col1_hits 3 | hot2 8
- rank    8 | canon 002 | section Combined | score 64.0 | col1_hits 6 | hot2 8
- rank   16 | canon 036 | section Midday | score 53.0 | col1_hits 4 | hot2 8
- rank   23 | canon 3677 | section Midday | score 48.5 | col1_hits 0 | hot2 6
- rank   10 | canon 347 | section Midday | score 60.5 | col1_hits 7 | hot2 6
- rank   83 | canon 034 | section Midday | score 35.0 | col1_hits 3 | hot2 6

## Top families (patterns_families.csv)
- rank 1404 | family 30 | score 6.0 | hot2 0 | section Midday
- rank  855 | family 12 | score 13.5 | hot2 1 | section Midday
- rank  703 | family 24 | score 15.0 | hot2 0 | section Midday
- rank  703 | family 6 | score 15.0 | hot2 0 | section Midday
- rank  515 | family 7 | score 17.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 022 (canon 022): exact_boxed=True exact_straight=True | rank 287/5098 (rank_frac 0.056); Evening 498 (canon 489): exact_boxed=True exact_straight=True | rank 4058/5098 (rank_frac 0.796)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260110)

## Midday winner 022 (canonical 022)
- Stamp (winner_stamp.json): items_total=64 | exact_any=27 exact_final=0 | vtrac_any=53 vtrac_final=0 | drop_exact_any=36 drop_exact_final=0 | drop_vtrac_any=63 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=31 family_vtrac_final=0
- Flags (winner_flags.csv): rows=64 | exact_any=27 vtrac_any=53 | drop_exact_any=36 drop_vtrac_any=63 | family_exact_any=0 family_vtrac_any=31 | vt_boxed=36 vt_straight=0
- Hits (winner_hits.csv): rows=64 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=36 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.477143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 498 (canonical 489)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 022 (canonical 022)
- Stamp (winner_stamp.json): items_total=316 | exact_any=139 exact_final=0 | vtrac_any=298 vtrac_final=0 | drop_exact_any=133 drop_exact_final=0 | drop_vtrac_any=260 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=149 family_vtrac_final=0
- Flags (winner_flags.csv): rows=316 | exact_any=139 vtrac_any=298 | drop_exact_any=133 drop_vtrac_any=260 | family_exact_any=0 family_vtrac_any=149 | vt_boxed=265 vt_straight=0
- Hits (winner_hits.csv): rows=316 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=265 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 440 | score_v2 12.077143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set3 draw Draw1 col 5 | pattern 501 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set3 draw Draw1 col 5 | pattern 501 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 440 | score_v2 11.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 4 | pattern 559 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set3 draw Draw1 col 5 | pattern 501 | score_v2 11.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 440 | score_v2 10.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 522 | score_v2 10.777143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 501 | score_v2 10.584643 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set3 draw Draw1 col 4 | pattern 501 | score_v2 10.547143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 440 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 440 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 501 | score_v2 11.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 11.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 522 | score_v2 10.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 224 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 10.137143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 922 | score_v2 9.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 924 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 552 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 022 (canon 022): items_total=64 exact_any=27 vtrac_any=53 | top winner_present=False best_rank=None/22; Evening 498 (canon 489): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/18; Combined 022 (canon 022): items_total=316 exact_any=139 vtrac_any=298 | top winner_present=False best_rank=None/30
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 440, 440, 501, 559, 522.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260110_034642)

## Top indices (from enhanced JSON)
- index 21 | score 49.760724999999994 | features: presence=36.463224999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 39.274505 | features: presence=27.747005000000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 9 | score 37.374027500000004 | features: presence=25.906527500000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 30 | score 34.10435 | features: presence=23.77685, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 32.85133 | features: presence=19.89383, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 29.9345 | features: presence=19.517, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 6 | score 29.5264625 | features: presence=21.9189625, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 15 | score 27.817085000000002 | features: presence=16.999585, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 26.259450000000008 | features: presence=16.701950000000004, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 19.987000000000002 | features: presence=13.829500000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
324, 367, 263, 401, 362, 347, 732, 713, 241, 736

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 022 | index 10 | file OntarioCanada4_vtrac10_winner_022_20260110_034438.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 498 | index 34 | file OntarioCanada4_vtrac34_winner_498_20260110_034440.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 022 | index 10 rank 22/35 (rank_frac 0.6285714285714286) | score 7.416099999999999 (top 49.760724999999994, ratio 0.14903520798782574, delta 42.34462499999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 498 | index 34 rank 29/35 (rank_frac 0.8285714285714286) | score 3.4127083333333337 (top 49.760724999999994, ratio 0.0685823675867531, delta 46.34801666666666) | winner_in_index_straights=False | top_index_straights: 984 (1.09)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 022→idx10 rank 22/35 (frac 0.629); 498→idx34 rank 29/35 (frac 0.829).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 21, 20, 9, 30, 28.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-08)

## Midday winner 022 (canonical 022)
- Top lanes (hot_zones_top_lanes.csv): present | rank 175/212 (rank_frac 0.8254716981132075) | score_mean 15.706 (top 25.264, ratio 0.621675110829639, delta 9.558)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 498 (canonical 489)
- Top lanes (hot_zones_top_lanes.csv): present | rank 53/212 (rank_frac 0.25) | score_mean 18.585 (top 25.264, ratio 0.7356317289423686, delta 6.6789999999999985)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 555 | vt_triad 1 | score_mean 25.264 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 111 | vt_triad 2 | score_mean 24.896 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 23.004 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 127 | vt_triad 233 | score_mean 22.818 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 277 | vt_triad 33 | score_mean 22.693 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 227 | vt_triad 33 | score_mean 22.613 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 247 | vt_triad 335 | score_mean 22.388 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 279 | vt_triad 335 | score_mean 22.106 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 238 | vt_triad 344 | score_mean 21.638 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 015 | vt_triad 112 | score_mean 20.6 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 022 (canon 022): rank 175/212 (rank_frac 0.825) ratio_to_top=0.621675110829639; Evening 498 (canon 489): rank 53/212 (rank_frac 0.250) ratio_to_top=0.7356317289423686
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

Aux draws snapshot dir: `sharepacks/2026-01-08/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=698, 547, 433, 111, 797
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=547, 111, 555, 958, 968
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-08/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=698, 433, 797, 382, 032

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=62 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=20), P2:0 (gap=17), P3:4 (gap=35)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.6357 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 224: score=43.40072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=39.46358571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=39.254535714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=38.49127142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=38.39855714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 270: score=38.30985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=38.01956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 234: score=37.67724285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 220: score=37.07488571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=933 sev=B
- 039: ds=789 sev=B
- 333: ds=760 sev=B
- 188: ds=733 sev=B
- 266: ds=719 sev=B
- 477: ds=717 sev=B
- 126: ds=709 sev=B
- 669: ds=704 sev=B
- 007: ds=694 sev=B
- 005: ds=685 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=135 sev=red
  - 88: ds=44 sev=purple
  - 44: ds=35 sev=purple
  - 99: ds=23 sev=-
  - 66: ds=22 sev=-
  - 00: ds=19 sev=-
  - 55: ds=5 sev=-
  - 77: ds=4 sev=-
  - 11: ds=3 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 01: ds=70 sev=red
  - 15: ds=67 sev=red
  - 17: ds=61 sev=red
  - 12: ds=47 sev=blue
  - 24: ds=45 sev=blue
  - 26: ds=45 sev=blue
  - 67: ds=42 sev=blue
  - 36: ds=39 sev=blue
  - 48: ds=38 sev=blue
  - 08: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:345, 16:299, 17:171, 20:149, 26:89, 34:76, 8:72, 7:56, 21:55, 22:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=345 fs=1 fl=0 hz=0.005698005698005698, 16:ds=299 fs=2 fl=0 hz=0.006329113924050633, 17:ds=171 fs=19 fl=1 hz=0.024242424242424242, 20:ds=149 fs=13 fl=2 hz=0.01847290640394089, 26:ds=89 fs=2 fl=1 hz=0.006075334143377886, 34:ds=76 fs=14 fl=2 hz=0.019698725376593278, 8:ds=72 fs=39 fl=2 hz=0.044956140350877194, 7:ds=56 fs=43 fl=1 hz=0.04675876726886291, 21:ds=55 fs=37 fl=0 hz=0.03952991452991453, 22:ds=42 fs=52 fl=0 hz=0.0556745182012848

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=87 flags=purple
- S4: ds=81 flags=purple
- S24: ds=46 flags=purple
- S19: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 0}}
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
- current_index=12 streak=1 max=2 last_repeat_gap=23 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=29), P2:7 (gap=29), P3:0 (gap=21)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.6357 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 224: score=43.40072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=39.46358571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=39.254535714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=38.49127142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=38.39855714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 270: score=38.30985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=38.01956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 234: score=37.67724285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 220: score=37.07488571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=984 sev=B
- 255: ds=951 sev=B
- 355: ds=916 sev=B
- 466: ds=837 sev=B
- 446: ds=745 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=67 sev=purple
  - 77: ds=28 sev=purple
  - 88: ds=24 sev=-
  - 66: ds=19 sev=-
  - 44: ds=17 sev=-
  - 99: ds=11 sev=-
  - 33: ds=10 sev=-
  - 00: ds=9 sev=-
  - 55: ds=2 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 34: ds=76 sev=red
  - 07: ds=73 sev=red
  - 16: ds=59 sev=red
  - 39: ds=47 sev=blue
  - 37: ds=42 sev=blue
  - 67: ds=42 sev=blue
  - 48: ds=39 sev=blue
  - 01: ds=35 sev=purple
  - 15: ds=33 sev=purple
  - 17: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:172, 34:167, 16:149, 27:104, 17:85, 20:74, 19:59, 33:47, 26:44, 13:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=172 fs=4 fl=3 hz=0.010432190760059612, 34:ds=167 fs=8 fl=4 hz=0.014423076923076924, 16:ds=149 fs=3 fl=0 hz=0.007462686567164179, 27:ds=104 fs=14 fl=2 hz=0.0196078431372549, 17:ds=85 fs=28 fl=2 hz=0.033112582781456956, 20:ds=74 fs=24 fl=3 hz=0.029315960912052113, 19:ds=59 fs=20 fl=2 hz=0.023732470334412083, 33:ds=47 fs=18 fl=2 hz=0.021119324181626188, 26:ds=44 fs=0 fl=3 hz=0.005376344086021506, 13:ds=41 fs=13 fl=3 hz=0.01816239316239316

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=79 flags=purple
- S1: ds=68 flags=blue+purple
- S5: ds=66 flags=purple
- S9: ds=56 flags=purple
- S21: ds=43 flags=red+purple
- S4: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 0}}
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
- current_index=24 streak=1 max=3 last_repeat_gap=60 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=18), P2:6 (gap=21), P3:9 (gap=45)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.6357 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 224: score=43.40072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=39.46358571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=39.254535714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 264: score=38.49127142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=38.39855714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 270: score=38.30985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=38.01956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 234: score=37.67724285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 220: score=37.07488571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=908 sev=B
- 113: ds=859 sev=B
- 378: ds=852 sev=B
- 566: ds=841 sev=B
- 199: ds=833 sev=B
- 899: ds=811 sev=B
- 126: ds=807 sev=B
- 559: ds=802 sev=B
- 477: ds=791 sev=B
- 558: ds=757 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=237 sev=red
  - 22: ds=68 sev=purple
  - 00: ds=55 sev=purple
  - 44: ds=38 sev=purple
  - 11: ds=25 sev=purple
  - 99: ds=23 sev=-
  - 88: ds=22 sev=-
  - 66: ds=11 sev=-
  - 77: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 36: ds=80 sev=red
  - 24: ds=64 sev=red
  - 15: ds=57 sev=red
  - 78: ds=56 sev=red
  - 49: ds=50 sev=blue
  - 57: ds=47 sev=blue
  - 09: ds=37 sev=blue
  - 01: ds=35 sev=purple
  - 12: ds=35 sev=purple
  - 13: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:433, 1:348, 16:199, 26:131, 17:109, 20:100, 3:79, 23:72, 31:66, 12:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=433 fs=0 fl=2 hz=0.005366726296958855, 1:ds=348 fs=0 fl=0 hz=0.0, 16:ds=199 fs=3 fl=1 hz=0.007853403141361256, 26:ds=131 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=109 fs=13 fl=3 hz=0.018626309662398137, 20:ds=100 fs=15 fl=2 hz=0.01925254813137033, 3:ds=79 fs=15 fl=4 hz=0.02092511013215859, 23:ds=72 fs=25 fl=2 hz=0.03085714285714286, 31:ds=66 fs=23 fl=0 hz=0.02666666666666667, 12:ds=47 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=89 flags=purple
- S2: ds=79 flags=blue+purple
- S4: ds=77 flags=purple
- S25: ds=66 flags=purple
- S20: ds=59 flags=purple
- S9: ds=57 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:709(B); evening:807(B)
- 128 -> combined:933(B); evening:908(B)
- 226 -> combined:671(B); evening:709(B)
- 333 -> combined:760(B); midday:984(B)
- 477 -> combined:717(B); evening:791(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:70(red); evening:35(purple); midday:35(purple)
- 07 -> combined:26(purple); midday:73(red)
- 12 -> combined:47(blue); evening:35(purple)
- 15 -> combined:67(red); evening:57(red); midday:33(purple)
- 17 -> combined:61(red); evening:31(purple); midday:30(purple)
- 22 -> combined:135(red); evening:68(purple); midday:67(purple)
- 24 -> combined:45(blue); evening:64(red)
- 26 -> combined:45(blue); evening:28(purple)
- 36 -> combined:39(blue); evening:80(red)
- 44 -> combined:35(purple); evening:38(purple)
- 48 -> combined:38(blue); midday:39(blue)
- 67 -> combined:42(blue); midday:42(blue)
- 78 -> combined:31(purple); evening:56(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(7.969428571428571)[R1,XVAR-Cons(CEM)], 7(1.6787714285714284)[R2,Mirror-Echo], 1(1.1374285714285712)[R1,Double-Pressure], 8(0.9199999999999999)[R2,Double-Pressure], 6(0.3552785714285714)[R3,Swap]
- P2: 7(3.9714285714285715)[R2,Mirror-Echo], 2(2.7364571428571427)[R3,Mirror-Echo], 6(1.327)[R1,Double-Pressure], 8(1.2993142857142856)[R2,Mirror-Echo], 0(1.2342857142857142)[R1,Double-Pressure]
- P3: 4(6.6948428571428575)[R1,Mirror-Echo], 0(3.8689999999999998)[R2,XVAR-Cons(CM)], 9(3.8136785714285715)[R3,Mirror-Echo], 1(1.1225)[R2,Double-Pressure], 2(1.1179999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=20), P2:0(gap=17), P3:4(gap=35); top cartesian candidates: 274, 224, 284, 279, 264.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:709(B),evening:807(B); 128→combined:933(B),evening:908(B); 226→combined:671(B),evening:709(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:345, 16:299, 17:171, 20:149, 26:89.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=022 Evening=498; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 022 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 489 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 022 (canon 022): box `022` covers winner `022` (boxed hit).
  - Evening winner 498 (canon 489): box `489` covers winner `498` (boxed hit).
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
