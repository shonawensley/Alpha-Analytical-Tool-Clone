# Master Validation Run Report — OntarioCanada4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-02/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-02/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-02/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-02/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-02/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-02/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac18_winner_816_20260105_070920.html`
- `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac4_winner_053_20260105_070919.html`

Winners JSON files:
- `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac18_winner_816_20260105_070920.json`
- `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac4_winner_053_20260105_070919.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 053 (canon 035): exact_boxed=True exact_straight=True | rank 3538/3928 (rank_frac 0.901); Evening 816 (canon 168): exact_boxed=True exact_straight=True | rank 249/3928 (rank_frac 0.063)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 816 idx18 (rank 2/35, frac 0.057), 053 idx4 (rank 14/35, frac 0.400)
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

### 2.Stable — OntarioCanada4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-02)

## Midday winner 053 (canonical 035)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=17 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 3538/3928 (rank_frac 0.9007128309572301) | score 9.0 (top 37.0, ratio 0.24324324324324326, delta 28.0) | section Combined, Set Set1, Draw Draw6, Col 2, hot 0, vt_straight 2.0 | why straight|cov1|mirror|vtrac_straight
- Compound (patterns_compound.csv): rank 688/961 (rank_frac 0.7159209157127991) | score 11.5 (top 95.0, ratio 0.12105263157894737, delta 83.5) | section Midday, col1_hits 1, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x1|vstrx1
- Families (patterns_families.csv): count 14 | rank 329/1233 (rank_frac 0.26682887266828875) | score 20.0 (top 33.5, ratio 0.5970149253731343, delta 13.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=4

## Evening winner 816 (canonical 168)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=233 | exact_boxed=17 | exact_straight=6 | vt_boxed=17
- Scores (patterns_scores.csv): rank 249/3928 (rank_frac 0.06339103869653767) | score 21.5 (top 37.0, ratio 0.581081081081081, delta 15.5) | section Combined, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 0.0 | why boxed|cov4|hp_repeat2|vstr2|mirror|hot2|perm2|hidden3v|draw_chain5
- Compound (patterns_compound.csv): rank 82/961 (rank_frac 0.08532778355879292) | score 32.0 (top 95.0, ratio 0.3368421052631579, delta 63.0) | section Combined, col1_hits 1, hot2 1, set_chain 1, draw_chain 6 | why draw_chain6|col1x1|hot1x4|hot2x1|vstrx1
- Families (patterns_families.csv): count 78 | rank 2/1233 (rank_frac 0.0016220600162206002) | score 31.5 (top 33.5, ratio 0.9402985074626866, delta 2.0) | section Evening, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=17

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 118 | section Evening | score 95.0 | col1_hits 9 | hot2 11
- rank    3 | canon 1188 | section Evening | score 79.0 | col1_hits 8 | hot2 11
- rank    2 | canon 188 | section Evening | score 86.0 | col1_hits 8 | hot2 11
- rank   19 | canon 167 | section Combined | score 49.5 | col1_hits 4 | hot2 7
- rank    4 | canon 114 | section Evening | score 77.0 | col1_hits 2 | hot2 6
- rank   17 | canon 1158 | section Evening | score 51.0 | col1_hits 1 | hot2 6
- rank   15 | canon 11588 | section Evening | score 55.0 | col1_hits 1 | hot2 6
- rank   10 | canon 225 | section Midday | score 57.0 | col1_hits 0 | hot2 6
- rank   28 | canon 257 | section Midday | score 43.0 | col1_hits 4 | hot2 6
- rank   16 | canon 11488 | section Evening | score 54.0 | col1_hits 1 | hot2 6

## Top families (patterns_families.csv)
- rank 1199 | family 19 | score 5.5 | hot2 0 | section Midday
- rank  600 | family 7 | score 15.5 | hot2 0 | section Midday
- rank  863 | family 2 | score 12.0 | hot2 1 | section Midday
- rank  993 | family 27 | score 10.0 | hot2 1 | section Midday
- rank 1055 | family 11 | score 9.0 | hot2 6 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 053 (canon 035): exact_boxed=True exact_straight=True | rank 3538/3928 (rank_frac 0.901); Evening 816 (canon 168): exact_boxed=True exact_straight=True | rank 249/3928 (rank_frac 0.063)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260102)

## Midday winner 053 (canonical 035)
- Stamp (winner_stamp.json): items_total=3 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=3 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=3 | exact_any=0 vtrac_any=0 | drop_exact_any=1 drop_vtrac_any=3 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=3 vt_straight=0
- Hits (winner_hits.csv): rows=3 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=3 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 816 (canonical 168)
- Stamp (winner_stamp.json): items_total=372 | exact_any=44 exact_final=0 | vtrac_any=372 vtrac_final=31 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=79 drop_vtrac_final=27 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=40 family_vtrac_final=31
- Flags (winner_flags.csv): rows=372 | exact_any=44 vtrac_any=372 | drop_exact_any=0 drop_vtrac_any=79 | family_exact_any=0 family_vtrac_any=40 | vt_boxed=62 vt_straight=31
- Hits (winner_hits.csv): rows=372 | exact_final=0 vtrac_final=31 | drop_exact_final=0 drop_vtrac_final=27 | family_exact_final=0 family_vtrac_final=31 | vt_boxed=62 vt_straight=31
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.878571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 053 (canonical 035)
- Stamp (winner_stamp.json): items_total=76 | exact_any=0 exact_final=0 | vtrac_any=24 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=76 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=24 family_vtrac_final=0
- Flags (winner_flags.csv): rows=76 | exact_any=0 vtrac_any=24 | drop_exact_any=1 drop_vtrac_any=76 | family_exact_any=0 family_vtrac_any=24 | vt_boxed=16 vt_straight=0
- Hits (winner_hits.csv): rows=76 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=16 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.008571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 552 | score_v2 9.677143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 522 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 552 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 522 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 522 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 522 | score_v2 9.477143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 552 | score_v2 9.437143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 552 | score_v2 9.437143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 552 | score_v2 9.437143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 522 | score_v2 9.437143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 552 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 522 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 522 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 552 | score_v2 9.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 552 | score_v2 9.008571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 552 | score_v2 9.008571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 594 | score_v2 8.878571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 592 | score_v2 8.807143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 592 | score_v2 8.767143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 559 | score_v2 8.707143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 053 (canon 035): items_total=3 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/18; Evening 816 (canon 168): items_total=372 exact_any=44 vtrac_any=372 | top winner_present=False best_rank=None/22; Combined 053 (canon 035): items_total=76 exact_any=0 vtrac_any=24 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 522, 522, 552, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_071330)

## Top indices (from enhanced JSON)
- index 23 | score 90.27955999999996 | features: presence=63.802059999999955, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 85.03548749999995 | features: presence=55.60798749999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 31.267227499999994 | features: presence=20.519727499999995, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 21 | score 30.823055 | features: presence=17.045555, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 27.508205 | features: presence=17.620704999999997, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 10 | score 25.218500000000002 | features: presence=17.831000000000003, cross_section=0.5, set_echo=0.3, first_hit=0.33333333333333337
- index 27 | score 24.734650000000002 | features: presence=15.977150000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 2 | score 24.64844 | features: presence=16.60094, set_echo=0.6, first_hit=0.33333333333333337, column_span=0.25416666666666665
- index 6 | score 22.523762500000004 | features: presence=14.4162625, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 17 | score 19.354300000000002 | features: presence=8.136800000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
681, 186, 138, 831, 386, 836, 683, 183, 813, 568

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 816 | index 18 | file OntarioCanada4_vtrac18_winner_816_20260105_070920.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 053 | index 4 | file OntarioCanada4_vtrac4_winner_053_20260105_070919.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 816 | index 18 rank 2/35 (rank_frac 0.05714285714285714) | score 85.03548749999995 (top 90.27955999999996, ratio 0.9419129590352454, delta 5.244072500000016) | winner_in_index_straights=False | top_index_straights: 681 (20.602), 186 (20.476)
- winner 053 | index 4 rank 14/35 (rank_frac 0.4) | score 18.3384225 (top 90.27955999999996, ratio 0.20312928530001706, delta 71.94113749999997) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 816→idx18 rank 2/35 (frac 0.057); 053→idx4 rank 14/35 (frac 0.400).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 23, 18, 8, 21, 29.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-02)

## Midday winner 053 (canonical 035)
- Top lanes (hot_zones_top_lanes.csv): present | rank 160/210 (rank_frac 0.7619047619047619) | score_mean 16.217 (top 22.008, ratio 0.7368684114867321, delta 5.791)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 816 (canonical 168)
- Top lanes (hot_zones_top_lanes.csv): present | rank 66/210 (rank_frac 0.3142857142857143) | score_mean 17.697 (top 22.008, ratio 0.8041166848418757, delta 4.311)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 237 | vt_triad 334 | score_mean 22.008 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 118 | vt_triad 24 | score_mean 20.306 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 114 | vt_triad 25 | score_mean 20.201 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 239 | vt_triad 345 | score_mean 19.933 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 188 | vt_triad 24 | score_mean 19.908 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    6 | triad 225 | vt_triad 13 | score_mean 19.794 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 244 | vt_triad 35 | score_mean 19.782 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical3,vt_straight
- rank    8 | triad 189 | vt_triad 245 | score_mean 19.778 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    9 | triad 049 | vt_triad 155 | score_mean 19.751 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 456 | vt_triad 125 | score_mean 19.678 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 053 (canon 035): rank 160/210 (rank_frac 0.762) ratio_to_top=0.7368684114867321; Evening 816 (canon 168): rank 66/210 (rank_frac 0.314) ratio_to_top=0.8041166848418757
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

Aux draws snapshot dir: `sharepacks/2026-01-02/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=546, 528, 932, 918, 372
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=528, 918, 409, 006, 313
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=546, 932, 372, 043, 297

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=50 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=24), P2:8 (gap=22), P3:4 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=921 sev=B
- 555: ds=886 sev=B
- 039: ds=777 sev=B
- 333: ds=748 sev=B
- 188: ds=721 sev=B
- 266: ds=707 sev=B
- 477: ds=705 sev=B
- 126: ds=697 sev=B
- 669: ds=692 sev=B
- 007: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=123 sev=red
  - 55: ds=79 sev=blue
  - 11: ds=38 sev=purple
  - 88: ds=32 sev=purple
  - 44: ds=23 sev=-
  - 77: ds=14 sev=-
  - 99: ds=11 sev=-
  - 66: ds=10 sev=-
  - 33: ds=9 sev=-
  - 00: ds=7 sev=-
