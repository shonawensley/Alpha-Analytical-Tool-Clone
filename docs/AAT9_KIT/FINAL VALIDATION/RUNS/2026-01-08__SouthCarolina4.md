# Master Validation Run Report — SouthCarolina4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-08/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-08/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-08/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-08/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-08/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-08/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac26_winner_277_20260110_034447.html`
- `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac9_winner_910_20260110_034447.html`

Winners JSON files:
- `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac26_winner_277_20260110_034447.json`
- `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac9_winner_910_20260110_034447.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 277 (canon 277): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 910 (canon 019): exact_boxed=True exact_straight=True | rank 2310/4952 (rank_frac 0.466)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 277 idx26 (rank 34/35, frac 0.971), 910 idx9 (rank 4/35, frac 0.114)
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

### 2.Stable — SouthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-08)

## Midday winner 277 (canonical 277)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=305 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 81 | rank 153/1423 (rank_frac 0.10751932536893886) | score 21.5 (top 33.5, ratio 0.6417910447761194, delta 12.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=1
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 910 (canonical 019)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=11 | family_rows=2 | exact_boxed=11 | exact_straight=10 | vt_boxed=11
- Scores (patterns_scores.csv): rank 2310/4952 (rank_frac 0.4664781906300485) | score 12.5 (top 37.5, ratio 0.3333333333333333, delta 25.0) | section Combined, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|hidden3v|vtrac_straight|draw_chain2
- Compound (patterns_compound.csv): rank 461/1763 (rank_frac 0.2614861032331254) | score 18.0 (top 80.0, ratio 0.225, delta 62.0) | section Combined, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|vstrx3
- Families (patterns_families.csv): count 2 | rank 1017/1423 (rank_frac 0.7146872803935348) | score 11.0 (top 33.5, ratio 0.3283582089552239, delta 22.5) | section Midday, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=71

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 099 | section Combined | score 73.0 | col1_hits 6 | hot2 8
- rank    1 | canon 599 | section Evening | score 80.0 | col1_hits 6 | hot2 8
- rank    7 | canon 009 | section Combined | score 61.0 | col1_hits 6 | hot2 7
- rank   27 | canon 0059 | section Combined | score 46.0 | col1_hits 4 | hot2 6
- rank   25 | canon 0099 | section Combined | score 47.5 | col1_hits 5 | hot2 6
- rank   18 | canon 059 | section Combined | score 49.0 | col1_hits 4 | hot2 6
- rank   14 | canon 0599 | section Combined | score 52.0 | col1_hits 5 | hot2 6
- rank   13 | canon 00599 | section Combined | score 54.5 | col1_hits 5 | hot2 6
- rank   11 | canon 005 | section Combined | score 57.0 | col1_hits 5 | hot2 6
- rank    4 | canon 599 | section Combined | score 67.5 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1329 | family 1 | score 7.0 | hot2 0 | section Midday
- rank  704 | family 17 | score 14.0 | hot2 0 | section Midday
- rank 1120 | family 27 | score 10.0 | hot2 1 | section Midday
- rank 1120 | family 7 | score 10.0 | hot2 3 | section Midday
- rank 1192 | family 11 | score 9.0 | hot2 5 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 277 (canon 277): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 910 (canon 019): exact_boxed=True exact_straight=True | rank 2310/4952 (rank_frac 0.466)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260110)

## Midday winner 277 (canonical 277)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=36 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.14381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 910 (canonical 019)
- Stamp (winner_stamp.json): items_total=55 | exact_any=6 exact_final=0 | vtrac_any=16 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=47 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=55 | exact_any=6 vtrac_any=16 | drop_exact_any=0 drop_vtrac_any=47 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=31 vt_straight=0
- Hits (winner_hits.csv): rows=55 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=31 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 277 (canonical 277)
- Stamp (winner_stamp.json): items_total=44 | exact_any=44 exact_final=0 | vtrac_any=44 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=44 | exact_any=44 vtrac_any=44 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=44 vt_straight=0
- Hits (winner_hits.csv): rows=44 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=44 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=18 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=15.377143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 599 | score_v2 15.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 599 | score_v2 15.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 15.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 599 | score_v2 15.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 15.287143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 599 | score_v2 15.127143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 5 | pattern 599 | score_v2 15.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 599 | score_v2 15.037143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 14.787143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 14.627143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 15.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 599 | score_v2 14.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 13.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 559 | score_v2 13.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 559 | score_v2 13.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 599 | score_v2 13.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 599 | score_v2 12.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 592 | score_v2 12.157143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 990 | score_v2 12.14381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 559 | score_v2 11.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 277 (canon 277): items_total=0 exact_any=0 vtrac_any=0 | top winner_present=False best_rank=None/36; Evening 910 (canon 019): items_total=55 exact_any=6 vtrac_any=16 | top winner_present=False best_rank=None/14; Combined 277 (canon 277): items_total=44 exact_any=44 vtrac_any=44 | top winner_present=False best_rank=None/18
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 599, 599, 559, 559, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260110_034645)

## Top indices (from enhanced JSON)
- index 24 | score 38.90331 | features: presence=27.355809999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 38.7449125 | features: presence=27.037412500000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 5 | score 38.204341666666664 | features: presence=27.192050000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 37.77979 | features: presence=24.672290000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 18.02405 | features: presence=11.756549999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 13 | score 17.572200000000002 | features: presence=6.834700000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 3 | score 14.684016666666668 | features: presence=9.199850000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 14.196955 | features: presence=9.899455000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 4 | score 14.0044 | features: presence=4.8568999999999996, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 23 | score 12.743283333333334 | features: presence=9.224325, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
936, 593, 059, 093, 596, 963, 659, 906, 903, 096

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 277 | index 26 | file SouthCarolina4_vtrac26_winner_277_20260110_034447.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 910 | index 9 | file SouthCarolina4_vtrac9_winner_910_20260110_034447.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 277 | index 26 rank 34/35 (rank_frac 0.9714285714285714) | score 0.0 (top 38.90331, ratio 0.0, delta 38.90331) | winner_in_index_straights=False | top_index_straights: (none)
- winner 910 | index 9 rank 4/35 (rank_frac 0.11428571428571428) | score 37.77979 (top 38.90331, ratio 0.9711201951710536, delta 1.1235199999999992) | winner_in_index_straights=False | top_index_straights: 596 (13.853), 659 (12.471), 906 (12.217)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 277→idx26 rank 34/35 (frac 0.971); 910→idx9 rank 4/35 (frac 0.114).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 24, 14, 5, 9, 8.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-08)

## Midday winner 277 (canonical 277)
- Top lanes (hot_zones_top_lanes.csv): present | rank 23/210 (rank_frac 0.10952380952380952) | score_mean 18.47 (top 21.25, ratio 0.8691764705882352, delta 2.780000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 910 (canonical 019)
- Top lanes (hot_zones_top_lanes.csv): present | rank 132/210 (rank_frac 0.6285714285714286) | score_mean 16.247 (top 21.25, ratio 0.7645647058823529, delta 5.003)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 016 | vt_triad 122 | score_mean 21.25 | tags hot20,set1_bonus
- rank    1 | triad 156 | vt_triad 122 | score_mean 21.25 | tags hot20,set1_bonus
- rank    3 | triad 336 | vt_triad 24 | score_mean 21.03 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 288 | vt_triad 34 | score_mean 20.492 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 127 | vt_triad 233 | score_mean 20.233 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 117 | vt_triad 23 | score_mean 20.162 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 124 | vt_triad 235 | score_mean 19.853 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 568 | vt_triad 124 | score_mean 19.29 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    9 | triad 038 | vt_triad 144 | score_mean 19.238 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 688 | vt_triad 24 | score_mean 19.161 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 277 (canon 277): rank 23/210 (rank_frac 0.110) ratio_to_top=0.8691764705882352; Evening 910 (canon 019): rank 132/210 (rank_frac 0.629) ratio_to_top=0.7645647058823529
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

Aux draws snapshot dir: `sharepacks/2026-01-08/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-08/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=336, 288, 412, 586, 712
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-08/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=288, 586, 171, 189, 308
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-08/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=336, 412, 712, 432, 051

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=2 last_repeat_gap=26 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=14), P2:9 (gap=28), P3:7 (gap=20)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.622144999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=41.394014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.8923 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.58602714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 897: score=36.354014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=35.24435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.95164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.73832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 698: score=33.17665714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=32.706064285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=981 sev=B
- 449: ds=910 sev=B
- 156: ds=893 sev=B
- 778: ds=863 sev=B
- 279: ds=862 sev=B
- 033: ds=794 sev=B
- 004: ds=782 sev=B
- 688: ds=749 sev=B
- 278: ds=716 sev=B
- 377: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=190 sev=red
  - 55: ds=127 sev=red
  - 77: ds=111 sev=red
  - 22: ds=73 sev=blue
  - 66: ds=61 sev=purple
  - 00: ds=34 sev=purple
  - 44: ds=13 sev=-
  - 11: ds=5 sev=-
  - 88: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 78: ds=62 sev=red
  - 29: ds=43 sev=blue
  - 06: ds=36 sev=purple
  - 16: ds=36 sev=purple
  - 59: ds=32 sev=purple
  - 13: ds=28 sev=purple
  - 39: ds=28 sev=purple
  - 07: ds=25 sev=purple
  - 37: ds=25 sev=purple
  - 02: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:454, 35:397, 1:178, 26:166, 31:128, 4:119, 28:111, 27:94, 19:78, 18:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=454 fs=0 fl=0 hz=0.002197802197802198, 35:ds=397 fs=0 fl=0 hz=0.001949317738791423, 1:ds=178 fs=6 fl=4 hz=0.012195121951219513, 26:ds=166 fs=2 fl=0 hz=0.0062402496099844, 31:ds=128 fs=26 fl=0 hz=0.03002309468822171, 4:ds=119 fs=21 fl=2 hz=0.026589595375722544, 28:ds=111 fs=16 fl=2 hz=0.021479713603818614, 27:ds=94 fs=26 fl=0 hz=0.02911534154535274, 19:ds=78 fs=15 fl=1 hz=0.0189520624303233, 18:ds=72 fs=17 fl=1 hz=0.019801980198019802

