# Master Validation Run Report — Pennsylvania4 — results 2026-01-02 (history workbook ~ 2026-01-01)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-02/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-02/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-02/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-02/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-02/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-02/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-02/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_871_20260105_070920.html`
- `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20260105_070922.html`

Winners JSON files:
- `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac21_winner_871_20260105_070920.json`
- `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20260105_070922.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-02/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 871 (canon 178): exact_boxed=True exact_straight=True | rank 2208/4466 (rank_frac 0.494); Evening 360 (canon 036): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 871 idx21 (rank 29/35, frac 0.829), 360 idx8 (rank 22/35, frac 0.629)
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

### 2.Stable — Pennsylvania4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-02)

## Midday winner 871 (canonical 178)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=294 | exact_boxed=17 | exact_straight=15 | vt_boxed=17
- Scores (patterns_scores.csv): rank 2208/4466 (rank_frac 0.49440214957456335) | score 13.0 (top 37.0, ratio 0.35135135135135137, delta 24.0) | section Combined, Set Set1, Draw Draw6, Col 2, hot 0, vt_straight 2.0 | why straight|cov1|vtrac_straight|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 246/1208 (rank_frac 0.20364238410596028) | score 22.0 (top 86.0, ratio 0.2558139534883721, delta 64.0) | section Combined, col1_hits 1, hot2 0, set_chain 3, draw_chain 4 | why set_chain3|draw_chain4|col1x1|hot1x1|vstrx2
- Families (patterns_families.csv): count 44 | rank 148/1308 (rank_frac 0.11314984709480122) | score 22.0 (top 34.5, ratio 0.6376811594202898, delta 12.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=81

## Evening winner 360 (canonical 036)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=518 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 59 | rank 132/1308 (rank_frac 0.10091743119266056) | score 23.0 (top 34.5, ratio 0.6666666666666666, delta 11.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=42
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 0559 | section Combined | score 75.0 | col1_hits 7 | hot2 11
- rank    1 | canon 559 | section Combined | score 86.0 | col1_hits 7 | hot2 11
- rank    2 | canon 055 | section Combined | score 81.5 | col1_hits 7 | hot2 11
- rank   20 | canon 0557 | section Combined | score 50.5 | col1_hits 3 | hot2 7
- rank   16 | canon 079 | section Combined | score 52.0 | col1_hits 4 | hot2 7
- rank    5 | canon 579 | section Midday | score 63.5 | col1_hits 3 | hot2 7
- rank   14 | canon 057 | section Combined | score 53.5 | col1_hits 3 | hot2 7
- rank    9 | canon 05579 | section Combined | score 57.0 | col1_hits 3 | hot2 7
- rank   16 | canon 0599 | section Combined | score 52.0 | col1_hits 5 | hot2 6
- rank    6 | canon 359 | section Midday | score 58.5 | col1_hits 0 | hot2 6

## Top families (patterns_families.csv)
- rank 1282 | family 6 | score 5.0 | hot2 0 | section Midday
- rank  148 | family 23 | score 22.0 | hot2 0 | section Midday
- rank  600 | family 27 | score 15.0 | hot2 0 | section Midday
- rank  687 | family 12 | score 14.0 | hot2 0 | section Midday
- rank  687 | family 21 | score 14.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 871 (canon 178): exact_boxed=True exact_straight=True | rank 2208/4466 (rank_frac 0.494); Evening 360 (canon 036): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260102)

## Midday winner 871 (canonical 178)
- Stamp (winner_stamp.json): items_total=158 | exact_any=2 exact_final=0 | vtrac_any=158 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=158 | exact_any=2 vtrac_any=158 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=158 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 2 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 360 (canonical 036)
- Stamp (winner_stamp.json): items_total=126 | exact_any=0 exact_final=0 | vtrac_any=82 vtrac_final=0 | drop_exact_any=4 drop_exact_final=0 | drop_vtrac_any=69 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=19 family_vtrac_final=0
- Flags (winner_flags.csv): rows=126 | exact_any=0 vtrac_any=82 | drop_exact_any=4 drop_vtrac_any=69 | family_exact_any=0 family_vtrac_any=19 | vt_boxed=23 vt_straight=0
- Hits (winner_hits.csv): rows=126 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=23 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=30 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.777143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 871 (canonical 178)
- Stamp (winner_stamp.json): items_total=390 | exact_any=4 exact_final=0 | vtrac_any=390 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=390 | exact_any=4 vtrac_any=390 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=390 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=23.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 23.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 21.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 21.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 21.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 559 | score_v2 21.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 559 | score_v2 21.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 21.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 21.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 21.627143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 21.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 23.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 21.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 15.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 14.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 594 | score_v2 13.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 597 | score_v2 13.30131 | tags exact,vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 599 | score_v2 13.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 559 | score_v2 12.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 559 | score_v2 12.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 994 | score_v2 12.610476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 871 (canon 178): items_total=158 exact_any=2 vtrac_any=158 | top winner_present=False best_rank=None/16; Evening 360 (canon 036): items_total=126 exact_any=0 vtrac_any=82 | top winner_present=False best_rank=None/30; Combined 871 (canon 178): items_total=390 exact_any=4 vtrac_any=390 | top winner_present=False best_rank=None/18
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 559, 594.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_071331)

## Top indices (from enhanced JSON)
- index 12 | score 63.556784999999984 | features: presence=45.39928499999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 58.378049999999995 | features: presence=45.800549999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 37.59986000000001 | features: presence=22.06236000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 29 | score 33.0772 | features: presence=17.5697, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 11 | score 31.882825 | features: presence=18.145325, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 31.383149999999997 | features: presence=13.845649999999997, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 30 | score 29.84598 | features: presence=17.048479999999998, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 23.8872 | features: presence=13.4497, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 3 | score 13.730099999999998 | features: presence=8.792599999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 13.219355 | features: presence=5.571855, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
907, 590, 593, 597, 759, 709, 795, 937, 097, 095

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 871 | index 21 | file Pennsylvania4_vtrac21_winner_871_20260105_070920.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 360 | index 8 | file Pennsylvania4_vtrac8_winner_360_20260105_070922.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 871 | index 21 rank 29/35 (rank_frac 0.8285714285714286) | score 0.0 (top 63.556784999999984, ratio 0.0, delta 63.556784999999984) | winner_in_index_straights=False | top_index_straights: (none)
- winner 360 | index 8 rank 22/35 (rank_frac 0.6285714285714286) | score 0.0 (top 63.556784999999984, ratio 0.0, delta 63.556784999999984) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 871→idx21 rank 29/35 (frac 0.829); 360→idx8 rank 22/35 (frac 0.629).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 12, 5, 14, 29, 11.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-02

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-02)

## Midday winner 871 (canonical 178)
- Top lanes (hot_zones_top_lanes.csv): present | rank 44/207 (rank_frac 0.21256038647342995) | score_mean 18.14 (top 23.35, ratio 0.7768736616702355, delta 5.210000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 360 (canonical 036)
- Top lanes (hot_zones_top_lanes.csv): present | rank 63/207 (rank_frac 0.30434782608695654) | score_mean 17.575 (top 23.35, ratio 0.7526766595289078, delta 5.775000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 23.35 | tags hot16,literal_draw,straight_lane,vertical1,vt_straight
- rank    2 | triad 559 | vt_triad 15 | score_mean 20.527 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 011 | vt_triad 12 | score_mean 20.394 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 168 | vt_triad 224 | score_mean 20.207 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 122 | vt_triad 23 | score_mean 19.823 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    6 | triad 117 | vt_triad 23 | score_mean 19.754 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    7 | triad 118 | vt_triad 24 | score_mean 19.653 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    8 | triad 055 | vt_triad 11 | score_mean 19.521 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 113 | vt_triad 24 | score_mean 19.473 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_straight
- rank   10 | triad 137 | vt_triad 234 | score_mean 19.377 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 871 (canon 178): rank 44/207 (rank_frac 0.213) ratio_to_top=0.7768736616702355; Evening 360 (canon 036): rank 63/207 (rank_frac 0.304) ratio_to_top=0.7526766595289078
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

Aux draws snapshot dir: `sharepacks/2026-01-02/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=328, 322, 221, 684, 173
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=322, 684, 186, 239, 502
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=328, 221, 173, 460, 422

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=23 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:4 (gap=28), P3:7 (gap=15)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=996 sev=B
- 666: ds=994 sev=B
- 159: ds=882 sev=B
- 007: ds=879 sev=B
- 088: ds=843 sev=B
- 008: ds=821 sev=B
- 444: ds=797 sev=B
- 039: ds=772 sev=B
- 355: ds=762 sev=B
- 344: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=139 sev=red
  - 77: ds=78 sev=blue
  - 88: ds=77 sev=blue
  - 44: ds=71 sev=blue
  - 66: ds=65 sev=purple
  - 55: ds=42 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=25 sev=purple
  - 99: ds=12 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 78: ds=72 sev=red
  - 03: ds=47 sev=blue
  - 07: ds=45 sev=blue
  - 35: ds=38 sev=blue
  - 69: ds=36 sev=purple
  - 36: ds=33 sev=purple
  - 09: ds=32 sev=purple
  - 34: ds=31 sev=purple
  - 19: ds=29 sev=purple
  - 47: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:281, 26:238, 16:96, 7:64, 6:59, 13:57, 19:53, 10:48, 31:44, 1:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=281 fs=2 fl=1 hz=0.007380073800738007, 26:ds=238 fs=0 fl=1 hz=0.003898635477582846, 16:ds=96 fs=3 fl=2 hz=0.007371007371007371, 7:ds=64 fs=36 fl=1 hz=0.03965702036441586, 6:ds=59 fs=22 fl=1 hz=0.02454642475987193, 13:ds=57 fs=21 fl=1 hz=0.024553571428571428, 19:ds=53 fs=21 fl=3 hz=0.025695931477516063, 10:ds=48 fs=23 fl=2 hz=0.02676659528907923, 31:ds=44 fs=22 fl=2 hz=0.02531645569620253, 1:ds=42 fs=1 fl=2 hz=0.0044742729306487695

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=90 flags=purple
- S20: ds=77 flags=purple
- S6: ds=56 flags=purple
- S25: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5', '9'], 'pairs': {'remaining_count': 0}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=33 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=27), P2:7 (gap=22), P3:5 (gap=27)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=977 sev=B
- 288: ds=964 sev=B
- 255: ds=935 sev=B
- 668: ds=917 sev=B
- 199: ds=865 sev=B
- 499: ds=791 sev=B
- 399: ds=774 sev=B
- 039: ds=762 sev=B
- 448: ds=751 sev=B
- 005: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=186 sev=red
  - 99: ds=133 sev=red
  - 77: ds=76 sev=blue
  - 33: ds=69 sev=purple
  - 88: ds=38 sev=purple
  - 44: ds=35 sev=purple
  - 66: ds=32 sev=purple
  - 11: ds=13 sev=-
  - 00: ds=12 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 59: ds=79 sev=red
  - 79: ds=73 sev=red
  - 12: ds=48 sev=blue
  - 78: ds=46 sev=blue
  - 06: ds=43 sev=blue
  - 35: ds=40 sev=blue
  - 56: ds=32 sev=purple
  - 69: ds=30 sev=purple
  - 13: ds=25 sev=purple
  - 57: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:375, 1:360, 34:214, 16:172, 15:163, 32:140, 35:117, 28:62, 5:47, 2:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=375 fs=0 fl=0 hz=0.0, 1:ds=360 fs=2 fl=2 hz=0.009124087591240877, 34:ds=214 fs=19 fl=1 hz=0.02631578947368421, 16:ds=172 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=163 fs=23 fl=0 hz=0.029411764705882353, 32:ds=140 fs=3 fl=1 hz=0.006720430107526881, 35:ds=117 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=62 fs=26 fl=2 hz=0.02997858672376874, 5:ds=47 fs=18 fl=2 hz=0.022175290390707498, 2:ds=43 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=94 flags=red+purple
