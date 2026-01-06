# Master Validation Run Report — SouthCarolina4 — results 2026-01-04 (history workbook ~ 2026-01-03)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-04/SouthCarolina4/`
- Winners lens: `sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2026-01-04/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-04/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2026-01-04/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2026-01-04/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2026-01-04/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-04/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac30_winner_432_20260105_055154.html`

Winners JSON files:
- `sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac30_winner_432_20260105_055154.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4/digest.md`.
- Q2: Stable environment quick read: Evening 432 (canon 234): exact_boxed=None exact_straight=None | rank 3048/4616 (rank_frac 0.660)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 432 idx30 (rank 17/35, frac 0.486)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **weak/noisy (no exact Stable hit; rely on cross-tool/Aux)**.
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

### 2.Stable — SouthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2026-01-04)

## Evening winner 432 (canonical 234)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=417 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): rank 3048/4616 (rank_frac 0.6603119584055459) | score 11.0 (top 43.5, ratio 0.25287356321839083, delta 32.5) | section Combined, Set Set1, Draw Draw6, Col 1, hot 1, vt_straight 0.0 | why boxed|cov2|hp_repeat2|hot1|perm2|draw_chain2
- Compound (patterns_compound.csv): rank 492/1641 (rank_frac 0.29981718464351004) | score 16.0 (top 73.0, ratio 0.2191780821917808, delta 57.0) | section Combined, col1_hits 2, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2|col1x2|hot1x1|vstrx2
- Families (patterns_families.csv): count 69 | rank 227/1401 (rank_frac 0.16202712348322626) | score 20.5 (top 32.0, ratio 0.640625, delta 11.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=None | exact_straight=None | vt_boxed_count=0

## Top compound candidates (patterns_compound.csv)
- rank   16 | canon 079 | section Midday | score 41.5 | col1_hits 1 | hot2 5
- rank    3 | canon 677 | section Combined | score 63.0 | col1_hits 4 | hot2 4
- rank    2 | canon 002 | section Combined | score 68.5 | col1_hits 2 | hot2 4
- rank   54 | canon 256 | section Combined | score 33.0 | col1_hits 2 | hot2 4
- rank   11 | canon 178 | section Midday | score 46.0 | col1_hits 4 | hot2 4
- rank   30 | canon 089 | section Midday | score 38.0 | col1_hits 0 | hot2 4
- rank   45 | canon 189 | section Midday | score 34.5 | col1_hits 4 | hot2 4
- rank   37 | canon 078 | section Midday | score 36.5 | col1_hits 0 | hot2 4
- rank   29 | canon 378 | section Midday | score 38.5 | col1_hits 0 | hot2 4
- rank   39 | canon 039 | section Midday | score 36.0 | col1_hits 0 | hot2 4

## Top families (patterns_families.csv)
- rank 1398 | family 11 | score 4.0 | hot2 0 | section Midday
- rank  376 | family 21 | score 18.5 | hot2 0 | section Midday
- rank 1166 | family 25 | score 10.0 | hot2 0 | section Midday
- rank 1291 | family 27 | score 8.5 | hot2 0 | section Midday
- rank 1306 | family 14 | score 8.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Evening 432 (canon 234): exact_boxed=None exact_straight=None | rank 3048/4616 (rank_frac 0.660)
- Q2: 4 hit criteria: see metrics_hits per winner (exact_boxed/exact_straight + vt_boxed_count).
- Q3: Winners artifacts alignment: spotlight + metrics.json consistent (see summary block).
- Q4: Dominance/noise: does not isolate winners (no exact boxed); use rank_frac + score_ratio_to_top to gauge strength.
- Q5: Top candidate clusters (compound canonicals): .
- Q6: Miss analysis: if a winner is absent/low, treat as tool outcome (not pipeline failure) unless gaps are listed.
- Q7: Validation (V): gaps list should be empty; if non-empty, flag as Fix-Now.
- Q8: Optimization notes: do not tune on 1 day; accumulate across days then adjust weights (Fix-Later).
- Q9: Cross-tool synergy: compare top compound canonicals vs DR top candidates + Hot Zones top lanes + Aux positional shortlist.
- Q10: Takeaway: Stable does not isolate winners (no exact boxed).

---

### 2.Digit Reduction — SouthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20260105)

## Midday: no winner in results file
- Skipped: state missing or blank for this period

## Evening winner 432 (canonical 234)
- Stamp (winner_stamp.json): items_total=146 | exact_any=12 exact_final=0 | vtrac_any=121 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=127 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=89 family_vtrac_final=0
- Flags (winner_flags.csv): rows=146 | exact_any=12 vtrac_any=121 | drop_exact_any=2 drop_vtrac_any=127 | family_exact_any=0 family_vtrac_any=89 | vt_boxed=139 vt_straight=0
- Hits (winner_hits.csv): rows=146 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=139 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.027143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 432 (canonical 234)
- Stamp (winner_stamp.json): items_total=417 | exact_any=123 exact_final=0 | vtrac_any=293 vtrac_final=0 | drop_exact_any=73 drop_exact_final=0 | drop_vtrac_any=344 drop_vtrac_final=0 | family_exact_any=4 family_exact_final=0 | family_vtrac_any=161 family_vtrac_final=0
- Flags (winner_flags.csv): rows=417 | exact_any=123 vtrac_any=293 | drop_exact_any=73 drop_vtrac_any=344 | family_exact_any=4 family_vtrac_any=161 | vt_boxed=368 vt_straight=0
- Hits (winner_hits.csv): rows=417 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=368 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.527143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 9.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 922 | score_v2 9.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 922 | score_v2 9.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw6 col 2 | pattern 592 | score_v2 9.527143 | match_types 
- area_rank 2 | variant Midday | section Midday | set Set1 draw Draw6 col 1 | pattern 522 | score_v2 9.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 922 | score_v2 9.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 922 | score_v2 9.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 922 | score_v2 9.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 922 | score_v2 9.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 922 | score_v2 9.227143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 224 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 592 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 922 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 522 | score_v2 9.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 592 | score_v2 9.187143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 224 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 552 | score_v2 9.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 552 | score_v2 9.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 592 | score_v2 8.987143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 552 | score_v2 8.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday: skipped (state missing or blank for this period); Evening 432 (canon 234): items_total=146 exact_any=12 vtrac_any=121 | top winner_present=False best_rank=None/20; Combined 432 (canon 234): items_total=417 exact_any=123 vtrac_any=293 | top winner_present=False best_rank=None/20
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 592, 922, 522, 592.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20260105_055543)

