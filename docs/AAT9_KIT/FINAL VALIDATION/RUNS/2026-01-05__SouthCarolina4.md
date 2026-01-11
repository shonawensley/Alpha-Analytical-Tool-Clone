# Master Validation Run Report — SouthCarolina4 — results 2026-01-05 (history workbook ~ 2026-01-04)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-05/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-05/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-05/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-05/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-05/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-05/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-05/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac17_winner_171_20260110_035743.html`
- `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac20_winner_712_20260110_035744.html`

Winners JSON files:
- `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac17_winner_171_20260110_035743.json`
- `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac20_winner_712_20260110_035744.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-05/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 171 (canon 117): exact_boxed=True exact_straight=False | rank 777/4581 (rank_frac 0.170); Evening 712 (canon 127): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 171 idx17 (rank 14/35, frac 0.400), 712 idx20 (rank 2/35, frac 0.057)
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

### 2.Stable — SouthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-05)

## Midday winner 171 (canonical 117)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=13 | family_rows=113 | exact_boxed=13 | exact_straight=0 | vt_boxed=13
- Scores (patterns_scores.csv): rank 777/4581 (rank_frac 0.1696136214800262) | score 15.5 (top 43.5, ratio 0.3563218390804598, delta 28.0) | section Evening, Set Set1, Draw Draw2, Col 6, hot 0, vt_straight 0.0 | why boxed|cov2|hp_repeat2|perm2|hidden3v|double_mirror|set_chain3|draw_chain3
- Compound (patterns_compound.csv): rank 142/1610 (rank_frac 0.08819875776397515) | score 25.5 (top 91.0, ratio 0.2802197802197802, delta 65.5) | section Evening, col1_hits 0, hot2 0, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|dblmirrorx9
- Families (patterns_families.csv): count 45 | rank 12/1401 (rank_frac 0.008565310492505354) | score 28.5 (top 32.5, ratio 0.8769230769230769, delta 4.0) | section Combined, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=False | vt_boxed_count=8

## Evening winner 712 (canonical 127)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=86 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 49 | rank 4/1401 (rank_frac 0.0028551034975017845) | score 31.0 (top 32.5, ratio 0.9538461538461539, delta 1.5) | section Combined, hot2 3
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=11
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 677 | section Combined | score 91.0 | col1_hits 7 | hot2 11
- rank    4 | canon 577 | section Combined | score 73.0 | col1_hits 5 | hot2 9
- rank    7 | canon 5677 | section Combined | score 60.5 | col1_hits 5 | hot2 9
- rank    3 | canon 667 | section Combined | score 78.0 | col1_hits 6 | hot2 8
- rank    5 | canon 6677 | section Combined | score 69.5 | col1_hits 6 | hot2 8
- rank    6 | canon 56677 | section Combined | score 64.0 | col1_hits 5 | hot2 8
- rank   11 | canon 579 | section Evening | score 50.5 | col1_hits 5 | hot2 6
- rank    9 | canon 266 | section Combined | score 55.0 | col1_hits 3 | hot2 5
- rank   22 | canon 566 | section Combined | score 42.5 | col1_hits 3 | hot2 5
- rank   10 | canon 366 | section Combined | score 51.5 | col1_hits 2 | hot2 4

## Top families (patterns_families.csv)
- rank 1361 | family 22 | score 6.5 | hot2 0 | section Midday
- rank 1288 | family 13 | score 8.0 | hot2 0 | section Midday
- rank 1155 | family 30 | score 10.0 | hot2 1 | section Midday
- rank  180 | family 21 | score 21.5 | hot2 0 | section Midday
- rank  487 | family 32 | score 17.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 171 (canon 117): exact_boxed=True exact_straight=False | rank 777/4581 (rank_frac 0.170); Evening 712 (canon 127): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — SouthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260110)

## Midday winner 171 (canonical 117)
- Stamp (winner_stamp.json): items_total=50 | exact_any=0 exact_final=0 | vtrac_any=50 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=7 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=50 | exact_any=0 vtrac_any=50 | drop_exact_any=0 drop_vtrac_any=7 | family_exact_any=0 family_vtrac_any=4 | vt_boxed=8 vt_straight=0
- Hits (winner_hits.csv): rows=50 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=8 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=32 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.977143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 712 (canonical 127)
- Stamp (winner_stamp.json): items_total=75 | exact_any=2 exact_final=0 | vtrac_any=74 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=14 drop_vtrac_final=0 | family_exact_any=1 family_exact_final=0 | family_vtrac_any=4 family_vtrac_final=0
- Flags (winner_flags.csv): rows=75 | exact_any=2 vtrac_any=74 | drop_exact_any=2 drop_vtrac_any=14 | family_exact_any=1 family_vtrac_any=4 | vt_boxed=18 vt_straight=0
- Hits (winner_hits.csv): rows=75 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=18 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.347143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 171 (canonical 117)
- Stamp (winner_stamp.json): items_total=334 | exact_any=0 exact_final=0 | vtrac_any=332 vtrac_final=32 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=87 drop_vtrac_final=32 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=49 family_vtrac_final=32
- Flags (winner_flags.csv): rows=334 | exact_any=0 vtrac_any=332 | drop_exact_any=0 drop_vtrac_any=87 | family_exact_any=0 family_vtrac_any=49 | vt_boxed=95 vt_straight=32
- Hits (winner_hits.csv): rows=334 | exact_final=0 vtrac_final=32 | drop_exact_final=0 drop_vtrac_final=32 | family_exact_final=0 family_vtrac_final=32 | vt_boxed=95 vt_straight=32
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.058571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 4 | pattern 501 | score_v2 10.347143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set3 draw Draw1 col 4 | pattern 501 | score_v2 10.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 5 | pattern 501 | score_v2 10.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 592 | score_v2 10.058571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 592 | score_v2 10.058571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 592 | score_v2 10.032597 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 592 | score_v2 10.032597 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 501 | score_v2 10.347143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 501 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 592 | score_v2 10.058571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 592 | score_v2 10.058571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 224 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 592 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 9.464921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 522 | score_v2 9.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 552 | score_v2 9.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 592 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 11 | variant Midday | best_pattern 552 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 12 | variant Evening | best_pattern 599 | score_v2 8.958571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 171 (canon 117): items_total=50 exact_any=0 vtrac_any=50 | top winner_present=False best_rank=None/32; Evening 712 (canon 127): items_total=75 exact_any=2 vtrac_any=74 | top winner_present=False best_rank=None/20; Combined 171 (canon 117): items_total=334 exact_any=0 vtrac_any=332 | top winner_present=False best_rank=None/22
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 501, 501, 592, 592, 224.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260110_035940)

## Top indices (from enhanced JSON)
- index 29 | score 44.822205000000004 | features: presence=24.224705, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 20 | score 44.10147499999999 | features: presence=33.003975, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 11 | score 26.961893333333336 | features: presence=11.092935, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 10 | score 23.710405 | features: presence=14.712904999999997, cross_section=0.5, set_echo=0.3, first_hit=0.33333333333333337
- index 7 | score 19.9257125 | features: presence=11.5782125, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 23 | score 19.54165 | features: presence=12.854149999999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 27 | score 16.431073333333337 | features: presence=7.622115000000003, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 13 | score 14.951510000000003 | features: presence=6.074010000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 21 | score 13.35375 | features: presence=7.366250000000001, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 32 | score 10.838773333333336 | features: presence=6.499815000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
783, 837, 267, 238, 832, 873, 387, 762, 386, 683

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 171 | index 17 | file SouthCarolina4_vtrac17_winner_171_20260110_035743.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 712 | index 20 | file SouthCarolina4_vtrac20_winner_712_20260110_035744.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 171 | index 17 rank 14/35 (rank_frac 0.4) | score 2.7487500000000002 (top 44.822205000000004, ratio 0.061325630901023276, delta 42.073455) | winner_in_index_straights=False | top_index_straights: (none)
- winner 712 | index 20 rank 2/35 (rank_frac 0.05714285714285714) | score 44.10147499999999 (top 44.822205000000004, ratio 0.9839202466723801, delta 0.7207300000000103) | winner_in_index_straights=False | top_index_straights: 267 (11.997), 762 (9.719)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 171→idx17 rank 14/35 (frac 0.400); 712→idx20 rank 2/35 (frac 0.057).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 29, 20, 11, 10, 7.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-05

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-05)

## Midday winner 171 (canonical 117)
- Top lanes (hot_zones_top_lanes.csv): present | rank 127/210 (rank_frac 0.6047619047619047) | score_mean 16.549 (top 21.323, ratio 0.776110303428223, delta 4.774000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 712 (canonical 127)
- Top lanes (hot_zones_top_lanes.csv): present | rank 49/210 (rank_frac 0.23333333333333334) | score_mean 18.185 (top 21.323, ratio 0.8528349669371101, delta 3.1380000000000017)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 015 | vt_triad 112 | score_mean 21.323 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 257 | vt_triad 133 | score_mean 20.56 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 227 | vt_triad 33 | score_mean 20.514 | tags col1,funnel_precol1,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 038 | vt_triad 144 | score_mean 20.171 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 003 | vt_triad 14 | score_mean 19.975 | tags col1,funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 277 | vt_triad 33 | score_mean 19.871 | tags col1,funnel_precol1,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 027 | vt_triad 133 | score_mean 19.829 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 189 | vt_triad 245 | score_mean 19.479 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 388 | vt_triad 44 | score_mean 19.302 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 068 | vt_triad 124 | score_mean 19.258 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 171 (canon 117): rank 127/210 (rank_frac 0.605) ratio_to_top=0.776110303428223; Evening 712 (canon 127): rank 49/210 (rank_frac 0.233) ratio_to_top=0.8528349669371101
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

Aux draws snapshot dir: `sharepacks/2026-01-05/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-05

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-05/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-04.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-05/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=432, 051, 189, 084, 308
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-05/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=189, 308, 910, 653, 754
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-05/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=432, 051, 084, 821, 044

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=20 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=20), P2:9 (gap=22), P3:7 (gap=14)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 295: score=35.34665714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.98462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.53499285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 797: score=33.80146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 795: score=33.0113 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 796: score=32.649271428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 696: score=31.870675000000002 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 595: score=31.184383571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 298: score=29.991950000000003 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 275: score=29.236235714285712 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=975 sev=B
- 449: ds=904 sev=B
- 156: ds=887 sev=B
- 778: ds=857 sev=B
- 279: ds=856 sev=B
- 033: ds=788 sev=B
- 004: ds=776 sev=B
- 688: ds=743 sev=B
- 278: ds=710 sev=B
- 377: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=184 sev=red
  - 55: ds=121 sev=red
  - 77: ds=105 sev=blue
  - 33: ds=92 sev=blue
  - 88: ds=87 sev=blue
  - 22: ds=67 sev=purple
  - 66: ds=55 sev=purple
  - 00: ds=28 sev=purple
  - 11: ds=24 sev=-
  - 44: ds=7 sev=-
