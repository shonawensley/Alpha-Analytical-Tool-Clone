# Master Validation Run Report — PuertoRico4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/PuertoRico4/`
- Winners lens: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2026-01-08/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2026-01-08/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2026-01-08/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2026-01-08/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2026-01-08/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2026-01-08/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac11_winner_073_20260110_034444.html`
- `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_479_20260110_034446.html`

Winners JSON files:
- `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac11_winner_073_20260110_034444.json`
- `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac31_winner_479_20260110_034446.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/PuertoRico4/winners/PuertoRico4/digest.md`.
- Q2: Stable environment quick read: Midday 073 (canon 037): exact_boxed=True exact_straight=True | rank 964/2869 (rank_frac 0.336); Evening 479 (canon 479): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 073 idx11 (rank 21/35, frac 0.600), 479 idx31 (rank 33/35, frac 0.943)
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

### 2.Stable — PuertoRico4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2026-01-08)

## Midday winner 073 (canonical 037)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=240 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 964/2869 (rank_frac 0.3360055768560474) | score 12.0 (top 35.5, ratio 0.3380281690140845, delta 23.5) | section Midday, Set Set1, Draw Draw2, Col 4, hot 1, vt_straight 0.0 | why straight|cov2|vstr2|hot1|draw_chain2
- Compound (patterns_compound.csv): rank 252/1247 (rank_frac 0.2020850040096231) | score 15.5 (top 51.5, ratio 0.30097087378640774, delta 36.0) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|hot1x2|vstrx1
- Families (patterns_families.csv): count 42 | rank 146/857 (rank_frac 0.17036172695449242) | score 19.0 (top 30.0, ratio 0.6333333333333333, delta 11.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=109

## Evening winner 479 (canonical 479)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=13 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 11 | rank 80/857 (rank_frac 0.09334889148191365) | score 21.0 (top 30.0, ratio 0.7, delta 9.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=2
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank   11 | canon 028 | section Evening | score 34.5 | col1_hits 1 | hot2 3
- rank    3 | canon 068 | section Evening | score 47.0 | col1_hits 2 | hot2 2
- rank  131 | canon 026 | section Evening | score 18.5 | col1_hits 0 | hot2 2
- rank    2 | canon 066 | section Midday | score 50.5 | col1_hits 0 | hot2 1
- rank    4 | canon 268 | section Evening | score 40.0 | col1_hits 0 | hot2 1
- rank  157 | canon 0235 | section Midday | score 17.5 | col1_hits 0 | hot2 0
- rank  157 | canon 01135 | section Midday | score 17.5 | col1_hits 0 | hot2 0
- rank  157 | canon 01156 | section Midday | score 17.5 | col1_hits 0 | hot2 0
- rank  157 | canon 0115 | section Midday | score 17.5 | col1_hits 0 | hot2 0
- rank  157 | canon 1344 | section Midday | score 17.5 | col1_hits 0 | hot2 0

## Top families (patterns_families.csv)
- rank  822 | family 5 | score 5.0 | hot2 0 | section Midday
- rank  459 | family 17 | score 11.0 | hot2 0 | section Midday
- rank  734 | family 27 | score 7.0 | hot2 0 | section Midday
- rank  822 | family 16 | score 5.0 | hot2 0 | section Midday
- rank  843 | family 14 | score 4.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 073 (canon 037): exact_boxed=True exact_straight=True | rank 964/2869 (rank_frac 0.336); Evening 479 (canon 479): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — PuertoRico4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20260110)

## Midday winner 073 (canonical 037)
- Stamp (winner_stamp.json): items_total=90 | exact_any=0 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=11 drop_exact_final=0 | drop_vtrac_any=73 drop_vtrac_final=0 | family_exact_any=9 family_exact_final=0 | family_vtrac_any=52 family_vtrac_final=0
- Flags (winner_flags.csv): rows=90 | exact_any=0 vtrac_any=84 | drop_exact_any=11 drop_vtrac_any=73 | family_exact_any=9 family_vtrac_any=52 | vt_boxed=15 vt_straight=0
- Hits (winner_hits.csv): rows=90 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=15 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=34 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.077143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 479 (canonical 479)
- Stamp (winner_stamp.json): items_total=36 | exact_any=0 exact_final=0 | vtrac_any=36 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=24 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=36 | exact_any=0 vtrac_any=36 | drop_exact_any=0 drop_vtrac_any=24 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=36 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=28 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.097143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 073 (canonical 037)
- Stamp (winner_stamp.json): items_total=227 | exact_any=0 exact_final=0 | vtrac_any=174 vtrac_final=0 | drop_exact_any=11 drop_exact_final=0 | drop_vtrac_any=181 drop_vtrac_final=0 | family_exact_any=9 family_exact_final=0 | family_vtrac_any=99 family_vtrac_final=0
- Flags (winner_flags.csv): rows=227 | exact_any=0 vtrac_any=174 | drop_exact_any=11 drop_vtrac_any=181 | family_exact_any=9 family_vtrac_any=99 | vt_boxed=78 vt_straight=0
- Hits (winner_hits.csv): rows=227 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=78 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.49381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 008 | score_v2 13.49381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 008 | score_v2 13.34381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 008 | score_v2 12.89381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 008 | score_v2 12.89381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 008 | score_v2 12.74381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 008 | score_v2 12.74381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 008 | score_v2 12.09381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 008 | score_v2 12.09381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 008 | score_v2 11.94381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 008 | score_v2 11.94381 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 008 | score_v2 13.49381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 008 | score_v2 11.89381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 440 | score_v2 9.665714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 520 | score_v2 9.64381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 552 | score_v2 9.197143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 208 | score_v2 9.097143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 203 | score_v2 9.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 524 | score_v2 8.997143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 220 | score_v2 8.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 440 | score_v2 8.865714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 073 (canon 037): items_total=90 exact_any=0 vtrac_any=84 | top winner_present=False best_rank=None/34; Evening 479 (canon 479): items_total=36 exact_any=0 vtrac_any=36 | top winner_present=False best_rank=None/28; Combined 073 (canon 037): items_total=227 exact_any=0 vtrac_any=174 | top winner_present=False best_rank=None/16
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 008, 008, 440, 520, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20260110_034644)

## Top indices (from enhanced JSON)
- index 8 | score 43.00200000000001 | features: presence=28.464500000000008, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 37.78312249999999 | features: presence=21.535622499999988, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 6 | score 28.024235 | features: presence=17.296734999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 2 | score 26.815034999999998 | features: presence=17.147534999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 26.2446225 | features: presence=16.847122499999998, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 4 | score 16.268637500000004 | features: presence=7.751137500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 19 | score 14.981700000000002 | features: presence=5.744200000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 13 | score 13.988637500000001 | features: presence=6.761137500000002, set_echo=0.3, first_hit=0.2666666666666667, column_span=0.17083333333333334
- index 15 | score 12.169458333333333 | features: presence=5.2205, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 25 | score 11.225758333333333 | features: presence=4.4068000000000005, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
086, 068, 680, 018, 186, 865, 681, 810, 568, 586

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 073 | index 11 | file PuertoRico4_vtrac11_winner_073_20260110_034444.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 479 | index 31 | file PuertoRico4_vtrac31_winner_479_20260110_034446.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 073 | index 11 rank 21/35 (rank_frac 0.6) | score 0.0 (top 43.00200000000001, ratio 0.0, delta 43.00200000000001) | winner_in_index_straights=False | top_index_straights: (none)
- winner 479 | index 31 rank 33/35 (rank_frac 0.9428571428571428) | score 0.0 (top 43.00200000000001, ratio 0.0, delta 43.00200000000001) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 073→idx11 rank 21/35 (frac 0.600); 479→idx31 rank 33/35 (frac 0.943).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 8, 18, 6, 2, 23.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — PuertoRico4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2026-01-08)

## Midday winner 073 (canonical 037)
- Top lanes (hot_zones_top_lanes.csv): present | rank 142/200 (rank_frac 0.71) | score_mean 16.888 (top 25.75, ratio 0.6558446601941749, delta 8.861999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 479 (canonical 479)
- Top lanes (hot_zones_top_lanes.csv): present | rank 120/200 (rank_frac 0.6) | score_mean 17.25 (top 25.75, ratio 0.6699029126213593, delta 8.5)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 049 | vt_triad 155 | score_mean 25.75 | tags hot16,literal_draw,straight_lane,vertical5,vt_straight
- rank    2 | triad 279 | vt_triad 335 | score_mean 24.9 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    3 | triad 237 | vt_triad 334 | score_mean 22.6 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 259 | vt_triad 135 | score_mean 22.5 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 144 | vt_triad 25 | score_mean 20.725 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_straight
- rank    6 | triad 359 | vt_triad 145 | score_mean 20.641 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_only_lane,vt_straight
- rank    7 | triad 226 | vt_triad 23 | score_mean 20.144 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    8 | triad 347 | vt_triad 345 | score_mean 20.13 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical4,vt_straight
- rank    9 | triad 346 | vt_triad 245 | score_mean 19.775 | tags funnel_precol1,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 011 | vt_triad 12 | score_mean 19.675 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 073 (canon 037): rank 142/200 (rank_frac 0.710) ratio_to_top=0.6558446601941749; Evening 479 (canon 479): rank 120/200 (rank_frac 0.600) ratio_to_top=0.6699029126213593
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

Aux draws snapshot dir: `sharepacks/2026-01-08/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-08/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=998 head=969, 426, 972, 732, 359
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-08/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=999 head=426, 732, 529, 144, 451
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-08/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=999 head=969, 972, 359, 917, 913

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=3 last_repeat_gap=13 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=66), P2:0 (gap=16), P3:0 (gap=14)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=66)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=42.85895714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.20663571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 205: score=37.844814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.603635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.568914285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.32476428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=35.198814285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=33.922178571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.36371428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 210: score=33.18457142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 447: ds=990 sev=B
- 000: ds=738 sev=B
- 039: ds=726 sev=B
- 466: ds=722 sev=B
- 677: ds=700 sev=B
- 577: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=70 sev=purple
  - 77: ds=69 sev=purple
  - 11: ds=54 sev=purple
  - 55: ds=35 sev=purple
  - 33: ds=30 sev=purple
  - 66: ds=29 sev=purple
  - 88: ds=22 sev=-
  - 00: ds=20 sev=-
  - 44: ds=7 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 47: ds=178 sev=red
  - 48: ds=56 sev=red
  - 56: ds=49 sev=blue
  - 05: ds=47 sev=blue
  - 28: ds=42 sev=blue
  - 06: ds=29 sev=purple
  - 01: ds=26 sev=purple
  - 03: ds=26 sev=purple
  - 12: ds=25 sev=purple
  - 16: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:197, 5:101, 32:95, 26:90, 31:87, 18:61, 34:60, 33:57, 35:55, 16:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=197 fs=18 fl=1 hz=0.025477707006369428, 5:ds=101 fs=27 fl=1 hz=0.0343980343980344, 32:ds=95 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=90 fs=4 fl=2 hz=0.01020408163265306, 31:ds=87 fs=13 fl=3 hz=0.017718715393133997, 18:ds=61 fs=20 fl=0 hz=0.022727272727272728, 34:ds=60 fs=26 fl=0 hz=0.02857142857142857, 33:ds=57 fs=10 fl=0 hz=0.016516516516516516, 35:ds=55 fs=1 fl=2 hz=0.005889281507656065, 16:ds=54 fs=6 fl=2 hz=0.01107419712070875

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=87 flags=purple
- S23: ds=69 flags=purple
- S26: ds=60 flags=blue+purple
- S8: ds=54 flags=purple
- S6: ds=50 flags=purple
- S5: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 059: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS
  - 239: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=63 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=33), P2:1 (gap=29), P3:0 (gap=13)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=42.85895714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.20663571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 205: score=37.844814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.603635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.568914285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.32476428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=35.198814285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=33.922178571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.36371428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 210: score=33.18457142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=963 sev=B
