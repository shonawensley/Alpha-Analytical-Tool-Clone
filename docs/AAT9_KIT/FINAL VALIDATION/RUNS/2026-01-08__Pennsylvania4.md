# Master Validation Run Report — Pennsylvania4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-08/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-08/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-08/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-08/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-08/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-08/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac12_winner_574_20260110_034442.html`
- `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac3_winner_750_20260110_034441.html`

Winners JSON files:
- `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac12_winner_574_20260110_034442.json`
- `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac3_winner_750_20260110_034441.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 750 (canon 057): exact_boxed=True exact_straight=True | rank 2382/5324 (rank_frac 0.447); Evening 574 (canon 457): exact_boxed=True exact_straight=False | rank 2181/5324 (rank_frac 0.410)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 574 idx12 (rank 9/35, frac 0.257), 750 idx3 (rank 14/35, frac 0.400)
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

### 2.Stable — Pennsylvania4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-08)

## Midday winner 750 (canonical 057)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=110 | exact_boxed=12 | exact_straight=12 | vt_boxed=12
- Scores (patterns_scores.csv): rank 2382/5324 (rank_frac 0.44740796393688953) | score 13.0 (top 46.5, ratio 0.27956989247311825, delta 33.5) | section Evening, Set Set3, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why straight|cov1|hp_repeat3|mirror|set_chain3
- Compound (patterns_compound.csv): rank 507/1859 (rank_frac 0.2727272727272727) | score 18.0 (top 91.0, ratio 0.1978021978021978, delta 73.0) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2
- Families (patterns_families.csv): count 46 | rank 160/1411 (rank_frac 0.11339475549255847) | score 23.0 (top 38.5, ratio 0.5974025974025974, delta 15.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=17

## Evening winner 574 (canonical 457)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=303 | exact_boxed=2 | exact_straight=0 | vt_boxed=2
- Scores (patterns_scores.csv): rank 2181/5324 (rank_frac 0.40965439519158525) | score 13.5 (top 46.5, ratio 0.2903225806451613, delta 33.0) | section Evening, Set Set2, Draw Draw1, Col 3, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat2|vstr2|hot1|perm2|hidden3v
- Compound (patterns_compound.csv): rank 704/1859 (rank_frac 0.378698224852071) | score 15.5 (top 91.0, ratio 0.17032967032967034, delta 75.5) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 0 | why hot1x2
- Families (patterns_families.csv): count 61 | rank 193/1411 (rank_frac 0.13678242381289865) | score 22.5 (top 38.5, ratio 0.5844155844155844, delta 16.0) | section Evening, hot2 3
- Metrics (metrics.json): exact_boxed=True | exact_straight=False | vt_boxed_count=91

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 445 | section Evening | score 89.5 | col1_hits 7 | hot2 11
- rank    1 | canon 112 | section Combined | score 91.0 | col1_hits 6 | hot2 9
- rank    2 | canon 113 | section Combined | score 90.0 | col1_hits 6 | hot2 9
- rank    7 | canon 144 | section Evening | score 70.0 | col1_hits 6 | hot2 8
- rank   13 | canon 1123 | section Combined | score 60.0 | col1_hits 3 | hot2 7
- rank    4 | canon 009 | section Midday | score 84.0 | col1_hits 1 | hot2 7
- rank   14 | canon 114 | section Evening | score 59.0 | col1_hits 5 | hot2 6
- rank   19 | canon 1144 | section Evening | score 51.5 | col1_hits 5 | hot2 6
- rank    6 | canon 223 | section Combined | score 70.5 | col1_hits 1 | hot2 6
- rank   26 | canon 115 | section Evening | score 47.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1405 | family 35 | score 4.0 | hot2 0 | section Midday
- rank  802 | family 28 | score 14.0 | hot2 1 | section Midday
- rank 1197 | family 20 | score 9.5 | hot2 1 | section Midday
- rank 1219 | family 21 | score 9.0 | hot2 2 | section Midday
- rank  257 | family 2 | score 21.0 | hot2 1 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 750 (canon 057): exact_boxed=True exact_straight=True | rank 2382/5324 (rank_frac 0.447); Evening 574 (canon 457): exact_boxed=True exact_straight=False | rank 2181/5324 (rank_frac 0.410)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260110)

## Midday winner 750 (canonical 057)
- Stamp (winner_stamp.json): items_total=98 | exact_any=0 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=17 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=98 | exact_any=0 vtrac_any=84 | drop_exact_any=0 drop_vtrac_any=17 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=5 vt_straight=0
- Hits (winner_hits.csv): rows=98 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=5 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 574 (canonical 457)
- Stamp (winner_stamp.json): items_total=158 | exact_any=24 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=24 drop_exact_final=0 | drop_vtrac_any=150 drop_vtrac_final=0 | family_exact_any=32 family_exact_final=0 | family_vtrac_any=55 family_vtrac_final=0
- Flags (winner_flags.csv): rows=158 | exact_any=24 vtrac_any=120 | drop_exact_any=24 drop_vtrac_any=150 | family_exact_any=32 family_vtrac_any=55 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=158 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.727143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 750 (canonical 057)
- Stamp (winner_stamp.json): items_total=218 | exact_any=0 exact_final=0 | vtrac_any=170 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=137 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=86 family_vtrac_final=0
- Flags (winner_flags.csv): rows=218 | exact_any=0 vtrac_any=170 | drop_exact_any=0 drop_vtrac_any=137 | family_exact_any=0 family_vtrac_any=86 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=218 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.287143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 559 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 559 | score_v2 11.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 559 | score_v2 11.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 6 | pattern 559 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 5 | pattern 559 | score_v2 11.477143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 559 | score_v2 12.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 559 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 11.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 599 | score_v2 11.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 554 | score_v2 11.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 559 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 221 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 221 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 922 | score_v2 10.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 554 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 750 (canon 057): items_total=98 exact_any=0 vtrac_any=84 | top winner_present=False best_rank=None/18; Evening 574 (canon 457): items_total=158 exact_any=24 vtrac_any=120 | top winner_present=False best_rank=None/16; Combined 750 (canon 057): items_total=218 exact_any=0 vtrac_any=170 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 599, 554.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260110_034643)

## Top indices (from enhanced JSON)
- index 27 | score 57.66842750000001 | features: presence=36.950927500000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 17 | score 50.874329999999986 | features: presence=36.20682999999999, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 18 | score 41.454995000000004 | features: presence=30.177495, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 5 | score 37.08495 | features: presence=24.62745, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 20 | score 34.74173 | features: presence=23.21423, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 34.137432499999996 | features: presence=22.509932499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 22.3365225 | features: presence=10.3590225, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 15 | score 15.748558333333337 | features: presence=7.689600000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 12 | score 11.1333 | features: presence=3.3858, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 11 | score 10.413408333333333 | features: presence=3.9044499999999998, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
132, 732, 237, 287, 231, 137, 371, 173, 172, 187

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 574 | index 12 | file Pennsylvania4_vtrac12_winner_574_20260110_034442.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 750 | index 3 | file Pennsylvania4_vtrac3_winner_750_20260110_034441.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 574 | index 12 rank 9/35 (rank_frac 0.2571428571428571) | score 11.1333 (top 57.66842750000001, ratio 0.19305711084284374, delta 46.53512750000001) | winner_in_index_straights=False | top_index_straights: 709 (4.212), 907 (2.562), 920 (1.913)
- winner 750 | index 3 rank 14/35 (rank_frac 0.4) | score 7.034858333333333 (top 57.66842750000001, ratio 0.12198803813981805, delta 50.633569166666675) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 574→idx12 rank 9/35 (frac 0.257); 750→idx3 rank 14/35 (frac 0.400).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 27, 17, 18, 5, 20.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-08)

## Midday winner 750 (canonical 057)
- Top lanes (hot_zones_top_lanes.csv): present | rank 18/212 (rank_frac 0.08490566037735849) | score_mean 20.068 (top 23.349, ratio 0.8594800633860123, delta 3.280999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (note: map is a top-20 snapshot)

## Evening winner 574 (canonical 457)
- Top lanes (hot_zones_top_lanes.csv): present | rank 115/212 (rank_frac 0.5424528301886793) | score_mean 16.433 (top 23.349, ratio 0.7037988778962696, delta 6.916)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 006 | vt_triad 12 | score_mean 23.349 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    2 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    3 | triad 559 | vt_triad 15 | score_mean 21.932 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_straight
- rank    4 | triad 005 | vt_triad 11 | score_mean 21.007 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 055 | vt_triad 11 | score_mean 20.911 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 059 | vt_triad 115 | score_mean 20.898 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 004 | vt_triad 15 | score_mean 20.882 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 445 | vt_triad 15 | score_mean 20.8 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 456 | vt_triad 125 | score_mean 20.777 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 227 | vt_triad 33 | score_mean 20.662 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 750 (canon 057): rank 18/212 (rank_frac 0.085) ratio_to_top=0.8594800633860123; Evening 574 (canon 457): rank 115/212 (rank_frac 0.542) ratio_to_top=0.7037988778962696
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

Aux draws snapshot dir: `sharepacks/2026-01-08/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-08/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=263, 060, 757, 684, 600
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-08/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=060, 684, 546, 359, 744
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-08/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=263, 757, 600, 980, 909

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=7 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=18), P2:1 (gap=25), P3:5 (gap=22)
- consensus_notes: P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=46.31889607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 815: score=41.35659285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 515: score=40.04691571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 495: score=36.50207857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 418: score=35.91097857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 435: score=35.747435714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 818: score=35.45233214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 895: score=34.45093571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=33.82778285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=33.69913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 159: ds=894 sev=B
- 007: ds=891 sev=B
- 088: ds=855 sev=B
- 008: ds=833 sev=B
- 444: ds=809 sev=B
- 039: ds=784 sev=B
- 355: ds=774 sev=B
- 344: ds=703 sev=B
- 788: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=151 sev=red
  - 88: ds=89 sev=blue
  - 66: ds=77 sev=blue
  - 55: ds=54 sev=purple
  - 11: ds=39 sev=purple
  - 22: ds=13 sev=-
  - 44: ds=9 sev=-
  - 99: ds=8 sev=-
  - 77: ds=2 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 07: ds=57 sev=red
  - 69: ds=48 sev=blue
  - 34: ds=43 sev=blue
  - 19: ds=41 sev=blue
  - 15: ds=33 sev=purple
  - 79: ds=28 sev=purple
  - 27: ds=27 sev=purple
  - 67: ds=27 sev=purple
  - 58: ds=26 sev=purple
  - 01: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:293, 26:250, 16:108, 7:76, 6:71, 13:69, 19:65, 1:54, 11:51, 23:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=293 fs=2 fl=1 hz=0.007380073800738007, 26:ds=250 fs=0 fl=1 hz=0.003898635477582846, 16:ds=108 fs=3 fl=2 hz=0.007371007371007371, 7:ds=76 fs=35 fl=1 hz=0.04, 6:ds=71 fs=21 fl=1 hz=0.025611175785797437, 13:ds=69 fs=21 fl=1 hz=0.024553571428571428, 19:ds=65 fs=21 fl=3 hz=0.025695931477516063, 1:ds=54 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=51 fs=48 fl=0 hz=0.05128205128205128, 23:ds=45 fs=22 fl=1 hz=0.02415966386554622

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S20: ds=89 flags=purple
- S25: ds=66 flags=purple
- S4: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=39 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=28), P2:9 (gap=15), P3:5 (gap=33)
- consensus_notes: P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=46.31889607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 815: score=41.35659285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 515: score=40.04691571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 495: score=36.50207857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 418: score=35.91097857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 435: score=35.747435714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 818: score=35.45233214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 895: score=34.45093571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=33.82778285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=33.69913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=983 sev=B
- 288: ds=970 sev=B
- 255: ds=941 sev=B
- 668: ds=923 sev=B
- 199: ds=871 sev=B
- 499: ds=797 sev=B
- 399: ds=780 sev=B
- 039: ds=768 sev=B
- 448: ds=757 sev=B
- 005: ds=749 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=192 sev=red
  - 99: ds=139 sev=red
  - 77: ds=82 sev=blue
  - 33: ds=75 sev=blue
  - 88: ds=44 sev=purple
  - 66: ds=38 sev=purple
  - 11: ds=19 sev=-
  - 22: ds=6 sev=-
  - 44: ds=4 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 79: ds=79 sev=red
  - 12: ds=54 sev=blue
  - 69: ds=36 sev=purple
  - 13: ds=31 sev=purple
  - 57: ds=30 sev=purple
  - 03: ds=29 sev=purple
  - 07: ds=28 sev=purple
  - 09: ds=24 sev=-
  - 37: ds=23 sev=-
  - 36: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:381, 1:366, 34:220, 16:178, 15:169, 32:146, 35:123, 28:68, 5:53, 7:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=381 fs=0 fl=0 hz=0.0, 1:ds=366 fs=2 fl=2 hz=0.009124087591240877, 34:ds=220 fs=19 fl=1 hz=0.02631578947368421, 16:ds=178 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=169 fs=23 fl=0 hz=0.029411764705882353, 32:ds=146 fs=3 fl=1 hz=0.006720430107526881, 35:ds=123 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=68 fs=26 fl=1 hz=0.03515625, 5:ds=53 fs=17 fl=2 hz=0.021253985122210415, 7:ds=40 fs=40 fl=1 hz=0.04311251314405889

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S23: ds=73 flags=purple
- S3: ds=67 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 015: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=69 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=35), P2:1 (gap=41), P3:6 (gap=25)
- consensus_notes: P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=46.31889607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 815: score=41.35659285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 515: score=40.04691571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 495: score=36.50207857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 418: score=35.91097857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 435: score=35.747435714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 818: score=35.45233214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 895: score=34.45093571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 414: score=33.82778285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 413: score=33.69913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=979 sev=B
- 009: ds=937 sev=B
- 255: ds=895 sev=B
- 138: ds=835 sev=B
- 117: ds=818 sev=B
- 158: ds=780 sev=B
- 344: ds=773 sev=B
- 199: ds=764 sev=B
- 112: ds=724 sev=B
- 277: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=134 sev=red
  - 33: ds=76 sev=blue
  - 44: ds=47 sev=purple
  - 66: ds=43 sev=purple
  - 11: ds=34 sev=purple
  - 55: ds=27 sev=purple
  - 22: ds=7 sev=-
  - 99: ds=4 sev=-
  - 00: ds=2 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 68: ds=92 sev=red
  - 07: ds=69 sev=red
  - 15: ds=57 sev=red
  - 78: ds=42 sev=blue
  - 19: ds=41 sev=blue
  - 01: ds=35 sev=purple
  - 18: ds=35 sev=purple
  - 14: ds=34 sev=purple
  - 39: ds=32 sev=purple
  - 16: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:623, 23:162, 26:125, 18:122, 13:71, 33:56, 16:54, 30:53, 24:50, 27:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=623 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=162 fs=17 fl=2 hz=0.025165562913907286, 26:ds=125 fs=2 fl=1 hz=0.0056657223796034, 18:ds=122 fs=23 fl=2 hz=0.02910360884749709, 13:ds=71 fs=20 fl=1 hz=0.024881516587677725, 33:ds=56 fs=18 fl=3 hz=0.023076923076923075, 16:ds=54 fs=5 fl=3 hz=0.009523809523809525, 30:ds=53 fs=35 fl=1 hz=0.03829787234042553, 24:ds=50 fs=37 fl=0 hz=0.04048140043763676, 27:ds=42 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=95 flags=blue+purple