- non_repeating:
  - 78: ds=56 sev=red
  - 68: ds=44 sev=blue
  - 29: ds=37 sev=blue
  - 06: ds=30 sev=purple
  - 16: ds=30 sev=purple
  - 59: ds=26 sev=purple
  - 17: ds=24 sev=-
  - 13: ds=22 sev=-
  - 39: ds=22 sev=-
  - 58: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:448, 35:391, 1:172, 26:160, 31:122, 4:113, 23:111, 28:105, 27:88, 19:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=448 fs=0 fl=0 hz=0.002197802197802198, 35:ds=391 fs=0 fl=0 hz=0.001949317738791423, 1:ds=172 fs=6 fl=4 hz=0.012195121951219513, 26:ds=160 fs=2 fl=0 hz=0.0062402496099844, 31:ds=122 fs=27 fl=0 hz=0.03085714285714286, 4:ds=113 fs=21 fl=2 hz=0.026589595375722544, 23:ds=111 fs=25 fl=1 hz=0.029850746268656716, 28:ds=105 fs=16 fl=2 hz=0.021479713603818614, 27:ds=88 fs=26 fl=0 hz=0.02911534154535274, 19:ds=72 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=97 flags=red+purple
- S0: ds=70 flags=blue+purple
- S23: ds=59 flags=purple
- S5: ds=58 flags=purple
- S24: ds=56 flags=blue+purple
- S4: ds=48 flags=purple
- S3: ds=47 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=5 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=15), P2:3 (gap=41), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 295: score=35.34665714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.98462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.53499285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 797: score=33.80146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 795: score=33.0113 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 796: score=32.649271428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 696: score=31.870675000000002 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 595: score=31.184383571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 298: score=29.991950000000003 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 275: score=29.236235714285712 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=879 sev=B
- 555: ds=874 sev=B
- 222: ds=851 sev=B
- 337: ds=828 sev=B
- 003: ds=819 sev=B
- 228: ds=810 sev=B
- 556: ds=712 sev=B
- 449: ds=670 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=114 sev=red
  - 55: ds=78 sev=blue
  - 77: ds=47 sev=purple
  - 33: ds=41 sev=purple
  - 88: ds=39 sev=purple
  - 22: ds=37 sev=purple
  - 66: ds=24 sev=-
  - 00: ds=15 sev=-
  - 11: ds=10 sev=-
  - 44: ds=7 sev=-