- non_repeating:
  - 01: ds=58 sev=red
  - 68: ds=56 sev=red
  - 15: ds=55 sev=blue
  - 17: ds=49 sev=blue
  - 12: ds=35 sev=purple
  - 69: ds=34 sev=purple
  - 24: ds=33 sev=purple
  - 26: ds=33 sev=purple
  - 67: ds=30 sev=purple
  - 36: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:333, 16:287, 17:159, 20:137, 33:83, 12:82, 26:77, 34:64, 8:60, 7:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=333 fs=1 fl=0 hz=0.005698005698005698, 16:ds=287 fs=2 fl=0 hz=0.006329113924050633, 17:ds=159 fs=19 fl=1 hz=0.024242424242424242, 20:ds=137 fs=13 fl=2 hz=0.01847290640394089, 33:ds=83 fs=24 fl=1 hz=0.027472527472527472, 12:ds=82 fs=45 fl=0 hz=0.04928806133625411, 26:ds=77 fs=2 fl=1 hz=0.006075334143377886, 34:ds=64 fs=14 fl=2 hz=0.019698725376593278, 8:ds=60 fs=39 fl=2 hz=0.044956140350877194, 7:ds=44 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=78 flags=blue+purple
- S21: ds=75 flags=purple
- S4: ds=69 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=3 tags=FLT,RS
  - 028: score=3 tags=FLT,RS
  - 037: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=2 tags=RS
  - 136: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS
  - 289: score=2 tags=RS
  - 379: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=17 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:7 (gap=23), P3:0 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=995 sev=B