## Top indices (from enhanced JSON)
- index 29 | score 49.641687499999996 | features: presence=27.5741875, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 10 | score 22.864325000000004 | features: presence=15.268699999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 11 | score 22.070858333333337 | features: presence=9.281900000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 27 | score 21.226330000000004 | features: presence=10.018830000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 23 | score 18.85565 | features: presence=12.16815, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 13 | score 16.14225 | features: presence=7.504750000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 32 | score 12.250368333333336 | features: presence=7.911410000000002, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 21 | score 11.80375 | features: presence=6.06625, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 8 | score 9.199158333333333 | features: presence=2.8802000000000003, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 33 | score 4.745475 | features: presence=0.971725, cross_section=0.5, set_echo=0.3, first_hit=0.08000000000000002

## Top straights (from enhanced JSON)
783, 837, 832, 238, 873, 387, 283, 386, 683, 527

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 432 | index 30 | file SouthCarolina4_vtrac30_winner_432_20260105_055154.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 432 | index 30 rank 17/35 (rank_frac 0.4857142857142857) | score 2.35625 (top 49.641687499999996, ratio 0.047465147110480485, delta 47.28543749999999) | winner_in_index_straights=False | top_index_straights: 243 (0.529), 347 (0.499), 847 (0.466)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 432→idx30 rank 17/35 (frac 0.486).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 29, 10, 11, 27, 23.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — SouthCarolina4 — 2026-01-04

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2026-01-04)