- S1: ds=80 flags=blue+purple
- S24: ds=63 flags=blue+purple
- S3: ds=51 flags=purple
- S20: ds=45 flags=purple
- S25: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:784(B); midday:768(B)
- 199 -> evening:764(B); midday:871(B)
- 255 -> evening:895(B); midday:941(B)
- 344 -> combined:703(B); evening:773(B)
- 444 -> combined:809(B); evening:979(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:25(purple); evening:35(purple)
- 07 -> combined:57(red); evening:69(red); midday:28(purple)
- 11 -> combined:39(purple); evening:34(purple)
- 14 -> combined:25(purple); evening:34(purple)
- 15 -> combined:33(purple); evening:57(red)
- 19 -> combined:41(blue); evening:41(blue)
- 33 -> combined:151(red); evening:76(blue); midday:75(blue)
- 34 -> combined:43(blue); evening:29(purple)
- 55 -> combined:54(purple); evening:27(purple); midday:192(red)
- 66 -> combined:77(blue); evening:43(purple); midday:38(purple)
- 69 -> combined:48(blue); midday:36(purple)
- 79 -> combined:28(purple); midday:79(red)
- 88 -> combined:89(blue); evening:134(red); midday:44(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(4.291714285714286)[R1,XVAR-Cons(CM)], 8(3.240571428571428)[R3,XVAR-Cons(CE)], 9(1.498)[R2,Mirror-Echo], 1(1.0519999999999998)[R2,Double-Pressure], 5(1.0088785714285713)[R2,Mirror-Echo]
- P2: 1(8.051514285714285)[R1,XVAR-Cons(CEM)], 9(3.6458571428571425)[R2,XVAR-Cons(CM)], 3(2.8912142857142857)[R3,XVAR-Cons(CE)], 4(0.3687142857142857)[R3,Swap], 0(0.23435714285714285)[R3,Swap]
- P3: 5(7.064507142857143)[R1,XVAR-Cons(CEM)], 8(2.06775)[R3,XVAR-Cons(CM)], 6(1.4164285714285714)[R1,Double-Pressure], 3(1.3559071428571428)[R2,Mirror-Echo], 4(0.9208)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:4(gap=18), P2:1(gap=25), P3:5(gap=22); top cartesian candidates: 415, 815, 515, 495, 418.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:784(B),midday:768(B); 199→midday:871(B),evening:764(B); 255→midday:941(B),evening:895(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:293, 26:250, 16:108, 7:76, 6:71.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=750 Evening=574; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 057 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 457 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 750 (canon 057): box `057` covers winner `750` (boxed hit).
  - Evening winner 574 (canon 457): box `457` covers winner `574` (boxed hit).
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