- non_repeating:
  - 49: ds=55 sev=blue
  - 67: ds=49 sev=blue
  - 34: ds=48 sev=blue
  - 27: ds=42 sev=blue
  - 07: ds=33 sev=purple
  - 05: ds=30 sev=purple
  - 15: ds=28 sev=purple
  - 78: ds=27 sev=purple
  - 69: ds=26 sev=purple
  - 16: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:415, 26:193, 35:179, 27:144, 6:112, 5:81, 1:78, 15:73, 34:59, 31:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=415 fs=1 fl=2 hz=0.006993006993006993, 26:ds=193 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=179 fs=1 fl=1 hz=0.004968944099378882, 27:ds=144 fs=18 fl=3 hz=0.026582278481012658, 6:ds=112 fs=24 fl=2 hz=0.02957906712172924, 5:ds=81 fs=20 fl=1 hz=0.023102310231023104, 1:ds=78 fs=7 fl=3 hz=0.012127894156560088, 15:ds=73 fs=17 fl=3 hz=0.021691973969631236, 34:ds=59 fs=28 fl=1 hz=0.03159041394335512, 31:ds=55 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=82 flags=purple
- S25: ds=79 flags=purple
- S21: ds=59 flags=purple
- S20: ds=55 flags=purple
- S17: ds=53 flags=purple
- S8: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 026: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=PAT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 012: score=2 tags=FLT,PAT
  - 017: score=2 tags=RS
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 035: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=33 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=19), P2:9 (gap=15), P3:8 (gap=22)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 295: score=35.34665714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 296: score=34.98462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.53499285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 797: score=33.80146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 795: score=33.0113 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 796: score=32.649271428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 696: score=31.870675000000002 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 595: score=31.184383571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 298: score=29.991950000000003 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 275: score=29.236235714285712 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=983 sev=B
- 117: ds=894 sev=B
- 005: ds=880 sev=B
- 577: ds=857 sev=B
- 155: ds=837 sev=B
- 777: ds=836 sev=B
- 669: ds=828 sev=B
- 179: ds=810 sev=B
- 366: ds=776 sev=B
- 222: ds=770 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=100 sev=blue
  - 77: ds=87 sev=blue
  - 66: ds=79 sev=blue
  - 33: ds=75 sev=blue
  - 55: ds=66 sev=purple
  - 88: ds=60 sev=purple
  - 22: ds=37 sev=purple
  - 11: ds=26 sev=purple
  - 00: ds=16 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 58: ds=101 sev=red
  - 35: ds=68 sev=red
  - 29: ds=63 sev=red
  - 47: ds=53 sev=blue
  - 19: ds=35 sev=purple
  - 78: ds=31 sev=purple
  - 68: ds=28 sev=purple
  - 38: ds=22 sev=-
  - 13: ds=20 sev=-
  - 17: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:488, 1:275, 32:242, 31:221, 4:141, 28:114, 19:110, 23:105, 26:87, 16:83

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=488 fs=3 fl=1 hz=0.017391304347826087, 1:ds=275 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=242 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=221 fs=16 fl=1 hz=0.021935483870967745, 4:ds=141 fs=21 fl=3 hz=0.028742514970059883, 28:ds=114 fs=10 fl=4 hz=0.017676767676767676, 19:ds=110 fs=12 fl=2 hz=0.016968325791855206, 23:ds=105 fs=24 fl=0 hz=0.02937576499388005, 26:ds=87 fs=0 fl=0 hz=0.002347417840375587, 16:ds=83 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=66 flags=purple
- S15: ds=57 flags=red+purple
- S17: ds=53 flags=purple
- S23: ds=50 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 046: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:770(B); midday:851(B)
- 366 -> combined:975(B); evening:776(B)
- 449 -> combined:904(B); midday:670(B)
- 688 -> combined:743(B); evening:735(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 22 -> combined:67(purple); evening:37(purple); midday:37(purple)
- 29 -> combined:37(blue); evening:63(red)
- 33 -> combined:92(blue); evening:75(blue); midday:41(purple)
- 55 -> combined:121(red); evening:66(purple); midday:78(blue)
- 66 -> combined:55(purple); evening:79(blue)
- 68 -> combined:44(blue); evening:28(purple)
- 77 -> combined:105(blue); evening:87(blue); midday:47(purple)
- 78 -> combined:56(red); evening:31(purple); midday:27(purple)
- 88 -> combined:87(blue); evening:60(purple); midday:39(purple)
- 99 -> combined:184(red); evening:100(blue); midday:114(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(3.304885714285714)[R2,Mirror-Echo], 7(1.9695285714285715)[R3,Mirror-Echo], 6(1.4192857142857143)[R1,Mirror-Echo], 5(1.2985714285714285)[R1,Double-Pressure], 1(1.2622571428571427)[R2,Mirror-Echo]
- P2: 9(6.360207142857144)[R1,XVAR-Cons(CEM)], 7(2.7497857142857143)[R3,XVAR-Cons(CM)], 3(1.7149999999999999)[R1,Double-Pressure], 1(0.9508)[R2,Double-Pressure], 6(0.942)[R2,Double-Pressure]
- P3: 7(3.3699)[R1,XVAR-Cons(CM)], 5(3.181564285714286)[R2,XVAR-Cons(CE)], 6(2.8195357142857143)[R3,XVAR-Cons(CM)], 8(1.3268571428571427)[R1,Double-Pressure], 1(0.4787785714285714)[R3,Mirror-Echo]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-04.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=20), P2:9(gap=22), P3:7(gap=14); top cartesian candidates: 295, 296, 297, 797, 795.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 016, 017, 026, 027, 036.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:851(B),evening:770(B); 366→combined:975(B),evening:776(B); 449→combined:904(B),midday:670(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:448, 35:391, 1:172, 26:160, 31:122.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=171 Evening=712; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 117 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 127 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 171 (canon 117): box `117` covers winner `171` (boxed hit).
  - Evening winner 712 (canon 127): box `127` covers winner `712` (boxed hit).
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