- 299: ds=954 sev=B
- 003: ds=945 sev=B
- 077: ds=931 sev=B
- 333: ds=880 sev=B
- 555: ds=854 sev=B
- 088: ds=825 sev=B
- 888: ds=819 sev=B
- 666: ds=804 sev=B
- 447: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=110 sev=red
  - 22: ds=83 sev=blue
  - 11: ds=59 sev=purple
  - 99: ds=43 sev=purple
  - 77: ds=34 sev=purple
  - 33: ds=28 sev=purple
  - 88: ds=25 sev=purple
  - 55: ds=17 sev=-
  - 66: ds=14 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 47: ds=116 sev=red
  - 38: ds=47 sev=blue
  - 03: ds=46 sev=blue
  - 04: ds=46 sev=blue
  - 35: ds=44 sev=blue
  - 48: ds=36 sev=purple
  - 19: ds=35 sev=purple
  - 18: ds=32 sev=purple
  - 13: ds=29 sev=purple
  - 49: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:100, 10:98, 26:94, 3:87, 16:59, 23:54, 15:52, 5:50, 32:47, 31:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=100 fs=16 fl=2 hz=0.020809248554913295, 10:ds=98 fs=20 fl=3 hz=0.026376146788990827, 26:ds=94 fs=7 fl=2 hz=0.011682242990654207, 3:ds=87 fs=31 fl=0 hz=0.03506787330316742, 16:ds=59 fs=4 fl=2 hz=0.009695290858725763, 23:ds=54 fs=31 fl=1 hz=0.034782608695652174, 15:ds=52 fs=25 fl=0 hz=0.026939655172413795, 5:ds=50 fs=28 fl=0 hz=0.03181818181818182, 32:ds=47 fs=2 fl=1 hz=0.006112469437652812, 31:ds=43 fs=22 fl=1 hz=0.024338624338624337

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=46 flags=purple
- S25: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 1}}
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
- current_index=25 streak=1 max=2 last_repeat_gap=5 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=33), P2:2 (gap=35), P3:6 (gap=25)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 200: score=42.85895714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 206: score=38.20663571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 205: score=37.844814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 280: score=36.603635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 207: score=36.568914285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 201: score=36.32476428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 204: score=35.198814285714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 800: score=33.922178571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 220: score=33.36371428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 210: score=33.18457142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=995 sev=B
- 579: ds=976 sev=B
- 114: ds=920 sev=B
- 555: ds=859 sev=B
- 888: ds=767 sev=B
- 067: ds=756 sev=B
- 446: ds=743 sev=B
- 259: ds=741 sev=B
- 224: ds=727 sev=B
- 449: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=147 sev=red
  - 44: ds=143 sev=red
  - 77: ds=45 sev=purple
  - 66: ds=36 sev=purple
  - 22: ds=35 sev=purple
  - 11: ds=27 sev=purple
  - 33: ds=15 sev=-
  - 88: ds=11 sev=-
  - 00: ds=10 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 25: ds=103 sev=red
  - 47: ds=89 sev=red
  - 45: ds=73 sev=red
  - 26: ds=66 sev=red
  - 24: ds=46 sev=blue
  - 05: ds=42 sev=blue
  - 56: ds=42 sev=blue
  - 23: ds=33 sev=purple
  - 89: ds=30 sev=purple
  - 48: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:452, 32:167, 4:121, 10:108, 31:96, 5:86, 33:72, 27:69, 1:61, 30:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=452 fs=5 fl=1 hz=0.01662049861495845, 32:ds=167 fs=6 fl=1 hz=0.009987515605493134, 4:ds=121 fs=23 fl=2 hz=0.03071253071253071, 10:ds=108 fs=16 fl=2 hz=0.0234375, 31:ds=96 fs=18 fl=3 hz=0.02394526795895097, 5:ds=86 fs=18 fl=2 hz=0.022446689113355782, 33:ds=72 fs=12 fl=1 hz=0.017361111111111112, 27:ds=69 fs=18 fl=1 hz=0.02358490566037736, 1:ds=61 fs=4 fl=4 hz=0.00909090909090909, 30:ds=46 fs=42 fl=0 hz=0.044823906083244394

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=79 flags=purple
- S23: ds=50 flags=blue+purple
- S16: ds=45 flags=red+purple
- S12: ds=41 flags=purple
- S21: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 489: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 447 -> combined:990(B); midday:743(B)
- 555 -> evening:859(B); midday:854(B)
- 888 -> evening:767(B); midday:819(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:26(purple); midday:46(blue)
- 05 -> combined:47(blue); evening:42(blue)
- 11 -> combined:54(purple); evening:27(purple); midday:59(purple)
- 22 -> combined:70(purple); evening:35(purple); midday:83(blue)
- 33 -> combined:30(purple); midday:28(purple)
- 47 -> combined:178(red); evening:89(red); midday:116(red)
- 48 -> combined:56(red); evening:28(purple); midday:36(purple)
- 55 -> combined:35(purple); evening:147(red)
- 56 -> combined:49(blue); evening:42(blue)
- 66 -> combined:29(purple); evening:36(purple)
- 77 -> combined:69(purple); evening:45(purple); midday:34(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.970571428571429)[R1,XVAR-Cons(CEM)], 8(2.533792857142857)[R2,XVAR-Cons(CE)], 3(1.2433999999999998)[R2,Double-Pressure], 1(1.0761999999999998)[R2,Double-Pressure], 0(0.25557142857142856)[R3,Swap]
- P2: 0(6.2402428571428565)[R1,XVAR-Cons(CEM)], 8(2.484921428571429)[R2,XVAR-Cons(CM)], 2(1.7449999999999999)[R1,Double-Pressure], 1(1.5658571428571428)[R1,Double-Pressure], 3(0.9717)[R2,Double-Pressure]
- P3: 0(3.648142857142857)[R1,Mirror-Echo], 6(1.4958214285714286)[R1,Mirror-Echo], 5(1.134)[R2,Mirror-Echo], 7(0.8581)[R2,Double-Pressure], 1(0.61395)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=Puerto Rico; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:2(gap=66), P2:0(gap=16), P3:0(gap=14); top cartesian candidates: 200, 206, 205, 280, 207.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '8'], 'pairs': {'remaining_count': 1}}; top candidates: 014, 023, 059, 068, 149.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 447→combined:990(B),midday:743(B); 555→midday:854(B),evening:859(B); 888→midday:819(B),evening:767(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 10:197, 5:101, 32:95, 26:90, 31:87.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=073 Evening=479; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 037 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 479 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 073 (canon 037): box `037` covers winner `073` (boxed hit).
  - Evening winner 479 (canon 479): box `479` covers winner `479` (boxed hit).
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