## Evening winner 432 (canonical 234)
- Top lanes (hot_zones_top_lanes.csv): present | rank 147/210 (rank_frac 0.7) | score_mean 15.815 (top 21.17, ratio 0.7470477090222012, delta 5.355000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 257 | vt_triad 133 | score_mean 21.17 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 015 | vt_triad 112 | score_mean 20.865 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 027 | vt_triad 133 | score_mean 20.306 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 038 | vt_triad 144 | score_mean 20.244 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 068 | vt_triad 124 | score_mean 19.782 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 059 | vt_triad 115 | score_mean 19.719 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    7 | triad 003 | vt_triad 14 | score_mean 19.643 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 189 | vt_triad 245 | score_mean 19.572 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 388 | vt_triad 44 | score_mean 19.48 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 044 | vt_triad 15 | score_mean 19.458 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Evening 432 (canon 234): rank 147/210 (rank_frac 0.700) ratio_to_top=0.7470477090222012
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

Aux draws snapshot dir: `sharepacks/2026-01-04/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=051, 189, 084, 308, 821
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=189, 308, 910, 653, 754
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=051, 084, 821, 044, 976

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=19 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=19), P2:3 (gap=35), P3:2 (gap=14)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=974 sev=B
- 449: ds=903 sev=B
- 156: ds=886 sev=B
- 778: ds=856 sev=B
- 279: ds=855 sev=B
- 033: ds=787 sev=B
- 004: ds=775 sev=B
- 688: ds=742 sev=B
- 278: ds=709 sev=B
- 377: ds=689 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=183 sev=red
  - 55: ds=120 sev=red
  - 77: ds=104 sev=blue
  - 33: ds=91 sev=blue
  - 88: ds=86 sev=blue
  - 22: ds=66 sev=purple
  - 66: ds=54 sev=purple
  - 00: ds=27 sev=purple
  - 11: ds=23 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 78: ds=55 sev=blue
  - 68: ds=43 sev=blue
  - 29: ds=36 sev=purple
  - 06: ds=29 sev=purple
  - 16: ds=29 sev=purple
  - 59: ds=25 sev=purple
  - 17: ds=23 sev=-
  - 13: ds=21 sev=-
  - 39: ds=21 sev=-
  - 58: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:447, 35:390, 1:171, 26:159, 31:121, 4:112, 23:110, 28:104, 27:87, 19:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=447 fs=0 fl=0 hz=0.002197802197802198, 35:ds=390 fs=0 fl=0 hz=0.001949317738791423, 1:ds=171 fs=6 fl=4 hz=0.012195121951219513, 26:ds=159 fs=2 fl=0 hz=0.0062402496099844, 31:ds=121 fs=27 fl=0 hz=0.03085714285714286, 4:ds=112 fs=21 fl=2 hz=0.026589595375722544, 23:ds=110 fs=25 fl=1 hz=0.029850746268656716, 28:ds=104 fs=16 fl=2 hz=0.021479713603818614, 27:ds=87 fs=26 fl=0 hz=0.02911534154535274, 19:ds=71 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=96 flags=red+purple
- S0: ds=69 flags=blue+purple
- S23: ds=58 flags=purple
- S5: ds=57 flags=purple
- S24: ds=55 flags=blue+purple
- S4: ds=47 flags=purple
- S3: ds=46 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=5 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=15), P2:3 (gap=41), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

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
- current_index=2 streak=1 max=3 last_repeat_gap=32 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=18), P2:3 (gap=19), P3:8 (gap=21)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=982 sev=B
- 117: ds=893 sev=B
- 005: ds=879 sev=B
- 577: ds=856 sev=B
- 155: ds=836 sev=B
- 777: ds=835 sev=B
- 669: ds=827 sev=B
- 179: ds=809 sev=B
- 366: ds=775 sev=B
- 222: ds=769 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=99 sev=blue
  - 77: ds=86 sev=blue
  - 66: ds=78 sev=blue
  - 33: ds=74 sev=blue
  - 55: ds=65 sev=purple
  - 88: ds=59 sev=purple
  - 22: ds=36 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=15 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 58: ds=100 sev=red
  - 35: ds=67 sev=red
  - 29: ds=62 sev=red
  - 47: ds=52 sev=blue
  - 19: ds=34 sev=purple
  - 78: ds=30 sev=purple
  - 68: ds=27 sev=purple
  - 38: ds=21 sev=-
  - 13: ds=19 sev=-
  - 17: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:487, 1:274, 32:241, 31:220, 4:140, 28:113, 19:109, 23:104, 26:86, 16:82

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=487 fs=3 fl=1 hz=0.017391304347826087, 1:ds=274 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=241 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=220 fs=16 fl=1 hz=0.021935483870967745, 4:ds=140 fs=21 fl=3 hz=0.028742514970059883, 28:ds=113 fs=10 fl=4 hz=0.017676767676767676, 19:ds=109 fs=12 fl=2 hz=0.016968325791855206, 23:ds=104 fs=24 fl=0 hz=0.02937576499388005, 26:ds=86 fs=0 fl=0 hz=0.002347417840375587, 16:ds=82 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=65 flags=purple
- S15: ds=56 flags=red+purple
- S9: ds=53 flags=purple
- S17: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 378: score=4 tags=FLT,MIR,RS
  - 027: score=3 tags=MIR,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=MIR,RS
  - 126: score=3 tags=MIR,RS
  - 135: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=MIR,RS
  - 369: score=3 tags=FLT,RS
  - 459: score=3 tags=MIR,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:769(B); midday:851(B)
- 366 -> combined:974(B); evening:775(B)
- 449 -> combined:903(B); midday:670(B)
- 688 -> combined:742(B); evening:734(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 22 -> combined:66(purple); evening:36(purple); midday:37(purple)
- 29 -> combined:36(purple); evening:62(red)
- 33 -> combined:91(blue); evening:74(blue); midday:41(purple)
- 55 -> combined:120(red); evening:65(purple); midday:78(blue)
- 66 -> combined:54(purple); evening:78(blue)
- 68 -> combined:43(blue); evening:27(purple)
- 77 -> combined:104(blue); evening:86(blue); midday:47(purple)
- 78 -> combined:55(blue); evening:30(purple); midday:27(purple)
- 88 -> combined:86(blue); evening:59(purple); midday:39(purple)
- 99 -> combined:183(red); evening:99(blue); midday:114(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(3.1486)[R2,XVAR-Cons(CM)], 6(1.3799285714285714)[R1,Mirror-Echo], 1(1.2277857142857143)[R2,Mirror-Echo], 5(1.197142857142857)[R1,Double-Pressure], 0(1.0478571428571428)[R1,Double-Pressure]
- P2: 3(8.622285714285715)[R1,XVAR-Cons(CEM)], 9(6.115521428571428)[R2,XVAR-Cons(CEM)], 7(1.2225)[R2,Double-Pressure], 1(0.24779285714285712)[R3,Swap], 6(0.2414285714285714)[R3,Swap]
- P3: 7(3.3159)[R2,Mirror-Echo], 2(2.771228571428572)[R1,Mirror-Echo], 5(2.3272714285714287)[R3,XVAR-Cons(CE)], 6(1.32225)[R1,Mirror-Echo], 8(1.297)[R1,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-03.xlsm aux_state_label=South Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:5(gap=19), P2:3(gap=35), P3:2(gap=14); top cartesian candidates: 232, 237, 292, 235, 297.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}; top candidates: 016, 027, 056, 057, 126.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 222→midday:851(B),evening:769(B); 366→combined:974(B),evening:775(B); 449→combined:903(B),midday:670(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 32:447, 35:390, 1:171, 26:159, 31:121.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=N/A Evening=432; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): N/A
- Candidate universe (Evening): BOX 234 (post-hoc); Stable exact_boxed=False
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
  - Midday: no winner in results file (expected on some days).
  - Evening winner 432 (canon 234): box `234` covers winner `432` (boxed hit).
- Key tags:
  - cross-variant convergence | VT lane density | doubles/mirror pressure | hot columns/col1 funnels | Aux positional pressure
- Drivers:
  - Overall: weak/noisy (no exact Stable hit; rely on cross-tool/Aux).
- Conflicts:
  - If tools disagree (Stable/DR/VTRAC/HotZones), treat as noisy day; log as negative-control (do not tune yet).
- Fix-now vs fix-later:
  - Fix-now: none (sharepack artifacts exist; audit PASS).
  - Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
- Next run:
  - Continue filling remaining states/days; then generate day synthesis + re-export corpus summary.
