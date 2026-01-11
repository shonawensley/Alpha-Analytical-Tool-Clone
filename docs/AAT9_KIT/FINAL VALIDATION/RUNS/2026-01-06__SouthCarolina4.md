# Master Validation Run Report — SouthCarolina4 — results 2026-01-06 (history workbook ~ 2026-01-05)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-06/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-06/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-06/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-06/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-06/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-06/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-06/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac22_winner_412_20260107_052321.html`
- `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac8_winner_586_20260107_052319.html`

Winners JSON files:
- `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac22_winner_412_20260107_052321.json`
- `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac8_winner_586_20260107_052319.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-06/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 586 (canon 568): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 412 (canon 124): exact_boxed=True exact_straight=True | rank 4412/4692 (rank_frac 0.940)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 412 idx22 (rank 3/35, frac 0.086), 586 idx8 (rank 21/35, frac 0.600)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **support (some Stable exact boxed hits)**.
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

### 2.Stable — SouthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-06)

## Midday winner 586 (canonical 568)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=325 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 56 | rank 131/1431 (rank_frac 0.09154437456324249) | score 23.0 (top 31.0, ratio 0.7419354838709677, delta 8.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=94
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 412 (canonical 124)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=159 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 4412/4692 (rank_frac 0.9403239556692242) | score 8.5 (top 39.5, ratio 0.21518987341772153, delta 31.0) | section Midday, Set Set1, Draw Draw4, Col 3, hot 0, vt_straight 2.0 | why straight|cov1|hidden3v|vtrac_straight
- Compound (patterns_compound.csv): rank 1397/1662 (rank_frac 0.8405535499398316) | score 9.5 (top 74.0, ratio 0.12837837837837837, delta 64.5) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1|vstrx1
- Families (patterns_families.csv): count 37 | rank 242/1431 (rank_frac 0.16911250873515024) | score 20.5 (top 31.0, ratio 0.6612903225806451, delta 10.5) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=51

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 566 | section Combined | score 71.5 | col1_hits 5 | hot2 7
- rank   17 | canon 579 | section Evening | score 47.5 | col1_hits 3 | hot2 6
- rank   22 | canon 369 | section Evening | score 43.5 | col1_hits 3 | hot2 6
- rank    8 | canon 569 | section Combined | score 54.5 | col1_hits 3 | hot2 6
- rank    7 | canon 5669 | section Combined | score 55.5 | col1_hits 3 | hot2 6
- rank    4 | canon 669 | section Combined | score 70.0 | col1_hits 3 | hot2 6
- rank    1 | canon 667 | section Combined | score 74.0 | col1_hits 1 | hot2 6
- rank   66 | canon 367 | section Evening | score 32.0 | col1_hits 2 | hot2 5
- rank   28 | canon 5667 | section Combined | score 41.5 | col1_hits 1 | hot2 5
- rank   36 | canon 566 | section Evening | score 39.5 | col1_hits 3 | hot2 4

## Top families (patterns_families.csv)
- rank 1382 | family 30 | score 6.0 | hot2 0 | section Midday
- rank  915 | family 24 | score 12.5 | hot2 0 | section Midday
- rank 1246 | family 33 | score 9.0 | hot2 0 | section Midday
- rank   74 | family 21 | score 24.5 | hot2 0 | section Midday
- rank  131 | family 23 | score 23.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 586 (canon 568): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 412 (canon 124): exact_boxed=True exact_straight=True | rank 4412/4692 (rank_frac 0.940)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260107)

## Midday winner 586 (canonical 568)
- Stamp (winner_stamp.json): items_total=142 | exact_any=0 exact_final=0 | vtrac_any=142 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=19 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=142 | exact_any=0 vtrac_any=142 | drop_exact_any=0 drop_vtrac_any=19 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=13 vt_straight=0
- Hits (winner_hits.csv): rows=142 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=13 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 412 (canonical 124)
- Stamp (winner_stamp.json): items_total=48 | exact_any=0 exact_final=0 | vtrac_any=48 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=48 | exact_any=0 vtrac_any=48 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=48 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 586 (canonical 568)
- Stamp (winner_stamp.json): items_total=303 | exact_any=1 exact_final=0 | vtrac_any=252 vtrac_final=0 | drop_exact_any=7 drop_exact_final=0 | drop_vtrac_any=106 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=23 family_vtrac_final=0
- Flags (winner_flags.csv): rows=303 | exact_any=1 vtrac_any=252 | drop_exact_any=7 drop_vtrac_any=106 | family_exact_any=1 family_vtrac_any=23 | vt_boxed=86 vt_straight=0
- Hits (winner_hits.csv): rows=303 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=86 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.227143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 2 | pattern 566 | score_v2 14.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 14.037143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 5 | pattern 559 | score_v2 14.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 13.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 5 | pattern 559 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 13.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 566 | score_v2 14.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 14.037143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 566 | score_v2 11.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 599 | score_v2 11.787143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 11.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 224 | score_v2 10.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 522 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 592 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 559 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 586 (canon 568): items_total=142 exact_any=0 vtrac_any=142 | top winner_present=False best_rank=None/36; Evening 412 (canon 124): items_total=48 exact_any=0 vtrac_any=48 | top winner_present=False best_rank=None/24; Combined 586 (canon 568): items_total=303 exact_any=1 vtrac_any=252 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 566, 559, 559, 566, 599.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260107_052529)

## Top indices (from enhanced JSON)
- index 17 | score 68.95305249999998 | features: presence=42.335552499999984, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 62.2978925 | features: presence=38.350392500000005, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 38.9275325 | features: presence=18.160032500000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 6 | score 37.592205 | features: presence=25.044705000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 7 | score 30.348022500000003 | features: presence=16.600522500000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 25.6349675 | features: presence=16.5174675, cross_section=0.5, set_echo=0.3, first_hit=0.2
- index 10 | score 24.592100000000006 | features: presence=14.164600000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 20.033732500000003 | features: presence=10.576232500000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 19 | score 19.016772500000002 | features: presence=8.239272500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 25 | score 14.492025000000005 | features: presence=6.1445250000000025, cross_section=0.5, set_echo=0.3, first_hit=0.2

## Top straights (from enhanced JSON)
267, 217, 712, 762, 167, 617, 671, 967, 216, 796

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 412 | index 22 | file SouthCarolina4_vtrac22_winner_412_20260107_052321.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 586 | index 8 | file SouthCarolina4_vtrac8_winner_586_20260107_052319.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 412 | index 22 rank 3/35 (rank_frac 0.08571428571428572) | score 38.9275325 (top 68.95305249999998, ratio 0.5645512575385986, delta 30.025519999999986) | winner_in_index_straights=False | top_index_straights: 967 (10.352), 796 (9.413), 246 (9.062)
- winner 586 | index 8 rank 21/35 (rank_frac 0.6) | score 0.0 (top 68.95305249999998, ratio 0.0, delta 68.95305249999998) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 412→idx22 rank 3/35 (frac 0.086); 586→idx8 rank 21/35 (frac 0.600).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 17, 20, 22, 6, 7.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-06)

## Midday winner 586 (canonical 568)
- Top lanes (hot_zones_top_lanes.csv): present | rank 64/210 (rank_frac 0.3047619047619048) | score_mean 17.413 (top 20.416, ratio 0.8529094827586207, delta 3.003)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 412 (canonical 124)
- Top lanes (hot_zones_top_lanes.csv): present | rank 174/210 (rank_frac 0.8285714285714286) | score_mean 15.132 (top 20.416, ratio 0.7411833855799372, delta 5.284000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 015 | vt_triad 112 | score_mean 20.416 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 127 | vt_triad 233 | score_mean 19.953 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 038 | vt_triad 144 | score_mean 19.907 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 237 | vt_triad 334 | score_mean 19.78 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_only_lane,vt_straight
- rank    5 | triad 005 | vt_triad 11 | score_mean 19.688 | tags col1,hot12,hot16,hot20,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4
- rank    6 | triad 234 | vt_triad 345 | score_mean 19.683 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 003 | vt_triad 14 | score_mean 19.472 | tags col1,funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 388 | vt_triad 44 | score_mean 19.25 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_only_lane,vt_straight
- rank    9 | triad 278 | vt_triad 334 | score_mean 19.24 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,vertical1,vertical2,vt_only_lane,vt_straight
- rank   10 | triad 117 | vt_triad 23 | score_mean 19.165 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 586 (canon 568): rank 64/210 (rank_frac 0.305) ratio_to_top=0.8529094827586207; Evening 412 (canon 124): rank 174/210 (rank_frac 0.829) ratio_to_top=0.7411833855799372
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

Aux draws snapshot dir: `sharepacks/2026-01-06/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-06

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-06/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-05.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-06/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=712, 171, 432, 051, 189
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-06/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=171, 189, 308, 910, 653
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-06/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=712, 432, 051, 084, 821

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=2 last_repeat_gap=22 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=22), P2:9 (gap=24), P3:7 (gap=16)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 595: score=37.68044428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 696: score=37.35633571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 697: score=37.04419285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 695: score=37.00035714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 297: score=36.209621428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=36.16578571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.765928571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 698: score=31.6045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 298: score=30.769928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=30.633329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=977 sev=B
- 449: ds=906 sev=B
- 156: ds=889 sev=B
- 778: ds=859 sev=B
- 279: ds=858 sev=B
- 033: ds=790 sev=B
- 004: ds=778 sev=B
- 688: ds=745 sev=B
- 278: ds=712 sev=B
- 377: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=186 sev=red
  - 55: ds=123 sev=red
  - 77: ds=107 sev=red
  - 33: ds=94 sev=blue
  - 88: ds=89 sev=blue
  - 22: ds=69 sev=purple
  - 66: ds=57 sev=purple
  - 00: ds=30 sev=purple
  - 44: ds=9 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 78: ds=58 sev=red
  - 68: ds=46 sev=blue
  - 29: ds=39 sev=blue
  - 06: ds=32 sev=purple
  - 16: ds=32 sev=purple
  - 59: ds=28 sev=purple
  - 13: ds=24 sev=-
  - 39: ds=24 sev=-
  - 58: ds=22 sev=-
  - 07: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:450, 35:393, 1:174, 26:162, 31:124, 4:115, 23:113, 28:107, 27:90, 19:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=450 fs=0 fl=0 hz=0.002197802197802198, 35:ds=393 fs=0 fl=0 hz=0.001949317738791423, 1:ds=174 fs=6 fl=4 hz=0.012195121951219513, 26:ds=162 fs=2 fl=0 hz=0.0062402496099844, 31:ds=124 fs=27 fl=0 hz=0.03085714285714286, 4:ds=115 fs=21 fl=2 hz=0.026589595375722544, 23:ds=113 fs=25 fl=1 hz=0.029850746268656716, 28:ds=107 fs=16 fl=2 hz=0.021479713603818614, 27:ds=90 fs=26 fl=0 hz=0.02911534154535274, 19:ds=74 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=99 flags=red+purple
