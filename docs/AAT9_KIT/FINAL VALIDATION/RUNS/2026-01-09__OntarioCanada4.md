# Master Validation Run Report — OntarioCanada4 — results 2026-01-09 (history workbook ~ 2026-01-08)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-09/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-09/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-09/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-09/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-09/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-09/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac26_winner_772_20260110_035057.html`
- `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_104_20260110_035057.html`

Winners JSON files:
- `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac26_winner_772_20260110_035057.json`
- `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_104_20260110_035057.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 772 (canon 277): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 104 (canon 014): exact_boxed=True exact_straight=True | rank 145/5201 (rank_frac 0.028)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 772 idx26 (rank 35/35, frac 1.000), 104 idx9 (rank 23/35, frac 0.657)
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

### 2.Stable — OntarioCanada4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-09)

## Midday winner 772 (canonical 277)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=504 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 69 | rank 35/1460 (rank_frac 0.023972602739726026) | score 27.0 (top 34.5, ratio 0.782608695652174, delta 7.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=0
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 104 (canonical 014)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=32 | family_rows=0 | exact_boxed=32 | exact_straight=27 | vt_boxed=32
- Scores (patterns_scores.csv): rank 145/5201 (rank_frac 0.02787925398961738) | score 22.0 (top 40.5, ratio 0.5432098765432098, delta 18.5) | section Evening, Set Set1, Draw Draw3, Col 2, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat4|hot2|perm3|set_chain3|draw_chain4
- Compound (patterns_compound.csv): rank 32/1873 (rank_frac 0.017084890549919914) | score 39.5 (top 81.0, ratio 0.4876543209876543, delta 41.5) | section Evening, col1_hits 0, hot2 2, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|hot1x6|hot2x2|vstrx3
- Families (patterns_families.csv): not present
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=158

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 347 | section Midday | score 73.5 | col1_hits 8 | hot2 10
- rank    4 | canon 367 | section Midday | score 72.0 | col1_hits 5 | hot2 9
- rank    2 | canon 015 | section Evening | score 74.5 | col1_hits 6 | hot2 9
- rank    5 | canon 346 | section Midday | score 65.5 | col1_hits 4 | hot2 8
- rank   19 | canon 034 | section Midday | score 47.0 | col1_hits 4 | hot2 6
- rank   26 | canon 036 | section Midday | score 41.5 | col1_hits 1 | hot2 6
- rank    6 | canon 055 | section Evening | score 60.0 | col1_hits 5 | hot2 6
- rank   93 | canon 067 | section Midday | score 31.5 | col1_hits 1 | hot2 5
- rank   23 | canon 037 | section Midday | score 43.5 | col1_hits 1 | hot2 5
- rank   59 | canon 024 | section Midday | score 35.5 | col1_hits 0 | hot2 5

## Top families (patterns_families.csv)
- rank 1434 | family 4 | score 5.0 | hot2 0 | section Midday
- rank  159 | family 10 | score 22.0 | hot2 0 | section Midday
- rank  803 | family 7 | score 14.0 | hot2 0 | section Midday
- rank  803 | family 27 | score 14.0 | hot2 0 | section Midday
- rank  608 | family 30 | score 16.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 772 (canon 277): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 104 (canon 014): exact_boxed=True exact_straight=True | rank 145/5201 (rank_frac 0.028)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260110)

## Midday winner 772 (canonical 277)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=8.108571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 104 (canonical 014)
- Stamp (winner_stamp.json): items_total=240 | exact_any=204 exact_final=0 | vtrac_any=240 vtrac_final=0 | drop_exact_any=24 drop_exact_final=0 | drop_vtrac_any=66 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=240 | exact_any=204 vtrac_any=240 | drop_exact_any=24 drop_vtrac_any=66 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=240 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.477143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 772 (canonical 277)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 11.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 11.077143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 501 | score_v2 10.984643 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 552 | score_v2 10.927143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 552 | score_v2 10.827143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 552 | score_v2 10.677143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 552 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 552 | score_v2 10.277143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 552 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 501 | score_v2 10.984643 | tags exact,vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 501 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 559 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 501 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 924 | score_v2 8.820476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 924 | score_v2 8.820476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 552 | score_v2 8.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 200 | score_v2 8.59381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 772 (canon 277): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/26; Evening 104 (canon 014): items_total=240 exact_any=204 vtrac_any=240 | top winner_present=False best_rank=None/20; Combined 772 (canon 277): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/36
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 552, 501, 559, 501, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260110_035302)

## Top indices (from enhanced JSON)
- index 30 | score 48.47049999999999 | features: presence=29.892999999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 47.5035525 | features: presence=34.1560525, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 40.7457 | features: presence=27.238200000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 32.695499999999996 | features: presence=16.677999999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 28.308137500000008 | features: presence=19.280637500000005, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 25.453037500000004 | features: presence=16.1255375, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 6 | score 24.981817500000002 | features: presence=14.374317499999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 24 | score 24.858610000000002 | features: presence=15.981110000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 24.763175000000004 | features: presence=14.385675, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 14 | score 24.016350000000006 | features: presence=12.658850000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
324, 347, 367, 243, 362, 732, 634, 036, 437, 234

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 772 | index 26 | file OntarioCanada4_vtrac26_winner_772_20260110_035057.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 104 | index 9 | file OntarioCanada4_vtrac9_winner_104_20260110_035057.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 772 | index 26 rank 35/35 (rank_frac 1.0) | score 0.0 (top 48.47049999999999, ratio 0.0, delta 48.47049999999999) | winner_in_index_straights=False | top_index_straights: (none)
- winner 104 | index 9 rank 23/35 (rank_frac 0.6571428571428571) | score 8.898325000000002 (top 48.47049999999999, ratio 0.18358228200658142, delta 39.57217499999999) | winner_in_index_straights=False | top_index_straights: 406 (2.954), 604 (2.499), 906 (2.143)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 772→idx26 rank 35/35 (frac 1.000); 104→idx9 rank 23/35 (frac 0.657).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 30, 2, 21, 27, 5.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-09

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-09)

## Midday winner 772 (canonical 277)
- Top lanes (hot_zones_top_lanes.csv): present | rank 7/212 (rank_frac 0.0330188679245283) | score_mean 20.81 (top 25.209, ratio 0.8254988297830139, delta 4.399000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Evening winner 104 (canonical 014)
- Top lanes (hot_zones_top_lanes.csv): present | rank 29/212 (rank_frac 0.13679245283018868) | score_mean 19.19 (top 25.209, ratio 0.7612360664841922, delta 6.018999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 111 | vt_triad 2 | score_mean 25.209 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_straight
- rank    2 | triad 555 | vt_triad 1 | score_mean 24.262 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    3 | triad 489 | vt_triad 455 | score_mean 22.55 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 279 | vt_triad 335 | score_mean 21.058 | tags col1,funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 247 | vt_triad 335 | score_mean 21.058 | tags col1,funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 457 | vt_triad 135 | score_mean 20.942 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 227 | vt_triad 33 | score_mean 20.81 | tags col1,funnel_precol1,hot16,ls_col_42,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 277 | vt_triad 33 | score_mean 20.81 | tags col1,funnel_precol1,hot16,ls_col_42,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 127 | vt_triad 233 | score_mean 20.75 | tags col1,funnel_precol1,hot16,ls_col_42,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 267 | vt_triad 233 | score_mean 20.75 | tags col1,funnel_precol1,hot16,ls_col_42,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 772 (canon 277): rank 7/212 (rank_frac 0.033) ratio_to_top=0.8254988297830139; Evening 104 (canon 014): rank 29/212 (rank_frac 0.137) ratio_to_top=0.7612360664841922
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

Aux draws snapshot dir: `sharepacks/2026-01-09/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-09

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-09/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-08.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-09/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=498, 022, 698, 547, 433
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-09/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=022, 547, 111, 555, 958
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-09/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=498, 698, 433, 797, 382

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=64 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=22), P2:0 (gap=19), P3:4 (gap=37)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.493185714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 264: score=43.4439 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=40.35779285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=39.32861428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=39.04497142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 234: score=38.56737857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=38.372328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 270: score=37.46711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 269: score=37.32304285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 260: score=36.41782857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=935 sev=B
- 039: ds=791 sev=B
- 333: ds=762 sev=B
- 188: ds=735 sev=B
- 266: ds=721 sev=B
- 477: ds=719 sev=B
- 126: ds=711 sev=B
- 669: ds=706 sev=B
- 007: ds=696 sev=B
- 005: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=46 sev=purple
  - 44: ds=37 sev=purple
  - 99: ds=25 sev=purple
  - 66: ds=24 sev=-
  - 00: ds=21 sev=-
  - 55: ds=7 sev=-
  - 77: ds=6 sev=-
  - 11: ds=5 sev=-
  - 33: ds=4 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 01: ds=72 sev=red
  - 15: ds=69 sev=red
  - 17: ds=63 sev=red
  - 12: ds=49 sev=blue
  - 24: ds=47 sev=blue
  - 26: ds=47 sev=blue
  - 67: ds=44 sev=blue
  - 36: ds=41 sev=blue
  - 08: ds=34 sev=purple
  - 78: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:347, 16:301, 17:173, 20:151, 26:91, 8:74, 7:58, 21:57, 22:44, 3:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=347 fs=1 fl=0 hz=0.005698005698005698, 16:ds=301 fs=2 fl=0 hz=0.006329113924050633, 17:ds=173 fs=19 fl=1 hz=0.024242424242424242, 20:ds=151 fs=13 fl=2 hz=0.01847290640394089, 26:ds=91 fs=2 fl=1 hz=0.006075334143377886, 8:ds=74 fs=39 fl=2 hz=0.044956140350877194, 7:ds=58 fs=43 fl=1 hz=0.04675876726886291, 21:ds=57 fs=37 fl=0 hz=0.03952991452991453, 22:ds=44 fs=52 fl=0 hz=0.0556745182012848, 3:ds=43 fs=19 fl=3 hz=0.023809523809523808

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=48 flags=purple
- S19: ds=46 flags=purple
- S2: ds=43 flags=blue+purple
- S17: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 146: score=4 tags=FLT,MIR,RS
  - 038: score=3 tags=MIR,RS
  - 056: score=3 tags=MIR,RS
  - 128: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 389: score=3 tags=MIR,RS
  - 479: score=3 tags=MIR,RS
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 029: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=2 last_repeat_gap=24 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:7 (gap=30), P3:0 (gap=22)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.493185714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 264: score=43.4439 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=40.35779285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=39.32861428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=39.04497142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 234: score=38.56737857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=38.372328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 270: score=37.46711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 269: score=37.32304285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 260: score=36.41782857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=985 sev=B
- 255: ds=952 sev=B
- 355: ds=917 sev=B
- 466: ds=838 sev=B
- 446: ds=746 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=29 sev=purple
  - 88: ds=25 sev=purple
  - 66: ds=20 sev=-
  - 44: ds=18 sev=-
  - 99: ds=12 sev=-
  - 33: ds=11 sev=-
  - 00: ds=10 sev=-
  - 55: ds=3 sev=-
  - 11: ds=2 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 34: ds=77 sev=red
  - 07: ds=74 sev=red
  - 16: ds=60 sev=red
  - 39: ds=48 sev=blue
  - 37: ds=43 sev=blue
  - 67: ds=43 sev=blue
  - 48: ds=40 sev=blue
  - 01: ds=36 sev=purple
  - 15: ds=34 sev=purple
  - 17: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:173, 34:168, 16:150, 27:105, 17:86, 20:75, 19:60, 33:48, 26:45, 13:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=173 fs=4 fl=3 hz=0.010432190760059612, 34:ds=168 fs=8 fl=3 hz=0.015068493150684932, 16:ds=150 fs=3 fl=0 hz=0.007462686567164179, 27:ds=105 fs=14 fl=2 hz=0.0196078431372549, 17:ds=86 fs=28 fl=2 hz=0.033112582781456956, 20:ds=75 fs=24 fl=3 hz=0.029315960912052113, 19:ds=60 fs=20 fl=2 hz=0.023732470334412083, 33:ds=48 fs=18 fl=2 hz=0.021119324181626188, 26:ds=45 fs=0 fl=3 hz=0.005376344086021506, 13:ds=42 fs=13 fl=3 hz=0.01816239316239316

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=80 flags=purple
- S1: ds=69 flags=blue+purple
- S5: ds=67 flags=purple
- S9: ds=57 flags=purple
- S21: ds=44 flags=red+purple
- S19: ds=25 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=61 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=19), P2:6 (gap=22), P3:9 (gap=46)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 274: score=44.493185714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 264: score=43.4439 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=40.35779285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=39.32861428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=39.04497142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 234: score=38.56737857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 279: score=38.372328571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 270: score=37.46711428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 269: score=37.32304285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 260: score=36.41782857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=909 sev=B
- 113: ds=860 sev=B
- 378: ds=853 sev=B
- 566: ds=842 sev=B
- 199: ds=834 sev=B
- 899: ds=812 sev=B
- 126: ds=808 sev=B
- 559: ds=803 sev=B
- 477: ds=792 sev=B
- 558: ds=758 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=238 sev=red
  - 22: ds=69 sev=purple
  - 00: ds=56 sev=purple
  - 44: ds=39 sev=purple
  - 11: ds=26 sev=purple
  - 99: ds=24 sev=-
  - 88: ds=23 sev=-
  - 66: ds=12 sev=-
  - 77: ds=3 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 36: ds=81 sev=red
  - 24: ds=65 sev=red
  - 15: ds=58 sev=red
  - 78: ds=57 sev=red
  - 57: ds=48 sev=blue
  - 09: ds=38 sev=blue
  - 01: ds=36 sev=purple
  - 12: ds=36 sev=purple
  - 13: ds=32 sev=purple
  - 17: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:434, 1:349, 16:200, 26:132, 17:110, 20:101, 3:80, 23:73, 31:67, 12:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=434 fs=0 fl=2 hz=0.005366726296958855, 1:ds=349 fs=0 fl=0 hz=0.0, 16:ds=200 fs=3 fl=1 hz=0.007853403141361256, 26:ds=132 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=110 fs=13 fl=3 hz=0.018626309662398137, 20:ds=101 fs=15 fl=2 hz=0.01925254813137033, 3:ds=80 fs=15 fl=4 hz=0.02092511013215859, 23:ds=73 fs=25 fl=2 hz=0.03085714285714286, 31:ds=67 fs=23 fl=0 hz=0.02666666666666667, 12:ds=48 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=90 flags=purple
