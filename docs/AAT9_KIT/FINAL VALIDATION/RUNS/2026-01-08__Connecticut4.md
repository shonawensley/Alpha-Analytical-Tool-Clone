# Master Validation Run Report — Connecticut4 — results 2026-01-08 (history workbook ~ 2026-01-07)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-08/Connecticut4/`
- Winners lens: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-08/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-08/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-08/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-08/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-08/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-08/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac23_winner_331_20260110_034415.html`
- `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_106_20260110_034414.html`

Winners JSON files:
- `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac23_winner_331_20260110_034415.json`
- `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_106_20260110_034414.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-08/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 106 (canon 016): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 331 (canon 133): exact_boxed=True exact_straight=True | rank 5536/5990 (rank_frac 0.924)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 331 idx23 (rank 12/35, frac 0.343), 106 idx6 (rank 20/35, frac 0.571)
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

### 2.Stable — Connecticut4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-08)

## Midday winner 106 (canonical 016)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=22 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 18 | rank 649/1474 (rank_frac 0.44029850746268656) | score 17.0 (top 37.5, ratio 0.4533333333333333, delta 20.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=4
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 331 (canonical 133)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=102 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 5536/5990 (rank_frac 0.9242070116861436) | score 9.0 (top 39.5, ratio 0.22784810126582278, delta 30.5) | section Midday, Set Set1, Draw Draw6, Col 2, hot 0, vt_straight 2.0 | why straight|cov1|double_mirror|vtrac_straight
- Compound (patterns_compound.csv): rank 1247/1684 (rank_frac 0.7404988123515439) | score 10.5 (top 112.0, ratio 0.09375, delta 101.5) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1|vstrx1|dblmirrorx1
- Families (patterns_families.csv): count 37 | rank 270/1474 (rank_frac 0.18317503392130258) | score 24.0 (top 37.5, ratio 0.64, delta 13.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=22

## Top compound candidates (patterns_compound.csv)
- rank    5 | canon 229 | section Evening | score 94.0 | col1_hits 8 | hot2 11
- rank    8 | canon 228 | section Evening | score 86.5 | col1_hits 7 | hot2 11
- rank   10 | canon 225 | section Evening | score 85.0 | col1_hits 7 | hot2 11
- rank   19 | canon 2289 | section Evening | score 69.5 | col1_hits 6 | hot2 11
- rank   20 | canon 289 | section Evening | score 69.0 | col1_hits 6 | hot2 11
- rank   31 | canon 1448 | section Midday | score 57.5 | col1_hits 5 | hot2 11
- rank   14 | canon 144 | section Midday | score 77.0 | col1_hits 7 | hot2 11
- rank    8 | canon 448 | section Midday | score 86.5 | col1_hits 6 | hot2 11
- rank   13 | canon 2248 | section Combined | score 77.5 | col1_hits 8 | hot2 11
- rank    1 | canon 224 | section Combined | score 112.0 | col1_hits 9 | hot2 11

## Top families (patterns_families.csv)
- rank 1459 | family 34 | score 5.5 | hot2 0 | section Midday
- rank  723 | family 9 | score 16.0 | hot2 0 | section Midday
- rank  914 | family 8 | score 14.0 | hot2 0 | section Midday
- rank 1092 | family 6 | score 12.0 | hot2 0 | section Midday
- rank 1169 | family 17 | score 11.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 106 (canon 016): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 331 (canon 133): exact_boxed=True exact_straight=True | rank 5536/5990 (rank_frac 0.924)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260110)

## Midday winner 106 (canonical 016)
- Stamp (winner_stamp.json): items_total=84 | exact_any=0 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=84 | exact_any=0 vtrac_any=84 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=84 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.59381 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 331 (canonical 133)
- Stamp (winner_stamp.json): items_total=60 | exact_any=12 exact_final=0 | vtrac_any=60 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=60 | exact_any=12 vtrac_any=60 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=60 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.427143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 106 (canonical 016)
- Stamp (winner_stamp.json): items_total=120 | exact_any=0 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=120 | exact_any=0 vtrac_any=120 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=120 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=10 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.358571 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 5 | pattern 922 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 6 | pattern 922 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 2 | pattern 922 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 3 | pattern 922 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 4 | pattern 922 | score_v2 14.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 599 | score_v2 14.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 14.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 599 | score_v2 14.258571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 599 | score_v2 14.258571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 14.258571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 922 | score_v2 14.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 599 | score_v2 14.358571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 592 | score_v2 14.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 922 | score_v2 13.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 448 | score_v2 13.59381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 224 | score_v2 13.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 922 | score_v2 13.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 922 | score_v2 13.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 592 | score_v2 13.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 559 | score_v2 12.837143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 106 (canon 016): items_total=84 exact_any=0 vtrac_any=84 | top winner_present=False best_rank=None/20; Evening 331 (canon 133): items_total=60 exact_any=12 vtrac_any=60 | top winner_present=False best_rank=None/16; Combined 106 (canon 016): items_total=120 exact_any=0 vtrac_any=120 | top winner_present=False best_rank=None/10
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 922, 599, 592, 922, 448.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260110_034634)