- S0: ds=72 flags=blue+purple
- S23: ds=61 flags=purple
- S5: ds=60 flags=purple
- S24: ds=58 flags=blue+purple
- S4: ds=50 flags=purple
- S3: ds=49 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=6 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=16), P2:3 (gap=42), P3:6 (gap=20)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 595: score=37.68044428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 696: score=37.35633571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 697: score=37.04419285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 695: score=37.00035714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 297: score=36.209621428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=36.16578571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.765928571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 698: score=31.6045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 298: score=30.769928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=30.633329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=880 sev=B
- 555: ds=875 sev=B
- 222: ds=852 sev=B
- 337: ds=829 sev=B
- 003: ds=820 sev=B
- 228: ds=811 sev=B
- 556: ds=713 sev=B
- 449: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=115 sev=red
  - 55: ds=79 sev=blue
  - 77: ds=48 sev=purple
  - 33: ds=42 sev=purple
  - 88: ds=40 sev=purple
  - 22: ds=38 sev=purple
  - 66: ds=25 sev=purple
  - 00: ds=16 sev=-
  - 44: ds=8 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 49: ds=56 sev=red
  - 67: ds=50 sev=blue
  - 34: ds=49 sev=blue
  - 27: ds=43 sev=blue
  - 07: ds=34 sev=purple
  - 05: ds=31 sev=purple
  - 15: ds=29 sev=purple
  - 78: ds=28 sev=purple
  - 69: ds=27 sev=purple
  - 16: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:416, 26:194, 35:180, 27:145, 6:113, 5:82, 1:79, 15:74, 34:60, 31:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=416 fs=1 fl=2 hz=0.006993006993006993, 26:ds=194 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=180 fs=1 fl=1 hz=0.004968944099378882, 27:ds=145 fs=18 fl=3 hz=0.026582278481012658, 6:ds=113 fs=24 fl=2 hz=0.02957906712172924, 5:ds=82 fs=20 fl=1 hz=0.023102310231023104, 1:ds=79 fs=7 fl=3 hz=0.012127894156560088, 15:ds=74 fs=17 fl=3 hz=0.021691973969631236, 34:ds=60 fs=28 fl=1 hz=0.03159041394335512, 31:ds=56 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=83 flags=purple
