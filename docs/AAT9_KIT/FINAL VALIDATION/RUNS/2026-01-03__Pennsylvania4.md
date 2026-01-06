# Master Validation Run Report — Pennsylvania4 — results 2026-01-03 (history workbook ~ 2026-01-02)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-03/Pennsylvania4/`
- Winners lens: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2026-01-03/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2026-01-03/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2026-01-03/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2026-01-03/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2026-01-03/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2026-01-03/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac15_winner_909_20260105_054601.html`
- `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac31_winner_744_20260105_054600.html`

Winners JSON files:
- `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac15_winner_909_20260105_054601.json`
- `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac31_winner_744_20260105_054600.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-03/Pennsylvania4/winners/Pennsylvania4/digest.md`.
- Q2: Stable environment quick read: Midday 744 (canon 447): exact_boxed=True exact_straight=True | rank 931/5396 (rank_frac 0.173); Evening 909 (canon 099): exact_boxed=True exact_straight=True | rank 206/5396 (rank_frac 0.038)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 909 idx15 (rank 3/35, frac 0.086), 744 idx31 (rank 25/35, frac 0.714)
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

### 2.Stable — Pennsylvania4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2026-01-03)

## Midday winner 744 (canonical 447)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=11 | family_rows=350 | exact_boxed=11 | exact_straight=11 | vt_boxed=11
- Scores (patterns_scores.csv): rank 931/5396 (rank_frac 0.17253521126760563) | score 17.5 (top 38.5, ratio 0.45454545454545453, delta 21.0) | section Combined, Set Set1, Draw Draw5, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|hot2|hidden3v|double_mirror|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 97/1824 (rank_frac 0.05317982456140351) | score 33.0 (top 106.5, ratio 0.30985915492957744, delta 73.5) | section Combined, col1_hits 3, hot2 2, set_chain 1, draw_chain 3 | why draw_chain3|col1x3|hot1x1|hot2x2|vstrx6|dblmirrorx6
- Families (patterns_families.csv): count 62 | rank 21/1310 (rank_frac 0.01603053435114504) | score 33.5 (top 38.5, ratio 0.8701298701298701, delta 5.0) | section Combined, hot2 9
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=10

## Evening winner 909 (canonical 099)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=39 | family_rows=39 | exact_boxed=39 | exact_straight=11 | vt_boxed=39
- Scores (patterns_scores.csv): rank 206/5396 (rank_frac 0.03817642698295033) | score 25.5 (top 38.5, ratio 0.6623376623376623, delta 13.0) | section Combined, Set Set1, Draw Draw1, Col 3, hot 2, vt_straight 0.0 | why boxed|cov3|hp_repeat6|vstr2|hot2|perm2|hidden3v|double_mirror|draw_chain7
- Compound (patterns_compound.csv): rank 8/1824 (rank_frac 0.0043859649122807015) | score 73.5 (top 106.5, ratio 0.6901408450704225, delta 33.0) | section Combined, col1_hits 6, hot2 10, set_chain 1, draw_chain 7 | why draw_chain7|col1x6|hot1x6|hot2x10|vstrx5|dblmirrorx27
- Families (patterns_families.csv): count 25 | rank 169/1310 (rank_frac 0.12900763358778625) | score 22.5 (top 38.5, ratio 0.5844155844155844, delta 16.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=25

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 559 | section Combined | score 106.5 | col1_hits 9 | hot2 11
- rank    4 | canon 599 | section Combined | score 88.5 | col1_hits 7 | hot2 11
- rank    5 | canon 5599 | section Combined | score 81.5 | col1_hits 7 | hot2 11
- rank    2 | canon 055 | section Combined | score 100.0 | col1_hits 8 | hot2 10
- rank    3 | canon 0559 | section Combined | score 89.5 | col1_hits 8 | hot2 10
- rank    8 | canon 099 | section Combined | score 73.5 | col1_hits 6 | hot2 10
- rank    9 | canon 0599 | section Combined | score 69.5 | col1_hits 6 | hot2 10
- rank   12 | canon 05599 | section Combined | score 66.0 | col1_hits 6 | hot2 10
- rank    7 | canon 455 | section Combined | score 75.5 | col1_hits 6 | hot2 8
- rank    6 | canon 499 | section Combined | score 76.0 | col1_hits 5 | hot2 8

## Top families (patterns_families.csv)
- rank 1250 | family 35 | score 6.0 | hot2 0 | section Midday
- rank  861 | family 12 | score 12.0 | hot2 0 | section Midday
- rank  920 | family 24 | score 11.5 | hot2 0 | section Midday
- rank 1250 | family 11 | score 6.0 | hot2 0 | section Midday
- rank  212 | family 14 | score 21.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 744 (canon 447): exact_boxed=True exact_straight=True | rank 931/5396 (rank_frac 0.173); Evening 909 (canon 099): exact_boxed=True exact_straight=True | rank 206/5396 (rank_frac 0.038)
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

### 2.Digit Reduction — Pennsylvania4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20260105)

## Midday winner 744 (canonical 447)
- Stamp (winner_stamp.json): items_total=28 | exact_any=1 exact_final=0 | vtrac_any=28 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=5 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=1 family_vtrac_final=0
- Flags (winner_flags.csv): rows=28 | exact_any=1 vtrac_any=28 | drop_exact_any=0 drop_vtrac_any=5 | family_exact_any=0 family_vtrac_any=1 | vt_boxed=6 vt_straight=0
- Hits (winner_hits.csv): rows=28 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=6 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 909 (canonical 099)
- Stamp (winner_stamp.json): items_total=156 | exact_any=36 exact_final=0 | vtrac_any=156 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=156 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=74 family_vtrac_final=0
- Flags (winner_flags.csv): rows=156 | exact_any=36 vtrac_any=156 | drop_exact_any=0 drop_vtrac_any=156 | family_exact_any=0 family_vtrac_any=74 | vt_boxed=26 vt_straight=0
- Hits (winner_hits.csv): rows=156 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=26 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 744 (canonical 447)
- Stamp (winner_stamp.json): items_total=354 | exact_any=83 exact_final=0 | vtrac_any=349 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=135 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=83 family_vtrac_final=0
- Flags (winner_flags.csv): rows=354 | exact_any=83 vtrac_any=349 | drop_exact_any=0 drop_vtrac_any=135 | family_exact_any=0 family_vtrac_any=83 | vt_boxed=307 vt_straight=0
- Hits (winner_hits.csv): rows=354 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=307 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=2 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=25.277143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 25.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 24.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 23.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 23.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw2 col 4 | pattern 559 | score_v2 22.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 22.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 22.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 559 | score_v2 22.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 22.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 559 | score_v2 22.727143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 559 | score_v2 25.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 24.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 559 | score_v2 17.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 17.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 559 | score_v2 15.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 15.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 559 | score_v2 14.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 599 | score_v2 14.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 594 | score_v2 12.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 599 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 744 (canon 447): items_total=28 exact_any=1 vtrac_any=28 | top winner_present=False best_rank=None/14; Evening 909 (canon 099): items_total=156 exact_any=36 vtrac_any=156 | top winner_present=False best_rank=None/24; Combined 744 (canon 447): items_total=354 exact_any=83 vtrac_any=349 | top winner_present=False best_rank=None/2
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 559, 559, 559, 559, 559.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20260105_054822)

## Top indices (from enhanced JSON)
- index 5 | score 97.05959999999999 | features: presence=70.9721, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 12 | score 52.87478749999999 | features: presence=35.9372875, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 49.438950000000006 | features: presence=38.98145000000001, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 14 | score 33.1451 | features: presence=19.8076, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 3 | score 32.450160000000004 | features: presence=21.932660000000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 27.856849999999998 | features: presence=12.619349999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 30 | score 22.100450000000002 | features: presence=12.58295, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 11 | score 21.336050000000004 | features: presence=10.87855, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 1 | score 15.8705 | features: presence=9.663, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 21 | score 14.855525000000002 | features: presence=7.248025000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
590, 095, 907, 059, 593, 709, 759, 597, 795, 705

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 909 | index 15 | file Pennsylvania4_vtrac15_winner_909_20260105_054601.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 744 | index 31 | file Pennsylvania4_vtrac31_winner_744_20260105_054600.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 909 | index 15 rank 3/35 (rank_frac 0.08571428571428572) | score 49.438950000000006 (top 97.05959999999999, ratio 0.5093669250645996, delta 47.62064999999998) | winner_in_index_straights=False | top_index_straights: (none)
- winner 744 | index 31 rank 25/35 (rank_frac 0.7142857142857143) | score 3.5104583333333337 (top 97.05959999999999, ratio 0.03616806924130466, delta 93.54914166666666) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 909→idx15 rank 3/35 (frac 0.086); 744→idx31 rank 25/35 (frac 0.714).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 5, 12, 15, 14, 3.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Pennsylvania4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2026-01-03)

## Midday winner 744 (canonical 447)
- Top lanes (hot_zones_top_lanes.csv): present | rank 110/207 (rank_frac 0.5314009661835749) | score_mean 17.162 (top 23.35, ratio 0.7349892933618842, delta 6.188000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 909 (canonical 099)
- Top lanes (hot_zones_top_lanes.csv): present | rank 9/207 (rank_frac 0.043478260869565216) | score_mean 20.12 (top 23.35, ratio 0.8616702355460385, delta 3.2300000000000004)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 267 | vt_triad 233 | score_mean 23.35 | tags hot16,literal_draw,straight_lane,vertical1,vt_straight
- rank    2 | triad 036 | vt_triad 124 | score_mean 21.308 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 224 | vt_triad 35 | score_mean 21.079 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 178 | vt_triad 234 | score_mean 20.933 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 122 | vt_triad 23 | score_mean 20.66 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    6 | triad 559 | vt_triad 15 | score_mean 20.448 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    7 | triad 223 | vt_triad 34 | score_mean 20.354 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 599 | vt_triad 15 | score_mean 20.346 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vertical4,vt_straight
- rank    9 | triad 099 | vt_triad 15 | score_mean 20.12 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 117 | vt_triad 23 | score_mean 20.026 | tags funnel_precol1,hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 744 (canon 447): rank 110/207 (rank_frac 0.531) ratio_to_top=0.7349892933618842; Evening 909 (canon 099): rank 9/207 (rank_frac 0.043) ratio_to_top=0.8616702355460385
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

Aux draws snapshot dir: `sharepacks/2026-01-03/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=360, 871, 328, 322, 221
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=871, 322, 684, 186, 239
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=360, 328, 221, 173, 460

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=25 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:4 (gap=30), P3:7 (gap=17)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=998 sev=B
- 666: ds=996 sev=B
- 159: ds=884 sev=B
- 007: ds=881 sev=B
- 088: ds=845 sev=B
- 008: ds=823 sev=B
- 444: ds=799 sev=B
- 039: ds=774 sev=B
- 355: ds=764 sev=B
- 344: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=141 sev=red
  - 77: ds=80 sev=blue
  - 88: ds=79 sev=blue
  - 44: ds=73 sev=blue
  - 66: ds=67 sev=purple
  - 55: ds=44 sev=purple
  - 11: ds=29 sev=purple
  - 00: ds=27 sev=purple
  - 99: ds=14 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 07: ds=47 sev=blue
  - 35: ds=40 sev=blue
  - 69: ds=38 sev=blue
  - 09: ds=34 sev=purple
  - 34: ds=33 sev=purple
  - 19: ds=31 sev=purple
  - 47: ds=26 sev=purple
  - 15: ds=23 sev=-
  - 45: ds=20 sev=-
  - 08: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:283, 26:240, 16:98, 7:66, 6:61, 13:59, 19:55, 10:50, 31:46, 1:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=283 fs=2 fl=1 hz=0.007380073800738007, 26:ds=240 fs=0 fl=1 hz=0.003898635477582846, 16:ds=98 fs=3 fl=2 hz=0.007371007371007371, 7:ds=66 fs=36 fl=1 hz=0.03965702036441586, 6:ds=61 fs=22 fl=1 hz=0.02454642475987193, 13:ds=59 fs=21 fl=1 hz=0.024553571428571428, 19:ds=55 fs=21 fl=3 hz=0.025695931477516063, 10:ds=50 fs=23 fl=2 hz=0.02676659528907923, 31:ds=46 fs=22 fl=2 hz=0.02531645569620253, 1:ds=44 fs=1 fl=2 hz=0.0044742729306487695

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=92 flags=purple
- S20: ds=79 flags=purple
- S6: ds=58 flags=purple
- S25: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=34 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:4 (gap=18), P3:5 (gap=28)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=978 sev=B
- 288: ds=965 sev=B
- 255: ds=936 sev=B
- 668: ds=918 sev=B
- 199: ds=866 sev=B
- 499: ds=792 sev=B
- 399: ds=775 sev=B
- 039: ds=763 sev=B
- 448: ds=752 sev=B
- 005: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=187 sev=red
  - 99: ds=134 sev=red
  - 77: ds=77 sev=blue
  - 33: ds=70 sev=purple
  - 88: ds=39 sev=purple
  - 44: ds=36 sev=purple
  - 66: ds=33 sev=purple
  - 11: ds=14 sev=-
  - 00: ds=13 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 59: ds=80 sev=red
  - 79: ds=74 sev=red
  - 12: ds=49 sev=blue
  - 06: ds=44 sev=blue
  - 35: ds=41 sev=blue
  - 56: ds=33 sev=purple
  - 69: ds=31 sev=purple
  - 13: ds=26 sev=purple
  - 57: ds=25 sev=purple
  - 03: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:376, 1:361, 34:215, 16:173, 15:164, 32:141, 35:118, 28:63, 5:48, 2:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=376 fs=0 fl=0 hz=0.0, 1:ds=361 fs=2 fl=2 hz=0.009124087591240877, 34:ds=215 fs=19 fl=1 hz=0.02631578947368421, 16:ds=173 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=164 fs=23 fl=0 hz=0.029411764705882353, 32:ds=141 fs=3 fl=1 hz=0.006720430107526881, 35:ds=118 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=63 fs=26 fl=2 hz=0.02997858672376874, 5:ds=48 fs=18 fl=2 hz=0.022175290390707498, 2:ds=44 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=95 flags=red+purple