- S2: ds=80 flags=blue+purple
- S4: ds=78 flags=purple
- S25: ds=67 flags=purple
- S20: ds=60 flags=purple
- S9: ds=58 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '5'], 'pairs': {'remaining_count': 0}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:711(B); evening:808(B)
- 128 -> combined:935(B); evening:909(B)
- 226 -> combined:673(B); evening:710(B)
- 333 -> combined:762(B); midday:985(B)
- 477 -> combined:719(B); evening:792(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:72(red); evening:36(purple); midday:36(purple)
- 07 -> combined:28(purple); midday:74(red)
- 12 -> combined:49(blue); evening:36(purple)
- 15 -> combined:69(red); evening:58(red); midday:34(purple)
- 17 -> combined:63(red); evening:32(purple); midday:31(purple)
- 24 -> combined:47(blue); evening:65(red)
- 26 -> combined:47(blue); evening:29(purple)
- 36 -> combined:41(blue); evening:81(red)
- 44 -> combined:37(purple); evening:39(purple)
- 67 -> combined:44(blue); midday:43(blue)
- 78 -> combined:33(purple); evening:57(red)
- 88 -> combined:46(purple); midday:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.062542857142857)[R1,XVAR-Cons(CEM)], 7(1.713242857142857)[R2,Mirror-Echo], 9(1.5347714285714287)[R3,XVAR-Cons(CE)], 1(1.2372857142857143)[R1,Double-Pressure], 8(0.964)[R2,Double-Pressure]
- P2: 7(3.9617142857142857)[R2,XVAR-Cons(CM)], 6(2.9124285714285714)[R3,XVAR-Cons(CE)], 8(1.3263214285714284)[R2,Mirror-Echo], 0(1.2971428571428572)[R1,Double-Pressure], 2(1.0135)[R2,Double-Pressure]
- P3: 4(7.468928571428572)[R1,Mirror-Echo], 0(3.9428571428571426)[R2,XVAR-Cons(CM)], 9(3.848071428571429)[R3,Mirror-Echo], 1(1.2134)[R2,Double-Pressure], 6(0.23435714285714285)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-08.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=22), P2:0(gap=19), P3:4(gap=37); top cartesian candidates: 274, 264, 284, 204, 224.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 146, 038, 056, 128, 137.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:711(B),evening:808(B); 128→combined:935(B),evening:909(B); 226→combined:673(B),evening:710(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:347, 16:301, 17:173, 20:151, 26:91.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=772 Evening=104; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 277 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 014 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 772 (canon 277): box `277` covers winner `772` (boxed hit).
  - Evening winner 104 (canon 014): box `014` covers winner `104` (boxed hit).
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