- S22: ds=79 flags=purple
- S23: ds=67 flags=purple
- S3: ds=61 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 567: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 579: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 679: score=2 tags=FLT,PAT
  - 789: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 017: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=63 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=29), P2:1 (gap=35), P3:6 (gap=19)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=973 sev=B
- 009: ds=931 sev=B
- 255: ds=889 sev=B
- 138: ds=829 sev=B
- 117: ds=812 sev=B
- 158: ds=774 sev=B
- 344: ds=767 sev=B
- 199: ds=758 sev=B
- 112: ds=718 sev=B
- 277: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=128 sev=red
  - 33: ds=70 sev=purple
  - 44: ds=41 sev=purple
  - 77: ds=39 sev=purple
  - 66: ds=37 sev=purple
  - 11: ds=28 sev=purple
  - 55: ds=21 sev=-
  - 00: ds=15 sev=-
  - 99: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 68: ds=86 sev=red
  - 07: ds=63 sev=red
  - 15: ds=51 sev=blue
  - 03: ds=45 sev=blue
  - 78: ds=36 sev=purple
  - 19: ds=35 sev=purple
  - 01: ds=29 sev=purple
  - 18: ds=29 sev=purple
  - 14: ds=28 sev=purple
  - 39: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:617, 23:156, 26:119, 18:116, 13:65, 33:50, 16:48, 30:47, 24:44, 27:36

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=617 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=156 fs=17 fl=2 hz=0.025165562913907286, 26:ds=119 fs=2 fl=1 hz=0.0056657223796034, 18:ds=116 fs=23 fl=2 hz=0.02910360884749709, 13:ds=65 fs=20 fl=1 hz=0.024881516587677725, 33:ds=50 fs=19 fl=3 hz=0.023255813953488372, 16:ds=48 fs=5 fl=3 hz=0.009523809523809525, 30:ds=47 fs=35 fl=1 hz=0.03829787234042553, 24:ds=44 fs=37 fl=0 hz=0.04048140043763676, 27:ds=36 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=89 flags=blue+purple
- S1: ds=74 flags=blue+purple
- S24: ds=57 flags=blue+purple
- S3: ds=45 flags=purple
- S20: ds=39 flags=purple
- S6: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:772(B); midday:762(B)
- 066 -> combined:996(B); midday:740(B)
- 199 -> evening:758(B); midday:865(B)
- 255 -> evening:889(B); midday:935(B)
- 344 -> combined:691(B); evening:767(B)
- 444 -> combined:797(B); evening:973(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:47(blue); evening:45(blue)
- 07 -> combined:45(blue); evening:63(red)
- 11 -> combined:27(purple); evening:28(purple)
- 19 -> combined:29(purple); evening:35(purple)
- 33 -> combined:139(red); evening:70(purple); midday:69(purple)
- 35 -> combined:38(blue); midday:40(blue)
- 44 -> combined:71(blue); evening:41(purple); midday:35(purple)
- 55 -> combined:42(purple); midday:186(red)
- 66 -> combined:65(purple); evening:37(purple); midday:32(purple)
- 69 -> combined:36(purple); midday:30(purple)
- 77 -> combined:78(blue); evening:39(purple); midday:76(blue)
- 78 -> combined:72(red); evening:36(purple); midday:46(blue)
- 88 -> combined:77(blue); evening:128(red); midday:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.549842857142857)[R2,XVAR-Cons(CEM)], 8(7.2816785714285714)[R1,XVAR-Cons(CEM)], 4(1.1598)[R2,Double-Pressure], 9(0.23971428571428574)[R3,Swap], 6(0.20435714285714285)[R3,Swap]
- P2: 5(5.611328571428572)[R2,XVAR-Cons(CEM)], 4(3.9053)[R1,XVAR-Cons(CM)], 1(3.328857142857143)[R3,XVAR-Cons(CE)], 7(1.3568571428571428)[R1,Double-Pressure], 3(1.0971)[R2,Double-Pressure]
- P3: 5(3.7261428571428574)[R2,XVAR-Cons(CM)], 7(2.678914285714286)[R1,XVAR-Cons(CE)], 9(2.4734)[R3,XVAR-Cons(CE)], 1(1.2433999999999998)[R2,Double-Pressure], 6(1.2372857142857143)[R1,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-01.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:8(gap=31), P2:4(gap=28), P3:7(gap=15); top cartesian candidates: 755, 757, 855, 759, 857.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 015, 016, 025, 027, 035.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:772(B),midday:762(B); 066→combined:996(B),midday:740(B); 199→midday:865(B),evening:758(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:281, 26:238, 16:96, 7:64, 6:59.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=871 Evening=360; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 178 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 036 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 871 (canon 178): box `178` covers winner `871` (boxed hit).
  - Evening winner 360 (canon 036): box `036` covers winner `360` (boxed hit).
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