- S22: ds=80 flags=purple
- S23: ds=68 flags=purple
- S3: ds=62 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=64 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:1 (gap=36), P3:6 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=974 sev=B
- 009: ds=932 sev=B
- 255: ds=890 sev=B
- 138: ds=830 sev=B
- 117: ds=813 sev=B
- 158: ds=775 sev=B
- 344: ds=768 sev=B
- 199: ds=759 sev=B
- 112: ds=719 sev=B
- 277: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=129 sev=red
  - 33: ds=71 sev=blue
  - 44: ds=42 sev=purple
  - 77: ds=40 sev=purple
  - 66: ds=38 sev=purple
  - 11: ds=29 sev=purple
  - 55: ds=22 sev=-
  - 00: ds=16 sev=-
  - 99: ds=7 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 68: ds=87 sev=red
  - 07: ds=64 sev=red
  - 15: ds=52 sev=blue
  - 78: ds=37 sev=blue
  - 19: ds=36 sev=purple
  - 01: ds=30 sev=purple
  - 18: ds=30 sev=purple
  - 14: ds=29 sev=purple
  - 39: ds=27 sev=purple
  - 16: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:618, 23:157, 26:120, 18:117, 13:66, 33:51, 16:49, 30:48, 24:45, 27:37

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=618 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=157 fs=17 fl=2 hz=0.025165562913907286, 26:ds=120 fs=2 fl=1 hz=0.0056657223796034, 18:ds=117 fs=23 fl=2 hz=0.02910360884749709, 13:ds=66 fs=20 fl=1 hz=0.024881516587677725, 33:ds=51 fs=19 fl=3 hz=0.023255813953488372, 16:ds=49 fs=5 fl=3 hz=0.009523809523809525, 30:ds=48 fs=35 fl=1 hz=0.03829787234042553, 24:ds=45 fs=37 fl=0 hz=0.04048140043763676, 27:ds=37 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=90 flags=blue+purple
- S1: ds=75 flags=blue+purple
- S24: ds=58 flags=blue+purple
- S3: ds=46 flags=purple
- S20: ds=40 flags=purple
- S6: ds=29 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:774(B); midday:763(B)
- 066 -> combined:998(B); midday:741(B)
- 199 -> evening:759(B); midday:866(B)
- 255 -> evening:890(B); midday:936(B)
- 344 -> combined:693(B); evening:768(B)
- 444 -> combined:799(B); evening:974(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:47(blue); evening:64(red)
- 11 -> combined:29(purple); evening:29(purple)
- 19 -> combined:31(purple); evening:36(purple)
- 33 -> combined:141(red); evening:71(blue); midday:70(purple)
- 35 -> combined:40(blue); midday:41(blue)
- 44 -> combined:73(blue); evening:42(purple); midday:36(purple)
- 55 -> combined:44(purple); midday:187(red)
- 66 -> combined:67(purple); evening:38(purple); midday:33(purple)
- 69 -> combined:38(blue); midday:31(purple)
- 77 -> combined:80(blue); evening:40(purple); midday:77(blue)
- 88 -> combined:79(blue); evening:129(red); midday:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.708600000000001)[R1,XVAR-Cons(CEM)], 9(2.798035714285714)[R2,XVAR-Cons(CM)], 8(1.4957142857142856)[R1,Double-Pressure], 4(1.2723071428571429)[R2,Mirror-Echo], 0(0.23971428571428574)[R3,Swap]
- P2: 5(6.364307142857142)[R2,XVAR-Cons(CEM)], 4(4.211357142857143)[R1,XVAR-Cons(CM)], 1(3.227142857142857)[R3,XVAR-Cons(CE)], 3(1.1179999999999999)[R2,Double-Pressure], 9(0.4786428571428571)[R3,Mirror-Echo]
- P3: 5(3.8)[R2,XVAR-Cons(CM)], 9(2.5825857142857145)[R3,XVAR-Cons(CE)], 7(2.555207142857143)[R1,XVAR-Cons(CE)], 6(1.2671428571428571)[R1,Double-Pressure], 3(1.2208714285714284)[R2,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-02.xlsm aux_state_label=Pennsylvania; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:7(gap=28), P2:4(gap=30), P3:7(gap=17); top cartesian candidates: 757, 755, 759, 747, 745.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 014, 015, 019, 024, 025.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 039→combined:774(B),midday:763(B); 066→combined:998(B),midday:741(B); 199→midday:866(B),evening:759(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:283, 26:240, 16:98, 7:66, 6:61.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=744 Evening=909; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 447 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 099 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 744 (canon 447): box `447` covers winner `744` (boxed hit).
  - Evening winner 909 (canon 099): box `099` covers winner `909` (boxed hit).
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