## Top indices (from enhanced JSON)
- index 28 | score 145.18455000000006 | features: presence=109.94705000000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 97.48726499999997 | features: presence=66.94976499999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 30 | score 89.69183999999998 | features: presence=60.10433999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 44.1624 | features: presence=31.3649, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 42.487919999999995 | features: presence=24.050420000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 30.689649999999997 | features: presence=21.13215, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 29.849837500000003 | features: presence=17.932337500000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 12 | score 28.448600000000003 | features: presence=21.361100000000004, cross_section=0.5, first_hit=0.4, column_span=0.3375
- index 14 | score 24.4016 | features: presence=14.6741, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 17.760650000000002 | features: presence=11.523150000000003, set_echo=0.6, first_hit=0.2666666666666667, column_span=0.17083333333333334

## Top straights (from enhanced JSON)
982, 984, 298, 892, 248, 824, 932, 284, 684, 243

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 331 | index 23 | file Connecticut4_vtrac23_winner_331_20260110_034415.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 106 | index 6 | file Connecticut4_vtrac6_winner_106_20260110_034414.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 331 | index 23 rank 12/35 (rank_frac 0.34285714285714286) | score 11.084200000000001 (top 145.18455000000006, ratio 0.07634558911399317, delta 134.10035000000005) | winner_in_index_straights=False | top_index_straights: 386 (4.315), 836 (4.082), 683 (4.061)
- winner 106 | index 6 rank 20/35 (rank_frac 0.5714285714285714) | score 5.1617 (top 145.18455000000006, ratio 0.035552681053183675, delta 140.02285000000006) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 331→idx23 rank 12/35 (frac 0.343); 106→idx6 rank 20/35 (frac 0.571).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 34, 30, 31, 24.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-08

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-08)