- S25: ds=80 flags=purple
- S21: ds=60 flags=purple
- S20: ds=56 flags=purple
- S17: ds=54 flags=purple
- S8: ds=52 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 134: score=4 tags=FLT,PAT,RS
  - 026: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 012: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 017: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=34 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=20), P2:9 (gap=16), P3:8 (gap=23)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 595: score=37.68044428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 696: score=37.35633571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 697: score=37.04419285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 695: score=37.00035714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 297: score=36.209621428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=36.16578571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.765928571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 698: score=31.6045 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 298: score=30.769928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=30.633329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=984 sev=B
- 117: ds=895 sev=B
- 005: ds=881 sev=B
- 577: ds=858 sev=B
- 155: ds=838 sev=B
- 777: ds=837 sev=B
- 669: ds=829 sev=B
- 179: ds=811 sev=B
- 366: ds=777 sev=B
- 222: ds=771 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=101 sev=blue
  - 77: ds=88 sev=blue
  - 66: ds=80 sev=blue
  - 33: ds=76 sev=blue
  - 55: ds=67 sev=purple
  - 88: ds=61 sev=purple
  - 22: ds=38 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=17 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 58: ds=102 sev=red
  - 35: ds=69 sev=red
  - 29: ds=64 sev=red
  - 47: ds=54 sev=blue
  - 19: ds=36 sev=purple
  - 78: ds=32 sev=purple
  - 68: ds=29 sev=purple
  - 38: ds=23 sev=-
  - 13: ds=21 sev=-
  - 09: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:489, 1:276, 32:243, 31:222, 4:142, 28:115, 19:111, 23:106, 26:88, 16:84

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=489 fs=3 fl=1 hz=0.017391304347826087, 1:ds=276 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=243 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=222 fs=16 fl=1 hz=0.021935483870967745, 4:ds=142 fs=21 fl=3 hz=0.028742514970059883, 28:ds=115 fs=10 fl=4 hz=0.017676767676767676, 19:ds=111 fs=12 fl=2 hz=0.016968325791855206, 23:ds=106 fs=24 fl=0 hz=0.02937576499388005, 26:ds=88 fs=0 fl=0 hz=0.002347417840375587, 16:ds=84 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=67 flags=purple
- S15: ds=58 flags=red+purple
- S17: ds=54 flags=purple
- S23: ds=51 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:771(B); midday:852(B)
- 366 -> combined:977(B); evening:777(B)
- 449 -> combined:906(B); midday:671(B)
- 688 -> combined:745(B); evening:736(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 16 -> combined:32(purple); midday:25(purple)
- 22 -> combined:69(purple); evening:38(purple); midday:38(purple)
- 29 -> combined:39(blue); evening:64(red)
- 33 -> combined:94(blue); evening:76(blue); midday:42(purple)
- 55 -> combined:123(red); evening:67(purple); midday:79(blue)
- 66 -> combined:57(purple); evening:80(blue); midday:25(purple)
- 68 -> combined:46(blue); evening:29(purple)
- 77 -> combined:107(red); evening:88(blue); midday:48(purple)
- 78 -> combined:58(red); evening:32(purple); midday:28(purple)
- 88 -> combined:89(blue); evening:61(purple); midday:40(purple)
- 99 -> combined:186(red); evening:101(blue); midday:115(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(3.1654999999999998)[R2,XVAR-Cons(CM)], 6(3.0000714285714287)[R3,XVAR-Cons(CE)], 5(2.8495285714285714)[R1,XVAR-Cons(CE)], 1(1.2967285714285715)[R2,Mirror-Echo], 0(1.1777142857142857)[R1,Double-Pressure]
- P2: 9(7.247714285714286)[R1,Mirror-Echo], 6(2.4800500000000003)[R2,XVAR-Cons(CE)], 4(1.9726285714285714)[R3,Mirror-Echo], 3(1.7149999999999999)[R1,Double-Pressure], 0(0.9508)[R2,Double-Pressure]
- P3: 7(3.296407142857143)[R1,XVAR-Cons(CM)], 5(3.2525714285714287)[R2,XVAR-Cons(CE)], 6(2.8527142857142858)[R3,XVAR-Cons(CM)], 8(1.3567142857142855)[R1,Double-Pressure], 0(0.27685714285714286)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-05.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=22), P2:9(gap=24), P3:7(gap=16); top cartesian candidates: 595, 696, 697, 695, 297.
- Q3: Blackapple: score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 016, 056, 126, 136, 146.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:852(B),evening:771(B); 366→combined:977(B),evening:777(B); 449→combined:906(B),midday:671(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:450, 35:393, 1:174, 26:162, 31:124.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=586 Evening=412; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 568 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 124 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 586 (canon 568): box `568` covers winner `586` (boxed hit).
  - Evening winner 412 (canon 124): box `124` covers winner `412` (boxed hit).
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