- 333: ds=978 sev=B
- 255: ds=945 sev=B
- 355: ds=910 sev=B
- 466: ds=831 sev=B
- 446: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=61 sev=purple
  - 55: ds=39 sev=purple
  - 11: ds=29 sev=purple
  - 77: ds=22 sev=-
  - 88: ds=18 sev=-
  - 66: ds=13 sev=-
  - 44: ds=11 sev=-
  - 99: ds=5 sev=-
  - 33: ds=4 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 34: ds=70 sev=red
  - 07: ds=67 sev=red
  - 16: ds=53 sev=blue
  - 39: ds=41 sev=blue
  - 68: ds=37 sev=blue
  - 37: ds=36 sev=purple
  - 67: ds=36 sev=purple
  - 03: ds=34 sev=purple
  - 48: ds=33 sev=purple
  - 01: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:166, 34:161, 16:143, 27:98, 12:95, 14:80, 17:79, 20:68, 19:53, 33:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=166 fs=4 fl=3 hz=0.010432190760059612, 34:ds=161 fs=8 fl=4 hz=0.014423076923076924, 16:ds=143 fs=3 fl=0 hz=0.007462686567164179, 27:ds=98 fs=15 fl=2 hz=0.0189520624303233, 12:ds=95 fs=45 fl=0 hz=0.05079006772009029, 14:ds=80 fs=39 fl=0 hz=0.04276315789473684, 17:ds=79 fs=29 fl=2 hz=0.033879781420765025, 20:ds=68 fs=24 fl=3 hz=0.029315960912052113, 19:ds=53 fs=20 fl=2 hz=0.023732470334412083, 33:ds=41 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=77 flags=purple