### Sums (source: aux_validation.sums_stats_by_variant)
- S17: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=76 flags=blue+purple
- S23: ds=65 flags=purple
- S5: ds=64 flags=purple
- S24: ds=62 flags=blue+purple
- S4: ds=54 flags=purple
- S3: ds=53 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}
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
- current_index=29 streak=1 max=3 last_repeat_gap=8 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=18), P2:3 (gap=44), P3:7 (gap=14)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.622144999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=41.394014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.8923 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.58602714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 897: score=36.354014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=35.24435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.95164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.73832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 698: score=33.17665714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=32.706064285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=882 sev=B
- 555: ds=877 sev=B
- 222: ds=854 sev=B
- 337: ds=831 sev=B
- 003: ds=822 sev=B
- 228: ds=813 sev=B
- 556: ds=715 sev=B
- 449: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=117 sev=red
  - 55: ds=81 sev=blue
  - 77: ds=50 sev=purple
  - 33: ds=44 sev=purple
  - 22: ds=40 sev=purple
  - 66: ds=27 sev=purple
  - 00: ds=18 sev=-
  - 44: ds=10 sev=-
  - 11: ds=2 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 49: ds=58 sev=red
  - 67: ds=52 sev=blue
  - 34: ds=51 sev=blue
  - 27: ds=45 sev=blue
  - 07: ds=36 sev=purple
  - 05: ds=33 sev=purple
  - 15: ds=31 sev=purple
  - 78: ds=30 sev=purple
  - 69: ds=29 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:418, 26:196, 35:182, 27:147, 6:115, 5:84, 1:81, 15:76, 34:62, 31:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=418 fs=1 fl=2 hz=0.006993006993006993, 26:ds=196 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=182 fs=1 fl=1 hz=0.004968944099378882, 27:ds=147 fs=18 fl=3 hz=0.026582278481012658, 6:ds=115 fs=24 fl=2 hz=0.02957906712172924, 5:ds=84 fs=20 fl=1 hz=0.023102310231023104, 1:ds=81 fs=7 fl=3 hz=0.012127894156560088, 15:ds=76 fs=17 fl=3 hz=0.021691973969631236, 34:ds=62 fs=28 fl=1 hz=0.03159041394335512, 31:ds=58 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S25: ds=82 flags=purple