## Midday winner 106 (canonical 016)
- Top lanes (hot_zones_top_lanes.csv): present | rank 133/210 (rank_frac 0.6333333333333333) | score_mean 16.925 (top 22.484, ratio 0.7527575164561465, delta 5.559000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 331 (canonical 133)
- Top lanes (hot_zones_top_lanes.csv): present | rank 198/210 (rank_frac 0.9428571428571428) | score_mean 13.95 (top 22.484, ratio 0.6204412026329834, delta 8.534000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 017 | vt_triad 123 | score_mean 22.484 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    2 | triad 066 | vt_triad 12 | score_mean 22.177 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 147 | vt_triad 235 | score_mean 21.2 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 237 | vt_triad 334 | score_mean 21.123 | tags funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 278 | vt_triad 334 | score_mean 21.123 | tags funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 036 | vt_triad 124 | score_mean 21.11 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 117 | vt_triad 23 | score_mean 21.085 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    8 | triad 113 | vt_triad 24 | score_mean 20.975 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    9 | triad 567 | vt_triad 123 | score_mean 20.865 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 668 | vt_triad 24 | score_mean 20.732 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 106 (canon 016): rank 133/210 (rank_frac 0.633) ratio_to_top=0.7527575164561465; Evening 331 (canon 133): rank 198/210 (rank_frac 0.943) ratio_to_top=0.6204412026329834
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

Aux draws snapshot dir: `sharepacks/2026-01-08/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-08

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-08/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-07.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=147, 603, 737, 576, 660
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=603, 576, 071, 569, 533
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-08/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=147, 737, 660, 311, 181

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=45 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=26), P2:9 (gap=17), P3:4 (gap=34)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 424: score=38.23747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 494: score=37.74998785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=36.452730714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 824: score=35.62255714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=35.13507142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 854: score=33.83781428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 484: score=32.566559285714284 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 474: score=31.776559285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 444: score=30.653059285714285 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=repeat_endcap
- 884: score=29.951642857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=897 sev=B
- 129: ds=879 sev=B
- 288: ds=867 sev=B
- 149: ds=849 sev=B
- 445: ds=781 sev=B
- 114: ds=751 sev=B
- 069: ds=715 sev=B
- 888: ds=713 sev=B
- 688: ds=709 sev=B
- 133: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=99 sev=blue
  - 99: ds=80 sev=blue
  - 00: ds=50 sev=purple
  - 88: ds=36 sev=purple
  - 55: ds=18 sev=-
  - 22: ds=13 sev=-
  - 33: ds=9 sev=-
  - 11: ds=6 sev=-
  - 66: ds=4 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 48: ds=86 sev=red
  - 78: ds=82 sev=red
  - 49: ds=80 sev=red
  - 25: ds=49 sev=blue
  - 58: ds=31 sev=purple
  - 68: ds=31 sev=purple
  - 15: ds=29 sev=purple
  - 89: ds=26 sev=purple
  - 34: ds=24 sev=-
  - 45: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:415, 32:182, 25:168, 29:141, 4:139, 15:127, 31:116, 34:111, 3:96, 35:80

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=415 fs=1 fl=2 hz=0.01098901098901099, 32:ds=182 fs=5 fl=2 hz=0.011267605633802818, 25:ds=168 fs=22 fl=2 hz=0.029055690072639227, 29:ds=141 fs=24 fl=1 hz=0.03071253071253071, 4:ds=139 fs=21 fl=2 hz=0.027677496991576414, 15:ds=127 fs=9 fl=4 hz=0.015531660692951015, 31:ds=116 fs=32 fl=0 hz=0.03665521191294387, 34:ds=111 fs=15 fl=2 hz=0.01951779563719862, 3:ds=96 fs=27 fl=0 hz=0.030337078651685393, 35:ds=80 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=90 flags=purple
- S24: ds=82 flags=blue+purple
- S22: ds=80 flags=purple
- S25: ds=72 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=2 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=32), P2:8 (gap=15), P3:4 (gap=36)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 424: score=38.23747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 494: score=37.74998785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=36.452730714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 824: score=35.62255714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=35.13507142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 854: score=33.83781428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 484: score=32.566559285714284 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 474: score=31.776559285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 444: score=30.653059285714285 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=repeat_endcap
- 884: score=29.951642857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=885 sev=B
- 478: ds=866 sev=B
- 459: ds=861 sev=B
- 159: ds=817 sev=B
- 099: ds=798 sev=B
- 127: ds=789 sev=B
- 559: ds=731 sev=B
- 004: ds=690 sev=B
- 155: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=97 sev=blue
  - 88: ds=57 sev=purple
  - 44: ds=49 sev=purple
  - 55: ds=34 sev=purple
  - 00: ds=30 sev=purple
  - 66: ds=17 sev=-
  - 77: ds=12 sev=-
  - 11: ds=9 sev=-
  - 22: ds=6 sev=-
  - 33: ds=4 sev=-
- non_repeating:
  - 78: ds=75 sev=red
  - 13: ds=62 sev=red
  - 49: ds=49 sev=blue
  - 19: ds=48 sev=blue
  - 48: ds=45 sev=blue
  - 37: ds=29 sev=purple
  - 08: ds=27 sev=purple
  - 25: ds=24 sev=-
  - 34: ds=22 sev=-
  - 47: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:207, 25:108, 31:97, 32:95, 18:92, 3:80, 29:70, 4:69, 15:63, 34:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=207 fs=3 fl=0 hz=0.008565310492505354, 25:ds=108 fs=21 fl=1 hz=0.025974025974025976, 31:ds=97 fs=20 fl=2 hz=0.024608501118568233, 32:ds=95 fs=3 fl=4 hz=0.009510869565217392, 18:ds=92 fs=23 fl=1 hz=0.026519337016574582, 3:ds=80 fs=22 fl=2 hz=0.02631578947368421, 29:ds=70 fs=18 fl=2 hz=0.023446658851113716, 4:ds=69 fs=26 fl=0 hz=0.02931228861330327, 15:ds=63 fs=23 fl=1 hz=0.02564102564102564, 34:ds=55 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=91 flags=blue+purple
- S24: ds=88 flags=purple
- S23: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=4 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=22), P2:9 (gap=21), P3:2 (gap=19)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 424: score=38.23747357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 494: score=37.74998785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=36.452730714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 824: score=35.62255714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=35.13507142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 854: score=33.83781428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 484: score=32.566559285714284 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 474: score=31.776559285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 444: score=30.653059285714285 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=repeat_endcap
- 884: score=29.951642857142858 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=912 sev=B
- 668: ds=909 sev=B
- 399: ds=908 sev=B
- 044: ds=904 sev=B
- 133: ds=901 sev=B
- 145: ds=873 sev=B
- 677: ds=780 sev=B
- 333: ds=775 sev=B
- 112: ds=727 sev=B
- 344: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=119 sev=red
  - 22: ds=76 sev=blue
  - 99: ds=40 sev=purple
  - 33: ds=26 sev=purple
  - 00: ds=25 sev=purple
  - 88: ds=18 sev=-
  - 55: ds=9 sev=-
  - 11: ds=3 sev=-
  - 66: ds=2 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 57: ds=55 sev=blue
  - 69: ds=53 sev=blue
  - 23: ds=50 sev=blue
  - 25: ds=48 sev=blue
  - 07: ds=47 sev=blue
  - 48: ds=43 sev=blue
  - 78: ds=41 sev=blue
  - 49: ds=40 sev=blue
  - 15: ds=33 sev=purple
  - 02: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:318, 26:146, 4:129, 34:98, 32:91, 25:84, 29:72, 15:71, 2:61, 31:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=318 fs=2 fl=1 hz=0.005961251862891207, 26:ds=146 fs=3 fl=1 hz=0.008680555555555556, 4:ds=129 fs=18 fl=1 hz=0.02243211334120425, 34:ds=98 fs=14 fl=3 hz=0.019144144144144143, 32:ds=91 fs=2 fl=0 hz=0.008450704225352114, 25:ds=84 fs=21 fl=0 hz=0.023836549375709424, 29:ds=72 fs=27 fl=0 hz=0.030100334448160536, 15:ds=71 fs=15 fl=1 hz=0.019698725376593278, 2:ds=61 fs=23 fl=2 hz=0.028344671201814057, 31:ds=58 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=98 flags=blue+purple
- S8: ds=75 flags=red+purple
- S20: ds=58 flags=purple
- S3: ds=45 flags=blue+purple
- S24: ds=41 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 049: score=3 tags=FLT,RS
  - 058: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 247: score=3 tags=FLT,RS
  - 256: score=3 tags=FLT,RS
  - 589: score=3 tags=FLT,RS
  - 679: score=3 tags=FLT,RS
  - 013: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:705(B); evening:901(B)
- 445 -> combined:781(B); evening:696(B)
- 459 -> combined:690(B); midday:861(B)
- 888 -> combined:713(B); evening:704(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:50(purple); evening:25(purple); midday:30(purple)
- 15 -> combined:29(purple); evening:33(purple)
- 25 -> combined:49(blue); evening:48(blue)
- 44 -> combined:99(blue); evening:119(red); midday:49(purple)
- 48 -> combined:86(red); evening:43(blue); midday:45(blue)
- 49 -> combined:80(red); evening:40(blue); midday:49(blue)
- 78 -> combined:82(red); evening:41(blue); midday:75(red)
- 88 -> combined:36(purple); midday:57(purple)
- 99 -> combined:80(blue); evening:40(purple); midday:97(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(3.091807142857143)[R1,XVAR-Cons(CE)], 4(2.6101)[R2,XVAR-Cons(CM)], 7(1.6554285714285715)[R1,Double-Pressure], 9(1.3568571428571428)[R1,Double-Pressure], 5(1.0135)[R2,Double-Pressure]
- P2: 9(3.8312857142857144)[R1,XVAR-Cons(CE)], 2(3.318771428571429)[R2,XVAR-Cons(CE)], 5(2.5340285714285713)[R3,XVAR-Cons(CM)], 8(1.1478571428571427)[R1,Double-Pressure], 7(0.3578571428571428)[R3,Mirror-Echo]
- P3: 4(7.711978571428571)[R1,XVAR-Cons(CEM)], 2(2.8794285714285714)[R3,XVAR-Cons(CE)], 5(2.5814857142857144)[R2,XVAR-Cons(CM)], 8(1.0761999999999998)[R2,Double-Pressure], 7(0.9508)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-07.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:8(gap=26), P2:9(gap=17), P3:4(gap=34); top cartesian candidates: 424, 494, 454, 824, 894.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '8', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 018, 019, 023, 024.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:705(B),evening:901(B); 445→combined:781(B),evening:696(B); 459→combined:690(B),midday:861(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:415, 32:182, 25:168, 29:141, 4:139.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=106 Evening=331; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 016 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 133 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 106 (canon 016): box `016` covers winner `106` (boxed hit).
  - Evening winner 331 (canon 133): box `133` covers winner `331` (boxed hit).
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