- S25: ds=73 flags=purple
- S1: ds=62 flags=blue+purple
- S5: ds=60 flags=purple
- S8: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 127: score=1 tags=FLT
  - 137: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=54 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=16), P2:1 (gap=52), P3:9 (gap=39)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=52)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=902 sev=B
- 113: ds=853 sev=B
- 378: ds=846 sev=B
- 566: ds=835 sev=B
- 199: ds=827 sev=B
- 899: ds=805 sev=B
- 126: ds=801 sev=B
- 559: ds=796 sev=B
- 477: ds=785 sev=B
- 558: ds=751 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=231 sev=red
  - 22: ds=62 sev=purple
  - 00: ds=49 sev=purple
  - 44: ds=32 sev=purple
  - 11: ds=19 sev=-
  - 99: ds=17 sev=-
  - 88: ds=16 sev=-
  - 33: ds=14 sev=-
  - 77: ds=7 sev=-
  - 66: ds=5 sev=-
- non_repeating:
  - 36: ds=74 sev=red
  - 24: ds=58 sev=red
  - 18: ds=52 sev=blue
  - 89: ds=52 sev=blue
  - 15: ds=51 sev=blue
  - 78: ds=50 sev=blue
  - 49: ds=44 sev=blue
  - 57: ds=41 sev=blue
  - 09: ds=31 sev=purple
  - 01: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:427, 1:342, 16:193, 26:125, 18:110, 17:103, 20:94, 3:73, 23:66, 33:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=427 fs=0 fl=2 hz=0.005366726296958855, 1:ds=342 fs=0 fl=0 hz=0.0, 16:ds=193 fs=3 fl=1 hz=0.007853403141361256, 26:ds=125 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=110 fs=16 fl=1 hz=0.019384264538198404, 17:ds=103 fs=13 fl=3 hz=0.018626309662398137, 20:ds=94 fs=15 fl=2 hz=0.01925254813137033, 3:ds=73 fs=15 fl=4 hz=0.02092511013215859, 23:ds=66 fs=25 fl=2 hz=0.03085714285714286, 33:ds=64 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=83 flags=purple
- S2: ds=73 flags=blue+purple
- S4: ds=71 flags=purple
- S25: ds=60 flags=purple
- S20: ds=53 flags=purple
- S9: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:697(B); evening:801(B)
- 128 -> combined:921(B); evening:902(B)
- 333 -> combined:748(B); midday:978(B)
- 477 -> combined:705(B); evening:785(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:58(red); evening:29(purple); midday:29(purple)
- 11 -> combined:38(purple); midday:29(purple)
- 12 -> combined:35(purple); evening:29(purple)
- 15 -> combined:55(blue); evening:51(blue); midday:27(purple)
- 17 -> combined:49(blue); evening:25(purple)
- 22 -> combined:123(red); evening:62(purple); midday:61(purple)
- 24 -> combined:33(purple); evening:58(red)
- 36 -> combined:27(purple); evening:74(red)
- 48 -> combined:26(purple); midday:33(purple)
- 55 -> combined:79(blue); evening:231(red); midday:39(purple)
- 67 -> combined:30(purple); midday:36(purple)
- 68 -> combined:56(red); evening:28(purple); midday:37(blue)
- 69 -> combined:34(purple); midday:28(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.061800000000001)[R1,XVAR-Cons(CEM)], 8(3.5957142857142856)[R2,XVAR-Cons(CE)], 7(2.112085714285714)[R3,XVAR-Cons(CM)], 2(1.2150571428571428)[R2,Mirror-Echo], 4(0.8716999999999999)[R2,Double-Pressure]
- P2: 8(6.676492857142858)[R1,XVAR-Cons(CEM)], 6(3.8024999999999998)[R2,XVAR-Cons(CE)], 1(1.8875)[R1,Mirror-Echo], 7(1.3867142857142856)[R1,Double-Pressure], 3(0.37535714285714283)[R3,Mirror-Echo]
- P3: 4(6.047185714285714)[R1,XVAR-Cons(CEM)], 1(2.679242857142857)[R3,XVAR-Cons(CE)], 9(1.7366071428571428)[R1,Mirror-Echo], 0(1.1178571428571429)[R1,Double-Pressure], 5(0.974)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=24), P2:8(gap=22), P3:4(gap=23); top cartesian candidates: 184, 181, 164, 884, 484.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 019, 028, 037, 046, 127.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:697(B),evening:801(B); 128→combined:921(B),evening:902(B); 333→combined:748(B),midday:978(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:333, 16:287, 17:159, 20:137, 33:83.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=053 Evening=816; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 035 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 168 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 053 (canon 035): box `035` covers winner `053` (boxed hit).
  - Evening winner 816 (canon 168): box `168` covers winner `816` (boxed hit).
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