- S21: ds=62 flags=purple
- S20: ds=58 flags=purple
- S17: ds=56 flags=purple
- S8: ds=54 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 134: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 089: score=2 tags=RS
  - 125: score=2 tags=RS
  - 179: score=2 tags=RS
  - 269: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=36 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=22), P2:9 (gap=18), P3:8 (gap=25)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 695: score=46.622144999999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 895: score=41.394014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 697: score=38.8923 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 595: score=37.58602714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 897: score=36.354014285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 665: score=35.24435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=34.95164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 692: score=33.73832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 698: score=33.17665714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=32.706064285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=986 sev=B
- 117: ds=897 sev=B
- 005: ds=883 sev=B
- 577: ds=860 sev=B
- 155: ds=840 sev=B
- 777: ds=839 sev=B
- 669: ds=831 sev=B
- 179: ds=813 sev=B
- 366: ds=779 sev=B
- 222: ds=773 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=103 sev=blue
  - 77: ds=90 sev=blue
  - 66: ds=82 sev=blue
  - 55: ds=69 sev=purple
  - 88: ds=63 sev=purple
  - 22: ds=40 sev=purple
  - 11: ds=29 sev=purple
  - 00: ds=19 sev=-
  - 44: ds=7 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 58: ds=104 sev=red
  - 35: ds=71 sev=red
  - 29: ds=66 sev=red
  - 47: ds=56 sev=red
  - 19: ds=38 sev=blue
  - 78: ds=34 sev=purple
  - 68: ds=31 sev=purple
  - 38: ds=25 sev=purple
  - 13: ds=23 sev=-
  - 09: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:491, 1:278, 32:245, 31:224, 4:144, 28:117, 19:113, 26:90, 16:86, 13:85

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=491 fs=3 fl=1 hz=0.017391304347826087, 1:ds=278 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=245 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=224 fs=16 fl=1 hz=0.021935483870967745, 4:ds=144 fs=21 fl=3 hz=0.028742514970059883, 28:ds=117 fs=10 fl=4 hz=0.017676767676767676, 19:ds=113 fs=12 fl=2 hz=0.016968325791855206, 26:ds=90 fs=0 fl=0 hz=0.002347417840375587, 16:ds=86 fs=6 fl=4 hz=0.011820330969267141, 13:ds=85 fs=22 fl=0 hz=0.024363233665559245

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=69 flags=purple
- S15: ds=60 flags=red+purple
- S17: ds=56 flags=purple
- S23: ds=53 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['8', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:773(B); midday:854(B)
- 366 -> combined:981(B); evening:779(B)
- 449 -> combined:910(B); midday:673(B)
- 688 -> combined:749(B); evening:738(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:25(purple); midday:36(purple)
- 16 -> combined:36(purple); midday:27(purple)
- 22 -> combined:73(blue); evening:40(purple); midday:40(purple)
- 29 -> combined:43(blue); evening:66(red)
- 55 -> combined:127(red); evening:69(purple); midday:81(blue)
- 66 -> combined:61(purple); evening:82(blue); midday:27(purple)
- 77 -> combined:111(red); evening:90(blue); midday:50(purple)
- 78 -> combined:62(red); evening:34(purple); midday:30(purple)
- 99 -> combined:190(red); evening:103(blue); midday:117(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(3.9773571428571426)[R1,XVAR-Cons(CE)], 8(2.4390714285714283)[R3,XVAR-Cons(CM)], 1(1.3656714285714284)[R2,Mirror-Echo], 0(1.2374285714285713)[R1,Double-Pressure], 9(0.964)[R2,Double-Pressure]
- P2: 9(7.782871428571428)[R1,Mirror-Echo], 6(2.5949214285714284)[R2,XVAR-Cons(CE)], 4(2.3022142857142858)[R3,Mirror-Echo], 3(1.7449999999999999)[R1,Double-Pressure], 0(0.9925999999999999)[R2,Double-Pressure]
- P3: 5(6.172071428571429)[R2,XVAR-Cons(CEM)], 7(3.632071428571429)[R1,XVAR-Cons(CM)], 8(1.4164285714285714)[R1,Double-Pressure], 2(0.9781)[R2,Mirror-Echo], 0(0.3227285714285714)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=14), P2:9(gap=28), P3:7(gap=20); top cartesian candidates: 695, 895, 697, 595, 897.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 013, 014, 015, 016.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:854(B),evening:773(B); 366→combined:981(B),evening:779(B); 449→combined:910(B),midday:673(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:454, 35:397, 1:178, 26:166, 31:128.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=277 Evening=910; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Evening): BOX 019 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 277 (canon 277): box `277` covers winner `277` (boxed hit).
  - Evening winner 910 (canon 019): box `019` covers winner `910` (boxed hit).
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
